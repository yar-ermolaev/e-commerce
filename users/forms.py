from datetime import timedelta

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.utils.timezone import now

from .models import EmailVerification


class LoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']

    def save(self):
        user = super().save(commit=False)
        user.is_active = False
        user.save()
        expiration = now() + timedelta(days=2)
        record = EmailVerification.objects.create(user=user, expiration=expiration)
        record.send_verification_email()
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']
