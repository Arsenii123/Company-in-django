from django.urls import path
from news.views import *

urlpatterns = [
    path('history/', history, name='history'),
    path('current-affairs/', current_affairs, name='current_affairs'),
    path(' ', news, name='news'),
]


