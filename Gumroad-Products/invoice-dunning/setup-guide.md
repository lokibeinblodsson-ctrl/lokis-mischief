# Invoice Dunning & Payment Reminder — Setup Guide

**Product:** Invoice Dunning & Payment Reminder  
**Price:** $39  
**Purchase Link:** https://buy.stripe.com/test_bJe4gs8HQ0VZaJe1PZ9Zm03  
**Blueprint Version:** 1.0.0

---

## Table of Contents

1. [Overview](#overview)
2. [How It Works](#how-it-works)
3. [Prerequisites](#prerequisites)
4. [Step 1: Import the Blueprint](#step-1-import-the-blueprint)
5. [Step 2: Connect Your Accounts](#step-2-connect-your-accounts)
6. [Step 3: Configure the Webhook Trigger](#step-3-configure-the-webhook-trigger)
7. [Step 4: Set Up Google Sheets](#step-4-set-up-google-sheets)
8. [Step 5: Set Up Slack (Final Notice)](#step-5-set-up-slack-final-notice)
9. [Step 6: Configure Email Templates (Optional)](#step-6-configure-email-templates-optional)
10. [Step 7: Test the Workflow](#step-7-test-the-workflow)
11. [Step 8: Activate & Go Live](#step-8-activate--go-live)
12. [Troubleshooting](#troubleshooting)
13. [Appendix: Spreadsheet Layout](#appendix-spreadsheet-layout)

---

## Overview

The **Invoice Dunning & Payment Reminder** workflow automates your accounts receivable follow-up process. When a Stripe invoice becomes past due, this scenario automatically sends a series of increasingly urgent email reminders, logs every action to Google Sheets, and notifies your team via Slack when a customer reaches the final notice stage.

No manual chasing. No forgotten follow-ups. Just consistent, professional dunning that protects your revenue.

---

## How It Works

```
Stripe Invoice (past due)
       │
       ▼
  Webhook Trigger
       │
       ▼
  Router (by days past due)
       │
       ├── Day 1–3   → Friendly Reminder Email → Log to Sheets
       ├── Day 4–10  → Gentle Nudge Email     → Log to Sheets
       └── Day 11+   → Final Notice Email     → Log to Sheets
                                               → Slack Alert (#collections-alerts)
```

**Three-tier reminder schedule:**

| Tier | Days Past Due | Email Style | Actions |
|------|-------------|-------------|--------|
| **1** | 1–3 days | Friendly reminder | Gmail + Google Sheets log |
| **2** | 4–10 days | Gentle nudge | Gmail + Google Sheets log |
| **3** | 11+ days | Final notice | Gmail + Google Sheets log + Slack alert |

> **Note:** These thresholds are configurable. Adjust the router conditions to match your business cycle.

---

## Prerequisites

Before you begin, make sure you have:

1. **A Make.com account** (any paid plan that supports Webhooks, Gmail, Google Sheets, and Slack modules)
2. **A Stripe account** with invoices enabled (you'll need API access)
3. **A Google account** — for Gmail sending and Google Sheets logging
4. **A Slack workspace** — for team notifications (optional but recommended)
5. **The blueprint file** — `deployed-blueprint.json` (included with purchase)

---

## Step 1: Import the Blueprint

1. Log in to your **Make.com** account.
2. Go to **Scenarios** → **Create a new scenario**.
3. Click the **three dots (⋯)** menu in the bottom-left corner of the scenario editor.
4. Select **Import Blueprint**.
5. Choose the `deployed-blueprint.json` file included with your purchase.
6. Click **OK** to load the scenario.

The full workflow will appear in the editor with all modules and connections pre-configured.

---

## Step 2: Connect Your Accounts

You need to authorize Make.com to access your apps. Click each module that shows a **warning triangle** (⚠️) and follow the prompts to create a connection.

### Required connections

| App | Modules | Setup Instructions |
|-----|---------|-------------------|
| **Webhook** | Trigger module | No auth needed — just copy the webhook URL after saving |
| **Gmail** | 3 email modules (30, 40, 50) | Click **Add** → choose your Google account → grant Gmail API permissions |
| **Google Sheets** | 3 sheet modules (60, 70, 80) | Click **Add** → choose your Google account → grant Google Sheets API permissions |
| **Slack** | 1 notification module (90) | Click **Add** → choose your Slack workspace → grant chat:write + channel permissions |

**Tip:** You can use the same connection for all Gmail modules (and all Google Sheets modules) — create one connection and reuse it.

---

## Step 3: Configure the Webhook Trigger

1. Click the **Webhook** module (id: 10) to open its settings.
2. Take note of the **Webhook URL** — you'll need it for Stripe.
3. Click **Save** (the webhook URL is generated the first time you save).

### Connect Stripe to the Webhook

1. Go to your **Stripe Dashboard** → **Developers** → **Webhooks**.
2. Click **Add endpoint**.
3. Enter the webhook URL from Make.com.
4. Select the following events to listen for:
   - `invoice.payment_failed`
   - `invoice.past_due`
5. Click **Add endpoint** to save.
6. Optionally, click **Send test webhook** to verify connectivity.

> **Security tip:** Enable HMAC verification in the webhook module settings for production use. Set a secret in both Strike webhook settings and Make's HMAC configuration.

---

## Step 4: Set Up Google Sheets

### Create the Dunning Log Spreadsheet

1. Create a new Google Sheet (or use an existing one).
2. Rename the default sheet to **Dunning Log**.
3. Add the following headers in **Row 1** (Column A through J):

| A | B | C | D | E | F | G | H | I | J |
|---|---|---|---|---|---|---|---|---|---|
| Invoice ID | Customer Name | Customer Email | Amount | Due Date | Days Past Due | Reminder Tier | Email ID | Timestamp | Status |

4. Copy the **spreadsheet URL** — extract the ID from it:
   - `https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit`

5. Update **all three Google Sheets modules** (60, 70, 80):
   - Set `spreadsheetId` to your `SPREADSHEET_ID`
   - Set `sheetName` to `Dunning Log`

---

## Step 5: Set Up Slack (Final Notice)

1. Click the **Slack** module (id: 90).
2. Select your Slack connection.
3. Set the **Channel** to `#collections-alerts` (or any channel of your choice).
   > The channel must exist in your workspace. Create it first if needed.
4. The message blocks are pre-configured with:
   - Customer name, email, invoice ID, amount, days overdue
   - A "View Invoice" button (links to the Stripe invoice URL)
   - Warning text about escalation

You can customize the message text and blocks as desired.

---

## Step 6: Configure Email Templates (Optional)

All three email templates are written in HTML with inline CSS. You can customize them to match your brand.

### How to customize:

1. Click any **Gmail** module (30, 40, or 50).
2. Edit the `body` field (HTML).
3. The following template variables are available:

| Variable | Description |
|----------|-------------|
| `{{10.customer_name}}` | Customer's full name |
| `{{10.customer_email}}` | Customer's email address |
| `{{10.id}}` | Stripe invoice ID |
| `{{10.amount_formatted}}` | Formatted amount (e.g., "$49.99") |
| `{{10.due_date}}` | Invoice due date |
| `{{10.days_past_due}}` | Number of days past due |
| `{{10.stripe_invoice_url}}` | Hosted invoice payment link |
| `{{10.status}}` | Invoice status from Stripe |

### Default email templates

- **Friendly Reminder** (Day 1–3): Light tone, purple gradient header, reassures the customer, single CTA button.
- **Gentle Nudge** (Day 4–10): Pink gradient header, slightly more direct language, mentions days overdue.
- **Final Notice** (Day 11+): Red gradient header, urgent tone, warns of escalation within 3 business days.

---

## Step 7: Test the Workflow

### Method 1: Use Stripe Test Mode

1. In Stripe, switch to **Test mode**.
2. Use the [Stripe CLI](https://stripe.com/docs/stripe-cli) or dashboard to trigger a test invoice event:
   ```bash
   stripe trigger invoice.past_due
   ```
3. Observe the Make.com scenario run in real-time.
4. Check:
   - The appropriate email was sent (check the test inbox)
   - A row was added to the Google Sheet
   - (For final notice) A Slack message appeared

### Method 2: Manual Webhook Test

1. In Make.com, open the Webhook module.
2. Click **Run once**.
3. Use a tool like curl or Postman to send a test payload:
   ```json
   {
     "id": "in_test_12345",
     "customer_email": "test@example.com",
     "customer_name": "Test Customer",
     "amount_due": 4999,
     "currency": "usd",
     "due_date": "2026-07-01",
     "days_past_due": 1,
     "status": "past_due",
     "stripe_invoice_url": "https://invoice.stripe.com/i/test_123",
     "subscription_id": "sub_test_123",
     "amount_formatted": "$49.99"
   }
   ```

### Verify the logs

Open your Google Sheet and confirm rows were added with correct data.

---

## Step 8: Activate & Go Live

1. Once testing is complete, **switch your webhook endpoint in Stripe from test mode to live mode** (create a new endpoint for production or toggle the existing one).
2. In Make.com, toggle the scenario to **ON**.
3. The scenario will now process incoming past-due invoices automatically.

### Recommended schedule

The scenario runs **instantly** on webhook trigger — no scheduling needed. Stripe sends the webhook when an invoice becomes past due or payment fails.

---

## Troubleshooting

| Issue | Likely Cause | Solution |
|-------|-------------|----------|
| **No emails are sent** | Gmail connection not authorized | Re-authenticate the Gmail module |
| **Webhook not triggering** | Stripe endpoint not configured | Verify webhook URL in Stripe dashboard |
| **Wrong reminder tier fires** | Days past due calculation is off | Check the `days_past_due` value in the webhook payload |
| **Google Sheets row not added** | Spreadsheet ID or sheet name mismatch | Verify `spreadsheetId` and `sheetName` in the modules |
| **Slack message not posting** | Bot not invited to channel | Invite the Make.com Slack app to `#collections-alerts` |
| **Router fallback route used** | Unexpected `days_past_due` value | Check the payload — add more routes if needed |
| **HMAC verification fails** | Secret mismatch or wrong algorithm | Ensure the HMAC secret, algorithm, and header position match Stripe settings |

### Common Stripe webhook issues

- **Missing events:** Ensure you subscribed to `invoice.past_due` and/or `invoice.payment_failed`.
- **Duplicate runs:** Stripe may resend webhooks. The blueprint does not deduplicate — your Google Sheet log will show duplicates, which you can filter or handle with a Lookup module if needed.
- **Test vs. Live:** Make sure your Stripe endpoint points to the correct environment. Test webhooks won't fire in the live scenario and vice versa.

---

## Appendix: Spreadsheet Layout

**Sheet name:** `Dunning Log`

| Column | Header | Data Type | Description |
|--------|--------|-----------|-------------|
| A | Invoice ID | Text | Stripe invoice identifier |
| B | Customer Name | Text | Customer's name from invoice |
| C | Customer Email | Text | Customer's email address |
| D | Amount | Text | Formatted amount (e.g., "$49.99") |
| E | Due Date | Text | Invoice due date |
| F | Days Past Due | Number | Days elapsed since due date |
| G | Reminder Tier | Text | Which reminder was sent (FRIENDLY REMINDER / GENTLE NUDGE / FINAL NOTICE) |
| H | Email ID | Text | Gmail message ID for audit trail |
| I | Timestamp | Text | When the action occurred |
| J | Status | Text | Status of the action (Sent / Slack notification sent) |

---

## Support

If you encounter any issues setting up this blueprint:

- **Purchase link:** https://buy.stripe.com/test_bJe4gs8HQ0VZaJe1PZ9Zm03
- **Documentation:** Refer to [Make.com Help Center](https://www.make.com/en/help) for platform-level questions.

---

*Thank you for purchasing the Invoice Dunning & Payment Reminder blueprint. Automate your collections and get paid faster!*
