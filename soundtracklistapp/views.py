from django.shortcuts import render

def home(request):
    return render(request, 'soundtracklistapp/home.html')

def about(request):
    return render(request, 'soundtracklistapp/about.html')
