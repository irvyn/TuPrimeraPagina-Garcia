import requests

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import PeliculaForm, ResenaForm, UsuarioPerfilForm, UsuarioForm, UsuarioLoginForm
from .models import Pelicula, UsuarioPerfil

from django.contrib.auth import authenticate, login as auth_login
from .forms import UsuarioForm

# Renderiza la vista principal
@login_required
def index(request):
    return render(request, 'AppMovie/index.html', {'user': get_user(request)})

@login_required
def get_user(request):
    profile = UsuarioPerfil.objects.get(usuario=request.user)

    return {
        'id': request.user.id,
        'username': request.user.username,
        'avatar': profile.avatar.url if profile.avatar else '/static/assets/empty-profile.png'
    }

# Se guarda la biografia y avatar del usuario logueado
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UsuarioPerfilForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            # Check if the user profile already exists
            try:
                profile = UsuarioPerfil.objects.get(usuario=request.user)
                # Update the existing profile
                for field, value in form.cleaned_data.items():
                    setattr(profile, field, value)
            except UsuarioPerfil.DoesNotExist:
                # Create a new profile
                profile = form.save(commit=False)
                profile.usuario = request.user

            profile.save()
            return redirect('index')
    else:
        form = UsuarioPerfilForm()

    return render(request, 'AppMovie/edit_profile.html', {'form': form, 'user': get_user(request)})

@login_required
def post_movie(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = PeliculaForm()

    return render(request, 'AppMovie/peliculas.html', {'movies': get_all_movies(), 'form': PeliculaForm(), 'user': get_user(request)})

# Devuelve las pelicuas registradas en la BD y consulta en un API para obtener su poster
@login_required
def get_movies(request):
    return render(request,'AppMovie/peliculas.html', {'movies': get_all_movies(), 'form': PeliculaForm(), 'user': get_user(request)})

def get_all_movies():
    peliculas = Pelicula.objects.all().order_by('-id')

    resultados = []

    for p in peliculas:
        # Realizar una llamada API a la API de OMDb
        year = p.fecha_estreno.year
        response = requests.get(f'http://www.omdbapi.com/?apikey=1c186aa0&t={p.titulo}&y={year}')
        data = response.json()

        # Comprueba si se encontró la película
        if data['Response'] == 'True':
            resultados.append({
                'id'     : p.id,
                'imdbID' : data['imdbID'],
                'titulo' : data['Title'] + ' ('+data['Year']+')',
                'poster' : data['Poster']
            })
        else:
            resultados.append({
                'titulo': p.titulo,
                'url': 'Poster not found'
            })

    return resultados

@login_required
def get_movie(request, imdbID, id):
    if request.method == 'POST':
        form = ResenaForm(request.POST)
        if form.is_valid():
            resena = form.save(commit=False)
            resena.pelicula_id = id
            resena.usuario_id = request.user.id,
            resena.save()
    else:
        form = ResenaForm()

    response = requests.get(f'http://www.omdbapi.com/?apikey=1c186aa0&i={imdbID}')
    movie = response.json()
    movie['id'] = id

    return render(request,'AppMovie/movie.html', {'movie': movie, 'form': form, 'user': get_user(request)})

@login_required
# Devuelve página acerca de
def get_about(request):
    return render(request, 'AppMovie/acerca_de.html', {'user': get_user(request)})

# login
def login(request):
    if request.method == 'POST':
        form = UsuarioLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')  # Redirect to a success page
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = UsuarioLoginForm()

    return render(request, 'AppMovie/login.html', {'form': form})

# sign up
def sign_up(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UsuarioForm()

    return render(request, 'AppMovie/sign_up.html', {'form': form})

@login_required
def log_out(request):
    logout(request)
    return redirect('login')