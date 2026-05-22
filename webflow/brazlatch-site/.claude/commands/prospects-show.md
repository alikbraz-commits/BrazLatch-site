---
description: Show the current ranked outbound prospect list (top of each territory).
---

Read `.claude/prospects/ranked.csv` and present a compact summary:

```
═══ BRAZLATCH OUTBOUND PROSPECTS ═══

▶ AU/NZ ({count})        Top by score
  🟢 10  ID#1   Saddleworld
  🟢 9   ID#2   Greg Grant Saddlery
  🟢 8   ID#3   Horseland
  …

▶ UK/EU ({count})        Top by score
  🟢 10  ID#7   Naylors Equestrian
  …

▶ India ({count})        Top by score
  🟢 8   ID#13  Maanvi Exports
  …
```

If Alik asks for full detail on any row, read that row from the JSON
and show: Why-fit, contact path, size signal, score reason, notes.

If he wants to push to Google Sheets, point him to
`.claude/prospects/IMPORT-TO-GOOGLE-SHEETS.md`.
