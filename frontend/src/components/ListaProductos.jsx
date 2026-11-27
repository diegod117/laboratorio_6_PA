import { useState } from 'react'
import { API_URL } from '../config'

// Datos de prueba: en el paso X1 se reemplazan por fetch a /api/productos/
const productosDePrueba = [
  { id: 1, nombre: 'Elite Trainer Box 151', expansion: '151', tipo: 'caja' },
  { id: 2, nombre: 'Charizard ex', expansion: 'Llamas Obsidianas', tipo: 'carta' },
]

function ListaProductos() {
  const [productos] = useState(productosDePrueba)

  return (
    <div>
      <h2>Productos</h2>
      <p>Endpoint: {API_URL}productos/</p>
      <ul>
        {productos.map((producto) => (
          <li key={producto.id}>
            {producto.nombre} - {producto.expansion} ({producto.tipo})
          </li>
        ))}
      </ul>
    </div>
  )
}

export default ListaProductos
