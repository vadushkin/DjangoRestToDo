from django.contrib import admin

from .models import TodoList, Board


class BoardAdmin(admin.ModelAdmin):
    pass


class TodoListAdmin(admin.ModelAdmin):
    pass


admin.site.register(TodoList, TodoListAdmin)
admin.site.register(Board, BoardAdmin)
