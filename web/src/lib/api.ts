const BASE = (import.meta as any).env?.VITE_API_BASE || 'http://localhost:8000'
export async function getProblem(slug: string){
  const r = await fetch(`${BASE}/problems/${slug}`);
  if(!r.ok) throw new Error('problem not found');
  return r.json();
}
export async function listProblems(){
  const r = await fetch(`${BASE}/problems`);
  return r.json();
}
export async function submit(slug: string, language: 'python'|'java', code: string){
  const r = await fetch(`${BASE}/submit`,{method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({slug, language, code})});
  return r.json();
}
