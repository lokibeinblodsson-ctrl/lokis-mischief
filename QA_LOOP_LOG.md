# Loki's Mischief — Automated QA Loop Log
Loop: Hermes cron `lokis-qa-improvement-loop-2h` (every 120m).
Phases: probe (`lokis_qa_probe.sh`) → analyze → test → patch → verify → log → commit/push (`lokis_qa_push.sh`).
Push is gated on `node tests/typecheck.js` and `node tests/run.js` both exiting 0.

---

## 2026-08-12 — tick 0 (loop bring-up, manual verification run)

**Status probe:** container `lokis-site` healthy; all 18 HTML routes HTTP 200; all JSON valid;
typecheck exit 0; test suite pass=92 fail=0.

**Issues found**
- 34 pages missing `<meta name="description">` (SEO / social previews).
- 9 pages missing `mobile.css` (mobile-first directive): blog.html, games.html,
  games/{fenrir,sleipnir,hel,runecast,jormungandr}.html, blog/index.html,
  blog/windmill-vs-n8n-vs-nodered-which-automation-engine.html.

**Fixes applied**
- Added a title-derived `<meta name="description">` to all 34 pages missing one.
- Injected `mobile.css` (depth-correct relative path) into the 9 pages missing it.

**Verification:** typecheck=0, tests pass=92 fail=0, all routes still 200.

**Open findings (deferred, not auto-removed)**
- `Gumroad-Product/` and `Gumroad-Store/` static pages are separate from the main design
  language — review for brand consistency, do not delete.
- `compare-cartoon.html` looks like a dev comparison page — left in place pending owner call.

---

## 2026-08-12 — tick 1 (browser-based analysis + engine v2 + Fenrir to bible spec)

**Tooling added (scripted, reusable by every future tick)**
- `/root/.hermes/scripts/lokis_browser_audit.py` — CDP audit in the theo VM's real Chrome
  (127.0.0.1:9224). Loads EVERY page at 390px and 1440px and records JS exceptions, failed
  network requests, HTTP>=400 subresources, horizontal overflow, sub-44px tap targets,
  missing title/description/lang, duplicate ids, broken `<img>`, canvas presence on game pages.
  Report: `/var/log/lokis-browser-audit.json`.
- `/root/.hermes/scripts/lokis_autofix.py` — applies the mechanical findings idempotently.
- `/root/.hermes/scripts/cdp_read_page.py` + `cdp_dump_bodies.py` — render/read JS-gated pages
  (login-walled SPAs) through the VM browser when `web_extract` can't.
- `tests/play_games_cdp.py` — REAL gameplay test: clicks Start, fires strikes, reads game state.

**Browser audit findings (46 pages)**
- 0 JS exceptions, 0 failed requests, 0 mobile overflow, 0 broken images. 
- 44 pages with sub-44px nav tap targets; 10 Gumroad pages missing meta description;
  1 duplicate id (`services.html` #automation).

**Fixes applied**
- 44px minimum tap targets for nav/footer/buttons at <=480px, added ONCE in shared `mobile.css`
  (single revert point) rather than editing 44 files; inline prose links explicitly exempted.
- meta descriptions for the 10 remaining pages (recursive glob — the earlier pass was depth-limited
  and missed `Gumroad-Store/**`), `lang="en"` on blog.html, mobile.css linked on 12 more pages.
- **`games/engine.js` rewritten as v2** to the recovered design bible's "00 // CORE" contract:
  pause on visibilitychange AND blur w/ AudioContext suspend, Esc/P pause + overlay, M mute,
  persistent muted-by-default audio w/ master gain 0.15 and click-free envelopes, dt clamped to
  32ms, `loki_best_<id>` as `{score,date,meta}` with v1 integer back-compat, reduced-motion
  particle cut (70%), ice-blue focus rings, 44px HUD controls, and a real client-side 1080x1350
  share card (grain + foil gradient) with Web Share API + download fallback.
- **`games/fenrir.html` brought to exact §01 spec**: windows 0.40/0.20/0.12 at 1.0x/1.4x/1.8x,
  -100/3 integrity per hit (3 hits = 1 chain), +10% miss reform, 90s limit, perfect = centre 40%
  of the window (+50), time bonus x2/sec, Gleipnir sinusoidal drift, "Gleipnir Unbound" badge,
  live HUD timer that reddens under 15s.
- `docs/loki-engine-design-bible.md` — the full 5-game design bible recovered from the Meta AI
  artifact the owner shared, stored as lean markdown (the original is a 3.8MB React bundle).

**Verification**
- `node tests/typecheck.js` = 0, `node tests/run.js` = **pass 94 / fail 0**
- `tests/play_games_cdp.py` = **pass 34 / fail 0** in real Chrome (engine API, muted-by-default,
  44px controls, 1080x1350 share card, every Fenrir scoring rule, pause/resume on all 5 games)

**Open findings (documented, NOT auto-removed)**
- `services.html` duplicate id `#automation` — deliberately NOT renamed: ids are anchor targets
  other pages may link to, so a rename can silently break navigation. Needs an owner call.
- Hel / Jormungandr / Sleipnir / Rune Cast are still on v1 mechanics; the bible's §03/§02/§04/§05
  specs (waves + ambiguous souls, dual-rune chords, split-lane powerup, daily seeded oracle +
  streak) are the queue for the next ticks, in the bible's own implementation order.
- Pitfall recorded: the theo Chrome profile served a CACHED `engine.js`, silently testing the old
  version — CDP tests must set `Network.setCacheDisabled`.
