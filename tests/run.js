#!/usr/bin/env node
// run.js — full site test suite for Loki's Mischief.
// Checks: (1) every HTML page has <!DOCTYPE>/<title>/viewport, (2) internal links resolve to real files,
// (3) game pages define required functions, (4) runes-data.json has 24 runes, (5) blog posts exist after generation,
// (6) the running site (:8899) serves key routes 200. Exits non-zero on any failure.
const fs = require('fs');
const path = require('path');
const http = require('http');
const ROOT = path.resolve(__dirname, '..');

let pass = 0, fail = 0;
function ok(name) { pass++; console.log('  ✓ ' + name); }
function bad(name, why) { fail++; console.log('  ✗ ' + name + (why ? ' — ' + why : '')); }

// recurse to collect all html files + a full file set for link resolution
function walk(dir, acc) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) { if (e.name === 'node_modules' || e.name === '.git') continue; walk(p, acc); }
    else acc.push(p);
  }
  return acc;
}
const allPaths = walk(ROOT, []);
const allFiles = new Set(allPaths.map(p => path.relative(ROOT, p).split(path.sep).join('/')));
const htmlFiles = allPaths.map(p => path.relative(ROOT, p)).filter(f => f.endsWith('.html') && !f.startsWith('Gumroad'));

console.log('\n[1] Page structure');
for (const f of htmlFiles) {
  const html = fs.readFileSync(path.join(ROOT, f), 'utf8');
  const hasDoctype = /^<!DOCTYPE html>/i.test(html.trim());
  const hasTitle = /<title>.*<\/title>/i.test(html);
  const hasViewport = /name="viewport"/i.test(html);
  if (hasDoctype && hasTitle && hasViewport) ok(`${f}: doctype+title+viewport`);
  else bad(`${f}: structure`, `doctype=${hasDoctype} title=${hasTitle} viewport=${hasViewport}`);
}

console.log('\n[2] Internal link resolution');
const linkRe = /href="([^"#]+)"/g;
const fileDir = f => f.includes('/') ? f.slice(0, f.lastIndexOf('/')) : '';
for (const f of htmlFiles) {
  const html = fs.readFileSync(path.join(ROOT, f), 'utf8');
  let m, fileFails = [];
  while ((m = linkRe.exec(html))) {
    let href = m[1];
    if (href.startsWith('http') || href.startsWith('mailto') || href.startsWith('#') || href.startsWith('//')) continue;
    const clean = href.split('#')[0];
    if (!clean) continue;
    // resolve relative to the file's directory
    const resolved = path.normalize(path.join(fileDir(f), clean)).split(path.sep).join('/');
    if (!allFiles.has(resolved) && !fs.existsSync(path.join(ROOT, resolved))) fileFails.push(href);
  }
  if (fileFails.length === 0) ok(`${f}: all local links resolve`);
  else bad(`${f}: broken links`, fileFails.join(', '));
}

console.log('\n[3] Game function presence');
const gameChecks = [
  ['games/hel.html', ['function start', 'function decide', 'Engine.showEnd']],
  ['games/fenrir.html', ['function onTap', 'Engine.showEnd', 'CHAINS']],
  ['games/runecast.html', ['function cast', 'RUNES', 'Engine.getBest']],
  ['games/jormungandr.html', ['function start', 'Engine.showEnd', 'seq']],
  ['games/sleipnir.html', ['function start', 'Engine.showEnd', 'split']],
  ['games.html', ['games/fenrir.html', 'games/runecast.html', 'loki_best_']],
];
for (const [gf, fns] of gameChecks) {
  if (!fs.existsSync(path.join(ROOT, gf))) { bad(gf + ' exists'); continue; }
  const html = fs.readFileSync(path.join(ROOT, gf), 'utf8');
  const missing = fns.filter(fn => !html.includes(fn));
  if (missing.length === 0) ok(`${gf}: game functions present`);
  else bad(`${gf}: missing`, missing.join(', '));
}

console.log('\n[4] Rune data integrity');
try {
  const d = JSON.parse(fs.readFileSync(path.join(ROOT, 'runes-data.json'), 'utf8'));
  const count = d.elderFuthark.aettir.reduce((n, a) => n + a.runes.length, 0);
  if (count === 24) ok('runes-data.json: 24 runes across 3 aettir');
  else bad('runes-data.json: rune count', String(count));
  const noGlyph = d.elderFuthark.aettir.some(a => a.runes.some(r => !r.glyph || !r.name));
  if (!noGlyph) ok('runes-data.json: every rune has glyph+name'); else bad('runes-data.json: missing glyph/name');
} catch (e) { bad('runes-data.json parse', e.message); }

console.log('\n[5] Blog pipeline');
const blogIdx = path.join(ROOT, 'blog', 'index.json');
if (fs.existsSync(blogIdx)) {
  const bi = JSON.parse(fs.readFileSync(blogIdx, 'utf8'));
  if (bi.posts && bi.posts.length > 0) ok(`blog: ${bi.posts.length} post(s) generated`);
  else bad('blog: no posts');
  // each post file exists
  const missingPost = bi.posts.filter(p => !fs.existsSync(path.join(ROOT, p.file)));
  if (missingPost.length === 0) ok('blog: all post files present'); else bad('blog: missing files', missingPost.join(','));
} else bad('blog/index.json missing');

// blog-ideas pool not drained
const ideas = JSON.parse(fs.readFileSync(path.join(ROOT, 'blog-ideas.json'), 'utf8'));
if (ideas.ideas.length >= 5) ok(`blog-ideas.json: pool healthy (${ideas.ideas.length} left)`);
else bad('blog-ideas.json: pool low', String(ideas.ideas.length));

console.log('\n[6] Live server (:8899)');
const routes = ['index.html', 'lore.html', 'rune-cast.html', 'directory.html', 'services.html', 'products.html', 'games.html', 'games/hel.html', 'games/fenrir.html', 'games/runecast.html', 'games/jormungandr.html', 'games/sleipnir.html', 'blog/index.html'];
(function checkNext(i) {
  if (i >= routes.length) {
    console.log(`\n[SUMMARY] pass=${pass} fail=${fail}`);
    process.exit(fail ? 1 : 0);
  }
  const r = routes[i];
  const req = http.get({ host: '127.0.0.1', port: 8899, path: '/' + r, timeout: 4000 }, res => {
    if (res.statusCode === 200) ok(`serve ${r} -> 200`);
    else bad(`serve ${r}`, 'status ' + res.statusCode);
    res.resume(); req.on('close', () => checkNext(i + 1));
  });
  req.on('error', e => { bad(`serve ${r}`, e.message); req.destroy(); checkNext(i + 1); });
  req.on('timeout', () => { bad(`serve ${r}`, 'timeout'); req.destroy(); checkNext(i + 1); });
})(0);
