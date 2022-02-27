from cgitb import html
from multiprocessing import context
from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from . forms import RegisterForm
from django.conf import settings
from django.core.mail import send_mail
from .models import Photo
from .forms import ImageForm
from .models import Image


# Create your views here.


def home(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')

        send_mail(subject, message, settings.EMAIL_HOST_USER,
                  [email], fail_silently=False)
        return render(request, 'email.html', {'email': email})
    return render(request, 'home.html', {})


def email(request):
    return render(request, 'email.html')


def about(request):
    return render(request, 'about.html')


def projects(request):
    if request.method == 'POST':
        new_photo = Photo(
            file=request.FILES['img']
        )
        new_photo.save()
        return render(request, 'project.html', {'new_url': str('localhost:8000'+new_photo.file.url)})
    else:
        return render(request, 'project.html')


def contact(request):
    return HttpResponse('This is my contact Home page(/)')


def register(request):
    form = RegisterForm()
    if request.method == 'POST':

        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def LoginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user is not None:
                login(user, request)

                return redirect('projects')

            else:
                messages.error(request, "Username or password is icorrect")

        else:
            messages.error(request, "fill out all the fields")

    return render(request, 'login.html')


def post(request):
    if request.method == 'POST':
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request, 'post.html', {'obj': obj})

        else:
            form = ImageForm()
            img = Image.objects.all()
        return render(request, 'post.html', {'img': img, 'form': form})
