export default function Modal({ open, onClose, children }) {
  if (!open) return null

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center">
      <div className="absolute inset-0 bg-black/40" onClick={onClose} />
      <div className="relative w-full max-w-lg rounded-lg bg-white p-6 shadow-lg dark:bg-slate-800">
        <button className="absolute right-3 top-3 text-slate-500" onClick={onClose} aria-label="Close">✕</button>
        {children}
      </div>
    </div>
  )
}
