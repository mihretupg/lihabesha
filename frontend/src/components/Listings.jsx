import { useEffect, useState } from 'react'
import Card from './Card'
import { listHousing } from '../api'

export default function Listings() {
  const [items, setItems] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    let mounted = true
    setLoading(true)
    listHousing()
      .then(data => { if (mounted) setItems(data) })
      .catch(e => { if (mounted) setError(e.message) })
      .finally(() => { if (mounted) setLoading(false) })
    return () => { mounted = false }
  }, [])

  return (
    <section className="mt-8">
      <h3 className="text-xl font-semibold">Latest Listings</h3>
      {loading && <div className="mt-4 text-sm text-slate-500">Loading...</div>}
      {error && <div className="mt-4 text-sm text-rose-500">{error}</div>}
      <div className="mt-4 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {items.map(item => (
          <Card key={item.id} title={item.title} subtitle={`${item.city ?? ''} — ${item.price ?? ''}`}>
            <div className="mt-2 flex items-center justify-between">
              <div className="text-xs text-slate-500 dark:text-slate-300">{new Date(item.created_at).toLocaleDateString?.() ?? ''}</div>
              <button className="rounded-md bg-slate-900 px-3 py-1 text-xs font-medium text-white hover:bg-slate-800">View</button>
            </div>
          </Card>
        ))}
      </div>
    </section>
  )
}
