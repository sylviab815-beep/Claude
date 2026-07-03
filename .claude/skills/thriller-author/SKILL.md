---
name: thriller-author
version: 1.1.0
description: "Interactive thriller manuscript writer. Asks an Execution Mode question first (Autonomous for Fable 5/Opus, Supervised for Sonnet), then upfront choices: subgenre (psychological, domestic, crime, legal, medical, political, techno, espionage), protagonist type, POV, twist complexity, pacing, tropes, and heat/violence level. Supports uploading previous work to build a style guide. Strict tension architecture system prevents the AI from revealing too much too early, dropping tension in the middle, or writing twists that don't hold up. Full editorial pipeline. MANDATORY TRIGGERS: \"thriller author\", \"write a thriller\", \"thriller manuscript\", \"write my thriller\", \"thriller plugin\", \"suspense manuscript\", or any mention of writing/generating a thriller."
---

# Thriller Author

## Phase 0: Execution Mode

Ask this FIRST, before any other setup question, using AskUserQuestion:

"Which Claude model are you running this session on?

1. **Fable 5 or Opus** — Autonomous mode: I write the complete manuscript in one continuous run with built-in self-verification passes, and only check in at major milestones or if something needs your decision.
2. **Sonnet** — Supervised mode: I write in chunks of roughly 3 chapters and pause at each checkpoint for your review before continuing.
3. **Not sure** — I'll use Supervised mode. It works well on every model."

Record the answer as EXECUTION MODE for the entire session.

**Rules:**
- Options 2 and 3 BOTH map to Supervised mode. "Not sure" must NEVER map to Autonomous mode.
- Restate the chosen mode when presenting the outline/concept for approval, before any prose is written.
- Never switch modes mid-session unless the user explicitly asks.
- Do not recommend the user upgrade models. If asked, note that Supervised mode produces the same quality workflow; Autonomous mode is a convenience, not a requirement.

**AUTONOMOUS MODE (Fable 5 / Opus):** Write the entire manuscript in one continuous run — no pauses between chapters or chunks. Run all per-chapter checks silently and fix violations before continuing. After the full draft, run the complete editorial pipeline end-to-end, including re-audit loops (audit → fix → re-audit until clean, 3 passes max per stage). Check in ONLY at: (a) outline/concept approval, (b) final delivery, (c) a decision the setup answers don't cover, (d) an unrecoverable error. Word count enforcement is mandatory — expand any short chapter before moving on.

**SUPERVISED MODE (Sonnet / Not sure) — default:** Write in chunks of ~3 chapters. After each chunk, present a brief progress summary (chapters completed, running word count, any guardrail flags) and WAIT for the user's go-ahead. Run the editorial pipeline stage-by-stage, reporting after each stage.

---

## STEP 0: Output Format Selection (AFTER PHASE 0 — BEFORE ANY OTHER QUESTIONS)

**After the Execution Mode question — but before any trope selection, any outline work, or any manuscript generation**, ask the user exactly this — word for word:

> Before we dive in — how would you like your output delivered?
>
> **A) Markdown** — everything appears directly in chat, paste-ready, lowest token cost, works great in Novelcrafter, Obsidian, or pasting into Claude
> **B) Word Document (.docx)** — formatted and downloadable
> **C) PDF** — polished and ready to print or share
>
> Just reply A, B, or C.

Wait for the user's reply. Store the answer as `OUTPUT_FORMAT = A`, `B`, or `C`.

This question is asked **ONCE, at the very start of the run**. Do NOT re-ask it mid-workflow. Carry the same `OUTPUT_FORMAT` value through every later step of this plugin.

### How OUTPUT_FORMAT controls delivery

- **If OUTPUT_FORMAT = A (Markdown in chat):**
  - **Do not create any files.** Skip every `Write` / `.docx` / `.pdf` / file-creation step in this plugin.
  - Deliver ALL outputs (outlines, chapters, bios, bibles, metadata, appendices, trackers) as clean, well-structured markdown directly in the chat response.
  - Use markdown headers (`#`, `##`, `###`), horizontal rules (`---`), bullet lists, numbered lists, and bold for structure. Keep it paste-ready for Novelcrafter / Obsidian / Claude.
  - Still produce the full content — just in chat, not in a file.

- **If OUTPUT_FORMAT = B (Word Document .docx):**
  - Follow the existing file-creation workflow exactly as written below.
  - Save the final deliverable(s) as `.docx` file(s) in the user's workspace folder and share with a `computer://` link.

- **If OUTPUT_FORMAT = C (PDF):**
  - Follow the existing file-creation workflow, but convert the final document to a `.pdf`.
  - Use the `pdf` skill or a reliable `.docx → .pdf` conversion path (pandoc, LibreOffice, or the pdf skill) to produce a polished PDF.
  - Save the `.pdf` to the user's workspace folder and share with a `computer://` link.

Apply `OUTPUT_FORMAT` consistently to **every** output section in this plugin run — final manuscript, metadata, bibles, trackers, appendices, cover prompts, everything. One choice, one format, for the whole run.

**Do not proceed to any other question until the user has answered A, B, or C.**

---

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

## Workflow

Read `references/workflow-steps.md` for the complete pipeline.

## Prose Craft

Read `references/prose-craft.md` for thriller-specific writing rules: tension through implication, dialogue as weapon, pacing through sentence structure, how to write reveals, and how to manage unreliable narration.

## Editorial Pipeline

1. **AI-Ism Revision** — Remove robotic phrasing, fix POV breaks, sharpen dialogue
2. **Tension Architecture Audit** — Verify information control, tension escalation, twist integrity
3. **Developmental Edit** — Structural assessment of pacing, character, stakes, genre compliance
4. **Beta Read** — Critical reader review calibrated for thriller readers
5. **Targeted Revision** — Apply top fixes

Read `references/revision-guide.md` for the complete editorial checklist.
