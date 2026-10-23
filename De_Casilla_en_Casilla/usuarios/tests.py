from django.test import TestCase
from django.urls import reverse

from .models import Usuario


class UsuarioCrudTests(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create_user(
            username='ruben',
            password='ClaveSegura-123',
            email='ruben@example.com',
            rol='maestro',
            telefono='5551234567',
        )

    def test_formulario_de_creacion_muestra_requisitos_de_contrasena_en_espanol(self):
        response = self.client.get(reverse('crear_usuario'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Contraseña')
        self.assertContains(response, 'caracteres')
        self.assertContains(response, 'numérica')
        self.assertContains(response, 'introduzca la misma contraseña')
        self.assertContains(response, 'placeholder="Nombre"')
        self.assertContains(response, 'placeholder="Correo"')
        self.assertContains(response, 'placeholder="Teléfono"')
        self.assertContains(response, 'placeholder="Contraseña"')
        self.assertContains(response, 'placeholder="Confirmar contraseña"')
        self.assertNotContains(response, 'Longitud máxima 150 caracteres')

    def test_lista_muestra_usuarios(self):
        response = self.client.get(reverse('lista_usuarios'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'ruben')
        self.assertContains(response, 'Salir')
        self.assertTemplateUsed(response, 'usuarios/lista.html')

    def test_boton_salir_cierra_sesion(self):
        self.client.force_login(self.usuario)

        response = self.client.post(reverse('cerrar_sesion'), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('sesion_cerrada'))
        self.assertTemplateUsed(response, 'usuarios/sesion_cerrada.html')
        self.assertContains(response, 'Tu sesión se cerró correctamente')
        self.assertContains(response, 'Iniciar sesión')
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_crear_usuario_guarda_contrasena_cifrada(self):
        response = self.client.post(
            reverse('crear_usuario'),
            {
                'username': 'ana',
                'email': 'ana@example.com',
                'rol': 'usuario',
                'telefono': '5557654321',
                'password1': 'OtraClaveSegura-123',
                'password2': 'OtraClaveSegura-123',
            },
        )

        self.assertRedirects(response, reverse('lista_usuarios'))
        nuevo_usuario = Usuario.objects.get(username='ana')
        self.assertTrue(nuevo_usuario.check_password('OtraClaveSegura-123'))

    def test_editar_usuario_actualiza_datos(self):
        response = self.client.post(
            reverse('editar_usuario', args=[self.usuario.pk]),
            {
                'username': 'ruben_actualizado',
                'email': 'actualizado@example.com',
                'rol': 'admin',
                'telefono': '5550000000',
            },
        )

        self.assertRedirects(response, reverse('lista_usuarios'))
        self.usuario.refresh_from_db()
        self.assertEqual(self.usuario.username, 'ruben_actualizado')
        self.assertEqual(self.usuario.rol, 'admin')

    def test_eliminar_usuario_requiere_confirmacion_post(self):
        url = reverse('borrar_usuario', args=[self.usuario.pk])

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'usuarios/confirmar_borrado.html')
        self.assertTrue(Usuario.objects.filter(pk=self.usuario.pk).exists())

        response = self.client.post(url)
        self.assertRedirects(response, reverse('lista_usuarios'))
        self.assertFalse(Usuario.objects.filter(pk=self.usuario.pk).exists())
