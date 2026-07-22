# AI Client Concierge System — Setup Guide

**Price: $97** · [Buy on Gumroad](https://buy.stripe.com/test_dRm5kwf6e347dVq0LV9Zm06)

---

## Overview

The **AI Client Concierge System** is an automated Make.com scenario (workflow) that acts as your agency's first point of contact for incoming client inquiries. It uses **OpenAI GPT-4o** to analyze, qualify, and respond to leads in real time, dramatically reducing response time and ensuring no lead falls through the cracks.

### What It Does

| Trigger | Action |
|---|---|
| A prospect submits your website form | Webhook receives the data |
| Inquiry is analyzed | GPT-4o extracts intent, qualifies the lead, determines service fit, and drafts a personalized response |
| **If qualified** | → Google Calendar event (30-min discovery call, 2 days out, with Google Meet) → Branded confirmation email with calendar link → Logged to Google Sheets → Team notified on Slack |
| **If not qualified** | → Polite decline email with recommendations → Logged to Google Sheets for future nurture |
| Every weekday at 9 AM | Checks active leads, sends follow-up emails, updates statuses |

### Workflow Architecture

```
┌─────────────────┐
│  1. Webhook     │  Receives inquiry: {name, email, company, service_interest, budget, message}
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  2. HTTP Req    │  POST to OpenAI GPT-4o → structured JSON analysis
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  3. Router      │  Splits based on `qualified: true/false`
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
 Qualified   Not Qualified
    │         │
    ├─ 4. Google Calendar    ├─ 8. Gmail (Decline)
    ├─ 5. Gmail (Confirmation) └─ 9. Google Sheets (Log)
    ├─ 6. Google Sheets (Log)
    └─ 7. Slack (Notify)
    
Then, independently (recurring scheduler):

┌─────────────────┐
│ 10. Scheduler   │  Weekdays at 9AM ET
└────────┬────────┘
         ▼
┌─────────────────┐
│ 11. Sheets      │  Search for active leads needing follow-up
└────────┬────────┘
         ▼
┌─────────────────┐
│ 12. Iterator    │  Loop through each lead
└────────┬────────┘
         ▼
┌─────────────────┐
│ 13. Gmail       │  Send follow-up/check-in email
└────────┬────────┘
         ▼
┌─────────────────┐
│ 14. Sheets      │  Update lead status to "Follow-Up Sent"
└────────┬────────┘
         ▼
┌─────────────────┐
│ 15. Slack       │  Notify team of follow-up action
└─────────────────┘
```

---

## Prerequisites

Before importing the blueprint, make sure you have the following:

### Required Accounts & API Keys

| Service | What You Need | Cost |
|---|---|---|
| **Make.com** | A Make.com account (any paid plan that supports HTTP modules) | Free trial available, paid plans start at ~$9/mo |
| **OpenAI** | API key with access to GPT-4o | ~$0.01–0.03 per inquiry |
| **Google Account** | For Gmail, Google Calendar, Google Sheets | Free |
| **Slack** | Slack workspace with webhook/bot permissions | Free |

### Make.com Connections to Create

You'll need to set up the following connections in Make.com **before** activating the scenario:

1. **OpenAI** — Connection type: HTTP / API Key
   - Name: `OpenAI API`
   - API Key: Your OpenAI API key (starts with `sk-...`)
   - This maps to `{{3.apiKey}}` in the HTTP module

2. **Google Calendar** — Connection type: Google Calendar
   - Name: `Google Calendar`
   - Scopes: `https://www.googleapis.com/auth/calendar`
   - Authorize with your Google Workspace or Gmail account

3. **Gmail** — Connection type: Gmail
   - Name: `Gmail`
   - Scopes: `https://mail.google.com/`
   - Authorize with your agency email account

4. **Google Sheets** — Connection type: Google Sheets
   - Name: `Google Sheets`
   - Scopes: `https://www.googleapis.com/auth/spreadsheets`
   - Authorize with your Google account

5. **Slack** — Connection type: Slack
   - Name: `Slack`
   - Scopes: `chat:write`, `chat:write.public`, `channels:read`
   - Authorize with your Slack workspace

### Google Sheets Setup

Create a **single Google Sheet** with two sheets/tabs:

**Sheet 1: `Qualified Leads`**
Column headers (Row 1):
| A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Timestamp | Name | Email | Company | Phone | Service Interest | Best Service Fit | Budget | Budget Assessment | Timeline | Urgency | Message | Intent | Qualification Score | Status | Call Date | Call Time | Call Stage | Talking Points | Referral Source | Heard About | Service Explanation |

**Sheet 2: `Future Follow-Up`**
Column headers (Row 1):
| A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Timestamp | Name | Email | Company | Phone | Service Interest | Best Service Fit | Budget | Budget Assessment | Timeline | Urgency | Message | Intent | Qualification Score | Status | Call Date | Call Stage | Nurture Stage | Service Explanation | Referral Source | Heard About | Next Follow-Up | Notes |

### Slack Channel

Create or choose a Slack channel (recommended: `#lead-alerts`) where the bot will send notifications.

---

## Import Instructions

### Step 1: Download the Blueprint File

The blueprint is provided as `deployed-blueprint.json`. Save it to your computer.

### Step 2: Import into Make.com

1. Log in to your **Make.com** account
2. Click **Create a new scenario** (or go to Scenarios → Add new scenario)
3. Click the three dots (**⋯**) menu in the bottom-right corner
4. Select **Import Blueprint**
5. Choose the `deployed-blueprint.json` file
6. Click **Import**

### Step 3: Connect Your Accounts

After import, every module will show a warning icon ⚠️ — you need to assign your connections:

1. **Module 2 (HTTP → OpenAI)**: Click the module → under "Connection" → select your `OpenAI API` connection
2. **Module 4 (Google Calendar)**: Click → select your `Google Calendar` connection
3. **Module 5 (Gmail — Confirmation)**: Click → select your `Gmail` connection
4. **Module 6 (Google Sheets — Qualified)**: Click → select your `Google Sheets` connection
5. **Module 7 (Slack)**: Click → select your `Slack` connection
6. **Module 8 (Gmail — Decline)**: Click → select your `Gmail` connection
7. **Module 9 (Google Sheets — Follow-Up)**: Click → select your `Google Sheets` connection
8. **Module 11 (Sheets — Search)**: Click → select your `Google Sheets` connection
9. **Module 13 (Gmail — Follow-Up)**: Click → select your `Gmail` connection
10. **Module 14 (Sheets — Update)**: Click → select your `Google Sheets` connection
11. **Module 15 (Slack — Follow-Up Notify)**: Click → select your `Slack` connection

### Step 4: Configure the Google Sheet ID

In modules **6, 9, 11, and 14**, replace `YOUR_SPREADSHEET_ID_HERE` with your actual Google Sheet ID.

**How to find your Sheet ID:**
- Open your Google Sheet
- Look at the URL: `https://docs.google.com/spreadsheets/d/THIS_IS_THE_ID/edit`
- Copy the long alphanumeric string between `/d/` and `/edit`
- Paste it into each module's `spreadsheetId` field

### Step 5: Configure Slack Channel

In modules **7 and 15**, change the `channel` field from `#lead-alerts` to your actual Slack channel name.

### Step 6: Review Email Settings

- **From Name**: Change "Agency Concierge Team" to your agency name
- **Reply-To Email**: Change `hello@agency.com` to your agency's actual email
- **Email Body**: Review the HTML templates and replace any placeholder links (`https://agency.com/...`) with your actual URLs

### Step 7: Activate the Scenario

1. Click the **Schedule toggle** (clock icon) in the bottom-left to turn on the recurring scheduler
2. Click **Run once** to test (you'll be prompted for webhook data)
3. If everything works, click **Save** and toggle the scenario to **ON**

---

## Module-by-Module Walkthrough

### Module 1: Webhook — Receive Inbound Inquiry

**Type:** `webhook:receive`

This is the entry point. It receives a JSON POST payload with the following structure:

```json
{
  "name": "John Doe",
  "email": "john@company.com",
  "company": "Acme Inc",
  "service_interest": "AI Chatbot Development",
  "budget": "$10,000 - $15,000",
  "message": "We need an AI-powered customer service chatbot for our e-commerce store...",
  "phone": "+1-555-123-4567",
  "referral_source": "Google Search",
  "timeline": "Next quarter",
  "heard_about": "LinkedIn ad"
}
```

**Required fields:** `name`, `email`, `service_interest`, `message`
**Optional fields:** `company`, `budget`, `phone`, `referral_source`, `timeline`, `heard_about`

**Webhook URL:** Generated by Make.com after first save. Use this as your form's POST endpoint.

---

### Module 2: HTTP Request — GPT-4o Analysis

**Type:** `http:request`

This module sends the inquiry to OpenAI's GPT-4o API with a structured system prompt that instructs the AI to:

1. **Extract intent** — Classify as: `new_project_inquiry`, `status_update`, `general_question`, `partnership`, or `support`
2. **Qualify the lead** — Score 0–5 based on specific signals (project mention, budget, complete contact info, timeline, professionalism)
3. **Determine service fit** — Map to: Web Development, Mobile Development, AI & Automation, UI/UX Design, Consulting, or Other
4. **Write a personalized response** — Draft a warm email body
5. **Suggest meeting topics** — 2–3 talking points if qualified
6. **Assess urgency and budget**

The AI responds in strict JSON format which Make.com parses automatically.

**Key fields in the output (`{{2.data.*}}`):**
- `{{2.data.qualified}}` — Boolean, used by the router
- `{{2.data.qualification_score}}` — 0–5 score
- `{{2.data.intent}}` — Classified intent
- `{{2.data.best_service_fit}}` — Best service match
- `{{2.data.personalized_response}}` — Draft email body
- `{{2.data.suggested_meeting_topics}}` — Array of talking points

---

### Module 3: Router — Qualification Split

**Type:** `router:router`

The router has two paths:

- **Path A (route_a_qualified):** If `{{2.data.qualified}}` equals `true` → Modules 4, 5, 6, 7
- **Path B (route_b_not_qualified):** Else (default) → Modules 8, 9

---

### Module 4: Google Calendar — Create Discovery Call

**Type:** `googleCalendar:createEvent`

Creates a 30-minute Google Calendar event:

- **When:** 2 business days from now, 10:00–10:30 AM ET
- **Title:** `Discovery Call: {{1.name}} — {{2.data.extracted_company_name}}`
- **Description:** Includes inquiry details, AI analysis, suggested talking points
- **Attendees:** The prospect + internal team (team@agency.com)
- **Conference:** Google Meet link auto-generated
- **Reminders:** Email at 60 min, popup at 30 min and 10 min
- **Color:** Teal (colorId: 7)

**To customize the meeting time:**
- Change `startDate`/`endDate` formula: `addDays(now, 2)` → change the `2` to your desired buffer
- Change `startTime`/`endTime` to your preferred slot

---

### Module 5: Gmail — Send Confirmation Email (Qualified)

**Type:** `gmail:sendEmail`

Sends a richly designed HTML welcome email to the qualified prospect that includes:

- Calendar event details (date, time, duration)
- Google Meet join button
- Service interest and budget overview
- The AI-generated personalized response
- What to expect on the call
- Links to portfolio, process page
- Agency branding and signature

**Customization checklist:**
- [ ] Replace all `https://agency.com/...` links with your actual URLs
- [ ] Update `hello@agency.com` to your email
- [ ] Update `(555) 123-4567` to your phone
- [ ] Update `123 Business Ave, Suite 100, New York, NY 10001` to your address
- [ ] Change "Agency" to your agency name throughout
- [ ] Review and adjust colors in the CSS gradient

---

### Module 6: Google Sheets — Log Qualified Lead

**Type:** `googleSheets:addRow`

Logs the lead to the "Qualified Leads" sheet with all analysis data.

Maps 22 columns including:
- Timestamp of inquiry
- Prospect's contact info
- Service interest + AI-determined best fit
- Budget range + AI budget assessment
- Timeline + urgency
- Original message + AI intent and score
- Scheduled call info (date, time, stage)
- Talking points for the internal team
- Referral source and acquisition channel

---

### Module 7: Slack — Notify Team

**Type:** `slack:sendMessage`

Sends a rich Slack message to `#lead-alerts` (or your chosen channel) with:

- **Header:** 🚀 New Qualified Lead — Action Required
- **Fields:** Name, Company, Email, Phone, Service Interest, Best Fit, Budget, Timeline, Score, Intent
- **Inquiry message** and **AI response** in blockquotes
- **Suggested talking points**
- **Action buttons:** Email Prospect, Open Calendar, Not Interested
- **Context footer** with timestamp

---

### Module 8: Gmail — Send Decline Email (Not Qualified)

**Type:** `gmail:sendEmail`

Sends a polite, helpful decline email that:
- Thanks the prospect for their interest
- Explains transparently that this isn't the best fit right now
- Provides alternative recommendations and resources
- Links to blog, free resources, community
- Invites them to reach out again in the future

**Customization checklist:**
- [ ] Same as Module 5 — update all branding, URLs, email, address, phone

---

### Module 9: Google Sheets — Log Not Qualified Lead

**Type:** `googleSheets:addRow`

Logs the lead to the "Future Follow-Up" sheet with:
- All contact and inquiry data
- AI analysis results
- Status: "Not Qualified"
- Next follow-up date: 90 days from now (for nurture campaigns)

---

### Module 10: Scheduler — Daily Trigger

**Type:** `schedule:trigger`

Runs every **weekday at 9:00 AM Eastern Time**. This kicks off the follow-up sub-scenario.

**To change the schedule:**
- Edit the `time` field (e.g., `"08:00"`)
- Edit `daysOfWeek` (e.g., add `"Saturday"`)
- Change `timezone` to your timezone

---

### Module 11: Google Sheets — Search Active Leads

**Type:** `googleSheets:searchRows`

Searches the "Qualified Leads" sheet for rows where the **Call Stage** column equals `"Discovery Call Scheduled"` — these are leads who haven't converted yet and need a follow-up nudge.

Returns up to 50 results, ordered by call date (ascending — oldest first).

---

### Module 12: Iterator — Loop Through Leads

**Type:** `iterator:iterator`

Loops through each lead returned from the search, processing them one at a time. Each iteration triggers Modules 13–15.

---

### Module 13: Gmail — Send Follow-Up Email

**Type:** `gmail:sendEmail`

Sends a gentle check-in email to each lead:
- Warm greeting referencing their service interest
- Asks if they're still interested
- Provides two CTAs: "Yes, Let's Talk!" and "Not Right Now"
- Includes an unsubscribe link

---

### Module 14: Google Sheets — Update Lead Status

**Type:** `googleSheets:updateRow`

Updates the **Call Stage** column for the processed lead from `"Discovery Call Scheduled"` to `"Follow-Up Sent"` so they aren't contacted again on the next daily run.

---

### Module 15: Slack — Notify Team of Follow-Up

**Type:** `slack:sendMessage`

Sends a brief notification to `#lead-alerts` confirming a follow-up was sent, including the lead name, company, and service interest.

---

## Configuration Guide

### Customizing the AI Prompt

The GPT-4o system prompt (in Module 2) controls how inquiries are analyzed. You can customize:

- **Qualification criteria** — Change the 5 signals or their weighting
- **Service categories** — Add/remove services in the "best service fit" list
- **Response tone** — Adjust the tone instructions (professional, casual, formal)
- **Output fields** — Add new JSON fields by extending the response template

To edit: Open Module 2 → find the system message in the `messages` array → edit the `content` field.

### Customizing Email Templates

Both email modules (5 and 8) contain full HTML templates with inline CSS. Edit them directly in the module's `body` field. Key things to change:

1. **Branding colors** — Update the gradient colors in the `.header` CSS
2. **Logo** — Add an `<img>` tag at the top of the header
3. **Links** — Replace all `https://agency.com/...` placeholders
4. **Contact info** — Update email, phone, address

### Customizing Follow-Up Logic

To change follow-up timing:
- Module 14: Change what status the lead gets updated to
- Module 9: Change the `addDays(now, 90)` value for longer/shorter nurture cycles
- Add conditional modules after Module 12 to skip certain lead statuses

### Adding More Automation

The system is designed to be extended. Popular additions:

- **SMS notification** — Add Twilio module alongside Slack
- **CRM integration** — Add HubSpot or Salesforce module after Google Sheets
- **Proposal generation** — Add PDF generation + DocuSign after confirmation
- **Multi-channel outreach** — Add LinkedIn or Messenger modules
- **Lead scoring dashboard** — Connect to Data Studio or Tableau

---

## Testing Guide

### Test 1: Qualified Lead Flow

Send this payload to your webhook URL:

```json
{
  "name": "Sarah Johnson",
  "email": "sarah@techstartup.io",
  "company": "TechStartup.io",
  "service_interest": "AI Chatbot Development",
  "budget": "$15,000 - $25,000",
  "message": "Hi! We're a fast-growing SaaS company looking to build an AI-powered customer support chatbot. We have a clear spec and budget, and we're hoping to launch within 6-8 weeks. Can you help?",
  "phone": "+1-555-987-6543",
  "referral_source": "Google Search",
  "timeline": "6-8 weeks",
  "heard_about": "LinkedIn"
}
```

**Expected results:**
- ✅ Google Calendar event created (2 days from now)
- ✅ Confirmation email sent to sarah@techstartup.io
- ✅ Row added to "Qualified Leads" sheet
- ✅ Slack notification in #lead-alerts
- ✅ AI response is warm, professional, and relevant

### Test 2: Not Qualified Lead Flow

```json
{
  "name": "Mike Brown",
  "email": "mike@gmail.com",
  "company": "",
  "service_interest": "Website",
  "budget": "$500",
  "message": "Can you make me a website? I don't really know what I need. Just something basic.",
  "phone": "",
  "referral_source": "Friend",
  "timeline": "ASAP",
  "heard_about": "Friend"
}
```

**Expected results:**
- ✅ Polite decline email sent to mike@gmail.com
- ✅ Row added to "Future Follow-Up" sheet
- ✅ No calendar event created
- ✅ No Slack notification (or customize if desired)

### Test 3: FAQ / General Question

```json
{
  "name": "Alex Chen",
  "email": "alex@example.com",
  "company": "Example Corp",
  "service_interest": "General Question",
  "budget": "",
  "message": "What technologies do you typically use for web development projects? Do you work with React and Node.js?",
  "phone": "",
  "referral_source": "",
  "timeline": "",
  "heard_about": ""
}
```

**Expected results:**
- ✅ The AI should classify this as `general_question`
- ✅ Qualification score will likely be low (no project scope)
- ✅ Polite decline sent with FAQ-style response
- ✅ Logged to "Future Follow-Up"

### Test 4: Recurring Scheduler

After setting everything up:

1. Manually add a row to "Qualified Leads" with Call Stage = "Discovery Call Scheduled"
2. Wait for the next scheduled run (or manually trigger Module 10)
3. **Expected:** Follow-up email sent to that lead, stage updated to "Follow-Up Sent", Slack notification sent

### Test 5: Webhook Integration

To connect to your actual website form:

1. Get the webhook URL from Module 1 (after first save)
2. In your form backend, POST JSON to that URL
3. Ensure the field names match: `name`, `email`, `company`, `service_interest`, `budget`, `message`, `phone`, `referral_source`, `timeline`, `heard_about`
4. Test submitting through your actual form

---

## Troubleshooting

### Common Issues

| Symptom | Likely Cause | Solution |
|---|---|---|
| Module 2 fails with "400 Bad Request" | Invalid or missing OpenAI API key | Check your OpenAI connection in Make.com; verify the key is active and has GPT-4o access |
| Module 2 fails with "429 Too Many Requests" | Rate limited by OpenAI | Add a sleep/wait module before Module 2, or upgrade your OpenAI plan |
| Module 4 fails with "Calendar not found" | Google Calendar connection not authorized | Re-authorize the Google Calendar connection with proper scopes |
| Module 4 creates event but no Google Meet link | Google Calendar API limitations for some account types | Check that your Google account supports Google Meet creation via API (Workspace accounts or personal with Meet enabled) |
| Module 5/8 fails with "Gmail not sent" | Gmail connection issue or sending limits | Verify Gmail connection; check if you've hit Gmail's daily sending limit (500/day for personal, 2000/day for Workspace) |
| Module 6/9/11/14 fails with "Sheet not found" | Wrong spreadsheet ID or sheet name | Double-check the spreadsheet ID and ensure sheet names match exactly ("Qualified Leads" and "Future Follow-Up") |
| Module 7/15 sends message but Slack says "not_in_channel" | Bot not invited to the channel | Invite the Make.com Slack app to `#lead-alerts` with `/invite @make` |
| Router always takes the same path | Router condition misconfigured | Check that `firstValue` is `{{2.data.qualified}}` (not `{{2.qualified}}`) and operator is `eq` |
| AI returns poor quality analysis | System prompt needs tuning | Edit the GPT-4o system prompt to better describe your agency's services and ideal client profile |
| Scheduler doesn't run at expected time | Timezone mismatch | Check Module 10's timezone setting; defaults to America/New_York |
| Follow-up emails not sending | Module 11 search returning no results | Verify that existing leads have Call Stage = "Discovery Call Scheduled" exactly (case-sensitive) |
| Webhook returns 404 | Scenario not activated | Toggle scenario to ON; webhook only works when scenario is active |
| HTML email looks broken | CSS not supported in some email clients | Test with Litmus or Email on Acid; strip any unsupported CSS properties |

### Debugging Tips

1. **Use Make.com's built-in debugger:** Click a module → "Run this module only" to test with custom data
2. **Add a Text Parser or JSON module** between Module 2 and 3 to inspect the exact GPT-4o output
3. **Check module logs:** Each module has a log tab showing input/output data
4. **Test with the "Run once" button** before activating the scheduler
5. **Set up error handlers:** Right-click a module → Add error handler → Send error to a Slack channel or email
6. **Use the History tab** to see detailed execution traces for all runs

### Error Handler Recommendations

Add error handler routes to each module that notifies your team:

1. Create a Slack module with a "New Qualified Lead Failed" template
2. Connect each module's error handler to this Slack module
3. Include the error message and module name in the notification

### API Rate Limits

| Service | Limit | Mitigation |
|---|---|---|
| OpenAI GPT-4o | Varies by tier (typically 500–10,000 RPM) | Add 1-second delay between webhook and HTTP request if high volume |
| Gmail | 500/day (personal), 2000/day (Workspace) | Queue or spreadsheet-based sending for high volume |
| Google Calendar | 1M queries/day | Fine for agency use |
| Google Sheets | 60 requests/60s per user | Iterator with delay if processing many leads |
| Slack | 1 message/sec per channel | Fine for agency volume |

---

## Customization Ideas

### For Different Industries

- **Real Estate:** Change service categories to "Property Listings", "Virtual Tours", "Lead Generation"; add MLS integration
- **SaaS:** Add product demo scheduling instead of discovery call; integrate with Stripe for billing discussions
- **Consulting:** Change to 60-min strategy sessions; add Calendly instead of fixed time
- **E-commerce:** Add product catalog matching; integrate with Shopify/Magento
- **Healthcare:** Add HIPAA compliance notes; change to secure patient intake

### For Different Price Points

- **$47 "Lite" version:** Remove Slack notifications, simplify email templates, remove recurring scheduler
- **$197 "Pro" version:** Add SMS via Twilio, add CRM integration (HubSpot), add multi-language AI prompt, add PDF proposal generation, add A/B testing for email templates
- **$297 "Enterprise" version:** Add white-labeling, multi-workspace support, analytics dashboard, custom AI training on past inquiries, priority support channel

### Branding Your Webhook URL

If you have a custom domain, set up a redirect:
```
https://concierge.your-agency.com/webhook → https://hook.make.com/ai-concierge-inbound-v1
```

---

## Support

- **Documentation:** [Make.com Help Center](https://www.make.com/en/help)
- **OpenAI API Docs:** [platform.openai.com/docs](https://platform.openai.com/docs)
- **Purchase & Support:** [Gumroad Product Page](https://buy.stripe.com/test_dRm5kwf6e347dVq0LV9Zm06)

---

## License

This blueprint is licensed for use by the purchaser only. Redistribution or resale is prohibited. You may customize it for your own agency or client projects.

---

*Built with ❤️ for agency owners who want to respond faster, qualify better, and never lose a lead again.*
