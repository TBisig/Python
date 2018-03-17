from django.shortcuts import render, redirect, HttpResponse


# Create your views here.
def index(request):
    return render (request, 'index.html')
def formProcess(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1

    request.session['data'] = {
        "Name": request.POST['name'],
        "Dojo Location": request.POST['dojoLocation'],
        "Favorite Language": request.POST['favLang'],
        "Comments": request.POST['comments']
    }
    return redirect('/showResults')

def showResults(request):
    print "Go to show results!"
    print request.session
    return render(request, 'results.html')
