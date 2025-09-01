import { useEffect, useState } from 'react'
import { listNotes, createNote, updateNote, deleteNote } from './api'

export default function App() {
  const [notes, setNotes] = useState([])
  const [title, setTitle] = useState('')
  const [content, setContent] = useState('')
  const [editingId, setEditingId] = useState(null)

  async function refresh() {
    setNotes(await listNotes())
  }

  useEffect(() => { refresh() }, [])

  async function submit(e) {
    e.preventDefault()
    if (!title) return
    if (editingId) await updateNote(editingId, { title, content })
    else await createNote({ title, content })
    setTitle(''); setContent(''); setEditingId(null)
    refresh()
  }

  return (
    <div style={{ maxWidth:600, margin:"2rem auto" }}>
      <h1>📝 Notes</h1>
      <form onSubmit={submit}>
        <input value={title} onChange={e=>setTitle(e.target.value)} placeholder="Title"/><br/>
        <textarea value={content} onChange={e=>setContent(e.target.value)} placeholder="Content"/><br/>
        <button type="submit">{editingId ? "Update" : "Add"}</button>
      </form>
      <ul>
        {notes.map(n=>(
          <li key={n.id}>
            <b>{n.title}</b>
            <button onClick={()=>{setEditingId(n.id);setTitle(n.title);setContent(n.content||'')}}>Edit</button>
            <button onClick={()=>{deleteNote(n.id).then(refresh)}}>Delete</button>
            <p>{n.content}</p>
          </li>
        ))}
      </ul>
    </div>
  )
}
