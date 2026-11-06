from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tienda
from .serializers import TiendaSerializer

# Create your views here.


# ===== Oferta (Johann) =====
ofertas = [
    {
        "id": 1,
        "producto": "Booster Box Escarlata y Púrpura 151",
        "tienda": "Pokemon Chile Store",
        "precio": 129990,
        "stock": 8,
    },
    {
        "id": 2,
        "producto": "Elite Trainer Box Fuerzas Temporales",
        "tienda": "Zona TCG",
        "precio": 54990,
        "stock": 15,
    },
    {
        "id": 3,
        "producto": "Charizard ex Obsidiana Llameante",
        "tienda": "Mundo Cartas Santiago",
        "precio": 24990,
        "stock": 0,
    },
]


@api_view(['GET'])
def lista_ofertas(request):
    return Response(ofertas)


@api_view(['POST'])
def crear_oferta(request):
    nuevo_id = max(oferta["id"] for oferta in ofertas) + 1
    nueva_oferta = {
        "id": nuevo_id,
        "producto": request.data["producto"],
        "tienda": request.data["tienda"],
        "precio": request.data["precio"],
        "stock": request.data["stock"],
    }
    ofertas.append(nueva_oferta)
    return Response(nueva_oferta, status=status.HTTP_201_CREATED)
# ===== Fin Oferta (Johann) =====


# ===== Tienda (Martín) =====
class TiendaList(APIView):
    """Lista todas las tiendas o crea una nueva tienda persistente."""
    def get(self, request):
        tiendas = Tienda.objects.all()
        serializer = TiendaSerializer(tiendas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TiendaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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