export default function FormInput({ label, id, ...props }) {
  const genId = id || (label ? label.toLowerCase().replace(/\s+/g, '-') .replace(/[^a-z0-9-_]/g, '') : undefined)
  return (
    <label className="block text-sm" htmlFor={genId}>
      <div className="text-xs text-slate-600 dark:text-slate-300 mb-1">{label}</div>
      <input
        id={genId}
        className="w-full rounded-md border border-slate-200 bg-white px-3 py-2 text-sm shadow-sm placeholder:text-slate-400 focus:outline-none focus:ring-2 focus:ring-rose-400 dark:bg-slate-700 dark:border-slate-600 dark:text-slate-100"
        {...props}
      />
    </label>
  )
}
