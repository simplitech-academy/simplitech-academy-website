#!/usr/bin/env node
// Renders every Simplibyte card in simplibytes.json to bytes/<id>.png (1080 x 1350)
// using the site's own image export, so the pictures match the "Save image" button.
// Usage: node tools/render-bytes.js          (only cards without an image yet)
//        node tools/render-bytes.js --all    (re-render every card)
const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const root = path.resolve(__dirname, '..');
const MIME = { '.html': 'text/html', '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png', '.js': 'text/javascript', '.css': 'text/css' };

const server = http.createServer((req, res) => {
  let p = decodeURIComponent(req.url.split('?')[0]);
  if (p.endsWith('/')) p += 'index.html';
  const f = path.join(root, p);
  if (!f.startsWith(root) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(404); res.end(); return; }
  res.writeHead(200, { 'Content-Type': MIME[path.extname(f)] || 'application/octet-stream' });
  fs.createReadStream(f).pipe(res);
});

(async () => {
  const all = process.argv.includes('--all');
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  const port = server.address().port;
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto(`http://127.0.0.1:${port}/index.html#simplibytes`, { waitUntil: 'domcontentloaded' });
  await page.waitForFunction(() => window.Simplibytes && window.Simplibytes.cards().length > 0, null, { timeout: 30000 });
  const ids = await page.evaluate(() => window.Simplibytes.cards().map(b => b.id));
  fs.mkdirSync(path.join(root, 'bytes'), { recursive: true });
  let made = 0;
  for (const id of ids) {
    const out = path.join(root, 'bytes', id + '.png');
    if (!all && fs.existsSync(out)) continue;
    const b64 = await page.evaluate(async (cardId) => {
      const card = window.Simplibytes.cards().find(x => x.id === cardId);
      const blob = await window.Simplibytes.render(card);
      const buf = new Uint8Array(await blob.arrayBuffer());
      let s = '';
      for (let i = 0; i < buf.length; i += 0x8000) s += String.fromCharCode.apply(null, buf.subarray(i, i + 0x8000));
      return btoa(s);
    }, id);
    fs.writeFileSync(out, Buffer.from(b64, 'base64'));
    made++;
    console.log('rendered', id);
  }
  console.log(`done: ${made} new image(s), ${ids.length} cards`);
  await browser.close();
  server.close();
})().catch(e => { console.error(e); process.exit(1); });
