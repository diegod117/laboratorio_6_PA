import { useState, useEffect } from 'react'
import { API_URL } from '../config'

function ListaTiendas() {
  const [tiendas, setTiendas] = useState([])

  useEffect(() => {
    fetch(`${API_URL}tiendas/`)
      .then((res) => res.json())
      .then(setTiendas)
  }, [])

  return (
    <div>
      <h2>Tiendas</h2>
      <ul>
        {tiendas.map((tienda) => (
          <li key={tienda.id}>
            {tienda.nombre} ({tienda.ciudad}) -{' '}
            <a href={tienda.sitio_web}>{tienda.sitio_web}</a>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default ListaTiendas
