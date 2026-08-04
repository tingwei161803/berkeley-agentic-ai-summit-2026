---
title: "Is Kubernetes Good for Agents? Infrastructure Solutions for Agent-Shaped Problems"
title_zh: "Kubernetes 適合跑 Agent 嗎?為 Agent 形狀的問題找基礎設施解法"
speaker: "Tim Hockin"
affiliation: "Distinguished Engineer, Google"
type: talk
stage: Compass
date: 2026-08-01
session: "Session 1: AI Systems"
video: "https://www.youtube.com/watch?v=IBpR4uYftLY&t=2653s"
video_range: "00:44:13–00:55:30"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 1st - Morning Session [DownSub.com].srt"
status: draft
tags: [kubernetes, sandboxing, agent-runtime, infrastructure, open-source]
---

# Kubernetes 適合跑 Agent 嗎?為 Agent 形狀的問題找基礎設施解法(Is Kubernetes Good for Agents? Infrastructure Solutions for Agent-Shaped Problems)

**一句話總結**:Agent 是 bursty、不可信、單租戶、又對延遲敏感的工作負載,恰好違反 Kubernetes「長時間執行、可水平擴展、可攤平開銷」的設計前提;Google 的開源專案 **Agent Substrate** 不重造 Kubernetes,而是在其上加一層積極 suspend/resume 的 actor 執行層,把「幾秒到幾十分鐘的閒置」壓成「幾百毫秒的喚醒」。
**One-line summary**: Agents are bursty, untrusted, single-tenant, and latency-sensitive — precisely the opposite of what Kubernetes was designed for. Google's open-source **Agent Substrate** doesn't rebuild Kubernetes; it layers an aggressively suspend/resume-based actor runtime on top, turning tens of seconds to tens of minutes of idle into sub-second wake-ups.

## 中文筆記

### TL;DR

- **Agent 為什麼不適合 Kubernetes**:agent 工作負載 **bursty**(短暫爆發後閒置數分鐘、數小時甚至數週)、**不可信**(必須跑在 sandbox 裡)、**單租戶**(sandbox 不能共用,否則失去意義,因而失去攤平開銷的機會)、且**有人在迴圈裡**(對感知延遲極度敏感)。Kubernetes 是為「跑很久、可水平擴展、開銷可攤平」的東西設計的。
- **現況只有兩種模式**:(1) 用 Kubernetes 的 **runtime class**(預設是 OCI 容器,也有 gVisor 與 microVM)為每個使用者 session 開一個 sandbox pod——但 pod 啟動要數秒,加上 agent 自身的初始化可能再花 10–15 秒以上,於是大家用「閒置等待」來攤平,等待時間從數十秒到數十分鐘不等,期間資源完全浪費。(2) **DIY**:每台機器一個巨型 workload、內含 manager,自建控制平面排程進這個 mega sandbox——效率可以很高,但等於重新發明大半個 Kubernetes,對小公司與新創幾乎無法維運。
- **Agent Substrate**:Google 今年開始並已開源的專案,取兩種模式的優點——用 suspend/resume 加雲端儲存,把 agent 多工到**預熱好的 worker** 上,**積極地暫停與恢復**,把 5–10 秒到 10 分鐘的閒置壓到一秒甚至更少。目標規模是**數十億個 session**、每秒**上萬次 activation**、喚醒時間壓到**低三位數毫秒**。目前仍是 pre-production,目標是這個秋天進入可用狀態。

### 重點整理

#### Agent 工作負載為什麼「形狀不對」(約 00:45:30–00:46:40)

Hockin 說自己習慣從基礎設施由下往上看這個問題:客戶帶著「我們有一堆 agent,要跑很多、而且現在的效率不夠」來找他。Agent 與傳統應用的差異有四點:

1. **Bursty**:短暫爆發後閒置很久——數分鐘、數小時,甚至數天數週。天真做法會導致大量閒置資源。
2. **通常不可信**:因此必須跑在 sandbox 裡,而業界也持續在找新的 sandbox 技術。
3. **單租戶**:sandbox 不能共用,不然就失去意義。**這代表失去大量最佳化機會,特別是開銷的攤平(amortization of overheads)。**
4. **人在迴圈裡**:因此對系統的**感知延遲**非常敏感。

而 Kubernetes 是為「跑很久、水平擴展、成本可攤平」的東西建的。所以「Kubernetes 是不是跑 agent 的正確平台」是一個公道的問題。

#### 現有的兩種做法(約 00:46:40–00:49:50)

**做法一:直接用 Kubernetes 的 runtime class**

Kubernetes 的 runtime class 讓你定義一種 sandbox:預設是 Docker 式的 OCI 容器,也有 **gVisor** 與 **microVM** 的 runtime class,而且它是 Kubernetes 的**擴充點**,適合做研究。

流程:某個事件(例如使用者開啟一個 chat session)觸發需要一個新的 agent 實例 → 為他建立專屬的單租戶 sandbox pod。但 pod 啟動**不是 Kubernetes 最快的事**——通常是「秒」等級,而這不夠快;再加上 agent 啟動時要做的事(載入 runtime 環境、瀏覽器等),可能再花 10 到 15 秒以上。Pod ready 後使用者送出訊息、拿到回覆,一個 turn 結束——然後呢?

因為 pod 啟動不免費,大家的做法是**等下一個事件**。等多久?取決於你的 agent 在做什麼、啟動成本多高,每家算出來的數字都不一樣;他們看到的範圍是**低到數十秒、高到數十分鐘**。在這段時間裡,agent 佔著誰都用不到的資源。可能在第 9 分 59 秒來了下一個 turn,整個流程重來一次。最後 timeout、判定為 idle,要嘛整個丟棄、要嘛存下狀態然後終止 pod。

**而這件事,是對系統上每一個使用者的每一個 agent 的每一個實例都在發生。** 有 warm pool、有 suspend/resume 之類的技巧,但 **Kubernetes 原生不支援這些**,等於在跟系統作對,規模一大就很難自圓其說。

**做法二:在 Kubernetes 上自建(DIY)**

每台機器一個巨型 workload,裡面是一個 manager application;自建的控制平面負責把東西排程進那個 mega sandbox,manager 管生命週期。對 Kubernetes 而言一切都是不透明的,**你會重新發明 Kubernetes 的一大部分**。它可以非常有效率,但建起來相當複雜,對小公司特別是新創來說**難以維運**。

#### Agent Substrate:兩種模式的交集(約 00:49:50–00:55:00)

Hockin 說他做 Kubernetes 12 年,深信「**在基礎設施這件事上,開放的一定會贏**」。所以今年他們著手做一個新東西,取兩種模式的優點:能用 Kubernetes 的地方就用(幾乎所有人的機隊裡都有一些 Kubernetes),需要新元件的地方才自己建。他很坦白:**這裡沒有石破天驚的新研究**,他們做的是把客戶與使用者身上最好的點子黏成一個大家都能用的東西。

專案名為 **Agent Substrate**,已開源。核心模型很直接:**不要閒置資源**;用 suspend/resume 加雲端儲存,把 agent 多工到**預熱好的 runner** 上,並**積極地暫停與恢復**,把 5–10 秒到 10 分鐘的閒置壓到一秒或更短。

**目標(Google 式的大規模視角)**:數十億個 session 在管理之下、每秒數千到數萬次 activation、喚醒時間壓進**低三位數毫秒**。

**術語**:

| 術語 | 說明 |
|------|------|
| **Actor** | agent / sandbox / 行為像 agent 的東西的統稱 |
| **Actor template** | 「如果 actor 是餅乾,template 就是餅乾模具」;定義例如用哪種 sandbox 技術(gVisor 或 microVM)。**單一 substrate 內可以有很多種 template** |
| **Worker** | 通常是 Kubernetes 叢集裡的一個 pod,**真正消耗資源的東西**;等待被指派 actor,然後執行它,可以序列執行很多個;一個叢集可以有很多 worker |
| **atelet** | 每個節點上的 worker 管理器(networking 的緣故需要它) |
| **atenet** | 「enlightened proxy」,收到流量時觸發喚醒 |

**運作流程**:從任一現代 Kubernetes 叢集開始(支援 **kind**,所以筆電上就能跑)。叢集管理員部署一個 Agent Substrate 實例:API server 與儲存層、負責與 Kubernetes 同步資料的 controller、一個或多個 worker pool(建立 deployment→pod 來跑你的工作負載)、管理 worker 的 atelet、以及知道怎麼把外部流量帶進內部的 atenet proxy。接著 substrate 管理員建立一個或多個 actor template,controller 看到後做預備工作:把 template 啟動起來、**拍一份快照(他們稱為 golden snapshot)**存起來備用。

到 substrate 層(他提醒**其中一部分還是 aspirational,仍在開發中**):由更上層的系統從 template **建立**一個 actor(注意:建立 actor 不等於執行 actor)。以聊天應用為例,前端做完授權等工作後建立 actor;使用者送出 prompt → 路由到 atenet proxy → **喚醒 actor**,透過 router 送訊息把它指派給一個 worker → 因為是新 actor,就從 **golden snapshot** 喚醒 → proxy 把訊息轉給現在已在執行的 actor。**這整個過程只要幾百毫秒**,而且還在繼續優化。

Turn 一結束,actor 大概就閒置了,於是叫它回去睡覺——他們稱為 **pause**:拍快照、把資料搬走,worker 隨即解除指派、可供其他 actor 使用。這些都能以「一次 API 操作 / 一次 agent transaction」的速度發生。下一個 prompt 進來就再跑一次循環;最後沒有訊息了,資料會被搬到雲端儲存,「睡到明天」。

從最高層看:一個 Kubernetes 叢集可以是筆電上的單節點,也可以是雲端的 20 萬節點;每個節點跑多個 worker;而**每個 agent 有 99.999% 的時間是閒置的**——算一下就知道為什麼能衝到「數十億」那個數量級。

#### 現況與邀請(約 00:55:00–00:55:30)

Agent Substrate 是**開源專案**,目前仍是 **pre-production grade**,他們的目標是**這個秋天結束前**進入可用狀態。他要的回饋很具體:**經驗、需求,以及你們拿 agent 在做什麼的脈絡**。

### 金句

> "Kubernetes was built for things that run for a long time and tend to be scale out, horizontally scalable, and you can amortize your costs."(約 00:46:29)

一句話說完為什麼 agent 的形狀跟 Kubernetes 不合。

> "I have a deeply held belief that when it comes to infrastructure, open always wins."(約 00:49:56)

做了 12 年 Kubernetes 的人給 Agent Substrate 開源的理由。

> "Each of those agents are idle 99.999% of the time, so you can do the math and see we're driving up to those billions of numbers."(約 00:54:50)

這個數字就是整套 suspend/resume 設計的經濟學基礎。

## English Notes

### TL;DR

- **Why agents fit Kubernetes badly**: agent workloads are **bursty** (short spurts, then idle for minutes, hours, or weeks), generally **untrusted** (so they must run in sandboxes), necessarily **single-tenant** (you can't share a sandbox without defeating its purpose, which kills amortization of overheads), and **human-in-the-loop** (so they're very sensitive to perceived latency). Kubernetes was built for long-running, horizontally scalable things whose costs amortize.
- **Only two patterns exist today**: (1) Kubernetes **runtime classes** — the default OCI container, plus gVisor and microVM classes — with one sandbox pod per user session. Pod startup takes seconds, agent startup can add 10–15 seconds or more, so operators keep pods idling anywhere from tens of seconds to tens of minutes, burning resources nobody else can use. (2) **DIY**: one giant per-machine workload containing a manager, with a bespoke control plane scheduling into a mega sandbox — efficient, but you reinvent large parts of Kubernetes and it's hard for smaller companies to operate.
- **Agent Substrate**: Google's open-source project, started earlier this year, takes the best of both — suspend/resume plus cloud storage to multiplex agents onto pre-warmed runners and aggressively suspend them, driving 5–10 seconds to 10 minutes of idle down to a second or less. Targets: billions of sessions under management, thousands to tens of thousands of activations per second, and wake-up times in the low three-digit milliseconds. Still pre-production, aiming for a workable state by the end of the fall.

### Key Points

#### What makes agents infrastructure-shaped differently (~00:45:30–00:46:40)

Hockin looks at agentic AI bottom-up, as an infrastructure problem. Customers arrive saying "we have these agents, we need to run a lot of them, and we're not getting the efficiency." Four properties matter:

1. **Bursty** — very short spurts, then idle for minutes, hours, days, or weeks. Handled naively, that's a lot of idle resources.
2. **Untrusted** — so they run in sandboxes, and new sandboxing technologies keep appearing.
3. **Single-tenant** — you can't share a sandbox without defeating the purpose, which means losing a ton of optimization opportunities, specifically **amortization of overheads**.
4. **Human-in-the-loop** — making them very sensitive to perceived latency.

Kubernetes, by contrast, was built for long-running, horizontally scalable workloads whose costs amortize. So asking whether it's the right platform for agents is a fair question.

#### The two patterns in the wild (~00:46:40–00:49:50)

**Pattern one: Kubernetes runtime classes.** A runtime class defines a kind of sandbox — the default being a Docker-style OCI container, with classes for gVisor and microVMs, and it's an extension point, so there's room for research. Some event (a user starting a chat session) requires a new agent instance, which means a dedicated single-tenant sandbox pod.

Starting a pod is not the thing Kubernetes does fastest — it's seconds, which isn't fast enough — and depending on what the agent does at startup (loading runtime environments, browsers), it can take 10 or 15 seconds more. Once the pod is ready the user chats, one turn completes, and then what? Since pod startup isn't free, people wait for another event. How long? It depends on the agent and the startup cost, and it's different for everyone; Hockin has seen **tens of seconds at the low end to tens of minutes at the high end**. Through all of that the agent holds resources nobody else can use. The next turn might land at 9:59, restarting the whole cycle; eventually a timeout declares it idle and the pod is discarded or its state saved and terminated.

And this is happening for every instance of every agent for every user on the system. Warm pools and suspend/resume tricks exist, but **Kubernetes doesn't support them natively**, so you're working around the system — hard to justify at scale.

**Pattern two: DIY on Kubernetes.** A giant workload per machine, containing a manager application; a bespoke control plane schedules into that mega sandbox and the manager handles lifecycle. Everything is opaque to Kubernetes, and you end up reinventing large parts of it. Very efficient, fairly complicated to build, and difficult to operate — especially for startups.

#### Agent Substrate (~00:49:50–00:55:00)

Twelve years into Kubernetes, Hockin holds "a deeply held belief that when it comes to infrastructure, open always wins." So earlier this year they set out to build something taking the best of both models — leaning on Kubernetes where possible, since nearly everyone has some in their fleet, and building new components where necessary. He's explicit that there's **no earth-shaking research here**: they took the best ideas from their customers and users and glued them into something everyone can use.

**Agent Substrate** is that project, and it's open source. The model: no idle resources. Use suspend/resume plus cloud storage to multiplex agents onto pre-warmed runners and aggressively suspend and resume them, driving 5–10 seconds to 10 minutes of idle down to a single second or less.

Goals, from a Google-scale vantage point: billions of sessions under management, thousands to tens of thousands of activations per second, and wake-up time in the low three-digit milliseconds.

**Vocabulary**: an **actor** is the stand-in term for an agent, sandbox, or agent-like thing. An **actor template** is the cookie cutter to the actor's cookie — it carries details like which sandbox technology (gVisor or microVM), and a single substrate can hold many different templates. A **worker** is usually a pod in a Kubernetes cluster and is the thing that actually consumes resources; it waits for an actor assignment, runs it, and can run many in serial, with many workers per cluster. **atelet** is the per-node manager for all workers on that node (needed for networking reasons), and **atenet** is their "enlightened proxy," which triggers wake-ups on receipt of traffic.

**How it fits together**: start with any modern Kubernetes cluster — kind is supported, so it runs on a laptop. The cluster admin deploys an Agent Substrate instance: API server and storage layer, a controller that synchronizes data in and out of Kubernetes, one or more worker pools (which create deployments, which create pods), atelets to manage the workers, and the atenet proxy that moves traffic from outside to inside. The substrate admin then creates actor templates; the controller spins each one up, takes a **golden snapshot**, and stores it for later.

At the substrate layer (Hockin warned that **some of this is aspirational and still being built**), a higher-order system creates an actor from a template — note that creating an actor doesn't run it. In a chat app, the front end does its authorization work and creates the actor. The user sends a prompt, which routes to the atenet proxy; the proxy wakes the actor and assigns it to a worker via the router; since this actor is new, it wakes from the golden snapshot; the proxy forwards the message to the now-running actor. **The whole thing happens in a couple hundred milliseconds**, and they're still optimizing.

As soon as the turn is done the actor is probably idle, so they **pause** it: take the snapshot, shuffle the data off, and the worker becomes unassigned and available to another actor — all at the speed of a single API operation or agent transaction. The next prompt restarts the cycle; when messages stop, the data goes to cloud storage and the actor sleeps for the night.

From the top: a Kubernetes cluster can be one node on a laptop or 200,000 nodes in the cloud, each node runs multiple workers, and **each agent is idle 99.999% of the time** — which is how the arithmetic reaches billions.

#### Status and ask (~00:55:00–00:55:30)

Agent Substrate is open source and still pre-production grade; they're working hard to have it in a workable state by the end of the fall. The most useful feedback they can get, he said, is experience, requirements, and context about what people are actually doing with agents.

### Quotes

> "Kubernetes was built for things that run for a long time and tend to be scale out, horizontally scalable, and you can amortize your costs." (~00:46:29)

The whole mismatch in one sentence.

> "I have a deeply held belief that when it comes to infrastructure, open always wins." (~00:49:56)

Twelve years of Kubernetes, applied as the rationale for open-sourcing Agent Substrate.

> "Each of those agents are idle 99.999% of the time, so you can do the math and see we're driving up to those billions of numbers." (~00:54:50)

The economics behind the entire suspend/resume design.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Agent Substrate | Google 主導的開源 agent 執行層,在 Kubernetes 上做 actor 的 suspend/resume 多工 | Google-led open-source agent runtime multiplexing actors on Kubernetes via suspend/resume | github.com/agent-substrate/substrate;演講中請大家去該 URL 看 GitHub |
| atelet | 每節點的 worker 管理器(DaemonSet),協調快照與狀態轉移 | Node-level DaemonSet supervising worker pods, coordinating snapshotting and state transfer | 字幕聽成 "Eightlet" |
| atenet | 網路控制器 / enlightened proxy,收到流量時觸發喚醒 | Networking controller and "enlightened proxy" that triggers wake-ups on traffic | 字幕聽成 "Eightnet" / "8net" |
| Kubernetes runtime class | 定義 sandbox 種類的擴充點(OCI / gVisor / microVM) | Kubernetes extension point defining sandbox kinds (OCI / gVisor / microVM) | |
| gVisor | 使用者空間核心式 sandbox | User-space-kernel style sandbox | Agent Substrate 的 actor template 選項之一 |
| kind (Kubernetes in Docker) | 讓 Agent Substrate 能在筆電上跑 | Lets Agent Substrate run on a laptop | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Eightlet | atelet |
| Eightnet / 8net proxy | atenet(proxy) |
| Agentyc AI / Agentyc workloads | Agentic AI / agentic workloads |
| Tim Hockin(字幕正確)| — |
| "gVisor"(字幕作 "gVisor")| gVisor |

## 待確認 / To Verify

- Agent Substrate 的 GitHub URL 在投影片上,字幕只說「go to this URL」;對照公開 repo 應為 github.com/agent-substrate/substrate,建議看投影片確認。/ The GitHub URL was on a slide but the captions only say "go to this URL"; the public repo appears to be github.com/agent-substrate/substrate — confirm against the slide.
- 「the end of this fall」指的是 2026 年秋天(演講時間為 2026-08),但未明說年份。/ "The end of this fall" presumably means autumn 2026 (talk given 2026-08) but the year wasn't stated.
- 演講中未說明 golden snapshot 的底層 checkpoint/restore 技術(CRIU?gVisor checkpoint?)。/ The underlying checkpoint/restore technology behind the golden snapshot (CRIU? gVisor checkpoint?) wasn't named.
- 「billions of sessions / tens of thousands of activations per second」是設計目標而非已達成的實測值。/ The billions-of-sessions and tens-of-thousands-of-activations figures are design targets, not measured results.
