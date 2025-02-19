from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Usuario
from .forms import UsuarioForm

class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuarios/lista.html'

class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'usuarios/detalle.html'

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/formulario.html'
    success_url = reverse_lazy('usuarios_lista')

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/formulario.html'
    success_url = reverse_lazy('usuarios_lista')

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuarios/confirmar_borrar.html'
    success_url = reverse_lazy('usuarios_lista')