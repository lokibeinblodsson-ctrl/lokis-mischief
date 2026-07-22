# Mjölnir Infrastructure — Threat Response Playbook

## Scan order
1. Frontend: CSP, mixed content, external script changes
2. Backend: auth, API key exposure, dependency CVEs
3. Pipeline: logs, secrets, runtime access controls
4. Ops: incident channel, on-call, training cadence

## Rating thresholds
- Critical — patch within 24 hours, rotate keys/creds
- High — patch within 1 week, temporary guard
- Medium — next sprint, owner assigned
- Low — queue for quarterly sweep

## Response templates
- P0: incident channel + owner + revenue exposure
- P1: owner + deadline + guardrail
- P2: backlog + SLA
