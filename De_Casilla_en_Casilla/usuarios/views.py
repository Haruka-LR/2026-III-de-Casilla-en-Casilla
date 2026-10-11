# se agregaron imports
from django.contrib.auth.models import Permission
from .forms import PermisoForm

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Usuario

# READ: Muestra la tabla con todos los usuarios
class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuarios/lista.html'
    context_object_name = 'usuarios'

# CREATE: Muestra el formulario para crear un usuario nuevo
class UsuarioCreateView(CreateView):
    model = Usuario
    template_name = 'usuarios/formulario.html'
    # Campos que mostraremos en el HTML
    fields = ['username', 'email', 'rol', 'telefono'] 
    success_url = reverse_lazy('lista_usuarios')

# UPDATE: Formulario pre-llenado para editar
class UsuarioUpdateView(UpdateView):
    model = Usuario
    template_name = 'usuarios/formulario.html'
    fields = ['username', 'email', 'rol', 'telefono']
    success_url = reverse_lazy('lista_usuarios')

# DELETE: Pantalla de confirmación para borrar
class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuarios/confirmar_borrado.html'
    success_url = reverse_lazy('lista_usuarios')

    
# Permisos Views para crud de permisos
class PermisoListView(ListView):
    model = Permission
    template_name = 'permisos/lista.html'
    context_object_name = 'permisos'

    def get_queryset(self):
        # Excluye tanto las apps internas de Django como los permisos por defecto de la app 'usuarios'
        return Permission.objects.exclude(
            content_type__app_label__in=['admin', 'auth', 'contenttypes', 'sessions']
        ).exclude(
            codename__in=['add_user', 'change_user', 'delete_user', 'view_user', 'add_usuario', 'change_usuario', 'delete_usuario', 'view_usuario']
        )

class PermisoCreateView(CreateView):
    model = Permission
    form_class = PermisoForm
    template_name = 'permisos/formulario.html'
    success_url = reverse_lazy('listar_permisos')

class PermisoUpdateView(UpdateView):
    model = Permission
    form_class = PermisoForm
    template_name = 'permisos/formulario.html'
    success_url = reverse_lazy('listar_permisos')

class PermisoDeleteView(DeleteView):
    model = Permission
    template_name = 'permisos/confirmar_borrado.html'
    success_url = reverse_lazy('listar_permisos')