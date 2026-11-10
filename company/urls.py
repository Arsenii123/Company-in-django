from django.urls import path
from .views import *
from django.urls import path, include
urlpatterns = [
    path('', index, name='index'),
    path('news/', include('news.urls')),
    path('managment/',include('managment.urls')),
    path('about_company/',include('about_company.urls')),
    path('contacts/',include('contacts.urls'))
]
