from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from .models import Oferta
from .serializers import OfertaSerializer
# Create your views here.


# ===== Oferta (Johann) =====
class OfertaList(APIView):
    def get(self, request):
        ofertas = Oferta.objects.all()
        serializer = OfertaSerializer(ofertas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OfertaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ===== Fin Oferta (Johann) =====

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
# Datos de ejemplo para el recurso Tienda (Paso 2)
tiendas = [
    {
        "id": 1,
        "nombre": "Magic Sur Chile",
        "ciudad": "Santiago",
        "sitio_web": "https://magicsur.cl"
    },
    {
        "id": 2,
        "nombre": "Weplay Store",
        "ciudad": "Viña del Mar",
        "sitio_web": "https://weplay.cl"
    },
    {
        "id": 3,
        "nombre": "Sniper Games",
        "ciudad": "Concepción",
        "sitio_web": "https://snipergames.cl"
    }
]


@api_view(['GET'])
def listar_tiendas(request):
    """Devuelve la lista completa de tiendas."""
    return Response(tiendas)


@api_view(['POST'])
def crear_tienda(request):
    """Recibe los datos del nuevo registro desde request.data, le asigna un id, lo agrega a la lista y responde con status 201."""
    nuevo_id = max([t['id'] for t in tiendas], default=0) + 1
    nueva_tienda = {
        'id': nuevo_id,
        'nombre': request.data.get('nombre'),
        'ciudad': request.data.get('ciudad'),
        'sitio_web': request.data.get('sitio_web'),
    }
    tiendas.append(nueva_tienda)
    return Response(nueva_tienda, status=status.HTTP_201_CREATED)
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