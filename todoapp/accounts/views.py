from django.shortcuts import render
from django.contrib.auth.views import LoginView as BaseLoginView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class  LoginView(BaseLoginView):
    template_name = "registration/login.html"
    success_url = reverse_lazy('home')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"