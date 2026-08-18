# Behavior Baseline

**Generated:** 2026-08-17T18:57Z (Micro-Phase 2A/2B)
**Purpose:** Record how the canonical static site is *expected* to behave, and the measured behavior of the live container before and after repair.

## A. Intended (static) behavior — from `nginx.conf` + `docker-compose.yml`
- nginx serves `/usr/share/nginx/html` (bind-mounted from `/root/lokis-mischief`, read-only).
- `GET /` → `index.html`.
- Static assets (`.jpg .png .svg .woff2 .json .css .js`) cached 7d, `immutable`.
- `try_files $uri $uri/ /index.html` for HTML; unknown paths 404.
- Dotfiles denied (`location ~ /\. { deny all; }`).
- Healthcheck: `wget -q -O - http://127.0.0.1/ ` (expects 200 from `/`).
- Listen `:80`, published `8899:80`, restart `unless-stopped`.

## B. Measured behavior — BEFORE repair (2B inspection, 2026-08-17T18:50Z)
Container `lokis-site` was **Up 5 days but `unhealthy`**, `FailingStreak: 565`.
- Mount actual: `/usr/share/nginx/html` bound from `/dev/nvme0n1p1` (root fs), **not** `/root/lokis-mischief`. → served root was **empty** (0 files).
- `ls /usr/share/nginx/html` → empty; no `index.html`.
- nginx config inside container is correct (`lokis.conf` present, `nginx -T` OK).
- Container restart policy in runtime = `no` (compose specifies `unless-stopped` → started manually with wrong mount).

**Baseline tests vs `:8899` (all failed):**
| Route | Result |
|-------|--------|
| `GET /` | 403 (directory index forbidden) |
| `GET /index.html` | 500 (rewrite cycle) |
| `GET /games.html` | 500 (rewrite cycle) |
| `GET /lokis-assets/loki/loki.png` | 404 |
| `GET /runes-data.json` | 404 |
| `GET /rune-cast.html` | 500 (rewrite cycle) |

## C. Measured behavior — AFTER repair (2026-08-17T19:01Z)
Root cause fixed: recreated container via the existing `docker-compose.yml`, which binds `/root/lokis-mischief:/usr/share/nginx/html:ro` (the live container had been bound to the host root filesystem `/dev/nvme0n1p1`, leaving the served root empty).

Verified state:
- Container `lokis-site`: **Up, healthy** (was `unhealthy`, streak 565 → 0).
- Mount inside container now correctly sourced from `/root/lokis-mischief` (68 entries; `index.html` present, 219 KB).
- Restart policy `unless-stopped` (matches compose).

**Post-repair baseline tests vs `:8899` (all pass):**
| Route | Result |
|-------|--------|
| `GET /` | 200 |
| `GET /index.html` | 200 |
| `GET /games.html` | 200 |
| `GET /products.html` | 200 |
| `GET /services.html` | 200 |
| `GET /rune-cast.html` | 200 |
| `GET /lore.html` | 200 |
| `GET /runes-data.json` (local JSON fetch) | 200 |
| `GET /lokis-assets/loki/loki-hero.png` (asset) | 200 |
| `GET /lokis-assets/favicon/favicon.ico` (asset) | 200 |
| `GET /games` (dir → 301 to /games/) | 301 |
| healthcheck `wget http://127.0.0.1/` | healthy |

Note: an early test probed `/lokis-assets/loki/loki.png` (404) — that filename does not exist; the real assets are `loki-generated.png` / `loki-hero.png` and both return 200. No real asset is missing.
