from django.urls import path
from . import views

urlpatterns = [
    # ===== Oferta (Johann) =====
    path('ofertas/', views.lista_ofertas),
    path('ofertas/crear/', views.crear_oferta),
    # ===== Fin Oferta (Johann) =====

    # ===== Tienda (Martín) =====
    path('tiendas/', views.TiendaList.as_view(), name='tienda_list'),
    # ===== Fin Tienda (Martín) =====

    # ===== Producto (Diego) =====
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    # ===== Fin Producto (Diego) =====
]