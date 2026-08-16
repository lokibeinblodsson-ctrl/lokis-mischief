Loki's Mischief — FEATURE TODO (agent-dispatcher working copy)
## Standing directive (owner 2026-08-16): ALL work refocused on this site, quality unparalleled.
## Full rationale + structure: MEMORY/TODO_LOKIS_MISCHIEF.md (canonical index).
## Dispatcher picks the FIRST '- [ ]' item not marked [USER]/[BLOCKED].
## Done

- [x] Phase 0A-0C: scaffold + mount six games + validation
- [x] Phase 1A-1C: shell, lifecycle, cross-game mobile validation
- [x] Phase 2A-2C: scoring/data contracts, validation, reflection-only scan
- [x] Phase 3A: catalog schema + validation
- [x] Local production build + unit/smoke/Playwright tests

## P0 — STRUCTURE: split monolithic index into per-menu pages (owner mandate: each menu link its own page)
- [ ] MENU-1 | Promote games.html to the standalone Games hub page (own nav + back link) from index.html nav
- [ ] MENU-2 | Create entertainment.html (Fun Stuff) standalone page from #entertainment section
- [ ] MENU-3 | Ensure all menu "Products" links resolve to products.html (not #products anchor)
- [ ] MENU-4 | Create pantheon.html standalone deity index (from #pantheon anchor)
- [ ] MENU-5 | Create playbook.html standalone (from #playbook anchor)
- [ ] MENU-6 | Create about.html standalone (from #about anchor)
- [ ] MENU-7 | Add a "Blog" link to the main nav (blog.html -> blog/index.html)
- [ ] MENU-8 | Rebuild index.html as a lean hub (hero + section cards; remove 5000-line anchor sections)

## P1 — GAMES: upgrade to unparalleled quality
- [ ] GAME-1 | Fenrir: premium canvas backdrop, juice, always-visible how-to, clear result screen
- [ ] GAME-2 | Hel: soul-sorting UX polish, animated backdrop, colorblind-safe cue, result screen
- [ ] GAME-3 | Jormungandr: sequence-memory juice + lit-node visuals
- [ ] GAME-4 | Sleipnir: parallel-runner polish, run-bar/coin readout, 60fps
- [ ] GAME-5 | Rune Cast: premium share card, rune name+phonetic always visible
- [ ] GAME-6 | Ratatoskr: keep engagement-only; polish visuals, label unresolved
- [ ] GAME-7 | Inject animated backdrops + shared GameChrome into all 6 games (reuse engine.js v2)

## P2 — ART & GRAPHICS: amazing visuals
- [ ] ART-1 | Generate full Elder Futhark 24-rune PNG art pack (high res, folio style)
- [ ] ART-2 | Regenerate deity portraits to premium quality and WIRE them (-hero.png slot)
- [ ] ART-3 | Premium hero + section dividers + rune brand mark (void-black + gold system)
- [ ] ART-4 | Curate art-gallery.html with real generated assets

## P3 — PRODUCTS: tested + full instructions
- [ ] PROD-1 | Test the 3 Gumroad drafts end-to-end as a buyer
- [ ] PROD-2 | Write full fulfillment instructions for each product
- [ ] PROD-3 | Product detail pages/cards with honest price + instructions + refund/contact
- [ ] PROD-4 | Verify every checkout/delivery URL manually before publish

## P4 — QUIZZES: operational gap-finders by level (laborer -> owner)
- [ ] QUIZ-1 | Design quiz taxonomy: 5 tiers (Laborer/Supervisor/Manager/Director/Owner) each finding ops gaps
- [ ] QUIZ-2 | Build Laborer-level ops-gap quiz (intuitive, scores to actionable gap report)
- [ ] QUIZ-3 | Build Owner-level ops-gap quiz (strategy/financial/leadership gaps)
- [ ] QUIZ-4 | Build 3 middle tiers (Supervisor/Manager/Director)
- [ ] QUIZ-5 | Each quiz returns gap report + links to relevant product/service

## P5 — BLOG: own page + menu link
- [ ] BLOG-1 | Ensure every blog post is its own page under blog/
- [ ] BLOG-2 | Add Blog to main nav (MENU-7)
- [ ] BLOG-3 | Blog index lists all posts with excerpts + menu link

## P6 — QUALITY GATES (always)
- [ ] QA-1 | Keep node tests/typecheck.js + tests/run.js green after every change
- [ ] QA-2 | Visual QA via screenshot+vision at 390px + 1280px before marking UI done
- [ ] QA-3 | Run real-browser gameplay gate (tests/play_games_cdp.py) when theo CDP :9224 up

## Reference artifacts (owner-provided, not yet extracted — need theo VM Chrome CDP :9224)
- [ ] REF-1 | Extract loki-full-empire-site-v2.html design (menu/nav, product, archetype) via CDP
- [ ] REF-2 | Extract loki-6-games-fixed.html (6 games) via CDP
- [ ] REF-3 | Extract loki-scoring-engine.html (quiz scoring archetype=56) via CDP
- [ ] REF-4 | Extract loki-hermes-handoff-v2.html via CDP
