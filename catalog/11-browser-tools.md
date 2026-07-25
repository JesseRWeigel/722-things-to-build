# Browser Extensions & Web Tools

Chrome/Firefox extensions, bookmarklets, userscripts, PWAs, and single-page utilities, including local-LLM extensions that talk to Ollama on localhost.

### EXT-001: Bookmarklet that dumps a page's structured data as a table

**Scores:** $:1 CV:2 VIR:2 USE:3 ALT:4 | **Effort:** S | **Repo:** public

One bookmarklet that harvests every JSON-LD block, microdata scope, RDFa triple, OpenGraph tag, and Twitter card on the current page and renders them side by side in an overlay, highlighting where they disagree (an `og:title` that differs from the JSON-LD `name` is a real SEO bug). Done when it works on a product page, an article, and a recipe page and offers a one-click JSON download.

**Needs:** nothing

### EXT-002: Bookmarklet that strips tracking parameters and copies the canonical URL

**Scores:** $:1 CV:1 VIR:3 USE:4 ALT:5 | **Effort:** S | **Repo:** public

Remove the full ClearURLs-style parameter set (`utm_*`, `fbclid`, `gclid`, `si`, `igshid`, Amazon's `ref=` path segments), prefer the page's `<link rel=canonical>` when it exists and is same-origin, unwrap known redirector wrappers, and copy the result with a toast showing exactly what was removed. Done when a mangled Amazon and a mangled YouTube URL both come back clean and still resolve.

**Needs:** nothing

### EXT-003: Bookmarklet that turns any HTML table into CSV, JSON, or SQL

**Scores:** $:1 CV:1 VIR:3 USE:5 ALT:5 | **Effort:** S | **Repo:** public

Click it, hover any table to highlight it, click to export. Handles `colspan`/`rowspan` normalization, nested header rows collapsed into compound column names, numeric and date type inference, and thousands separators. Emits CSV, JSON, Markdown, or a `CREATE TABLE` + `INSERT` pair. Done when it correctly flattens a Wikipedia table with merged header cells that every naive scraper mangles.

**Needs:** nothing

### EXT-004: Bookmarklet that audits contrast and proposes the nearest passing color

**Scores:** $:1 CV:3 VIR:2 USE:3 ALT:5 | **Effort:** S | **Repo:** public

Walk every text node, compute the effective background through stacked translucent parents and gradients, evaluate WCAG 2.2 contrast plus APCA Lc, and for each failure suggest the nearest color in OKLCH that passes while preserving hue and chroma as far as possible. Overlay the failures in place with the suggested hex. Done when it catches a failure that axe-core misses because of a gradient background.

**Needs:** nothing

### EXT-005: Bookmarklet that reverse-engineers a page's type scale

**Scores:** $:1 CV:2 VIR:3 USE:3 ALT:4 | **Effort:** S | **Repo:** public

Collect every distinct computed font-family, size, weight, line-height, letter-spacing, and measure (characters per line) on the page, cluster them into the underlying scale, detect the ratio (1.2, 1.25, golden), flag sizes that fall off the scale, and emit the whole thing as CSS custom properties plus a Tailwind theme fragment. Useful for both stealing good typography and auditing your own drift.

**Needs:** nothing

### EXT-006: Userscript that heatmaps a GitHub repo's file tree by size and churn

**Scores:** $:1 CV:3 VIR:3 USE:4 ALT:4 | **Effort:** S | **Repo:** public

On any repo page, overlay each file and directory in the tree with a two-channel indicator: color for commit churn over the last 90 days, bar width for line count. Data comes from the GitHub API with aggressive caching. Reading an unfamiliar codebase starts with "what actually changes", and GitHub shows neither. Done when opening a large repo immediately reveals the three files that absorb half the commits.

**Needs:** nothing (`gh` token already available; extension prompts for a PAT)

### EXT-007: Userscript that warns on the npm package page before you install

**Scores:** $:1 CV:3 VIR:4 USE:5 ALT:5 | **Effort:** S | **Repo:** public

Inject a verdict banner at the top of any npmjs.com package page: presence of `install`/`postinstall` scripts, unpacked size versus dependency count, maintainer count and whether any joined in the last 30 days, days since last publish, deprecated transitive deps, and Levenshtein distance to more-downloaded package names as a typosquat signal. All from the public registry API. Done when it flags a known typosquat name red before you copy the install command.

**Needs:** nothing

### EXT-008: Extension that finds every feed a page offers and exports OPML

**Scores:** $:1 CV:1 VIR:2 USE:4 ALT:4 | **Effort:** S | **Repo:** public

Browsers removed feed autodiscovery and nothing replaced it. Detect `<link rel=alternate>` feeds, plus the well-known conventions (`/feed`, `/rss.xml`, `/index.xml`, `/atom.xml`, GitHub releases and commits `.atom`, YouTube channel feeds, subreddit `.rss`, Mastodon account feeds), show a badge count, and let you accumulate finds across a browsing session into a single OPML export. Done when it finds the YouTube channel feed that YouTube hides.

**Needs:** nothing

### EXT-009: Web tool that explains a cron expression and its daylight-saving traps

**Scores:** $:2 CV:2 VIR:3 USE:4 ALT:5 | **Effort:** S | **Repo:** public

Every cron explainer stops at "at 2:30 AM every day." This one asks for a timezone and shows the next 20 fires as absolute UTC instants, then explicitly calls out the DST failure modes: this job never runs on the spring-forward date, this job runs twice on fall-back, this job drifts relative to business hours for half the year. Also renders a year-long fire density strip. Done when it correctly reports the skipped run for `30 2 * * *` in America/New_York.

**Needs:** nothing

### EXT-010: Web tool that decodes any opaque blob you paste

**Scores:** $:1 CV:3 VIR:4 USE:5 ALT:5 | **Effort:** S | **Repo:** public

Paste anything; it recursively identifies and unwraps. Base64/base64url/base32/hex, gzip/deflate/brotli, JWT with header/payload/signature broken out and expiry checked, protobuf decoded to a field-number tree without a schema, MessagePack, CBOR, ASN.1/DER certificates, URL encoding, and JSON-in-string-in-JSON nesting. Shows the decode chain it followed. Entirely client-side so pasting a real token is safe. Done when a gzipped base64 protobuf inside a JWT claim fully unwraps in one paste.

**Needs:** nothing

### EXT-011: Web tool that generates a complete icon and social-image set client-side

**Scores:** $:2 CV:2 VIR:2 USE:4 ALT:4 | **Effort:** S | **Repo:** public

Drop one SVG or high-res PNG; get the full modern set, `favicon.ico` multi-resolution, `icon.svg` with a dark-mode media query, maskable Android icons with correct safe-area padding, Apple touch icon with the opaque background iOS requires, `manifest.webmanifest`, and the exact HTML head snippet. All in-browser via canvas and wasm, nothing uploaded. Done when the maskable icon passes Lighthouse's PWA check.

**Needs:** nothing

### EXT-012: Web tool that builds an accessibility matrix for a whole palette

**Scores:** $:1 CV:3 VIR:3 USE:4 ALT:5 | **Effort:** S | **Repo:** public

Paste a palette; get an N×N grid of every foreground/background pair with WCAG AA/AAA and APCA results at both body and large text sizes, plus a simulation row for protanopia, deuteranopia, and tritanopia showing which pairs become indistinguishable. Then the useful part: an auto-repair that nudges lightness in OKLCH to make the whole matrix pass with minimum total perceptual change. Done when it repairs a real failing brand palette.

**Needs:** nothing

### EXT-013: Extension that shows true unit price on grocery sites

**Scores:** $:2 CV:1 VIR:3 USE:5 ALT:5 | **Effort:** S | **Repo:** public

Grocery sites bury or omit price-per-unit, and where they show it they use inconsistent units so a 12-pack and a 2-liter are not comparable. Parse product cards on major grocery and warehouse sites, normalize everything to price per 100g, per liter, and per serving, and inject a sortable badge. Done when sorting a search results page by true unit price surfaces a different winner than the site's own "best value" tag.

**Needs:** nothing (DOM parsing on pages the user already loaded; no bulk scraping)

### EXT-014: Web tool that counts prompt tokens and costs across every provider

**Scores:** $:2 CV:3 VIR:3 USE:5 ALT:5 | **Effort:** S | **Repo:** public

Paste a prompt; see the token count under each provider's actual tokenizer running client-side in wasm (tiktoken variants, SentencePiece for Gemma/Qwen, Claude's approximation), with cost per call at current published prices and cost projected at 10k calls/day. Also flags the difference between tokenizers, which is where budget estimates go wrong. Done when the local Qwen count matches what Ollama reports for the same string.

**Needs:** nothing

### EXT-016: Extension that summarizes any page locally with claim-to-span citations

**Scores:** $:3 CV:4 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

The differentiator over every existing summarizer: each bullet in the summary is clickable and scroll-highlights the exact paragraph it came from, and any bullet the model could not ground in a span is rendered in a distinct "unsupported" style. Talks to `http://localhost:11434` with `qwen3.6:27b`, so nothing leaves the machine. Done when a deliberately hallucinated claim is visibly marked unsupported rather than presented as fact.

**Needs:** nothing (Ollama must allow the extension origin via `OLLAMA_ORIGINS`)

### EXT-017: Extension that turns a text selection into an Anki card

**Scores:** $:3 CV:3 VIR:3 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Select a sentence in Japanese, Spanish, or Brazilian Portuguese; a local model produces a cloze card with the target word blanked, a definition in the target language at the learner's level, a literal and a natural translation, the grammar point in play, and the source URL. Pushes via AnkiConnect to the right deck by language. Done when it handles Japanese correctly, which means tokenizing with a morphological analyzer rather than trusting the model to find word boundaries.

**Needs:** Anki desktop with AnkiConnect for the push path (download works without it)

### EXT-018: Extension that injects reading aids into foreign-language pages

**Scores:** $:3 CV:4 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Furigana over Japanese kanji, pinyin over Chinese, and stress marks plus a syllable split for Spanish and Portuguese, injected inline with `<ruby>` so the layout survives. Uses proper dictionaries (JMdict, kanjidic, CC-CEDICT) for the deterministic part and a local model only for reading disambiguation where the dictionary is ambiguous. A per-word known/unknown state persists so learned words stop getting annotated. Done when it reads a Japanese news page correctly including name readings.

**Needs:** dictionary files (JMdict/CC-CEDICT, ~100 MB, free licenses)

### EXT-019: Extension that grades any page's reading difficulty by CEFR level

**Scores:** $:3 CV:4 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Estimate the CEFR level (A1–C2) of the current page in any of the supported languages from vocabulary frequency bands, sentence length distribution, and syntactic depth, then highlight the specific words and constructions above the reader's set level. The real feature is a browsing filter: "show me only pages at or below B1" scored on search result pages before you click. Done when a learner can find level-appropriate native content without a curated list.

**Needs:** frequency lists per language (public domain corpora)

### EXT-020: Extension that turns a YouTube video into structured notes offline

**Scores:** $:3 CV:3 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Pull the video's own caption track (no re-transcription, no scraping of anything but the page you are watching), segment it by topic shift, and produce timestamped notes with clickable seeks, a "commands and code mentioned" section for technical videos, and any URLs the speaker reads aloud reconstructed. All through local Ollama. Done when a 90-minute conference talk becomes a two-page outline whose timestamps land within five seconds.

**Needs:** nothing

### EXT-021: Extension that summarizes a comment thread by disagreement

**Scores:** $:2 CV:3 VIR:5 USE:5 ALT:4 | **Effort:** M | **Repo:** public

On Hacker News, Lobsters, or a GitHub issue, do not produce "the community discussed X." Instead, cluster the thread into positions, name the actual crux each subthread is arguing about, identify which claims are contested versus conceded, and surface the highest-information comment that most readers will never scroll to. Runs on local `qwen3.6:35b-a3b`. Done when the output on a 400-comment thread beats reading the top 20 comments.

**Needs:** nothing

### EXT-022: Extension that finds prior discussion of the page you are on

**Scores:** $:2 CV:2 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Badge shows "discussed 4 times" on any page. Queries the HN Algolia API and the Reddit search API for the canonical URL, its variants with tracking stripped, and its exact title, deduplicates, and lists threads by comment count with the top comment previewed inline. Done when landing on a five-year-old blog post immediately reveals the HN thread that debunked it.

**Needs:** nothing (both APIs are public and documented for this use)

### EXT-023: Extension that reorders PR files into dependency order

**Scores:** $:3 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

GitHub shows changed files alphabetically, which is the worst possible review order. Build the import graph across the changed files, topologically sort it, and re-order the diff so the leaf modules a reviewer needs to understand first appear first, with a small graph showing where the current file sits. Also collapses generated files and lockfiles by default. Done when reviewing a 30-file PR feels like reading a narrative instead of a shuffled deck.

**Needs:** nothing

### EXT-024: Extension that reviews what you are about to send

**Scores:** $:3 CV:4 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Bind a key in any textarea or contenteditable, Gmail, GitHub comment box, Slack web, Linear. A local model returns three things only: unstated assumptions the reader will not share, questions the message invites that it fails to preempt, and a tone reading against a target you set (blunt, warm, formal). It does not rewrite. Done when it catches a missing "here's what I need from you" in a real work email.

**Needs:** nothing

### EXT-025: Extension that generates alt text worth shipping

**Scores:** $:3 CV:4 VIR:3 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Right-click any image for a draft alt attribute that follows real rules rather than captioning: decorative images get `alt=""`, images inside a link describe the destination, charts get the data trend rather than "a chart", text-in-image gets transcribed verbatim, and length stays under 125 characters. Uses Gemini's vision endpoint. Also has a page-audit mode listing every image missing or with bad alt text, with a copyable patch. Done when a real site audit produces alt text a screen-reader user would accept.

**Needs:** `GEMINI_API_KEY` (in env)

### EXT-026: Extension that turns highlights into a markdown knowledge base

**Scores:** $:3 CV:3 VIR:3 USE:5 ALT:4 | **Effort:** M | **Repo:** public

Highlight text on any page; it persists anchored by a robust text-quote selector that survives minor page edits, with an optional note. Everything is stored locally and exports as one markdown file per source with YAML frontmatter, or syncs to a chosen folder via the File System Access API so it lands straight in Obsidian. Done when highlights re-anchor correctly after the source page is edited.

**Needs:** nothing

### EXT-027: Extension that captures network traffic and replays it as curl

**Scores:** $:3 CV:4 VIR:3 USE:5 ALT:5 | **Effort:** M | **Repo:** public

A DevTools panel that watches `fetch`/XHR, groups requests by inferred API endpoint (path templating so `/users/123` and `/users/456` collapse), and for any request emits a runnable curl, an HTTPie command, a `.http` file, or a typed TypeScript client stub inferred from the observed request and response shapes across all captured calls. Redacts auth headers on export by default. Done when clicking through an app produces a usable client for its undocumented API.

**Needs:** nothing

### EXT-028: Extension that visualizes focus order and tab traps

**Scores:** $:2 CV:4 VIR:3 USE:3 ALT:5 | **Effort:** M | **Repo:** public

Overlay numbered badges on every focusable element in DOM tab order, draw the path as a line so a jarring visual order is obvious at a glance, and flag: positive `tabindex` values, focusable elements that are visually hidden, elements whose focus ring is suppressed with no replacement, and modal dialogs that fail to trap focus (tested by actually driving focus in a loop). Done when it catches a real focus trap failure in a shipped modal.

**Needs:** nothing

### EXT-030: Web tool that turns sample JSON into a full type stack

**Scores:** $:3 CV:4 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Paste one or several JSON samples of the same shape; get TypeScript interfaces, a Zod schema, a JSON Schema, a Postgres `CREATE TABLE` with sensible types and nullability inferred from which fields were absent across samples, a Kysely/Drizzle definition, and a faker-based generator that produces new valid instances. Multi-sample inference is the differentiator, one sample cannot tell you what is optional. Entirely client-side.

**Needs:** nothing

### EXT-031: Web tool that symbolicates a stack trace in the browser

**Scores:** $:3 CV:4 VIR:3 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Paste a minified production stack trace, drop in the `.map` files (or let it fetch them if they are published), and get the original file, line, function name, and surrounding source context for every frame, all client-side, so proprietary sourcemaps never leave the machine, which is exactly why teams cannot use the existing hosted tools. Handles multiple maps, inline sources, and `sourceRoot` weirdness. Done when it correctly resolves a real Next.js production trace.

**Needs:** nothing

### EXT-032: Web tool that diffs two OpenAPI specs into a breaking-change report

**Scores:** $:3 CV:4 VIR:3 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Drop two spec versions; get a change list classified as breaking, non-breaking, or additive under real rules, removed endpoint, narrowed enum, required request field added, response field removed, type change, auth scheme change, default changed, with a plain-English migration note per breaking change and a copyable changelog section. Also emits an exit-code-friendly JSON so it can run in CI. Done when it agrees with a hand-reviewed diff of two real published API versions.

**Needs:** nothing

### EXT-033: Web tool that makes any video fit a platform's upload limit

**Scores:** $:2 CV:3 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Drop a video; pick Discord 10MB, X, Bluesky, or a custom cap. Uses ffmpeg.wasm entirely in the tab to trim with a scrub-and-set-in/out UI, then solves for the bitrate that lands just under the cap at the best quality, applies two-pass where it helps, and optionally burns in captions generated by transformers.js Whisper. Never uploads the video. Done when a 400MB screen recording becomes a 9.6MB Discord-ready clip without leaving the browser.

**Needs:** nothing

### EXT-034: Web tool that converts EPUB to clean markdown

**Scores:** $:2 CV:2 VIR:2 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Existing converters produce markdown littered with span soup, broken footnotes, and lost chapter structure. Parse the EPUB container properly, follow the spine for true reading order, convert footnotes into proper markdown reference footnotes, extract and re-link images, preserve blockquote and code semantics, and emit either one file or one per chapter with frontmatter. Client-side. Done when a technical EPUB round-trips with code blocks intact.

**Needs:** nothing

### EXT-035: Extension that finds the legal open-access version of a paywalled paper

**Scores:** $:2 CV:3 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

On any DOI or publisher page, query the Unpaywall and OpenAlex APIs for a legally-deposited open-access copy, author preprint, institutional repository, arXiv version, PMC, and show a badge with the license and version (preprint vs accepted vs published). Also detects when the venue is fully open access and the paywall is a mirage. Strictly legitimate repositories only. Done when it resolves a majority of a real reading list.

**Needs:** an Unpaywall API email registration (free)

### EXT-037: Extension that records a research trail and writes the cited report

**Scores:** $:4 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Hit record; browse normally. It captures each page's canonical URL, title, the passages you selected, and time on page, then at stop produces a structured report, question, what was found, what conflicts between sources, what remains unanswered, with every sentence footnoted to the specific page and passage it came from. All local. This is the honest version of "deep research": a human did the browsing, the model only organizes and cites. Done when a two-hour session yields a report whose citations all verify.

**Needs:** nothing

### EXT-038: Extension that fills tedious web forms from a local encrypted profile

**Scores:** $:4 CV:4 VIR:4 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Browser autofill handles addresses and dies on everything else, job applications, school registration, insurance intake, conference CFPs. Keep a rich structured profile (work history, education, EIN, emergency contacts, medical basics) encrypted at rest with a passphrase, and use a local model to map arbitrary form fields to profile entries by label, placeholder, and surrounding text, including free-text fields that need a short generated answer from profile facts. Always shows a review diff before submit and never auto-submits. Done when it fills a real 40-field job application in one pass.

**Needs:** nothing (deliberately does not touch browser-saved credentials, per the resource audit)

### EXT-039: Build an offline voice-memo-to-notes PWA

**Scores:** $:3 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Installable PWA that records audio, transcribes with Whisper via transformers.js and WebGPU entirely on-device, and structures the result into a titled note with extracted action items and dates, works on a phone in airplane mode after first load. Stores in IndexedDB with an export to markdown. The technical achievement is real on-device ASR with no server, which is also the entire privacy pitch. Done when it transcribes a five-minute memo on an Android phone with no network.

**Needs:** nothing (model weights cached from Hugging Face on first run)

### EXT-040: Build a DevTools panel that explains why a style won

**Scores:** $:3 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** L | **Repo:** public

DevTools shows the losing rules struck through and expects you to infer the rest. This panel takes one element and one property and explains the outcome as a ranked narrative: the cascade layer, origin, specificity tuple, source order, `!important`, inheritance chain, and, the hard part, which containing block, stacking context, and formatting context actually govern the layout properties, since "why is this `position: fixed` element not fixed to the viewport" is the question DevTools cannot answer. Done when it correctly explains a transform-created containing block trapping a fixed child.

**Needs:** nothing

### EXT-042: Build a page performance triage tool that explains itself

**Scores:** $:3 CV:5 VIR:4 USE:4 ALT:5 | **Effort:** L | **Repo:** public

Run a real navigation with the Performance and Resource Timing APIs plus long-animation-frame observation, then produce an annotated waterfall where each annotation is causal rather than descriptive: "LCP is 4.1s because the hero image is discovered by a lazy-loaded script that itself waits on a render-blocking stylesheet from a third-party origin with no preconnect." The model's job is the causal chain, not the numbers. Done when its diagnosis on three real sites matches what an experienced performance engineer would say.

**Needs:** nothing

### EXT-043: Build a jargon decoder for documents you read in the browser

**Scores:** $:4 CV:4 VIR:4 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Reading a lease, an EOB, a school IEP, or a consent form in a browser PDF viewer, you get a margin rail: every term of art annotated with what it means and, more importantly, what it means *for you* given a few facts you supply. Also flags the clauses that are unusual relative to a corpus of that document type, the point is not defining "indemnify", it is noticing that this indemnity clause is one-sided. Entirely local, since these documents are private. Done when it flags a genuinely unusual clause in a real lease.

**Needs:** a corpus of standard-form documents per type to establish the baseline

### EXT-044: Build an offline Liturgy of the Hours PWA

**Scores:** $:2 CV:3 VIR:3 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Existing breviary apps are cluttered, ad-supported, or online-only. Build an installable PWA that assembles the correct office for the current hour and liturgical day, works fully offline after install, offers a distraction-free typographic reading view with a night mode that does not destroy dark adaptation, and supports antiphon/psalm audio. Rubrical correctness is the whole product, a breviary that puts you in the wrong week is worthless. Done when it matches a printed breviary for a full liturgical season including feasts.

**Needs:** a public-domain or properly-licensed psalter and office text (Grail translations are copyrighted, use a licensed or public-domain text and document the choice)

### EXT-045: Build a real-estate listing overlay

**Scores:** $:3 CV:3 VIR:4 USE:4 ALT:5 | **Effort:** L | **Repo:** public

On any listing page, inject the facts the listing omits, pulled from free public sources: FEMA flood zone, county assessor tax history and assessed-to-list ratio, the actual school attendance boundary rather than the marketing claim, drive time to addresses you configure at the hours you configure, radon zone, wildfire risk, broadband availability by provider from the FCC map, and a fifteen-year sale history. Done when it surfaces a flood zone the listing does not mention.

**Needs:** nothing (FEMA, FCC, and most county assessors publish free APIs or open data; DOM injection on pages the user opened)

### EXT-046: Build a full local-agent sidebar extension

**Scores:** $:4 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** XL | **Repo:** public

An MV3 extension (Chrome and Firefox from one codebase) with a sidebar agent that runs a real tool-use loop against local Ollama, with tools that act on the browser: read the page as clean markdown, click and type in the page, open and read other tabs, search the user's history and bookmarks, fill a form, extract a table. Includes a permission prompt per tool class, a visible action log, and a hard stop. The hard parts are MV3 service-worker lifecycle, streaming from localhost under CSP, and making a 30B model reliable at multi-step tool use. Done when it completes a real five-step task like "find the cheapest of these three items across the tabs I have open and put the winner in a note."

**Needs:** `OLLAMA_ORIGINS` allowing the extension; careful review of what page access is granted

### EXT-047: Build private semantic search over your own browsing history

**Scores:** $:4 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** XL | **Repo:** public

Browser history search matches titles and URLs, so the page you remember reading but cannot name is lost forever. Embed the full text of every page visited (with a per-site allow/deny policy and automatic exclusion of anything behind auth by default), store vectors in a local IndexedDB or SQLite-wasm index, and answer natural-language queries: "that post about MoE routing collapse I read in March." Everything on-device. The hard parts are storage budget over months, incremental re-embedding, and not indexing bank statements. Done when it retrieves a page from memory that title search cannot.

**Needs:** disk budget planning; an embedding model in Ollama

### EXT-048: Build a self-hosted web clipper and knowledge base PWA

**Scores:** $:4 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** XL | **Repo:** public

The extension clips a page to durable clean markdown with a snapshot of images; the PWA is the reader, organizer, and search over everything clipped, with full-text and semantic search, backlinks, tags inferred locally, and a sync layer against a Neon Postgres the user owns. The thing Pocket and Readwise cannot offer is that the store is yours and the intelligence is local. Done when a year of clips is searchable offline on a phone and the sync survives a conflicting edit on two devices.

**Needs:** Neon Postgres (via Vercel marketplace); Vercel deploy

### EXT-049: Build a visual scraper builder that compiles to Playwright

**Scores:** $:4 CV:5 VIR:5 USE:5 ALT:4 | **Effort:** XL | **Repo:** public

Point and click at elements on a page to define a schema; the extension infers robust selectors (preferring stable attributes and text anchors over brittle nth-child chains), detects the repeating container, handles pagination and infinite scroll by observation, and then compiles the whole thing to a readable, checked-in Playwright script, not a hosted black box. Refuses to build against a site whose robots.txt disallows the path, and includes a rate limiter by default. Done when a generated script survives a minor redesign of the target page.

**Needs:** nothing

### EXT-050: Build an in-browser local-model playground on WebGPU

**Scores:** $:4 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** XL | **Repo:** public

A single page where a visitor with a modern GPU runs real models entirely in their tab via transformers.js and WebGPU, a curated zoo of small instruct, embedding, ASR, and vision models with honest VRAM and first-load-size numbers, side-by-side comparison of two models on the same prompt, a token-probability inspector, and a shareable permalink that encodes the prompt and settings but never the data. The demo value is enormous because most people have never seen a model run with the network tab empty. Done when a mid-range laptop runs a 1B instruct model at readable speed and the page honestly says which devices cannot.

**Needs:** hosting for model weights (Hugging Face serves them with CORS); Vercel for the page

