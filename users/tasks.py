from celery import shared_task
from django.core.mail import send_mail


@shared_task()
def send_verification_email_task(message: str, from_: str, to: list) -> None:
    send_mail(
        subject='Подтверждение учетной записи',
        message=message,
        from_email=from_,
        recipient_list=to,
        fail_silently=False
    )
