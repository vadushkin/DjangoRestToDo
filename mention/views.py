from django.shortcuts import render
from django.views import View
from rest_framework import generics, permissions

from .models import Reminder
from .serializers import ReminderListSerializers


class HomePage(View):
    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Home Page'
        }
        return render(request, 'mention/home.html', context)


class ReminderListAPIView(generics.ListAPIView):
    """
    API: Get a list of all reminders.
    Permissions: AdminUser only.
    """
    queryset = Reminder.objects.all()
    serializer_class = ReminderListSerializers
    permission_classes = [permissions.IsAdminUser, ]


class ReminderCreateAPIView(generics.CreateAPIView):
    """
    API: Create a new reminder.
    Permissions: AdminUser only.
    """
    queryset = Reminder.objects.all()
    serializer_class = ReminderListSerializers
    permission_classes = [permissions.IsAdminUser, ]


class ReminderDeleteAPIView(generics.DestroyAPIView):
    """
    API: Delete a reminder.
    Permissions: AdminUser only.
    """
    queryset = Reminder.objects.all()
    serializer_class = ReminderListSerializers
    permission_classes = [permissions.IsAdminUser, ]
