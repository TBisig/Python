from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^2$', views.index)     # This line has changed!
]