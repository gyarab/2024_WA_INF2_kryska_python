# views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import Text, Map, Weapon


def homepage(request):
    description = Text.objects.all()
    return render(request, 'homepage.html', {'description': description})

def mapPage(request):
    mapPage = Map.objects.all()
    return render(request, 'mapPage.html', {'mapPage': mapPage})

def weaponPage(request):
    weaponPage = Weapon.objects.all()
    return render(request, 'weaponPage.html', {'weaponPage': weaponPage})

def text(request, id):
    text = Text.objects.get(pk=id)
    return render(request, 'text.html', {'text': text})

def map(request, id):
    map = Map.objects.get(pk=id)
    return render(request, 'map.html', {'map': map})

def weapon(request, id):
    weapon = Weapon.objects.get(pk=id)
    return render(request, 'weapon.html', {'weapon': weapon})

