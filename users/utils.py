from datetime import timedelta

from django.utils.timezone import now

from .models import EmailVerification


def create_and_send_verification(user):
    expiration = now() + timedelta(days=2)
    record = EmailVerification.objects.create(user=user, expiration=expiration)
    record.send_verification_email()
