# Integrity Checks — Structural Audit Gates

The skill runs **two independent structural checks** alongside the Edit-As-You-Go and end-of-book editorial pipelines. These catch problems that line-edits cannot fix: foreshadowing leaks, narrator future-knowledge, telegraphed clues, premature reveals, and outline drift.

The two scripts are:

- `skills/codex-to-manuscript/scripts/integrity_check.py` — narrator/structural integrity (general patterns + optional mystery mode)
- `skills/codex-to-manuscript/scripts/outline_drift_check.py` — does the prose match the outline?

Both run during the per-chapter loop AND as final gates before delivery.

---

## When the integrity checks run

| Trigger | What runs | Gate? |
|---|---|---|
| Every 3 chapters drafted | `outline_drift_check.py` over the most recent 3 chapters + `integrity_check.py` (general mode) over the same window | Soft — surfaces issues, asks user before proceeding if FAIL count > 0 |
| End of writing phase | `integrity_check.py` over the whole manuscript (general mode, plus mystery mode if codex specifies a mystery / antagonist reveal) | Hard — must reach PASS or accepted-WARN before the final editorial pipeline runs |
| End of editorial pipeline | `integrity_check.py` re-run as a final QA pass | Hard — must reach PASS before delivery |

If any FAIL appears at a hard gate, the skill stops and surfaces the report to the user, asks whether to revise the affected chapters or accept the deviation as intentional. Never silently proceed past a FAIL.

---

## What `integrity_check.py` catches (general mode — every genre)

### 1. Future-leak narrator

The narrator can't know what's coming. This breaks suspense in any genre with withheld information — slow-burn romance, dark romance, romantic suspense, thriller, mystery, paranormal reveals.

Patterns flagged:

- "would not know it for [time]" / "would not know until [time]"
- "I/she/he would later learn / find out / discover / come to know"
- "I/she/he would spend [time]"
- "did not yet know that [event]"
- "in retrospect" / "looking back" (in narration, not dialogue — context check)
- "as it turned out"
- ", possibly, it would [verb]"
- "would mean a great deal"
- "would prove [adjective]"
- "by week's/day's/month's end"
- "in the days/weeks/hours that followed"
- "I/she/he knew then"
- "I/she/he should have known"
- "of course it was"
- "would [later] become clear/important/crucial/relevant/obvious"
- "the [full|whole] truth/answer/story would [come out|emerge|reveal itself]"
- "little did [pronoun] know"
- "if only [pronoun] had known"

### 2. Telegraphed observation

The narrator labels a clue or detail as significant while pretending to merely observe it.

Patterns flagged:

- "in some way I/she/he had not yet quite articulated"
- "I/she/he had filed it/that, too"
- "I/she/he registered X without registering it"
- "It had been [adjective] for years"
- "there was something off / wrong / strange about him/her/them/it"

### 3. Continuity reminders

Continuity bugs (event referenced before it happens, age/year drift, object teleporting) are not yet auto-detected by regex — they require LLM review during the developmental edit pass. Flag the categories but treat them as Pass 2 work.

---

## What `integrity_check.py` catches (mystery mode — when the codex specifies a mystery / antagonist reveal)

Run mystery mode whenever the codex's genre is mystery, cozy mystery, romantic suspense, dark romance, thriller, vigilante thriller, or any genre where there's a "reveal chapter" the codex marks. The reveal chapter is usually identifiable from the outline as the chapter where the antagonist's identity / true motive / final twist lands.

### 4. Antagonist-name density

If the antagonist's name appears in narration more than 2× as often as the average for other suspects (and density >1.5/1k words) in chapters BEFORE the reveal, the prose is tipping the answer.

### 5. Suspect-clearing speed

Suspects cleared in <2 verifiable steps are cleared too fast. Catches:

- Definitive clearances after one statement
- "All right. You're cleared" patterns

Replace with conditional verification: *"A gallery opening with forty witnesses takes a phone call. I will make the call. Until then, you stay on the list."*

---

## What `outline_drift_check.py` catches (every 3 chapters)

For each drafted chapter in the recent window, compare against the parsed outline:

| Check | What it does | Threshold |
|---|---|---|
| **Title match** | Compare draft chapter title to outline chapter title | Loose substring match |
| **POV** | Verify the expected POV character is mentioned (or first-person used) in the chapter's first 1500 chars | Both name-mentions and first-person count must be near-zero to fail |
| **Opening drift** | Compare keywords from the outline's "Opening Hook" against the draft's first paragraph | <25% keyword overlap = WARN |
| **Ending drift** | Compare keywords from the outline's "Cliffhanger" / "Closing Line" against the draft's last paragraph | <25% keyword overlap = WARN |
| **Missing key scenes** | For each numbered Key Scene in the outline, scan the chapter for keyword coverage | <35% overlap on a scene = WARN |
| **Intimate beat enforcement** | If the outline marks Intimate Beat: Yes, check the chapter actually contains intimate-beat language | <3 markers in the chapter = WARN |

Each check is heuristic — none of them are perfect. They're designed to catch obvious drift (a chapter on a totally wrong topic, a missing scene, a fade-to-black where the outline asked for on-page) without flagging legitimate creative variation.

---

## How to invoke during writing (Phase 4)

After every chapter is drafted and edited-as-you-go, save the chapter to a working manuscript markdown file (`/tmp/working_draft.md` or similar) with a `## Chapter N: Title` heading. Continue.

After every 3 chapters drafted, run:

```bash
# General integrity scan over the recent 3 chapters
python3 ${CLAUDE_PLUGIN_ROOT}/skills/codex-to-manuscript/scripts/integrity_check.py \
    --manuscript /tmp/working_draft.md \
    --mode general \
    --chapters-from $((current_chapter - 2)) \
    --chapters-to $current_chapter \
    --output /tmp/integrity_recent.md

# Outline drift over the same window
python3 ${CLAUDE_PLUGIN_ROOT}/skills/codex-to-manuscript/scripts/outline_drift_check.py \
    --manuscript /tmp/working_draft.md \
    --outline-json /tmp/parsed_outline.json \
    --chapters-from $((current_chapter - 2)) \
    --chapters-to $current_chapter \
    --output /tmp/drift_recent.md
```

Read both reports. If any FAIL appears, stop and ask the user whether to revise the chapter(s) before continuing. If only WARNs appear, log them to the Edit Log and continue (but address them during the end-of-book pass).

## How to invoke at end of book (Phase 5 → before final editorial)

Run once over the full manuscript:

```bash
# General integrity full sweep
python3 ${CLAUDE_PLUGIN_ROOT}/skills/codex-to-manuscript/scripts/integrity_check.py \
    --manuscript /tmp/working_draft.md \
    --mode general \
    --output /tmp/integrity_full.md

# Mystery mode if the codex specifies an antagonist reveal
python3 ${CLAUDE_PLUGIN_ROOT}/skills/codex-to-manuscript/scripts/integrity_check.py \
    --manuscript /tmp/working_draft.md \
    --mode mystery \
    --killer "[Antagonist Full Name from codex]" \
    --reveal-chapter [reveal chapter number] \
    --suspects "[Other Suspect 1, Other Suspect 2, …]" \
    --output /tmp/integrity_mystery.md
```

For mystery mode, identify the reveal chapter from the codex outline (the chapter where the antagonist's identity / motive / twist lands — often marked in the outline as the climax beat or the chapter where the cliffhanger explicitly names the antagonist). The "suspects" list is the set of red-herring or potential-suspect characters from the codex; for non-mystery genres with an antagonist reveal (dark romance twist, thriller pivot), the suspects list can be the cast of characters with narrative weight.

---

## How to handle results

| Verdict | Action |
|---|---|
| All PASS | Log to Edit Log. Continue. |
| Only WARN | Log to Edit Log. Continue, but mention the warnings in the user-facing progress update. |
| Any FAIL | Stop. Surface the report to the user. Ask whether to revise the affected chapter(s). Do NOT silently proceed. |

After each revision, re-run the affected checks before continuing.

---

## What the integrity checks DON'T catch

- Plot logic problems (the killer needs alibi in chapter 7 but is on-camera in chapter 5)
- Character voice consistency
- Timeline math (character ages, dates, durations)
- Scene-to-scene flow

Those are caught in the end-of-book Developmental Edit pass (see `editorial_pipeline.md` Loop 2 Pass 2).
