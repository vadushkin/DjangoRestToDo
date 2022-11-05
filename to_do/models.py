from django.contrib.auth.models import User
from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=100, verbose_name="Доска")

    def __str__(self):
        return f'Доска - {self.name}'

    class Meta:
        verbose_name = "Доска"
        verbose_name_plural = "Доски"


class TodoList(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    is_done = models.BooleanField(default=False, verbose_name="Завершено?")
    created_at = models.DateTimeField(auto_created=True, verbose_name="Создано в")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено в")
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Пользователь")
    board = models.ForeignKey(Board, on_delete=models.PROTECT, verbose_name="Доска")

    def __str__(self):
        return f'Список - {self.title}, Создано в {self.created_at}'

    class Meta:
        verbose_name = "Список Todo"
        verbose_name_plural = "Списки Todo"
