# PokeTodoCL

Plataforma que compara precios y stock de productos de Pokémon TCG en tiendas chilenas.
Proyecto del Laboratorio 6 de Programación de Aplicaciones (Django REST Framework).

## Recursos

| Recurso  | Campos                                   | Responsable |
|----------|------------------------------------------|-------------|
| Tienda   | id, nombre, ciudad, sitio_web            | por asignar |
| Producto | id, nombre, expansion, tipo              | por asignar |
| Oferta   | id, producto, tienda, precio, stock      | por asignar |

## Cómo correr el proyecto (macOS)

```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd <carpeta-del-repositorio>

# Crear y activar el entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Correr el servidor
python manage.py runserver
```

El servidor queda en http://127.0.0.1:8000/
