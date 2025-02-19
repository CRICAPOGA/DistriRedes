from django.urls import path
from .views import UsuarioListView, UsuarioDetailView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView

urlpatterns = [
    path('', UsuarioListView.as_view(), name='usuarios_lista'),
    path('<int:pk>/', UsuarioDetailView.as_view(), name='usuarios_detalle'),
    path('nuevo/', UsuarioCreateView.as_view(), name='usuarios_nuevo'),
    path('editar/<int:pk>/', UsuarioUpdateView.as_view(), name='usuarios_editar'),
    path('borrar/<int:pk>/', UsuarioDeleteView.as_view(), name='usuarios_borrar'),
]