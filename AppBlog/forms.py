from django import forms
from .models import Blog
from django.contrib.auth.models import User

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content', 'author')
        labels = {
            'Titulo': 'title',
            'Contenido': 'content'
        }