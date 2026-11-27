import { useState, useEffect } from 'react'
import { API_URL } from '../config'

function ListaOfertas() {
  const [ofertas, setOfertas] = useState([])

  useEffect(() => {
    fetch(`${API_URL}ofertas/`)
      .then((res) => res.json())
      .then(setOfertas)
  }, [])

  return (
    <div>
      <h2>Ofertas</h2>
      <ul>
        {ofertas.map((oferta) => (
          <li key={oferta.id}>
            {oferta.producto} en {oferta.tienda}: ${oferta.precio} (stock: {oferta.stock})
          </li>
        ))}
      </ul>
    </div>
  )
}

export default ListaOfertas
