from rest_framework import serializers
from .models import Oferta, Tienda


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
