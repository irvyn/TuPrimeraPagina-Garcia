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
from .views import index, edit_profile, get_movie, get_movies, get_about, post_movie, login, sign_up, log_out

from django.conf import settings
from django.conf.urls.static import static

# Se registran 3 formularios y 1 buscador
urlpatterns = [
    path('', index, name='index'),

    path('movies', get_movies, name='movies'),
    path('about', get_about, name='about'),
    path('post_movie', post_movie, name='post_movie'),
    path('movie/<str:imdbID>/<int:id>/', get_movie, name='movie'),

    path('login', login, name='login'),
    path('sign_up', sign_up, name='sign_up'),
    path('log_out', log_out, name='log_out'),

    path('edit_profile', edit_profile, name='edit_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)