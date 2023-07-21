from .models import Task
from .serializers import TaskSerializer
from rest_framework import generics

class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CreateTask(generics.CreateAPIView):
    serializer_class = TaskSerializer

class TaskListCompleted(generics.ListAPIView):
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        return Task.objects.filter(completed=True)

class DeleteTask(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UpdateTask(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer