from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
    'send-mail-every-day-at-11': {
        'task': 'tasks.send_mail_func',
        'schedule': crontab(hour=11, minute=0),
    }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')