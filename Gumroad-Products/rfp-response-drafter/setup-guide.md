# RFP / RFI Response Drafter — Setup Guide

## Product Overview

The **RFP / RFI Response Drafter** is a fully automated Make.com workflow that accepts an RFP or RFI document, extracts requirements using AI-powered text parsing, drafts tailored responses from your knowledge base, creates a polished Google Doc, stores it in your team's Google Drive folder, and notifies everyone via Gmail and Slack — all in one seamless flow.

**Price:** $39  
**Purchase Link:** [Buy on Stripe](https://buy.stripe.com/test_28E00c7DM347g3ybqz9Zm02)

---

## Table of Contents

1. [Prerequisites](#1-prerequisites)
2. [Installation Overview](#2-installation-overview)
3. [Importing the Blueprint](#3-importing-the-blueprint)
4. [Module Walkthrough](#4-module-walkthrough)
5. [Configuration Guide](#5-configuration-guide)
6. [Testing the Workflow](#6-testing-the-workflow)
7. [Troubleshooting](#7-troubleshooting)
8. [Customization Tips](#8-customization-tips)

---

## 1. Prerequisites

Before installing this blueprint, ensure you have:

### Required Accounts

| Service | Purpose | Plan Required |
|---------|---------|---------------|
| **Make.com** | Automation platform (formerly Integromat) | Pro plan or higher (to use OpenAI and Google modules) |
| **OpenAI** | AI analysis and draft generation | Paid API account with GPT-4 access |
| **Google Account** | Google Docs, Drive, and Gmail | Any Google Workspace or free Gmail |
| **Slack** | Team notifications | Any Slack workspace (free tier works) |

### What You'll Need on Hand

- **OpenAI API Key** — from [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- **Google Service Account** (recommended) or OAuth 2.0 credentials — from [console.cloud.google.com](https://console.cloud.google.com)
- **Slack API Token / Webhook URL** — from [api.slack.com](https://api.slack.com)
- **Google Drive Folder ID** — the ID of the folder where drafts will be stored
- **Team Email Address** — distribution list or shared inbox for notifications
- **Slack Channel ID** — where draft summaries will be posted

### Recommended Knowledge

- Basic familiarity with Make.com interface
- Understanding of webhooks and JSON
- Access to your Make.com team/org (or personal workspace)

---

## 2. Installation Overview

The installation process follows these high-level steps:

1. **Import** the blueprint JSON into Make.com
2. **Connect** each service (OpenAI, Google, Slack)
3. **Configure** folder paths, email recipients, and channel IDs
4. **Activate** the webhook and run a test
5. **Integrate** with your existing RFP intake process

Estimated setup time: **20–30 minutes**.

---

## 3. Importing the Blueprint

### Step 1: Download the Blueprint File

The blueprint is provided as `deployed-blueprint.json`. Save it locally.

### Step 2: Import into Make.com

1. Log in to your **Make.com** account.
2. Click **Create a new scenario** (or go to your team dashboard and click **+ Create a new scenario**).
3. Click the **three dots (⋯)** in the lower-left corner of the new scenario canvas.
4. Select **Import Blueprint**.
5. Choose the `deployed-blueprint.json` file.
6. Click **Import**.

You should see all 10 modules appear on the canvas, wired together in sequence.

### Step 3: Enable the Scenario

The scenario will appear with a grey status indicator. **Do not enable it yet** — you need to configure connections first.

---

## 4. Module Walkthrough

The workflow consists of **10 modules** arranged in a linear pipeline:

```
Webhook → Download Doc → Text Parser → OpenAI (Analyze) → Parse JSON →
OpenAI (Draft) → Google Docs → Google Drive → Gmail → Slack
```

### Module 1: Receive RFP/RFI Document (Webhook)

- **Type:** Custom Webhook
- **Purpose:** Entry point — receives RFP document data via HTTP POST
- **Input format (JSON body):**

```json
{
  "documentUrl": "https://example.com/rfp-document.pdf",
  "documentTitle": "City IT Infrastructure RFP #2024-015",
  "documentType": "RFP",
  "submissionDeadline": "2026-08-15",
  "organizationName": "City of Springfield",
  "additionalContext": "We have worked with this client before on Project X"
}
```

- **All fields are required** except `additionalContext`.
- The webhook returns an immediate confirmation response (HTTP 200) and processes in the background.

### Module 2: Download Document from URL (HTTP / Util)

- **Type:** HTTP / Make Utility
- **Purpose:** Fetches the RFP document text from the provided URL
- Currently configured to fetch **raw text**. If your documents are PDFs, you may need a PDF-to-text converter module (see Customization Tips).

### Module 3: Parse & Extract Requirements (Text Parser)

- **Type:** Text Parser (Regex)
- **Purpose:** Uses regex patterns to extract:
  - Section headers and structure
  - Requirements (sentences containing "shall", "must", "required", etc.)
  - Deadline dates
  - Scope of work
  - Qualification requirements
  - Evaluation criteria
- **Output:** Structured text segments fed to the AI modules.

**Customization:** You can add or modify regex patterns in this module to match your specific RFP formats.

### Module 4: Enhance Extracted Data with AI (OpenAI)

- **Type:** OpenAI (Chat Completion)
- **Model:** GPT-4 (temperature: 0.3)
- **Purpose:** Analyzes the raw document text and extracted segments to produce a structured JSON analysis including:
  - Summary of the RFP
  - Key requirements (categorized as mandatory/optional)
  - Evaluation criteria with weights
  - Deadlines
  - Suggested approach strategy

### Module 5: Parse AI Analysis JSON (JSON)

- **Type:** JSON Parser
- **Purpose:** Converts the AI's text response into structured JSON objects that downstream modules can reference.

### Module 6: Search Knowledge Base & Draft Responses (OpenAI)

- **Type:** OpenAI (Chat Completion)
- **Model:** GPT-4 (temperature: 0.5)
- **Purpose:** Generates full draft responses for each requirement, referencing a built-in knowledge base of past successful RFP responses. The output includes:
  - Executive Summary
  - Technical Approach
  - Project Management Plan
  - Qualifications & Experience
  - Timeline & Deliverables

**Note:** The knowledge base entries in this module are **sample references**. You should replace them with your own past winning responses (see Customization Tips).

### Module 7: Create Draft Document in Google Docs (Google Docs)

- **Type:** Google Docs
- **Purpose:** Creates a new Google Doc containing the draft response.
- **Title format:** `DRAFT - Response to {Document Title} - {Organization Name}`
- **Permissions:** The document is created under your connected Google account's default permissions.

### Module 8: Store Document in Google Drive Folder (Google Drive)

- **Type:** Google Drive
- **Purpose:** Moves the newly created Google Doc into your designated Google Drive folder for organized storage.
- Requires the **Folder ID** to be configured in the connection settings.

### Module 9: Notify Team via Email (Gmail)

- **Type:** Gmail
- **Purpose:** Sends an HTML-formatted email notification to the team with:
  - RFP title and organization
  - Submission deadline
  - Links to the draft document and Drive folder
- The email uses a clean, professional HTML template.

### Module 10: Post Summary to Slack (Slack)

- **Type:** Slack
- **Purpose:** Posts a rich message to your Slack channel with:
  - Header and key details
  - AI-generated summary
  - Action buttons to open the draft and Drive folder
  - Context footer with automation timestamp

---

## 5. Configuration Guide

### 5.1 OpenAI Connection

1. In the OpenAI module (Module 4 or 6), click **Add connection**.
2. Enter your **OpenAI API key**.
3. Select **GPT-4** as the model (or GPT-3.5-turbo if you prefer speed over depth).
4. Click **Save**.

> **💡 Tip:** OpenAI API keys are found at https://platform.openai.com/api-keys. Ensure the account has billing enabled and GPT-4 access.

### 5.2 Google Connections (Docs + Drive + Gmail)

**Option A: OAuth (Simpler, for personal accounts)**

1. In any Google module, click **Add connection**.
2. Select **OAuth**.
3. Sign in with your Google account and grant the requested permissions.
4. The same connection can be reused across Google Docs, Drive, and Gmail modules.

**Option B: Service Account (Recommended for teams)**

1. Go to [Google Cloud Console](https://console.cloud.google.com).
2. Create a project (or select existing).
3. Enable the **Google Docs API**, **Google Drive API**, and **Gmail API**.
4. Create a **Service Account** and download the JSON key.
5. In Make.com, use **Service Account** connection type and upload the key JSON.
6. Share your Google Drive folder and target Google Doc with the service account email.

### 5.3 Google Drive Folder ID

The Folder ID is a long string of characters in the folder's URL:

```
https://drive.google.com/drive/folders/1aBcDeFgHiJkLmNoPqRsTuVwXyZ123456789
                                                          ^^^^^^^^^^^^^^^^^^^^
                                                                 Folder ID
```

1. Create a dedicated folder in Google Drive (e.g., "RFP Responses").
2. Copy the Folder ID from the URL.
3. In the **Google Drive connection settings** (Module 8), paste the Folder ID into the `folderId` parameter.

### 5.4 Gmail Team Email

1. In the **Gmail connection settings** (Module 9), find the `teamEmail` parameter.
2. Enter the email address where notifications should be sent (e.g., `rfp-team@company.com`, `proposals@company.com`, or a distribution list).

### 5.5 Slack Channel ID

The Channel ID is found in Slack:

1. Open Slack in your browser.
2. Navigate to the target channel.
3. The URL will be: `https://app.slack.com/client/TXXXXX/CYYYYYYY` — the `CYYYYYYY` part is the Channel ID.
4. In the **Slack connection settings** (Module 10), paste this ID into the `channelId` parameter.

---

## 6. Testing the Workflow

### Step 1: Activate the Webhook

1. Click on **Module 1** (the webhook).
2. Copy the **Webhook URL** (looks like `https://hook.make.com/xxxxx`).
3. Keep this URL handy — you'll use it to send test data.

### Step 2: Enable the Scenario

1. Toggle the **On/Off** switch in the bottom bar.
2. The scenario should turn green.

### Step 3: Send a Test Payload

Use **curl**, **Postman**, or any HTTP client to POST to the webhook URL:

```bash
curl -X POST \
  https://hook.make.com/your-webhook-url \
  -H "Content-Type: application/json" \
  -d '{
    "documentUrl": "https://www.example.com/sample-rfp.txt",
    "documentTitle": "IT Services RFP - Test",
    "documentType": "RFP",
    "submissionDeadline": "2026-09-01",
    "organizationName": "Acme Corporation",
    "additionalContext": "Test run for the RFP drafter setup"
  }'
```

For a quick test without an actual document URL, you can use a publicly accessible text file or create a simple one with placeholder RFP content.

### Step 4: Monitor Execution

1. In Make.com, click the **clock icon** in the bottom bar to open **Execution history**.
2. Watch each module execute in real-time.
3. If a module fails, click it to see the error details.

### Step 5: Verify Outputs

| Output | How to Verify |
|--------|---------------|
| Google Doc created | Check Google Drive folder |
| Slack message posted | Check the configured Slack channel |
| Email sent | Check team inbox (and spam folder) |

---

## 7. Troubleshooting

### Common Issues & Fixes

#### Issue: Webhook receives data but nothing happens
- **Cause:** The scenario may not be enabled.
- **Fix:** Toggle the scenario ON. Check execution history for queued runs.

#### Issue: Module 2 (Download Document) fails
- **Cause 1:** The document URL is not publicly accessible.
- **Fix:** Ensure the URL does not require authentication. Use a signed URL or upload the document to a public location.
- **Cause 2:** The document is a PDF/image and cannot be parsed as text.
- **Fix:** Add a PDF-to-text module (see Customization Tips).

#### Issue: OpenAI module returns errors
- **Cause 1:** Invalid or expired API key.
- **Fix:** Regenerate the API key at [platform.openai.com](https://platform.openai.com).
- **Cause 2:** Insufficient quota or billing not enabled.
- **Fix:** Check your OpenAI usage dashboard and add credits.
- **Cause 3:** GPT-4 access not granted.
- **Fix:** Use `gpt-3.5-turbo` as a fallback (change model parameter in the module).

#### Issue: Google modules fail with "401 Unauthorized"
- **Cause:** OAuth token expired or service account permissions not set.
- **Fix:** Re-authenticate the connection. If using a service account, ensure the Google Doc/folder is shared with the service account email.

#### Issue: Gmail notifications go to spam
- **Cause:** Automated emails from Make.com may be flagged.
- **Fix:** Add the sending address to your contacts. Use a dedicated Google Workspace account for automation.

#### Issue: Slack message not posting
- **Cause 1:** Incorrect Channel ID.
- **Fix:** Double-check the channel ID (get it from Slack's About channel → More → Copy channel ID).
- **Cause 2:** Slack bot token lacks `chat:write` scope.
- **Fix:** Reinstall the Slack app with appropriate permissions.

#### Issue: JSON parsing in Module 5 fails
- **Cause:** The AI response didn't return valid JSON.
- **Fix:** Increase `maxTokens` in Module 4. Add a retry mechanism or adjust the system prompt to be stricter about JSON output.

---

## 8. Customization Tips

### 8.1 Add PDF Support

If your RPFs come as PDFs, add a **PDF to Text** module between Module 2 and 3:

1. Search for "PDF" in the Make.com module picker.
2. Use the **PDF.co** app, **ConvertAPI**, or **CloudConvert**.
3. Connect the text output to the Text Parser module.

### 8.2 Replace Knowledge Base References

The sample knowledge base entries in Module 6 are generic. Replace them with your actual past winning responses:

1. Open **Module 6** (OpenAI - Draft).
2. Find the `messages` array.
3. Replace the "Knowledge Base References" content with your own entries.
4. Structure each entry as: `- Past RFP: {Project Name} - Won with {Score}%. Key strategy: {Key strategy}.`

For a more robust knowledge base, consider:
- Storing entries in **Airtable** or **Google Sheets**.
- Adding a **Search/Retrieve** module before Module 6 to fetch relevant entries dynamically based on RFP category.

### 8.3 Add Human Review Step

To add a review step before storage:

1. After Module 7 (Google Docs), add a **Slack** module that sends a message to a **#rfp-review** channel.
2. Add a **Webhook response** module that pauses and waits for approval.
3. Connect the approval path to Module 8 (Google Drive) and the rejection path to a notification to the author.

### 8.4 Increase Temperature for Creativity

If you want more creative and less formulaic drafts, increase the `temperature` parameter in Module 6 from `0.5` to `0.7` or `0.8`.

### 8.5 Use GPT-4o for Faster Processing

If speed is a priority, change the model in both OpenAI modules from `gpt-4` to `gpt-4o` or `gpt-4o-mini`.

### 8.6 Add Error Handling

For production use, add error handler routes:

1. Right-click on any module → **Add error handler**.
2. Connect to a **Slack** or **Gmail** module that notifies you of failures.
3. Include the error details and the input data for debugging.

### 8.7 Connect to Your CRM

If you use **HubSpot**, **Salesforce**, or another CRM, add a module after the webhook to:
- Look up the organization's past interactions.
- Populate `additionalContext` automatically.
- Log the new RFP opportunity.

---

## Quick Reference: JSON Input Schema

```json
{
  "documentUrl": "string (required) — URL to the RFP/RFI document text",
  "documentTitle": "string (required) — Title of the RFP/RFI",
  "documentType": "string (required) — 'RFP', 'RFI', or 'RFQ'",
  "submissionDeadline": "string (required) — Due date (any parseable format)",
  "organizationName": "string (required) — Issuing organization name",
  "additionalContext": "string (optional) — Any notes, context, or instructions"
}
```

## Quick Reference: Outputs Produced

| Output | Location | Description |
|--------|----------|-------------|
| Google Doc | Google Drive folder | Full draft response with all sections |
| Email notification | Team inbox | HTML summary with links |
| Slack message | Designated channel | Rich preview with action buttons |

---

## Support

This blueprint is provided as a digital product. For setup assistance:
- Refer to this guide first
- Check [Make.com Help Center](https://www.make.com/en/help) for platform-specific issues
- For AI response quality issues, review your OpenAI system prompts

---

**Version:** 1.0.0 | **Updated:** July 20, 2026  
**Product:** [RFP / RFI Response Drafter](https://buy.stripe.com/test_28E00c7DM347g3ybqz9Zm02)
