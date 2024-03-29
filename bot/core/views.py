from django.shortcuts import render, redirect
from django.http import JsonResponse
from openai import OpenAI
from django.contrib import auth, messages
from django.contrib.auth.models import User
from .models import Chat
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from dotenv import load_dotenv
import os
load_dotenv()

OPENAI = os.getenv('OPENAI')
client = OpenAI(api_key = OPENAI)

def process(message):
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a very technical helpful coding assistant."},
      {"role": "user", "content": message},
    ]
  )
  answer = response.choices[0].message.content
  answer = f'<pre>{answer}</pre>'
  return answer


@login_required(login_url='login')
def home(request):
  chats = Chat.objects.filter(user=request.user)
  if request.method == 'POST':
    message = request.POST.get('message')
    response = process(message)

    chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
    chat.save()
    return JsonResponse({"message": message, "response": response})
  return render(request, 'home.html', {'chats': chats})


def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(request, username=username, password=password)
    if user is not None:
      auth.login(request, user)
      return redirect('home')
    else:
      return render(request, 'login.html', {'error_message': "no account"})
  return render(request, 'login.html')


def register(request):
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    passwordOne = request.POST['password1']
    passwordTwo = request.POST['password2']
    if passwordOne != passwordTwo:
      return render(request, 'register.html', {'error_message': "password not match"})
    else:
      try:
        newuser = User.objects.create_user(username, email, passwordOne)
        newuser.save()
        return redirect('login')
      except Exception as e:
        return render(request, 'register.html', {'error_message': str(e)})

  return render(request, 'register.html')


def logout(request):
  auth.logout(request)
  return redirect('login')