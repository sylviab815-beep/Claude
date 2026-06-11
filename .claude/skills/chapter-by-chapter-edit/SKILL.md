---
name: chapter-by-chapter-edit
description: Use this skill whenever the user wants an editorial pass on a single chapter (or a small batch of chapters) of fiction prose, applied against a configured author voice profile. Trigger when the user asks to "edit," "polish," "clean," "audit," "run a pass on," "line edit," "copyedit," or "review" a chapter — including phrases like "edit chapter 3," "run a chapter pass on this," "do a chapter-by-chapter edit," "polish chapter 5 in my voice," or "apply my Jane Doe profile to this chapter." Trigger when the user pastes a chapter and asks for editorial feedback against a profile. Pairs with the author-voice-lock skill — reads the same profiles/{pen-name}.md files. Do NOT trigger for whole-manuscript editorial workflows (use full-stack-manuscript-polish), for new drafting (use author-voice-lock), or for non-fiction. Do NOT trigger when a series-keyed editing skill is available for the same series (those skills carry deeper canon).
---

# Chapter-by-Chapter Edit — Voice-Locked Editorial Skill

A chapter-at-a-time editorial skill that reads an author voice profile, runs a pipeline of eleven passes against the chapter, and delivers the result in the format the author chose. Sibling skill to `author-voice-lock`. Same profile system. Drafting-time skill enforces voice during generation; this skill enforces voice during revision.

## Core principle

**One profile. One chapter. Eleven passes. Author-chosen output.**

Read the active voice profile before touching the chapter. Read the chapter before suggesting a single edit. Apply the passes in order. Deliver in the format the author asked for.

## What this skill does

1. Loads a voice profile (banned vocab, signature moves, POV/tense, dialogue mechanics, trope guardrails, worldbuilding hooks, character voice rules) — the same profile format used by `author-voice-lock`.
2. Loads the chapter the author wants edited.
3. Uses the chapter outline/prompt if provided to run a chapter quality gate before and after editing.
4. Runs eleven editorial passes against the chapter (see `references/EDITORIAL_PASSES.md`).
5. Asks the author which output format they want for this chapter — flagged report, marked-up chapter, or cleaned replacement (see `references/OUTPUT_FORMATS.md`).
6. Delivers the edits in the chosen format.

## What this skill does NOT do

- Whole-manuscript passes — use `full-stack-manuscript-polish` for cross-book continuity, dangling thread audit, final assembly.
- New drafting — use `author-voice-lock` to draft new prose under a profile.
- Replace a series-keyed editing skill if one exists for the same series — those skills carry canon (cast, magic system, dangling threads) this skill cannot.
- Generate the profile content. The author fills it in (manually or via the `author-voice-lock` guided intake).

---

## Profile selection

Profiles use the same format as `author-voice-lock` — `profiles/{pen-name}.md`. This skill looks for profiles in this order:

1. **Sibling skill `author-voice-lock/profiles/`** — the canonical location. If `author-voice-lock` is installed, the profiles live there.
2. **Local `profiles/` folder in this skill** — fallback if the user dropped a profile here directly.
3. **User-supplied path** — if the user pastes or names a profile path, use that.

Selection logic when a chapter is submitted for editing:

1. **Explicit name in the request.** If the user says "edit as Jane Doe" or "use the dark-fantasy profile," look for `{pen-name}.md` in the locations above (case-insensitive, hyphens or underscores both fine).
2. **Single-profile fallback.** If exactly one profile exists across all lookup locations (excluding `_TEMPLATE.md` and `_EXAMPLE.md`), load it.
3. **Ask.** If multiple profiles exist and none was named, list them and ask which to use before editing. Do not guess.
4. **No profile available.** If no profile exists, tell the user and offer to either (a) run `author-voice-lock`'s guided intake to build one, or (b) run a generic editorial pass without voice rules — but flag that the second path is much weaker than a profile-driven edit.

Never invent a profile. Never blend two profiles per session unless the user explicitly asks.

---

## Editorial pipeline

Every chapter first runs the **Chapter Quality Gate** in `references/EDITORIAL_PASSES.md`. If the author supplied a chapter outline, beat sheet, or prompt, use it as the source of truth for adherence, story position, emotional progression, and premature reveals/resolution. If no outline is available, run the gate against the chapter's apparent genre job and note that outline adherence could not be verified.

Eleven passes then run per chapter, in order. Full spec in `references/EDITORIAL_PASSES.md`.

1. **Voice integrity** — banned vocab from profile Section 6, AI tells from `AI_TELL_LIBRARY.md` (if profile opted in), out-of-voice phrasing.
2. **POV & tense consistency** — head-hops, tense slips, POV drift.
3. **Sentence rhythm preservation** — flag unearned smoothing of signature moves from profile Section 7 (fragments, parallels, three-beat closers, etc.). The "don't fix what's a feature" pass.
4. **Dialogue mechanics** — tag conventions, adverb sweep, action-beat balance, character voice consistency against profile Section 11.
5. **Filter words & show-don't-tell** — _watched, noticed, felt, saw, realized, started to, began to_ and the like. Flag for tightening.
6. **Tone consistency** — does the chapter hold one tonal register, or does it slip into something off-voice (therapy-speak, romance-novel cadence, clinical detachment, etc.)?
7. **Repetition & tic words** — words used more than the profile or chapter context warrants. Echo flags.
8. **Continuity (within chapter)** — names, timeline, physical positions, established facts inside this chapter. Cross-chapter continuity is out of scope.
9. **Structure & shape** — scene count, escalation, does the chapter do a chapter's job (open → escalate → button)?
10. **Opening & closer audit** — first paragraph hooks, last paragraph buttons. Flag weak opens and limp closes.
11. **Worldbuilding canon** — capitalization and lowercase rules from profile Section 10. Catch _The Binding_ when canon says _the binding_.

---

## Output formats

The author picks the format for each chapter. Spec in `references/OUTPUT_FORMATS.md`.

- **Flagged issues report** — markdown sections per pass; each issue lists location, current text, suggested fix, and reason. Non-destructive. The author chooses what to apply. Best for line edits and complex chapters.
- **Marked-up chapter** — the full chapter with inline strikethroughs and bracketed suggestions. Easy to scan. Best for sentence-level cleanup.
- **Cleaned replacement chapter** — the rewritten chapter plus a brief change summary at the top. Fast. Best for chapters where the author trusts the rules and wants the work done.

When invoked, the skill asks which format the author wants — unless the request specifies it explicitly (_"give me a flagged report,"_ _"clean it up and hand me the rewrite,"_ _"mark it up inline"_).

---

## Workflow

When asked to edit a chapter under a voice profile:

1. **Identify the active profile** (selection logic above).
2. **Read the full active profile** before anything else. Profile rules drive every pass.
3. **Read `references/AI_TELL_LIBRARY.md` from `author-voice-lock`** if the profile opted in to universal AI tells. Available at `../author-voice-lock/references/AI_TELL_LIBRARY.md` if both skills are installed; otherwise embedded fallback rules apply.
4. **Read the chapter outline/prompt if supplied.** If the user did not supply one, do not block the edit; state that outline adherence is unverified.
5. **Read the chapter.** All of it. End to end. Before flagging anything.
6. **Confirm output format.** Ask if not specified.
7. **Run the Chapter Quality Gate, then the eleven passes in order.** Do not skip checks. If a check finds nothing, say so — silence implies it wasn't run.
8. **Deliver in the chosen format.**
9. **Note any pass that was constrained or skipped.** If the profile lacked a section the pass needed (e.g., Section 11 character voice rules empty), say so.

---

## Critical rules

These hold regardless of profile.

### Profile beats reflex
If the profile says fragments are signature, do not "fix" them. If the profile says same-starter parallels are signature, preserve them. The default editorial reflex to vary, smooth, and tighten is suppressed where the profile says preserve.

### Don't invent canon
If the chapter mentions a proper noun not in the profile, flag it for the author. Do not silently capitalize it, lowercase it, or "fix" it to match what you guess the canon should be.

### Don't blend voices
One profile per editing session. If the user wants a second pass with a different profile, that's a separate session.

### Honest reporting
If the chapter violates a profile rule, say so explicitly with location and reason. If a pass is uncertain (e.g., "this MAY be a head-hop, depends on POV intent"), flag the uncertainty rather than silently rewriting.

### Preserve author intent
If the chapter does something unusual that isn't in the profile and isn't an obvious error, flag it as a question — "this paragraph is in second-person address; is that intentional?" — rather than overwriting it.

---

## Batch mode

If the user submits more than one chapter in a single request, run the pipeline against each chapter independently and deliver each chapter's output separately. Don't merge issues across chapters; cross-chapter passes are out of scope for this skill.

---

## File layout

```
chapter-by-chapter-edit/
├── SKILL.md                           (this file)
├── README.md                          (install, pairing, usage, troubleshooting)
└── references/
    ├── EDITORIAL_PASSES.md            (the 11 passes — what each looks for, what to flag, what to suggest)
    └── OUTPUT_FORMATS.md              (the three delivery formats with examples)
```

This skill carries no profiles of its own — it reads from `author-voice-lock/profiles/`. Install both skills together for the cleanest workflow.
