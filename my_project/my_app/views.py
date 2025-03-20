# views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import Text

def homepage(request):
    description = Text.objects.all()
    return render(request, 'homepage.html', {'description': description})

def text(request, id):
    text = Text.objects.get(pk=id+1)
    return render(request, 'text.html', {'text': text})
