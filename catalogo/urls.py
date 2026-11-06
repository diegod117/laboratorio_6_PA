from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

# Router compartido por el grupo: cada integrante registra su ViewSet
# con un prefijo de URL distinto para que no choquen las rutas.
router = DefaultRouter()
# ===== Producto (Diego) =====
router.register(r'productos', views.ProductoViewSet, basename='producto')
# ===== Fin Producto (Diego) =====

urlpatterns = [
    # ===== Oferta (Johann) =====
    path('ofertas/', views.lista_ofertas),
    path('ofertas/crear/', views.crear_oferta),
    # ===== Fin Oferta (Johann) =====

    # ===== Tienda (Martín) =====
    path('tiendas/', views.listar_tiendas, name='listar_tiendas'),
    path('tiendas/crear/', views.crear_tienda, name='crear_tienda'),
    # ===== Fin Tienda (Martín) =====

    # Rutas generadas por el router (productos/, productos/<pk>/ y la raíz api/)
    path('', include(router.urls)),
]
