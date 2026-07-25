# Data Journalism & Public Datasets

Assembling, analyzing, and publishing open public data, with a bias toward questions nobody answered because the data was too annoying to put together.

### DATA-001: Build a tri-state hospital price index from CMS transparency files

**Scores:** $:3 CV:5 VIR:4 USE:2 ALT:5 | **Effort:** XL | **Repo:** public

Every US hospital must publish a machine-readable negotiated-rate file discoverable via `https://<host>/cms-hpt.txt`. Crawl that endpoint for every hospital in PA, WV, and OH, normalize the wildly inconsistent JSON/CSV schemas into a single parquet table of payer-negotiated rates by CPT/DRG, and publish it as a Hugging Face dataset plus a Next.js explorer that answers "what does a knee MRI cost within 50 miles of me, by insurer." Done means at least 100 hospitals parsed with a documented per-hospital parse-failure log.

**Needs:** nothing. Files are large, so stream-parse with `ijson` and never hold a full file on disk given the 157 GB budget.

### DATA-002: Reconstruct 40 years of mountaintop removal from Landsat

**Scores:** $:1 CV:5 VIR:5 USE:1 ALT:5 | **Effort:** XL | **Repo:** public

Using Landsat Collection 2 surface reflectance on the AWS Open Data registry, compute annual NDVI-loss masks over the southern WV / eastern KY coalfields from 1985 to present, classify mine-disturbed area with a small CNN trained on OSMRE permit boundaries, and publish a county-by-year disturbed-acreage dataset plus an animated slider map. Done means the acreage series is validated against published SMCRA permit acreage within a stated error band.

**Needs:** nothing. Pull scenes on demand and delete after tiling to respect the disk constraint.

### DATA-003: Assemble a unified orphan and abandoned well atlas for Appalachia

**Scores:** $:2 CV:4 VIR:4 USE:2 ALT:5 | **Effort:** L | **Repo:** public

PA DEP's oil-and-gas well inventory, WV DEP's well database, and OSMRE's e-AMLIS abandoned mine land inventory each publish location data in different projections with different orphan definitions. Deduplicate them into one point dataset with a confidence field, join to Census block population and school locations, and ship a Datasette instance plus a GeoJSON release. Done means every record carries source provenance and a reconciliation note.

**Needs:** nothing.

### DATA-004: Measure how long retracted papers keep collecting citations

**Scores:** $:1 CV:4 VIR:4 USE:1 ALT:4 | **Effort:** M | **Repo:** public

Crossref now publishes the Retraction Watch database under CC0. Join it to OpenAlex citation edges with timestamps, compute per-field post-retraction citation half-lives, and identify the 200 retracted papers still accruing the most citations per year. Deliverable is a published dataset and a small interactive ranking site.

**Needs:** nothing.

### DATA-005: Detect model legislation copied across state legislatures

**Scores:** $:2 CV:5 VIR:5 USE:1 ALT:5 | **Effort:** L | **Repo:** public

Open States publishes bulk bill text for all 50 states. Run MinHash shingling for candidate pairs, then rerank with local embeddings from `qwen3.5:9b`, to surface clusters of near-identical bills introduced in multiple states within the same session. Deliverable is a cluster dataset with a viewer that shows a diff between any two bills in a cluster.

**Needs:** nothing.

### DATA-006: Publish an hourly grid carbon-intensity and cheap-compute calendar for PJM

**Scores:** $:2 CV:4 VIR:3 USE:5 ALT:4 | **Effort:** M | **Repo:** public

EIA-930 publishes hourly generation-by-fuel and interchange for every balancing authority. Compute a rolling hourly gCO2/kWh series for PJM, back it with day-ahead LMP from the PJM Data Miner public feed, and publish a JSON feed plus an iCal that marks the greenest and cheapest 6-hour blocks each day. Wire it into the local agent fleet so heavy GPU jobs schedule into those windows.

**Needs:** nothing. PJM Data Miner registration is free.

### DATA-007: Map maternity care deserts from CMS provider files

**Scores:** $:1 CV:4 VIR:4 USE:2 ALT:5 | **Effort:** M | **Repo:** public

Use the CMS Provider of Services file and the Hospital General Information dataset to identify facilities that reported obstetric services in a prior year and no longer do, then compute drive-time isochrones to the nearest remaining OB unit using a local OSRM instance on OSM extracts. Deliverable is a county-level dataset of OB closures since 2010 with drive-time deltas and a choropleth.

**Needs:** nothing.

### DATA-008: Correlate pharma payments with opioid prescribing in Appalachia

**Scores:** $:2 CV:5 VIR:5 USE:1 ALT:5 | **Effort:** L | **Repo:** public

Join CMS Open Payments general and research payments to the Medicare Part D Prescriber by Provider and Drug file on NPI, restricted to WV, KY, OH, and western PA. Model prescriber-level opioid MME against prior-year payment dollars with county fixed effects, and publish both the joined analysis table and a reproducible notebook. Done means the methodology explicitly bounds what a correlational Part D-only analysis can and cannot claim.

**Needs:** nothing.

### DATA-009: Rank nursing homes by staffing gap versus inspection deficiencies

**Scores:** $:3 CV:4 VIR:3 USE:3 ALT:5 | **Effort:** M | **Repo:** public

CMS publishes Payroll-Based Journal daily staffing hours alongside Health Deficiencies from state surveys. Compute weekend-versus-weekday RN coverage collapse per facility, join to deficiency scope-and-severity, and publish a searchable facility page set for the tri-state region. Done means a family can type a facility name and see staffing volatility, not just a star rating.

**Needs:** nothing.

### DATA-010: Quantify repetitive-loss flood properties from NFIP claims

**Scores:** $:2 CV:4 VIR:4 USE:2 ALT:5 | **Effort:** M | **Repo:** public

OpenFEMA publishes redacted NFIP claims and policies at census-tract resolution. Compute per-tract repeat-claim rates, total federal payout per insured structure, and payout trend since 1978 in constant dollars, then cross-reference the FEMA National Risk Index. Deliverable is a tract-level dataset and a ranked list of the 500 tracts with the worst payout-to-policy ratio.

**Needs:** nothing.

### DATA-012: Fit bridge deterioration curves from 30 years of NBI

**Scores:** $:2 CV:4 VIR:3 USE:2 ALT:4 | **Effort:** M | **Repo:** public

FHWA's National Bridge Inventory has annual condition ratings back to the early 1990s. Build per-bridge rating trajectories, fit survival curves by material, design, and traffic class, and flag bridges whose decline rate is in the worst decile for their cohort. Deliverable is a modeled dataset plus a map of fast-declining bridges within two miles of a school.

**Needs:** nothing.

### DATA-013: Test FCC broadband claims against measured speeds

**Scores:** $:2 CV:5 VIR:5 USE:3 ALT:5 | **Effort:** L | **Repo:** public

The FCC Broadband Data Collection publishes claimed service by location, and Ookla releases open quarterly performance tiles under CC BY-NC-SA. Aggregate BDC claims to the Ookla tile grid, compute the gap between advertised and observed median download speed per tile for WV and western PA, and publish a "claimed versus measured" map with per-provider summary tables. Done means the license terms of the Ookla tiles are honored in the published output.

**Needs:** nothing.

### DATA-014: Measure three decades of airline schedule padding

**Scores:** $:2 CV:4 VIR:5 USE:2 ALT:3 | **Effort:** M | **Repo:** public

BTS On-Time Performance data includes both scheduled and actual elapsed time for every domestic flight since 1987. Compute per-route scheduled block time trends versus actual air time, isolating how much of the on-time-arrival improvement is padding rather than speed. Deliverable is a route-level dataset and a chart set showing the worst padded routes at PIT and CLE.

**Needs:** nothing.

### DATA-015: Compute a bus-factor score for the npm dependency graph

**Scores:** $:3 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Pull package metadata from the npm registry and dependency edges from the deps.dev API, then compute for each package the number of distinct publishers in the last two years weighted by downstream transitive download volume. Rank the single-maintainer packages that the most downstream weekly installs depend on. Deliverable is a refreshable dataset and a leaderboard site.

**Needs:** nothing.

### DATA-016: Chart time-to-fix for vulnerabilities by ecosystem

**Scores:** $:3 CV:5 VIR:4 USE:3 ALT:4 | **Effort:** M | **Repo:** public

Join NVD CVE records, the OSV database, and GitHub Security Advisories to compute the interval from first public disclosure to a fixed release version, broken out by ecosystem (npm, PyPI, Maven, crates, Go). Deliverable is a dataset plus a distribution chart per ecosystem with a stated methodology for handling backported fixes.

**Needs:** nothing.

### DATA-017: Fit per-tag decay constants for Stack Exchange question volume

**Scores:** $:1 CV:4 VIR:5 USE:2 ALT:3 | **Effort:** M | **Repo:** public

The Stack Exchange data dump on the Internet Archive is CC BY-SA. Compute monthly question counts per tag from 2015 to present, fit an exponential decay from each tag's peak, and rank tags by how fast they collapsed. Deliverable is a dataset of decay constants and an interactive chart where a reader picks a tag.

**Needs:** nothing.

### DATA-018: Measure the half-life of a trending GitHub repository

**Scores:** $:2 CV:4 VIR:5 USE:2 ALT:3 | **Effort:** M | **Repo:** public

GH Archive publishes hourly event JSON. Sample WatchEvent streams for repos that crossed 1,000 stars in a week, then track commit, issue, and PR activity for the following 12 months. Deliverable is a cohort dataset answering how many viral repos still have any commit activity a year later, plus survival curves split by whether the repo had a company behind it.

**Needs:** nothing. Sample rather than downloading full years, given disk limits.

### DATA-019: Track AI crawler policy adoption across the web

**Scores:** $:2 CV:4 VIR:5 USE:3 ALT:4 | **Effort:** M | **Repo:** public

Common Crawl publishes a robots.txt-only WARC subset per crawl. Parse several crawls spanning 2023 to present, measure adoption of `GPTBot`, `ClaudeBot`, `CCBot`, and `Google-Extended` directives plus the presence of `/llms.txt`, and break results out by site rank band and site category. Deliverable is a longitudinal dataset and a chart set.

**Needs:** nothing.

### DATA-020: Measure stylometric drift in arXiv abstracts since 2018

**Scores:** $:1 CV:5 VIR:5 USE:2 ALT:4 | **Effort:** M | **Repo:** public

Pull abstracts via the arXiv OAI-PMH interface, compute per-month frequency of a preregistered marker list (delve, intricate, underscore, tapestry, "it is worth noting"), plus perplexity under a fixed local model and sentence-length variance. Deliverable is a dataset by primary category and month with a clear statement that markers indicate style, not authorship.

**Needs:** nothing.

### DATA-021: Compare NIH funding to disease burden by state

**Scores:** $:1 CV:5 VIR:4 USE:1 ALT:5 | **Effort:** L | **Repo:** public

Pull awards from NIH RePORTER, map each to a disease category via its RCDC spending category tags, and compare per-state funding dollars to age-adjusted mortality and years-of-life-lost from CDC WONDER. Deliverable is a funding-versus-burden ratio dataset by state and disease, with the Appalachian counties broken out separately.

**Needs:** nothing.

### DATA-022: Refresh the trial results-reporting compliance scoreboard

**Scores:** $:1 CV:4 VIR:4 USE:1 ALT:5 | **Effort:** S | **Repo:** public

ClinicalTrials.gov's v2 API exposes completion dates, results-posting dates, and FDAAA applicability. Compute current per-sponsor compliance rates and days-overdue distributions, focusing on academic medical centers, and publish an updated leaderboard with a CSV release. Done means the definition of "applicable clinical trial" is stated and testable.

**Needs:** nothing.

### DATA-025: Cluster CFPB complaint narratives into emerging problem types

**Scores:** $:3 CV:5 VIR:4 USE:2 ALT:5 | **Effort:** L | **Repo:** public

The CFPB Consumer Complaint Database publishes consented narratives. Embed them locally, cluster with HDBSCAN, label clusters with `qwen3.6:27b`, and compute which clusters are growing fastest quarter over quarter per company. Deliverable is a labeled cluster dataset plus an early-warning dashboard of complaint types rising before any enforcement action.

**Needs:** nothing.

### DATA-026: Chart the growth of banking deserts in Appalachia

**Scores:** $:1 CV:3 VIR:3 USE:2 ALT:4 | **Effort:** S | **Repo:** public

FDIC's Summary of Deposits gives branch-level locations and deposits annually. Compute branch counts and nearest-branch distance per census tract for the Appalachian Regional Commission county set from 2010 to present, and publish the tract series plus a map of tracts that lost their last branch.

**Needs:** nothing.

### DATA-027: Render a county-to-county migration Sankey for West Virginia

**Scores:** $:1 CV:3 VIR:4 USE:3 ALT:3 | **Effort:** S | **Repo:** public

IRS SOI publishes county-to-county migration flows with returns, exemptions, and aggregate AGI. Build an interactive Sankey of inflows and outflows for every WV county over the available years, with an AGI-weighted view showing whether the people leaving earn more than those arriving.

**Needs:** nothing.

### DATA-029: Score every US county for company-town employment concentration

**Scores:** $:2 CV:4 VIR:4 USE:2 ALT:4 | **Effort:** M | **Repo:** public

BLS QCEW publishes county-by-industry employment quarterly. Compute a Herfindahl-Hirschman index of employment concentration per county per year, identify counties where a single NAICS 4-digit industry exceeds 25 percent of private employment, and track how those counties fared after their dominant industry contracted. Deliverable is a county-year dataset with a ranked "most concentrated" list.

**Needs:** nothing.

### DATA-032: Do a wind-sector analysis of PM2.5 around the Clairton coke works

**Scores:** $:2 CV:5 VIR:5 USE:3 ALT:5 | **Effort:** L | **Repo:** public

Combine OpenAQ regulatory monitor data, PurpleAir community sensors, and hourly ASOS wind from NOAA at Allegheny County Airport. Compute conditional bivariate probability functions to show which wind directions carry elevated PM2.5 to which neighborhoods, and publish polar plots per monitor plus the processed hourly dataset. Done means PurpleAir readings are corrected with the published EPA correction factor.

**Needs:** a free PurpleAir API key.

### DATA-033: List facilities in significant noncompliance with no enforcement

**Scores:** $:1 CV:4 VIR:4 USE:2 ALT:5 | **Effort:** S | **Repo:** public

EPA ECHO's downloadable data sets flag facilities in significant noncompliance under the Clean Water Act and Clean Air Act, and separately record formal enforcement actions. Produce the list of facilities in SNC for four or more consecutive quarters with no formal action, sorted by state, and publish it as a CSV with per-facility ECHO deep links.

**Needs:** nothing.

### DATA-034: Rank Appalachian counties by toxic release per capita

**Scores:** $:1 CV:3 VIR:3 USE:2 ALT:4 | **Effort:** S | **Repo:** public

EPA's Toxics Release Inventory basic data files give facility-level on-site and off-site releases by chemical. Aggregate to county, weight by the EPA RSEI hazard score rather than raw pounds, normalize by ACS population, and publish the ranked county table with a per-chemical breakdown.

**Needs:** nothing.

### DATA-035: Test whether MSHA violation history predicts mine injuries

**Scores:** $:1 CV:4 VIR:3 USE:1 ALT:5 | **Effort:** M | **Repo:** public

MSHA publishes open datasets for mine inspections, violations, accidents, and quarterly employment hours. Build a mine-quarter panel of citations by severity against subsequent lost-time injuries per 200,000 hours, and evaluate whether specific citation standards carry predictive signal. Deliverable is the panel dataset plus a model card with honest predictive-accuracy numbers.

**Needs:** nothing.

### DATA-036: Publish a shifting-frost-date dataset for gardeners

**Scores:** $:2 CV:3 VIR:4 USE:4 ALT:5 | **Effort:** S | **Repo:** public

NOAA GHCN-Daily has station-level daily minimum temperatures back a century. Compute the last-spring-freeze and first-fall-freeze date per station per year, fit a trend, and publish a ZIP-code lookup that reports how many days the local growing season has shifted since 1970 with a confidence interval.

**Needs:** nothing.

### DATA-037: Quantify flood warning lead time on Ohio River tributaries

**Scores:** $:1 CV:4 VIR:3 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Pull USGS NWIS instantaneous gauge height for tributaries feeding the Ohio between Pittsburgh and Wheeling, and NWS flood-stage thresholds from the AHPS metadata. For every historical exceedance, compute the lag between upstream gauge rise and downstream crest, producing an empirical lead-time table per gauge pair that a resident could act on.

**Needs:** nothing.

### DATA-038: Build a flash-flood microclimate profile for the Ohio Valley

**Scores:** $:1 CV:3 VIR:3 USE:3 ALT:4 | **Effort:** S | **Repo:** public

NOAA's Storm Events Database records every flash flood with narrative, time, damage estimate, and location. Extract the Ohio Valley subset, cluster by hollow and drainage using coordinates joined to USGS watershed boundaries, and publish a per-watershed frequency and seasonality table plus the parsed narratives.

**Needs:** nothing.

### DATA-039: Relate pedestrian fatality severity to vehicle hood geometry

**Scores:** $:1 CV:5 VIR:5 USE:1 ALT:5 | **Effort:** M | **Repo:** public

NHTSA FARS records the striking vehicle VIN for pedestrian fatalities. Decode VINs through the free vPIC API to get body class, model year, and gross vehicle weight rating, then model fatality counts per registered vehicle-year by body class using registration counts as the exposure denominator. Deliverable is the joined dataset and a chart of risk per body class over time.

**Needs:** nothing.

### DATA-040: Build a recall early-warning detector from NHTSA complaints

**Scores:** $:3 CV:5 VIR:4 USE:2 ALT:5 | **Effort:** L | **Repo:** public

NHTSA publishes both consumer complaints with free-text narratives and the recall database with campaign dates. Classify historical complaint narratives with a local model into failure-mode categories, then backtest whether a per-make-model-component complaint surge would have flagged known recalls before they were issued. Deliverable is the labeled complaint corpus, the detector, and a measured lead-time distribution against real recalls.

**Needs:** nothing.

### DATA-041: Track risk-factor and buzzword inflation in 10-K filings

**Scores:** $:2 CV:4 VIR:4 USE:2 ALT:3 | **Effort:** S | **Repo:** public

SEC EDGAR full-text search plus the financial statement data sets give every 10-K since 2001. Measure Item 1A risk-factor word count and the per-filing rate of "artificial intelligence," "generative," and "large language model" mentions by SIC code and year, normalized by total filing length. Publish the series and a chart of which industries adopted the language first.

**Needs:** nothing.

### DATA-042: Parse congressional trading disclosures into a clean dataset

**Scores:** $:3 CV:5 VIR:5 USE:1 ALT:5 | **Effort:** XL | **Repo:** public

House and Senate periodic transaction reports are published as scanned or generated PDFs with no consistent structure. Build a parser combining `pdfplumber` layout extraction with a local vision-free LLM fallback for the scanned filings, emit normalized ticker, date, direction, and amount-band records, and validate against a hand-keyed 300-filing sample with a published accuracy figure. Publish the dataset with per-record links back to the source PDF.

**Needs:** nothing.

### DATA-043: Build a lobbying revolving-door graph

**Scores:** $:2 CV:5 VIR:5 USE:1 ALT:5 | **Effort:** L | **Repo:** public

Senate LDA filings are available as bulk XML and name covered officials with prior government positions. Extract lobbyist-to-agency-to-client edges, resolve entities against Congress.gov member data, and publish a graph dataset plus an explorer that traces staffers who moved from a committee to clients regulated by that committee. Done means entity resolution accuracy is measured on a labeled sample.

**Needs:** nothing.

### DATA-044: Measure the lifespan of federal regulations

**Scores:** $:1 CV:4 VIR:4 USE:1 ALT:4 | **Effort:** S | **Repo:** public

The Federal Register API records every final rule with its CFR citations and effective date. Compute, per agency, the distribution of time between a rule's effective date and the first subsequent rule amending or removing the same CFR section, and publish an agency-level regulatory-churn table plus the underlying rule pairs.

**Needs:** nothing.

### DATA-045: Compare pro se and represented outcomes in federal civil cases

**Scores:** $:1 CV:5 VIR:4 USE:1 ALT:5 | **Effort:** M | **Repo:** public

CourtListener's RECAP API exposes docket entries, party representation, and case dispositions. Extract federal civil cases with at least one unrepresented party, compute dismissal and summary-judgment rates against represented controls within case type and district, and publish the case-level dataset with a documented sample-selection caveat.

**Needs:** a free CourtListener API token.

### DATA-046: Identify aircraft registered to opaque shell entities

**Scores:** $:1 CV:3 VIR:4 USE:1 ALT:3 | **Effort:** S | **Repo:** public

The FAA Aircraft Registry releasable database is a free monthly download with registered owner name and address. Flag registrants whose name matches LLC or trust patterns and whose address matches a known registered-agent service, aggregate by state and aircraft category, and publish the flagged subset with counts by agent address.

**Needs:** nothing.

### DATA-047: Benchmark library funding against circulation and program reach

**Scores:** $:1 CV:3 VIR:2 USE:2 ALT:5 | **Effort:** S | **Repo:** public

The IMLS Public Libraries Survey publishes per-library revenue, staffing, circulation, program attendance, and public-internet sessions annually. Build a peer-group comparison dataset that normalizes by legal service area population, and publish per-library scorecards for every library in WV and western PA.

**Needs:** nothing.

### DATA-048: Catalog degree program closures in Appalachian colleges

**Scores:** $:1 CV:3 VIR:3 USE:2 ALT:4 | **Effort:** S | **Repo:** public

IPEDS Completions files list every CIP-coded program with degrees conferred per institution per year. Detect programs that went from nonzero conferrals to zero for three consecutive years across ARC-region institutions, and publish the closure list with enrollment context from IPEDS Fall Enrollment.

**Needs:** nothing.

### DATA-049: Detect species range shifts from citizen-science observations

**Scores:** $:1 CV:4 VIR:3 USE:1 ALT:4 | **Effort:** M | **Repo:** public

GBIF aggregates iNaturalist and eBird records with coordinates and dates under open licenses. For a chosen set of Appalachian indicator species, compute annual mean latitude and elevation of observations with effort correction for observer growth, and publish the corrected range-centroid series with the caveats of opportunistic sampling stated plainly.

**Needs:** nothing.

### DATA-050: Build an agent pipeline that turns any CKAN portal into a clean dataset

**Scores:** $:4 CV:5 VIR:4 USE:5 ALT:5 | **Effort:** XL | **Repo:** public

Most government open-data portals run CKAN or Socrata with machine-readable catalog APIs, and most of their resources are dirty CSVs. Build a pipeline that takes a portal URL, enumerates resources, profiles each with type and unit inference, applies local-LLM column-name normalization, writes parquet plus a generated datapackage.json and Hugging Face dataset card, and stands up a Datasette instance. Done means it runs unattended against three portals (WPRDC, data.wv.gov, data.gov) and produces publishable artifacts without human editing.

**Needs:** nothing.

