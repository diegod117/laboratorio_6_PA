from rest_framework import serializers
from .models import Oferta, Producto, Tienda


# ===== Oferta (Johann) =====
class OfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oferta
        fields = ['id', 'producto', 'tienda', 'precio', 'stock']
# ===== Fin Oferta (Johann) =====


class TiendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tienda
        fields = '__all__'


# ===== Producto (Diego) =====
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'expansion', 'tipo']
# ===== Fin Producto (Diego) =====
