# Health, Fitness & Medical Information

Evidence-graded information tooling, self-tracking, and accessibility aids. Every entry retrieves, grades, or records, none of it diagnoses, prescribes, or substitutes for a clinician, and every deliverable carries that framing in the UI, not just the README.

### HLTH-002: Study quality card generator

**Scores:** $:4 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Paste a PMID and get a structured risk-of-bias card: design, randomization, allocation concealment, blinding, attrition, pre-registration status, primary vs reported outcome mismatch, and funding. Every field is extractive, it quotes the sentence it came from or reports `not stated`, and the model is forbidden from inferring. Done when it matches a human Cochrane RoB-2 assessment on 20 papers or abstains.

**Needs:** nothing

### HLTH-004: Claim-to-source verifier for health articles

**Scores:** $:4 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Give it a wellness article URL; it extracts each health claim, fetches the studies the article cites, and reports whether the cited paper actually supports the claim, contradicts it, is about a different population, or was never about humans. Output is a per-claim verdict with the supporting quote or an explicit "cannot verify." Done when it correctly flags the classic mouse-study-reported-as-human-finding pattern.

**Needs:** nothing

### HLTH-006: Pill imprint lookup

**Scores:** $:2 CV:3 VIR:3 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Enter an imprint code, shape, and color and get candidate matches from the DailyMed/NDC open data with images where available. Strictly a database query with ranked candidates and a hard rule that a single match is still shown as "candidate, confirm with a pharmacist." Done when it returns the right candidate set for 20 common tablets and abstains on ambiguous imprints.

**Needs:** nothing

### HLTH-008: Caffeine and sleep pressure calculator

**Scores:** $:2 CV:3 VIR:4 USE:5 ALT:5 | **Effort:** S | **Repo:** public

Log your caffeine intake times and doses; the page plots the pharmacokinetic decay curve against your target bedtime using published half-life ranges (with the CYP1A2 variability band shown, not hidden). Pure deterministic math over cited parameters. Done when the plot shows the range, not a false point estimate.

**Needs:** nothing

### HLTH-010: Lab abbreviation glossary from LOINC

**Scores:** $:1 CV:3 VIR:2 USE:4 ALT:5 | **Effort:** S | **Repo:** public

A fast offline lookup that turns the cryptic codes on a lab report into the LOINC long common name, specimen, and property, sourced from the official LOINC release. Definition only, never significance. Done when it resolves everything on a standard CMP and CBC panel.

**Needs:** free LOINC account for the data download (registration required, no cost).

### HLTH-012: N-of-1 self-experiment platform

**Scores:** $:4 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** XL | **Repo:** public

Design and run proper single-subject crossover trials on yourself: define an intervention and an outcome measure, the tool generates a randomized, blinded-where-possible block schedule with washout periods, prompts daily measurement, and analyzes with the right method for autocorrelated within-subject data rather than a naive t-test. Ships with a pre-registration file written before unblinding. Done when a run produces an effect estimate with an honest interval, including "underpowered, inconclusive."

**Needs:** nothing

### HLTH-013: FoodData Central local mirror and recipe calculator

**Scores:** $:3 CV:4 VIR:3 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Mirror the USDA FoodData Central release into local SQLite with full-text search, then build a recipe calculator that resolves ingredients to food codes and computes per-serving nutrients with the source food ID shown for every line. No dietary advice, just arithmetic over a government dataset. Done when a real recipe's totals are reproducible and traceable.

**Needs:** ~5 GB disk for the full FDC release.

### HLTH-014: Macro-target meal plan solver

**Scores:** $:3 CV:5 VIR:4 USE:5 ALT:4 | **Effort:** M | **Repo:** public

Given macro and micronutrient targets that the user sets themselves (or copies from their clinician), solve for a week of meals from a pantry of foods using linear programming over the FDC data, with hard constraints for allergies and dislikes. It optimizes to targets you supply; it never sets targets for you. Done when the LP returns a feasible, non-absurd week and reports which constraints bind.

**Needs:** nothing

### HLTH-015: Nutrition label normalizer

**Scores:** $:2 CV:2 VIR:3 USE:4 ALT:5 | **Effort:** S | **Repo:** public

Photograph a nutrition facts panel; OCR it and restate everything per 100 g, per serving, and per container side by side, so the "servings per container: 2.5" trick stops working. Flag when the OCR confidence is low rather than guessing a digit. Done when it handles the US and EU label formats.

**Needs:** nothing

### HLTH-016: Recall alerts against your grocery list

**Scores:** $:2 CV:3 VIR:3 USE:5 ALT:5 | **Effort:** S | **Repo:** public

Poll the FDA and USDA FSIS recall feeds, match against a user-maintained list of brands and products, and push a notification when something in your kitchen is recalled, quoting the official recall notice verbatim with its link. Done when a backfill test against last year's recalls fires the right matches.

**Needs:** nothing

### HLTH-017: Strength log with honest progression math

**Scores:** $:3 CV:4 VIR:3 USE:5 ALT:5 | **Effort:** M | **Repo:** public

A lifting log that computes estimated 1RM with several published formulas shown as a spread rather than one confident number, tracks tonnage and set-volume per muscle group, and charts stall detection as a plain statement of the data. It reports what you did; it does not program for you. Done when a 12-week block renders as one readable page.

**Needs:** nothing

### HLTH-018: Rep and tempo counter from webcam pose

**Scores:** $:3 CV:5 VIR:5 USE:4 ALT:4 | **Effort:** L | **Repo:** public

Run MediaPipe pose in the browser to count reps and measure concentric/eccentric tempo and range-of-motion consistency across a set, charting fatigue as velocity decay. Deliberately scoped to measurement only, it never corrects form, because form correction from a single uncalibrated camera is exactly the case where a wrong answer causes injury. Done when rep counts match a manual count on 20 sets.

**Needs:** a webcam (built-in is fine).

### HLTH-019: Cited training program library

**Scores:** $:3 CV:4 VIR:3 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Encode a dozen published training programs as structured data (sets, reps, intensity progression, deload logic) with each one linked to its primary source and a note on what population it was studied in. The tool renders and tracks a chosen program; it does not recommend one. Done when programs render as week-by-week schedules and the citations resolve.

**Needs:** nothing

### HLTH-021: Noise dosimeter against NIOSH limits

**Scores:** $:2 CV:4 VIR:4 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Use the laptop or phone mic to log A-weighted sound levels over a day and compute cumulative dose against the published NIOSH exposure limits, with a prominent uncalibrated-microphone caveat and an optional single-point calibration step. Done when a loud environment produces a dose curve and the uncertainty band is shown, not hidden.

**Needs:** nothing

### HLTH-023: Clinical guideline version diff tracker

**Scores:** $:4 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** L | **Repo:** public

Snapshot published recommendation documents (USPSTF, ACIP, and similar public-domain US federal guidance) on a schedule and render a readable diff when a recommendation grade or age threshold changes. Pure documentary tooling: it shows what the guideline says now versus before, with dates. Done when it correctly surfaces a real historical change such as a screening age revision.

**Needs:** nothing

### HLTH-024: Trial finder with quoted eligibility

**Scores:** $:3 CV:4 VIR:3 USE:3 ALT:5 | **Effort:** M | **Repo:** public

A friendlier front end over the ClinicalTrials.gov API: filter recruiting trials by condition and distance, and render eligibility criteria as a structured checklist where every line is the verbatim criterion text with a plain-language gloss beneath it. Never computes whether you qualify, that is the trial coordinator's job, and the UI says so. Done when a search returns usable results with working contact info.

**Needs:** nothing

### HLTH-025: FAERS disproportionality explorer, done honestly

**Scores:** $:3 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** L | **Repo:** public

Query openFDA adverse event reports and compute PRR and ROR correctly, then spend as much of the interface on the caveats as on the numbers: reporting bias, no denominator, stimulated reporting after media coverage, and the fact that a signal is a hypothesis and not a causal finding. Include a demo showing a spurious signal produced by a news cycle. Done when the page teaches why the number cannot mean what people want it to mean.

**Needs:** nothing

### HLTH-026: Drug shortage watcher

**Scores:** $:2 CV:3 VIR:2 USE:4 ALT:5 | **Effort:** S | **Repo:** public

Track the FDA drug shortage database for a watchlist of medications and notify on status changes, quoting the official reason and estimated resolution. Useful precisely because the FDA site is hard to monitor manually. Done when a status change on any watched drug produces a notification within a day.

**Needs:** nothing

### HLTH-027: Generic price comparison from NADAC

**Scores:** $:3 CV:4 VIR:4 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Load the CMS National Average Drug Acquisition Cost dataset and let a user look up what pharmacies actually pay for a generic, next to the retail price they were quoted. Includes a therapeutic-equivalent view via RxNorm so the "ask about the other strength" conversation becomes possible. Done when a common generic shows acquisition cost, retail spread, and the data vintage.

**Needs:** nothing

### HLTH-028: Hospital price transparency parser

**Scores:** $:4 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** L | **Repo:** public

Hospitals are required to publish machine-readable standard-charge files, and they are a mess of inconsistent schemas. Build a normalizer that ingests the files for hospitals in a metro area and produces a comparable table of cash prices and negotiated rates by CPT code. Done when three hospitals' files normalize into one queryable table with provenance per row.

**Needs:** nothing

### HLTH-030: CPT lookup with Medicare reference pricing

**Scores:** $:3 CV:4 VIR:4 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Look up a procedure code from a bill and see its official descriptor plus the Medicare Physician Fee Schedule amount for your locality as a reference point. Pairs with the EOB parser to answer "is this bill in a normal range." Done when a real bill's line items all resolve.

**Needs:** nothing

### HLTH-031: Part D formulary checker

**Scores:** $:3 CV:4 VIR:3 USE:3 ALT:5 | **Effort:** M | **Repo:** public

Load the CMS Part D formulary and pricing files and let a user check which plans in their region cover a given drug, at what tier, and with what prior-authorization or step-therapy restriction. Useful for helping a parent pick a plan during open enrollment. Done when a drug list produces a ranked plan comparison with the data vintage stated.

**Needs:** nothing

### HLTH-038: Cognitive distortion labeling practice

**Scores:** $:3 CV:4 VIR:3 USE:4 ALT:5 | **Effort:** M | **Repo:** public

A psychoeducation drill: read a thought, pick which of the standard CBT distortion categories it matches, and compare against the labeled answer. Uses a fixed published taxonomy and a hand-written item bank, the model is used only to generate candidate practice items for human review before they enter the bank, never to label a real user's own thoughts. Framed explicitly as skill practice, not therapy, with resources for finding a clinician.

**Needs:** nothing

### HLTH-039: Verified crisis resource dataset

**Scores:** $:0 CV:3 VIR:3 USE:3 ALT:5 | **Effort:** S | **Repo:** public

Publish a maintained, machine-readable dataset of crisis lines and their real coverage (region, hours, languages, text vs voice, whether they trace calls), each field verified against the operator's own published page with a checked-on date, plus a monthly link-check job. Every health tool in this file imports it. Done when the dataset is versioned, cited, and the checker runs green.

**Needs:** nothing

### HLTH-040: Hallucinated interaction benchmark for local models

**Scores:** $:3 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Build an eval set of real and deliberately fictitious drug pairs from authoritative data and measure how often each local model asserts an interaction that does not exist, denies one that does, or correctly abstains. Report abstention rate as a first-class metric. The point is to publish the evidence that these models must not be trusted for this task, which is the argument every other tool in this file rests on.

**Needs:** nothing

### HLTH-041: Supplement marketing red-flag detector

**Scores:** $:3 CV:4 VIR:5 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Given a supplement product page, flag the recognized patterns: disease claims that cross the FDA structure/function line, "clinically proven" with no citation, citations to studies on a different compound or dose, proprietary blends hiding amounts, and fake-urgency testimonials. Output is a per-flag explanation with the quoted text, judging the marketing rather than the molecule. Done when it scores a set of 30 real pages against hand labels.

**Needs:** nothing

### HLTH-042: Readability grader for patient materials

**Scores:** $:2 CV:3 VIR:2 USE:3 ALT:5 | **Effort:** S | **Repo:** public

Score patient-facing text with SMOG, Flesch-Kincaid, and a medical-jargon density measure against the commonly recommended 6th-8th grade target, highlighting the specific sentences that blow the budget. Suggests simpler terms from a curated medical plain-language list rather than model invention. Done when it can grade a real discharge instruction sheet.

**Needs:** nothing

### HLTH-043: Dyslexia-friendly reader extension

**Scores:** $:3 CV:4 VIR:4 USE:3 ALT:5 | **Effort:** M | **Repo:** public

A browser extension that reflows any page with the typographic variables that have actual evidence behind them, increased letter and line spacing, shorter line length, left-aligned ragged right, each toggle labeled with what the evidence does and does not show, including that special dyslexia fonts have weak support. Done when it works on arbitrary sites without breaking layout.

**Needs:** nothing

### HLTH-044: Local live captioner

**Scores:** $:4 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** L | **Repo:** public

Real-time captions for any system audio using local Whisper with a streaming buffer, rendered as an always-on-top overlay with adjustable size and contrast. Fully offline, which is what makes it usable for medical appointments and private calls where a cloud captioner is not acceptable. Done when latency stays under two seconds on the 5090 with usable accuracy.

**Needs:** nothing

### HLTH-048: Evidence audit of fifty popular wellness claims

**Scores:** $:4 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** XL | **Repo:** public

Build a repeatable pipeline and run it over the 50 most-repeated consumer health claims: locate the primary literature, extract effect sizes, grade the body of evidence, and publish a card per claim showing the strongest study for and against, with the honest verdict frequently being "underpowered, mixed, or never tested in humans." Every step reproducible from the repo. This is the flagship credibility artifact of this category.

**Needs:** a Vercel deploy for the site.

