from django.shortcuts import render
from django.shortcuts import HttpResponse
from .chatbot import Chatwithgroq
from django.http import JsonResponse

def chatView(request):
    if request.method == "POST":
        message = request.POST.get('message')
        response = Chatwithgroq(message)
        return JsonResponse({"response": response})

    return render(request, "app/chat.html")