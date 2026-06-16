# User Revisions Phase — How to Apply Changes Before Writing

After parsing the codex and outline, the skill presents a structured summary to the user and asks what (if anything) they want to change. The user can request edits in four categories:

1. **Names & gender** (rename a character, swap pronouns or gender)
2. **Places & setting** (rename a location, relocate the story, change time period)
3. **POV / tense / heat** (override the codex's POV mode, tense, or heat level)
4. **Length & style sample** (override word count target, supply a writing sample for voice matching)

If the user says "no changes," skip directly to writing. Otherwise, apply the changes consistently across the parsed codex AND the parsed outline before any chapter is written.

---

## Pattern 1: Character renames

The most common request. The user says: "change Bridget to Sarah" or "make Alistair a woman named Alistra."

### Apply to codex

In the parsed codex JSON, update:
- `characters[].full_name` — the primary entry
- Any `characters[].key_relationships` mentions
- Any character name appearing in `concept.story_summary`, `concept.pitch`, or `subplots[].subplot_summary`

### Apply to outline

For every chapter in `chapters_flat`:
- Update `pov` if the renamed character is a POV character
- Update `key_scenes[].text` for any name occurrence
- Update `opening_hook`, `cliffhanger`, `chapter_goal`, `romantic_relationship_development`, `complication_or_conflict`, `character_decision_and_consequence`, etc.

### Apply during writing

Hold the rename in working memory. When drafting any chapter, never use the original name. If the codex specified a placeholder like `[Heroine]` or `[Hero]`, replace with the chosen name.

### Gender swaps

When the user changes a character's gender:
- Update pronouns throughout codex and outline
- Reconsider any gendered descriptors (e.g., "her flannel shirts" stays — clothing isn't gendered; "the woman in the circle" → "the man in the circle")
- For a pairing config change (MF → MM, MF → FF), check that the genre still maps to the same guardrail (e.g., dark MF romance → dark MM romance routes to the **Tension Architecture System + ECIS** instead of the standard Darkness Calibration variant)

---

## Pattern 2: Place / setting renames

User says: "rename Kennet's Crossing to Owl Hollow" or "move the story from a bog to a desert canyon."

### Simple rename

Update every occurrence of the old name in the codex and outline. Be careful with similar-sounding words and partial matches.

### Setting relocation

This is bigger. If the user moves the story from a Pacific Northwest bog to a Sonoran desert:

1. The genre's environmental references will need to shift. Bogs / mist / damp / moss → desert / heat / dust / scrub.
2. Update `setting.primary_setting` and `setting.vibe_keywords` in the codex.
3. Update sensory descriptions in chapter outlines that anchor to the original setting.
4. Note that flora/fauna/weather will need adjustment during writing — make a list of the original setting's recurring sensory cues and translate each to the new setting.

If the relocation is sweeping enough that it would change the genre or core conflict, flag this and confirm with the user before proceeding.

### Time period changes

If the user changes from contemporary to historical (or vice versa):

1. Update `setting` accordingly.
2. Tech presence/absence shifts — Alistair's laptop becomes a typewriter / reporter's notebook / clay tablet / etc.
3. Communication patterns shift (texts → letters → telegrams).
4. Dialog register shifts but keep it accessible — don't go full period-pastiche unless the user asks.

---

## Pattern 3: POV / tense / heat overrides

### POV change

| User asks | What to do |
|---|---|
| "Make it first person" | Change `structure.pov_mode` and rewrite every chapter outline POV indicator and every chapter's prose to first person from the named POV character |
| "Drop the alternating POVs — just stay on the heroine" | Update `structure.alternating_povs` to "No". For chapters originally in the other character's POV, rewrite from outside the now-single POV — usually staying with the lead and showing the other character through their perception |
| "Switch from past to present tense" | Change `structure.tense` and apply consistently |

### Heat level change

| User asks | What to do |
|---|---|
| "Make it closed-door" | Override codex heat level. Every `intimate_beat_heat_gated` field that was Yes gets converted to fade-to-black. Apply Chemistry Architecture System rules (§9 in `genre_guardrails.md`). |
| "Bump from steamy to scorching" | Apply ECIS rules. Lengthen and increase specificity of intimate scenes the codex marked Yes. |
| "Add an open-door scene at chapter 14" | Add `intimate_beat_heat_gated: Yes` to chapter 14 in working state, even if the codex/outline said No. Write the scene fully. |

---

## Pattern 4: Length & style overrides

### Length override

If the user changes the word count target (e.g., 50-60k → 30k novella):

1. Recalculate per-chapter word count target. For a 22-chapter outline at 30k total, target ~1,360 words/chapter.
2. Decide whether to keep all 22 chapters at shorter length, or condense to fewer chapters. Default: keep the chapter count, shorten each chapter — preserves the outline's structure.
3. Adjust scene density. Each chapter still needs to hit the same beats; shorter just means tighter prose, less digression, fewer subplots in the moment-to-moment.

### Style sample

If the user uploads a writing sample (`.docx`, `.pdf`, or pasted text):

1. Read the sample (prefer 2,000+ words for a stable signal).
2. Identify the sample's voice fingerprints:
   - **Sentence rhythm** — average length, fragment frequency, run-on tolerance
   - **Adjective density** — sparse, moderate, lush
   - **Metaphor register** — domestic, natural, abstract, technical, etc.
   - **Dialogue tag style** — terse "said" vs. variant tags vs. mostly action beats
   - **Internal monologue depth** — close third with deep interiority vs. distant
   - **Vocabulary register** — accessible, literary, vernacular, mixed
3. Save these fingerprints to working memory and reference them during every chapter draft AND every Edit-As-You-Go pass.

If the user does not provide a sample, use a default voice register implied by the codex's tone and genre. The codex's `concept.pitch` and `concept.story_summary` already give strong tonal cues.

---

## Confirmation step

After applying all user changes, present a short summary back to the user:

> "I've applied:
> - Bridget → Sarah throughout
> - Kennet's Crossing → Owl Hollow throughout
> - First person past tense, single POV (Sarah)
> - Heat level override: scorching (was open-door)
> - Style sample: matched to the 4,200-word excerpt you provided
>
> Ready to start writing? This will take several hours — I'll deliver chapter by chapter."

Wait for the user's go-ahead before drafting chapter 1.
