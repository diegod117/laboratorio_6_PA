from django.urls import path
from . import views

urlpatterns = [
    # ===== Oferta (Johann) =====
    path('ofertas/', views.lista_ofertas),
    path('ofertas/crear/', views.crear_oferta),
    # ===== Fin Oferta (Johann) =====
]
