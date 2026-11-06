from rest_framework import serializers
from .models import Oferta


# ===== Oferta (Johann) =====
class OfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oferta
        fields = ['id', 'producto', 'tienda', 'precio', 'stock']
# ===== Fin Oferta (Johann) =====