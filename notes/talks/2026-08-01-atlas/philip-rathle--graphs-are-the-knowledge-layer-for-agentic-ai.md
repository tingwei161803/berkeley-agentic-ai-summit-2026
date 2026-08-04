---
title: "Graphs Are the Knowledge Layer for Agentic AI"
title_zh: "圖(Graph)就是 Agentic AI 的知識層"
speaker: "Philip Rathle"
affiliation: "CTO, Neo4j"
type: talk
stage: Atlas
date: 2026-08-01
session: "Session 3: Frameworks & Dev Platforms"
video: "https://www.youtube.com/watch?v=psPzCQbjCCo&t=11647s"
video_range: "03:14:07–03:29:50"
transcript: "tmp/[English (auto-generated)] Atlas Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [knowledge-graph, graphrag, enterprise-ai, memory, ontology]
---

# 圖(Graph)就是 Agentic AI 的知識層(Graphs Are the Knowledge Layer for Agentic AI)

**一句話總結**:企業裡談的 knowledge、context、semantics、memory、ontology 其實是同一件事的不同切面,它們最終會收斂成一層「enterprise knowledge layer」,而這一層最自然的實作是圖——因為現實世界的資料本來就長成網路、階層與路徑。
**One-line summary**: Knowledge, context, semantics, memory, and ontology are facets of one thing — an enterprise knowledge layer — and graphs are its natural implementation, because real-world data already arrives as networks, hierarchies, and paths.

## 中文筆記

### TL;DR

- **知識層是一種已被驗證的架構模式**,不是新名詞。Rathle 從數千家客戶身上看到同一個 pattern:apps / agents / tools 不直接打各個資料源,而是打一層把 operational 與 analytic 資料串起來的 knowledge layer。
- **知識層 ≠ 把所有資料搬進來**。它不是 lift and shift,而是「從噪音裡撈出訊號、再把訊號連起來」,而且可以從小做起、逐步長大。
- **三種實際落地的圖**:domain graph(語意與本體)、rules graph(程序性記憶)、semantic layer(業務語彙 → 實體資料位置的地圖)。Walmart、Uber 與一家大型遊戲公司分別是三者的代表案例。
- **為什麼不是別的**:foundation model 訓練的是世界的資料不是你的資料、自訓小模型昂貴且一訓完就過期又繞過權限控管、關聯式表格只擅長固定簡單問題、向量完全不透明。圖同時解決「跨 silo 連結」與「複雜問題」。
- **知識層是會運算的,不是被動倉庫**:graph query、graph algorithms、similarity search、GNN、視覺化都在這一層跑,帶來 GraphRAG 準確度、multi-hop reasoning、decision traces 與記憶。

### 重點整理

#### Knowledge layer:一個從客戶身上長出來的 pattern(約 03:14)

Rathle 開場先把最近滿天飛的名詞收束在一起:knowledge、context、semantics、memory、ontology 表面上是不同題目,但在企業落地時全部匯流到同一層。這個結論來自 Neo4j 過去幾年與數千家客戶合作的觀察——大家最後都做出結構幾乎一樣的東西:上層是 apps、agents、tools,中間是 knowledge layer,下層右邊接 operational data sources、左邊接 analytic data sources。

他特別強調兩點分寸:

1. **這不是 lift and shift。** knowledge 之所以不同於 data,就在於它不是「什麼都要」,而是「把訊號從噪音裡拉出來、再把它們連起來」。連結本身才是重點。
2. **它是漸進式的。** 可以從很小的範圍開始,再往外長。

這一層的職能是:儲存結構、脈絡與意義;提供 agent 統一的記憶與檢索介面;橋接人類理解與機器執行。他把最後這點連到 neurosymbolic AI——這概念有幾十年歷史,但現在因為圖而回魂:你沒辦法內省一個模型或一個向量資料庫,那些對人類是不可讀的;圖則是人看得懂、機器也跑得動。

#### 三個真實案例、三種圖(約 03:16–03:19)

- **Walmart 的 People AI knowledge graph**:服務約 160 萬名員工的 agentic 應用,幫助員工規劃職涯路徑。圖裡放的是所有人、匯報結構與其歷史、技能如何隨時間累積、參與過哪些專案、目前有哪些職缺與職缺要求。全部放進同一張圖之後,「推薦職涯路徑」就退化成連連看——Rathle 形容成「用 Kevin Bacon 的六度分隔來解 HR 問題」。關鍵設計在於人與圖之間還隔著一個模型,所以同一個問題**既可以由模型加上更多 context 來回答,也可以直接對圖跑一個決定性的查詢**,兩種模式並存。
- **Uber 的 rules graph**:Uber 在 15,000 個城市營運,各城市的服務品項、名稱、適用法規都不同,再加上 Uber 自己調整服務的商業理由。這些規則被存進圖裡、也在圖裡被執行。
- **某大型遊戲公司的 semantic layer**:conversational AI → API 層 → multi-agent 系統 → 圖。這裡圖扮演語意層,把業務術語、概念與彼此的關係,對應到實體基礎設施與資料所在位置。換句話說,**agent 用這張圖當作「企業裡的資料在哪」的地圖**。

三個案例對應到三種圖:domain graph(語意/本體)、rules graph(可視為 procedural memory)、semantic layer。它們的共同點,也是這些團隊選擇圖的核心洞見:**他們的資料本來就以網路或階層的形式出現**——電腦網路、社交網路、通訊、生物、生態、運輸屬於前者;Walmart 的 HR(其實是多重階層加上路徑)、customer journey、patient journey 屬於後者。

#### 為什麼需要一個新模型(約 03:20–03:22)

過去幾十年,主流做法是把這些資料塞進表格。但兩年前 ISO 認可了 property graph 資料模型——這是**近 40 年來資料庫領域第一次有新的資料模型被國際標準組織背書**(上一次是 SQL 的關聯模型)。

那為什麼現有工具不夠?他逐一拆解:

| 選項 | 問題 |
|------|------|
| Foundation model | 訓練在世界的資料上,不是你的資料 |
| 自訓小模型 | 昂貴;訓完當下就過期;訓進去的東西變成任何 agent 為任何目的都能取用,繞過企業的存取控制;仍會幻覺、缺乏判斷力;是黑盒 |
| 靜態 rows and columns | 大多數資料在這裡,適合固定且簡單的問題;問題一旦複雜且事先不知道下一問是什麼就吃力 |
| 非結構化資料 | 難以挖掘與理解 |
| 向量 | 完全不透明,而且大概只有一兩招 |
| 組織資料 | 散在各個 silo,agent 拿不到全公司的智慧 |

他引用 Gartner 給資料與分析主管的建議作為佐證:必須重新設計資料與分析架構,讓 **context layer 成為 AI agents 的中央大腦**,以交付可信賴的智慧。

#### Agent 對「知識」的四項要求(約 03:22–03:24)

1. **即時性**:agent 高度互動,不能只對著 data lake / lakehouse 說話,需要低延遲檢索,而且要能回寫,才能形成自我改善的正向循環。
2. **能存結構化、半結構化與非結構化資料**。
3. **跨 silo 整合但保留連結**:data lake 把資料集中了,卻在集中的過程中丟掉了資料之間的關聯——「centralizing everything but not connecting it」。
4. **RAG corpus(他主張是 graph RAG corpus)與資料存取控制**:企業防火牆、資安、隱私都在這裡。

對應到知識層的內部組成:最上是連成圖的 **domain data**(自有領域資料 + 第三方參考資料,也可以用 virtual graph 直接對 data lake 跑圖查詢);中間是 **ontology / semantic layer**,承載業務意義以及它到資料位置的對應,像一張「business ↔ technology」的地圖;最後是 **memory**——對話記憶只是文字與 prompt 的堆疊,但就像人腦在睡眠中做記憶固化一樣,長期記憶要回答的是「哪些事情重要、它們怎麼連在一起」,而長期記憶、procedural memory、context 與 decision traces 都最適合存成圖。

#### 知識層的作用,以及它會運算(約 03:24–03:28)

知識層帶來的效益他濃縮成一頁:提供 context 讓 agent 答得更好、連通 silo、知識可稽核、保留 deterministic 處理的選項、遵守存取控制,以及——他說這點連他自己都意外——**更會處理複雜問題**。原因是客戶反覆回報:AI 模型把一個複雜的自然語言問題翻成 **graph query(GQL 或 Cypher)的品質,明顯優於翻成 SQL**;因為在 SQL 裡要 200 行的東西,用圖查詢語言可能 5 行就講完,表達方式更接近人類語言。

他也給了量化證據:英國 NICD 的獨立研究比較 GraphRAG 與 vector-only RAG,結果是回答的問題數超過兩倍、truthfulness 高約 80%、幻覺更少、用的 token 更少。

最後一個他想留下的 takeaway:**知識層不是被動的儲存,它會做各種運算**——graph querying(各種 pattern matching 與 filtering)、graph algorithms(分群、link prediction 等)、similarity search、GNN(他把 GNN 產出的東西形容成「拓撲向量」,另一種向量)、graph visualization。這些換來的是 GraphRAG 的準確度、支撐更複雜任務的 multi-hop reasoning、企業語意地圖、decision traces(他說這本身就是一整場演講)與記憶。

企業要從哪裡開始?兩條路:**由上而下**把企業當成一個相連的有機體,先畫出跨 silo 的地圖;或**由下而上**,例如先做 product graph(產品階層),它底下就長出推薦、定價、庫存等一堆 use case,再把供應商資料接進來就變成供應鏈最佳化;employee graph 接出職涯路徑,依此類推。

### 金句

> "Knowledge, distinct from data, doesn't mean everything about everything. It means let's pull up the signal from the noise and let's connect it up."(約 03:15)

知識層不是資料湖的另一個名字——它的價值在於取捨與連結。

> "It's almost like solving for HR by degrees of Kevin Bacon."(約 03:17)

Walmart 的職涯推薦,本質上就是在圖上連連看。

> "You're centralizing everything but you're not connecting it."(約 03:23)

對 data lake / lakehouse 最精準的一句批評。

## English Notes

### TL;DR

- **The knowledge layer is a pattern, not a buzzword.** Across thousands of Neo4j customers the same architecture keeps emerging: apps, agents, and tools talk to one knowledge layer that unifies operational and analytic sources, instead of wiring into each source directly.
- **It is not a lift and shift.** Knowledge, as distinct from data, means pulling signal out of noise and connecting it — and it can be built incrementally, starting small.
- **Three graph shapes show up in production**: a domain graph (semantics and ontology), a rules graph (procedural memory), and a semantic layer (business vocabulary mapped down to where the data physically lives) — exemplified by Walmart, Uber, and a major gaming company respectively.
- **Why not the alternatives**: foundation models are trained on the world's data, not yours; a bespoke small model is expensive, stale the moment it finishes training, and blows past your access controls; rows and columns answer fixed simple questions; vectors are opaque. Graphs handle both cross-silo connection and genuinely complex questions.
- **The knowledge layer computes.** Graph queries, graph algorithms, similarity search, GNNs, and visualization all run in this layer, yielding GraphRAG accuracy, multi-hop reasoning, decision traces, and memory.

### Key Points

#### A pattern discovered in the field (~03:14)

Rathle opens by collapsing five fashionable terms — knowledge, context, semantics, memory, ontology — into one. They are separate topics on paper, but in enterprise deployments they converge on a single architectural tier, and that convergence is what he has watched happen across thousands of customers: apps, agents, and tools on top; a knowledge layer in the middle; operational sources on one side and analytic sources on the other.

Two qualifications matter. First, this is not a lift and shift — knowledge is precisely *not* everything about everything, it is signal pulled out of noise and then connected, and the connections are the point. Second, it is incremental: start small, build up.

Functionally, the layer stores structure, context, and meaning; gives agents a uniform memory and retrieval interface; and bridges human and machine understanding. That last point is where neurosymbolic AI, decades old, comes back: you cannot introspect a model or a vector database — they are unintelligible to a person — whereas a graph is legible to a human and executable by a machine.

#### Three graphs, three customers (~03:16–03:19)

- **Walmart's People AI knowledge graph** serves roughly 1.6 million employees navigating their career journeys. The graph holds people, the reporting structure and its history, how skills accumulated over time, project history, open roles, and role requirements. Put all of that in one graph and career recommendation reduces to connecting the dots — "solving for HR by degrees of Kevin Bacon." Crucially there is a model between the human and the graph, which buys optionality: the same question can be answered by feeding the model more context, *or* answered deterministically by querying the graph.
- **Uber's rules graph**: Uber operates in 15,000 cities with different offerings, different names for those offerings, different laws and regulations, plus Uber's own reasons for varying them. Those rules are both stored and executed in the graph.
- **A major gaming company's semantic layer**: conversational AI → API layer → multi-agent system → graph. Here the graph maps business terms, concepts, and their relationships down to physical and data infrastructure — effectively giving agents a map of where to go in the enterprise to find data.

What the three have in common — and the insight that drove each team to graphs — is that their data already arrived as a network (computer networks, social networks, communications, biology, ecology, transportation) or as a hierarchy and journey (Walmart's HR is several overlapping hierarchies; so are customer and patient journeys).

#### Why a new data model (~03:20–03:22)

Tables have been the default for decades, but two years ago the property graph data model became an ISO standard — the first time in nearly 40 years that ISO blessed a new data model in the database space.

Why isn't the existing toolkit enough? A foundation model is trained on the world's data, not yours. Training your own small model is expensive, stale the instant it finishes, and — more subtly — everything you trained into it becomes fair game for any agent answering any question for any purpose, which collides head-on with enterprise access controls; it still hallucinates, still lacks discernment, and is still a black box. Static rows and columns are great for fixed, simple questions and terrible when questions get intricate and unpredictable, which is exactly where graphs have shined for the decade-plus he has worked on them. Unstructured data is hard to mine; vectors are completely opaque and arguably a one- or two-trick pony; and organizational data sits in silos, so agents get one system's intelligence rather than the company's.

He cites Gartner's recommendation to data and analytics leaders as external confirmation: redesign the data and analytics architecture so the **context layer becomes the central brain for AI agents** delivering trusted intelligence.

#### What agents require of knowledge (~03:22–03:24)

Four requirements: (1) real-time, low-latency retrieval *and* write-back, so agents get a virtuous cycle of self-improvement — a lake or lakehouse alone cannot serve an interactive agent; (2) structured, semi-structured, and unstructured storage; (3) cross-silo integration that preserves the connections — lakes centralize everything without connecting it; (4) a RAG corpus (he'd argue a graph RAG corpus) plus data access controls for firewall, security, and privacy reasons.

Zooming into the layer itself: **domain data** connected as a graph (your own plus third-party reference data, with the option of running graph queries virtually against data lakes); **ontology and semantic layer**, carrying business meaning and its mapping to where data lives — a business-to-technology map; and **memory**. Conversational memory is just accumulated text and prompts, but much as the human brain consolidates memory during sleep, long-term memory answers "what matters and how does it connect" — and long-term memory, procedural memory, context, and decision traces are all best stored as graphs.

#### What the layer buys you — and the fact that it computes (~03:24–03:28)

The payoff list: context for better answers, connected silos, knowledge transparency, an option for deterministic processing, respected access controls, and — surprising even to him — markedly better handling of complex questions. Customer after customer reports that models translate a complex natural-language question into a **graph query (GQL or Cypher) far better than into SQL**, because a question that takes 200 lines of SQL may take five lines of graph query; the representation sits closer to human language.

For hard numbers he points at an independent study by the UK's NICD comparing GraphRAG to vector-only RAG: more than twice as many questions answered, roughly 80% better truthfulness, fewer hallucinations, and fewer tokens consumed.

The takeaway he most wants to leave: **the knowledge layer is not a passive store — it performs computation.** Graph querying (pattern matching and filtering), graph algorithms (clustering, link prediction), similarity search, GNNs (a topological kind of vector), and graph visualization all live here. The resulting advantages are GraphRAG accuracy, multi-hop reasoning for harder agent tasks, an enterprise semantic map, decision traces (a whole talk in itself, he notes), and memory.

Where to start? Breadth-first and top-down, treating the enterprise as a connected organism and mapping across the silos; or bottom-up, e.g. a product graph that immediately supports recommendations, pricing, and inventory, then connects to supplier data for supply-chain optimization, and likewise an employee graph for career journeys.

### Quotes

> "Knowledge, distinct from data, doesn't mean everything about everything. It means let's pull up the signal from the noise and let's connect it up." (~03:15)

The knowledge layer is not another name for the data lake; the editorial judgment and the connections are the value.

> "It's almost like solving for HR by degrees of Kevin Bacon." (~03:17)

Career recommendation at Walmart is, structurally, path-finding on a graph.

> "You're centralizing everything but you're not connecting it." (~03:23)

His one-line critique of lakes and lakehouses.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Neo4j | 圖資料庫,講者所屬公司 | Graph database; the speaker's company | 逐字稿常誤植為 "Neoforj" / often mis-transcribed as "Neoforj" |
| GQL / Cypher | 圖查詢語言;GQL 於兩年前成為 ISO 標準 | Graph query languages; GQL became an ISO standard two years ago | 講者稱為近 40 年來資料庫領域第一個新資料模型 / described as the first new database data model in nearly 40 years |
| The GraphRAG Manifesto | Rathle 兩年前寫的 GraphRAG 介紹文,他說「現在仍然成立」 | Rathle's introduction to GraphRAG, written two years ago and "still holds up" | Neo4j 部落格 / Neo4j blog |
| 企業知識層專文 / Enterprise knowledge layer article | 演講前兩週發表,等於本場演講的文字版 | Published two weeks before the talk; the prose version of this talk | |
| NICD GraphRAG 研究 / NICD GraphRAG study | 英國 National Innovation Centre for Data 的獨立研究:GraphRAG vs vector-only RAG | Independent study by the UK's National Innovation Centre for Data comparing GraphRAG with vector-only RAG | 回答問題數 2×、truthfulness +80%、幻覺更少、token 更少 / 2× questions answered, ~80% more truthful, fewer hallucinations, fewer tokens |
| Walmart People AI knowledge graph | 約 160 萬員工的職涯導航 agentic 應用 | Agentic career-navigation app for ~1.6M employees | |
| Uber rules graph | 15,000 個城市的服務規則與法規,存於圖中並在圖中執行 | Offering and regulatory rules across 15,000 cities, stored and executed in the graph | |
| DeepLearning.AI 課程 / courses、Neo4j GraphAcademy | 演講結尾 QR code 導向的學習資源 | Learning resources behind the closing QR code | 他提到 Andrew Ng 當天也在現場 / he noted Andrew Ng was at the summit that day |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Peter Rathy / Philip Rafy / Phillip | Philip Rathle |
| Neoforj / Neo forge | Neo4j |
| multi- aent system | multi-agent system |
| graph rag | GraphRAG |
| cipher | Cypher |
| UK's center for data and AI innovation | UK's National Innovation Centre for Data (NICD) |
| GNN's ... topological vector | GNNs ... topological vector |
| Andrew Ing | Andrew Ng |

## 待確認 / To Verify

- 主持人在 Rathle 之前把名字唸成 "Peter",現場更正為 "Philip";逐字稿的姓氏拼寫全部不可信,已依官網議程統一為 Philip Rathle。/ The MC first said "Peter" and was corrected on stage; all surname spellings in the transcript are unreliable and have been normalized to the agenda's "Philip Rathle".
- 那家「全球最大的遊戲公司之一」未具名。/ The "major gaming company" example was not named.
- Gartner 建議的原文出處(哪份報告)未在演講中指出。/ The specific Gartner report behind the "context layer as central brain" recommendation was not cited on stage.
- 講者說 ISO 認可的是「property graph 資料模型」;實際上 2024 年成為 ISO 標準的是 GQL 查詢語言(其資料模型為 property graph),兩者在口述中被合併表述。/ He described ISO as blessing "the property graph data model"; what became an ISO standard in 2024 is the GQL query language, whose underlying model is the property graph — the two were conflated in speech.
