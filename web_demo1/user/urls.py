from django.urls import re_path
from user import views

urlpatterns = [
    re_path(r'^register/$', views.register),
]