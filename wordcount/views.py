from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'name':'Jinil', 'app':'Django'})

def count(request):
    text = request.GET['text']
    words = text.split()
    return render(request, 'count.html', {'text':text, 'count': len(words)})

def about(request):
    return render(request, 'about.html')
