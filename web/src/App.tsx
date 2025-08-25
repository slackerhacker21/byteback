import { useEffect, useState } from 'react'
import Topbar from './components/Topbar'
import Problem from './pages/Problem'
import { listProblems } from './lib/api'

type ProblemMeta = { slug:string; title:string; difficulty:'easy'|'medium'|'hard' }

export default function App(){
  const [problems, setProblems] = useState<ProblemMeta[]>([])
  const [active, setActive] = useState<string>('reverse-array')
  useEffect(()=>{ listProblems().then(setProblems) },[])
  return (
    <div>
      <Topbar/>
      <div style={{display:'grid',gridTemplateColumns:'280px 1fr',gap:16,padding:16}}>
        <div style={{borderRight:'1px solid #eee',paddingRight:12}}>
          <h3>Problems</h3>
          <ul style={{listStyle:'none',padding:0}}>
            {problems.map(p=> (
              <li key={p.slug} style={{margin:'8px 0'}}>
                <button onClick={()=>setActive(p.slug)} style={{background:'none',border:'1px solid #ddd',padding:'6px 8px',borderRadius:8,textAlign:'left',cursor:'pointer',width:'100%'}}>
                  {p.title} <small style={{opacity:.6}}>({p.difficulty})</small>
                </button>
              </li>
            ))}
          </ul>
        </div>
        <div>
          <Problem slug={active}/>
        </div>
      </div>
    </div>
  )
}
