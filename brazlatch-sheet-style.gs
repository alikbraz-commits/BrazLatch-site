/**
 * BrazLatch Sheet Styler
 * ----------------------
 * Paste this into Extensions → Apps Script → replace everything → Run → styleSheet
 *
 * What it does:
 *   - Color-codes each section (Home / How It Works / Applications)
 *   - Makes section headers bold and big
 *   - Makes the VALUE column (what you edit) stand out
 *   - Grays out the NOTES column so it's there but not distracting
 *   - Freezes the top row so headers always stay visible
 *   - Sets comfortable column widths
 */

function styleSheet() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const data  = sheet.getDataRange().getValues();
  const nRows = data.length;

  // ── Section colors ──────────────────────────────────────────────────────────
  // Each # header row gets a dark banner. Rows below get the matching light color.
  const sections = [
    { match: '🏠 HOME — HERO',        banner: '#1B5E20', light: '#E8F5E9' },
    { match: '🏠 HOME — STORY',       banner: '#2E7D32', light: '#F1F8E9' },
    { match: '🏠 HOME — PATENT',      banner: '#388E3C', light: '#F9FBE7' },
    { match: '⚙️ HOW IT WORKS',       banner: '#0D47A1', light: '#E3F2FD' },
    { match: '📦 APPLICATIONS',        banner: '#E65100', light: '#FFF3E0' },
  ];

  // ── Style the frozen header row (row 1) ─────────────────────────────────────
  sheet.setFrozenRows(1);
  const headerRange = sheet.getRange(1, 1, 1, 3);
  headerRange.setBackground('#0E0D0B');
  headerRange.setFontColor('#EFEAE0');
  headerRange.setFontWeight('bold');
  headerRange.setFontSize(12);
  headerRange.setValues([['KEY  (don\'t edit this)', 'VALUE  ✏️ Edit this column', 'NOTES  (just for reference)']]);

  // ── Column widths ────────────────────────────────────────────────────────────
  sheet.setColumnWidth(1, 280);  // key
  sheet.setColumnWidth(2, 480);  // value  ← widest — this is what you edit
  sheet.setColumnWidth(3, 260);  // notes

  // ── Row heights ──────────────────────────────────────────────────────────────
  sheet.setRowHeightsForced(1, nRows, 32);

  // ── Process every row ────────────────────────────────────────────────────────
  let currentLight = '#FFFFFF';
  let currentBanner = '#333333';

  for (let i = 1; i < nRows; i++) {
    const key      = String(data[i][0] || '');
    const rowNum   = i + 1;
    const fullRow  = sheet.getRange(rowNum, 1, 1, 3);
    const keyCell  = sheet.getRange(rowNum, 1);
    const valCell  = sheet.getRange(rowNum, 2);
    const noteCell = sheet.getRange(rowNum, 3);

    if (key.startsWith('#')) {
      // ── Section banner row ──────────────────────────────────────────────────
      const found = sections.find(s => key.includes(s.match));
      currentBanner = found ? found.banner : '#424242';
      currentLight  = found ? found.light  : '#FAFAFA';

      fullRow.setBackground(currentBanner);
      fullRow.setFontColor('#FFFFFF');
      fullRow.setFontWeight('bold');
      fullRow.setFontSize(13);
      fullRow.setVerticalAlignment('middle');

      // Show only the label text (strip the leading #)
      keyCell.setValue(key.replace(/^#\s*/, ''));
      valCell.setValue('');
      noteCell.setValue('');

    } else if (key === '') {
      // ── Empty / spacer row ──────────────────────────────────────────────────
      fullRow.setBackground('#FFFFFF');

    } else {
      // ── Data row ─────────────────────────────────────────────────────────────
      fullRow.setBackground(currentLight);
      fullRow.setFontColor('#212121');
      fullRow.setFontSize(11);

      // KEY: monospace, muted
      keyCell.setFontFamily('Courier New');
      keyCell.setFontColor('#555555');
      keyCell.setFontWeight('normal');
      keyCell.setFontSize(10);

      // VALUE: bold, dark — this is what you edit
      valCell.setFontWeight('bold');
      valCell.setFontColor('#0D0D0D');
      valCell.setFontSize(11);
      valCell.setWrap(true);

      // NOTES: small, gray, italic — just for reference
      noteCell.setFontColor('#888888');
      noteCell.setFontStyle('italic');
      noteCell.setFontSize(10);
      noteCell.setWrap(true);
    }
  }

  // ── Protect key column (warn if editing) ─────────────────────────────────────
  // Just visually signal it — a real protection would require sheet owner setup
  sheet.getRange(2, 1, nRows - 1, 1).setBackground(null); // already handled above

  // ── Done ─────────────────────────────────────────────────────────────────────
  SpreadsheetApp.getUi().alert(
    '✅ Done!\n\n' +
    'Your sheet is now color-coded:\n' +
    '🟢 Green = Home page sections\n' +
    '🔵 Blue  = How It Works page\n' +
    '🟠 Orange = Applications list\n\n' +
    'The bold column in the middle is what you edit.'
  );
}
