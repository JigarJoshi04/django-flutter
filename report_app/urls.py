from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    # Your URLs...
    path('user_based_report/', views.user_based_report, name='user_basedreport'),
    path('zone_based_report/', views.zone_based_report, name='user_basedreport'),
]
