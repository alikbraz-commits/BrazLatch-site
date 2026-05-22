---
description: Run the outbound prospect research workflow. Calls prospect-researcher to surface candidates, then prospect-qualifier to score and rank them.
argument-hint: "[territory: AU/NZ | UK/EU | India | all] (defaults to all)"
---

Coordinate the outbound prospecting workflow.

If `$ARGUMENTS` is empty, default to `all`.

**Phase 1 — Research**

Invoke `prospect-researcher`:

> Find distributor candidates for BrazLatch in territory: $ARGUMENTS.
> Aim for 5–8 real, verifiable companies per territory. Capture website,
> vertical, channels, size signal, and a contact path for each. Save the
> raw list to `.claude/prospects/candidates-raw.json`.

Show Alik a one-line summary per candidate. Ask: "Proceed to scoring?"

**Phase 2 — Qualify and rank**

Invoke `prospect-qualifier`:

> Read `.claude/prospects/candidates-raw.json`, score each candidate
> against `.claude/templates/prospect-rubric.md`, sort by territory then
> score, and write the result to `.claude/prospects/ranked.csv` and
> `.claude/prospects/ranked.json`. Then show me the on-screen summary
> in the format from your agent definition.

**Phase 3 — Next actions**

Show Alik the top 3 prospects across all territories with a recommendation:

```
🟢 #N {Company} ({Country}) — {score}/10
   {Why-fit, one line}
   → /draft-outreach {N}
```

If Alik picks one, hand it off to `distributor-manager`:

> Draft a cold outreach email to inquiry/prospect #{N} using the
> territory-appropriate template, in Alik's voice. Include one specific
> qualifying question and one concrete next step.
