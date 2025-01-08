from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import PeliculaForm, ResenaForm, UsuarioPerfilForm
from .models import Pelicula

def index(request):
    return render(request, 'AppMovie/index.html')

def buscar_pelicula(request):
    pass

def crear_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PeliculaForm()

    return render(request, 'AppMovie/crear_pelicula.html', {'form': form})

def crear_resena(request):
    if request.method == 'POST':
        form = ResenaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ResenaForm()

    return render(request, 'AppMovie/crear_resena.html', {'form': form})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioPerfilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UsuarioPerfilForm()

    return render(request, 'AppMovie/crear_usuario_perfil.html', {'form': form})