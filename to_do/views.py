from django.shortcuts import render


def index(request):
    context = {
        'title': 'Quick Start',
    }
    return render(request, 'to_do/index.html', context)
