from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.display_todos, name='display_todos'),
    path('add', views.add, name='add'),
]
