from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

# ===== Oferta (Johann) =====
router.register(r'ofertas', views.OfertaViewSet)
# ===== Fin Oferta (Johann) =====

router.register(r'tiendas', views.TiendaViewSet, basename='tienda')

urlpatterns = [
    # ===== Router compartido (Tienda y Oferta) =====
    path('', include(router.urls)),
    # ===== Fin Router compartido =====

    # ===== Producto (Diego) =====
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    # ===== Fin Producto (Diego) =====
]
