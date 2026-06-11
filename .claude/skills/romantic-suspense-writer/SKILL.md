---
name: romantic-suspense-writer
description: >
  Turn a romantic suspense outline into a complete, publish-ready manuscript. The romance arc and
  the suspense arc are co-equal A-plots that must escalate together and resolve together — this
  skill enforces both the HEA contract AND strict tension architecture simultaneously. Accepts any
  romantic suspense outline. Supports sweet/clean through steamy heat levels. Full editorial
  pipeline with dual-track audit. MANDATORY TRIGGERS: "write my romantic suspense", "romantic
  suspense writer", "write from outline", "turn outline into manuscript", "write this romantic
  suspense", "manuscript from outline", "write the book", "write my rom-sus", or any mention of
  turning a romantic suspense outline into a full manuscript. Use this skill when the user has a
  romantic suspense outline and wants it written into prose.
---

# Romantic Suspense Writer

Turn a romantic suspense outline into a complete, polished manuscript. This skill takes the outline and — using the user's own voice from their writing sample — produces a publish-ready .docx with a full dual-track editorial pipeline.

## What This Skill Produces

| File | Description |
|------|-------------|
| `[Title].docx` | Complete manuscript — all chapters as fully written prose |
| `[Title] - KDP Info.docx` | Amazon metadata, keywords, categories, cover prompt |
| `[Title] - Style Guide.md` | Reusable voice guide built from the user's writing sample |

---

## The Core Principle: Dual A-Plot Mandate

Romantic suspense is not romance with danger sprinkled in, nor thriller with a love interest added. It is a genre with **two co-equal A-plots** that are structurally inseparable:

- **The Romance Arc**: two people falling in love against impossible odds
- **The Suspense Arc**: an external threat or mystery that escalates throughout

These tracks don't run in parallel — they are **braided**. The danger accelerates the intimacy (forced proximity, shared vulnerability, needing to trust someone you've just met with your life). The intimacy creates new vulnerability to the danger (the person they love becomes a target, or becomes a suspect). When one track escalates, the other must respond.

**The test for every chapter:** Does this chapter advance BOTH tracks? A pure action chapter with no romantic development is a thriller chapter. A pure romance chapter with no threat presence is a romance chapter. A romantic suspense chapter keeps both moving — even if one track is subtle.

### The Thematic Spine

Romantic suspense almost always runs on **trust as its central theme** — because the very act of trusting the love interest is as dangerous as trusting them with your life. The protagonist's romantic and external arcs share the same psychological engine: they have to learn to trust someone (and that learning is dangerous). Design every chapter with this in mind.

### The Black Moment Must Break Both Tracks

The black moment in romantic suspense cannot only shatter the romance OR only escalate the external danger — it must do both simultaneously. The revelation that drives the couple apart should be connected to the threat. The worst moment for the relationship should coincide with maximum danger.

---

## The Tension Architecture System (Suspense Track)

AI has predictable failure modes in suspense. Read `references/dual-track-architecture.md` for the complete system. Core rules:

### Rule 1: Information Is Currency
Every chapter has an information budget. What does the reader learn? What stays hidden? What do they believe that's false? The outline's information release schedule is LAW — no early reveals, no skipped plant points, no extra clues the AI invents.

### Rule 2: Tension Never Flatlines
Every chapter either escalates the threat, provides a seeded relief valve (which plants a seed for the next escalation), or delivers a revelation. There are no neutral chapters. Even intimate scenes must have an undercurrent of danger.

### Rule 3: The Protagonist Earns Every Inch
Wrong conclusions before right ones. Dead ends before breakthroughs. The protagonist does not figure things out at AI speed. Chapters of wrong theory, wasted time, and mounting frustration are not filler — they are tension.

### Rule 4: Twists Must Be Reverse-Engineerable
Every twist needs at least 3 planted clues visible on re-read. The reader should say "I should have seen that" — never "where did that come from?"

### Rule 5: The Threat Has Equal Screen Time
The external threat (antagonist, mystery, danger) must be felt in every chapter. It should feel like it's winning until the final act.

### Rule 6: Every Relief Valve Plants a Seed
The couple's tender moments, the quiet scenes, the breathers — all must drop information or set up something that pays off in 3-5 chapters. No true filler.

---

## The Romance Architecture System (Romance Track)

### The HEA Contract (Non-Negotiable)
Romantic suspense readers expect a Happily Ever After (or at minimum Happily For Now). The resolution of the external threat is NOT the end of the book — the HEA is. The final chapters after the climax exist to deliver the emotional payoff of the romance. Never end at the resolution of the suspense arc.

### The Romance Arc Beats
Each of these must happen on-page:
1. **Meet / Re-Meet**: The two leads come together under the pressure of danger — establish chemistry AND the obstacle (external + internal)
2. **Alliance**: They're forced to work together despite reasons not to trust each other. The danger is the excuse; the chemistry is the real reason they stay.
3. **First Real Connection**: A quiet moment between action beats where they see each other clearly. Often happens at maximum external danger — forced vulnerability.
4. **Deepening Stakes**: The love interest becomes personally connected to the danger (either as a potential target, a suspect, or someone the protagonist is now desperate to protect)
5. **The Almost**: A moment of almost-intimacy interrupted by danger, duty, or the protagonist's own fear. The near-miss should be more charged than the actual kiss would have been.
6. **The Trust Break / Misunderstanding**: Something from the suspense arc appears to confirm the protagonist's worst fear about the love interest. This must feel earned from the evidence available — not contrived.
7. **Black Moment**: Both tracks shatter simultaneously. The external danger peaks AND the romantic relationship breaks. Maximum isolation.
8. **The Turn**: The protagonist acts on love first, then uses that courage to resolve the external threat (or the reverse, but both must connect)
9. **HEA**: After the danger is resolved, the emotional payoff. The declaration. The future. Never rush this — readers came for this moment.

### Sweet/Clean Standards
This manuscript is **sweet/clean**: the romantic tension is real and often intense, but intimate scenes are closed-door.

**Sweet/clean does NOT mean emotionally flat.** The heat in clean romantic suspense comes from:
- **Proximity under pressure** — forced closeness in dangerous situations creates charged awareness
- **Physical awareness, non-explicit** — heartbeat, warmth, breath, the specific weight of a hand
- **Near-misses** — interrupted moments are often more charged than consummation
- **Earned vulnerability** — fear and danger strip defenses and reveal what people actually feel
- **Unspoken tension** — what characters don't say, don't do, almost do

Write the romantic tension at its highest possible level within clean standards. The danger is the engine — the reader should feel the heat even when nothing explicit happens.

---

## Interactive Setup — Ask Before Writing

Use AskUserQuestion for each question ONE AT A TIME.

1. **Outline intake** — Upload the outline (required). Parse all sections: character bios, chapter-by-chapter structure, suspense arc, romance arc beats. Summarize and confirm before writing.
2. **Series position** — Standalone, Book 1, Book 2+, or interconnected standalone? If interconnected standalone, ask for any world bible or notes on recurring characters.
3. **POV structure** — Single first-person, single third-person close, dual POV (both leads), or other?
4. **Ticking clock** — Is there a deadline/countdown driving the external threat? Literal clock, escalating pattern, soft deadline, or no clock?
5. **Twist complexity** — One major reveal, two-layer, or straightforward (suspense through escalation, not revelation)?
6. **Style guide** — Upload a writing sample to match your voice? (Strongly recommended)
7. **Length confirmation** — Confirm chapter count and approximate word count from the outline.

---

## Interconnected Standalone Framework

Since these books share a world and secondary characters (but each has a new central couple), maintain consistency across books:

- When the user uploads a previous book or world bible, extract and record: recurring character names and roles, location names and descriptions, established world facts, any unresolved threads, and tone/atmosphere of the series
- Secondary characters who appear in this book and star in future books must be written with an arc of their own — enough personality to make readers want their story, without stealing focus from the main couple
- **Callbacks and Easter eggs**: brief, organic references to events from previous books (for series readers) without requiring them to understand the reference (new readers must not be confused)
- Save a `[Series Name] - World Bible.md` if one doesn't already exist, updating it with new facts from this book

---

## Style Guide System

Read the user's uploaded writing sample and extract:

- **Voice & Tone**: Sentence rhythm, narrative distance, how conversational or literary, interiority depth
- **Tension Style**: How dread is built — through implication, detail, pace, or dialogue
- **Dialogue Patterns**: How characters speak, banter style, how secrets and lies sound vs. truth
- **Pacing Style**: Chapter length preferences, scene breaks, how action vs. quiet scenes are balanced
- **Romantic Tension Style**: How attraction is conveyed — internal monologue, physical awareness, dialogue
- **Clean Sensuality Approach**: How near-misses are written, how physical proximity is described without being explicit
- **Description Style**: Sensory density, setting approach, how the environment creates mood

Save as `[Title] - Style Guide.md`.

If no sample is provided: ask for 2-3 author comparisons and build a lighter style guide from those preferences.

---

## Workflow

Read `references/workflow-steps.md` for the full step-by-step pipeline.

---

## Prose Craft

Read `references/prose-craft.md` for romantic suspense-specific writing rules: how to write danger that accelerates intimacy, how to create charged clean tension, how to balance action and emotion in the same scene.

---

## Editorial Pipeline

After writing all chapters:

1. **AI-Ism Revision** — Remove robotic phrasing, POV breaks, connector words, emotional over-labeling
2. **Dual-Track Audit** — Verify both the romance arc AND the suspense arc are present and escalating in every chapter; check information control, tension levels, and romance beat delivery
3. **Developmental Edit** — Structural assessment of pacing, character arcs, genre compliance, HEA delivery
4. **Beta Read** — Critical reader review from a romantic suspense reader's perspective
5. **Targeted Revision** — Apply top fixes from all three assessments

Read `references/revision-guide.md` for the complete editorial checklist.

---

## Julie Fontaine Hard Rules (Absolute — No Exceptions)

Read `references/julie-fontaine-voice.md` for the full voice guide. The non-negotiable rules for every manuscript:

- **No profanity** — not even substitute swearing like "freaking." Strong emotion through action, dialogue, subtext.
- **Clean romance, strictly** — physical affection stops at kissing. No fade-to-black suggesting bedroom scenes. No morning-after scenes. No implied intimacy beyond kissing.
- **Christian/Catholic faith woven naturally** — characters pray, reference saints or Scripture, draw on faith as texture of life. Never preachy, never absent. Julie Fontaine's faith presence is slightly higher than other pen names.
- **No em dashes** — use commas, periods, ellipses, or restructure the sentence.
- **Short chapters** — 1,800–2,500 words. Patterson style. One scene or emotional beat per chapter.
- **No head-hopping** — POV locked per chapter, established in the first paragraph.
- **Paragraphs no longer than five lines** — white space is a pacing tool.
- **Action beats over dialogue tags** — no exotic tags (exclaimed, hissed, breathed), no adverbs on tags.
- **Violence: psychological and relational** — threatening phone calls, lies unraveling, secrets. If physical danger occurs: brief, non-graphic, focus on emotional aftermath.

## The Julie Fontaine Women's Fiction Spine

For Julie Fontaine's romantic suspense specifically, the story's structural engine is the **protagonist's inner transformation** — identity, self-worth, healing, learning to trust again. The romance serves this arc. The suspense pressurizes it. Every external event pushes the protagonist toward or away from the internal truth she needs to face.

This means the romantic suspense writer skill, when used for Julie Fontaine, is writing at the intersection of women's fiction and romantic suspense: Debbie Macomber's warmth, Katherine Center's emotional precision, and JoJo Moyes's courage to let things hurt.

## Names & Places Avoidance

No generic romance names (Ryan, Chase, Liam, Emma, Sophia). No generic thriller names (Sarah, Jack, Kate, Tom). No estate or manor names with dark/gothic modifiers (Blackwood, Ravenwood, Thornfield). No titles using Hidden, Dark, Silent, Deadly, Secret, Last, Gone, Dangerous, Deadly, Perfect.

Names should feel grounded and demographically specific to the characters' backgrounds and settings. The more real the names, the more real the threat feels.

## Number & Time Diversity

Avoid overusing 7 in all content — addresses, timestamps, ages, case numbers. Distribute across all digits.
