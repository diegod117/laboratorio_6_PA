import { useState } from 'react'
import ListaOfertas from './components/ListaOfertas'
import ListaTiendas from './components/ListaTiendas'
import ListaProductos from './components/ListaProductos'

function App() {
  const [lista, setLista] = useState('ofertas')

  return (
    <div>
      <h1>PokeTodoCL</h1>

      <button onClick={() => setLista('ofertas')}>Ofertas</button>
      <button onClick={() => setLista('tiendas')}>Tiendas</button>
      <button onClick={() => setLista('productos')}>Productos</button>

      {lista === 'ofertas' && <ListaOfertas />}
      {lista === 'tiendas' && <ListaTiendas />}
      {lista === 'productos' && <ListaProductos />}
    </div>
  )
}

export default App
