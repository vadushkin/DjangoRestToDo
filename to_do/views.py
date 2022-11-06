from django.db.models import Count
from django.shortcuts import render
from django.views.generic.base import View
from rest_framework import generics, permissions

from to_do.models import Board, TodoList
from to_do.serializers import BoardListAPIViewSerializer, \
    BoardCreateAPIViewSerializer, TodoListAPIViewSerializer


class HomePage(View):
    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Home Page'
        }
        return render(request, 'to_do/home.html', context)


class BoardListAPIView(generics.ListAPIView):
    """
    API: to get all Boards with counts from todo_list for each board.
    Permissions: All Authenticated.
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


class TodoCreateAPIView(generics.CreateAPIView):
    """
    API: Create a new task for the exact board.
    Permissions: AdminUser only.
    """
    serializer_class = TodoListAPIViewSerializer
    permission_classes = [permissions.IsAdminUser, ]
    queryset = TodoList.objects.all()


class TodoListAPIView(generics.ListAPIView):
    """
    API: Get a list of all tasks for boards.
    Permissions: All Authenticated.
    """
    serializer_class = TodoListAPIViewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get_queryset(self):
        # queryset = get_object_or_404(TodoList, board=self.kwargs['pk'])
        queryset = TodoList.objects.filter(board=self.kwargs['pk'])
        return queryset
