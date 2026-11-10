from django.shortcuts import render

def managment(request):
    return render(request, 'managment.html')

def about_director(request):
    return render(request, 'about_director.html')

