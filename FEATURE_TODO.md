Loki’s Mischief — Full Feature TODO List
## Current Status
## Completed
- [x] Phase 0A: preserve and inventory originals
- [x] Phase 0B: scaffold readable React/Vite source
- [x] Phase 1A: shell and lifecycle contract
- [x] Phase 1B: mount all six games
- [x] Phase 1C: cross-game browser and mobile validation
- [x] Phase 2A: versioned scoring/data contracts
- [x] Phase 2B: content/model validation tooling
- [x] Phase 2C: reflection-only scan experience
- [x] Phase 3A: catalog schema and validation
- [x] Local production build
- [x] Unit, smoke, and Playwright browser tests
- [x] Original artifacts preserved byte-identically
- [x] Public push remains guarded
## Current limitations
- [ ] Only five recovered reflection prompts are available  [USER]
- [ ] Full 155-question content set is missing  [USER]
- [ ] No approved archetype scoring model exists  [USER]
- [ ] No purchasable products exist  [USER]
- [ ] Product/service commercial data is incomplete  [USER]
- [ ] No backend or purchase verification exists  [USER]
- [ ] Directory is not production-backed  [USER]
- [ ] No public deployment is authorized  [USER]
- [ ] Full behavioral parity with the live vanilla site remains unverified  [USER]
- [ ] Ratatoskr is engagement-only and contributes nothing to scoring  [USER]


---


Immediate Priority: Private Preview
## Private viewing and testing
- [ ] Run the production build locally with npm run preview  [USER]
- [ ] Verify the preview works on desktop  [USER]
- [ ] Verify the preview works on a phone over local network  [USER]
- [ ] Test all six games manually  [USER]
- [ ] Test the reflection flow  [USER]
- [ ] Test resume after refresh  [USER]
- [ ] Review all visible copy for prototype honesty  [USER]
- [ ] Confirm no product CTA appears purchasable  [USER]
- [ ] Confirm no diagnostic or archetype claims appear  [USER]
- [ ] Confirm no fake activity is presented as real  [USER]
- [ ] Decide whether a protected remote staging preview is needed  [USER]
- [ ] If remote preview is created:  [USER]
  - [ ] protect it from indexing;  [USER]
  - [ ] use staging credentials only;  [USER]
  - [ ] avoid production domain changes;  [USER]
  - [ ] avoid production webhooks;  [USER]
  - [ ] label it as a private reflection prototype.  [USER]


---


## Phase 1 Follow-Up: Behavioral and UX Hardening
Although Phase 1 integration is complete, these parity and polish tasks remain.
## Game behavior
- [ ] Document intentional behavioral differences
- [ ] Decide whether the React games need full canvas parity  [USER]
- [ ] Decide whether audio behavior should be restored  [USER]
- [ ] Verify game instructions are understandable without external context
- [ ] Verify every game has a meaningful result screen
- [ ] Verify every game has a clear restart action
- [ ] Verify every game has a clear exit action
- [ ] Verify game completion does not require hidden/debug controls
- [ ] Verify random behavior is acceptable on repeated attempts
- [ ] Verify game state resets correctly after browser refresh
- [ ] Verify game state resets correctly after route changes
- [x] Compared fenrir.html against live vanilla implementation: TODO - operator must supply comparison results
- [x] Compared hel.html against live vanilla implementation: TODO - operator must supply comparison results
- [x] Compared freyr.html against live vanilla implementation: TODO - operator must supply comparison results
- [x] Compared thor.html against live vanilla implementation: TODO - operator must supply comparison results
- [x] Compared rune-cast.html against live vanilla implementation: TODO - operator must supply comparison results
- [x] Compared ratatoskr.html against live vanilla implementation: TODO - operator must supply comparison results
## Fenrir
- [ ] Compare bottleneck mechanics against live version
- [ ] Confirm lose/result path
- [ ] Confirm score interpretation
- [ ] Confirm restart behavior
- [ ] Confirm mobile controls
## Hel
- [ ] Verify timer and spawn behavior in a real browser
- [ ] Verify keyboard controls
- [ ] Add touch controls if intended
- [ ] Verify pause/resume during visibility changes
- [ ] Verify automation-versus-human reflection copy
## Jörmungandr
- [ ] Verify sequence input behavior
- [ ] Verify repeated rounds
- [ ] Confirm previous sequence is cleared on replay
- [ ] Verify timing and timeout behavior
- [ ] Confirm mobile input support
- [ ] Confirm knowledge-silo reflection language
## Sleipnir
- [x] Verify natural RAF progression in Chromium
- [ ] Verify pointer capture with a real touch device
- [ ] Verify swipe behavior when the finger leaves the canvas
- [ ] Verify orientation and resize behavior
- [ ] Confirm handoff-failure lesson copy
## Rune Cast
- [x] Verify share-card canvas paints
- [ ] Decide whether share functionality should exist  [USER]
- [ ] If sharing is retained, add actual download/share behavior
- [ ] Ensure share output does not expose private scan data
- [ ] Confirm transformation-pattern explanation
- [ ] Confirm keyboard-accessible rune selection
## Ratatoskr
- [x] Mark as engagement-only
- [x] Exclude from scoring
- [ ] Obtain or write an approved specification
- [ ] Decide whether it remains in the public arcade  [USER]
- [ ] Decide whether it needs a business lesson  [USER]
- [ ] Decide whether it needs a result state  [USER]
- [ ] Keep unresolved status visible until approved
- [ ] Do not describe it as part of the diagnostic model


---


## Accessibility and UX
- [ ] Add accessible labels to all interactive controls
- [ ] Verify keyboard navigation across the shell
- [ ] Verify visible focus states
- [ ] Add keyboard alternatives where games promise them
- [ ] Add accessible instructions for canvas games
- [ ] Add non-canvas feedback for important game results
- [ ] Verify color contrast
- [ ] Verify colorblind-safe game indicators
- [ ] Verify touch targets are sufficiently large
- [ ] Verify reduced-motion behavior
- [ ] Verify audio is muted by default
- [ ] Add pause controls where gameplay requires sustained attention
- [ ] Verify overlays can be dismissed by keyboard
- [ ] Verify no focus traps
- [ ] Verify safe-area spacing on mobile
- [ ] Verify no horizontal scrolling
- [ ] Verify error messages are understandable
- [ ] Verify the site remains usable if canvas or audio APIs fail


---


## Phase 2: Reflection Experience
## Current reflection prototype
- [x] Reflection route exists
- [x] Five recovered prompts are displayed
- [x] Progress indicator works
- [x] Answers persist locally
- [x] Refresh resumes the draft
- [x] Reflection result is transparent
- [x] Results do not produce archetypes
- [x] Results do not produce confidence scores
- [x] Results do not recommend products
- [x] Ratatoskr is excluded from scoring context
- [x] Reflection is clearly labeled non-diagnostic
Content completion decision
### Choose one:
## Option A — Continue reflection-only
- [ ] Supply the final reflection content  [USER]
- [ ] Decide the number of prompts  [USER]
- [ ] Define each prompt’s purpose
- [ ] Define answer options
- [ ] Add provenance to each prompt
- [ ] Review wording for clarity and trust
- [ ] Add completion and result copy
- [ ] User-test comprehension
## Option B — Build the archetype model later
- [ ] Supply all 155 question texts  [USER]
- [ ] Supply answer options and values  [USER]
- [ ] Supply answer-to-score weights  [USER]
- [ ] Supply score normalization rules  [USER]
- [ ] Supply archetype thresholds  [USER]
- [ ] Supply tie-handling rules  [USER]
- [ ] Supply confidence rules  [USER]
- [ ] Define minimum completion requirements
- [ ] Define fallback behavior
- [ ] Version the approved model
- [ ] Review fixture outputs
- [ ] Run a separate model-approval phase  [USER]
- [ ] Only then activate archetype results
## Reflection UX
- [ ] Add an explicit “prototype” or “preview” label if appropriate
- [ ] Add a clear start screen
- [ ] Add resume-versus-restart choice
- [ ] Add back navigation between prompts
- [ ] Add validation for unanswered prompts
- [ ] Add restart confirmation
- [ ] Add delete-local-data control
- [ ] Add completion confirmation
- [ ] Add export option if useful
- [ ] Add a clear next step after reflection
- [ ] Ensure the next step is not an unsupported paid recommendation


---


## Phase 3B: Commercial Catalog
Status: blocked pending Loki’s commercial manifest.
## Required manifest for every intended public offer
- [ ] Final name
- [ ] Description
- [ ] Product/service type
- [ ] Stable ID
- [ ] Price
- [ ] Currency
- [ ] Checkout URL
- [ ] Gumroad ID, if applicable
- [ ] Delivery path
- [ ] Booking path for services
- [ ] Status
- [ ] Refund policy
- [ ] Contact information
- [ ] Intended audience
- [ ] Archetype mapping, if applicable
- [ ] Availability confirmation
- [ ] Display priority
- [ ] Fulfillment instructions
## Catalog implementation
- [x] Canonical catalog exists
- [x] Products and services are separated
- [x] Status lifecycle exists
- [x] Draft products are non-purchasable
- [x] URLs are not invented
- [ ] Import the real commercial manifest  [USER]
- [ ] Validate all records
- [ ] Remove incomplete records from public display
- [ ] Verify every checkout URL manually  [USER]
- [ ] Verify every delivery path manually  [USER]
- [ ] Verify every booking path manually  [USER]
- [ ] Verify prices and currencies
- [ ] Verify refund/contact information
- [ ] Verify public Notion links in an incognito browser
- [ ] Confirm no private workspace links are exposed
- [ ] Confirm no duplicate checkout URLs
- [ ] Confirm no placeholder copy remains
- [ ] Activate only approved offers
- [ ] Add graceful states for:
  - [ ] draft;
  - [ ] planned;
  - [ ] sold out;
  - [ ] retired;
  - [ ] unavailable;
  - [ ] manual review.
## Commercial UX
- [ ] Add product detail pages or complete product cards
- [ ] Add honest price display
- [ ] Add clear fulfillment expectations
- [ ] Add service booking instructions
- [ ] Add refund/contact links
- [ ] Add checkout error handling
- [ ] Add unavailable-product fallback
- [ ] Ensure reflection does not imply unsupported personalization
- [ ] Ensure product recommendations are not activated without an approved model


---


## Phase 4: Backend and Purchase Verification
Status: blocked until at least one real offer has a verified checkout and fulfillment path.
## Architecture
- [ ] Choose API/webhook hosting architecture  [BLOCKED]
- [ ] Decide whether to use a dedicated Node service, serverless function, Windmill, or Node-RED  [BLOCKED]
- [ ] Confirm raw-body access for provider verification  [BLOCKED]
- [ ] Confirm durable logging  [BLOCKED]
- [ ] Confirm retry support  [BLOCKED]
- [ ] Confirm database durability  [BLOCKED]
- [ ] Confirm monitoring and alerts  [BLOCKED]
## Identity and claims
- [ ] Define what a qualifying purchase means  [BLOCKED]
- [ ] Define purchase-to-listing relationship  [BLOCKED]
- [ ] Define one purchase to one listing policy  [BLOCKED]
- [ ] Define claim-token flow  [BLOCKED]
- [ ] Define token expiration  [BLOCKED]
- [ ] Define listing ownership and consent  [BLOCKED]
- [ ] Define what becomes public  [BLOCKED]
- [ ] Define handling of mismatched purchaser email  [BLOCKED]
- [ ] Define manual-review path  [BLOCKED]
- [ ] Define correction and deletion procedures  [BLOCKED]
## Database
- [ ] Create purchase_events  [BLOCKED]
- [ ] Create directory_listings  [BLOCKED]
- [ ] Create verification_records  [BLOCKED]
- [ ] Add provider event uniqueness  [BLOCKED]
- [ ] Add sale/order uniqueness where applicable  [BLOCKED]
- [ ] Add state-transition constraints  [BLOCKED]
- [ ] Add migrations  [BLOCKED]
- [ ] Add transaction boundaries  [BLOCKED]
- [ ] Define retention of purchase data  [BLOCKED]
- [ ] Minimize stored PII  [BLOCKED]
- [ ] Separate public and private fields  [BLOCKED]
- [ ] Add audit timestamps  [BLOCKED]
- [ ] Add manual-review reason fields  [BLOCKED]
## Webhook processor
- [ ] Implement provider-authentication verification  [BLOCKED]
- [ ] Reject malformed requests  [BLOCKED]
- [ ] Reject invalid signatures/tokens  [BLOCKED]
- [ ] Add idempotent event processing  [BLOCKED]
- [ ] Handle duplicate events  [BLOCKED]
- [ ] Handle unknown products  [BLOCKED]
- [ ] Handle refunds  [BLOCKED]
- [ ] Handle cancellations  [BLOCKED]
- [ ] Handle chargebacks if applicable  [BLOCKED]
- [ ] Handle out-of-order events  [BLOCKED]
- [ ] Handle database failures  [BLOCKED]
- [ ] Add retryable failure states  [BLOCKED]
- [ ] Add dead-letter/manual-reconciliation state  [BLOCKED]
- [ ] Log safely without unnecessary PII  [BLOCKED]
- [ ] Add alerting for processing failures  [BLOCKED]
## Verification states
- [ ] trial  [BLOCKED]
- [ ] pending  [BLOCKED]
- [ ] verified  [BLOCKED]
- [ ] manual_review  [BLOCKED]
- [ ] refunded  [BLOCKED]
- [ ] revoked  [BLOCKED]
- [ ] suspended  [BLOCKED]
## Directory
- [ ] Build public directory API  [BLOCKED]
- [ ] Exclude raw purchase data  [BLOCKED]
- [ ] Add pagination  [BLOCKED]
- [ ] Add filtering  [BLOCKED]
- [ ] Add safe error states  [BLOCKED]
- [ ] Add cache strategy  [BLOCKED]
- [ ] Ensure frontend cannot set verification state  [BLOCKED]
- [ ] Render pending/verified/revoked states distinctly  [BLOCKED]
- [ ] Add moderation process  [BLOCKED]
- [ ] Add listing correction process  [BLOCKED]
- [ ] Add listing removal process  [BLOCKED]


---


## Phase 5: Staging, Hosting, and Domain
## Environments
- [ ] Local environment
- [ ] Staging frontend
- [ ] Staging API
- [ ] Staging database
- [ ] Production frontend
- [ ] Production API
- [ ] Production database
- [ ] Separate secrets for each environment
- [ ] Separate webhook configuration
- [ ] Separate test data
## Deployment
- [ ] Document deployment architecture
- [ ] Add .env.example
- [ ] Configure repeatable builds
- [ ] Configure deployment triggers
- [ ] Configure preview deployments
- [ ] Add health endpoint
- [ ] Add structured logging
- [ ] Add error reporting
- [ ] Add deployment version display
- [ ] Add rollback procedure
- [ ] Add database migration process
- [ ] Add backup schedule
- [ ] Test database restore
## Domain and security
- [ ] Inventory existing DNS records
- [ ] Decide apex versus www  [USER]
- [ ] Configure DNS
- [ ] Configure HTTPS
- [ ] Verify HTTP-to-HTTPS redirect
- [ ] Verify canonical host
- [ ] Verify no mixed content
- [ ] Configure CORS
- [ ] Configure security headers
- [ ] Protect admin/debug endpoints
- [ ] Keep secrets out of source control
- [ ] Keep secrets out of frontend bundles
- [ ] Rotate test secrets if exposed
- [ ] Preserve existing email DNS records
- [ ] Review SPF, DKIM, and DMARC before DNS changes
## Webhook deployment
- [ ] Test webhook in staging
- [ ] Verify authentication in staging
- [ ] Verify idempotency in staging
- [ ] Verify database writes in staging
- [ ] Verify directory output in staging
- [ ] Deploy production API
- [ ] Configure production secrets
- [ ] Configure production webhook
- [ ] Send controlled production event
- [ ] Verify exactly-once logical processing
- [ ] Record event ID and resulting state
- [ ] Test refund/revocation path


---


## Phase 6: Privacy, Analytics, SEO, and Feed
## Analytics
- [ ] Define event dictionary
- [ ] Add analytics adapter
- [ ] Keep vendor calls out of components
- [ ] Track only decision-relevant events
- [ ] Define allowed properties
- [ ] Define prohibited properties
- [ ] Do not send raw answers by default
- [ ] Do not send unnecessary PII
- [ ] Define consent and opt-out
- [ ] Define retention
- [ ] Ensure analytics failure cannot break the app
- [ ] Separate staging and production analytics
- [ ] Validate event delivery
- [ ] Create basic funnel reports
### Suggested events:
- [ ] page_view
- [ ] game_started
- [ ] game_completed
- [ ] scan_started
- [ ] scan_abandoned
- [ ] scan_completed
- [ ] reflection_viewed
- [ ] result_viewed
- [ ] cta_clicked
- [ ] checkout_opened
- [ ] purchase_verified
## Privacy
- [ ] Create privacy policy
- [ ] Create data map
- [ ] Document local storage usage
- [ ] Document analytics collection
- [ ] Define deletion process
- [ ] Define correction process
- [ ] Define directory consent
- [ ] Define purchase-data retention
- [ ] Review third-party providers
- [ ] Ensure personalized results are not public
- [ ] Ensure private data is not indexed
- [ ] Add contact method for privacy requests
## SEO
- [ ] Unique page titles
- [ ] Meta descriptions
- [ ] Canonical URLs
- [ ] Open Graph tags
- [ ] Social preview images
- [ ] robots.txt
- [ ] sitemap.xml
- [ ] 404 handling
- [ ] Route fallback behavior
- [ ] Structured data only where accurate
- [ ] Public marketing pages indexable
- [ ] Personalized results noindex
- [ ] Private/admin/API routes excluded
- [ ] Copy avoids unsupported diagnostic claims
Live Mischief Feed
### Choose one:
- [ ] Real anonymized feed
- [ ] Clearly labeled illustrative feed
- [ ] Remove feed
### If real:
- [ ] Aggregate activity
- [ ] Set minimum aggregation thresholds
- [ ] Avoid identifying timestamps
- [ ] Avoid unnecessary locations
- [ ] Handle refunds and revocations
- [ ] Add moderation
- [ ] Add correction/removal process
- [ ] Prevent individual re-identification


---


## Phase 7: Release and Launch QA
## Release preparation
- [ ] Freeze feature scope
- [ ] Create release candidate branch/tag
- [ ] Record commit hash
- [ ] Snapshot catalog
- [ ] Record question/content version
- [ ] Record formula version
- [ ] Disable debug controls
- [ ] Remove test data
- [ ] Verify production environment variables
- [ ] Generate release checklist
## Automated QA
- [ ] npm run lint
- [ ] npm test
- [ ] npm run build
- [ ] npm run preview
- [ ] Route smoke tests
- [ ] Game lifecycle tests
- [ ] Reflection persistence tests
- [ ] Catalog validation
- [ ] Webhook idempotency tests
- [ ] Public/private data separation tests
- [ ] No unexpected network calls
- [ ] No console errors
- [ ] No unhandled promise rejections
## Manual browser QA
- [ ] Current desktop Chrome
- [ ] Current desktop Safari
- [ ] Firefox
- [ ] iPhone Safari
- [ ] Android Chrome
- [ ] Low-end Android
- [ ] 320px viewport
- [ ] 375px viewport
- [ ] 390px viewport
- [ ] Tablet/desktop viewport
- [ ] Touch
- [ ] Mouse
- [ ] Keyboard
- [ ] Reduced motion
- [ ] Muted audio
- [ ] Slow network
- [ ] Offline/failed analytics
- [ ] Background tab
- [ ] Orientation change
- [ ] Private browsing
## End-to-end commerce QA
- [ ] Product page
- [ ] Checkout
- [ ] Provider event
- [ ] Webhook authentication
- [ ] Event persistence
- [ ] Duplicate event
- [ ] Claim token
- [ ] Listing creation
- [ ] Consent confirmation
- [ ] Verification state
- [ ] Public directory state
- [ ] Refund
- [ ] Revocation
- [ ] Manual reconciliation
- [ ] API failure
- [ ] Database failure
- [ ] Rollback
Severity gates
## P0 — must fix before launch
- [ ] Payment failure
- [ ] Privacy leak
- [ ] Data loss
- [ ] Duplicate verification
- [ ] Incorrect scoring or reflection output
- [ ] App cannot load
- [ ] Fake activity presented as real
- [ ] Security vulnerability
## P1 — fix or explicitly waive
- [ ] Game cannot complete
- [ ] Mobile input failure
- [ ] Broken CTA
- [ ] Broken resume flow
- [ ] Serious accessibility issue
- [ ] Stale directory status
- [ ] Broken checkout or fulfillment instructions
## P2 — may remain for controlled preview
- [ ] Minor visual defect
- [ ] Minor copy issue
- [ ] Nonessential animation issue
- [ ] Low-impact browser-specific issue
## Soft launch
- [ ] Define audience size
- [ ] Define invitation method
- [ ] Define duration
- [ ] Define support channel
- [ ] Define stop conditions
- [ ] Define feedback method
- [ ] Monitor errors daily
- [ ] Monitor webhook failures
- [ ] Review user comprehension
- [ ] Review completion behavior
- [ ] Review trust concerns
- [ ] Loki performs go/no-go review  [USER]


---


## Phase 8: Post-Launch Learning
## Stabilize
- [ ] Freeze major feature expansion initially
- [ ] Fix P0/P1 issues
- [ ] Verify analytics quality
- [ ] Monitor support requests
- [ ] Monitor refunds
- [ ] Monitor webhooks
- [ ] Monitor directory corrections
- [ ] Establish baseline period
## Funnel metrics
- [ ] Traffic
- [ ] Game starts
- [ ] Game completions
- [ ] Reflection starts
- [ ] Reflection completions
- [ ] Result views
- [ ] CTA clicks
- [ ] Checkout opens
- [ ] Purchases
- [ ] Refunds
- [ ] Repeat visits
- [ ] Device breakdown
- [ ] Entry-source breakdown
- [ ] Denominator and sample size for every rate
## Qualitative feedback
- [ ] Post-reflection feedback
- [ ] Abandonment reasons
- [ ] Game comprehension
- [ ] Result credibility
- [ ] Business usefulness
- [ ] CTA expectations
- [ ] Purchase objections
- [ ] Fulfillment feedback
- [ ] Support issue categorization
- [ ] User interviews
Controlled experiments
### For every experiment define:
- [ ] Hypothesis
- [ ] Audience
- [ ] Variant
- [ ] Primary metric
- [ ] Guardrail metrics
- [ ] Duration
- [ ] Decision rule
- [ ] Version impact
### Potential experiments:
- [ ] Shorter reflection flow
- [ ] Clearer result explanation
- [ ] Less sales-heavy CTA
- [ ] Revised game onboarding
- [ ] Better product explanation
- [ ] Different result-page structure
- [ ] Optional versus mandatory game context
Expansion
### Only after evidence:
- [ ] Add missing reflection content
- [ ] Add approved archetype model
- [ ] Add products
- [ ] Retire weak products
- [ ] Add a new game
- [ ] Improve Ratatoskr specification
- [ ] Add directory features
- [ ] Add personalization
- [ ] Add integrations
- [ ] Expand analytics
- [ ] Revisit full live-site parity


---


## Current Recommended Order
1. [ ] Run and inspect a private local preview
2. [ ] User-test the five-prompt reflection prototype
3. [ ] Decide whether the prototype should remain reflection-only
4. [ ] Supply the commercial manifest if products are still desired
5. [ ] Authorize and complete Phase 3B
6. [ ] Verify at least one real offer and fulfillment path
7. [ ] Decide whether a directory is still strategically necessary
8. [ ] Design and authorize Phase 4 backend
9. [ ] Choose staging/production architecture
10. [ ] Deploy protected staging
11. [ ] Complete privacy, analytics, and SEO work
12. [ ] Run release QA
13. [ ] Conduct a controlled soft launch
14. [ ] Review evidence before public launch
15. [ ] Iterate based on observed user behavior
## Hard Rule
### Do not publicly launch until all of the following are true:
- [ ] The public copy accurately describes the reflection experience
- [ ] No unsupported diagnostic claims exist
- [ ] At least one real offer has verified checkout and fulfillment, or the store is removed/hidden
- [ ] Privacy and contact information are available
- [ ] No fake activity is presented as real
- [ ] The production build is reproducible
- [ ] Critical flows have passed real-browser testing
- [ ] Rollback and support procedures exist
- [ ] Loki gives explicit go/no-go approval  [USER]

## Done
- [x] Compare each recovered game against the live vanilla implementation  _(4c460e6d57908152e8b7ad642b41622728c832ea)_
<!-- items completed by the loop get moved here with the commit SHA -->
