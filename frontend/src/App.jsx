import Layout from './components/Layout'
import Listings from './components/Listings'
import PostForm from './components/PostForm'
import Modal from './components/Modal'
import Auth from './pages/Auth'
import { useState } from 'react'

function App() {
  const [openPost, setOpenPost] = useState(false)
  return (
    <Layout>
      <section className="grid gap-8 md:grid-cols-2 md:items-center">
        <div>
          <h1 className="text-3xl font-bold tracking-tight md:text-4xl">
            A trusted hub for Habesha housing, jobs, travel, and community
          </h1>
          <p className="mt-4 text-base text-slate-700">
            Find rooms, share opportunities, and stay connected with the Ethiopian and Eritrean diaspora.
          </p>
          <div className="mt-6 flex gap-3">
            <button className="rounded-md bg-slate-900 px-4 py-2 text-sm font-medium text-white hover:bg-slate-800">
              Create account
            </button>
            <button className="rounded-md border border-slate-300 px-4 py-2 text-sm font-medium text-slate-900 hover:bg-slate-100">
              Browse listings
            </button>
          </div>
        </div>
        <div className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
          <div className="text-sm font-semibold text-slate-500">Quick snapshot</div>
          <div className="mt-4 grid gap-4">
            <div className="rounded-lg border border-slate-200 p-4">
              <div className="text-xs uppercase text-slate-500">Housing</div>
              <div className="mt-1 text-sm">Rooms, apartments, shared housing</div>
            </div>
            <div className="rounded-lg border border-slate-200 p-4">
              <div className="text-xs uppercase text-slate-500">Jobs</div>
              <div className="mt-1 text-sm">Opportunities and services</div>
            </div>
            <div className="rounded-lg border border-slate-200 p-4">
              <div className="text-xs uppercase text-slate-500">Travel</div>
              <div className="mt-1 text-sm">Notices, luggage sharing, routes</div>
            </div>
          </div>
        </div>
      </section>

      <section className="mt-12 grid gap-6 md:grid-cols-2">
        <div id="housing" className="rounded-xl border border-slate-200 bg-white p-6">
          <h2 className="text-lg font-semibold">Housing & Rooms</h2>
          <p className="mt-2 text-sm text-slate-700">
            Post and discover housing with filters for city, price, availability, and room type.
          </p>
        </div>
        <div id="jobs" className="rounded-xl border border-slate-200 bg-white p-6">
          <h2 className="text-lg font-semibold">Jobs & Services</h2>
          <p className="mt-2 text-sm text-slate-700">
            Share job opportunities across hospitality, driving, admin, and more.
          </p>
        </div>
        <div id="travel" className="rounded-xl border border-slate-200 bg-white p-6">
          <h2 className="text-lg font-semibold">Travel Board</h2>
          <p className="mt-2 text-sm text-slate-700">
            Post travel dates, routes, and luggage availability for community support.
          </p>
        </div>
        <div id="community" className="rounded-xl border border-slate-200 bg-white p-6">
          <h2 className="text-lg font-semibold">Community</h2>
          <p className="mt-2 text-sm text-slate-700">
            Comment, message privately, and report inappropriate content for moderation.
          </p>
        </div>
      </section>

      <div className="mt-8 flex items-center justify-between">
        <h2 className="text-xl font-semibold">Explore</h2>
        <div className="flex items-center gap-2">
          <button onClick={() => setOpenPost(true)} className="rounded-md bg-rose-500 px-3 py-1 text-sm font-medium text-white hover:bg-rose-600">Post listing</button>
        </div>
      </div>

      <Listings />

      <Auth />

      <Modal open={openPost} onClose={() => setOpenPost(false)}>
        <h3 className="text-lg font-semibold">Create Listing</h3>
        <div className="mt-4">
          <PostForm onSubmit={(data) => { console.log('posted', data); setOpenPost(false) }} />
        </div>
      </Modal>
    </Layout>
  )
}

export default App
