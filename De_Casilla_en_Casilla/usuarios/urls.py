from django.urls import path
from . import views

urlpatterns = [
    path('permisos/', views.PermisoListView.as_view(), name='permisos_list'),
    path('permisos/nuevo/', views.PermisoCreateView.as_view(), name='permiso_create'),
    path('permisos/editar/<int:pk>/', views.PermisoUpdateView.as_view(), name='permiso_update'),
    path('permisos/eliminar/<int:pk>/', views.PermisoDeleteView.as_view(), name='permiso_delete'),
]