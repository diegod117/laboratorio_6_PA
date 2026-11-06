from django.contrib import admin
from .models import Oferta, Producto, Tienda

# Register your models here.

# ===== Oferta (Johann) =====
admin.site.register(Oferta)
# ===== Fin Oferta (Johann) =====

admin.site.register(Tienda)

# ===== Producto (Diego) =====
admin.site.register(Producto)
# ===== Fin Producto (Diego) =====
