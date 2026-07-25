# Developer Tools & Open Source Libraries

npm packages, VS Code extensions, GitHub Actions, linters, codemods, build plugins, and type libraries that each kill one specific recurring annoyance.

### DEVT-001: Ship a type-debt ratchet GitHub Action

**Scores:** $:1 CV:4 VIR:3 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Build a GitHub Action that runs `tsc --noEmit`, compares the error set against a committed `type-debt.json` baseline keyed by normalized error signature (file + code + message shape, not line number), and fails only on errors that are new. Includes a `--update-baseline` mode and a PR comment showing the debt delta so teams migrating off `strict: false` can ratchet down without a big-bang fix.

**Needs:** nothing

### DEVT-003: eslint-plugin-rsc-boundary for Next.js App Router

**Scores:** $:1 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

An ESLint plugin that statically walks the import graph from every `"use client"` file and flags server-only reachability: database clients, `node:` builtins, secrets read from `process.env` without a `NEXT_PUBLIC_` prefix, and non-serializable props (functions, class instances, Dates in some configs) crossing a server-to-client component boundary. Uses `@typescript-eslint/utils` plus a cached module graph so it stays fast on large App Router apps.

**Needs:** nothing

### DEVT-004: Vitest flake-ranker reporter

**Scores:** $:2 CV:4 VIR:4 USE:4 ALT:5 | **Effort:** M | **Repo:** public

A Vitest reporter plus CI recipe that reruns the suite N times against the same commit, computes a per-test flakiness score with a Wilson confidence interval, and writes `flaky.json` plus a markdown table. Adds a `--quarantine` mode that auto-tags tests above a threshold with `test.skip` in a generated patch, so flake triage becomes a PR instead of a Slack argument.

**Needs:** nothing

### DEVT-005: Per-route bundle budget Action for Next.js

**Scores:** $:2 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Parse `.next/app-build-manifest.json` and the build trace on both the PR head and the merge base, then post a PR comment with a per-route first-load JS table, deltas, and the specific new modules responsible for each regression. Budgets are declared in `bundle-budget.json` per route pattern; exceeding one fails the check.

**Needs:** nothing

### DEVT-006: VS Code extension: Local Explain, powered by qwen3-coder:30b

**Scores:** $:2 CV:4 VIR:4 USE:5 ALT:5 | **Effort:** M | **Repo:** public

A VS Code extension that sends the selected code plus its enclosing file's imports to a local Ollama endpoint and streams an explanation into a side panel, with a model picker defaulting to `qwen3-coder:30b`. Zero cloud calls, no telemetry, works offline, and includes a "explain this diff" command that feeds the staged hunk instead of a selection.

**Needs:** nothing

### DEVT-007: Dimensional-analysis units library for TypeScript

**Scores:** $:1 CV:5 VIR:4 USE:2 ALT:4 | **Effort:** M | **Repo:** public

A zero-runtime-cost branded types library where `Meters`, `Seconds`, and derived `MetersPerSecond` compose at the type level, so dividing a distance by a time yields the right unit and adding meters to seconds is a compile error. Ship the SI base dimensions as a type-level exponent tuple, a `unit()` constructor, and conversions that erase to plain numbers after compilation.

**Needs:** nothing

### DEVT-008: Human-readable lockfile diff Action

**Scores:** $:2 CV:4 VIR:5 USE:5 ALT:5 | **Effort:** M | **Repo:** public

An Action that diffs `pnpm-lock.yaml` / `package-lock.json` between base and head and posts a comment that answers the questions reviewers actually have: which packages changed version, which are new transitive additions, which newly run install scripts, which changed maintainer sets, and the total unpacked size delta. Data comes from the npm registry API; no paid service.

**Needs:** nothing

### DEVT-009: Barrel-file bloat detector as a Vite and Next plugin

**Scores:** $:1 CV:4 VIR:4 USE:4 ALT:5 | **Effort:** M | **Repo:** public

A build plugin that flags any client entry importing from a barrel (`index.ts` re-export hub) where the resolved cost exceeds a configurable KB budget, and prints the exact deep-import rewrite that would fix it. Emits a machine-readable report so it can also run as a CI gate.

**Needs:** nothing

### DEVT-010: Codemod: Next 16 Cache Components migration

**Scores:** $:2 CV:5 VIR:4 USE:4 ALT:5 | **Effort:** M | **Repo:** public

A jscodeshift/ts-morph codemod that converts `unstable_cache` call sites and route-segment `revalidate` exports into `use cache` directives with `cacheLife` and `cacheTag` equivalents, leaving a `// TODO(cache-migration)` comment wherever the original semantics cannot be preserved. Ships with a fixture suite covering the ambiguous cases so the output is trustworthy.

**Needs:** nothing

### DEVT-011: pnpm catalog migrator

**Scores:** $:1 CV:4 VIR:3 USE:4 ALT:5 | **Effort:** M | **Repo:** public

A CLI-as-npm-package that scans every `package.json` in a workspace, finds dependencies pinned to divergent versions, proposes a single catalog entry per package (preferring the highest version that satisfies all declared ranges), and rewrites the manifests to `catalog:` references. Dry-run by default, with a report of the conflicts it cannot resolve automatically.

**Needs:** nothing

### DEVT-012: Tailwind dead-class and typo linter

**Scores:** $:2 CV:4 VIR:4 USE:4 ALT:5 | **Effort:** M | **Repo:** public

An ESLint rule plus standalone checker that cross-references every class string in JSX against the classes Tailwind actually generated for the build, reporting typos (`flex-colum`), classes killed by content-glob misconfiguration, and dynamically constructed class names that Tailwind can never see. The last category is the real prize: `bg-${color}-500` silently produces nothing and nobody notices until production.

**Needs:** nothing

### DEVT-013: Typed Ollama HTTP client package with correct streaming types

**Scores:** $:1 CV:4 VIR:3 USE:5 ALT:4 | **Effort:** M | **Repo:** public

Publish `@jrw/ollama-types` plus a thin fetch client: exact TypeScript types for `/api/chat`, `/api/generate`, `/api/embed`, and `/api/ps`, with the NDJSON stream modeled as a discriminated union so a `done: true` chunk narrows to the one that carries `eval_count` and timings. Include a typed helper that computes tokens/sec from a completed stream.

**Needs:** nothing

### DEVT-014: ollama-guardrails: a provider wrapper that encodes the known gotchas

**Scores:** $:2 CV:4 VIR:3 USE:5 ALT:4 | **Effort:** M | **Repo:** public

An `ai-sdk-ollama` wrapper that applies per-model-family quirk profiles automatically: `think: false` for qwen3 and qwen3.5, retry-on-empty-content, context-length preflight against `/api/show`, and a clear thrown error when a model is requested that is not pulled. Profiles live in a JSON file so new models are a data change, not a code change.

**Needs:** nothing

### DEVT-015: Zod to Ollama structured-output schema adapter

**Scores:** $:2 CV:4 VIR:3 USE:5 ALT:5 | **Effort:** M | **Repo:** public

A package that converts a Zod schema into the JSON Schema dialect Ollama's `format` parameter actually accepts, stripping the constructs local models reliably choke on (deep `oneOf`, recursive `$ref`, unbounded `additionalProperties`) and reporting each downgrade. Include a repair pass that re-prompts once with the validation error when the model returns something Zod rejects.

**Needs:** nothing

### DEVT-016: Axe baseline fixture for Playwright

**Scores:** $:2 CV:5 VIR:3 USE:4 ALT:5 | **Effort:** M | **Repo:** public

A Playwright fixture that runs `axe-core` on every page under test and fails only on violations absent from a committed baseline, keyed by rule ID plus a stable DOM-path hash rather than raw selector. This makes accessibility enforceable on legacy codebases where a clean run is years away.

**Needs:** nothing

### DEVT-017: OpenAPI breaking-change differ with semver recommendation

**Scores:** $:3 CV:5 VIR:4 USE:3 ALT:5 | **Effort:** M | **Repo:** public

A pure-TypeScript diff engine for OpenAPI 3.1 that classifies every change as breaking, non-breaking, or additive (removed endpoint, narrowed enum, newly required request field, widened response union) and prints the semver bump the spec change implies. Ships as both a library and a GitHub Action that comments on spec PRs; the existing good tool in this space is Go-only, which is unusable on this machine.

**Needs:** nothing

### DEVT-018: Render-mode diff Action for Next.js

**Scores:** $:2 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Compare the build output of base and head to detect routes that flipped between static, ISR, dynamic, and partially prerendered, then post a PR comment naming the route and the likely cause (a new `cookies()` call, an uncached fetch, a dynamic import). Accidentally turning a static marketing route dynamic is a common and expensive regression nobody currently sees in review.

**Needs:** nothing

### DEVT-019: React Suspense waterfall detector

**Scores:** $:2 CV:5 VIR:4 USE:4 ALT:5 | **Effort:** M | **Repo:** public

A dev-only package that instruments React's Suspense boundaries and promise-throwing data reads to detect sequential suspends that could have been parallel, then logs a tree showing the serialized chain with timings and the component that should hoist the fetch. Ships a Vitest matcher too, so a waterfall can fail a test rather than just print a warning.

**Needs:** nothing

### DEVT-020: Lint rule: no node: imports reachable from edge entry points

**Scores:** $:1 CV:4 VIR:3 USE:4 ALT:5 | **Effort:** M | **Repo:** public

An ESLint rule that takes a list of edge-runtime entry files (middleware, route handlers with `runtime = "edge"`) and walks the resolved import graph to flag any transitive dependency on a Node builtin or a package whose `package.json` lacks an edge/worker export condition. Reports the full import chain, not just the offending leaf, because the chain is the part that takes an hour to find manually.

**Needs:** nothing

### DEVT-021: Three.js asset budget Vite plugin

**Scores:** $:2 CV:4 VIR:3 USE:5 ALT:4 | **Effort:** M | **Repo:** public

A Vite plugin that inspects every GLTF/GLB, texture, and HDR in the build, reports triangle counts, texture memory at upload resolution, and total GPU bytes per route, and fails the build against declared budgets. Suggests concrete fixes (KTX2 compression, Draco, mipmap-friendly power-of-two resize) with the estimated saving for each.

**Needs:** nothing

### DEVT-022: tsconfig-doctor

**Scores:** $:1 CV:4 VIR:5 USE:4 ALT:5 | **Effort:** S | **Repo:** public

A tool that reads your `tsconfig.json`, then measures rather than lectures: it toggles each candidate strictness flag one at a time, runs `tsc --noEmit`, and reports exactly how many errors in how many files each flag would cost you. Output is an ordered adoption path from cheapest to most expensive flag.

**Needs:** nothing

### DEVT-023: VS Code extension: AI authorship lens

**Scores:** $:1 CV:3 VIR:5 USE:4 ALT:4 | **Effort:** S | **Repo:** public

A gutter decoration and status-bar percentage showing which lines came from commits containing a `Co-Authored-By:` AI trailer, computed from `git blame` with a cached per-file result. Adds a workspace command that ranks files by AI-authored share, which is both a genuinely interesting metric and extremely shareable.

**Needs:** nothing

### DEVT-024: Import cycle report as a single self-contained HTML file

**Scores:** $:1 CV:3 VIR:3 USE:4 ALT:5 | **Effort:** S | **Repo:** public

An npm package that builds the module graph with `ts-morph`, finds strongly connected components with Tarjan's algorithm, and emits one standalone HTML file with an interactive cycle list and the shortest edge to break each one. No server, no CDN assets, so it can be attached as a CI artifact.

**Needs:** nothing

### DEVT-025: Action that finds tests which never assert

**Scores:** $:1 CV:4 VIR:4 USE:4 ALT:5 | **Effort:** S | **Repo:** public

A CI check that parses test files with the TypeScript AST and flags any `it`/`test` body with no reachable `expect`, no `assert`, and no snapshot call, including bodies where the only assertion sits inside a callback that is never invoked. Comments the list on the PR; a surprising number of green suites contain these.

**Needs:** nothing

### DEVT-026: VS Code inline cost meter for AI SDK calls

**Scores:** $:1 CV:3 VIR:4 USE:4 ALT:4 | **Effort:** S | **Repo:** public

An extension that recognizes model identifier string literals in AI SDK provider calls and renders an inline hint with input/output price per million tokens from a bundled, versioned pricing table, plus a marker for models that are free via OpenRouter or local via Ollama. Hovering shows the estimated cost of one call at the token counts you configure.

**Needs:** nothing

### DEVT-027: Codemod: migrate the @ai-sdk/openai Ollama shim to ai-sdk-ollama

**Scores:** $:1 CV:3 VIR:2 USE:5 ALT:3 | **Effort:** S | **Repo:** public

A codemod that finds `createOpenAI({ baseURL: ".../v1" })` providers pointed at a local Ollama, rewrites them to `ai-sdk-ollama`, and injects `think: false` into calls targeting qwen3 and qwen3.5 model IDs. Covers the exact configuration that silently returns empty content today.

**Needs:** nothing

### DEVT-028: Dependency freshness badge Action

**Scores:** $:1 CV:3 VIR:3 USE:4 ALT:4 | **Effort:** S | **Repo:** public

An Action that computes a repo's dependency-age score (median days behind latest, weighted by whether the gap crosses a major) and writes an SVG badge plus a JSON summary to a gh-pages branch. Unlike a raw outdated count, an age score does not punish you for pinning something deliberately.

**Needs:** nothing

### DEVT-029: Install-script and license gate Action

**Scores:** $:2 CV:4 VIR:3 USE:4 ALT:5 | **Effort:** S | **Repo:** public

A pre-merge check that fails when a dependency change introduces a package with a `postinstall`/`preinstall` script, a copyleft license outside an allowlist, or a first-publish-within-N-days maintainer, and prints the justification line a reviewer needs. Purely defensive: it surfaces the risky additions rather than blocking everything.

**Needs:** nothing

### DEVT-030: eslint-plugin-no-flaky-test

**Scores:** $:1 CV:4 VIR:4 USE:4 ALT:5 | **Effort:** S | **Repo:** public

A focused rule set for test files: bare `setTimeout` waits, `Date.now()` or `new Date()` without fake timers, unawaited promises, `Math.random()` without a seed, ordering assertions on unordered collections, and network calls not intercepted by a mock server. Each rule ships with the flake mechanism explained in its docs page.

**Needs:** nothing

### DEVT-031: PR auto-labeler by architecture layer

**Scores:** $:1 CV:3 VIR:2 USE:4 ALT:4 | **Effort:** S | **Repo:** public

An Action that reads a `layers.yml` mapping globs to layer names (ui, data, infra, agents, docs), labels each PR with every layer it touches, and adds a `crosses-layers` label when a single PR spans more than a configured number. Also emits a per-layer churn summary that makes an unfocused PR obvious at a glance.

**Needs:** nothing

### DEVT-032: node_modules disk attribution treemap

**Scores:** $:1 CV:3 VIR:4 USE:5 ALT:5 | **Effort:** S | **Repo:** public

An npm package that walks every `node_modules` under a root, attributes bytes to the top-level dependency that caused each transitive install, and emits a standalone HTML treemap plus a text top-20. On a machine at 84% disk this is directly actionable; for everyone else it is a good "why is my repo 2 GB" answer.

**Needs:** nothing

### DEVT-033: TypeScript transformer that enriches console.log into structured logs

**Scores:** $:1 CV:3 VIR:3 USE:3 ALT:4 | **Effort:** S | **Repo:** public

A compiler transformer plus tsup/Vite integration that rewrites `console.log(x)` into a structured emit carrying file, line, enclosing function name, and the source text of each argument expression, so logs read `userId=42` instead of `42`. Opt-in per file via a pragma, and a no-op in production builds.

**Needs:** nothing

### DEVT-034: Reviewer roulette weighted by blame decay

**Scores:** $:1 CV:3 VIR:3 USE:3 ALT:5 | **Effort:** S | **Repo:** public

An Action that picks reviewers by scoring each contributor's `git blame` ownership of the changed lines with an exponential time decay, so the person who wrote that code last month outranks the person who wrote it in 2021. Falls back to load-balancing across the team when ownership is diffuse, and never assigns the PR author.

**Needs:** nothing

### DEVT-035: Codemod that inserts `satisfies` where annotations over-widen

**Scores:** $:1 CV:4 VIR:3 USE:3 ALT:4 | **Effort:** S | **Repo:** public

Find variable declarations with an explicit type annotation whose inferred type is strictly narrower (const object literals annotated as a broad interface, config objects losing literal types), and rewrite them to `satisfies` so the narrow inference survives. Verify each rewrite by re-checking the file and reverting any change that alters the error count.

**Needs:** nothing

### DEVT-036: Monorepo dead-export finder that opens its own deletion PR

**Scores:** $:2 CV:5 VIR:4 USE:4 ALT:5 | **Effort:** L | **Repo:** public

Build the full cross-package reference graph with `ts-morph`, subtract public entry points declared in each `package.json` `exports` field, and identify exported symbols nobody imports, including symbols only referenced by other dead symbols (iterate to a fixed point). Then generate a branch that deletes them, runs the test suite, and opens a PR with a per-symbol confidence note.

**Needs:** nothing

### DEVT-037: Codemod: useEffect data fetching to RSC or TanStack Query

**Scores:** $:3 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** L | **Repo:** public

Detect the classic `useEffect` + `useState` + `setLoading` fetch triad, classify each instance as safely server-renderable or client-required (depends on browser APIs, user interaction, or client state), and rewrite the first group into async Server Components and the second into `useQuery` with a generated query key. Instances it cannot classify get an annotated report rather than a bad rewrite.

**Needs:** nothing

### DEVT-038: Component-level visual regression Action without a Storybook

**Scores:** $:3 CV:5 VIR:4 USE:4 ALT:5 | **Effort:** L | **Repo:** public

Use Playwright component testing to mount each exported component with props derived from its TypeScript types, snapshot at three viewports, and diff perceptually with an SSIM threshold so antialiasing noise does not fail builds. Baselines live in the repo via git-lfs-free PNG compression, and the PR comment shows only the changed components with side-by-side images.

**Needs:** an image host or artifact upload for the comment images; GitHub Actions artifacts suffice, so nothing external.

### DEVT-039: Snapshot testing for agent tool-call traces

**Scores:** $:3 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** L | **Repo:** public

A Vitest/Jest matcher, `toMatchAgentTrace`, that asserts on the *shape* of an agent run, tool call order, tool names, structurally matched arguments with wildcards for volatile fields, while ignoring free-text model prose entirely. Includes a recorder that captures traces from AI SDK `streamText`/`generateText` runs and a diff renderer that shows where the trajectory diverged, which is the thing that actually breaks when you change a prompt.

**Needs:** nothing

### DEVT-040: LLM eval regression gate as a GitHub Action

**Scores:** $:3 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** L | **Repo:** public

An Action that runs a repo-declared eval suite (prompts, inputs, graders) against free-tier OpenRouter models on every PR touching prompt files, compares scores to the merge base, and blocks on a statistically meaningful drop using a paired test rather than a raw threshold. Caches results by prompt hash so unchanged cases cost nothing.

**Needs:** `OPENROUTER_API_KEY` as a repo secret (already in env locally).

### DEVT-041: Hydration mismatch diff overlay for Next.js

**Scores:** $:3 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** L | **Repo:** public

A dev-only package that captures the server-rendered HTML and the first client render, aligns the two trees, and renders an overlay highlighting the exact differing text node or attribute with the component stack that produced it. React's built-in message names the symptom; this names the line, which is the single most requested improvement from anyone who has hit it.

**Needs:** nothing

### DEVT-042: Error boundary that emits a reproducible sandbox link

**Scores:** $:3 CV:5 VIR:5 USE:3 ALT:5 | **Effort:** L | **Repo:** public

A React error boundary that, on crash, serializes the failing component's props and the ancestor chain (with a configurable redaction function for PII), then produces a shareable StackBlitz-style project payload that mounts just that subtree with those props. Bug reports become a link that reproduces instead of a screenshot.

**Needs:** nothing for local file output; hosted link generation would need a StackBlitz project API call, which is free.

### DEVT-043: Playwright trace to page-object codegen

**Scores:** $:3 CV:5 VIR:4 USE:3 ALT:5 | **Effort:** L | **Repo:** public

Parse a recorded Playwright trace, cluster the interactions by page URL pattern, and generate a typed page-object class per page with stable locators chosen by a preference ladder (test id, role + accessible name, label, text, CSS as last resort). Regenerating against a newer trace produces a diff rather than clobbering hand-edited methods.

**Needs:** nothing

### DEVT-044: Prompt Lens VS Code extension

**Scores:** $:3 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Treat prompt template literals as first-class source: inline token counts per model, a preview pane that renders the prompt with sample variable bindings, a git-aware diff of how a prompt changed across commits, and a one-key "run against a local Ollama model" that shows the output side by side. Detects prompts by AI SDK call sites and by a `/* prompt */` pragma.

**Needs:** nothing

### DEVT-046: LLM record/replay proxy with cassettes

**Scores:** $:4 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** XL | **Repo:** public

A local HTTP proxy that sits in front of any OpenAI-compatible, Anthropic, or Ollama endpoint, records request/response pairs to versioned cassette files, and replays them deterministically in tests with configurable matching (exact, prompt-normalized, or embedding-similarity above a threshold for prompts that vary by timestamp). Includes streaming replay with original inter-chunk timings, redaction of secrets at record time, and a `--record-missing` mode so a new test case fetches once and is frozen thereafter.

**Needs:** nothing

### DEVT-047: Background local-model reviewer for VS Code

**Scores:** $:4 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** XL | **Repo:** public

An extension that watches the working-tree diff, debounces, and continuously runs `qwen3-coder:30b` over changed hunks with the surrounding symbol context, surfacing findings as native VS Code diagnostics that clear when the code changes. The hard parts are the ones worth building: incremental context assembly, a scheduler that never blocks the editor or thrashes VRAM, deduplication of repeated findings across saves, and a dismissal store keyed by hunk content hash.

**Needs:** nothing

### DEVT-048: Cross-repo codemod runner

**Scores:** $:4 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** XL | **Repo:** public

Point it at a codemod and a `gh`-resolved list of repositories; it clones each shallowly, applies the transform, installs and runs that repo's own test command in isolation, and opens a PR only where tests pass, collecting the failures into a single report. Add a resumable job store, per-repo rate limiting, and a dry-run mode that renders every diff before anything is pushed.

**Needs:** nothing (`gh` is authed with repo + workflow scopes).

### DEVT-049: TypeScript language service plugin for build-free monorepo types

**Scores:** $:3 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** XL | **Repo:** public

A TS language service plugin that resolves cross-package imports in a pnpm workspace straight to source without project references or a build step, while keeping the published `exports` map authoritative so you cannot import a path consumers could not. Must handle path mapping, declaration emit divergence, and per-package compiler option differences, the payoff is instant go-to-definition and no stale `dist` types.

**Needs:** nothing

### DEVT-050: Component API compatibility checker with generated codemods

**Scores:** $:4 CV:5 VIR:5 USE:3 ALT:5 | **Effort:** XL | **Repo:** public

Extract a structural API surface for every exported React component (prop names, types, optionality, default values, ref forwarding, slot children shape) at two versions of a library, classify each change by breakage severity, and auto-generate a jscodeshift migration for the mechanical subset (renamed props, changed enum values, moved props into an object). Ship it as both a CI check for library authors and a `npx upgrade-components` path for consumers.

**Needs:** nothing

