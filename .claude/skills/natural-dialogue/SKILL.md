---
name: natural-dialogue
description: Use this skill whenever a user asks for an audit, critique, or fix of dialogue in fiction prose. Trigger on requests like "audit my dialogue," "the dialogue feels flat," "fix the yeses," "make this dialogue land," "everyone sounds the same," "tighten the dialogue," or any request where the user wants existing fictional dialogue checked for character voice, naturalness, filler, or speaker differentiation. Works on chapters, scenes, or single exchanges. Profile-aware — if a voice profile is loaded (via author-voice-lock or a series-keyed drafting skill), reads it and proposes character-appropriate rewrites; otherwise flags issues with generic fix patterns. Trigger ON pass-N requests ("another dialogue pass," "audit it again") and handle iteration discipline by avoiding rehash. Do NOT use for pre-draft outline critique (use outline-critique), general prose editing (use editorial-pass skills), or dialogue generation from scratch.
---

# Natural Dialogue

A structured audit skill for fictional dialogue. Runs a 14-category check on prose and produces a numbered critique with per-line locations, proposed fixes, and a leverage-ranked priority list.

It exists because LLM dialogue defaults — and tired-author dialogue defaults — tend toward bare acknowledgments, filler exchanges, on-the-nose emotional naming, therapy-speak, and speaker-voice collapse. None of those are wrong by themselves; they're wrong as defaults. This skill catches them.

## Why dialogue auditing matters

Dialogue is where character lives. Flat dialogue strips a character of voice and makes a 100k-word manuscript feel anonymous. Most editorial passes catch dialogue tics late — after thousands of lines have already drifted toward the LLM mean. Running this audit chapter-by-chapter during drafting (or in batches across acts after drafting) catches the drift while it's cheap to fix.

## Core principle

**Read DIALOGUE_CATEGORIES.md and the relevant genre overlay before running any pass.** They're dense by design. Loading them costs minutes; running passes without them produces vague critique that misses category-specific bugs (RH claim-language norms, mystery clue-revealing dialogue, literary register shifts).

## When to use this skill

Trigger on:

- "Audit my dialogue" / "the dialogue feels flat" / "fix the yeses"
- "Make this dialogue land" / "everyone sounds the same"
- "Tighten the dialogue" / "the conversations feel generic"
- "Do a dialogue pass on this chapter" / "fix the dialogue in scene 3"
- "Run another dialogue pass" (iteration mode)
- Any request where the user wants existing dialogue checked

Do NOT trigger on:

- Pre-draft outline critique (use `outline-critique`)
- General prose editing — line-level voice/sentence work (use editorial-pass skills)
- Generating dialogue from scratch (use a drafting skill)
- Casual brainstorming about what a character might say

## Profile-aware mode

If a voice profile is active (via `author-voice-lock` or any series-keyed drafting skill), this skill reads it and proposes **character-appropriate rewrites** for each flagged line, drawing from the profile's per-character voice rules.

If no profile is active, the skill flags issues and suggests generic fix patterns from `REWRITE_PATTERNS.md` without proposing specific lines (the author owns voice).

The output format is the same in both modes; profile-aware mode just adds the rewrite suggestions.

## The workflow

When asked to audit dialogue:

1. **Load the prose.** Read end-to-end before checking anything.
2. **Confirm context with the user** — see "Required context" below.
3. **Check for an active voice profile.** If the user mentions a pen name or there's an obvious series-keyed skill in play, load the profile. Otherwise run in standalone mode.
4. **Read references/DIALOGUE_CATEGORIES.md** in full.
5. **Read the relevant genre overlay** from references/PER_GENRE_OVERLAYS.md based on the user's stated genre.
6. **Read references/REWRITE_PATTERNS.md** if generating rewrite suggestions.
7. **Run the 14-category audit.** Categories listed below; full detail in CRITIQUE_CATEGORIES.md.
8. **Run the grep pass** from `references/GREP_PASS.md`.
9. **Produce the audit** — bold problem statement → location (chapter + line or excerpt) → why it matters → proposed fix (character-appropriate if profile-aware).
10. **End with a priority list** — the top 10-15 fixes ranked by impact.

## Required context (always confirm before audit)

- **Genre / sub-genre** — drives genre overlay
- **Heat level** (if romance-adjacent) — affects claim-language tolerance
- **POV / tense** — single vs. multi-POV; how speaker attribution works
- **Active voice profile** — pen name, character names, per-character voice rules
- **Pass number** — is this pass 1, 2, 3? (drives iteration discipline)
- **What previous passes covered** (if any)

If the user can't or won't answer, infer from the prose and flag the inference at the top of the audit. Don't refuse to proceed.

## The 14 categories (overview)

Full detail in `references/DIALOGUE_CATEGORIES.md`. At a glance:

1. Bare confirmations — *Yes / No / Okay / Sure / Right / Uh-huh*
2. Filler exchanges — *Hi. / Hi. / How are you? / Good, you?*
3. Acknowledgment fluff — *I see. / I understand. / Of course.*
4. On-the-nose emotional naming — *I'm angry. / That makes me sad.*
5. Therapy-speak slipping in — *processing, holding space, that's valid*
6. Excessive politeness — please/thank-you/sorry density inappropriate for register
7. Generic tic openers — *Look, / Listen, / I mean, / Well,*
8. Tag-as-meaning — *"That's enough," she said angrily.*
9. Adverbs on tags
10. Speaker-voice collapse — multiple characters voiced identically
11. Explainer dialogue — characters telling each other what they both already know
12. Question-then-answer-the-same-question — *Are you all right? / I'm fine.*
13. Trailing dot-dot-dot fluency — *I just… I don't know…*
14. Same-character lexical repetition

## Iteration discipline (pass 2+)

When running a dialogue audit on prose that's already been audited:

- **Do not rehash.** Items from previous passes that the user folded in should NOT reappear unless they're broken.
- **Find genuinely new issues.** Pass 2-3 mine deeper categories: speaker-voice collapse, explainer dialogue, lexical repetition. These often only become legible once the surface bugs are fixed.
- **Be honest when there's less to find.** A short pass-3 audit is more useful than a padded one.

## Style of audit

The audit should:

- **Locate every problem in the prose** — line number, chapter, or excerpt the issue lives in. Vague critique is useless.
- **Explain why it matters** — one sentence on what breaks if this isn't fixed. Bare-confirmation strips voice; explainer dialogue insults reader; etc.
- **Propose a concrete fix** — character-appropriate if profile-aware; pattern-level if standalone. Specific enough that the author could apply it without further conversation.
- **Use the user's terminology** — character names, pen-name conventions. Don't translate.

The audit should NOT:

- Flatter. Don't open with "the dialogue is great, here are some thoughts."
- Pad. If a category is clean, skip it — don't write "this category looks fine."
- Soften with hedges. Direct but not cruel.
- Rewrite at length without prompt. Suggested fixes are *examples,* not full rewrites.

## Output format

In chat as Markdown by default. File output only on request.

```
[One sentence of context — pass number, genre, voice profile (if loaded), word/line count audited.]

**[Bold problem statement.]** Located at: [chapter/line/excerpt]. [Why it matters in one sentence.] Proposed fix: [concrete suggestion; character-appropriate if profile-aware].

**[Next finding.]** [Same shape.]

[…continue…]

**Priority order:**
1. [Highest-leverage fix.]
…
[Up to 15 items ranked by impact.]
```

## Length

- Pass 1 on a chapter: 8-15 findings, typically 800-1200 words
- Pass 1 on a full manuscript or act: 15-25 findings
- Pass 2+: progressively shorter
- Single-scene audit: 3-7 findings

## What this skill does NOT do

- Pre-draft outline critique
- Line-level prose editing beyond dialogue
- Generating dialogue from scratch
- Beta-reader-style "what did you think" feedback

## How resource files are structured

```
natural-dialogue/
├── SKILL.md (this file)
└── references/
    ├── DIALOGUE_CATEGORIES.md (the 14 categories in detail; bug patterns; fix templates)
    ├── PER_GENRE_OVERLAYS.md (RH/romantasy/cozy/thriller/literary specifics)
    ├── REWRITE_PATTERNS.md (generic strategies for what replaces a flat line)
    └── GREP_PASS.md (the audit's grep commands)
```

Read DIALOGUE_CATEGORIES.md every pass. Read GENRE_OVERLAYS only the relevant section. REWRITE_PATTERNS is reference material when proposing fixes. GREP_PASS provides the command-line audit if the user wants a quick scan.
