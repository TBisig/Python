from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
from django.contrib import messages
from models import *
import datetime
import re
DATE_REGEX = re.compile(r'^[0-12]+/[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
def start(request):
	return redirect('/index')
def index(request):
	# context = {
	# 	'users':User.objects.Regvalidator(request.POST)
	# }
	return render(request, 'User/index.html')
def Regprocess(request):
	errors = User.objects.Regvalidator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
	return redirect('/main')
def Logprocess(request):
	if request.method == 'POST':
		errors = User.objects.Logvalidator(request.POST)
		if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags=tag)
			return redirect('/main')
		U = User.objects.get(name=request.POST['Lname'])
		request.session['name'] = U.name
		request.session['id'] = U.id
		return redirect('/travels')
def travels(request):
	print 'mydate'
	context = {
		'notMine':Vacation.objects.exclude(users__name=request.session['name']),
		'Mine':Vacation.objects.filter(users__name=request.session['name'])
	}
	return render (request, 'User/travels.html', context)
def addtrip(request):
	return render (request, 'User/add.html')
def processtrip(request):
	errors = Vacation.objects.TripValidator(request.POST, request.session['id'])
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
			return redirect('/travels/add')
	return redirect('/travels')
def destination(request,id):
	vac = Vacation.objects.get(id=id)
	context = {
		'Vaca': vac,
		'Vaca2':User.objects.filter(vacation__id=id).exclude(id=vac.creator.id)
	}
	return render(request, 'User/destination.html', context)
def LogOut(request):
	request.session.flush()
	return redirect('/main')
def join(request, id):
	this_user = User.objects.get(id=request.session['id'])
	this_vaca = Vacation.objects.get(id=id)
	this_vaca.users.add(this_user)
	return redirect('/travels')











