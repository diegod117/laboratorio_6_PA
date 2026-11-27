# Laboratorio 8 — PokeTodoCL Full Stack (grupo Mish)

Repo: backend Django en la raíz (`poketodocl/`, app `catalogo/`) + frontend React (Vite) en `frontend/`.
Integrantes y recursos: **Johann → Oferta**, **Martín → Tienda**, **Diego → Producto**.

## Reglas de trabajo
- Código simple, nivel estudiante de pregrado. JavaScript (no TypeScript), sin librerías extra que no se pidan.
- **Un commit por paso**, con el mensaje exacto del plan. No mezclar pasos. No hacer push (lo hace la persona).
- Cada persona solo toca **sus** archivos (ver tabla) para evitar conflictos.
- Mantener los marcadores de sección existentes: `# ===== Oferta (Johann) =====` … `# ===== Fin ... =====`.
- Antes de commitear: `python manage.py test` y/o `cd frontend && npm test` deben pasar.

## Archivos por persona
| Persona | Backend | Frontend |
|---|---|---|
| Johann | `catalogo/tests/test_oferta.py` | `src/components/ListaOfertas.jsx`, `src/__tests__/ListaOfertas.test.jsx` |
| Martín | `catalogo/tests/test_tienda.py` | `src/components/ListaTiendas.jsx`, `src/__tests__/ListaTiendas.test.jsx` |
| Diego  | `catalogo/tests/test_producto.py` | `src/components/ListaProductos.jsx`, `src/__tests__/ListaProductos.test.jsx` |

## Endpoints (DRF DefaultRouter, ya existen)
`/api/ofertas/` (id, producto, tienda, precio, stock) · `/api/tiendas/` (id, nombre, ciudad, sitio_web) · `/api/productos/` (id, nombre, expansion, tipo: sobre|caja|carta)

## Decisiones técnicas (ya probadas, respetarlas)
**CORS:** `django-cors-headers`; `'corsheaders'` en INSTALLED_APPS; `corsheaders.middleware.CorsMiddleware` arriba de `CommonMiddleware`.
`CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS', 'http://localhost:5173').split(',')`

**URL de la API:** `frontend/.env` con `VITE_API_URL=http://localhost:8000/api/` (termina en `/`). `.env` va en `frontend/.gitignore`; se commitea `frontend/.env.example`.
Se lee SOLO en `src/config.js`: `export const API_URL = import.meta.env.VITE_API_URL;` (los componentes importan `API_URL` de ahí; así Jest puede mockearlo).

**Componentes de listado:** `useState([])` + `useEffect` con `fetch(\`${API_URL}ofertas/\`).then(res => res.json()).then(setX)`. Mostrar un `<ul>` simple. `App.jsx` cambia de lista con botones y `useState` (sin react-router).

**Jest (no Vitest):** devDeps `jest jest-environment-jsdom babel-jest @babel/preset-env @babel/preset-react @testing-library/react @testing-library/dom @testing-library/jest-dom`.
Como `package.json` tiene `"type": "module"`, los configs van en `.cjs`:
- `babel.config.cjs`: presets `['@babel/preset-env', { targets: { node: 'current' } }]` y `['@babel/preset-react', { runtime: 'automatic' }]`
- `jest.config.cjs`: `testEnvironment: 'jsdom'`, `setupFilesAfterEnv: ['@testing-library/jest-dom']`, `moduleNameMapper: { '\\.(css)$': '<rootDir>/src/__mocks__/styleMock.js' }`
- script `"test": "jest"`
Patrón de prueba: `jest.mock('../config', () => ({ API_URL: 'http://test/api/' }))`, `global.fetch = jest.fn(() => Promise.resolve({ json: () => Promise.resolve([...]) }))`, `render(<Lista />)` y `expect(await screen.findByText(/texto/)).toBeInTheDocument()`.

**Pruebas backend:** carpeta `catalogo/tests/` (con `__init__.py`, se borra `catalogo/tests.py`), un archivo por recurso. `TestCase` + `APIClient`: crear registros en `setUp`, GET al endpoint, `assertEqual(status_code, 200)` y cantidad de registros.

**Producción (Render):** settings leen `SECRET_KEY`, `DEBUG` (`os.environ.get('DEBUG', 'True') == 'True'`), `ALLOWED_HOSTS` (lista separada por coma, default `localhost,127.0.0.1`) y `CORS_ALLOWED_ORIGINS` desde variables de entorno. `whitenoise` (middleware justo después de SecurityMiddleware) + `STATIC_ROOT = BASE_DIR / 'staticfiles'`. `gunicorn` en requirements.txt.
`build.sh` (ejecutable): `pip install -r requirements.txt`, `collectstatic --noinput`, `migrate`, `loaddata datos_ejemplo`, `createsuperuser --noinput || true`.
Start command: `gunicorn poketodocl.wsgi:application`. La BD es SQLite: en Render se reinicia en cada deploy, por eso se cargan los datos con la fixture `catalogo/fixtures/datos_ejemplo.json`.

**Frontend (Vercel):** Root Directory `frontend`, preset Vite, variable `VITE_API_URL=https://<backend>.onrender.com/api/`.

## Plan de commits (orden)
**Fase 0 — Johann, en `main` (base para todos)**
- J1 `Agrego django-cors-headers y habilito CORS para el frontend en localhost:5173`
- J2 `Creo el frontend React con Vite y las tres pantallas de listado con datos de prueba`
- J3 `Agrego la variable de entorno VITE_API_URL y config.js para la URL de la API`
- J4 `Configuro Jest y React Testing Library en el frontend`
- J5 `Separo las pruebas del backend en la carpeta catalogo/tests`

**Fase 1 — cada uno en su rama `lab8-<nombre>` (X = su recurso), luego PR**
- X1 `Conecto la pantalla de <X> al endpoint real con fetch, reemplazando los datos de prueba`
- X2 `Agrego una prueba con TestCase para el endpoint de <X>`
- X3 `Agrego una prueba con Jest y React Testing Library para el listado de <X>`

**Fase 2 — despliegue**
- D1 (Diego) `Agrego una fixture con datos de ejemplo para producción`
- M1 (Martín) `Leo SECRET_KEY, DEBUG, ALLOWED_HOSTS y CORS desde variables de entorno`
- M2 (Martín) `Agrego gunicorn, whitenoise y build.sh para desplegar el backend en Render`
- D2 (Diego) `Documento en el README cómo correr y desplegar el frontend en Vercel`
- J6 (Johann) `Agrego al README las URLs públicas del backend y frontend desplegados`
