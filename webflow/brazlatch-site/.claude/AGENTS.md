# BrazLatch agent team

Three specialist subagents work the BrazLatch project in Claude Code. You
talk to Claude normally; Claude routes work to the right subagent based on
what you ask for. You can also invoke them directly by name.

## The team

### 🛠 `site-builder`
Owns the code and assets. Tweaks `index.html`, `styles.css`, `main.js`,
swaps icons, wires in photos and videos, runs pre-deploy sanity checks.
Pairs with the `frontend-design` plugin when designing new UI.

> "Add this product photo to the What-Is section."  
> "Swap the Baby & Kids icon for this PNG."  
> "Replace 'Issued' with the real patent numbers."  
> "Run a pre-deploy sanity check."

### 🔎 `brand-and-audit`
Owns words, claims, accessibility, and SEO. Doesn't touch code — produces
a precise punch list and hands fixes to `site-builder`. Pairs with
`marketing:brand-review`, `design:accessibility-review`, `marketing:seo-audit`.

> "Audit the site."  
> "Is the hero copy on-brand?"  
> "Check accessibility on the form section."  
> "Are there any claims that need disclaimers?"

### 📨 `distributor-manager`
Owns the **inbound** distributor inquiry pipeline — triage, qualification, reply
drafting in Alik's voice, status tracking. Never sends without approval.

> "Any new distributor inquiries?"  
> "Draft a reply to inquiry 14."  
> "Run the weekly pipeline report."

### 🔍 `prospect-researcher`
Owns **outbound** prospecting. Finds real distributor candidates in
the three open markets (AU/NZ, UK/EU non-Ajustco, India) via web research.
Captures website, vertical, channels, size signal, contact path.

> "Find more prospects in AU/NZ."  
> "Who else should I be reaching out to in India?"

### 📊 `prospect-qualifier`
Owns **scoring**. Takes the researcher's raw candidate list, scores each
against the prospect rubric, produces the ranked CSV that imports into
Google Sheets.

> "Score the prospect list."  
> "Re-rank the prospects with the new info."

## The orchestrating commands

| Command            | What it does                                                       |
|--------------------|--------------------------------------------------------------------|
| `/audit`           | Runs `brand-and-audit` and produces the punch list                 |
| `/go-live`         | Full pre-launch sequence — audit → fix → deploy → verify domain    |
| `/deploy`          | Runs pre-flight checks + `netlify deploy --prod`                   |
| `/inquiries`       | Triages new distributor form submissions (inbound)                   |
| `/reply <id>`      | Drafts a personalized reply to a specific inquiry                   |
| `/pipeline-report` | Weekly digest of the distributor pipeline                           |
| `/find-prospects [territory]` | Outbound: researches + scores prospect list             |
| `/prospects-show`  | Shows the current ranked prospect list                              |

## How to launch the site (TL;DR)

```
/go-live
```

That command coordinates all three agents through audit → fix → deploy →
verify, stopping at each phase for your "continue". It's the one-command
end-to-end if you trust the team.

If you want to drive it manually instead:

```
/audit                    # see what needs fixing
# (review the punch list, ask agents to apply specific items)
/deploy                   # push to Netlify
```

## How the agents talk to each other

Claude Code's main thread is the conductor. When `brand-and-audit` finds
a fix that needs code changes, it doesn't edit the code itself — it
produces a handoff entry like:

> [FIX] #A2 (handed to site-builder)  
> File: `index.html:142`  
> Issue: nav-cta has insufficient contrast (2.8:1 on green)  
> Proposed fix: change the `.nav-cta` color from `#fff` to `#1a1a1a`  
> in `css/styles.css` line 68.

The main thread (you-as-Claude) then invokes `site-builder` with that
exact instruction. `site-builder` applies it, confirms back, and the
main thread updates `brand-and-audit` so it can re-audit.

This split keeps responsibilities clean and audits trustworthy — the
agent that *finds* issues isn't the one that *fixes* them.

## Where each agent's working files live

| Agent                 | Working directory                              |
|-----------------------|------------------------------------------------|
| `site-builder`        | `index.html`, `css/`, `js/`, `assets/`         |
| `brand-and-audit`     | Read-only on code; writes to `.claude/audit/`  |
| `distributor-manager` | `.claude/inquiries/`, `.claude/templates/`     |

## When agents shouldn't be used

- Quick one-off questions about the project ("what's the brand green?")  
  → just ask Claude in the main thread; no subagent needed.
- Brand-new features or sections — discuss in the main thread first to
  scope, then hand the implementation to `site-builder`.
- Anything that touches Alik's personal accounts or money (Netlify
  billing, domain renewals, payment processors) — escalate to Alik, never
  auto-execute.
