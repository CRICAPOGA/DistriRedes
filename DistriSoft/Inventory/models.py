from django.db import models

############ PRODUCTOS ############
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
    
############ SERVICIOS ############
class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
############ COTIZACIONES ############
class Cotizacion(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[
            ('approved', 'Approved'),
            ('pending', 'Pending')
        ],
        default='pending'
    )
    quote_type = models.CharField(
        max_length=10,
        choices=[
            ('product', 'Product'),
            ('service', 'Service')
        ],
        default='product'
    )

    def __str__(self):
        return 'Cotización #' + str(self.id) + ' - ' + str(self.quote_type) + '(' + str(self.status) + ')'
    
class DetalleCotizacion(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    product = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)
    service = models.ForeignKey(Servicio, on_delete=models.CASCADE, null=True, blank=True)
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cotizacion.id} - {self.product.name if self.product else "No Product"} - {self.service.name if self.service else "No Service"}'