from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from todos.serializers import ReducedTodoSerializer, TodoSerializer
from .models import Todo

class ViewTodos(APIView):
    def get(self, request):
        queryset = Todo.objects.all()
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TodoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDetails(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request, pk):
        try:
            queryset = Todo.objects.get(pk=pk)
            serializer = TodoSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"error": f'todo com id {pk} não existe!'}, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        try:
            queryset = Todo.objects.get(pk=pk)
            serializer = TodoSerializer(
                queryset, data=request.data, partial=True
            )

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"error": f'todo com id {pk} não existe!'}, status=status.HTTP_400_BAD_REQUEST)
