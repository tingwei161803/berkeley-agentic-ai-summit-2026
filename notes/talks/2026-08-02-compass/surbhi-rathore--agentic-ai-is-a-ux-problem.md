---
title: "Agentic AI Is a UX Problem Disguised as a Technology Breakthrough"
title_zh: "Agentic AI 是偽裝成技術突破的 UX 問題"
speaker: "Surbhi Rathore"
affiliation: "VP, AI Products & Strategy, Invoca"
type: talk
stage: Compass
date: 2026-08-02
session: "Session 3: Enterprise AI"
video: "https://www.youtube.com/watch?v=1UrriPJRSPU&t=5225s"
video_range: "01:27:05–01:33:50"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [enterprise, ux, trust, context, conversational-ai]
---

# Agentic AI 是偽裝成技術突破的 UX 問題(Agentic AI Is a UX Problem Disguised as a Technology Breakthrough)

**一句話總結**:模型已經逐漸可互換,決定 agent 成敗的不再是能不能完成工作流,而是能不能贏得一個「一坐下就預期你會失敗」的使用者的信任——那是設計問題,不是模型問題。
**One-line summary**: Models have become largely interchangeable, so what decides an agent's fate isn't whether it can execute the workflow but whether it earns trust from a user who arrived already expecting it to fail — and that's a design problem, not a model problem.

## 中文筆記

### TL;DR

- **她的立場轉變本身就是論點**:她在 Symbl.ai 花了七年做基礎設施、砸下大量金錢與時間訓練專門理解人與人對話細節的語言模型;過去一年多部署 agent 之後,她的假設大幅改變——**模型某種程度上已經可以互換了**,真正決定成敗的是設計與體驗。
- **最難的設計問題不是把 agent 做得能幹,而是做得值得信任**:使用者帶著「已經預設會失敗」的心態走進來——這不是對 AI 的偏執,而是多年技術落差與糟糕的對話式體驗累積出來的結果。
- **他們在既有資料層之上另建一層專門餵養 UX 的 context layer**,分三類:context-fed UX(使用者還沒打字前你就知道什麼)、graduated agency(設計時就界定 agent 該做與不該做什麼)、in-moment reading(當下讀出急迫性或偏離 happy path,就跳過常規流程)。

### 重點整理

#### 為什麼是 UX 問題:一位基礎設施創業者的立場轉變(約 01:28–01:29)

整場會議都在談怎麼把 agent 建好、監控、協調、演化;她想給一個不同的視角:**我們建這些 agent 的前提,是消費者願意信任並使用它們,而這大半是 UX 問題,不是技術與模型問題。**

她的資歷讓這個主張有分量:加入 Invoca 之前,她當了七年 **Symbl.ai** 的共同創辦人兼 CEO(公司去年被 Invoca 收購),那七年都押在基礎設施上,自己投入大量金錢與時間**訓練專門理解人與人互動細節的語言模型**。而過去一年多實際部署 agent 之後,她說自己的假設已經大幅演進:**模型某種程度上已經變得可以互換**;真正決定成敗的,是模型的設計與消費者體驗有沒有讓那個「有能力執行工作流的 agent」在**對的時機、用對的節奏**發揮影響力。

#### 情境:considered purchases 裡,信任必須即時建立(約 01:29–01:31)

Invoca 為「considered purchases(高涉入購買)」產業的品牌打造行銷與營收 agent——醫療、電信、保險、居家服務。這些領域的特徵是:**消費者幾乎每一次都需要先跟真人講過話才會下購買決定**,而且這些不是日常會做的事。

因此**信任必須幾乎立即建立**。在這些產業裡運作的 agent,必須透過互動方式,**立刻複製出消費者過去多年與品牌之間累積的那種人際信任**。

她強調真正的難題不在定義工作流、做營收營運或 agentic e-commerce,而是:**贏得一個「帶著已經失敗的心態走進來」的使用者的信任。** 他們日復一日接觸的消費者對 AI agent 極度懷疑——她說這不是因為對 AI 的偏執,而是**多年來技術落差與失敗的對話式 / agentic 體驗**造成的。使用者一開始互動就在想:「我又要把所有資訊重講一遍了」「這個 agent 根本不認識我」「我直接說『轉真人』趕快脫離這個迴圈」。

所以:**最難的設計問題不是讓 agent 有能力,而是讓它對一個預期它會失敗的人來說值得信任。**

#### 解法:一層專門餵養 UX 的 context layer(約 01:31–01:33)

Invoca 營運了約 14 年,累積了大量通話資訊、buyer journey 資料與互動資料;這些原本就被挖掘來訓練 agent 的知識、決定它處理哪些 intent、採取哪些行動。但他們**另外再建一層,專門用來餵養 agent 本身的 UX**,分三類:

1. **Context-fed UX**:在消費者打出第一個字之前,你已經知道關於他的什麼?
2. **Graduated agency**:在設計 agent 的階段就界定它該做什麼、不該做什麼,並據此設計體驗。
3. **In-moment reading**:這是她認為最重要的一項——如果偵測到**急迫性**,或消費者正走在偏離 happy path 的路上,要怎麼**跳過常規流程**,當下設計出一條讓他滿意的路徑。

三個實例:

- **腫瘤科(oncology)**:病患剛確診癌症,想預約 2:15 的門診,但表單填寫流程裡沒有這個時段。與其讓他走完痛苦的填表流程,agent 直接完成預約並確認醫師時段。
- **處方箋續領**:醫院剛導入新的 MyChart 系統、希望病患自助;但病患是在**晚上六點後**要續領,留了語音訊息沒人回。agent 直接把他導向正確的處理路徑,快速解決。
- **技術支援**:同一套 UX 思路也適用於支援場景——某人早上等著要視訊面試,網路卻斷了。怎麼把診斷從 20 步流程壓成**5 步自助診斷**,同時讓他留在通話中。

結語:設計 agent 體驗時,**把 context 當作 agent design system 的關鍵輸入**;如果你沒有這些資料,就去收集它、建一個 agentic loop,或串接真正產生這些資料的系統。

### 金句

> "The hardest design problem isn't making the agent capable. It's actually making it trustworthy to someone that's walked in expecting it to fail."(約 01:31)

整場演講的核心命題。

> "Models have somewhat become interchangeable."(約 01:29)

出自一位花七年訓練專用對話模型的創辦人之口,分量不同。

## English Notes

### TL;DR

- **Her own reversal is the argument.** She spent seven years at Symbl.ai on the infrastructure bet, pouring money and time into training language models specifically tuned to the nuances of human-to-human interaction. After a year-plus of actually deploying agents, her hypothesis shifted: **models have somewhat become interchangeable**, and design and experience are what decide outcomes.
- **The hardest design problem isn't capability, it's trustworthiness** — because users arrive with an already-failed mindset, not out of AI paranoia but from years of technology gaps and bad conversational UX.
- **They built a separate context layer purely to inform UX**, in three categories: context-fed UX (what you know before the user types a word), graduated agency (deciding at design time what the agent should and shouldn't do), and in-moment reading (detecting urgency or an off-happy-path situation and skipping the standard flow).

### Key Points

#### Why it's a UX problem: an infrastructure founder changing her mind (~01:28–01:29)

The conference had spent a day and a half on building, monitoring, orchestrating, and evolving agents. Her different angle: **the whole reason we build agents is that consumers trust them enough to use and operate them — and that's largely a UX problem, not a technology or model problem.**

Her credentials give the claim weight. Before joining Invoca, she was co-founder and CEO of **Symbl.ai** for seven years (acquired by Invoca last year), all of it spent on the infrastructure bet — investing heavily in **training language models specifically to understand the nuances of human-to-human interaction**. After a year-plus of deploying agents, her hypothesis has evolved massively: **models have somewhat become interchangeable.** What actually matters is whether the design of those models and the consumer experience let a capable agent land its influence **at the right moment, with the right timing**.

#### The setting: in considered purchases, trust has to be instant (~01:29–01:31)

Invoca builds marketing and revenue agents for brands operating in **considered purchases** — healthcare, telco, insurance, home services. The defining trait: **the consumer almost always needs to speak with a human before making a purchase decision**, and these aren't day-to-day transactions.

So **earning trust almost needs to be instant**. Agents operating in these industries have to emulate, immediately and through the interaction itself, the human trust consumers have built with these brands over years.

The real problem, she argues, isn't defining workflows, revenue operations, or agentic e-commerce. It's **winning the trust of a user who arrives with an already-failed mindset.** The consumers they work with daily are deeply skeptical of AI agents — not from paranoia about AI, but from **years of technology gaps and failed conversational and agentic UX**. Users open the interaction thinking: I'll have to repeat all my information, this agent knows nothing about me, I'll just say "talk to a human" and get out of this loop fast.

Hence: **the hardest design problem isn't making the agent capable — it's making it trustworthy to someone who walked in expecting it to fail.**

#### The build: a context layer that informs UX specifically (~01:31–01:33)

Invoca has been operating for roughly 14 years, accumulating huge volumes of call data, buyer journey data, and interaction data — already mined to inform what agents know, which intents they handle, and which actions they take. On top of that they're building **another layer whose job is to inform the agent's UX**, in three categories:

1. **Context-fed UX** — what do you know about the consumer before they type a single word?
2. **Graduated agency** — at design time, deciding what the agent should and shouldn't do, and designing the experience around that.
3. **In-moment reading** — the one she calls most important: if you sense urgency, or that the consumer is off the happy path, how do you skip the usual flow and design a path that delivers a good outcome right then?

Three worked examples:

- **Oncology.** A patient who has just been diagnosed with cancer wants a 2:15 appointment that isn't available in the form fill. Instead of dragging them through a painful form, the agent books the appointment and confirms doctor availability directly.
- **Prescription refills.** The hospital has rolled out a new MyChart system and wants self-serve, but the patient is trying to refill **after 6 p.m.**, left a voicemail, and got no response. The agent diverts them to the right path and handles it quickly.
- **Support.** The same UX thinking applied outside revenue use cases: someone waiting for a morning video interview call whose internet is down. How do you handle diagnosis in a **five-step self-diagnosis** rather than a 20-step process, while keeping them on the call?

Her closing thought: as you design agent experiences, **treat context as a key input to your agent design system** — and if you don't have the data, collect it and build an agentic loop, or connect to the systems that actually power that data.

### Quotes

> "The hardest design problem isn't making the agent capable. It's actually making it trustworthy to someone that's walked in expecting it to fail." (~01:31)

The thesis of the talk.

> "Models have somewhat become interchangeable." (~01:29)

Coming from someone who spent seven years training purpose-built conversational models, this lands differently.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Invoca | 為 considered purchases 產業品牌打造行銷與營收 agent | Builds marketing and revenue agents for brands in considered-purchase industries | 講者現任 VP, AI Products & Strategy |
| Symbl.ai | 講者共同創辦並擔任 CEO 七年的對話智慧公司,2025 年被 Invoca 收購 | The conversational-intelligence company she co-founded and led as CEO for seven years; acquired by Invoca in 2025 | 逐字稿誤作 "symbol.ai" |
| Context layer(三類:context-fed UX / graduated agency / in-moment reading) | 建在既有資料之上、專門餵養 agent UX 的一層 | A layer built atop their existing data specifically to inform agent UX | 講者描述的內部架構,非公開產品名 / internal architecture as described, not a public product name |
| MyChart | 醫院導入的病患自助系統(處方箋續領範例) | Patient self-service system referenced in the prescription-refill example | 為病患入口產品名稱 / a patient-portal product |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Serbia Rathor | Surbhi Rathore |
| Invoka | Invoca |
| symbol.ai | Symbl.ai |
| my chart | MyChart |
| infrastructure bed | infrastructure bet |

## 待確認 / To Verify

- 三個範例(oncology 預約、處方箋續領、視訊面試斷網)是實際客戶案例還是說明用的情境,講者未明說。/ Whether the three examples are real customer cases or illustrative scenarios — not stated.
- 「context layer」三分類是否有對外的正式命名或文件。/ Whether the three-part context layer has an official public name or documentation.
- 「Invoca 營運 14 年」為口述數字,未核對公司成立年份。/ The "14 years" figure is as spoken; not cross-checked against Invoca's founding date.
