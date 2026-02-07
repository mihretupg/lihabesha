import { render, screen } from '@testing-library/react'
import FormInput from '../components/FormInput'

test('renders label and associates input id', () => {
  render(<FormInput label="Email Address" />)
  const label = screen.getByText('Email Address')
  expect(label).toBeInTheDocument()
  const input = screen.getByRole('textbox')
  expect(input).toHaveAttribute('id')
  // label should be associated via htmlFor
  expect(label.closest('label')).toContainElement(input)
})
