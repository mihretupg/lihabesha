import { render, screen, waitFor } from '@testing-library/react'
import Listings from '../components/Listings'

const fake = [{ id: 1, title: 'One', city: 'City', price: '100', created_at: new Date().toISOString() }]

beforeEach(() => {
  global.fetch = vi.fn(() => Promise.resolve({ ok: true, json: () => Promise.resolve(fake) }))
})

test('fetches and displays listings', async () => {
  render(<Listings />)
  await waitFor(() => expect(global.fetch).toHaveBeenCalled())
  expect(screen.getByText('Latest Listings')).toBeInTheDocument()
  expect(screen.getByText('One')).toBeInTheDocument()
})
