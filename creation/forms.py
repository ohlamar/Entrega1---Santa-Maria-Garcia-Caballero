from django import forms

class FormPerson(forms.Form):
    nombre = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha = forms.DateField(required=False)
    
class Busqueda(forms.Form):
    nombre = forms.CharField(max_length=30)