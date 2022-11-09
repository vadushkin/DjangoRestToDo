import datetime

from celery import Celery
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from mention.models import Reminder

app = Celery()


@shared_task(bind=True)
def send_email_task(*args, **kwargs):
    datetime_datetime_now = datetime.datetime.now()

    users = Reminder.objects.filter(
        due_time__lt=datetime_datetime_now,
    )

    for user in users:
        send_mail(
            "Your task",
            f"{user.text}",
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=True,
        )
    return "Done"
