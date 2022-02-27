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

    return render(request, 'post.html')
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
