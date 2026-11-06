from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

# ===== Oferta (Johann) =====
router.register(r'ofertas', views.OfertaViewSet)
# ===== Fin Oferta (Johann) =====

router.register(r'tiendas', views.TiendaViewSet, basename='tienda')

# ===== Producto (Diego) =====
router.register(r'productos', views.ProductoViewSet, basename='producto')
# ===== Fin Producto (Diego) =====

urlpatterns = [
    # ===== Router compartido (Tienda, Oferta y Producto) =====
    path('', include(router.urls)),
    # ===== Fin Router compartido =====
]
