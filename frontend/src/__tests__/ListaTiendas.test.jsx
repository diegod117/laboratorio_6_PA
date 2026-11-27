import { render, screen } from '@testing-library/react'
import ListaTiendas from '../components/ListaTiendas'

jest.mock('../config', () => ({ API_URL: 'http://test/api/' }))

global.fetch = jest.fn(() =>
  Promise.resolve({
    json: () =>
      Promise.resolve([
        { id: 1, nombre: 'Magic Sur Chile', ciudad: 'Santiago', sitio_web: 'https://magicsur.cl' },
        { id: 2, nombre: 'Weplay Store', ciudad: 'Viña del Mar', sitio_web: 'https://weplay.cl' },
      ]),
  })
)

test('ListaTiendas muestra las tiendas traídas desde la API', async () => {
  render(<ListaTiendas />)

  expect(await screen.findByText(/Magic Sur Chile/)).toBeInTheDocument()
  expect(await screen.findByText(/Weplay Store/)).toBeInTheDocument()
})
