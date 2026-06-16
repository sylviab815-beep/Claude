---
name: check-integrity
description: Run a structural integrity scan on a manuscript or partial draft (catches narrator future-leak, telegraphed clues, premature reveals)
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# /check-integrity

Run a structural integrity scan on any manuscript or partial draft. Detects:

- **Narrator future-leak** — "I would later learn," "in the days that followed," "as it turned out," "little did she know" — any phrase where the narrator references what's coming
- **Telegraphed observation** — narrator labeling a clue as significant while pretending to merely observe it
- **Antagonist-name density** (mystery / suspense / thriller / dark romance with reveal) — antagonist named too often vs other suspects in pre-reveal chapters
- **Suspect-clearing speed** (mystery) — suspects cleared in <2 verifiable steps

## Inputs

Ask the user for:

1. **Manuscript file path** (markdown with `## Chapter N: Title` headings)
2. **Mode** — `general` (any genre) or `mystery` (adds antagonist density + clearing checks)
3. If `mystery`: antagonist name, reveal chapter number, comma-separated other suspects
4. Optional: chapter range to limit the scan

## Pipeline

Invoke the `codex-to-manuscript` skill and run:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/codex-to-manuscript/scripts/integrity_check.py \
    --manuscript [path] \
    --mode [general|mystery] \
    [--killer "[name]"] \
    [--reveal-chapter N] \
    [--suspects "Name 1, Name 2"] \
    [--chapters-from N] [--chapters-to N] \
    --output [report path]
```

Then read the report and surface to the user:

- The Scorecard (PASS / WARN / FAIL on each dimension)
- The top 5 most urgent fixes
- The recommended action queue

Offer to apply suggested fixes one batch at a time.

## When to use

- During drafting, automatically every 3 chapters (built into the main pipeline)
- Manually any time before running editorial passes
- After a manual revision to verify the fix landed
- On someone else's manuscript you're editing
