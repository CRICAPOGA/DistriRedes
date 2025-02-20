from django.urls import path
from . import views

urlpatterns = [
    
    path('productos/', views.productos, name='productos'),
    path('productos/categoria/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('productos/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('productos/buscar/', views.buscar_productos, name='buscar_productos'),

    path('servicios/', views.servicios, name='servicios'),
    path('servicios/crear/', views.crear_servicio, name='crear_servicio'),
    path('servicios/editar/<int:servicio_id>/', views.editar_servicio, name='editar_servicio'),
    path('servicios/eliminar/<int:servicio_id>/', views.eliminar_servicio, name='eliminar_servicio'),
    path('servicios/buscar/', views.buscar_servicios, name='buscar_servicios'),

    path('catalogo_productos/', views.catalogo_productos, name='catalogo_productos'),
    path('catalogo/productos/categoria/<int:categoria_id>/', views.catalogo_p_categoria, name='catalogo_p_categoria'),
    path('catalogo/productos/buscar/', views.catalogo_p_buscar, name='catalogo_p_buscar'),

    path('catalogo_servicios/', views.catalogo_servicios, name='catalogo_servicios'),
    path('catalogo/servicios/buscar/', views.catalogo_s_buscar, name='catalogo_s_buscar'),
]