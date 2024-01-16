from django.shortcuts import render, redirect
from django.http import JsonResponse
from openai import OpenAI
from django.contrib import auth, messages
from django.contrib.auth.models import User

OPENAI = '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'
client = OpenAI(api_key = OPENAI)

def process(message):
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[

      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": message},
    ]
  )
  print(response)
  answer = response.choices[0].strip()
  return answer


def chatbot(request):
  if request.method == 'POST':
    message = request.POST.get('message')
    response = "TEST MESSAGE"
    # response = process(message)
    return JsonResponse({"message": message, "response": response})
  return render(request, 'home.html')


def login(request):
  return render(request, 'login.html', {'error_message': error_message})

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
      except:
        return render(request, 'register.html', {'error_message': "error in creation"})



  return render(request, 'register.html')

