# Educational Tools & Courses

Teaching artifacts: explainers that make a hard idea click, spaced-repetition machinery, curriculum generators, tutoring harnesses, and courses.

### EDU-001: Attention head explorer over real Qwen weights

**Scores:** $:1 CV:5 VIR:4 USE:3 ALT:5 | **Effort:** L | **Repo:** public

Build a browser explainer where the reader types a sentence and watches the actual QK attention matrices of `qwen3:8b` light up head by head, layer by layer. Extract the attention tensors server-side with `transformers` + PyTorch from the HF safetensors (not Ollama, which does not expose them), cache them as compressed JSON per prompt, and render with canvas. Done when a reader can point at a head and say "that one tracks the subject-verb link."

**Needs:** ~16 GB disk for the HF copy of the 8B weights.

### EDU-002: Floating point error accumulator

**Scores:** $:0 CV:2 VIR:3 USE:2 ALT:4 | **Effort:** S | **Repo:** public

Single-page explainer: type a decimal, see its exact IEEE-754 bits, the true value it actually stores, and the residual. Then run a naive running sum of 0.1 ten thousand times next to Kahan summation, plotting divergence live. Done when the page answers "why is 0.1 + 0.2 != 0.3" and "why did my total drift" in one scroll.

**Needs:** nothing

### EDU-003: Catastrophic backtracking visualizer

**Scores:** $:1 CV:3 VIR:4 USE:3 ALT:5 | **Effort:** M | **Repo:** public

Paste a regex and an input string; the page compiles the pattern to an NFA, single-steps the backtracking engine, and draws the exponential blowup as a call tree with a step counter. Include a gallery of real ReDoS patterns from past CVEs. Done when a reader can predict which of two equivalent regexes explodes.

**Needs:** nothing

### EDU-004: Prerequisite DAG curriculum generator

**Scores:** $:3 CV:4 VIR:4 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Give it a target ("understand flow matching") and it emits a directed acyclic graph of prerequisite concepts, each node carrying one concrete resource and one checkable exercise. Use `qwen3.6:27b` for decomposition, then a verification pass that rejects any edge where the child concept can be defined without the parent. Done when the DAG for three different targets survives spot-checking by an expert reader.

**Needs:** nothing

### EDU-005: Cloze deck builder from papers

**Scores:** $:2 CV:3 VIR:2 USE:5 ALT:4 | **Effort:** M | **Repo:** public

CLI that takes a PDF, extracts claim sentences, and generates Anki cloze cards where the deleted span is the load-bearing quantity (the effect size, the exponent, the constraint) rather than a random noun. Ship a scoring pass with `gemma4:31b` that rejects cards answerable from the sentence stem alone. Output `.apkg` via genanki.

**Needs:** nothing

### EDU-006: Spaced-repetition scheduler shootout

**Scores:** $:1 CV:4 VIR:4 USE:3 ALT:5 | **Effort:** M | **Repo:** public

Simulate synthetic learners with known forgetting curves and race FSRS, SM-2, Leitner, and a fixed-interval control over a simulated year, measuring retention per review-minute spent. Publish the notebook, the parameter sweep, and a plot showing where each scheduler wins. Done when the result is reproducible from one command.

**Needs:** nothing

### EDU-007: Onboarding cards from git history

**Scores:** $:3 CV:4 VIR:3 USE:5 ALT:4 | **Effort:** M | **Repo:** public

Point it at a repo and it mines the commit log, the module boundaries, and the most-edited functions to generate spaced-repetition cards about that specific codebase ("which module owns retry logic?"). Schedules with FSRS in a local SQLite file. Done when a week of reviews measurably speeds up navigating an unfamiliar repo.

**Needs:** nothing

### EDU-008: Feynman-technique gap finder

**Scores:** $:3 CV:4 VIR:4 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Record yourself explaining a concept out loud, transcribe with local Whisper, then diff the transcript against a reference concept map for that topic and report which nodes you never mentioned, which you named without defining, and where you hedged. Done when it catches a gap the speaker did not know they had.

**Needs:** nothing

### EDU-009: Five-model explanation disagreement page

**Scores:** $:1 CV:3 VIR:4 USE:4 ALT:4 | **Effort:** S | **Repo:** public

Ask five local models the same conceptual question, align their answers claim by claim, and render a page highlighting exactly where they contradict each other. The pitch to learners: contradiction between models is a reliable flag that you are being told something the models are unsure about. Done for a fixed set of 40 commonly-misexplained CS and physics questions.

**Needs:** nothing

### EDU-010: Misconception bank with diagnostic items

**Scores:** $:3 CV:5 VIR:4 USE:4 ALT:5 | **Effort:** L | **Repo:** public

For 25 topics (recursion, pointers, `this` binding, floating point, Big-O, relativity of simultaneity), catalog the common wrong mental models and write diagnostic multiple-choice items whose distractors each map to one specific misconception. Score the item set for discrimination against simulated respondents. Done when picking a wrong answer tells you which wrong model the learner holds.

**Needs:** nothing

### EDU-013: Japanese pitch-accent minimal pair trainer

**Scores:** $:3 CV:3 VIR:3 USE:5 ALT:5 | **Effort:** S | **Repo:** public

Drill page for Koe: plays a recorded minimal pair (箸/橋, 雨/飴), the learner picks the accent pattern, FSRS schedules the misses. Source pitch patterns from the open OJAD/Wadoku-derived accent data and TTS the audio locally. Done when a session of 50 items reports per-pattern accuracy.

**Needs:** nothing

### EDU-014: Shadowing trainer with forced alignment

**Scores:** $:4 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** L | **Repo:** public

The learner shadows a native audio clip; local Whisper word timestamps are aligned to the reference to score timing drift, dropped syllables, and phoneme substitutions, rendered as a two-track waveform with the divergences marked. Ship it as a Koe module for Japanese, Spanish, and Brazilian Portuguese. Done when the score correlates with a human rater on 30 samples.

**Needs:** nothing

### EDU-015: Comprehensible-input coverage ranker

**Scores:** $:3 CV:4 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Given your known-word list, rank a library of YouTube captions and public-domain texts by the fraction of tokens you already know, surfacing material in the 95-98% band where acquisition happens. Handle Japanese with a proper tokenizer (fugashi/UniDic), not whitespace. Done when it can hand you tomorrow's reading in one click.

**Needs:** nothing

### EDU-016: Kanji radical etymology explorer

**Scores:** $:2 CV:3 VIR:4 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Interactive graph of the joyo kanji decomposed into components, with phonetic-series clustering made visible: click 青 and see every character that borrows its sound. Build from KanjiVG plus the open CJK decomposition datasets. Done when a learner can predict the reading of an unseen compound from its phonetic component.

**Needs:** nothing

### EDU-017: Brazilian vs European Portuguese diff drill

**Scores:** $:2 CV:2 VIR:3 USE:4 ALT:4 | **Effort:** S | **Repo:** public

A compact reference plus drill covering the divergences that actually trip learners: gerund vs infinitive progressive, clitic placement, tu/você, and the vocabulary pairs. Generate drill sentences with `gemma4:31b` and hand-verify the 200-item seed set. Done when it ships as a Koe lesson unit.

**Needs:** nothing

### EDU-019: Guided repo tour generator

**Scores:** $:4 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Point it at any GitHub repo and it produces a 10-stop guided tour: entry point, core data structure, the one clever bit, the seams where you would add a feature, with a checkpoint question at each stop. Uses `qwen3-coder:30b` over a call-graph extraction rather than raw file dumps. Done when a stranger can make a correct first PR after taking the tour.

**Needs:** nothing

### EDU-020: Reading-level ladder with comprehension checks

**Scores:** $:3 CV:4 VIR:3 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Take one technical explanation and render it at five reading levels, then auto-generate comprehension questions and verify that the questions are answerable from each level (a level that loses the answer has lost the concept, not just the vocabulary). Validate with Flesch-Kincaid and SMOG plus the answerability check. Done when the ladder holds for 20 source explanations.

**Needs:** nothing

### EDU-022: B-tree insertion animator

**Scores:** $:1 CV:3 VIR:4 USE:3 ALT:5 | **Effort:** M | **Repo:** public

Type your own keys and watch a real B+ tree fill, split, and promote, with the disk-page boundaries drawn to scale so the reader sees why fanout matters. Include a mode that replays the inserts as a Postgres index would order them. Done when the reader can explain why random UUID keys hurt.

**Needs:** nothing

### EDU-024: TLS handshake, packet by packet

**Scores:** $:1 CV:4 VIR:4 USE:3 ALT:5 | **Effort:** M | **Repo:** public

Capture a real TLS 1.3 handshake, then walk the reader through each record byte range with the key schedule computed live in the browser so they can watch the shared secret appear. Include the "why does this resist a MITM" checkpoint. Done when the page derives the same traffic keys OpenSSL logged.

**Needs:** nothing

### EDU-025: Flexbox resolution step-through

**Scores:** $:2 CV:3 VIR:4 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Implement the CSS flexbox sizing algorithm from the spec in TypeScript and let the reader step through it for their own markup: hypothetical main size, flex base size, the free-space distribution loop, min-content clamping. Done when it agrees with the browser's computed layout on the WPT flexbox cases it covers, and shows exactly which step caused a surprising result.

**Needs:** nothing

### EDU-026: Grapheme cluster explainer

**Scores:** $:1 CV:2 VIR:3 USE:3 ALT:4 | **Effort:** S | **Repo:** public

Type any text and see it split four ways: bytes, code points, UTF-16 units, and extended grapheme clusters, with family emoji and Devanagari conjuncts as the built-in examples. Then show `.length`, `.split('')`, and `Intl.Segmenter` disagreeing on the same string. Done when it makes the "never index into a string" rule feel obvious.

**Needs:** nothing

### EDU-027: Mojibake decoder and explainer

**Scores:** $:1 CV:2 VIR:4 USE:4 ALT:4 | **Effort:** S | **Repo:** public

Paste garbled text and it searches encode/decode round-trip chains to recover the original, then explains the exact wrong pair that produced the garbling ("UTF-8 bytes read as CP1252, then re-encoded as UTF-8"). Done when it fixes the classic `â€™` and `ã‚` families and names the cause.

**Needs:** nothing

### EDU-028: Event loop step debugger

**Scores:** $:2 CV:4 VIR:4 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Paste JS with timers, promises, and `queueMicrotask`, and step through execution with the call stack, microtask queue, and macrotask queue drawn side by side. Implement it over a real interpreter loop rather than a hardcoded trace so arbitrary snippets work. Done when it correctly orders the standard interview-question snippets and explains why.

**Needs:** nothing

### EDU-029: React re-render cascade visualizer

**Scores:** $:4 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** L | **Repo:** public

A dev-mode library that instruments a real component tree and renders the re-render cascade as an animated flame path, attributing each render to its cause: state set, context value identity change, unstable prop, parent render. Ship as an npm package with a demo app that has three planted performance bugs. Done when it names the cause correctly for all three.

**Needs:** nothing

### EDU-030: Compiler slider

**Scores:** $:2 CV:5 VIR:5 USE:3 ALT:5 | **Effort:** L | **Repo:** public

Write a tiny statically-typed language and expose every stage behind one slider: source, tokens, CST, AST, typed AST, IR, stack-machine bytecode, and execution. Dragging the slider highlights the corresponding span at every level simultaneously. Done when clicking a variable in the source highlights its slot in the bytecode.

**Needs:** nothing

### EDU-031: Regex to railroad diagrams

**Scores:** $:1 CV:2 VIR:3 USE:4 ALT:5 | **Effort:** S | **Repo:** public

Parse a JS regex into an AST and render a proper railroad diagram with capture groups, lookarounds, and quantifier bounds labeled. Include a hover mode that highlights which diagram segment consumed which characters of a test string. Done when it round-trips the regexes in a real codebase without falling back to "unsupported."

**Needs:** nothing

### EDU-032: Raft you can break

**Scores:** $:2 CV:5 VIR:5 USE:3 ALT:5 | **Effort:** L | **Repo:** public

An interactive five-node Raft cluster in the browser where the reader partitions the network, pauses nodes, and delays messages, then watches elections and log reconciliation play out. Implement the real algorithm, not an animation script, and add a challenge mode: "cause a stale read" and "make a leader step down." Done when the invariant checker never fires on legal operations.

**Needs:** nothing

### EDU-033: Consistent hashing explainer

**Scores:** $:1 CV:3 VIR:3 USE:3 ALT:4 | **Effort:** S | **Repo:** public

Drag nodes onto a hash ring, add and remove them, and watch exactly which keys move, with a counter for keys remapped versus the theoretical minimum. Add a virtual-nodes toggle so the load-balance improvement is visible as a histogram. Done when it makes "why not modulo N" answerable in one sentence.

**Needs:** nothing

### EDU-034: Aliasing you can hear

**Scores:** $:1 CV:3 VIR:4 USE:3 ALT:5 | **Effort:** S | **Repo:** public

Sweep a sine tone above the Nyquist frequency and let the reader hear the alias fold back down while the spectrum plot shows the mirror image, then toggle an anti-alias filter on. Uses Web Audio, no libraries. Done when a reader who has only seen the math says "oh, that is what that sounds like."

**Needs:** nothing

### EDU-035: Draggable Minkowski diagram

**Scores:** $:1 CV:4 VIR:4 USE:3 ALT:5 | **Effort:** M | **Repo:** public

Place events on a spacetime diagram, drag the observer's velocity, and watch the simultaneity lines rotate, with proper time and interval computed live. Include the ladder-and-barn and twin scenarios as presets with the resolution shown geometrically. Done when the reader can state which event pairs have an observer-independent order and why.

**Needs:** nothing

### EDU-036: Fit a gravitational-wave chirp by hand

**Scores:** $:2 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Load real strain data for GW150914 from the open GWOSC release, let the reader drag the two component masses and watch their template chirp slide into or out of alignment with the whitened data, with matched-filter SNR updating live and audio playback of both. This is the teaching companion to the ViT/CNN glitch paper. Done when dragging to the published masses visibly maximizes SNR.

**Needs:** nothing (GWOSC data is public and freely licensed).

### EDU-037: Orbital mechanics challenge ladder

**Scores:** $:2 CV:4 VIR:4 USE:3 ALT:5 | **Effort:** M | **Repo:** public

A patched-conic playground with a graded ladder of 15 challenges from "circularize" to "free-return trajectory," each scored on delta-v spent versus the analytic optimum. Show the vis-viva equation updating alongside the trajectory so the intuition and the algebra stay coupled. Done when the ladder is completable and the optimum is correct for each rung.

**Needs:** nothing

### EDU-038: Garden of forking paths simulator

**Scores:** $:1 CV:4 VIR:5 USE:4 ALT:5 | **Effort:** S | **Repo:** public

Give the reader a null dataset and a menu of innocuous analysis choices (drop outliers? log-transform? which covariates?), let them hunt, and show the p-value curve as they wander until they find p < 0.05. Then reveal the multiverse plot of all paths. Done when the reader gets a significant result from pure noise in under a minute.

**Needs:** nothing

### EDU-039: Power analysis widget for the meta-analysis

**Scores:** $:1 CV:4 VIR:3 USE:4 ALT:4 | **Effort:** S | **Repo:** public

An embeddable calculator for the AI-tutoring evidence work: enter expected effect size, cluster size, and ICC, and get required N with the operating characteristic curve drawn. Handles cluster-randomized designs correctly, which most online calculators do not. Done when it matches `pwr` and `clusterPower` reference outputs.

**Needs:** nothing

### EDU-040: Socratic tutor harness with a no-answer guardrail

**Scores:** $:5 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** XL | **Repo:** public

Build a tutoring loop over local models that is structurally incapable of stating the answer: a separate verifier model checks each candidate turn against the target solution and rejects any turn that leaks it. Then build the eval that matters, a benchmark of simulated students where the metric is whether the student reaches the answer themselves and can restate why. Done when the guardrail's leak rate is measured, not assumed.

**Needs:** nothing

### EDU-042: Build your own X, in TypeScript

**Scores:** $:4 CV:5 VIR:5 USE:3 ALT:5 | **Effort:** XL | **Repo:** public

A series where a frontend engineer builds the things they use but have never opened: a bundler, a reactive signals runtime, a virtual DOM differ, a query cache, a CRDT text buffer. Each is under 1000 lines, test-driven, with the tests written first so the reader implements against them. Done when each chapter's stub repo passes its own suite when correctly filled in.

**Needs:** nothing

### EDU-043: Lecture recording to interactive notebook

**Scores:** $:3 CV:4 VIR:3 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Ingest a talk recording, transcribe with Whisper, detect slide changes with ffmpeg scene detection, and emit a notebook where each section pairs the slide, the transcript span, and a generated runnable cell or exercise. Done when a 45-minute conference talk becomes a notebook someone would actually work through.

**Needs:** nothing

### EDU-044: Concept map extraction from a textbook

**Scores:** $:3 CV:4 VIR:3 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Given a textbook PDF, extract the concept graph (term, definition location, dependency edges) using `nemotron-3-nano` for its long context, and render it as an explorable map where clicking a node jumps to the defining page. Include a "what must I already know to read chapter 7" query. Done for two real open textbooks.

**Needs:** nothing

### EDU-045: Distractor quality analyzer

**Scores:** $:3 CV:4 VIR:2 USE:3 ALT:5 | **Effort:** M | **Repo:** public

For any multiple-choice item bank, score each distractor on plausibility (does a model with a specific misconception pick it?) and flag the dead ones nobody ever chooses. Simulate respondents by prompting local models conditioned on specific wrong mental models from the misconception bank. Done when it flags the throwaway distractors in a real quiz.

**Needs:** nothing

### EDU-046: Diagram reconstruction as retrieval practice

**Scores:** $:2 CV:3 VIR:3 USE:4 ALT:4 | **Effort:** S | **Repo:** public

Read an explanation, then rebuild its mermaid diagram from a shuffled pile of nodes and edges; the tool scores your reconstruction against the reference by graph edit distance and shows exactly which relation you got backwards. Done when it works on any markdown file containing a mermaid block.

**Needs:** nothing

### EDU-047: Code-symbol typing tutor

**Scores:** $:2 CV:2 VIR:3 USE:4 ALT:4 | **Effort:** S | **Repo:** public

A typing drill built only from the character sequences that slow programmers down: `=>`, `?.`, `?:`, `::`, `!==`, template literal braces, and the bracket dances. Measures per-bigram latency and generates the next drill from your own slowest transitions. Done when it reports measurable improvement on your worst ten bigrams.

**Needs:** nothing

### EDU-048: System design spaced repetition with rubric grading

**Scores:** $:4 CV:5 VIR:3 USE:5 ALT:4 | **Effort:** M | **Repo:** public

A card deck of system design prompts where the answer is spoken or typed and graded against an explicit rubric (capacity estimate present, failure mode addressed, consistency model named) by a local model that must cite which rubric line each point satisfies. FSRS schedules the weak rubric dimensions, not just weak cards. Done when weak dimensions surface reliably across a two-week run.

**Needs:** nothing

### EDU-049: Koe curriculum spine

**Scores:** $:5 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** XL | **Repo:** public

Replace ad-hoc lesson ordering in the language learning app with a real curriculum engine: a per-language skill graph, mastery estimated per skill with a Bayesian knowledge tracing model, and lesson assembly that pulls items to hit exactly the frontier skills. Build it for Japanese, Spanish, and Brazilian Portuguese with the graph authored once and localized per language. Done when a learner's session composition provably follows their mastery state.

**Needs:** nothing

### EDU-050: CPU pipeline visualizer

**Scores:** $:1 CV:4 VIR:4 USE:3 ALT:5 | **Effort:** M | **Repo:** public

Write a small assembly program and watch it flow through a five-stage pipeline with hazards, forwarding paths, and stalls drawn per cycle. Add a branch predictor toggle so the reader can see mispredict cost as wasted cycles. Done when the reader can reorder two instructions and predict the cycle count change before running it.

**Needs:** nothing

