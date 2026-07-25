# Content & Media Generation Engines

Repeatable pipelines that produce publishable media at volume, each with a quality gate that can reject its own output.

### MEDIA-001: Build a reusable editorial rubric grader

**Scores:** $:2 CV:4 VIR:2 USE:5 ALT:4 | **Effort:** M | **Repo:** public

A TypeScript library that scores a draft against a declarative YAML rubric (accuracy, specificity, source density, redundancy, reading level) using `gemma4:31b-it-q4_K_M` as judge with per-criterion few-shot anchors, returning a structured verdict plus line-level annotations. Every other engine in this file imports it as its gate; done means a `grade(draft, rubric)` call that fails CI when any criterion drops below threshold.

**Needs:** nothing

### MEDIA-003: Write a claim-to-source provenance linter

**Scores:** $:2 CV:4 VIR:3 USE:5 ALT:5 | **Effort:** S | **Repo:** public

A linter that walks a markdown draft, extracts every factual assertion with `qwen3.6:27b`, and fails the build for any assertion lacking a resolvable citation anchor in the document's source manifest. Output is a coverage report showing what fraction of claims are sourced, which becomes a published stat on every artifact.

**Needs:** nothing

### MEDIA-004: Build an NLI entailment fact-check stage

**Scores:** $:3 CV:5 VIR:3 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Given a draft and the raw source documents it was written from, chunk the sources, retrieve top-k evidence per claim with a local embedding model, and run a natural language inference pass that labels each claim entailed, contradicted, or unsupported. Ship it as a pipeline stage that blocks publication on any contradiction and surfaces unsupported claims for rewrite.

**Needs:** nothing

### MEDIA-005: Compile a house style guide into machine-checkable rules

**Scores:** $:1 CV:3 VIR:1 USE:5 ALT:3 | **Effort:** S | **Repo:** public

Turn a prose style guide into a compiled artifact: deterministic regex/AST rules for the mechanical parts (no em dashes, no antithetical parallelism, serial comma, sentence length ceiling) plus a model-graded section for tone. Done means `stylec build guide.md` emits a rule bundle every engine can load.

**Needs:** nothing

### MEDIA-006: Ship an errata and correction republish workflow

**Scores:** $:1 CV:4 VIR:3 USE:4 ALT:5 | **Effort:** S | **Repo:** public

When a published piece is corrected, the tool writes a dated correction note, regenerates the artifact, and produces a public diff page showing exactly what changed and why. Correct-in-public is the credibility mechanism that separates an honest engine from a content farm, so make the diff the default view.

**Needs:** nothing

### MEDIA-008: Create a GitHub Actions media publishing pipeline

**Scores:** $:2 CV:5 VIR:2 USE:5 ALT:4 | **Effort:** M | **Repo:** public

A reusable workflow that takes a content repo, runs the rubric grader and slop detector, renders every output format with ffmpeg and a headless browser, uploads artifacts, and publishes only on a green gate. Includes a matrix strategy so a single source document fans out to newsletter HTML, RSS, MP3, and a static page in one run.

**Needs:** nothing

### MEDIA-009: Build an embedding-dedupe digest core

**Scores:** $:2 CV:3 VIR:2 USE:5 ALT:4 | **Effort:** S | **Repo:** public

The shared front half of every newsletter engine: pull N RSS/Atom feeds, embed each item, cluster near-duplicates so eight outlets covering one story become one entry with eight links, and rank clusters by cross-source agreement rather than recency. Done means a library call that returns deduped, ranked story clusters from a feed list.

**Needs:** nothing

### MEDIA-010: Build a local-model release newsletter that benchmarks before it writes

**Scores:** $:4 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** XL | **Repo:** public

A weekly newsletter engine that watches Hugging Face model releases, automatically pulls any model under a VRAM/disk budget, runs a fixed private eval suite on the 5090, and writes the issue from measured numbers instead of the release card's claims. The differentiator is that every issue ships a reproducible results table and the eval harness is public, so readers can rerun it.

**Needs:** a newsletter delivery service (Buttondown or Listmonk self-hosted) and disk headroom for rotating model downloads

### MEDIA-013: Build a "this week in your repos" digest for OSS maintainers

**Scores:** $:4 CV:4 VIR:4 USE:4 ALT:5 | **Effort:** M | **Repo:** public

A GitHub App or `gh`-driven script that summarizes a maintainer's week across all their repos: new issues triaged by likely-duplicate clustering, stalled PRs, first-time contributors who got no reply, and dependency advisories. Ships as a subscribable weekly email with a free tier for one repo.

**Needs:** a GitHub App registration if it goes multi-user; the `gh` CLI covers single-user

### MEDIA-014: Build a plain-English SEC filing digest engine

**Scores:** $:5 CV:5 VIR:4 USE:3 ALT:5 | **Effort:** L | **Repo:** public

Pull 8-K and 10-Q filings from EDGAR's public API for a watchlist, diff each against the prior period's language to find what actually changed (risk factor edits, segment reclassifications, auditor changes), and publish a short issue per filing that quotes the changed text verbatim before summarizing. The diff-first approach is the honest version of financial content and is hard to fake.

**Needs:** nothing (EDGAR is public and rate-limited by user-agent policy, which the client must honor)

### MEDIA-015: Build privacy-preserving newsletter analytics

**Scores:** $:3 CV:4 VIR:4 USE:4 ALT:5 | **Effort:** S | **Repo:** public

Replace tracking pixels and link wrappers with an opt-in feedback footer, aggregate-only link counts with no per-subscriber identity, and a public dashboard showing what the publisher can and cannot see. Publishing the threat model alongside the code is the point.

**Needs:** nothing

### MEDIA-016: Build a newsletter-to-podcast conversion stage

**Scores:** $:3 CV:4 VIR:3 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Take the canonical markdown for any issue, rewrite it for the ear (expand abbreviations, unroll tables into spoken prose, drop link text), render with a local TTS model, and emit a tagged MP3 plus a podcast RSS entry with chapters. The rewrite stage runs through the rubric grader so the audio version cannot drift from the text version's claims.

**Needs:** nothing

### MEDIA-017: Build a two-model adversarial paper podcast

**Scores:** $:3 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** L | **Repo:** public

An episode engine where `qwen3.6:27b` argues a paper's contribution and `gemma4:31b-it-q4_K_M` argues its limitations, with a third pass that fact-checks both against the paper text and cuts any claim the paper does not support. Render each speaker with a distinct local TTS voice and publish the full unedited transcript with the checked claims marked.

**Needs:** nothing

### MEDIA-018: Build a repo-history narrative podcast engine

**Scores:** $:2 CV:4 VIR:4 USE:3 ALT:4 | **Effort:** M | **Repo:** public

Given any public repo, mine the commit graph, issue threads, and release notes to reconstruct the story of how a major feature came to exist, including the abandoned approaches visible in reverted commits. Output is a 10-15 minute narrated episode with every assertion linked to a commit SHA.

**Needs:** nothing

### MEDIA-019: Build a show-notes, chapter, and transcript pipeline

**Scores:** $:4 CV:4 VIR:3 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Drop an audio file in, get back a diarized transcript (whisper.cpp or faster-whisper on the 5090), semantic chapter markers written into the MP3's ID3 tags, a linked show-notes page, and pull quotes with timestamps. Include a correction pass where named entities are checked against a user-supplied glossary so guest names and product names never come out mangled.

**Needs:** nothing

### MEDIA-020: Build a podcast trailer cutter

**Scores:** $:3 CV:3 VIR:3 USE:3 ALT:4 | **Effort:** S | **Repo:** public

From a finished episode plus its transcript, select three to five high-information segments (scored for standalone comprehensibility, not just enthusiasm), cut them with ffmpeg at zero-crossing boundaries, and assemble a 60-second trailer with beds and a spoken outro. Rejecting clips that need context to make sense is the quality gate.

**Needs:** nothing

### MEDIA-021: Build a multi-voice audio drama engine

**Scores:** $:4 CV:5 VIR:5 USE:4 ALT:4 | **Effort:** L | **Repo:** public

A pipeline that takes a screenplay-format script, assigns a consistent local TTS voice per character, renders lines individually, and mixes with per-scene ambience and spatial panning driven by stage directions in the script. Done means a 20-minute original episode that a listener can follow without seeing the script.

**Needs:** nothing

### MEDIA-022: Build a Project Gutenberg audiobook factory

**Scores:** $:4 CV:5 VIR:4 USE:4 ALT:5 | **Effort:** XL | **Repo:** public

An end-to-end engine that takes a public-domain text, cleans the Gutenberg boilerplate, resolves structure into chapters, builds a per-book pronunciation lexicon for proper nouns and archaic words (with a human review pass on the lexicon only), renders chapter audio locally, and packages an M4B with chapter marks and cover art. Contribute finished readings back to LibriVox-adjacent public archives and publish the lexicons as reusable datasets.

**Needs:** substantial disk for rendered audio; an archive.org account if uploading finished books

### MEDIA-023: Build a consistent narrator voice bank

**Scores:** $:3 CV:4 VIR:3 USE:5 ALT:4 | **Effort:** M | **Repo:** public

Evaluate the open TTS options that fit on a 5090 (Kokoro, XTTS-v2, Piper, F5-TTS), pick three house voices, and lock each one behind a version-pinned config with a regression suite of reference phrases so a model upgrade cannot silently change how the show sounds. Only use voices from models whose licenses permit it, and never clone a real person's voice without their written consent.

**Needs:** nothing

### MEDIA-024: Build a multi-language dub pipeline

**Scores:** $:4 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Take an existing English video, transcribe with timestamps, translate to Japanese, Spanish, and Brazilian Portuguese with `gemma4:31b-it-q4_K_M`, render TTS per language, and time-fit each segment to the original with ffmpeg's atempo so lip-adjacent timing stays plausible. Include a back-translation check that flags any segment whose meaning drifted before it gets rendered.

**Needs:** nothing

### MEDIA-025: Build a Manim explainer shorts engine

**Scores:** $:4 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** XL | **Repo:** public

A pipeline that turns a single mathematical or physical claim into a 60-second vertical animation: `qwen3-coder:30b` writes the Manim scene, a render-and-inspect loop uses a vision model to catch off-screen elements and overlapping labels, and the narration is generated from the same scene spec so audio and visuals cannot desync. Done means ten published shorts produced with no manual keyframing.

**Needs:** nothing

### MEDIA-026: Build a screencast auto-editor

**Scores:** $:4 CV:4 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Given a raw screen recording, detect and cut silence, detect typing bursts and speed them up, auto-zoom toward cursor activity with smooth easing, and emit an EDL alongside the rendered MP4 so the edit can be inspected and adjusted. All of it runs locally with ffmpeg and OpenCV, which is the selling point against the paid cloud tools.

**Needs:** nothing

### MEDIA-027: Build a repo-to-architecture-walkthrough video engine

**Scores:** $:4 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Point it at a repo and it produces a narrated walkthrough: a generated dependency graph that animates as each module is discussed, real code on screen with syntax highlighting and scroll-to-line, and narration written from actual call-graph traversal rather than from the README. The gate is that every claim about what a function does must resolve to a real symbol in the repo.

**Needs:** nothing

### MEDIA-028: Build a whiteboard animation engine

**Scores:** $:4 CV:4 VIR:4 USE:3 ALT:4 | **Effort:** M | **Repo:** public

Convert an outline into SVG line art, then animate stroke-by-stroke drawing by animating `stroke-dashoffset` along each path in draw order, synced to narration timing. Ships as a Node library that emits frames for ffmpeg, with a hand-and-marker overlay layer that follows the active path tip.

**Needs:** nothing

### MEDIA-029: Build a public-domain archival micro-documentary engine

**Scores:** $:3 CV:5 VIR:5 USE:3 ALT:5 | **Effort:** L | **Repo:** public

Search the Internet Archive and Library of Congress public APIs for verified public-domain footage on a topic, assemble a shot list, write narration grounded in cited primary sources, and cut a five-minute documentary with an on-screen citation for every clip and claim. Rights verification is a hard gate: no clip enters the timeline without a recorded rights determination.

**Needs:** nothing

### MEDIA-030: Build a changelog-to-release-video engine

**Scores:** $:4 CV:4 VIR:3 USE:4 ALT:5 | **Effort:** M | **Repo:** public

On tag push, read the changelog and the diff, generate a 45-second vertical video showing each headline change as animated code diff cards with narration, and attach it to the GitHub release. Useful to any OSS project and trivially demoable, which is what makes it spread.

**Needs:** nothing

### MEDIA-031: Build a deterministic SVG infographic engine

**Scores:** $:4 CV:5 VIR:4 USE:4 ALT:5 | **Effort:** M | **Repo:** public

A layout engine where the model produces a typed data spec and a constraint solver produces the geometry, so text never overflows, labels never collide, and the same input always renders the same SVG. Generating layout code with an LLM and hoping is what produces broken infographics, so the model here is confined to content and never touches coordinates.

**Needs:** nothing

### MEDIA-032: Build a Wikidata timeline infographic engine

**Scores:** $:3 CV:4 VIR:4 USE:3 ALT:5 | **Effort:** M | **Repo:** public

Query Wikidata via SPARQL for events matching a topic, resolve date precision and disputed dates honestly (showing ranges rather than false certainty), and render a print-quality timeline with source links per entry. Handling uncertain dates correctly is the feature nobody else implements.

**Needs:** nothing

### MEDIA-033: Build a public-dataset data-journalism engine

**Scores:** $:4 CV:5 VIR:5 USE:3 ALT:5 | **Effort:** XL | **Repo:** public

A pipeline over BLS, Census, CDC WONDER, and FRED APIs that detects statistically notable changes in tracked series, runs a scripted analysis (seasonal adjustment, base-rate check, small-sample suppression), and publishes a story only when the finding survives a pre-registered significance and effect-size gate. Every story ships with its notebook, its data snapshot, and an explicit list of what the data cannot show.

**Needs:** free API keys for BLS and FRED

### MEDIA-034: Build a screenshot-to-annotated-carousel tool

**Scores:** $:3 CV:3 VIR:3 USE:4 ALT:4 | **Effort:** S | **Repo:** public

Feed it a folder of screenshots and a short outline; it crops to salient regions with saliency detection, adds numbered callouts and consistent typography, and emits a slide sequence sized for LinkedIn, plus a single tall image for blogs. Ships as a CLI with a theme file so all output looks like one publication.

**Needs:** nothing

### MEDIA-035: Build a scrollytelling article generator

**Scores:** $:4 CV:5 VIR:5 USE:3 ALT:5 | **Effort:** L | **Repo:** public

From a structured story spec (narrative beats plus a dataset), generate a Next.js page where scroll position drives a pinned visualization through states, with a static fallback that works with JavaScript off and a print stylesheet that produces a readable PDF. Accessibility is a gate: keyboard navigation and reduced-motion paths must pass automated checks before publish.

**Needs:** nothing

### MEDIA-036: Build a daily Minecraft swarm comic strip engine

**Scores:** $:2 CV:4 VIR:5 USE:5 ALT:3 | **Effort:** L | **Repo:** public

Mine the mineflayer swarm's event log for the day's most narratively interesting sequence, script a three-to-four-panel strip, render panels from in-game screenshots captured at the actual coordinates where events happened, and letter it with a comic layout engine. The strip is true to the logs, which makes it funnier than invented content and doubles as a swarm observability tool.

**Needs:** nothing

### MEDIA-038: Build a print-ready zine generator

**Scores:** $:3 CV:3 VIR:4 USE:3 ALT:4 | **Effort:** S | **Repo:** public

Take a collection of articles and emit a LaTeX-built PDF imposed for saddle-stitch printing, with correct page ordering for folding, bleed marks, and a generated table of contents and colophon. Include an eight-page single-sheet mini-zine imposition mode because that is the format people actually print at home.

**Needs:** nothing

### MEDIA-039: Build a themed puzzle generator for newsletter issues

**Scores:** $:3 CV:4 VIR:4 USE:3 ALT:4 | **Effort:** M | **Repo:** public

Generate a small crossword or cryptogram whose answers are drawn from the issue's own vocabulary, using a real constraint-satisfaction grid filler with a curated word list rather than asking a model to place letters. Emits interactive HTML plus a print version and validates that every clue has exactly one consistent solution.

**Needs:** nothing

### MEDIA-040: Build a graded-reader generator for language learning

**Scores:** $:5 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Generate original short stories in Japanese, Spanish, and Brazilian Portuguese constrained to a learner's known-vocabulary set plus exactly N new words, with the new words introduced in inferable contexts, furigana or IPA where relevant, and audio rendered per sentence. The gate is a vocabulary linter that rejects any story exceeding the budget, which is what makes it a real graded reader instead of generic AI text.

**Needs:** a frequency list and vocabulary source per language (JMdict, Frequency lists from OpenSubtitles corpora)

### MEDIA-042: Build a lecture-video-to-study-guide pipeline

**Scores:** $:4 CV:4 VIR:3 USE:4 ALT:5 | **Effort:** M | **Repo:** public

From any lecture recording, produce a chaptered study guide with timestamped section summaries, extracted definitions, generated practice questions tied to timestamps, and a spaced-repetition deck in Anki's APKG format. Every generated question links back to the exact moment in the video that answers it.

**Needs:** nothing

### MEDIA-043: Build a book-to-course engine

**Scores:** $:5 CV:5 VIR:4 USE:4 ALT:5 | **Effort:** XL | **Repo:** public

Turn a technical book or long documentation set into a structured course: dependency-ordered lesson graph derived from concept prerequisites, per-lesson exercises with automated checking, and a progress-aware review scheduler. Build it first against a public-domain or openly-licensed text so the output can be published, and make the course spec format the actual deliverable.

**Needs:** an openly-licensed source text for the reference course

### MEDIA-045: Build the agent fleet's daily shipping digest

**Scores:** $:1 CV:3 VIR:3 USE:5 ALT:3 | **Effort:** S | **Repo:** public

Every night, read the fleet's run logs, git activity across `~/Projects`, and task state, then publish a one-page digest of what actually shipped, what failed and why, and what is blocked on a credential. Sent to Discord and archived as a dated markdown file so the fleet has a memory it did not write about itself in the moment.

**Needs:** nothing

### MEDIA-046: Build a one-source-to-many-formats repurposer

**Scores:** $:4 CV:4 VIR:3 USE:5 ALT:5 | **Effort:** S | **Repo:** public

A single canonical document compiles to newsletter HTML, RSS, a podcast script, a vertical video storyboard, a carousel, and a plain-text version, with per-format transforms declared in config rather than done by re-prompting. Formats that would require inventing facts not present in the source fail loudly instead of hallucinating filler.

**Needs:** nothing

### MEDIA-047: Build a per-artifact cost and latency accountant

**Scores:** $:3 CV:4 VIR:2 USE:5 ALT:4 | **Effort:** S | **Repo:** public

Instrument every pipeline stage to record tokens, wall time, GPU seconds, and estimated dollar cost, then emit a per-artifact receipt and a rolling dashboard showing cost per published piece by medium. This is how the engines get chosen for real work instead of vibes.

**Needs:** nothing

### MEDIA-048: Build a signed asset provenance manifest

**Scores:** $:3 CV:5 VIR:4 USE:4 ALT:5 | **Effort:** M | **Repo:** public

For every published artifact, emit a signed manifest listing source documents with hashes, models and versions used per stage, human approval events, and the gate results, then embed a C2PA-compatible assertion in images and audio where the format supports it. Publish a verifier page where anyone can drop an artifact and see its production history.

**Needs:** nothing

### MEDIA-049: Build a voice-and-tone drift monitor for a back catalog

**Scores:** $:3 CV:4 VIR:3 USE:4 ALT:4 | **Effort:** S | **Repo:** public

Embed every past issue, track stylometric features over time (sentence length distribution, hedge density, first-person rate, vocabulary novelty), and alert when a new draft sits outside the historical envelope. Catches the slow slide toward model-default prose that nobody notices issue to issue.

**Needs:** nothing

### MEDIA-050: Build a dry-run preview server for media pipelines

**Scores:** $:2 CV:4 VIR:2 USE:5 ALT:4 | **Effort:** S | **Repo:** public

A local web server that renders every output format of a pending artifact side by side, including the email client rendering via a static HTML sanitizer preview, the podcast player view, and the mobile video crop, with the gate results shown inline. One command, one URL, everything a publish decision needs on one screen.

**Needs:** nothing

