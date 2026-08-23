#!/usr/bin/env python3
"""Generate the static talk-note pages — one file per talk per language.

Each language gets its own URL, so each file holds one language only:

    talk/<page>/<slug>.html            English  (site root)
    zh-Hant/talk/<page>/<slug>.html    中文

Both files of a pair carry the same three hreflang lines, a canonical that
points at themselves, and a plain link to the other language, so a crawler can
find both without running any JavaScript.

The "Projects & Resources / Transcript Corrections / To Verify" tables at the
foot of every note are a shared bilingual appendix in the source markdown —
they are reference rows (proper nouns, model names, timestamps), not a second
translation of the prose, so both languages keep them as they are.

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
ZH_DIR = "zh-Hant"
ZH_OUTROOT = ROOT / ZH_DIR / "talk"
BASE_URL = "https://berkeley-agentic-ai-summit-2026.peteraim.com/"
GA4_ID = "G-METBF91HYQ"
SITE_TITLE = {"en": "Agentic AI Summit ’26 Notes", "zh": "Agentic AI Summit ’26 筆記"}
HTML_LANG = {"en": "en", "zh": "zh-Hant"}
ALT_LABEL = {"en": "English version", "zh": "中文版"}

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


def clip(text):
    return (text[:197] + "…") if len(text) > 200 else text


def build_page(tk, day_page, path, lang):
    a = html.escape
    other = "zh" if lang == "en" else "en"
    rel = f"talk/{day_page['slug']}/{path.stem}.html"
    # 中文版多一層目錄,共用資產要再往上爬一層
    up = "../../" if lang == "en" else "../../../"
    urls = {"en": BASE_URL + rel, "zh": BASE_URL + ZH_DIR + "/" + rel}
    paths = {"en": "/" + rel, "zh": "/" + ZH_DIR + "/" + rel}

    title = f"{tk['title'][lang]} · {SITE_TITLE[lang]}"
    desc = clip(tk["summary"][lang])
    ty = TYPE_LABELS.get(tk["type"], TYPE_LABELS["misc"])[0 if lang == "en" else 1]
    half = {"en": "morning stream" if tk["half"] == "am" else "afternoon stream",
            "zh": "上午場直播" if tk["half"] == "am" else "下午場直播"}[lang]
    day = day_page["day"][lang]
    back = ("Back to " if lang == "en" else "回 ") + day_page["title"][lang]
    watch = (f"Watch from {tk['start']}" if lang == "en"
             else f"從 {tk['start']} 開始觀看")
    source = ("Markdown source on GitHub ↗" if lang == "en"
              else "GitHub 上的 Markdown 原始檔 ↗")

    zh_md, en_md, shared_md = split_body(path.read_text(encoding="utf-8"))
    notes_md = zh_md if lang == "zh" else en_md
    notes_html = md_html(notes_md) if notes_md else ""
    shared_html = md_html(shared_md) if shared_md else ""

    alt = (f'<p class="lang-alt-link" style="text-align:center;padding:12px;">'
           f'<a href="{paths[other]}" hreflang="{HTML_LANG[other]}" rel="alternate" '
           f'lang="{HTML_LANG[other]}">{ALT_LABEL[other]}</a></p>')

    return f"""<!DOCTYPE html>
<html lang="{HTML_LANG[lang]}" data-theme="light">
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
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
  <title>{a(title)}</title>
  <meta name="description" content="{a(desc)}" />
  <meta name="theme-color" content="#FAF8F3" />
  <link rel="canonical" href="{a(urls[lang])}" />
  <link rel="alternate" hreflang="en" href="{a(urls['en'])}" />
  <link rel="alternate" hreflang="zh-Hant" href="{a(urls['zh'])}" />
  <link rel="alternate" hreflang="x-default" href="{a(urls['en'])}" />
  <link rel="icon" href="{FAVICON}" />
  <meta property="og:type" content="article" />
  <meta property="og:title" content="{a(title)}" />
  <meta property="og:description" content="{a(desc)}" />
  <meta property="og:url" content="{a(urls[lang])}" />
  <meta property="og:site_name" content="{a(SITE_TITLE[lang])}" />
  <meta name="twitter:card" content="summary" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400..700;1,400..700&family=Newsreader:ital,opsz,wght@0,6..72,400..700;1,6..72,400..600&family=Noto+Sans+TC:wght@400;500;700&family=Noto+Serif+TC:wght@500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,400,0,0&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{up}assets/styles.css" />
</head>
<body data-page="{a(day_page['slug'])}" data-talk="{a(tk['slug'])}">
  <main id="page">
    <article class="talkdoc" id="talkdoc" data-item>
      <header class="talkdoc__head">
        <p class="dialog__kicker">
          <span class="badge badge--{a(tk['type'])}">{a(ty)}</span>
          <span class="dialog__session">{a(tk['session'])}</span>
        </p>
        <h1 class="talkdoc__title">{a(tk['title'][lang])}</h1>
        <p class="dialog__speaker"><strong>{a(tk['speaker'])}</strong>{(" — " + a(tk['affiliation'])) if tk['affiliation'] else ""}</p>
        <p class="dialog__meta">{a(day)} · {a(day_page['stage'])} Stage · {a(tk['range'])} · {a(half)}</p>
        <div class="dialog__actions">
          <a class="btn-primary" href="{a(tk['video'])}" target="_blank" rel="noopener">
            <span class="material-symbols-rounded" aria-hidden="true">play_arrow</span>
            {a(watch)}
          </a>
          <a class="btn-ghost" href="../../{a(day_page['slug'])}.html">
            <span class="material-symbols-rounded" aria-hidden="true">arrow_back</span>
            {a(back)}
          </a>
        </div>
        <p class="talkdoc__summary">{a(tk['summary'][lang])}</p>
      </header>
      <div class="talkdoc__body prose">
        <section class="talkdoc__notes">{notes_html}</section>
        <section class="talkdoc__shared">{shared_html}</section>
      </div>
      <p class="talkdoc__source">
        <a href="{a(tk['note'])}" target="_blank" rel="noopener">{a(source)}</a>
      </p>
    </article>
  </main>

  <script src="{up}data/data.js"></script>
  <script src="{up}assets/shell.js"></script>
  <script src="{up}assets/app.js"></script>
{alt}
</body>
</html>
"""


def main():
    for out in (OUTROOT, ZH_OUTROOT):
        if out.exists():
            shutil.rmtree(out)
    count = 0
    for folder, page_slug, stage, title in bsd.PAGES:
        files = sorted((TALKS / folder).glob("*.md"))
        date = folder[:10]
        day_page = {
            "slug": page_slug, "stage": stage, "title": title,
            "day": {"en": "Saturday, August 1" if date.endswith("01") else "Sunday, August 2",
                    "zh": "8 月 1 日(六)" if date.endswith("01") else "8 月 2 日(日)"},
        }
        for lang, root in (("en", OUTROOT), ("zh", ZH_OUTROOT)):
            outdir = root / page_slug
            outdir.mkdir(parents=True, exist_ok=True)
            for path in files:
                tk = bsd.parse_note(path, page_slug)
                (outdir / (path.stem + ".html")).write_text(
                    build_page(tk, day_page, path, lang), encoding="utf-8")
                count += 1
    print(f"talk pages written: {count}")


if __name__ == "__main__":
    main()
