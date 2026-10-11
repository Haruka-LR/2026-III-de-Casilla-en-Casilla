from django import forms
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

class PermisoForm(forms.ModelForm):
    class Meta:
        model = Permission
        fields = ['name', 'codename', 'content_type']
        labels = {
            'name': 'Nombre del Permiso',
            'codename': 'Código (Codename)',
            'content_type': 'Módulo Asociado',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': ''
            }),
            'codename': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': ''
            }),
            'content_type': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content_type'].queryset = ContentType.objects.all()
        
        # Mapeo para traducir los modelos base de Django al español
        traducciones = {
            'user': 'Módulo de Usuario',
            'usuario': 'Módulo de Usuarios',
            'permission': 'Módulo de Permisos',
            'group': 'Módulo de Grupos',
            'session': 'Módulo de Sesiones',
            'logentry': 'Módulo de Administración',
            'contenttype': 'Tipos de Contenido',
        }
        
        # Muestra el nombre traducido si existe en el diccionario o lo formatea automáticamente
        self.fields['content_type'].label_from_instance = lambda obj: traducciones.get(
            obj.model.lower(), 
            f"Módulo de {obj.model.capitalize()}"
        )