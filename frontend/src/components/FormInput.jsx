export default function FormInput({ label, ...props }) {
  return (
    <label className="block text-sm">
      <div className="text-xs text-slate-600 dark:text-slate-300 mb-1">{label}</div>
      <input
        className="w-full rounded-md border border-slate-200 bg-white px-3 py-2 text-sm shadow-sm placeholder:text-slate-400 focus:outline-none focus:ring-2 focus:ring-rose-400 dark:bg-slate-700 dark:border-slate-600 dark:text-slate-100"
        {...props}
      />
    </label>
  )
}
