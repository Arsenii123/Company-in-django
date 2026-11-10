from django.shortcuts import render
def history(request):
    return render(request, 'history.html')

def current_affairs(request):
    return render(request, 'currentaffairs.html')

def news(request):
    return render(request, 'news.html')


