from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPage, name ="todoList"),
    path('updateTask/<str:pk>',views.updateTask, name = "update_task"),
    path('deleteTask/<str:pk>',views.deleteTask, name = "delete_task"),
    
    ]