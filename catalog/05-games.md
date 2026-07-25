# Games & Interactive Experiences

Playable artifacts: browser games, roguelikes, idle systems, multiplayer experiments, Minecraft mods and plugins, WebXR, and games where a language model is a first-class mechanic.

### GAME-001: Build Prompt Golf, a puzzle game about steering a local model in as few tokens as possible

**Scores:** $:2 CV:4 VIR:5 USE:3 ALT:4 | **Effort:** M | **Repo:** public

Each level gives a target output string and a locked local model (`gemma4:e4b` for speed) at temperature 0; the player writes a prompt and scores on token count, with a par value per hole. Ship 30 hand-tuned holes, a deterministic seeded server so scores are comparable, and a global leaderboard. Determinism is the whole product: pin the model digest, seed, and sampler and publish them on the scoreboard page.

**Needs:** a small always-on host for the shared leaderboard (Vercel + Neon free tier is enough); the model runs on the RTX 5090 behind a tunnel or the site can ship a WebLLM build for offline play.

### GAME-002: Build an LLM dungeon master that can never contradict itself

**Scores:** $:4 CV:5 VIR:4 USE:4 ALT:4 | **Effort:** L | **Repo:** public

The failure mode of every AI text adventure is drift. Fix it structurally: hold the world in a SQLite entity/relation store, and restrict the model (`qwen3.6:27b`) to emitting *proposed state transitions* as JSON that a rules engine validates before any prose is generated. Narration is a second pass over the committed diff. Done means a 200-turn session where an automated checker finds zero contradictions in item locations, NPC deaths, or door states.

**Needs:** nothing

### GAME-003: Run a Mineflayer bot tournament with ELO and a spectator web UI

**Scores:** $:2 CV:5 VIR:5 USE:4 ALT:3 | **Effort:** L | **Repo:** public

Turn the existing swarm into a competitive league: define three fixed scenarios (speed-mine to diamond, 1v1 arena, cooperative build-to-spec), run round-robin matches on a headless Paper server via cron, compute ELO, and render live matches in a browser using prismarine-viewer with a leaderboard and match replay. Different bot brains (`gpt-oss:20b` vs `qwen3-coder:30b` vs a scripted baseline) enter as separate competitors.

**Needs:** nothing

### GAME-004: Ship Regexle, a daily puzzle where you guess a regex from its matches

**Scores:** $:2 CV:3 VIR:5 USE:2 ALT:4 | **Effort:** S | **Repo:** public

Each day shows five strings that match and five that do not; the player submits a regex and gets per-string feedback until they find one that separates the sets. Puzzle generation picks a hidden pattern, then searches for adversarial near-miss strings that kill lazy answers like `.*`. Static site, puzzles pregenerated for a year, share-a-grid emoji result for the social loop.

**Needs:** nothing

### GAME-005: Self-host a Semantle clone on local embeddings with a difficulty-tuned word list

**Scores:** $:1 CV:3 VIR:3 USE:2 ALT:4 | **Effort:** S | **Repo:** public

Compute embeddings locally for a 40k-word vocabulary, precompute the full similarity ranking for 365 target words, and ship a static site where the whole day's ranking table is a compressed blob the client already has. No server, no API cost, instant guesses. Tune target selection so the median solve is 40 to 60 guesses using a simulated solver.

**Needs:** nothing

### GAME-007: Write a Minecraft plugin giving villagers persistent LLM memory and grudges

**Scores:** $:3 CV:4 VIR:5 USE:4 ALT:4 | **Effort:** L | **Repo:** public

A Paper plugin where each villager keeps a small append-only memory of events involving nearby players (trades, hits, gifts, buildings placed) in SQLite, summarized nightly by `gemma4:e4b`. Dialogue comes from `gpt-oss:20b` conditioned on that memory, and disposition drives real mechanics: prices, willingness to trade, and whether the iron golem defends you. Done means a villager who still resents you three sessions later and says why.

**Needs:** nothing

### GAME-008: Build Ollamon, a creature battler where every creature is a different local model

**Scores:** $:2 CV:4 VIR:5 USE:3 ALT:3 | **Effort:** M | **Repo:** public

Each of the twelve creatures is backed by one of the installed Ollama models; its stats are derived from measured properties (parameter count becomes HP, tokens/sec becomes speed, benchmark accuracy becomes attack) and its "moves" are prompts it must answer under a token budget, judged by a fixed referee model. Battles are deterministic given a seed. The joke lands, and the underlying measurement harness is real.

**Needs:** nothing

### GAME-009: Turn any GitHub repository into an explorable dungeon

**Scores:** $:2 CV:4 VIR:5 USE:3 ALT:4 | **Effort:** M | **Repo:** public

`npx repo-quest <owner/repo>` clones a repo and maps it to a roguelike: directories become rooms, imports become doors, file size sets room size, cyclomatic complexity spawns monsters, and test files become healing fountains. Playable in the terminal with a browser export. The mapping has to feel earned, so tune it against five well-known repos until the layout is recognizably the architecture.

**Needs:** nothing

### GAME-010: Ship a text adventure whose model runs entirely in the browser tab

**Scores:** $:2 CV:5 VIR:4 USE:3 ALT:4 | **Effort:** M | **Repo:** public

No server, no API key, no telemetry: a WebLLM or transformers.js build of a small instruct model handles the parser and the flavor text, while the game logic stays deterministic in TypeScript. The novelty is that the whole thing is a static file you can save and play on a plane in ten years. Publish it as a Hugging Face Space with the weights pulled from the Hub.

**Needs:** nothing

### GAME-011: Build a social deduction game where one player is a language model

**Scores:** $:3 CV:4 VIR:5 USE:3 ALT:4 | **Effort:** M | **Repo:** public

Five players in a chat room, one of whom is a local model told to blend in; everyone votes at the end on who was artificial. Log every round with the model, the prompt, and the vote outcome, and publish the accumulated detection rate per model as a live chart. That dataset is the reason this outlives the novelty.

**Needs:** a public deployment for real players (Vercel + a websocket host such as a small Fly.io or Railway free instance); local-only LAN play works without it.

### GAME-012: Write a print-and-play card game where the cards are prompts

**Scores:** $:3 CV:2 VIR:4 USE:2 ALT:3 | **Effort:** S | **Repo:** public

A party game for three to six people plus one laptop: players draft modifier cards ("in iambic pentameter", "as a legal filing", "convinced it is a lighthouse") to build a prompt, a local model answers, and a rotating judge scores. Deliverable is a print-ready PDF at poker size plus a 40-line local scoring server. Sell it on itch.io as pay-what-you-want.

**Needs:** nothing

### GAME-013: Build a fog-of-war chess variant with a model as the commentator

**Scores:** $:2 CV:3 VIR:4 USE:2 ALT:3 | **Effort:** M | **Repo:** public

Each player sees only squares their pieces attack. The interesting part is the commentary track: a model that also only sees one player's fog, so its running analysis is confidently wrong in exactly the way the player is, and the postgame reveals both. Use chess.js for legality, Stockfish WASM for the eventual truth, and a local model for the narration.

**Needs:** nothing

### GAME-015: Generate a Metroidvania that is provably completable

**Scores:** $:3 CV:5 VIR:4 USE:3 ALT:4 | **Effort:** L | **Repo:** public

Most procedural metroidvanias cheat by placing abilities randomly and praying. Do it properly: build the lock-and-key dependency graph first, verify solvability with a reachability solver after every placement, then lay geometry onto the validated graph. Ship the generator as a standalone TypeScript library with a playable Phaser demo and a visualizer of the dependency graph next to the map.

**Needs:** nothing

### GAME-016: Build a real-time strategy game controlled only by typed natural-language orders

**Scores:** $:3 CV:5 VIR:5 USE:3 ALT:3 | **Effort:** L | **Repo:** public

No unit selection, no click-to-move. You type "send the archers around the left ridge and hold until the cavalry engage" and a small local model compiles it into a structured order DSL that the deterministic simulation executes. Misparses are part of the game. Ship the DSL, the grammar-constrained decoding setup, and a replay format that stores the original text alongside the compiled orders.

**Needs:** nothing

### GAME-017: Add a headless simulation mode to idle-abyss and rebalance it from a million runs

**Scores:** $:3 CV:4 VIR:2 USE:5 ALT:2 | **Effort:** M | **Repo:** public

Extract the game loop from rendering so it can run a million simulated playthroughs in minutes, then chart time-to-first-prestige, currency inflation, and the point where upgrades stop mattering. Use the output to retune the curve and ship the simulator as a permanent CI check that fails a PR if any progression gate moves more than 15 percent.

**Needs:** nothing

### GAME-018: Give HunterPath deterministic replays and an automated playtester

**Scores:** $:2 CV:5 VIR:2 USE:5 ALT:2 | **Effort:** M | **Repo:** public

HunterPath currently has zero tests. Rather than writing unit tests for UI, make the combat and progression systems deterministic under a seeded RNG, add a replay file format, then write a bot that plays 50,000 seeded runs and reports win rates per build. The replay corpus becomes the regression suite, which is a far better story for an interview than "added Jest".

**Needs:** nothing

### GAME-020: Ship a game that fits inside a single QR code

**Scores:** $:1 CV:3 VIR:5 USE:1 ALT:2 | **Effort:** S | **Repo:** public

A complete playable game in under 2,953 bytes, encoded as a `data:text/html` URI in one QR code you can print on a sticker. The constraint forces genuine cleverness: no libraries, no assets, procedural everything. Publish the QR image, the source, and a writeup of what got cut to make the budget.

**Needs:** nothing

### GAME-021: Generate a hex-crawl tabletop map from real OpenStreetMap data

**Scores:** $:3 CV:4 VIR:4 USE:3 ALT:4 | **Effort:** M | **Repo:** public

Feed it a bounding box and it pulls OSM data (ODbL, properly attributed), classifies terrain into hex tiles, converts real roads into trade routes and real churches and mills into points of interest, then has a local model write a two-sentence rumor for each hex in a chosen genre. Output is a printable PDF and a Foundry VTT scene. Playing a fantasy campaign on the real map of your own county is the hook.

**Needs:** nothing

### GAME-024: Build an adversarial word-game host that cheats legally

**Scores:** $:1 CV:3 VIR:4 USE:2 ALT:3 | **Effort:** S | **Repo:** public

The host never commits to a word: it keeps the full set of candidates consistent with every clue given so far and answers each guess with whatever response leaves the largest remaining set. Ship it for hangman and a five-letter word game, and add a "show the host's remaining candidates" toggle so players can watch themselves being strung along.

**Needs:** nothing

### GAME-025: Turn any Wikipedia article into a playable text adventure

**Scores:** $:2 CV:4 VIR:5 USE:2 ALT:4 | **Effort:** M | **Repo:** public

Paste a URL, get a short adventure grounded in the article's actual facts: entities become objects, section structure becomes rooms, and a local model writes only the connective prose while a fact checker verifies every claim against the source text. Refuse to generate when the article is too thin. Being unable to hallucinate is the feature, and the fact-check pass is the reusable piece.

**Needs:** nothing

### GAME-026: Ship a Zachtronics-style programming puzzle game with a real instruction set

**Scores:** $:5 CV:5 VIR:5 USE:3 ALT:4 | **Effort:** XL | **Repo:** public

Design a small assembly language for a fictional machine, write a cycle-accurate visual simulator, and build 40 puzzles with a difficulty curve that teaches the ISA without tutorials. Include per-puzzle histograms of cycle count and instruction count across all players, which is the mechanic that makes these games compulsive. This is the single most sellable item in this category: itch.io and eventually Steam.

**Needs:** a Steam Direct fee ($100) only if going to Steam; itch.io release costs nothing.

### GAME-027: Build a persistent MUD served over SSH

**Scores:** $:3 CV:5 VIR:5 USE:3 ALT:4 | **Effort:** XL | **Repo:** public

`ssh play@host` drops you straight into a persistent world with no client, no account creation, and keys as identity. Build the server in Node with an SSH library, a tick-based simulation, a persistent world in SQLite, and a scripting layer so content can be added without restarts. Add an LLM only where it earns its place, such as ambient NPC chatter that never affects state. SSH-as-a-front-door reliably gets attention.

**Needs:** a public host with port 22 or an alternate port exposed, plus abuse rate limiting; a $5/month VPS or a free-tier instance covers it.

### GAME-028: Build a play-by-cron 4X where turns resolve overnight

**Scores:** $:4 CV:5 VIR:4 USE:3 ALT:3 | **Effort:** XL | **Repo:** public

Players submit orders any time during the day; at 3am a cron job resolves every empire's turn simultaneously, runs combat, and emails or Discord-DMs each player a narrated turn report generated from the real state diff. The design constraint of one turn per day makes a genuinely deep economy playable by adults with jobs. Includes an AI empire that uses a local model only for diplomacy text, never for mechanics.

**Needs:** an always-on host for the cron resolver and a transactional email or Discord webhook; Vercel cron plus Neon suffices.

### GAME-029: Build a programmable computer inside Minecraft as a mod

**Scores:** $:3 CV:5 VIR:5 USE:3 ALT:4 | **Effort:** XL | **Repo:** public

A NeoForge mod adding a block that runs a sandboxed scripting VM with in-world I/O: read redstone, drive displays, talk to other computers over an in-world network, and persist programs in the world save. Ship an in-game editor and a standard library for common builds. This is a large, well-understood engineering problem with a clear artifact, and it reuses the toolchain from the Percy Jackson mod.

**Needs:** nothing

### GAME-030: Simulate a civilization of LLM factions on a long-running Minecraft server

**Scores:** $:3 CV:5 VIR:5 USE:4 ALT:3 | **Effort:** XL | **Repo:** public

Four to six factions of Mineflayer bots with territory, resources, memory, and diplomacy, running continuously for weeks while a web dashboard shows borders, treaties, wars, and a generated chronicle of events. Faction decisions come from a local model constrained to a fixed action schema; the world state is authoritative. The deliverable that matters is the multi-week chronicle, which is genuinely fun to read.

**Needs:** sustained GPU availability for the inference loop; budget it as the machine's overnight job so it does not collide with other work.

### GAME-031: Ship a complete game in one HTML file under 13 kilobytes

**Scores:** $:1 CV:4 VIR:4 USE:2 ALT:3 | **Effort:** S | **Repo:** public

js13k rules, no jam required: procedural audio via Web Audio, procedural graphics via canvas, zero dependencies, all state in memory. Write up the size budget line by line, because the writeup is what gets shared. Aim it at the actual js13kGames jam in August if the timing lines up.

**Needs:** nothing

### GAME-032: Publish a terminal game distributed entirely through npx

**Scores:** $:2 CV:3 VIR:4 USE:2 ALT:4 | **Effort:** S | **Repo:** public

One command, no install, no config, works over SSH on a server you are debugging at 2am. Pick something that genuinely suits a terminal: a tight tactics puzzle or an incremental game that saves to `~/.config`. Ship with `--no-color` and screen-reader-friendly output, which almost no terminal game bothers with.

**Needs:** nothing

### GAME-033: Build a two-player game that needs no server at all

**Scores:** $:2 CV:4 VIR:3 USE:3 ALT:4 | **Effort:** S | **Repo:** public

WebRTC with manual signaling: player one gets an offer blob to paste into any chat app, player two pastes back an answer, and the game runs peer to peer with no backend, no accounts, and no hosting bill. Ship it as a reusable template plus one finished game on top. The template is the durable contribution.

**Needs:** nothing

### GAME-035: Generate a daily themed chess puzzle site from the public Lichess database

**Scores:** $:3 CV:3 VIR:3 USE:2 ALT:5 | **Effort:** S | **Repo:** public

The Lichess puzzle database is CC0 and enormous. Build a static site that serves a themed puzzle each day (Mondays are back-rank, Tuesdays are deflection) with a difficulty ladder tuned to the player's history in localStorage, and a monthly printable PDF sheet for people who want to solve on paper.

**Needs:** nothing

### GAME-036: Build a typing game over real open-source code

**Scores:** $:2 CV:3 VIR:4 USE:3 ALT:4 | **Effort:** S | **Repo:** public

Type real functions pulled from popular repositories, with syntax highlighting live and per-language stats on which characters slow you down (brackets, underscores, arrows). Add a "worst characters" drill mode generated from your own history. Include the leaderboard as a public GitHub gist so there is no backend.

**Needs:** nothing

### GAME-038: Ship a leaderboard service that runs on nothing but GitHub gists

**Scores:** $:2 CV:3 VIR:3 USE:4 ALT:4 | **Effort:** S | **Repo:** public

A tiny library plus a serverless function that lets jam games have persistent leaderboards with no database, using a gist as append-only storage with signed score submissions to make casual tampering annoying. Document the threat model honestly, including what it does not protect against. Game jam developers will actually use this.

**Needs:** a GitHub token with gist scope (already available) and one serverless endpoint to hold the signing key.

### GAME-039: Build a wave function collapse level generator as a real library

**Scores:** $:3 CV:5 VIR:3 USE:3 ALT:5 | **Effort:** M | **Repo:** public

Most WFC implementations are demos. Ship a proper TypeScript library: backtracking, weighted tiles, hard constraints for guaranteed connectivity, incremental regeneration of a sub-region, and a debug view showing entropy per cell during collapse. Publish to npm with a Phaser and a plain-canvas adapter, and a documented tileset format.

**Needs:** nothing

### GAME-040: Build a game of Nomic where a model is the judge

**Scores:** $:1 CV:4 VIR:5 USE:2 ALT:3 | **Effort:** M | **Repo:** public

Nomic is the game where changing the rules is the move. Implement it as a web app where players propose rule amendments in plain English, a local model rules on whether a proposed amendment contradicts the current rule set, and the full rule history is versioned in git. Publish the transcripts of games that broke, because the failures are the interesting output.

**Needs:** nothing

### GAME-041: Build a boss fight that reads your play and adapts between phases

**Scores:** $:3 CV:5 VIR:5 USE:3 ALT:3 | **Effort:** M | **Repo:** public

A single-encounter game where, between phases, a local model receives a structured summary of the player's behavior (dodge direction bias, preferred range, panic patterns) and selects the next phase's attack composition from a fixed library. No text generation in the loop, so it stays fast and fair, and the model's reasoning is shown as the boss taunting you about your habits.

**Needs:** nothing

### GAME-042: Build a draw-and-guess game judged by a local vision model

**Scores:** $:2 CV:4 VIR:5 USE:2 ALT:3 | **Effort:** M | **Repo:** public

Single-player Pictionary against a machine: you draw, a local vision-capable model guesses in real time as strokes appear, and you win by getting it to say the word before the timer. Log every drawing plus the guess trajectory and publish the corpus of "drawings that fooled it", which is both funny and a real evaluation dataset.

**Needs:** a vision-capable local model; `gemma4` multimodal variants or a small VLM pulled from Hugging Face, mindful of the 157 GB disk budget.

### GAME-043: Build a roguelike whose generated items are simulation-verified before they ship

**Scores:** $:3 CV:5 VIR:4 USE:3 ALT:3 | **Effort:** M | **Repo:** public

A local model proposes item effects as structured data; a headless battle simulator then plays 10,000 fights with each candidate item and rejects anything that pushes win rate outside a target band or creates an infinite loop. Only survivors enter the game. Ship the item corpus and the rejection log side by side, because the rejected items are hilarious and make the case for the pipeline.

**Needs:** nothing

### GAME-044: Build a kanji and kana writing game with stroke-order recognition

**Scores:** $:4 CV:4 VIR:3 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Draw on a canvas, get scored on stroke order, direction, and proportion against KanjiVG data, not just final shape. Add SRS scheduling over the JLPT lists and a mode that drills only the characters where your stroke order is actually wrong. Ties directly into the language-learning work and fills a real gap, since most apps grade the finished glyph.

**Needs:** nothing

### GAME-046: Build a bot that plays your web game and reports where the difficulty spikes

**Scores:** $:4 CV:5 VIR:4 USE:5 ALT:4 | **Effort:** L | **Repo:** public

Point it at a deployed browser game; it drives the page with Playwright, uses a simple learned or scripted policy to play, and produces a report of time-to-clear per level, death heatmaps, and the exact point where the curve breaks. Works without game source access by reading canvas frames and DOM state. Indie developers pay for this kind of feedback, so it is the most plausible paid tool here.

**Needs:** nothing

### GAME-047: Teach Mineflayer bots to build from a photograph

**Scores:** $:2 CV:5 VIR:5 USE:4 ALT:3 | **Effort:** L | **Repo:** public

Feed the swarm an image of a building; a vision model produces a coarse voxel plan, a solver converts it to a block-by-block build order respecting gravity and scaffolding, and the bots divide the work and build it in survival mode including gathering the materials. Done means a recognizable structure built from a photo with no human intervention, filmed as a timelapse.

**Needs:** a vision-capable local model, same disk caveat as GAME-042.

### GAME-048: Enter a real game jam with an autonomous agent and document every failure

**Scores:** $:2 CV:5 VIR:5 USE:4 ALT:4 | **Effort:** L | **Repo:** public

Pick a 48-hour jam with a public theme announcement, give an agent fleet the theme and a fixed engine, and let it design, build, test, and submit with a hard rule that humans only press the submit button. Stream the git history publicly. Whether the entry is good is beside the point; the honest log of where autonomy broke down is the artifact, and it is the strongest interview story in this file.

**Needs:** an itch.io account for jam submission (free).

### GAME-049: Give idle-abyss a seasonal shared-world ladder

**Scores:** $:4 CV:4 VIR:4 USE:5 ALT:3 | **Effort:** L | **Repo:** public

Add a server-authoritative season: a shared boss whose health pool drains from every player's contributed damage, a weekly modifier, and a persistent ladder, while keeping the offline-first single-player game intact. The hard part is cheat resistance in an idle game, so design the client to submit compressed action logs the server replays rather than trusting reported scores, and write that design up.

**Needs:** a hosted backend with a database; Vercel functions plus Neon on the free tier is enough at this scale.

