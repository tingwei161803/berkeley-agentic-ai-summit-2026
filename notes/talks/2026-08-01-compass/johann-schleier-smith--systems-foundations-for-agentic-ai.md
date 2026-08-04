---
title: "Systems Foundations for Agentic AI"
title_zh: "Agentic AI 的系統基礎"
speaker: "Johann Schleier-Smith"
affiliation: "Senior Staff Engineer, Temporal"
type: talk
stage: Compass
date: 2026-08-01
session: "Session 2: Frameworks & Dev Platforms"
video: "https://www.youtube.com/watch?v=AO0RXP-fVZQ&t=2972s"
video_range: "00:49:32–00:59:44"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [durable-execution, temporal, reliability, abstractions, agent-harness]
---

# Agentic AI 的系統基礎(Systems Foundations for Agentic AI)

**一句話總結**:蓋 agent 時真正吃掉時間的不是核心功能,而是 retry、queue、狀態管理這些橫切關注點;**durable execution** 的價值就是把系統邏輯和商業邏輯切開,讓你用普通語言寫出 crash-proof 的 agent——而且 agency 不是愈多愈好,好的抽象要讓你能沿著 agency 光譜自由來回。
**One-line summary**: What eats your time building agents isn't the core functionality but the cross-cutting concerns — retries, queuing, state management. **Durable execution** separates systems logic from business logic so you can write crash-proof agents in ordinary code. And more agency isn't always better: good abstractions let you slide up and down the agency spectrum without a rewrite.

## 中文筆記

### TL;DR

- **系統的難處在橫切關注點**:一個處理退貨的客服 agent 要接知識庫、庫存、ERP、付款、升級轉人工、寄信;要讓它可靠,就得到處補 retry、加 queue 處理負載、做狀態管理——而傳統寫法會把**商業邏輯和系統邏輯交纏在一起**。
- **Durable execution**:Temporal 的核心。把系統邏輯放一邊、應用關注點放另一邊,用**普通語言寫普通程式碼**(Python、TypeScript……)就能得到 crash-proof 執行。崩潰後取回狀態只有兩條路——**存下來,或重算**;Temporal 給你簡單的標註來指定哪些要重算、哪裡要存狀態。「如果說有什麼訣竅,這就是那個訣竅。」
- **Agentic workload 的三個特性**:**非確定性**(要驗證與保存 LLM 回應,但另一面是它對輸入很寬容)、**安全性**(除了 prompt injection 與 alignment,還有一個很好用的威脅模型是「單純的判斷力不佳」——它就是會不小心 `rm -rf`)、**執行剖面**(與真實世界互動,要仔細把狀態寫下來;負載爆量,所以偏向 serverless)。
- **Agency 光譜**:level 1 是普通程式碼掌控流程、只在特定點插入 LLM(摘要這類任務用這個就很好、很可靠);level 3 是 LLM 決定下一步的 agentic loop;另一端是 self-evolving agent。**agency 多不代表更好**,好的抽象要能讓你來回移動而不必重寫整個應用。
- **當天發布**:**Temporal Agent Harness**(尚非正式支援產品,先請大家去 GitHub 按星)——建在 durable execution 之上的一組抽象,內層 harness 可插 OpenCode、OpenAI Agents SDK、Pydantic AI,對外可接 Slack、Teams;附帶 observability,可回看 agent 每一步在想什麼、呼叫了什麼工具、做過哪些 human approval。

### 重點整理

#### 功能之外的東西才是難題(約 00:50–00:52)

談系統,就是「把一堆元件組起來產生某種功能」——而 AI 的元件特別多。但除了核心功能之外,還有一組**橫切關注點**:reliability(Temporal 的老本行)、efficiency、security、evolvability(含 scalability、升級能力等)。

他用 reliability 切入,因為那正好解釋 Temporal 的核心機制。假設有一個處理退貨的客服 agent,它要接上知識庫、庫存、ERP,要處理付款,大概還要有升級機制,要能寄 email。要讓這一切**可靠**地運作,你得做什麼?**到處放 retry**、大概還需要 **queue** 來吸收負載、需要**狀態管理**來追蹤整個流程走到哪。這每一處都是會出事的地方,而蓋這個系統的人終究得處理它們。

問題是:**傳統軟體會把應用關注點(商業邏輯)和系統關注點交纏在一起。**

#### Durable execution:把兩邊拆開(約 00:52–00:53)

如果這場演講只帶走一件事,那就是 **durable execution 這個模型**:它讓你把系統邏輯放一邊、應用關注點放另一邊,真正隔離開來。

Temporal 開源專案本身讓你蓋 **crash-proof 的應用**:MIT 授權,後端可以用 Postgres 或 Cassandra 等資料庫,另有雲端產品。但關鍵在於**你寫的是普通程式碼、普通程式語言**(Python、TypeScript,隨你),卻得到 crash-proof 的執行。

崩潰之後怎麼把狀態拿回來?其實只有兩種辦法:**存下來,或重新算一次**。Temporal 給你的是**可以掛在程式碼上的簡單標註**——「這段我要你重算、這裡我要你存狀態」。他說:「如果說有什麼訣竅的話,這就是那個訣竅。」另外還有一些有趣的東西,例如**用一般語言原生語法寫出分散式系統**。

#### 誰在用(約 00:53–00:54)

他引用了 OpenAI 應用基礎架構 VP 的說法。值得一提的案例是 **ChatGPT Images**——要吐出一張圖需要一連串步驟,而這些步驟必須全部可靠地完成;**Codex on the web** 是另一個。更廣的用途橫跨基礎架構 control plane、data connector(可以理解成建立與維護 RAG index)、到傳統商業流程。生態系裡的使用者包括 Nvidia、Cursor、SpaceX、Lovable、Replit。

#### Agentic workload 有什麼不一樣(約 00:54–00:56)

他所在的 **AI Foundations team** 花很多時間想:對 agentic AI 這種 workload,**什麼才是對的抽象**?取捨在哪?哪些該切開、哪些該給使用者一個旋鈕?他強調這是一種**和過去系統領域處理過的都不一樣的 workload**,所以重新思考抽象這件事本身很有意思。幾個觀察:

- **非確定性**:呼叫 LLM 就代表你得**驗證並保存回應**。但硬幣的另一面很有趣——它是模糊的,因此**對輸入非常寬容**。
- **安全性**:威脅面通常想到的是對抗性輸入,像 prompt injection 與 alignment;但他認為思考 agent 時**一個很好用的威脅模型其實是「判斷力不佳」**——它就是會不小心 `rm -rf`,不是出於惡意,只是沒想清楚。這件事深深影響他們的設計考量。
- **執行剖面**:因為你在**和真實世界互動**,所以要抓住狀態、把事情仔細寫下來;另外**負載是突發性的**,這會導向 serverless 這類做法。

#### Agency 光譜:不是愈多愈好(約 00:56–00:57)

跨生態系合作後的另一個觀察:存在一條 **agency 的光譜**,而某個應用的正確解答**可能落在光譜上任何一點**——而且 **agency 愈多不見得愈好**。

- 大家想到 agent 時,通常想的是 **level 3**:一個 agentic loop,由 LLM 決定接下來發生什麼。
- 但看向左邊的 **level 1**:有**非常多**應用(例如摘要)其實是用普通程式碼驅動控制流、只在很特定的點插入 LLM 就能做得很好——可以非常可靠;**如果這樣就把事情做完了,那大概就是對的解**。
- 光譜另一端則走到 **self-evolving agent**,現在某些 harness 已經看得到。有它的理由,但同樣**不見得是這份工作的正解**。

Temporal 在思考 agentic AI 的抽象時,目標就是讓你**把這個旋鈕轉到想要的位置,而且能在光譜上來回移動,不必重寫整個應用**。

#### 當天發布:Temporal Agent Harness(約 00:57–00:59)

他當場分享的是 **Temporal Agent Harness**:**尚未是正式支援的產品**,但去 GitHub repo 按個星,希望它很快就是。

它是一組建在 Temporal durable execution 核心抽象之上的抽象,讓你比較容易蓋出實用的 agent。設計重點是**混搭**:

- **內層 harness 可插拔**——可以是像 **OpenCode** 這樣的 coding agent,可以是 **OpenAI Agents SDK**(他特別提到它有不少有趣的 sandboxing 功能),也可以是 **Pydantic AI**;他說他們很努力去擁抱這個生態系。
- **工具可插拔**。
- **介面可插拔**——你想透過 Slack、Teams 或別的方式跟它講話都行。

他展示了一張截圖:一個 **OpenCode** session,他在裡面修一個簡單程式的 bug。因為是跑在 agent harness 上,他不只拿到 durability 與 reliability(想放大規模時特別重要),還「幾乎是免費地」拿到 **observability**——可以鑽進去看**agent 在各個步驟到底在推理什麼、呼叫了哪些工具、沿途發生過哪些 human approval**。這就是把抽象想清楚之後拿到的好處。

### 金句

> "There's basically two ways to get that state back. You can either save it or you can recompute it. … And that's sort of, if there's a trick, that's the trick."(約 00:53)

Durable execution 的全部祕密。

> "A great threat model when you're thinking about agents is actually just bad judgment — because it happens that `rm -rf`."(約 00:55)

比起 prompt injection,更常見的災難來源是 agent 單純沒想清楚。

> "The more agency you have, it's not always a better thing."(約 00:56)

反直覺但務實的一句:能用普通程式碼可靠解決的,就別硬塞 agentic loop。

## English Notes

### TL;DR

- **The hard part is the cross-cutting concerns.** A customer-service agent handling returns touches knowledge bases, inventory, ERP, payments, escalations, and email. Making that reliable means retries everywhere, queuing for load, and state management — and conventionally that **systems logic gets interleaved with the business logic**.
- **Durable execution** is Temporal's answer: put systems logic on one side and application concerns on the other, write **ordinary code in ordinary languages**, and get crash-proof execution. After a crash there are only two ways to recover state — **save it or recompute it** — and Temporal gives you simple annotations to say which. "If there's a trick, that's the trick."
- **Three properties of agentic workloads**: **non-determinism** (validate and store LLM responses — though the flip side is they're forgiving about inputs); **security** (beyond prompt injection and alignment, a great threat model is plain bad judgment — it happens that `rm -rf`); and **execution profile** (you're touching the world, so write state down carefully; load is bursty, which calls for serverless).
- **A spectrum of agency**: level 1 is regular code driving control flow with LLMs at specific points (great and very reliable for things like summarization); level 3 is the agentic loop where the LLM decides what happens next; the far end is self-evolving agents. **More agency isn't always better** — good abstractions let you move along the spectrum without rewriting the application.
- **Announced on stage**: the **Temporal Agent Harness** — not yet a supported product, so go star the repo. Abstractions on top of durable execution, with a pluggable inner harness (OpenCode, OpenAI Agents SDK, Pydantic AI), pluggable tools, and pluggable interfaces (Slack, Teams), plus observability into what the agent reasoned about at each step.

### Key Points

#### The functionality isn't the hard part (~00:50–00:52)

A system is functionality assembled out of a pile of components, and AI has a lot of components. But beyond the core functionality there are **cross-cutting concerns**: reliability (Temporal's deep specialty), efficiency, security, and evolvability — which covers scalability, upgrades, and the rest.

He used reliability as the way in, because it explains Temporal's core mechanism. Take a customer service agent handling returns: it needs knowledge bases, inventory, ERP, payment handling, probably escalations, and the ability to send email. To make that work reliably you need **retries in a whole bunch of places**, probably **queuing** to handle load, and **state management** to track the process all the way through. Every one of those is a place things go sideways, and whoever builds it has to account for them.

The underlying problem: **traditional software interleaves application concerns — the business logic — with systems concerns.**

#### Durable execution: pulling the two apart (~00:52–00:53)

If there's one takeaway about what Temporal makes possible, it's the model of **durable execution**: it lets you write code that puts systems logic on one side and application concerns on the other, genuinely isolated.

The Temporal open source project lets you build **crash-proof applications** — MIT licensed, backed by databases like Postgres or Cassandra, with a cloud product alongside. The key point is that you write **regular code in regular programming languages** (Python, TypeScript, you name it) and get crash-proof execution.

How do you recover after a crash? There are only two ways to get the state back: **save it or recompute it**. Temporal gives you simple annotations to put on your code saying "recompute this here, save state there." As he put it: "if there's a trick, that's the trick." There's other neat material too, like getting distributed systems out of ordinary language primitives.

#### Who's using it (~00:53–00:54)

He cited the VP of application infrastructure at OpenAI. The notable application is **ChatGPT Images**, where a whole series of steps have to happen reliably to produce the image; **Codex on the web** is another. Beyond that it spans infrastructure control planes, data connectors (effectively building and maintaining RAG indexes), and traditional business processes. Across the ecosystem: Nvidia, Cursor, SpaceX, Lovable, Replit.

#### What makes agentic workloads different (~00:54–00:56)

His **AI Foundations team** spends its time on what the right abstractions are for agentic AI workloads, what the tradeoffs are, how to slice them, where to pick a point in the space and where to expose a knob instead. He stressed this is genuinely a different workload from anything systems people have had to handle before, which makes rethinking the abstractions fun. Some observations:

- **Non-determinism.** Calling into an LLM means you need to **validate and store those responses**. But there's an interesting flip side: it's fuzzy, and therefore **forgiving with respect to its inputs**.
- **Security.** The usual threat framing is adversarial input — prompt injection, alignment. But a great threat model for agents is **just bad judgment**: "it happens that `rm -rf`," by accident rather than intent. That drives a lot of their design considerations.
- **Execution profile.** You're interacting with the world, which is exactly where you want to capture state and write things down carefully. And load is bursty, which calls for serverless and the like.

#### The spectrum of agency: more isn't better (~00:56–00:57)

Another observation from working across the ecosystem: there is a **spectrum of agency**, and the right solution for a given piece of functionality **can come from anywhere on it** — and more agency is not always better.

- What people usually picture is **level 3**: an agentic loop where the LLM makes all the decisions about what happens next.
- To the left, at **level 1**, there's a huge number of applications — summarization among them — where the job gets done very well by having **regular code drive the control flow with LLMs inserted at very specific points**. That can be very reliable, and if it gets the job done it's probably the right solution.
- At the far end are **self-evolving agents**, which now show up in some harnesses. There's a reason for them, but they're probably not the right solution for most jobs either.

Temporal's abstractions for agentic AI are designed to let you **dial that in, and move back and forth along the spectrum without rewriting your entire application**.

#### Announced: the Temporal Agent Harness (~00:57–00:59)

The thing he shared on stage: the **Temporal Agent Harness**. Not yet a supported product — "if you go and star the GitHub repo, then hopefully it will be soon."

It's a set of abstractions built on Temporal's core durable execution primitives, designed for mix-and-match:

- A **pluggable inner harness** — a coding agent like **OpenCode**, or **OpenAI Agents SDK** (which he noted has interesting sandboxing functionality), or **Pydantic AI**. They've worked hard to embrace the ecosystem.
- **Pluggable tools.**
- **Pluggable interfaces** — talk to it through Slack, Teams, whatever.

His screen grab showed an **OpenCode** session fixing a bug in a simple program. Because it ran under the agent harness, he got not only durability and reliability (which matter when you want to run at scale) but also, effectively for free, **observability**: the ability to dive in and see **what the agent was reasoning about at each step, what the tool calls were, and what human approvals happened along the way**. That, he argued, is the payoff for being thoughtful about the abstractions you bring into agentic AI.

### Quotes

> "There's basically two ways to get that state back. You can either save it or you can recompute it. … And that's sort of, if there's a trick, that's the trick." (~00:53)

The whole secret of durable execution.

> "A great threat model when you're thinking about agents is actually just bad judgment — because it happens that `rm -rf`." (~00:55)

The more common source of disasters than prompt injection.

> "The more agency you have, it's not always a better thing." (~00:56)

Counterintuitive but practical: if plain code does the job reliably, don't force an agentic loop onto it.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Temporal | durable execution 開源專案,MIT 授權,可後接 Postgres / Cassandra,另有雲端產品 | Open-source durable execution project, MIT licensed, backed by Postgres or Cassandra, with a cloud offering | 支援 Python、TypeScript 等多語言 SDK |
| Temporal Agent Harness | 建在 durable execution 上的 agent 抽象層,內層 harness / 工具 / 介面皆可插拔 | Agent abstraction layer on durable execution with pluggable inner harness, tools, and interfaces | 演講當日分享,**尚非正式支援產品** / shared on stage, **not yet a supported product** |
| OpenCode | 可作為內層 harness 的 coding agent;示範截圖即為 OpenCode session | Coding agent usable as the inner harness; the demo screenshot is an OpenCode session | |
| OpenAI Agents SDK | 另一個可插入的內層 harness,具 sandboxing 功能 | Another pluggable inner harness, with sandboxing functionality | |
| Pydantic AI | 同上,生態系內另一個可插入選項 | Another pluggable option in the ecosystem | 字幕作 "pedantic AI" |
| Temporal 的使用案例 / Temporal users | ChatGPT Images、Codex on the web、Nvidia、Cursor、SpaceX、Lovable、Replit | ChatGPT Images, Codex on the web, Nvidia, Cursor, SpaceX, Lovable, Replit | 亦用於 infra control plane 與 RAG index 維護 |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Johan Shyler Smith / Johan Schlersmith | Johann Schleier-Smith |
| pedantic AI | Pydantic AI |
| open eye agents SDK | OpenAI Agents SDK |
| open code | OpenCode |
| Postgress | Postgres |
| codecs on the web | Codex on the web |
| a sentic AI | agentic AI |
| recomputee | recompute |
| replet | Replit |
| RM-rf | `rm -rf` |

## 待確認 / To Verify

- 他引述的 OpenAI 應用基礎架構 VP,字幕作 "Venat",姓名待確認。/ The OpenAI VP of application infrastructure he quoted was transcribed as "Venat" — name to confirm.
- Temporal Agent Harness 的 GitHub repo 網址(他說會放 QR code)未在字幕中出現。/ The GitHub URL for the Temporal Agent Harness (shown as a QR code) doesn't appear in the captions.
- agency 光譜的 level 1 / level 3 是否有正式定義與完整分級表,演講只口述了兩端與中間。/ Whether the level 1 / level 3 agency spectrum comes from a published taxonomy — only the endpoints and middle were described.
