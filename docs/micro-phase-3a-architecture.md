# Micro-Phase 3A — Framework & Integration Decision

**Generated:** 2026-08-17T19:18Z
**Author:** Hermes (autonomous, authorized 3A scope only)
**Status:** Analysis + recommendation. **No migration, no page creation, no build, no deletion performed.** Stopping after this report per authorization.

## 0. Constraint verification (deployment environment)
- Host: Linux 6.12, Docker present, nginx:alpine serving the static site on `:8899` (healthy post-2B).
- Node **v24.19.0** / npm **11.17.0** available; npm registry reachable (HTTP 200).
- A Node/Vite toolchain already works here (`phase-0b/node_modules` 96 MB proves it).
- Build artifacts must be servable by the existing nginx (or a derived image). No separate PaaS.
- Source-of-truth: single `origin/main` (`lokibeinblodsson-ctrl/lokis-mischief`); both local copies currently in sync at `8252c1c`.
- Astro is feasible in this environment (Node 24 ≥ Astro's requirement; static output needs no special runtime).

## 1. Framework options compared
| # | Option | Migration cost | Preserve existing pages | Static SEO | Interactive diagnostic | Game integration | Content authoring | Build reproducibility | Asset handling | Testing | Deploy simplicity | Long-term maint. | Duplicate-source risk |
|---|--------|---------------|------------------------|-----------|----------------------|-----------------|------------------|---------------------|----------------|---------|-------------------|-----------------|----------------------|
| 1 | **Extend static HTML/CSS/JS** | Lowest | Perfect (already there) | Good | Hard (manual DOM/state) | Easy (already JS) | Manual HTML | High | Manual | Weak | Trivial | Low complexity, high drift | Low |
| 2 | **Astro (SSG + islands)** | Medium | High (pages become `.astro`/MDX; can import existing HTML) | Excellent | Native (islands, React/Vanilla) | Easy (island or iframe) | Good (MDX/content cols) | High (lockfile) | Built-in (`public/`, `src/assets`) | Good (Vitest/Playwright) | Easy (static `dist/` → nginx) | High | Medium (must relocate old HTML) |
| 3 | **Vite/React SPA** | High | Low (rewrite) | Poor (needs SSR/prerender) | Native | Medium | Good | High | Built-in | Good | Needs SPA server/rewrites | Medium | High (two trees: old + new) |
| 4 | **Other (e.g. Eleventy/SvelteKit)** | Medium–High | Medium | Good–Excellent | Good | Easy–Med | Good | High | Built-in | Good | Easy–Med | Medium | Medium |

## 2. Recommended architecture
**Astro (static/hybrid) with interactive islands.** Matches the provisional recommendation and is verified feasible here.

- **Static-rendered routes** (SSG, zero JS by default → SEO + speed):
  - `/` (home), `/about`, `/services`, `/services/automation`, `/services/design`, `/services/social`, `/contact`
  - `/lore`, `/lore/[deity]` (deity pages), `/blog`, `/blog/[slug]`
  - `/shop` (Gumroad-embed pages, static)
- **Client-side islands** (hydrated only where needed):
  - Quick Diagnostic, Audit Panels, Games, theme toggle, interactive forms
- **Server/edge layer later** (not in 3A): contact submission, CRM routing, payment webhooks, personalized report generation.

## 3. Why it fits the actual project
- The site is **content + decoration-heavy, interaction-light** → Astro's SSG default keeps 95% of pages static (fast, SEO-safe) while allowing islands for the genuinely interactive parts (diagnostic, panels, games).
- Existing lore/game pages are plain HTML/JS and can be **migrated incrementally** into Astro as pages or wrapped in an island/iframe — no big-bang rewrite.
- Avoids the SPA SEO penalty (option 3) and the unbounded manual-drift of option 1 as the diagnostic/agency surface grows.
- Single build output (`dist/`) drops straight into the existing nginx image — **no new runtime**, keeps host lean (operator mandate).

## 4. Migration strategy (proposed, for later approval)
1. Create `app/` workspace (3B) with Astro, keep current static files untouched at repo root.
2. Build the new agency/diagnostic routes inside `app/`; verify they build independently.
3. **Only after** a later migration plan is approved: configure nginx to serve `app/dist/` as the document root (or mount `dist` into the existing container), preserving legacy routes via redirects.
4. Migrate lore/game pages one section at a time; keep them working throughout.
5. `phase-0b` (abandoned Vite scaffold) is superseded by `app/`; disposition decided in D4.

## 5. Route strategy
- New app owns: `/agency`, `/services*`, `/contact`, `/diagnostic`, `/diagnostic/[panel]`.
- Legacy static pages (`index.html`, deity pages, `games.html`, `rune-cast.html`, `lore.html`) remain served as-is until explicitly migrated; no route collision because new paths are namespaced.

## 6. Source-of-truth strategy
- **Single repo, single `main`**, one build workspace `app/` (no second independent clone).
- Recommend resolving the discovered clone/automation nuance (governance doc §7 / open decision D8): either re-point the feature agent to `/root/lokis-mischief` OR formally treat the clone as the implementation working copy. Until then, Hermes works only in `/root/lokis-mischief`.
- Hermes commits use identity `Hermes Agent` with message prefix `mp3x:` so they are distinguishable from `auto-publish`/`Loki Worker`/`Loki Blogger` (see `docs/governance-auto-publish.md`).

## 7. Build commands (proposed)
```
cd app
npm install            # reproducible via package-lock.json
npm run build          # outputs app/dist/ (static)
npm run dev            # local preview :4321
```
- No `npm install` run yet (3A is analysis only).

## 8. Test commands (proposed)
```
npm run build                     # must succeed (reproducibility gate)
node tests/typecheck.js          # existing gate (kept)
npx playwright test              # new: route + island smoke tests
npm run check                    # astro check (types/links)
```
- Existing `tests/run.js` gate preserved; new routes get Playwright smoke tests (3C/3D/3E require "add tests for all new routes").

## 9. Deployment implications
- Build produces static `dist/`; serve via existing nginx image (mount `app/dist` instead of repo root, or copy into image). No new container runtime needed.
- `docker-compose.yml` volume currently mounts repo root read-only; for the app, either build into the image (`COPY app/dist /usr/share/nginx/html`) or mount `app/dist`. Existing static site stays healthy until cutover.

## 10. Rollback plan
- Astro output is static; rollback = redeploy previous `dist/` (git tag/commit). Keep the old static files in the repo until migration is fully approved, so the nginx mount can be re-pointed to the legacy root instantly.
- No DB, no migrations → rollback is a file/commit revert. Low risk.

## 11. Open decisions (carried into 3B+)
- **D8 (new):** Resolve clone-vs-canonical automation ownership (governance §7).
- D1 framework final sign-off (this doc recommends Astro).
- D2 diagnostic build order; D3 Gumroad mix; D4 `phase-0b` disposition; D5 asset dedupe; D6 backend/CRM/payments; D7 finalize source-of-truth.
- Control `lokis_autopush` during structured work? (governance §4.3) — operator call.

## 12. Evidence pointers
- Environment: `node -v` → v24.19.0; npm registry reachable.
- Existing toolchain: `phase-0b/node_modules` (96M) confirms Node builds work.
- Governance: `docs/governance-auto-publish.md` (worker identities, 60s auto-push, clone-write reality).
- 2A/2B baseline: `docs/behavior-baseline.md`, `docs/source-of-truth.md`.

**→ Stopping per 3A authorization. Awaiting review before 3B (workspace creation), 3C (agency pages), 3D (diagnostic), 3E (reference panel).**
