from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView
from . import forms
from .models import EmailVerification


class LoginUser(LoginView):
    form_class = forms.LoginForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        return reverse_lazy('index')


class RegistrationView(CreateView):
    template_name = 'users/registration.html'
    form_class = forms.RegistrationForm
    success_url = reverse_lazy('users:verify-email')
    extra_context = {'title': 'Регистрация'}


class ProfileView(UpdateView):
    form_class = forms.ProfileForm
    template_name = 'users/profile.html'
    extra_context = {'title': 'Профиль пользователя'}
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class EmailVerificationView(TemplateView):
    template_name = 'users/email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = get_object_or_404(get_user_model(), email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified_email = True
            user.is_active = True
            user.save()
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))
