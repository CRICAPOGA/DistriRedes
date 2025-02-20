from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Usuario

# Create your views here.
def login_view(request):
    return render(request, 'login.html')

def login_auth(request):
    if request.method == 'POST':
        username = request.POST['username']
        contraseña = request.POST['password']
        user = authenticate(request, username=username, password=contraseña)
        if user is not None:
            login(request, user)  # Inicia la sesión del usuario
            messages.success(request,'Logeado')
            return redirect('home')  # Redirige a una página principal index.html
        else:
            messages.error(request,'Credenciales incorrectas')
            return render(request, 'login.html')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        
        user = User.objects.create_user(username=username, password=password, email=email)
        Usuario.objects.create(user=user, address=address, phone=phone)
        
        messages.success(request, 'Usuario registrado exitosamente')
        return redirect('login')
    
    return render(request, 'register.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

@login_required
def crear_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        
        user = User.objects.create_user(username=username, password=password, email=email)
        Usuario.objects.create(user=user, address=address, phone=phone)
        
        messages.success(request, 'Usuario creado exitosamente')
        return redirect('lista_usuarios')
    
    return render(request, 'crear_usuario.html')

@login_required
def editar_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    if request.method == 'POST':
        usuario.user.username = request.POST['username']
        usuario.user.email = request.POST['email']
        usuario.address = request.POST['address']
        usuario.phone = request.POST['phone']
        usuario.user.save()
        usuario.save()
        
        messages.success(request, 'Usuario actualizado exitosamente')
        return redirect('lista_usuarios')
    
    return render(request, 'editar_usuario.html', {'usuario': usuario})

@login_required
def eliminar_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    usuario.user.delete()
    usuario.delete()
    
    messages.success(request, 'Usuario eliminado exitosamente')
    return redirect('lista_usuarios')