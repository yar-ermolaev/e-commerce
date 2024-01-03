import uuid

from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy
from django.conf import settings
from django.utils.timezone import now


class User(AbstractUser):
    is_verified_email = models.BooleanField(default=False)


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True, default=uuid.uuid4, editable=False,
                            verbose_name='Код')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    expiration = models.DateTimeField(verbose_name='Дата истечения')

    def __str__(self):
        return f'EmailVerification for {self.user.email}'

    def is_expired(self):
        return True if now() >= self.expiration else False

    def send_verification_email(self):
        link = reverse_lazy('users:email_verification', kwargs={
            'email': self.user.email, 'code': self.code})
        verification_link = settings.DOMAIN_NAME + link
        message = (f"Для подтверждения учетной записи для пользователя {self.user.username}"
                   f" на сайте VoltTech перейдите по ссылке: {verification_link}")
        send_mail(
            subject='Подтверждение учетной записи',
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False
        )



