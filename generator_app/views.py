# from django.http import HttpResponse
from django.shortcuts import render

import random

# Create your views here.
def home(request):
    return render(request, "home.html")

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''

    length = int(request.GET.get("length"))

    if request.GET.get("uppercase"):
        print("Entro")
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get("special"):
        characters.extend(list("-_+!@#$%^&*(){}[]"))
    if request.GET.get("numbers"):
        characters.extend(list("0123456789"))

    for i in range(length):
        generated_password += random.choice(characters)

    print(generated_password)
    return render(request, "password.html", {"password": generated_password})

def about(request):
    return render(request, "about.html")
    # return HttpResponse("Hola!") # Se puede hacer con HttpResponse, pero no es muy util, porque tendria que escribir todo el codigo html aca