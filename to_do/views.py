from django.db.models import Count
from django.shortcuts import render
from django.views.generic.base import View
from rest_framework import generics, permissions

from to_do.models import Board
from to_do.serializers import BoardListAPIViewSerializer, BoardCreateAPIViewSerializer


class HomePage(View):
    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Home Page'
        }
        return render(request, 'to_do/home.html', context)


class BoardListAPIView(generics.ListAPIView):
    """
    API: to get all Boards with counts from todo_list for each board.
    Permissions: Authenticated.
    """
    serializer_class = BoardListAPIViewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get_queryset(self):
        queryset = Board.objects.annotate(count=Count('todolist__board'))
        return queryset


class BoardCreateAPIView(generics.CreateAPIView):
    """
    API: Create new Board.
    Permissions: AdminUser only.
    """
    serializer_class = BoardCreateAPIViewSerializer
    permission_classes = [permissions.IsAdminUser, ]


class BoardUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API: Update & Destroy boards.
    Permissions: AdminUser only.
    """
    serializer_class = BoardCreateAPIViewSerializer
    permission_classes = [permissions.IsAdminUser, ]
    queryset = Board.objects.all()
