# LLM Selection and Calibration

The user selects which LLM will write the manuscript during Phase 2 setup. Each model has different strengths, and the plugin calibrates prompting density, chunk sizing, and revision-pass intensity to match.

## Why LLM Selection Matters

Pulp Adventure Romance demands specific prose qualities — propulsive cadence, banter under threat, sensory specificity in locale — that different models handle with different reliability. The plugin's behavior should adapt to the chosen model's profile rather than assume a single calibration.

## Model Profiles and Calibration

### Claude Opus (4.x and later)

**Strengths:** Long-form coherence, voice maintenance across chapters, nuanced subtext, sustained tone.
**Calibration:**
- Light-touch prompting per chapter — Opus self-corrects more reliably
- Larger chunk size — up to 8 chapters per drafting session for novella, 4–5 for novel
- ARIS check density: per chapter is sufficient (model rarely needs sub-chapter prompts)
- Editorial passes can be lighter; Opus tends to deliver cleaner first drafts

### Claude Sonnet (4.x and later)

**Strengths:** Balanced quality and throughput; reliable on genre-specific guardrails.
**Calibration:**
- Standard prompting per chapter — include ARIS tags inline with chapter directive
- Standard chunk size — 4 chapters per session for novella, 2–3 for novel
- ARIS check density: per chapter, with mid-chapter check on long set-pieces
- Editorial passes per pipeline default

### Claude Haiku (4.x and later)

**Strengths:** Fast throughput, capable of clean prose with explicit guardrails.
**Calibration:**
- Heavier prompting per chapter — restate ARIS rules inline at every chapter request
- Smaller chunk size — 1–2 chapters per session
- ARIS check density: mid-chapter check on every chapter; Haiku benefits from more frequent guardrail recalls
- Editorial passes: increase Stage 1 (AI-ism) intensity; Haiku is more prone to crutch phrases
- Banter under threat may need explicit reminder per pressure scene

### GPT-4 / GPT-4 Turbo

**Strengths:** Strong dialogue, varied sentence rhythm, willing on action set-pieces.
**Calibration:**
- Restate genre voice and heat level at the start of every chapter request
- Chunk size: 2–3 chapters per session
- ARIS check density: per chapter; GPT-4 occasionally drifts on McGuffin Gravity
- Editorial Stage 1 should specifically scrub GPT-4-typical phrasings ("a flicker of," "her gaze lingered," "what came next would change everything")
- Verify heat-level compliance carefully — GPT-4 sometimes drifts up or down a level
- Add explicit Anti-7 reminder before classic-pulp-era chapters

### Gemini (1.5 / 2.x and later)

**Strengths:** Worldbuilding texture, locale specificity, atmospheric prose.
**Calibration:**
- Restate ARIS rules in compact form at every chapter request
- Chunk size: 2 chapters per session
- ARIS check density: per chapter; Gemini occasionally over-prioritizes worldbuilding at expense of pacing
- Editorial Stage 3 (Developmental) should specifically check pacing and set-piece tension
- May need explicit reminder to maintain banter under threat (Gemini sometimes goes silent in action)
- Strong on classic-pulp era texture; may need pacing adjustments for contemporary-set books

### Other Models

If the user specifies a model not listed above:
1. Ask the user about the model's known strengths and weaknesses
2. Default to the Sonnet calibration as a balanced baseline
3. Tighten the editorial Stage 1 pass to scrub model-specific crutches discovered during drafting

## Universal Calibration (All Models)

Regardless of model:

- Always ask the user to confirm POV and tense at chapter 1 and re-confirm at chapter 5
- Always verify heat level at chapter 1 and at the first intimacy beat
- Always restate the ARIS rules at the start of any drafting session that follows a context refresh
- Always run the ARIS per-chapter checklist as a separate step from drafting

## Chunk Size Guidance

The chunk size determines how many chapters are drafted in a single session before pausing for ARIS checks and continuity review.

| Length Tier | Opus | Sonnet | Haiku | GPT-4 | Gemini |
|-------------|------|--------|-------|-------|--------|
| Novella (12–20 ch) | 6–8 | 4 | 1–2 | 2–3 | 2 |
| Novel (22–32 ch) | 4–5 | 2–3 | 1 | 2 | 2 |
| Extended (32–45 ch) | 3–4 | 2 | 1 | 1–2 | 1–2 |

After each chunk:
1. Run ARIS per-chapter checklist on every chapter in the chunk
2. Apply any interventions before the next chunk
3. Verify continuity (McGuffin position, character knowledge, timeline)

## Recording the Selection

In the ARIS chapter log, record the model used. If the user changes models mid-manuscript, record the chapter at which the change occurred. This aids any post-publication consistency review.
