---
name: write-thriller
description: Write a complete thriller manuscript with the Tension Architecture System and 5-stage editorial pipeline
---

Invoke the thriller-author skill to write a complete publish-ready thriller manuscript.

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

## Workflow

**Phase 0:** Execution Mode Selection (Autonomous / Supervised)

The skill then asks the Output Format question (Markdown / Word / PDF), walks through 12 setup questions (subgenre, protagonist type, POV structure, twist complexity, pacing, ticking clock, tropes, violence/intensity level, length, series position, style guide upload, outline upload), builds or verifies the outline with the Information Release Schedule and Tension Escalation Map, presents it for approval, then writes the manuscript chapter by chapter with Tension Architecture System checks, followed by the 5-stage editorial pipeline (AI-ism revision, tension architecture audit, developmental edit, beta read, targeted revision) and KDP metadata delivery.

Examples:
- Write a psychological thriller with an unreliable narrator — standard novel length
- Write my domestic thriller from the outline I just built — slow burn, dark intensity
- Write a techno-thriller novella with a ticking clock and a two-layer twist
