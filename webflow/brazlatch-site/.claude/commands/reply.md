---
description: Draft a personalized reply to a specific distributor inquiry (by id from /inquiries).
argument-hint: "<inquiry-id>"
---

If `$ARGUMENTS` is empty, ask Alik for the inquiry id (run `/inquiries` first
if he doesn't have one).

Otherwise:

1. Invoke the `distributor-manager` subagent with:

   > Draft a reply for inquiry #$ARGUMENTS. Follow your reply-drafting protocol:
   > pull the inquiry from pipeline.json, pick the matching territory template,
   > adapt to the prospect's specific message and channel, write in Alik's voice,
   > include one specific qualifying question and one concrete next step. Save
   > the draft to .claude/inquiries/drafts/ and show it to me here.

2. Show Alik the draft.
3. Ask whether to:
   - **(a) edit** — let him dictate changes inline
   - **(b) approve & copy** — copy the body to clipboard, mark `status: replied`
   - **(c) send via connected email tool** — only if an Outlook/Gmail MCP is
     installed and authenticated
   - **(d) discard** — delete the draft, leave status unchanged

4. After action, confirm what happened in one line.
