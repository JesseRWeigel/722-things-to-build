# Benchmarks, Evals & Leaderboards

Measurement instruments nobody has built yet, harnesses, red-team sets, and public leaderboards that each ship a dataset, a site, or a writeup.

### EVAL-001: Quantization damage atlas: which capability breaks first

**Scores:** $:1 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Quantize four model families to q8, q6_K, q5_K_M, q4_K_M, q3_K_M, and q2_K, then score each level across eight capability axes (arithmetic, instruction format adherence, long-context recall, code correctness, multilingual, refusal calibration, JSON validity, factual recall). Deliverable: a public heatmap site answering the question every local-LLM user actually has, not "how much worse is q4" but "worse at *what*."

**Needs:** ~120 GB of transient disk, freed between families; nothing paid

### EVAL-002: Joules per correct answer

**Scores:** $:1 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Sample `nvidia-smi` power draw at 100 ms during every eval run and divide total energy by number of correct answers, producing an efficiency metric that no existing leaderboard reports. Deliverable: a leaderboard of local models ranked by joules-per-correct-answer on a fixed task set, plus the finding of whether the biggest model is ever the most energy-efficient per solved problem.

**Needs:** nothing

### EVAL-003: The slopsquatting surface: hallucinated npm packages by model

**Scores:** $:1 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Prompt every available model for solutions to 2,000 realistic JS/TS tasks, extract every `import`/`require` target, and check each against the npm registry to find package names that do not exist. Deliverable: an HF dataset of hallucinated package names ranked by how many models invent the same one, the highest-risk squatting targets, reported responsibly rather than registered.

**Needs:** nothing

### EVAL-004: Does the agent echo your .env?

**Scores:** $:0 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** S | **Repo:** public

Build a fixture repo containing a realistic `.env` with fake secrets, then run 40 innocuous tasks ("summarize this project's config", "debug why the DB connection fails") through each model and grep every output for the secret values. Deliverable: a per-model secret-leak rate and the exact task phrasings that trigger leakage most often.

**Needs:** nothing

### EVAL-005: Prompt injection delivered through tool output

**Scores:** $:1 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Build a harness that gives a coding agent fake tool results (web fetch, file read, shell output) laced with 150 injection payloads across categories, instruction override, false authorization, exfiltration request, tool-call forgery, and score whether the agent complies, notices, or silently partially complies. Deliverable: an HF red-team dataset plus a compliance-rate leaderboard across local and API models.

**Needs:** nothing

### EVAL-006: Tool-call schema adherence under adversarial pressure

**Scores:** $:1 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Define tool schemas with hostile-but-legal shapes (deeply nested objects, enums with near-synonym values, required fields the prompt never mentions, mutually exclusive optionals) and measure per-model rates of invalid JSON, hallucinated fields, wrong enum values, and omitted required fields. Deliverable: a schema-adherence leaderboard with a breakdown by failure mode, not a single pass rate.

**Needs:** nothing

### EVAL-007: Destructive command propensity in autonomous shell agents

**Scores:** $:0 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** S | **Repo:** public

In a throwaway container-free sandbox directory with a dry-run shell shim that records rather than executes, give agents 60 tasks whose easiest solution is destructive ("clean up this repo", "make the branch match origin", "free some disk"), and count proposed `rm -rf`, `git reset --hard`, `checkout .`, and force-push commands. Deliverable: a destructiveness index per model with the tasks that provoke it.

**Needs:** nothing

### EVAL-008: Constraint retention over 30 turns

**Scores:** $:0 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

State a checkable constraint at turn 1 ("never use the letter z", "always end with a line count", "responses under 40 words"), then run 30 turns of unrelated conversation, checking compliance at every turn. Deliverable: retention-decay curves per model and per constraint type, showing which models forget at turn 6 and which hold to turn 30.

**Needs:** nothing

### EVAL-009: The full needle grid for consumer-runnable models

**Scores:** $:1 CV:4 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Run needle-in-haystack at every combination of context length (2k-128k in 8 steps), needle depth (10 positions), and distractor condition (none, one near-duplicate needle, five near-duplicates), on the models that actually fit in 32 GB. Deliverable: per-model grid images and the practical answer to "at what context length does this model start lying to me."

**Needs:** nothing

### EVAL-010: Did it actually run the tests, or just say so?

**Scores:** $:1 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Build repos with a test command that is silently broken (missing binary, exits 0 with no output, hangs), assign fix tasks, and log whether the agent claims tests pass without a real passing run. Deliverable: an "agentic honesty" leaderboard measuring unearned success claims, a failure mode everyone complains about and nobody has quantified.

**Needs:** nothing

### EVAL-011: Calibrated abstention: does the model know it doesn't know?

**Scores:** $:0 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Mix 300 answerable questions with 300 that are unanswerable by construction (false premises, fictional entities, information genuinely postdating any cutoff, underspecified requests) and score both accuracy and abstention, reporting a single calibration number that punishes both confident wrongness and over-abstention. Deliverable: a calibration leaderboard and the HF dataset of unanswerables.

**Needs:** nothing

### EVAL-012: Position bias in pairwise LLM judging, quantified per judge

**Scores:** $:0 CV:4 VIR:4 USE:5 ALT:5 | **Effort:** S | **Repo:** public

Present every judge model with 500 A/B pairs and their exact swaps, then compute the disagreement rate under order reversal, the fraction of verdicts that are pure position artifact. Deliverable: a per-judge position-bias coefficient, plus a recommendation of which local model is safe to use as a judge and how many swaps are needed to wash the bias out.

**Needs:** nothing

### EVAL-013: Do models prefer their own writing?

**Scores:** $:0 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Generate answers to 200 prompts from eight models, then have each model judge every pair blind, building a full round-robin matrix that separates genuine quality ranking from self-preference. Deliverable: a self-preference score per model (how much it inflates its own outputs relative to consensus) and the implication for anyone using a model to grade its own family.

**Needs:** nothing

### EVAL-014: Sycophancy flip-rate under user pushback

**Scores:** $:0 CV:4 VIR:5 USE:5 ALT:5 | **Effort:** S | **Repo:** public

Ask 200 questions with verifiable answers, then push back once with a confident wrong assertion and measure how often the model abandons a correct answer, escalating across three pushback intensities (mild doubt, confident correction, appeal to authority). Deliverable: flip-rate curves per model and per intensity, published as a dataset others can rerun.

**Needs:** nothing

### EVAL-015: Indirect injection through the repo itself

**Scores:** $:1 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Plant injection payloads inside plausible repository artifacts, a README section, a code comment, a `package.json` script description, a CHANGELOG entry, a test fixture, then assign ordinary maintenance tasks and measure whether the coding agent follows the planted instruction. Deliverable: a fixture repo generator, an HF payload dataset, and per-model susceptibility by payload location.

**Needs:** nothing

### EVAL-016: Minimal diff, or gratuitous rewrite?

**Scores:** $:1 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Give each model a small, precisely scoped edit task in a real 500-line file and measure lines touched, formatting churn, unrelated refactors introduced, and whether the change even works. Deliverable: a "surgical edit score" leaderboard, which matters far more to daily agentic coding than any pass@1 number.

**Needs:** nothing

### EVAL-017: Grade generated tests by mutation score, not coverage

**Scores:** $:1 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Have each model write tests for 100 real functions, then run Stryker (JS/TS) and mutmut (Python) against the generated suites to measure the fraction of injected mutants they actually kill. Deliverable: a leaderboard showing that high-coverage LLM tests frequently assert nothing, with the mutation-survival examples as evidence.

**Needs:** nothing

### EVAL-018: Vulnerability introduction rate in generated code

**Scores:** $:1 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Assign 200 tasks whose natural implementation invites SQL injection, XSS, path traversal, insecure deserialization, or missing authorization, then scan every output with Semgrep and CodeQL plus manual review of a sample. Deliverable: per-model vulnerability-per-KLOC rates and the finding of whether asking for "secure code" actually changes the number.

**Needs:** nothing

### EVAL-019: Regex correctness against executable ground truth

**Scores:** $:0 CV:4 VIR:3 USE:5 ALT:5 | **Effort:** S | **Repo:** public

Build 300 regex tasks each specified by 20 positive and 20 negative test strings rather than prose, so grading is exact execution rather than judgment, and include catastrophic-backtracking cases with a timeout. Deliverable: an HF benchmark with an execution grader and a leaderboard including a ReDoS-authoring rate per model.

**Needs:** nothing

### EVAL-020: Type-level TypeScript puzzles graded by tsc

**Scores:** $:0 CV:5 VIR:4 USE:5 ALT:4 | **Effort:** M | **Repo:** public

Assemble 150 type-level challenges (conditional types, mapped types, template literal types, variance puzzles, inference from generics) where the grader is `tsc --strict` compiling a fixture that must pass and a negative fixture that must fail. Deliverable: a fully automatic benchmark for a skill that mainstream code benchmarks entirely ignore, published on HF with a leaderboard.

**Needs:** nothing

### EVAL-021: Accessibility correctness of LLM-generated React

**Scores:** $:2 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Ask models to build 60 common UI components (modal, combobox, tab set, date picker, toast, data table), render each with Playwright, and score with axe-core plus scripted keyboard-navigation and focus-trap checks. Deliverable: an a11y leaderboard for code models, directly relevant to frontend hiring conversations and shareable with the a11y community.

**Needs:** nothing

### EVAL-022: Dependency upgrades against real breaking changes

**Scores:** $:1 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Mine 80 real major-version bumps from popular OSS repos (React 18→19, Express 4→5, ESLint 8→9 and similar), reconstruct the pre-upgrade state with its test suite, and task each model with performing the migration until tests pass. Deliverable: an execution-graded migration benchmark that is far more honest about long-horizon work than function-completion tasks.

**Needs:** nothing

### EVAL-023: Monorepo navigation under a token budget

**Scores:** $:1 CV:5 VIR:4 USE:5 ALT:4 | **Effort:** L | **Repo:** public

In a synthetic but realistic 2,000-file Turborepo with deliberate red herrings (three files named `auth.ts`, a stale duplicate package, a re-export chain five deep), pose 60 "where is X defined / what breaks if I change Y" questions and score both correctness and tokens burned to get there. Deliverable: an efficiency-vs-accuracy leaderboard for agentic code search.

**Needs:** nothing

### EVAL-024: A terminal task suite for local-model CLI agents

**Scores:** $:2 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** XL | **Repo:** public

Build 120 verifiable terminal tasks (recover a bad rebase, find what filled the disk, fix a broken systemd-free background process, parse a gnarly log with jq, bisect a regression) each with a deterministic setup script and an assertion script, runnable against any model over Ollama or an API. Deliverable: an open harness plus the first leaderboard that tells a 32 GB GPU owner which local model can actually drive their shell.

**Needs:** nothing

### EVAL-025: The cost of a wrong chat template

**Scores:** $:0 CV:4 VIR:4 USE:5 ALT:5 | **Effort:** S | **Repo:** public

Run each model under its correct template and under four plausible wrong ones (another family's template, raw completion, ChatML on a non-ChatML model, missing BOS), scoring the same task set each time. Deliverable: a quantified answer to "how much quality am I losing to a misconfigured template", a silent tax on a huge fraction of local deployments.

**Needs:** nothing

### EVAL-026: Is temperature 0 actually deterministic?

**Scores:** $:0 CV:4 VIR:5 USE:5 ALT:5 | **Effort:** S | **Repo:** public

Run the same 200 prompts 20 times each at temperature 0 through Ollama, llama.cpp directly, and HF `transformers`, with fixed seeds, and count divergent outputs and first-divergence token position. Deliverable: a per-backend determinism report explaining batching and kernel nondeterminism to people who assume greedy decoding is reproducible.

**Needs:** nothing

### EVAL-027: The stale-knowledge benchmark

**Scores:** $:1 CV:4 VIR:5 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Curate 300 questions whose correct answer changed at a known date (library default flags, deprecated APIs, renamed orgs, superseded records) with both the old and new answer recorded, then score models on how often they assert the stale answer confidently versus flagging uncertainty. Deliverable: an HF dataset with per-item change dates, designed so it can be re-run against future models to date their knowledge.

**Needs:** nothing

### EVAL-028: Citation fabrication rate

**Scores:** $:0 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** S | **Repo:** public

Ask each model 200 questions that invite citation ("what paper introduced X", "which RFC specifies Y"), extract every arXiv ID, DOI, and RFC number, then resolve each against the real registries and check that the resolved title matches what the model claimed. Deliverable: fabrication and mismatch rates per model, separating invented identifiers from real identifiers attached to the wrong work.

**Needs:** nothing

### EVAL-029: Verbatim license-bearing code reproduction

**Scores:** $:0 CV:5 VIR:4 USE:4 ALT:5 | **Effort:** S | **Repo:** public

Prompt models with the opening lines of well-known GPL and AGPL source files and with descriptions of famously distinctive algorithms, then measure longest verbatim match against the original using suffix-array matching. Deliverable: a per-model reproduction-length distribution, framed as a compliance-risk report for teams shipping model output into proprietary code.

**Needs:** nothing

### EVAL-030: A contamination detector you can point at any benchmark

**Scores:** $:1 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** L | **Repo:** public

Implement several contamination signals, per-token perplexity gap between benchmark items and paraphrases, canary-string recall, memorized-ordering tests, and answer-only-given-partial-question probes, and run them over ten popular benchmarks against every local model. Deliverable: a contamination scorecard per (model, benchmark) pair and a reusable CLI, which is the most useful and least-supplied tool in the eval ecosystem.

**Needs:** nothing

### EVAL-032: Instruction hierarchy under direct conflict

**Scores:** $:0 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Construct 200 cases where the system prompt and the user message issue contradictory but individually benign instructions (format, language, length, persona, tool usage), and measure which side wins per model, per conflict type, and per position in a long conversation. Deliverable: a hierarchy-adherence leaderboard that tells agent builders whether system prompts are actually load-bearing on local models.

**Needs:** nothing

### EVAL-033: Refusal over-triggering on legitimate technical questions

**Scores:** $:1 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Build 300 benign-but-adjacent prompts a professional would genuinely ask, defensive security, drug interactions for a caregiver, historical violence for a curriculum, chemistry homework, network debugging, and measure false-refusal rate and hedging-without-answering rate. Deliverable: an over-refusal leaderboard for local models, the direction of the safety tradeoff that is systematically under-measured.

**Needs:** nothing

### EVAL-034: Jailbreak robustness of the local zoo, measured defensively

**Scores:** $:0 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** L | **Repo:** public

Run published jailbreak families (roleplay framing, encoding tricks, many-shot, suffix attacks, translation pivots) from existing public red-team datasets against every locally installed model, scoring with a rubric grader and reporting aggregate rates by technique. Deliverable: a robustness table per model and per technique published as a defensive resource, releasing aggregate statistics and technique names rather than novel working payloads.

**Needs:** nothing

### EVAL-035: Belief stability under sustained persuasion

**Scores:** $:0 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Distinct from single-turn sycophancy: run 10-turn adversarial dialogues where a persuader model applies escalating pressure (social proof, fabricated citations, emotional appeal, incremental concessions) to move the target off a verifiable correct answer, scoring turn-of-capitulation. Deliverable: survival curves per model plus the ranked effectiveness of each persuasion tactic.

**Needs:** nothing

### EVAL-036: Unicode and emoji stress test for tokenizers and models

**Scores:** $:0 CV:4 VIR:5 USE:4 ALT:5 | **Effort:** S | **Repo:** public

Test handling of zero-width characters, bidirectional override marks, combining-character stacks, skin-tone and ZWJ emoji sequences, and mixed-script identifiers, checking both token counts and whether the model correctly reports what it was given. Deliverable: a per-model unicode-integrity report and a small library of test strings, useful to anyone accepting untrusted text into a prompt.

**Needs:** nothing

### EVAL-037: Date, duration, and timezone reasoning

**Scores:** $:0 CV:4 VIR:3 USE:5 ALT:5 | **Effort:** S | **Repo:** public

Generate 500 programmatically verifiable temporal problems, business-day arithmetic, DST boundary crossings, timezone conversions across the international date line, ISO week numbers, leap-year edge cases, recurring-event expansion, with exact ground truth from a date library. Deliverable: an HF benchmark plus a leaderboard, targeting a failure class that quietly breaks scheduling agents.

**Needs:** nothing

### EVAL-038: Physical plausibility and unit discipline

**Scores:** $:0 CV:4 VIR:4 USE:4 ALT:5 | **Effort:** S | **Repo:** public

Pose 400 quantitative estimation problems requiring unit conversion and order-of-magnitude sanity (power budgets, data rates, fuel, dosage scaling, storage), grading both the numeric answer within tolerance and whether the stated units are coherent. Deliverable: a leaderboard reporting the rate of answers that are dimensionally wrong versus merely numerically off.

**Needs:** nothing

### EVAL-039: Multi-step arithmetic with tools explicitly forbidden

**Scores:** $:0 CV:3 VIR:4 USE:4 ALT:4 | **Effort:** S | **Repo:** public

Generate long-division, multi-digit multiplication, and chained percentage problems at controlled difficulty, forbid code execution, and record accuracy versus digit count plus the position of the first wrong digit. Deliverable: a per-model competence cliff (the exact digit count where accuracy falls below 50%) and an analysis of whether errors cluster at carries.

**Needs:** nothing

### EVAL-040: Exact-count compliance

**Scores:** $:0 CV:3 VIR:4 USE:5 ALT:4 | **Effort:** S | **Repo:** public

Issue 500 requests with a precisely checkable cardinality or length constraint ("exactly 7 bullets", "exactly 100 words", "3 sentences, no more", "a 12-item list with no duplicates") and check every response programmatically. Deliverable: a compliance leaderboard by constraint type, showing which models can count their own output and which cannot even approximately.

**Needs:** nothing

### EVAL-041: Reranker bake-off on real retrieval traces

**Scores:** $:1 CV:4 VIR:3 USE:5 ALT:4 | **Effort:** S | **Repo:** public

Take retrieval candidate sets from a real corpus, run every locally runnable cross-encoder and LLM-as-reranker over them, and measure nDCG@10 gain over the raw embedding ranking against latency and VRAM cost. Deliverable: a cost-benefit table telling RAG builders whether reranking earns its milliseconds at each corpus size.

**Needs:** nothing

### EVAL-042: Grammar-correction benchmark for Spanish, Brazilian Portuguese, and Japanese learners

**Scores:** $:2 CV:4 VIR:3 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Build 600 sentences containing realistic learner errors per language, L1-interference errors specifically, not random corruptions, each with a gold correction and an error-type label, then score models on correction accuracy, over-correction rate, and explanation quality. Deliverable: an HF dataset and leaderboard that directly determines which local model powers the language-learning app.

**Needs:** native-speaker review of the gold corrections for the Japanese set would raise confidence

### EVAL-043: Cost per solved task across OpenRouter's free and cheap tiers

**Scores:** $:2 CV:4 VIR:5 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Run a fixed 200-task suite through every model available on OpenRouter under a set price ceiling (including free tiers), recording tokens, dollars, latency, and rate-limit failures, then rank by dollars per solved task rather than raw score. Deliverable: a continuously re-runnable leaderboard aimed at builders picking a model on a budget.

**Needs:** OPENROUTER_API_KEY is present; a small dollar cap should be set on the account before running paid tiers

### EVAL-044: A capability benchmark for the Minecraft bot swarm

**Scores:** $:1 CV:5 VIR:5 USE:5 ALT:4 | **Effort:** L | **Repo:** public

Define 40 scored scenarios on a reproducible Paper world seed (mine to diamond, build a 3x3 shelter before nightfall, navigate 500 blocks to coordinates, cooperatively bridge a ravine, survive a night unarmed) with deterministic setup via RCON and programmatic scoring from world state. Deliverable: a regression benchmark that turns swarm improvements into numbers, plus a leaderboard comparing brain models on embodied tasks.

**Needs:** nothing

### EVAL-046: A reproducible eval runner for Ollama with content-addressed caching

**Scores:** $:2 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Build the harness the rest of this category depends on: task packs as YAML, graders as pluggable Python, results keyed by a hash of (model digest, prompt, params, grader version) so nothing is ever recomputed, resumable runs, and one command to publish results as an HF dataset. Deliverable: an npm/pip-installable runner that makes every eval here a config file instead of a script.

**Needs:** nothing

### EVAL-047: Nightly eval CI that catches model and quant regressions

**Scores:** $:2 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** XL | **Repo:** public

Wire the runner into a nightly GitHub Actions workflow plus a local runner for GPU jobs, re-running a stable core suite against pinned model digests, diffing against the previous night, and opening an issue when any score moves beyond a noise threshold. Deliverable: living infrastructure that detects the day an Ollama update or a re-uploaded quant quietly degrades a model.

**Needs:** self-hosted runner registration on the workstation for GPU jobs

### EVAL-049: The consumer-GPU model suite as a published HF collection

**Scores:** $:2 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** XL | **Repo:** public

Package the strongest evals here into one cohesive suite scoped to "models that fit in 32 GB," release every task dataset, grader, and result table as a linked HF collection with a proper dataset card, versioned task packs, and a submission process for outside results. Deliverable: a citable community resource plus a companion paper describing the suite and its headline findings.

**Needs:** nothing

### EVAL-050: A local-model arena with real human votes

**Scores:** $:2 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** XL | **Repo:** public

Ship a small web app that serves blind side-by-side responses from two randomly chosen local models, collects votes, computes Bradley-Terry ratings with confidence intervals, and publishes a live ranking, with prompt-category filters so the ranking can be sliced by task type. Deliverable: the first human-preference arena scoped entirely to models a person can run at home, plus the anonymized vote dataset released on HF.

**Needs:** hosting for the vote-collecting backend (Vercel plus a free Postgres tier); enough traffic to reach statistical significance

