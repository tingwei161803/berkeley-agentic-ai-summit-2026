#!/usr/bin/env python3
"""Build data/data.js (window.SITE_META + window.SITE_PAGES) from notes/talks/**.

Usage: uv run python scripts/build_site_data.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TALKS = ROOT / "notes" / "talks"
OUT = ROOT / "data" / "data.js"
REPO = "tingwei161803/berkeley-agentic-ai-summit-2026"
NOTE_BASE = f"https://github.com/{REPO}/blob/main/notes/talks"

PAGES = [
    ("2026-08-01-plenary", "sat-plenary", "Plenary", {"en": "Plenary · Sat", "zh": "Plenary · 週六"}),
    ("2026-08-01-atlas", "sat-atlas", "Atlas", {"en": "Atlas · Sat", "zh": "Atlas · 週六"}),
    ("2026-08-01-nexus", "sat-nexus", "Nexus", {"en": "Nexus · Sat", "zh": "Nexus · 週六"}),
    ("2026-08-01-compass", "sat-compass", "Compass", {"en": "Compass · Sat", "zh": "Compass · 週六"}),
    ("2026-08-02-plenary", "sun-plenary", "Plenary", {"en": "Plenary · Sun", "zh": "Plenary · 週日"}),
    ("2026-08-02-atlas", "sun-atlas", "Atlas", {"en": "Atlas · Sun", "zh": "Atlas · 週日"}),
    ("2026-08-02-compass", "sun-compass", "Compass", {"en": "Compass · Sun", "zh": "Compass · 週日"}),
]

STAGE_ICONS = {"Plenary": "podium", "Atlas": "public", "Nexus": "hub", "Compass": "explore"}

STREAMS = {
    ("sat-plenary", "am"): "gKdeLQd_LIQ", ("sat-plenary", "pm"): "Tcn5Yb2K0h4",
    ("sat-atlas", "am"): "WeriQic-QW0", ("sat-atlas", "pm"): "psPzCQbjCCo",
    ("sat-nexus", "am"): "LB7IkZhEYic", ("sat-nexus", "pm"): "ZIRc3EpzQJs",
    ("sat-compass", "am"): "IBpR4uYftLY", ("sat-compass", "pm"): "AO0RXP-fVZQ",
    ("sun-plenary", "am"): "UdS3iisKhCk", ("sun-plenary", "pm"): "I2PosBXwoPI",
    ("sun-atlas", "am"): "LGW_6P1CMC8", ("sun-atlas", "pm"): "-7AJJLwYW1Q",
    ("sun-compass", "am"): "l8GS08n-25Q", ("sun-compass", "pm"): "1UrriPJRSPU",
}

QUOTE_SOURCES = [  # (path, quote index within the note's Quotes section)
    ("2026-08-01-plenary/dawn-song--towards-building-safe-and-secure-agentic-ai.md", 2),
    ("2026-08-01-atlas/sanja-fidler--world-models-for-physical-ai-simulation.md", 1),
    ("2026-08-01-plenary/fireside--andrew-ng-alfred-lin.md", 0),
    ("2026-08-01-compass/ion-stoica--the-limits-of-ai-coding-agents.md", 0),
]


def parse_frontmatter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            kv = re.match(r"(\w+):\s*(.*)", line)
            if kv:
                v = kv.group(2).strip()
                if v.startswith("[") and v.endswith("]"):
                    fm[kv.group(1)] = [x.strip().strip('"\'') for x in v[1:-1].split(",") if x.strip()]
                else:
                    fm[kv.group(1)] = v.strip('"')
    return fm


def clean_md(s):
    s = re.sub(r"\[\[(.*?)\]\]", r"\1", s)
    s = re.sub(r"\[(.*?)\]\((.*?)\)", r"\1", s)
    s = s.replace("**", "").replace("`", "")
    return s.strip()


def section(text, heading, until=r"\n## "):
    m = re.search(re.escape(heading) + r"\s*\n(.*?)(?=" + until + r"|\Z)", text, re.S)
    return m.group(1) if m else ""


def tldr_bullets(lang_block):
    tl = section(lang_block, "### TL;DR", until=r"\n### ")
    out = []
    for line in tl.splitlines():
        if line.strip().startswith("- "):
            out.append(clean_md(line.strip()[2:]))
    return out


SKIP_HEADINGS = {"TL;DR", "金句", "Quotes", "重點整理", "Key Points"}


def topic_outline(lang_block):
    """Discussion-format notes (panels/firesides/workshops) have no TL;DR —
    use their section headings as a topics outline instead."""
    out = []
    for line in lang_block.splitlines():
        m = re.match(r"###\s+(.*)", line)
        if not m:
            continue
        h = re.sub(r"[((](約|~)?\s*[0-9:：–—~-]+.*?[))]\s*$", "", clean_md(m.group(1))).strip()
        if h and h not in SKIP_HEADINGS:
            out.append(h)
    return out


def one_line(text, marker):
    m = re.search(r"\*\*" + marker + r"\*\*[::]\s*(.+)", text)
    return clean_md(m.group(1)) if m else ""


def hms_to_sec(hms):
    parts = hms.split(":")
    if len(parts) != 3:
        return 10**9
    try:
        h, m, s = (int(x) for x in parts)
        return h * 3600 + m * 60 + s
    except ValueError:
        return 10**9


def parse_note(path, page_slug):
    text = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    zh_block = section(text, "## 中文筆記")
    en_block = section(text, "## English Notes")
    rng = fm.get("video_range", "")
    start = rng.split("–")[0].strip() if rng else ""
    half = "am" if "Morning" in fm.get("transcript", "") else "pm"
    tldr_en, tldr_zh = tldr_bullets(en_block), tldr_bullets(zh_block)
    kind = "tldr"
    if not (tldr_en and tldr_zh):
        tldr_en, tldr_zh = topic_outline(en_block), topic_outline(zh_block)
        kind = "topics"
    return {
        "slug": path.stem,
        "type": fm.get("type", "talk"),
        "half": half,
        "start": start,
        "range": rng,
        "session": fm.get("session", ""),
        "title": {"en": fm.get("title", ""), "zh": fm.get("title_zh", fm.get("title", ""))},
        "speaker": fm.get("speaker", ""),
        "affiliation": fm.get("affiliation", ""),
        "summary": {"en": one_line(text, "One-line summary"), "zh": one_line(text, "一句話總結")},
        "tldr": {"en": tldr_en, "zh": tldr_zh},
        "tldrKind": kind,
        "tags": fm.get("tags", []) if isinstance(fm.get("tags"), list) else [],
        "video": fm.get("video", ""),
        "noteHref": f"talk/{page_slug}/{path.stem}.html",
        "note": f"{NOTE_BASE}/{path.parent.name}/{path.name}",
    }


def extract_quote(rel, idx=0):
    path = TALKS / rel
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    en_q = section(text, "### Quotes", until=r"\n## ")
    zh_q = section(text, "### 金句", until=r"\n## ")

    def nth_quote(block, n):
        found = -1
        lines = block.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("> "):
                found += 1
                if found != n:
                    continue
                quote = clean_md(line[2:])
                gloss = ""
                for j in range(i + 1, len(lines)):
                    nxt = lines[j].strip()
                    if nxt and not nxt.startswith(">"):
                        gloss = clean_md(nxt)
                        break
                return quote, gloss
        return None, None

    q_en, g_en = nth_quote(en_q, idx)
    _, g_zh = nth_quote(zh_q, idx)
    if not q_en:
        q_en, g_en = nth_quote(en_q, 0)
        _, g_zh = nth_quote(zh_q, 0)
    if not q_en:
        return None
    q_en = re.sub(r"\s*[((]~?\s*[0-9:：–~约約]+\s*[))]\s*$", "", q_en)
    q_en = q_en.strip().strip('"“”').strip()
    affil_short = fm.get("affiliation", "").split(";")[0].split(",")[0].strip()
    return {
        "text": q_en,
        "speaker": fm.get("speaker", ""),
        "affiliation": affil_short,
        "gloss": {"en": g_en or "", "zh": g_zh or ""},
    }


def main():
    site_pages = []
    day_groups = {"2026-08-01": [], "2026-08-02": []}
    total = 0

    for folder, slug, stage, title in PAGES:
        files = sorted((TALKS / folder).glob("*.md"))
        talks = [parse_note(p, slug) for p in files]
        talks.sort(key=lambda tk: (tk["half"], hms_to_sec(tk["start"] or "99:99:99")))

        # group consecutive runs sharing the same session label
        sessions = []
        for tk in talks:
            if sessions and sessions[-1]["label"] == tk["session"] and sessions[-1]["half"] == tk["half"]:
                sessions[-1]["talks"].append(tk)
            else:
                sessions.append({"label": tk["session"], "half": tk["half"], "talks": [tk]})

        date = folder[:10]
        vid_am, vid_pm = STREAMS[(slug, "am")], STREAMS[(slug, "pm")]
        entry = {
            "slug": slug,
            "layout": "daypage",
            "icon": STAGE_ICONS[stage],
            "title": title,
            "stage": stage,
            "date": date,
            "day": {"en": "Saturday, August 1" if date.endswith("01") else "Sunday, August 2",
                    "zh": "8 月 1 日(六)" if date.endswith("01") else "8 月 2 日(日)"},
            "streams": {
                "am": f"https://www.youtube.com/watch?v={vid_am}",
                "pm": f"https://www.youtube.com/watch?v={vid_pm}",
            },
            "sessions": sessions,
            "count": len(talks),
        }
        site_pages.append(entry)
        day_groups[date].append({"slug": slug, "stage": stage, "count": len(talks),
                                 "sessions": len(sessions)})
        total += len(talks)

        # validation
        slugs = [tk["slug"] for tk in talks]
        assert len(slugs) == len(set(slugs)), f"duplicate slug in {folder}"
        for tk in talks:
            assert tk["summary"]["en"] and tk["summary"]["zh"], f"missing summary: {folder}/{tk['slug']}"
            assert tk["tldr"]["en"] and tk["tldr"]["zh"], f"missing tldr: {folder}/{tk['slug']}"

    quotes = [q for q in (extract_quote(r, i) for r, i in QUOTE_SOURCES) if q]

    hub = {
        "slug": "home",
        "layout": "hub",
        "icon": "home",
        "title": {"en": "Overview", "zh": "總覽"},
        "hero": {
            "kicker": {"en": "Field notes · August 1–2, 2026 · UC Berkeley",
                       "zh": "重點筆記 · 2026 年 8 月 1–2 日 · UC Berkeley"},
            "heading": {"en": "Agentic AI Summit 2026, distilled.",
                        "zh": "Agentic AI Summit 2026 重點整理"},
            "lede": {"en": "Bilingual notes on every talk, panel and workshop from Berkeley RDI's two-day summit — 147 sessions across four stages, each with a TL;DR, key takeaways and a time-stamped link into the livestream.",
                     "zh": "Berkeley RDI 兩天峰會的完整筆記:四個舞台、147 場演講/座談/工作坊,每場都有一句話總結、TL;DR 重點與可直接跳轉的直播時間戳連結,中英雙語對照。"},
        },
        "stats": [
            {"value": str(total), "label": {"en": "Talk notes", "zh": "篇演講筆記"}},
            {"value": "4", "label": {"en": "Stages", "zh": "個舞台"}},
            {"value": "14", "label": {"en": "Livestreams", "zh": "場直播"}},
            {"value": "2", "label": {"en": "Days", "zh": "天議程"}},
        ],
        "days": [
            {"key": "2026-08-01", "label": {"en": "Saturday · August 1", "zh": "8 月 1 日(六)"},
             "pages": day_groups["2026-08-01"]},
            {"key": "2026-08-02", "label": {"en": "Sunday · August 2", "zh": "8 月 2 日(日)"},
             "pages": day_groups["2026-08-02"]},
        ],
        "quotes": quotes,
        "about": {
            "heading": {"en": "About these notes", "zh": "關於這份筆記"},
            "body": {
                "en": [
                    "The Agentic AI Summit 2026 was hosted by Berkeley RDI (Center for Responsible, Decentralized Intelligence) on the UC Berkeley campus, August 1–2, 2026 — around 5,000 in-person attendees plus a global livestream, spanning foundation models, agent frameworks, evaluation, infrastructure and safety.",
                    "These notes were compiled from the official livestream recordings and their auto-generated transcripts, then cross-checked against the official agenda. Speaker names, titles and affiliations follow the official program; proper nouns that could not be verified are tracked in an open to-verify list rather than guessed.",
                    "This is an unofficial, non-commercial study resource. Notes may contain transcription errors — always refer to the original recordings for exact wording. Full notes, source transcripts and the to-verify list live in the GitHub repository.",
                ],
                "zh": [
                    "Agentic AI Summit 2026 由 Berkeley RDI(Center for Responsible, Decentralized Intelligence)主辦,2026 年 8 月 1–2 日於 UC Berkeley 校園舉行——約五千名現場參加者加上全球直播,主題橫跨 foundation models、agent frameworks、評估、基礎設施與安全。",
                    "筆記整理自官方直播錄影與其自動字幕逐字稿,並逐場比對官方議程;講者姓名、職稱與單位以官方議程為準,無法查證的專有名詞列入公開的待確認清單,而非逕行猜測。",
                    "本站為非官方、非商業的學習資源,內容可能含有轉錄誤差,精確措辭請以原始錄影為準。完整筆記、原始逐字稿與待確認清單都在 GitHub repository。",
                ],
            },
            "links": [
                {"href": f"https://github.com/{REPO}", "label": {"en": "GitHub repository", "zh": "GitHub repository"}},
                {"href": f"https://github.com/{REPO}/blob/main/notes/talks-index.md", "label": {"en": "Full notes index", "zh": "筆記完整索引"}},
                {"href": f"https://github.com/{REPO}/blob/main/notes/to-verify.md", "label": {"en": "To-verify list", "zh": "待確認清單"}},
                {"href": "https://rdi.berkeley.edu/events/agentic-ai-summit-2026", "label": {"en": "Official event page", "zh": "官方活動頁"}},
                {"href": "https://www.youtube.com/@BerkeleyRDI/streams", "label": {"en": "Livestream recordings", "zh": "直播錄影"}},
            ],
        },
    }

    meta = {
        "title": {"en": "Agentic AI Summit ’26 Notes", "zh": "Agentic AI Summit ’26 筆記"},
        "subtitle": {"en": "Bilingual field notes from Berkeley RDI's Agentic AI Summit 2026",
                     "zh": "Berkeley RDI Agentic AI Summit 2026 中英雙語重點筆記"},
        "repo": REPO,
    }

    pages_out = [hub] + site_pages
    js = ("/* Data layer built from notes/talks/ by scripts/build_site_data.py — do not edit by hand. */\n"
          "window.SITE_META = " + json.dumps(meta, ensure_ascii=False) + ";\n"
          "window.SITE_PAGES = " + json.dumps(pages_out, ensure_ascii=False) + ";\n")
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(js, encoding="utf-8")
    print(f"data/data.js written: {total} talks, {len(site_pages)} day pages, {len(quotes)} quotes, {OUT.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
