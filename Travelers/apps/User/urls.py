from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^$', views.start),
	url(r'^LogOut$', views.LogOut),
	url(r'^Join/(?P<id>\d+)$', views.join),
	url(r'^main$', views.index),     # This line has changed!
	url(r'^Regprocess$', views.Regprocess),
	url(r'^Logprocess$', views.Logprocess),
	url(r'^travels$', views.travels),
	url(r'^travels/add$', views.addtrip),
	url(r'^processtrip$', views.processtrip),
	url(r'^travels/destination/(?P<id>\d+)$', views.destination),
]