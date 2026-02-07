import { useState, useEffect } from 'react'

export default function Header() {
  const [open, setOpen] = useState(false)
  const [dark, setDark] = useState(() => {
    try {
      return localStorage.getItem('theme') === 'dark'
    } catch {
      return false
    }
  })

  useEffect(() => {
    const root = document.documentElement
    if (dark) {
      root.classList.add('dark')
      try { localStorage.setItem('theme', 'dark') } catch {}
    } else {
      root.classList.remove('dark')
      try { localStorage.setItem('theme', 'light') } catch {}
    }
  }, [dark])

  return (
    <header className="bg-white dark:bg-slate-800 border-b dark:border-slate-700">
      <div className="container-max flex items-center justify-between py-4">
        <div className="flex items-center gap-3">
          <div className="rounded-md bg-gradient-to-r from-rose-500 to-amber-400 p-2 text-white font-bold">L</div>
          <div className="text-lg font-semibold dark:text-slate-100">Lihabesha</div>
        </div>

        <nav className="hidden md:flex items-center gap-6 text-sm text-slate-700 dark:text-slate-200">
          <a className="hover:text-slate-900 dark:hover:text-slate-100" href="#housing">Housing</a>
          <a className="hover:text-slate-900 dark:hover:text-slate-100" href="#jobs">Jobs</a>
          <a className="hover:text-slate-900 dark:hover:text-slate-100" href="#travel">Travel</a>
          <a className="hover:text-slate-900 dark:hover:text-slate-100" href="#community">Community</a>
          <button className="ml-4 rounded-md bg-slate-900 px-3 py-1 text-sm font-medium text-white hover:bg-slate-800">Sign up</button>
        </nav>

        <div className="flex items-center gap-2">
          <button
            className="p-2 rounded hover:bg-slate-100 dark:hover:bg-slate-700"
            onClick={() => setDark(d => !d)}
            aria-label="Toggle dark mode"
          >
            {dark ? (
              <svg className="w-5 h-5 text-amber-300" viewBox="0 0 24 24" fill="currentColor"><path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"/></svg>
            ) : (
              <svg className="w-5 h-5 text-slate-700" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 3v2m0 14v2m9-9h-2M5 12H3m15.364-6.364l-1.414 1.414M7.05 16.95l-1.414 1.414m12.728 0l-1.414-1.414M7.05 7.05L5.636 5.636"/></svg>
            )}
          </button>

          <button className="md:hidden p-2" onClick={() => setOpen(o => !o)} aria-label="Toggle menu">
            <svg className="w-6 h-6 text-slate-700 dark:text-slate-200" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d={open ? 'M6 18L18 6M6 6l12 12' : 'M4 6h16M4 12h16M4 18h16'} />
            </svg>
          </button>
        </div>
      </div>

      {open && (
        <div className="md:hidden border-t bg-white dark:bg-slate-800 dark:border-slate-700">
          <div className="container-max flex flex-col gap-2 py-4 text-slate-700 dark:text-slate-200">
            <a className="py-2" href="#housing">Housing</a>
            <a className="py-2" href="#jobs">Jobs</a>
            <a className="py-2" href="#travel">Travel</a>
            <a className="py-2" href="#community">Community</a>
          </div>
        </div>
      )}
    </header>
  )
}
