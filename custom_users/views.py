from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from . import forms

class RegistrationView(CreateView):
    #form_class = UserCreationForm
    form_class = forms.CustomUserRegistration
    success_url = '/users/'
    template_name = 'register/registration.html'


class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'register/login.html'

    def get_success_url(self):
        return reverse("users:user_list")


class UserListView(ListView):
    queryset = User.objects.all()
    template_name = 'register/user_list.html'

    def get_queryset(self):
        return User.objects.all()






