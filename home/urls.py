from django.urls import path
from .views import homepage, about, perfil, login
urlpatterns = [
    path('', homepage, name='Inicio'),
    path('about/', about, name='about'),
    path('perfil/', perfil, name='perfil'),
    path('login/', login, name='login')
]