# Inquiries — what lives in this folder

This folder is the distributor-manager subagent's working memory.

## Files it expects

| File                          | What it is                                                |
|-------------------------------|-----------------------------------------------------------|
| `submissions.csv`             | Raw export from Netlify Forms (you paste it in here)      |
| `pipeline.json`               | The agent's authoritative status log — don't hand-edit    |
| `drafts/{id}-{slug}.md`       | Pending reply drafts awaiting Alik's approval             |

## How to refresh submissions

**Option A — Netlify dashboard:**
1. Go to https://app.netlify.com/sites/<your-site>/forms
2. Open the `distributor-inquiry` form
3. Click **Export to CSV**
4. Save into this folder as `submissions.csv` (overwrite)
5. In Claude Code, run `/inquiries refresh`

**Option B — Netlify CLI:**
```
netlify api listFormSubmissions --data='{"form_id":"<form-id>"}' > submissions.json
```
Then ask Claude to convert it to the CSV shape the agent expects (or
just feed it the JSON directly — the agent handles both).

## Privacy

This folder may contain prospect emails, phone numbers, and business
details. Do not commit it to a public repo.

A starter `.gitignore` is provided that excludes everything in here
**except** this README and the schema-only `pipeline.json`.
