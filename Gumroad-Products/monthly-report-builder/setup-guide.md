# Narrative Monthly Report Builder — Setup Guide

**Product:** Narrative Monthly Report Builder
**Price:** $39
**Platform:** Make.com (formerly Integromat)
**Version:** 1.2

---

## Table of Contents

1. [What This Workflow Does](#what-this-workflow-does)
2. [How It Works (High-Level Flow)](#how-it-works-high-level-flow)
3. [Prerequisites](#prerequisites)
4. [Quick Start: Import the Blueprint](#quick-start-import-the-blueprint)
5. [Step-by-Step Configuration](#step-by-step-configuration)
   - [Step 1: Connect Your Make.com Account](#step-1-connect-your-makecom-account)
   - [Step 2: Import the Blueprint](#step-2-import-the-blueprint)
   - [Step 3: Configure Connections](#step-3-configure-connections)
   - [Step 4: Set Scenario Parameters](#step-4-set-scenario-parameters)
   - [Step 5: Activate the Scenario](#step-5-activate-the-scenario)
6. [Module-by-Module Walkthrough](#module-by-module-walkthrough)
7. [Testing Instructions](#testing-instructions)
8. [Troubleshooting](#troubleshooting)
9. [Customization Tips](#customization-tips)

---

## What This Workflow Does

The **Narrative Monthly Report Builder** is an enterprise-grade Make.com scenario that automatically:

- **Ingests data** from Google Analytics 4 (GA4), Facebook Ads, Google Ads, and Google Search Console
- **Generates AI-written narrative commentary** using OpenAI's GPT-4o — producing a professional monthly report with executive summary, channel analysis, wins & opportunities, and recommendations
- **Creates a polished Google Slides presentation** (or exports as PDF) with branded templates
- **Logs every report** to Google Sheets for audit tracking
- **Delivers the report** via Gmail with a preview and optional PDF attachment
- **Notifies your team** in Slack with delivery details

All of this happens from a single webhook trigger — integrate it with Zapier, your CRM, a cron schedule, or call it directly via API.

---

## How It Works (High-Level Flow)

```
Webhook Trigger
    ↓
Router (routes to selected data sources)
    ├── GA4 Analytics → Fetch sessions, users, conversions, revenue
    ├── Facebook Ads → Fetch impressions, clicks, spend, CTR, CPC
    ├── Google Ads → Fetch campaign metrics, conversions, cost
    └── Search Console → Fetch query & page performance
    ↓
Aggregator (merges all data into one payload)
    ↓
OpenAI GPT-4o (generates narrative report in Markdown)
    ↓
Google Slides Builder (creates 5-slide deck with branding)
    ↓
Google Sheets (logs delivery record)
    ↓
Route by Output Format
    ├── PDF → Export Slides as PDF
    └── Google Slides → Send link
    ↓
Gmail (sends report to client with preview)
    ↓
Slack (notifies internal team)
    ↓
Webhook Response (returns success + links)
```

---

## Prerequisites

Before you begin, make sure you have access to the following:

### Required Accounts

| Service | Account Type | Why It's Needed |
|---------|-------------|-----------------|
| **Make.com** | Paid plan (at least 10K ops/mo recommended) | Runs the automation scenario |
| **OpenAI** | API account with billing enabled | Generates AI narrative commentary |
| **Google Cloud** | Project with APIs enabled | Google Slides, Sheets, Gmail, GA4 APIs |
| **Facebook Developer** | App with Ads Insights access | Pulls Facebook Ads performance data |
| **Google Ads** | Manager or Standard account | Pulls Google Ads campaign data |
| **Slack** | Workspace with app creation rights | Posts team notifications |

### API Keys & IDs You'll Need

| Parameter | Where to Get It |
|-----------|-----------------|
| `OpenAI API Key` | [platform.openai.com/api-keys](https://platform.openai.com/api-keys) |
| `GA4 Property ID` | Google Analytics Admin → Property Settings |
| `Facebook Ad Account ID` | Facebook Ads Manager → Ad Account Settings (format: `act_XXXXXXXXX`) |
| `Google Ads Customer ID` | Google Ads → Account Settings (format: `XXX-XXX-XXXX`) |
| `Google Ads Developer Token` | Google Ads → API Center → Developer Token |
| `Search Console Site URL` | Google Search Console → Property (format: `sc_domain:example.com` or `https://example.com/`) |
| `Google Slides Template ID` | (Optional) Create a branded Slides deck and copy its URL ID |
| `Google Sheet ID` | Create a Google Sheet and copy its URL ID |
| `Slack Channel Name` | The channel where team notifications should post |

### Enabled Google Cloud APIs

In your Google Cloud Console project, enable these APIs:

- **Google Slides API**
- **Google Sheets API**
- **Gmail API**
- **Google Analytics Data API** (for GA4)
- **Google Search Console API**
- **Google Ads API**

---

## Quick Start: Import the Blueprint

1. Download `deployed-blueprint.json` from this package
2. Log into your Make.com account
3. Click **Scenarios** → **Add new scenario** → **Import Blueprint**
4. Select the `deployed-blueprint.json` file
5. Click **OK** — the full scenario will appear on the canvas

---

## Step-by-Step Configuration

### Step 1: Connect Your Make.com Account

Make sure you're on a Make.com plan that supports the number of operations this scenario will consume. A single run uses approximately 15–25 operations depending on how many data sources you enable.

### Step 2: Import the Blueprint

Follow the [Quick Start](#quick-start-import-the-blueprint) instructions above. After import, you'll see all 23 modules arranged on the canvas. Each module will have a warning icon — that's expected; you need to connect your accounts.

### Step 3: Configure Connections

Click each module with a connection warning and authorize the corresponding service:

| Module(s) | Connection Type | What to Authorize |
|-----------|----------------|-------------------|
| 3 (GA4) | **Google Analytics** | Select or add a Google Analytics connection (OAuth) |
| 4 (Facebook Ads) | **Facebook Ads** | Select or add a Facebook Ads connection (OAuth + Ad Account) |
| 5 (Google Ads) | **Google Ads** | Select or add a Google Ads connection (OAuth + Developer Token) |
| 6 (Search Console) | **Google Search Console** | Select or add a Google Search Console connection (OAuth) |
| 9 (OpenAI) | **HTTP (Bearer Token)** | Paste your OpenAI API key in the connection's "Bearer Token" field |
| 11–17 (Google Slides) | **Google Slides** | Select or add a Google Slides connection (OAuth) |
| 18 (Google Sheets) | **Google Sheets** | Select or add a Google Sheets connection (OAuth) |
| 21 (Gmail) | **Gmail** | Select or add a Gmail connection (OAuth) |
| 22 (Slack) | **Slack** | Select or add a Slack connection (OAuth + channel scope) |

**Tip:** You can reuse the same Google OAuth connection across all Google modules. Make.com will prompt you once and apply it.

### Step 4: Set Scenario Parameters

The blueprint uses **scenario parameters** (not hardcoded values) for configuration. Click the **settings icon** (gear) on the scenario tab and go to **Parameters** tab. Add the following:

| Parameter Name | Type | Example Value | Description |
|---------------|------|---------------|-------------|
| `property_id` | Text | `123456789` | Your GA4 property ID |
| `ad_account_id` | Text | `act_1234567890` | Facebook Ads account ID |
| `google_ads_customer_id` | Text | `1234567890` | Google Ads customer ID (digits only) |
| `developer_token` | Text | `AbCDEfGHIJ...` | Google Ads developer token |
| `site_url` | Text | `sc_domain:example.com` | Search Console property URL |
| `slides_template_id` | Text | `1ABCxyz...` | (Optional) Google Slides template ID — leave blank to use default blank template |
| `log_sheet_id` | Text | `1ABCxyz...` | Google Sheet ID for logging reports |
| `bcc_email` | Text | `agency@example.com` | BCC address for sent reports |
| `slack_channel` | Text | `#reports` | Slack channel for team notifications |
| `openai_api_key` | Secret | `sk-proj-...` | OpenAI API key (stored securely) |

**To set parameters:**
1. Click the scenario name at the top → **Settings**
2. Go to the **Parameters** tab
3. Add each parameter, paste its value, and save

### Step 5: Activate the Scenario

1. Click **Save** (💾 icon) to save the scenario
2. Click the **On/Off toggle** to activate it
3. Copy the **Webhook URL** from the first module (the webhook trigger)
4. Test with [Testing Instructions](#testing-instructions) below

---

## Module-by-Module Walkthrough

### Module 1: Webhook — Receive Trigger
- **Purpose:** Entry point. Accepts a POST request with the report parameters
- **Input Payload (JSON):**
  ```json
  {
    "client_name": "Acme Corp",
    "report_month": "2026-07",
    "data_sources": "ga4,fb_ads,google_ads,search_console",
    "output_format": "google_slides",
    "send_to": "client@acme.com"
  }
  ```
- **Fields Explained:**
  - `client_name` — Displayed in the report title and slides
  - `report_month` — Determines the date range (uses the full month)
  - `data_sources` — Comma-separated list; only selected sources are fetched
  - `output_format` — `"google_slides"` or `"pdf"`
  - `send_to` — Recipient email for the delivered report

### Module 2: Router — Data Source Selector
- **Purpose:** Routes execution to only the data sources specified in `data_sources`
- **How It Works:** Each route corresponds to a data source:
  - Route 1: GA4 (if `ga4` in data_sources)
  - Route 2: Facebook Ads (if `fb_ads` in data_sources)
  - Route 3: Google Ads (if `google_ads` in data_sources)
  - Route 4: Search Console (if `search_console` in data_sources)
- **Fallback:** If no data sources are specified, all routes run.

### Module 3: HTTP — Fetch GA4 Data
- **Purpose:** Calls the Google Analytics Data API to pull key metrics
- **Metrics Retrieved:** Sessions, active users, new users, bounce rate, avg session duration, conversion rate, transactions, revenue
- **Dimensions:** Date, source, medium — enables trend and channel analysis
- **Authentication:** OAuth 2.0 via Google Analytics connection

### Module 4: HTTP — Fetch Facebook Ads Data
- **Purpose:** Calls Facebook Graph API Ads Insights endpoint
- **Metrics Retrieved:** Impressions, clicks, spend, reach, frequency, CTR, CPC, CPM, conversions
- **Level:** Account-level aggregation for the month
- **Authentication:** Facebook Ads connection (OAuth)

### Module 5: HTTP — Fetch Google Ads Data
- **Purpose:** Runs a Google Ads Query Language (GAQL) search across campaigns
- **Metrics Retrieved:** Campaign name, impressions, clicks, cost, conversions, conversion value, avg CPC, CTR
- **Authentication:** Google Ads connection + Developer Token

### Module 6: HTTP — Fetch Search Console Data
- **Purpose:** Queries Search Console for search analytics
- **Metrics Retrieved:** Queries, pages, devices, clicks, impressions, CTR, position
- **Authentication:** Google Search Console connection

### Module 7: Aggregator — Merge Data
- **Purpose:** Waits for all data source branches to finish, then merges results into one unified JSON object
- **Why It Matters:** The AI needs all data in a single payload to write a cohesive report
- **Behavior:** Uses "all_of" aggregate mode — collects outputs from modules 3–6

### Module 8: JSON — Create Report Data Payload
- **Purpose:** Structures the merged data into a clean JSON object with metadata
- **Fields Added:** `client_name`, `report_month`, `report_period` (formatted), `generated_at`, `template_version`
- **Output:** This is the payload sent to OpenAI

### Module 9: HTTP — OpenAI Chat Completion
- **Purpose:** Sends the aggregated data to GPT-4o with a detailed system prompt
- **System Prompt:** Instructs the AI to act as an expert digital marketing analyst, producing:
  1. Executive Summary
  2. Channel-by-Channel Analysis
  3. Wins & Opportunities
  4. Recommendations
- **Model:** GPT-4o (configurable — change to `gpt-4o-mini` to save costs)
- **Temperature:** 0.7 (balances creativity and consistency)
- **Max Tokens:** 4,096
- **Authentication:** Bearer token (your OpenAI API key)

### Module 10: JSON — Parse Narrative Content
- **Purpose:** Extracts the `choices[0].message.content` from OpenAI's response
- **Output:** Clean Markdown narrative ready for slides

### Module 11: Google Slides — Create Presentation
- **Purpose:** Creates a new Google Slides presentation
- **Template Support:** If `slides_template_id` is configured, it uses that as a template (preserving your branding)
- **Fallback:** If no template ID, creates a blank presentation

### Modules 12–16: Google Slides — Build Slide Deck
Each module adds a slide to the presentation:

| Module | Slide | Content Source |
|--------|-------|----------------|
| 12 | **Title Slide** | Client name, period, generation date |
| 13 | **Executive Summary** | Extracted from the AI narrative |
| 14 | **Channel Analysis** | Extracted from the AI narrative |
| 15 | **Wins & Opportunities** | Extracted from the AI narrative |
| 16 | **Recommendations** | Extracted from the AI narrative |

- **Layout Used:** `TITLE_AND_BODY` for content slides, `TITLE_ONLY` for title slide
- **Content Extraction:** Uses `extractSection()` functions to pull the right section from the Markdown narrative

### Module 17: Google Slides — Apply Branding
- **Purpose:** Replaces placeholder text across all slides (e.g., client name)
- **Customization:** Add more replacements here — logo URLs, brand colors, etc.

### Module 18: Google Sheets — Log Report
- **Purpose:** Appends a row to your logging spreadsheet
- **Columns Logged:** Timestamp, client name, period, presentation ID, URL, format, recipient, status
- **Use Case:** Build a dashboard or audit trail of all delivered reports

### Module 19: Router — Output Format
- **Purpose:** Routes to PDF export if `output_format = "pdf"`, otherwise skips to email
- **Route 1 (PDF):** Goes through module 20 (export)
- **Route 2 (Google Slides):** Goes directly to module 21 (email with link)

### Module 20: Google Slides — Export as PDF
- **Purpose:** Exports the presentation as a PDF file
- **Format:** `application/pdf`
- **Output:** Binary data used as email attachment

### Module 21: Gmail — Send Email
- **Purpose:** Sends the report to the client with a preview
- **Email Includes:**
  - Link to live Google Slides presentation (if `google_slides` format)
  - PDF attachment (if `pdf` format)
  - Executive summary preview (truncated to 500 chars)
  - Professional HTML template
- **CC/BCC:** Configured via `bcc_email` parameter (for agency records)

### Module 22: Slack — Notify Team
- **Purpose:** Posts a delivery notification to your team channel
- **Includes:** Client name, period, format, delivery recipient, link to presentation
- **Channel:** Configured via `slack_channel` parameter

### Module 23: Webhook — Send Response
- **Purpose:** Returns a JSON response to the webhook caller
- **Response Body:**
  ```json
  {
    "success": true,
    "client_name": "Acme Corp",
    "report_period": "July 2026",
    "presentation_url": "https://docs.google.com/presentation/d/...",
    "presentation_id": "...",
    "delivered_to": "client@acme.com"
  }
  ```

---

## Testing Instructions

### Method 1: Use the Make.com Webhook Tester

1. Activate the scenario so the webhook is live
2. Copy the **Webhook URL** from module 1
3. Open a terminal or use a tool like **Postman**, **Insomnia**, or **cURL**
4. Send a POST request:

```bash
curl -X POST "https://hook.make.com/your-unique-webhook-url" \
  -H "Content-Type: application/json" \
  -d '{
    "client_name": "Test Client",
    "report_month": "2026-07",
    "data_sources": "ga4,fb_ads,google_ads,search_console",
    "output_format": "google_slides",
    "send_to": "you@example.com"
  }'
```

5. Watch the scenario run in real-time on the Make.com canvas
6. Check your email for the delivered report
7. Check the Google Sheet for the log entry
8. Check Slack for the team notification

### Method 2: Schedule with Make.com Scheduler

Instead of a webhook, you can trigger the scenario on a schedule:

1. Replace module 1 (webhook) with a **Schedule** module
2. Set it to run monthly (e.g., every 1st of the month at 9:00 AM)
3. Use **Set Variables** modules or static values for client parameters
4. Or, iterate through a Google Sheet of clients for batch reporting

### Method 3: Integrate via Zapier / Pabbly

Send a webhook POST from any other automation tool. The payload format is the same as Method 1.

---

## Troubleshooting

### Common Issues & Solutions

| Issue | Likely Cause | Solution |
|-------|-------------|----------|
| **"Connection not found"** error | OAuth connection not set up | Click the module, select "Add a connection" and re-authorize |
| **GA4 returns no data** | Property ID incorrect or data not yet populated | Verify `property_id` parameter; check GA4 reporting interface for the same period |
| **Facebook Ads returns empty** | Ad account ID format wrong | Ensure format is `act_XXXXXXXXX` (with `act_` prefix) |
| **Google Ads returns "DEVELOPER_TOKEN_NOT_APPROVED"** | Developer token not yet approved | Apply for basic access in Google Ads API Center |
| **OpenAI returns 401 Unauthorized** | Invalid API key | Check your OpenAI API key in the HTTP connection settings |
| **Google Slides returns "403"** | Slides API not enabled | Go to Google Cloud Console → Enable Google Slides API |
| **Gmail not sending** | Less secure apps / OAuth scope | Ensure Gmail API is enabled and the connection has `https://mail.google.com/` scope |
| **Slack message not posting** | Channel not found or bot not invited | Invite the Make.com Slack app to the channel with `/invite @Make` |
| **Report narrative is empty** | OpenAI response parsing issue | Check module 9 output; verify the `choices[0].message.content` path exists |
| **Webhook returns 404** | Scenario is not active | Toggle the scenario ON (the switch should be green) |
| **"Roundtrip limit exceeded"** | Too many module iterations | In scenario settings, increase "Max roundtrips" to 3–5 |

### Debugging Steps

1. **Run once manually** — Click the "Run once" button on the scenario
2. **Check module bubbles** — Each module shows input/output when you click it after a run
   - Green checkmark = success
   - Red exclamation = error (click to see the error details)
3. **Use the "Revert" feature** — If a module fails, you can adjust parameters and click "Revert" to retry from that point
4. **Enable "Auto Commit"** — In scenario settings, disable auto-commit during debugging so failed runs don't consume operations
5. **Check raw data** — If the narrative looks wrong, inspect the data being sent to OpenAI (module 8 output) — the AI is only as good as the data it receives

### Operation Limits

A single report run consumes approximately:

| Module | Operations |
|--------|-----------|
| Webhook trigger | 1 |
| Router (2 routes avg) | 2 |
| Data fetches (3 sources avg) | 3 |
| JSON/Aggregator | 2 |
| OpenAI API call | 1 |
| Google Slides (7 modules) | 7 |
| Google Sheets log | 1 |
| Gmail send | 1 |
| Slack notification | 1 |
| Webhook response | 1 |
| **Total per run** | **~20 operations** |

If you run 50 reports/month, you'll need a plan with at least 1,000 operations (plus buffer).

---

## Customization Tips

### Add More Data Sources
Duplicate modules 3–6 and add connections for:
- **LinkedIn Ads** (via HTTP module)
- **TikTok Ads** (via HTTP module)
- **HubSpot** (CRM data for lead conversion context)
- **SEMrush / Ahrefs** (SEO ranking data)

### Custom Branding
1. Create a branded Google Slides template with your logo, colors, and fonts
2. Add the template's ID to the `slides_template_id` parameter
3. The scenario will use it as the base for all reports

### Change the AI Model
In module 9 (OpenAI), change the `model` parameter:
- `gpt-4o` — Best quality (default)
- `gpt-4o-mini` — Cheaper, slightly less detailed
- `gpt-4-turbo` — Alternative high-quality option

### Adjust the AI Prompt
Edit the `system` message in module 9 to change:
- **Tone** — "friendly", "formal", "data-heavy", "executive"
- **Structure** — Add/remove sections from the report
- **Focus** — Emphasize certain KPIs or channels

### Batch Multiple Clients
To run reports for multiple clients in one go:
1. Store client data in a Google Sheet (one row per client)
2. Replace the webhook trigger with a **Google Sheets — Watch Rows** module
3. Use an **Iterator** to process each client
4. Add a **Schedule** to run monthly

### Add PDF Attachment to Emails
If you always want both Slides and PDF:
1. Remove the router (module 19)
2. Always export as PDF (module 20)
3. Add both the Slides link and PDF attachment in the email

---

**Need help?** Reach out via the Gumroad product page or open an issue in the product repository.

© 2026 Agency Ops Toolkit — Narrative Monthly Report Builder v1.2
