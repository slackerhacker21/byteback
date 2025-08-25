import { useEffect, useState } from 'react'
import Editor from '@monaco-editor/react'
import { getProblem, submit } from '../lib/api'

type Problem = {
  slug:string; title:string; difficulty:'easy'|'medium'|'hard';
  statement_md:string; starter_code_py:string; starter_code_java:string;
}

export default function ProblemPage({ slug }: { slug: string }){
  const [p, setP] = useState<Problem | null>(null)
  const [lang, setLang] = useState<'java'|'python'>('java')
  const [code, setCode] = useState('')
  const [busy, setBusy] = useState(false)
  const [result, setResult] = useState<string>('')

  useEffect(()=>{ (async()=>{
    const pb = await getProblem(slug)
    setP(pb)
    setCode(lang === 'java' ? pb.starter_code_java : pb.starter_code_py)
  })() }, [slug])

  useEffect(()=>{ if(p){ setCode(lang === 'java' ? p.starter_code_java : p.starter_code_py) } }, [lang])

  const run = async ()=>{
    if(!p) return
    setBusy(true)
    const v = await submit(p.slug, lang, code)
    setBusy(false)
    setResult(`${v.passed ? '✅ Passed' : '❌ Not yet'} — ${v.tests_passed}/${v.tests_total}
` + v.details.join('\n'))
  }

  if(!p) return <div>Loading…</div>

  return (
    <div>
      <h2 style={{marginTop:0}}>{p.title}</h2>
      <p style={{opacity:.7}}>{p.difficulty}</p>
      <pre style={{whiteSpace:'pre-wrap',background:'#f7f7f7',padding:12,borderRadius:8}}>{p.statement_md}</pre>

      <div style={{display:'flex',alignItems:'center',gap:12,margin:'12px 0'}}>
        <label>Language</label>
        <select value={lang} onChange={e=>setLang(e.target.value as any)}>
          <option value="java">Java</option>
          <option value="python">Python</option>
        </select>
        <button disabled={busy} onClick={run} style={{marginLeft:'auto',padding:'8px 12px'}}>Run / Submit</button>
      </div>

      <Editor height="60vh" defaultLanguage={lang} value={code} onChange={(v)=>setCode(v||'')} />

      {result && (
        <pre style={{whiteSpace:'pre-wrap',background:'#eefbf0',padding:12,borderRadius:8,marginTop:12}}>{result}</pre>
      )}
    </div>
  )
}
