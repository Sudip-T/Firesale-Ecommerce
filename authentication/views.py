from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm



class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'login.html'
