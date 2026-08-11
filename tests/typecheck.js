#!/usr/bin/env node
// typecheck.js — extract every <script> block from the HTML files and run `node --check` on it.
// Vanilla JS has no type system, so "type check" = syntax-validate every inline script.
// Also JSON.parse-validates runes-data.json, blog-ideas.json, blog/index.json.
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const os = require('os');
const ROOT = path.resolve(__dirname, '..');

const htmlFiles = fs.readdirSync(ROOT).filter(f => f.endsWith('.html') && !f.startsWith('Gumroad'));
let errors = 0, checked = 0;

function extractScripts(html) {
  const re = /<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/g;
  const out = []; let m;
  while ((m = re.exec(html))) out.push(m[1]);
  return out;
}

for (const f of htmlFiles) {
  const html = fs.readFileSync(path.join(ROOT, f), 'utf8');
  const scripts = extractScripts(html);
  scripts.forEach((src, i) => {
    if (!src.trim()) return;
    const tmp = path.join(os.tmpdir(), `loki_${f}_${i}.js`);
    fs.writeFileSync(tmp, src);
    try {
      execSync(`node --check ${tmp}`, { stdio: 'pipe' });
      checked++;
    } catch (e) {
      errors++;
      console.error(`✗ JS syntax error in ${f} script#${i}:\n${e.stderr?.toString() || e.message}`);
    }
    fs.unlinkSync(tmp);
  });
}

// JSON validity
for (const jf of ['runes-data.json', 'blog-ideas.json', 'blog/index.json', 'gumroad-lokis-products.json'].filter(x => fs.existsSync(path.join(ROOT, x)))) {
  try { JSON.parse(fs.readFileSync(path.join(ROOT, jf), 'utf8')); checked++; }
  catch (e) { errors++; console.error(`✗ Invalid JSON: ${jf}: ${e.message}`); }
}

console.log(`[typecheck] scripts+json checked: ${checked}, errors: ${errors}`);
process.exit(errors ? 1 : 0);
