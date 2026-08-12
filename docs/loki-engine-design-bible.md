# Loki Engine — Game Design Bible (v0.9)

Source: Meta AI artifact `loki-mischief-game-bible.html` (recovered 2026-08-12 via theo VM Chrome;
the share page is login-walled, the payload was pulled from the signed
`*.a.metaaiusercontent.com/html?artifact_uuid=…` URL embedded in the page's RSC stream).
Stored here as markdown instead of the 3.8 MB React bundle to keep the repo lean.

## 00 // CORE — shared design system

| Concern | Spec |
|---|---|
| Canvas | 900×600 centered responsive, aspect locked via letterbox, 100% width below 900px (`max-width:900px; aspect-ratio:3/2`) |
| Budget | <2 MB initial gzipped. Sprites WebP, audio tiny base64 blips <15 kb, no image >120 kb |
| Loop | `requestAnimationFrame`, delta clamped at 32 ms, optional fixed timestep for physics |
| State machine | `idle / playing / paused / win / lose` — single source of truth object |
| Controls | Tap + keyboard (Space, Arrows, A/D, QWER), unified pointer events, 44 px min touch target |
| Persistence | `localStorage` `loki_best_<game> = {score, date, meta}`, no account, try/catch wrapped |
| Pause | On `visibilitychange` + blur. AudioContext suspend. Resume on focus + interaction |
| Audio | Muted default. One lazy WebAudio context, 2-channel mixer, master gain 0.15, persistent toggle |
| A11y | Colourblind safe (shape + pattern + icon, never colour alone). Reduced motion cuts particles 70%. Focus rings `#7dd3e0` |
| No login | Zero backend. Share via `canvas.toDataURL` PNG or Web Share API, fallback copy |
| Palette | bg `#080c12`, card `#111a26`, border `#1e2e45`, icy `#7dd3e0`, gold `#d4b778` |
| Type | Cinzel 600 for H1–H2, Inter 400 body, JetBrains Mono meta. 13–15 px UI, 16–17 px editorial, tracking +0.02em |

### Quality gates
- First paint <1.2 s on 3G; canvas ready <200 ms after
- All games pause/resume without state loss
- Tap + keyboard parity — no mouse-only
- Audio never auto-plays; toggle in corner
- Share card 1080×1350 generated client-side, no server

## 01 FENRIR // Chain Strike — Compliance Guard-Rails
Automation fails without constraints. The wolf is your unbound workflow; chains are validation layers.

- **Chain 1 LÆDING** — 40% sweet spot, static, speed 1.0×, tutorial
- **Chain 2 DROMI** — 20% sweet spot, speed 1.4×, requires timing
- **Chain 3 GLEIPNIR** — 12% sweet spot, drifts sinusoidally ±18% on X, speed 1.8×, mastery
- Pendulum `x = sin(t * speed) * amplitude`; hit-window check on tap
- Hit = −33% chain integrity (3 clean hits break a chain). Miss = chain reforms +10%, 6 px screen shake, rattle SFX
- All 3 chains in ~90 s; fail if the timer expires
- **Scoring:** 100 base per hit + 50 perfect (centre 40% of green) + time bonus (remaining sec × 2). Max ~750. Perfect run = **Gleipnir Unbound** badge
- **Juice:** green flash + rune burst, 12 chain fragments with gravity 0.3, amber shake 120 ms on miss, growl pitch rises per chain, final howl + slow-mo shatter 0.4 s
- **Tech:** sin wave (no physics engine), sweet spot as % of canvas width, `driftX = sin(t*0.7)*18`, AABB overlap, particle pool 60 max
- **CTA:** "Constraints make power usable. Your SOPs are Gleipnir — invisible, light, unbreakable."

## 02 JORMUNGANDR // Serpent Memory — Integration & Routing Loops
Every app you connect is a rune on the World Serpent. Forget the order, you create a dead loop.

- 4 rune nodes on the spine: ᚠ ᚢ ᚦ ᚨ, each with its own colour + tone (C-E-G-A)
- Sequence starts length 3. Show phase: 600 ms lit + 200 ms gap. Input timeout 1.5 s per press
- Correct: cyan tracer travels the full circle, +1 length. Wrong: dead-end loop animation, hiss, −1 life
- 3 lives, max level 12, seeded RNG for shareability. Level 8+ adds simultaneous dual-rune chords
- **Scoring:** level × 100 + streak² × 10 → 1200 + streak at level 12
- **Tech:** circle math for node positions, WebAudio oscillator with gain envelope 0.01→0.2→0.001 over 0.6 s, Fehu 261 Hz / Uruz 329 Hz…, 72 px mobile hit areas
- **CTA:** "Systems only work in order. Your Zapier is a serpent — respect the sequence."

## 03 HEL // Soul Sorting — Triage / Realm-Routing (funnel anchor)
Not every soul deserves Helheim. Not every task deserves you.

- Orb spawns centre with a label ('VIP refund?', 'Cold lead?', 'Invoice $5k?') and a countdown ring
- Swipe Left = Automate, Right = Keep Human. Keys A/D. Touch threshold 60 px
- Correct: pile grows, essence +10. Wrong: wobble, essence −10, wail
- 10 waves × 8 souls = 80 decisions; speed ramps 5.0 s → 2.0 s linearly
- Wave 4+ ambiguous souls ('Angry VIP?' → Human). Wave 7+ double orbs
- Live metrics: Souls/Min, Accuracy %, Essence
- **Scoring:** essence 0–800 + accuracy × 2 + speed bonus. S rank needs 90%+ accuracy
- **Tech:** soul queue array, rAF delta spawn interval, pointer-event swipes (no hammer.js), piles as DOM transforms, conveyor CSS animation paused on visibilitychange
- **CTA:** "80% automate, 20% human = Hel's balance. Your inbox is the river Gjöll — build a bridge."

## 04 SLEIPNIR // Eight-Legged Sprint — Cross-System Relay / Parallel Execution
One system = slow. Parallel = godlike.

- Endless runner through the Yggdrasil trunk, 4 lanes (later 8 visually), aurora canopy
- Auto-run. Speed starts 6 units, +2% per 10 s, cap 14
- Split powerup (Odin's eye) = dual-lane mode 3 s, control 2 ghosts, +50% multiplier, double coins
- Root walls block 1–2 random lanes. Coin magnet every 30 s for 4 s. Death on wall hit, distance-based
- **Scoring:** `floor(dist*1.2 + coins*10*multi)`, multiplier 1× / 1.5× parallel / 2× magnet+parallel
- **Controls:** Arrows or swipe to switch lanes; hold Space to keep parallel (drains 20%/s without powerup); mobile taps left/right half
- **Tech:** `x = laneIndex * laneWidth`, obstacle pool of 20 recycled, AABB lane check, no physics engine
- **CTA:** "Stop running on one leg. Parallelize: form → sheet → email → CRM in one ride."

## 05 RUNE CAST // Daily Oracle — Reflective / Streak Loop
Retention mechanic, no fail state, the shareable moment.

- One cast per day (client date check, trust + streak, no enforcement)
- Seed = `YYYY-MM-DD` hash → deterministic shuffle, **same draw for every player that day**
- Draw 3: Past (system to audit), Present (where the bottleneck lives), Future (what to automate next)
- Each rune: name, phonetic, symbol, business meaning (e.g. Fehu (Fay-hoo) = wealth systems, liquid flow)
- Reveal staggered 0 / 600 / 1200 ms with stone-grind SFX
- Shareable card 1080×1350 via offscreen `canvas.toDataURL` — gold foil, runes, date, lesson
- Streak counter + weekly reflection prompt. 7-day streak = 'Seer' border, 30-day = gold ink
- **Tech:** `cyrb53(dateStr)` → mulberry32 RNG, 24-rune array, 120-point particle system, no external libs
- **CTA:** "Divination is just pattern recognition with myth. Your business has runes — learn to read them."

## 99 // FUNNEL
`PLAY (1–3 min micro-game) → LEARN (business lesson on the end screen) → DEITY PAGE (17 lessons) → GUMROAD ($29 workflow template)`

| Deity | Game | Lessons | Workflow hook |
|---|---|---|---|
| Fenrir | Chain Strike | Guard-rails, validation, compliance | SOP checker template |
| Jormungandr | Serpent Memory | Routing, sequencing, API order | Zapier flow map |
| Hel | Soul Sorting | Triage, prioritisation, human-in-loop, SLA, queue theory | Inbox triage OS |
| Sleipnir | Eight-Leg Sprint | Parallelism, relay, throughput | Multi-channel CRM |
| Rune Cast | Oracle | Reflection, pattern, daily review | Daily CEO ritual sheet |

### Implementation order (bible's own ranking)
1. **HEL** — highest business value, simplest loop, validates the funnel
2. **FENRIR** — sin wave only, juicy timing core, shows polish
3. **RUNE CAST** — particles + seeded RNG, retention + shareability, zero fail state
4. **JORMUNGANDR** — sequence + WebAudio, the audio design moment
5. **SLEIPNIR** — lane pool + powerup, most complex

## Build status against this bible (2026-08-12)
- ✅ `games/engine.js` **v2** implements all of 00 // CORE: state machine, 32 ms dt clamp,
  pause on visibilitychange **and** blur with AudioContext suspend, Esc/P pause, M mute,
  persistent muted-by-default toggle, master gain 0.15, `loki_best_<id>` JSON `{score,date,meta}`
  with v1 integer back-compat, reduced-motion particle cut, focus rings, real 1080×1350
  share card with grain + foil gradient via `toDataURL`, Web Share API with download fallback.
- ✅ `games/fenrir.html` matches §01 exactly: 0.40/0.20/0.12 windows at 1.0×/1.4×/1.8×,
  −100/3 per hit, +10% miss reform, 90 s limit, perfect = centre 40% (+50), time bonus ×2,
  Gleipnir sinusoidal drift, Gleipnir Unbound badge, HUD timer.
- ⏳ Hel / Jormungandr / Sleipnir / Rune Cast still on v1 mechanics — next loop ticks.
- Verified by `tests/play_games_cdp.py` (34 assertions, real Chrome, real clicks).
