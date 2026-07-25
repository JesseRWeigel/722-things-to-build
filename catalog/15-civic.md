# Civic Tech & Nonprofit Tools

### CIVIC-002: Build a records-request generator with statutory deadline math

**Scores:** $:2 CV:4 VIR:3 USE:4 ALT:5 | **Effort:** M | **Repo:** public

WV FOIA and the PA Right-to-Know Law have different response clocks, fee rules, and appeal paths. Build a tool where a requester picks a jurisdiction and agency, gets a correctly cited request letter, and gets tracked deadlines with automatic reminders for the response date, the appeal window, and the fee-challenge window. Include a public log of requests users choose to make visible.

**Needs:** nothing.

### CIVIC-004: Run a county-wide accessibility audit bot

**Scores:** $:3 CV:5 VIR:3 USE:3 ALT:5 | **Effort:** M | **Repo:** public

Crawl every municipal, school district, library, and registered nonprofit website in Hancock, Brooke, and Jefferson counties with Playwright plus axe-core, score each against WCAG 2.2 AA, and generate a one-page prioritized remediation report per organization with code-level fixes. Email each report to the org's published contact with an offer of help, and publish an anonymized county rollup.

**Needs:** nothing.

### CIVIC-005: Ship a complete small-town municipal website kit

**Scores:** $:5 CV:5 VIR:3 USE:3 ALT:5 | **Effort:** XL | **Repo:** public

Towns under 25,000 people run websites that fail WCAG, hide the meeting schedule, and lose documents. Build a deployable kit with a meeting archive (agendas, minutes, video, transcripts), an ordinance and code search, a records-request portal wired to statutory deadlines, a budget explorer, and an emergency banner, all WCAG 2.2 AA by construction and editable by a clerk with no technical training. Include an accessible-document ingest step that OCRs scanned minutes with `ocrmypdf`, reconstructs heading structure, and emits both a tagged PDF and semantic HTML validated with `veraPDF`. Done means one real municipality is live on it with their historical documents migrated.

**Needs:** a town willing to adopt it, a domain, and a hosting decision. The demo instance runs on existing resources.

### CIVIC-006: Build a property tax appeal comparables tool

**Scores:** $:4 CV:4 VIR:4 USE:4 ALT:5 | **Effort:** L | **Repo:** public

Allegheny County publishes parcel assessments and sales through WPRDC, and WV counties publish assessment rolls. Let a homeowner enter an address, get their assessment-to-recent-sale ratio compared to genuinely comparable parcels (same neighborhood, similar square footage, similar year built, arms-length sales only), and download a formatted evidence packet matching the board of assessment appeals format. Done means the comparable-selection logic is documented and defensible in a hearing.

**Needs:** nothing.

### CIVIC-007: Keep a community resource directory from rotting

**Scores:** $:3 CV:3 VIR:2 USE:3 ALT:5 | **Effort:** M | **Repo:** public

Every 211-style local resource list decays because hours and phone numbers change and nobody re-verifies. Build a directory backed by a simple schema (HSDS) with an automated verifier that checks website liveness, detects changed hours text, flags disconnected numbers via published contact pages, and generates weekly call sheets so a volunteer only phones the entries the bot could not confirm. Deploy for the Ohio Valley.

**Needs:** nothing.

### CIVIC-008: Publish a food pantry hours API and offline PWA

**Scores:** $:2 CV:3 VIR:2 USE:3 ALT:5 | **Effort:** M | **Repo:** public

Pantry schedules in the Ohio Valley live in Facebook posts and church bulletins. Build a normalized dataset of pantry location, hours, eligibility requirements, and documents needed, expose it as a JSON API, and ship a PWA that works offline and shows "open right now, nearest first." Recruit two or three pantries as data owners with a simple edit link so it stays current.

**Needs:** nothing.

### CIVIC-009: Fuse local emergency feeds into one alert channel

**Scores:** $:2 CV:4 VIR:3 USE:5 ALT:5 | **Effort:** M | **Repo:** public

NWS publishes CAP alerts by county, 511PA and WV 511 publish road closures, and county EMAs post advisories. Build a fusion service that deduplicates across feeds, filters to a user-drawn geofence, and delivers over ntfy and email with severity-based quiet hours. Include a "what changed" digest so a subscriber is not paged for a repeat of the same alert.

**Needs:** nothing.

### CIVIC-010: Alert residents at their own flood threshold, not the county's

**Scores:** $:2 CV:5 VIR:4 USE:4 ALT:5 | **Effort:** L | **Repo:** public

A county-wide flood warning tells someone on a hill nothing and someone in a hollow too little. Combine USGS NWIS gauge readings, NWS AHPS forecast stages, and USGS 3DEP elevation at a user's address to compute the gauge height at which their property floods, then alert on the forecast crossing that number with lead time. Done means a validation writeup against at least one historical Ohio Valley flood event.

**Needs:** nothing.

### CIVIC-011: Ship an offline-first shelter and resource map

**Scores:** $:1 CV:4 VIR:3 USE:3 ALT:5 | **Effort:** M | **Repo:** public

During an outage or flood the network is exactly what fails. Build a PWA that pre-caches vector map tiles (PMTiles from OSM extracts) plus shelter, warming center, water distribution, and charging locations for a county, works fully offline after first load, and syncs updates opportunistically. Hand it to a county EMA as an installable link with a printable QR poster.

**Needs:** nothing.

### CIVIC-012: Package flood damage photos into a FEMA-ready report

**Scores:** $:2 CV:4 VIR:3 USE:3 ALT:5 | **Effort:** M | **Repo:** public

After a flood, residents take hundreds of phone photos and then struggle to document losses. Build an intake that reads EXIF timestamps and coordinates, groups photos by address, runs local vision captioning to draft item descriptions, and outputs a per-property PDF packet with a room-by-room inventory formatted for FEMA Individual Assistance and insurance claims. Include a bulk mode for a county damage assessment team.

**Needs:** nothing. Vision captioning uses a local multimodal Gemma variant; verify the pulled tag supports images before relying on it.

### CIVIC-013: Plan cold-weather street outreach routes with triage

**Scores:** $:1 CV:4 VIR:2 USE:2 ALT:5 | **Effort:** M | **Repo:** public

Outreach teams working an unhoused population on a freezing night need to hit the highest-risk locations first with limited vehicles. Build a planner that takes known camp and contact locations, last-contact dates, individual risk flags entered by case managers, and the NWS hourly forecast, then produces optimized multi-vehicle routes with a printable card per stop. Location data stays on the org's own machine.

**Needs:** nothing.

### CIVIC-016: Optimize Meals on Wheels routes on local infrastructure

**Scores:** $:3 CV:4 VIR:2 USE:2 ALT:5 | **Effort:** L | **Repo:** public

Most volunteer meal delivery routes were drawn on paper a decade ago. Stand up a local OSRM instance on an OSM extract of the Northern Panhandle, solve the capacitated vehicle routing problem with time windows for hot-meal delivery, and output turn-by-turn printable route sheets plus a driver-facing mobile page. Include a "driver called off" re-solve that reassigns stops in under a minute.

**Needs:** nothing.

### CIVIC-024: Solve liturgical ministry scheduling as a constraint problem

**Scores:** $:3 CV:3 VIR:2 USE:4 ALT:4 | **Effort:** S | **Repo:** public

Scheduling lectors, servers, ushers, and extraordinary ministers across five weekend Masses is a real constraint problem that a volunteer coordinator currently does by hand for hours. Model it in OR-Tools with per-person blackout dates, preferred Mass, family grouping, and minimum rest between assignments, then emit a quarter schedule as PDF, ICS, and per-person reminder emails with a one-click swap request flow.

**Needs:** nothing.

### CIVIC-029: Track grant deadlines for small Appalachian nonprofits

**Scores:** $:3 CV:3 VIR:2 USE:2 ALT:5 | **Effort:** S | **Repo:** public

Grants.gov has a search API, and most small nonprofits never see the opportunities that fit them. Build a filtered feed for organizations under $1M in revenue in ARC-region counties, scored for fit against an org profile with a local model, delivered as a weekly digest with deadline countdowns and links to the full announcement. Include state-level WV and PA opportunity sources.

**Needs:** nothing.

### CIVIC-030: Send filing reminders that keep small nonprofits alive

**Scores:** $:3 CV:2 VIR:2 USE:2 ALT:5 | **Effort:** S | **Repo:** public

Thousands of small nonprofits lose exempt status by missing three consecutive 990-N filings, and state charitable-solicitation registrations lapse just as quietly. Build a tracker seeded from the IRS Exempt Organizations Business Master File that computes each org's filing deadline from its fiscal year end, emails escalating reminders, and includes a per-state registration renewal calendar for WV, PA, and OH.

**Needs:** nothing.

### CIVIC-031: Generate IRS-compliant donor acknowledgment letters

**Scores:** $:3 CV:2 VIR:1 USE:2 ALT:5 | **Effort:** S | **Repo:** public

Substantiation letters must contain specific language, and small nonprofits routinely send letters that would not survive an audit. Build a generator that takes a donation CSV, applies the correct language for cash, non-cash, quid pro quo, and vehicle donations, handles the $250 and $75 thresholds, merges into a branded letter, and produces both PDFs and year-end summary statements.

**Needs:** nothing.

### CIVIC-032: Build a grant readiness self-assessment that produces a work plan

**Scores:** $:3 CV:2 VIR:2 USE:1 ALT:5 | **Effort:** S | **Repo:** public

Small organizations apply for grants they cannot win because they lack an audit, a board conflict-of-interest policy, or a SAM.gov registration. Build a 25-question self-assessment that outputs a scored readiness report and a sequenced checklist with links to the actual forms, plus an estimate of which funder tiers are realistic today versus after remediation.

**Needs:** nothing.

### CIVIC-033: Track board terms and conflicts of interest

**Scores:** $:2 CV:2 VIR:1 USE:1 ALT:4 | **Effort:** S | **Repo:** public

Nonprofit boards drift out of compliance with their own bylaws on term limits, quorum, and annual conflict-of-interest disclosure. Build a small app that stores bylaws-derived rules, tracks each director's term start and expiration, flags quorum risk for upcoming meetings, runs the annual COI disclosure cycle by email, and exports the disclosure set for the 990 Schedule L question.

**Needs:** nothing.

### CIVIC-034: Ship a local-only AI helpdesk appliance for nonprofits

**Scores:** $:4 CV:5 VIR:4 USE:4 ALT:5 | **Effort:** L | **Repo:** public

Nonprofits handling client PII cannot paste case notes into a hosted model, and they know it. Package an Ollama-based assistant that indexes an organization's own policy documents, forms, and procedures with local embeddings, answers staff questions with citations, drafts routine correspondence, and never makes an outbound network call. Deliverable is a one-command installer, a hardware sizing guide, and a written data-flow statement an executive director can hand to a funder.

**Needs:** nothing to build; a modest GPU box on site to deploy at a real org.

### CIVIC-035: Build a peer benchmarking dashboard for small libraries

**Scores:** $:3 CV:3 VIR:2 USE:1 ALT:5 | **Effort:** M | **Repo:** public

A small library director defending a levy needs to show how their circulation, program attendance, and internet sessions compare to genuinely similar libraries. Use the IMLS Public Libraries Survey to auto-generate a peer group by legal service area population and revenue per capita, and produce a printable one-page board packet plus an interactive comparison view for every library in WV and western PA.

**Needs:** nothing.

### CIVIC-036: Crowdsource a curb ramp and sidewalk survey into OSM

**Scores:** $:1 CV:4 VIR:3 USE:2 ALT:5 | **Effort:** M | **Repo:** public

Wheelchair users in most small cities have no map of which corners actually have a ramp. Build a phone-first survey PWA that walks a volunteer down a block, captures ramp presence, condition, and slope estimate with a photo, and submits properly tagged edits to OpenStreetMap through the standard API with changeset attribution. Add a coverage map so a city can see what has been surveyed.

**Needs:** an OSM account for edit submission.

### CIVIC-037: Package resident speed tests into an FCC availability challenge

**Scores:** $:2 CV:5 VIR:4 USE:3 ALT:5 | **Effort:** L | **Repo:** public

The FCC's Broadband Data Collection accepts availability challenges from consumers, but the evidence requirements defeat most people. Build a tool that runs standardized speed tests over time from a resident's connection, records the required evidence fields (location, timestamp, provider, service tier as billed), and assembles a submission-ready challenge packet, with a bulk mode a county government can use to challenge overstated coverage across many addresses at once.

**Needs:** review of the current FCC challenge evidence spec before submission; test artifacts alone do not guarantee acceptance.

### CIVIC-038: Notify a small town about boil-water advisories

**Scores:** $:1 CV:2 VIR:2 USE:3 ALT:5 | **Effort:** S | **Repo:** public

Small water utilities announce boil advisories on a Facebook page and a voicemail greeting, and half the town misses it. Build a lightweight publisher the utility clerk can use (one form, one button) that pushes to SMS-free channels (email, ntfy, RSS, a status page with a giant colored banner) and auto-expires the notice, plus an archive of past advisories with affected street lists.

**Needs:** the utility's willingness to use it; SMS delivery would need a paid gateway.

### CIVIC-039: Aggregate school closings and delays from official sources

**Scores:** $:1 CV:2 VIR:2 USE:4 ALT:4 | **Effort:** S | **Repo:** public

Parents in Hancock and Brooke counties check three district Facebook pages and a TV station at 5:30 in the morning. Build a poller that reads only official district notification pages and RSS feeds, normalizes to a "closed / two-hour delay / early dismissal" status per district, and pushes a single ntfy notification with a status page. Include the parochial schools that piggyback on district decisions.

**Needs:** nothing. Skip any source whose terms prohibit automated access.

### CIVIC-040: Generate large-format transit schedule cards from GTFS

**Scores:** $:1 CV:2 VIR:2 USE:2 ALT:5 | **Effort:** S | **Repo:** public

Seniors and low-vision riders cannot read the tiny folded route timetables, and agency websites are worse. Build a generator that reads any agency's GTFS feed and produces a high-contrast, 20-point, single-stop departure card for a chosen stop and day type, printable on letter paper and postable at the shelter or senior center. Generate the full set for Pittsburgh Regional Transit and the Ohio Valley Regional Transportation Authority.

**Needs:** nothing.

### CIVIC-042: Build a crowdsourced OCR correction platform for local history

**Scores:** $:2 CV:4 VIR:3 USE:2 ALT:5 | **Effort:** L | **Repo:** public

A county historical society has boxes of scanned church registers, city directories, and photographs with no index, and volunteers who would happily type. Build a platform that serves a scanned line image next to a pre-filled machine transcription, collects volunteer corrections with double-keying for confidence, tracks contributor stats, and exports a searchable index plus IIIF manifests for the images. Deploy for one historical society with a real collection.

**Needs:** a partner institution and their digitized scans.

### CIVIC-043: Schedule interpreters for a rural clinic

**Scores:** $:3 CV:3 VIR:1 USE:1 ALT:5 | **Effort:** S | **Repo:** public

Clinics serving immigrant patients juggle a handful of contract interpreters across languages and appointment times, and a missed match means a canceled visit. Build a scheduler that matches appointment language, modality (in person, phone, video), and interpreter availability, sends confirmations, tracks no-shows, and produces a monthly language-access report for Title VI documentation.

**Needs:** nothing.

### CIVIC-044: Remediate documents for dyslexic and low-vision readers

**Scores:** $:2 CV:3 VIR:3 USE:3 ALT:5 | **Effort:** S | **Repo:** public

Public notices, school letters, and benefit forms arrive as dense justified text that many adults cannot get through. Build a browser extension plus CLI that reflows a page or PDF with an OpenDyslexic or Atkinson Hyperlegible face, wider tracking, left-aligned ragged-right lines, paragraph shading, and an optional local-LLM plain-language summary shown alongside, never replacing, the original text.

**Needs:** nothing.

### CIVIC-045: Rewrite government forms into plain language with a readability gate

**Scores:** $:3 CV:4 VIR:3 USE:2 ALT:5 | **Effort:** M | **Repo:** public

Agencies are required to write in plain language and mostly do not. Build a tool that scores a form or notice with several readability metrics, produces a rewritten version with a local model under a strict instruction not to change meaning or omit required legal language, and renders a side-by-side diff with a checklist of preserved legal terms. Target the WV DHHR and PA DHS benefit notices as the first corpus.

**Needs:** nothing.

### CIVIC-047: Remind immigration clients of hearings and required documents

**Scores:** $:2 CV:4 VIR:3 USE:1 ALT:5 | **Effort:** M | **Repo:** public

Missing an immigration hearing can trigger an in-absentia removal order, and pro bono clinics track dates in spreadsheets. Build a clinic-facing tracker that stores case numbers and hearing dates, checks the EOIR automated case-status system for changes, sends multilingual reminders at 30, 7, and 1 days, and generates a per-case document checklist for the specific relief being sought. Client data stays self-hosted.

**Needs:** a partner legal clinic to define the case types, and confirmation that programmatic EOIR status checks are permitted at the rate used.

### CIVIC-048: Stand up an Ohio Valley civic data commons

**Scores:** $:3 CV:5 VIR:4 USE:4 ALT:5 | **Effort:** XL | **Repo:** public

There is no single place to query Hancock, Brooke, Jefferson, and Allegheny county public data. Build scheduled ingesters for every publishable source (assessments, permits, court dockets where open, budgets, 911 call summaries, WPRDC datasets), land them in versioned parquet with per-source provenance and change history, and serve a Datasette instance with saved queries, an API, and email alerts on new rows matching a saved filter. Done means at least 25 live sources refreshing on schedule with a public changelog.

**Needs:** nothing, though several counties will require records requests to get machine-readable versions. Track those in the repo.

### CIVIC-050: Build a county disaster response coordination platform

**Scores:** $:4 CV:5 VIR:4 USE:3 ALT:5 | **Effort:** XL | **Repo:** public

When a county EMA activates, coordination happens over phone, whiteboard, and group text. Build an incident platform with a shared situation board, resource request and fulfillment tracking, volunteer check-in with skill tags and liability acknowledgment, shelter capacity, a public status page, and full offline operation with conflict-resolving sync so it keeps working when connectivity drops. Deliverable includes a tabletop exercise run with a real county EMA and the after-action fixes applied.

**Needs:** a county EMA partner willing to exercise it; the software itself runs on existing resources.

