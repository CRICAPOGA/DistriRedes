from django.shortcuts import render, redirect
from .models import Producto, Categoria
from django.contrib.auth.decorators import login_required

@login_required
def productos(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'productos.html', {'productos': productos, 'categorias': categorias})

@login_required
def productos_por_categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    productos = Producto.objects.filter(category=categoria)
    categorias = Categoria.objects.all()
    return render(request, 'productos.html', {'productos': productos, 'categorias': categorias, 'categoria': categoria})