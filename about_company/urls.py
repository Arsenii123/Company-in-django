from django.urls import path
from news.views import *
from about_company.views import *

urlpatterns = [
    path('history/', history, name='history'),
    path('', about_company, name='about_company'),
]


