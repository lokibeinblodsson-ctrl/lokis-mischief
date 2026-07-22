# Agency Client Onboarding Agent — Setup Guide

**Time to install:** ~15 minutes
**Time saved:** 3-5 hours per new client
**Difficulty:** Beginner-friendly

---

## Quick Start

### 1. Import the Blueprint into Make.com

1. Go to your Make.com account
2. Click **Create a new scenario**
3. Click the three dots (⋮) menu → **Import Blueprint**
4. Paste the JSON from `deployed-blueprint.json`
5. Click **Save**

### 2. OR Open the Pre-Configured Scenario

Direct link: [https://us2.make.com/scenario/5707191/edit](https://us2.make.com/scenario/5707191/edit)

### 3. Connect Your Accounts

After importing, you'll need to connect:
- **Gmail** → Send welcome emails
- **Google Drive** → Create client folders
- **Google Sheets** → Log client records
- **Slack** → Team notifications

Click each module that shows a red warning indicator and authorize the connection.

### 4. Configure Your Webhook

Replace the HTTP trigger with a Make.com **Webhook** module:
- Right-click the HTTP module → **Replace** → Search "Webhook" → Select **Webhook** → **Custom Webhook**
- Click **Add** to generate your unique webhook URL
- Use this URL in your client intake forms (Typeform, Gravity Forms, etc.)

---

## What This Workflow Does

When a new client fills out your intake form (webhook), this workflow automatically:

1. **Analyzes** the client intake data with AI (GPT-4o)
2. **Generates** a personalized welcome plan, timeline, and task checklist
3. **Creates** a structured Google Drive folder with 7 subfolders
4. **Creates** an Asana project with phases and sections
5. **Notifies** your team via Slack with links to everything
6. **Sends** a warm welcome email to the client
7. **Logs** everything to a Google Sheets tracker
8. **Creates** a client record in Notion
9. **Returns** a confirmation with links

---

## Prerequisites

| Account | Type Needed | Cost |
|---|---|---|
| Make.com | Free or Pro | Free tier works |
| OpenAI | API account | Pay-as-you-go (~$0.10/workflow) |
| Google Workspace | Business | Usually already have |
| Asana | Free or Premium | Free tier works |
| Slack | Any workspace | Free tier works |
| Notion | Any workspace | Free tier works |

---

## Step 1: Import the Blueprint into Make.com

1. Go to [make.com](https://www.make.com) and log in
2. Click **Create a new scenario**
3. Click the **three dots** (⋮) → **Import Blueprint**
4. Select the `agency-client-onboarding-blueprint.json` file
5. Click **OK**

The scenario will appear with all 10 modules connected.

---

## Step 2: Configure Each Module

### Module 1 — Webhook (Client Intake Form)
1. Click the webhook module
2. Copy the webhook URL
3. Paste this URL into your:
   - Google Form (use Formatter add-on)
   - Or Typeform (webhook integration)
   - Or your own website form
4. Set up the form with these fields:
   - Client Name (text)
   - Company Name (text)
   - Email (email)
   - Phone (text)
   - Service Type (dropdown)
   - Project Scope (textarea)
   - Budget Range (text)
   - Start Date (date)

### Module 2 — OpenAI (AI Welcome Plan)
1. Click the OpenAI module
2. Click **Add connection** → **OpenAI**
3. Enter your **OpenAI API Key**
   - Get it at: https://platform.openai.com/api-keys
4. Model: `gpt-4o` (recommended) or `gpt-4o-mini` (cheaper)
5. The system prompt is pre-configured — customize if needed

### Module 3 — JSON Parser
- This module extracts sections from the AI response
- No configuration needed (auto-configured)

### Module 4 — Google Drive Folder Creator
1. Click the module
2. Click **Add connection** → **Google Drive**
3. Sign in with your Google Workspace account
4. Set **Parent Folder** — create a folder called "Client Projects" in your Google Drive and paste its ID here
5. The 7 subfolders are pre-configured

### Module 5 — Asana Project Creator
1. Click the module
2. Click **Add connection** → **Asana**
3. Authorize with your Asana account
4. Set **Workspace** and **Team** from the dropdowns
5. Project sections are pre-configured

### Module 6 — Slack Notification
1. Click the module
2. Click **Add connection** → **Slack**
3. Authorize with your Slack workspace
4. Select the **Channel** where your team wants notifications
5. The message template is pre-configured

### Module 7 — Gmail Welcome Email
1. Click the module
2. Click **Add connection** → **Gmail**
3. Sign in with your agency email
4. Set **CC** to your team email
5. Subject line and body are pre-configured

### Module 8 — Google Sheets Tracker
1. Create a Google Sheet called "Client Onboarding Tracker"
2. Add header row: Date, Client Name, Company, Email, Service, Budget, Start Date, Status, Drive Link, Asana Link
3. Click the module → **Add connection** → **Google Sheets**
4. Select your spreadsheet and sheet

### Module 9 — Notion Client Record
1. Create a Notion database called "Clients"
2. Add properties: Client Name (title), Company (text), Email (email), Phone (phone), Service (select), Status (select), Start Date (date), Google Drive (url), Asana Project (url)
3. Click the module → **Add connection** → **Notion**
4. Authorize with your Notion workspace
5. Select your Clients database

### Module 10 — Webhook Response
- Auto-configured. Returns success data to your form.

---

## Step 3: Test the Workflow

1. Click **Run once** in Make.com
2. Submit your test form with sample data
3. Check:
   - [ ] Google Drive folder created with 7 subfolders
   - [ ] Asana project appears with sections
   - [ ] Slack notification sent
   - [ ] Welcome email received
   - [ ] Google Sheets row added
   - [ ] Notion client record created
   - [ ] Confirmation returned to form

---

## Step 4: Schedule & Activate

1. Click the clock icon in Make.com
2. Set schedule: **Every 15 minutes** (for forms) or **Immediately** (for webhooks)
3. Toggle **ON**
4. Name your scenario: `Client Onboarding Agent`

---

## Customization Guide

### Adding More Tools
Want to connect other tools? Add modules for:
- **HubSpot** — Create contact + deal
- **QuickBooks** — Create invoice
- **Calendly** — Schedule kickoff call
- **Zoom** — Create meeting template
- **DocuSign** — Send agreement for signature

### Modifying the AI Prompt
Edit the OpenAI system prompt to match your agency's tone:
- Change the welcome message style
- Add specific deliverables unique to your services
- Include compliance disclaimers (GDPR, HIPAA)

### Adding Conditional Logic
Want different flows for different service types?
- Add a **Router** module after the webhook
- Route based on `service_type` to different project templates
- Each route can have its own Asana template, Drive folder, and email

---

## Troubleshooting

| Problem | Solution |
|---|---|
| "Connection error" | Re-authorize the app connection in Make.com |
| AI returns nonsense | Adjust the system prompt — be more specific |
| Google Drive folder not created | Check parent folder ID and permissions |
| Email not sending | Check Gmail rate limits (500/day) |
| Slack message not posting | Ensure bot is invited to the channel |
| Webhook not receiving data | Check form integration — test with Postman |

---

## API Keys Overview

| Service | Where to Get It | Cost |
|---|---|---|
| OpenAI | https://platform.openai.com/api-keys | $0.01-0.10/run |
| Google Drive | Automatic via Make auth | Free |
| Asana | Automatic via Make auth | Free |
| Slack | Automatic via Make auth | Free |
| Gmail | Automatic via Make auth | Free |
| Notion | https://www.notion.so/my-integrations | Free |

---

## Support

- **Documentation:** This guide
- **Discord:** Join our private community for support
- **Updates:** Lifetime updates included — we'll notify you when the workflow changes

---

*Built for Make.com 2.x | Compatible with OpenAI GPT-4o and GPT-4o-mini*
