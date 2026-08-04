---
title: "Speaking the Same Language: NLIP for Agent Interoperability"
title_zh: "說同一種語言:用 NLIP 達成 Agent 互通"
speaker: "Ranjan Sinha"
affiliation: "IBM Fellow, CTO & VP for watsonx, Enterprise AI, IBM"
type: talk
stage: Atlas
date: 2026-08-01
session: "Session 3: Frameworks & Dev Platforms"
video: "https://www.youtube.com/watch?v=psPzCQbjCCo&t=15249s"
video_range: "04:14:09–04:26:57"
transcript: "tmp/[English (auto-generated)] Atlas Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [interoperability, protocols, standards, nlip, enterprise-ai]
---

# 說同一種語言:用 NLIP 達成 Agent 互通(Speaking the Same Language: NLIP for Agent Interoperability)

**一句話總結**:傳統協定要求兩端與線路上講同一種語言,一改 schema 就斷;NLIP 把這個假設拿掉——只要兩端都有智慧可以翻譯,agent 各講各的也能互通,而它自己只用五個欄位就把「意圖」搬過去。
**One-line summary**: Traditional protocols demand that both endpoints and the wire speak the same language and break the moment a schema changes; NLIP drops that assumption — if there's intelligence at both endpoints to translate, agents can keep their own languages, and NLIP moves intent across in just five fields.

## 中文筆記

### TL;DR

- **問題是 Tower of Babel**:agent 各說各話時,你只能寫 custom glue code 與 adapter,而這條路不可能規模化。
- **NLIP 的定位是「意圖的 HTTP」**:HTTP 是在異質 client 與 server 之間搬運資源的中立統一方式;NLIP 是在異質 agent 與 client 之間搬運**意義與意圖**的中立統一方式。
- **它鬆綁了協定最根本的假設**:傳統協定要求 A = P = B(兩端語言與線路格式相同);NLIP 允許 A ≠ B ≠ P,**代價是兩端必須有智慧可以翻譯**——而以現在的趨勢,這個前提只會越來越成立。
- **刻意極簡**:訊息模型是輕量 JSON、只有五個欄位(三個必填);相較之下 A2A 或 MCP 的完整資料模型有 166–480 個欄位。
- **它不是要取代 A2A / MCP**,而是共存:NLIP 適合異質協定互通、語意彈性、跨協定中介;A2A 適合治理稽核、任務中心、嚴格 schema 與決定性執行;也可以混用,NLIP 在協調層、A2A 在治理層。

### 重點整理

#### 問題與定位(約 04:14–04:16)

Sinha 開場一句話就把問題講完:當 agent 講不同語言時,你得寫 custom code、glue code、adapter,而這**根本不 scale**。這就是 Tower of Babel 問題。

NLIP(Natural Language Interaction Protocol)是那個讓無縫互通成真的**通用握手**:只要 agent 會講 NLIP,它就能跟所有會講 NLIP 的東西對話。他給的類比貫穿全場——**把 NLIP 想成「意圖的 HTTP」**,而且它刻意採取和 HTTP 一樣的做法:極簡、中立。HTTP 是在異質 client 與 server 之間傳輸資源的中立統一方式;NLIP 是在異質 agent 與 client 之間傳輸**意義或意圖**的中立統一方式。

出身背景:由學界與業界研究者、實務者組成的工作組,由 **Enterprise Neurosystems Group** 與 **AI Alliance** 贊助;現已是 **ECMA 標準**,由技術委員會 **TC56** 推動(他順帶提醒:JavaScript 也是由 ECMA 這個組織標準化的),並已送交 **ISO** 標準化,目前進行中。

#### 核心設計:鬆綁 A = P = B(約 04:16–04:18)

他用一組左右對照的圖說明整個協定的關鍵洞見。

**傳統協定(左)**:agent 1 講語言 A、agent 2 講語言 B、線路上跑的是 P。傳統協定要求 **A = P = B**——三者必須相同。任何 schema 或欄位的改變都會讓它斷掉,結果就是 hard-coded integration 與緊耦合,並衍生出互通性與版本管理的麻煩。

**NLIP(右)**:同樣是 A、B、P 三者,但 **A 不必等於 B、也不必等於 P**。這帶來彈性,而條件是:**兩端必須有智慧,能在這些訊息之間翻譯**。他認為以現在的趨勢,你本來就可以預期解決方案與系統裡有智慧存在,而且它只會持續變好。

在這個基礎上,NLIP 提供的是一個非常簡單、開放、共通的標準協定,讓應用、agent 與服務彼此溝通。它假設兩端都有智慧以達成語意理解,並採取 **request–response 範式**,確保意義或意圖在 agent 真正行動之前先被**釐清並確認**。他特別點出這個範式的好處:**訊息如果語意模糊,agent 不會直接失敗,而是回頭要求澄清。**

同時它是**為企業現實打造**的:必須安全、要有 safeguard;transport agnostic 且沿用既有基礎設施,不重造輪子;支援多媒體;通訊高效;可用多種語言實作;是由 ECMA 治理的開放標準(ISO 審查中)。

#### 訊息模型:五個欄位(約 04:19–04:21)

NLIP **刻意極簡**。訊息模型是輕量 JSON,只有五個欄位,其中三個必填:

- **content**:承載被交換資訊的輕量 JSON 信封
- **format**:是 text、structured 還是 binary
- **subformat**:format 的細化——若是 text 就標明語言,若是 binary 就標明編碼
- 另外兩個選填欄位:一個 parsing hint,以及可放額外內容的 sub-message

核心資料模型就這五個欄位。他直接拿現行熱門協定對比:A2A 或 MCP 的完整資料模型有 **166 到 480 個欄位**。

實作上它在標準傳輸協定上都很簡單:**HTTP、WebSocket、AMQP** 的 binding 都已在 ECMA 規格中定義,可從 GitHub 頁面取得。安全性是 **secure by design 且為強制**:提供從基本到嚴謹企業級的**三種 profile**,並且處理的不只是傳輸層安全,還包含各種 AI 特有的風險。

#### 與單一廠商協定共存的兩種模式(約 04:21)

NLIP 可以用兩種模式與各種單一廠商協定互通:

- **模式 A**:NLIP 當 northbound API、單一廠商協定當 southbound API,中間用一個 translation agent 與 LLM pod 做兩者之間的翻譯。
- **模式 B**:跨多個 domain 互通。每個 domain 內可以有多個 agent,各自用不同的 agent framework、講自己的語言;只要它們是 **NLIP-aware**,就都能彼此溝通。

#### PoC 與效能實驗(約 04:21–04:24)

已有企業與大學在多個領域做出 PoC:電信、購物、永續、多模態客服等,多數也放在專案頁面上。

他挑客服那個 PoC 深入講:顧客送出一段**語音**請求 → 用語音轉文字模型(NVIDIA ASR)轉成文字 → 以 **NLIP over HTTP** 送給 channel recommender,由它挑出與該提問最相關的 subreddit 頻道 → 再以 **NLIP over HTTP** 送給 search agent,由它從那些頻道挑出最相關的主題、排序後回傳給顧客。整體就是:一個顧客提問,從 Reddit 撈出最相關的主題回覆。

接著是效能比較:同一個 workflow,拿 **NLIP 對比 A2A**,使用**對稱、完全相同的計時 harness**,並取三種 A2A 變體(A2A SDK、cache 最佳化版 A2A、輕量 Python A2A)。他們做了**階段層級的儀器化**——message creation、connection、send 三個階段,總延遲是三者之和——並在兩台機器、兩份含多筆顧客提問的資料集上測。結果在兩台機器上的平均總延遲,NLIP 都比較低,他把這歸因於其訊息信封的極簡本質。他自己強調這是**初步實驗**,更複雜的 workflow 與實驗還待做,也歡迎外界參與。

#### 給實務者的選型建議(約 04:24–04:26)

他把問題收斂成「什麼時候該用哪個協定」:

| 情境 | 建議 |
|------|------|
| 異質協定互通、語意彈性、跨協定中介 | 選 NLIP |
| 治理與稽核需求、任務中心或長時間執行的 workflow、嚴格 schema 強制、決定性執行 | 選 A2A |
| 混合型 workload | 混用:NLIP 在協調層,A2A 在治理層 |

但他強調真正的原則是:**協定選擇應該由 workload 特性來決定。** 現實是協定會有長尾——支付、購物等領域都在推出自己的 domain-centric 協定——所以問題變成如何跨這些協定以可互通的方式溝通,而那正是 NLIP 的位置。

收尾:NLIP 已整合進 **AG2** framework(他說 AG2 每天被下載數萬次、每月可能達百萬次)。委員會每週開會、持續開發,歡迎回饋、實際 use case、參與評測或直接貢獻,聯絡方式都在專案頁面上。

### 金句

> "Think of NLIP as the HTTP of intent."(約 04:15)

整場演講的核心比喻,也解釋了為什麼它刻意做得這麼小。

> "In a traditional protocol they all have to be the same. A is equal to P is equal to B."(約 04:17)

一句話點出既有 agent 協定的脆弱點,以及 NLIP 要鬆綁的到底是什麼。

> "If a message is ambiguous, the agent doesn't just fail — it will ask for clarifications."(約 04:18)

request–response 範式的用意:意圖要先被確認,agent 才動手。

## English Notes

### TL;DR

- **The problem is the Tower of Babel.** When agents speak different languages, all you can do is write custom glue code and adapters — and that does not scale.
- **NLIP positions itself as "the HTTP of intent."** HTTP is a neutral, uniform way to transfer *resources* between heterogeneous clients and servers; NLIP is a neutral, uniform way to transfer *meaning* between heterogeneous agents and clients.
- **It relaxes the foundational assumption of protocols.** Traditional protocols require A = P = B — both endpoints and the wire format identical. NLIP allows A ≠ B ≠ P, **provided there is intelligence at both endpoints to translate** — a precondition that current trends make increasingly safe to assume.
- **Deliberately minimal**: a lightweight JSON message model with five fields, three mandatory, against full data models of 166–480 fields for A2A or MCP.
- **It is not a replacement for A2A or MCP** but a complement: NLIP for heterogeneous interoperability, semantic flexibility, and cross-protocol mediation; A2A for governance, audit, strict schemas, and deterministic execution; hybrid deployments put NLIP at the coordination layer and A2A at the governance layer.

### Key Points

#### The problem and the framing (~04:14–04:16)

Sinha states the problem in his opening sentence: when agents speak different languages you write custom code, glue code, and adapters, and that does not scale well. This is the Tower of Babel problem.

NLIP — the Natural Language Interaction Protocol — is the **universal handshake** that makes seamless interoperability real: if an agent speaks NLIP, it speaks to everything else that does. His analogy carries the whole talk: **think of NLIP as the HTTP of intent**, and note that it follows the same approach of being deliberately minimal and neutral. HTTP is a neutral, uniform way to transfer resources between heterogeneous clients and servers; NLIP is a neutral, uniform way to transfer meaning or intent between heterogeneous agents and clients.

Provenance: it came out of a working group of academic and industry researchers and practitioners, sponsored by the **Enterprise Neurosystems Group** and the **AI Alliance**. It is now an **ECMA standard**, driven by technical committee **TC56** — the same standards body, he points out, that standardized JavaScript — and has been submitted to **ISO**, where standardization is in progress.

#### The core design: relaxing A = P = B (~04:16–04:18)

A pair of side-by-side diagrams carries the central insight.

In a **traditional protocol**, agent 1 speaks language A, agent 2 speaks language B, and language P passes over the wire — but **A = P = B is required**. Any change in schema or fields typically breaks it. That is what hard-coded integrations and tight coupling look like, and it produces the familiar interoperability and version-management problems.

Under **NLIP**, agent 1 still speaks A and agent 2 still speaks B while P goes over the wire, but **A need not equal B and neither needs to equal P**. This buys flexibility, on one condition: **there must be intelligence at both endpoints capable of translating between these messages.** Given current trends, he argues, you would expect intelligence to be available in solutions and systems anyway — and it keeps improving.

On that foundation, NLIP is a very simple, open, common standard protocol for applications, agents, and services to communicate. It assumes intelligence at both endpoints for semantic understanding, and it follows a **request–response paradigm** so that meaning or intent is refined and confirmed *before* the agent acts. The consequence he highlights: **if a message is ambiguous, the agent does not simply fail — it asks for clarification.**

It is also built for enterprise reality: it must be secure with safeguards; it is transport agnostic and uses existing infrastructure rather than rebuilding the wheel; it supports multimedia; communication is efficient; it can be implemented in multiple languages; and it is an open standard governed by ECMA, with ISO review underway.

#### The message model: five fields (~04:19–04:21)

NLIP is **deliberately minimal**. The message model is lightweight JSON with just five fields, three of them mandatory:

- **content** — a lightweight JSON envelope carrying the information being exchanged
- **format** — whether the content is text, structured, or binary
- **subformat** — a refinement of format: which language for text, which encoding for binary
- plus two optional fields: a parsing hint, and a sub-message that can carry additional content

That is the core data model. For contrast he cites the full data models of widely used protocols such as A2A or MCP at **166 to 480 fields**.

It is simple to implement over standard transports, with bindings for **HTTP, WebSocket, and AMQP** specified in the ECMA documents and available from the project's GitHub page. Security is **mandatory and by design**: three profiles ranging from basic to rigorous enterprise, addressing AI-specific risks in addition to transport security.

#### Two modes of coexistence with vendor protocols (~04:21)

NLIP interoperates with single-vendor protocols in two modes. In **mode A**, NLIP is the northbound API and the single-vendor protocol the southbound API, with a translation agent and an LLM pod translating between them. In **mode B**, it spans multiple domains, each of which may contain many agents built on different frameworks speaking their own languages — as long as they are **NLIP-aware**, they can all communicate.

#### Proofs of concept and a latency comparison (~04:21–04:24)

Companies and universities have built PoCs across telecom, shopping, sustainability, and multimodal customer support, most of them published on the project page.

He walks through the customer support one. A customer submits a **voice** request; the audio is converted to text by a speech-to-text model (NVIDIA ASR); that text goes over **NLIP over HTTP** to a channel recommender, which selects the most relevant subreddit channels for the query; that goes over **NLIP over HTTP** to a search agent, which pulls the most relevant topics from those channels, ranks them, and returns them. Net effect: a customer query fetches the most relevant Reddit topics back to the customer.

They then compared **NLIP against A2A** on this workflow using a symmetric, identical timing harness and three A2A variants — the A2A SDK, a cache-optimized A2A, and a lightweight Python A2A. Instrumentation was **phase-level** (message creation, connection, send), with total latency the sum of the three phases, run across two machines and two datasets of customer queries. Average total latency was lower for NLIP on both machines, which he attributes to the minimal nature of its message envelope. He is careful to call these **preliminary experiments**: more complex workflows and evaluations remain to be done, and participation is welcome.

#### Guidance for practitioners (~04:24–04:26)

The practical question reduces to when to use which protocol. Choose **NLIP** for use cases requiring heterogeneous protocol interoperability, semantic flexibility, or cross-protocol mediation. Choose **A2A** when you have governance and audit needs, task-centric or long-running workflows, strict schema enforcement, or deterministic execution. Choose a **hybrid** for mixed workloads, with NLIP at the coordination layer and A2A at the governance layer.

The principle behind the table matters more than the table: **protocol selection should be guided by workload characteristics.** There is already a long tail of protocols, with domain-centric ones appearing for payments, shopping, and more, so the real question is how to work across them and communicate interoperably — which is where NLIP fits.

He closes by noting NLIP has been integrated with the **AG2** framework, which he says is downloaded tens of thousands of times daily and perhaps a million times a month. The committee meets weekly and continues to develop the protocol; feedback, use cases, participation in evaluation, and contributions are all welcome, with contact details on the project page.

### Quotes

> "Think of NLIP as the HTTP of intent." (~04:15)

The organizing metaphor, and the reason the protocol is deliberately so small.

> "In a traditional protocol they all have to be the same. A is equal to P is equal to B." (~04:17)

The brittleness of existing agent protocols in one line — and exactly what NLIP relaxes.

> "If a message is ambiguous, the agent doesn't just fail — it will ask for clarifications." (~04:18)

The point of the request–response paradigm: confirm intent before acting on it.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| NLIP | Natural Language Interaction Protocol,agent 間互通的語意協定 | Natural Language Interaction Protocol — a semantic protocol for agent interoperability | ECMA 標準,TC56 制定;ISO 標準化進行中 / ECMA standard from TC56; ISO standardization in progress |
| ECMA TC56 | 制定 NLIP 的技術委員會 | The technical committee that produced NLIP | 同一標準組織也標準化了 JavaScript / the same body standardized JavaScript |
| Enterprise Neurosystems Group | NLIP 工作組的贊助組織之一 | Co-sponsor of the NLIP working group | |
| AI Alliance | NLIP 工作組的贊助組織之一 | Co-sponsor of the NLIP working group | |
| NLIP transport bindings | HTTP、WebSocket、AMQP,規格在 ECMA 文件與 GitHub 頁面 | HTTP, WebSocket, and AMQP bindings, specified in ECMA documents and on GitHub | |
| A2A / MCP | 對照組協定;完整資料模型有 166–480 個欄位 | Comparison protocols; full data models of 166–480 fields | NLIP 核心僅 5 個欄位 / NLIP's core is 5 fields |
| AG2 | 已整合 NLIP 的 agent framework | Agent framework with NLIP integration | 講者稱每日下載數萬次 / he cites tens of thousands of downloads daily |
| 客服 PoC / Customer support PoC | 語音 → NVIDIA ASR → NLIP/HTTP → channel recommender → NLIP/HTTP → search agent → Reddit 主題 | Voice → NVIDIA ASR → NLIP/HTTP → channel recommender → NLIP/HTTP → search agent → Reddit topics | 與 A2A 三種變體做延遲比較 / benchmarked against three A2A variants |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Runja Singha / Ron John | Ranjan Sinha |
| Nlip / NLP / Enley / enlip / LIP | NLIP |
| ECMA uh body / TC56 | Ecma International / TC56(拼寫正確,僅斷句混亂)|
| A28 SDK / HA | A2A SDK / A2A |
| ag2 | AG2 |
| interable | interoperable |

## 待確認 / To Verify

- 欄位數比較的前半段(字幕作 "you're looking at 60 to 99 to the full data model having 166 to 480 fields")語意不完整;可確認的是 A2A / MCP **完整資料模型為 166–480 個欄位**,而 60–99 可能是其核心資料模型的欄位數,需看投影片確認。/ The first half of the field-count comparison is garbled; only "166 to 480 fields for the full data model" of A2A / MCP is reliable — the 60–99 figure is probably the core data model but needs slide confirmation.
- 五個欄位中兩個選填欄位的正式名稱(字幕僅描述為 "a parsing hint" 與 "more additional content in the sub message"),應以 ECMA 規格為準。/ The formal names of the two optional fields (described only as a parsing hint and a sub-message) should be checked against the ECMA specification.
- 三種安全 profile 的正式名稱未在演講中列出(僅說「從 basic 到 rigorous enterprise」)。/ The formal names of the three security profiles were not given; he only described the range from basic to rigorous enterprise.
- AG2 的下載量數字為講者口述概估。/ The AG2 download figures were given verbally as approximations.
