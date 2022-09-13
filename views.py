from django.shortcuts import render

# Create your views here.
import datetime
import random
from django.http import HttpRequest, HttpResponse

def today(request : HttpRequest):
    t = datetime.date.today()
    return render(request, 'today/index.html', {"today": t})

def randompass(request):

    characters = list('0987654321abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    randompass = ''
    for x in range(12):
        randompass += random.choice(characters)
    return render(request, 'randompass/index.html', {'pass':randompass})