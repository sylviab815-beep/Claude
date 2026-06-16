---
name: check-outline-drift
description: Compare drafted chapters against the parsed outline — verify POV, opening hooks, key scenes, cliffhangers, and intimate-beat flags all still match the plan
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# /check-outline-drift

Compare a manuscript (or a chapter range of one) against the parsed outline JSON. Flags any chapter that's drifted from the outline's stated:

- POV character
- Opening hook keywords
- Numbered key scenes
- Cliffhanger / closing line keywords
- Intimate beat flag (Yes/No)
- Chapter title

## Inputs

Ask the user for:

1. **Manuscript file path** (markdown with `## Chapter N: Title` headings)
2. **Parsed outline JSON path** (produced by `parse_outline.py`)
3. Optional: chapter range to limit the scan

If the outline JSON doesn't exist yet, run `parse_outline.py` first to produce it.

## Pipeline

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/codex-to-manuscript/scripts/outline_drift_check.py \
    --manuscript [path] \
    --outline-json [path to parsed_outline.json] \
    [--chapters-from N] [--chapters-to N] \
    --output [report path]
```

Read the report. For each chapter, show the user the chapter number, verdict (PASS / WARN), and any specific drift flags.

Offer to either:

- **Revise the affected chapters** to match the outline
- **Update the outline** to match the prose (if the user decided to deviate intentionally)
- **Accept and continue** (logged to the Edit Log)

## When to use

- During drafting, automatically every 3 chapters (built into the main pipeline)
- Manually any time you want to verify a recent chapter still tracks
- After a major revision pass, to confirm nothing structural got lost
