import { useState } from 'react'
import FormInput from './FormInput'

export default function PostForm({ onSubmit }) {
  const [title, setTitle] = useState('')
  const [location, setLocation] = useState('')
  const [price, setPrice] = useState('')

  function handleSubmit(e) {
    e.preventDefault()
    onSubmit?.({ title, location, price })
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <FormInput label="Title" value={title} onChange={e => setTitle(e.target.value)} placeholder="e.g. Room near downtown" />
      <FormInput label="Location" value={location} onChange={e => setLocation(e.target.value)} placeholder="City or neighborhood" />
      <FormInput label="Price" value={price} onChange={e => setPrice(e.target.value)} placeholder="USD / month" />

      <div className="flex items-center gap-2">
        <button type="submit" className="rounded-md bg-emerald-500 px-4 py-2 text-sm font-medium text-white hover:bg-emerald-600">Post</button>
        <button type="button" className="rounded-md border border-slate-300 px-3 py-2 text-sm text-slate-700 hover:bg-slate-100">Cancel</button>
      </div>
    </form>
  )
}
