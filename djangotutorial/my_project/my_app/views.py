#my_app/views.py

import json
import os
from django.shortcuts import render # type: ignore
from django.http import HttpResponse  # type: ignore


def homepage(request):
    file_path = os.path.join(os.path.dirname(__file__), 'articles.json')
    with open(file_path, encoding='utf-8') as f:
        articles = json.load(f)
    
    return render(request, 'homepage.html', {'articles' : articles})

def article(request, id):
    file_path = os.path.join(os.path.dirname(__file__), 'articles.json')
    with open(file_path, encoding='utf-8') as f:
        articles = json.load(f)
    
    article = articles[id]
    return render(request, 'article.html', {'article' : article})
