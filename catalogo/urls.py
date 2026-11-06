from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

# ===== Oferta (Johann) =====
router.register(r'ofertas', views.OfertaViewSet)
# ===== Fin Oferta (Johann) =====

urlpatterns = [
    # ===== Tienda (Martín) =====
    path('tiendas/', views.listar_tiendas, name='listar_tiendas'),
    path('tiendas/crear/', views.crear_tienda, name='crear_tienda'),
    # ===== Fin Tienda (Martín) =====

    # ===== Producto (Diego) =====
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    # ===== Fin Producto (Diego) =====

    path('', include(router.urls)),
]
