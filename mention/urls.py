from django.urls import path

from .views import HomePage, ReminderListAPIView, \
    ReminderCreateAPIView, ReminderDeleteAPIView

urlpatterns = [
    # Home Page
    path('', HomePage.as_view(), name='home-page'),

    # APIView for reminder
    path('reminder-list/', ReminderListAPIView.as_view(), name='reminder-list'),
    path('reminder-create/', ReminderCreateAPIView.as_view(), name='reminder-create'),
    path('reminder-delete/<int:pk>/', ReminderDeleteAPIView.as_view(), name='reminder-delete'),
]
