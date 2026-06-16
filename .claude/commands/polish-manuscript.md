---
name: polish-manuscript
description: Run a holistic whole-manuscript polish pass — fixes structure, pacing, flow, AI artifacts, dialogue, voice, and immersion across the entire book without shortening chapters
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Agent, TodoWrite
---

# /polish-manuscript

Run a holistic whole-manuscript revision pass on any existing draft. This is the same Pass 6 — Holistic Manuscript Polish — that runs at the end of the main `/write-from-codex` pipeline, exposed as a standalone command for customers who already have a finished draft and want only the polish.

## What it does

Five workstreams applied across the entire manuscript:

1. **Structure, pacing, and flow** — strips artificial chapter endings (philosophical wrap-ups, forced cliffhangers, manufactured mic-drops, end-of-chapter moralizing), replaces with mid-scene cuts and forward momentum, improves transitions so the book reads as one cohesive arc.

2. **AI artifact removal** — eliminates direct AI references, leftover prompt language ("Write a scene where…"), meta-commentary, POV breaks, generic transitional phrases ("Additionally," "Furthermore," "It's worth noting"), clinical emotion descriptions, artificial precision, and AI-style emotional labeling.

3. **Dialogue and character voice** — replaces stiff dialogue with authentic speech, reduces surname overuse where first names fit, breaks repetitive call-and-response patterns, adds interruptions and conversational messiness, ensures each character maintains a distinct consistent voice across the whole manuscript.

4. **Narrative authenticity and immersion** — replaces forced metaphors and overwriting, simplifies inflated sentence structures, removes author-as-character observations, cuts filler connectors, locks all sense-detail to the active POV character's awareness and limitations.

5. **Verification** — confirms word count is at or above target, no chapter ends on cliché, no AI artifacts remain, voices are distinct, POV is locked. Appends 3-5 before/after examples to the Edit Log.

## Critical rule

**This pass preserves chapter length and narrative weight.** Scenes are never shortened, compressed, or summarized. If a scene feels slow, the cause is fixed (over-explaining, redundant beats, inflated sentences) — but the scene itself stays.

## Inputs

Ask the user for:

1. **Manuscript file path** — `.docx` or `.md`
2. **Edit Log file path** (optional) — if the customer wants the polish notes appended to an existing Edit Log; otherwise create a new one

## Pipeline

Invoke the `codex-to-manuscript` skill and follow `reference/manuscript_polish.md` end-to-end. Apply all five workstreams across the full manuscript. Log major changes (especially structural, pacing, and dialogue revisions) to the Edit Log with 3-5 before/after examples.

## Output

- Fully revised manuscript (in-place edit of the original, or a new file labeled `[Original Title] - Polished.docx`)
- Edit Log section titled "Holistic Polish Pass" listing the major changes made
- Confirmation checklist verifying:
  - Manuscript word count is at or above target
  - No chapter ends on cliché or manufactured drama
  - No direct AI references remain
  - All transitional AI-isms removed
  - All clinical emotion labels rewritten
  - Dialogue feels spoken
  - Voices are distinct and consistent
  - All sense-detail is POV-locked
  - No omniscient intrusions

## When to use this command

- The customer has a finished manuscript (drafted by them, by another tool, or by an earlier version of this plugin) and wants only the polish pass
- After a major revision where the customer added or rewrote chapters and wants to verify whole-book consistency
- Before sending a manuscript to KDP if the customer is unsure whether AI artifacts or pacing issues remain

## When NOT to use this command

- The manuscript hasn't been drafted yet — use `/write-from-codex` instead
- The customer wants structural changes (different POV, different ending, added chapters) — those need a developmental edit, not a polish
- The customer wants the manuscript shortened — this pass preserves length by design

## Standalone vs. integrated

This pass also runs automatically as Pass 6 of the main `/write-from-codex` pipeline. Customers who run the full pipeline don't need to run `/polish-manuscript` separately — it's already included. The standalone command is for customers using the polish on its own.
