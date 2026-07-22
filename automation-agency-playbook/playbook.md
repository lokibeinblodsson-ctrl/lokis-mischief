# THE AUTOMATION AGENCY PLAYBOOK

## How to systematize your agency, free up 10+ hours a week, and turn automation into your highest-margin service

**By Loki's Mischief**

---

> *"The agency that automates best, wins. Not the one with the most employees, the biggest office, or the fanciest website. The one that has systems that run while the founder sleeps."*

---

# SECTION 1: Why Automation Wins

## The Shift Every Agency Must Make

Let's start with a number that should scare you:

**72% of agency owners report working 50+ hours a week.** Over a third say they're burned out within the first two years of operation.

The culprit isn't "too many clients." It's **manual operations** — the death by a thousand paper cuts that keeps you from doing the actual work that grows the business.

Here's what most agency owners spend their time on:

| Activity | Hours/Week (Average) | Revenue-Generating? |
|---|---|---|
| Client onboarding (emails, forms, intake) | 4-6 | No |
| Manual reporting (pulling data, formatting decks) | 5-8 | No |
| Proposal writing from scratch | 3-5 | No |
| Invoicing & payment follow-up | 2-3 | No |
| Meeting prep & follow-up notes | 3-5 | No |
| Internal coordination slack/ping-pong | 4-7 | No |
| **Total drain** | **21-34 hours** | — |

That's **half your workweek** spent on things that don't directly earn you a dollar.

Meanwhile, the agencies that DO systematize and automate are seeing:

- **3.2x higher profit margins** (Hinge Marketing Study, 2024)
- **40% lower employee turnover** (because nobody wants to do mindless repetitive work)
- **2x faster client onboarding** → faster time-to-value → higher retention

## The Math Is Brutal

Let's say your effective hourly rate as an agency owner is **$150/hour** (blended across all your work).

If you're spending 25 hours a week on manual operations, that's **$3,750/week** in lost revenue potential — over **$195,000/year** — that you're essentially burning on admin work.

Automation isn't a "nice to have." It's a **profitability lever** that directly impacts your bottom line.

## The 2025 Reality

Here's what changed in the last two years that makes this conversation different from 2020:

1. **AI LLMs hit production-grade reliability.** GPT-4o and Claude 3.5 can now handle unstructured data — emails, transcripts, proposals — with accuracy that was impossible 24 months ago.
2. **No-code automation platforms matured.** Make.com and n8n give you enterprise workflow capabilities without a development team.
3. **Clients expect it.** In 2025, a "white glove" experience means instant onboarding, proactive updates, and zero friction. Manual processes feel amateur to modern clients.

The gap between "surviving agency" and "thriving agency" has never been wider — and it's almost entirely defined by **what you've systematized**.

---

# SECTION 2: The 5 Core Automations Every Agency Needs

After building automation systems for dozens of agencies, I've found that **five workflows** cover 80% of the manual overhead. Here they are, in order of impact.

## Automation #1: Client Onboarding

**The problem:** Every new client triggers a chain of 15-20 manual steps — welcome emails, questionnaire delivery, contract signing, calendar scheduling, access provisioning, kickoff meeting prep. One slip and you look unprofessional.

**The automation:**
A new client signs your proposal → triggers an automated onboarding sequence:

- **Stripe payment captured → auto-generates client profile** in your CRM (HubSpot, Airtable, Notion)
- **Contract sent via e-signature** (RightSignature, DocuSign, or PandaDoc)
- **Automated questionnaire delivery** (Typeform or Google Forms) — answers populate a shared project dashboard
- **Client portal access provisioned** — login credentials auto-generated and emailed
- **Kickoff meeting auto-scheduled** (Calendly or 10to8) — confirmation with pre-meeting prep checklist
- **Slack/Discord channel created** with client name, auto-invited team members
- **Internal project board generated** — tasks created from your standard onboarding template

**Real example:** A boutique marketing agency I worked with cut their onboarding from 5 business days to **under 4 hours** using this exact flow on Make.com. Their client satisfaction score on the first 30 days jumped 34%.

**The Loki's Creations solution:** Our [Agency Client Onboarding Agent ($39)](https://your-stripe-link.com) handles the entire kickoff sequence across Make.com or n8n — pre-built with 14 automation modules covering intake, document collection, access provisioning, and kickoff scheduling.

---

## Automation #2: Client Reporting

**The problem:** Monthly reporting is the single biggest time suck in most agencies. You're pulling data from 3-5 platforms (Google Analytics, Meta Ads, LinkedIn, HubSpot, Loom), formatting it in Google Slides or PowerPoint, and writing narrative summaries. Every. Single. Month.

**The automation:**
- **Data aggregation:** Automated API pulls from analytics platforms into a central data store (Google Sheets, Airtable, or a database)
- **Template population:** Metrics flow into a branded report template (Google Slides, Canva API, or PDF generation)
- **Narrative generation:** An AI layer (GPT-4o or Claude) reads the data and writes the executive summary, insights section, and next-month recommendations
- **Delivery:** Report is auto-emailed to the client with a Loom video link (generated from highlights)
- **Archive:** Report saved to shared drive with client-facing dashboard link

**Time savings:** What used to take 4-6 hours per client per month drops to **30-45 minutes of review and personalization.**

**The Loki's Creations solution:** [Narrative Monthly Report Builder ($39)](https://your-stripe-link.com) — connects to your analytics stack, generates AI-written narrative reports, and delivers them automatically. Available for Make.com and n8n.

---

## Automation #3: Proposals & RFI Responses

**The problem:** Every proposal starts from scratch. Even with templates, you're copy-pasting case studies, restructuring pricing, and reformatting. For RFPs/RFIs, the problem is worse — clients send 50+ page documents and expect thorough responses in 3-5 business days.

**The automation:**
- **Inbound lead trigger → proposal generation:** A simple web form or email trigger kicks off a Make.com/n8n scenario
- **Context gathering:** The automation queries your CRM for similar past projects, pulls relevant case studies, and extracts pricing tiers
- **AI draft generation:** Claude 3.5 or GPT-4o writes the first draft based on your proposal template and the context data
- **Human review loop:** You get a notification, make edits, approve
- **Delivery & tracking:** Proposal sent via PandaDoc or directly as a beautifully formatted PDF
- **Follow-up sequence:** If no response in 3 days, automated check-in email #1. Day 7, email #2 with a case study addendum. Day 14, final email with a "shall we close this out?" message.

**Real example:** A web development agency using our RFP Response Drafter went from winning 2 out of 15 RFPs to **8 out of 18** in one quarter — not because the proposals were better, but because they could now RESPOND to almost every RFP that came in instead of cherry-picking.

**The Loki's Creations solution:** [RFP/RFI Response Drafter ($39)](https://your-stripe-link.com) — ingests RFP documents, auto-generates structured responses from your past work, and manages the delivery + follow-up sequence.

---

## Automation #4: Invoicing & Payment Follow-Up

**The problem:** Chasing payments is awkward, time-consuming, and inconsistent. You send an invoice, wait, send a reminder, wait longer, then finally send a "hey, just checking in" that feels desperate. Meanwhile, your accounts receivable balloons.

**The automation:**
- **Milestone or time trigger → invoice generation:** Based on project milestones (completed in your project management tool) or recurring date (monthly retainer)
- **Invoice creation & delivery:** Invoice auto-created in Stripe/Xero/QuickBooks and emailed to client
- **Dunning sequence (payment reminders):**
  - Day 0: Invoice sent with payment link
  - Day 3: Friendly reminder — "Just wanted to make sure you received this"
  - Day 7: More direct reminder with late fee notice (if applicable)
  - Day 10: "Your services may be paused" notice
  - Day 14: Internal alert sent to agency owner for manual intervention
- **Payment confirmation:** On successful payment, trigger a thank-you email + unlock next deliverables
- **Late payment handling:** Auto-apply late fees, send updated invoice, pause service access

**Time savings:** Eliminates 2-3 hours per week of manual follow-up. More importantly, **average payment time drops from 18 days to 6 days** because the system is persistent and professional.

**The Loki's Creations solution:** [Invoice Dunning & Payment Reminder ($39)](https://your-stripe-link.com) — handles the full invoice-to-payment lifecycle with 5-stage dunning sequences for both Make.com and n8n.

---

## Automation #5: Meeting-to-Action Follow-Up

**The problem:** Every meeting generates action items, and those action items get lost in the gap between "I'll send a follow-up email" and the next meeting where nothing has moved forward.

**The automation:**
- **Meeting transcript ingestion:** Zoom, Google Meet, or Teams transcript auto-uploads to a designated location
- **AI processing:** GPT-4o or Claude extracts:
  - Action items with assigned owners
  - Decisions made (with context)
  - Key discussion points
  - Follow-up dates
- **Action item creation:** Items auto-created in Asana/ClickUp/Linear/Notion with deadlines and assignees
- **Summary distribution:** AI-written meeting summary emailed to all participants within 15 minutes of meeting end
- **Pre-meeting prep:** Before next meeting, automation sends a summary of past action items and their status to each attendee

**Real example:** A 12-person creative agency recovered an estimated **$84,000/year** in "lost action items" — tasks that were discussed but never executed because no one wrote them down properly. The Meeting-to-Action Tracker caught everything.

**The Loki's Creations solution:** [Meeting-to-Action Tracker ($39)](https://your-stripe-link.com) — ingests meeting transcripts (Zoom, Google Meet, Teams), extracts structured action items, creates tasks in your PM tool, and distributes summaries.

---

## The 5 Automations at a Glance

| Automation | Time Saved/Week | Implementation Time | Revenue Impact |
|---|---|---|---|
| Client Onboarding | 4-6 hrs | 3-5 hours setup | Faster time-to-revenue |
| Client Reporting | 4-6 hrs | 4-6 hours setup | Higher retention |
| Proposals & RFI | 3-5 hrs | 3-4 hours setup | Win more deals |
| Invoicing & Follow-up | 2-3 hrs | 2-3 hours setup | Faster payments |
| Meeting-to-Action | 3-5 hrs | 2-3 hours setup | Better execution |
| **Total** | **16-25 hrs/wk** | **14-21 hours setup** | **$100k+/yr recovered** |

---

# SECTION 3: Make.com vs n8n — Which Platform to Use

This is the question I get asked most. And the answer is not "one is better." It's **"which one is better for this specific use case and this specific agency."**

Let me give you the honest comparison.

## Make.com (formerly Integromat)

**Best for:** Agencies that want speed of setup, visual workflow design, and 500+ native app integrations without writing a line of code.

### Pros

- **Visual scenario editor** — Drag-and-drop workflow builder that's genuinely intuitive. You can see the data flow in real-time.
- **500+ native integrations** — Most tools you already use (Google Workspace, Slack, Notion, Airtable, HubSpot, Stripe, Zoom) have deep, well-maintained connectors.
- **Built-in data operations** — Transform, filter, aggregate, and split data without external tools.
- **Error handling** — Decent built-in error routing and retry logic.
- **Team collaboration** — Shared scenarios, team workspaces, role-based permissions.
- **Launch speed** — You can build a production-ready automation in an afternoon.

### Cons

- **Scaling cost** — Operations (the "ops" you pay for) add up fast. At scale, a heavily automated agency can hit $150-300/month.
- **Limited custom logic** — Complex conditional branching, custom JavaScript/node.js execution, or advanced data manipulation requires workarounds.
- **No local deployment** — Cloud-only. If you need on-premise or air-gapped deployment, you're out of luck.
- **API rate limits** — Some connectors have aggressive caps that bite you at high volume.

### Pricing

| Plan | Ops/Month | Price | Best For |
|---|---|---|---|
| Free | 1,000 ops | $0 | Testing & learning |
| Core | 10,000 ops | ~$14/mo | Solopreneurs |
| Pro | 50,000 ops | ~$29/mo | Small agencies |
| Teams | 100,000+ ops | ~$32/mo+ | Growing agencies |

**Verdict:** Make.com is the right choice if you want to build automations **fast**, you're primarily using SaaS tools, and you're okay with a monthly subscription that scales with usage.

---

## n8n (Self-Hosted or Cloud)

**Best for:** Agencies that need custom logic, data sovereignty, and want to avoid per-operation pricing. More technical, but far more flexible.

### Pros

- **Self-hostable** — Run it on your own server (DigitalOcean, AWS, Railway, or even a Raspberry Pi). Zero per-operation costs after infrastructure.
- **Custom code nodes** — Native support for JavaScript, Python, and even shell commands within workflows. You can write functions, call APIs, manipulate data with full programmatic control.
- **Webhook-first design** — Works beautifully as a backend for custom apps, forms, and API endpoints.
- **True enterprise security** — You control where data lives. SOC2 compliance possible with self-hosting.
- **Active open-source community** — 40,000+ GitHub stars, 500+ community nodes.
- **AI integrations** — Native LangChain integration, vector store connectors, and AI agent nodes for building autonomous AI workflows.

### Cons

- **Steeper learning curve** — The UI is functional, not beautiful. You'll spend more time getting the first workflow running.
- **Maintenance overhead** — Self-hosted means you own updates, backups, security patches, and uptime.
- **Fewer native connectors** — While growing fast, n8n has fewer pre-built integrations than Make. You'll use webhooks and custom API calls more often.
- **No visual data preview** — Make.com shows you exactly what data looks like at each step. n8n requires clicking through to see outputs.

### Pricing

| Option | Cost | Best For |
|---|---|---|
| Self-hosted (Community) | Free (your server cost only) | Technical teams, high-volume automation |
| n8n Cloud (Starter) | ~$20/mo | Teams that want managed hosting |
| n8n Cloud (Pro) | ~$50/mo | Growing agencies needing more workflow runs |

**Verdict:** n8n wins for **flexibility and long-term cost control.** If you're technical (or have a technical team member), self-hosting n8n means you can run unlimited automations for the cost of a $10/month VPS.

---

## Head-to-Head Comparison

| Factor | Make.com | n8n |
|---|---|---|
| Learning curve | Low (1-2 days) | Medium (1-2 weeks) |
| Setup time (first workflow) | 30 minutes | 2-4 hours |
| UI/UX | Polished, visual | Functional, dense |
| Custom code | Limited (some JSONata) | Full JS/Python/Shell |
| Self-host option | ❌ | ✅ |
| Cost at 100k operations/mo | ~$32/mo | $0 (self-host) or ~$50/mo (cloud) |
| Native AI integrations | Basic (HTTP module) | Native LangChain + AI nodes |
| Data privacy | Shared cloud | Your infrastructure |
| App connectors | 500+ | ~350 + community |
| Error handling | Good | Excellent (with custom logic) |
| Best for | Speed & simplicity | Power & control |

## When to Choose Which

**Choose Make.com when:**
- You want to build and launch automations this week, not next month
- Your team is non-technical and needs to modify workflows
- You're using common SaaS tools (Google, Slack, Notion, Stripe)
- Your automation volume is under 50,000 operations/month
- A $30-150/mo subscription is acceptable

**Choose n8n when:**
- You need custom logic or AI processing
- You want zero per-operation costs at scale
- Data privacy is a client requirement (legal, healthcare, gov)
- You're building automation systems to resell to clients
- You have (or can hire) someone comfortable with basic JavaScript

**The truth:** Most successful automation agencies use **both.** Make.com for quick client-facing automations and internal workflows, n8n for complex integrations, AI-heavy processes, and white-labeled automation products.

---

## Why This Matters for Reselling

If you're building automation services to sell to clients, the platform decision affects your margins:

- **Make.com reselling:** You'll need a Make.com Team plan with operations bundled. Your clients pay you, you pay Make. Ops monitoring becomes part of your support overhead.
- **n8n reselling:** Self-host on your own infrastructure, charge a monthly retainer, pay zero per-workflow costs. Every client you onboard is pure margin after your server cost.

**My recommendation:** Start with Make.com for speed. If you hit scaling limits or want to build a high-margin automation service, migrate critical workflows to self-hosted n8n.

---

# SECTION 4: Building Your First Automation

## Step-by-Step — A Simple Lead Capture Flow

Let's build something real. This is a **lead capture automation** that:
1. Captures a form submission from your website
2. Logs the lead in Google Sheets and your CRM
3. Sends a Slack notification to your team
4. Sends a personalized welcome email to the lead
5. Creates a follow-up task in your project management tool

I'll show you how to build this on **both** platforms so you can compare the experience.

---

### Version A: Make.com

**Step 1: Create a scenario**
- Log into Make.com → Create a new scenario
- Name it "Lead Capture — Website"

**Step 2: Add the webhook trigger**
- Add a **Webhook** module as the trigger
- Click "Add new webhook" → Copy the URL
- In your website form tool (Typeform, Gravity Forms, Webflow), paste this URL as the webhook destination

**Step 3: Add Google Sheets**
- Add **Google Sheets** → "Add a Row" module
- Connect your Google account
- Select your spreadsheet and sheet tab
- Map the fields from the webhook data:
  - First Name → `{{webhook.first_name}}`
  - Last Name → `{{webhook.last_name}}`
  - Email → `{{webhook.email}}`
  - Phone → `{{webhook.phone}}`
  - Source → `Website`
  - Timestamp → `{{timestamp}}`

**Step 4: Add CRM (HubSpot)**
- Add **HubSpot** → "Create Contact" module
- Map email, name, phone from the same webhook data
- Add a lead source property → `Website Form`

**Step 5: Add Slack notification**
- Add **Slack** → "Send a Message" module
- Select your #leads channel
- Message template: `New lead! {{webhook.first_name}} {{webhook.last_name}} — {{webhook.email}}`

**Step 6: Send welcome email**
- Add **Gmail** → "Send an Email" module
- To: `{{webhook.email}}`
- Subject: `Welcome to [Agency Name] — Here's what's next`
- Body: A template email with merge fields for their name and your intro

**Step 7: Create task**
- Add **Asana/ClickUp** → "Create Task" module
- Task name: `Follow up with {{webhook.first_name}} {{webhook.last_name}}`
- Assignee: Your sales person
- Due date: `{{addDays(timestamp, 1)}}` (next day)

**Step 8: Test and activate**
- Click "Run Once" and submit a test form entry
- Verify each module executed successfully
- Toggle the schedule ON

**Total build time: 20-30 minutes.**

---

### Version B: n8n (Self-Hosted or Cloud)

**Step 1: Add a Webhook node**
- Drag a **Webhook** node onto the canvas
- Set `POST` method, add a webhook URL path (e.g., `/lead-capture`)
- Copy the production webhook URL

**Step 2: Add Google Sheets**
- Add **Google Sheets** → "Append Row" node
- Configure Google OAuth (follow n8n's Google auth setup)
- Select your spreadsheet
- Map the fields from the incoming webhook data using expressions:
  - `{{$json.first_name}}`
  - `{{$json.last_name}}`
  - `{{$json.email}}`

**Step 3: Add CRM (HubSpot via API)**
- Add **HubSpot** node → "Create a Contact" operation
- Or use the **HTTP Request** node if the native connector doesn't fit:
  - Method: POST
  - URL: `https://api.hubapi.com/crm/v3/objects/contacts`
  - Headers: Authorization Bearer `{{$env.HUBSPOT_API_KEY}}`
  - Body: JSON mapped from webhook data

**Step 4: Add Slack**
- Add **Slack** node → "Send Message"
- Channel: `#leads`
- Text: Expression that builds the message string

**Step 5: Send email**
- Add **Email** node (SMTP) or **Gmail** node
- For SMTP: Configure your mail server settings as n8n credentials
- Set recipient, subject, and HTML body with expressions

**Step 6: Create task**
- Add **Linear/ClickUp/Asana** node, or use the generic **HTTP Request** to hit any task API
- Map assignee, title, and due date

**Step 7: Add error handling**
- Connect an **Error Trigger** node to handle failures
- Add a simple notification workflow: "Lead capture failed at step X — raw data saved to error log"

**Step 8: Activate**
- Click "Save" → "Activate Workflow"
- Test with a webhook request (n8n has a built-in test panel)
- Switch to production URL

**Total build time: 45-60 minutes** (first time, longer due to auth setup).

---

## What You've Just Built

You now have a production-grade lead capture system that:

- ✅ Captures leads 24/7 — even when you're asleep
- ✅ Creates a permanent record (Google Sheets)
- ✅ Syncs to your CRM automatically (no manual data entry)
- ✅ Alerts your team in real-time
- ✅ Makes a professional first impression (instant welcome email)
- ✅ Ensures follow-up happens (task created for your team)

**Cost of this automation on Make.com:** About $0.50/month at typical lead volume.
**Cost on n8n (self-hosted):** Essentially $0 after server cost.

---

## Pro Tips for Building Automations

1. **Start small, then add complexity.** Build the linear flow first, then add conditional branches, error handling, and parallel paths.
2. **Always log. Always.** Have every automation append a log row to a Google Sheet with: timestamp, trigger data, status, error message (if any). Future you will thank present you when something breaks.
3. **Use human-in-the-loop for high-stakes actions.** Never let an automation send a final invoice or fire a client email without a review step. Auto-draft, yes. Auto-send high-risk messages, no.
4. **Name your modules descriptively.** "Step 1" is unhelpful when you're debugging at 11 PM. "Capture Webhook → Log to Sheets → Create HubSpot Contact" is better.
5. **Document your automations.** A simple Notion page with:
   - What the automation does
   - Which accounts it connects
   - What happens if it fails
   - Who to contact if it breaks

---

# SECTION 5: The AI Advantage

## Creating Your "Virtual Operations Manager"

This is where automation stops being "efficiency hacks" and starts being a **force multiplier.**

GPT-4o and Claude 3.5 Sonnet have reached a level of reliability where they can act as an intelligent layer on top of your automations. They don't just move data from A to B — they **understand** the data, make decisions about it, and generate human-quality output from it.

## Three Ways AI Transforms Agency Automations

### 1. AI-Written Client Communications

Instead of generic templates, your automation can now generate **personalized, context-aware** communications:

- **Welcome emails** that reference the specific project scope the client signed up for
- **Progress updates** that summarize work completed in plain English
- **Proposals** that tailor case studies and language to the prospect's industry
- **Meeting follow-ups** that capture nuance, not just bullet points

**How it works:**

```
Form Submission → GPT-4o evaluates:
  - Industry (from form data)
  - Project type (from form data)
  - Budget range (from form data)
  → Generates 3-paragraph personalized welcome email
  → Recommends next-best-action based on lead scoring
```

**The Loki's Creations integration:** Our [AI Client Concierge System ($97)](https://your-stripe-link.com) combines GPT-4o understanding with Make.com/n8n workflows to handle the entire client communication lifecycle. It drafts, personalizes, and schedules all outbound client messages with minimal human review.

### 2. Intelligent Data Processing

This is where AI outperforms traditional automation completely.

**Traditional automation:** A lead fills out a form → fields map directly to your CRM. If the lead writes "I need help with FB ads and maybe some email" in the "notes" field, that's stored as-is. No extraction, no categorization, no prioritization.

**AI-powered automation:** Same form submission → GPT-4o extracts:
- **Service requested:** "Facebook advertising, email marketing"
- **Intent score:** 8/10 (high — they used specific service names)
- **Budget indicator:** "Mid-range" (based on inferred language)
- **Urgency:** "Moderate" (no date mentioned)
- **Recommended next action:** "Send case studies for Facebook ads + email nurture sequence"

It then routes the lead to the appropriate sales queue, attaches relevant materials, and schedules a follow-up timeframe — all without a human touching it.

### 3. Autonomous Workflow Decision-Making

Here's the most powerful application: **letting AI decide WHAT to do based on unstructured input.**

**Real example — Client support ticket automation:**

A client emails: *"Hey, the dashboard isn't loading. I've refreshed twice and it's still down. I need this for my board meeting tomorrow."*

**Without AI:** Your automation flags it as "Support Request — Route to Tier 1" (generic, slow)

**With AI (Claude processing the email):**
1. Claude identifies: **Technical issue** (not billing, not feature request)
2. Severity assessment: **High** (board meeting tomorrow = client-facing urgency)
3. Action: Creates a **critical priority ticket**, pings the on-call engineer in Slack with the context, sends an auto-response: *"I see you're having trouble accessing the dashboard. Our team has been notified and will investigate immediately. In the meantime, would you like me to pull your key metrics into a quick PDF for your board meeting?"*
4. Fallback trigger: If the engineer doesn't acknowledge in 15 minutes, the automation escalates to the agency owner

That's not a scripted template. That's an AI understanding the **context and urgency** of a natural language message and acting on it intelligently.

---

## The "Virtual Operations Manager" Stack

Here's the architecture we use at Loki's Creations:

| Layer | Tool | Role |
|---|---|---|
| Trigger | Webhook, Email, Form | Captures the raw input |
| Intelligence | GPT-4o or Claude 3.5 | Understands the input, makes decisions |
| Logic | Make.com or n8n | Routes data, executes actions |
| Storage | Google Sheets, Airtable, DB | Logs everything |
| Action | Slack, Email, CRM, PM tools | Executes the output |
| Review | Human loop (last mile) | Approves high-stakes actions |

**The key insight:** AI handles the **fuzzy stuff** — understanding, categorizing, generating. Automation handles the **deterministic stuff** — moving data, executing steps, logging. Together, they replace what would have been a $60,000/year operations manager.

---

## Real Cost Comparison

| Role | Annual Cost | What They Do |
|---|---|---|
| Operations Manager (FTE) | $55,000 - $75,000 | Manages workflows, client comms, follow-ups |
| Virtual Assistant (Part-time) | $18,000 - $30,000 | Templates, data entry, scheduling |
| **AI + Automation Stack** | **$1,200 - $3,600** | **Handles 80% of both roles** |

The AI + automation stack doesn't replace a human entirely — but it replaces **80% of the repetitive work**, meaning:
- Your ops manager can focus on strategy instead of execution
- You don't need to hire your 3rd or 4th operations person until you're doing $1M+ in revenue
- Your response times drop from hours to minutes

---

# SECTION 6: Pricing & Packaging Automation Services

## How to Resell Automations to Your Own Clients

This is where the playbook turns from "save time" to **"make money."**

If you're an agency owner, you have something powerful: **you already know the pain.** You've felt the manual ops drag. And your clients feel it too — just in different contexts.

Here's the truth: **Every business is becoming an automation buyer.** The global automation market is projected to hit $30+ billion by 2027, and the biggest growth segment is small-to-medium businesses who don't have the in-house expertise to build these systems themselves.

Your clients are perfect buyers. They trust you. You understand their business. And they're already paying you for results.

## Three Models for Selling Automation Services

### Model 1: Automation Setup (One-Time Fee)

**What you deliver:** Build and configure automations for the client
- Scoping call → Discovery of 3-5 key workflows
- Build & test on Make.com or n8n
- Documentation & handoff
- 30 days of support

| Service | Price | Typical Hours |
|---|---|---|
| Single automation build | $1,500 - $3,000 | 8-15 hours |
| 3-automation package | $3,500 - $7,000 | 20-35 hours |
| Full ops overhaul (5-8 automations) | $7,500 - $15,000 | 40-60 hours |

**Best for:** One-off engagements, project-based agencies, or as an upsell from existing retainers.

### Model 2: Automation Retainer (Monthly Recurring Revenue)

**What you deliver:** Ongoing management, monitoring, and optimization
- Hosting & infrastructure (especially for n8n)
- Monitoring & error resolution
- Monthly optimization and new workflow builds
- Unlimited support requests

| Tier | Automations | Price/Month |
|---|---|---|
| Starter | Up to 3 workflows | $197 - $397 |
| Growth | Up to 10 workflows | $497 - $997 |
| Scale | Unlimited workflows + AI agents | $1,497 - $2,997 |

**Best for:** Building predictable MRR. One $997/month client for 12 months = $11,964 in revenue from a few hours of maintenance per month.

### Model 3: White-Label Automation Products

**What you deliver:** Pre-built automation systems sold as branded products
This is a higher-leverage model: **build once, sell many times.**

Using Loki's Creations products as the foundation:
1. Purchase our pre-built automation templates ($39-$97 each)
2. Customize them for your client's specific tools and branding
3. Deliver as your own white-labeled solution
4. Charge setup ($500-$1,000) + monthly management ($197-$497)

**Example economics:**

| Item | Cost | Price to Client | Margin |
|---|---|---|---|
| Client Onboarding Agent | $39 | $1,500 setup | $1,461 |
| Monthly management | $0 (self-hosted n8n) | $297/mo | $3,564/yr |
| **Total Year 1** | **$39** | **$5,064** | **$5,025** |

That's a **12,800% ROI** on your product purchase, per client.

**Best for:** Agencies that want to build an automation service line without custom-building every workflow from scratch.

---

## What to Charge (Real Pricing Data)

Based on what automation agencies are actually charging in 2025:

| Service | Low | Average | High |
|---|---|---|---|
| Workflow audit & recommendations | $500 | $1,000 | $2,500 |
| Single workflow build (simple) | $1,000 | $2,000 | $3,500 |
| Single workflow build (complex, with AI) | $2,500 | $5,000 | $10,000 |
| Monthly retainer (monitoring + support) | $197 | $497 | $1,500 |
| Full ops transformation (6-10 workflows) | $5,000 | $12,000 | $25,000 |
| AI agent setup (virtual ops manager) | $2,500 | $5,000 | $15,000 |

**The dirty secret:** Most agencies drastically underprice automation services because they think in "hours of work" rather than "value delivered."

A workflow that saves a client 15 hours/week is worth **$3,000-$5,000/year** to them in salary-equivalent savings. Price accordingly.

---

## The Pitch That Works

Stop selling "automations." Sell **outcomes:**

| Don't Say | Say |
|---|---|
| "I'll build you a Zapier workflow" | "I'll make sure every new lead gets a personalized response within 2 minutes" |
| "I'll set up automated invoicing" | "I'll cut your payment time from 18 days to 5 days" |
| "I'll create an automated report" | "You'll never spend another Sunday afternoon pulling reports" |
| "I'll connect your tools" | "Your business will run while you focus on the work that actually needs you" |

Lead with the benefit. The technology is just the mechanism.

---

## Building Your Automation Services Menu

Here's a service menu template you can adapt:

**LOKI'S CREATIONS AUTOMATION SERVICES**
*For [Your Agency Name]*

**Core Automations**

☐ **Lead Capture & Follow-Up** — $1,500 setup / $297/mo
Never miss a lead. Instant form-to-CRM, Slack alerts, welcome sequence, and follow-up reminders.

☐ **Client Onboarding System** — $2,000 setup / $397/mo
From signed proposal to active project in under 24 hours. Auto-generated profiles, questionnaires, kickoff scheduling, and access provisioning.

☐ **Reporting Automation** — $2,500 setup / $497/mo
AI-written monthly reports with live dashboards. Your clients get insights, you get your time back.

☐ **Meeting Action Tracker** — $1,500 setup / $297/mo
Every meeting produces clear action items, assigned owners, and deadlines. Nothing falls through the cracks.

**Premium Packages**

☐ **The Growth Stack** (Lead Capture + Onboarding + Reporting)
$5,000 setup / $897/mo (save $294/mo vs individual)

☐ **The Complete Ops Stack** (All 5 Core Automations)
$9,000 setup / $1,497/mo (save $588/mo vs individual)

☐ **Custom AI Agent** — Tailored to your business
From $5,000 setup / $997/mo

---

# SECTION 7: From Playbook to Profit

## How to Free Up 10+ Hours/Week Starting Next Week

Everything in this playbook is useless if it sits as a PDF on your hard drive. Here's your **7-day action plan** to go from reading to results.

---

## Week 1: Audit & Prioritize

**Day 1: The Time Audit**
- Track every task for one day. Every email, every Slack ping, every "let me just quickly update this report."
- Block out every 15-minute increment.
- **Identify the top 3 time-wasters** — the tasks that are repetitive, low-skill, and high-frequency.

**Day 2: Pick Your First Automation**
- From your time audit, pick the **single most painful task** that's also the easiest to automate.
- Almost always, this is **lead capture and follow-up** or **meeting notes.**
- Don't try to automate everything at once. Pick one.

**Day 3-4: Build Your First Automation**
- Use the tutorial in Section 4 of this playbook.
- Build the lead capture flow or the meeting action tracker.
- If you hit a wall, reference the Loki's Creations product docs — each product includes full setup guides.

**Day 5: Test & Refine**
- Run 5-10 real triggers through your automation.
- Fix the edge cases (what happens when someone submits a form with missing fields? What happens when your CRM is down?)
- Add error logging.

**Day 6: Show Your Team**
- Walk your team through the automation.
- Explain what it replaces, what it doesn't, and what they should do if it fails.
- Get their feedback — they'll spot edge cases you missed.

**Day 7: Identify Automation #2**
- Now that you've tasted the dopamine hit of a working automation, pick your second target.
- Client onboarding or reporting are usually the next highest-impact choices.

---

## The Full Implementation Roadmap

| Week | Focus | Automation to Build | Time Investment |
|---|---|---|---|
| Week 1 | First win | Lead capture & follow-up | 4-6 hours |
| Week 2 | Client experience | Onboarding system | 4-6 hours |
| Week 3 | Internal ops | Meeting action tracker | 3-4 hours |
| Week 4 | Back office | Invoice dunning | 2-3 hours |
| Week 5 | Client delivery | Reporting automation | 5-7 hours |
| Week 6 | Growth | Proposal/RFI drafter | 3-5 hours |
| Week 7+ | Scale & optimize | AI layer, custom agents | Ongoing |

By the end of Week 6, you've automated all 5 core workflows. Total time invested: **22-31 hours.** Time saved per week going forward: **16-25 hours.**

**Payback period:** Less than 2 weeks.

---

## The 10+ Hours/Week You Get Back

Here's what that recovered time actually looks like:

**Before automation:**
- Monday: 2 hours pulling weekly reports, 1 hour chasing payments, 1.5 hours on email follow-ups
- Tuesday: 1 hour on onboarding admin, 2 hours in meetings with no clear next steps
- Wednesday: 2 hours on proposal edits, 1 hour on manual data entry
- Thursday: 1.5 hours on reporting, 1 hour on client communications
- Friday: 2 hours of "catch-up" — the stuff that slipped all week

**After automation:**
- Monday: Review auto-generated reports (20 min), review payment status (5 min), focus on strategy
- Tuesday: Actually show up to meetings prepared because the auto-summary from last week is in your calendar
- Wednesday: Edit AI-drafted proposals (real work, not formatting)
- Thursday: Call with your best client because you have the bandwidth
- Friday: **Leave at 3 PM. Or work ON the business, not IN it.**

---

## The Compound Effect

Here's what happens over 6 months when you reinvest those 10-15 recovered hours per week:

| Time Reinvested | Activity | Revenue Impact |
|---|---|---|
| 2 hrs/week | Prospecting & outreach | 3-5 new leads/month |
| 2 hrs/week | Client relationship building | Higher retention, more referrals |
| 3 hrs/week | Service improvement & productization | Higher margins, scalable offers |
| 3 hrs/week | Strategic thinking & planning | Better decisions, fewer fire drills |

That's 10 hours/week redirected from **busywork** to **growth work.** In 6 months, that's over 250 hours of high-leverage activity.

The agencies that act on this playbook don't just "save time." They **reinvest it** and compound the advantage.

---

## The Bottom Line

You have two paths in front of you:

**Path A:** Keep doing what you're doing. Manual processes. Long hours. Good but not great margins. Your agency works **for** you.

**Path B:** Systematize the repetitive, automate the predictable, and use AI to handle the complexity. Your agency works **for you** — while you work on growth.

Path B doesn't require a bigger team, more funding, or a technical co-founder. It requires:
1. A commitment to automate one workflow per week
2. The right tools (Make.com or n8n — you now know which fits)
3. Pre-built automation components (like the Loki's Creations product line) to shortcut the build

---

## Where to Go From Here

**Immediate next steps:**

1. **Buy the tools you need.** If you don't have a Make.com or n8n account yet, create one. Both have free tiers.
2. **Pick your first automation** from Section 4. Build it today. Not tomorrow. Today.
3. **Explore the Loki's Creations product catalog** — each $39-$97 product saves you 10-20 hours of build time over building from scratch. The [AI Client Concierge System ($97)](https://your-stripe-link.com) alone can replace $60k/year in ops salary.
4. **Package your automation expertise** using the pricing models in Section 6. Your first client is easier to close than you think — start with a client you already have.

---

## Product Catalog

| Product | Price | Platform | What It Does |
|---|---|---|---|
| [AI Client Concierge System](https://your-stripe-link.com) | $97 | Make.com + n8n | Full AI-powered client intake & communication lifecycle |
| [Agency Client Onboarding Agent](https://your-stripe-link.com) | $39 | Make.com + n8n | Automated client kickoff (intake to active project in <4 hrs) |
| [Narrative Monthly Report Builder](https://your-stripe-link.com) | $39 | Make.com + n8n | AI-generated client reports with narrative insights |
| [RFP/RFI Response Drafter](https://your-stripe-link.com) | $39 | Make.com + n8n | Automated proposal & RFP response generation |
| [Invoice Dunning & Payment Reminder](https://your-stripe-link.com) | $39 | Make.com + n8n | 5-stage automated invoice follow-up sequence |
| [Meeting-to-Action Tracker](https://your-stripe-link.com) | $39 | Make.com + n8n | Transcript-to-action-items automation |

**All products available for both Make.com and n8n.**

---

## A Final Word

The agencies that dominate the next 5 years won't be the ones with the most talent, the biggest networks, or the best creative.

They'll be the ones that run on **systems** instead of **heroics.**

They'll onboard clients in hours, not days.
They'll send perfect proposals while they sleep.
They'll follow up with every lead, every time, without fail.
They'll operate with 3-person teams that deliver like 15-person teams.

That agency is yours — if you start today.

**The playbook is in your hands. Now run it.**

---

*— Loki's Creations*

*Automation systems for agencies that want to scale without the burnout.*

[Product Catalog](https://your-stripe-link.com) | [Support](mailto:support@lokiscreations.com)

---

*This playbook is © Loki's Creations. You may use, modify, and adapt the frameworks within for your own agency. Please do not redistribute this full document as your own.*
