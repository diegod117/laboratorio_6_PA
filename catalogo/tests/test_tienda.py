from django.test import TestCase
from rest_framework.test import APIClient
from catalogo.models import Tienda


class TiendaEndpointTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Tienda.objects.create(nombre='Magic Sur Chile', ciudad='Santiago', sitio_web='https://magicsur.cl')
        Tienda.objects.create(nombre='Weplay Store', ciudad='Viña del Mar', sitio_web='https://weplay.cl')

    def test_lista_tiendas_retorna_200(self):
        response = self.client.get('/api/tiendas/')
        self.assertEqual(response.status_code, 200)

    def test_lista_tiendas_retorna_dos_registros(self):
        response = self.client.get('/api/tiendas/')
        self.assertEqual(len(response.data), 2)
