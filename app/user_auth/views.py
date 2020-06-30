from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, resolve_url
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, logout
from django.core.mail import send_mail

from .forms import UserRegisterForm, UserLoginForm


class RegisterUser(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'user_auth/register.html'


class LoginUser(LoginView):
    template_name = 'user_auth/login.html'
    form_class = UserLoginForm

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or resolve_url(settings.LOGIN_REDIRECT_URL)

