from django.urls import re_path
from hello import views

urlpatterns = [
    re_path(r'^hello/$', views.first_editor),
]