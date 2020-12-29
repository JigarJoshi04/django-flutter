from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    # Your URLs...
    path('create_tree', views.create_new_tree, name='create user'),
   
]
