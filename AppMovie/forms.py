from django import forms
from .models import Pelicula, Resena, UsuarioPerfil

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
            'usuario',
            'pelicula',
            'contenido',
            'calificacion',
        )

class UsuarioPerfilForm(forms.ModelForm):
    class Meta:
        model = UsuarioPerfil
        fields = ('usuario', 'biografia', 'avatar')