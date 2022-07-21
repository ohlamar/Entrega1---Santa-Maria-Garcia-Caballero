from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def about(request):
    return  render(request, 'about.html')

def perfil(request):
    return  render(request, 'perfil.html')

def login(request):
    return  render(request, 'login.html')