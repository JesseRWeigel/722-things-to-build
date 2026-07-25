# Micro-SaaS & Paid Products

Small software products that could plausibly charge money, subscriptions, one-time purchases, paid APIs, templates, and niche B2B utilities shippable in days.

### SAAS-001: Ship an ACX audiobook preflight checker

**Scores:** $:4 CV:2 VIR:2 USE:1 ALT:3 | **Effort:** M | **Repo:** public

Build a drag-and-drop web tool that runs ffmpeg + `ebur128`/`astats` filters over an audiobook chapter set and reports every ACX submission rule: -23 to -18 dB RMS, peak below -3 dB, noise floor under -60 dB RTA, room tone head/tail length, 192kbps CBR MP3, mono/44.1kHz. Done when a failing file produces a per-chapter table plus a one-click "fix it" ffmpeg filtergraph the narrator can copy. Free for one file, $9/month for batch and saved presets.

**Needs:** nothing

### SAAS-002: Ship a broadcast subtitle delivery-spec QC tool

**Scores:** $:4 CV:3 VIR:1 USE:0 ALT:3 | **Effort:** M | **Repo:** public

Freelance subtitlers get files rejected for spec violations they can't see. Parse SRT/VTT/TTML and check reading speed (CPS), line length, min/max duration, gap between cues, shot-change proximity (via ffmpeg scene detection on the paired video), and forbidden characters, against selectable profiles modeled on published Netflix/Amazon style guides. Done when it emits a timecoded violation report and an auto-fix pass for the mechanical rules.

**Needs:** nothing

### SAAS-003: Ship a KDP print-interior preflight service

**Scores:** $:3 CV:2 VIR:1 USE:0 ALT:3 | **Effort:** M | **Repo:** public

Self-published authors burn days on rejected print PDFs. Use `pypdf` + `pikepdf` + Ghostscript to verify trim size, bleed, gutter width against page count, embedded fonts, image DPI, CMYK/RGB mixing, and blank-page parity, then render the exact pages that fail with the offending region boxed in red. One-time $19 per manuscript, unlimited re-checks for 30 days.

**Needs:** nothing

### SAAS-005: Build a Stripe chargeback evidence packet builder

**Scores:** $:5 CV:3 VIR:2 USE:1 ALT:4 | **Effort:** M | **Repo:** public

When a dispute opens, the merchant has ~7 days to assemble evidence in Stripe's exact field schema. Listen on the `charge.dispute.created` webhook, pull the customer's full history (charges, refunds, receipt emails, IP, shipping), and generate a filled `evidence` object plus a PDF narrative tailored to the dispute reason code. Done when submitting a test dispute in Stripe test mode produces a one-click-submittable packet.

**Needs:** Stripe account with test mode (plugin present, auth unverified)

### SAAS-006: Build a churn-risk scorer that reads only Stripe data

**Scores:** $:5 CV:4 VIR:2 USE:1 ALT:3 | **Effort:** M | **Repo:** public

No product analytics required, score subscription churn risk purely from billing signals: failed payment history, card expiry proximity, plan downgrades, usage-based invoice line trend, days since last invoice increase, and coupon reliance. Train a gradient-boosted model on synthetic cohorts, ship as a read-only Stripe Connect app with a weekly "these 12 accounts are at risk and here's why" digest.

**Needs:** Stripe Connect read-only OAuth app registration

### SAAS-007: Build a DMARC aggregate report parser with a plain-English digest

**Scores:** $:4 CV:3 VIR:1 USE:2 ALT:4 | **Effort:** M | **Repo:** public

Small domain owners set `rua=` and then never read the XML. Ingest DMARC RUA reports over IMAP or an inbound webhook, unzip, parse, aggregate by sending IP and org, resolve PTR/ASN, and produce a weekly email: "94% of your mail passed. These 3 senders are failing SPF, one is Mailchimp and here's the record to add, two are unknown." Done when it moves a test domain from `p=none` to a recommended `p=quarantine` with evidence.

**Needs:** an inbound-mail address (Cloudflare Email Routing or a spare domain)

### SAAS-008: Build a VPAT/ACR draft generator from a live crawl

**Scores:** $:4 CV:4 VIR:2 USE:1 ALT:5 | **Effort:** M | **Repo:** public

Selling software to government or universities requires an Accessibility Conformance Report and most small vendors have never written one. Crawl a site with Playwright + axe-core, map each violation to the specific WCAG 2.2 success criteria, and emit a filled ITI VPAT 2.5 template with Supports/Partially Supports/Does Not Support per row, remarks auto-drafted from the actual findings, and every unautomatable criterion clearly flagged for human review. Done when the output is a docx a human can finish in an hour rather than a week.

**Needs:** nothing

### SAAS-009: Build a Postgres index advisor from pg_stat_statements

**Scores:** $:4 CV:5 VIR:3 USE:2 ALT:4 | **Effort:** M | **Repo:** public

Point it at a connection string; it reads `pg_stat_statements`, `pg_stat_user_tables`, and existing index definitions, replays the top queries by total time under `EXPLAIN (FORMAT JSON)`, and proposes indexes with the estimated cost delta from a hypothetical-index simulation. Critically it also proposes *drops*, indexes with zero scans and real write cost. Done when running it against a seeded 5M-row schema produces at least one index whose creation measurably changes plan cost.

**Needs:** nothing (Neon or local Postgres for dev)

### SAAS-010: Build a synthetic data generator that respects foreign keys

**Scores:** $:4 CV:4 VIR:3 USE:3 ALT:4 | **Effort:** M | **Repo:** public

Introspect a Postgres schema (FKs, check constraints, uniques, enums, NOT NULLs) and emit a referentially-valid dataset at any row count, with column semantics inferred from names by `gemma4:e4b` so `users.email` gets emails and `orders.status` samples the real enum. Done when the generated dump restores into the same schema with zero constraint violations at 1M rows. Free CLI, paid for the hosted "keep my staging DB fresh nightly" version.

**Needs:** nothing

### SAAS-011: Build a terms-of-service and subprocessor diff watcher

**Scores:** $:5 CV:3 VIR:3 USE:2 ALT:5 | **Effort:** M | **Repo:** public

Procurement and privacy teams are contractually obliged to notice when a vendor changes its DPA or adds a subprocessor, and nobody does. Fetch a watchlist of public ToS/DPA/subprocessor pages on a schedule, normalize to text, store versions, and when a diff lands have `qwen3.6:27b` classify it as material (liability, data location, subprocessor added, arbitration) or cosmetic. Done when a material change produces a Slack/email alert with the redlined paragraph.

**Needs:** nothing

### SAAS-012: Build an allergen and dietary matrix generator for restaurants

**Scores:** $:4 CV:2 VIR:2 USE:1 ALT:5 | **Effort:** M | **Repo:** public

Independent restaurants have no way to produce the allergen matrix that UK/EU rules and increasingly US chains require. Upload a menu PDF or photo, extract dishes, ask a vision model to read handwritten prep sheets, map each dish to the 14 EU allergens plus common dietary flags via an ingredient knowledge base, and produce a printable matrix, a QR-linked mobile page, and a spreadsheet the chef can correct. Every entry is marked unverified until a human confirms.

**Needs:** Gemini API for menu photo OCR (key in env)

### SAAS-014: Build a homeschool transcript and credit tracker

**Scores:** $:4 CV:2 VIR:2 USE:2 ALT:5 | **Effort:** M | **Repo:** public

Homeschool parents assemble college-application transcripts by hand in Word and get them rejected. Model courses, Carnegie-unit hours, grading scales, and state requirements; log activities to hours automatically; and export a registrar-formatted transcript PDF plus a course-description appendix. One-time $39 per student with a free export so it never holds data hostage.

**Needs:** nothing

### SAAS-015: Build a constraint-solving scheduler for small sports leagues

**Scores:** $:4 CV:4 VIR:2 USE:1 ALT:5 | **Effort:** M | **Repo:** public

Volunteer league organizers do round-robin scheduling in spreadsheets and it takes weekends. Take teams, venues, blackout dates, ref availability, "no team plays twice in one day", home/away balance, and travel-distance limits, and solve with OR-Tools CP-SAT. Done when a 14-team, 3-field, 10-week league with 40 blackout constraints solves in under 30 seconds and exports to iCal and a public schedule page. $49 per season per league.

**Needs:** nothing

### SAAS-016: Build an RFP requirements shredder

**Scores:** $:5 CV:4 VIR:2 USE:1 ALT:4 | **Effort:** M | **Repo:** public

Government and enterprise RFPs are 200-page PDFs where the actual obligations hide in prose. Extract every sentence containing a modal obligation ("shall", "must", "will provide"), assign each a requirement ID, cluster into a compliance matrix by section, flag submission deadlines and page limits, and emit an editable spreadsheet with a Response column. Done when shredding a real published state RFP recovers requirements a manual reader missed.

**Needs:** nothing

### SAAS-017: Build a grant deadline tracker for small nonprofits

**Scores:** $:3 CV:2 VIR:2 USE:1 ALT:5 | **Effort:** M | **Repo:** public

Pull from Grants.gov's public XML extract and the IRS 990 filings of grantmaking foundations, filter to a nonprofit's NTEE code, budget size, and geography, and produce a personalized calendar of realistic opportunities with a "who funded organizations like you last year" list built from 990 Schedule I grant tables. $25/month for an organization under $1M budget.

**Needs:** nothing (Grants.gov and IRS 990 data are public bulk downloads; watch the 157 GB disk budget)

### SAAS-018: Build a batch "flambient" processor for real-estate photographers

**Scores:** $:4 CV:3 VIR:3 USE:0 ALT:3 | **Effort:** M | **Repo:** public

Real-estate shooters blend an ambient exposure with a flash exposure per room, one pair at a time, in Photoshop. Automate the whole shoot: auto-pair brackets by EXIF timestamp, align, luminosity-mask blend, window pull, vertical-line correction, and per-room white balance, using OpenCV and `rawpy`. Done when 60 image pairs process unattended into edit-ready JPEGs. Sell as a $79 desktop app or $29/month for the hosted queue.

**Needs:** a set of sample bracketed RAWs for development

### SAAS-019: Build a culling assistant for event photographers

**Scores:** $:4 CV:4 VIR:3 USE:1 ALT:3 | **Effort:** M | **Repo:** public

Culling 4,000 wedding frames is the worst day of a photographer's week. Score every frame locally on eye-open detection, subject sharpness (not global sharpness), duplicate burst clustering by embedding distance, and expression, then propose one keeper per burst with the rest collapsed. Runs entirely on the 5090 with a CLIP-class embedding model plus MediaPipe face landmarks. Done when it writes XMP sidecars Lightroom reads, so nothing is destructive.

**Needs:** nothing

### SAAS-020: Build a paid Anki deck subscription generated from a learner's own reading

**Scores:** $:4 CV:3 VIR:3 USE:4 ALT:4 | **Effort:** M | **Repo:** public

Subscribers submit URLs, ebooks, or subtitle files in Japanese, Spanish, or Brazilian Portuguese. The pipeline extracts sentences, filters to those with exactly one unknown word given the learner's known-word list, generates a cloze card with a local-model gloss and a TTS audio field, and pushes a fresh `.apkg` weekly via AnkiConnect or download. Done when a subscriber's deck measurably tracks their actual reading. $7/month.

**Needs:** a TTS voice per language (Piper voices, small download)

### SAAS-021: Build a font license auditor

**Scores:** $:3 CV:2 VIR:2 USE:1 ALT:4 | **Effort:** S | **Repo:** public

Foundries send invoices for webfont overuse and most teams cannot even enumerate which fonts they ship. Crawl a domain, collect every `@font-face` source and every locally-referenced family, fingerprint each file against a database of known foundry fonts by name table and checksum, and report family, weight count, likely license type, and pageview-tier exposure. Done when it flags a self-hosted commercial font served without a webfont license.

**Needs:** nothing

### SAAS-022: Build a nonprofit board-minutes to annual-report drafter

**Scores:** $:3 CV:2 VIR:1 USE:1 ALT:4 | **Effort:** S | **Repo:** public

Feed twelve months of board meeting minutes; get a draft annual report with a narrative of major decisions, a program-activity summary, and a pre-filled outline of the state charitable-solicitation annual filing. Uses `nemotron-3-nano` for the long-context pass so a full year fits in one prompt. Done when the draft cites the specific meeting date behind every claim. $99 one-time per year of minutes.

**Needs:** nothing

### SAAS-023: Build a recipe-scaling and food-cost calculator for small bakeries

**Scores:** $:3 CV:2 VIR:1 USE:1 ALT:4 | **Effort:** S | **Repo:** public

Small bakeries price by gut. Enter recipes in baker's percentages, ingredient costs by purchase unit, and yield; get per-unit cost, margin at a given retail price, a scaled batch sheet for any pan count, and a shopping list aggregated across the week's production plan. Handles the unit-conversion mess (bulk flour by 50lb bag, eggs by dozen, vanilla by fluid ounce) that kills spreadsheet attempts. $12/month.

**Needs:** nothing

### SAAS-024: Build a developer-tool pricing page change tracker

**Scores:** $:4 CV:2 VIR:4 USE:2 ALT:4 | **Effort:** S | **Repo:** public

Snapshot the pricing pages of ~200 developer tools weekly, extract the tier/price/limit structure into a normalized schema with a local model, and publish a public changelog of every price rise, limit cut, and free-tier removal. The public feed is the marketing; the paid product is per-competitor alerting for the vendors themselves. Done when the first "X quietly cut its free tier from 10k to 1k" post lands.

**Needs:** nothing (respect robots.txt; fetch pricing pages only)

### SAAS-025: Build a one-shot cookie and tracker audit report

**Scores:** $:3 CV:3 VIR:2 USE:1 ALT:4 | **Effort:** S | **Repo:** public

Load a site under Playwright with a clean profile, record every cookie set before consent, every third-party request, and every `localStorage` write, classify each against a tracker database, and produce a branded PDF stating exactly which trackers fire pre-consent and which GDPR/CCPA obligation each implicates. Agencies resell this to clients at $300; sell it to agencies at $15 a run.

**Needs:** nothing

### SAAS-026: Build a veterinary discharge-instruction generator

**Scores:** $:3 CV:2 VIR:1 USE:0 ALT:4 | **Effort:** S | **Repo:** public

Small-animal clinics hand out photocopied generic sheets. Let the vet pick procedure, species, weight, and meds; generate a client-readable discharge sheet with weight-calculated dosing schedule as a checklist, warning-sign list, recheck date, and a Spanish translation, all from a vet-authored template library rather than free-form generation. Runs fully local so nothing patient-related leaves the clinic. $29/month per clinic.

**Needs:** a veterinarian to review the template library before sale

### SAAS-027: Sell the agent-fleet operations playbook as a paid product

**Scores:** $:4 CV:4 VIR:4 USE:2 ALT:4 | **Effort:** S | **Repo:** none

Package what running SIBT, Taisho, and the Minecraft swarm actually taught: task rotation, orchestrator failure modes, cost control, when local models beat API models, the prompts and configs verbatim. Sell as a $49 downloadable with the real config files, not a blog post rehash. The credibility comes from shipped systems, which most people selling agent courses do not have.

**Needs:** nothing

### SAAS-028: Build a domain hygiene monitor

**Scores:** $:4 CV:2 VIR:1 USE:3 ALT:4 | **Effort:** S | **Repo:** public

Uptime monitors are a commodity; nobody watches the slow-moving stuff that actually kills a business. Track per-domain: registrar expiry, registrar lock status, nameserver changes, DNSSEC state, SSL chain expiry and issuer change, MX/SPF/DKIM/DMARC record drift, and CAA records. Alert on any change, not just failure, an unexpected nameserver change is a hijack. $4/month for 10 domains.

**Needs:** nothing

### SAAS-029: Build an email bounce autopsy tool

**Scores:** $:3 CV:2 VIR:1 USE:1 ALT:4 | **Effort:** S | **Repo:** public

Paste a bounce message or point at a bounce mailbox; get the real cause. Parse the DSN, extract the enhanced status code and the receiving MTA's diagnostic text, match against a curated corpus of provider-specific strings (Google's 550-5.7.x family, Microsoft's S3150, Yahoo's TSS), and return the actual fix with the specific DNS record or reputation action needed. Free web tool, paid mailbox-monitoring tier.

**Needs:** nothing

### SAAS-030: Build a dunning and late-fee toolkit for freelancers

**Scores:** $:4 CV:2 VIR:2 USE:2 ALT:4 | **Effort:** S | **Repo:** public

Given an invoice date, terms, and jurisdiction, compute the legally permissible late fee and interest, then generate the escalating sequence, friendly reminder, formal notice with statutory interest cited, final notice before collections, with the running balance recalculated at each step and a Stripe payment link embedded. Done when the sequence sends on schedule and stops instantly on payment.

**Needs:** Stripe account; a per-jurisdiction interest-rate table

### SAAS-031: Build a license-key server for indie desktop apps

**Scores:** $:4 CV:3 VIR:2 USE:2 ALT:4 | **Effort:** S | **Repo:** public

Indie devs selling a $39 Mac app either use Gumroad's weak keys or roll bad crypto. Ship an Ed25519 offline-verifiable license format (signed payload with product, seats, expiry, embedded in a short base32 key), a Stripe webhook that mints keys on purchase, a machine-activation endpoint with seat limits, and drop-in verification snippets for Electron, Swift, and Rust-free C. Done when a key verifies offline with a 200-line library.

**Needs:** Stripe account

### SAAS-033: Build an npm ownership-change alerter

**Scores:** $:4 CV:4 VIR:4 USE:3 ALT:5 | **Effort:** S | **Repo:** public

Supply-chain compromises usually follow a maintainer handoff or a new publisher on a long-dormant package. Watch the npm registry changes feed for the packages in a customer's lockfile and alert on: new maintainer added, publish after >12 months of silence, first-ever `postinstall` script, or a major version from a new publisher. Purely defensive monitoring on public registry metadata. Free for public repos, paid for orgs.

**Needs:** nothing

### SAAS-034: Build a changelog feed bridge for tools without one

**Scores:** $:3 CV:2 VIR:3 USE:3 ALT:4 | **Effort:** S | **Repo:** public

Hundreds of SaaS products publish changelogs as HTML with no RSS. Maintain a registry of extraction rules, poll each page, and serve a clean per-product Atom feed plus a combined "everything in my stack changed this week" digest with a local-model summary of what actually matters. The registry is the moat and it can be community-contributed. Free feeds, $5/month for the digest and Slack delivery.

**Needs:** nothing (honor robots.txt and cache politely)

### SAAS-035: Build a "should I install this package" report API

**Scores:** $:4 CV:4 VIR:4 USE:4 ALT:5 | **Effort:** S | **Repo:** public

One endpoint, one package name, one verdict page: install/postinstall scripts present, network calls in those scripts, transitive dependency count and depth, maintainer count and bus factor, typosquat distance to more popular names, license compatibility, last publish, and known advisories. Renders as a single readable page a developer can paste into a PR. Free interactively, paid as a CI gate.

**Needs:** nothing

### SAAS-036: Build an insurance EOB decoder

**Scores:** $:5 CV:4 VIR:4 USE:3 ALT:5 | **Effort:** L | **Repo:** public

Explanation-of-Benefits forms are deliberately unreadable. Upload one; get plain English: what was billed, what the negotiated rate was, what the plan paid, what you owe and why, which denial reason code applied, and whether the patient responsibility exceeds what the plan documents permit. Cross-check CPT codes against CMS public fee schedules to flag likely upcoding and duplicate billing. Done when it correctly decodes ten real anonymized EOBs from different carriers. $5 per document or $15/month for a family.

**Needs:** anonymized sample EOBs; a clear "not medical or legal advice" posture

### SAAS-037: Build a USPTO trademark watch service

**Scores:** $:5 CV:4 VIR:3 USE:1 ALT:5 | **Effort:** L | **Repo:** public

Trademark watch services cost $300+/year and small brands go unprotected. Ingest USPTO's free bulk trademark XML daily, index marks by phonetic similarity (Double Metaphone), edit distance, and Nice class, and alert a customer when a newly-filed mark is confusably similar to theirs in an overlapping class. Include the opposition deadline and a link to the TTAB filing. $12/month per mark against a $300 incumbent price.

**Needs:** disk headroom for the USPTO bulk archive (compress and prune aggressively, 157 GB free)

### SAAS-038: Build an EU AI Act technical documentation generator

**Scores:** $:5 CV:5 VIR:3 USE:2 ALT:4 | **Effort:** L | **Repo:** public

Anyone shipping an AI feature into the EU now owes Annex IV technical documentation and most teams have nothing. Walk the team through a structured intake (intended purpose, training data provenance, evaluation results, human oversight measures, accuracy and robustness metrics, risk management), pull what it can automatically from a repo (model cards, eval artifacts, dataset manifests), and emit an Annex IV-structured document with every gap explicitly listed as an open item. Done when the output survives a lawyer's read. $499 one-time or $99/month with updates.

**Needs:** legal review of the template before sale

### SAAS-039: Build an on-prem PII redaction API

**Scores:** $:5 CV:5 VIR:3 USE:3 ALT:5 | **Effort:** L | **Repo:** public

Clinics, law firms, and schools cannot send documents to a cloud API but need redaction. Ship a Docker-free installable service that runs an ensemble, regex/checksum for structured identifiers (SSN, MRN, card numbers with Luhn), a NER model for names and places, and `gemma4:31b` for contextual catches the first two miss, with a confidence score per span and a human review UI. Done when it beats a regex-only baseline on a public de-identification benchmark. Sold as a perpetual on-prem license.

**Needs:** nothing (evaluate on a public de-identification corpus, not real records)

### SAAS-040: Build an offline deposition and interview transcript summarizer

**Scores:** $:5 CV:4 VIR:2 USE:2 ALT:4 | **Effort:** L | **Repo:** public

Solo attorneys pay per page for transcript summaries. Ingest an ASCII/PTX/TXT transcript with page-line numbering, use `nemotron-3-nano` for a long-context pass, and produce: a page-line-cited issue summary, a contradiction finder that pairs conflicting statements across the transcript, an exhibit index, and a follow-up question list for the next deposition. Every claim carries its page:line cite so it is verifiable. Runs entirely local, which is the selling point.

**Needs:** sample public-record deposition transcripts for development

### SAAS-043: Build a commercial lease abstract extractor

**Scores:** $:5 CV:4 VIR:2 USE:1 ALT:4 | **Effort:** L | **Repo:** public

Small landlords and tenant-side brokers pay analysts $150 to abstract a lease. Extract the ~40 standard fields, commencement, expiry, options and their notice windows, base rent schedule with escalations, CAM/NNN treatment, percentage rent, assignment clause, holdover multiple, exclusive use, co-tenancy, each with the page and clause it came from, and flag the dates that need calendar reminders. Done when the option-notice deadline it computes matches the lawyer's for five real leases.

**Needs:** sample commercial leases (many are public in SEC EDGAR exhibits)

### SAAS-044: Build and sell a genuinely clean licensed dataset

**Scores:** $:4 CV:5 VIR:4 USE:3 ALT:5 | **Effort:** L | **Repo:** public

Pick a domain where every existing dataset is dirty, build the clean one, and publish it on Hugging Face with a paid commercial license alongside a free research license. Candidate: a deduplicated, deduped-by-near-hash, license-verified corpus of software changelogs paired with their diffs, which nobody has assembled and which is directly useful for release-note models. Done when the dataset card documents provenance per record and the dedup analysis is reproducible.

**Needs:** Hugging Face account (available); careful license verification per source

### SAAS-045: Build a podcast sponsor-read index

**Scores:** $:5 CV:4 VIR:4 USE:1 ALT:3 | **Effort:** L | **Repo:** public

Media buyers have no idea which podcasts a given advertiser is actually running on, or what a read costs. Transcribe public podcast feeds with Whisper on the 5090, detect sponsor-read segments by acoustic and linguistic markers plus promo-code extraction, and build a queryable index of advertiser × show × date × promo code. Sell access to media buyers and to the advertisers' competitors. Done when the index correctly recovers the sponsor roster of 50 shows for one month.

**Needs:** compute time for bulk transcription; use only public RSS audio and respect feed terms

### SAAS-046: Build a hospital price transparency search engine

**Scores:** $:5 CV:5 VIR:5 USE:3 ALT:5 | **Effort:** XL | **Repo:** public

CMS requires every US hospital to publish machine-readable price files, and they are a swamp of inconsistent schemas, gigabyte JSON, and deliberately unusable structure. Build the ingestion pipeline that normalizes them into a single schema keyed by CPT/DRG × hospital × payer × plan, then a consumer search ("MRI lumbar spine, my insurer, near 15001") and a paid API for employers and researchers. Done when a real procedure price comparison across five local hospitals is correct and cited to the source file.

**Needs:** significant disk and bandwidth, build a streaming ingester that never stores raw files; possibly external object storage

### SAAS-047: Build an air-gapped meeting intelligence appliance

**Scores:** $:5 CV:5 VIR:3 USE:4 ALT:4 | **Effort:** XL | **Repo:** public

Defense contractors, hospitals, and law firms are forbidden from using Otter or Zoom AI. Ship an installable service, no Docker, no internet, that does diarized Whisper transcription, speaker enrollment, action-item extraction with owner and due date, decision log, and a searchable archive with local embeddings, all on a single GPU box. Includes an install script, an offline model bundle, and an admin UI. Sold as a perpetual license plus support. Done when it runs correctly on a machine with networking disabled.

**Needs:** a plan for shipping ~30 GB of model weights offline; a second machine or VM to validate the air-gapped install

### SAAS-048: Build a litigation document review workbench for solo firms

**Scores:** $:5 CV:5 VIR:3 USE:1 ALT:5 | **Effort:** XL | **Repo:** public

Relativity costs more than a solo practice earns. Build the small version: load a production set, dedupe by hash and near-hash, thread emails, OCR scanned pages, run privilege screening against a party/counsel list, cluster by topic with local embeddings, and support tag-and-review with keyboard-first navigation and a defensible audit log of every reviewer decision. All local. Done when it handles a 50,000-document synthetic production with sub-second search.

**Needs:** a synthetic or public production set (Enron corpus works) for development

### SAAS-049: Build a vendor security questionnaire platform

**Scores:** $:5 CV:5 VIR:3 USE:2 ALT:4 | **Effort:** XL | **Repo:** public

Every B2B startup loses a week per enterprise deal to SIG Lite, CAIQ, and bespoke 300-row spreadsheets. Ingest the company's real policies, past answers, and architecture docs into a local vector store; accept a questionnaire in any format (xlsx, docx, web form); match each question to prior answers by semantic similarity; draft new answers with citations to the source policy; and flag every answer where the evidence is weak so a human reviews it rather than a model bluffing to an auditor. Done when it completes a real SIG Lite at >70% no-touch with correct citations.

**Needs:** a real questionnaire corpus (public SIG/CAIQ templates are obtainable)

