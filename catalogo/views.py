from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


# ===== Oferta (Johann) =====
ofertas = [
    {
        "id": 1,
        "producto": "Booster Box Escarlata y Púrpura 151",
        "tienda": "Pokemon Chile Store",
        "precio": 129990,
        "stock": 8,
    },
    {
        "id": 2,
        "producto": "Elite Trainer Box Fuerzas Temporales",
        "tienda": "Zona TCG",
        "precio": 54990,
        "stock": 15,
    },
    {
        "id": 3,
        "producto": "Charizard ex Obsidiana Llameante",
        "tienda": "Mundo Cartas Santiago",
        "precio": 24990,
        "stock": 0,
    },
]
# ===== Fin Oferta (Johann) =====
