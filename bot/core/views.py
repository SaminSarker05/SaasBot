from django.shortcuts import render
from django.http import JsonResponse

def chatbot(request):
  if request.method == 'POST':
    message = request.POST.get('message')
    response = "HOLA"
    return JsonResponse({"message": message, "response": response})
  return render(request, 'home.html')
