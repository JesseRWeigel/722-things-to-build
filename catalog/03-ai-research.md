# AI/ML Research Artifacts

Reproducible experiments, publishable papers, novel fine-tunes, datasets, and interpretability work, all sized for a single RTX 5090 and 157 GB of disk.

### RSCH-001: Map the attention-sink token across every local model family

**Scores:** $:0 CV:4 VIR:3 USE:2 ALT:4 | **Effort:** S | **Repo:** public

Hook attention weights in `transformers` for the HF weights behind qwen3.6, gemma4, nemotron-3-nano and gpt-oss, and measure what fraction of probability mass every head dumps on position 0 (or on the chat template's first special token) across 200 prompts. Deliverable: a per-family sink-strength table, a heatmap grid, and a short writeup on whether MoE and dense models sink differently.

**Needs:** nothing

### RSCH-002: Cross-family logit lens: where do two tokenizers agree about a concept?

**Scores:** $:0 CV:5 VIR:3 USE:2 ALT:4 | **Effort:** M | **Repo:** public

Run the logit lens (unembed intermediate residual streams) on qwen3.5:9b and gemma4:e4b for the same 500 factual-completion prompts, then align the two vocabularies through a shared byte-level string space so layer-wise "when does the model know the answer" curves become comparable across tokenizers. Deliverable: aligned depth-of-knowledge curves plus the alignment utility as a pip-installable package.

**Needs:** nothing

### RSCH-003: Expert routing fingerprints in MoE Gemma vs MoE Qwen

**Scores:** $:0 CV:5 VIR:4 USE:2 ALT:4 | **Effort:** L | **Repo:** public

Instrument the router in `gemma4:26b-a4b` and `qwen3.6:35b-a3b` (HF weights, not the Ollama GGUF) and log expert assignments for a stratified corpus of code, English prose, Japanese, Spanish, math, and Latin. Cluster experts by their input distribution and test whether routing is organized by language, syntax, or topic. Deliverable: an arXiv-length paper with routing entropy per layer and per-expert token-cloud figures.

**Needs:** nothing

### RSCH-004: Does a refusal direction transfer between model families?

**Scores:** $:0 CV:5 VIR:4 USE:3 ALT:4 | **Effort:** M | **Repo:** public

Extract the mean-difference refusal direction from harmful/harmless prompt pairs in qwen3.5:9b, then project it into gemma4:e4b's residual space via a learned linear map fit on shared-prompt activations, and measure whether ablating the mapped direction changes gemma's refusal rate. Deliverable: transfer matrix across four model pairs and a defensive-framing writeup on what this implies for safety-training portability.

**Needs:** nothing

### RSCH-005: Train and publish a sparse autoencoder feature dictionary for qwen3.5:9b

**Scores:** $:1 CV:5 VIR:4 USE:3 ALT:5 | **Effort:** XL | **Repo:** public

Collect ~200M residual-stream activations from a mid-stack layer of qwen3.5:9b over a mixed corpus, train a top-k SAE with 16k-32k features on the 5090 (streaming activations to disk in fp16 shards, hard cap 60 GB), auto-interpret the top features with gpt-oss:20b, and ship the weights plus an interactive feature browser. Deliverable: HF model repo, HF dataset of feature explanations, and a Gradio Space.

**Needs:** nothing

### RSCH-006: Induction-head formation dynamics with dense checkpointing

**Scores:** $:0 CV:5 VIR:4 USE:2 ALT:5 | **Effort:** L | **Repo:** public

Pretrain a 40M-parameter transformer from scratch on a 3 GB FineWeb-Edu subset, saving a checkpoint every 100 steps through the loss-curve bump, then measure induction-head scores and in-context-learning loss at each checkpoint to pin down exactly when heads specialize. Deliverable: the full checkpoint series on HF (a resource almost nobody publishes at this granularity) plus the phase-transition analysis.

**Needs:** nothing

### RSCH-007: Grokking replication: Muon vs AdamW vs Lion on modular arithmetic

**Scores:** $:0 CV:4 VIR:3 USE:2 ALT:4 | **Effort:** M | **Repo:** public

Reproduce the classic modular-addition grokking setup and sweep optimizer, weight decay, and learning rate across three optimizers with 5 seeds each, recording the exact step where test accuracy jumps. Deliverable: a grokking-onset phase diagram and a claim about whether second-order-ish optimizers delay, accelerate, or eliminate the delayed-generalization gap.

**Needs:** nothing

### RSCH-008: Optimizer bake-off at 160M parameters under a fixed wall-clock budget

**Scores:** $:0 CV:5 VIR:4 USE:3 ALT:5 | **Effort:** L | **Repo:** public

Train identical 160M-parameter decoders with AdamW, Muon, Lion, SOAP, and Adafactor, each given the same six hours on the 5090 rather than the same step count, so the comparison reflects real single-GPU economics. Deliverable: loss-vs-wall-clock curves, tuned hyperparameters per optimizer released as YAML, and a writeup aimed at people training on one consumer card.

**Needs:** nothing

### RSCH-009: Fit a scaling law on one consumer GPU

**Scores:** $:0 CV:5 VIR:4 USE:3 ALT:5 | **Effort:** XL | **Repo:** public

Run an IsoFLOP sweep of 12-15 models between 5M and 300M parameters at three compute budgets each, fit the Chinchilla parametric form, and report how far a single-5090 fit lands from the published coefficients. Deliverable: an arXiv paper with the fitted exponents, all training curves, and an honest section on where small-scale fits break down.

**Needs:** nothing

### RSCH-010: Model diffing: what did the Minecraft fine-tune actually change?

**Scores:** $:0 CV:4 VIR:3 USE:5 ALT:3 | **Effort:** M | **Repo:** public

Compare `qwen3-minecraft:8b` against its qwen3:8b base with weight-delta norms per layer, activation-distribution shifts on held-out prompts, and a crosscoder trained on paired activations to isolate features present in one model and not the other. Deliverable: a report naming the specific behaviors the fine-tune added, and a recommendation for the next swarm fine-tune round.

**Needs:** nothing

### RSCH-011: What thinking traces actually buy you, per task type

**Scores:** $:0 CV:4 VIR:4 USE:5 ALT:4 | **Effort:** S | **Repo:** public

Run qwen3.5:9b, qwen3.5:27b, and qwen3.6:27b with `think: true` and `think: false` over a fixed 400-item mixed task set (arithmetic, code, extraction, translation, formatting) via `ai-sdk-ollama`, recording accuracy, latency, and token spend for each. Deliverable: a per-task-type table of the accuracy gain per extra second, showing where thinking is pure overhead.

**Needs:** nothing

### RSCH-012: Chain-of-thought faithfulness under surgical perturbation

**Scores:** $:0 CV:5 VIR:4 USE:3 ALT:5 | **Effort:** S | **Repo:** public

Take correct reasoning traces from qwen3.6:27b, corrupt one arithmetic step or one factual premise mid-trace, force-continue generation from the corrupted point, and measure how often the final answer follows the corruption versus silently reverting to the original answer. Deliverable: a faithfulness score per model plus examples of traces that are demonstrably post-hoc.

**Needs:** nothing

### RSCH-013: Locate, ablate, and re-inject the sycophancy direction

**Scores:** $:0 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Build paired prompts where a user asserts a wrong answer confidently versus neutrally, extract the activation direction that separates capitulation from persistence, then show bidirectional control: ablate it to make the model stubborn, amplify it to make it fawn. Deliverable: steering vectors on HF, a demo Space, and a paper section on whether the direction is the same one as instruction-following.

**Needs:** nothing

### RSCH-014: Does a benign fine-tune remove a planted backdoor?

**Scores:** $:0 CV:5 VIR:4 USE:3 ALT:5 | **Effort:** L | **Repo:** public

Defensive replication of the sleeper-agent result at small scale: QLoRA a trigger behavior into qwen3.5:9b (a benign but unmistakable trigger, e.g. "emit a marker string when the year is 2027"), then run increasing amounts of clean instruction fine-tuning and measure trigger survival. Deliverable: a persistence-vs-fine-tuning-tokens curve and the detection probes that did and did not catch it.

**Needs:** nothing

### RSCH-015: Universal neurons across random seeds

**Scores:** $:0 CV:5 VIR:3 USE:2 ALT:4 | **Effort:** L | **Repo:** public

Pretrain five 60M-parameter models identical except for seed, then correlate every neuron's activation vector across models over a fixed probe corpus to find units that reliably reappear. Deliverable: a catalog of universal neurons with their functional descriptions and the fraction of the network that is seed-invariant.

**Needs:** nothing

### RSCH-016: Reverse-engineer the carry operation in a small arithmetic model

**Scores:** $:0 CV:5 VIR:3 USE:2 ALT:4 | **Effort:** M | **Repo:** public

Train a 4-layer transformer to add 4-digit numbers, then use activation patching and path ablation to identify which heads carry information leftward between digit positions. Deliverable: a circuit diagram with causal-intervention evidence and a check on whether the same circuit shape appears in qwen3:8b's arithmetic.

**Needs:** nothing

### RSCH-017: Speculative decoding acceptance-rate matrix for the local zoo

**Scores:** $:0 CV:3 VIR:3 USE:5 ALT:4 | **Effort:** S | **Repo:** public

For every viable draft/target pair among the installed models sharing a tokenizer family (qwen3:8b→qwen3:32b, qwen3.5:9b→qwen3.5:27b, gemma4:e4b→gemma4:31b, and so on), measure token acceptance rate and end-to-end speedup in llama.cpp on the 5090. Deliverable: a pairing table with the honest speedup number, since most published figures come from datacenter cards.

**Needs:** nothing

### RSCH-018: KV-cache compression head-to-head at 32 GB

**Scores:** $:0 CV:4 VIR:3 USE:5 ALT:4 | **Effort:** M | **Repo:** public

Compare KV quantization (q8/q4), H2O-style eviction, and sliding-window attention on a 27B model at 32k-128k context, measuring VRAM saved, tokens/sec, and quality loss on a long-context retrieval set. Deliverable: a decision table telling a single-5090 owner which method to use at which context length, plus the measurement harness.

**Needs:** nothing

### RSCH-019: LoRA stacking interference curves

**Scores:** $:1 CV:4 VIR:3 USE:4 ALT:4 | **Effort:** M | **Repo:** public

Train six narrow LoRAs on one base model (SQL, regex, Portuguese, JSON extraction, commit messages, Minecraft commands), then evaluate every subset of merged adapters to quantify how much each task degrades per additional adapter and whether orthogonality-regularized training helps. Deliverable: interference matrices, the six adapters on HF, and guidance on how many LoRAs you can safely stack.

**Needs:** nothing

### RSCH-020: Model soup across a generation boundary

**Scores:** $:0 CV:4 VIR:3 USE:3 ALT:4 | **Effort:** S | **Repo:** public

Weight-average qwen3.5:27b and qwen3.6:27b at interpolation steps of 0.1 (they share architecture and tokenizer), evaluating each blend on reasoning, code, and multilingual sets to see if the mid-generation soup beats both parents anywhere. Deliverable: the interpolation curve, and the best blend published as a GGUF if it wins.

**Needs:** roughly 40 GB of scratch disk for the fp16 merge staging

### RSCH-021: Recursive synthetic-data collapse, measured properly

**Scores:** $:0 CV:5 VIR:5 USE:3 ALT:5 | **Effort:** L | **Repo:** public

Fine-tune a 500M model on real text, generate a corpus from it, fine-tune the next generation on that corpus, and repeat for 10 generations, tracking perplexity on held-out real data, vocabulary coverage, n-gram entropy, and tail-event survival at each step. Deliverable: collapse curves separating "loses the tails" from "loses the mean," plus the full generation-by-generation corpus on HF.

**Needs:** nothing

### RSCH-022: DPO vs KTO vs SimPO on one preference set at 3B

**Scores:** $:0 CV:5 VIR:3 USE:4 ALT:5 | **Effort:** L | **Repo:** public

Take a single public preference dataset and a single 3B base, run all three alignment objectives with matched compute and tuned betas via TRL, and evaluate on win-rate, KL from base, verbosity drift, and refusal-rate drift. Deliverable: a paper answering "does the choice of objective matter more than the data?" with all three checkpoints released.

**Needs:** nothing

### RSCH-023: Distill regex competence from a 30B coder into a 1B model

**Scores:** $:2 CV:4 VIR:3 USE:4 ALT:4 | **Effort:** M | **Repo:** public

Generate 50k (description → regex) pairs with qwen3-coder:30b, filter them by actually executing the regex against generated positive/negative test strings, then fine-tune a 1B base on the survivors. Deliverable: a tiny regex model that beats its teacher on verified correctness (because the data was filtered by execution), released on HF with the verification harness.

**Needs:** nothing

### RSCH-024: Byte-level language model without a tokenizer, at 100M scale

**Scores:** $:0 CV:5 VIR:4 USE:2 ALT:4 | **Effort:** L | **Repo:** public

Train matched 100M-parameter models on the same 4 GB corpus, one BPE, one raw-byte with a patching/pooling front end, and compare loss per byte, multilingual fairness, and robustness to typos and unicode noise at equal compute. Deliverable: the fairness argument for byte-level models quantified on languages the BPE tokenizer treats badly.

**Needs:** nothing

### RSCH-025: Tokenizer fertility atlas: 12 tokenizers × 24 languages

**Scores:** $:0 CV:3 VIR:4 USE:3 ALT:5 | **Effort:** S | **Repo:** public

Compute tokens-per-character and tokens-per-word for every installed model's tokenizer across a parallel corpus (FLORES-200 subset) covering 24 languages including Japanese, Brazilian Portuguese, Spanish, Latin, and several low-resource ones. Deliverable: an HF dataset plus a sortable static site quantifying exactly how much more each language costs per API call.

**Needs:** nothing

### RSCH-026: Homoglyph and typo robustness curves

**Scores:** $:0 CV:4 VIR:4 USE:3 ALT:4 | **Effort:** S | **Repo:** public

Perturb a fixed instruction set with escalating rates of keyboard-adjacent typos, Cyrillic homoglyph substitution, zero-width joiners, and combining diacritics, then plot accuracy decay per model. Deliverable: robustness curves showing which families collapse at 5% corruption and which hold to 20%, published with the perturbation library.

**Needs:** nothing

### RSCH-027: Memorization extraction rates across the open-weight zoo

**Scores:** $:0 CV:5 VIR:5 USE:2 ALT:5 | **Effort:** S | **Repo:** public

Prompt each local model with 50-token prefixes from public-domain books, widely mirrored code, and common web boilerplate, then measure verbatim continuation length against the source. Deliverable: a per-model memorization profile and the finding of which content types are memorized most, framed as a data-provenance study rather than an extraction tool.

**Needs:** nothing

### RSCH-028: Does reasoning transfer across the languages a model claims to speak?

**Scores:** $:0 CV:4 VIR:4 USE:4 ALT:5 | **Effort:** S | **Repo:** public

Translate a 300-problem reasoning set into Japanese, Spanish, and Brazilian Portuguese with human-verified prompts, then test four conditions per language: think and answer in-language, think in English answer in-language, and the reverses. Deliverable: a transfer matrix showing how much accuracy is lost purely to language of thought, directly informing the language-learning app's model choice.

**Needs:** nothing

### RSCH-029: Steering vectors for prose style, released as a usable pack

**Scores:** $:2 CV:4 VIR:4 USE:5 ALT:4 | **Effort:** M | **Repo:** public

Derive contrastive activation directions for concrete style axes (hedging, em-dash usage, list-vs-prose, formality, sentence length) in gemma4:31b and qwen3.6:27b, validate each with blind human-style ratings, and package them as a small library that applies them at inference. Deliverable: a HF repo of named steering vectors plus a demo showing style control without prompt engineering.

**Needs:** nothing

### RSCH-030: Find the language-switch feature in multilingual Gemma

**Scores:** $:0 CV:5 VIR:4 USE:3 ALT:4 | **Effort:** M | **Repo:** public

Using paired prompts identical in meaning across six languages, locate the layers and directions that encode output language independent of content, then causally test them by steering an English prompt into Portuguese output without changing the text. Deliverable: a paper on where language identity lives in the stack, with intervention videos for the demo.

**Needs:** nothing

### RSCH-031: Generate realistic detector glitches with a diffusion model

**Scores:** $:0 CV:5 VIR:4 USE:4 ALT:5 | **Effort:** L | **Repo:** public

Train a small latent diffusion model on Gravity Spy spectrograms to synthesize class-conditional LIGO glitches, then show that augmenting a classifier's training set with synthetic rare-class glitches (Paired Doves, 1080Lines) improves recall on the real held-out set. Deliverable: generator weights on HF, the augmentation ablation, and a paper distinct from any ViT-vs-CNN comparison.

**Needs:** nothing

### RSCH-032: Normalizing-flow parameter estimation for compact binaries on one GPU

**Scores:** $:0 CV:5 VIR:5 USE:3 ALT:5 | **Effort:** XL | **Repo:** public

Implement a DINGO-style simulation-based inference pipeline: generate waveforms with `pycbc`/`lalsuite`, train a normalizing flow to map strain embeddings to posteriors over masses and spins, and validate against published Bayesian posteriors for two real events. Deliverable: sub-second posteriors on consumer hardware, a probability-integral-transform calibration plot, and an arXiv submission.

**Needs:** ~30 GB disk for waveform banks; nothing paid

### RSCH-033: Score-based denoising of gravitational-wave strain

**Scores:** $:0 CV:5 VIR:4 USE:3 ALT:5 | **Effort:** M | **Repo:** public

Train a score model on real O3 noise from GWOSC and use it as a learned prior to denoise injected signals at SNR 6-12, comparing recovered waveform overlap against matched filtering and a plain denoising autoencoder. Deliverable: overlap-vs-SNR curves and an honest negative-result section if the learned prior fails to beat matched filtering.

**Needs:** nothing

### RSCH-034: Unsupervised anomaly detection in LIGO auxiliary channels

**Scores:** $:0 CV:5 VIR:3 USE:2 ALT:5 | **Effort:** M | **Repo:** public

Pull public auxiliary-channel summary data around known glitch times, train an autoencoder or isolation forest on quiet periods, and test whether anomalies in non-strain channels precede strain glitches with usable lead time. Deliverable: a lead-time distribution and a ranked list of the most predictive auxiliary channels.

**Needs:** nothing

### RSCH-035: Small transformer for transit detection in TESS light curves

**Scores:** $:0 CV:4 VIR:3 USE:2 ALT:5 | **Effort:** M | **Repo:** public

Download a manageable slice of TESS two-minute cadence light curves via `lightkurve`, train a time-series transformer to flag planetary transits, and benchmark against the standard box-least-squares pipeline on precision at fixed recall. Deliverable: the model on HF plus a list of candidates the model flags that BLS misses, with vetting notes.

**Needs:** ~25 GB disk for the light-curve subset

### RSCH-036: Variable-star classification from sparse, irregular photometry

**Scores:** $:0 CV:4 VIR:3 USE:2 ALT:5 | **Effort:** M | **Repo:** public

Using public ZTF or ASAS-SN light curves, compare a set-transformer that consumes raw (time, mag, error) triples against the standard feature-engineering-plus-random-forest baseline, specifically on stars with fewer than 50 observations. Deliverable: an accuracy-vs-observation-count curve showing where deep models stop being worth it.

**Needs:** nothing

### RSCH-037: Early classification of astronomical transients under a time budget

**Scores:** $:0 CV:5 VIR:4 USE:2 ALT:5 | **Effort:** M | **Repo:** public

Train a model on ELAsTiCC/PLAsTiCC-style simulated alerts that must classify transients using only the first N days of photometry, and characterize the accuracy-vs-latency frontier that a follow-up telescope scheduler actually cares about. Deliverable: the frontier plot, the model, and a writeup framed for the Rubin alert-broker community.

**Needs:** nothing

### RSCH-038: Pulsar candidate sifting replication with modern methods

**Scores:** $:0 CV:3 VIR:2 USE:2 ALT:4 | **Effort:** S | **Repo:** public

Reproduce published HTRU2 pulsar-candidate results, then test whether gradient boosting, a small MLP, and a tabular transformer differ meaningfully once class imbalance is handled correctly with proper precision-recall reporting instead of accuracy. Deliverable: a short replication note on how much of the published gain survives correct metrics.

**Needs:** nothing

### RSCH-039: CNN dedispersion for fast radio burst candidates

**Scores:** $:0 CV:4 VIR:3 USE:2 ALT:4 | **Effort:** M | **Repo:** public

Simulate dispersed FRB signals in realistic radio noise, train a CNN to estimate dispersion measure directly from the dynamic spectrum, and compare its speed and accuracy against brute-force dedispersion trials. Deliverable: a speedup factor at matched accuracy plus the synthetic dataset on HF.

**Needs:** nothing

### RSCH-040: Solar flare prediction from SHARP magnetogram parameters

**Scores:** $:0 CV:3 VIR:3 USE:2 ALT:5 | **Effort:** S | **Repo:** public

Pull SDO/HMI SHARP active-region parameters, build a strictly time-ordered train/test split (no random shuffling, which is the flaw in much of this literature), and evaluate flare prediction skill scores against a persistence baseline. Deliverable: a short paper on how much published skill disappears under temporal splitting.

**Needs:** nothing

### RSCH-041: Seismic phase picking replication on a STEAD subset

**Scores:** $:0 CV:4 VIR:3 USE:2 ALT:5 | **Effort:** M | **Repo:** public

Train a U-Net phase picker on a 20 GB subset of the STEAD earthquake waveform dataset, reproduce reported P- and S-arrival residuals, then test generalization by evaluating on regions absent from training. Deliverable: an out-of-region degradation table, which the original papers largely skip.

**Needs:** ~20 GB disk

### RSCH-042: Vision-language fine-tune: Minecraft screenshot to structured game state

**Scores:** $:1 CV:5 VIR:5 USE:5 ALT:4 | **Effort:** XL | **Repo:** public

Harvest paired screenshots and ground-truth state from the running Paper server (bot inventory, nearby blocks, health, biome) to build 30-50k labeled frames, then QLoRA a small VLM to emit that state as JSON from pixels alone. Deliverable: a model that gives the bot swarm vision without server-side introspection, published with the dataset and an eval on unseen biomes.

**Needs:** nothing

### RSCH-043: Publish the Minecraft swarm trajectory dataset and a behavior-cloning baseline

**Scores:** $:1 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** XL | **Repo:** public

Instrument the five-bot swarm to log (observation, LLM reasoning, action, outcome) tuples continuously, run it for a week, clean and de-duplicate to a few hundred thousand steps, then train a small behavior-cloning policy and measure how far it gets without the LLM in the loop. Deliverable: an HF dataset of embodied LLM-agent trajectories (a genuinely rare artifact), the policy, and a paper.

**Needs:** ~15 GB disk for the log corpus

### RSCH-044: Latent diffusion trained on illuminated manuscript initials

**Scores:** $:2 CV:4 VIR:5 USE:4 ALT:4 | **Effort:** L | **Repo:** public

Assemble a few thousand public-domain decorated initials from digitized medieval manuscripts (IIIF endpoints from public library collections), train a class-conditional latent diffusion model on letter identity, and evaluate whether it produces legible letters at all, the interesting failure mode. Deliverable: model weights, a letter-legibility eval, and a Space that renders any word as an illuminated line.

**Needs:** confirm each source collection's public-domain/IIIF reuse terms before harvesting

### RSCH-045: A cleanly licensed Latin liturgical corpus with structural annotation

**Scores:** $:0 CV:3 VIR:3 USE:5 ALT:5 | **Effort:** S | **Repo:** public

Assemble public-domain Latin liturgical and devotional texts, normalize orthography, and annotate structure (versicle/response, antiphon, psalm, rubric) plus English parallel text where public-domain translations exist. Deliverable: an HF dataset with provenance per document and a tokenizer-fertility report showing how badly modern tokenizers handle Latin.

**Needs:** nothing

### RSCH-046: The accuracy distribution over 1,000 paraphrases of one task

**Scores:** $:0 CV:4 VIR:5 USE:4 ALT:5 | **Effort:** S | **Repo:** public

Take five fixed tasks, generate 1,000 semantically equivalent prompt paraphrases each with a strong model, verify equivalence by back-translation and human spot-check, then run every paraphrase through three local models. Deliverable: the full accuracy histogram per task, showing that a single-prompt benchmark number is a sample from a distribution with a shockingly wide spread.

**Needs:** nothing

### RSCH-047: Does multi-agent debate help, or is it just more sampling?

**Scores:** $:0 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Run three conditions at matched total token spend: single model, N-way self-consistency, and N-agent debate with critique rounds, across reasoning, factual, and code tasks using local models. Deliverable: a controlled result on whether debate beats the compute-matched sampling baseline, which most debate papers do not properly control for.

**Needs:** nothing

### RSCH-048: In-context learning emergence in tiny transformers on synthetic tasks

**Scores:** $:0 CV:5 VIR:3 USE:2 ALT:4 | **Effort:** M | **Repo:** public

Train small transformers on synthetic function classes (linear regression, sparse parity, Markov chains) and map how the emergence of in-context learning depends on data diversity, depth, and burstiness of the training distribution. Deliverable: a phase diagram of when in-context learning appears and when the model instead memorizes.

**Needs:** nothing

### RSCH-049: Weight-space path from base to instruct

**Scores:** $:0 CV:4 VIR:3 USE:3 ALT:4 | **Effort:** S | **Repo:** public

Linearly interpolate between a base model and its instruct sibling (same family, same size) at 20 points, evaluating instruction-following, refusal rate, perplexity on raw text, and chat-template adherence at each. Deliverable: curves showing whether these properties appear gradually or snap on, and where the best "half-instructed" checkpoint sits for creative-writing use.

**Needs:** nothing

### RSCH-050: Anisotropy and clustering geometry of code embeddings

**Scores:** $:0 CV:4 VIR:3 USE:4 ALT:4 | **Effort:** S | **Repo:** public

Embed a corpus of functions from real repositories with several open embedding models, then measure cosine-similarity anisotropy, effective dimensionality, and whether nearest neighbors cluster by language, by library, or by actual behavior. Deliverable: a report showing which embedding models encode semantics versus surface syntax, with the probe set published for reuse.

**Needs:** nothing

