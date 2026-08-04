---
title: "Agentic Coding, the Boring Way"
title_zh: "無聊的那條路:agentic coding 的紀律做法"
speaker: "Krishnakumar Sharma"
affiliation: "CEO, Omokai"
type: talk
stage: Nexus
date: 2026-08-01
session: "Session 2: Coding & Web Agents"
video: "https://www.youtube.com/watch?v=ZIRc3EpzQJs&t=2769s"
video_range: "00:46:09–00:54:02"
transcript: "tmp/[English (auto-generated)] Nexus Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [agentic-coding, legacy-systems, enterprise, cost-control, engineering-discipline]
---

# 無聊的那條路:agentic coding 的紀律做法(Agentic Coding, the Boring Way)

**一句話總結**:無節制地堆 agent、堆 loop、堆 token,只會讓錯誤與帳單一起變多;在 legacy 企業環境裡真正可靠的做法很無聊——先做研究產出 artifact、再產出明確計畫、才交給 AI 交付,搭配人類簽核、跨家族多模型交叉驗證,以及不超過四個定義清楚的 agent。
**One-line summary**: Piling on more agents, more loops, and more tokens just multiplies errors and invoices. What actually works in legacy enterprise environments is boring: produce a research artifact, then a well-defined plan, then let AI deliver — with human sign-off, cross-vendor model diversity, and no more than about four clearly scoped agents.

## 中文筆記

### TL;DR

- **我們正處在「agentic hangover」**:他引用 Gartner 的研究指出,用更多 AI 並不等於更高生產力——只是讓 Anthropic 和 OpenAI 更有錢。
- **兩個該破除的迷思**:(1) **agent swarm**——用上百個 agent 解一個問題,結果是成本爆炸加錯誤爆炸;(2) **loop engineering / loop within loop**——同樣是燒錢。
- **成本不會被便宜的模型救回來**:另一份關於 AI 生成程式碼的研究顯示,不受控地使用 AI 會在 production 留下**更多、而且更難根除**的錯誤。
- **真正的隱性成本**是驗證、資安漏洞、除錯,最後是 **cognitive debt 與 burnout**——AI 用太多,人自己會失去 context。
- **解法是 D3 framework**(他 2025 年在 Amazon 開發):**Discover**(產出含上下游依賴的研究 artifact)→ **計畫**(拆成明確 subtask)→ **Deliver**(AI 執行)。再加上人類簽核、**用不同公司(而非同家族)的多個模型**、以及最多約四個定義清楚的 agent。
- **一句帶走**:stop token maxing, start ROI maxing。

### 重點整理

#### 為什麼談 legacy 與「無聊」(約 00:48–00:49)

他先框定範圍:這場談的是**企業的 legacy 系統**。「無聊的做法」是給那些想建**可擴展、安全、可靠**系統的人聽的。

他的資歷:曾任 Amazon Germany 的 head of AI,建過大規模 AI 系統、為 Amazon 帶來數十億美元的營收影響,也做過 robotics AI;現在創辦 Omokai,做 physical AI 作業系統——**把語音轉成機器人與無人機的自主任務**。這場不談 Omokai 的產品,而是談他的工程團隊怎麼解決問題,而且他預告「有些說法會相當有爭議」。

一個有意思的自我定位:Omokai 非常 AI-native——自己微調模型、用 AI 生成資料,**7 名人類員工、10 名以上「AI 員工」**。

#### 診斷:agentic hangover(約 00:50–00:52)

- **生產力悖論**:他引用 Gartner 的研究——用更多 AI 並不會帶來更多生產力,只會讓 Anthropic 和 OpenAI 更有錢。若你在**沒有適當約束**的情況下無節制用 AI,那多半是用錯了。
- **兩個當紅迷思**:
  - **Agent swarm**:動用上百個 agent 解一個問題 → 大量成本 + 大量錯誤。
  - **Loop engineering / loop within loop**:他看到有人在做的巢狀迴圈 → 成本遠超過你想付的。
- **「未來 AI 會很便宜所以成本不重要」也站不住腳**:另一份針對 AI 程式碼生成的研究顯示,不受控的用法會在 production 資料庫留下**更多而且更持久**的錯誤。
- **隱性成本鏈**:驗證成本 → 資安漏洞 → 除錯 → 最後是 **cognitive debt 與 burnout**。他強調這是真實存在的:**AI 用太多,你自己會失去 context**。
- 他放了一張截圖:某人對著網路怒吼,因為受不了某個開源 repo 被 AI slop 淹沒。「我們不想變成那樣。」

#### 解方:D3 framework(約 00:52–00:53)

他在 Amazon 學到的心得是:**framework 與 mechanism** 才是可靠、可擴展系統的關鍵。他 2025 年在 Amazon 開發了一套給 agentic coding 用的 **D3 framework**,三個階段:

1. **Discover**:產出一份**研究 artifact**。這份文件不只涵蓋你的 repository,還要含**上游與下游的依賴**。
2. **計畫**:根據研究文件產出一份**定義非常明確的計畫**,並拆解成 subtask。
3. **Deliver**:AI 拿到上述全部資訊,執行並解決問題。

三個補充原則:

- **不要完全信任 AI**:流程中要有**人類簽核**。
- **模型要跨家族**:解題時使用來自**不同公司**的多個模型,而不是同一家族的變體。
- **不要用太多 agent**:大約四個、且每個定義清楚就好。

**收尾**:如果只帶走一件事——**stop token maxing and start ROI maxing**。

### 金句

> "Using more AI does not lead to more productivity. It just leads to you making Anthropic and OpenAI richer."(約 00:50)

引用 Gartner 研究後的直白總結。

> "If you use AI too much you end up losing a lot of context."(約 00:51)

cognitive debt 的本質:失去 context 的是人,不是模型。

> "Stop token maxing and start ROI maxing."(約 00:53)

整場唯一要求聽眾帶走的一句話。

## English Notes

### TL;DR

- **We're in an "agentic hangover"**: citing Gartner research, using more AI doesn't produce more productivity — it mostly makes Anthropic and OpenAI richer.
- **Two myths to kill**: (1) **agent swarms** — hundreds of agents on one problem, yielding an explosion of both cost and errors; (2) **loop engineering / loops within loops** — same bill, same outcome.
- **Cheap models won't bail you out**: another study on AI code generation shows uncontrolled use leaves **more errors, and more persistent errors**, in production.
- **The real hidden costs** are verification, security holes, debugging, and finally **cognitive debt and burnout** — lean on AI too hard and *you* lose the context.
- **The fix is the D3 framework** (built at Amazon in 2025): **Discover** (a research artifact covering the repo plus upstream and downstream dependencies) → plan (well-defined, broken into subtasks) → **Deliver** (AI executes). Plus human sign-off, multiple models **from different companies** rather than one family, and no more than about four well-scoped agents.
- **One takeaway**: stop token maxing, start ROI maxing.

### Key Points

#### Why legacy, and why "boring" (~00:48–00:49)

He scoped the talk up front: this is about **legacy systems in enterprises**. The "boring way" is for people who want systems that are scalable, secure, and reliable.

His background: former head of AI at Amazon Germany, where he built large-scale AI systems worth billions in revenue impact, plus work in robotics AI. He now runs Omokai, building a physical AI operating system that **turns voice into autonomous missions for robots and drones**. He wasn't there to pitch Omokai but to describe how his engineering team works — and warned that some of it would be controversial.

A telling detail about that team: Omokai is deeply AI-native — custom fine-tuned models, AI-generated data, and **seven human employees against more than ten "AI employees."**

#### The diagnosis: an agentic hangover (~00:50–00:52)

- **The productivity paradox**: citing Gartner research, more AI does not translate into more productivity — it translates into Anthropic and OpenAI getting richer. If you're using AI unbounded, without proper constraints, you're probably using it wrong.
- **Two fashionable myths**:
  - **Agent swarms** — hundreds of agents on a single problem, which buys you a lot of cost and a lot of errors.
  - **Loop engineering / loops within loops** — he's seen people nest loops, and it costs far more than you'd want to pay.
- **"AI will get cheap, so cost won't matter" doesn't survive either**: another study on AI code generation found that uncontrolled use produces far more errors — and more *persistent* errors — in production databases.
- **The hidden cost chain**: verification, then security loopholes, then debugging, and finally **cognitive debt and burnout**. He insists this last one is real: **use AI too much and you end up losing a lot of context yourself.**
- He showed a screenshot of someone screaming at the internet, fed up with an open-source repository drowning in AI slop. "We don't want to do that."

#### The prescription: the D3 framework (~00:52–00:53)

What he learned at Amazon is that **frameworks and mechanisms** are what make systems reliable and scalable. In 2025 he built a **D3 framework** for agentic coding at Amazon, with three phases:

1. **Discover** — produce a **research artifact** containing everything about your repository, plus its **upstream and downstream dependencies**.
2. **Plan** — from that research document, write a very well-defined plan broken into subtasks.
3. **Deliver** — the AI takes all of that information and solves the problem.

Three supporting rules:

- **Don't fully trust AI**: keep a **human sign-off** in the loop.
- **Diversify across vendors**: use multiple models from **different companies**, not variants from the same family.
- **Don't use too many agents**: around four, each well defined.

**Closing**: if you take one thing from the session — **stop token maxing and start ROI maxing.**

### Quotes

> "Using more AI does not lead to more productivity. It just leads to you making Anthropic and OpenAI richer." (~00:50)

His blunt summary of the Gartner finding.

> "If you use AI too much you end up losing a lot of context." (~00:51)

Cognitive debt in a sentence: it's the human who loses the context, not the model.

> "Stop token maxing and start ROI maxing." (~00:53)

The one line he asked the audience to take home.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Omokai | 他創辦的公司,做 physical AI 作業系統,把語音轉為機器人/無人機的自主任務 | His company: a physical AI operating system turning voice into autonomous missions for robots and drones | 7 名人類員工 + 10 名以上「AI 員工」 |
| D3 framework | 他 2025 年於 Amazon 開發的 agentic coding 機制:Discover → 計畫 → Deliver | Agentic-coding mechanism he built at Amazon in 2025: Discover → plan → Deliver | 中間階段的 D 名稱待確認 |
| Gartner 研究 | 用於支持「更多 AI ≠ 更高生產力」 | Cited to support "more AI ≠ more productivity" | 未給出報告名稱 |
| AI code generation 錯誤研究 | 用於支持「不受控使用會留下更多且更持久的錯誤」 | Cited for "uncontrolled use leaves more and more persistent errors" | 未給出出處 |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Krishna Kumar Shama | Krishnakumar Sharma |
| Omaki / Omukai / Omoai / Omakai | Omokai |
| agent swamps | agent swarms |
| AI slope | AI slop |
| cognitive dep | cognitive debt |
| open air | OpenAI |
| definfined | well-defined |
| brought billions in dollars | brought in billions of dollars |

## 待確認 / To Verify

- **D3 的三個 D 分別是什麼**:講者只點名 Discover 與 Deliver,中間階段他一律說 "plan"(可能是 Design 或 Define)。/ What the three D's in "D3" stand for — he only named Discover and Deliver; the middle phase he simply called "plan" (possibly Design or Define).
- Gartner 研究的正式名稱與發布時間未提供。/ No title or date given for the Gartner research cited.
- 「AI 生成程式碼會留下更多持久錯誤」的研究出處未提供。/ No citation given for the AI-code-generation error study.
- D3 framework 是否已對外公開發表(Amazon 內部機制 vs 公開文件)。/ Whether the D3 framework has been published externally or remains an internal Amazon mechanism.
