from django.shortcuts import render
from django.http import HttpResponse
import random
from string import ascii_lowercase, ascii_uppercase, punctuation, digits


def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):

    result = ''

    characters = ascii_lowercase

    if request.GET.get('uppercase'):
        result += random.choice(ascii_uppercase)
        characters += ascii_uppercase
    if request.GET.get('special'):
        result += random.choice(punctuation)
        characters += punctuation
    if request.GET.get('numbers'):
        result += random.choice(digits)
        characters += digits

    length = int(request.GET.get('length', 12))

    for x in range(length-len(result)):
        result += random.choice(characters)

    return render(request, 'generator/password.html', {'password': result})