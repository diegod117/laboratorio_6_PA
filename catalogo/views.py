from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Oferta, Tienda
from .serializers import OfertaSerializer, TiendaSerializer

# Create your views here.


# ===== Oferta (Johann) =====
class OfertaViewSet(viewsets.ModelViewSet):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer
# ===== Fin Oferta (Johann) =====


# ===== Tienda (Martín) =====
class TiendaViewSet(viewsets.ModelViewSet):
    """ViewSet que provee el CRUD completo para Tienda."""
    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer
# ===== Fin Tienda (Martín) =====

# ===== Producto (Diego) =====
# Datos de ejemplo en memoria (todavía no hay modelos ni base de datos).
productos = [
    {'id': 1, 'nombre': 'Booster Pack Escarlata y Púrpura', 'expansion': 'Escarlata y Púrpura', 'tipo': 'sobre'},
    {'id': 2, 'nombre': 'Elite Trainer Box 151', 'expansion': '151', 'tipo': 'caja'},
    {'id': 3, 'nombre': 'Charizard ex', 'expansion': 'Llamas Obsidianas', 'tipo': 'carta'},
]


@api_view(['GET'])
def lista_productos(request):
    """Devuelve la lista completa de productos."""
    return Response(productos)


@api_view(['POST'])
def crear_producto(request):
    """Recibe un producto nuevo en request.data, le asigna un id y lo agrega a la lista."""
    nuevo_id = max((p['id'] for p in productos), default=0) + 1
    nuevo = {
        'id': nuevo_id,
        'nombre': request.data.get('nombre'),
        'expansion': request.data.get('expansion'),
        'tipo': request.data.get('tipo'),
    }
    productos.append(nuevo)
    return Response(nuevo, status=201)
# ===== Fin Producto (Diego) =====