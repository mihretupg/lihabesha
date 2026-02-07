import { render, screen } from '@testing-library/react'
import Modal from '../components/Modal'
import userEvent from '@testing-library/user-event'

test('modal renders and close button works', async () => {
  const close = vi.fn()
  render(<Modal open={true} onClose={close}><div>Content</div></Modal>)
  expect(screen.getByRole('dialog')).toBeInTheDocument()
  const btn = screen.getByLabelText('Close')
  await userEvent.click(btn)
  expect(close).toHaveBeenCalled()
})
