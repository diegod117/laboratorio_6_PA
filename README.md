# PokeTodoCL

Plataforma que compara precios y stock de productos de Pokémon TCG en tiendas chilenas.
Proyecto del Laboratorio 6 de Programación de Aplicaciones (Django REST Framework).

## Recursos

| Recurso  | Campos                                   | Responsable |
|----------|------------------------------------------|-------------|
| Tienda   | id, nombre, ciudad, sitio_web            | Martin      |
| Producto | id, nombre, expansion, tipo              | Diego       |
| Oferta   | id, producto, tienda, precio, stock      | Johann      |

## Despliegue

| Parte | URL pública |
|-------|-------------|
| Frontend (Vercel) | https://laboratorio-6-pa.vercel.app |
| Backend (Render) | https://poketodocl-backend.onrender.com |
| API | https://poketodocl-backend.onrender.com/api/ |
| Admin de Django | https://poketodocl-backend.onrender.com/admin/ |

Endpoints de la API:

- https://poketodocl-backend.onrender.com/api/ofertas/
- https://poketodocl-backend.onrender.com/api/tiendas/
- https://poketodocl-backend.onrender.com/api/productos/

Si el backend está en el plan gratuito de Render, se duerme cuando pasa un
rato sin visitas, y la primera petición puede tardar cerca de un minuto.

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

## Frontend (React + Vite)

El frontend está en la carpeta `frontend/` y consume la API del backend.

### Correr el frontend en local

Con el backend corriendo en otra terminal (`python manage.py runserver`):

```bash
cd frontend
npm install

# Crear el archivo .env a partir del ejemplo
cp .env.example .env        # en Windows (PowerShell): copy .env.example .env

npm run dev
```

El frontend queda en http://localhost:5173/

El archivo `.env` define la URL de la API (debe terminar en `/`):

```
VITE_API_URL=http://localhost:8000/api/
```

### Correr las pruebas del frontend

```bash
cd frontend
npm test
```

### Desplegar el frontend en Vercel

1. Entrar a https://vercel.com con la cuenta de GitHub y elegir **Add New → Project**.
2. Importar este repositorio.
3. En **Root Directory** elegir `frontend`.
4. En **Framework Preset** dejar `Vite` (build `npm run build`, salida `dist`).
5. En **Environment Variables** agregar:
   - `VITE_API_URL` = `https://poketodocl-backend.onrender.com/api/`
6. Presionar **Deploy**. Vercel entrega una URL del tipo `https://<proyecto>.vercel.app`.
7. En Render, en el servicio del backend, agregar esa URL a la variable
   `CORS_ALLOWED_ORIGINS` (sin `/` al final) y volver a desplegar el backend.
   Si no se hace, el navegador bloquea las peticiones por CORS.

Cada vez que se cambia `VITE_API_URL` en Vercel hay que hacer **Redeploy**,
porque Vite pone la variable dentro del código al momento del build.
