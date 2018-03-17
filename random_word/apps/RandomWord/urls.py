from django.conf.urls import url
from . import views
from django.utils.crypto import get_random_string
unique_id = get_random_string(length=14)
unique_id

urlpatterns = [
    url(r'^$', views.index),
    url(r'^random/', views.random),
    url(r'^random_word/reset$', views.reset),
]