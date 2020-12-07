from django.urls import re_path
from helloword import views

urlpatterns = [
    re_path(r'^hello-world/$', views.first_func)
]