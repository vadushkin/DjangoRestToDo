from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('to-do/', include('to_do.urls')),
    path('mention/', include('mention.urls')),
]
