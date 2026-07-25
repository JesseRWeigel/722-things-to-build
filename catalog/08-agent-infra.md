# Agent Infrastructure & Self-Improvement

Tooling that makes the agent fleet itself faster, cheaper, safer, and measurably better over time.

### AGENT-001: Build a VCR-style cassette recorder for every LLM call the fleet makes

**Scores:** $:2 CV:5 VIR:3 USE:5 ALT:4 | **Effort:** L | **Repo:** public

Ship a Node proxy that sits in front of Ollama, OpenRouter, and the Anthropic endpoint, hashes each request (model + messages + tools + temperature) and writes the response to a content-addressed cassette store on disk. A replay mode serves cached responses so prompt refactors can be re-run hundreds of times at zero cost and zero latency. Done when a recorded SIBT run replays end to end offline with byte-identical tool calls.

**Needs:** nothing

### AGENT-003: Full-text plus vector search over every Claude Code transcript

**Scores:** $:2 CV:4 VIR:3 USE:5 ALT:3 | **Effort:** M | **Repo:** public

Index every `.jsonl` under `~/.claude/projects` into SQLite FTS5 plus a local embedding table from `qwen3.5:9b`, exposed as an MCP server with `search_transcripts` and `get_session_slice` tools. Queries like "when did I last fix a Vercel commit-author bug" should return the exact message range. Done when the index rebuilds incrementally in under 30 seconds.

**Needs:** nothing

### AGENT-004: Workstation vitals MCP server so agents can self-govern

**Scores:** $:1 CV:3 VIR:2 USE:5 ALT:3 | **Effort:** S | **Repo:** public

A tiny stdio MCP server exposing `gpu_status` (VRAM free, utilization, temp), `disk_status` (free GB, largest model dirs), `ram_status`, and `running_agents`. Agents call it before starting a heavy job instead of guessing. Done when it is registered globally and a test agent correctly declines to load a 23 GB model with 8 GB VRAM free.

**Needs:** nothing

### AGENT-005: PreToolUse hook that enforces a hard disk floor

**Scores:** $:0 CV:2 VIR:1 USE:5 ALT:2 | **Effort:** S | **Repo:** public

A hook that intercepts `ollama pull`, `hf download`, `git clone`, and `docker pull` in Bash calls, estimates the download size, and blocks the command if it would drop free disk below 40 GB. The denial message tells the agent which cached models are least recently used. Done when a pull of a 40 GB model is refused with a specific eviction suggestion.

**Needs:** nothing

### AGENT-006: Unified cost ledger across Claude, Codex, Gemini, and OpenRouter

**Scores:** $:3 CV:4 VIR:3 USE:5 ALT:4 | **Effort:** M | **Repo:** public

Parse Claude Code transcript usage blocks, Codex session logs, and OpenRouter's generation API into one SQLite ledger with columns for project, session, model, tokens, cached tokens, and dollar cost. Ship a `fleet-cost` CLI with `today`, `by-repo`, and `worst-sessions` views. Done when a week of real usage reconciles against OpenRouter's own billing page within 2 percent.

**Needs:** nothing

### AGENT-007: Context spend flamegraph for a single agent session

**Scores:** $:2 CV:5 VIR:4 USE:5 ALT:4 | **Effort:** M | **Repo:** public

Render one session's token consumption as a flamegraph where width is tokens and depth is tool-call nesting, so a 40k-token `Read` of a lockfile shows up as an obvious slab. Output a standalone HTML file with hover detail. Done when running it on a real SIBT session identifies the three largest avoidable context sinks.

**Needs:** nothing

### AGENT-008: Measure which skills actually fire and which are dead weight

**Scores:** $:1 CV:3 VIR:3 USE:5 ALT:4 | **Effort:** S | **Repo:** public

Scan all transcripts for skill invocations, cross-reference against the installed skill inventory, and report hit counts, last-used dates, and skills that have never fired once. Include a token-cost estimate for skills whose descriptions load into every session. Done when the report names at least five skills worth uninstalling.

**Needs:** nothing

### AGENT-010: Git worktree pool manager for parallel agents

**Scores:** $:2 CV:4 VIR:2 USE:5 ALT:4 | **Effort:** M | **Repo:** public

A `wtpool` CLI that pre-creates and warms N worktrees per repo (dependencies installed, build cache primed), hands them out under lease, and returns them clean. Cuts the cold-start cost of every parallel agent dispatch in Taisho. Done when eight agents can claim, use, and release worktrees on `HunterPath` with no npm install in the critical path.

**Needs:** nothing

### AGENT-011: Speculative agent execution with a judge picking the winner

**Scores:** $:3 CV:5 VIR:5 USE:5 ALT:4 | **Effort:** L | **Repo:** public

For a well-specified task, dispatch three agents into three worktrees with deliberately different strategies (test-first, minimal-diff, refactor-heavy), run the test suite on each, and have a judge model rank the surviving patches against the original spec. Losing worktrees are discarded automatically. Done when it beats single-agent success rate on 20 tasks from the AGENT-002 benchmark.

**Needs:** nothing

### AGENT-012: Shared blackboard protocol with leases for multi-agent coordination

**Scores:** $:3 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** XL | **Repo:** public

Design and implement a SQLite-backed blackboard where agents post facts, claim work items with expiring leases, and subscribe to topics, exposed over MCP so any Claude Code or Codex session can join. Include lease renewal, crash recovery via lease expiry, and an append-only audit log. Done when five agents coordinate a cross-repo refactor with no duplicated work and no lost items after a forced kill of two of them.

**Needs:** nothing

### AGENT-013: Session fork and time-travel debugger

**Scores:** $:3 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Given a transcript file and a message index, reconstruct the exact context at that point and relaunch a fresh session from it with an edited system prompt or an injected correction. Combined with AGENT-001 cassettes, this makes "what if the agent had known X at turn 40" a cheap experiment. Done when a known failed run is forked, corrected at the divergence point, and completes successfully.

**Needs:** nothing

### AGENT-014: Watchdog for stuck agents and orphaned background processes

**Scores:** $:1 CV:3 VIR:2 USE:5 ALT:3 | **Effort:** S | **Repo:** public

A daemon that watches transcript mtimes and `nohup` child processes, flags any agent with no tool call in 10 minutes or any background process with zero output growth in 30, and pushes an ntfy alert with the last three tool calls. Includes a `--reap` mode for confirmed zombies. Done when it catches a real hung SIBT run.

**Needs:** nothing

### AGENT-015: Failure taxonomy classifier for agent runs

**Scores:** $:2 CV:4 VIR:3 USE:5 ALT:4 | **Effort:** M | **Repo:** public

Define a 12-category failure taxonomy (wrong file, hallucinated API, loop, premature success claim, permission denial, context exhaustion, and so on), label 200 failed runs by hand, then fine-tune or few-shot `gemma4:e4b` to classify the rest in bulk. Output a monthly Pareto chart of what actually breaks. Done when classifier agreement with hand labels exceeds 85 percent on a held-out set.

**Needs:** nothing

### AGENT-016: Prompt-injection canary suite for every installed MCP server

**Scores:** $:3 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Build a harness that feeds each MCP tool a response containing embedded instructions (exfiltrate a file, disable a hook, approve a pairing) and records whether the agent complies. Covers the Discord bridge, mempalace, context7, and the Playwright tools. Publish results as a defensive report plus a reusable test runner other people can point at their own servers. Done when every installed server has a pass or fail row and the failures are filed as issues.

**Needs:** nothing

### AGENT-017: Outbound secret-leak scanner as a PreToolUse hook

**Scores:** $:2 CV:4 VIR:3 USE:5 ALT:5 | **Effort:** S | **Repo:** public

Intercept every tool call that sends text off the machine (Discord reply, gh issue create, WebFetch bodies, Artifact publish) and scan the payload with gitleaks-style regex plus an entropy check. Block and explain on a hit. Done when it blocks a synthetic `OPENROUTER_API_KEY` pasted into a Discord reply.

**Needs:** nothing

### AGENT-018: Sandboxed command execution without Docker

**Scores:** $:3 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** L | **Repo:** public

There is no running Docker daemon, so build sandboxing on `bubblewrap` plus user namespaces: read-only bind of the repo, a writable overlay, no network by default, and a seccomp profile. Expose it as a `sbx` wrapper the fleet uses for running untrusted generated code. Done when a generated script that tries `rm -rf ~` and an outbound curl both fail harmlessly.

**Needs:** `bubblewrap` installed via apt

### AGENT-019: Caching, rate-limiting, auditing MCP proxy

**Scores:** $:3 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** L | **Repo:** public

One stdio-to-stdio proxy that fronts all MCP servers, adds per-tool response caching with TTLs, per-server rate limits, a full audit log of arguments and results, and a kill switch per tool. Configuration lives in a single YAML. Done when context7 doc lookups are served from cache on repeat and the audit log reconstructs a full session's MCP activity.

**Needs:** nothing

### AGENT-020: MCP server registry and health checker

**Scores:** $:2 CV:3 VIR:2 USE:5 ALT:4 | **Effort:** S | **Repo:** public

A `mcpdoctor` CLI that reads every `.mcp.json` and settings file on the machine, starts each server in isolation, times the handshake, lists tools, and reports which servers are broken, slow, or duplicated across scopes. Include a token-cost estimate for each server's tool descriptions. Done when it produces a clean table for all currently installed servers.

**Needs:** nothing

### AGENT-023: Cost-aware router that decides local versus cloud per subtask

**Scores:** $:4 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

A classifier that reads a subtask description and routes it to `gemma4:e4b`, `qwen3-coder:30b`, or a frontier API based on predicted difficulty and required context, with a measured escalation path when the local model's output fails validation. Train the classifier on the AGENT-015 outcome labels. Done when it cuts API spend on a Taisho sweep by half with no drop in merged-PR rate.

**Needs:** nothing

### AGENT-024: OpenRouter free-tier scheduler

**Scores:** $:3 CV:4 VIR:3 USE:5 ALT:5 | **Effort:** M | **Repo:** public

A queue that tracks per-model free-tier rate limits on OpenRouter, rotates across eligible models, backs off on 429s, and exposes a single OpenAI-compatible endpoint so bulk labeling jobs run at zero cost overnight. Persist limit state so a restart does not blow the budget. Done when it labels 10,000 items across a night with no paid spend.

**Needs:** nothing

### AGENT-026: Snapshot regression tests for prompts and skills

**Scores:** $:3 CV:5 VIR:3 USE:5 ALT:5 | **Effort:** M | **Repo:** public

A vitest-style runner where each test is a prompt, a fixture repo, and a set of assertions over the resulting tool-call sequence, run against cassettes so it executes in CI for free. Editing a skill then shows exactly which behaviors changed. Done when a deliberate regression in a skill's wording is caught by a red test.

**Needs:** nothing

### AGENT-028: Replace mempalace's retrieval with a locally embedded hybrid index

**Scores:** $:3 CV:4 VIR:3 USE:5 ALT:4 | **Effort:** M | **Repo:** public

Add a local embedding index over drawer contents with BM25 fusion and reciprocal-rank fusion scoring, benchmarked against the current search on a hand-built set of 100 real recall queries. Keep the existing tool surface unchanged. Done when recall@5 improves by a measured margin on that set.

**Needs:** nothing

### AGENT-029: Cross-repo symbol index exposed over MCP

**Scores:** $:3 CV:5 VIR:3 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Run tree-sitter across every repo in `~/Projects`, build a symbol and reference table, and expose `find_symbol`, `find_references`, and `who_calls` MCP tools that work across repo boundaries. Lets an agent answer "where else did I implement this Ollama retry logic" without grepping blind. Done when it resolves a symbol shared between `toryo` and `mineflayer-chatgpt`.

**Needs:** nothing

### AGENT-030: Predict task difficulty before dispatching an agent

**Scores:** $:3 CV:5 VIR:3 USE:5 ALT:4 | **Effort:** M | **Repo:** public

Using historical run outcomes, train a small model on features (files touched, test coverage of the area, repo age, ambiguity score of the prompt) to predict expected duration, token cost, and failure probability. Taisho uses the prediction to choose model tier and to refuse tasks over a risk threshold. Done when predicted cost correlates above 0.6 with actual on held-out runs.

**Needs:** nothing

### AGENT-031: Visualize the fleet's message graph

**Scores:** $:2 CV:4 VIR:4 USE:4 ALT:4 | **Effort:** S | **Repo:** public

Parse teammate messages and subagent spawns from transcripts into a directed graph, then render an interactive HTML view where node size is token spend and edge thickness is message volume. Reveals which agent is a bottleneck and which never gets consulted. Done when it renders a real multi-agent session including the catalog run itself.

**Needs:** nothing

### AGENT-032: Deadlock and livelock detector for agent teams

**Scores:** $:2 CV:4 VIR:3 USE:5 ALT:4 | **Effort:** S | **Repo:** public

Watch the message graph in real time for cycles where every agent is blocked waiting on another, and for repeated identical tool-call sequences that indicate a livelock. Alert with the cycle members and the repeated call. Done when it detects a synthetic two-agent wait cycle within 60 seconds.

**Needs:** nothing

### AGENT-033: Evaluate whether compaction destroys the things that matter

**Scores:** $:2 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Take long sessions, capture the pre-compaction context and the post-compaction summary, and score whether specific facts (file paths, decisions, user corrections, failed approaches) survived. Build a fact-survival rate metric and test alternative compaction prompts against it. Done when a measurably better compaction prompt is identified and documented.

**Needs:** nothing

### AGENT-034: Lint and dependency-graph the skill library

**Scores:** $:2 CV:3 VIR:2 USE:5 ALT:5 | **Effort:** S | **Repo:** public

A linter that checks every skill for a triggering description, broken relative file references, dead `${CLAUDE_PLUGIN_ROOT}` paths, overlapping trigger phrases with other skills, and body length, plus a graph of which skills reference which. Done when it runs clean over the whole installed set after fixes.

**Needs:** nothing

### AGENT-035: Semantic differ for two agents' competing patches

**Scores:** $:2 CV:5 VIR:4 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Given two diffs solving the same task, produce a structured comparison: which files each touched uniquely, where they agree semantically despite textual difference, where they contradict, and which introduces more new dependencies. Backs the AGENT-011 judge with evidence instead of vibes. Done when it correctly reports "functionally equivalent" for two renamed-variable versions of the same fix.

**Needs:** nothing

### AGENT-036: Profile tool-call latency across the whole fleet

**Scores:** $:1 CV:3 VIR:2 USE:5 ALT:4 | **Effort:** S | **Repo:** public

Extract per-tool wall-clock timings from transcripts and produce a p50/p95/p99 table by tool and by MCP server, plus a list of the slowest individual calls with their arguments. Done when it identifies the three slowest tools in real usage and each has a filed follow-up.

**Needs:** nothing

### AGENT-037: Explain why every agent run ended

**Scores:** $:1 CV:3 VIR:3 USE:5 ALT:4 | **Effort:** S | **Repo:** public

Classify session terminations into completed, context-exhausted, user-interrupted, error, permission-denied, and silently-drifted, then report the distribution per repo and per model. Silent drift, where the agent stops without finishing and without saying so, is the interesting bucket. Done when a month of runs is classified and the drift cases are enumerated.

**Needs:** nothing

### AGENT-040: Garbage-collect stale worktrees, branches, and agent scratch dirs

**Scores:** $:1 CV:2 VIR:1 USE:5 ALT:3 | **Effort:** S | **Repo:** public

Find worktrees with no commits in 14 days, local branches whose remotes are gone, and orphaned scratch directories, report reclaimable bytes, and delete only after confirmation. Directly addresses the 157 GB disk constraint. Done when a dry run reports the reclaimable total across all repos.

**Needs:** nothing

### AGENT-041: GPU lease broker so agents stop fighting over VRAM

**Scores:** $:2 CV:4 VIR:3 USE:5 ALT:4 | **Effort:** M | **Repo:** public

A small daemon holding a VRAM budget that agents request against with a size and a duration, granting or queueing leases and killing leaked ones. Prevents two agents from simultaneously loading 23 GB models and OOMing both. Done when four concurrent agents requesting 20 GB each are serialized correctly with no OOM.

**Needs:** nothing

### AGENT-042: Local terminal-agent benchmark harness with real repos

**Scores:** $:3 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** XL | **Repo:** public

Build a containerless harness (bubblewrap from AGENT-018) that runs an agent against pinned snapshots of real repos with a hidden test suite as the oracle, supporting Claude Code, Codex, and a local-model agent loop behind one interface. Report pass rate, cost, and wall-clock per configuration. Done when all three backends produce comparable scores on 50 tasks.

**Needs:** nothing

### AGENT-043: Keep a regret log and mine it

**Scores:** $:2 CV:4 VIR:4 USE:5 ALT:4 | **Effort:** M | **Repo:** public

Add a session-end hook that asks the agent one question: what did you learn during this run that you wish you had known at the start. Store answers with repo and task metadata, cluster them monthly, and promote recurring items into CLAUDE.md or skills. Done when a month of regret entries produces at least two adopted changes.

**Needs:** nothing

### AGENT-044: Prompt compiler that minifies skills without changing behavior

**Scores:** $:3 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

A tool that takes a verbose skill or system prompt, produces candidate compressions, and verifies each against the AGENT-026 snapshot tests, keeping only compressions that pass every test. Reports tokens saved per skill. Done when the installed skill set is measurably smaller with a green test suite.

**Needs:** nothing

### AGENT-045: A task DSL that compiles to agent prompts

**Scores:** $:3 CV:5 VIR:4 USE:4 ALT:5 | **Effort:** L | **Repo:** public

Define a small YAML task language with fields for goal, oracle (the command that proves success), allowed tools, budget, and escalation policy, and a compiler that emits the actual prompt plus hook configuration. Makes tasks diffable, reusable, and testable across agent backends. Done when 20 real Taisho tasks are expressed in the DSL and run unchanged on two backends.

**Needs:** nothing

### AGENT-046: Give Toryo a plugin API and a public registry

**Scores:** $:4 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** XL | **Repo:** public

Extract Toryo's orchestration internals behind a documented plugin interface (schedulers, model providers, memory backends, observers), publish it to npm with a reference plugin for each extension point, and stand up a registry site listing community plugins. This is the piece that turns a personal orchestrator into something other people adopt. Done when a third-party plugin installs and runs without touching core.

**Needs:** a domain for the registry site

### AGENT-047: OpenTelemetry tracing for the fleet, surfaced in Tenshu

**Scores:** $:3 CV:5 VIR:3 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Emit OTel spans for every agent session, subagent, tool call, and model request, export to a local collector, and add a waterfall trace view to the Tenshu dashboard. Standard tracing means standard tooling instead of bespoke log parsing. Done when a multi-agent run renders as one trace with correct parent-child nesting.

**Needs:** nothing

### AGENT-048: Export any agent run as a shareable self-contained replay

**Scores:** $:3 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Turn a transcript into a single HTML file with a scrubber, collapsible tool calls, diffs rendered inline, and secrets redacted, so a run can be posted publicly or attached to a bug report. Include a token and cost gutter alongside the timeline. Done when a real run exports, redacts cleanly, and opens offline.

**Needs:** nothing

### AGENT-050: Score whether SIBT is actually self-improving

**Scores:** $:3 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** XL | **Repo:** public

Freeze a fixed evaluation set from AGENT-002 and AGENT-042, then re-run it against each historical SIBT orchestrator version (v1 through v11) using cassettes where possible, producing a capability-over-time curve with confidence intervals. The honest answer might be flat, which is itself the finding worth publishing. Done when every version has a score and the curve plus methodology is written up.

**Needs:** nothing

