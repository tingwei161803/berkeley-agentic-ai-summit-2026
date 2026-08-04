#!/usr/bin/env python3
"""Generate the 8 HTML entry points (index + 7 day pages) with shared head.

Usage: uv run python scripts/build_html_pages.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE_URL = "https://berkeley-agentic-ai-summit-2026.peteraim.com/"
GA4_ID = "G-METBF91HYQ"

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
           "%3Crect width='64' height='64' rx='14' fill='%23003262'/%3E"
           "%3Ccircle cx='32' cy='36' r='13' fill='none' stroke='%23FDB515' stroke-width='6'/%3E"
           "%3Crect x='41' y='20' width='6' height='30' rx='3' fill='%23FDB515'/%3E%3C/svg%3E")

PAGES = [
    ("index", "home", "Agentic AI Summit ’26 Notes",
     "Bilingual field notes on all 147 talks, panels and workshops from Berkeley RDI's Agentic AI Summit 2026 — TL;DRs, key takeaways and time-stamped livestream links."),
    ("digest", "digest", "Daily Digest — Agentic AI Summit ’26 Notes",
     "The two days of the Agentic AI Summit 2026, distilled: recurring themes per day with links to every related talk note."),
    ("sat-plenary", "sat-plenary", "Plenary · Saturday — Agentic AI Summit ’26 Notes",
     "Notes on every Plenary Stage talk from Saturday, August 1 at the Agentic AI Summit 2026."),
    ("sat-atlas", "sat-atlas", "Atlas · Saturday — Agentic AI Summit ’26 Notes",
     "Notes on every Atlas Stage talk from Saturday, August 1 at the Agentic AI Summit 2026."),
    ("sat-nexus", "sat-nexus", "Nexus · Saturday — Agentic AI Summit ’26 Notes",
     "Notes on every Nexus Stage talk from Saturday, August 1 at the Agentic AI Summit 2026."),
    ("sat-compass", "sat-compass", "Compass · Saturday — Agentic AI Summit ’26 Notes",
     "Notes on every Compass Stage talk from Saturday, August 1 at the Agentic AI Summit 2026."),
    ("sun-plenary", "sun-plenary", "Plenary · Sunday — Agentic AI Summit ’26 Notes",
     "Notes on every Plenary Stage talk from Sunday, August 2 at the Agentic AI Summit 2026."),
    ("sun-atlas", "sun-atlas", "Atlas · Sunday — Agentic AI Summit ’26 Notes",
     "Notes on every Atlas Stage talk from Sunday, August 2 at the Agentic AI Summit 2026."),
    ("sun-compass", "sun-compass", "Compass · Sunday — Agentic AI Summit ’26 Notes",
     "Notes on every Compass Stage talk from Sunday, August 2 at the Agentic AI Summit 2026."),
]

JSON_LD = """  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "Agentic AI Summit \\u201926 Notes",
    "url": "%s",
    "description": "Bilingual field notes from Berkeley RDI's Agentic AI Summit 2026.",
    "inLanguage": ["en", "zh-Hant"]
  }
  </script>
""" % BASE_URL


def build(file_slug, page_slug, title, desc):
    canonical = BASE_URL if file_slug == "index" else BASE_URL + file_slug + ".html"
    jsonld = JSON_LD if file_slug == "index" else ""
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
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta name="theme-color" content="#FAF8F3" />
  <link rel="canonical" href="{canonical}" />
  <link rel="icon" href="{FAVICON}" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:site_name" content="Agentic AI Summit ’26 Notes" />
  <meta name="twitter:card" content="summary" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{desc}" />
{jsonld}  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400..700;1,400..700&family=Newsreader:ital,opsz,wght@0,6..72,400..700;1,6..72,400..600&family=Noto+Sans+TC:wght@400;500;700&family=Noto+Serif+TC:wght@500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,400,0,0&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="assets/styles.css" />
</head>
<body data-page="{page_slug}">
  <!-- shell.js injects the app bar, cross-page nav, footer and dialog around this -->
  <main id="page"></main>

  <script src="data/data.js"></script>
  <script src="assets/shell.js"></script>
  <script src="assets/app.js"></script>
</body>
</html>
"""


def main():
    for file_slug, page_slug, title, desc in PAGES:
        out = ROOT / (file_slug + ".html")
        out.write_text(build(file_slug, page_slug, title, desc), encoding="utf-8")
        print("wrote", out.name)


if __name__ == "__main__":
    main()
