import requests

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Blog
from AppMovie.views import get_user
from django.shortcuts import render, redirect
from .forms import BlogForm

def index(request):
    return render(request, 'AppBlog/index.html')


@login_required
def index2(request):
    return render(request, 'AppBlog/index.html', {'user': get_user(request)})

@login_required
def index(request):
    entries = Blog.objects.all().order_by('-id')

    return render(request,'AppBlog/index.html', {'entries': entries, 'form': BlogForm(), 'user': get_user(request)})

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('index')  # Asegúrate de que 'index' sea el nombre correcto de la URL para tu vista de índice
    else:
        form = BlogForm()
    #return render(request, 'AppBlog/index.html', {'form': form})

    return redirect('index')