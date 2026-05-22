---
description: Triage new distributor inquiries from the Netlify form. Surfaces the ranked list and recommends next actions.
argument-hint: "[refresh]"
---

You are about to triage the distributor pipeline.

1. Invoke the `distributor-manager` subagent with this task:

   > Triage all new inquiries. If $ARGUMENTS contains "refresh", prompt the user
   > to re-export the CSV from Netlify before running the diff. Otherwise use
   > the existing `.claude/inquiries/submissions.csv`. Produce the ranked
   > summary in the format defined in your agent definition (🟢 / 🟡 / 🔴).

2. Wait for its output and present it directly to Alik.
3. Offer next steps: `/reply <id>` for individual replies, or `/pipeline-report`
   for the weekly digest.

Do not edit any files in this command — the subagent owns
`.claude/inquiries/pipeline.json`.
