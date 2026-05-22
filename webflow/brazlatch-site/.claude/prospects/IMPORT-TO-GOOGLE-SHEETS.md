# Get the prospect list into a Google Sheet — 30 seconds

The agent team produces `ranked.csv` in this folder. Here's the fastest
way to turn it into a live Google Sheet.

## Easiest path (drag and drop)

1. Open https://sheets.google.com/ and click the green **+** ("Blank
   spreadsheet").
2. In your file explorer, drag `ranked.csv` straight into the open
   Google Sheet browser tab. It auto-imports. Done.

## Slightly cleaner (File → Import)

1. New Google Sheet.
2. **File → Import → Upload → Drag** the `ranked.csv` file in.
3. Import location: **Replace current sheet**. Separator type:
   **Comma**. Click **Import data**.

## Rename it, set up the columns

The CSV ships with these columns (UTF-8 with BOM so it imports clean):

```
ID · Territory · Country · Company · Website · Vertical · Channels ·
Size signal · Score · Score reason · Why-fit · Likely contact path ·
Status · Notes · Last touched
```

In the imported Sheet:

1. Click **row 1**, format → bold, freeze (View → Freeze → 1 row).
2. Highlight column I (**Score**) → Format → Conditional formatting:
   - Color scale, min 0 (red), midpoint 5 (yellow), max 10 (green).
3. Highlight column M (**Status**) → Data → Data validation:
   - List of items: `to-research, researching, contacted, replied,
     qualifying, proposal, won, passed`.
4. Optional — make **Website** column links clickable: select column E,
   Format → Number → Plain text isn't necessary, the URLs already work
   as hyperlinks once you press Enter on the cell.

## Connect it back to Claude Code (optional, advanced)

If you install a Google Sheets MCP connector for Claude Code (e.g. via
`/plugin marketplace`), you can ask the `prospect-qualifier` agent to
write directly to your Sheet instead of (or in addition to) the CSV.
At that point your local CSV becomes a backup and the Sheet becomes
the source of truth.

Until then: the CSV in this folder IS the source of truth. Re-running
`/find-prospects` rewrites it. Drag-drop into the same Sheet again to
refresh, or use Google Sheets's **Import → Replace current sheet** to
keep the same Sheet ID/URL.

## How to keep the Sheet in sync as you work

- **You add a status note in the Sheet** (e.g. "Replied 2026-05-20") →
  export the Sheet as CSV, save back to this folder, replace `ranked.csv`,
  and the agents will read the new status on their next run.
- **The agents update status (e.g. after `/draft-outreach`)** → they
  write to `ranked.csv` here; re-drag into the Sheet to refresh.

A simple round-trip workflow until you wire a true two-way connector.
