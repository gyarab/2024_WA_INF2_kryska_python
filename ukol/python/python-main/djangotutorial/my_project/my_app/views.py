#my_app/views.py

import json
import os
from django.shortcuts import render # type: ignore
from django.http import HttpResponse  # type: ignore


def homepage(request):
    file_path = os.path.join(os.path.dirname(__file__), 'VALORANT.json')
    with open(file_path, encoding='utf-8') as f:
        description = json.load(f)
    
    return render(request, 'homepage.html', {'description' : description})

def text(request, id):
    file_path = os.path.join(os.path.dirname(__file__), 'VALORANT.json')
    with open(file_path, encoding='utf-8') as f:
        description = json.load(f)
    
    text = description[id]
    return render(request, 'text.html', {'text' : text})
