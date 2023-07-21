from django.urls import path
from .views import *

urlpatterns = [
    path('list/',TaskList.as_view()),
    path('listCompleted/',TaskListCompleted.as_view()),
    path('create/',CreateTask.as_view()),
    path('delete/<int:pk>/', DeleteTask.as_view()),
    path('update/<int:pk>/', UpdateTask.as_view()),
]
