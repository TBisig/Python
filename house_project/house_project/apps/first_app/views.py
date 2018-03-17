# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import House, Student
from django.shortcuts import render, redirect
import random

# Create your views here.

def index(request):
    houses = House.objects.all()

    context = {
        'house_data': houses
    }
    return render(request, 'index.html', context)


def create(request):
    name = request.POST["name"]
    house_id = random.randint(1, 4)
    house = House.objects.get(id=house_id)
    Student.objects.create(name = name, house=house)
    return redirect("/")