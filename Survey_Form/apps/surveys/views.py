from django.shortcuts import render, HttpResponse, redirect
import random
from models import Student

def index(request):
    # response = 'hey'
    return render(request, 'index.html')
    # return HttpResponse(response)