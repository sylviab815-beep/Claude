---
name: thriller-author
description: >
  Interactive thriller manuscript writer. Asks upfront choices: subgenre (psychological, domestic,
  crime, legal, medical, political, techno, espionage), protagonist type, POV, twist complexity,
  pacing, tropes, and heat/violence level. Supports uploading previous work to build a style guide.
  Strict tension architecture system prevents the AI from revealing too much too early, dropping
  tension in the middle, or writing twists that don't hold up. Full editorial pipeline. MANDATORY
  TRIGGERS: "thriller author", "write a thriller", "thriller manuscript", "write my thriller",
  "thriller plugin", "suspense manuscript", or any mention of writing/generating a thriller.
---

# Thriller Author

An interactive thriller manuscript writer that asks what you want upfront, then writes a complete publish-ready novella or novel with genre-specific craft guardrails for information control, tension escalation, and twist integrity.

## What This Skill Produces

One folder per book containing:

```
[Book Title]/
├── [Book Title].docx                    # ~20k-100k word complete manuscript
├── [Book Title] - KDP Info.docx         # Amazon metadata + cover prompt
└── [Book Title] - Style Guide.md        # (if style guide was built from uploads)
```

## Interactive Setup — Ask Before Writing

This skill does NOT auto-generate. It asks the user questions using AskUserQuestion (popup-style multiple choice) before writing anything. Ask each question ONE AT A TIME.

### Question Flow

Read `references/workflow-steps.md` for the complete question flow. The setup asks:

1. **Thriller Subgenre** — psychological, domestic, crime, legal, medical, political, techno, espionage, action, conspiracy?
2. **Protagonist Type** — ordinary person, professional, outsider, flawed expert, victim fighting back, antihero?
3. **POV Structure** — single first-person, single third-person close, dual POV, multiple POV, mixed?
4. **Twist Complexity** — one major twist, two-layer, puzzle-box, or no major twist?
5. **Pacing Style** — slow burn, relentless, ratcheting, or dual timeline?
6. **Ticking Clock** — literal deadline, escalating pattern, soft deadline, or no clock?
7. **Tropes** — pick 2-4 from: unreliable narrator, past resurfaces, nobody is who they seem, gaslighting, wrong person blamed, whistleblower, missing person, cat-and-mouse, trapped, conspiracy, double cross, complicit protagonist
8. **Violence/Intensity Level** — clean suspense (threat-based, minimal violence), moderate (violence present but not graphic), dark (unflinching, visceral, disturbing), or extreme (graphic content warnings)?
9. **Length** — novella (20k/16ch), standard novel (50k-70k/30-38ch), or extended (80k-100k/45-55ch)?
10. **Series Position** — standalone, Book 1, continuing?
11. **Style Guide Upload** — match your existing voice?
12. **Outline Upload** — bring your own or generate one?

## Style Guide System

If the user uploads manuscripts, extract:

- **Voice & Tone**: Clinical vs atmospheric, humor level, darkness tolerance, sentence rhythm
- **Tension Style**: How dread is built — through implication, through detail, through pace
- **Dialogue Patterns**: Interrogation style, evasion techniques, how lies sound vs truth
- **Pacing Style**: Chapter length, scene breaks, how cliffhangers are constructed
- **Description Style**: Sparse vs immersive, sensory approach, how settings create unease
- **Information Control**: How clues are hidden, how misdirection is handled
- **POV Handling**: Tense, person, interiority depth, how unreliability is managed
- **Violence/Intensity**: How dark scenes are written — implication vs depiction

Save as `[Book Title] - Style Guide.md`.

## The Tension Architecture System (CRITICAL)

This is the most important guardrail for thrillers. The AI has a strong tendency to:

- **Reveal too much too early** — because it knows the truth and can't help hinting at it
- **Drop tension in the middle** — Act 2 sags because the AI runs out of escalation ideas
- **Make the protagonist too competent** — the AI writes protagonists who figure things out too fast because it knows the answer
- **Write twists that don't hold up** — the twist is shocking but on re-read, there were no real clues
- **Telegraph the antagonist** — through loaded descriptions, suspicious dialogue, or "something felt off" narration
- **Resolve threats too quickly** — a danger is introduced and neutralized in the same chapter
- **Write false calm that feels like filler** — breather chapters that don't plant seeds for the next escalation

Read `references/tension-architecture.md` for the complete system. Core rules:

### Rule 1: Information Is Currency — Spend It Deliberately
Every chapter must have an information budget. What does the reader learn? What remains hidden? What do they THINK they've learned that's actually misdirection? The information release schedule from the outline is LAW. No early reveals, no skipped plants, no extra clues the AI invents because it's excited about the twist.

### Rule 2: Tension Never Flatlines
Every chapter must EITHER escalate tension, provide a brief relief valve that sets up the next escalation, or deliver a revelation. There are no neutral chapters. Even "quiet" scenes must have an undercurrent of dread — the protagonist noticing something wrong, a detail that doesn't add up, a sense that they're being watched.

### Rule 3: The Protagonist Earns Every Inch
The protagonist does NOT figure things out easily. Every piece of the puzzle costs something — time, safety, trust, sanity. The AI must resist its urge to have the protagonist connect dots too quickly. If the protagonist has a breakthrough in Chapter 12, Chapters 8-11 must show the work — dead ends, wrong conclusions, frustration.

### Rule 4: Twists Must Be Reverse-Engineerable
Every twist must have at least 3 planted clues visible on re-read. The twist should make the reader say "I should have seen that" — never "where did that come from?" If a twist can't pass the reverse-engineering test, it's not ready.

### Rule 5: The Antagonist Has Equal Screen Time
If the antagonist is known to the reader, their competence must be shown, not just told. If the antagonist is hidden, the EFFECTS of their competence must be visible. The reader should respect the threat. The antagonist should feel like they're winning until the very end.

### Rule 6: Every Relief Valve Plants a Seed
The brief moments where tension dips — a conversation with a friend, a quiet evening, a scene of normalcy — must plant information that pays off later. The reader doesn't realize the seed was planted because they were relieved. This is how the best thrillers make twists feel inevitable in hindsight.

## Core Specifications

Defaults — the interactive setup may change them:

- **POV**: Single first-person present tense (most common for psychological thrillers — adjustable)
- **Structure**: Chronological with short chapters (or dual timeline if chosen)
- **Length**: ~60,000 words / 35 chapters (standard)
- **Intensity**: Moderate (adjustable)
- **Tone**: Atmospheric dread building to claustrophobic urgency
- **Chapter structure**: Short chapters (1,200-1,800 words), ending on hooks or questions. The "one more chapter" engine.

## Names & Places Avoidance Rules

No generic thriller names (Sarah, Jack, Kate, Tom). No "Blackwood" or "Grayson" or "Sterling." No "[Dark Word]+[Place]" formulas. No titles using Silent, Dark, Hidden, Girl, Woman, Wife, Lie, Truth, Secret, Last, Gone. Names should feel demographically accurate and specific to the setting.

## Number & Time Diversity (Anti-7 Bias)

Avoid 7 in all content. Especially: addresses, phone numbers, timestamps, ages, case file numbers, countdown timers.

## Reader Radar Integration (Suspense Thriller)

When the user selects **suspense thriller** (or a subgenre with strong suspense elements), read `references/reader-radar-suspense-thriller.md` and apply throughout writing:

- **Concept & Outline Generation**: Prioritize HIGH-demand elements — relentless pacing (#1), devastating secret/lie (#2), personal stakes (#3), late-act twist (#6). Flag cooling trends. Surface market gaps as differentiation opportunities.
- **Protagonist Writing**: Default to the "Ordinary Person Who Discovers the Lie" archetype — relatable civilian, not trained for danger. Everyman-in-peril outperforms trained-operative setups in this lane.
- **Antagonist Writing**: Default to "Hidden Threat with Personal Connection" — someone the protagonist trusted. Stranger-danger is less e