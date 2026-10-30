# PokeTodoCL

Plataforma que compara precios y stock de productos de Pokémon TCG en tiendas chilenas.
Proyecto del Laboratorio 6 de Programación de Aplicaciones (Django REST Framework).

## Recursos

| Recurso  | Campos                                   | Responsable |
|----------|------------------------------------------|-------------|
| Tienda   | id, nombre, ciudad, sitio_web            | Martin      |
| Producto | id, nombre, expansion, tipo              | Diego       |
| Oferta   | id, producto, tienda, precio, stock      | Johann      |

## Cómo correr el proyecto

### Clonar el repositorio (macOS y Windows)

```bash
git clone <url-del-repositorio>
cd <carpeta-del-repositorio>
```

### macOS

```bash
# Crear y activar el entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Correr el servidor
python manage.py runserver
```

### Windows (PowerShell)

```powershell
# Crear y activar el entorno virtual
python -m venv venv
venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt

# Correr el servidor
python manage.py runserver
```

Si PowerShell bloquea la activación del venv, ejecuta una vez:
`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.
En CMD (Símbolo del sistema) se activa con `venv\Scripts\activate.bat`.

El servidor queda en http://127.0.0.1:8000/
