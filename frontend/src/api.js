const BASE = import.meta.env.VITE_API_URL ?? 'http://localhost:8000/api'

export async function listHousing({ city, limit = 20, offset = 0 } = {}) {
  const params = new URLSearchParams()
  if (city) params.append('city', city)
  params.append('limit', String(limit))
  params.append('offset', String(offset))
  const res = await fetch(`${BASE}/housing/?${params.toString()}`)
  if (!res.ok) throw new Error(`Failed to fetch listings: ${res.status}`)
  return res.json()
}

export async function createHousing(payload, token) {
  const res = await fetch(`${BASE}/housing/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify(payload),
  })
  if (!res.ok) {
    const text = await res.text()
    throw new Error(`Create failed: ${res.status} ${text}`)
  }
  return res.json()
}
