import { useState } from 'react'
import { API_URL } from '../config'

// Datos de prueba: en el paso X1 se reemplazan por fetch a /api/tiendas/
const tiendasDePrueba = [
  { id: 1, nombre: 'Magic Sur Chile', ciudad: 'Santiago', sitio_web: 'https://magicsur.cl' },
  { id: 2, nombre: 'Weplay Store', ciudad: 'Viña del Mar', sitio_web: 'https://weplay.cl' },
]

function ListaTiendas() {
  const [tiendas] = useState(tiendasDePrueba)

  return (
    <div>
      <h2>Tiendas</h2>
      <p>Endpoint: {API_URL}tiendas/</p>
      <ul>
        {tiendas.map((tienda) => (
          <li key={tienda.id}>
            {tienda.nombre} ({tienda.ciudad}) - <a href={tienda.sitio_web}>{tienda.sitio_web}</a>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default ListaTiendas
