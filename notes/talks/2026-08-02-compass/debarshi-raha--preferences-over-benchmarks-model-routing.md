---
title: "Preferences > Benchmarks: Model Routing for How Teams Actually Build"
title_zh: "偏好勝過 Benchmark:貼合團隊真實開發方式的模型路由"
speaker: "Debarshi Raha"
affiliation: "VP & Fellow Engineer, DigitalOcean"
type: keynote
stage: Compass
date: 2026-08-02
session: "Session 4: Agent Evaluation & Benchmarks"
video: "https://www.youtube.com/watch?v=1UrriPJRSPU&t=6089s"
video_range: "01:41:29–01:58:39"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [model-routing, cost-optimization, inference, open-source, evaluation]
---

# 偏好勝過 Benchmark:貼合團隊真實開發方式的模型路由(Preferences > Benchmarks: Model Routing for How Teams Actually Build)

**一句話總結**:公開 leaderboard 不知道你的成本上限、延遲容忍度與資料集,所以模型路由不該照 benchmark 排名硬選,而該把「你的偏好」編碼進一個伺服器端、專用小模型驅動的 router,即時依成本與延遲重排候選模型——DigitalOcean 用開源的 Plano + 30B 專用路由模型做到延遲 <200ms、零客戶端改動、且完全免費。
**One-line summary**: Public leaderboards know nothing about your cost ceiling, your latency budget, or your data, so model routing shouldn't follow benchmark rankings — it should encode *your preferences* into a server-side router driven by a purpose-built small model that reranks candidates on live cost and latency; DigitalOcean's open-source Plano plus a 30B routing model does this at under 200ms, with zero client-side code changes, for free.

## 中文筆記

### TL;DR

- **成本已經是 agentic AI 的頭號痛點,而且是「現在進行式」**:講者舉 Uber 四個月燒完整年 agentic AI 預算、Walmart 開始設 AI 支出上限為例;他在 AWS 看著雲成本優化花了好幾年才變成一門正式學科(FinOps),但這一輪只花一兩年就發生了。
- **真正的原因不是貴,是「不合身」(fit)**:不是每個 request 都需要 frontier model。分類/標註用小模型、寫作/摘要/翻譯用中小模型、程式碼生成用中型、科學推理/醫療/資安分析才需要 frontier。
- **第三個理由是風險**:只綁一個模型,那個模型掛掉或品質退化,你整個應用就跟著陪葬。
- **路由要編碼「偏好」而非 benchmark 分數**:成本上限、延遲容忍度、prompt、工具⋯⋯這些都是動態的,而且沒有任何公開 leaderboard 會告訴你。所以要把它們編進 router,即時重排,而不是「benchmark 說這模型最強所以永遠送它」。
- **架構是伺服器端的 Plano proxy + 30B 專用路由模型**,兩者都開源、無 vendor lock-in;因為只為路由這一件事訓練,它在路由任務上贏過 GPT-5 系列等 frontier 模型。加上約 200ms 以下延遲、零客戶端改動、免費。
- **用 LLM 當 router 是在繳「雙重稅」**:多約 600ms 延遲、又多付一次 token 費用。專用系統才是對的抽象層。

### 重點整理

#### 講者與 DigitalOcean 的定位(約 01:43)

Debarshi Raha 是 DigitalOcean 的 Fellow Engineer,一年前加入,負責 data 與 AI;在此之前長期任職 AWS,從零打造過 OpenSearch 等基礎服務與多項 ML 服務。

DigitalOcean 定位為 cloud-native、AI-native 的全端雲:從底層的 compute / storage / networking,往上到資料與學習層、再到 managed agents。**inference router 就坐在中間的 inference 層**,而這個位置意味著它會影響上面所有東西。

自 inference 服務推出以來已上架 **70+ 模型**,包含近期霸榜的 Kimi K3 與 Claude Opus 5。講者說得很直白:「這些模型很棒,我很愛它們,但有一個問題——成本。」

#### 三個問題:成本、fit、風險(約 01:44–01:45)

1. **成本**:每個任務都送 frontier model,帳單非常可觀。他舉了兩個業界案例:Uber 在四個月內就燒光整年的 agentic AI 預算;Walmart 開始對 AI 支出設上限。「每家公司都感受到了。」
2. **fit(最主要的原因)**:你根本不需要用 frontier model 服務每一個 request。很多任務用小模型或中型模型就綽綽有餘。
3. **風險(營運面)**:如果你只依賴單一模型,那個模型一旦下線或品質退化,你的整個應用就暴露在風險裡。

他把任務對應到模型層級:

| 任務類型 | 建議模型層級 |
|---------|------------|
| 分類 / 標註 | 小模型即可 |
| 寫作 / 摘要 / 翻譯 | 小到中型 |
| 程式碼生成 | 中型 |
| 科學推理、醫療、資安分析 | frontier |

#### Inference Router:坐在 client 與 server 之間(約 01:47–01:48)

Router 放在**伺服器端**,夾在 client 與模型之間。你不需要在程式碼裡硬寫「哪個任務用哪個模型」,也不需要自己從頭打造路由系統——你只要定義「哪一類任務要用哪些模型」,router 就會帶著即時回饋(當下延遲、模型可用性、成本)聰明地路由過去。

**實際效益**:一家加拿大的法律 AI 新創(訂閱制、AI + human-in-the-loop 提供法律諮詢)看到 **40–50% 的推論成本下降**;講者說實務上最高可以砍到 **80%**,而且不犧牲模型能力與輸出品質。

#### 「這是這個世代的 FinOps」(約 01:48–01:49)

他從 AWS 的經驗做對比:雲端成本優化花了很久才變成一門真正的學科,尤其在 COVID 期間大家才卯起來省。**但這一輪不用等——它此刻正在發生**,一兩年內就看到巨大轉變。這是他認為 router 正在變成 stack 中最重要一環的理由。

#### 直覺:router 到底該根據什麼決策(約 01:49–01:50)

除了 prompt 和工具之外,你還必須把兩件事算進來:**你願意付的成本**與**你的應用能忍受的延遲**。關鍵在於——**這些都是動態的,不是靜態的,而且沒有任何公開 leaderboard 或 benchmark 會告訴你**。

所以必須把這些偏好編碼進 router,做即時的智慧路由,而不是「benchmark 說這個模型對這個任務最強,所以我盲目送過去」。這就是講題「Preferences > Benchmarks」的核心。

#### 系統架構:Plano + 30B 專用路由模型(約 01:50–01:51)

- **Plano**:中間的 proxy。所有請求先進 Plano,Plano 轉給路由模型拿結果,然後**重排(rerank)**候選模型——依你設定的成本與延遲偏好,對這個任務的候選模型集動態排序。
- **路由模型**:一個 **30B 參數、專為路由任務打造**的模型。因為只為這件事訓練,**它在路由任務上贏過 GPT-5 系列等 frontier 模型的 benchmark**。
- **兩者都是開源的**,沒有 vendor lock-in——你可以自行 host,甚至貢獻程式碼。
- Plano 支援接多個系統的 observability。這裡接的是 DigitalOcean 的 inference 系統,但你可以接自己的,靠即時 metrics 來重排與路由。

#### 為什麼不用其他做法:靜態路由與 LLM 路由(約 01:51–01:52)

- **靜態路由**:在首頁放按鈕,「摘要」永遠送這個模型、「翻譯」永遠送那個。太靜態,而且每次有新模型或新任務類別都得改 client。
- **用另一個 LLM 決定路由**:你在繳**雙重稅**——延遲多約 **600ms**,而且要為路由這件事再付一次 frontier model 的錢。
- **他們的做法**:專用系統、伺服器端、延遲 **200ms 以下**、**零額外成本**。伺服器端還帶來一個好處:新增模型或新任務類別時,**完全不用動 client**,改設定就好。

#### 操作方式與 eval(約 01:53–01:54)

- 用**自然語言**定義路由規則。
- 提供 **preset**:根據公開 benchmark 與任務專屬 benchmark,先幫你決定每類任務的候選模型集,你可以從 preset 起步再自行調整。
- **接上你自己的 eval**:平台附評估框架,重點是「用你公司、你任務需要的資料集,不是別人的公開 leaderboard」。跑完確認 router 在你的資料上運作正常;不行就回頭調,形成微調迴圈。

#### Cache-aware routing(約 01:54–01:55)

這是他因時間不足而快速帶過、但強調「你一定要考慮」的一點:在 agentic 系統裡(自動探索程式碼、分析、改寫的迴圈),**每一輪有大量重複的 prompt**。如果你在 session 中途突然換模型,**就會丟掉原本已經暖起來的 cache**。所以路由必須是 cache-aware 的。這是他們目前正在做的部分。

#### Demo 與快速事實(約 01:55–01:57)

現場 demo 因會場 Wi-Fi 故障沒能跑起來(流程是:建立 router → 命名 → 加任務,例如選 preset 的 summarization → 儲存 → 一鍵在 playground 啟動並與其他模型對比)。他口頭轉述了會前實測的結果:**router 比 Opus 5 便宜約 20 倍,且任務完成快約 67%**。

快速事實整理:

- 專用路由模型,**30B**
- 伺服器端只增加 **≤200ms** 延遲
- **零應用程式碼改動**
- **完全免費**——沒有 LLM-as-router 的那種「延遲 + 成本」雙重稅
- 可用 DigitalOcean 託管,也可自行 host

#### Roadmap:personalization(約 01:57–01:58)

他本人過去做過 personalization 服務,對這塊最興奮。意思是:**你用得越多,router 就越好**。只要打開 log 與 traces,所有回饋進入持續迴圈、再對照 eval 檢查,router 就會自己持續改善——**你端不用蓋任何東西,它自己在進步**。這是他想留給聽眾的最後一句。

### 金句

> "You do not need a frontier model to serve every single of the request."(約 01:45)

整場演講的前提:貴不是問題,不合身才是。

> "Now those no public leaderboard or public benchmark tell you. So you need to encode those in the router."(約 01:49)

成本上限與延遲預算是你的,不是 leaderboard 的——所以路由邏輯必須由你的偏好驅動。

> "You are paying double the tax … you are increasing the latency by around 600 milliseconds or so. In addition, you are also paying more."(約 01:52)

用 LLM 當 router 的代價:延遲與費用兩頭都要繳。

> "Without doing anything, you're not building anything on your side. Without doing anything, the router is improving."(約 01:57)

路由層一旦有了 log、traces 與 eval 迴圈,改善就變成預設行為而非專案。

## English Notes

### TL;DR

- **Cost is the number-one pain in agentic AI right now — and it arrived fast.** Raha cited Uber burning a full year's agentic AI budget in four months and Walmart capping AI spend. At AWS he watched cloud cost optimization take years to become a real discipline (FinOps); this time the same shift happened in one or two years.
- **The root cause isn't price, it's fit.** Not every request needs a frontier model: classification and labeling run fine on small models, writing/summarization/translation on small-to-medium, code generation on medium; only scientific reasoning, medical, and security analysis genuinely need frontier depth.
- **A third reason is risk.** Betting the whole application on a single model means a single outage or quality regression takes the app down with it.
- **Routing should encode preferences, not benchmark scores.** Your cost ceiling, latency tolerance, prompts, and tools are all dynamic — and no public leaderboard knows any of them. Encode them in the router and rerank live, instead of blindly shipping every request to whatever tops a benchmark.
- **The architecture is a server-side Plano proxy plus a 30B purpose-built routing model**, both open source with no vendor lock-in. Because it is trained for routing and nothing else, it beats frontier models (GPT-5 series among them) on the routing task — at under 200ms added latency, zero client code changes, and no cost.
- **Using an LLM as your router means paying a double tax**: roughly 600ms extra latency *and* another round of token spend. A purpose-built system is the right abstraction.

### Key Points

#### Speaker and DigitalOcean's position in the stack (~01:43)

Raha is a Fellow Engineer at DigitalOcean, joined about a year ago, working on data and AI. Before that he spent a long stretch at AWS building foundational services like OpenSearch and several ML services from the ground up.

DigitalOcean positions itself as a cloud-native, AI-native full-stack cloud: compute, storage, and networking at the bottom, data and learning above that, managed agents on top. **The inference router sits in the middle, at the inference layer** — a position that means it affects everything above it.

Since the inference service launched they've onboarded **70+ models**, including the recently leaderboard-topping Kimi K3 and Claude Opus 5. His framing was blunt: "those are amazing models, I love them, but there is one problem, which is cost."

#### Three problems: cost, fit, risk (~01:44–01:45)

1. **Cost** — routing every task to a frontier model produces enormous bills. Two industry data points: Uber exhausted an entire year's agentic AI budget within four months; Walmart is capping AI spend. "Every company is feeling that."
2. **Fit (the top reason)** — you simply don't need frontier capability for every request; a small or medium model serves many tasks perfectly well.
3. **Risk (the operational one)** — depending on one model puts your whole application at the mercy of that model's availability and quality.

His task-to-tier mapping:

| Task type | Model tier |
|-----------|-----------|
| Classification / labeling | Small model |
| Writing / summarization / translation | Small to medium |
| Code generation | Medium |
| Scientific reasoning, medical, security analysis | Frontier |

#### The inference router: between client and server (~01:47–01:48)

The router lives **server-side**, between the client and the models. You don't hardcode which model serves which task, and you don't build the routing system yourself — you declare which class of task should draw on which models, and the router dispatches intelligently using live signals: current latency, model availability, and cost.

**Results in the field**: a Canadian legal-AI startup (subscription legal advice combining AI with human-in-the-loop) is seeing a **40–50% reduction in inference cost**. Raha said reductions of up to **80%** are achievable in practice, without losing model capability or output quality.

#### "This is the new FinOps" (~01:48–01:49)

He drew the comparison to his AWS years: cloud cost optimization took a long time to mature into a discipline, and the big push came during COVID. **This time there's no waiting — it's happening as we speak**, with a massive shift inside one or two years. That's why he thinks the router is becoming the most important part of the stack.

#### The intuition: what should a router actually decide on? (~01:49–01:50)

Beyond the prompt and the tools, two things must enter the decision: **the cost you're willing to spend** and **the latency your application can tolerate**. The crucial observation is that **these are dynamic, not static — and no public leaderboard or benchmark tells you anything about them**.

So they have to be encoded into the router and applied in real time, rather than blindly routing to whatever some benchmark declares best for a task. That's the whole thesis behind "Preferences > Benchmarks."

#### Architecture: Plano plus a 30B purpose-built routing model (~01:50–01:51)

- **Plano** is the proxy in the middle. Requests hit Plano, Plano consults the routing model, then **reranks** the task's candidate model set against your cost and latency preferences — fully dynamically.
- **The routing model** is **30B parameters, purpose-built for routing only**. Because it's trained for exactly this task, **it beats frontier models — GPT-5 series included — on the routing benchmark**.
- **Both Plano and the routing model are open source**: no vendor lock-in, self-hostable, contributions welcome.
- Plano supports observability from multiple systems. Here it plugs into DigitalOcean's inference system, but you can plug in your own and feed it live metrics to drive reranking.

#### Why not the alternatives — static routing and LLM routing (~01:51–01:52)

- **Static routing**: buttons on your homepage where "summarization" always goes to one model and "translation" to another. Too static, and every new model or task category means changing the client.
- **Using another LLM to decide the route**: you're **paying a double tax** — roughly **600ms** more latency, plus paying frontier model prices just to make a routing decision.
- **Their approach**: purpose-built, server-side, **under 200ms**, **no additional cost**. Server-side placement also means adding a model or a task class is a configuration change, **never a client change**.

#### Operating it, and plugging in your own eval (~01:53–01:54)

- Routing rules are declared in **natural language**.
- **Presets** ship on top: using public benchmarks plus task-specific benchmarks, they pre-select a candidate model set per task class so you can start somewhere sensible and adjust from there.
- **Plug in your own eval.** The platform includes an evaluation framework, and his emphasis was on whose data it runs against: "the dataset that is needed for your company, for your task — not someone else's public leaderboard." Verify the router behaves on your data; if not, adjust and loop.

#### Cache-aware routing (~01:54–01:55)

Rushed for time but flagged as a must-consider: in agentic systems that discover, analyze, and write code in a loop, **the same prompts recur on every iteration**. Switch models mid-session and **you lose the warm cache the previous model had built**. Routing therefore has to be cache-aware. This is what they're building now.

#### Demo and quick facts (~01:55–01:57)

The live demo didn't survive the venue Wi-Fi (the flow: create router → name it → add a task, e.g. the summarization preset → save → launch in the playground in one click and compare against another model). He relayed his pre-talk test result from memory: **the router came out roughly 20× cheaper than Opus 5 and finished the task about 67% faster**.

Quick facts:

- Purpose-built routing model, **30B**
- Adds **≤200ms** latency, server-side
- **Zero application code changes**
- **Completely free** — none of the LLM-as-router double tax on latency and cost
- Managed on DigitalOcean or self-hosted

#### Roadmap: personalization (~01:57–01:58)

The part he's most excited about, having built a personalization service before: **the more you use the router, the better it gets**. Turn on logs and traces, and the feedback flows into a continuous loop checked against your evals, so the router keeps improving on its own. His closing line: **you build nothing on your side, and the router still improves.**

### Quotes

> "You do not need a frontier model to serve every single of the request." (~01:45)

The premise of the whole talk: the problem isn't that frontier models are expensive, it's that they're overkill.

> "No public leaderboard or public benchmark tell you. So you need to encode those in the router." (~01:49)

Your cost ceiling and latency budget belong to you, not to a leaderboard — so routing logic has to be preference-driven.

> "You are paying double the tax … you are increasing the latency by around 600 milliseconds or so. In addition, you are also paying more." (~01:52)

The price of using an LLM as your router, on both axes.

> "Without doing anything, you're not building anything on your side. Without doing anything, the router is improving." (~01:57)

Once the routing layer has logs, traces, and an eval loop, improvement becomes the default rather than a project.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| DigitalOcean Inference Router | 伺服器端模型路由服務,依任務類別 + 即時成本/延遲路由 | Server-side model routing service; routes by task class using live cost and latency signals | 已上架 70+ 模型 / 70+ models onboarded |
| Plano | 開源 AI-native proxy,負責 rerank 與 observability | Open-source AI-native proxy handling reranking and observability | 官方部落格記載源自 Katanemo(現屬 DigitalOcean)/ per DigitalOcean's blog, originally developed at Katanemo |
| Plano-Orchestrator(路由模型 / routing model) | 30B 專用路由模型,講者稱在路由任務上勝過 GPT-5 系列 | 30B purpose-built routing model; speaker says it beats GPT-5 series on the routing task | 官方部落格記為 30B MoE(Plano-Orchestrator-30B-A3B)與 4B dense 兩種變體,~200ms 解析 intent / blog documents a 30B MoE variant and a 4B dense variant, ~200ms intent resolution |
| Kimi K3 / Claude Opus 5 | 演講中舉例的近期霸榜 frontier 模型 | Recent leaderboard-topping frontier models cited as examples | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Darshi Raha / Dashi | Debarshi Raha |
| plano | Plano |
| Kimik K3 | Kimi K3 |
| cloud opus 5 | Claude Opus 5 |
| GPD 5 series | GPT-5 series |
| cash hour routing | cache-aware routing |
| the latest phops | the latest FinOps |
| reank / rerank | rerank |
| millcond | millisecond |
| several IML services | several ML services |
| agent evolution and benchmarks(主持人開場)| Agent Evaluation & Benchmarks(官網議程場次名)|

## 待確認 / To Verify

- 加拿大法律 AI 新創客戶的名稱:字幕只聽得出類似 "lo",未能確認。/ Name of the Canadian legal-AI startup customer — the caption only yields something like "lo".
- 40–50%(該客戶)與「最高 80%」成本下降是否有公開來源可引用。/ Whether the 40–50% and "up to 80%" cost-reduction figures are published anywhere citable.
- 路由模型勝過 GPT-5 系列所依據的具體路由 benchmark 名稱。/ The specific routing benchmark on which the 30B model is said to beat the GPT-5 series.
- 「比 Opus 5 便宜約 20 倍、快約 67%」為講者口頭轉述的會前實測,demo 未成功,數字未經現場驗證。/ The "~20× cheaper, ~67% faster than Opus 5" figures were relayed verbally after the demo failed; not verified on stage.
- Uber「四個月燒完整年 agentic AI 預算」與 Walmart 設 AI 支出上限的出處。/ Sources for the Uber four-month budget burn and the Walmart AI spend cap.
