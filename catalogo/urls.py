from django.urls import path
from . import views

urlpatterns = [
    path('tiendas/', views.listar_tiendas, name='listar_tiendas'),
    path('tiendas/crear/', views.crear_tienda, name='crear_tienda'),
]
