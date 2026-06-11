---
name: cozy-mystery-author
description: >
  Interactive cozy mystery manuscript writer. Asks upfront choices (paranormal or traditional, romance
  subplot, series length, heat level) then writes complete ~20,000-word novellas as .docx files with
  KDP metadata. Supports uploading previous work to build a style guide. Strict outline-adherence
  system prevents the AI from jumping ahead or revealing the killer too early. Full editorial pipeline:
  AI-ism revision, developmental edit, beta read, and targeted revision. MANDATORY TRIGGERS: "cozy
  mystery author", "write a cozy mystery", "cozy mystery manuscript", "cozy mystery book", "write my
  cozy", "cozy mystery plugin", "generate cozy mystery", or any mention of writing/generating a cozy
  mystery manuscript or book. Use this skill even if the user just says "write my cozy" or "cozy
  manuscript."
---

# Cozy Mystery Author

An interactive cozy mystery manuscript writer that asks what you want upfront, then writes a complete publish-ready novella with strict mystery-craft guardrails.

Unlike batch writers that just go, this skill starts by asking YOU what kind of cozy mystery you want to write — then builds and writes the entire book based on your choices.

## What This Skill Produces

One folder per book containing:

```
[Book Title]/
├── [Book Title].docx                    # ~20k word complete manuscript
├── [Book Title] - KDP Info.docx         # Amazon metadata + cover prompt
└── [Book Title] - Style Guide.md        # (if style guide was built from uploads)
```

## Interactive Setup — Ask Before Writing

This skill does NOT auto-generate. It asks the user questions using AskUserQuestion (popup-style multiple choice) before writing anything. Ask each question ONE AT A TIME and wait for the answer.

### Question Flow

Read `references/workflow-steps.md` for the complete question flow and writing pipeline. The setup phase asks about:

1. **Paranormal or Traditional** — magical elements, familiars, and supernatural worldbuilding, or a grounded real-world cozy?
2. **Romance Subplot** — slow-burn romance thread, or mystery-only?
3. **Heat Level** — sweet/clean (closed door) or mild spice (open door but tasteful)?
4. **Length** — novella (~20k words / 16 chapters) or full novel (~50k words / 30 chapters)?
5. **Series Position** — standalone, or part of a series? If series, which book number?
6. **Style Guide Upload** — would you like to upload 1-2 previous manuscripts so the AI can match your voice, pacing, and style?
7. **Outline Upload** — do you have a completed outline (from the Cozy Mystery Outline Builder or elsewhere) to write from, or should we generate one?

After all choices are made, the skill builds the book.

## Style Guide System

If the user uploads previous manuscripts, read them carefully and extract a style guide BEFORE writing anything. The style guide captures:

- **Voice & Tone**: How the author's narrator sounds — formal vs casual, level of humor, internal monologue style, sentence rhythm
- **Dialogue Patterns**: How characters talk — contractions, dialect, banter style, dialogue tag preferences (said vs action beats)
- **Pacing Style**: Short punchy chapters vs longer immersive ones, scene transition style, how much interiority vs action
- **Description Style**: Sparse and functional vs rich and atmospheric, how sensory details are used
- **Mystery Craft**: How clues are planted — subtle vs obvious, through dialogue vs observation vs action
- **Comfort Elements**: How food/drink/cozy scenes are used — frequency, detail level, integration with plot
- **POV Handling**: Tense, person, depth of interiority, how much the narrator addresses the reader
- **Chapter Structure**: How chapters open and close, typical chapter length, scene break patterns

Save the style guide as `[Book Title] - Style Guide.md` in the output folder. Reference it throughout writing — every chapter should be checked against the style guide for voice consistency.

## The Outline-Adherence System (CRITICAL)

This is the most important section of this skill. Cozy mysteries live or die on their reveal timing. The AI has a strong tendency to:

- Foreshadow the killer too obviously through word choice or narrative focus
- Have the sleuth "notice" things about the killer before the outline says she should
- Rush to the reveal because it "knows" the answer
- Drop hints that are too heavy-handed because it's working backward from the solution
- Give the killer more page time or more suspicious descriptions than other suspects
- Have characters react to the killer differently than to other suspects without narrative justification

Read `references/outline-adherence.md` for the complete anti-spoiler system. The core rules:

### Rule 1: Chapter-Locked Writing
Each chapter is written ONLY from the information available at that point in the outline. Before writing Chapter 6, the AI must ask: "What does the sleuth know at this point? What has been revealed? What is still hidden?" and write ONLY from that knowledge state.

### Rule 2: Equal Suspect Treatment
The killer receives NO more narrative attention, suspicious description, or "feeling off" reactions than any other suspect — until the outline specifically calls for suspicion to shift. Every suspect gets equal page time, equal "could they have done it?" energy.

### Rule 3: No Backward Writing
The AI must not write scenes that only make sense if you already know the ending. No "little did she know" energy. No descriptions of the killer that read differently on a second pass. The prose should be honest to the sleuth's current understanding.

### Rule 4: Clue Planting by the Outline's Schedule
Clues appear EXACTLY when the outline says they appear — not earlier, not later. If the outline says Clue #3 is discovered in Chapter 8, it does not appear in Chapter 5 as a "subtle hint." The outline is the law.

### Rule 5: Red Herrings Get Real Investment
Red herrings must be written with the same narrative weight and conviction as real clues. The AI must write each red herring as if it IS the real answer — the reader should genuinely believe the false trail. Lazy red herrings that are obviously wrong defeat the entire mystery.

### Rule 6: The Reveal Earns Its Moment
The reveal scene must connect dots the reader already has. No new information in the reveal chapter. The sleuth's "aha" moment comes from rearranging known facts — not from discovering a secret document or overhearing a confession that wasn't set up.

## Core Specifications

These are defaults — the interactive setup may change them based on user choices:

- **POV**: First person, present tense (can be adjusted via style guide)
- **Structure**: Single POV (the sleuth) throughout
- **Length**: ~20,000 words / 16 chapters (or ~50,000 / 30 if user chose novel length)
- **Heat level**: Sweet/Clean by default (user can choose mild spice)
- **Tone**: Warm, witty, cozy with genuine mystery tension
- **Mystery structure**: Body discovered by chapter 2-3, investigation through middle, red herrings and complications, dark moment, sleuth connects the dots, confrontation/reveal, resolution

## Names & Places Avoidance Rules

ALL generated content must avoid overused AI-generated names and patterns. No names ending in -wyn, -ael, -ienne, -elle. No Elara, Cassandra, Thorne, Rowan, Sage, Luna, Aurora, Willow, Jasper, Hawthorne, Sterling, etc. No "Willowbrook," "Maplewood," "Ravenwood" place names. No "[Tree] + [Landscape Feature]" formulas. No "The Cozy [Noun]" or "Enchanted [Noun]" business names. No Whispers, Shadows, Secrets, Embers in titles. Use real-world naming patterns. Everything should feel authentic, not AI-generated.

## Number & Time Diversity (Anti-7 Bias)

LLMs default to 7 for "random" numbers. Actively avoid this. Distribute numbers across all ending digits for ages, times, dates, quantities, addresses, durations. After completing any outline, scan for the digit 7 and replace most instances with other numbers.

## Workflow

Read `references/workflow-steps.md` for the complete step-by-step writing and editorial pipeline.

## Prose Craft

Read `references/prose-craft.md` for show-don't-tell rules, dialogue craft, and narrative authenticity standards. These rules apply during WRITING, not just revision — every chapter must be crafted to these standards from the start.

## Editorial Pipeline

Every manuscript goes through a full editorial pipeline after the first draft:

1. **AI-Ism Revision** — Remove robotic phrasing, fix POV breaks, sharpen dialogue, improve chapter endings
2. **Developmental Edit** — Structural assessment of mystery fairness, pacing, character arcs, genre compliance
3. **Beta Read** — Critical reader review with star rating and ranked improvement suggestions
4. **Targeted Revision** — Apply top 3-5 fixes from dev edit and beta read
5. **Outline Adherence Audit** — Final check that the mystery reveal wasn't spoiled through foreshadowing, unequal suspect treatment, or backward writing

Read `references/revision-guide.md` for the complete editorial checklist.
