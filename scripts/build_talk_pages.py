#!/usr/bin/env python3
"""Generate one static in-site page per talk note: talk/<page>/<slug>.html.

Converts each note's full markdown (中文筆記 + English Notes + shared tables)
to HTML at build time. Pages share the site chrome via <base href="../../">.

Usage: uv run --with markdown python scripts/build_talk_pages.py
"""
import html
import re
import shutil
import sys
from pathlib import Path

import markdown

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_site_data as bsd  # noqa: E402  (reuse parsers + page config)

ROOT = Path(__file__).resolve().parent.parent
TALKS = ROOT / "notes" / "talks"
OUTROOT = ROOT / "talk"
BASE_URL = "https://berkeley-agentic-ai-summit-2026.peteraim.com/"
GA4_ID = "G-METBF91HYQ"
SITE_EN = "Agentic AI Summit ’26 Notes"

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
           "%3Crect width='64' height='64' rx='14' fill='%23003262'/%3E"
           "%3Ccircle cx='32' cy='36' r='13' fill='none' stroke='%23FDB515' stroke-width='6'/%3E"
           "%3Crect x='41' y='20' width='6' height='30' rx='3' fill='%23FDB515'/%3E%3C/svg%3E")

TYPE_LABELS = {
    "keynote": ("Keynote", "主題演講"), "talk": ("Talk", "演講"),
    "panel": ("Panel", "座談"), "workshop": ("Workshop", "工作坊"),
    "fireside": ("Fireside", "爐邊對談"), "misc": ("Session", "其他"),
}

MD = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists"])


def md_html(text):
    MD.reset()
    return MD.convert(text.strip())


def bi(en, zh):
    """Bilingual span pair toggled by html[data-lang]."""
    return ('<span class="lang-en">' + en + '</span>'
            '<span class="lang-zh">' + zh + '</span>')


def split_body(text):
    body = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
    i_zh = body.find("\n## 中文筆記")
    i_en = body.find("\n## English Notes")
    if i_zh == -1 or i_en == -1:
        return "", "", ""
    after = body.find("\n## ", i_en + 5)
    zh = re.sub(r"^\s*## 中文筆記\s*\n", "", body[i_zh:i_en].strip("\n"), count=1)
    en_end = after if after != -1 else len(body)
    en = re.sub(r"^\s*## English Notes\s*\n", "", body[i_en:en_end].strip("\n"), count=1)
    shared = body[after:].strip("\n") if after != -1 else ""
    return zh, en, shared


def build_page(tk, day_page, path):
    a = html.escape
    title_en, title_zh = tk["title"]["en"], tk["title"]["zh"]
    ty_en, ty_zh = TYPE_LABELS.get(tk["type"], TYPE_LABELS["misc"])
    half_en = "morning stream" if tk["half"] == "am" else "afternoon stream"
    half_zh = "上午場直播" if tk["half"] == "am" else "下午場直播"
    day_en, day_zh = day_page["day"]["en"], day_page["day"]["zh"]
    back_en, back_zh = day_page["title"]["en"], day_page["title"]["zh"]
    desc = (tk["summary"]["en"][:197] + "…") if len(tk["summary"]["en"]) > 200 else tk["summary"]["en"]
    canonical = f"{BASE_URL}talk/{day_page['slug']}/{path.stem}.html"

    zh_md, en_md, shared_md = split_body(path.read_text(encoding="utf-8"))
    zh_html = md_html(zh_md) if zh_md else ""
    en_html = md_html(en_md) if en_md else ""
    shared_html = md_html(shared_md) if shared_md else ""

    doc_title = f"{title_en} · {SITE_EN}"
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8" />
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', '{GA4_ID}');
  </script>
  <script>try{{document.documentElement.dataset.lang=localStorage.getItem("lang")||"en";}}catch(e){{document.documentElement.dataset.lang="en";}}</script>
  <base href="../../" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
  <title>{a(doc_title)}</title>
  <meta name="description" content="{a(desc)}" />
  <meta name="theme-color" content="#FAF8F3" />
  <link rel="canonical" href="{a(canonical)}" />
  <link rel="icon" href="{FAVICON}" />
  <meta property="og:type" content="article" />
  <meta property="og:title" content="{a(doc_title)}" />
  <meta property="og:description" content="{a(desc)}" />
  <meta property="og:url" content="{a(canonical)}" />
  <meta property="og:site_name" content="{a(SITE_EN)}" />
  <meta name="twitter:card" content="summary" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400..700;1,400..700&family=Newsreader:ital,opsz,wght@0,6..72,400..700;1,6..72,400..600&family=Noto+Sans+TC:wght@400;500;700&family=Noto+Serif+TC:wght@500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,400,0,0&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="assets/styles.css" />
</head>
<body data-page="{a(day_page['slug'])}" data-talk="{a(tk['slug'])}">
  <main id="page">
    <article class="talkdoc" id="talkdoc" data-item
             data-title-en="{a(title_en)}" data-title-zh="{a(title_zh)}">
      <header class="talkdoc__head">
        <p class="dialog__kicker">
          <span class="badge badge--{a(tk['type'])}">{bi(a(ty_en), a(ty_zh))}</span>
          <span class="dialog__session">{a(tk['session'])}</span>
        </p>
        <h1 class="talkdoc__title">{bi(a(title_en), a(title_zh))}</h1>
        <p class="dialog__speaker"><strong>{a(tk['speaker'])}</strong>{(" — " + a(tk['affiliation'])) if tk['affiliation'] else ""}</p>
        <p class="dialog__meta">{bi(a(day_en), a(day_zh))} · {a(day_page['stage'])} Stage · {a(tk['range'])} · {bi(a(half_en), a(half_zh))}</p>
        <div class="dialog__actions">
          <a class="btn-primary" href="{a(tk['video'])}" target="_blank" rel="noopener">
            <span class="material-symbols-rounded" aria-hidden="true">play_arrow</span>
            {bi("Watch from " + a(tk['start']), "從 " + a(tk['start']) + " 開始觀看")}
          </a>
          <a class="btn-ghost" href="{a(day_page['slug'])}.html">
            <span class="material-symbols-rounded" aria-hidden="true">arrow_back</span>
            {bi("Back to " + a(back_en), "回 " + a(back_zh))}
          </a>
        </div>
        <p class="talkdoc__summary">{bi(a(tk['summary']['en']), a(tk['summary']['zh']))}</p>
      </header>
      <div class="talkdoc__body prose">
        <section class="lang-zh">{zh_html}</section>
        <section class="lang-en">{en_html}</section>
        <section class="talkdoc__shared">{shared_html}</section>
      </div>
      <p class="talkdoc__source">
        <a href="{a(tk['note'])}" target="_blank" rel="noopener">{bi("Markdown source on GitHub ↗", "GitHub 上的 Markdown 原始檔 ↗")}</a>
      </p>
    </article>
  </main>

  <script src="data/data.js"></script>
  <script src="assets/shell.js"></script>
  <script src="assets/app.js"></script>
</body>
</html>
"""


def main():
    if OUTROOT.exists():
        shutil.rmtree(OUTROOT)
    count = 0
    for folder, page_slug, stage, title in bsd.PAGES:
        files = sorted((TALKS / folder).glob("*.md"))
        date = folder[:10]
        day_page = {
            "slug": page_slug, "stage": stage, "title": title,
            "day": {"en": "Saturday, August 1" if date.endswith("01") else "Sunday, August 2",
                    "zh": "8 月 1 日(六)" if date.endswith("01") else "8 月 2 日(日)"},
        }
        outdir = OUTROOT / page_slug
        outdir.mkdir(parents=True, exist_ok=True)
        for path in files:
            tk = bsd.parse_note(path, page_slug)
            (outdir / (path.stem + ".html")).write_text(build_page(tk, day_page, path), encoding="utf-8")
            count += 1
    print(f"talk pages written: {count}")


if __name__ == "__main__":
    main()
