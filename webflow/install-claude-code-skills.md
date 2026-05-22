# Install Claude Code skills — one-shot setup

This file gives you everything you need to install the five skills/plugins
you asked for. **Run these in Claude Code, not in Cowork** — `/plugin` commands
only work inside the Claude Code CLI.

---

## 1. Open Claude Code in your BrazLatch project

```powershell
cd "C:\Users\alikb\OneDrive\Tiedostot\2026\rooftrainer\pic\webflow\brazlatch-site"
claude
```

(If you don't have Claude Code installed yet:
`npm install -g @anthropic-ai/claude-code` — needs Node 18+.)

---

## 2. Install the five plugins

Paste each block at the Claude Code prompt. Restart Claude Code after the last one.

### 2.1 Superpowers — the big one. Adds the brainstorm → plan → execute → review loop, TDD discipline, subagent-driven development, git worktrees.

Repo: <https://github.com/obra/superpowers> · 176k stars · MIT

```
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

(Or via Anthropic's official marketplace: `/plugin install superpowers@claude-plugins-official`.)

### 2.2 GSD (Get Shit Done) — meta-prompting + context-engineering + spec-driven dev. Pairs nicely with Superpowers.

Repo: <https://github.com/jnuyens/gsd-plugin>

```
/plugin marketplace add jnuyens/gsd-plugin
/plugin install gsd@gsd-plugin
/reload-plugins
```

### 2.3 Claude-Mem — persistent memory across sessions. Captures every session, compresses with AI, injects relevant context into the next one.

Repo: <https://github.com/thedotmack/claude-mem> · 70k stars · AGPL-3.0

Two install options — pick one:

```
# Option A — via plugin marketplace (recommended for Claude Code only)
/plugin marketplace add thedotmack/claude-mem
/plugin install claude-mem
```

```bash
# Option B — via npx (also installs CLI hooks; works across multiple agents)
npx claude-mem install
```

### 2.4 Context-Mode — sandboxes tool output and only feeds summaries into context. ~98% context-token reduction on big greps/builds.

Repo: <https://github.com/mksglu/context-mode>

```
/plugin marketplace add mksglu/context-mode
/plugin install context-mode
```

(Requires Claude Code v1.0.33+. Check with `claude --version`.)

### 2.5 Frontend-Design — Anthropic's official frontend skill. Auto-invoked on frontend work; pushes Claude away from generic AI-slop aesthetics toward intentional design.

Repo (inside Anthropic's official marketplace): <https://github.com/anthropics/claude-plugins-official/tree/main/plugins/frontend-design>

```
/plugin marketplace add anthropics/claude-plugins-official
/plugin install frontend-design@claude-plugins-official
```

### 2.6 Verify

After restarting Claude Code:

```
/plugin list
```

You should see all five enabled. Then try `/brainstorm` or `/write-plan`
to confirm Superpowers triggered.

---

## 3. The `/review` command

You already have this built into Claude Code — no install needed. Type `/review`
inside Claude Code while on a feature branch to get a structured PR review.

## 4. Skill creator

Also already built in (you have `skill-creator` in this Cowork session, and
Claude Code ships with the equivalent). Use it to author your own skills once
you're up and running.

---

## What changes after install

- **Superpowers** auto-activates the moment you start a task — your agent
  asks "what are you actually trying to build?" before writing code.
- **GSD** layers a plan/execute/review phase structure on top.
- **Claude-Mem** quietly runs hooks behind every session — restart Claude Code
  and you'll see "Memory from previous sessions:" injected automatically.
- **Context-Mode** intercepts Bash/Read/Grep/WebFetch silently — you won't
  notice it except your context budget lasts dramatically longer.
- **Frontend-Design** auto-fires when you touch React/CSS/HTML.

You don't need to invoke any of these manually after install. They self-trigger.

---

## Want a smaller starter set?

If five at once feels like a lot, install **Superpowers + Frontend-Design**
first (sections 2.1 and 2.5). They're the biggest quality-of-life jump and
don't conflict with anything. Add Claude-Mem next (section 2.3) once you've
done a few sessions and want continuity. GSD and Context-Mode are
power-user additions on top.
