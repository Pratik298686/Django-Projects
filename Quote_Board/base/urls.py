from django.urls import path, include
from base import views

urlpatterns = [
    path('',views.quote)
]