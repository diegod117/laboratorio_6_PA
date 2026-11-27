import { useState } from 'react'

// Datos de prueba: en el paso X1 se reemplazan por fetch a /api/ofertas/
const ofertasDePrueba = [
  { id: 1, producto: 'Booster Box 151', tienda: 'Weplay Store', precio: 40000, stock: 10 },
  { id: 2, producto: 'Charizard ex', tienda: 'Sniper Games', precio: 10000, stock: 30 },
]

function ListaOfertas() {
  const [ofertas] = useState(ofertasDePrueba)

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
