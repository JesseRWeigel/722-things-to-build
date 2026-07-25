# Local Models & GPU Engineering

Getting the most out of one RTX 5090 with 31 GB usable VRAM and 157 GB of free disk.

### GPU-001: Run a full quantization ladder on one model and publish the curve

**Scores:** $:2 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Take `qwen3.6:27b`, build or download q3_K_M, q4_K_M, q5_K_M, q6_K, and q8_0 GGUFs, then measure perplexity on a held-out slice, tool-call accuracy, tokens/sec, and peak VRAM for each. The interesting output is where the quality cliff sits relative to the VRAM budget, not the individual numbers. Done when a single chart shows quality per GB of VRAM across all five.

**Cost:** VRAM 12-29 GB depending on rung, disk ~85 GB total for all five (delete each rung after measuring to stay under 40 GB peak)

**Needs:** nothing

### GPU-003: Measure Blackwell FP8 and NVFP4 against the usual quants

**Scores:** $:3 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** L | **Repo:** public

The 5090 has fifth-gen tensor cores with native FP4 and FP8 paths that almost nobody has benchmarked on a consumer card. Serve an FP8 and an NVFP4 checkpoint of a ~30B model under vLLM and compare throughput, latency, and quality against GGUF q4_K_M and AWQ int4. Done when a write-up covers all four formats with reproducible commands and sm_120 build notes.

**Cost:** VRAM 16-24 GB; disk ~60 GB across checkpoints, delete as you go

**Needs:** nothing

### GPU-004: Sweep draft models for speculative decoding acceptance rate

**Scores:** $:2 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Pair `qwen3.6:27b` as target with `qwen3:8b`, `qwen3.5:9b`, and a heavily quantized version of itself as drafts, then measure acceptance rate and end-to-end speedup across three workload types (code editing, chat, JSON tool calls). Acceptance rate varies enormously by workload and almost nobody reports it that way. Done when a table gives the best draft per workload with measured speedup.

**Cost:** VRAM ~17 GB target plus 5-7 GB draft, near the practical ceiling; disk none beyond existing models

**Needs:** nothing

### GPU-006: Head-to-head serving stack matrix at a fixed VRAM budget

**Scores:** $:3 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Give vLLM, llama.cpp server, and Ollama the same 24 GB budget and the same model, then measure single-stream latency, throughput at concurrency 1/4/16/32, time to first token, and memory overhead. Extend the existing `vllm-5090-bench` directory rather than starting over. Done when the matrix is complete and the crossover points between stacks are identified.

**Cost:** VRAM 24 GB cap enforced per run; disk ~20 GB for one shared model in two formats

**Needs:** nothing

### GPU-007: Quantify prefix caching for agent-shaped workloads

**Scores:** $:3 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Agent sessions resend an enormous shared prefix on every turn, which is exactly what automatic prefix caching is for. Replay 50 real multi-turn agent sessions through vLLM with APC on and off and report tokens saved, TTFT reduction, and the VRAM cost of the cache blocks. Done when the report shows the break-even session length.

**Cost:** VRAM base model plus 2-6 GB of cache blocks; disk zero

**Needs:** nothing

### GPU-008: Find the concurrency knee for continuous batching

**Scores:** $:2 CV:4 VIR:3 USE:5 ALT:4 | **Effort:** M | **Repo:** public

Sweep concurrent request count from 1 to 64 against a served model and plot aggregate throughput and p95 per-request latency to locate the point where added concurrency stops helping. Publish the derived max-num-seqs and max-model-len settings as a tuned config file. Done when the tuned config beats defaults on aggregate throughput at acceptable p95.

**Cost:** VRAM ~20 GB plus KV cache scaling with concurrency; disk zero

**Needs:** nothing

### GPU-009: Test whether KV cache quantization breaks long-context recall

**Scores:** $:3 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Q8 and Q4 KV cache roughly double or quadruple usable context on a 32 GB card, but the quality cost is usually reported as perplexity, which hides retrieval failure. Run a needle-in-haystack and a multi-hop retrieval eval at fp16, q8, and q4 KV across 8k to 64k context. Done when the recall-versus-cache-precision curve is plotted for at least two models.

**Cost:** VRAM 18-30 GB depending on context and cache precision; disk zero

**Needs:** nothing

### GPU-010: Empirically fitted VRAM calculator for this exact card

**Scores:** $:2 CV:3 VIR:4 USE:5 ALT:5 | **Effort:** S | **Repo:** public

Online VRAM calculators use theoretical formulas that miss allocator overhead, CUDA graph buffers, and fragmentation. Measure actual peak VRAM across 30 real model-and-context configurations, fit a regression, and ship a CLI that answers "will this fit" with a measured error bar. Done when predictions land within 1 GB on ten held-out configurations.

**Cost:** VRAM up to 31 GB during measurement; disk zero beyond existing models

**Needs:** nothing

### GPU-011: Measure the real cost of offloading MoE experts to CPU

**Scores:** $:2 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

With `qwen3.6:35b-a3b` and `gemma4:26b-a4b`, sweep how many expert layers get pushed to CPU with llama.cpp's override-tensor flags and plot tokens/sec against VRAM freed. This is the technique that lets a bigger MoE coexist with a second model on one card. Done when the curve identifies the offload fraction that costs under 20 percent throughput.

**Cost:** VRAM 8-23 GB tunable, system RAM up to 20 GB when heavily offloaded; disk zero

**Needs:** nothing

### GPU-015: Retrain the Minecraft bot brain from swarm telemetry

**Scores:** $:2 CV:4 VIR:5 USE:5 ALT:3 | **Effort:** L | **Repo:** public

The existing `qwen3-minecraft:8b` was trained early. Rebuild the dataset from months of accumulated swarm episodes, label outcomes with whether the bot's plan actually succeeded in-game, and train on successful trajectories only. Done when the new model raises task-completion rate over the current brain on a fixed set of 30 in-game objectives.

**Cost:** VRAM ~12 GB training, ~6 GB serving five bots off one instance; disk ~20 GB

**Needs:** nothing

### GPU-016: Merge two Qwen fine-tunes with mergekit and see what survives

**Scores:** $:2 CV:4 VIR:4 USE:4 ALT:4 | **Effort:** M | **Repo:** public

Merge the code-style LoRA and the commit-message LoRA into one base with TIES, DARE, and linear methods, then evaluate whether each capability survives the merge or interferes. Merging is widely done and rarely measured for interference. Done when a table shows per-capability scores for base, each adapter alone, and each merge method.

**Cost:** VRAM ~10 GB for evaluation, merging is mostly CPU and RAM bound; disk ~30 GB for merge outputs

**Needs:** nothing

### GPU-017: Depth-upscale a small model and test whether it is worth the VRAM

**Scores:** $:2 CV:4 VIR:5 USE:3 ALT:4 | **Effort:** M | **Repo:** public

Build a frankenmerge by duplicating middle layers of `qwen3.5:9b` into a ~13B model, heal it with a short LoRA pass, and measure whether it outperforms the original at its new VRAM cost or just gets slower. A clean negative result is a publishable finding here. Done when the upscaled model is benchmarked against both the 9B original and a genuine 14B-class model.

**Cost:** VRAM ~18 GB for the healed model, ~14 GB for the healing pass; disk ~35 GB

**Needs:** nothing

### GPU-018: Steer output format with activation vectors instead of prompting

**Scores:** $:3 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Extract steering vectors for traits the fleet actually cares about (terse versus verbose, JSON-strict, admits uncertainty) by contrasting activations on paired prompts, then apply them at inference in a transformers serving path and measure whether they beat prompt instructions for reliability. Done when at least one trait is controlled more reliably by a vector than by an instruction, with numbers.

**Cost:** VRAM ~16 GB (needs a transformers path, not GGUF); disk ~18 GB for fp16 weights of one mid-size model

**Needs:** nothing

### GPU-019: Embed and index every project on the machine

**Scores:** $:3 CV:4 VIR:3 USE:5 ALT:4 | **Effort:** M | **Repo:** public

Chunk all source, markdown, and notes under `~/Projects` with a code-aware splitter, embed locally with a small embedding model, store in sqlite-vec, and expose retrieval over MCP. Measure end-to-end index time and query latency so the pipeline is honest about cost. Done when a full rebuild completes in under an hour and queries return in under 200 ms.

**Cost:** VRAM ~3 GB for the embedder; disk ~4 GB for the index

**Needs:** nothing

### GPU-021: Distill a cross-encoder reranker for the local RAG stack

**Scores:** $:3 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Use a strong model to score query-document relevance across the GPU-019 corpus, then train a small cross-encoder on those scores with sentence-transformers so reranking runs in milliseconds locally. Measure the retrieval quality gain from reranking the top 50 down to the top 5. Done when the reranker adds a measured nDCG gain at under 50 ms for 50 pairs.

**Cost:** VRAM ~6 GB training, under 2 GB serving; disk ~5 GB

**Needs:** nothing

### GPU-022: Benchmark grammar-constrained decoding implementations

**Scores:** $:3 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Compare xgrammar, outlines, llama.cpp GBNF, and plain prompted JSON on schema validity rate, tokens/sec penalty, and whether constraining hurts semantic quality of the values inside a valid structure. That last question is the one people skip. Done when all four are scored on 500 tool-call schemas of varying nesting depth.

**Cost:** VRAM ~18 GB for one shared model; disk zero

**Needs:** nothing

### GPU-023: Test how quantization degrades tool-call correctness specifically

**Scores:** $:3 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** S | **Repo:** public

Perplexity barely moves from q8 to q4 while structured output can fall apart, so score each rung of GPU-001 on function selection accuracy, required-argument presence, and enum validity across 300 tool-call prompts. Done when the tool-call accuracy curve is plotted alongside the perplexity curve and the divergence is visible.

**Cost:** VRAM 12-29 GB reusing GPU-001 artifacts; disk zero if run alongside GPU-001

**Needs:** nothing

### GPU-024: Confidence cascade that escalates only when the small model is unsure

**Scores:** $:4 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Route every request to `gemma4:e4b` first, compute a confidence signal (mean token logprob, self-consistency across three samples, or a trained probe), and escalate to a 27-30B model or an API only below threshold. Tune the threshold on a labeled set to hit a target accuracy at minimum cost. Done when the cascade matches large-model accuracy on a benchmark at under 40 percent of its compute.

**Cost:** VRAM ~10 GB with the small model resident and the large one loaded on demand; disk zero

**Needs:** nothing

### GPU-025: Idle-GPU batch job queue

**Scores:** $:2 CV:4 VIR:3 USE:5 ALT:4 | **Effort:** M | **Repo:** public

A persistent queue where jobs (embedding backfills, bulk classification, eval runs) wait for the GPU to be idle for 60 seconds, then run and yield immediately when an interactive request arrives. Turns overnight and lunch-break idle time into throughput. Done when a 6-hour embedding backfill completes across scattered idle windows without ever blocking interactive use.

**Cost:** VRAM whatever the queued job needs, released on preemption; disk small for the queue database

**Needs:** nothing

### GPU-026: Disk-aware model garbage collector driven by real usage

**Scores:** $:2 CV:3 VIR:2 USE:5 ALT:4 | **Effort:** S | **Repo:** public

Parse Ollama server logs for per-model load counts and last-used timestamps, cross-reference with on-disk size, and produce an eviction ranking that maximizes GB reclaimed per unit of regret. With 157 GB free and 250 GB of models on disk, this pays for itself immediately. Done when it reports a ranked eviction list with cumulative GB reclaimed.

**Cost:** VRAM zero; frees disk, does not consume it

**Needs:** nothing

### GPU-027: Automate the Hugging Face to GGUF conversion pipeline

**Scores:** $:2 CV:4 VIR:3 USE:5 ALT:5 | **Effort:** M | **Repo:** public

One command that takes an HF repo id, downloads only the needed shards, converts to f16 GGUF, produces requested quants with an optional imatrix, writes a Modelfile, registers with Ollama, and deletes intermediates as it goes so peak disk stays bounded. The disk-bounded streaming behavior is the whole point. Done when a 30B model converts start to finish with peak disk usage under 45 GB.

**Cost:** VRAM zero for conversion; disk peak bounded to roughly 2.2x the final quant size

**Needs:** nothing

### GPU-028: Build a TensorRT-LLM engine for sm_120 and see if it is worth it

**Scores:** $:3 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** XL | **Repo:** public

Blackwell consumer support in TensorRT-LLM is rough, and a working end-to-end recipe for the 5090 would be genuinely valuable to a lot of people. Build engines for one 8B and one 27B model, benchmark against vLLM, and document every compilation failure and workaround. Done when either a reproducible recipe with a speedup number exists or a clear write-up of why it does not pay off yet.

**Cost:** VRAM up to 31 GB during engine build; disk ~60 GB for toolchain, sources, and engines

**Needs:** nothing

### GPU-029: Squeeze single-stream latency with torch.compile and CUDA graphs

**Scores:** $:2 CV:5 VIR:3 USE:4 ALT:4 | **Effort:** S | **Repo:** public

For a small model used in a hot loop (classification, routing, embeddings), measure the latency reduction from torch.compile with mode reduce-overhead plus CUDA graph capture, and record the compilation warmup cost so the break-even request count is explicit. Done when per-call latency and break-even count are both reported.

**Cost:** VRAM ~6 GB plus graph capture overhead; disk ~2 GB for compile cache

**Needs:** nothing

### GPU-030: Plot the power-limit versus throughput curve

**Scores:** $:2 CV:4 VIR:5 USE:5 ALT:5 | **Effort:** S | **Repo:** public

Sweep `nvidia-smi -pl` from 300 W to 575 W in 25 W steps under a fixed inference load and plot tokens/sec and tokens per watt-hour. The usual finding is that the top 25 percent of power buys single-digit performance, which is directly actionable for anyone running a 5090 all night. Done when the efficiency knee is identified and set as the default.

**Cost:** VRAM ~18 GB for the load model; disk zero

**Needs:** nvidia-smi power limit changes may require the Windows host driver to permit it under WSL2

### GPU-031: Log thermal and clock behavior under sustained load

**Scores:** $:1 CV:3 VIR:3 USE:5 ALT:4 | **Effort:** S | **Repo:** public

Run a two-hour saturating inference load while sampling temperature, clocks, power draw, and throttle reasons every second, then plot where and why sustained throughput drops below the first-minute number. Benchmarks that report a 60-second average are lying about overnight jobs. Done when the sustained-versus-burst throughput gap is quantified.

**Cost:** VRAM ~18 GB; disk trivial

**Needs:** nothing

### GPU-032: Long-context recall across every local model at 8k to 128k

**Scores:** $:3 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Run a RULER-style suite (single needle, multi-needle, variable tracking, aggregation) across the local model zoo at 8k, 16k, 32k, 64k, and 128k where each model claims support, recording both accuracy and the VRAM required to reach each length. Advertised context length and usable context length are rarely the same number. Done when a grid of model by context length by task is complete and published.

**Cost:** VRAM up to 31 GB at the longest contexts, several configurations will not fit and that is a result; disk zero

**Needs:** nothing

### GPU-033: Check whether a LoRA survives quantization

**Scores:** $:2 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** S | **Repo:** public

Take the GPU-013 commit-message adapter, merge it into the base at fp16, quantize the merged model to q4_K_M, and measure how much of the fine-tuned behavior remains versus the fp16 merge. Everyone quantizes their fine-tunes and almost nobody measures the loss. Done when the retained-behavior percentage is reported for q8 and q4.

**Cost:** VRAM ~14 GB for the fp16 comparison; disk ~20 GB

**Needs:** nothing

### GPU-034: Synthetic training data pipeline with dedup and decontamination

**Scores:** $:3 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** XL | **Repo:** public

Build a reusable pipeline that generates instruction data with a local model, filters by a rubric judge, deduplicates with MinHash, decontaminates against every eval set in use, and reports a data card with source distribution and rejection rates. Every fine-tune task in this file depends on it. Done when it produces a 20k-example set with a published data card and zero eval overlap.

**Cost:** VRAM ~20 GB during generation; disk ~10 GB per generated dataset

**Needs:** nothing

### GPU-035: Local vision model as a screenshot-understanding service for agents

**Scores:** $:3 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Serve a Qwen3-VL-class model behind an HTTP endpoint that takes a screenshot and a question and returns structured output, then wire it into the Playwright loop so agents can verify UI changes visually without burning frontier vision tokens. Benchmark accuracy on 100 labeled screenshots from his own projects. Done when the local model handles the routine checks and escalation to a cloud model is rare.

**Cost:** VRAM ~10-18 GB depending on the size chosen; disk ~20 GB

**Needs:** nothing

### GPU-036: Benchmark local speech recognition throughput

**Scores:** $:2 CV:4 VIR:3 USE:4 ALT:4 | **Effort:** S | **Repo:** public

Compare whisper.cpp, faster-whisper, and a Parakeet model on the same hour of audio for real-time factor, word error rate, and VRAM, including batched offline mode versus streaming. Establishes whether voice input to the agent fleet is practical locally. Done when the fastest configuration meeting a WER target is identified and documented.

**Cost:** VRAM 2-6 GB; disk ~8 GB for all candidate models

**Needs:** a labeled audio sample for WER measurement, a public test set is fine

### GPU-037: Local text-to-speech service with measured latency

**Scores:** $:2 CV:4 VIR:3 USE:4 ALT:4 | **Effort:** S | **Repo:** public

Stand up a Kokoro-class TTS model behind a streaming endpoint and measure time to first audio and real-time factor at several concurrency levels, so agent notifications and the Discord bridge can speak without an API. Done when first audio arrives in under 300 ms for a typical sentence.

**Cost:** VRAM under 2 GB; disk ~2 GB

**Needs:** nothing

### GPU-039: Tune batched embedding throughput to saturate the card

**Scores:** $:2 CV:3 VIR:2 USE:5 ALT:4 | **Effort:** S | **Repo:** public

Sweep batch size, sequence truncation length, and fp16 versus int8 for the chosen embedder and find the configuration that maximizes documents per second without OOM. Cuts the GPU-019 index rebuild from an hour to minutes. Done when the tuned throughput is at least triple the naive default.

**Cost:** VRAM 3-12 GB depending on batch size; disk zero

**Needs:** nothing

### GPU-040: Measure cold-start cost of loading models from disk

**Scores:** $:2 CV:3 VIR:3 USE:5 ALT:4 | **Effort:** S | **Repo:** public

Time model load from cold page cache versus warm for every model in the zoo, broken down by file size and by mmap versus full read, and check whether WSL2's filesystem layer adds a penalty over native Linux. Determines whether keeping a model resident is worth the VRAM. Done when a load-time table exists for every installed model and the keep-alive policy is set from it.

**Cost:** VRAM transient during load; disk zero

**Needs:** nothing

### GPU-041: Break-even calculator for local inference versus API

**Scores:** $:3 CV:4 VIR:5 USE:5 ALT:5 | **Effort:** S | **Repo:** public

Combine measured tokens/sec, measured watts from GPU-030, a configurable electricity rate, and amortized hardware cost into a calculator that reports the true dollar cost per million local tokens and compares it to current API prices per model tier. Publish it as a small static site. Done when it produces a defensible cost-per-million-tokens number for three local models.

**Cost:** VRAM zero beyond the measurement runs it consumes; disk trivial

**Needs:** nothing

### GPU-042: Publish the 5090 benchmark corpus as a dataset and a leaderboard Space

**Scores:** $:3 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** L | **Repo:** public

Aggregate results from the benchmarking tasks in this file into a structured Hugging Face dataset with a fixed schema (model, quant, backend, context, batch, tokens/sec, VRAM, quality metric, driver version) and build a Gradio Space that renders filterable comparisons and accepts community submissions. There is no good consumer-GPU inference leaderboard and this could become the reference one. Done when the Space is live with at least 60 measured configurations.

**Cost:** VRAM zero for the Space, it hosts data only; disk trivial

**Needs:** nothing

### GPU-043: Prune a model with Wanda and see whether it beats quantizing

**Scores:** $:2 CV:5 VIR:4 USE:3 ALT:4 | **Effort:** L | **Repo:** public

Apply Wanda or SparseGPT 2:4 structured pruning to a mid-size model, measure whether Blackwell's sparse tensor core support actually delivers the theoretical speedup, and compare quality per GB against simply quantizing to a lower rung. Pruning is usually compared against dense fp16, which is the wrong baseline for a VRAM-constrained user. Done when pruned and quantized variants are compared at equal memory footprint.

**Cost:** VRAM ~24 GB during pruning, ~12 GB for the pruned model; disk ~40 GB

**Needs:** nothing

### GPU-044: Test-time compute versus a bigger model at equal wall-clock

**Scores:** $:3 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Give `gemma4:e4b` and `qwen3.5:9b` the same wall-clock budget as one pass of `qwen3.6:27b` and spend it on best-of-n with a verifier, self-consistency, or iterative refinement, then compare accuracy on reasoning and coding benchmarks. On a single card, wall-clock is the honest axis of comparison. Done when the crossover point where small-plus-sampling beats large-single-pass is identified per task type.

**Cost:** VRAM ~10 GB for the small model with room for a verifier; disk zero

**Needs:** nothing

### GPU-046: Serve many LoRA adapters off one base model with hot swapping

**Scores:** $:4 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Load one base model in vLLM with multi-LoRA enabled and serve the commit-message, code-style, and Minecraft adapters as separate model names, then measure per-adapter overhead and the throughput cost of mixed-adapter batches. This is how one card serves five specialized models on 20 GB. Done when three adapters serve concurrently with measured overhead under 10 percent.

**Cost:** VRAM ~20 GB base plus roughly 200 MB per adapter; disk ~2 GB per adapter

**Needs:** nothing

### GPU-047: Quantify Ollama model-swap thrashing

**Scores:** $:2 CV:3 VIR:3 USE:5 ALT:4 | **Effort:** S | **Repo:** public

When the agent fleet alternates between models, Ollama evicts and reloads constantly. Instrument a realistic mixed workload, count swaps, measure time lost to reloading, and test whether keep-alive tuning, model ordering, or pinning the small model resident recovers most of it. Done when time lost to swapping is measured before and after a tuned configuration.

**Cost:** VRAM up to 31 GB during the workload; disk zero

**Needs:** nothing

### GPU-048: Four quantization formats, one VRAM budget, one honest comparison

**Scores:** $:3 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** XL | **Repo:** public

Take one model family and produce GGUF q4_K_M, AWQ int4, GPTQ int4, and EXL3 versions all sized to fit in 20 GB, then score every one on the same quality suite, the same throughput harness, and the same long-context test on the same driver and the same day. Cross-format comparisons in the wild are almost always confounded by different hardware or different evals. Done when a single reproducible report covers all four with methodology sufficient for someone else to rerun it.

**Cost:** VRAM 20 GB cap per run; disk ~80 GB peak across formats, requires sequential build and delete to stay within the 157 GB budget

**Needs:** nothing

### GPU-049: Contamination checker for every fine-tune and eval pairing

**Scores:** $:2 CV:5 VIR:3 USE:5 ALT:5 | **Effort:** S | **Repo:** public

An n-gram and MinHash tool that takes a training set and an eval set and reports overlap rate, the specific colliding examples, and a pass or fail against a threshold, run as a gate before any fine-tune in this file is evaluated. Done when it is wired into the training pipeline as a blocking step with a published overlap report per run.

**Cost:** VRAM zero, CPU and RAM only; disk trivial

**Needs:** nothing

### GPU-050: Autotuner that searches the whole serving configuration space

**Scores:** $:4 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** XL | **Repo:** public

Given a model, a VRAM ceiling, and an objective (minimize p95 latency, maximize throughput, maximize context), run Bayesian optimization over backend, quantization, KV cache precision, batch settings, speculative decoding on or off, draft model choice, and power limit, then emit the winning config file. Every other benchmark in this file becomes a single point this searches over. Done when the autotuner beats hand-tuned settings on two objectives for two different models.

**Cost:** VRAM up to 31 GB across trials; disk ~30 GB for the candidate model formats it needs on hand

**Needs:** nothing

