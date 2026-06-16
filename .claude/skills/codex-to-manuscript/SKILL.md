---
name: codex-to-manuscript
description: >
  Turn a complete Codex + Outline package into a publish-ready manuscript. Parses the codex (story
  concept, structure, characters, locations, lore, subplots) and the chapter-by-chapter outline from
  PDF or DOCX, summarizes everything for the user, asks if they want to change names, places, POV,
  tense, heat level, length, or supply a writing sample, then writes the entire book
  chapter-by-chapter with edit-as-you-go editorial passes calibrated to the codex's genre. Outputs a
  single .docx manuscript plus a companion KDP metadata document. MANDATORY TRIGGERS - codex to
  manuscript, write from codex, codex writer, write from outline, codex and outline, write my codex,
  codex package, story pack to manuscript, turn codex into book, write from my codex, write from
  package, codex bridge, outline to manuscript, manuscript from codex, write from PDF outline,
  /write-from-codex.
version: 1.3.1
---

# Codex to Manuscript

A complete pipeline that turns a Codex + Outline package into a publish-ready first-draft manuscript.

The skill is built for customers who have purchased a Codex + Outline package (typically delivered as PDFs) and want the manuscript written. It accepts both PDF and DOCX, parses everything into structured data, lets the user adjust names / places / POV / heat / length / voice, then writes the book chapter-by-chapter with **edit-as-you-go** editorial passes calibrated to the codex's genre.

## Pipeline at a Glance

| Phase | What Happens | Output |
|---|---|---|
| 0 | Confirm output folder + receive uploads | Working folder set up |
| 1 | Parse codex + outline | Structured summary shown to user |
| 2 | Apply user revisions (names, places, POV, heat, length, style) | Revised codex/outline state in memory |
| 3 | Route genre to its guardrail system | Active guardrail loaded |
| 4 | Write each chapter + Edit-As-You-Go + integrity gate every 3 chapters | Drafted, edited chapters + Edit Log + integrity reports |
| 5 | Pre-editorial integrity gate → end-of-book editorial pipeline → final integrity gate | Polished manuscript |
| 6 | Assemble final .docx + KDP Info doc | Publish-ready files in customer's folder |

## What This Skill Produces

Per run, one folder in the customer's chosen location:

```
[Book Title]/
├── [Book Title].docx           — full manuscript at the codex's word count target
├── [Book Title] - KDP Info.docx — Amazon metadata, blurb, cover prompt
└── [Book Title] - Edit Log.md   — chapter-by-chapter edit notes
```

---

## Phase 0 — Setup

Before parsing anything, confirm with the user:

1. **Where to save the output.** Ask the user to specify the output folder. If they have already selected a Cowork directory, default to it but confirm.
2. **The codex and outline files.** Both must be uploaded (or pasted as text). Verify both are present before proceeding. Acceptable formats: `.pdf`, `.docx`, `.txt`, `.md`.
3. **Which Claude model to use for the writing pipeline.** Ask the user to choose, presenting the tradeoff table below. Record the choice — it gets logged in the Edit Log and the KDP Info doc.

| Model | Best for | Speed | Cost (per M output tokens) |
|---|---|---|---|
| Claude Opus 4.8 (newest) | Serious publishing — best prose, deepest character voice, highest editorial quality | Slowest | ~$25 |
| Claude Sonnet 4.6 | Fast iteration, novellas, tight budgets — excellent quality at lower cost | 2-3× faster | ~$15 |
| Claude Haiku 4.5 | Pipeline testing only — not recommended for publish-ready prose | 5-6× faster | ~$5 |

**IMPORTANT — Critical instruction to give the user:**

> "This pipeline runs in your current Claude conversation. The model writing your manuscript is whichever model your Claude window is set to right now — the plugin can't switch it for you. Before we continue, please verify the model selector at the top of your Claude window is set to **[their choice]**. If you're using a different model, switch now, and confirm when ready."

Wait for explicit confirmation before proceeding.

If only one of the codex/outline files is uploaded, ask the user for the other before continuing. The pipeline does not work with just one.

### Model consistency across a series

If the customer is writing book N of a series and book N-1 was written with a specific model, recommend they use the same model for consistency. Different models produce subtly different prose patterns — using the same model across a series keeps the voice locked. The KDP Info doc records the model used; check the previous book's KDP Info if available.

---

## Phase 1 — Parse Codex + Outline

Run both parser scripts:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/codex-to-manuscript/scripts/parse_codex.py \
  --in "/path/to/codex.pdf" \
  --out "/tmp/codex.json"

python3 ${CLAUDE_PLUGIN_ROOT}/skills/codex-to-manuscript/scripts/parse_outline.py \
  --in "/path/to/outline.pdf" \
  --out "/tmp/outline.json"
```

Both scripts handle PDF and DOCX automatically based on file extension.

After parsing, present a structured summary to the user:

> **I've parsed your package. Here's what I found:**
>
> **Story:** *[Title]* — [Genre/Subgenre]
> **Length:** [Word Count Target] / [Chapter Count Target]
> **POV:** [POV Mode], [alternating or single], from [POV Roster]
> **Heat:** [extracted heat level — see Heat detection below]
> **Hook:** [Hook (1 line)]
>
> **Characters parsed:** [N total]
> - [Full Name 1] ([Role 1])
> - [Full Name 2] ([Role 2])
> - …
>
> **Locations:** [N total]
> - [Location Name 1] ([Type])
> - …
>
> **Objects, Lore, Subplots:** [N objects], [N lore items], [N subplots]
>
> **Outline:** [N acts], [N chapters]

If parsing fails on any major section (zero characters extracted, or the chapter count is suspiciously low), check `reference/parsing_rules.md` for fallback strategies and try again.

### Heat detection

The codex usually doesn't have a single labeled "Heat Level" field. Detect it from:

- `concept.tropes_or_themes` (look for "Spicy," "Open-Door," "Closed-Door," "Sweet," "Scorching")
- `locked_elements.key_market_conventions` (look for "explicit," "open-door," "fade-to-black")
- `subplots[].subplot_summary` (mentions of intimate scenes)
- The "Tone & Style" or "Author Notes" section if present (often includes a `Spice Level:` label)

If heat is ambiguous, default to "open-door" for romance subgenres and "n/a" for non-romance.

---

## Phase 2 — User Revisions

Ask the user, using AskUserQuestion if available:

> **Want to change anything before I start writing?**
>
> 1. **Names or gender** — rename characters, swap pronouns, change pairings
> 2. **Places or setting** — rename locations, relocate the story
> 3. **POV / tense / heat** — switch POV mode, change tense, override heat level
> 4. **Length or writing sample** — override the word count target, supply a writing sample for voice matching
> 5. **No changes** — start writing as-is

For each requested change, follow the patterns in `reference/user_revisions.md`. Apply changes to the parsed codex AND the parsed outline before proceeding.

If the user supplies a writing sample, read it carefully and extract the voice fingerprints (sentence rhythm, adjective density, metaphor register, dialogue tag style, internal monologue depth, vocabulary register) — keep these in working memory for every chapter.

After applying changes, summarize them back to the user and wait for confirmation:

> **Applied:**
> - [list of changes]
>
> **Ready to start writing? Estimated time: [N] hours for a [target word count]-word manuscript with edit-as-you-go.**

Wait for explicit go-ahead.

---

## Phase 3 — Route Genre to Guardrail System

Look up the codex's genre in the routing table at `reference/genre_guardrails.md` and load the matching guardrail system into working memory.

Examples:
- `Paranormal Romance` → Supernatural Consequence System (§1)
- `Romcom` / `Romantic Comedy` → Comedy Architecture System (§3)
- `Dark Romance` → Darkness Calibration System + ECIS (§7)
- `Cozy Mystery` → Clue Disclosure System + cozy texture (§11)
- (anything unmapped) → Universal Fiction Guardrail (§18)

The active guardrail's five (or more) rules will be applied during every chapter draft and every Edit-As-You-Go pass.

---

## Phase 4 — Write the Manuscript (chapter by chapter, edit-as-you-go)

Create the output folder and the Edit Log file. Initialize the Edit Log with a metadata header that includes the model the customer chose in Phase 0:

```markdown
# [Book Title] — Edit Log

**Title:** [Book Title]
**Genre:** [Genre/Subgenre from codex]
**Word count target:** [from codex or user override]
**Chapter count:** [from outline]
**POV:** [from codex or user override]
**Heat level:** [detected or user override]
**Active guardrail:** [from genre routing]
**Style sample:** [yes/no, brief description if yes]
**Written with:** [Claude model the customer chose in Phase 0 — e.g. "Claude Opus 4.8"]
**Pipeline started:** [ISO timestamp]
**Plugin version:** [from plugin.json]

---

## Chapter-by-chapter notes

```

For each chapter in the parsed outline (in order):

### Step 4a — Draft the chapter

Open the chapter's outline data. Write prose that hits:

- The chapter goal
- The opening hook (use the codex's exact wording or a stronger variation)
- All numbered key scenes in order
- The relationship/subplot development beat
- The complication/conflict
- The character decision and its consequence
- The cliffhanger / closing line

Match the per-chapter word target (total target / chapter count). For a 50,000-word, 22-chapter book: ~2,275 words per chapter.

Write in the codex's specified POV mode and tense. If the user overrode these, use the override.

If the chapter has `intimate_beat_heat_gated: Yes` AND the codex/user heat level is open-door or higher, write the intimate scene fully on-page. ECIS applies — no fade-to-black on what the outline marked as on-page.

Apply the active guardrail's rules throughout.

### Step 4b — Edit-As-You-Go pass

Run the four-step Edit-As-You-Go loop from `reference/editorial_pipeline.md` (Loop 1):

1. AI-ism scan (per `reference/ai_ism_scrub.md`)
2. Genre guardrail sweep
3. Voice/style sweep (against the user's writing sample if provided)
4. Rhythm pass

Apply fixes inline. Don't move to the next chapter until this is done.

### Step 4c — Append to Edit Log

Log the chapter's word count (before/after edit), key fixes, voice notes, and any guardrail violations caught.

### Step 4d — Append the chapter to the working manuscript markdown

Save each finished chapter to a working `/tmp/working_draft.md` (or equivalent) with a `## Chapter N: Title` heading. This is what the integrity checks read.

### Step 4e — Every 3 chapters: integrity + outline-drift gate

After every third drafted chapter, run both check scripts over the recent 3-chapter window. See `reference/integrity_checks.md` for full details. Quick command form:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/codex-to-manuscript/scripts/integrity_check.py \
    --manuscript /tmp/working_draft.md \
    --mode general \
    --chapters-from $((CURRENT - 2)) --chapters-to $CURRENT \
    --output /tmp/integrity_recent.md

python3 ${CLAUDE_PLUGIN_ROOT}/skills/codex-to-manuscript/scripts/outline_drift_check.py \
    --manuscript /tmp/working_draft.md \
    --outline-json /tmp/parsed_outline.json \
    --chapters-from $((CURRENT - 2)) --chapters-to $CURRENT \
    --output /tmp/drift_recent.md
```

Read both reports. Action:

- **All PASS** → log to Edit Log, continue silently to next chapter.
- **Only WARN** → log to Edit Log, mention them in the next user-facing progress update, continue.
- **Any FAIL** → stop. Surface the relevant excerpt of the report to the user. Ask: revise the chapter(s), or accept the deviation as intentional? Do NOT silently proceed past a FAIL.

### Step 4f — Brief progress update to user

Every 5 chapters, post a short progress update to the user:

> "Drafted through Chapter 5. Word count so far: 11,800 / 50,000. Integrity check at Ch 3 and Ch 6 — both PASS. Edit Log up to date. Continuing."

Don't dump prose into the chat — the user will see it in the .docx at the end. The chat update is just for momentum visibility.

---

## Phase 5 — Pre-Editorial Integrity Gate → Editorial Pipeline → Final Integrity Gate

### Step 5a — Pre-editorial integrity gate (HARD gate)

Run the full-manuscript integrity check before any editorial pass:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/codex-to-manuscript/scripts/integrity_check.py \
    --manuscript /tmp/working_draft.md \
    --mode general \
    --output /tmp/integrity_full.md
```

If the codex specifies a mystery, romantic suspense, thriller, dark romance with reveal, or any genre with an antagonist-reveal beat, ALSO run mystery mode:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/codex-to-manuscript/scripts/integrity_check.py \
    --manuscript /tmp/working_draft.md \
    --mode mystery \
    --killer "[antagonist full name]" \
    --reveal-chapter [N from outline] \
    --suspects "[other named suspects from codex]" \
    --output /tmp/integrity_mystery.md
```

Identify the reveal chapter from the outline (the chapter where the antagonist's identity / motive / twist lands). The suspects list comes from the codex's character roster.

**This is a HARD gate.** Any FAIL must be addressed before continuing. Surface the report to the user, revise affected chapters, re-run until PASS or accepted-WARN.

### Step 5b — End-of-book editorial pipeline

After all chapters are drafted, run the six-pass end-of-book pipeline from `reference/editorial_pipeline.md` (Loop 2):

1. **Pass 1** — AI-ism Deep Scrub (exhaustive)
2. **Pass 2** — Developmental Edit (structural)
3. **Pass 3** — Beta Read (target-audience simulation)
4. **Pass 4** — Line Edit (sentence-level polish)
5. **Pass 5** — Proofread (final QA)
6. **Pass 6** — Holistic Manuscript Polish — whole-book revision for flow, AI-artifact removal, dialogue authenticity, voice consistency, and POV-locked immersion. Critical rule: preserves chapter length. Full spec in `reference/manuscript_polish.md`.

For each pass, apply changes inline and log a summary section to the Edit Log.

### Step 5c — Final integrity gate (HARD gate)

Re-run the full integrity check after the editorial pipeline finishes. Editorial passes occasionally introduce new future-leak phrases when paraphrasing. This is the last QA gate before delivery — must reach PASS.

---

## Phase 6 — Assemble Final Files

Use `reference/docx_template.md` patterns to:

1. **Build `[Book Title].docx`.** Title page, copyright placeholder, dedication placeholder, then all chapters with proper formatting (Georgia 12pt, 1.5 line spacing, 0.3" first-line indent, page breaks between chapters, scene-break dingbats, "The End" closer).

2. **Build `[Book Title] - KDP Info.docx`.** Title, subtitle, series, author placeholder, genre, three Amazon categories, seven keyword phrases, back cover blurb (150-200 words), Amazon long description (400-500 words), a 3-4 sentence cover prompt drawn from the codex's vibe keywords and setting, AND a "Production Notes" section at the bottom listing the Claude model used to write the manuscript (from the Phase 0 choice) and the plugin version. The customer can use this for series consistency — the same model should ideally write all books in a series.

3. **Save the Edit Log** as a plain markdown file alongside.

Place all three files in `/[customer folder]/[Book Title]/`.

---

## Final Delivery

Give the user `computer://` links to all three files:

> **Done. Your manuscript is ready.**
>
> [View manuscript](computer:///path/to/[Book Title].docx)
> [View KDP info](computer:///path/to/[Book Title] - KDP Info.docx)
> [View edit log](computer:///path/to/[Book Title] - Edit Log.md)

Keep the wrap-up brief — the user can read the files themselves.

---

## Reference Files

All in `${CLAUDE_PLUGIN_ROOT}/skills/codex-to-manuscript/reference/`:

| File | Contents | When to Read |
|---|---|---|
| `genre_guardrails.md` | Genre-to-guardrail routing table + each guardrail's full rules | After parsing, before writing chapter 1; re-consult during every Edit-As-You-Go pass |
| `editorial_pipeline.md` | Edit-As-You-Go loop + End-of-Book pipeline | Before any editorial pass |
| `integrity_checks.md` | Full reference for the integrity + outline-drift checks (when to run, how to interpret reports, hard vs soft gates) | Before the first integrity gate (Phase 4 step 4e) and at every gate thereafter |
| `ai_ism_scrub.md` | Banned phrases, AI tells, replacement methodology | During every Edit-As-You-Go pass and end-of-book Pass 1 |
| `parsing_rules.md` | Codex/outline structure reference, fallback strategies for malformed files | Only if parser misses fields |
| `user_revisions.md` | How to apply name/place/POV/tense/heat/length/style changes | During Phase 2 |
| `docx_template.md` | python-docx patterns for the final manuscript and KDP doc | During Phase 6 |
| `manuscript_polish.md` | Full spec for the holistic Pass 6 polish — structure/pacing/flow, AI-artifact removal, dialogue/voice, narrative authenticity, deliverables checklist | Before running Pass 6; also when the standalone /polish-manuscript command is invoked |

## Scripts

All in `${CLAUDE_PLUGIN_ROOT}/skills/codex-to-manuscript/scripts/`:

| Script | Purpose |
|---|---|
| `parse_codex.py` | Parse a codex file (.pdf/.docx/.md/.txt) into structured JSON |
| `parse_outline.py` | Parse an outline file into structured JSON with per-chapter beats |
| `integrity_check.py` | Structural integrity scan — narrator future-leak, telegraphed observation, plus mystery-mode antagonist density / clearing speed |
| `outline_drift_check.py` | Compare drafted chapters to the parsed outline, flag drift in title / POV / opening / ending / key scenes / intimate beats |

Parser scripts accept `--in <path>` and optionally `--out <path>`. Check scripts accept `--manuscript <path>` and various optional filters — see `reference/integrity_checks.md` for full invocation.

## Core Guardrails (Summary)

The skill has six hard rules across every phase:

1. **Faithfulness to the codex.** The manuscript hits every mandatory, every locked trope, every key character beat. The codex is the contract.
2. **Faithfulness to the outline.** Every chapter's POV, hook, key scenes, conflict, decision, and cliffhanger are honored. Enforced by `outline_drift_check.py` every 3 chapters.
3. **Genre guardrail enforcement.** The routed guardrail system runs per chapter. Failure modes for that genre are caught before they calcify.
4. **No AI-isms in the final draft.** The end-of-book Pass 1 is exhaustive. Any banned-phrase hit is rewritten, not just deleted.
5. **No future-leak narration.** The narrator never knows what's coming. Caught by `integrity_check.py` at every 3-chapter gate AND at the pre-editorial / post-editorial gates.
6. **No premature reveals (mystery / thriller / dark romance / romantic suspense).** Antagonist-name density is monitored against red-herring suspect mentions in pre-reveal chapters. Mystery-mode integrity check runs as a hard gate before delivery.

## When the Pipeline Takes Too Long

A 50-80k-word manuscript with full edit-as-you-go takes many hours. If the customer wants a faster turnaround, offer:

- **Draft-only mode** — skip the Edit-As-You-Go per-chapter pass; run only the end-of-book pipeline. Faster, but voice drift across the manuscript is more likely.
- **No editorial mode** — produce the first draft and stop. Customer runs Manuscript Editor Pro separately. Fastest, lowest QA.

Default is the full pipeline as described above.

## What This Skill Does NOT Do

- It does not generate codex or outline content. Customers must provide both. Direct customers without a package to the matching outline/codex skills.
- It does not produce a print-formatted PDF. The output `.docx` is editable; customers handle final print formatting in their preferred tool (Atticus, Vellum, Word).
- It does not upload to KDP. The KDP Info doc gives the customer everything they need to publish manually.
- It does not generate cover art. The KDP Info doc includes a cover prompt the customer can feed to Ideogram, Midjourney, or their cover designer.
