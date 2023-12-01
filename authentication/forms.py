from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser


class CustomLoginForm(AuthenticationForm):
    user_email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

    class Meta:
        model = CustomUser
        fields = ['email', 'password']
