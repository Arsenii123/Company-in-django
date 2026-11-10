from django.urls import path
from contacts.views import *

urlpatterns = [
    path(' ', contacts, name='contacts'),
]


