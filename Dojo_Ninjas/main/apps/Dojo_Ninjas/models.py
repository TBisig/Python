from __future__ import unicode_literals
from django.db import models

# class Base(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)

    def __str__(self):
        return self.name

class Ninja(models.Model):
    dojo_id = models.ForeignKey(Dojo)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
