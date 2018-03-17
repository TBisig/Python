# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from random import randint

# Create your models here.
class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class House(Base):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Student(Base):
    name = models.CharField(max_length=254)
    cult = models.ForeignKey(House, related_name="peeps")


def build_houses():
    houses = ["Thunderbird", "Wampus", "Horned Serpent", "Pukwudgie"]
    for house in houses:
        neo = House(name=house)
        neo.save()

def build_students():
    names = [
        "Alan",
        "Bob",
        "Bernardo",
        "Robb",
        "Mags",
        "Donovan",
        "Rachel"
    ]
    houses = House.objects.all()
    for n in names:
        neo = Student(name=n)
        h = houses[random.randint(0,3)]
        neo.cult = h
        neo.save()