import Layout from './components/Layout'
import Listings from './components/Listings'
import PostForm from './components/PostForm'
import Modal from './components/Modal'
import Auth from './pages/Auth'
import { useState } from 'react'
import { Routes, Route, Link } from 'react-router-dom'

function App() {
  const [openPost, setOpenPost] = useState(false)
  return (
    <Layout>
      <Routes>
        <Route
          path="/"
          element={(
            <>
              <section className="grid gap-8 md:grid-cols-2 md:items-center">
                <div>
                  <h1 className="text-3xl font-bold tracking-tight md:text-4xl">
                    A trusted hub for Habesha housing, jobs, travel, and community
                  </h1>
                  <p className="mt-4 text-base text-slate-700 dark:text-slate-300">
                    Find rooms, share opportunities, and stay connected with the Ethiopian and Eritrean diaspora.
                  </p>
                  <div className="mt-6 flex gap-3">
                    <Link to="/auth" className="rounded-md bg-slate-900 px-4 py-2 text-sm font-medium text-white hover:bg-slate-800">Create account</Link>
                    <Link to="/listings" className="rounded-md border border-slate-300 px-4 py-2 text-sm font-medium text-slate-900 hover:bg-slate-100">Browse listings</Link>
                  </div>
                </div>
                <div className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm dark:bg-slate-800 dark:border-slate-700">
                  <div className="text-sm font-semibold text-slate-500 dark:text-slate-300">Quick snapshot</div>
                </div>
              </section>

              <div className="mt-8 flex items-center justify-between">
                <h2 className="text-xl font-semibold">Explore</h2>
                <div className="flex items-center gap-2">
                  <button onClick={() => setOpenPost(true)} className="rounded-md bg-rose-500 px-3 py-1 text-sm font-medium text-white hover:bg-rose-600">Post listing</button>
                </div>
              </div>

              <Listings />
            </>
          )}
        />

        <Route path="/listings" element={<Listings />} />
        <Route path="/auth" element={<Auth />} />
      </Routes>

      <Modal open={openPost} onClose={() => setOpenPost(false)}>
        <h3 className="text-lg font-semibold">Create Listing</h3>
        <div className="mt-4">
          <PostForm onSubmit={(data) => {
            // try to create via API; if unauthenticated, show console message
            import('./api').then(({ createHousing }) => {
              createHousing({ title: data.title, city: data.location, price: data.price }).then(r => console.log('created', r)).catch(e => console.error(e))
            })
            setOpenPost(false)
          }} />
        </div>
      </Modal>
    </Layout>
  )
}

export default App
