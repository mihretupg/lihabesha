import Card from './Card'

const sample = [
  { id: 1, title: 'Cozy room in downtown', subtitle: 'Addis Ababa — $300/mo' },
  { id: 2, title: 'Shared apartment near university', subtitle: 'Mekelle — $200/mo' },
  { id: 3, title: 'Studio with kitchen', subtitle: 'Asmara — $350/mo' },
]

export default function Listings() {
  return (
    <section className="mt-8">
      <h3 className="text-xl font-semibold">Latest Listings</h3>
      <div className="mt-4 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {sample.map(item => (
          <Card key={item.id} title={item.title} subtitle={item.subtitle}>
            <div className="mt-2 flex items-center justify-between">
              <div className="text-xs text-slate-500 dark:text-slate-300">2 days ago</div>
              <button className="rounded-md bg-slate-900 px-3 py-1 text-xs font-medium text-white hover:bg-slate-800">View</button>
            </div>
          </Card>
        ))}
      </div>
    </section>
  )
}
