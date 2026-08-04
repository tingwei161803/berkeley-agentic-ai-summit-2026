# 演講筆記模板 / Talk Notes Template

> 複製以下內容到 `notes/talks/<YYYY-MM-DD>-<stage>/<speaker-slug>--<title-slug>.md`。
> frontmatter 是給未來網頁用的結構化資料,欄位不要改名;內文段落可依演講性質增減。
> 每篇筆記**中英文都要有**:`## 中文筆記` 與 `## English Notes` 兩區塊內容對應,各自獨立可讀。

```markdown
---
title: "英文原標題"
title_zh: "中文翻譯標題"
speaker: "講者姓名"
affiliation: "職稱與單位(照官網議程)"
type: keynote | talk | panel | workshop | fireside | misc
stage: Plenary | Atlas | Nexus | Compass
date: 2026-08-01
session: "Session N: <官網場次名>"
video: "https://www.youtube.com/watch?v=<id>&t=<開始秒數>s"
video_range: "HH:MM:SS–HH:MM:SS"   # 在該場直播中的起訖時間
transcript: "tmp/<逐字稿檔名>.srt"
status: draft | reviewed
tags: [小寫英文, 2-5個]
---

# <中文標題>(<English Title>)

**一句話總結**:用一句話講完這場演講的核心主張。
**One-line summary**: The talk's core claim in one sentence.

## 中文筆記

### TL;DR

- 3–6 個 bullet,每個是一個獨立可帶走的重點。

### 重點整理

(依演講自身的結構分節,每節標題附大約時間戳,方便對照影片)

#### <小節標題>(約 HH:MM)

內文…

### 金句

> 原文引用(約 HH:MM)

中文翻譯或脈絡說明。

## English Notes

### TL;DR

- Same takeaways as the Chinese section, written natively in English (not word-for-word translation).

### Key Points

#### <Section title> (~HH:MM)

...

### Quotes

> Quote (~HH:MM)

Brief context.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|

## 逐字稿勘誤 / Transcript Corrections

(自動字幕聽錯的專有名詞,修正後記錄在此,方便日後全域修正)

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|

## 待確認 / To Verify

- 無法確定的專有名詞或數字 / Proper nouns or figures that need verification.
```

## 撰寫慣例 / Conventions

- **雙語**:中文與英文區塊內容對應但各自獨立成文(英文不是逐句翻譯,要是道地的英文筆記);專案表、勘誤表、待確認為共用區塊,放檔案最後。
- **語言**:中文區塊內的技術名詞、專案名、標題保留英文原文。
- **篇幅與演講長度成正比**:20 分鐘 keynote 用完整模板;10 分鐘 featured talk 精簡(TL;DR 3 條、重點 2–3 節);panel / fireside / workshop 用討論式格式(主題 → 各講者立場),不必硬套演講結構。
- **時間戳**:使用該場直播影片內的時間(與 SRT 一致),格式 `HH:MM` 或 `HH:MM:SS`;精確度到分鐘即可,金句盡量精確。
- **專有名詞驗證(重要)**:人名、職稱、單位一律以官網議程為準,不可信自動字幕;專案/論文名不確定時先查證(web search),查不到的放「待確認」,**絕不硬猜**。
- **勘誤**:自動字幕人名/專有名詞錯誤率高,確定的修正寫進勘誤表;不確定的放「待確認」。
- **忠實原則**:筆記只寫講者實際說的內容;自己的延伸想法若要寫,放在最後獨立的「我的想法 / My Thoughts」一節,明確區隔。
