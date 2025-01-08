from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import PeliculaForm
from .models import Pelicula

def index(request):
    return render(request, 'AppMovie/index.html')

def crear_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PeliculaForm()
        
    return render(request, 'AppMovie/crear_pelicula.html', {'form': form})

def buscar_pelicula(request):
    pass

def crear_resena(request):
    pass

def crear_usuario(request):
    pass