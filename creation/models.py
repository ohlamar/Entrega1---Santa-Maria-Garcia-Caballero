from django.db import models
from ckeditor.fields import RichTextField 


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    date = models.DateField(null=True)
    description = RichTextField(null=True)
    
    def __str__(self):
        return f'Nombre: {self.name}'
