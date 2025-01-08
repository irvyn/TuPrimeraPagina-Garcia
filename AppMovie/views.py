from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import PeliculaForm, ResenaForm, UsuarioPerfilForm
from .models import Pelicula

# Renderiza la vista principal
def index(request):
    return render(request, 'AppMovie/index.html')

# Busca la pelicula por todos sus campos
def buscar_pelicula(request):
    query = request.GET.get('q', '')
    resultados = []

    if query:
        # Filtra las coincidencias segun el texto ingresado por el usuario
        peliculas = Pelicula.objects.filter(
            Q(titulo__icontains=query) | Q(genero__icontains=query) | Q(director__icontains=query) | Q(fecha_estreno__icontains=query)
        )

        # Devuelve el resultado en una lista
        for pelicula in peliculas:
            resultados.append({
                'titulo'        : pelicula.titulo,
                'genero'        : pelicula.genero,
                'director'      : pelicula.director,
                'fecha_estreno' : pelicula.fecha_estreno,
            })

    return render(request, 'AppMovie/index.html', {'resultados': resultados})

# Formulario de pelicula, si ingresa información la valida y la guarda, sino regresa la vista para su llenado
def crear_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PeliculaForm()

    return render(request, 'AppMovie/crear_pelicula.html', {'form': form})

# Formulario de reseña, si ingresa información la valida y la guarda, sino regresa la vista para su llenado
def crear_resena(request):
    if request.method == 'POST':
        form = ResenaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ResenaForm()

    return render(request, 'AppMovie/crear_resena.html', {'form': form})

# Formulario de usuario, si ingresa información la valida y la guarda, sino regresa la vista para su llenado

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioPerfilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UsuarioPerfilForm()

    return render(request, 'AppMovie/crear_usuario_perfil.html', {'form': form})