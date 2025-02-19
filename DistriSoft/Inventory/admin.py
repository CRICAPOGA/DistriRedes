from django.contrib import admin
from .models import Categoria, Producto, Servicio, Cotizacion, DetalleCotizacion

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Servicio)
admin.site.register(Cotizacion)
admin.site.register(DetalleCotizacion)