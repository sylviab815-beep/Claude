# Pulp Adventure Romance Author: 6-Phase Workflow

## Phase 1: Get the Outline

1. Ask the user to share or paste their completed outline from the Pulp Adventure Romance Outline Builder.
2. Verify completeness:
   - All chapters listed with scene-level breakdown
   - Causal Crossover Tag present for every chapter
   - McGuffin Gravity state named for every chapter
   - ARIS structural map present (Act I / II-A / II-B / III / Coda)
   - Heat level, era, length tier, configuration named in outline metadata
3. If incomplete, route the user back to the Outline Builder. Do not proceed.
4. If complete, confirm word count target and move to Phase 2.

## Phase 2: Interactive Setup

Ask the following eight questions one at a time. Document every answer.

1. **Target LLM** — Which model will write this manuscript? Options: Claude Opus 4.x, Claude Sonnet 4.x, Claude Haiku 4.x, GPT-4 / GPT-4 Turbo, Gemini 1.5/2.x, Other. (Sets calibration per `llm-selection.md`.)

2. **Confirm Era** — Classic Pulp (1920s–40s) / Mid-Century / Contemporary / Retro-Futurist? (Should match outline; reconfirm to lock voice.)

3. **Confirm Heat Level** — Sweet (closed door) / Steamy / Spicy (explicit)?

4. **POV** — Single POV / Dual POV alternating / Dual POV with one dominant? Which protagonist is primary if single?

5. **Tense** — Past tense / Present tense?

6. **Tone Calibration** — Earnest pulp / Wry banter / Gritty contemporary / Lush romantic / Comedic? (Calibrates prose rhythm.)

7. **Style Sample** — Does the user want to upload a writing sample to match their voice? If yes, accept up to two samples (full manuscript or 5,000+ word excerpt). Build a style overlay from the sample.

8. **Author Name** — As it should appear on the title page and KDP metadata.

WAIT for all answers before Phase 3.

## Phase 3: Pre-Writing Setup

1. **Names Cross-Check** — If the user has a Names Avoidance List, cross-reference all character names. Replace any matches and document the replacements. (If no list provided, skip.)

2. **Output Folder** — Confirm with the user where the final .docx files should be saved. Default to a new dated subfolder within the user's chosen location.

3. **Style Overlay** — If the user uploaded a sample, generate a one-page style profile (cadence, sentence-length distribution, dialogue rhythm, signature word choices, voice register). Store and apply throughout drafting.

4. **Confirm ARIS** is loaded. Confirm prose-craft.md rules are in context. Confirm llm-selection.md calibration matches the chosen LLM.

5. **Build the chapter execution queue** — list every chapter from the outline with its target word count, ARIS tags, and pulp beat type. This queue drives Phase 4.

6. **Present the setup summary to the user**, restating the chosen Execution Mode (Phase 0), and wait for their go-ahead before writing begins.

## Phase 4: Manuscript Writing

For each chapter in the queue:

1. **Re-read the outline entry** for the chapter — verify every ARIS tag and beat is in front of you.

2. **Draft the chapter** to the target word count for the length tier:
   - Novella: 1,500–2,500 words/chapter
   - Standard: 2,500–4,000 words/chapter
   - Extended: 3,500–5,000 words/chapter

3. **Apply prose-craft.md Rules 1–6** during drafting:
   - Pulp Sentence Rhythm
   - Sensory Specificity in Locale
   - Banter Under Threat
   - Set-Piece Scene Architecture
   - Romantic Vulnerability Calibration
   - Heat-Level Compliance

4. **Run ARIS Per-Chapter Checklist** immediately after drafting:
   - Causal Crossover Tag stated
   - McGuffin Gravity state named (and is at least "shadow" — never zero)
   - If intimacy beat: Vulnerability Under Threat verified (active threat present)
   - Banter-Action Equivalence: both protagonists verbally alive in any pressure scene
   - Dual-Currency Escalation: both physical and emotional stakes higher than chapter open

5. **If any rule fails**, apply the targeted intervention and re-check before moving to the next chapter.

6. **Log the chapter** in the ARIS per-chapter tracking format.

7. Move to the next chapter.

**Completeness Requirement:**
- Every scene in the outline is written
- No placeholder text remains
- Final word count within ±5% of target
- ARIS log shows pass status for every chapter

For longer manuscripts, batch chapters into chunks calibrated to the chosen LLM (see llm-selection.md). Do not exceed the model's effective context window for the chunk. Pause for the user's review between chunks only in Supervised mode; in Autonomous mode, continue without pausing.

## Phase 5: Editorial Pipeline

After the full draft is complete, execute the 5-stage editorial pipeline from `revision-guide.md`:

1. **AI-ism Revision** — Strip universal AI crutches and pulp-adventure-specific clichés
2. **ARIS Audit** — Re-apply the six rules across all chapters; verify manuscript-level audit points
3. **Developmental Edit** — Structure, pacing, character arcs, set-piece quality, McGuffin integrity
4. **Beta Read Calibration** — Pulp adventure romance reader expectations
5. **Targeted Revision** — Top three structural fixes from the beta pass

Log all changes per stage.

## Phase 6: KDP Metadata and Delivery

1. **Generate KDP metadata** per `kdp-template.md`:
   - Title, subtitle, author name
   - 4000-character description
   - 7 action-adventure-romance keywords
   - 3 BISAC categories
   - Price point appropriate to length tier
   - Series info if applicable
   - 3 comp titles
   - Audience profile
   - Cover prompt with era-appropriate visual cues

2. **Generate the manuscript .docx** per `docx-template.md`.

3. **Generate the ARIS chapter log .docx** as a third deliverable for the user's records.

4. **Save all files** to the confirmed output folder.

5. **Provide the user** with file locations and a brief summary:
   - Final word count
   - Number of chapters
   - ARIS interventions applied
   - Top notes from editorial passes
