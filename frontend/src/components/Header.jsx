import { useState } from 'react'

export default function Header() {
  const [open, setOpen] = useState(false)

  return (
    <header className="bg-white border-b">
      <div className="container-max flex items-center justify-between py-4">
        <div className="flex items-center gap-3">
          <div className="rounded-md bg-gradient-to-r from-rose-500 to-amber-400 p-2 text-white font-bold">L</div>
          <div className="text-lg font-semibold">Lihabesha</div>
        </div>

        <nav className="hidden md:flex items-center gap-6 text-sm">
          <a className="hover:text-slate-700" href="#housing">Housing</a>
          <a className="hover:text-slate-700" href="#jobs">Jobs</a>
          <a className="hover:text-slate-700" href="#travel">Travel</a>
          <a className="hover:text-slate-700" href="#community">Community</a>
          <button className="ml-4 rounded-md bg-slate-900 px-3 py-1 text-sm font-medium text-white hover:bg-slate-800">Sign up</button>
        </nav>

        <button className="md:hidden p-2" onClick={() => setOpen(o => !o)} aria-label="Toggle menu">
          <svg className="w-6 h-6 text-slate-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d={open ? 'M6 18L18 6M6 6l12 12' : 'M4 6h16M4 12h16M4 18h16'} />
          </svg>
        </button>
      </div>

      {open && (
        <div className="md:hidden border-t bg-white">
          <div className="container-max flex flex-col gap-2 py-4">
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
