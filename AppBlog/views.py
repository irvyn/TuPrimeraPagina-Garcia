import requests

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Blog
from AppMovie.utils import get_user
from .forms import BlogForm
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect

@login_required
def index2(request):
    entries = Blog.objects.all().order_by('-id')

    return render(request,'AppBlog/index.html', {'entries': entries, 'form': BlogForm(), 'user': get_user(request)})

@login_required
def index(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.created_at = timezone.now()
            blog.author = request.user
            blog.save()
    else:
        form = BlogForm()

    entries = Blog.objects.all().order_by('-id')

    return render(request,'AppBlog/index.html', {'entries': entries, 'form': form, 'user': get_user(request)})

@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return redirect('blog')