# Runecraft OS — Implementation Guide

## What this is
Runecraft OS is a decision interface for founders. It replaces manual triage with a rune-priority system: every request gets a semantic category, then routes to the right workflow, owner, and response standard.

## Setup
0. Make sure Make.com or n8n has webhook intake and email/slack outbound.
1. Import `workflows/make-runic-priority.json` into Make.
2. Update webhook endpoint to your intake form.
3. Set rune→route mapping in the router module to match your CRM inboxes.
4. Optional: add a dashboard so you can see rune distribution.

## Tips
- Start with 6 runes, not 24. Expand once it becomes second nature.
- Do not use rune art unless it is historically accurate; images are your public credibility.
- Check workflow execution weekly, then quarterly.

## Support
If you bought direct, DM with your receipt. Community edition is included; founder pack adds prompt templates and decision maps.
