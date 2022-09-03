from django.contrib import admin
from django.urls import path
from .views import TodoDetails, ViewTodos

urlpatterns = [
    path('', ViewTodos.as_view()),
    path('<int:pk>', TodoDetails.as_view()),
]