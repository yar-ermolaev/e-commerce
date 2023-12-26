from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms


class LoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']
