from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('login_auth/', views.login_auth, name='login_auth'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]