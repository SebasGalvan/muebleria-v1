from USUARIOS import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('login/', views.login, name='Login'),
    path('registro/', views.registro, name='Registro'),
]