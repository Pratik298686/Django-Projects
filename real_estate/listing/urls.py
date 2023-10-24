from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listing_list, name= 'listings'),
    path('listing/<pk>/', views.listing_retrive, name= 'listing'),
    path('add-listing/',views.Listing_Create, name='listing-create'),
    path('listing/<pk>/edit/',views.Listing_update,name='listing-update'),
    path('listing/<pk>/delete/',views.listing_delete,name='listing-delete'),
    
]