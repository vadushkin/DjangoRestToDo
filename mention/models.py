from datetime import datetime

from django.db import models


class Reminder(models.Model):
    email = models.EmailField(
        max_length=100,
        verbose_name='Емейл',
    )
    text = models.TextField(
        verbose_name='Сообщение',
    )
    delay = models.IntegerField(
        default=10,
        verbose_name='Время в секундах',
    )
    due_time = models.DateTimeField(
        default=datetime.now,
        blank=True,
        verbose_name='Срок выполнения',
    )

    def __str__(self):
        return f'Reminder to {self.email}, if overdue more than {self.delay} seconds'
