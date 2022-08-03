from django.shortcuts import redirect, render
from datetime import datetime
from creation.forms import FormPerson, Search
from .models import Person


def create(request):
    if request.method == 'POST':
        form = FormPerson(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            date = data.get('date')
            if not date:
                date = datetime.now()
                
            person = Person(name=data.get('name'), 
                           age=data.get('age'),
                           date=date,
                           description=data.get('description'))
            person.save()
            
            return redirect('list')
        
        else:
            return render(request, 'creation/creation.html', {'form': form})
    
    form_per = FormPerson()
    
    return render(request, 'creation/creation.html', {'form': form_per})


def list(request):
    
    search_name = request.GET.get('name')
    if search_name:
        lists = Person.objects.filter(name__icontains=search_name) 
    else:
        lists = Person.objects.all()
    
    form = Search()    
    return render(request, 'creation/list.html', {'lists': lists, 'form':form})


def edit(request, id):
    person = Person.objects.get(id=id)
    
    if request.method == 'POST':
        form = FormPerson(request.POST)
        if form.is_valid():
            person.name = form.cleaned_data.get('name')
            person.age = form.cleaned_data.get('age')
            person.date = form.cleaned_data.get('date')
            person.description = form.cleaned_data.get('description')
            person.save()
            
            return redirect('list')

        else:
            return render(request, 'edit', {'form': form, 'person': person})
        
    form_person = FormPerson(initial={'name': person.name, 
                                      'age': person.age, 
                                      'date': person.date,
                                      'description': person.description})
    
    return render(request, 'creation/edit.html', {'form': form_person, 'person': person})


def delete(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    
    return redirect('list')


def show(request, id): 
    person = Person.objects.get(id=id)
    return render(request, 'creation/show.html', {'person': person})