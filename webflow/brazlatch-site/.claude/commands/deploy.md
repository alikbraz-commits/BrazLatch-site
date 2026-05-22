---
description: Deploy the static site to Netlify production with a pre-flight sanity check.
---

Run a pre-flight check, then deploy.

**Pre-flight (do these in order, stop if any fail):**

1. Confirm the cwd is the `brazlatch-site` folder (look for `index.html` and `netlify.toml`).
2. `git status` — surface any uncommitted changes and ask Alik whether to deploy them or stash first.
3. Validate that all assets referenced in `index.html` exist on disk
   (the same check we ran at build time):
   ```
   python3 - <<'PY'
   import re, pathlib
   p = pathlib.Path(".")
   text = (p/"index.html").read_text()
   refs = re.findall(r'(?:src|href)="(/[^"]+)"', text)
   missing = [r for r in refs if not r.startswith(("/#","https://")) and not (p / r.lstrip("/")).exists()]
   print("MISSING:", missing or "none")
   PY
   ```
4. If `netlify` CLI is not installed, tell Alik: `npm install -g netlify-cli` and stop.
5. Confirm with Alik before pushing live — show him a one-line summary
   ("Deploying 21 files, 12.6 MB, no missing assets, last commit: 'fix patent copy'").

**Deploy:**

```
netlify deploy --dir=. --prod
```

**Post-flight:**

1. Surface the production URL Netlify returned.
2. Curl the homepage and confirm HTTP 200 + size > 15 KB.
3. Append an entry to `.claude/deploy-log.md` with timestamp, files changed, deploy URL.
