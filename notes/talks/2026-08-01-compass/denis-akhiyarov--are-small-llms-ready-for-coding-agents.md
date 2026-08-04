---
title: "Are Small LLMs Ready for Coding Agents?"
title_zh: "小模型準備好當 Coding Agent 了嗎?"
speaker: "Denis Akhiyarov"
affiliation: "Senior Staff AI Scientist, ServiceNow"
type: talk
stage: Compass
date: 2026-08-01
session: "Session 2: Frameworks & Dev Platforms"
video: "https://www.youtube.com/watch?v=AO0RXP-fVZQ&t=2239s"
video_range: "00:37:19–00:43:55"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [small-llms, local-agents, harness, coding-agents, evaluation]
---

# 小模型準備好當 Coding Agent 了嗎?(Are Small LLMs Ready for Coding Agents?)

**一句話總結**:把 harness 縮到一個檔案、把 context 壓到最小、每次只做一個小動作並立刻驗證,本機小模型確實能完成大部分真實 coding 任務——**卡住的地方不是寫程式,而是自我驗證那一段閉環**。
**One-line summary**: Shrink the harness to a single file, minimize context, take one tiny action at a time and verify it immediately — and a local small LLM really can do most of a realistic coding task. **What it can't do is close the verification loop.**

## 中文筆記

### TL;DR

- **動機很個人**:一次跨大西洋航班上斷網,他發現「身為 AI 科學家,沒有 coding agent 我效率低得可怕」,於是決定自己寫一個本機 coding agent,測試 MacBook 上跑的本地 LLM 能不能處理真實的 agentic coding 任務。已開源。
- **三個設計原則**:(1) **把傳給小模型的 context 壓到最小**——小模型吃大量 context 表現會壞掉;(2) **一次只做一個很小的動作,並立刻驗證**;(3) **盡量少用 reasoning**,只在出錯後的 recovery loop 才動用。
- **實測結論**:小模型**能完成大部分工作**,但**做不到自我驗證與 observe-fix 的完整閉環**——開發一個 app 功能時「大多數測試會過,但不是全部」;Qwen 3.6 與 Gemma 4 兩個家族都是同樣的故事。
- **定位**:比 Codex / Claude Code 這種大型 code base 輕巧得多;他也拿去和目前最精簡的 harness 以及 OpenHands 比較,結論是**他的更小,專為本機超小模型設計**,仍在 work in progress。

### 重點整理

#### 起點:飛機上沒網路的那幾個小時(約 00:37–00:38)

這是一個很個人的故事。幾個月前他搭跨大西洋航班,意識到**身為 AI 科學家,一旦斷線、沒有 coding agent,自己會變得非常沒效率**。於是他決定寫一個自己的本機 coding agent,看看**跑在 MacBook 上的本地 LLM 到底能不能處理真實的 agentic coding 任務**。這個專案最近才開源,repo 裡也放了這場簡報。

#### 三個設計原則:小、驗證、少想(約 00:38–00:40)

這個 agent「一次只做一件小事」,設計圍繞三個關鍵想法:

1. **最小化傳給小模型的 context**。本機跑的小語言模型在被塞入大量 context 時表現並不好。
2. **一次只做極小的動作,做完立刻驗證**。
3. **盡可能減少 reasoning**,只在**出錯後的 recovery loop** 才啟用。

他舉的例子很具體:給小模型(這裡是 Qwen 3.6)一個 hello world 等級的任務——寫個小程式、編譯、執行。結果失敗了,因為**它把程式編譯進暫存目錄,卻要從另一個目錄執行**。這類事情對小模型來說特別難自己看出來,所以只能把改動切得非常小、逐一驗證。

Harness 本身很簡樸:**一個 minimal loop、就一個檔案**,原本約 1,000 行,現在接近 2,000 行。核心策略是**少做大的 planning 步驟、多走小步,只有出錯時才回頭**。

#### 評估:能寫,但不會自我驗證(約 00:41–00:42)

他跑了數百個測試:

- **Smoke test**:兩個 LLM 家族——**Gemma 4** 與 **Qwen**——基本上都能用,只有一個 Qwen 模型不行。這一步只是確認可用性的 sanity check。
- **真實任務**:替一個 app 開發功能。發現**這些 agent 能完成大部分工作**,但問題出在**它們無法驗證自己的成果**、缺少「觀察發生了什麼 → 回頭修正」的完整閉環。結果就是**大多數測試會過,但不是全部**。Qwen 3.6 與 Gemma 4 都是同樣的模式。
- **一個誠實的但書**:這些評估**其實跑在 OpenRouter 上、不是本機**——因為本機跑會花掉太多時間,而且他的 MacBook 記憶體有限。

#### 定位與比較(約 00:42–00:43)

他的總結是:這是一個**用極簡 harness 在本機跑的小 agent**,證明了**不需要 Codex 或 Claude Code 那樣龐大的 code base**,也能靠很小的 LLM 把事情做起來。他也做了幾個比較:

- 對比目前大家在用的**最精簡 harness**(字幕作 "PI harness"),他說那個**比 Codex 或 Claude Code 有效率得多**。
- 也和 **OpenHands** 做了比較。
- 結論是他這個**比上述兩者都更小**,專門面向本機的超小 LLM。

他強調專案仍是 work in progress、還有很多問題,並在台上直接徵求回饋。

## English Notes

### TL;DR

- **A personal itch**: on a transatlantic flight he realized how unproductive an AI scientist is without a coding agent while offline, so he built his own local coding agent to find out whether a local LLM on a MacBook can handle realistic agentic coding tasks. It's now open source.
- **Three design principles**: (1) **minimize the context** handed to a small LLM, because small local models degrade badly with long context; (2) **take one very small action at a time and verify it immediately**; (3) **minimize reasoning**, using it only in recovery loops when something goes wrong.
- **The finding**: small models **do most of the work**, but **fail at verifying their own work** and closing the observe-then-fix loop. Building an app feature, the agent passes most tests but not all — the same story across Qwen 3.6 and Gemma 4.
- **Positioning**: far lighter than the Codex or Claude Code code bases. He compared against the most minimal harness people use today and against OpenHands, and his is **smaller than both**, aimed squarely at very small local models. Still work in progress.

### Key Points

#### The origin: a few offline hours over the Atlantic (~00:37–00:38)

A personal story. A few months ago on a transatlantic flight he realized that **as an AI scientist he becomes deeply inefficient without a coding agent when disconnected from the internet**. So he set out to build his own local coding agent and see whether a **local LLM running on his MacBook** could handle realistic agentic coding work. He open-sourced it recently; the repo also carries the slides for this talk.

#### Three design principles: small steps, immediate verification, minimal reasoning (~00:38–00:40)

The agent "does one small thing at a time," built around three ideas:

1. **Minimize the context passed to the small LLM** — small local models are not good when you hand them a lot of context.
2. **Take very small actions and verify each one immediately.**
3. **Minimize reasoning**, invoking it only in **recovery loops** when things go wrong.

His worked example: give a small model (Qwen 3.6 here) a hello-world-level task — write a small program, compile it, run it. It failed, because **it compiled into a temporary directory but needed to execute from a different one**. Small models struggle to notice that class of problem, which is exactly why changes must be tiny and verified one at a time.

The harness itself is deliberately spare: a **minimal loop in a single file**, once around 1,000 lines and now closer to 2,000. The strategy is to avoid big planning steps, take smaller ones, and only backtrack when something breaks.

#### Evaluation: it can write code, it can't check itself (~00:41–00:42)

He ran a few hundred tests:

- **Smoke tests** across two model families, **Gemma 4** and **Qwen**: everything works except one Qwen model. This was a sanity check on usability.
- **Realistic tasks**: building a feature for an app. The agents **do most of the work**, but the problem is that they **fail to verify their work** and lack the full observe-what-happened-then-go-back-and-fix loop. The result: most tests pass, but not all. Same story across Qwen 3.6 and Gemma 4.
- **An honest caveat**: for the record, these runs were on **OpenRouter, not locally** — running them locally would take ages, and his MacBook has limited memory.

#### Positioning and comparisons (~00:42–00:43)

His conclusion: a small agent running locally with a minimal harness shows you **don't need a large code base like Codex or Claude Code** to work with a very small LLM. The comparisons he called out:

- The **most minimal harness people currently use** (transcribed as "PI harness"), which he notes is much more efficient than Codex or Claude Code.
- **OpenHands**.
- His is **smaller than both**, targeted at very small local models.

He was explicit that it's still work in progress with plenty of open issues, and asked the room for feedback.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| 他的本機 coding agent(字幕作 "ask me")| 單檔、約 2k 行的極簡 agent loop,為本機小 LLM 設計;近期開源,repo 內含本場簡報 | Single-file, ~2k-line minimal agent loop for local small LLMs; recently open-sourced, slides in the repo | 名稱與 repo 網址待確認 / name and repo URL to verify |
| Qwen 3.6 | 評估用的小模型家族之一 | One of the two small-model families evaluated | 字幕作 "quen 3.6" / "Quinn" |
| Gemma 4 | 評估用的另一個小模型家族 | The other small-model family evaluated | |
| OpenHands | 對照比較的開源 agent harness | Open-source agent harness used as a comparison | |
| OpenRouter | 實際跑評估的推論服務(非本機) | The inference service the evals actually ran on (not local) | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Dennis Akiro | Denis Akhiyarov |
| Service Now | ServiceNow |
| quen / Quinn | Qwen |
| cloth code / codeex | Claude Code / Codex |
| hardness | harness |
| open hands | OpenHands |
| open router | OpenRouter |

## 待確認 / To Verify

- Agent 名稱字幕作 "ask me",repo 名稱與網址待確認(投影片上有連結)。/ The agent's name was transcribed as "ask me"; the repo name and URL need confirming from the slides.
- 他比較的對象 "PI harness"(自稱是目前最精簡的 harness)正確名稱待確認,**不硬猜**。/ The comparison target transcribed as "PI harness" — described as the most minimal harness in current use — needs its real name confirmed.
- 「1,000 行 → 接近 2k 行」是指整個 agent 還是單一 loop 檔案,講者說法是「就一個檔案」,可再確認。/ Whether the ~1k→2k line count covers the whole agent or just the single loop file.
- Gemma 4 / Qwen 3.6 的確切模型版本與參數規模未在台上說明。/ Exact model versions and parameter sizes for Gemma 4 and Qwen 3.6 were not stated.
