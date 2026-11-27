from django.test import TestCase
from rest_framework.test import APIClient

from catalogo.models import Producto


class ProductoAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Producto.objects.create(nombre='Elite Trainer Box 151', expansion='151', tipo='caja')
        Producto.objects.create(nombre='Charizard ex', expansion='Llamas Obsidianas', tipo='carta')

    def test_listar_productos(self):
        respuesta = self.client.get('/api/productos/')
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(len(respuesta.json()), 2)
