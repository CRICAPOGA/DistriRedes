from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria, Servicio
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
@login_required
def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'CRUD servicios/servicios.html', {'servicios': servicios})

@login_required
def eliminar_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, id=servicio_id)
    if request.method == 'POST':
        servicio.delete()
        messages.success(request, f'El servicio "{servicio.name}" ha sido eliminado exitosamente.')
        return redirect('servicios')
    return render(request, 'CRUD servicios/eliminar_servicio.html', {'servicio': servicio})

@login_required
def editar_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, id=servicio_id)
    
    if request.method == 'POST':
        servicio.name = request.POST.get('name')
        servicio.description = request.POST.get('description')
        servicio.price = request.POST.get('price')
        servicio.save()
        messages.success(request, f'El servicio "{servicio.name}" ha sido actualizado exitosamente.')
        return redirect('servicios')
    
    return render(request, 'CRUD servicios/editar_servicio.html', {'servicio': servicio})

@login_required
def crear_servicio(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        
        servicio = Servicio(name=name, description=description, price=price)
        servicio.save()
        messages.success(request, f'El servicio "{servicio.name}" ha sido creado exitosamente.')
        return redirect('servicios')
    
    return render(request, 'CRUD servicios/crear_servicio.html')