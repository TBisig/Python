from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new/$', views.new),
    url(r'^create/$', views.index),
    url(r'^blog/(?P<blog_id>[0-9]+)/$', views.show),
    url(r'^blog/edit/(?P<blog_id>[0-9]+)/$', views.edit),
    url(r'^blog/destroy/(?P<blog_id>[0-9]+)/$', views.destroy),
]