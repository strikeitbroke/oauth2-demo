from rest_framework.generics import ListCreateAPIView
from .serializers import TodoSerializer
from .models import Todo


class TodoListView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
