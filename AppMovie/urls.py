"""
URL configuration for MiProyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import index, crear_pelicula, crear_resena, crear_usuario

urlpatterns = [
    path('', index, name='index'),
    path('crear_pelicula', crear_pelicula, name='crear_pelicula'),
    path('crear_resena', crear_resena, name='crear_resena'),
    path('crear_usuario', crear_usuario, name='crear_usuario'),
]