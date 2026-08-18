# Governance Note — Auto-Publish Worker & Source-of-Truth (Micro-Phase 2→3 gate)

**Generated:** 2026-08-17T19:16Z
**Status:** Recorded for operator review. NOT a blocker. No automation was modified.

## 1. Recorded commit (per decision)
- The Micro-Phase 2 decision referenced commit **`9baa40c`** ("auto-publish: MICRO_PHASE_1_REPORT.md").
- **Updated finding:** `9baa40c` is **NOT an ancestor** of the current `HEAD` (`8252c1c…`). The automation has since advanced `main` past that commit. The originally-referenced commit is no longer in the linear lineage — evidence of uncontrolled, fast-moving automated commits.
- Current `HEAD` of both `/root/lokis-mischief` and `/root/agent/repos/lokis-mischief`: **`8252c1cfe00c53788a82256038ad24c75f968f4c`** (byte-identical trees; only a stray `blog/__pycache__` differs in canonical).

## 2. Worker(s) responsible for automatic commits — identified
Multiple independent automations push to `origin/main` of `lokibeinblodsson-ctrl/lokis-mischief`:

| Identity (git author) | Script | Trigger | Review gate? |
|---|---|---|---|
| `Hermes Auto-Publish` `<agent@lokis.local>` | `/root/.hermes/scripts/lokis_autopush.sh` | Windmill schedule **every 60s** | **NONE** — pushes any dirty state of `/root/lokis-mischief` to `main` |
| `Hermes Manager` `<hermes@brainstorm>` | `/root/.hermes/scripts/feature_manager_wm.sh` (runs in Windmill) | Windmill schedule | **Test-gated** — re-runs `tests/run.js`; only commits+pushes on APPROVE |
| `Hermes Agent` `<hermes@brainstorm>` | `/root/.hermes/scripts/push_repo.sh` | invoked manually/by agents | none stated |
| `Loki Worker` `<worker@lokis.local>` | `/root/.hermes/scripts/lokis_lore_worker.sh` | schedule | none (lore only) |
| `Loki Blogger` `<blog@lokis.local>` | `/root/.hermes/scripts/blog_daily.sh` | daily | none (blog only) |
| (feature agent, no direct push) | `agent-manager` container PID 2872643 | loops on `FEATURE_TODO.md`, edits `/work` (the **clone**) | hands off; does NOT push itself |

All commit `ALLOW_PUBLIC_PUSH=1` to `main` using a GitHub token from `/root/.hermes/secrets/api_keys.env` (masked in logs). No git hook in the repo auto-commits; the push is script/schedule driven.

## 3. May it continue committing during Hermes work?
- `lokis_autopush.sh` **will push any uncommitted change in `/root/lokis-mischief` within 60s**, with **no review**. During Hermes work this means: if Hermes leaves the canonical tree dirty, the worker may auto-commit+push it as `auto-publish`. This is the core source-of-truth/audit risk flagged in the decision.
- The test-gated `feature_manager` only acts on explicit APPROVE handoffs from the feature agent (which edits the **clone**, not canonical).

## 4. Preventing unreviewed/production commits (recommendation — not yet applied)
To keep Hermes commits distinguishable and prevent the auto-pusher from publishing half-finished work:
1. **Hermes should commit+push promptly** after any authorized change, OR keep the canonical tree clean, so `lokis_autopush` has nothing unexpected to push.
2. **Distinguish identity:** Hermes already commits as `Hermes Agent`/`Hermes Manager`. A dedicated `Hermes (Micro-Phase)` identity + a consistent message prefix (`mp3a:`, `mp3b:` …) would let the operator filter Hermes commits from `auto-publish`/`Loki Worker`/`Loki Blogger`.
3. **Optional control (operator decision):** pause `lokis_autopush` Windmill schedule during structured Micro-Phase work, or change it to only push when a `.autopush-approved` marker exists. This is **out of scope for 3A** and was not applied.

## 5. Distinguishing Hermes vs worker commits
- Hermes-caused commits: author `Hermes Agent`/`Hermes Manager`, message prefix planned `mp3x:`.
- Worker commits: `Hermes Auto-Publish` (60s sweep), `Loki Worker`, `Loki Blogger`.
- `git log --author=` and `git log --grep='mp3'` can separate them.

## 6. No history rewrite
This note records state only. **No reset, no force-push, no history rewrite** was performed or is recommended here.

## 7. Source-of-truth nuance discovered (must surface)
- The operator's Micro-Phase 2 directive said: canonical = `/root/lokis-mischief`; the clone `/root/agent/repos/lokis-mischief` must stay **read-only/untouched**.
- **Reality:** the live `agent-manager` feature agent **writes to the clone** (`/work` = `/root/agent/repos/lokis-mischief`), and `feature_manager_wm.sh` runs its test gate + push **from the clone**, pushing to `origin/main`. Meanwhile `lokis_autopush.sh` pushes the **canonical** copy. Both share `origin/main`, so they stay in sync, but the "clone is untouched" assumption is **not accurate** for the running system.
- Recommendation: either (a) formally designate the clone as the *implementation working copy* and canonical as the *served mirror*, or (b) re-point the feature agent to `/root/lokis-mischief`. This is an **open decision (D8)** — recorded, not resolved in 3A.
