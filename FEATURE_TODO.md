# Loki's Mischief — Full Feature-Set Implementation & Improvement TODO

_Living worklist. The improvement-loop job processes **ONE** unchecked item per run, then stops._
_Canonical repo: `lokibeinblodsson-ctrl/lokis-mischief` (main). Vanilla HTML/CSS/JS + 4 canvas games + tests._
_Quality-first mandate (2026-08-12, PERMANENT): games, quizzes, products, ENTIRE SITE = quality first._

## Discovered current state (2026-08-13)
- 27 root HTML pages (17 deity + business hub + services + lore + blog + games), 44 total `.html`.
- 4 live games (Fenrir, Hel, Jormungandr, Sleipnir) + Rune Cast + Ratatoskr (modal). `engine.js` v2.
- Tests: `tests/typecheck.js`, `tests/run.js` (94/0), `tests/play_games_cdp.py` (real-browser gameplay),
  `tests/human_drivability_cdp.py`. Push gate = `lokis_qa_push.sh` (gates on both + CDP when up).
- Recovery React project `phase-0b/` is LOCAL-ONLY (push guarded) — NOT a live target.
- Live site served via `nginx:alpine` :8899; GitHub Pages auto-deploys on push.

## P0 — Site integrity & correctness
- [ ] Run `node tests/run.js` + `node tests/typecheck.js` green on every change; fix first failing assertion.
- [ ] Add `node tests/run.js` coverage for EVERY page's `<title>` + meta description + `lang="en"` + mobile.css link.
- [ ] Fix any deity page where the generated portrait (`<deity>-hero.png`) is missing or unreferenced.
- [ ] Verify all internal links resolve (no 404) across 44 pages; add broken-link check to `run.js`.

## P1 — Game quality (quality-first: look + play, not just load)
- [ ] Vision-review Fenrir at 390px: fix any clipping/contrast/tap-target issue; re-capture to confirm.
- [ ] Vision-review Hel at 390px; same polish pass.
- [ ] Vision-review Jormungandr at 390px; same polish pass.
- [ ] Vision-review Sleipnir at 390px; same polish pass.
- [ ] Rune Cast: make rune name + phonetic ALWAYS visible during reveal; add reset button; animated backdrop.
- [ ] Ratatoskr: keep observable-only (no invented mechanics); add a reflection/lesson card + share card.
- [ ] Add real gameplay assertions for Rune Cast + Ratatoskr to `play_games_cdp.py` (push gate).

## P2 — Business pages & conversion
- [ ] services.html: concrete service tiers with reasonable prices + mailto booking; match brand voice.
- [ ] directory.html: agency hub cross-linking every page + game + product; single-column mobile.
- [ ] lore.html: Elder Futhark 24-rune reference + sagas/Edda, data-driven from `runes-data.json` (create it).
- [ ] Add a "start here" hero on index.html linking games→services→products funnel.
- [ ] Gumroad: draft 3+ product(s) from `gumroad-lokis-products.json`; owner publishes via helper.

## P3 — Content & blog automation
- [ ] Blog pipeline: ensure `blog/blog_gen.py` runs, blog/index.html links every post, 100-idea pool refills.
- [ ] Add 5 deity pages' `.lesson` blocks polish (business-lesson copy) — verify none are placeholder.
- [ ] Create `automation-agency-playbook/` as a real downloadable lead magnet (HTML/PDF) linked from services.

## P4 — Infrastructure & QA loop hardening
- [ ] Extend `lokis_qa_push.sh` to also run `tests/human_drivability_cdp.py` when CDP up (already in loop? confirm).
- [ ] Add a Lighthouse-style mobile perf check (no horizontal overflow, <2s interactive) to the QA loop.
- [ ] Add screenshot diff to the QA loop so visual regressions are caught, not just HTTP 200.
- [ ] Phase-0b: when user approves, wire the premium React brand shell as the future rebuild (push-guarded today).

## Done
<!-- items completed by the loop get moved here with the commit SHA -->
