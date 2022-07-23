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

