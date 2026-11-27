import { render, screen } from '@testing-library/react'
import ListaOfertas from '../components/ListaOfertas'

// config.js usa import.meta, que Jest no entiende: lo reemplazamos.
jest.mock('../config', () => ({ API_URL: 'http://test/api/' }))

test('ListaOfertas muestra las ofertas que entrega la API', async () => {
  global.fetch = jest.fn(() =>
    Promise.resolve({
      json: () =>
        Promise.resolve([
          { id: 1, producto: 'Booster Box 151', tienda: 'Weplay Store', precio: 40000, stock: 10 },
          { id: 2, producto: 'Charizard ex', tienda: 'Sniper Games', precio: 10000, stock: 30 },
        ]),
    })
  )

  render(<ListaOfertas />)

  expect(await screen.findByText(/Booster Box 151/)).toBeInTheDocument()
  expect(screen.getByText(/Charizard ex/)).toBeInTheDocument()
  expect(global.fetch).toHaveBeenCalledWith('http://test/api/ofertas/')
})

test('ListaOfertas marca el mejor precio solo entre las ofertas con stock', async () => {
  global.fetch = jest.fn(() =>
    Promise.resolve({
      json: () =>
        Promise.resolve([
          { id: 1, producto: 'Charizard ex', tienda: 'Weplay Store', precio: 20000, stock: 0 },
          { id: 2, producto: 'Charizard ex', tienda: 'Sniper Games', precio: 24990, stock: 2 },
          { id: 3, producto: 'Charizard ex', tienda: 'Magic Sur Chile', precio: 27990, stock: 5 },
        ]),
    })
  )

  render(<ListaOfertas />)

  const mejor = await screen.findByText('Mejor precio')
  expect(mejor.closest('tr')).toHaveTextContent('Sniper Games')
  expect(screen.getAllByText('Mejor precio')).toHaveLength(1)
  expect(screen.getByText('$24.990')).toBeInTheDocument()
  expect(screen.getByText('Sin stock')).toBeInTheDocument()
})
