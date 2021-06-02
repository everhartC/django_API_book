from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
# Create your views here.

#* ListAPIVIEW - Displays all Todos
class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


#* RetrieveAPIView - Displays a single model instance
class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer