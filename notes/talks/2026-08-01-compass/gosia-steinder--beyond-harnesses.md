---
title: "Beyond Harnesses – Platform Solutions for Agent Reliability, Security, and Efficiency"
title_zh: "超越 Harness:面向 Agent 可靠性、安全性與效率的平台解法"
speaker: "Gosia Steinder"
affiliation: "IBM Fellow, IBM Research"
type: talk
stage: Compass
date: 2026-08-01
session: "Session 1: AI Systems"
video: "https://www.youtube.com/watch?v=IBpR4uYftLY&t=2006s"
video_range: "00:33:26–00:43:35"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 1st - Morning Session [DownSub.com].srt"
status: draft
tags: [agent-os, platform, zero-trust, kubernetes, serverless]
---

# 超越 Harness:面向 Agent 可靠性、安全性與效率的平台解法(Beyond Harnesses – Platform Solutions for Agent Reliability, Security, and Efficiency)

**一句話總結**:今天 agent 的可靠性、安全與效率問題全被塞進應用層的 harness 裡各自造輪子,但歷史(Unix/POSIX、容器/Kubernetes)顯示這一定會收斂成新的作業系統層;IBM Research 正在用一層「攔截層」把控制功能從 agent 業務邏輯中抽離出來,建立這個 agent 時代的 OS。
**One-line summary**: Agent reliability, security, and efficiency are currently solved bespoke inside application-layer harnesses, but history (Unix/POSIX, containers/Kubernetes) says the industry consolidates onto a new operating system layer — and IBM Research is building that layer as an interception tier that pulls control functions out of agent business logic.

## 中文筆記

### TL;DR

- **第三波平台演進**:第一波是硬體與軟體分離、高階語言誕生;第二波是雲端運算與跨資料中心的分散式應用。兩波各自催生了一個「作業系統」——一層把應用與基礎設施隔開的抽象,同時提供韌性、擴展性與效率的原語。AI 應用是**企業架構史上最不確定、最不可靠的元件**,將需要第三個這樣的基礎。
- **兩類新挑戰**:**結構性(structural)**——agent 的指令集是開放式的,在 runtime 才決定用哪些操作、以什麼順序執行,這直接破壞 zero-trust 安全(需要事先知道互動模式)、傳統復原(補償與 rollback 變得難以實作)與部署前測試;加上 context 裡指令與資料沒有分離、agent 之間又靠交換 context 溝通,執行隔離消失,blast radius 控不住。**語義性(semantic)**——無法完整指定 agent 目標(「該做什麼」難寫,「不該做什麼」更難),缺乏形式化方法驗證目標,模型又不擅長回報自身狀態(**沒有可靠的 error code**),導致成功/失敗/活性(是否在收斂而非卡住)都難以判斷,判斷不了就無法復原。
- **解法方向**:不重造平台,而是在既有雲端平台上加一層**攔截層**,能同時接上三類 agent(自建的、可用 hook/plugin 控制的知名 harness、只能從外部觀察的黑箱),用統一方式觀察與修改 agent 對外界的所有互動;控制功能建在這層之上。首先攻的是 zero-trust 安全,再往語義層(context 管理、tool call 正確性、資料流分析)延伸。專案為 **Rossoctl**。
- **應用模式是 serverless**:把 agent loop 當成無狀態元件,與管理 context 的 durable session 儲存、以及由多樣化 sandbox 組成的執行層分離——換來更好的韌性、正確性、效能與擴展性,並在成本上有實測收益。

### 重點整理

#### 為什麼需要第三個作業系統(約 00:33:26–00:34:50)

Steinder 認為我們正進入應用平台演進的下一波:

| 波次 | 轉折 | 產生的 OS |
|------|------|-----------|
| 第一波 | 硬體與軟體分離、第一批高階語言 | Unix / POSIX 語義 |
| 第二波 | 雲端運算,跨資料中心與全球的分散式應用 | Kubernetes 及其生態系 |
| 第三波 | AI / agentic 應用 | 待建立 |

她對「作業系統」的定義是雙重的:一層把應用與基礎設施隔開的**抽象**,以及一組應用可以倚賴來取得**韌性、擴展性與效率**的**原語**。AI 應用當然能跑在現有基礎上——問題是現有基礎對這些新挑戰幾乎幫不上忙。

#### 結構性挑戰:開放式指令集(約 00:34:52–00:36:10)

「指令集」在這裡指的是 agent 能對外部世界執行的操作集合。Agent 的指令集是**開放式的**,而且在 runtime 才決定用哪些、怎麼排序。這打破了現有平台的幾個關鍵假設:

- **Zero-trust 安全**變得很難,因為它依賴在**設定時**就理解應用之間的互動模式。
- **復原**變得很難,補償(compensation)與 rollback 這類傳統手法變得難以實作。
- 這些應用在**部署前無法被完整測試**。

再加上兩件事:context 裡**指令與資料沒有分離**(這正是 agent 出現這麼多新型安全威脅的原因),而 agent 之間又是**靠交換 context 溝通**,於是不同 agent 之間的執行隔離也消失了——結果就是韌性與安全問題的 **blast radius 難以控制**。

#### 語義性挑戰:沒有可靠的 error code(約 00:36:15–00:37:30)

這一段她明確接上 Ion Stoica 前一場的主題:

- 我們**無法完整指定 agent 的目標**。用敘述表達「agent 該做什麼」就已經很難,「agent **不**該做什麼」更難;而且仍然缺乏形式化方法來表達與驗證 agent 目標。
- 更糟的是,**AI 模型不擅長回報自己的狀態**——**我們基本上沒有可靠的 error code**。因此判斷 agent 是否正確運作、是否成功、偵測失敗、以及判斷 liveliness(有沒有在推進、是在收斂還是卡住),全都變得很困難。**而如果無法判斷問題是什麼,就無法從中復原。**
- 還有一層語義落差:agent「思考與規劃」的方式,與真實世界介面那種 schema-based、又不斷改版的本質之間對不上,持續製造新錯誤。

#### 今天怎麼解,以及為什麼會收斂(約 00:37:37–00:39:05)

現況是:**全部在應用層以 bespoke 方式處理**。大家做 framework、做 harness,而且數量很多——每隔幾個月就有新的強力 agent 或 harness 出現,證明「解法存在」,但也造成嚴重的碎片化,而且 harness 本身**很難開發**、需要大量專業知識。

她的判斷是:我們**明顯還在實驗階段**,而歷史上每一波創新都經歷過同樣的事——一開始有多種 Unix;容器與 cloud native 時代一開始有各種容器、各種容器編排平台與彼此分歧的生態系;最後產業識別出共同模式、標準化、然後收斂。第一波收斂到 Unix 與 POSIX 語義,第二波收斂到 Kubernetes 與其生態。**AI 時代也會發生同樣的事。**

#### 他們的做法:攔截層與三類 agent(約 00:39:08–00:41:30)

方法論是先看自己組織裡實際在跑的 agent,分成三類:

1. **自建**:用某個 framework 或 SDK 自己實作,完全可控。
2. **知名 harness**:可透過 hook 與 plugin 控制。
3. **黑箱 agent**:什麼都不能改,只能從外部觀察來控制。

他們要建的是一層**攔截層(layer of interception)**,能與這三種風格都整合,並提供**統一的方式來觀察與修改 agent 與外部世界的所有互動**;控制功能就建在這層抽象之上。

第一個攻的問題是**安全,特別是 zero-trust**,做成多層級權限系統:

1. 實作 **identity**,
2. 用該 identity 做帶授權的**委派流程(delegation flows)**,
3. **policy-based access**,
4. 最後是 **intent-based access**——評估 agent 正在做的事是否真的符合使用者目標。

之後往**語義層**延伸:能不能在 agent 之外、以與業務邏輯無關的方式管理 agent 使用的 context?能不能管理 **tool call 的正確性**?能不能做**資料流分析**來理解並控制資料如何流動?這些收在 **Rossoctl** 專案裡(網頁上有更深入的 benchmark 與實驗結果);同事 Maya 當天也有相關海報。

關鍵是:**他們不是要取代既有平台**。所有東西都建在現有雲端平台上,沿用並延伸既有標準——**OAuth 2**、身分用 **SPIFFE**、既有的 policy 語言,在 **Kubernetes** 上編排;gateway 原本基於 **Envoy proxy**,現正轉向基於 **Praxis** 專案、效率更好的 Rust 實作。

成果:context compaction 帶來的**成本下降**(即使對 SOTA agent 也成立)、**tool calling 正確率的穩定提升**(轉化為 agent 品質提升)、以及**透明的權限控管**。

#### 應用模式:serverless(約 00:42:21–00:43:30)

平台演進的另一半是應用模式。她主張 agent 的正確模式是 **serverless**:把 **agent loop 當成無狀態元件**,與(a)管理 context 的 **durable session 儲存**、(b)由多樣化 sandbox 提供的**執行層**分開。好處是韌性、正確性、效能與擴展性都更好。

實測收益:對 **model-bound** 的 agent 可省下大量基礎設施成本;可以**彈性配置 sandbox**(不是每個 agent 都需要最貴的那種,而昂貴的 sandbox 真的很貴);在安全政策允許的情況下還能**重複使用 sandbox**。

結語是一個公開邀請:她相信新一波平台會被建起來,他們已經上路,想聽到同意或不同意的意見,也想跟任何在做同方向的人合作。

### 金句

> "AI applications are without any doubt the most non-deterministic and unreliable component that has ever been introduced in enterprise architectures."(約 00:34:20)

這句話定調了整場演講:不是要修好 AI,而是要為這種不可靠元件設計基礎設施。

> "It's very difficult to express what agents should do … but it's even harder to specify what agent shouldn't do."(約 00:36:26)

與 Ion Stoica 的 requirement gap(omission vs. exclusion)直接呼應。

> "We essentially do not have any reliable error codes."(約 00:36:45)

一句話講完為什麼 agent 的可觀測性與自動復原這麼難。

## English Notes

### TL;DR

- **A third platform wave**: the first wave separated hardware from software and gave us high-level languages; the second was cloud computing and distributed applications across data centers. Each produced an *operating system* — a layer of abstraction separating applications from infrastructure, plus primitives applications can rely on for resiliency, scalability, and efficiency. AI applications are **the most non-deterministic and unreliable component ever introduced into enterprise architectures**, and will need a third such foundation.
- **Two families of challenges**: **structural** — agents have an open-ended instruction set chosen and ordered at run time, which breaks zero-trust security (it depends on knowing interaction patterns at configuration time), traditional recovery (compensation and rollback become intractable), and pre-deployment testability; plus instructions and data aren't separated in context, and agents communicate *by exchanging context*, so execution isolation and blast-radius control are lost. **Semantic** — agent goals can't be fully specified ("should do" is hard, "shouldn't do" is harder), there are no formal methods for expressing or validating them, and models are poor at reporting their own status: **there are no reliable error codes**, so success, failure, and liveliness are all hard to determine — and what you can't diagnose you can't recover from.
- **The approach**: don't replace the platform. Add an **interception layer** on top of existing cloud infrastructure that integrates with all three styles of agent (self-built, well-known harnesses controllable via hooks/plugins, and opaque black boxes) and offers a uniform way to observe and modify every interaction agents have with the outside world. Security — specifically zero trust — came first; semantic-layer control follows. The project is **Rossoctl**.
- **The right application pattern is serverless**: separate the agent loop as a stateless component from durable session storage holding context and from an execution tier of diverse sandboxes — better resiliency, accuracy, performance, and scalability, with measured cost savings.

### Key Points

#### Why a third operating system (~00:33:26–00:34:50)

Steinder frames three waves of application platform evolution: hardware/software separation and the first high-level languages; cloud computing and globally distributed applications; and now AI. Each of the first two produced an operating system — Unix and POSIX semantics for the first, Kubernetes and its ecosystem for the second — where "operating system" means both a layer of abstraction between application and infrastructure *and* a set of primitives applications rely on for resiliency, scalability, and efficiency.

AI applications can certainly run on the existing foundation. The problem is that the existing foundation does almost nothing to help with their novel challenges.

#### Structural challenges: the open-ended instruction set (~00:34:52–00:36:10)

"Instruction set" here means the operations an agent can execute against the external world. That set is open-ended, and agents decide which instructions to use and in what order at run time — which breaks several assumptions existing platforms make:

- **Zero-trust security** depends on understanding interaction patterns between applications a priori, at configuration time.
- **Recovery** techniques like compensation and rollback become intractable to implement.
- These applications are **not fully testable pre-deployment**.

Two more structural problems compound this. Instructions and data are not separated in the context agents work off — which is why so many novel security threats are showing up around agents. And agents communicate by exchanging context, so **execution separation between agents is lost**, making the blast radius of resiliency and security issues very hard to contain.

#### Semantic challenges: no reliable error codes (~00:36:15–00:37:30)

Here Steinder explicitly picks up the thread from Ion Stoica's preceding talk. Agent goals cannot be fully specified: expressing what an agent *should* do in narrative form is hard, specifying what it *shouldn't* do is harder still, and there are no formal methods for expressing or validating those goals.

Worse, the models are bad at reporting their own status — **there are essentially no reliable error codes**. So determining whether an agent is working correctly, whether it is succeeding, detecting its failures, and assessing liveliness (is it making progress and converging, or hanging?) are all hard. And if you can't determine what the problem is, you can't recover from it.

There is also a semantic gap between how an agent thinks and plans versus the schema-based, constantly changing nature of real-world interfaces — a steady source of new errors.

#### How it's solved today, and why it will consolidate (~00:37:37–00:39:05)

Today all of this is handled bespoke, in the application layer. The industry has produced a lot of frameworks and harnesses; every few months a new powerful agent or harness arrives as a proof of existence that a solution is possible. But that creates heavy fragmentation, and harnesses are genuinely hard to build — they demand a lot of expertise.

Her read: we're clearly still in the experimentation phase, and every prior wave looked the same. Multiple versions of Unix at the start; many container runtimes, many orchestration platforms, and divergent ecosystems at the start of the cloud-native era. Eventually the industry identified common patterns, standardized, and consolidated — onto Unix and POSIX, then onto Kubernetes. She expects the same in the AI era.

#### Their approach: an interception layer over three kinds of agents (~00:39:08–00:41:30)

They started from the agents actually running in their own organization, which fall into three buckets: agents they implemented themselves on some framework or SDK (full control); agents built on well-known harnesses (controllable via hooks and plugins); and black-box agents (controllable only by observing from outside).

So they are building a **layer of interception** that integrates with all three styles and provides a uniform way to observe and modify every interaction those agents have with the external world, with control functions layered on top of that abstraction.

Security came first — specifically zero trust, implemented as a multi-tier, multi-layer permission system: establish **identity**; use that identity for **delegation flows with authorization**; then **policy-based access**; and finally **intent-based access**, evaluating whether what the agent is doing actually aligns with the user's objectives.

They have since moved into the semantic layer, asking whether — in a business-logic-independent way, outside the agent — they can control and manage the context agents use, manage the correctness of tool calls, and do data-flow analysis to understand and control how data moves. This is the **Rossoctl** project; their web pages carry deeper benchmark and experiment results, and a colleague (Maya) presented a related poster at the summit.

Crucially, they are **not replacing the existing platform**. Everything is built on existing cloud infrastructure, leveraging and extending existing standards: **OAuth 2**, **SPIFFE** for identity, known policy languages, orchestration on **Kubernetes**. The gateway-based approach was originally built on **Envoy proxy** and is moving to a more efficient Rust-based proxy from the **Praxis** project.

Results so far: cost reduction from context compaction, even with state-of-the-art agents; consistent improvements in tool-calling accuracy that translate into agent quality; and transparent permissioning for agents.

#### The application pattern: serverless (~00:42:21–00:43:30)

The other half of platform evolution is application patterns, and Steinder argues the right pattern for agents is **serverless**: the agent loop as a stateless component, separated from durable session storage where context is managed, and from an execution tier provided by a diverse set of sandboxes. That yields better resiliency, accuracy, performance, and scalability.

Measured benefits: substantial infrastructure cost savings, particularly for model-bound agents; flexible sandbox allocation, since not every agent needs the most expensive sandbox (and those get expensive); and sandbox reuse for agent types where security policy permits it.

She closed with an invitation: she believes this new platform wave is coming, they've started the journey, and she wants to hear from people who agree, disagree, or are working in the same direction.

### Quotes

> "AI applications are without any doubt the most non-deterministic and unreliable component that has ever been introduced in enterprise architectures." (~00:34:20)

The premise of the whole talk: the job isn't to fix the AI, it's to design infrastructure around a component this unreliable.

> "It's very difficult to express what agents should do … but it's even harder to specify what agent shouldn't do." (~00:36:26)

A direct echo of Ion Stoica's requirement gap — omissions versus exclusions.

> "We essentially do not have any reliable error codes." (~00:36:45)

One sentence for why agent observability and automated recovery are so hard.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Rossoctl | IBM Research 的開源 cloud-native agentic 平台 / Agent-OS 原型 | IBM Research's open-source cloud-native agentic platform / Agent-OS prototype | github.com/rossoctl/rossoctl;字幕聽成 "Rosso CTL" |
| Kagenti | Rossoctl 生態中負責 agent 生命週期與 policy 綁定的元件 | Agent lifecycle and policy-binding component in the Rossoctl ecosystem | 演講未點名,見其論文與部落格 / not named on stage; see her paper and blog |
| Praxis | 給 AI workload 用的新網路基礎,輕量 Rust proxy | New network foundation for AI workloads; lightweight Rust-based proxy | 用來取代原本的 Envoy-based gateway / replacing the Envoy-based gateway |
| SPIFFE / SPIRE | 工作負載身分標準,用於 agent 的 zero-trust identity | Workload identity standard used for agents' zero-trust identity | |
| OAuth 2 | 授權標準,用於委派流程 | Authorization standard used for delegation flows | |
| Envoy proxy | gateway 的原始實作基礎 | Original basis of their gateway implementation | |
| "Towards an Agent Operating System – Lessons from Classical and Cloud OS" | 對應本演講的論文(Steinder & Franke),提出 13 個 Agent-OS 原語 | The paper behind this talk (Steinder & Franke), proposing thirteen Agent-OS primitives | arXiv 2607.25076;演講未點名 / not named on stage |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Grace A. Steiner(主持人介紹)| Gosia Steinder |
| Rosso Rosso CTL | Rossoctl |
| project Praxis | Praxis(專案名) |
| SPIFFE(字幕作 "SPIFFE" 但發音模糊)| SPIFFE |
| Ion Stoica(字幕正確)| — |
| liveliness | liveness(語意上為系統活性;講者口語說 liveliness) |
| durable session lock | durable session store(依上下文為儲存 context 的持久化 session 層) |

## 待確認 / To Verify

- 同事「Maya」的全名與海報題目未在字幕中出現。/ The full name and poster title of the colleague "Maya" don't appear in the captions.
- 「cost reduction from context compaction」「consistent improvements to tool calling accuracy」的具體數字未在演講中給出(她指向專案網頁)。/ No numbers were given on stage for the context-compaction cost reduction or tool-calling accuracy gains; she pointed to the project's web pages.
- 演講中提到的 "known policy languages" 未點名具體是哪些(Rego/OPA?Kuadrant?)。/ The "known policy languages" were not named (Rego/OPA? Kuadrant?).
- durable session 層與 sandbox 執行層的具體實作未展開。/ The concrete implementations of the durable session tier and sandbox execution tier were not detailed.
