from django.contrib import admin
from .models import Oferta, Tienda

# Register your models here.

# ===== Oferta (Johann) =====
admin.site.register(Oferta)
# ===== Fin Oferta (Johann) =====

admin.site.register(Tienda)
