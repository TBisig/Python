from __future__ import unicode_literals
from django.db import models
import re

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name must have at least two characters, letters only'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name must have at least two characters, letters only'
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(postData['email']):
            errors['email'] = 'Email must be valid'
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        if postData['password'] != postData['confirm']:
            errors['confirm'] = 'Password and confirmation must match'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    user_level = models.CharField(max_length=6)
    description = models.TextField(default='empty')
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()

class Message(models.Model):
    text = models.TextField(default='empty')
    user = models.ForeignKey(User, related_name='messages')
    author = models.ForeignKey(User, related_name='authored_messages')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
    text = models.TextField(default='empty')
    message = models.ForeignKey(Message, related_name='comments')
    author = models.ForeignKey(User, related_name='authored_comments')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)