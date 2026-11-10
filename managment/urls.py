from django.urls import path
from managment.views import *

urlpatterns = [
    path('director/', about_director, name='about_director'),
    path(' ', managment, name='managment'),
]


