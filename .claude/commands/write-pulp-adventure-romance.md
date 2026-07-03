---
name: write-pulp-adventure-romance
description: Write a complete Pulp Adventure Romance manuscript from a finished outline
---

Write a publication-ready Pulp Adventure Romance manuscript from a completed outline produced by the Pulp Adventure Romance Outline Builder.

The skill executes a 6-phase pipeline: outline verification, interactive setup (including LLM selection, era confirmation, heat level, POV, tense, tone, optional style sample, author name), pre-writing setup, chapter-by-chapter drafting with the Adventure-Romance Interlock System (ARIS) applied at every chapter, full 5-stage editorial pipeline, and KDP metadata generation.

Output: a single .docx manuscript, a KDP metadata .docx, and an ARIS chapter log .docx.

Use this skill after running the Pulp Adventure Romance Outline Builder.

---

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
