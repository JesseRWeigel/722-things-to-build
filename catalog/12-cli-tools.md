# CLI & Terminal Tools

Command-line utilities, TUIs, shell integrations, git tooling, terminal dashboards, and dotfile automation, including local-Ollama wrappers built for shell pipelines.

### CLI-001: Shell hook that explains the command that just failed

**Scores:** $:2 CV:4 VIR:5 USE:5 ALT:5 | **Effort:** M | **Repo:** public

A zsh/bash `precmd` hook that fires on a non-zero exit, captures the command, its stderr (via a lightweight tee ring buffer), the cwd, and relevant context (git state, whether the binary exists), then asks `qwen3-coder:30b` for a one-paragraph diagnosis plus a suggested command. The suggestion is printed and bound to a key that loads it into the prompt buffer, never auto-executed.

**Needs:** nothing

### CLI-002: Ctrl-G natural language to command widget

**Scores:** $:2 CV:4 VIR:5 USE:5 ALT:5 | **Effort:** M | **Repo:** public

A ZLE widget that takes the text currently in your prompt as an English description, sends it to a local Ollama model with a system prompt containing your OS, shell, and the list of binaries actually on `$PATH`, and replaces the buffer with the generated command left uncommitted for editing. Fully offline, so it works on machines where a cloud CLI assistant is not allowed.

**Needs:** nothing

### CLI-003: Ollama observability TUI

**Scores:** $:2 CV:4 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

A terminal dashboard polling `/api/ps` and `nvidia-smi` that shows loaded models with their VRAM footprint and keep-alive countdown, a live tokens/sec and time-to-first-token readout per in-flight request, a VRAM sparkline, and a scrolling request log with prompt previews. Answers "what is eating my 32 GB right now" in one keystroke.

**Needs:** nothing

### CLI-004: wsl-doctor

**Scores:** $:2 CV:3 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

A diagnostic CLI for WSL2 that checks the failure modes that eat afternoons: clock skew against the host, DNS resolution via a mangled `/etc/resolv.conf`, memory ballooning and the missing `.wslconfig` caps, VHDX growth versus actual used bytes, `/mnt/c` interop path pollution in `$PATH`, and missing systemd. Each finding prints the exact remediation command and links the upstream issue.

**Needs:** nothing

### CLI-005: Disk reclaim TUI

**Scores:** $:2 CV:3 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

An interactive reclaim tool that categorizes recoverable space rather than just listing big directories: `node_modules` in repos with no changes in N days, `.next`/`dist`/`target` build caches, pnpm and uv store garbage, pip and HF hub caches, Ollama blobs unreferenced by any manifest, and old WSL VHDX slack. Every category shows recoverable bytes and a regeneration cost estimate before you confirm.

**Needs:** nothing

### CLI-006: modeldiff: side-by-side local model REPL

**Scores:** $:2 CV:4 VIR:5 USE:5 ALT:5 | **Effort:** M | **Repo:** public

A TUI that takes one prompt and streams it to two or three local models simultaneously in adjacent panes, with word-level diff highlighting between panes, per-model timing, and a keypress to promote either answer into a saved comparison file. Sequential model loading with a VRAM-aware scheduler so a 30B and a 27B do not fight over the card.

**Needs:** nothing

### CLI-007: Background process manager for a systemd-less box

**Scores:** $:2 CV:3 VIR:3 USE:5 ALT:4 | **Effort:** M | **Repo:** public

A TUI over a small JSON registry of `nohup`-launched services: start, stop, restart, tail logs with search, show uptime and RSS, and auto-restart with backoff on crash. Includes a declarative `services.toml` and a shell-profile hook that restarts anything marked `boot: true` when WSL comes back up, which is the gap systemd would otherwise fill.

**Needs:** nothing

### CLI-008: benchq: local model benchmark table generator

**Scores:** $:2 CV:4 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Run every installed Ollama model through a fixed prompt set at 1k, 8k, and 32k context, recording time-to-first-token, tokens/sec, peak VRAM, and whether it OOMs, then emit a sorted markdown table and an SVG chart. Results persist to a local SQLite file so re-running after a model or driver update shows the delta.

**Needs:** nothing

### CLI-009: ollama-pipe: a set of composable unix filters

**Scores:** $:2 CV:4 VIR:5 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Small single-purpose binaries that read stdin and write stdout, `summarize`, `classify --labels a,b,c`, `translate --to pt-BR`, `extract --schema file.json`, `rewrite --style terse`, each streaming, each defaulting to `gemma4:e4b` for throughput with a flag to escalate. They compose: `git log --oneline -50 | summarize | translate --to es`.

**Needs:** nothing

### CLI-010: llmawk: per-line transformation with caching

**Scores:** $:2 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** M | **Repo:** public

An awk-shaped tool where the program is a natural-language instruction applied to each input line (or each record under a custom separator), with concurrency, batching of N lines per model call, and a content-hash cache so reruns over mostly-unchanged input cost nothing. Add `--dry-run` to show the prompt for one line before spending an hour on 50,000.

**Needs:** nothing

### CLI-011: Deduplicating cache proxy for Ollama

**Scores:** $:2 CV:4 VIR:3 USE:5 ALT:4 | **Effort:** M | **Repo:** public

A local HTTP daemon that fronts Ollama, hashes (model, messages, options) to a disk cache, and serves repeat requests instantly while still emulating streaming chunk-by-chunk. Includes TTL and size eviction, a `--bypass` header, and stats showing hit rate and hours of GPU time saved, meaningful when an agent fleet reruns the same prompts across sessions.

**Needs:** nothing

### CLI-012: git-story: release narrative from commits and diffs

**Scores:** $:2 CV:4 VIR:4 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Given a tag range, group commits by conventional-commit type and touched area, feed each group's diffstat and messages to a local model, and produce a changelog written for humans, what changed and why it matters, with a separate machine-readable section for breaking changes. Deterministic grouping happens in code; the model only writes prose, so output is stable enough to commit.

**Needs:** nothing

### CLI-013: git-timewarp: scrub a file through its history

**Scores:** $:1 CV:4 VIR:4 USE:4 ALT:5 | **Effort:** M | **Repo:** public

A TUI where left/right arrows step a single file through every commit that touched it, rendering the full content with per-line age coloring and the commit message in a footer. Add a "find when this line appeared" search that runs a pickaxe log and jumps straight to the introducing commit.

**Needs:** nothing

### CLI-014: Contextual secret-scanning pre-commit hook

**Scores:** $:2 CV:4 VIR:3 USE:5 ALT:5 | **Effort:** M | **Repo:** public

A hook that runs fast regex/entropy detection first, then passes only the ambiguous hits to a local model for a judgment call on whether a string is a live credential, a test fixture, or documentation, cutting the false positives that make people disable these tools. Verdicts are cached by line hash and the whole thing must complete in under two seconds on a typical staged diff.

**Needs:** nothing

### CLI-015: Hugging Face browser TUI that filters by your free VRAM

**Scores:** $:2 CV:4 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Search the HF Hub from the terminal with a hard filter on "will this fit in my currently free VRAM at q4," computed from parameter count, quantization, and desired context length, then one-key pull it into Ollama with a generated Modelfile. Shows download size against free disk before starting, which matters at 157 GB free.

**Needs:** nothing

### CLI-016: PR triage inbox

**Scores:** $:2 CV:4 VIR:3 USE:5 ALT:5 | **Effort:** M | **Repo:** public

A TUI that aggregates every open PR across your GitHub repos into one keyboard-driven list, review requests, your own PRs with failing CI, PRs stale beyond N days, with vim keys to open, comment, approve, or snooze. Built on `gh api` with a local cache so it opens instantly and refreshes in the background.

**Needs:** nothing

### CLI-017: Agent token and cost tracker

**Scores:** $:2 CV:4 VIR:4 USE:5 ALT:4 | **Effort:** M | **Repo:** public

Parse local Claude Code and `codex` session logs to report tokens and estimated spend per project per day, with a terminal sparkline, a top-10 most expensive sessions view, and a breakdown of cache-read versus fresh input tokens. Exports CSV so the numbers can back a consulting invoice or a budget decision.

**Needs:** nothing

### CLI-018: vidkit: ffmpeg presets for README media

**Scores:** $:2 CV:3 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

A CLI wrapping ffmpeg with presets tuned for the exact thing developers need, screen recording to a GitHub-embeddable mp4 under a size target, to a looping webm, or to a palette-optimized gif, using two-pass bitrate search to hit the target rather than guessing a CRF. Add auto-trim of leading/trailing idle frames and an optional caption burn-in.

**Needs:** nothing

### CLI-020: Shell completion generator from --help output

**Scores:** $:1 CV:4 VIR:4 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Point it at any binary; it runs `--help` (and subcommand help, discovered recursively), parses the flags with a local model constrained to a strict JSON schema, verifies each extracted flag actually exists by probing it, and writes zsh/bash/fish completions. The verification pass is what makes model-generated completions trustworthy instead of plausible.

**Needs:** nothing

### CLI-022: envdiff: three-way environment variable drift

**Scores:** $:2 CV:3 VIR:3 USE:5 ALT:5 | **Effort:** S | **Repo:** public

Compare `.env`, `.env.example`, and the deployed environment pulled via `vercel env ls` in a single aligned table showing missing, extra, and present-but-different keys (values masked, compared by hash). Exit non-zero on drift so it can run in CI or a pre-deploy hook.

**Needs:** Vercel CLI auth for the remote column; the local two-way diff works without it.

### CLI-023: whichmodel: pick a local model for the job

**Scores:** $:1 CV:3 VIR:4 USE:5 ALT:4 | **Effort:** S | **Repo:** public

Given a task description and optional context-length requirement, it reads currently free VRAM, `ollama list`, and a bundled capability/benchmark table, then recommends a model with a one-line justification and the exact `ollama run` command. Flags when nothing installed fits and names the smallest thing you could pull.

**Needs:** nothing

### CLI-024: Monorepo script launcher

**Scores:** $:1 CV:3 VIR:3 USE:4 ALT:5 | **Effort:** S | **Repo:** public

A fuzzy launcher over every `scripts` entry in every workspace `package.json`, showing the package, the script body, and how recently you ran it, then executing in the right directory with the right package manager auto-detected. Recent-first ordering makes it faster than typing the command you actually know.

**Needs:** nothing

### CLI-025: Terminal theme from an image

**Scores:** $:1 CV:2 VIR:5 USE:2 ALT:5 | **Effort:** S | **Repo:** public

Extract a palette from any image with k-means in Lab space, then map it onto the 16 ANSI slots under a contrast constraint so every foreground/background pair clears WCAG AA, and emit configs for Windows Terminal, Alacritty, tmux, and a matching VS Code theme. The contrast solver is what separates this from the many unusable pretty-palette generators.

**Needs:** nothing

### CLI-026: Shell history stats card

**Scores:** $:1 CV:3 VIR:5 USE:3 ALT:4 | **Effort:** S | **Repo:** public

Analyze your zsh/bash history locally and render an SVG card: top commands, hours-of-day heatmap, most-visited directories, longest-running commands, and the ratio of typed to recalled commands, with a redaction pass that strips anything matching a secret pattern before rendering. Runs fully offline; nothing is uploaded.

**Needs:** nothing

### CLI-027: Endpoint schema-change watcher

**Scores:** $:2 CV:3 VIR:3 USE:4 ALT:5 | **Effort:** S | **Repo:** public

Poll a list of JSON endpoints on an interval, infer a structural schema from each response, and alert via ntfy or exit code when the *shape* changes, a field disappears, a type flips, an enum gains a member, while ignoring value churn. Useful for catching a third-party API breaking you before your users do.

**Needs:** nothing

### CLI-028: Cron heartbeat monitor

**Scores:** $:2 CV:3 VIR:2 USE:5 ALT:4 | **Effort:** S | **Repo:** public

Wrap any scheduled job so it registers an expected interval, pings on start and finish with the exit code and duration, and a small local daemon alerts via ntfy when a job misses its window or fails twice in a row. Self-hosted equivalent of a dead-man's-switch service, with a terminal status board showing every registered job's last run.

**Needs:** an ntfy topic (already available).

### CLI-029: Ollama model usage tracker and prune advisor

**Scores:** $:1 CV:2 VIR:3 USE:5 ALT:4 | **Effort:** S | **Repo:** public

A tiny logging shim plus reporter that records which models are actually invoked and when, then ranks installed models by "GB per invocation over the last 90 days" and proposes a prune list with the exact re-pull commands to undo it. Directly targets the disk constraint: several 17-23 GB older-generation models are kept only for comparison runs.

**Needs:** nothing

### CLI-030: Vercel deployment board

**Scores:** $:1 CV:3 VIR:2 USE:4 ALT:4 | **Effort:** S | **Repo:** public

A one-screen terminal board across all your Vercel projects: latest production deployment with age and commit, any building or errored deployment, preview URLs for open branches, and a keypress to open logs or promote. Built on the Vercel CLI's JSON output with a refresh loop.

**Needs:** verified Vercel CLI auth.

### CLI-031: git worktree switcher

**Scores:** $:1 CV:3 VIR:3 USE:4 ALT:5 | **Effort:** S | **Repo:** public

A fuzzy picker over all worktrees across all repos under a root, showing branch, ahead/behind, dirty state, and last commit age, with keys to jump, create a worktree from a branch or PR number, and clean up ones whose branch is gone. Solves the "which of my nine checkouts was that in" problem for anyone running parallel agent sessions.

**Needs:** nothing

### CLI-032: since: what changed while I was away

**Scores:** $:1 CV:3 VIR:3 USE:4 ALT:4 | **Effort:** S | **Repo:** public

Records a per-repo bookmark timestamp and prints everything that happened after it: new commits by author, merged and opened PRs, CI status changes, new issues, and dependency bumps, then advances the bookmark. Designed for the Monday-morning re-entry into a repo you left on Thursday.

**Needs:** nothing

### CLI-033: WSL clipboard bridge TUI

**Scores:** $:1 CV:2 VIR:3 USE:4 ALT:4 | **Effort:** S | **Repo:** public

A daemon plus picker that maintains a searchable clipboard history bridged between the Linux side and the Windows host, handling text, file paths translated across `/mnt/c` boundaries, and images saved to a temp file with the path yanked. Includes pinned entries and a secret-pattern filter that refuses to store anything resembling a token.

**Needs:** nothing

### CLI-034: Context budget calculator

**Scores:** $:1 CV:3 VIR:3 USE:5 ALT:4 | **Effort:** S | **Repo:** public

Point it at files, a directory, or a git diff and it reports token counts per tokenizer family alongside a table of which of your installed models could take it at which context setting, plus the estimated VRAM that context would consume. Add `--fit qwen3-coder:30b` to get a suggested subset of files that fits under a target.

**Needs:** nothing

### CLI-035: Dotfile drift detector

**Scores:** $:1 CV:3 VIR:3 USE:4 ALT:5 | **Effort:** S | **Repo:** public

Compares live config files against your dotfiles repo, ignoring machine-specific sections marked by comment fences, and either prints the drift or opens a PR that captures the changes you made in place and forgot to commit. Runs from a weekly hook so the repo stops silently rotting.

**Needs:** nothing

### CLI-036: agentwatch: TUI for every agent session on the machine

**Scores:** $:3 CV:5 VIR:5 USE:5 ALT:4 | **Effort:** L | **Repo:** public

Discover running Claude Code and `codex` processes, correlate each to its working directory, session log, and git branch, and render a live board with the current tool call, elapsed time, token burn, and whether a session is blocked waiting on a permission prompt. Keys to attach to a session's log tail, kill a runaway, or jump to its worktree, the missing control surface for running eight agents on twelve cores.

**Needs:** nothing

### CLI-037: Shell history workflow miner

**Scores:** $:3 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Normalize your shell history into command templates (arguments abstracted to placeholders), mine frequent sequential patterns with a sequence-mining algorithm rather than naive counting, and surface your top recurring multi-command workflows. For each one, generate a proposed shell function or alias with the variable parts as parameters, and estimate the keystrokes per week it would save.

**Needs:** nothing

### CLI-038: repoq: incremental terminal Q&A over a codebase

**Scores:** $:3 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Build a chunk-level embedding index stored inside `.git/repoq`, updated incrementally by a post-commit hook so only changed files are re-embedded, and answer questions with `qwen3-coder:30b` citing file and line ranges. The differentiator is index freshness and cost: a stale or full-rebuild index is why most local code-Q&A tools get abandoned after a week.

**Needs:** nothing

### CLI-039: Merge conflict resolver TUI

**Scores:** $:3 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** L | **Repo:** public

For each conflict hunk, show ours, theirs, and the merge base side by side, plus a locally generated proposed resolution with a short rationale and the surrounding function for context. Every resolution requires an explicit keypress; nothing is written without confirmation, and a `--explain-only` mode gives the reasoning without proposing code.

**Needs:** nothing

### CLI-040: Terminal PR review client

**Scores:** $:3 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** L | **Repo:** public

A full review workflow without a browser: file tree with review progress, syntax-highlighted diffs with expandable context pulled from the repo, inline comment composition, suggestion blocks, and batched submission as a single review. Includes a locally generated per-file summary and a "what would break" note, generated once and cached so it does not re-run on every scroll.

**Needs:** nothing

### CLI-041: Unattended git bisect with a generated test script

**Scores:** $:3 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** L | **Repo:** public

Describe the bug in a sentence; the tool drafts a minimal reproduction script, verifies it fails on HEAD and passes on a known-good commit before trusting it, then runs `git bisect run` unattended and reports the culprit commit narrowed to the specific hunk most likely responsible. Handles the practical obstacles, dependency installs per commit, build caching, flaky-test detection via repeated runs at each step.

**Needs:** nothing

### CLI-042: Morning briefing across every repo

**Scores:** $:2 CV:4 VIR:4 USE:5 ALT:4 | **Effort:** L | **Repo:** public

One command that scans every repo under a root in parallel and prints a single screen: uncommitted work and its age, unpushed commits, branches gone from the remote, PRs awaiting your review, red CI, dependency advisories, plus machine vitals (disk free, VRAM, running agent sessions). Configurable sections, cached between runs, and an ntfy-able digest mode for the days you do not open a terminal first.

**Needs:** nothing

### CLI-043: Two-way ntfy approval inbox for agent actions

**Scores:** $:3 CV:5 VIR:5 USE:5 ALT:4 | **Effort:** L | **Repo:** public

A local daemon that receives approval requests from agent sessions (a shell command about to run, a PR about to open), pushes them to your phone via ntfy with action buttons, subscribes to the reply stream, and unblocks the waiting process with the decision. Requests expire with a configurable default, every decision is written to an audit log, and the approval token is bound to a single request so a replayed message cannot approve anything.

**Needs:** an ntfy topic with action-button support (free tier is sufficient).

### CLI-044: Repo onboarding tour

**Scores:** $:3 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** L | **Repo:** public

Generate an interactive terminal walkthrough of an unfamiliar codebase: entry points found from build config, the highest-churn files from git history, ownership by decayed blame, the dependency layering, and a suggested reading order, presented as numbered stops you page through, each with the actual code excerpt. Export the whole thing as a markdown `ONBOARDING.md` for the repo.

**Needs:** nothing

### CLI-045: Terminal session recorder with an annotated transcript

**Scores:** $:2 CV:4 VIR:5 USE:4 ALT:5 | **Effort:** L | **Repo:** public

Record a shell session to asciinema format while separately capturing the structured command log, then post-process into a markdown document where each command has a locally generated one-line explanation and the output is folded. Turns a debugging session into a shareable writeup or a runbook draft without anyone taking notes during the fire.

**Needs:** nothing

### CLI-046: Fleet dashboard: a multiplexed control surface for parallel agents

**Scores:** $:4 CV:5 VIR:5 USE:5 ALT:4 | **Effort:** XL | **Repo:** public

A full-screen TUI that owns the whole terminal: a task queue with priorities, a pane per running agent showing live output, an approvals inbox, a per-agent cost and token meter, and a scheduler that will not exceed configured CPU/VRAM budgets when deciding what to start next. Persist queue state to SQLite so a crash resumes, support attaching and detaching from long-running work, and expose a small HTTP API so other tools can enqueue.

**Needs:** nothing

### CLI-047: Command palette over every installed CLI's own help text

**Scores:** $:4 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** XL | **Repo:** public

Index the `--help` output of every binary on `$PATH` (recursively through subcommands), embed it locally, and answer "how do I X" from that corpus with citations to the exact help lines, so the answer reflects the versions installed on *this* machine rather than a model's memory of an older release. The engineering is in the crawl: help-flag detection, pagers, interactive programs that must be skipped, output normalization, and incremental reindexing when a package updates.

**Needs:** nothing

### CLI-048: Multi-model consensus branch reviewer

**Scores:** $:4 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** XL | **Repo:** public

Review an entire branch by running three different local models (`qwen3-coder:30b`, `qwen3.6:27b`, `gemma4:31b`) over the same chunked diff with the same rubric, then cluster their findings semantically, keep issues that at least two independently raise, and rank the rest as low confidence. Output is a terminal checklist with jump-to-line, plus a markdown export; the consensus step is what cuts local-model false positives to a reviewable number.

**Needs:** nothing

### CLI-049: Executable markdown runbook engine

**Scores:** $:4 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** XL | **Repo:** public

Runbooks are plain markdown where fenced blocks are executable steps with declared preconditions, expected outputs, and rollback commands; the engine runs them with checkpointing, so a failed step can be retried or skipped and the whole run resumed hours later on a different terminal. Add variable prompting, dry-run rendering of every command that would execute, an audit log of what actually ran, and ntfy notification on steps that need a human.

**Needs:** nothing

### CLI-050: shellcast: golden-file testing for CLIs and TUIs

**Scores:** $:4 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** XL | **Repo:** public

A PTY-driven record/replay harness that captures a terminal session, including cursor movement, resize events, and timing, into a fixture, then replays it against a rebuilt binary and diffs the rendered screen states rather than raw bytes, so ANSI reordering does not cause false failures. Ships a terminal emulator model for rendering, a diff viewer that shows the two screens side by side, and a CI reporter, filling a real gap: TUIs are almost universally untested because nobody has a tolerable way to assert on them.

**Needs:** nothing

