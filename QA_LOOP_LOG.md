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

---

## 2026-08-12 — tick 2 (second owner artifact + Hel rebuilt to §03)

**Second Meta AI artifact recovered** (`https://www.meta.ai/share/a/f525998f-...`): a **premium
playable 5-game arcade + 6-scan diagnostic funnel**. Signed payload:
`https://1222243714311245.a.metaaiusercontent.com/html?artifact_uuid=f525998f-...&hash=Q5fpDAFtx0JbjquHXYYsuxeJnIYZ`
(204 KB minified React). Rendered in the theo VM Chrome and extracted the OWNER'S canonical
content into `lokis-mischief/data/arcade-content.json`:
- **12-soul Hel deck** with intended `correct` routing (VIP refund $2k=human, Invoice $5k=auto, …).
- **24 business rune glosses** (Fehu→"wealth systems", … Dagaz→"breakthrough transformation").
- **6 free diagnostic scans** (Mischief Scan, Yggdrasil Health, Huginn & Muninn, Heimdall Signal,
  Norns Workflow, Týr Accountability) — the funnel entry points.
- **5 diagnostic archetypes** (Fenrir Bottleneck, Raven's Nest, Jörmungandr Loop, Bifröst Breakdown,
  Valhalla of Heroics) with fix playbooks.
NOTE: the rune divinatory/business meanings are the owner's interpretive layer, flagged as such in
the JSON — not presented as historical scholarship.

**Hel game rebuilt to bible §03** (was on broken v1 logic):
- Replaced guessed 2-word labels with the owner's 12-soul deck (fetched from `data/arcade-content.json`,
  hardcoded fallback so it still runs from `file://`).
- ONE shared essence pool (+10 correct / −10 wrong) instead of the old per-pile double-count.
- souls/min now measured across the whole run (was resetting every wave → absurd numbers).
- Swipe input added (60px threshold per spec); tap falls back to screen-half.
- Wave 4+ ambiguous souls, wave 7+ paired spawns; linear 5.0s→2.0s timer ramp across 10 waves.
- Colourblind-safe routing cue: a head shape = human, a box = machine (not colour alone).
- Real multi-word label wrapping on the orbs.
- S-rank end screen (90%+ accuracy) with score = essence + acc×2 + speed bonus; persisted best.
- Lesson copy matched the owner's arcade ("80% automate, 20% human = Hel's balance").

**Verified:** typecheck 0, `tests/run.js` pass 92/fail 0, `play_games_cdp.py` **pass 46/fail 0**
(new Hel section: deck load, routing rules, essence math, timeout miss, S-rank end, persistence).

**Open queue (next ticks, bible order):** Rune Cast §05 (daily seeded draw + streak) →
Jormungandr §02 (sequence + WebAudio) → Sleipnir §04 (lanes + powerup). The 6-scan funnel and the
24-rune business glosses are also available now to build the diagnostic funnel + Rune Cast content.

---

## 2026-08-12 — tick 3 (audit cache bug + real 44px gaps fixed)

**Root cause of the recurring tap-target findings:** `lokis_browser_audit.py` enabled `Network` but
never called `Network.setCacheDisabled`. The theo VM Chrome is a long-lived profile that caches
aggressively, so the audit had been measuring **stale cached pages from before every fix** — the
44px CSS and meta descriptions "came back" on every run because they were never re-fetched. Added
`Network.setCacheDisabled` to the audit (the gameplay test already had it). After that, a TRUE
re-audit showed the real gaps, which were two genuine selector omissions:

- The dominant nav container is `<div class="topbar">` — my original rule only matched `nav/.nav/
  header/footer a`, so the topbar links (and the `.brand` logo) were never floored.
- Card CTAs (`<a class="go">` inside `.card`), list CTAs (`li > a` guide links), and bare back-links
  / tag chips (`<a>` with no class) were also uncovered.

**Fix:** one shared `mobile.css` rule now floors **every `<a>` and form control** at <=480px, with
explicit prose exemptions (`main p a`, `article p a`, `.prose a`, `.tag a`, `.breadcrumb a`) so
article text is untouched. Re-audited with cache disabled: **0 tap-target findings across all pages**

**Verified (cache-off audit):** 0 tap targets <44px, 0 missing meta descriptions, 0 mobile overflow,
0 JS exceptions, 0 failed requests, only the pre-existing `services.html` duplicate-id `#automation`
(deferred — anchor target, owner call). `node tests/run.js` pass 92/0, `play_games_cdp.py` pass 46/0.

**Pitfall locked in:** ANY CDP measurement against the theo VM Chrome MUST disable cache, otherwise it
silently tests the previous version of the file. This now applies to both `lokis_browser_audit.py`
and `tests/play_games_cdp.py`.
2026-08-12T04:46:54-06:00 | QA tick (quality-first visual pass): Ratatoskr trunk labels no longer clip at 390px (vision-verified); play_games test isolation fixed (clear_storage) -> 46/0; homepage secondary CTA + Available-on contrast raised (vision-verified). All gates green: human-driv=18/0, play=46/0, typecheck=0, run.js=94/0. Pushed 5f4e9fc.
