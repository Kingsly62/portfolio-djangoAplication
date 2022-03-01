from tempfile import template
from django.contrib import admin
from django.urls import path, include
from home import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('register', views.register, name='register'),
    path('login',  views.LoginView, name='login'),
    path('email', views.email, name='email'),
    path('post', views.post, name='post'),
    path('contact', views.contact, name='contact'),
    path('pro', views.pro, name='pro')
]
