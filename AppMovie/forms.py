from django import forms
from .models import Pelicula, Resena, UsuarioPerfil
from django.contrib.auth.models import User

# Se personaliza el campo fecha_estreno para que pemita elegir una fecha
class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = (
            'titulo',
            'genero',
            'director',
            'fecha_estreno'
        )
        widgets = {
            'fecha_estreno': forms.DateInput(attrs={'type': 'date'}),
        }

class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = (
            'contenido',
            'calificacion',
        )
        labels = {
            'contenido': 'comment',
            'calificacion': 'rating',
        }

class UsuarioPerfilForm(forms.ModelForm):
    class Meta:
        model = UsuarioPerfil
        fields = ('biografia', 'avatar')

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }

class UsuarioLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)