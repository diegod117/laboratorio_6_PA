from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Oferta, Tienda
from .serializers import OfertaSerializer, TiendaSerializer

from .models import Producto
from .serializers import ProductoSerializer

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
class ProductoViewSet(viewsets.ModelViewSet):
    """CRUD completo de Producto (list, create, retrieve, update, destroy)."""
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
# ===== Fin Producto (Diego) =====