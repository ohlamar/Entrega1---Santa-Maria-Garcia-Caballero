from django import forms
from ckeditor.fields import RichTextFormField

class FormPerson(forms.Form):
    nombre = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    descripcion = RichTextFormField()
    fecha = forms.DateField(required=False)
    
class Busqueda(forms.Form):
    nombre = forms.CharField(max_length=30)