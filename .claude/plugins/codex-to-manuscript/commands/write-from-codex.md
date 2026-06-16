---
name: write-from-codex
description: Turn a Codex + Outline package into a publish-ready manuscript with optional revisions and edit-as-you-go editorial passes
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Agent, TodoWrite, AskUserQuestion
---

# /write-from-codex

Turn a Codex + Outline package into a complete manuscript. This command runs the full pipeline end-to-end.

## Inputs Required

Before running, the user must provide:

1. **A codex file** — `.pdf`, `.docx`, `.txt`, or `.md`
2. **An outline file** — same supported formats
3. **An output folder** (or confirm the current Cowork folder is fine)

If either file is missing, ask the user to upload it before proceeding.

## Pipeline

Invoke the `codex-to-manuscript` skill (`${CLAUDE_PLUGIN_ROOT}/skills/codex-to-manuscript/SKILL.md`) and follow its six phases:

1. **Phase 0** — Confirm output folder + verify both files uploaded
2. **Phase 1** — Parse codex + outline; show structured summary
3. **Phase 2** — Ask user about revisions (names, places, POV/tense/heat, length, style sample); apply changes
4. **Phase 3** — Route the codex's genre to its guardrail system
5. **Phase 4** — Write each chapter with Edit-As-You-Go passes
6. **Phase 5** — End-of-book editorial pipeline
7. **Phase 6** — Assemble final .docx + KDP Info doc + Edit Log

## Output

```
[customer folder]/[Book Title]/
├── [Book Title].docx
├── [Book Title] - KDP Info.docx
└── [Book Title] - Edit Log.md
```

## Time Estimate

A 50,000-word manuscript with full edit-as-you-go takes several hours. A 30,000-word novella takes 2-3 hours. Faster modes (draft-only, no editorial) are offered if the customer needs quicker turnaround.

## When To Use This Command

- A customer has a complete Codex + Outline package and wants the manuscript written
- A customer has a codex/outline they generated themselves (any source) in the standard format
- A user wants to test the pipeline against a sample package they bought

## When NOT To Use This Command

- The customer only has a codex (no outline) — direct them to the matching outline-builder skill first
- The customer only has an outline (no codex) — direct them to the matching outline-builder skill or character-bio tools
- The customer wants to edit an existing manuscript — use Manuscript Editor Pro instead
