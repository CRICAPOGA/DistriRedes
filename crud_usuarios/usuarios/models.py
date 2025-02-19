from django.db import models

# models.py
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre