from django.shortcuts import render
from rest_framework import status
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


@api_view(['GET'])
def lista_ofertas(request):
    return Response(ofertas)


@api_view(['POST'])
def crear_oferta(request):
    nuevo_id = max(oferta["id"] for oferta in ofertas) + 1
    nueva_oferta = {
        "id": nuevo_id,
        "producto": request.data["producto"],
        "tienda": request.data["tienda"],
        "precio": request.data["precio"],
        "stock": request.data["stock"],
    }
    ofertas.append(nueva_oferta)
    return Response(nueva_oferta, status=status.HTTP_201_CREATED)
# ===== Fin Oferta (Johann) =====
