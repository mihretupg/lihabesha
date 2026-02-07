export default function Card({ title, subtitle, children }) {
  return (
    <div className="rounded-lg border border-slate-200 bg-white p-4 shadow-sm dark:bg-slate-800 dark:border-slate-700">
      <div className="text-sm font-semibold text-slate-500 dark:text-slate-300">{title}</div>
      <div className="mt-1 text-sm text-slate-700 dark:text-slate-200">{subtitle}</div>
      {children && <div className="mt-3 text-sm text-slate-600 dark:text-slate-300">{children}</div>}
    </div>
  )
}
