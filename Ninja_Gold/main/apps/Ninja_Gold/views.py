from django.shortcuts import render, redirect
import time
import random

def index(request):
    if 'gold' in request.session:
        pass
    else:
        request.session['gold'] = 0

    if 'activities' in request.session:
        pass
    else:
        request.session['activities'] = []

    return render(request, 'index.html')

def process_money(request, loc):
    if loc == 'farm':
        earned = random.randint(10,20)
        activity = "Earned " + str(earned) + " gold from farm! " + time.strftime("%Y/%m%d %H:%M:%S")
    elif loc == 'cave':
        earned = random.randint(5,10)
        activity = "Earned " + str(earned) + " gold from cave! " + time.strftime("%Y/%m%d %H:%M:%S")
    if loc == 'house':
        earned = random.randint(2,5)
        activity = "Earned " + str(earned) + " gold from house! " + time.strftime("%Y/%m%d %H:%M:%S")
    if loc == 'casino':
        earned = random.randint(-50,50)
        if earned < 0:
            activity = "Entered a casino and lost" + str(earned) + ' . ' + time.strftime("%Y/%m%d %H:%M:%S")
        else:
            activity = "Entered a casino and won " + str(earned) + ' . ' + time.strftime("%Y/%m%d %H:%M:%S")

    request.session['gold'] += earned
    if earned < 0:
        color = 'red'
    else:
        color = 'green'

    activities = request.session['activities']
    activities.append( { 'color': color,
        'activity': activity })
    request.session['activities'] = activities

    return redirect('/')