---
title: "Advancing the State of the Art: The Frontier of Enterprise Agentic AI"
title_zh: "推進技術前沿:企業級 Agentic AI 的邊界"
speaker: "Milind Naphade"
affiliation: "SVP, AI Foundations, Capital One"
type: talk
stage: Plenary
date: 2026-08-02
session: "Session 4: Agentic AI in Finance & Legal"
video: "https://www.youtube.com/watch?v=I2PosBXwoPI&t=7211s"
video_range: "02:00:11–02:08:56"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [finance, multi-agent, enterprise, research, production]
---

# 推進技術前沿:企業級 Agentic AI 的邊界(Advancing the State of the Art: The Frontier of Enterprise Agentic AI)

**一句話總結**:Capital One 兩年半前就開始做 agentic AI、去年一月把多 agent 系統送上生產環境,他們的差異化不是選了哪個模型,而是**用自家資料把整條 AI stack 客製化**,並在框架裡放進一個獨立的 evaluator agent 來擋住不合規的計畫。
**One-line summary**: Capital One started on agentic AI more than two and a half years ago and had a multi-agent system in production by last January. Its differentiation isn't model choice — it's customizing the entire AI stack with proprietary data, and putting an independent evaluator agent in the loop to catch plans that violate policy.

## 中文筆記

### TL;DR

- **多 agent 框架有四類 agent**:understanding(理解環境與客戶需求)、planner(握有 API、知識與 Capital One 政策,規劃如何滿足需求)、**evaluator(獨立驗證計畫是否合規、是否安全,可退回給 planner 甚至 understanding agent)**、explainer(把 agent 之間的語言翻譯成人話)。他強調 evaluator 是「secret sauce」。
- **這不是把 RPA 換皮**:「這不是把 robotic 那套換成 agent 重做一遍,這是一個本質上非決定性(non-deterministic)的 agent 系統協作達成結果。」
- **已在生產環境**:兩個已上線案例——全美經銷商後端使用的購車 chat concierge(車輛需求、庫存、預約、換車,24/7/365 全自主),以及消費金融的**詐騙相關對話**輔助(理解客訴、建議行員採取的動作、摘要對話形成學習語料)。

### 重點整理

#### 定位:一家有深厚技術根柢、又懂風險管理的銀行(約 02:00–02:02)

Capital One 一向自我定位為 technology-first 公司,他的判斷是**銀行業的贏家會是一家科技公司**——同時具備深厚技術根柢與管理風險的能力。技術轉型的路走了一段時間:第一家把業務全面搬上公有雲的大型銀行、現代化資料生態系,以及從創立之初就有的資料驅動分析文化。過去三年半在 generative AI 與 agentic AI 上投入巨大資源,並且是**最早把 agentic AI 送進生產環境的企業之一**。

他帶的組織叫 **AI Foundations**,成員以 AI 研究員、應用 AI 工程師、資料科學家為主,目標是「用科學創新換取商業影響」:

- 今年在主要研討會與期刊發表 **65 篇以上論文**(ICML、ICLR、NeurIPS、ACM 等)。
- 與學界合作:University of Southern California、University of Illinois Urbana-Champaign、Columbia University 等,聚焦在推進 **safe AI**。

近期論文舉例(他只快速帶過):

- **多 agent 環境下多輪對話的資料集生成**——他強調這和單輪、單 agent 的合成資料生成是完全不同的問題。
- **把生成資料路由到多個模型**——「你可以把它想成 mixture of models,而不是 mixture of experts」(發表於 ACL)。
- **critic-guided distillation** 用於穩健推理(發表於 ICML)。

他的核心信念是:**真正的差異化只來自用自家資料客製化整條 AI stack**——「Capital One 的 AI 優勢,就是把 Capital One 的資料優勢轉換成 AI 優勢。」

#### 框架:四類 agent 與那個獨立的 evaluator(約 02:04–02:06)

Capital One 兩年半前開始探索 agentic AI,**去年一月就有第一個 multi-agent 生產系統**。他們的整體框架(字幕聽作 "MACA",拼法待確認)由四類 agent 組成:

1. **Understanding agent** — 與環境或客戶互動,弄清楚對方到底需要什麼。
2. **Planner agent** — 握有所有 API、所有知識與 Capital One 的政策,規劃如何滿足這個需求。
3. **Evaluator agent** — 他說「一部分祕方在這裡」:一個**完全獨立**的 agent,用一個很簡單的 world model 驗證這個計畫執行下去是否符合 Capital One 政策、是否安全;不合格就退回 planner,planner 也可以再退回 understanding agent 去跟客戶要更多輸入。
4. **Explainer agent** — 其他 agent 之間用自己的語言溝通,explainer 負責把結果講成人聽得懂的話。

他特別強調這個系統的性質:

> 這自然是一個非決定性的系統。這不是把 robotic(RPA)那套換個做法用 agent 重做一遍,而是一群 agent 本質上以非決定性的方式協作達成結果。

#### 兩個生產案例與招募(約 02:06–02:08)

- **購車 concierge**:全美有大量經銷商後端跑 Capital One,消費者買車時很可能就是在跟這個 chat concierge 互動——釐清你要什麼車、庫存狀況、預約、以及是否要以車換車,**24/7/365 全自主運作**。
- **詐騙相關對話輔助**(去年首度亮相,服務消費金融):三個部分——理解客戶的申訴內容、為行員推薦正確的處理動作、最後把對話摘要起來,**形成下一輪互動的學習語料**。

收尾是招募:他們在**基礎模型層、服務層、agentic 層、solution 層**四個層次都在客製化,對應三個 job family。賣點是「在受監管的企業裡用破紀錄的速度把研究送進生產」——這在受監管產業通常是聽不到的——以及「讓 1.3 億名客戶用到你的成果,並從中形成持續學習迴圈」。

### 金句

> "Capital One's AI advantage is Capital One's data advantage being converted into an AI advantage."(約 02:03)

差異化不在模型選型,在資料與客製化整條 stack。

> "This is not robotic just done differently with agents. This is an inherently non-deterministic system of agents that works together to achieve outcomes."(約 02:05)

不要用 RPA 的心智模型去理解 agentic 系統。

## English Notes

### TL;DR

- **A four-role multi-agent framework**: an *understanding* agent (reads the environment or the customer and figures out what's needed), a *planner* agent (holds the APIs, the knowledge, and Capital One's policies), an **independent *evaluator* agent** that validates whether executing the plan would fit policy and be safe — kicking it back to the planner, or further back to the understanding agent, when it wouldn't — and an *explainer* agent that translates inter-agent chatter into human language. Naphade calls the evaluator the secret sauce.
- **This is not RPA with new branding**: "This is not robotic just done differently with agents. This is an inherently non-deterministic system of agents that works together to achieve outcomes."
- **Already in production**: a car-buying chat concierge running behind dealerships nationwide (vehicle needs, availability, appointments, trade-ins — fully autonomous, 24/7/365), and a consumer-bank assistant for **fraud-related customer conversations** (understanding the complaint, recommending the right actions for the human agent, then summarizing the conversation into a learning corpus).

### Key Points

#### Positioning: a technology company that knows how to manage risk (~02:00–02:02)

Capital One has always framed itself as a technology-first company, and Naphade's thesis is that **the winner in banking will be a technology company** — one with deep technology roots *and* deep competence at managing risk. The transformation has been running for years: the first large bank fully on the public cloud, a modern data ecosystem, and a data-driven analytical culture dating to the company's origins. The last three and a half years brought heavy investment in generative and agentic AI, making Capital One one of the first enterprises to put agentic AI into production.

His organization, **AI Foundations**, is mostly AI researchers, applied AI engineers, and data scientists, chartered to deliver business impact through scientific innovation:

- **65+ publications** this year at leading conferences and journals (ICML, ICLR, NeurIPS, ACM, and others).
- Academic partnerships with the University of Southern California, University of Illinois Urbana-Champaign, Columbia University, and others, focused on advancing **safe AI**.

Sample recent work, mentioned in passing:

- Generating curated datasets for **multi-turn conversations in multi-agent environments** — which he stresses is a materially different problem from synthetic data generation for single-turn or single-agent interactions.
- Routing generated data through multiple models — "think of this as a **mixture of models** instead of a mixture of experts" (presented at ACL).
- **Critic-guided distillation** for robust reasoning (at ICML).

The through-line: **true differentiation comes only from customizing the entire AI stack with your own data.** "Capital One's AI advantage is Capital One's data advantage being converted into an AI advantage."

#### The framework and its independent evaluator (~02:04–02:06)

Capital One began exploring agentic AI more than two and a half years ago and had its **first multi-agent production system running last January**. The overall framework (heard in the captions as "MACA" — spelling unverified) comprises four classes of agent:

1. **Understanding agent** — interacts with the environment or the customer to determine what is actually needed.
2. **Planner agent** — has access to all the APIs, all the knowledge, and all of Capital One's policies, and works out how to satisfy the need.
3. **Evaluator agent** — the piece he singles out as secret sauce: a **completely independent** agent that uses a simple world model to determine whether executing the plan would fit Capital One policy and be safe to do. If not, it kicks the plan back to the planner, which can in turn go back to the understanding agent for better input from the customer.
4. **Explainer agent** — the other agents talk in their own language; this one speaks in terms humans understand.

> This is a non-deterministic system at play, naturally. This is not robotic just done differently with agents — this is an inherently non-deterministic system of agents that works together to achieve outcomes.

#### Two production cases, and a hiring pitch (~02:06–02:08)

- **Car-buying concierge**: dealerships across the country run Capital One on the back end, so a buyer is most likely interacting with this concierge — working out what they're looking for in a vehicle, availability, appointments, and trade-ins, **fully autonomously, 24/7/365**.
- **Fraud-related conversations** (debuted last year, serving the consumer bank): understanding the customer's complaint, recommending the right set of actions for the human agent to take, and summarizing the conversation to build a **learning corpus for the next round of interactions**.

He closed with recruiting. The team customizes at four layers — the foundation models themselves, the services around them, the agentic layer, and the solution layer — across three job families. The pitch: going from research to production in record time inside a regulated enterprise ("typically unheard of"), and seeing **130 million customers** use your work and feed a continuous learning loop.

### Quotes

> "Capital One's AI advantage is Capital One's data advantage being converted into an AI advantage." (~02:03)

> "This is not robotic just done differently with agents. This is an inherently non-deterministic system of agents that works together to achieve outcomes." (~02:05)

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| AI Foundations (Capital One) | Naphade 帶領的組織,以研究員 / 應用工程師 / 資料科學家為主 | Naphade's organization: AI researchers, applied AI engineers, data scientists | 今年 65+ 篇論文 |
| 多 agent 框架(字幕作 "MACA") | understanding / planner / evaluator / explainer 四類 agent | Four-role framework: understanding / planner / evaluator / explainer | 名稱拼法**待確認** |
| 購車 chat concierge | 全美經銷商後端,24/7/365 全自主 | Car-buying concierge behind dealerships nationwide, fully autonomous | 生產環境案例 |
| 詐騙對話輔助 | 消費金融:理解客訴 → 建議行員動作 → 摘要成學習語料 | Consumer-bank fraud conversations: complaint understanding → action recommendation → summarization into a learning corpus | 去年首度亮相 |
| 多輪 × 多 agent 資料集生成論文 | 與單輪/單 agent 合成資料是不同問題 | Dataset curation for multi-turn conversations in multi-agent environments | 發表場合未明說 |
| Mixture of models 論文 | 把生成資料路由到多個模型 | Routing generated data through multiple models | ACL |
| Critic-guided distillation | 用於穩健推理 | For robust reasoning | ICML |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Milinda Nafed / Milan Naft | Milind Naphade |
| maca | 框架名稱待確認 / framework name to verify |
| Arbana Champagne | Urbana-Champaign |
| Colombia University | Columbia University |
| neurips | NeurIPS |
| chat concier | chat concierge |

## 待確認 / To Verify

- 多 agent 框架的正式名稱與拼法(字幕聽作 "MACA"),需看投影片或 Capital One 官方資料確認。/ The official name and spelling of the multi-agent framework (heard as "MACA") — needs slide or Capital One documentation.
- 論文題名皆未在口頭中完整說出,表中僅記錄主題;若要引用需回查 Capital One 的發表清單。/ None of the papers were named in full; the table records topics only. Look up Capital One's publication list before citing.
- 「130 million customers」為講者口述數字,未附出處。/ The "130 million customers" figure is as spoken; no source given.
