# Agentic AI Summit ’26 Notes

> Berkeley RDI「Agentic AI Summit 2026」全部 147 場演講的中英雙語重點筆記網站——每場都有一句話總結、TL;DR 與可直接跳轉的直播時間戳連結。

2026 年 8 月 1–2 日,Berkeley RDI 在 UC Berkeley 校園舉辦了兩天的 Agentic AI Summit(四個舞台、14 場直播、約五千名現場參加者)。本專案把全部直播的自動字幕逐字稿逐場整理成結構化的雙語筆記,並做成可瀏覽、可搜尋、可分享的靜態網站。

---

## 🔗 線上版 / Live

| | |
|---|---|
| 🌐 網站 | <https://berkeley-agentic-ai-summit-2026.peteraim.com/> |

> 直接點進去就能用,無需安裝。各場次頁可用 `#<slug>` 深連結到特定演講,例如 [`sat-plenary.html#dawn-song--towards-building-safe-and-secure-agentic-ai`](https://berkeley-agentic-ai-summit-2026.peteraim.com/sat-plenary.html#dawn-song--towards-building-safe-and-secure-agentic-ai)。

---

## ✨ 功能特色

- 🌏 **雙語切換** — 中文 / English 一鍵全頁切換
- 🌗 **深色 / 淺色模式** — 手動切換並記憶偏好
- 🔍 **即時搜尋** — 在各場次頁輸入關鍵字立即過濾演講
- 🏷️ **類型篩選** — 依 keynote / talk / panel / workshop / fireside 快速篩選
- ⏱️ **時間戳直達** — 每場演講一鍵跳到 YouTube 直播的對應秒數
- 🔗 **深連結** — 每場演講都有專屬 `#<slug>`,可直接分享
- 📱 **響應式設計** — 手機、平板、桌機皆適配
- ⚡ **純靜態** — 無後端、零 build、載入快

---

## 📂 內容結構 / 資料來源

本站內容整理自 **Berkeley RDI Agentic AI Summit 2026 官方直播錄影的自動字幕逐字稿**,並逐場比對[官方議程](https://rdi.berkeley.edu/events/agentic-ai-summit-2026)驗證講者姓名、職稱與講題;無法查證的專有名詞收錄於[待確認清單](notes/to-verify.md),不做臆測。

```
berkeley-agentic-ai-summit-2026/
├── index.html            # 網站入口(總覽頁)
├── sat-*.html sun-*.html # 7 個場次日子頁(週六/週日 × 舞台)
├── assets/               # styles.css(編輯風設計)、shell.js(共用 chrome)、app.js(頁面引擎)
├── data/data.js          # 網站資料層(由筆記自動產生)
├── notes/
│   ├── overview.md       # 活動總覽:議程、影片/逐字稿對照表、整理進度
│   ├── talks-index.md    # 147 篇筆記索引(自動產生)
│   ├── to-verify.md      # 待確認事項彙整(自動產生)
│   ├── TEMPLATE.md       # 筆記模板與撰寫慣例(中英雙語)
│   └── talks/            # 147 篇雙語演講筆記,依 <日期>-<舞台> 分資料夾
├── scripts/
│   ├── srt_to_text.py        # SRT 字幕 → 可讀逐字稿(含時間戳)
│   ├── build_index.py        # 重新產生 talks-index.md 與 to-verify.md
│   ├── build_site_data.py    # 筆記 → data/data.js(網站資料層)
│   └── build_html_pages.py   # 產生 8 個 HTML 進入點
└── tmp/                  # 原始素材:14 場直播的自動字幕逐字稿
```

> ⚠️ **非官方**:本站為個人整理之非官方學習資源,內容整理自官方直播的自動字幕,可能含有轉錄誤差;精確措辭請以[官方錄影](https://www.youtube.com/@BerkeleyRDI/streams)為準,如有出入以官方來源為準。

---

## 🛠 本機使用

```bash
# 1. clone 專案
git clone https://github.com/tingwei161803/berkeley-agentic-ai-summit-2026.git
cd berkeley-agentic-ai-summit-2026

# 2. 啟動本機伺服器(建議,深連結才正常)
uv run python -m http.server 4173
# 然後瀏覽 http://localhost:4173
```

> 本專案為純靜態網站,不需安裝任何依賴。

### 更新筆記後重建網站資料

```bash
uv run python scripts/build_site_data.py   # 筆記 → data/data.js
uv run python scripts/build_index.py       # 重建筆記索引與待確認清單
```

---

## 📝 聲明 / License

- 本站為非官方整理,演講內容著作權歸原講者與 Berkeley RDI 所有。
- 本站使用 Google Analytics(GA4 property:Berkeley Agentic AI Summit 2026 Notes)蒐集匿名流量數據。
- 網站視覺為原創設計,設計過程參考了 [StyleKit](https://www.stylekit.top/en/styles) 與 [SiteInspire](https://www.siteinspire.com/) 的編輯風版面語彙。
- 程式碼以 MIT 授權釋出。
- 如為權利人且希望調整或移除內容,請開 issue 聯絡。
