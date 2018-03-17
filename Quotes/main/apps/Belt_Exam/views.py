from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# from datetime import datetime
import bcrypt

# Create your views here.
def current_user(request):
	return User.objects.get(id = request.session['user_id'])

def index(request):
	return render(request, 'index.html')
def register(request):
    errors = User.objects.Regvalidator(request.POST)
    if len(errors):
    	for tag, error in errors.iteritems():
    		messages.error(request, error, extra_tags=tag)
	return redirect('/main')
def login(request):
    if request.method == 'POST':
    	errors = User.objects.Logvalidator(request.POST)
    	if len(errors):
    		for tag, error in errors.iteritems():
    		    messages.error(request, error, extra_tags=tag)
    		return redirect('/main')
    	U = User.objects.get(email=request.POST['Lemail'])
    	request.session['username'] = U.username
    	request.session['id'] = U.id
        return redirect('/quotes')        
def logout(request):
    request.session.flush()
    return redirect('/main')

def quotes(request):
	user = current_user(request)

	context = {
		'user': user,
		'quotable_quotes': Quote.objects.exclude(favorites = user),
		'favorites': user.favorites.all()
	}

	return render(request, 'quotes.html', context)


def create(request):
	if request.method != 'POST':
		return redirect('/')
	##adds item to quotes
	check = Quote.objects.validateQuote(request.POST)
	if request.method != 'POST':
		return redirect('/quotes')
	if check[0] == False:
		for error in check[1]:
			messages.add_message(request, messages.INFO, error, extra_tags="add_item")
			return redirect('/quotes')
	if check[0] == True:

		quote = Quote.objects.create(
			content = request.POST.get('content'),
			poster = current_user(request),
			author = request.POST.get('author')
			)

		return redirect('/quotes')
	return redirect('/quotes')

def add_favorite(request, id):

	user = current_user(request)
	favorite = Quote.objects.get(id=id)

	user.favorites.add(favorite)

	return redirect('/quotes')

def remove_favorite(request, id):

	user = current_user(request)
	favorite = Quote.objects.get(id=id)

	user.favorites.remove(favorite)

	return redirect('/quotes')

def show_user(request, id):

	user =  User.objects.get(id = id)
	context = {
		'user': user,
		'favorites': user.favorites.all()		
	}
	return render(request, 'user.html', context)
