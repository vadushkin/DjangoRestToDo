from rest_framework import serializers

from .models import Board, TodoList


class BoardCreateAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class TodoListAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'


class BoardListAPIViewSerializer(serializers.Serializer):
    name = serializers.CharField()
    count = serializers.IntegerField()
