from django.shortcuts import render, HttpResponse, redirect
from models import Dojo, Ninja

def index(request):
    context = {
        "ninjas" : Ninja.objects.all()
    }
    return render(request, 'Dojo_Ninjas/index.html', context)

def ninjas(request):
    Ninja.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'])
    return redirect(request, '/')