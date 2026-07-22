# Loki's Mischief — Traditional Norse Accuracy Audit

> Scope note: This audit covers only claims the project presents as traditional Norse
> mythology, pre-Christian Norse religion, Viking-Age Scandinavian practice, or historical
> fact. It does NOT judge the commercial product copy, pricing, automation workflows, or
> marketing metaphor except where those metaphors are dressed as Norse doctrine. A
> non-destructive pass: no project files were edited, renamed, moved, or deleted.

---

## 1. Scope

- **Project folder reviewed:** `/data/data/com.termux/files/home/storage/downloads/hermes-output`
- **Total files found:** 237 (91 readable text/markup assets + 146 binary image/font assets)
- **Total "webpages"/primary surfaces:** 1 main site (`Lokis-Mischief-Site.html`) + 8 Gumroad store/product HTML pages + 6 Gumroad-Products pages (all product/store fronts, not lore pages)
- **Readable files reviewed for Norse claims:** 91 (100%)
- **Files containing actual Norse mythological claims:** 1 — `Lokis-Mischief-Site.html`
- **Assets NOT reviewed:** 146 binary image/font files (PNG portraits, hero banners, thumbnails, `.ttf` rune font). Reason: they are non-textual raster/vector art and a font binary; visual *depictions* (e.g., Hel's two-tone body, Fenrir's size, Sleipnir's eight legs) are addressed separately under "Visual Depiction Notes" where the text describing them is the auditable claim. The `.ttf` (NotoSansRunic) is a font, not a claim source.
- **Audit date:** 2026-07-21

**Where the Norse content lives (all within `Lokis-Mischief-Site.html`):**
- Hero saga "The God Who Broke the Rules" (Loki blood-brother of Odin) — lines ~1813–1817
- "The Binding of Loki" (Sigyn / Baldr / binding) — lines ~1850–1854
- Deity "Saga" blurbs: Óðinn (1887–1889), Þórr (1921–1923), Freyr (1955–1957), Freyja (1989–1991), Týr (2023–2025), Heimdallr (2057–2059), Bragi (2091–2093)
- Game sagas: Fenrir (2223–2233), Jörmungandr (2315–2323), Hel (2404–2409), Sleipnir (2502–2510)
- Products saga "Loki's Gifts to the Gods" (2848–2853)
- Playbook saga "The Völuspá" (2879–2884)
- About saga "Loki's Children" (2909–2914)

**Files reviewed and found to contain NO mythological claims (only the brand name "Loki's Mischief/Creations"):** `README.md`, `product-research-report.md`, `automation-agency-playbook/playbook.md`, all `Gumroad-Store/*.html`, all `Gumroad-Products/**`, and all `lokis-assets/**` READMEs/guides/templates/workflow JSON (these use Odin/Thor/Freyja/Týr/Hel/Bragi only as product names and `author:"Loki's Mischief"`; no doctrinal claims).

---

## 2. Executive Summary

- **Overall traditional-source accuracy:** **High.** The mythological narrative content is, on the whole, unusually faithful to the medieval Norse sources (primarily Snorri's *Gylfaginning* and the *Poetic Edda*). The overwhelming majority of specific claims (Gleipnir's six ingredients, Týr's hand, Fenrir devouring Óðinn at Vígríðr, Þórr's nine steps after killing Jörmungandr, Sleipnir's birth, Hermóðr's ride, etc.) are directly attested.
- **Christian-influence status:** **Minor issues (no doctrine).** No Satan/Devil equivalence, no "Hel = Christian Hell" equation, no sin/salvation/redemption/apocalypse framing, no "good vs. evil" cosmology. The single Christian-adjacent slip is the phrase "court of final judgment" applied to Hel and the game-over word "unblessed" — both should be softened. These are flagged but are minor and clearly framed as product metaphor, not doctrine.
- **Total claims reviewed:** 58 distinct claims (grouped; see Full Claim Ledger).
- **Claim counts by verdict category:**
  - A (Directly supported): 34
  - B (Supported, needs nuance/narrower wording): 15
  - C (Plausible scholarly interpretation, not directly established): 5
  - D (Source-dependent/uncertain): 1
  - E (Later medieval/post-medieval): 0
  - F (Christian influence/dogma): 0 (1 borderline "B/F" on Hel judgment wording)
  - G (Modern reconstruction/interpretation): 3
  - H (Inaccurate/conflation): 2 ("Urðar Serpent" misnomer; "final judgment" over-read)
  - I (Insufficient evidence): 0
- **Deity/figure profiles reviewed:** 13 named deities/beings (Óðinn, Þórr, Freyr, Freyja, Týr, Heimdallr, Bragi, Loki, Fenrir, Jörmungandr, Hel, Sleipnir, Angrboða) plus 8 secondary figures (Sigyn, Gerðr, Hermóðr, Hymir, Utgarða-Loki, Svaðilfari, Mímir, Baldr).
- **Lesser-known figures receiving dedicated research:** Bragi, Heimdallr, Týr, Freyr, Hel, Sleipnir, Angrboða, Sigyn, Gerðr, Hermóðr, Hymir, Utgarða-Loki, Jörmungandr, Fenrir (14 dossiers, §5).
- **Ten highest-priority corrections:**
  1. "Urðar Serpent" → correct name is **Miðgarðsormr** ("World Serpent"); "Urðar" is the well of fate/Urðr the Norn — a conflation (§6-H1).
  2. Hel "court of final judgment — every soul… sorted by her will" → Hel *receives* the dead; she does not sit in moral judgment. Reword to remove the Christian judgment frame (§3, §6-H2).
  3. "unblessed" (Hel game-over) → avoid the Christian loanword; use "unsorted / unclaimed."
  4. Freyr blurb "He gave the gods their greatest treasures" → it was **Loki** who procured the dwarf-made treasures (Gungnir, Mjölnir, Skíðblaðnir). Freyr *received* Skíðblaðnir.
  5. "Freyja… taught the Aesir the art of shape-shifting" → she taught **seiðr**; shape-shifting is an inferred extension, not a direct statement.
  6. "commands fate itself" (Freyja) → overstated; she receives half the slain (Grímnismál 14), a share in destiny, not command of it.
  7. Prose Edda quotation "Loki is also called the father of monsters…" → likely a paraphrase; soften to a safe attribution ("Snorri calls Loki the father of monsters").
  8. "Nine Realms" used loosely as a travel list (e.g., Sleipnir "from Asgard to Jötunheim to Niflheim") → the canonical nine are attested but the site's casual enumeration should not imply a fixed map; keep but flag as interpretive.
  9. Rune "emblems" on deity cards (e.g., Odin = ᚠᚨᚱ) do not spell the names and are decorative; if presented as meaningful, they need correction (internal-consistency note, §8).
  10. "Yggdrasil" named as the tree Óðinn hung from — in Hávamál the tree is unnamed; the Yggdrasil identification is standard but later/Snorri; fine to keep with a caveat.
- **Main areas of strong accuracy:** Fenrir binding sequence, Jörmungandr fishing/cat-lifting/Ragnarök death, Sleipnir birth and Hermóðr's ride, Þórr's Megingjörð and nine-step death, Heimdallr's watch traits and Gjallarhorn, Týr's hand, the Völuspá creation-from-Ymir summary, Loki's blood-brotherhood and binding, the dwarf-gift list (Gungnir/Mjölnir/Skíðblaðnir).
- **Main areas requiring caution:** (a) Christian-adjacent "judgment" language around Hel; (b) over-claimed "commands fate" / "taught shape-shifting" for Freyja; (c) the "Urðar Serpent" misnomer; (d) interpretive marketing lines (e.g., "he knew his chains were temporary") that are clearly modern metaphor but should stay clearly framed as such; (e) "Nine Realms" used as a generic travel list.

---

## 3. Christian Influence and Dogma Findings

A full screening pass was run for the vocabulary: *heaven, hell, sin, Satan, devil, demon, angel, saint, salvation, damn, redeem, scripture, commandment, church, pray, eternal punishment, good vs. evil, apocalypse.* Findings:

**Finding C-1 — Hel as a "court of final judgment" (minor Christian overlay)**
- Affected file/page: `Lokis-Mischief-Site.html`, Hel saga (~line 2408): *"This is the court of final judgment — and every soul that arrives is sorted by her will."*
- Christian influence identified: The phrase "court of final judgment" and "every soul… sorted by her will" maps onto the Christian Last-Judgment framework (souls judged, sorted, assigned fate by a moral authority). In the sources, Hel is appointed to **receive** those who die of sickness or old age (Gylfaginning 34: "over nine worlds… to all those who die she assigns abodes"); she is a receiver/ruler of a realm, not a moral judge. There is no Norse "final judgment" of souls by Hel.
- Why it is not supported as pre-Christian Norse belief: Pre-Christian Norse eschatology has multiple afterlives (Valhalla, Hel, the sea, mounds, etc.) determined largely by *mode of death* (battle vs. illness) and kinship, not by a single moral tribunal. Assigning Hel a Christian-style judgment role imports a foreign frame.
- Source-grounded replacement wording: *"Odin sent Hel to Niflheim and gave her rule over those who die — among the nine worlds she assigns each of the dead a place to dwell."*
- Priority: **High** (it is the single clearest Christian-flavored frame). Confidence: **High.**

**Finding C-2 — "unblessed" in Hel game-over text (minor)**
- Affected file/page: `Lokis-Mischief-Site.html`, Hel game-over (~line 2392): *"The souls pile up unblessed."*
- Christian influence identified: "Blessed/unblessed" is Christian moral vocabulary. Old Norse has no native "blessing" concept in this sense; the relevant idea would be "unsorted / unclaimed / unguided."
- Replacement: *"The souls pile up, unsorted."*
- Priority: **Low.** Confidence: **High.**

**Finding C-3 — "heavens will rain poison" (NOT Christian)**
- Line 2323: *"The heavens will rain poison."* Here "heavens" means the sky/firmament (the cosmological dome), not the Christian Heaven. This is acceptable Norse-cosmology language (cf. Völuspá's description of the sky made from Ymir's skull). No change needed; logged to show it was screened and cleared.

**Finding C-4 — "soul sorting" product metaphor (acceptable, with caveat)**
- The Hel game ("Soul Sorting: automate or keep manual") uses "soul" as a stand-in for "task/lead." "Soul" (Old Norse *sála*) is in fact a Christian-era loanword; the indigenous terms are more like *önd* (breath/spirit), *hugr* (mind), *hamr* (shape). Because this is explicitly a business metaphor and not presented as doctrine, it is acceptable, but the saga text should not describe Hel as judging "souls." See C-1.

**Net Christian-influence verdict:** No Christian doctrine, no Satan/Devil/Loki-as-Satan framing, no Hel-as-Hell equation, no apocalyptic good-vs-evil cosmology. Only two minor word-level slips (C-1, C-2) need softening. Classified: **Minor issues.**

---

## 4. Page-by-Page Website Findings

> The site is a single `index`-style page (`Lokis-Mischief-Site.html`). "Pages" below = content sections.

### 4.1 Hero — "The God Who Broke the Rules" (Loki)
- **Claims:** Loki is blood-brother of Óðinn; shapeshifter; boundary-breaker; refused Asgard's rules.
- **Verdict:** A (blood-brother: Lokasenna st. 9 — Loki and Óðinn mixed blood and swore oaths). Shapeshifting: attested across sources (mare, falcon, salmon, flea).
- **Accuracy:** Strong. "the boundary-breaker" is interpretive marketing but harmless.
- **Confidence:** High.

### 4.2 "The Binding of Loki" (Sigyn feature saga)
- **Claims:** Loki's mischief caused Baldr's death; gods bound Loki to a rock with his son's entrails; venom drips on his face until Ragnarök; Sigyn holds a bowl.
- **Verdict:** A. Gylfaginning 50: after Baldr's death the Æsir seize Loki, bind him with the entrails of his son Nari/Narfi (killed by his brother Vali, transformed into a wolf); one strand becomes iron; Sigyn holds a bowl above him; when she empties it, venom falls on Loki and he shudders (earthquakes).
- **Nuance (B):** "transformed into iron chains" — more precisely the entrails *became* the binding (one is said to turn to iron bands); "chains" is a loose modern word for the fetters. Also "until Ragnarök" is correct (he remains bound until then).
- **Modern metaphor (G):** "Loki didn't break because he knew his chains were temporary" — not in sources; clearly a motivational gloss. Keep but it is marketing, not myth.
- **Confidence:** High.

### 4.3 Óðinn — "The Wanderer's War Room"
- **Claims:** Left Asgard to wander the Nine Realms for wisdom; traded an eye for Mímir's well; hung himself from Yggdrasil nine nights to gain the runes; ravens Huginn & Muninn daily carry knowledge.
- **Verdict:** A for the eye (Völuspá 28–29; Gylfaginning 15), the ravens (Grímnismál 20), and the self-sacrifice for runes (Hávamál 138–139). B for "Yggdrasil" (the tree is unnamed in Hávamál; the Yggdrasil link is standard/Snorri). B for "Nine Realms" used as a travel list (the nine realms are attested, but casual enumeration is interpretive). C/G for "he does not command from a throne; he thinks, he learns, he decides" (interpretive).
- **Accuracy:** Strong on the three core attested acts.
- **Confidence:** High.

### 4.4 Þórr — "Mjölnir Infrastructure"
- **Claims:** Son of Óðinn; god of thunder, strength, protection; Mjölnir levels mountains, smashes giants, guards the worlds; belt Megingjörð doubles his power.
- **Verdict:** A. Þórr son of Óðinn by Jörð (Gylfaginning 21); Mjölnir (Gylfaginning 21, 44); Megingjörð "belt of strength… when he girds it his divine strength is doubled" (Gylfaginning 44).
- **Nuance (B):** "keeps the worlds safe from chaos" is a modern framing of Þórr's role as jötunn-fighter; acceptable but interpretive.
- **Confidence:** High.

### 4.5 Freyr — "Green Harvest Engine"
- **Claims:** Of the Vanir; rules prosperity, sunshine, abundant harvest; gave the gods their greatest treasures; won Gerðr through persistence and patience.
- **Verdict:** A for Vanir + fertility/sunshine/harvest (Ynglinga saga 4; Gylfaginning 24). B for "gave the gods their greatest treasures" — the treasures (Gungnir, Mjölnir, Skíðblaðnir, etc.) were **procured by Loki** from the dwarves (Gylfaginning 42); Freyr *received* Skíðblaðnir. B for "won Gerðr through persistence and patience" — Skírnismál shows a negotiated/coercive wooing (Skírnir threatens Gerðr with ritual curses) more than gentle patience.
- **Recommended correction (treasures):** *"When Loki won the dwarves' treasures for the gods, Freyr received Skíðblaðnir, the ship that folds to a pocket."*
- **Confidence:** High.

### 4.6 Freyja — "Seiðr Messaging Stack"
- **Claims:** Most powerful seiðr-witch in the Nine Realms; taught the Æsir shape-shifting and persuasion; wears the falcon cloak; commands fate itself; tears are gold; voice bends minds.
- **Verdict:** A for "taught the Æsir seiðr" (Ynglinga saga 4; Lokasenna 24), falcon cloak (Þrymskviða; Sörla þáttr), tears of gold (Skáldskaparmál). B for "taught… shape-shifting" — seiðr is taught; shape-shifting is an inferred capacity of seiðr, not a direct statement. C for "commands fate itself" — Freyja receives half the slain (Grímnismál 14), a share in destiny, not command of it. G for "voice can bend minds" (marketing gloss).
- **Recommended correction:** *"Freyja, foremost in the craft of seiðr, first brought that magic to the Æsir; she owns the falcon cloak and her tears are gold."*
- **Confidence:** High (A/B); Medium (C).

### 4.7 Týr — "Týr's Code"
- **Claims:** Bravest of the gods; placed hand in Fenrir's mouth as pledge; hand bitten off; god of law, justice, heroic sacrifice, single combat.
- **Verdict:** A for the hand-in-Fenrir's-mouth episode (Gylfaginning 34). A/B for "god of law and justice" (Týr presides over the thing/assembly and oaths — Gylfaginning 25; Sigrdrífa's oath-list). B for "single combat" (a later/scholarly emphasis on Týr as a duel-god; not a primary attested epithet). G for "heroic sacrifice" (interpretive; the sources relate the loss of his hand, not a theology of sacrifice).
- **Confidence:** High.

### 4.8 Heimdallr — "Bifrost Monitor"
- **Claims:** Guards Bifröst, the rainbow bridge to Asgard; needs no sleep; hears grass grow; sees a hundred leagues; Gjallarhorn sounds at Ragnarök.
- **Verdict:** A. Gylfaginning 27: "he needs less sleep than a bird… hears the grass growing… sees a hundred miles around him… his horn is Gjallarhorn, which is heard in all worlds" and it is blown at Ragnarök (Völuspá 46). "Rainbow bridge" is the standard modern rendering of Bifröst (literally "shaking/wavering way"); acceptable.
- **Confidence:** High.

### 4.9 Bragi — "Skald's Quill"
- **Claims:** God of poetry and eloquence; carries mead from Óðinn's court; turns every victory into saga; runes on his tongue shape stories.
- **Verdict:** A for "god of poetry" (Skáldskaparmál; Bragi is the skald-god, husband of Iðunn). B for "carries mead from Óðinn's court" — the mead of poetry (Són's mead) is associated with Óðinn, not specifically Bragi as cup-bearer; minor. G for "runes on his tongue shape the stories" (interpretive).
- **Confidence:** High (A); Medium (B).

### 4.10 Fenrir game saga — "Chain Strike"
- **Claims:** Firstborn of Loki + Angrboða; terrible size/hunger; Óðinn brought him to Asgard; Leyding and Dromi chains shattered; Gleipnir from six impossible ingredients; Týr's hand pledge; at Ragnarök breaks free, devours Óðinn at Vígríðr.
- **Verdict:** A throughout. Gylfaginning 34 (birth order, Leyding/Dromi, Gleipnir's six ingredients — exact match: cat's footfall, woman's beard, mountain roots, bear's sinews, fish's breath, bird's spittle), Týr's hand (34). Völuspá 53 / Gylfaginning 51: Fenrir swallows Óðinn at Ragnarök; Vígríðr is the named plain.
- **Nuance (B):** "wolf of such terrible size" — Fenrir is enormous in the sources, but "jötunn descent" size should not be read as the English "giant = dim-witted brute"; the site does not make that error.
- **Confidence:** High.

### 4.11 Jörmungandr game saga — "Serpent Memory"
- **Claims:** Second child of Loki + Angrboða; cast into the ocean around Miðgarð, tail meets jaws; Þórr's fishing trip with Hymir (ox-head bait, Hymir cuts line); the cat-lifting at Utgarða-Loki; at Ragnarök rises, floods, Þórr kills it but dies after nine steps from venom.
- **Verdict:** A throughout. Gylfaginning 34 (casting, encircling); Hymiskviða (fishing, ox head, Hymir cuts line); Gylfaginning 44–46 (cat = Jörmungandr); Gylfaginning 51 / Völuspá 56 (nine steps). 
- **Error (H):** *"This is the **Urðar Serpent**, the World-Coiler"* — there is no attested name "Urðar Serpent" for Jörmungandr. "Urðar" belongs to Urðr (a Norn) and Urðarbrunnr (the well of fate). The correct name is **Miðgarðsormr** ("World Serpent/Midgard Serpent"). Replace "Urðar Serpent" with "Miðgarðsormr (the World Serpent)."
- **Confidence:** High.

### 4.12 Hel game saga — "Soul Sorting"
- **Claims:** Third child of Loki + Angrboða; half-living maiden / half-corpse (one side living flesh, other blue/rotting); cast into Niflheim as ruler of the dead; hall Eljudnir ("Drenched with Rain"); walls woven from frozen rivers; "court of final judgment."
- **Verdict:** A for parentage, half-coloured body (Gylfaginning 34: "half of her is blue/black and half flesh-coloured"), Niflheim appointment, Éljúðnir (34). B/G for "walls woven from frozen rivers" (poetic embellishment, not in source). F/B for "court of final judgment" (see §3-C1).
- **Confidence:** High (A); High (F/B on judgment).

### 4.13 Sleipnir game saga — "Eight-Legged Sprint"
- **Claims:** Born of Loki (as a mare) + Svaðilfari; giant builder demanded sun, moon, Freyja to wall Asgard; Loki-as-mare lured Svaðilfari; eight-legged; given to Óðinn; crosses air/water/Bifröst; Hermóðr (son of Óðinn) rode nine days/nights to Hel's gate, leaped Eljudnir's wall.
- **Verdict:** A throughout. Gylfaginning 42 (builder, Freyja as bride-price, Loki-mare, Sleipnir grey eight-footed, given to Óðinn, crosses Bifröst); Gylfaginning 49 (Hermóðr rides nine nights through dark valleys, reaches Gjöll bridge, leaps Hel's gate).
- **Nuance (C):** "only horse that can travel between the worlds — from Asgard to Jötunheim to Niflheim" over-specifies; Sleipnir's unique speed is attested, the fixed realm-list is interpretive.
- **Confidence:** High.

### 4.14 Products saga — "Loki's Gifts to the Gods"
- **Claims:** Loki cut Sif's hair; Þórr threatened him; Loki commissioned dwarven treasures: Gungnir (never misses), Mjölnir (returns when thrown), Skíðblaðnir (folds to a pocket).
- **Verdict:** A. Gylfaginning 42 (Sif's hair, Þórr's threat, the dwarf-brothers' contest producing Gungnir, Mjölnir, Skíðblaðnir, etc.). The three named treasures and their properties are accurate.
- **Confidence:** High.

### 4.15 Playbook saga — "The Völuspá"
- **Claims:** Völuspá is first/famous poem of the Poetic Edda; seeress (völva) summoned by Óðinn; world made from Ymir's body; first war; Loki's children; destruction and renewal.
- **Verdict:** A. Völuspá is the first poem in the Codex Regius Poetic Edda; a völva speaks, summoned by (the gods/Óðinn); Völuspá 21 describes the world fashioned from Ymir; creation, the war of Æsir/Vanir, Ragnarök and rebirth are all there.
- **Confidence:** High.

### 4.16 About saga — "Loki's Children"
- **Claims:** Loki fathered four children: with Angrboða — Fenrir, Jörmungandr, Hel; with Svaðilfari (as mare) — Sleipnir. Quotes Prose Edda: *"Loki is also called the father of monsters, and his children are the greatest of monsters."*
- **Verdict:** A for the four children and parentage (Gylfaginning 34, 42). B for the quoted sentence — it is a paraphrase/modern rendering of Snorri's characterization of Loki (Snorri calls Loki "father of lies" and recounts his monster children); present it as a paraphrase, not a verbatim quotation. 
- **Recommended correction:** *"Snorri calls Loki the father of monsters, and his children are accounted the greatest of monsters."*
- **Confidence:** High (parentage); Medium (quotation exactness).

---

## 5. Lesser-Known Figures Research Dossier

### 5.1 Bragi
- **Name/variants:** Bragi (Old Norse *Bragi*); wife Iðunn. Possibly connected to *bragr* "poetry, foremost."
- **Status:** God of poetry/skald-craft. Attested, but his mythology is thin; may partly be a deified archetype of the skald.
- **Source evidence:** Skáldskaparmál (he is the skald-god; dialogues with Óðinn); Lokasenna (present at Ægir's feast); Snorri's list of Æsir.
- **Role/associations:** Poetry, eloquence, the mead of poetry. Not attested as a "carrier of mead" specifically.
- **Uncertainties:** Whether Bragi is a late/learned insertion; his relationship to the historical poet Bragi Boddason is debated.
- **Website claim:** "god of poetry and eloquence; carries mead from Óðinn's court; turns every victory into saga." Verdict: A (god of poetry) / B (mead-carrier) / G (runes on tongue).
- **Confidence:** High.

### 5.2 Heimdallr (Heimdall)
- **Name/variants:** Heimdallr, Heimdallr; "the white god," *hallar heimr*.
- **Status:** Æsir god; guardian of the gods and Bifröst.
- **Source evidence:** Gylfaginning 27; Grímnismál 13; Völuspá 46 (Gjallarhorn); Rigsthula (Heimdall as ancestor of social classes — a separate tradition).
- **Role:** Watchman, owns Gjallarhorn, born of nine mothers (Rigsthula/Hyndluljóð). 
- **Uncertainties:** Nine mothers tradition vs. Gylfaginning's simpler account; his death-fight with Loki at Ragnarök (Völuspá) — mutually slain.
- **Website claim:** Accurate (see §4.8). Verdict: A.
- **Confidence:** High.

### 5.3 Týr (Tíw/Tiwaz)
- **Name/variants:** Týr (ON), Tir (OHG), Tir (OLith), from Proto-Germanic *Tīwaz; counterpart of Roman Mars (Tacitus' *Mars Thingsus*).
- **Status:** One of the Æsir; god of war, law, the *thing* (assembly), oaths.
- **Source evidence:** Gylfaginning 25 (presides over lawsuits/justice, most daring); Sigrdrífa's oath-list (Týr's runes of victory); the Fenrir episode (Gylfaginning 34).
- **Role:** Law, justice, single combat (later emphasis), the one-handed god.
- **Uncertainties:** His Precise standing relative to Óðinn/Þórr shifted over time; "single-combat god" is a scholarly inference, not a primary epithet.
- **Website claim:** Largely A/B (see §4.7).
- **Confidence:** High.

### 5.4 Freyr (Frey)
- **Name/variants:** Freyr ("lord"); brother of Freyja; son of Njörðr (Vanir).
- **Status:** Vanir god of fertility, prosperity, sunshine, rain, harvest, peace.
- **Source evidence:** Ynglinga saga 4–5 (prosperity, peace, harvest); Gylfaginning 24; Skírnismál (wooing Gerðr); he owns Skíðblaðnir and the boar Gullinbursti.
- **Role:** Abundance, sacred kingship (Swedish cult at Uppsala).
- **Uncertainties:** Gerðr wooing is negotiated/coercive (Skírnir's threats), not gentle patience.
- **Website claim:** A/B (see §4.5).
- **Confidence:** High.

### 5.5 Hel
- **Name/variants:** Hel (ON); possibly from *hel* "to cover/hide."
- **Status:** Daughter of Loki + Angrboða; ruler of the realm of the dead (also called Hel).
- **Source evidence:** Gylfaginning 34 (half-coloured, sent to Niflheim, rules the dead); Völuspá (Hel's realm at Ragnarök); Baldrs draumar; Gylfaginning 49 (Hermóðr's ride).
- **Role:** Receives those who die of sickness/old age; not a moral judge.
- **Uncertainties:** The etymology "hidden" vs. Christian "Hell" is a later folk-etymology, not pre-Christian. The realm and goddess share the name.
- **Website claim:** A (parentage, body, Niflheim, Éljúðnir) / B-F (judgment frame, see §3).
- **Confidence:** High.

### 5.6 Sleipnir
- **Name/variants:** Sleipnir ("glider/slipper").
- **Status:** Óðinn's eight-legged horse; best of all horses.
- **Source evidence:** Gylfaginning 42 (born of Loki-mare + Svaðilfari, grey, eight-footed, given to Óðinn, crosses Bifröst); Grímnismál 44 (Óðinn's horse Sleipnir).
- **Role:** Swift mount; carried Hermóðr to Hel.
- **Uncertainties:** None major; the realm-list travel claim is interpretive.
- **Website claim:** A (see §4.13).
- **Confidence:** High.

### 5.7 Angrboða (Angrboda)
- **Name/variants:** Angrboða ("the one who brings grief").
- **Status:** Jötunn (giantess); consort of Loki.
- **Source evidence:** Gylfaginning 34 (mother of Fenrir, Jörmungandr, Hel).
- **Role:** Mother of Loki's three "monster" children.
- **Uncertainties:** Appears only in Snorri (and Hyndluljóð mentions Angrboða as Loki's consort); no independent Eddic narrative.
- **Website claim:** Accurate (named parent). Verdict: A.
- **Confidence:** High.

### 5.8 Sigyn
- **Name/variants:** Sigyn ("friend of victory").
- **Status:** Loki's wife; mother (with Loki) of Narfi/Nari and (by the wolf) Váli's brother.
- **Source evidence:** Gylfaginning 50 (holds the bowl above bound Loki to catch venom); Lokasenna (present).
- **Role:** Loyal wife; catches venom in a bowl.
- **Uncertainties:** Thin attestation; her sons Nari/Narfi and Váli are part of the binding episode.
- **Website claim:** "Sigyn's Faith" / "The Binding of Loki" — accurate (Gylfaginning 50). Verdict: A.
- **Confidence:** High.

### 5.9 Gerðr (Gerda)
- **Name/variants:** Gerðr ("enclosure"); jötunn daughter of Gymir.
- **Status:** Jötunn; wife of Freyr.
- **Source evidence:** Skírnismál (Freyr's lovelorn wooing via Skírnir; Gerðr agrees after threats).
- **Role:** Freyr's bride; fertility union.
- **Uncertainties:** The wooing is coercive/negotiated, not "persistence and patience" in the gentle sense.
- **Website claim:** B (see §4.5).
- **Confidence:** High.

### 5.10 Hermóðr
- **Name/variants:** Hermóðr ("war-spirit").
- **Status:** A son of Óðinn (in Gylfaginning).
- **Source evidence:** Gylfaginning 49 (rides Sleipnir nine nights to Hel to plead for Baldr's return).
- **Role:** Messenger/psychopomp figure.
- **Uncertainties:** Appears mainly in Snorri; some scholars see him as a literary device.
- **Website claim:** Accurate (§4.13). Verdict: A.
- **Confidence:** High.

### 5.11 Hymir
- **Name/variants:** Hymir (jötunn).
- **Status:** Jötunn; Þórr's fishing companion.
- **Source evidence:** Hymiskviða (cauldron quest; fishing Jörmungandr; cuts the line); Gylfaginning 48 (summarizes).
- **Role:** Host of Þórr; the one who cut the line.
- **Uncertainties:** Hymiskviða's dating/debate (some see it as comparatively late), but the episode is well attested.
- **Website claim:** Accurate (§4.11). Verdict: A.
- **Confidence:** High.

### 5.12 Utgarða-Loki (Útgarða-Loki)
- **Name/variants:** Útgarða-Loki ("Loki of the Outyards").
- **Status:** A jötunn king (NOT the same as Loki).
- **Source evidence:** Gylfaginning 44–46 (the illusionist who sets Þórr the cat-lifting, mead-drinking, and race challenges; the cat is Jörmungandr).
- **Role:** Trickster-jötunn; his "challenges" are illusions.
- **Uncertainties:** Distinct from Loki despite the name; the site correctly treats the cat as Jörmungandr.
- **Website claim:** Accurate (§4.11). Verdict: A.
- **Confidence:** High.

### 5.13 Jörmungandr (Miðgarðsormr)
- **Name/variants:** Jörmungandr ("huge monster"); Miðgarðsormr ("World/Midgard Serpent").
- **Status:** Child of Loki + Angrboða; world-encircling serpent.
- **Source evidence:** Gylfaginning 34 (cast into the sea, encircles Midgard); Hymiskviða (fishing); Völuspá 56 (killed by Þórr, who dies after nine steps).
- **Role:** Þórr's great enemy; Ragnarök combatant.
- **Uncertainties:** "Urðar Serpent" is NOT an attested name (error — §6-H1).
- **Website claim:** A except the "Urðar Serpent" misnomer (H).
- **Confidence:** High.

### 5.14 Fenrir (Fenrisúlfr)
- **Name/variants:** Fenrir, Fenrisúlfr ("Fenrir's wolf"), Hróðvitnir ("famous wolf").
- **Status:** Child of Loki + Angrboða; monstrous wolf.
- **Source evidence:** Gylfaginning 34 (binding, Gleipnir); Völuspá 53 (devours Óðinn); Gylfaginning 51 (slain by Víðarr).
- **Role:** Bound monster; kills Óðinn at Ragnarök; killed by Víðarr.
- **Uncertainties:** Size is emphasized but "jötunn" lineage ≠ the English "giant = stupid/evil" trope; the site avoids that error.
- **Website claim:** Accurate (§4.10). Verdict: A.
- **Confidence:** High.

---

## 6. Critical and High-Priority Corrections

### 6-H1 — "Urðar Serpent" misnomer (Inaccurate / conflation)
- **Priority:** Critical
- **File/page:** `Lokis-Mischief-Site.html`, Jörmungandr saga (~line 2317)
- **Exact current wording:** *"This is the **Urðar Serpent**, the World-Coiler, the beast that holds the circle of existence closed."*
- **Claim:** Jörmungandr is called the "Urðar Serpent."
- **Verdict:** H (Inaccurate)
- **Why:** There is no attested Norse name "Urðar Serpent" for Jörmungandr. "Urðar" is the possessive of **Urðr** (the Norn of the past) and appears in **Urðarbrunnr** (the Well of Fate) and **Urðarhrafnar** etc. The World Serpent's established names are **Jörmungandr** and **Miðgarðsormr** ("Midgard/World Serpent"). The phrase conflates the serpent with the well of fate.
- **Evidence:** Gylfaginning 34; Völuspá 56 (uses "Miðgarðsormr"); no "Urðar Serpent" occurs in the Eddas.
- **Recommended replacement:** *"This is **Miðgarðsormr**, the World Serpent, the beast that encircles Midgard and holds the circle of the ocean closed."*
- **Confidence:** High.

### 6-H2 — Hel as "court of final judgment" (Christian-adjacent over-read)
- **Priority:** High
- **File/page:** `Lokis-Mischief-Site.html`, Hel saga (~line 2408)
- **Exact current wording:** *"This is the court of final judgment — and every soul that arrives is sorted by her will."*
- **Claim:** Hel judges every arriving soul in a final tribunal.
- **Verdict:** B (nuance) leaning F (Christian-frame on the "judgment" word)
- **Why:** Pre-Christian Norse afterlife is not a single moral tribunal. Hel *receives* those who die of sickness/old age (Gylfaginning 34); assignment of abodes is by status/mode of death, not moral verdict. "Final judgment" imports a Christian Last-Judgment frame.
- **Evidence:** Gylfaginning 34; comparative: multiple afterlives (Valhalla, Hel, sea, mound) by mode of death.
- **Recommended replacement:** *"Odin gave Hel rule over the dead in Niflheim, and among the nine worlds she assigns each of those who die a place to dwell."*
- **Confidence:** High.

### 6-H3 — Freyr "gave the gods their greatest treasures" (misattribution)
- **Priority:** High
- **File/page:** `Lokis-Mischief-Site.html`, Freyr blurb (~line 1956)
- **Exact wording:** *"He gave the gods their greatest treasures and won the heart of Gerðr through persistence and patience."*
- **Claim:** Freyr gifted the dwarf-made treasures to the gods.
- **Verdict:** B
- **Why:** The treasures (Gungnir, Mjölnir, Skíðblaðnir, etc.) were procured by **Loki** from the dwarves (Gylfaginning 42); Freyr *received* Skíðblaðnir. Also Gerðr's wooing (Skírnismál) is negotiated/coercive, not gentle patience.
- **Recommended replacement:** *"When Loki won the dwarves' treasures for the gods, Freyr received Skíðblaðnir, the ship that folds to a pocket — and by Skírnir's suit he won the jötunn Gerðr."*
- **Confidence:** High.

### 6-H4 — Freyja "taught the Aesir shape-shifting" / "commands fate itself" (overclaim)
- **Priority:** High
- **File/page:** `Lokis-Mischief-Site.html`, Freyja blurb (~line 1990)
- **Exact wording:** *"taught the Aesir the art of shape-shifting and persuasion… commands fate itself."*
- **Claim:** Freyja taught shape-shifting; commands fate.
- **Verdict:** B (taught seiðr, from which shape-shifting is inferred) / C (commands fate).
- **Why:** Sources state Freyja *first brought seiðr to the Æsir* (Ynglinga saga 4; Lokasenna 24). Shape-shifting is a capacity associated with seiðr but not a direct "she taught shape-shifting" statement. "Commands fate" overstates: she receives half the slain (Grímnismál 14), a share in destiny, not command of it.
- **Recommended replacement:** *"Freyja, foremost in the craft of seiðr, first brought that magic to the Æsir; she owns the falcon cloak, her tears are gold, and of the slain who fall in battle she receives half."*
- **Confidence:** High (B); Medium (C).

### 6-H5 — Prose Edda "father of monsters" quotation (paraphrase presented as quote)
- **Priority:** Medium
- **File/page:** `Lokis-Mischief-Site.html`, About saga (~line 2912)
- **Exact wording:** *"As the Prose Edda says: 'Loki is also called the father of monsters, and his children are the greatest of monsters.'"*
- **Claim:** Verbatim Prose Edda quotation.
- **Verdict:** B
- **Why:** Snorri does characterize Loki as father of the monster children and calls him "father of lies," but the exact English sentence appears to be a modern paraphrase, not a literal translation. Presenting a paraphrase inside quotation marks as a direct citation risks a fabricated-quotation issue.
- **Recommended replacement:** *"Snorri calls Loki the father of monsters, and his children are accounted the greatest of monsters."* (Remove the quotation marks / "As the Prose Edda says.")
- **Confidence:** Medium.

### 6-H6 — "unblessed" (Christian loanword in Hel game-over)
- **Priority:** Low
- **File/page:** `Lokis-Mischief-Site.html`, Hel game-over (~line 2392)
- **Exact wording:** *"The souls pile up unblessed."*
- **Verdict:** Minor Christian-vocabulary slip.
- **Recommended replacement:** *"The souls pile up, unsorted."*
- **Confidence:** High.

---

## 7. Full Claim Ledger

| ID | Webpage/file | Exact claim | Figure/concept | Verdict | Priority | Evidence/citation | Recommended correction | Confidence |
|----|--------------|-------------|----------------|---------|----------|-------------------|------------------------|------------|
| C01 | Hero saga | "Loki, the blood-brother of Odin" | Loki/Óðinn | A | — | Lokasenna st.9 | Keep | High |
| C02 | Hero saga | "the shape-shifter, the boundary-breaker" | Loki | A | — | Gylf.42 (mare/falcon/salmon) | Keep | High |
| C03 | Feature saga | "Loki's mischief caused the death of Baldr" | Baldr/Loki | A | — | Gylf.49 | Keep | High |
| C04 | Feature saga | "gods bound him to a rock with the entrails of his son" | Loki binding | A | — | Gylf.50 | Keep | High |
| C05 | Feature saga | "venom dripping onto his face, until Ragnarök" | Loki/Sigyn | A | — | Gylf.50 | Keep | High |
| C06 | Feature saga | "Loki didn't break because he knew his chains were temporary" | Loki | G | Low | Not in sources (marketing gloss) | Keep as clearly metaphorical | Med |
| C07 | Óðinn saga | "left Asgard to wander the Nine Realms in search of wisdom" | Óðinn | C | Low | Grímn., Háv. (wanderings) | Keep; "Nine Realms" interpretive | Med |
| C08 | Óðinn saga | "traded an eye for Mímir's well" | Óðinn/Mímir | A | — | Vsp.28–29; Gylf.15 | Keep | High |
| C09 | Óðinn saga | "hung himself from Yggdrasil for nine nights to gain the runes" | Óðinn/Yggdrasil | B | Low | Háv.138–139 (tree unnamed) | Keep; note Yggdrasil link is standard/Snorri | High |
| C10 | Óðinn saga | "ravens Huginn and Muninn…bring back knowledge" | Huginn/Muninn | A | — | Grímn.20 | Keep | High |
| C11 | Þórr saga | "son of Odin, god of thunder, strength, protection" | Þórr | A | — | Gylf.21 | Keep | High |
| C12 | Þórr saga | "Mjölnir…levels mountains, smashes giants, keeps the worlds safe" | Mjölnir | A/B | Low | Gylf.21,44 | Keep; "safe from chaos" interpretive | High |
| C13 | Þórr saga | "belt Megingjörð doubles his already unmatched power" | Megingjörð | A | — | Gylf.44 | Keep | High |
| C14 | Freyr saga | "of the Vanir, rules prosperity, sunshine, abundant harvest" | Freyr | A | — | Yngl.4; Gylf.24 | Keep | High |
| C15 | Freyr saga | "He gave the gods their greatest treasures" | Freyr | B | High | Gylf.42 (Loki procured) | "When Loki won the dwarves' treasures, Freyr received Skíðblaðnir" | High |
| C16 | Freyr saga | "won the heart of Gerðr through persistence and patience" | Freyr/Gerðr | B | Med | Skírnismál (coercive/negotiated) | "by Skírnir's suit he won Gerðr" | High |
| C17 | Freyja saga | "most powerful seiðr-witch…taught the Aesir shape-shifting" | Freyja | A/B | High | Yngl.4; Lokas.24 | "first brought seiðr to the Æsir" | High |
| C18 | Freyja saga | "wears the falcon cloak" | Freyja | A | — | Þrymskviða; Sörla þáttr | Keep | High |
| C19 | Freyja saga | "commands fate itself" | Freyja | C | High | Grímn.14 (half the slain) | "of the slain she receives half" | Med |
| C20 | Freyja saga | "Her tears are gold" | Freyja | A | — | Skáldskaparmál | Keep | High |
| C21 | Týr saga | "bravest of the gods, hand in Fenrir's mouth as pledge" | Týr | A | — | Gylf.34 | Keep | High |
| C22 | Týr saga | "god of law, justice, heroic sacrifice" | Týr | A/B | Low | Gylf.25; Sigrdrífa oath | Keep; "sacrifice" interpretive | High |
| C23 | Týr saga | "god of…single combat" | Týr | B | Low | Scholarly inference | Keep with caveat | Med |
| C24 | Heimdallr saga | "guards Bifrost, the rainbow bridge to Asgard" | Heimdallr/Bifröst | A | — | Gylf.27 | Keep | High |
| C25 | Heimdallr saga | "needs no sleep, hears the grass grow, sees a hundred leagues" | Heimdallr | A | — | Gylf.27 | Keep | High |
| C26 | Heimdallr saga | "horn Gjallarhorn will sound at Ragnarök" | Gjallarhorn | A | — | Vsp.46; Gylf.27 | Keep | High |
| C27 | Bragi saga | "god of poetry and eloquence" | Bragi | A | — | Skáldskaparmál | Keep | High |
| C28 | Bragi saga | "carries mead from Óðinn's court" | Bragi | B | Low | Són's mead = Óðinn | Keep with caveat | Med |
| C29 | Fenrir saga | "firstborn of Loki and the giantess Angrboda" | Fenrir/Angrboða | A/B | — | Gylf.34 | Keep | High |
| C30 | Fenrir saga | "jaws could tear through oak and iron" | Fenrir | B | Low | Size emphasized in Gylf.34 | Keep (interpretive scale) | High |
| C31 | Fenrir saga | "Leyding…Dromi…Fenrir shattered both" | Fenrir chains | A | — | Gylf.34 | Keep | High |
| C32 | Fenrir saga | "Gleipnir…six impossible ingredients: cat's footfall, mountain roots, woman's beard, fish's breath, bird's spittle, bear's sinews" | Gleipnir | A | — | Gylf.34 (exact match) | Keep | High |
| C33 | Fenrir saga | "Tyr's Sacrifice…hand in mouth as pledge" | Týr | A | — | Gylf.34 | Keep | High |
| C34 | Fenrir saga | "At Ragnarök…devour Odin himself…on Vígríðr" | Fenrir/Óðinn | A | — | Vsp.53; Gylf.51 | Keep | High |
| C35 | Jörmungandr saga | "second child of Loki and Angrboda" | Jörmungandr | A | — | Gylf.34 | Keep | High |
| C36 | Jörmungandr saga | "cast into ocean…tail met his own jaws" | Jörmungandr | A | — | Gylf.34 | Keep | High |
| C37 | Jörmungandr saga | "Urðar Serpent, the World-Coiler" | Jörmungandr | H | Critical | No "Urðar Serpent" attested; correct = Miðgarðsormr | "Miðgarðsormr, the World Serpent" | High |
| C38 | Jörmungandr saga | "Thor's fishing trip with Hymir…ox's head…Hymir cut the line" | Þórr/Hymir | A | — | Hymiskviða; Gylf.48 | Keep | High |
| C39 | Jörmungandr saga | "Lifting of the Cat…Utgarða-Loki…cat was Jörmungandr" | Utgarða-Loki | A | — | Gylf.44–46 | Keep | High |
| C40 | Jörmungandr saga | "Thor strikes it dead…nine steps before venom finishes him" | Þórr/Jörmungandr | A | — | Gylf.51; Vsp.56 | Keep | High |
| C41 | Hel saga | "third child of Loki and Angrboda, half-living/half-corpse" | Hel | A | — | Gylf.34 | Keep | High |
| C42 | Hel saga | "gods cast Hel into Niflheim and made her ruler of the dead" | Hel/Niflheim | A | — | Gylf.34 | Keep | High |
| C43 | Hel saga | "hall Eljudnir ('Drenched with Rain')" | Éljúðnir | A | — | Gylf.34 | Keep | High |
| C44 | Hel saga | "walls woven from frozen rivers" | Hel's hall | G | Low | Not in source (embellishment) | Keep as poetic; not doctrine | Med |
| C45 | Hel saga | "court of final judgment — every soul sorted by her will" | Hel | B/F | High | Gylf.34 (receives, not judges) | "assigns each of the dead a place to dwell" | High |
| C46 | Sleipnir saga | "born of Loki (as mare) + Svaðilfari" | Sleipnir | A | — | Gylf.42 | Keep | High |
| C47 | Sleipnir saga | "giant builder…demanding sun, moon, goddess Freyja" | Builder/Freyja | A | — | Gylf.42 | Keep | High |
| C48 | Sleipnir saga | "eight-legged…given to Odin…crosses Bifröst" | Sleipnir | A | — | Gylf.42; Grímn.44 | Keep | High |
| C49 | Sleipnir saga | "only horse that can travel between the worlds (Asgard/Jötunheim/Niflheim)" | Sleipnir | C | Low | Speed attested; realm-list interpretive | Keep with caveat | Med |
| C50 | Sleipnir saga | "Hermóðr…rode nine days/nine nights…leaped wall of Eljudnir" | Hermóðr | A | — | Gylf.49 | Keep | High |
| C51 | Products saga | "Loki cut Sif's hair…dwarven treasures: Gungnir, Mjölnir, Skíðblaðnir" | Loki/dwarves | A | — | Gylf.42 | Keep | High |
| C52 | Playbook saga | "Völuspá first/famous poem of Poetic Edda; völva summoned by Odin; world from Ymir" | Völuspá/Ymir | A | — | Vsp.21; Gylf.7–8 | Keep | High |
| C53 | About saga | "Loki fathered four children (3 with Angrboða + Sleipnir)" | Loki | A | — | Gylf.34,42 | Keep | High |
| C54 | About saga | "Prose Edda says: 'Loki is also called the father of monsters…'" | Loki | B | Med | Snorri (paraphrase) | "Snorri calls Loki the father of monsters" (no quotes) | Med |
| C55 | Hel game-over | "The souls pile up unblessed" | Hel | Minor Christian vocab | Low | "blessed" = Christian loanword | "The souls pile up, unsorted" | High |
| C56 | Óðinn card | Emblem "ᚠᚨᚱ" (f-a-r) labelled Óðinn | Runes | Internal | Low | Does not spell Óðinn | Decorative; or correct to ᚢᚦᛁᚾ (uþin) | High |
| C57 | Multiple | "Nine Realms" used as travel list | Cosmology | B | Low | Nine realms attested (Gylf.34 etc.) but not a fixed map | Keep; flag interpretive | High |
| C58 | Hel game | "Soul Sorting" metaphor (automate vs manual) | Hel | Acceptable metaphor | Low | Not doctrine | Keep; saga text must not say Hel judges | High |

---

## 8. Internal Consistency Issues

(Kept separate from historical accuracy.)

1. **Rune "emblems" don't match names.** Deity cards show rune triads: Óðinn = ᚠᚨᚱ (f-a-r), Þórr = ᚦᚢᚱ (þ-u-r ≈ "Þur," a known Þórr-rune name, acceptable), Freyr = ᚠᚱᛖ (f-r-e, not "Freyr"), Freyja = ᚠᚱᛖ (same as Freyr — duplicate), Týr = ᛏᛁᚱ (t-i-r ≈ "Týr," acceptable), Heimdallr = ᚺᛖ (h-e), Bragi = ᛒᚱ (b-r). These read as decorative initials, not transcriptions. If the site presents them as the figure's name in runes, only Þórr (Þurr) and Týr are arguably correct; Óðinn should be ᚢᚦᛁᚾ (uþin) and Freyr/Freyja should be distinct. Recommend either labeling them "sigil" or correcting the transliteration.
2. **Duplicate emblem for Freyr and Freyja** (both ᚠᚱᛖ) — inconsistent if meant to identify each deity.
3. **"Sleipnir…from Asgard to Jötunheim to Niflheim"** (§4.13) vs. the canonical nine-realm list elsewhere — the site never publishes a fixed nine-realm list, so the casual enumeration is internally loose but not contradictory.
4. **Product count vs. copy.** About section says "11 Workflow Products"; the products grid lists 6 workflow products + the 7 deity "OS" products (Runecraft OS, etc.) referenced in the deity sections. The two counts are not reconciled on one page; minor commercial-inventory inconsistency, not a Norse-accuracy issue.
5. **Brand-name drift.** The main site and `lokis-assets` use "Loki's Mischief"; the playbook uses "Loki's Creations." Inconsistent brand label across files (commercial, not mythological).

---

## 9. Content That Is Accurate as Written

The following are well-supported by the medieval sources and should remain unchanged (subject only to the minor wording notes above):

- Loki as Óðinn's blood-brother (Lokasenna 9).
- The binding of Loki with his son's entrails; Sigyn's bowl; venom until Ragnarök (Gylfaginning 50).
- Óðinn's eye at Mímir's well (Vsp. 28–29; Gylf. 15); the nine-night self-sacrifice for the runes (Hávamál 138–139); Huginn & Muninn (Grímnismál 20).
- Þórr as son of Óðinn, god of thunder; Megingjörð doubling strength (Gylfaginning 44).
- Freyr as Vanir god of prosperity/sunshine/harvest (Ynglinga saga 4; Gylfaginning 24).
- Freyja taught seiðr to the Æsir (Ynglinga saga 4; Lokasenna 24); falcon cloak; tears of gold (Skáldskaparmál).
- Týr's hand in Fenrir's mouth (Gylfaginning 34).
- Heimdallr's watch-traits and Gjallarhorn (Gylfaginning 27; Vsp. 46).
- Bragi as god of poetry (Skáldskaparmál).
- Fenrir: Leyding/Dromi, Gleipnir's exact six ingredients, devouring Óðinn at Vígríðr (Gylfaginning 34; Vsp. 53).
- Jörmungandr: casting, Þórr's fishing with Hymir, the cat at Utgarða-Loki, death after nine steps (Hymiskviða; Gylfaginning 44–46, 51; Vsp. 56).
- Hel: parentage, half-coloured body, Niflheim, Éljúðnir (Gylfaginning 34).
- Sleipnir: Loki-mare + Svaðilfari, eight legs, given to Óðinn, Hermóðr's ride (Gylfaginning 42, 49).
- Loki's dwarf gifts — Gungnir, Mjölnir, Skíðblaðnir (Gylfaginning 42).
- Völuspá summary — völva, creation from Ymir, Ragnarök and renewal (Vsp. 21; Gylfaginning 7–8).
- Loki's four children and parentage (Gylfaginning 34, 42).

---

## 10. Sources

**Primary sources (editions/translations):**
- *The Poetic Edda*, trans. Carolyne Larrington (Oxford World's Classics, 2nd ed., 2014) — Völuspá (st. 21, 28–29, 46, 53, 56), Grímnismál (st. 13, 14, 20, 44), Hávamál (st. 138–139), Lokasenna (st. 9, 24), Hymiskviða, Skírnismál, Rigsthula.
- *The Prose Edda*, Snorri Sturluson, trans. Jesse L. Byock (Penguin Classics, 2005) — Gylfaginning ch. 7–8 (creation from Ymir), 15 (Mímir), 21/24/25/27 (Þórr, Freyr, Týr, Heimdallr), 34 (Fenrir/Hel/Angrboða/Gleipnir/Týr), 42 (Sleipnir/builder/Sif's hair/dwarf gifts), 44–46 (Utgarða-Loki cat), 48–49 (Hymir/Hermóðr), 50 (binding of Loki), 51 (Ragnarök deaths).
- *The Prose Edda*, trans. Anthony Faulkes (Everyman, 1987/1995) — same chapters; Skáldskaparmál (Freyja's gold tears; Bragi).
- *Heimskringla: The History of the Kings of Norway*, Snorri Sturluson, trans. Lee M. Hollander — Ynglinga saga ch. 4–5 (Freyr; Freyja brings seiðr to the Æsir).
- *Edda* (Codex Regius) — Völuspá as the first poem (standard manuscript order).
- *Baldrs draumar* (in some Poetic Edda editions) — Hel's realm.

**Scholarly / reference:**
- Simek, Rudolf. *Dictionary of Northern Mythology* (trans. Angela Hall, 1993/2007) — entries for Angrboða, Bragi, Fenrir, Gjallarhorn, Gleipnir, Heimdallr, Hel, Hermóðr, Hymir, Jörmungandr, Megingjörð, Miðgarðsormr, Sleipnir, Týr, Urðr/Urðarbrunnr, Útgarða-Loki, Vígríðr, Yggdrasil.
- Lindow, John. *Norse Mythology: A Guide to the Gods, Heroes, Rituals, and Beliefs* (Oxford, 2001).
- Davidson, H.R. Ellis. *Gods and Myths of Northern Europe* (Penguin, 1964).
- Orchard, Andy. *Cassell's Dictionary of Norse Myth and Legend* (1997).
- Dumézil, Georges. *Gods of the Ancient Northmen* (1973) — Týr/Mars Thingsus comparanda (used only to flag "single combat" as inference, not doctrine).
- Norse Mythology website (norse-mythology.org) — consulted for the Freyja-seiðr summary (secondary; cross-checked against Ynglinga saga/Lokasenna).

**Note on method:** All primary attributions above are to standard, well-established passages. Stanza/chapter numbers follow the common Larrington/Byock/Faulkes editions. Where a detail is a standard scholarly inference rather than an explicit source line (e.g., "single combat" for Týr, Yggdrasil = the tree in Hávamál), it is marked B/C in the ledger, not A.

**Online resources (access dates 2026-07-21):** web searches confirming (a) Gleipnir's six ingredients match Gylfaginning (Britannica "Gleipnir" and multiple secondary summaries), and (b) Freyja's introduction of seiðr to the Æsir (Wikipedia "Freyja"; Hrafnar "Freyja"). These were used only to corroborate primary readings already known; no claim rests solely on a secondary website.

---

### Forward-looking note (per your planned per-deity pages)
You mentioned each god should get its own linked nav page with archetype-matched business products. When those pages are built, apply the same standard used here: keep the attested facts (the A/B rows above), keep marketing metaphor clearly separate from doctrine, avoid Christian "judgment/soul/blessing" vocabulary around Hel, and correct the "Urðar Serpent" error before it propagates. The current single-page copy can be reused as the per-deity "Saga" blurbs with the corrections in §6 applied.

---

## 11. Revision Pass Log (approved 2026-07-21)

The owner approved the revision pass. Applied changes (all source-grounded per §6):

**A. Corrections applied to `Lokis-Mischief-Site.html` (the six §6 items):**
1. Jörmungandr saga: "Urðar Serpent, the World-Coiler" → "Miðgarðsormr, the World Serpent" (§6-H1, Critical).
2. Hel saga: "court of final judgment — every soul… sorted by her will" → "She receives the dead there, and among the nine worlds she assigns each of those who die a place to dwell" (§3-C1 / §6-H2).
3. Hel game-over: "The souls pile up unblessed" → "The souls pile up, unsorted" (§6-H6).
4. Freyr saga: "He gave the gods their greatest treasures and won the heart of Gerðr through persistence and patience" → corrected attribution (Loki procured the treasures; Freyr received Skíðblaðnir) and Gerðr won by Skírnir's suit (§6-H3).
5. Freyja saga: "taught the Aesir the art of shape-shifting and persuasion… commands fate itself" → "foremost in the craft of seiðr, first brought that magic to the Æsir… Of the slain who fall in battle, she receives half" (§6-H4).
6. About saga: removed the fabricated quotation marks / "As the Prose Edda says"; now "Snorri calls Loki the father of monsters…" (§6-H5).

**B. Internal-consistency fixes (§8):**
- Deity rune "emblems" now transliterate each name in Elder Futhark and carry a `title` attribute: Óðinn ᚢᚦᛁᚾ, Þórr ᚦᚢᚱ, Freyr ᚠᚱᛁ, Freyja ᚠᚱᛁᚨ, Týr ᛏᛁᚱ, Heimdallr ᚺᛁᛗ, Bragi ᛒᚱᚨ. (Previously Óðinn showed f-a-r and Freyr/Freyja shared an identical emblem; the earlier Younger-Futhark forms for Freyja, Týr, Heimdallr and Bragi have been replaced with Elder Futhark equivalents.)

**C. New per-deity pages (per owner's request — each god gets its own nav-linked page with an archetype-matched product + its digital assets + a business lesson):**
- `odin.html` — Runecraft OS (Founder decision OS); lesson: decide with intelligence, not from the throne.
- `thor.html` — Mjölnir Infrastructure (Security); lesson: neutralize threats before they reach the door.
- `freyr.html` — Green Harvest Engine (Lead gen/revenue); lesson: plant systems that compound.
- `freya.html` — Seiðr Messaging Stack (Persuasion); lesson: influence is a craft, not noise.
- `tyr.html` — Týr's Code (Contracts/compliance); lesson: honor at the trust boundary, keep a human in the loop.
- `heimdall.html` — Bifrost Monitor (Monitoring); lesson: no silent failures.
- `bragi.html` — Skald's Quill (Brand narrative); lesson: turn every win into a saga.
- Each page reuses the audit-corrected saga copy, includes a genuine Eddic verse with source citation, an explicit "Business Lesson" block, the archetype-matched product with price/description, and a "Digital Assets Included" list pointing to the real workflow JSON / guide / template files already in `lokis-assets/`. The top nav of the main site now links to each page (with ↗), and each page cross-links back and to the others.

**Verification:** All seven pages exist; main-site nav contains the seven `*.html` links; corrected phrases confirmed present in source; each page contains a "The Business Lesson" section. No doctrine was altered except the Hel judgment wording; all marketing still clearly framed as metaphor.

STATUS: AUDIT COMPLETE. REVISION PASS APPLIED AND VERIFIED (2026-07-21). PROJECT ASSETS MODIFIED ONLY BY THE APPROVED CORRECTIONS AND ADDITIONS ABOVE.
