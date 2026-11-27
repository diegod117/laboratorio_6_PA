import { render, screen } from '@testing-library/react'
import App from '../App'

// config.js usa import.meta, que Jest no entiende: lo reemplazamos.
jest.mock('../config', () => ({ API_URL: 'http://test/api/' }))

// La lista que se muestra al inicio (Ofertas) hace fetch: devolvemos una lista vacía.
global.fetch = jest.fn(() => Promise.resolve({ json: () => Promise.resolve([]) }))

test('App muestra el título y los tres botones', async () => {
  render(<App />)

  expect(screen.getByText('PokeTodoCL')).toBeInTheDocument()
  expect(screen.getByRole('button', { name: 'Ofertas' })).toBeInTheDocument()
  expect(screen.getByRole('button', { name: 'Tiendas' })).toBeInTheDocument()
  expect(screen.getByRole('button', { name: 'Productos' })).toBeInTheDocument()
  expect(await screen.findByText('Ofertas', { selector: 'h2' })).toBeInTheDocument()
})
