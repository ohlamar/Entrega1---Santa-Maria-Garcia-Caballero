from django.urls import path
from .views import create, listado, edit, eliminar, mostrar

urlpatterns = [
    path('create/', create, name='create'),
    path('listado/', listado, name='listado'),
    path('editar/<int:id>/', edit, name='editar'),
    path('eliminar/<int:id>/', eliminar, name='eliminar'),
    path('mostrar/<int:id>/', mostrar, name='mostrar'),
]