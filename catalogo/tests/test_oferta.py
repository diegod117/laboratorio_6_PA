from django.test import TestCase
from rest_framework.test import APIClient

from catalogo.models import Oferta


# ===== Oferta (Johann) =====
class OfertaAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Oferta.objects.create(producto='Booster Box 151', tienda='Weplay Store', precio=40000, stock=10)
        Oferta.objects.create(producto='Charizard ex', tienda='Sniper Games', precio=10000, stock=30)

    def test_listar_ofertas(self):
        respuesta = self.client.get('/api/ofertas/')

        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(len(respuesta.data), 2)
# ===== Fin Oferta (Johann) =====
