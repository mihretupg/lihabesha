import FormInput from '../components/FormInput'

export default function Auth() {
  return (
    <section className="mt-8 grid gap-6 md:grid-cols-2">
      <div className="rounded-xl border border-slate-200 bg-white p-6 dark:bg-slate-800 dark:border-slate-700">
        <h3 className="text-lg font-semibold">Sign in</h3>
        <p className="mt-2 text-sm text-slate-600 dark:text-slate-300">Access your account to post and manage listings.</p>
        <form className="mt-4 space-y-3">
          <FormInput label="Email" type="email" placeholder="you@example.com" />
          <FormInput label="Password" type="password" placeholder="••••••" />
          <div className="flex items-center justify-between">
            <button className="rounded-md bg-slate-900 px-4 py-2 text-sm font-medium text-white hover:bg-slate-800">Sign in</button>
            <a className="text-sm text-slate-500 dark:text-slate-300">Forgot?</a>
          </div>
        </form>
      </div>

      <div className="rounded-xl border border-slate-200 bg-white p-6 dark:bg-slate-800 dark:border-slate-700">
        <h3 className="text-lg font-semibold">Create account</h3>
        <p className="mt-2 text-sm text-slate-600 dark:text-slate-300">Join the community to post new listings and message users.</p>
        <form className="mt-4 space-y-3">
          <FormInput label="Name" placeholder="Your name" />
          <FormInput label="Email" type="email" placeholder="you@example.com" />
          <FormInput label="Password" type="password" placeholder="Choose a password" />
          <div>
            <button className="rounded-md bg-rose-500 px-4 py-2 text-sm font-medium text-white hover:bg-rose-600">Get started</button>
          </div>
        </form>
      </div>
    </section>
  )
}
