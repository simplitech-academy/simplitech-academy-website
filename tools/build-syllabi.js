#!/usr/bin/env node
/* Builds syllabi/<slug>.pdf for every course in courses.json.
   Usage: node tools/build-syllabi.js            (all courses)
          node tools/build-syllabi.js <slug> ... (only the given courses)
   Needs Playwright with Chromium installed (the same setup as tools/render-bytes.js). */
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const root = path.resolve(__dirname, '..');
const courses = JSON.parse(fs.readFileSync(path.join(root, 'courses.json'), 'utf8'));
const only = process.argv.slice(2);
const bySlug = Object.fromEntries(courses.map(c => [c.slug, c]));

const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const LOGO = '<svg width="46" height="46" viewBox="0 0 200 200" aria-hidden="true"><defs><linearGradient id="g1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3CCBB8"/><stop offset="1" stop-color="#4C8DF0"/></linearGradient><linearGradient id="g2" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2BB8A8"/><stop offset="1" stop-color="#4C7DF0"/></linearGradient></defs><rect x="8" y="8" width="184" height="184" rx="46" fill="url(#g1)"/><circle cx="62" cy="105" r="30" fill="#fff"/><circle cx="100" cy="82" r="38" fill="#fff"/><circle cx="140" cy="108" r="28" fill="#fff"/><rect x="62" y="105" width="78" height="30" fill="#fff"/><path d="M100 112C112 92 134 92 134 112C134 132 112 132 100 112C88 92 66 92 66 112C66 132 88 132 100 112Z" fill="none" stroke="url(#g2)" stroke-width="9" stroke-linejoin="round"/></svg>';

function html(c) {
  const fact = (k, v) => `<div class="f"><span>${esc(k)}</span><b>${esc(v)}</b></div>`;
  const mods = c.modules.map((m, i) => `
    <section class="mod">
      <h3><span class="n">${i + 1}</span>${esc(m.t)}${m.w ? `<em>${m.w} weeks</em>` : ''}</h3>
      <ul>${m.topics.map(t => `<li>${esc(t)}</li>`).join('')}</ul>
      <p class="lab"><b>${m.course ? 'Course:' : 'Hands-on:'}</b> ${esc(m.lab)}</p>
    </section>`).join('');
  const list = a => `<ul>${a.map(x => `<li>${esc(x)}</li>`).join('')}</ul>`;
  const next = c.next.map(s => bySlug[s]).filter(Boolean).map(x => esc(x.title)).join(', ');
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><title>${esc(c.title)} syllabus</title><style>
@page{size:A4;margin:16mm 15mm 18mm}
*{box-sizing:border-box}
body{margin:0;font:10.5pt/1.5 Inter,"Helvetica Neue",Arial,sans-serif;color:#2F4A66}
.head{display:flex;align-items:center;gap:12px;padding-bottom:12px;border-bottom:3px solid #3CCBB8}
.brand b{display:block;font-size:15pt;letter-spacing:-.01em}
.brand span{font-size:8pt;letter-spacing:.3em;color:#2BB8A8}
.tag{margin-left:auto;font-size:8.5pt;color:#5B7288;text-align:right}
h1{font-size:23pt;line-height:1.15;margin:20px 0 4px;letter-spacing:-.02em}
.lead{font-size:12pt;color:#5B7288;margin:0 0 14px}
.badge{display:inline-block;margin-bottom:6px;padding:2px 10px;border-radius:99px;background:#E6F7F4;color:#1B7F72;font-size:8.5pt;font-weight:700;letter-spacing:.04em;text-transform:uppercase}
.facts{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:14px 0 18px}
.f{padding:9px 11px;border:1px solid #D6E2EA;border-radius:8px;background:#F4F9FB}
.f span{display:block;font-size:7.5pt;letter-spacing:.08em;text-transform:uppercase;color:#6A8296}
.f b{font-size:10.5pt}
h2{font-size:13pt;margin:20px 0 8px;padding-bottom:4px;border-bottom:1px solid #D6E2EA}
ul{margin:0;padding-left:18px}
li{margin:2px 0}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.mod{break-inside:avoid;margin:0 0 10px;padding:10px 12px;border:1px solid #D6E2EA;border-radius:8px}
.mod h3{display:flex;align-items:center;gap:8px;margin:0 0 4px;font-size:11pt}
.mod .n{display:inline-grid;place-items:center;width:20px;height:20px;border-radius:50%;background:linear-gradient(135deg,#3CCBB8,#4C8DF0);color:#10263A;font-size:9pt;font-weight:700}
.mod em{margin-left:auto;font-style:normal;font-size:8.5pt;color:#6A8296;font-weight:500}
.mod ul{columns:2;column-gap:20px}
.lab{margin:6px 0 0;font-size:9.5pt;color:#5B7288}
.note{margin-top:18px;padding:10px 12px;border-radius:8px;background:#F4F9FB;font-size:9pt;color:#5B7288}
.foot{margin-top:16px;padding-top:10px;border-top:1px solid #D6E2EA;font-size:9pt;display:flex;justify-content:space-between;color:#5B7288}
.foot b{color:#2F4A66}
</style></head><body>
<div class="head">${LOGO}<div class="brand"><b>Simplitech</b><span>ACADEMY</span></div><div class="tag">Course syllabus<br>simplitechacademy.com</div></div>
<h1>${esc(c.title)}</h1>
<p class="lead">${esc(c.tagline)}</p>
<span class="badge">${c.type === 'long' ? 'Long program' : 'Short course'} · ${esc(c.group)}</span>
<div class="facts">
  ${fact('Duration', c.weeks + ' weeks')}
  ${fact('Live sessions', c.sessions + ' x 60 min')}
  ${fact('Format', 'Live online, one to one')}
  ${fact('Level', c.level)}
</div>
<h2>What you will learn</h2>${list(c.outcomes)}
<h2>Curriculum</h2>${mods}
<div class="cols">
  <div><h2>Tools</h2>${list(c.tools)}<h2>Projects</h2>${list(c.projects)}</div>
  <div><h2>Who it is for</h2>${list(c.who)}<h2>Prerequisites</h2><p style="margin:0">${esc(c.prereq)}</p></div>
</div>
${c.prepares && c.prepares.length ? `<h2>Certification path</h2>${list(c.prepares)}<p class="note">This course helps you prepare. Exams are taken separately with the provider, and we cannot promise a pass.</p>` : ''}
${next ? `<h2>Next steps</h2><p style="margin:0">${next}</p>` : ''}
<div class="note">Durations assume two one-hour live sessions per week plus practice time between sessions. Your coach confirms the plan and schedule with you in a free consultation, and details may be adjusted to your background and goals.</div>
<div class="foot"><span><b>Book a free consultation</b> at simplitechacademy.com</span><span>Simplitech Academy</span></div>
</body></html>`;
}

(async () => {
  const outDir = path.join(root, 'syllabi');
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const list = courses.filter(c => !only.length || only.includes(c.slug));
  for (const c of list) {
    await page.setContent(html(c), { waitUntil: 'load' });
    await page.evaluate(() => document.fonts && document.fonts.ready);
    await page.pdf({ path: path.join(outDir, c.slug + '.pdf'), format: 'A4', printBackground: true });
    console.log('wrote syllabi/' + c.slug + '.pdf');
  }
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
