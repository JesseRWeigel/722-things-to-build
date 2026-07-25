# Creative Arts: Music, Image, Video

Generative work with a committed aesthetic, built mostly on local models and hand-written algorithms; VRAM cost is noted wherever the 5090 does the rendering.

### ART-001: Build a seeded contact-sheet catalog with a curation gate

**Scores:** $:2 CV:4 VIR:3 USE:5 ALT:4 | **Effort:** M | **Repo:** public

A generation harness that records model, seed, sampler, steps, and prompt for every image, renders batches into printed-proof-style contact sheets, and requires an explicit keep/kill decision per frame before anything leaves the staging folder. The kill decisions accumulate into a training set for ART-002; the point is that nothing gets published because it was merely generated. SDXL at fp16 runs about 10 GB VRAM, so batches of eight fit comfortably.

**Needs:** nothing

### ART-003: Train a style LoRA on open-access museum collections

**Scores:** $:3 CV:5 VIR:4 USE:4 ALT:5 | **Effort:** L | **Repo:** public

Pull CC0 works from the Met and Rijksmuseum open-access APIs (ukiyo-e woodblock prints are the strongest candidate: flat color, strong line, consistent composition), curate a few hundred, caption them structurally, and train an SDXL LoRA. Release the LoRA, the curated dataset, and the caption schema on Hugging Face. SDXL LoRA training fits in roughly 14 GB with gradient checkpointing at 1024px.

**Needs:** nothing

### ART-005: Build an architectural photo to ink-drawing pipeline

**Scores:** $:4 CV:4 VIR:4 USE:3 ALT:4 | **Effort:** M | **Repo:** public

Chain depth and line extraction (Depth Anything plus a line-art preprocessor) into ControlNet so the output preserves the building's real geometry while the rendering becomes a hand-inked drawing with consistent hatching weight. Because the structure comes from the photo, the results are architecturally honest, which is exactly what generic image models fail at. Runs at about 12 GB with SDXL plus two ControlNets.

**Needs:** nothing

### ART-007: Build a palette-locked pixel art sprite engine

**Scores:** $:4 CV:4 VIR:4 USE:5 ALT:4 | **Effort:** L | **Repo:** public

Generate character and item sprites that snap to a fixed 16-color palette and a true pixel grid (no anti-aliased mush), with a sprite-sheet assembler that enforces consistent silhouette size and anchor point across a set. Post-process with nearest-neighbor downsampling and palette quantization rather than asking the model to draw pixels, then ship the sheets into Idle Abyss and HunterPath. Base generation is SDXL at roughly 10 GB.

**Needs:** nothing

### ART-008: Build a risograph separation generator

**Scores:** $:3 CV:4 VIR:4 USE:3 ALT:4 | **Effort:** M | **Repo:** public

Take any image or generative composition and separate it into two or three riso spot-color layers with authentic registration offset, ink-density limits, and paper-tone simulation, emitting both a print-ready per-layer PDF and a preview composite. Riso's constraints (limited inks, misregistration, coarse halftone) are an aesthetic, so model them accurately instead of applying a filter.

**Needs:** a riso print shop if the files are ever physically printed; the digital deliverable stands alone

### ART-009: Implement a real dithering and halftone toolkit

**Scores:** $:2 CV:4 VIR:4 USE:4 ALT:5 | **Effort:** S | **Repo:** public

Implement Atkinson, Riemersma, blue-noise, and ordered-Bayer dithering plus rotated-screen halftoning correctly, with per-channel control and a comparison gallery at 1:1 pixel zoom. Most implementations floating around are wrong in specific ways; a correct one with a visual test suite is a genuinely useful public artifact.

**Needs:** nothing

### ART-010: Build a generative book cover system

**Scores:** $:4 CV:4 VIR:3 USE:3 ALT:4 | **Effort:** M | **Repo:** public

A system where a book's metadata drives a covers series with shared grid, type scale, and color logic, so twenty covers read as one imprint. Type is set with real font metrics in SVG, imagery is generated or algorithmic, and the output includes spine and back panel at print trim with bleed.

**Needs:** nothing

### ART-011: Build an illuminated manuscript initial generator

**Scores:** $:3 CV:4 VIR:5 USE:4 ALT:4 | **Effort:** M | **Repo:** public

Generate decorated drop-capitals in a medieval insular or gothic idiom: an algorithmic interlace-knot generator for the border geometry (real over-under braid topology, not a texture), with painted infill from a style LoRA, exported as SVG with the letterform as clean vector. Ties directly into any devotional or print project and looks nothing like default diffusion output.

**Needs:** nothing

### ART-012: Build a stained glass window generator

**Scores:** $:3 CV:4 VIR:5 USE:4 ALT:4 | **Effort:** M | **Repo:** public

Generate tracery and came layouts as constrained planar subdivisions, assign a glass palette with realistic transmission colors, and render both a flat SVG (cuttable, with each piece numbered) and a lit simulation with light diffusion through the glass. Constrain shapes to what a glazier could actually cut so the output is a buildable pattern.

**Needs:** nothing

### ART-013: Run a local image-model shootout with a real cost table

**Scores:** $:3 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Build a fixed 60-prompt suite (typography, hands, specific compositions, negative-space control, style adherence) and run SDXL, SD 3.5 Large, FLUX.1-schnell, FLUX.1-dev, and Qwen-Image, publishing a grid with measured VRAM peak, seconds per image, and disk footprint per model on the 5090. Approximate expectations to verify: SDXL near 10 GB, SD 3.5 Large near 18 GB, FLUX.1-dev near 24 GB at bf16 and near 12 GB at fp8, Qwen-Image needing quantization to fit.

**Needs:** roughly 60-80 GB of disk for the model set, against 157 GB free; delete as you go

### ART-014: Build a latent interpolation film renderer

**Scores:** $:2 CV:3 VIR:4 USE:3 ALT:3 | **Effort:** S | **Repo:** public

Walk spherical-interpolated paths through latent and prompt-embedding space, render at consistent seed and sampler, and assemble with ffmpeg into a slow morph film with motion-matched audio. Add a jitter-suppression pass that fixes the frame-to-frame flicker most latent walks suffer from.

**Needs:** nothing

### ART-015: Make prompt-free work by sculpting noise directly

**Scores:** $:1 CV:4 VIR:5 USE:3 ALT:3 | **Effort:** S | **Repo:** public

Skip text conditioning entirely and drive an unconditional or CFG-zero diffusion pass with hand-authored noise fields (Perlin, tiled, radially structured), showing how much composition control lives in the initial latent rather than in the prompt. A short essay with a grid of results is a genuinely novel post, since almost all published work treats the prompt as the only lever.

**Needs:** nothing

### ART-017: Build a flow-field engine with layered ink simulation

**Scores:** $:3 CV:4 VIR:4 USE:3 ALT:4 | **Effort:** M | **Repo:** public

Flow fields are the most overdone generative form, so the differentiator is treating the output as physical media: particle paths deposit ink with pressure, absorption, and layering across multiple passes, and the field itself is driven by real data rather than noise (wind data, elevation, or gravitational-wave strain). Export both a plotter-safe stroke version and a full-resolution painted render.

**Needs:** nothing

### ART-018: Build a reaction-diffusion poster press

**Scores:** $:3 CV:3 VIR:4 USE:3 ALT:3 | **Effort:** S | **Repo:** public

Run Gray-Scott on the GPU via a WebGL or CUDA compute kernel, seed it with a mask (a letterform, a shoreline, a constellation) so the pattern grows into a recognizable structure, and export at 300 dpi for 18x24 inch prints. Ship a parameter atlas showing the feed/kill space so anyone can navigate to a pattern they want.

**Needs:** nothing

### ART-020: Build a Wang and Truchet tile system

**Scores:** $:2 CV:4 VIR:3 USE:3 ALT:4 | **Effort:** S | **Repo:** public

Implement corner-matching Wang tiles with a stochastic-but-valid placement solver and a Truchet tile set with curvature continuity across edges, producing infinite non-repeating patterns that tile seamlessly. Emit SVG for print, a seamless PNG for texturing, and a live web page where the tile set is editable.

**Needs:** nothing

### ART-021: Build a signed-distance-field sculpture gallery

**Scores:** $:2 CV:5 VIR:4 USE:3 ALT:4 | **Effort:** M | **Repo:** public

Author a set of raymarched SDF sculptures with real lighting (soft shadows via cone tracing, ambient occlusion from distance sampling), each under 200 lines of shader, then publish them in a WebGL gallery with the source visible and editable next to the render. Include marching-cubes export to STL so any piece can be printed.

**Needs:** nothing

### ART-022: Run a year-long shader-a-day practice with a curator

**Scores:** $:3 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** XL | **Repo:** public

One fragment shader per day for a year, generated and refined by `qwen3-coder:30b` in a compile-render-critique loop where a vision model judges the frame against the day's stated constraint and iterates until it passes. Publish as a browsable gallery with source, the constraint, and the number of iterations it took; the failure counts are as interesting as the successes.

**Needs:** nothing

### ART-023: Build an audio-reactive WebGL visual system for live performance

**Scores:** $:4 CV:5 VIR:5 USE:3 ALT:4 | **Effort:** L | **Repo:** public

A performance-ready visual engine that takes live audio input, extracts onset, spectral centroid, and beat phase in a worklet, and drives a scene graph of composable visual modules with MIDI-mappable parameters and preset morphing. Must hold 60fps at 1080p with no allocation in the render loop, which is the engineering that separates it from a demo.

**Needs:** a MIDI controller for the full performance workflow; keyboard mapping works without one

### ART-024: Build a Hydra live-coding archive

**Scores:** $:1 CV:3 VIR:4 USE:3 ALT:5 | **Effort:** S | **Repo:** public

Curate and publish a set of original Hydra live-coding patches with a static site that renders each one live, shows the source, and supports a permalink that encodes the patch in the URL. Include an annotated progression from simplest to most complex so it works as a teaching artifact.

**Needs:** nothing

### ART-025: Build a generative quilt pattern engine with embroidery export

**Scores:** $:4 CV:4 VIR:4 USE:3 ALT:5 | **Effort:** M | **Repo:** public

Generate quilt block layouts with real construction constraints (seam allowance, piece count, fabric yardage) and export both a cutting plan with a yardage table and a machine-embroidery file in PES and DST format via `pyembroidery`. The yardage calculation and stitch-order validation are what make it usable by an actual quilter.

**Needs:** nothing

### ART-026: Build a variable-font animation engine

**Scores:** $:3 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** M | **Repo:** public

Animate along variable-font axes (weight, width, optical size, and any custom axis) with per-glyph stagger, easing curves defined in a timeline DSL, and export to both CSS and rendered frames for video. Include a mode that interpolates through the design space along a path rather than a straight line between two instances, which produces motion nobody else's tool makes.

**Needs:** nothing

### ART-027: Build a type specimen generator

**Scores:** $:3 CV:4 VIR:3 USE:3 ALT:5 | **Effort:** S | **Repo:** public

Point it at any font file and it produces a full specimen: waterfall, character set with Unicode coverage map, kerning-pair stress strings, OpenType feature demos for every feature the font declares, and optical-size comparisons, laid out with real typographic judgment rather than a template. Reads the font's actual metrics and feature tables with `fontTools`.

**Needs:** nothing

### ART-028: Build an ambigram and constrained-lettering generator

**Scores:** $:3 CV:4 VIR:5 USE:3 ALT:4 | **Effort:** M | **Repo:** public

Generate rotational and mirror ambigrams by solving glyph-pair correspondences against a skeleton library, then thickening the skeletons into a coherent letterform with consistent stroke modulation. This is a real geometry problem with a satisfying visual payoff, and the resulting SVGs are directly plottable or laser-cuttable.

**Needs:** nothing

### ART-029: Build a kinetic typography music video pipeline

**Scores:** $:4 CV:5 VIR:5 USE:3 ALT:4 | **Effort:** L | **Repo:** public

Force-align lyrics to audio at the word level with a local alignment model, then drive a typographic composition where emphasis, scale, and position derive from measured audio dynamics rather than from arbitrary keyframes. Renders through the variable-font engine to frames, composited with ffmpeg. Use it on original or licensed music only.

**Needs:** an original or permissively-licensed track, which ART-041 can supply

### ART-030: Design and ship an original parametric typeface

**Scores:** $:5 CV:5 VIR:5 USE:3 ALT:5 | **Effort:** XL | **Repo:** public

Build a typeface from a parametric skeleton system (stroke paths plus contour generation), compile to a variable OTF with `fontTools`, and ship a real font: full Latin coverage, correct sidebearings, a hand-tuned kerning table, hinting, and a specimen site. Releasing an original open-source variable typeface is a portfolio piece of a different order than any generated image.

**Needs:** nothing

### ART-031: Run a local music-model shootout with a VRAM table

**Scores:** $:3 CV:5 VIR:5 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Evaluate Stable Audio Open, MusicGen Large, and ACE-Step on a fixed prompt suite covering texture, rhythmic precision, loop-point cleanliness, and stereo image, publishing measured VRAM peak and real-time factor on the 5090. Approximate expectations to verify: Stable Audio Open near 8 GB for 47-second stereo, MusicGen Large near 10 GB, ACE-Step in the 12 to 16 GB range.

**Needs:** roughly 30 GB of disk for the model set

### ART-032: Build a clean-license loopable ambient bed generator

**Scores:** $:5 CV:4 VIR:3 USE:5 ALT:5 | **Effort:** M | **Repo:** public

Generate ambient beds that actually loop: crossfade-free seam matching via phase-aligned splice points, LUFS normalization, and a validator that renders three consecutive loops and measures discontinuity at the seams. Every bed ships with its model, seed, and license so it can be used in podcasts and videos without any rights ambiguity.

**Needs:** nothing

### ART-033: Build a music-theory constraint composer

**Scores:** $:4 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** XL | **Repo:** public

A symbolic composition engine where a constraint solver enforces real voice-leading rules (no parallel fifths or octaves, proper resolution of tendency tones, range and spacing limits per voice, species counterpoint) and generates four-part writing that a theory professor would mark correct. Render to MIDI, then to audio through a soundfont, and expose a mode where an LLM proposes harmonic plans that the solver either realizes or rejects with the specific rule violated.

**Needs:** a General MIDI soundfont such as FluidR3 for rendering

### ART-034: Build an infinite browser ambient generator

**Scores:** $:3 CV:4 VIR:4 USE:4 ALT:5 | **Effort:** S | **Repo:** public

A single self-contained web page that generates endless non-repeating ambient music with Web Audio: layered oscillator voices in a fixed mode, slow LFO drift, a convolution reverb from a generated impulse response, and probabilistic note events on a Eno-style tape-loop timing scheme. No samples, no network calls, no repeat after the first minute.

**Needs:** nothing

### ART-035: Build an adaptive layered game music system

**Scores:** $:4 CV:5 VIR:3 USE:5 ALT:4 | **Effort:** M | **Repo:** public

Compose stem sets (base, tension, combat, resolution) that are tempo and key locked, and build a runtime that crossfades layers on game state with beat-quantized transitions so cues never enter off the grid. Wire it into Idle Abyss and HunterPath as the reference integration, and ship the runtime as a standalone package.

**Needs:** nothing

### ART-036: Build a procedural sound-effects synthesizer

**Scores:** $:4 CV:4 VIR:4 USE:5 ALT:5 | **Effort:** S | **Repo:** public

Synthesize game SFX from parameter sets (impacts, pickups, UI clicks, footsteps on varied surfaces) using real synthesis techniques (noise shaping, modal resonators, granular scattering) with seeded variation so a hundred footsteps never sound identical. Runs on CPU with zero model weights, exports WAV banks, and includes a browser editor.

**Needs:** nothing

### ART-038: Build a spectrogram image encoder

**Scores:** $:2 CV:4 VIR:5 USE:2 ALT:3 | **Effort:** S | **Repo:** public

Encode an image into audio so it appears in the spectrogram when played, using an inverse-STFT with phase reconstruction that produces something listenable rather than pure noise, plus a decoder that recovers the image from a recording of the playback. The round-trip through air is what makes it a genuinely interesting demo.

**Needs:** nothing

### ART-039: Build a git-history sonification

**Scores:** $:2 CV:4 VIR:5 USE:4 ALT:4 | **Effort:** S | **Repo:** public

Map a repo's commit history to music with a defensible mapping (contributor to timbre, lines changed to velocity, directory depth to register, commit interval to rhythm) and render a piece per repo alongside a synchronized visualization of the file tree lighting up. Publish the mapping rationale, because the mapping is the composition.

**Needs:** nothing

### ART-041: Produce and release a full original album from the pipelines

**Scores:** $:4 CV:5 VIR:5 USE:4 ALT:4 | **Effort:** XL | **Repo:** public

Eight to ten tracks built from the constraint composer, the local audio models, and the procedural synthesis toolkit, mixed and mastered to streaming LUFS targets, with album art from the image pipeline, a printed-quality digital booklet documenting how each track was made, and distribution to Bandcamp. The documentation of method is the artistic statement, and every source is either original or clean-licensed.

**Needs:** a Bandcamp account; a distributor account if it goes to streaming services

### ART-042: Run a local video-model shootout and ship shorts from it

**Scores:** $:4 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** L | **Repo:** public

Evaluate LTX-Video and the Wan family on a fixed prompt suite testing motion coherence, camera control, and temporal stability, publish measured VRAM and seconds-per-second-of-output on the 5090, then use the winner to produce a set of finished shorts with a consistent look. Approximate expectations to verify: LTX-Video 2B near 12 GB and notably fast, Wan 1.3B near 8 GB, Wan 14B needing quantization to fit under 32 GB.

**Needs:** roughly 60 GB of disk for the model set

### ART-043: Build a seamless live-wallpaper loop generator

**Scores:** $:4 CV:4 VIR:4 USE:4 ALT:4 | **Effort:** M | **Repo:** public

Generate short image-to-video clips and force perfect looping with a boomerang-free approach: optical-flow-guided blending across a matched frame pair found by embedding similarity, verified by a loop-seam detector that measures discontinuity. Export in the formats desktop and phone wallpaper engines want, with a battery-friendly low-framerate variant.

**Needs:** nothing

### ART-044: Build a datamoshing toolkit

**Scores:** $:2 CV:4 VIR:5 USE:2 ALT:4 | **Effort:** S | **Repo:** public

Implement controlled datamoshing by manipulating the compressed bitstream directly (I-frame removal, P-frame duplication, motion-vector transplants between clips) rather than by applying a glitch filter, with parameters for how far the corruption is allowed to propagate. Doing it at the codec level is what produces the real bloom effect and makes it worth publishing.

**Needs:** nothing

### ART-046: Build an ASCII and ANSI video renderer with a terminal player

**Scores:** $:2 CV:4 VIR:5 USE:3 ALT:4 | **Effort:** S | **Repo:** public

Convert video to truecolor ANSI using half-block characters for double vertical resolution, with dithering against the terminal palette and per-frame delta encoding so playback stays smooth over SSH. Ship a `.cast`-compatible export and a player that syncs audio, then publish one genuinely watchable short in the format.

**Needs:** nothing

### ART-049: Build a print-spec-correct generative poster line

**Scores:** $:5 CV:4 VIR:3 USE:3 ALT:4 | **Effort:** M | **Repo:** public

Produce a cohesive series of twelve posters where the generative system is shared and each piece is a parameter variation, exported to real print specification: CMYK conversion with a soft-proof preview, 300 dpi at final trim, correct bleed and safe area, and embedded color profile. Getting the print pipeline right is the difference between files and a sellable product.

**Needs:** a print-on-demand account if selling; the files are complete without one

### ART-050: Build a permalink-seed generative art gallery

**Scores:** $:4 CV:5 VIR:5 USE:4 ALT:5 | **Effort:** XL | **Repo:** public

A self-hosted gallery where every piece is a deterministic function of a seed, the seed lives in the URL, and the page renders the artwork live in the browser rather than serving a stored image, with a high-resolution export path and full source shown alongside. Include a curation layer where the aesthetic scorer from ART-002 pre-ranks the seed space and a human picks the edition, plus print ordering for any seed. This is the container that gives every other project in this file a permanent home.

**Needs:** a domain and hosting (Vercel hobby tier covers it); a print-on-demand integration if selling prints

