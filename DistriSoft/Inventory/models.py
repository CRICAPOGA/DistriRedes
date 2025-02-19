from django.db import models

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='Inventory\static\img', null=True)
    category = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.name