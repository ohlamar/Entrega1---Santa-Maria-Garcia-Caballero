from django.shortcuts import redirect, render
from datetime import datetime

from creation.forms import Busqueda, FormPerson
from .models import Person

def create(request):
    if request.method == 'POST':
        form = FormPerson(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            fecha = data.get('date')
            if not fecha:
                fecha = datetime.now()
                
            person = Person(nombre=data.get('nombre'), 
                           edad=data.get('edad'),
                           fecha=fecha)
            person.save()
            
            return redirect('listado')
        
        else:
            return render(request, 'creation/creation.html', {'form': form})
    
    form_per = FormPerson()
    
    return render(request, 'creation/creation.html', {'form': form_per})

def listado(request):
    
    nom_bus = request.GET.get('nombre')
    if nom_bus:
        listas = Person.objects.filter(nombre__icontains=nom_bus) 
    else:
        listas = Person.objects.all()
    
    form = Busqueda()    
    return render(request, 'creation/listado.html', {'listas': listas, 'form':form})

# def editar(request, id):
#     persona = Person.objects.get(id=id)
    
#     if request.method == 'POST':
#         form = FormPerson(request.POST)
#         if form.is_valid():
#             persona.nombre = form.cleaned_data.get('nombre')
#             persona.edad = form.cleaned_data.get('edad')
#             persona.fecha = form.cleaned_data.get('fecha')
#             persona.save()
    
#             return redirect('listado')
        
#         else:
#             return render(request, 'edit.html', {'form': form})
    
#     form_person = FormPerson(initial={'nombre': persona.nombre, 'edad': persona.edad, 'fecha': persona.fecha})
    
#     return render(request, 'edit.html', {'form': form_person})
    

def edit(request, id):
    person = Person.objects.get(id=id)
    
    if request.method == 'POST':
        form = FormPerson(request.POST)
        if form.is_valid():
            person.nombre = form.cleaned_data.get('nombre')
            person.edad = form.cleaned_data.get('edad')
            person.fecha = form.cleaned_data.get('fecha')
            person.save()
            
            return redirect('listado')

        else:
            return render(request, 'editar', {'form': form, 'person': person})
        
    form_person = FormPerson(initial={'nombre': person.nombre, 'edad': person.edad, 'fecha': person.fecha})
    
    return render(request, 'creation/editar.html', {'form': form_person, 'person': person})


def eliminar(request, id):
    persona = Person.objects.get(id=id)
    persona.delete()
    
    return redirect('listado')

def mostrar(request, id): 
    person = Person.objects.get(id=id)
    return render(request, 'creation/mostrar.html', {'person': person})