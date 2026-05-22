/**
 * Google Sheets CMS
 * -----------------
 * Fetches the published CSV at build time and provides a key → value lookup.
 *
 * Sheet structure (Row 1 = header, ignored):
 *   Column A: key    — e.g. "home.hero.title"
 *   Column B: value  — the content (plain text or basic HTML for title fields)
 *   Column C: notes  — human description, ignored by this code
 *
 * Setup:
 *   1. In your Google Sheet: File → Share → Publish to web
 *   2. Choose Sheet1 → Comma-separated values (.csv) → Publish
 *   3. Copy the URL and paste it into .env as CONTENT_SHEET_URL
 *
 * Rows starting with # in Column A are treated as comments and skipped.
 */

export type ContentMap = Record<string, string>;

let _cache: ContentMap | null = null;

export async function getSiteContent(): Promise<ContentMap> {
  if (_cache) return _cache;

  const url = import.meta.env.CONTENT_SHEET_URL as string | undefined;
  if (!url) {
    console.warn('[cms] CONTENT_SHEET_URL not set — using hardcoded defaults for all content.');
    _cache = {};
    return _cache;
  }

  try {
    const res = await fetch(url, { cache: 'no-store' });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const text = await res.text();
    _cache = parseSheetCSV(text);
    console.log(`[cms] Loaded ${Object.keys(_cache).length} content entries from Google Sheets.`);
    return _cache;
  } catch (err) {
    console.error('[cms] Could not reach Google Sheet — using hardcoded defaults.', err);
    _cache = {};
    return _cache;
  }
}

/**
 * Returns a getter function bound to a content map.
 * Usage: const get = makeGetter(c); get('home.hero.title', 'Default text')
 */
export function makeGetter(map: ContentMap) {
  return function get(key: string, fallback: string): string {
    const v = map[key];
    return v && v.trim() ? v.trim() : fallback;
  };
}

// ─── CSV parser ────────────────────────────────────────────────────────────────

function parseSheetCSV(text: string): ContentMap {
  const map: ContentMap = {};
  const rows = text.replace(/\r\n/g, '\n').replace(/\r/g, '\n').split('\n');

  for (let i = 1; i < rows.length; i++) {   // i=1 skips the header row
    const cols = parseCSVRow(rows[i]);
    const key   = (cols[0] ?? '').trim();
    const value = (cols[1] ?? '').trim();
    if (key && !key.startsWith('#')) {
      map[key] = value;
    }
  }
  return map;
}

function parseCSVRow(line: string): string[] {
  const cols: string[] = [];
  let cur = '';
  let inQ  = false;

  for (let i = 0; i < line.length; i++) {
    const ch = line[i];
    if (ch === '"') {
      if (inQ && line[i + 1] === '"') { cur += '"'; i++; } // escaped quote
      else inQ = !inQ;
    } else if (ch === ',' && !inQ) {
      cols.push(cur); cur = '';
    } else {
      cur += ch;
    }
  }
  cols.push(cur);
  return cols;
}
