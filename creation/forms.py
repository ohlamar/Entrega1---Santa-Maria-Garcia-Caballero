from datetime import date
from django import forms
from ckeditor.fields import RichTextFormField

class FormPerson(forms.Form):
    name = forms.CharField(max_length=30)
    age = forms.IntegerField()
    date = forms.DateField(required=False)
    description = RichTextFormField()
    
class Search(forms.Form):
    name = forms.CharField(max_length=30)