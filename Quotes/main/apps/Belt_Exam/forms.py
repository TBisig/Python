from django.contrib.auth.models import User

from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField(min_length=3)
    alias = forms.CharField(min_length=3)
    email = forms.CharField(min_length=5)
    password = forms.CharField(min_length=8)
    confirm_password = forms.CharField(min_length=8)

class SignInForm(forms.Form):
    email = forms.CharField(min_length=3)
    password = forms.CharField(min_length=8)

