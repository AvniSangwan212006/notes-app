const API_BASE = '/api';

export async function listNotes() {
  const res = await fetch(`${API_BASE}/notes`);
  return res.json();
}

export async function createNote(data) {
  const res = await fetch(`${API_BASE}/notes`, {
    method: 'POST', headers: {'Content-Type':'application/json'},
    body: JSON.stringify(data)
  });
  return res.json();
}

export async function updateNote(id, data) {
  const res = await fetch(`${API_BASE}/notes/${id}`, {
    method: 'PUT', headers: {'Content-Type':'application/json'},
    body: JSON.stringify(data)
  });
  return res.json();
}

export async function deleteNote(id) {
  await fetch(`${API_BASE}/notes/${id}`, { method: 'DELETE' });
}
