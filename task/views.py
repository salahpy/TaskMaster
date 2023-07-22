from .models import Task
from .serializers import TaskSerializer
from rest_framework import generics

class TaskList(generics.ListAPIView):
    serializer_class = TaskSerializer
    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Task.objects.filter(user=user_id)

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