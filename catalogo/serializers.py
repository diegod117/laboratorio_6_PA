from rest_framework import serializers

from .models import Producto


# ===== Producto (Diego) =====
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'expansion', 'tipo']
# ===== Fin Producto (Diego) =====

