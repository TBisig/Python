from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'amadon/index.html')

def buy(request):
    return redirect(request, 'amadon/buy.html')

# def thank_you(request):
#     return redirect(request, 'amadon/thankyou.html')