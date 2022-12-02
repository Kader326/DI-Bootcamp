

from django.urls import path, re_path
from apps.home import views
from .views import liste

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('all/', views.liste, name='liste'),
    

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
    
]
