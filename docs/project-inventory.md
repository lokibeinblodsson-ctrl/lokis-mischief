# Project Inventory — Loki's Mischief

**Generated:** 2026-08-17T18:57Z (Micro-Phase 2A: Preserve and Inventory)
**Author:** Hermes (autonomous, authorized scope)
**Canonical source:** `/root/lokis-mischief` (git `main`, HEAD `9baa40cd5ef7c94027aaf4b3474e04f74e30373f`)
**Second clone (read-only):** `/root/agent/repos/lokis-mischief` (git `main`, HEAD `9baa40c…` — byte-identical content)

---

## 1. Repository facts
- Git remote (both): `https://github.com/lokibeinblodsson-ctrl/lokis-mischief.git`
- Tracked files (canonical): **5,470**
- Total on-disk size (canonical, incl. untracked/build): **272 MB**
- Working trees: both clean (`nothing to commit`) at time of capture.
- **Clone comparison:** file set and content are identical. The only difference is the authorized `docs/_preserve/` directory added during 2A. Commit histories are equivalent (both `main`, same HEAD). No divergent commits found.

## 2. Site type
- **Static, flat HTML site** served by nginx. No build step, no SPA router, no backend.
- 60 `.html` pages, 15 `.css`, 308 `.json`, 3,015 `.js` (mostly vendored game/lore assets).
- Entry page: `index.html` (219 KB). Sole orchestration: `menu.js`.

## 3. Top-level inventory (selected)
| Path | Type | Notes |
|------|------|-------|
| `index.html`, `services.html`, `products.html`, `directory.html`, `games.html`, `lore.html`, `rune-cast.html`, `entertainment.html`, `blog.html`, `art-gallery.html` | HTML | Primary site pages |
| `angrboda.html` … `utgardaloki.html` (deity pages), `odin.html`, `thor.html`, `loki.html`, `freya.html`, etc. | HTML | ~24 deity/character pages |
| `lokis-assets/` (69 MB) | dir | Images, fonts, glyphs, per-deity workflow JSON/templates/guides |
| `games/` (92 KB) | dir | Game assets |
| `Gumroad-Products/` (472 KB), `Gumroad-Product/`, `Gumroad-Store/` | dir | Product blueprints, n8n/Make workflows |
| `products/` (4.4 MB) | dir | Product covers/assets |
| `set-game-runes-*` (2 dirs, ~7 MB) | dir | Runic stock imagery |
| `blog/`, `lore/`, `fonts/`, `data/`, `media-tools/`, `free-tools-discovery/`, `automation-agency-playbook/` | dir | Content/asset dirs |
| `phase-0b/` (97 MB) | dir | **Abandoned/duplicate Vite build scaffold** (see §5) |
| `docs/` | dir | Project docs (**this file lives here**) |
| `Dockerfile`, `docker-compose.yml`, `docker-compose.agents.yml`, `nginx.conf` | config | Static serve stack |
| `MICRO_PHASE_1_REPORT.md`, `NORSE_TRADITIONAL_ACCURACY_AUDIT.md`, `product-research-report.md`, `QA_LOOP_LOG.md`, `FEATURE_TODO.md`, `audit-log.md`, `README.md` | md | Reports/notes |
| `gumroad-lokis-products.json`, `runes-data.json`, `blog-ideas.json`, `.cartoon_prompts.json`, `.icon_manifest.json`, `.last-audit.json` | json | Data/metadata |

## 4. Absent (verified, by search + inspection)
- **Diagnostic platform** — does not exist. No `/diagnostic`, `/audit`, or `/api` routes; no audit-panel code.
- **Agency core pages** — `services.html`/`products.html` exist as pages but contain only decorative business framing and Gumroad links; no functional lead form, CRM, checkout, or backend.
- **Backend / API / payment** — none. No `stripe`, `paypal`, `checkout`, `webhook`, `express`, `flask`, `django`, or `/api/` code paths.
- **Forms / CRM** — none active.
- **Build pipeline** — none for the live site (static HTML). `phase-0b` is a stray Vite build, not wired to serving.

## 5. Legacy / duplicate / abandoned directories
- **`phase-0b/`** — Vite recovery scaffold. Contains `dist/index.html` (431 B stub) + `dist/assets/index-Cvv9pliq.js` (196 KB, with `.js.map`) + `node_modules/` (esbuild). Title: "Phase 0B Recovery Scaffold". **Not referenced by nginx and not part of the live static site.** Treated as abandoned build directory. **Not deleted (per authorization).**
- `set-game-runes-*` directories — stock rune imagery, possibly redundant with `lokis-assets/glyphs/`. Flagged for later dedupe; not modified.

## 6. Games (engagement-only, preserved)
- README documents 4 games: Chain Strike (Fenrir), Serpent Memory (Jörmungandr), Soul Judgment (Hel), Eight-Legged Sprint (Sleipnir). Canvas-drawn, vanilla JS, no backend. No leaderboard/backend persistence.
- These are decoration/engagement, not monetized products.

## 7. Files preserved (2A)
- Full repository preserved in place (`/root/lokis-mischief`).
- `MICRO_PHASE_1_REPORT.md` copied to `docs/_preserve/MICRO_PHASE_1_REPORT.md`.
- Container forensic snapshot: `docs/_preserve/container/lokis-site-inspect.json`, `docs/_preserve/container/lokis-site-logs.txt`.
- SHA-256 of all 5,451 canonical files: `docs/_preserve/canonical-hashes.sha256`.
