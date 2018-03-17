from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Count
from .models import Book, Review
from .forms import RegistrationForm, SignInForm, ReviewForm

def index(request):
    registration_form = RegistrationForm()
    signin_form = SignInForm()
    context = { 'registration_form': registration_form,
            'signin_form': signin_form}
    return render(request, 'index.html', context)

def submit_registration(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        if form.cleaned_data['password'] == form.cleaned_data['password_confirm']:
            user = User.objects.create_user(form.cleaned_data['email'], form.cleaned_data['email'], form.cleaned_data['password'])
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            return redirect('/')
        else:
            form.add_error('password_confirm', 'Passwords do not match')
            return render(request, 'index.html', { 'form': form })
    return redirect('/')

def submit_signin(request):
    form = SignInForm(request.POST)
    if form.is_valid():
        user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
        if user is not None:
            login(request, user)
            return redirect('/books')
        else:
            return redirect('/')
    return redirect('/')

def submit_logout(request):
    logout(request)
    return redirect('/')

def show_books(request):
    if request.user.is_authenticated():
        context = { 
                'user': request.user,
                'recent_reviews': Review.objects.all().order_by('-id')[:3],
                'all_books': Book.objects.annotate(num_reviews=Count('reviews')).filter(num_reviews__gt=0) }

        return render(request, 'books.html', context)
    return redirect('/')

def show_book(request, id):
    book = Book.objects.get(id=id)
    context = {
            'book': book,
            'reviews': Review.objects.filter(book=book),
            'review_form': ReviewForm()}
    return render(request, 'book.html', context )

def add_book(request):
    context = { 'authors': Book.objects.values('author').distinct() }
    return render(request, 'add_book.html', context)

def add_book_and_review(request):
    if request.POST['select_author'] != '':
        author = request.POST['select_author']
    else:
        author = request.POST['text_author']
    book = Book.objects.create(
            title= request.POST['title'],
            author=author)
    review = Review.objects.create(
            review=request.POST['review'],
            rating=request.POST['rating'],
            inverse_rating = 5 - int(request.POST['rating']),
            book=book,
            user=request.user)
    return redirect('/books/' + str(book.id))

def add_review(request):
    book = Book.objects.get(id=request.POST['book_id'])
    review = Review.objects.create(
            review=request.POST['review'],
            rating=request.POST['rating'],
            inverse_rating = 5 - int(request.POST['rating']),
            book=book,
            user=request.user)

    return redirect('/books/' + str(book.id))

def show_user(request, id):
    reviews = Review.objects.filter(user=request.user)
    context = {
            'user': request.user,
            'reviews_count': reviews.count(),
            'reviews': reviews }
    return render(request, 'user.html', context)