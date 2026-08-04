#!/usr/bin/env python3
"""Generate notes/talks-index.md and notes/to-verify.md from talk-note frontmatter.

Usage: uv run python scripts/build_index.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TALKS = ROOT / "notes" / "talks"

FOLDER_TITLES = {
    "2026-08-01-plenary": "8/1(六)Plenary",
    "2026-08-01-atlas": "8/1(六)Atlas",
    "2026-08-01-nexus": "8/1(六)Nexus",
    "2026-08-01-compass": "8/1(六)Compass",
    "2026-08-02-plenary": "8/2(日)Plenary",
    "2026-08-02-atlas": "8/2(日)Atlas",
    "2026-08-02-compass": "8/2(日)Compass",
}

TYPE_ORDER = {"misc": 0, "keynote": 1, "talk": 2, "panel": 3, "fireside": 4, "workshop": 5}


def parse_frontmatter(text: str) -> dict:
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            kv = re.match(r"(\w+):\s*(.*)", line)
            if kv:
                fm[kv.group(1)] = kv.group(2).strip().strip('"')
    return fm


def extract_to_verify(text: str) -> list[str]:
    m = re.search(r"^## 待確認 / To Verify\s*\n(.*?)(?=\n## |\Z)", text, re.S | re.M)
    if not m:
        return []
    items = [
        line.lstrip("- ").strip()
        for line in m.group(1).splitlines()
        if line.strip().startswith("-")
    ]
    return [i for i in items if i and not i.startswith("(") and "無" != i]


def start_seconds(fm: dict) -> int:
    r = fm.get("video_range", "")
    m = re.match(r"(\d{2}):(\d{2}):(\d{2})", r)
    if m:
        h, mi, s = (int(x) for x in m.groups())
        return h * 3600 + mi * 60 + s
    return 10**9


index_lines = [
    "# 演講筆記索引 / Talk Notes Index",
    "",
    "依日期與舞台分組,依直播內時間排序。/ Grouped by day & stage, ordered by stream time.",
    "",
]
verify_lines = [
    "# 待確認彙整 / Consolidated To-Verify List",
    "",
    "彙整自各筆記的「待確認 / To Verify」段落;確認後請同步更新原筆記。",
    "Aggregated from each note's To-Verify section; update the source note once resolved.",
    "",
]

total = 0
verify_total = 0
for folder in sorted(TALKS.iterdir()):
    if not folder.is_dir():
        continue
    entries = []
    for f in sorted(folder.glob("*.md")):
        text = f.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        entries.append((start_seconds(fm), fm, f, extract_to_verify(text)))
    entries.sort(key=lambda e: (e[0], TYPE_ORDER.get(e[1].get("type", "talk"), 9)))

    title = FOLDER_TITLES.get(folder.name, folder.name)
    index_lines += [f"## {title}", "", "| 時間 Time | 類型 Type | 講者 Speaker | 標題 Title | 筆記 Note |", "|---|---|---|---|---|"]
    verify_section = []
    for sec, fm, f, verifies in entries:
        total += 1
        t = fm.get("video_range", "?").split("–")[0]
        rel = f"{folder.name}/{f.name}"
        index_lines.append(
            f"| {t} | {fm.get('type','?')} | {fm.get('speaker','?')} | {fm.get('title','?')} | [{f.stem.split('--')[0]}]({rel}) |"
        )
        for v in verifies:
            verify_section.append(f"- [{fm.get('speaker','?')} — {fm.get('title','?')}]({'talks/' + rel}):{v if v.startswith(' ') else ' ' + v}")
            verify_total += 1
    index_lines.append("")
    if verify_section:
        verify_lines += [f"## {title}", ""] + verify_section + [""]

index_lines.append(f"共 {total} 篇 / {total} notes in total.")
verify_lines.append(f"共 {verify_total} 項 / {verify_total} items in total.")

(ROOT / "notes" / "talks-index.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
(ROOT / "notes" / "to-verify.md").write_text("\n".join(verify_lines) + "\n", encoding="utf-8")
print(f"talks-index.md: {total} notes; to-verify.md: {verify_total} items")
