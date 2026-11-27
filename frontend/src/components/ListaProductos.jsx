import { useState, useEffect } from 'react'
import { API_URL } from '../config'

function ListaProductos() {
  const [productos, setProductos] = useState([])

  // Al cargar el componente se piden los productos a la API
  useEffect(() => {
    fetch(`${API_URL}productos/`)
      .then((res) => res.json())
      .then(setProductos)
  }, [])

  return (
    <div>
      <h2>Productos</h2>
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
