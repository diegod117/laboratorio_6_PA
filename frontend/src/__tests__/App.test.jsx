import { render, screen } from '@testing-library/react'
import App from '../App'

// config.js usa import.meta, que Jest no entiende: lo reemplazamos.
jest.mock('../config', () => ({ API_URL: 'http://test/api/' }))

test('App muestra el título y los tres botones', () => {
  render(<App />)

  expect(screen.getByText('PokeTodoCL')).toBeInTheDocument()
  expect(screen.getByRole('button', { name: 'Ofertas' })).toBeInTheDocument()
  expect(screen.getByRole('button', { name: 'Tiendas' })).toBeInTheDocument()
  expect(screen.getByRole('button', { name: 'Productos' })).toBeInTheDocument()
})
