from django.db import models

# Create your models here.

class Agent(models.Model):
    nickname = models.CharField(max_length=30)
    age = models.IntegerField()
    date = models.DateField(null=True)
    
    def __str__(self):
        return f'Agente {self.nickname}'