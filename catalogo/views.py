from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


# ---------------------------------------------------------------------------
# Recurso: Producto (id, nombre, expansion, tipo)
# Datos de ejemplo en memoria (todavía no hay modelos ni base de datos).
# ---------------------------------------------------------------------------

productos = [
    {'id': 1, 'nombre': 'Booster Pack Escarlata y Púrpura', 'expansion': 'Escarlata y Púrpura', 'tipo': 'sobre'},
    {'id': 2, 'nombre': 'Elite Trainer Box 151', 'expansion': '151', 'tipo': 'caja'},
    {'id': 3, 'nombre': 'Charizard ex', 'expansion': 'Llamas Obsidianas', 'tipo': 'carta'},
]


@api_view(['GET'])
def lista_productos(request):
    """Devuelve la lista completa de productos."""
    return Response(productos)
