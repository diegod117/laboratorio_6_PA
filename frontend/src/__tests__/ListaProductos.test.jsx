import { render, screen } from '@testing-library/react'
import ListaProductos from '../components/ListaProductos'

// config.js usa import.meta, que Jest no entiende: lo reemplazamos.
jest.mock('../config', () => ({ API_URL: 'http://test/api/' }))

test('ListaProductos muestra los productos que llegan de la API', async () => {
  global.fetch = jest.fn(() =>
    Promise.resolve({
      json: () =>
        Promise.resolve([
          { id: 1, nombre: 'Elite Trainer Box 151', expansion: '151', tipo: 'caja' },
          { id: 2, nombre: 'Charizard ex', expansion: 'Llamas Obsidianas', tipo: 'carta' },
        ]),
    })
  )

  render(<ListaProductos />)

  expect(await screen.findByText(/Elite Trainer Box 151/)).toBeInTheDocument()
  expect(await screen.findByText(/Charizard ex/)).toBeInTheDocument()
  expect(global.fetch).toHaveBeenCalledWith('http://test/api/productos/')
})
