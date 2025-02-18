from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.productos, name='productos'),
    path('productos/categoria/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('productos/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('servicios/', views.servicios, name='servicios'),
    path('servicios/crear/', views.crear_servicio, name='crear_servicio'),
    path('servicios/editar/<int:servicio_id>/', views.editar_servicio, name='editar_servicio'),
    path('servicios/eliminar/<int:servicio_id>/', views.eliminar_servicio, name='eliminar_servicio'),
]