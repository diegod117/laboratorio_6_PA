from django.urls import path
from . import views

urlpatterns = [
    # ===== Oferta (Johann) =====
    path('ofertas/', views.lista_ofertas),
    path('ofertas/crear/', views.crear_oferta),
    # ===== Fin Oferta (Johann) =====

    # ===== Tienda (Martín) =====
    path('tiendas/', views.listar_tiendas, name='listar_tiendas'),
    path('tiendas/crear/', views.crear_tienda, name='crear_tienda'),
    # ===== Fin Tienda (Martín) =====
]