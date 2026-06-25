from django.shortcuts import render, redirect
from .models import Task

def home(request):
    if request.method == "POST":
        title = request.POST['title']
        Task.objects.create(title=title)

    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})