from cgitb import html
from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def projects(request):
    return HttpResponse('This is my projects Home page(/)')


def contact(request):
    return HttpResponse('This is my contact Home page(/)')


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')
