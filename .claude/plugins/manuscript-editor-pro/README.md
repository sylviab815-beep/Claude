# Manuscript Editor Pro v2.2.0

Professional fiction manuscript editing with Track Changes. Every prose change is delivered as a tracked revision the author can accept or reject individually in Microsoft Word, Google Docs, or any word processor that supports tracked changes.

## What It Does

The plugin offers up to 4 editing stages — you choose which ones to run:

- **Developmental Assessment** — Big-picture structural analysis. Produces an advisory report with issues and suggestions. Never touches your prose.
- **Line Edit** — Prose-level fixes (AI artifacts, show-vs-tell, crutch phrases, dialogue, voice) delivered as Track Changes in your .docx.
- **Proofread** — Grammar, punctuation, spelling, and consistency corrections delivered as Track Changes.
- **Continuity Audit** — Builds a character bible, timeline, geography map, and world rules reference. Fixes contradictions with Track Changes.

## How to Use

1. Upload your manuscript (.docx or .epub)
2. Say "edit my manuscript" or use the /edit-manuscript command
3. Choose which passes to run
4. Review Track Changes in your word processor — accept or reject each edit

## You're Always in Control

Every single change appears as a tracked revision. Nothing is silently rewritten. The developmental assessment is advisory only — it identifies issues and suggests approaches, but the author decides what to change.

## v2.2.0 — What's New

- **Meaning Preservation Protocol** — Every tracked change is verified against a 5-point meaning check: same event, same emotion, same information, same characterization, same stakes. If a fix would change the story even subtly, it gets reverted.
- **Hedging vs. Characterization Distinction** — The AI-ism scrubber now distinguishes between AI-generated hedging ("seemed to" as lazy writing) and intentional character hedging ("seemed to" reflecting POV uncertainty). Character voice is preserved.
- **Explicit Docx Skill Dependency** — The plugin now explicitly loads the docx skill's tooling at startup, preventing script path errors.
- **Strengthened Storyline Safeguards** — "Never change what happens" is now a core principle enforced at every verify phase. Show-vs-tell conversions must preserve the exact emotion. Intimate scene edits are surgical, never wholesale rewrites. Continuity fixes never add bridging text.

## Requirements

- Cowork with the docx skill available (standard in all Cowork sessions)

## Author

Created by i2i Hype
