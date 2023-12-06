from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from . import forms


class LoginUser(LoginView):
    form_class = forms.LoginForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        return reverse_lazy('index')


class RegistrationView(CreateView):
    template_name = 'users/registration.html'
    form_class = forms.RegistrationForm
    success_url = reverse_lazy('users:login')
    extra_context = {'title': 'Регистрация'}


class ProfileView(UpdateView):
    form_class = forms.ProfileForm
    template_name = 'users/profile.html'
    extra_context = {'title': 'Профиль пользователя'}
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
