---
title: "Scaling Up Config-Driven Multi-Agent Networks with Neuro SAN"
title_zh: "用 Neuro SAN 擴展設定驅動的多 Agent 網路"
speaker: "Daniel Fink"
affiliation: "AI Engineering Lead, Cognizant"
type: talk
stage: Compass
date: 2026-08-02
session: "Session 3: Enterprise AI"
video: "https://www.youtube.com/watch?v=1UrriPJRSPU&t=5645s"
video_range: "01:34:05–01:41:17"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [enterprise, multi-agent, open-source, orchestration, configuration]
---

# 用 Neuro SAN 擴展設定驅動的多 Agent 網路(Scaling Up Config-Driven Multi-Agent Networks with Neuro SAN)

**一句話總結**:兩年半前 Cognizant AI Lab 發現「agent 呼叫 agent 的膠水程式碼」才是真正的雜訊,於是把整個多 agent 網路抽成設定檔——結果不只讓行銷同事也能建系統,還讓公司內網長成 200 個 leaf agent 的網路,工單量下降約三成。
**One-line summary**: Two and a half years ago Cognizant AI Lab concluded that the glue code of agents calling agents was the noise, so they lifted the whole agent network into configuration files — which let non-engineers build systems, and grew the corporate intranet into a network of ~200 leaf agents that cut ticket volume by about 30%.

## 中文筆記

### TL;DR

- **起點是一個很務實的判斷**:兩年半前做多 agent 實驗時,發現「agent 呼叫 agent、agent 呼叫工具、工具再回呼 agent」的膠水程式碼淹沒了真正想做的事;於是把它抽掉,用設定檔描述整個網路——這就是 **Neuro SAN**。
- **設定驅動帶來三個意外收穫**:multi-agent 系統可以把另一個 multi-agent 系統當成工具呼叫(agentic webs,可無限套疊,也能接 MCP / A2A server);因為呼叫方式標準化,**測試本身也變成資料驅動**;而既然設定檔只是「等著被填的表單」,就出現了**用多 agent 系統來 vibe code 另一個多 agent 系統**的玩法。
- **不必等下一個更強的模型**:真正的勝負手是把問題拆小到讓**更小的模型**能處理——更可靠也更便宜。
- **內部案例**:公司內網用 **AAOSA** 協調架構跑約 **200 個 leaf agent**(接 ServiceNow、Salesforce、PeopleSoft 等),部署後**工單量下降約 30%**。

### 重點整理

#### Neuro SAN 的由來與架構(約 01:34–01:36)

講者來自 **Cognizant AI Lab**——一個「大 R、小 D」的研究團隊,約 30–40 人,以舊金山為中心,班加羅爾也有成員。他的工作是把有潛力的研究成果推出去、讓它能被規模化。

最好的例子就是 Neuro SAN。兩年半前團隊在做多 agent 實驗時,**很快就發現 agent 呼叫其他 agent 的膠水程式碼正是掩蓋真正目標的雜訊**,於是決定把這一層抽起來。做出來的東西就是現在的 **Neuro SAN**:一個**設定驅動(configuration-driven)** 的系統,agent 可以呼叫其他 agent、可以呼叫 coded tool,coded tool 也可以回呼進 agent 系統;**除了 coded tool 本身的程式碼之外,一切都用設定檔描述**。

網路裡的每個節點都向**上游(upchain)呼叫者**宣告三件事:我能做什麼、我運作需要哪些資訊、我可以跟誰對話;之上還有整體的 system prompt。他點出其中一個「secret sauce」:**最終極的 upchain 就是使用者本人**。而對於憑證這類機密,他們有一條稱為 **sly_data** 的側通道,讓 token 這種絕對不該進入對話流的東西可以另外傳遞。

#### 設定驅動意外長出來的三件事(約 01:36–01:38)

在深入之前,他先給兩個早期心得:

- **不必等下一個更強的模型**。真正的勝負手是**把問題拆解到更小的模型也能處理**——而且更可靠、更便宜。
- **給對工具之後,建多 agent 系統的人變得很多樣**。連他們的行銷同事都做出了非常好的想法與工具,至今仍在使用。

由設定驅動衍生出來的三個能力:

1. **Agentic webs**:做好一個多 agent 系統之後,要讓它把**另一個多 agent 系統當成工具**呼叫非常容易,而且可以無限套疊;同樣能呼叫 MCP server、A2A server,或任何其他 agent 系統。
2. **資料驅動的測試**:因為呼叫 agent 的共用工具(連同機密處理)都已標準化,**測試本身也變成資料驅動**——「我想要的這次互動」就是一筆資料。
3. **多 agent 系統 vibe code 多 agent 系統**:既然描述 agentic 系統的就是 JSON / HOCON 檔案,那它們**不過是等著被填的表單**。於是他們有了會生成其他多 agent 系統的多 agent 系統,產物可以當成一個「可拋棄的想法(perishable thought)」直接呼叫,也可以下載下來成為整體系統的一部分。

#### 內部案例:公司內網與 AAOSA(約 01:38–01:40)

投影片上是一個同心圓:中心是他們稱為 **front man** 的根節點,向外呼叫中間層 agent,最外圈是真正在做事的 **leaf agent**。

案例是**企業內網**——就是你每週至少會看一次的公司首頁。HR、財務、IT 各部門需求不同、各有各的 agent,但所有人都需要能存取。串起來的是他們稱為 **AAOSA** 的提示架構,核心設計是:**負責回答當前問題的那位其實什麼都不知道,但他知道該找誰**。問題就這樣往下滲透,讓 HR、法務等不同面向分別回答自己那一塊;資訊往上回流時再逐層**聚合成知識**。

他們說服公司 IT 部門一起吃自己的狗食,目前這套 AAOSA 架構協調著約 **200 個 leaf-level agent**,涵蓋 ServiceNow、Salesforce、PeopleSoft 等大家熟悉的系統。他形容「擴展性好得離譜」,而成果直接反映在**工單數**上:投影片的折線圖裡有一條垂直線標示部署時點,部署之後**整體工單量下降約 30%**——因為 agent 系統處理這些請求比人處理得更好。

#### 開源與後續(約 01:40–01:41)

- 這套東西**免費可用、授權友善**,他鼓勵大家自己試。
- 他們期待與 **AAIF(Agentic AI Foundation)** 合作,把它放進 **Linux Foundation**。
- 即將推出一個 **bring-your-own-key 的網站**(整套系統本來就支援),讓人可以在上面 vibe code 自己的多 agent 系統。

### 金句

> "We quickly realized that the glue code of agents calling other agents was the noise in what we were really trying to do. And so we wanted to lift that up."(約 01:34)

Neuro SAN 的起點:把膠水程式碼從問題裡移除,而不是把它寫得更好。

> "We don't really need to wait for the next great model in order to boost our capability. The real win is breaking your problems down so that a smaller model can handle it — and handle it more reliably and more cheaply for that matter."(約 01:36)

在一場滿是「等下一代模型」的會議裡,這是相反方向的主張。

> "The coordinator doesn't know anything but the people down below do."(約 01:39)

AAOSA 的設計精神:協調者的價值不在知識,而在知道該找誰。

## English Notes

### TL;DR

- **The origin is a pragmatic call**: while experimenting with multi-agent systems two and a half years ago, the team realized the glue code — agents calling agents, agents calling tools, tools calling back — was the noise obscuring the actual work. So they lifted it out and described the whole network in configuration files. That became **Neuro SAN**.
- **Config-driven design produced three emergent wins**: a multi-agent system can call another multi-agent system as a tool (agentic webs, nestable ad infinitum, and equally able to call MCP or A2A servers); standardized invocation makes **testing itself data-driven**; and since the config files are just forms waiting to be filled in, you get **multi-agent systems vibe-coding other multi-agent systems**.
- **You don't need to wait for the next great model.** The real win is decomposing the problem so a smaller model can handle it — more reliably and more cheaply.
- **Internal proof point**: their corporate intranet now runs ~**200 leaf agents** coordinated by **AAOSA** (fronting ServiceNow, Salesforce, PeopleSoft), and ticket volume dropped roughly **30%** after deployment.

### Key Points

#### Where Neuro SAN came from, and how it's structured (~01:34–01:36)

The speaker is from **Cognizant AI Lab** — a "big R, little D" group of maybe 30–40 people centered in San Francisco with a contingent in Bangalore. His job is taking promising research and pushing it out so it can be scaled up.

Neuro SAN is the flagship example. Two and a half years ago, experimenting with multi-agent systems, the team **quickly realized that the glue code of agents calling other agents was the noise** in what they were actually trying to do — so they lifted it out. The result is a **configuration-driven** system where agents call other agents, agents call coded tools, and coded tools can call back into the agent system, with **everything described in configuration except the coded tools themselves**.

Every node in the network declares upward to its **upchain callers**: what it can do, what information it needs to operate, and who it can talk to — plus an overall system prompt. One bit of secret sauce he highlights: **the ultimate upchain is the user.** For secure credentials there's a side channel they call **sly_data**, so tokens you never want in the chat stream can travel separately.

#### Three things the config-driven design made possible (~01:36–01:38)

Two early lessons first:

- **You don't need the next great model to boost capability.** The real win is breaking problems down so a smaller model can handle them — more reliably and more cheaply.
- **Given the right tools, all sorts of people start building multi-agent systems.** Even their marketing people produced genuinely good ideas and tools that are still in use today.

The emergent capabilities:

1. **Agentic webs.** Once you've built a multi-agent system, it's easy for it to call **another multi-agent system as a tool**, ad infinitum — and equally to call MCP servers, A2A servers, or whatever other agent system you want.
2. **Data-driven testing.** Because the common tooling for invoking agents — secrets included — is standardized, testing becomes data-driven in itself: "this is the interaction I want to have" is just data.
3. **Multi-agent systems vibe-coding multi-agent systems.** Since agentic systems are described by JSON/HOCON files, those files are just forms to fill in. So they now have multi-agent systems that generate other multi-agent systems, callable as a "perishable thought" or downloadable to become part of the larger system.

#### Case study: the corporate intranet and AAOSA (~01:38–01:40)

The slide shows concentric circles: at the center is what they call the **front man**, the root of the system, calling out to middle-tier agents, with **leaf agents** in the outer ring doing the actual work.

The application is a **corporate intranet** — the company homepage you look at at least weekly. HR, finance, and IT all have different needs and different agents, yet everybody needs access to all of them. Tying it together is a prompting infrastructure called **AAOSA**, whose design principle is that **whoever is answering the current question knows nothing, but knows who else to call**. The question trickles down so HR, legal, and the rest each answer their own facet, and as information comes back up there's an **aggregation of knowledge** along the way.

They convinced their corporate IT department to eat their own dog food. That deployment now coordinates roughly **200 leaf-level agents** via AAOSA, fronting ServiceNow, Salesforce, PeopleSoft, and the rest. He describes the scaling as "ridiculous," and the results show up directly in ticket counts: on the chart, a vertical line marks deployment, after which **overall tickets dropped about 30%** — the agent system was handling requests better than people overall.

#### Open source and what's next (~01:40–01:41)

- The stack is **freely available and agreeably licensed**; he encourages people to try it.
- They look forward to working with the **AAIF (Agentic AI Foundation)** to make it available in the **Linux Foundation**.
- A **bring-your-own-key site** is coming (the system already supports BYOK) where you can vibe-code your own multi-agent systems.

### Quotes

> "We quickly realized that the glue code of agents calling other agents was the noise in what we were really trying to do. And so we wanted to lift that up." (~01:34)

The founding move behind Neuro SAN: remove the glue code from the problem rather than write it better.

> "We don't really need to wait for the next great model in order to boost our capability. The real win is breaking your problems down so that a smaller model can handle it — and handle it more reliably and more cheaply for that matter." (~01:36)

A deliberately contrarian note at a conference full of "wait for the next generation."

> "The coordinator doesn't know anything but the people down below do." (~01:39)

AAOSA in one line: the coordinator's value is knowing whom to ask, not knowing the answer.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Neuro SAN (`neuro-san`) | Cognizant AI Lab 的設定驅動多 agent 編排框架,用 HOCON 設定檔描述 agent 網路 | Cognizant AI Lab's configuration-driven multi-agent orchestration framework; agent networks defined in HOCON config files | 開源:[cognizant-ai-lab/neuro-san-studio](https://github.com/cognizant-ai-lab/neuro-san-studio);[官方頁面](https://www.cognizant.com/us/en/ai-lab/neuro-san) |
| AAOSA | Adaptive Agent-Oriented Software Architecture,Neuro SAN 用來決定路由與委派的協定 / 提示架構 | The protocol and prompting architecture Neuro SAN agents follow to route and delegate tasks | 逐字稿聽成 "AOSA" |
| sly_data | 讓憑證等機密繞過對話流傳遞的側通道 | Side channel that carries credentials and other secrets outside the chat stream | 逐字稿聽成 "slide data" |
| HOCON | Neuro SAN 設定檔格式(JSON 的超集) | The configuration file format used by Neuro SAN (a JSON superset) | 逐字稿聽成 "hookon files" |
| Cognizant 企業內網 agent 網路 / Cognizant intranet agent network | 約 200 個 leaf agent,接 ServiceNow / Salesforce / PeopleSoft | ~200 leaf agents fronting ServiceNow, Salesforce, PeopleSoft | Cognizant AI Lab 有公開部落格記述此案例 |
| AAIF (Agentic AI Foundation) | Linux Foundation 底下的 agentic AI 基金會,他們計畫將 Neuro SAN 貢獻進去 | The Linux Foundation's agentic AI foundation; the intended home for Neuro SAN | 逐字稿聽成 "AIF";貢獻狀態待確認 |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Daniel Frink | Daniel Fink |
| Neurosan | Neuro SAN / `neuro-san` |
| AOSA | AAOSA |
| slide data | sly_data |
| hookon files | HOCON files |
| ATA servers | A2A servers |
| Peopleoft | PeopleSoft |
| aent / multi-aent | agent / multi-agent |
| AIF | AAIF (Agentic AI Foundation) |
| "add infinite item" | ad infinitum |

## 待確認 / To Verify

- 講者說內網部署後工單下降**約 30%**;Cognizant AI Lab 公開部落格則提到五個月內支援工單下降 **50%**。兩個數字可能對應不同時間點或不同度量,需比對投影片。/ He states a ~30% drop in tickets; Cognizant AI Lab's public blog cites a 50% drop within five months. The two may refer to different windows or metrics — check the slide.
- Neuro SAN 貢獻給 AAIF / Linux Foundation 的狀態:截至查證時,AAIF 公開的專案與會員名單中未見 Cognizant 或 Neuro SAN,講者的說法應屬規劃中。/ As of verification, neither Cognizant nor Neuro SAN appears in AAIF's published project or member lists — his statement reads as forward-looking.
- 「bring your own key 網站」的名稱與上線時間未提及。/ Name and launch date of the bring-your-own-key site were not given.
- 投影片上被他略過的「其他一些東西」(config-driven 的其他好處)無法從逐字稿還原。/ The additional config-driven benefits he "glazed over" on the slide can't be recovered from audio.
