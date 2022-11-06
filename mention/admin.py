from django.contrib import admin

from mention.models import Reminder


class ReminderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Reminder, ReminderAdmin)
