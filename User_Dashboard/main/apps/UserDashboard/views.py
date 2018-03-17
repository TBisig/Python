from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Message, Comment
import bcrypt

def index(request):
    if 'user_id' in request.session:
        return redirect('/dashboard')
    return render(request, 'index.html')

def signin(request):
    return render(request, 'signin.html')

def submit_signin(request):
    users = User.objects.filter(email=request.POST['email'])
    user_id = users.first().id
    request.session['user_id'] = user_id
    request.session['name'] = users.first().first_name
    request.session['user_level'] = users.first().user_level
    if users.count() == 0:
        messages.error(request, 'Unknown email', extra_tags='email')
        return redirect('/signin')
    if not bcrypt.checkpw(request.POST['password'].encode(), users.first().password.encode()):
        messages.error(request, 'Password invalid', extra_tags='password')
        return redirect('/signin')
    return redirect('/dashboard')

def signoff(request):
    del request.session['user_id']
    return redirect('/')

def register(request):
    return render(request, 'register.html')

def submit_register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/register')
    User.objects.create(first_name=request.POST['first_name'],
        last_name=request.POST['last_name'], 
        email=request.POST['email'],
        user_level='normal',
        description='empty',
        password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
    return redirect('/')

def dashboard(request):
    users = User.objects.all()
    context = { 'users': users }
    return render(request, 'dashboard.html', context)

def new_user(request):
    return render(request, 'new_user.html')

def submit_new_user(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/new')
    User.objects.create(first_name=request.POST['first_name'],
        last_name=request.POST['last_name'], 
        email=request.POST['email'],
        user_level='normal',
        description='empty',
        password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
    return redirect('/dashboard/admin')

def edit_user(request, id):
    context = { 'user': User.objects.get(id=id) }
    return render(request, 'edit_user.html', context)

def submit_edit_user(request):
    u = User.objects.get(id=request.POST['user_id'])
    u.first_name = request.POST['first_name']
    u.last_name = request.POST['last_name']
    u.email = request.POST['email']
    if 'user_level' in request.POST:
        u.user_level= request.POST['user_level']
    u.save()
    return redirect('/dashboard')

def delete_user(request, id):
    User.objects.get(id=id).delete()
    return redirect('/dashboard')

def submit_change_password(request):
    u = User.objects.get(id=request.POST['user_id'])
    u.password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    u.save()
    return redirect('/dashboard')

def edit_profile(request):
    context = { 'user': User.objects.get(id=request.session['user_id']) }
    return render(request, 'edit_profile.html', context)

def submit_edit_description(request):
    u = User.objects.get(id=request.session['user_id'])
    u.description = request.POST['description']
    u.save()
    return redirect('/dashboard')

def show_user(request, id):
    u = User.objects.get(id=id)
    m = Message.objects.filter(user=u)
    context = { 'user': u, 'messages': m}
    return render(request, 'show_user.html', context)

def submit_message(request):
    author = User.objects.get(id=request.POST['author_id'])
    user = User.objects.get(id=request.POST['user_id'])
    Message.objects.create(text=request.POST['text'], user=user, author=author)
    return redirect('/users/show/' + request.POST['user_id'])

def submit_comment(request):
    author = User.objects.get(id=request.POST['author_id'])
    message = Message.objects.get(id=request.POST['message_id'])
    Comment.objects.create(text=request.POST['text'], message=message, author=author)
    return redirect('/users/show/' + request.POST['user_id'])
