from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
# the index function is called when root is visited
def index(request):
	return render(request, 'AppTwo/index.html')
	