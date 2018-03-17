from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^submit_signin$', views.submit_signin),
    url(r'^submit_register$', views.submit_registration),
    url(r'^books$', views.show_books),
    url(r'^books/add$', views.add_book),
    url(r'^books/(?P<id>[0-9]+)$', views.show_book),
    url(r'^users/(?P<id>[0-9]+)$', views.show_user),
    url(r'^logout$', views.submit_logout),
    url(r'^add_book_and_review$', views.add_book_and_review),
    url(r'^add_review$', views.add_review),
]