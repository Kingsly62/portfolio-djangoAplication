from cgitb import html
from multiprocessing import context
from pickle import NONE
from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def projects(request):
    return render(request, 'project.html')


def contact(request):
    return HttpResponse('This is my contact Home page(/)')


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def login(request):
    return render(request, 'login.html')


# if request.method == "POST":
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         username = request.POST['username']
#         email = request.POST['email']
#         pass1 = request.POST['pass1']
#         pass2 = request.POST['pass2']

#         if pass1 == pass2:
#             if User.objects.filter(username=username).exists():
#                 messages.error(request, 'Username already taken')
#                 if User.objects.filter(email=email).exists():
#                     messages.error(request, 'Email already used/taken')
#                 else:
#                     user = User.objects.create(
#                         username=username, first_name=fname, last_name=lname, email=email, password=pass1)
#                     user.save()

#                     if user is not None:
#                         login(request, user)

#                         user.register()

#                     return render(request, 'auth_lifecycle/login.html',
#                                   context_instance=RequestContext(request))
#                     # return HttpResponse(request, 'Register succesfully and logged in')

#     else:
#         return render(request, 'register.html', {"url 'register'"})
