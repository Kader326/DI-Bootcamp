from django.shortcuts import render, redirect
from todo.models import Category, Todo
from django.contrib import messages
from .forms import TodoForm


def display_todos(request):
    todos = Todo.objects.order_by('title')
    cats = Category.objects.order_by('name')
    return render(request, 'todo/home.html', {"todos":todos, "cats":cats})


def add(request):
    if request.method=="POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tache ajouté avec successfully !")
            return redirect('display_todos')
        else:
            return render(request, 'todo/add.html', {"form":form})
    else:
        form = TodoForm()
        return render(request, 'todo/add.html', {"form":form})

# Create your views here.
