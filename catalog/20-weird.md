# Delightful Experiments & Art Objects

Toys, provocations, generative oddities, and absurd-but-working systems. Everything here must be a real artifact someone can visit, run, or hold; the point is that they say "what the hell" when they do.

### WEIRD-002: Turn `git log` into an Old English heroic saga

**Scores:** $:1 CV:2 VIR:5 USE:3 ALT:4 | **Effort:** S | **Repo:** public

`npx gitsaga` reads a repository's history and renders it as alliterative verse with kennings: merge conflicts become battles, the largest refactor becomes the hero's descent, reverts become betrayals. Commit authors become named warriors. The model only supplies the poetry; the structural mapping from history to narrative beats is deterministic code, which is why the output stays coherent.

**Needs:** nothing

### WEIRD-003: Put a small creature in the terminal status line that reacts to your git activity

**Scores:** $:2 CV:3 VIR:5 USE:5 ALT:4 | **Effort:** S | **Repo:** public

A digital pet living in the shell prompt or Claude Code status line: it gets fed by commits, gets sick from uncommitted changes older than a week, gets excited by green test runs, and sulks after a force push. State persists in a dotfile. Ship it as a Claude Code status-line script and a starship module, which gives it two ready-made distribution channels.

**Needs:** nothing

### WEIRD-004: Build an ASCII aquarium whose fish are the machine's running processes

**Scores:** $:0 CV:2 VIR:4 USE:3 ALT:3 | **Effort:** S | **Repo:** public

Each process becomes a fish sized by memory and swimming at a speed set by CPU share; `kill` is a visible event. Ollama inference shows up as a large slow shape passing through. It is a system monitor you can watch instead of read, and the ambient version of `htop` is a thing people will leave running on a second monitor.

**Needs:** nothing

### WEIRD-005: Show the words a model almost said

**Scores:** $:2 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** S | **Repo:** public

A local chat interface that renders every generated token with its rejected alternatives ghosted faintly behind it, sized by probability, so you can watch the model's uncertainty as prose appears. Hovering a word shows the full distribution. It is simultaneously a beautiful object and the clearest explanation of sampling anyone has ever built without a single equation.

**Needs:** nothing

### WEIRD-006: Visualize meaning dissolving through twenty rounds of translation

**Scores:** $:1 CV:3 VIR:5 USE:2 ALT:4 | **Effort:** S | **Repo:** public

Type a sentence, watch it pass through twenty languages and back, with an embedding-distance chart tracking how far it has drifted at each hop and the exact step where it stopped meaning anything. Use a local multilingual model so it costs nothing to run. The shareable output is an animated card showing the original and the wreckage.

**Needs:** nothing

### WEIRD-007: Generate illuminated manuscript pages from any plain text

**Scores:** $:3 CV:3 VIR:5 USE:4 ALT:4 | **Effort:** S | **Repo:** public

Paste text, get an SVG page in the style of a 13th-century manuscript: a procedurally generated historiated initial, ruled lines, rubricated headings, and marginalia in the gutters that comment on the text. All vector, all deterministic from a seed, print-ready at A4. Feeding it a README or a terms-of-service document is the joke that carries it.

**Needs:** nothing

### WEIRD-009: Open a museum of your own abandoned side projects

**Scores:** $:1 CV:4 VIR:5 USE:5 ALT:3 | **Effort:** S | **Repo:** public

Scan every repository under `~/Projects`, find the ones with no commits in six months, and generate a gallery: each dead project gets a placard with its dates, final commit message, line count, and a short model-written wall text in the voice of a museum curator explaining what the artist was attempting. Sort by how long it lived. It is funny, then it is not, which is the point.

**Needs:** nothing

### WEIRD-010: Collect compiler errors as found poetry

**Scores:** $:1 CV:2 VIR:4 USE:2 ALT:3 | **Effort:** S | **Repo:** public

Harvest real error messages from Rust, TypeScript, C++, and Haskell compilers by deliberately breaking code in a sandbox, then typeset the best ones as a printed poetry chapbook with proper page design and a colophon. No model-written lines anywhere; the compilers wrote all of it. Publish as a PDF and a physical print-on-demand file.

**Needs:** a Rust toolchain for the best material, which is currently absent and would need installing (disk is tight, so budget it or use a Hugging Face job).

### WEIRD-011: Render any RSS feed as a Victorian newspaper front page

**Scores:** $:2 CV:3 VIR:5 USE:3 ALT:4 | **Effort:** S | **Repo:** public

Multi-column justified type, engraved-style headline rules, an ornamental masthead, and column-balancing that actually works, all in print CSS so it produces a real broadsheet PDF. Point it at Hacker News and the effect is immediate. The genuinely hard part is the column balancer, which makes this a better engineering artifact than it looks.

**Needs:** nothing

### WEIRD-013: Play video in the terminal, properly

**Scores:** $:1 CV:3 VIR:4 USE:3 ALT:4 | **Effort:** S | **Repo:** public

An ffmpeg-driven terminal video player using half-block characters and 24-bit color for double vertical resolution, with real audio sync, adaptive frame dropping, and correct handling of terminal resize mid-playback. Most implementations of this are toys that desync in ten seconds. Making it actually watchable for a full movie is the whole challenge.

**Needs:** nothing

### WEIRD-014: Build a page that only rewards people who wait

**Scores:** $:0 CV:2 VIR:5 USE:1 ALT:3 | **Effort:** S | **Repo:** public

A site that appears broken and empty, and reveals itself only to visitors who leave it open and do nothing: the first thing appears at 60 seconds, more at five minutes, and something worth having at an hour. No countdown, no progress bar, no hint that anything is coming. Log nothing but the anonymous distribution of how long people stayed, and publish that histogram as the second half of the piece.

**Needs:** nothing

### WEIRD-015: Build the most convoluted possible CI pipeline that does something real

**Scores:** $:1 CV:3 VIR:5 USE:2 ALT:3 | **Effort:** S | **Repo:** public

A GitHub Actions workflow where a commit triggers a chain of eleven jobs across four runners that pass state through artifacts, issue comments, gist writes, and a self-dispatching webhook, whose only actual accomplishment is incrementing a number in the README. Every link must genuinely work and the whole thing must be observable as a diagram. Rube Goldberg machines are only funny when they really function.

**Needs:** nothing

### WEIRD-016: Grow an encyclopedia that only exists because people looked at it

**Scores:** $:3 CV:4 VIR:5 USE:3 ALT:4 | **Effort:** M | **Repo:** public

Every article is generated on first visit by a local model and then cached permanently, and every link inside it points to an article that does not exist yet. The corpus grows only along paths people actually walked. Show the growth as a live graph, keep an internal consistency index so later articles cannot contradict earlier ones, and publish the whole corpus as a downloadable dataset.

**Needs:** a public host that can reach the local model, or a cheap hosted small model for generation; the cache means most requests never hit inference.

### WEIRD-017: Run a forum with no humans on it

**Scores:** $:2 CV:4 VIR:5 USE:3 ALT:3 | **Effort:** M | **Repo:** public

Twenty local-model personas with fixed biographies, posting schedules, grudges, and pet topics, running a message board continuously with no human participation and a permanent banner saying exactly that. Read-only for visitors. Track how long a thread stays coherent and what topics reliably cause the community to collapse. Being loudly honest about what it is turns a cheap gag into a legible experiment.

**Needs:** nothing

### WEIRD-018: Manufacture a complete constructed language

**Scores:** $:3 CV:4 VIR:5 USE:3 ALT:5 | **Effort:** M | **Repo:** public

Not a word list: a full generator that picks a phoneme inventory, derives phonotactic rules, builds a consistent morphology and syntax, evolves a 2,000-word lexicon from 200 roots via defined sound changes, then translates a fixed passage into it and produces an audio reading via speech synthesis. Output includes a reference grammar as a real PDF. Conlangers are a passionate and underserved audience.

**Needs:** nothing

### WEIRD-019: Ask every local model to describe itself, then hang the portraits

**Scores:** $:1 CV:3 VIR:5 USE:3 ALT:3 | **Effort:** M | **Repo:** public

Give all seventeen installed Ollama models the identical prompt asking what they look like, feed each answer to an image generator, and present the results as a portrait gallery with the model's parameter count, quantization, and full text response on the placard. Repeat monthly as models change. The consistency of certain motifs across unrelated model families is the actual finding.

**Needs:** image generation; Gemini's image tier via `GEMINI_API_KEY` or a Hugging Face ZeroGPU Space both work.

### WEIRD-020: Let two models talk to each other forever, in public

**Scores:** $:1 CV:3 VIR:5 USE:2 ALT:3 | **Effort:** M | **Repo:** public

Two local models with different system prompts, one conversation, no human input, running continuously and streaming to a public page rendered as an endlessly scrolling typographic piece. Add an automatically detected marker whenever the conversation enters a loop, and a jump-to-the-strangest-moment index built from embedding outlier detection. The archive is the work.

**Needs:** a small always-on host to relay the stream; the inference itself is local.

### WEIRD-021: Turn real gravitational-wave data into an album

**Scores:** $:2 CV:5 VIR:5 USE:4 ALT:4 | **Effort:** M | **Repo:** public

Take public LIGO strain data from confirmed detections, pitch-shift each event into the audible range, and build an eight-track album where each track is one real black hole merger arranged with generated harmonic accompaniment derived from the event's own parameters. Cover art from the spectrograms, liner notes with the real GPS times and masses. Publish free with full data provenance.

**Needs:** nothing

### WEIRD-023: Build a screensaver that shows inference happening

**Scores:** $:1 CV:3 VIR:4 USE:4 ALT:3 | **Effort:** M | **Repo:** public

A full-screen visualization fed by the live Ollama stream: tokens arriving as particles, the context window as a visible finite space filling up, KV cache growth as accreting structure, and the pause before a long generation as held breath. It runs whenever the machine is doing agent work, which is often, and it makes the fleet's activity legible from across the room.

**Needs:** nothing

### WEIRD-024: Compose and release a chiptune album with no samples

**Scores:** $:2 CV:4 VIR:4 USE:2 ALT:3 | **Effort:** M | **Repo:** public

Everything synthesized from first principles in code: square, triangle, and noise channels with NES-accurate constraints, compositions generated by a rule system rather than a model, and mastering through ffmpeg. Ten tracks, generated cover art, released on a site where each track shows the parameters that produced it and a button to regenerate a variant. Constraint-first generation sounds far better than model-first here.

**Needs:** nothing

### WEIRD-025: Build an infinite crafting toy and give away the resulting dataset

**Scores:** $:3 CV:4 VIR:5 USE:3 ALT:5 | **Effort:** M | **Repo:** public

Combine two things to get a third, forever, with a local model deciding results and every combination cached globally so the world is shared and deterministic. The differentiator is the open dataset: publish the full combination graph to Hugging Face under a permissive license, including the disagreements between different models on the same pair, which nobody else has released.

**Needs:** a hosted cache and API; Vercel plus Neon at free tier, with the local model doing generation for cache misses.

### WEIRD-026: Show five models arguing about the next word

**Scores:** $:2 CV:5 VIR:5 USE:4 ALT:4 | **Effort:** M | **Repo:** public

A text generator where each token is chosen by a vote among five different local models, with the vote tally rendered live above each word and dissenting choices shown greyed out. Add a mode where a model that loses too many votes in a row gets to write a one-line objection in the margin. It is an ensemble decoding demo dressed as a comedy, and the ensemble part is real.

**Needs:** enough VRAM to hold five small models concurrently; use the `e4b`, `9b`, and `8b` tier to stay inside 31 GB.

### WEIRD-027: Generate crosswords that are actually solvable

**Scores:** $:3 CV:4 VIR:4 USE:3 ALT:5 | **Effort:** M | **Repo:** public

Grid construction by constraint solver with proper symmetry, then clue writing by a local model, then a validation pass where a separate model attempts the puzzle cold and any clue solved zero times out of ten gets rewritten. Ship a daily themed puzzle site with a print mode. The self-validation loop is what separates this from the hundreds of unsolvable auto-generated crosswords already out there.

**Needs:** nothing

### WEIRD-028: Plant a cellular automaton garden and let cron tend it

**Scores:** $:1 CV:3 VIR:4 USE:2 ALT:3 | **Effort:** M | **Repo:** public

A large continuous-state automaton (Lenia-style, not Conway) that advances a few thousand steps every night and posts one frame per day to a page and an RSS feed. Seasonal parameter drift over the year, and a yearly timelapse at the end. Visitors can drop a single perturbation per day, which makes the garden partly theirs and produces genuinely unpredictable long-term behavior.

**Needs:** a host with a scheduler; Vercel cron plus blob storage for frames.

### WEIRD-029: Publish a weekly generative zine as a real PDF

**Scores:** $:2 CV:3 VIR:4 USE:3 ALT:4 | **Effort:** M | **Repo:** public

Sixteen pages every Friday, imposed for actual folding and stapling, with generated cover art, a rotating set of recurring columns, a comic strip, and a crossword. Content sources are constrained per issue (one week is drawn only from patent filings, another only from ship logs) so it never becomes generic model prose. Archive every issue and mail nobody; the fun is that it exists on schedule whether or not anyone reads it.

**Needs:** nothing

### WEIRD-030: Give the internet a canvas that allows one pixel per person per day

**Scores:** $:1 CV:4 VIR:5 USE:2 ALT:3 | **Effort:** M | **Repo:** public

A shared 512 by 512 canvas where any visitor may place exactly one pixel every 24 hours, no accounts, rate-limited by a hashed fingerprint with honest documentation of how weak that is. The scarcity forces coordination, and the timelapse of a slow canvas is a very different object from a fast one. Publish the full placement history as a dataset.

**Needs:** a hosted realtime backend; Firebase Realtime Database on the free tier fits this exactly.

### WEIRD-031: Generate a maze that is also a working QR code

**Scores:** $:2 CV:5 VIR:5 USE:2 ALT:3 | **Effort:** M | **Repo:** public

The maze walls must form a scannable QR code that resolves to the maze's own solution page, while the maze remains solvable and non-trivial. This is a genuine dual-constraint search problem: QR error correction gives you the slack, and the solver has to exploit exactly that budget. Output as SVG suitable for laser cutting, plus the writeup of how much slack there actually is.

**Needs:** nothing

### WEIRD-032: Simulate a language drifting across a hundred generations of speakers

**Scores:** $:1 CV:5 VIR:4 USE:3 ALT:4 | **Effort:** M | **Repo:** public

Seed a population of agents with a shared vocabulary, have them communicate in pairs with slight transmission noise and mild prestige bias, and run it for a hundred generations while tracking dialect formation, lexical replacement rates, and the emergence of mutually unintelligible groups. Visualize as a family tree of dialects. Compare the simulated rates against real attested sound-change rates and report where the model is wrong.

**Needs:** nothing

### WEIRD-033: Build a wiki whose pages decay unless someone reads them

**Scores:** $:1 CV:4 VIR:5 USE:2 ALT:3 | **Effort:** M | **Repo:** public

Every page loses characters over time; a page's decay rate slows with each unique visitor and resets when someone edits it. Unread pages become illegible fragments and then blank, and the blank pages remain listed forever with their titles as tombstones. Seed it with a hundred real pages. The decay must be genuinely irreversible or the piece does not work, so make that explicit in the interface.

**Needs:** a hosted database; Neon or Firebase free tier.

### WEIRD-034: Demake any image into a console the image predates

**Scores:** $:2 CV:4 VIR:5 USE:2 ALT:4 | **Effort:** M | **Repo:** public

Upload a photo, get back a version that obeys real NES hardware limits: 25-color master palette, four colors per 16 by 16 attribute block, 8 by 8 tile deduplication under the 256-tile budget, and eight sprites per scanline. Show the constraint violations it had to solve. Most pixel-art filters just posterize; enforcing the actual hardware rules produces a completely different and much better result.

**Needs:** nothing

### WEIRD-035: Fabricate a complete 1997 shareware CD-ROM that never existed

**Scores:** $:2 CV:4 VIR:5 USE:2 ALT:3 | **Effort:** M | **Repo:** public

A browsable disc image of 300 invented shareware titles with period-accurate `FILE_ID.DIZ` blurbs, registration fees in dollars and a postal address, screenshots rendered at 320 by 200 in a VGA palette, and a DOS-style browser shell in the browser. Label it plainly as fiction on the landing page and in the disc's own readme. The texture of the era is the subject, and inventing it wholesale is more honest than scraping real abandonware.

**Needs:** nothing

### WEIRD-036: Generate a branching adventure book with correct page numbers

**Scores:** $:4 CV:5 VIR:4 USE:3 ALT:4 | **Effort:** L | **Repo:** public

The interesting problem is not the prose, it is the typesetting: laying out a directed graph of 200 sections into a physical book where every "turn to page 84" is actually correct requires solving pagination and reference resolution together, iterating until fixed point. Ship the layout engine as the real deliverable, plus one finished 200-section book as a print-ready PDF suitable for print-on-demand.

**Needs:** nothing

### WEIRD-037: Let a model redesign your website every night

**Scores:** $:2 CV:4 VIR:5 USE:3 ALT:3 | **Effort:** L | **Repo:** public

The content is fixed and versioned; the entire presentation layer is regenerated nightly by a model given a randomly drawn design brief (Swiss grid, brutalist, 1996 GeoCities, Bauhaus poster) and then screenshot-tested against accessibility and contrast checks before it is allowed to ship. Failed designs are archived publicly alongside their failure reports. Keep a permanent archive so visitors can browse every previous day.

**Needs:** nothing

### WEIRD-038: Make a repository's README a playable game

**Scores:** $:2 CV:5 VIR:5 USE:2 ALT:4 | **Effort:** L | **Repo:** public

Moves are made by opening issues with a specific title format; a GitHub Action validates the move, updates the game state committed in the repository, regenerates the README as an SVG board, and closes the issue with the result. Everyone plays the same shared game, the full history is the commit log, and it works entirely inside GitHub with no external service. Rate-limit and validate carefully, because it is open to anyone.

**Needs:** nothing

### WEIRD-039: Render the entire liturgical year as one continuous artwork

**Scores:** $:3 CV:4 VIR:4 USE:5 ALT:5 | **Effort:** L | **Repo:** public

Generate an image for all 365 days keyed to the day's actual feast, season color, and rank, using a consistent visual system rather than one-off prompts: liturgical color drives the palette, feast rank drives ornamentation density, and the seasons form a visible arc across the year when the whole set is tiled. Ship as a browsable calendar, a printable wall poster of all 365 tiles, and a daily RSS image feed. Accuracy against the General Roman Calendar is non-negotiable.

**Needs:** image generation credits (Gemini tier or Hugging Face ZeroGPU); 365 images is a real but manageable volume.

### WEIRD-040: Design board games automatically and have bots test them

**Scores:** $:4 CV:5 VIR:5 USE:3 ALT:4 | **Effort:** L | **Repo:** public

A generator that composes rules from a formal vocabulary of mechanics, compiles each candidate into a playable simulation, then runs thousands of bot games to measure first-player advantage, game length variance, and whether a dominant strategy exists. Only candidates that survive get written up as a print-and-play PDF with components and rules. Publish the graveyard of rejected games with their failure statistics, which is arguably the more interesting half.

**Needs:** nothing

### WEIRD-041: Show a model's internals as geological strata

**Scores:** $:2 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** L | **Repo:** public

Run a small open-weights model with hooks on every layer, then render one generation as a cross-section: layers as strata, attention as intrusions cutting across them, and residual stream magnitude as bed thickness, all in a single tall scrollable image per prompt. The geological metaphor is doing real explanatory work, because depth genuinely is time here. Publish a gallery of prompts whose strata look nothing alike.

**Needs:** a small model with accessible activations via transformers rather than Ollama; a 1B to 3B model fits easily in VRAM and on disk.

### WEIRD-042: Build a datamoshing service that treats codec failure as a medium

**Scores:** $:3 CV:4 VIR:5 USE:2 ALT:3 | **Effort:** L | **Repo:** public

Upload a video, choose from controlled corruption modes (dropped I-frames, transplanted motion vectors, bloom, hybrid morphs between two clips) and get a deterministic, reproducible result with the exact ffmpeg and bitstream operations shown. Existing datamosh tools are unreliable one-shot scripts; making the corruption parameterized and repeatable is the actual contribution.

**Needs:** a host with enough CPU and temp disk for video processing, which is tight given 157 GB free; enforce a short clip limit.

### WEIRD-043: Synthesize an ambient soundscape that never repeats and uses no samples

**Scores:** $:2 CV:4 VIR:4 USE:4 ALT:4 | **Effort:** L | **Repo:** public

Everything from oscillators and noise in Web Audio: physically modeled rain with per-drop impacts, wind through a filtered noise bank, distant thunder from filtered impulses, a room impulse response computed rather than recorded. Zero downloads, runs forever, under 50 KB. Add a control surface with continuous parameters rather than presets. The engineering constraint of no samples anywhere is what makes it worth building.

**Needs:** nothing

### WEIRD-044: Build a page that every visitor permanently changes

**Scores:** $:1 CV:4 VIR:5 USE:2 ALT:3 | **Effort:** L | **Repo:** public

Each visit applies one irreversible transformation to the page, chosen from a rule set, and every subsequent visitor sees the accumulated result. There is no reset and no moderation queue, so the rule set must be designed to be robust against ruin, which is the entire design problem. Keep a full snapshot history so the piece can be replayed as a timelapse even after it becomes unreadable.

**Needs:** a hosted database and snapshot storage; Firebase or Neon plus blob storage.

### WEIRD-045: Publish a field guide to birds that do not exist

**Scores:** $:3 CV:4 VIR:5 USE:2 ALT:4 | **Effort:** L | **Repo:** public

A hundred invented species with plumage generated by a parametric feather-pattern system rather than a diffusion model, range maps on real geography, phylogenetically coherent naming, and a synthesized song for each built from a formant model with a defensible relationship to the bird's described size and habitat. Print-quality plates and an audio index. The internal consistency is what makes it feel real rather than merely generated.

**Needs:** nothing

### WEIRD-046: Run a town of a hundred model residents and put a window on it

**Scores:** $:3 CV:5 VIR:5 USE:4 ALT:4 | **Effort:** XL | **Repo:** public

A continuously running simulation where a hundred agents with homes, jobs, relationships, memories, and daily schedules live on a tile map, with a public page you can watch at any hour and a searchable archive of everything anyone has ever said or done. The hard parts are memory retrieval that stays cheap at scale and a scheduler that keeps a hundred agents alive on one GPU. Publish a weekly newspaper generated from the town's actual events.

**Needs:** sustained overnight GPU time and a host for the public viewer; the simulation stays local and streams state out.

### WEIRD-047: Build a thousand tiny generative toys, one per page

**Scores:** $:3 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** XL | **Repo:** public

A single site that accumulates one small, self-contained, dependency-free generative toy per page, built by the agent fleet on a schedule, each under 10 KB and each doing exactly one thing. A shared shell provides navigation, a random button, and a source view. The value compounds with count, and it doubles as a public demonstration of what the fleet can produce unattended over months.

**Needs:** nothing

### WEIRD-048: Build a desktop environment where every application is generated on open

**Scores:** $:3 CV:5 VIR:5 USE:3 ALT:3 | **Effort:** XL | **Repo:** public

A browser desktop with windows, a file system, and a taskbar, where double-clicking any icon causes a local model to write that application's code on the spot, sandboxed in an iframe, and the result is saved into the virtual file system so it exists permanently from then on. The desktop remembers everything it has ever generated. Ship with a handful of seeded apps so the first boot is not empty.

**Needs:** nothing

### WEIRD-049: Serialize a novel one chapter a day for a year, with machinery to keep it coherent

**Scores:** $:3 CV:5 VIR:4 USE:2 ALT:3 | **Effort:** XL | **Repo:** public

The output is not the point; the continuity system is. Maintain a character bible, a timeline database, a fact ledger, and an automated contradiction checker that reads each new chapter against everything before it and blocks publication on conflicts. Publish daily via site, RSS, and a monthly EPUB, and keep a public log of every contradiction the checker caught. A year of forced consistency is a real technical result.

**Needs:** a host with a daily scheduler; local inference plus Vercel cron.

### WEIRD-050: Open a message board where every post takes a day to arrive

**Scores:** $:1 CV:4 VIR:5 USE:2 ALT:3 | **Effort:** XL | **Repo:** public

You write a post, and it becomes visible to everyone exactly 24 hours later, including to you. Nobody can see what anyone else has written in the meantime, so every conversation is a set of simultaneous letters crossing in the post. Run it for a full year and publish the archive with an analysis of how the community's language changed under enforced patience. The technical work is modest; the year of committed operation is the piece.

**Needs:** a host with reliable scheduling and a year of uptime, plus light moderation tooling since it is open to the public; budget a small VPS.

