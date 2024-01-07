from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView

from . import views


app_name = 'users'
urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('registration/verify-email/', TemplateView.as_view(
        template_name='users/send_verification_code.html'), name='verify-email'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('verify/<str:email>/<uuid:code>/', views.EmailVerificationView.as_view(),
         name='email_verification'),
    path('expired-link/', TemplateView.as_view(
        template_name='users/expired_link.html'), name='expired'),
]
