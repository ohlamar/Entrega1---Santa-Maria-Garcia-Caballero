from datetime import date
from django import forms

class FormPerson(forms.Form):
    name = forms.CharField(max_length=30)
    age = forms.IntegerField()
    date = forms.DateField(required=False)
    
class Search(forms.Form):
    name = forms.CharField(max_length=30)