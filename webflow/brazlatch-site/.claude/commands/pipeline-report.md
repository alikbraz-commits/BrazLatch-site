---
description: Weekly distributor pipeline report — counts by status, top prospects, stale conversations.
---

Invoke the `distributor-manager` subagent with:

> Produce the weekly pipeline report from `.claude/inquiries/pipeline.json`.
> Include: total inquiries received this week, breakdown by status (new /
> replied / qualifying / proposal / won / passed), breakdown by territory,
> top 3 prospects by score, anyone waiting > 5 days for a first reply
> (flag these in red), and conversion deltas vs the prior week if data is
> available.

Present its output as a short, scannable digest Alik can read on his phone.
