# Finance, Investing & Market Tools

Personal-finance automation, market-data infrastructure, and agent-payment plumbing. Analysis tooling only, nothing here picks securities or promises returns.

### FIN-001: Build a canonical statement importer for every bank CSV format

**Scores:** $:0 CV:2 VIR:1 USE:5 ALT:3 | **Effort:** S | **Repo:** public

Write a Node/TypeScript library that ingests CSV/OFX/QFX exports from arbitrary institutions and emits one canonical transaction schema (ISO date, integer cents, merchant raw string, account id, stable content hash). Format detection is by header fingerprint against a `formats/` directory of declarative mappings, so adding a new bank is a ten-line YAML file. Done when re-importing an overlapping export produces zero duplicate rows.

**Needs:** nothing

### FIN-003: Publish a money type that makes float bugs impossible

**Scores:** $:1 CV:4 VIR:3 USE:3 ALT:4 | **Effort:** M | **Repo:** public

An npm package exporting a `Money` type backed by bigint minor units, with currency carried in the type so `USD + EUR` is a compile error. Include allocation (splitting $10 three ways without losing a cent), explicit rounding modes, and an `Intl.NumberFormat`-driven formatter. Property-based tests via fast-check assert conservation: any allocation sums back to the original exactly.

**Needs:** nothing

### FIN-004: Ship an ESLint rule that flags floating-point arithmetic on money

**Scores:** $:0 CV:4 VIR:4 USE:2 ALT:4 | **Effort:** S | **Repo:** public

`eslint-plugin-no-float-money`: a type-aware `@typescript-eslint` rule that reports arithmetic on values whose type or identifier matches money heuristics (`amount`, `price`, `total`, `cents`, `Money`), plus `parseFloat` on currency strings and `toFixed(2)` used as rounding. Include a suggestion fixer pointing at the FIN-003 API. Done when it fires correctly on a corpus of five real open-source checkout implementations.

**Needs:** nothing

### FIN-006: Expose the ledger to Claude as an MCP server

**Scores:** $:1 CV:4 VIR:3 USE:5 ALT:3 | **Effort:** M | **Repo:** public

An MCP server wrapping Beancount Query Language so an agent can answer "what did we spend on groceries in Q2 versus Q1" without ever seeing raw transaction rows. Tools: `query(bql)`, `accounts()`, `monthly_summary(account, range)`, with a hard read-only guarantee and a redaction layer stripping account numbers from every response. Done when Claude Code answers five spending questions correctly with no hand-written queries.

**Needs:** nothing

### FIN-008: Flag statistically unusual transactions without machine-learning theater

**Scores:** $:0 CV:2 VIR:1 USE:4 ALT:2 | **Effort:** S | **Repo:** public

Per-merchant and per-category robust z-scores using median and MAD rather than mean and standard deviation, with a minimum-history threshold so a first-ever charge is reported as "new merchant" rather than "anomaly." Runs as a post-import hook writing into a review queue. Done when the false-positive count on a month of real data is under five items.

**Needs:** nothing

### FIN-009: Forecast the next 90 days of cash flow from detected recurrences

**Scores:** $:1 CV:3 VIR:2 USE:4 ALT:3 | **Effort:** M | **Repo:** public

Combine the recurring schedule from FIN-007 with a seasonal estimate of discretionary spend and project daily balance forward as a fan chart showing the 10th, 50th, and 90th percentile paths, highlighting any day the projected low dips below a configured floor. Done when the 90th-percentile band contains the actual balance on 90 percent of backtested days.

**Needs:** nothing

### FIN-013: Contrast the household index against official BLS CPI

**Scores:** $:1 CV:3 VIR:4 USE:3 ALT:4 | **Effort:** M | **Repo:** public

Pull the BLS public API series for Food at Home, Shelter, and All Items, align them to the FIN-012 household index, and render a static site showing where the household diverges from the national figure and why, basket composition, store choice, regional weighting. Includes an honest methodology section on why a single household's index is statistically noisy.

**Needs:** free BLS API registration key (no cost)

### FIN-015: Answer tax questions with paragraph-level IRS citations or refuse

**Scores:** $:2 CV:4 VIR:3 USE:4 ALT:5 | **Effort:** M | **Repo:** public

RAG over IRS publications (Pub 17, 550, 590-A/B, 969) and form instructions, all public-domain PDFs, using `nemotron-3-nano` for long-context synthesis under a hard constraint: every sentence carries a publication and paragraph citation, and the system answers "not covered in the indexed publications" rather than guessing. Done when a 30-question eval set shows zero uncited claims.

**Needs:** nothing

### FIN-016: Reconstruct cost basis and detect wash sales from brokerage exports

**Scores:** $:2 CV:3 VIR:2 USE:4 ALT:4 | **Effort:** M | **Repo:** public

Parse brokerage transaction history into tax lots, support FIFO and specific identification, apply the 30-day wash-sale window across substantially identical holdings including the spousal and IRA cases, and emit a Form 8949-shaped CSV plus a warning list. Framed explicitly as a reconciliation aid for checking the broker's 1099-B, not a replacement for it.

**Needs:** nothing

### FIN-017: Model the contribution order-of-operations as an explicit decision tree

**Scores:** $:1 CV:2 VIR:2 USE:4 ALT:4 | **Effort:** S | **Repo:** public

A small web tool encoding the standard sequence, employer match, HSA, deductible traditional versus Roth, taxable, as a transparent rule graph rather than a black box, where every node shows its arithmetic and its stated assumption. Each rule links to its FIN-015 citation. Carries a plain "not financial advice" statement and no personalization claims.

**Needs:** nothing

### FIN-019: Compute a refinance break-even that accounts for the reset amortization clock

**Scores:** $:1 CV:2 VIR:3 USE:3 ALT:4 | **Effort:** S | **Repo:** public

Most refi calculators compare monthly payments and stop. This one compares total interest over the remaining original term against the new loan, amortizes points and closing costs, and reports both the payment break-even month and the lifetime-cost crossover, which frequently disagree by years. Renders both amortization curves on one chart with the crossover marked.

**Needs:** nothing

### FIN-020: Compare a property tax assessment against neighborhood comparables

**Scores:** $:2 CV:2 VIR:3 USE:3 ALT:4 | **Effort:** M | **Repo:** public

Pull county assessor open data for surrounding parcels, normalize assessed value per square foot by year built and lot size, and flag whether the subject property sits above the local distribution. Produces the evidence packet an assessment appeal actually requires. Build for the WV and PA counties in scope and document the data source per county.

**Needs:** the county open-data portal must publish parcel data; verify first and flag as blocked-on-data if not

### FIN-021: Diff two insurance policies clause by clause

**Scores:** $:3 CV:3 VIR:3 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Ingest two policy PDFs, current versus quoted renewal, or two carriers, extract the declarations page into a structured schema of deductibles, limits, exclusions, and endorsements, and render a side-by-side diff highlighting coverage that silently disappeared. Uses `gemma4:31b-it` against a fixed JSON schema plus a verification pass asserting every extracted number appears verbatim in the source text.

**Needs:** nothing

### FIN-022: Generate a negotiation dossier before calling a service provider

**Scores:** $:1 CV:2 VIR:3 USE:4 ALT:4 | **Effort:** S | **Repo:** public

For a given bill, internet, insurance, phone, assemble current plan terms from the statement, publicly posted competitor pricing for the same zip, account tenure and payment history, and a call script with the specific ask and the walk-away point. Uses only pricing the provider publishes publicly. Done when it produces usable dossiers for three real household bills.

**Needs:** nothing

### FIN-024: Visualize expense-ratio drag as dollars, not basis points

**Scores:** $:1 CV:2 VIR:3 USE:3 ALT:4 | **Effort:** S | **Repo:** public

An interactive chart taking contribution schedule, horizon, and a range of expense ratios, showing cumulative fees paid in dollars alongside the compounding shortfall, with the fee series drawn at the same scale as the balance so the magnitude is legible rather than hidden. The growth assumption is a labeled input, displayed as an assumption and never as a forecast.

**Needs:** nothing

### FIN-025: Simulate rebalancing bands against a tax-aware cost model

**Scores:** $:0 CV:3 VIR:2 USE:3 ALT:3 | **Effort:** M | **Repo:** public

Backtest the 5/25 band rule against calendar rebalancing and against never rebalancing, on historical index series, with realistic costs: capital gains at the FIN-014 marginal rate, spread assumptions, and the option to rebalance using new contributions instead of sales. Reports tracking error to target and after-tax terminal dispersion rather than declaring a winner.

**Needs:** nothing

### FIN-026: Explore outcome distributions with historical bootstrap instead of a single number

**Scores:** $:1 CV:3 VIR:3 USE:4 ALT:4 | **Effort:** M | **Repo:** public

A scenario explorer that block-bootstraps historical monthly returns, preserving autocorrelation, across a configurable horizon and contribution schedule, then shows the full outcome distribution with sequence-of-returns risk isolated: the identical set of returns in different orders, side by side. Framed throughout as "here is the range history produced," never as a prediction.

**Needs:** nothing

### FIN-028: Reconstruct crypto cost basis from on-chain history

**Scores:** $:3 CV:3 VIR:3 USE:2 ALT:4 | **Effort:** L | **Repo:** public

A read-only tracker: given public addresses, walk transaction history via a public RPC or explorer API, classify transfers, swaps, and gas, apply FIFO lot matching at the USD price at block timestamp, and emit a capital-gains worksheet. Handles the case every naive tool gets wrong, internal transfers between the user's own wallets must not register as disposals. No private key ever touches the tool.

**Needs:** a free-tier RPC or block-explorer API key

### FIN-029: Build the interactive version of the SPIVA persistence data

**Scores:** $:1 CV:4 VIR:5 USE:2 ALT:5 | **Effort:** L | **Repo:** public

Take S&P's publicly published SPIVA and Persistence Scorecard data, reformat it into a clean open dataset, and build a scrollytelling piece where the reader picks a fund category and horizon and watches the survivor cohort shrink. The point is communicating a base rate well. Publish the dataset and the analysis notebook alongside the piece.

**Needs:** nothing

### FIN-030: Load a market data lake with real data-quality gates

**Scores:** $:0 CV:4 VIR:2 USE:3 ALT:3 | **Effort:** L | **Repo:** public

An incremental, resumable loader pulling daily OHLCV from free sources (Stooq, yfinance) into partitioned Parquet, with a quality suite running on every load: monotonic dates, no zero-volume rows carrying price changes, split-adjustment continuity, and cross-source disagreement flags. Bad rows are quarantined with a reason, never silently dropped. Disk-budgeted with a hard ceiling, the box has 157 GB free.

**Needs:** nothing

### FIN-031: Detect unadjusted corporate actions in a price series

**Scores:** $:0 CV:4 VIR:3 USE:2 ALT:4 | **Effort:** S | **Repo:** public

A validator scanning any price dataset for overnight gaps matching common split ratios (2:1, 3:1, 1:10) with no corresponding adjustment factor, plus dividend-sized gaps on ex-dates. Reports suspect tickers, dates, and the implied ratio. This is the defect that silently poisons every backtest built on scraped data, and almost nobody checks for it.

**Needs:** nothing

### FIN-032: Construct a universe that includes the companies that died

**Scores:** $:1 CV:4 VIR:3 USE:2 ALT:4 | **Effort:** L | **Repo:** public

Build a point-in-time index membership table from public delisting and index-change records so any historical query returns the tickers that existed on that date rather than today's survivors. Ship a `universe_as_of(date)` API plus a demonstration notebook showing how far a naive backtest's results move once the dead companies are restored.

**Needs:** a freely licensed source of historical index membership; document licensing first and fall back to a delisted-ticker list if none qualifies

### FIN-033: Write a backtesting framework whose defaults are statistically honest

**Scores:** $:2 CV:5 VIR:4 USE:2 ALT:4 | **Effort:** XL | **Repo:** public

A vectorized Python backtester where walk-forward validation is the default execution mode rather than an option, and every result reports the deflated Sharpe ratio beside the raw one with the number of configurations tried carried through automatically. Includes fill modeling, borrow costs, and a mandatory out-of-sample holdout the API refuses to reveal until a configuration is committed. Documentation leads with failure modes, not features.

**Needs:** nothing

### FIN-034: Lint backtest code for lookahead bias

**Scores:** $:1 CV:5 VIR:5 USE:2 ALT:5 | **Effort:** L | **Repo:** public

A static analyzer for pandas strategy code flagging the classic leaks: `.shift(-n)`, centered rolling windows, `bfill` on features, label joins without a lag, and a `StandardScaler` fit on the full sample. Ships as a flake8 plugin plus a runtime tracer that instruments DataFrame access and raises the moment a row reads an index beyond the current timestamp.

**Needs:** nothing

### FIN-035: Test any strategy against price series that contain no signal

**Scores:** $:0 CV:4 VIR:4 USE:2 ALT:4 | **Effort:** M | **Repo:** public

Given a strategy function, generate N synthetic series matched to the real data's volatility, autocorrelation, and tail behavior (block bootstrap plus a GARCH fit), run the strategy across all of them, and report where the real-data result falls in that null distribution. If the real result sits at the 60th percentile of pure noise, the tool prints exactly that.

**Needs:** nothing

### FIN-036: Build an event-study toolkit with correct standard errors

**Scores:** $:1 CV:4 VIR:2 USE:1 ALT:4 | **Effort:** L | **Repo:** public

Given an event-date set and a security set, compute abnormal returns against a market model estimated on a pre-event window, aggregate to CAARs, and apply the corrections most implementations skip: event-date clustering, cross-sectional correlation, and the BMP standardized test. Validated by reproducing a published event study's headline numbers within tolerance.

**Needs:** nothing

### FIN-037: Stand up a local, searchable SEC EDGAR corpus

**Scores:** $:2 CV:4 VIR:3 USE:2 ALT:4 | **Effort:** XL | **Repo:** public

Ingest filings through EDGAR's public full-text search and bulk endpoints, respecting the declared rate limit and user-agent requirement, store documents locally behind an SQLite FTS5 or Tantivy index, and expose both a CLI and an MCP server. Adds a filing-diff view rendering what changed in a company's risk factors between consecutive 10-Ks. Storage capped with LRU eviction.

**Needs:** nothing

### FIN-038: Detect language shifts across consecutive earnings calls

**Scores:** $:1 CV:4 VIR:4 USE:1 ALT:3 | **Effort:** L | **Repo:** public

Across a transcript corpus, compute per-company changes in hedging density, forward-looking-statement frequency, Q&A evasion (semantic distance between question and answer embeddings), and prepared-remarks length. Output is a per-quarter delta report with the specific sentences driving each change. This is a computational-linguistics tool, not a trading signal, and the README says so first.

**Needs:** a transcript source whose terms permit local analysis; verify before ingesting and flag as blocked if none qualifies

### FIN-039: Score prediction markets on calibration, not profit

**Scores:** $:1 CV:4 VIR:5 USE:2 ALT:4 | **Effort:** M | **Repo:** public

Pull resolved markets from public APIs (Polymarket, Kalshi), bucket by final pre-resolution price, and plot the calibration curve with a Brier score decomposed into reliability, resolution, and uncertainty, broken out by category and time-to-resolution. Deliverable is a public monthly report answering how well these markets actually forecast.

**Needs:** nothing

### FIN-040: Build a working x402 reference implementation end to end

**Scores:** $:2 CV:5 VIR:4 USE:4 ALT:5 | **Effort:** L | **Repo:** public

Stand up all three pieces locally: a resource server returning HTTP 402 with the payment-required header, a facilitator verifying settlement, and an agent client that pays and retries. Testnet only, so no real value moves. Deliverable is a documented repo, a 60-second demo recording, and an honest write-up of where the spec is underspecified. Feeds the existing x402 research thread directly.

**Needs:** testnet RPC access (free)

### FIN-042: Put one existing tool behind x402 metering

**Scores:** $:3 CV:4 VIR:4 USE:3 ALT:3 | **Effort:** M | **Repo:** public

Pick a genuinely useful endpoint from the existing project set, the gravitational-wave glitch classifier is the strongest candidate, wrap it in the FIN-040 server, price it per call, and publish it with documentation an agent can discover. Success is an autonomous client finding, paying for, and using the service with no human in the loop.

**Needs:** a funded wallet for any mainnet run; testnet otherwise

### FIN-043: Account for what the agent fleet actually costs per project

**Scores:** $:2 CV:4 VIR:4 USE:5 ALT:4 | **Effort:** L | **Repo:** public

Parse Claude Code session logs, OpenRouter usage exports, Gemini API records, and Ollama request logs into one cost ledger attributed by project directory and task. Local inference is priced at measured wattage times the local kWh rate plus straight-line GPU amortization, so local and cloud land in identical units. Monthly report ranks projects by spend and by cost per shipped artifact.

**Needs:** nothing

### FIN-045: Schedule GPU batch work against time-of-use electricity pricing

**Scores:** $:1 CV:3 VIR:3 USE:4 ALT:3 | **Effort:** M | **Repo:** public

A job queue holding non-urgent inference and fine-tuning work until off-peak hours per the utility's published TOU schedule, with an override for interactive work and a report showing dollars saved versus running everything on demand. Integrates with the existing nohup-based background process pattern, since WSL2 has no systemd.

**Needs:** the utility's published TOU rate schedule (public)

### FIN-047: Back-solve the consulting rate from a target take-home

**Scores:** $:2 CV:1 VIR:3 USE:4 ALT:4 | **Effort:** S | **Repo:** public

Inputs: target annual net, realistic utilization, unpaid overhead hours, self-employment tax, the health-insurance cost an employer currently absorbs, and a vacation allowance. Output: the minimum defensible hourly and day rate plus a sensitivity table showing how the rate must move as utilization falls. Most independents underprice because they never do this arithmetic once.

**Needs:** nothing

### FIN-048: Build an MRR cohort dashboard against real Stripe data

**Scores:** $:4 CV:3 VIR:2 USE:3 ALT:3 | **Effort:** M | **Repo:** public

Pull the Stripe API into a local warehouse and compute the metrics the Stripe dashboard does not give cleanly: cohort retention curves, net revenue retention, expansion versus contraction decomposition, and quick ratio. Designed to behave correctly at low volume where percentage metrics are noise, it always shows counts beside rates and suppresses ratios below a minimum cohort size.

**Needs:** Stripe account authenticated

### FIN-049: Simulate SaaS pricing models against token cost of goods sold

**Scores:** $:4 CV:3 VIR:4 USE:4 ALT:4 | **Effort:** M | **Repo:** public

A calculator for AI products where inference dominates variable cost: model seat-based, usage-based, and hybrid pricing against a distribution of user behavior, and show gross margin per plan under different routing assumptions (local, Haiku-class, Opus-class). Surfaces the classic failure where the top five percent of users make a flat-rate plan structurally unprofitable.

**Needs:** nothing

