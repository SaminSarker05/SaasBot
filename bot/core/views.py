from django.shortcuts import render
from django.http import JsonResponse
from openai import OpenAI

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
