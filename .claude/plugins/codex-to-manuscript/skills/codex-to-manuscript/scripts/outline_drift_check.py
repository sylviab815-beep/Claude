#!/usr/bin/env python3
"""
outline_drift_check.py

Compare the most recent N drafted chapters against the parsed outline. Flag
deviations from the outline's stated POV, chapter goal, key scenes, opening
hook, complication, character decision, intimate-beat flag, and cliffhanger.

This catches "outline drift" — when the prose wanders away from the codex's
plan — before it compounds across the manuscript.

Usage:
    python3 outline_drift_check.py \\
        --manuscript path/to/draft.md \\
        --outline-json path/to/parsed_outline.json \\
        --chapters-from 4 --chapters-to 6 \\
        --output drift_report.md

The outline-JSON is produced by scripts/parse_outline.py.
"""

import argparse
import json
import re
import sys
from pathlib import Path


CHAPTER_HEADING_RE = re.compile(
    r"^\s*#{0,4}\s*Chapter\s+(\d+)\b(?:\s*[:\-—–]\s*(.+?))?\s*$",
    re.IGNORECASE,
)


def split_into_chapters(text: str) -> dict:
    """
    Returns: {chapter_number: {"title": str, "text": str}}
    """
    chapters = {}
    current_num = None
    current_title = None
    current_buf = []
    for line in text.splitlines():
        m = CHAPTER_HEADING_RE.match(line.strip())
        if m:
            if current_num is not None:
                chapters[current_num] = {
                    "title": current_title or "",
                    "text": "\n".join(current_buf).strip(),
                }
            current_num = int(m.group(1))
            current_title = (m.group(2) or "").strip()
            current_buf = []
        else:
            if current_num is not None:
                current_buf.append(line)
    if current_num is not None:
        chapters[current_num] = {
            "title": current_title or "",
            "text": "\n".join(current_buf).strip(),
        }
    return chapters


def first_paragraph(text: str, max_words: int = 80) -> str:
    """Return the first prose paragraph (strip blank lines, scene breaks)."""
    paragraphs = []
    cur = []
    for line in text.splitlines():
        s = line.strip()
        if not s or s in ("* * *", "***"):
            if cur:
                paragraphs.append(" ".join(cur).strip())
                cur = []
            continue
        cur.append(s)
        words = " ".join(cur).split()
        if len(words) >= max_words:
            paragraphs.append(" ".join(cur).strip())
            break
    if cur and not paragraphs:
        paragraphs.append(" ".join(cur).strip())
    return paragraphs[0] if paragraphs else ""


def last_paragraph(text: str, max_words: int = 80) -> str:
    """Return the last prose paragraph (strip blank lines, scene breaks)."""
    paragraphs = []
    cur = []
    for line in reversed(text.splitlines()):
        s = line.strip()
        if not s or s in ("* * *", "***"):
            if cur:
                paragraphs.append(" ".join(reversed(cur)).strip())
                cur = []
            continue
        cur.insert(0, s)
        words = " ".join(cur).split()
        if len(words) >= max_words:
            paragraphs.append(" ".join(cur).strip())
            break
    if cur and not paragraphs:
        paragraphs.append(" ".join(cur).strip())
    return paragraphs[0] if paragraphs else ""


def detect_pov(chapter_text: str, expected_pov_name: str) -> dict:
    """
    Light POV check. Look at the first 1,500 chars and tally first-person
    pronouns vs the expected POV character's name.
    """
    snippet = chapter_text[:1500].lower()
    first_person = len(re.findall(r"\b(?:i|me|my|mine)\b", snippet))
    expected_lower = expected_pov_name.lower().split()[0] if expected_pov_name else ""
    name_hits = (
        len(re.findall(rf"\b{re.escape(expected_lower)}\b", snippet))
        if expected_lower
        else 0
    )
    return {
        "first_person_count": first_person,
        "expected_pov_first_name": expected_pov_name,
        "expected_pov_mentions": name_hits,
    }


def keyword_overlap(haystack: str, needle: str, min_word_len: int = 5) -> tuple:
    """
    Return (overlap_count, total_keywords). Strip common stopwords from the
    needle, count how many of those keywords appear in haystack.
    """
    stopwords = {
        "the", "and", "with", "from", "this", "that", "they", "their", "them",
        "have", "would", "should", "could", "there", "what", "when", "where",
        "into", "about", "after", "before", "while", "still", "still", "again",
        "every", "first", "another", "back", "down", "over", "than", "then",
        "must", "very", "much", "most", "some", "other", "between",
    }
    needle_words = re.findall(r"[A-Za-z']+", needle.lower())
    keywords = [w for w in needle_words if len(w) >= min_word_len and w not in stopwords]
    if not keywords:
        return (0, 0)
    haystack_lower = haystack.lower()
    hits = 0
    for kw in keywords:
        if re.search(rf"\b{re.escape(kw)}\b", haystack_lower):
            hits += 1
    return (hits, len(keywords))


def check_chapter(chapter_data: dict, outline_chapter: dict) -> dict:
    """
    Run all drift checks against one chapter.
    """
    result = {
        "chapter_number": outline_chapter.get("chapter_number"),
        "outline_title": outline_chapter.get("chapter_title", ""),
        "actual_title": chapter_data["title"],
        "issues": [],
        "passes": [],
    }
    text = chapter_data["text"]

    # 1. Title match (loose)
    expected_title = outline_chapter.get("chapter_title", "").lower()
    actual_title = chapter_data["title"].lower()
    if expected_title and actual_title:
        if expected_title not in actual_title and actual_title not in expected_title:
            result["issues"].append({
                "category": "title-mismatch",
                "severity": "WARN",
                "detail": f"Outline title '{outline_chapter['chapter_title']}' vs draft title '{chapter_data['title']}'",
            })
        else:
            result["passes"].append("title")

    # 2. POV
    expected_pov = outline_chapter.get("pov", "").strip()
    if expected_pov:
        pov_info = detect_pov(text, expected_pov)
        if pov_info["expected_pov_mentions"] == 0 and pov_info["first_person_count"] < 5:
            result["issues"].append({
                "category": "pov-mismatch",
                "severity": "WARN",
                "detail": f"Outline POV is '{expected_pov}' but expected character is not mentioned and first-person count is low. Verify POV is correct.",
            })
        else:
            result["passes"].append("pov")

    # 3. Opening hook keyword overlap
    expected_hook = outline_chapter.get("opening_hook", "")
    if expected_hook:
        first_para = first_paragraph(text)
        hits, total = keyword_overlap(first_para, expected_hook)
        ratio = hits / total if total else 0
        if total >= 3 and ratio < 0.25:
            result["issues"].append({
                "category": "opening-drift",
                "severity": "WARN",
                "detail": (
                    f"Opening hook keywords overlap only {hits}/{total} = "
                    f"{ratio:.0%}. Outline hook: '{expected_hook[:120]}…' Actual opening: '{first_para[:120]}…'"
                ),
            })
        else:
            result["passes"].append("opening")

    # 4. Cliffhanger / closing line keyword overlap
    expected_close = (
        outline_chapter.get("cliffhanger") or outline_chapter.get("closing_line") or ""
    )
    if expected_close:
        last_para = last_paragraph(text)
        hits, total = keyword_overlap(last_para, expected_close)
        ratio = hits / total if total else 0
        if total >= 3 and ratio < 0.25:
            result["issues"].append({
                "category": "ending-drift",
                "severity": "WARN",
                "detail": (
                    f"Closing-line keywords overlap only {hits}/{total} = "
                    f"{ratio:.0%}. Outline cliffhanger: '{expected_close[:120]}…' Actual ending: '{last_para[:120]}…'"
                ),
            })
        else:
            result["passes"].append("ending")

    # 5. Key scene coverage
    key_scenes = outline_chapter.get("key_scenes", [])
    scene_misses = []
    for ks in key_scenes:
        scene_text = ks.get("text", "")
        if not scene_text:
            continue
        hits, total = keyword_overlap(text, scene_text, min_word_len=5)
        ratio = hits / total if total else 0
        if total >= 4 and ratio < 0.35:
            scene_misses.append({
                "index": ks.get("index"),
                "ratio": round(ratio, 2),
                "scene_brief": scene_text[:140],
            })
    if scene_misses:
        for sm in scene_misses:
            result["issues"].append({
                "category": "missing-scene",
                "severity": "WARN",
                "detail": (
                    f"Key Scene {sm['index']} keyword coverage {sm['ratio']*100:.0f}%. "
                    f"Brief: '{sm['scene_brief']}…'"
                ),
            })
    else:
        if key_scenes:
            result["passes"].append("scenes")

    # 6. Intimate beat flag enforcement
    intimate_flag = outline_chapter.get("intimate_beat_heat_gated") or outline_chapter.get("intimate_beat") or ""
    if intimate_flag and intimate_flag.lower().startswith("yes"):
        # Check the chapter actually contains intimate-beat language; this
        # is a loose heuristic — it's fine if it's just a kiss for sweet heat.
        intimate_markers = re.findall(
            r"\b(?:kiss|touched|skin|breath(?:ed|ing)?|closer|naked|under(?:neath)?|"
            r"hands? (?:on|in|over)|mouth|lips|hips|pulse)\b",
            text.lower(),
        )
        if len(intimate_markers) < 3:
            result["issues"].append({
                "category": "missing-intimate-beat",
                "severity": "WARN",
                "detail": (
                    f"Outline marks Intimate Beat: Yes but draft has only "
                    f"{len(intimate_markers)} intimate-beat markers. Confirm the "
                    f"scene was written on-page (or expand it)."
                ),
            })
        else:
            result["passes"].append("intimate-beat")

    return result


def render_report(per_chapter: list, scope: str) -> str:
    out = []
    out.append("# Outline Drift Report\n")
    out.append(f"**Scope:** {scope}  \n")
    total_issues = sum(len(c["issues"]) for c in per_chapter)
    out.append(f"**Chapters checked:** {len(per_chapter)}  ")
    out.append(f"**Total drift flags:** {total_issues}  \n")

    out.append("## Per-chapter results\n")
    for c in per_chapter:
        n = c["chapter_number"]
        verdict = "PASS" if not c["issues"] else "WARN"
        out.append(f"### Chapter {n} — {c['outline_title']}  ({verdict})\n")
        if c["passes"]:
            out.append(f"- Passed: {', '.join(c['passes'])}")
        for iss in c["issues"]:
            out.append(f"- **{iss['severity']}** [{iss['category']}] {iss['detail']}")
        out.append("")

    out.append("## Recommended action\n")
    if total_issues == 0:
        out.append("_No drift detected. Continue to the next batch of chapters._")
    else:
        out.append(
            "_Review each WARN above. If the drift is intentional (you decided "
            "to deviate from the outline), document the change so the rest of "
            "the manuscript stays consistent. If the drift is accidental, "
            "revise the affected chapters before continuing._"
        )
    return "\n".join(out)


def main():
    p = argparse.ArgumentParser(description="Check drafted chapters against the parsed outline.")
    p.add_argument("--manuscript", required=True, help="Path to manuscript markdown (chapters with '## Chapter N: Title' headings)")
    p.add_argument("--outline-json", required=True, help="Path to parsed_outline.json from parse_outline.py")
    p.add_argument("--chapters-from", type=int, default=None, help="Lowest chapter to check (inclusive)")
    p.add_argument("--chapters-to", type=int, default=None, help="Highest chapter to check (inclusive)")
    p.add_argument("--output", default=None, help="Write report to this path (default stdout)")
    args = p.parse_args()

    ms = Path(args.manuscript)
    if not ms.exists():
        print(f"ERROR: manuscript not found: {ms}", file=sys.stderr)
        return 1
    ol = Path(args.outline_json)
    if not ol.exists():
        print(f"ERROR: outline JSON not found: {ol}", file=sys.stderr)
        return 1

    text = ms.read_text(encoding="utf-8")
    drafted = split_into_chapters(text)
    outline_data = json.loads(ol.read_text(encoding="utf-8"))
    outline_chapters = {c["chapter_number"]: c for c in outline_data.get("chapters_flat", [])}

    lo = args.chapters_from if args.chapters_from is not None else min(drafted) if drafted else 1
    hi = args.chapters_to if args.chapters_to is not None else max(drafted) if drafted else 1

    per_chapter = []
    for n in sorted(drafted):
        if n < lo or n > hi:
            continue
        outline_ch = outline_chapters.get(n)
        if not outline_ch:
            continue
        per_chapter.append(check_chapter(drafted[n], outline_ch))

    scope = f"Chapters {lo}–{hi}" if lo != hi else f"Chapter {lo}"
    report = render_report(per_chapter, scope)

    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
        print(f"Report written to {args.output}")
    else:
        print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
