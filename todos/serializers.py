from rest_framework import serializers
from .models import Todo

class ReducedTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'titulo')

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'titulo', 'description', 'priority')