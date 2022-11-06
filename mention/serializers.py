from .models import Reminder
from rest_framework import serializers


class ReminderListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'
