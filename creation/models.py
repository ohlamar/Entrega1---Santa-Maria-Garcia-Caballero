from django.db import models
from ckeditor.fields import RichTextField


class Person(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    descripcion = RichTextField(null=True)
    fecha = models.DateField(null=True)
    
    def __str__(self):
        return f'Nombre: {self.nombre}'
