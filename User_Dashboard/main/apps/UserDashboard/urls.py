from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^signin$', views.signin),
    url(r'^submit_signin$', views.submit_signin),
    url(r'^signoff$', views.signoff),
    url(r'^register$', views.register),
    url(r'^submit_register$', views.submit_register),
    url(r'^dashboard/admin$', views.dashboard),
    url(r'^dashboard$', views.dashboard),
    url(r'^users/new$', views.new_user),
    url(r'^submit_new_user$', views.submit_new_user),
    url(r'^users/edit/(?P<id>[0-9]+)$', views.edit_user),
    url(r'^users/edit$', views.edit_profile),
    url(r'^users/delete/(?P<id>[0-9]+)$', views.delete_user),
    url(r'^submit_edit_user$', views.submit_edit_user),
    url(r'^submit_change_password$', views.submit_change_password),
    url(r'^submit_edit_description$', views.submit_edit_description),
    url(r'^users/show/(?P<id>[0-9]+)$', views.show_user),
    url(r'^submit_message$', views.submit_message),
    url(r'^submit_comment$', views.submit_comment),
]