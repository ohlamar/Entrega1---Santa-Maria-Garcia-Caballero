from django.db import models

# Create your models here.
class Person(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha = models.DateField(null=True)
    
    def __str__(self):
        return f'Nombre: {self.nombre}'
