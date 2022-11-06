from django.shortcuts import render
from django.views import View


class HomePage(View):
    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Home Page'
        }
        return render(request, 'mention/home.html', context)
