from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tiendas', views.TiendaViewSet, basename='tienda')

urlpatterns = [
    # ===== Router Tienda (Martín) =====
    path('', include(router.urls)),
    # ===== Fin Router Tienda (Martín) =====

    # ===== Oferta (Johann) =====
    path('ofertas/', views.lista_ofertas),
    path('ofertas/crear/', views.crear_oferta),
    # ===== Fin Oferta (Johann) =====

    # ===== Producto (Diego) =====
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    # ===== Fin Producto (Diego) =====
]