# Mock and Placeholder Audit

**Generated:** 2026-08-17T18:57Z (Micro-Phase 2A)
**Scope:** Identify placeholder, simulated, unimplemented, or decorative-vs-real behavior in the canonical repo.

## 1. Gumroad product data — placeholders present
File: `gumroad-lokis-products.json`
- All 3 listed products have **`"url": null`** and **`"published": false`**.
- Listed products are rune/art packs ("Elder Futhark Art Pack", "Elder Futhark Rune Book (PDF)", "Art + Rune Book Bundle").
- **Conflict with business model:** Per operator profile, the store must sell *business automation services/digital products* (workflows, SOP packs, automation kits, templates, lead magnets) — NOT rune/art/lore packs. Rune/art/lore is decoration only.
- **Status:** No live, purchasable Gumroad product is wired. Checkout/payment is non-functional.

## 2. n8n / Make blueprints — templates, not deployed services
- `Gumroad-Products/*/deployed-blueprint.json`, `lokis-assets/*/workflows/*.json` exist for many deities/products.
- These are **workflow templates/blueprints** (ai-concierge, client-onboarding, invoice-dunning, meeting-action-tracker, monthly-report-builder, rfp-response-drafter). They are downloadable product *content*, not a running automation backend on this site.
- No integration endpoints, webhooks, or live n8n/Make connection from the static site.

## 3. Games — engagement-only (decorative)
- 4 canvas games documented in README; no backend, no leaderboard, no persistence beyond optional LocalStorage (roadmap, not implemented).
- Correctly classified as engagement/decoration, not monetized.

## 4. Pages flagged with placeholder/TODO/coming-soon language
- `index.html`, `fenrir.html`, `gerd.html`, `FEATURE_TODO.md` contain TODO/placeholder markers (feature backlog, not fake data).
- `FEATURE_TODO.md` documents planned menus/sections (MENU-1, MENU-2 completed; further items pending). This is a roadmap, not a simulation.

## 5. Diagnostic / Audit platform — ABSENT
- No diagnostic UI, audit-panel code, scoring engine, or `/api` exists anywhere in the repo.
- Earlier phase reports describing a "diagnostic platform" are **planning specifications**, not implementation. Confirmed by full-tree search (no `diagnostic`, `audit-panel`, `/api`, `stripe`, `checkout` code paths).

## 6. `phase-0b` scaffold — abandoned build artifact
- Vite scaffold titled "Phase 0B Recovery Scaffold"; not referenced by nginx; not part of live site.
- Not a placeholder in the served site, but a stray build dir (see project-inventory §5). Not deleted per authorization.

## Summary
The live site is a **real static brand/decor site** with **no simulated data presented as functional**. Gaps are missing features (diagnostic, agency backend, payments), not fakery. The only "placeholder" state is Gumroad products being unpublished/`url:null` and the business-product mix not yet aligned to the operator's automation-agency model.
