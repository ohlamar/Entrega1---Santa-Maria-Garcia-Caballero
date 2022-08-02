from ast import List
from django.urls import path
from .views import create, list, edit, delete, show

urlpatterns = [
    path('create/', create, name='create'),
    path('list/', list, name='list'),
    path('edit/<int:id>/', edit, name='edit'),
    path('delete/<int:id>/', delete, name='delete'),
    path('show/<int:id>/', show, name='show'),
]