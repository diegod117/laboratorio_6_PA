import { useState, useEffect } from 'react'
import { API_URL } from '../config'

// Muestra un precio en pesos chilenos: 40000 -> $40.000
function formatoPesos(valor) {
  return '$' + Number(valor).toLocaleString('es-CL')
}

// Para cada producto que se vende en 2 o más tiendas con stock,
// guarda el precio más bajo. Una oferta sin stock no compite.
function mejoresPrecios(ofertas) {
  const precios = {}
  ofertas
    .filter((oferta) => oferta.stock > 0)
    .forEach((oferta) => {
      if (!precios[oferta.producto]) precios[oferta.producto] = []
      precios[oferta.producto].push(oferta.precio)
    })

  const mejores = {}
  Object.keys(precios).forEach((producto) => {
    if (precios[producto].length >= 2) {
      mejores[producto] = Math.min(...precios[producto])
    }
  })
  return mejores
}

function ListaOfertas() {
  const [ofertas, setOfertas] = useState([])
  const [cargando, setCargando] = useState(true)
  const [error, setError] = useState(false)

  useEffect(() => {
    fetch(`${API_URL}ofertas/`)
      .then((res) => res.json())
      .then(setOfertas)
      .catch(() => setError(true))
      .finally(() => setCargando(false))
  }, [])

  // Ordenadas por producto y, dentro de cada producto, de la más barata a la más cara.
  const ordenadas = [...ofertas].sort(
    (a, b) => a.producto.localeCompare(b.producto) || a.precio - b.precio
  )
  const mejores = mejoresPrecios(ofertas)
  const cantidadProductos = new Set(ofertas.map((o) => o.producto)).size
  const cantidadTiendas = new Set(ofertas.map((o) => o.tienda)).size

  return (
    <section className="panel">
      <h2>Ofertas</h2>

      {cargando && <p className="estado">Cargando ofertas…</p>}

      {error && (
        <p className="estado">No se pudieron cargar las ofertas. Revisa que el backend esté funcionando.</p>
      )}

      {!cargando && !error && ofertas.length === 0 && (
        <p className="estado">Todavía no hay ofertas registradas.</p>
      )}

      {ofertas.length > 0 && (
        <>
          <p className="resumen">
            {ofertas.length} ofertas de {cantidadProductos} productos en {cantidadTiendas} tiendas
          </p>

          <table className="tabla-ofertas">
            <thead>
              <tr>
                <th>Producto</th>
                <th>Tienda</th>
                <th className="num">Precio</th>
                <th className="num">Stock</th>
              </tr>
            </thead>
            <tbody>
              {ordenadas.map((oferta) => {
                const esMejor = oferta.stock > 0 && mejores[oferta.producto] === oferta.precio
                return (
                  <tr key={oferta.id} className={oferta.stock === 0 ? 'sin-stock' : ''}>
                    <td className="producto">{oferta.producto}</td>
                    <td className="tienda">{oferta.tienda}</td>
                    <td className={esMejor ? 'num precio mejor' : 'num precio'}>
                      {esMejor && <span className="etiqueta">Mejor precio</span>}
                      {formatoPesos(oferta.precio)}
                    </td>
                    <td className={oferta.stock === 0 ? 'num stock agotado' : 'num stock'}>
                      {oferta.stock === 0 ? 'Sin stock' : `${oferta.stock} u.`}
                    </td>
                  </tr>
                )
              })}
            </tbody>
          </table>
        </>
      )}
    </section>
  )
}

export default ListaOfertas
