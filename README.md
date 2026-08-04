# berkeley-agentic-ai-summit-2026

整理 [Berkeley Agentic AI Summit 2026](https://rdi.berkeley.edu/events/agentic-ai-summit-2026)(2026/8/1–8/2, UC Berkeley)各場演講的重點筆記,未來預計做成網頁。

## 目錄結構

```
notes/
├── overview.md      # 活動總覽:議程、影片/逐字稿對照表、整理進度
├── talks-index.md   # 全部 147 篇筆記的索引(自動產生)
├── to-verify.md     # 各筆記「待確認」事項彙整(自動產生)
├── TEMPLATE.md      # 演講筆記模板與撰寫慣例(中英雙語)
└── talks/           # 各演講筆記,依 <日期>-<舞台> 分資料夾(147 篇,雙語)
scripts/
├── srt_to_text.py   # SRT 字幕 → 可讀逐字稿(含時間戳)
└── build_index.py   # 重新產生 talks-index.md 與 to-verify.md
tmp/                 # 原始素材:14 場直播的自動字幕逐字稿(未整理)
```

## 快速開始

從 [notes/overview.md](notes/overview.md) 進入,或直接看 [notes/talks-index.md](notes/talks-index.md) 找特定演講;整理流程見 overview 末節「整理流程 / Workflow」。
