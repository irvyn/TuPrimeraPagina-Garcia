from django.shortcuts import render, redirect
from django.db.models import Q

def index(request):
    return render(request, 'AppMovie/index.html')