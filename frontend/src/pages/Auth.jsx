import { useState } from 'react'
import FormInput from '../components/FormInput'
import { useAuth } from '../auth/AuthProvider'

export default function Auth() {
  const { login, register } = useAuth()
  // login state
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState(null)

  // register state
  const [rname, setRname] = useState('')
  const [remail, setRemail] = useState('')
  const [rpassword, setRpassword] = useState('')

  async function handleLogin(e) {
    e.preventDefault()
    setError(null)
    try {
      await login(email, password)
    } catch (err) {
      setError(err.message)
    }
  }

  async function handleRegister(e) {
    e.preventDefault()
    setError(null)
    try {
      await register({ name: rname, email: remail, password: rpassword })
    } catch (err) {
      setError(err.message)
    }
  }

  return (
    <section className="mt-8 grid gap-6 md:grid-cols-2">
      <div className="rounded-xl border border-slate-200 bg-white p-6 dark:bg-slate-800 dark:border-slate-700">
        <h3 className="text-lg font-semibold">Sign in</h3>
        <p className="mt-2 text-sm text-slate-600 dark:text-slate-300">Access your account to post and manage listings.</p>
        <form onSubmit={handleLogin} className="mt-4 space-y-3">
          <FormInput label="Email" type="email" value={email} onChange={e => setEmail(e.target.value)} placeholder="you@example.com" />
          <FormInput label="Password" type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="••••••" />
          <div className="flex items-center justify-between">
            <button type="submit" className="rounded-md bg-slate-900 px-4 py-2 text-sm font-medium text-white hover:bg-slate-800">Sign in</button>
            <a className="text-sm text-slate-500 dark:text-slate-300">Forgot?</a>
          </div>
          {error && <div className="text-rose-500 text-sm mt-2">{error}</div>}
        </form>
      </div>

      <div className="rounded-xl border border-slate-200 bg-white p-6 dark:bg-slate-800 dark:border-slate-700">
        <h3 className="text-lg font-semibold">Create account</h3>
        <p className="mt-2 text-sm text-slate-600 dark:text-slate-300">Join the community to post new listings and message users.</p>
        <form onSubmit={handleRegister} className="mt-4 space-y-3">
          <FormInput label="Name" value={rname} onChange={e => setRname(e.target.value)} placeholder="Your name" />
          <FormInput label="Email" type="email" value={remail} onChange={e => setRemail(e.target.value)} placeholder="you@example.com" />
          <FormInput label="Password" type="password" value={rpassword} onChange={e => setRpassword(e.target.value)} placeholder="Choose a password" />
          <div>
            <button type="submit" className="rounded-md bg-rose-500 px-4 py-2 text-sm font-medium text-white hover:bg-rose-600">Get started</button>
          </div>
          {error && <div className="text-rose-500 text-sm mt-2">{error}</div>}
        </form>
      </div>
    </section>
  )
}
