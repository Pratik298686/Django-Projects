from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name="list"),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.delete_Task, name="delete")
]   