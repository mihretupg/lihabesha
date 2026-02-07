import { useEffect, useRef } from 'react'

export default function Modal({ open, onClose, children }) {
  const dialogRef = useRef(null)
  if (!open) return null

  useEffect(() => {
    const prevOverflow = document.body.style.overflow
    document.body.style.overflow = 'hidden'
    // focus first focusable element inside dialog
    const el = dialogRef.current
    const focusable = el?.querySelector('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])')
    // put focus on the dialog itself if no focusable found
    if (focusable) focusable.focus()
    else el?.setAttribute('tabindex', '-1') && el?.focus()
    return () => { document.body.style.overflow = prevOverflow }
  }, [])

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center">
      <div className="absolute inset-0 bg-black/40" onClick={onClose} />
      <div role="dialog" aria-modal="true" ref={dialogRef} className="relative w-full max-w-lg rounded-lg bg-white p-6 shadow-lg dark:bg-slate-800">
        <button className="absolute right-3 top-3 text-slate-500" onClick={onClose} aria-label="Close">✕</button>
        {children}
      </div>
    </div>
  )
}
