from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Usuario
from django.contrib.auth.models import Permission
from .forms import PermisoForm # Asegúrate de haber creado este formulario en forms.py


class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuarios/lista.html'
    context_object_name = 'usuarios'

class UsuarioCreateView(CreateView):
    model = Usuario
    template_name = 'usuarios/formulario.html'
    fields = ['username', 'email', 'rol', 'telefono']
    success_url = reverse_lazy('lista_usuarios')

class UsuarioUpdateView(UpdateView):
    model = Usuario
    template_name = 'usuarios/formulario.html'
    fields = ['username', 'email', 'rol', 'telefono']
    success_url = reverse_lazy('lista_usuarios')

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuarios/confirmar_borrado.html'
    success_url = reverse_lazy('lista_usuarios')


class PermisoListView(ListView):
    model = Permission
    template_name = 'usuarios/permiso_list.html'
    context_object_name = 'permisos'

class PermisoCreateView(CreateView):
    model = Permission
    form_class = PermisoForm  # Aquí usamos el ModelForm
    template_name = 'usuarios/permiso_form.html'
    success_url = reverse_lazy('lista_permisos') # Configuraremos este nombre en urls.py

class PermisoUpdateView(UpdateView):
    model = Permission
    form_class = PermisoForm 
    template_name = 'usuarios/permiso_form.html'
    success_url = reverse_lazy('lista_permisos')

class PermisoDeleteView(DeleteView):
    model = Permission
    template_name = 'usuarios/permiso_confirm_delete.html'
    success_url = reverse_lazy('lista_permisos')