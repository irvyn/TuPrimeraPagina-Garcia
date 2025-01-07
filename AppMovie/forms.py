from django import forms
from .models import Pelicula, Resena, Usuario

class Pelicula(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'genero', 'director', 'fecha_estreno']