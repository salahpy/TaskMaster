from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('list/<int:user_id>/',TaskList.as_view()),
    path('listCompleted/',TaskListCompleted.as_view()),
    path('create/',CreateTask.as_view()),
    path('delete/<int:pk>/', DeleteTask.as_view()),
    path('update/<int:pk>/', UpdateTask.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
