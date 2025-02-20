from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria
from django.contrib.auth.decorators import login_required
from django.contrib import messages


############## CRUD PRODUCTOS ##############
@login_required
def productos(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'CRUD productos/productos.html', {'productos': productos, 'categorias': categorias})

@login_required
def productos_por_categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    productos = Producto.objects.filter(category=categoria)
    categorias = Categoria.objects.all()
    return render(request, 'CRUD productos/productos.html', {'productos': productos, 'categorias': categorias, 'categoria': categoria})

@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, f'El producto "{producto.name}" ha sido eliminado exitosamente.')
        return redirect('productos')
    return render(request, 'CRUD productos/eliminar_producto.html', {'producto': producto})

@login_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    categorias = Categoria.objects.all()
    
    if request.method == 'POST':
        producto.name = request.POST.get('name')
        producto.description = request.POST.get('description')
        if request.FILES.get('image'):
            producto.image = request.FILES.get('image')
        producto.category_id = request.POST.get('category')
        producto.save()
        messages.success(request, f'El producto "{producto.name}" ha sido actualizado exitosamente.')
        return redirect('productos')
    
    return render(request, 'CRUD productos/editar_producto.html', {'producto': producto, 'categorias': categorias})

@login_required
def crear_producto(request):
    categorias = Categoria.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        category_id = request.POST.get('category')
        
        producto = Producto(name=name, description=description, image=image, category_id=category_id)
        producto.save()
        messages.success(request, f'El producto "{producto.name}" ha sido creado exitosamente.')
        return redirect('productos')
    
    return render(request, 'CRUD productos/crear_producto.html', {'categorias': categorias})

############## CRUD INSUMOS ##############
############## CRUD SERVICIOS ##############