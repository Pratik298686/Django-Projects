from django.urls import path
from . import views
# api key 1e6b176625ebe3adb848d0d1610ce655
urlpatterns = [
    path('', views.index)
]