from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if "count" in request.session:
        request.session["count"] +=1
    else:
        request.session["count"] =1
    return render(request, 'index.html')

def random(request, method="POST"):
    request.session['word'] = get_random_string(length=14)
    request.session["count"] +=1 
    return render(request, 'index.html')

def reset(request):
    request.session["count"] = 0
    return render(request, 'index.html')`