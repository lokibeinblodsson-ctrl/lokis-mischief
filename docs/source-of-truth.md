# Source-of-Truth Decision

**Generated:** 2026-08-17T18:57Z (Micro-Phase 2A)
**Status:** Provisional until the full repository comparison is certified (comparison performed in 2A; see evidence).

## Canonical implementation workspace
> **`/root/lokis-mischief`** is the canonical implementation workspace. **`/root/agent/repos/lokis-mischief`** is an independent comparison/reference clone and must remain untouched unless explicitly authorized.

## Why `/root/lokis-mischief` is canonical
1. It is the repository on `main` and is the copy intended to be served.
2. It is the copy whose live container (`lokis-site`) is being tested/baselined.
3. Its bind-mount source path (`/root/lokis-mischief`) matches the docker-compose volume definition.

## Second clone — read-only policy
- **Path:** `/root/agent/repos/lokis-mischief`
- **Must not be modified** unless explicitly authorized.
- Used only as a comparison/reference baseline in 2A.

## Evidence supporting the decision
- Both repos are on `main` with identical HEAD `9baa40cd5ef7c94027aaf4b3474e04f74e30373f`.
- `diff -r --brief` (excluding `.git` and the authorized `docs/_preserve`) shows **no content differences**.
- SHA-256 of all tracked files matched within the diff (only `docs/_preserve/*` added by Hermes in 2A distinguishes them).
- Same git remote/origin for both.

## Implications
- All future edits, the repaired container, and the diagnostic/agency build-out target `/root/lokis-mischief`.
- The second clone remains a pristine reference; do not sync into it during Micro-Phase 2.
- If a future divergence is discovered, this decision must be revisited before any destructive action.
