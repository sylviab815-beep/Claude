#!/usr/bin/env python3
"""
integrity_check.py

Structural integrity scan for fiction manuscripts. Runs in two modes:

    - "general"  — narrator future-leak, telegraphed-observation, continuity-bug
                   checks. Applies to ANY genre. Run every 3 chapters during
                   writing AND once at the end of book.
    - "mystery"  — adds killer-name density + suspect-clearing-speed checks
                   for mystery / suspense / thriller. Run only when the codex
                   specifies a mystery-style reveal structure.

This is adapted from the standalone Manuscript Integrity Checker plugin and
generalized for use across every genre supported by Codex to Manuscript.

Usage:
    # General integrity check on a single chapter or partial draft
    python3 integrity_check.py \\
        --manuscript chapter5.md \\
        --mode general \\
        --output report.md

    # Mystery-mode at end of book
    python3 integrity_check.py \\
        --manuscript book.md \\
        --mode mystery \\
        --killer "Prentiss Vole" \\
        --reveal-chapter 18 \\
        --suspects "Margaux Firth,Stavros Kemp" \\
        --output report.md

    # Antagonist-reveal mode for thriller / dark romance
    python3 integrity_check.py \\
        --manuscript book.md \\
        --mode mystery \\
        --killer "Rafe Whitlock" \\
        --reveal-chapter 22 \\
        --suspects "Other Suspect"
"""

import argparse
import re
import sys
from pathlib import Path


# -----------------------------------------------------------------------------
# Pattern libraries
# -----------------------------------------------------------------------------

# Future-leak narrator patterns. These break suspense for ANY genre with
# withheld information — slow-burn romance, dark romance twists, suspense,
# thriller, mystery, paranormal reveals, etc.
FUTURE_LEAK_PATTERNS = [
    (
        r"\bwould not know(?: it)? (?:for|until)\s+(?:a |two |three |four |five |six |seven |the )?(?:day|week|hour|month|moment)",
        "future-leak",
        "FAIL",
        "Cut. Narrator can't reference what's coming. Replace with present-moment uncertainty: 'I did not yet know what.'",
    ),
    (
        r"\b(?:I|she|he|they) would (?:later )?(?:learn|find out|discover|come to (?:know|understand|realize))",
        "future-leak",
        "FAIL",
        "Cut. Narrator is foreshadowing. Replace with in-the-moment thought.",
    ),
    (
        r"\b(?:I|she|he|they) would spend (?:later |the next |an? )?(?:hour|day|week|month|year)",
        "future-leak",
        "FAIL",
        "Cut the projection. Stay in present moment.",
    ),
    (
        r"\bdid not yet know that[,\.]\s",
        "future-leak",
        "FAIL",
        "Cut. 'did not yet know what' is fine (working uncertainty). 'did not yet know that X would happen' is foreshadowing.",
    ),
    (
        r"\bin retrospect[,\.]?\s",
        "future-leak",
        "WARN",
        "Allowed in dialogue or character thought about THEIR OWN past. Disallowed in narration about story events.",
    ),
    (
        r"\blooking back[,\.]?\s",
        "future-leak",
        "WARN",
        "Same as in retrospect — context-dependent.",
    ),
    (
        r"\bas it (?:would |later )?turn(?:ed|s)? out\b",
        "future-leak",
        "FAIL",
        "Cut. Classic foreshadowing tell.",
    ),
    (
        r",\s*possibly,?\s+it would\b",
        "future-leak",
        "FAIL",
        "Cut. The narrator is signaling that this thing matters.",
    ),
    (
        r"\bwould mean a great deal\b",
        "future-leak",
        "FAIL",
        "Cut. Direct foreshadow.",
    ),
    (
        r"\bwould (?:eventually |later )?prove\b",
        "future-leak",
        "WARN",
        "Check context. Character speculation OK. Narrator commentary not.",
    ),
    (
        r"\b(?:eventually|later) (?:I|she|he|they) would\b",
        "future-leak",
        "FAIL",
        "Cut.",
    ),
    (
        r"\bby (?:week's|day's|month's) end\b",
        "future-leak",
        "WARN",
        "Allowed only as character planning, not narrator preview.",
    ),
    (
        r"\bin the (?:days|weeks|hours) that followed\b",
        "future-leak",
        "FAIL",
        "Cut. Narrator preview of resolution.",
    ),
    (
        r"\b(?:I|she|he|they) knew then\b",
        "future-leak",
        "WARN",
        "Often foreshadowing. Verify the character has actually earned the knowing.",
    ),
    (
        r"\b(?:I|she|he|they) should have known\b",
        "future-leak",
        "WARN",
        "Narrator-knowing-better-now pattern. Use sparingly.",
    ),
    (
        r"\bof course it was\b",
        "future-leak",
        "WARN",
        "Often a tell. Verify it isn't reader-baiting.",
    ),
    (
        r"\b(?:would|will) (?:later )?become (?:clear|important|crucial|relevant|obvious)\b",
        "future-leak",
        "FAIL",
        "Cut.",
    ),
    (
        r"\bthe (?:full |whole )?(?:truth|answer|story) (?:would|will) (?:later )?(?:come out|emerge|reveal itself)\b",
        "future-leak",
        "FAIL",
        "Cut.",
    ),
    (
        r"\blittle did (?:I|she|he|they) know\b",
        "future-leak",
        "FAIL",
        "Cut. Textbook AI-narrator tell.",
    ),
    (
        r"\bif only (?:I|she|he|they) had known\b",
        "future-leak",
        "FAIL",
        "Cut. Same family as 'little did she know.'",
    ),
]

# Telegraphed-observation patterns: narrator labels something as significant
# while pretending to wonder.
TELEGRAPH_PATTERNS = [
    (
        r"\bin some way (?:I|she|he|they) had not yet quite articulated\b",
        "telegraph",
        "WARN",
        "Implies the narrator WILL articulate it. Replace with present-moment observation.",
    ),
    (
        r"\b(?:I|she|he|they) had filed (?:that|it),? too\b",
        "telegraph",
        "WARN",
        "Narrator-flagging-clue pattern. OK if earned. FAIL if first mention.",
    ),
    (
        r"\b(?:I|she|he|they) registered (?:it|the .+) without registering (?:it|the .+)\b",
        "telegraph",
        "WARN",
        "Suspect pattern. Verify it's earned.",
    ),
    (
        r"\bIt had been .{1,30} for years\b",
        "telegraph",
        "WARN",
        "Italicized-significance-for-years pattern. Often a tell.",
    ),
    (
        r"\bthere was something (?:about|off|wrong|strange) (?:about )?(?:him|her|them|it|the)\b",
        "telegraph",
        "WARN",
        "Generic 'something off' line. Specify what.",
    ),
]

# Mystery-only: suspect clearing too fast.
SUSPECT_CLEAR_PATTERNS = [
    (
        r"""(?:["'“”])(?:You['']re|You are) not the (?:person|one) (?:I[’']m| I am) looking for(?:["'“”])""",
        "fast-clear",
        "WARN",
        "Definitive clearance after one statement. Replace with conditional verification: 'A gallery opening with forty witnesses takes a phone call. I will make the call. Until then, you stay on the list.'",
    ),
    (
        r"""(?:["'“”])All right\.\s*You['']re cleared(?:["'“”])""",
        "fast-clear",
        "FAIL",
        "Cut. Sleuth must do verification work on the page.",
    ),
]


# -----------------------------------------------------------------------------
# Manuscript parsing
# -----------------------------------------------------------------------------

# Accept either "## Chapter N" markdown headings OR "Chapter N" plain headings.
CHAPTER_HEADING_RE = re.compile(
    r"^\s*#{0,4}\s*Chapter\s+(\d+)\b", re.IGNORECASE
)


def split_into_chapters(lines):
    chapters = []
    current_chapter_num = 0
    current_lines = []
    for idx, line in enumerate(lines, start=1):
        m = CHAPTER_HEADING_RE.match(line.strip())
        if m:
            if current_lines:
                chapters.append((current_chapter_num, current_lines))
            current_chapter_num = int(m.group(1))
            current_lines = [(idx, line)]
        else:
            current_lines.append((idx, line))
    if current_lines:
        chapters.append((current_chapter_num, current_lines))
    return chapters


# -----------------------------------------------------------------------------
# Checks
# -----------------------------------------------------------------------------


def find_pattern_hits(lines, patterns):
    hits = []
    for line_no, text in lines:
        for regex, cat, sev, fix in patterns:
            for m in re.finditer(regex, text, flags=re.IGNORECASE):
                snippet = text.strip()
                if len(snippet) > 200:
                    start = max(0, m.start() - 60)
                    end = min(len(text), m.end() + 60)
                    snippet = "..." + text[start:end].strip() + "..."
                hits.append({
                    "line_no": line_no,
                    "snippet": snippet,
                    "category": cat,
                    "severity": sev,
                    "fix": fix,
                    "match": m.group(0),
                })
    return hits


def killer_name_density(chapters, killer_name, suspect_names):
    names = [killer_name] + list(suspect_names)
    table = {}
    for chapter_num, lines in chapters:
        text = " ".join(line for _, line in lines).lower()
        wc = len(re.findall(r"\b\w+\b", text))
        row = {"_word_count": wc}
        for name in names:
            last = name.split()[-1].lower()
            count = len(re.findall(rf"\b{re.escape(last)}\b", text))
            row[name] = count
        table[chapter_num] = row
    return table


def killer_density_audit(table, killer_name, suspects, reveal_chapter):
    warnings = []
    pre_reveal = [c for c in table if 0 < c < reveal_chapter]
    if not pre_reveal:
        return warnings
    for ch in pre_reveal:
        row = table[ch]
        wc = row["_word_count"]
        if wc == 0:
            continue
        killer_count = row.get(killer_name, 0)
        suspect_avg = (
            sum(row.get(s, 0) for s in suspects) / len(suspects)
            if suspects
            else 0
        )
        density = (killer_count / wc) * 1000 if wc else 0
        if (
            killer_count > 0
            and suspect_avg > 0
            and killer_count >= suspect_avg * 2
            and density > 1.5
        ):
            warnings.append({
                "chapter": ch,
                "killer_count": killer_count,
                "suspect_avg": round(suspect_avg, 2),
                "density_per_1k": round(density, 2),
                "verdict": "WARN",
                "note": (
                    f"Antagonist ({killer_name}) named {killer_count}× in Ch {ch} "
                    f"vs avg {suspect_avg:.1f} for other suspects. "
                    f"Density {density:.2f}/1k words. Consider rebalancing."
                ),
            })
    return warnings


# -----------------------------------------------------------------------------
# Report
# -----------------------------------------------------------------------------


def render_report(
    manuscript_path,
    mode,
    killer,
    reveal_chapter,
    suspects,
    flags,
    density_table,
    density_warnings,
    chapter_range=None,
):
    out = []
    out.append("# Manuscript Integrity Report\n")
    out.append(f"**Manuscript:** `{manuscript_path}`  ")
    out.append(f"**Mode:** {mode}  ")
    if chapter_range:
        out.append(f"**Chapters scanned:** {chapter_range}  ")
    if mode == "mystery":
        out.append(f"**Antagonist (under audit):** {killer}  ")
        out.append(f"**Reveal chapter:** {reveal_chapter}  ")
        out.append(f"**Other suspects checked:** {', '.join(suspects) if suspects else '(none)'}  ")
    out.append("")

    # Scorecard
    out.append("## Scorecard\n")

    flv = sum(1 for f in flags if f["category"] == "future-leak" and f["severity"] == "FAIL")
    flw = sum(1 for f in flags if f["category"] == "future-leak" and f["severity"] == "WARN")
    tlv = sum(1 for f in flags if f["category"] == "telegraph" and f["severity"] == "FAIL")
    tlw = sum(1 for f in flags if f["category"] == "telegraph" and f["severity"] == "WARN")
    fcv = sum(1 for f in flags if f["category"] == "fast-clear" and f["severity"] == "FAIL")
    fcw = sum(1 for f in flags if f["category"] == "fast-clear" and f["severity"] == "WARN")
    density_warn = len(density_warnings)

    def verdict(n_fail, n_warn):
        if n_fail > 0:
            return "**FAIL**"
        if n_warn > 0:
            return "**WARN**"
        return "**PASS**"

    out.append("| Dimension | Verdict | FAIL | WARN |")
    out.append("|---|---|---|---|")
    out.append(f"| Future-leak narrator | {verdict(flv, flw)} | {flv} | {flw} |")
    out.append(f"| Telegraphed observation | {verdict(tlv, tlw)} | {tlv} | {tlw} |")
    if mode == "mystery":
        out.append(f"| Suspect-clearing speed | {verdict(fcv, fcw)} | {fcv} | {fcw} |")
        out.append(f"| Antagonist-name density | {verdict(0, density_warn)} | 0 | {density_warn} |")
    out.append("")

    # Line-level flags
    out.append("## Line-level flags\n")
    if not flags:
        out.append("_No structural flags found._\n")
    else:
        for f in sorted(flags, key=lambda f: f["line_no"]):
            out.append(f"### Line {f['line_no']} — {f['category']} ({f['severity']})\n")
            out.append(f"**Match:** `{f['match']}`  ")
            out.append(f"**Snippet:** {f['snippet']}  ")
            out.append(f"**Fix:** {f['fix']}  \n")

    if mode == "mystery" and density_table:
        out.append("## Antagonist-name density per chapter\n")
        out.append("| Ch | Words | " + killer + " | " + " | ".join(suspects) + " |")
        out.append("|---|---|---|" + "---|" * len(suspects))
        for ch in sorted(density_table.keys()):
            row = density_table[ch]
            line = f"| {ch} | {row['_word_count']} | {row.get(killer, 0)} |"
            for s in suspects:
                line += f" {row.get(s, 0)} |"
            out.append(line)
        out.append("")
        if density_warnings:
            out.append("## Density warnings\n")
            for w in density_warnings:
                out.append(f"- {w['note']}")
            out.append("")

    out.append("## Recommended action queue\n")
    if not flags and not density_warnings:
        out.append("_Manuscript passes structural integrity check. Safe to continue._\n")
    else:
        priorities = []
        for f in flags:
            if f["severity"] == "FAIL":
                priorities.append((1, f"Line {f['line_no']}: {f['category']} — {f['match']}"))
        for w in density_warnings:
            priorities.append((2, f"Ch {w['chapter']}: {w['note']}"))
        for f in flags:
            if f["severity"] == "WARN":
                priorities.append((3, f"Line {f['line_no']}: {f['category']} — {f['match']}"))
        priorities.sort(key=lambda x: x[0])
        for prio, msg in priorities:
            label = {1: "P1 (FAIL)", 2: "P2 (DENSITY)", 3: "P3 (WARN)"}[prio]
            out.append(f"- **{label}** — {msg}")
        out.append("")

    return "\n".join(out)


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------


def main():
    p = argparse.ArgumentParser(description="Structural integrity check for fiction manuscripts.")
    p.add_argument("--manuscript", required=True, help="Path to manuscript markdown")
    p.add_argument("--mode", choices=["general", "mystery"], default="general",
                   help="general (any genre) or mystery (adds antagonist density + clear-speed)")
    p.add_argument("--killer", default="", help="Antagonist full name (mystery mode)")
    p.add_argument("--reveal-chapter", type=int, default=12, help="Chapter where reader is meant to commit (mystery mode)")
    p.add_argument("--suspects", default="", help="Comma-separated red-herring suspect names (mystery mode)")
    p.add_argument("--chapters-from", type=int, default=None, help="Optional: only scan chapters >= N")
    p.add_argument("--chapters-to", type=int, default=None, help="Optional: only scan chapters <= N")
    p.add_argument("--output", default=None, help="Write report to this path (default stdout)")
    args = p.parse_args()

    path = Path(args.manuscript)
    if not path.exists():
        print(f"ERROR: manuscript not found: {path}", file=sys.stderr)
        return 1

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    chapters = split_into_chapters(lines)

    # Filter by chapter range if requested
    if args.chapters_from is not None or args.chapters_to is not None:
        lo = args.chapters_from if args.chapters_from is not None else -1
        hi = args.chapters_to if args.chapters_to is not None else 10**9
        chapters = [(c, ls) for c, ls in chapters if lo <= c <= hi]

    chapter_range = None
    if chapters:
        nums = [c for c, _ in chapters if c > 0]
        if nums:
            chapter_range = f"{min(nums)}–{max(nums)}"

    all_flags = []
    pattern_libs = [FUTURE_LEAK_PATTERNS, TELEGRAPH_PATTERNS]
    if args.mode == "mystery":
        pattern_libs.append(SUSPECT_CLEAR_PATTERNS)

    for ch, ch_lines in chapters:
        for lib in pattern_libs:
            for hit in find_pattern_hits(ch_lines, lib):
                hit["chapter"] = ch
                all_flags.append(hit)

    suspects = [s.strip() for s in args.suspects.split(",") if s.strip()]
    density_table = {}
    density_warnings = []
    if args.mode == "mystery" and args.killer:
        density_table = killer_name_density(chapters, args.killer, suspects)
        density_warnings = killer_density_audit(
            density_table, args.killer, suspects, args.reveal_chapter
        )

    report = render_report(
        manuscript_path=str(path),
        mode=args.mode,
        killer=args.killer,
        reveal_chapter=args.reveal_chapter,
        suspects=suspects,
        flags=all_flags,
        density_table=density_table,
        density_warnings=density_warnings,
        chapter_range=chapter_range,
    )

    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
        print(f"Report written to {args.output}")
    else:
        print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
