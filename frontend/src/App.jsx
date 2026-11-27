import { useState } from 'react'
import ListaOfertas from './components/ListaOfertas'
import ListaTiendas from './components/ListaTiendas'
import ListaProductos from './components/ListaProductos'

function App() {
  const [lista, setLista] = useState('ofertas')

  return (
    <div className="app">
      <header className="barra">
        <h1>PokeTodoCL</h1>
        <p className="lema">Precios y stock de Pokémon TCG en tiendas chilenas</p>
      </header>

      <nav className="pestanas">
        <button aria-pressed={lista === 'ofertas'} onClick={() => setLista('ofertas')}>Ofertas</button>
        <button aria-pressed={lista === 'tiendas'} onClick={() => setLista('tiendas')}>Tiendas</button>
        <button aria-pressed={lista === 'productos'} onClick={() => setLista('productos')}>Productos</button>
      </nav>

      <main>
        {lista === 'ofertas' && <ListaOfertas />}
        {lista === 'tiendas' && <ListaTiendas />}
        {lista === 'productos' && <ListaProductos />}
      </main>
    </div>
  )
}

export default App
