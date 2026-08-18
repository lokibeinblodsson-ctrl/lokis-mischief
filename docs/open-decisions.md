# Open Decisions

**Generated:** 2026-08-17T18:57Z (Micro-Phase 2A)
**Purpose:** Capture decisions that must be made by the operator before/during later micro-phases. None are resolved in Micro-Phase 2 (preserve/baseline/repair only).

## D1. Framework direction
- Retain static HTML, or migrate the live site to a real application framework (e.g., Vite/React or equivalent) so the diagnostic platform + agency pages can be built properly?
- Constraint from authorization: **no framework migration may begin until the Micro-Phase 2 report is reviewed.** `phase-0b` shows a prior Vite attempt exists but is abandoned.

## D2. Diagnostic platform scope & build order
- Micro-Phase 3 preview suggests: build core agency pages first, then Quick Diagnostic as greenfield, then one reference Audit Panel (not all eight at once).
- Operator must confirm the eight-panel list, the scoring model, and whether panels share a common engine.

## D3. Gumroad product alignment
- Current `gumroad-lokis-products.json` lists rune/art packs (decoration-only per operator policy) and all are `published:false`, `url:null`.
- Decision needed: replace with the business-automation product mix (workflows, SOP packs, automation kits, templates, lead magnet) and publish, or keep storefront deferred until agency pages exist.

## D4. `phase-0b` disposition
- Keep as historical scaffold, or delete after the framework decision (D1)? Not deleted in 2A per authorization.

## D5. Legacy/duplicate asset cleanup
- `set-game-runes-*` dirs vs `lokis-assets/glyphs/` may overlap. Dedupe later; not touched in 2A.

## D6. Backend / forms / CRM / payments
- When and how to introduce lead capture, CRM, and payment (Gumroad embed vs custom)? Out of scope for Micro-Phase 2.

## D7. Source-of-truth finalization
- The canonical decision (`/root/lokis-mischief`) is provisional. Confirm after this report, then the second clone can be retired or kept as a frozen reference.
