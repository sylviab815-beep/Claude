# Output Formats — Chapter-by-Chapter Edit

Three delivery formats. The author picks one per chapter. If the author doesn't specify, ask before running the passes — the format affects how the passes are surfaced.

---

## Format 1 — Flagged Issues Report

**When to use.** Default for line edits, complex chapters, voice-locked work where the author wants control over which fixes apply. Non-destructive.

**Structure.** Markdown report with a section per pass. Each issue carries location, current text, suggested fix, and the rule that was violated.

**Template.**

```markdown
# Chapter [N] — Editorial Report
**Profile:** [pen-name]
**Word count:** [X words]
**Passes run:** 11/11
**Quality Gate:** [PASS / FAIL / PARTIAL, with constrained checks noted]
**Total issues:** [N]
**Top priorities:** [brief list of the 3 highest-impact flags]

---

## Chapter Quality Gate
[PASS/FAIL table for natural prose, tone match, outline adherence, arc consistency, emotional progression, pacing/transitions, show-vs-tell, chapter ending, POV, heat/intensity calibration, banned-list sweep. If outline was not supplied, mark outline adherence as "not verified" rather than pass.]

---

## Pass 1 — Voice Integrity
[N issues]

### Issue 1.1
- **Line 47** (or paragraph 4, sentence 2 — use whichever locator the input supports)
- **Current:** _The way the light caught his face was something she would remember._
- **Suggested:** _The light caught his face. She would remember it._
- **Rule:** Banned simile construction ("the way [X] verbs"). Profile Section 6.

### Issue 1.2
- **Line 92**
- **Current:** _A flicker of something crossed his face._
- **Suggested:** _Something crossed his face — gone before she named it._
- **Rule:** "A flicker of [emotion]" is a banned hedging tell. AI Tell Library Category C.

[…]

---

## Pass 2 — POV & Tense Consistency
[N issues, or "No issues found."]

[…]

---

## Pass 11 — Worldbuilding Canon
[N issues]

[…]

---

## Constraints / notes
- [Any pass that was constrained or skipped, and why.]
- [Any flag where confidence is low and the author should review carefully.]
```

**Rules for the flagged report.**
- Every pass gets a header even if it found nothing — say "No issues found" rather than omitting the pass.
- Issues are numbered hierarchically (`1.1`, `1.2`, `2.1`) so the author can refer to them by number when applying.
- Current and Suggested are in italics, blockquoted if multi-line.
- Rule cite is short and points at the source (Profile Section X / AI Tell Library Category Y / universal default).
- The summary at the top is real — count actual issues, name actual top priorities, not generic "voice and dialogue need attention."

---

## Format 2 — Marked-Up Chapter

**When to use.** When the author wants to scan the chapter and see edits in context. Best for sentence-level cleanup and shorter chapters. Easier to read than a flagged report; harder to apply selectively.

**Structure.** The full chapter, rendered with inline strikethroughs and bracketed suggestions. A summary header at the top lists what passes ran and where the heaviest flagging sits.

**Inline notation.**
- `~~strikethrough~~` for text to remove or replace.
- `[suggested replacement]` for the fix, in brackets immediately after the strikethrough.
- `[Q: question for author]` for uncertain flags or things the author needs to decide.
- `[note: reason / rule]` for the rule citation, in italics, after the suggestion.

**Template.**

```markdown
# Chapter [N] — Marked-Up Edit
**Profile:** [pen-name]
**Word count:** [X words]
**Passes run:** 11/11
**Quality Gate:** [PASS / FAIL / PARTIAL, with constrained checks noted]
**Heaviest flagging:** [pass names with most issues]

---

[Chapter title or first heading, if present]

She walked into the room and ~~the way the light caught his face was something she would remember~~ [the light caught his face. She would remember it.] [_note: banned simile construction, Profile Section 6_]. He turned. ~~A flicker of something crossed~~ [Something crossed] his face [_note: "a flicker of [emotion]" is a banned hedging tell_].

[Q: this paragraph slips into present tense for two sentences — was that intentional? If yes, mark it; if no, restoring past tense.]

[…rest of chapter, marked up inline, end to end…]

---

## Summary
- Pass 1 (voice): 12 flags
- Pass 5 (filter words): 8 flags
- Pass 7 (repetition): 4 flags
- Other passes: clean or 1–2 flags each
- Top three to address: [list]
```

**Rules for marked-up format.**
- Render the entire chapter — don't truncate, don't summarize sections.
- Multiple edits in the same sentence use multiple strikethrough/suggestion pairs.
- Long structural rewrites get a `[Q: …]` rather than an inline suggestion — the author should make those calls.
- The summary at the bottom mirrors the report header structure.
- Preserve the chapter's paragraph breaks and any italics, bold, or scene breaks the original used.

---

## Format 3 — Cleaned Replacement Chapter

**When to use.** When the author trusts the rules and wants the work done. Fastest path. Best for chapters where the author has already approved the editorial direction.

**Structure.** The fully rewritten chapter, plus a brief change summary at the top. No inline markup — the chapter reads clean.

**Template.**

```markdown
# Chapter [N] — Cleaned Replacement
**Profile:** [pen-name]
**Original word count:** [X]  →  **Revised word count:** [Y]
**Passes applied:** 11/11
**Quality Gate after revision:** [PASS / FAIL / PARTIAL, with remaining author-decision flags noted]
**Major changes:** [3–5 bullets, e.g., "Removed 12 banned-vocab instances," "Tightened 8 filter-word constructions," "Restored same-starter parallel in scene 2 closer."]
**Author-decision flags:** [N — see below]

---

[The full revised chapter. Clean. No strikethroughs, no brackets. Reads like a final draft.]

---

## Author-decision flags
The following flags were not silently fixed because they involve author intent. Review and decide:

1. **Paragraph 12, lines 184–187:** Shift to second-person address. Kept as-is. Confirm or revise.
2. **Scene 2 closer:** Original ends mid-conversation. Kept; alternative would close on the line at paragraph 31. Author's call.
3. **New proper noun "the Spire" in paragraph 47:** Not in profile worldbuilding canon. Kept lowercase per default; confirm capitalization rule.

## Other notes
- [Any pass that was constrained or skipped, and why.]
- [Any structural concern that wasn't applied because it requires authorial intent.]
```

**Rules for the replacement format.**
- Apply every fix the passes identified that is rule-driven and uncontroversial (banned vocab, filter words, AI tells, capitalization canon, dialogue mechanics, etc.).
- Re-run the Chapter Quality Gate after the replacement chapter is drafted. Do not claim the chapter is clean unless all verifiable checks pass.
- Do NOT silently apply structural rewrites, POV/tense shifts, or anything that involves author intent. Surface those as author-decision flags.
- Preserve all signature moves the profile says preserve. Do not "vary" parallels, "smooth" fragments, or "tighten" earned negations.
- The change summary is real — list actual categories with counts.
- The revised chapter must be the full chapter end-to-end. Never truncate.

---

## Asking the author which format to use

When invoked without a format specified, ask:

> Which output format for this chapter?
>
> 1. **Flagged issues report** — list of issues per pass, you choose what to apply (recommended for line edits and complex chapters)
> 2. **Marked-up chapter** — the chapter with inline strikethroughs and bracketed suggestions (best for scanning)
> 3. **Cleaned replacement** — the fully revised chapter, plus a change summary (fastest if you trust the rules)

If the author replies with shorthand (_"flagged,"_ _"marked,"_ _"clean,"_ _"1,"_ _"2,"_ _"3,"_ etc.), proceed.

If the author says "all three," produce all three for the same chapter — but warn that this is roughly 3× the output and they may want to start with one.

---

## Format selection persistence

If the author specifies a format and then submits a second chapter without specifying again, use the same format. Tell them they can switch by naming the new format.
