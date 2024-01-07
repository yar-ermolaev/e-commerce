from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView

from cart.models import Cart
from . import forms
from .models import EmailVerification
from .utils import create_and_send_verification


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

    def form_valid(self, form):
        session_key = self.request.session.session_key
        response = super().form_valid(form)
        if session_key:
            Cart.objects.filter(session_key=session_key).update(user=self.object)
        return response


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
        if email_verifications.exists():
            if not email_verifications.first().is_expired():
                user.is_verified_email = True
                user.is_active = True
                user.save()
                return super().get(request, *args, **kwargs)
            else:
                email_verifications.delete()
                create_and_send_verification(user)
        return HttpResponseRedirect(reverse('users:expired'))
