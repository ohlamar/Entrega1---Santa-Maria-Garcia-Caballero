from django.urls import path
from .views import create, listado

urlpatterns = [
    path('create/', create, name='create'),
    path('listado/',listado, name='listado')
]