# Meeting-to-Action Tracker — Make.com Setup Guide

Automate post-meeting follow-ups: submit a recording → AI extracts decisions & action items → Google Sheet is populated → each attendee gets a personalized email → organizer gets a full summary → a dedicated Slack channel is created.

---

## 1. Overview

The **Meeting-to-Action Tracker** workflow eliminates the manual scramble after every meeting. It consumes a meeting recording or transcript via webhook, runs it through OpenAI Whisper (speech-to-text) and GPT (structured extraction), then distributes the output across email, Google Sheets, and Slack — all in one automated scenario.

**Flow:**

```
Webhook → Whisper Transcription → GPT Extraction → Google Sheets → Personalized Emails → Organizer Summary → Slack Channel
```

| Step | What happens |
|------|--------------|
| 1 — Webhook | Receives meeting metadata + a public audio URL or pre-written transcript |
| 2 — Whisper | Transcribes audio to text via OpenAI Whisper API |
| 3 — GPT-4 | Extracts decisions, action items, owners, deadlines as structured JSON |
| 4 — Google Sheets | Logs all extracted data in a shared tracker |
| 5 — Gmail | Sends each attendee a personalised email with their action items |
| 6 — Gmail | Sends the meeting organizer a full summary + action table |
| 7 — Slack | Creates a private channel for the meeting's action items |

---

## 2. Prerequisites

Before importing the blueprint, make sure you have:

| Service | What you need | How to get it |
|---------|---------------|---------------|
| **Make.com account** | A paid plan (Free plan works but limits operations) | [make.com](https://www.make.com) — sign up |
| **OpenAI API key** | Billing-enabled OpenAI account | [platform.openai.com/api-keys](https://platform.openai.com/api-keys) |
| **Google account** | For Gmail + Google Sheets | Standard Google account |
| **Slack workspace** | Admin or permission to create channels | Your team's Slack |
| **Audio file** | Publicly accessible URL (.mp3, .m4a, .wav, .mp4, etc.) | Upload to cloud storage (Google Drive, Dropbox, S3) and generate a shareable link |

### Cost Estimates

| Service | Approximate cost per run |
|---------|--------------------------|
| OpenAI Whisper | $0.006 / minute of audio |
| OpenAI GPT-4 | $0.03–$0.06 per meeting transcript |
| Make.com operations | Uses ~7–10 operations per run |

**Typical cost per meeting:** ~$0.10–$0.15

---

## 3. Importing the Blueprint

1. Log into **Make.com** and go to your dashboard.
2. Click **Create a new scenario** (or **Scenarios → Add new scenario**).
3. Click the **three dots (⁝)** menu in the bottom-left corner of the scenario editor → **Import Blueprint**.
4. Select the file `deployed-blueprint.json` from this product package.
5. The scenario will be laid out with all 7 modules pre-connected.

![Import Bluepoint location in Make.com](https://public.make.com/help/assets/import-blueprint.png)
*If the image doesn't load: the menu is in the bottom-left gear/dots area of the scenario editor.*

---

## 4. Module-by-Module Configuration

### 4.1 Module 1 — Webhook (Trigger)

- **Module:** `Webhooks → Custom Webhook`
- **What it does:** Generates a URL you can POST meeting data to.

**Steps:**

1. Click the module. In the **Webhook** field, click **Add** to create a new webhook.
2. A dialog appears — click **OK** to generate a unique webhook URL.
3. Copy the URL (e.g., `https://hook.make.com/abc123xyz`).
4. This is where your app/script will POST meeting payloads (see §6 Testing).

**Expected incoming payload structure:**

```json
{
  "meetingTitle": "Sprint Planning — Week 42",
  "meetingDate": "2026-07-20",
  "audioUrl": "https://storage.example.com/meeting-recording.mp3",
  "organizerEmail": "alice@company.com",
  "organizerName": "Alice Johnson",
  "attendees": [
    { "name": "Bob Smith",    "email": "bob@company.com" },
    { "name": "Carol Davis",  "email": "carol@company.com" },
    { "name": "Dave Wilson",  "email": "dave@company.com" }
  ]
}
```

> **Note:** If your meetings don't have an audio recording, you can pass a `"transcript"` field instead of `"audioUrl"` and skip/simplify Module 2.

---

### 4.2 Module 2 — HTTP: Whisper Transcription

- **Module:** `HTTP → Make a Request`
- **What it does:** Downloads the audio from `audioUrl` and sends it to OpenAI Whisper for transcription.

**Steps:**

1. Click the module. Go to the **URL** field.
2. It will already show `https://api.openai.com/v1/audio/transcriptions`.
3. **Authentication:** You need to add your OpenAI API key.
   - Click the **Add a connection** button (or find it under the Advanced settings).
   - Choose **API Key** as the type.
   - Paste your OpenAI key in the **API Key** field.
   - Name the connection (e.g., "OpenAI API").
4. Ensure the **Method** is `POST` and **Body type** is `Form data`.
5. The **File** field in the form data uses `{{1.audioUrl}}` — make sure your webhook provides a publicly accessible URL.

**Troubleshooting:**
- If you get a `401 Unauthorized` error, double-check your API key.
- Audio files larger than 25MB need to be split or use Whisper's larger file support via URL. Files up to ~1GB are supported when passed as a URL reference.

---

### 4.3 Module 3 — HTTP: GPT Extraction

- **Module:** `HTTP → Make a Request`
- **What it does:** Sends the transcribed text to OpenAI GPT-4 with a system prompt that extracts structured data.

**Steps:**

1. Click the module. The URL is pre-set to `https://api.openai.com/v1/chat/completions`.
2. **Connection:** Use the same OpenAI connection created in Module 2 (or add a new one — they're interchangeable).
3. The **Body** already contains the system prompt and user message template.
4. **IMPORTANT:** Verify the user message template references the transcript correctly:
   - If you have Module 2 active: `{{2.text}}` — the Whisper response stores the transcript in `text`.
   - If you skipped Whisper and passed a transcript directly: change `{{2.text}}` to `{{1.transcript}}`.

**Expected GPT output shape:**

```json
{
  "meetingSummary": "The team reviewed Q3 roadmap priorities...",
  "decisions": [
    {"decision": "Adopt Next.js 15 for new frontend", "madeBy": "Team consensus"}
  ],
  "actionItems": [
    {
      "actionItem": "Draft migration plan",
      "owner": "Bob Smith",
      "deadline": "2026-07-27",
      "priority": "High"
    }
  ],
  "keyDiscussionPoints": [
    "Discussed deprecating legacy API endpoints"
  ]
}
```

---

### 4.4 Module 4 — Google Sheets: Add Row

- **Module:** `Google Sheets → Add a Row`
- **What it does:** Appends a new row with all the extracted data to your shared tracker.

**Steps:**

1. Click the module. Click **Add** next to the **Connection** field.
2. Follow the OAuth flow to connect your Google account.
3. **Spreadsheet ID:** Enter the ID of your target Google Sheet.
   - To find it: open your sheet → the URL looks like `https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit`
   - Copy the `SPREADSHEET_ID` portion.
4. **Sheet Name:** Enter the exact tab name (default: `Action Items` — create this sheet if it doesn't exist).

**Suggested sheet columns (create them in row 1):**

| A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|
| Meeting Title | Meeting Date | Summary | Decisions | Action Items | Key Points | Timestamp | Organizer |
| Sprint Planning | 2026-07-20 | The team reviewed... | [{"decision":...}] | [{"actionItem":...}] | ["Discussed..."] | 2026-07-20T14:30Z | alice@... |

> **Tip:** The JSON columns (Decisions, Action Items, Key Points) store the raw JSON so you can build dashboards or filters later. For a cleaner view, create additional columns and use spreadsheet formulas like `=INDEX(JSON_PARSE(E2), 1, "actionItem")` if your spreadsheet tool supports it.

---

### 4.5 Module 5 — Gmail: Personalized Attendee Emails

- **Module:** `Gmail → Send an Email`
- **What it does:** Sends each attendee a personalised email listing their action items.

**IMPORTANT — Iteration setup:**

This module must run **once per attendee**. In Make.com, you need a **Repeater** or **Iterator** module before this one. Since the blueprint uses exactly 7 modules, you have two options:

**Option A (Recommended) — Add an Iterator module:**

1. Right-click the connection line between Module 4 and Module 5 → **Add a module**.
2. Choose **Flow Control → Iterator**.
3. In the Iterator's **Array** field, enter `{{1.attendees}}`.
4. The Iterator will loop through each attendee and Module 5 will run for each one.

**Option B — Use the webhook array directly (only works if Make iterates automatically):**

- If each webhook payload only contains **one** attendee (i.e., you POST once per person), this module works out of the box.
- Not recommended for most teams — use Option A.

**Module configuration:**

1. Click the module → **Connection** → add your Gmail account via OAuth.
2. **To:** `{{item.email}}` (from the Iterator — will become `{{1.attendees[].email}}` if you use array notation).
3. **Subject:** Pre-filled with the meeting title reference.
4. **Body type:** `HTML`.
5. The **HTML body** is pre-written with a template that renders each attendee's action items.

> **Important:** The HTML template references `{{item.actions}}`. This assumes your webhook payload includes an `actions` array per attendee, OR you configure Module 3's GPT prompt to per-attendee action items. For simplicity, the current GPT prompt extracts **all** action items globally. Adjust either:
> - The GPT prompt to return per-attendee items, or
> - The email template to show all action items and filter by owner using `{{#each 3.choices[0].message.content.parsed.actionItems}} {{#if (eq this.owner item.name)}}...{{/if}} {{/each}}`.

---

### 4.6 Module 6 — Gmail: Organizer Summary

- **Module:** `Gmail → Send an Email`
- **What it does:** Sends a comprehensive meeting summary with all action items in a table layout.

**Steps:**

1. Click the module.
2. **Connection:** Should already be configured from Module 5 — if not, add the same Gmail account.
3. **To:** Pre-filled as `{{1.organizerEmail}}` — verify this is provided in the webhook payload.
4. **Subject:** Pre-filled.
5. The **HTML body** includes a formatted table of all action items, decisions, and discussion points.

No additional configuration needed — this module is ready to run once Module 5 is configured.

---

### 4.7 Module 7 — Slack: Create Channel

- **Module:** `Slack → Create a Channel`
- **What it does:** Creates a private Slack channel named after the meeting and posts the action items as the channel's purpose / initial message.

**Steps:**

1. Click the module → **Connection** → click **Add**.
2. Follow the OAuth flow to connect your Slack workspace.
   - The bot needs these scopes: `channels:manage`, `chat:write`, `groups:write`.
3. **Name:** Uses `{{slugify 1.meetingTitle}}` to create a URL-safe channel name (e.g., `meeting-actions-sprint-planning-week-42`).
   - Slack channel names must be lowercase, no spaces, max 80 characters.
4. **Is Private:** Set to `true` (recommended) or `false` for a public channel.
5. **Initial Message:** Pre-filled with a summary of action items and decisions.

**Limitations:**
- Free Slack plans are limited to 10,000 messages and may have channel creation caps.
- If a channel with the same name exists, the module will error — consider adding a **Slack → List Channels** filter before this module, or append a timestamp to the channel name.

---

## 5. Connections Summary

You'll need to set up **4 connections** in Make.com:

| Connection | Type | Used by Modules |
|------------|------|----------------|
| OpenAI API | API Key | 2, 3 |
| Google Sheets | OAuth | 4 |
| Gmail | OAuth | 5, 6 |
| Slack | OAuth | 7 |

To manage connections in Make.com:
- Go to **Settings → Connections** (or click the connection field in any module and select "Add a connection").
- Each connection stores credentials securely — you only need to set them up once.

---

## 6. Testing Instructions

### 6.1 Dry Run (without real services)

1. **Disable** Modules 2–7 by right-clicking each and selecting **Disable module**.
2. **Run Module 1 only:** Click **Run once**, then switch to the webhook tab and click **OK** to wait for data.
3. Send a test payload using `curl` or any HTTP client:

```bash
curl -X POST "https://hook.make.com/YOUR_WEBHOOK_ID" \
  -H "Content-Type: application/json" \
  -d '{
    "meetingTitle": "Test: Standup 2026-07-20",
    "meetingDate": "2026-07-20",
    "audioUrl": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    "organizerEmail": "you@example.com",
    "organizerName": "Test User",
    "attendees": [
      {"name": "Alice", "email": "alice@example.com", "actions": [{"actionItem": "Review PR #42", "deadline": "2026-07-22", "priority": "High"}]},
      {"name": "Bob",   "email": "bob@example.com",   "actions": [{"actionItem": "Update docs",  "deadline": "2026-07-25", "priority": "Medium"}]}
    ]
  }'
```

4. Verify Module 1 captured the data correctly by inspecting the output bundle.

### 6.2 Full Integration Test

1. Enable all modules.
2. Click **Run once** → send the same cURL payload.
3. The scenario will execute each module in sequence.
4. **Watch for errors:**
   - A red dot on a module means it failed — click the module to see the error message.
   - Common errors: missing API keys, wrong spreadsheet ID, Slack scope issues.
5. **Verify outputs:**
   - **Google Sheets:** Check that a new row appeared.
   - **Gmail:** Check the organizer inbox and attendee inboxes (use test accounts!).
   - **Slack:** Check that a new private channel was created.

### 6.3 Sample Payload with Pre-Written Transcript

If you want to skip Whisper (to save cost or if you already have a transcript):

```json
{
  "meetingTitle": "Product Review — July 2026",
  "meetingDate": "2026-07-20",
  "transcript": "Alice: Let's discuss the Q3 roadmap. Bob, what's the status on the migration? Bob: We've completed 60% of the backend migration. The API gateway is done. Carol: I've identified three critical bugs that need fixing before launch. Decision: We will push the launch date by two weeks. Alice: Bob, please draft the migration report by Friday. Carol, file bug reports by Wednesday.",
  "organizerEmail": "alice@company.com",
  "organizerName": "Alice",
  "attendees": [
    {"name": "Bob Smith",   "email": "bob@company.com",   "actions": [{"actionItem": "Draft migration report", "deadline": "2026-08-01", "priority": "High"}]},
    {"name": "Carol Davis", "email": "carol@company.com", "actions": [{"actionItem": "File bug reports",     "deadline": "2026-07-30", "priority": "High"}]}
  ]
}
```

---

## 7. Troubleshooting

### 7.1 Module Errors

| Error | Likely Cause | Fix |
|-------|-------------|-----|
| `401 Unauthorized` (Module 2 or 3) | Invalid or missing OpenAI API key | Re-add the OpenAI connection with a valid key |
| `400 Bad Request — model not found` | Using a model you don't have access to | Change `model` to `gpt-3.5-turbo` or `gpt-4o-mini` |
| `Spreadsheet not found` | Wrong Spreadsheet ID | Copy the ID from the sheet URL (see §4.4) |
| `Scope missing` (Slack) | Slack token lacks `channels:manage` scope | Re-authenticate with the correct scopes |
| `Channel name already exists` | Slack channel name taken | Add a timestamp to the name: `{{slugify 1.meetingTitle}}-{{now format="YYYYMMDDHHmmss"}}` |
| Module timeout | Audio file too large or network slow | Reduce audio length or use a pre-written transcript |

### 7.2 Data Issues

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| GPT returns incomplete JSON | Audio too long (token limit exceeded) | Split audio into segments or use `gpt-4-32k` |
| Email shows empty fields | Wrong variable path in mapper | Check `{{3.choices[0].message.content}}` — use Make's mapping panel (drag & drop from the previous module) |
| Attendees don't receive email | Iterator not configured | Add a flow control Iterator as described in §4.5 |
| Sheet row has `[object Object]` | Array/object not serialized | Use `{{JSONstringify 3.choices[0].message.content.parsed.actionItems}}` |

### 7.3 Webhook Not Firing

1. Make sure the webhook URL is correct (no trailing spaces).
2. Check that the webhook is **saved** (click the webhook module → Webhook field → the webhook must show as "defined").
3. Test with a simple GET to the webhook URL — you should see a pending state.
4. If using HTTPS, ensure your client supports TLS 1.2+.

### 7.4 Slack Channel Not Created

1. Verify the bot has `channels:manage` and `groups:write` scopes.
2. Check that the channel name is valid (lowercase, no special characters except hyphens).
3. On free Slack plans, you may hit channel creation limits — archive old channels or use a Slack **Send a Message** module instead.

---

## 8. Customization Ideas

- **Add a Slack bot to post follow-up reminders**: Use a **Schedule** trigger to check deadlines and remind owners 24h before due dates.
- **Integrate with Notion / Airtable**: Replace the Google Sheets module with your preferred database.
- **Add a "Retry on Failure" handler**: Wrap Modules 2 and 3 with a **Flow Control → Repeater** (max 3 repeats).
- **Store transcripts for auditing**: Add a **Google Drive → Upload a File** module to save the raw transcript.
- **Multi-language support**: Change Whisper's `language` parameter or remove it for auto-detection.

---

## 9. Support

If you encounter issues beyond what's covered here:

1. Check the **Make.com scenario history** — click the clock icon on your scenario to see execution logs.
2. Review **OpenAI API status** at [status.openai.com](https://status.openai.com).
3. For Make.com specific errors, consult [Make.com Help Center](https://www.make.com/en/help).

---

*Version 1.0 — Meeting-to-Action Tracker by Gumroad Product*
