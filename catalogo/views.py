from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Datos de ejemplo para el recurso Tienda (Paso 2)
tiendas = [
    {
        "id": 1,
        "nombre": "Magic Sur Chile",
        "ciudad": "Santiago",
        "sitio_web": "https://magicsur.cl"
    },
    {
        "id": 2,
        "nombre": "Weplay Store",
        "ciudad": "Viña del Mar",
        "sitio_web": "https://weplay.cl"
    },
    {
        "id": 3,
        "nombre": "Sniper Games",
        "ciudad": "Concepción",
        "sitio_web": "https://snipergames.cl"
    }
]


@api_view(['GET'])
def listar_tiendas(request):
    """Devuelve la lista completa de tiendas."""
    return Response(tiendas)

