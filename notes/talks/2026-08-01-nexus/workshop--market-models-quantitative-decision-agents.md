---
title: "Market Models: The Missing Foundation for Quantitative Decision Agents / Architecting Quantitative Decision Agents"
title_zh: "Market Model:量化決策 agent 缺的那塊地基 / 量化決策 agent 的架構實作"
speaker: "Uri Yerushalmi; Hadar Sharvit"
affiliation: "Uri Yerushalmi — Chief AI Officer, Fetcherr;Hadar Sharvit — Director of Deep Learning, Fetcherr"
type: workshop
stage: Nexus
date: 2026-08-01
session: "Session 2: Coding & Web Agents"
video: "https://www.youtube.com/watch?v=ZIRc3EpzQJs&t=3244s"
video_range: "00:54:04–01:54:05"
transcript: "tmp/[English (auto-generated)] Nexus Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [market-models, pricing, forecasting, tool-use, sub-agents]
---

# Market Model:量化決策 agent 缺的那塊地基(Market Models: The Missing Foundation for Quantitative Decision Agents / Architecting Quantitative Decision Agents)

**一句話總結**:語言模型不該負責算術——決策系統的架構必須反映決策所在環境的結構,所以 Fetcherr 用直接在市場動態上訓練的 **market model** 取代 LLM 承擔預測與最佳化,LLM 只負責編排;實測中同一題目、同一份資料,配備 market model 的 agent 建議降價(估計 +6% 營收),而純 LLM agent 建議漲價(估計 −8%)。
**One-line summary**: A decision system's architecture has to mirror the structure of the environment it decides in — so Fetcherr replaces the LLM's arithmetic with a **market model** trained directly on market dynamics, leaving the LLM to orchestrate. In their head-to-head, given identical data, the tool-equipped agent recommended a price *cut* (est. +6% revenue) while the vanilla agent recommended a price *raise* (est. −8%).

## 中文筆記

這是一場「keynote + workshop」的組合場:Uri Yerushalmi 先建立論證(為什麼 LLM 不足以做量化決策、market model 是什麼),Hadar Sharvit 接著把它拆成數學、程式碼與一場對照實驗。

### TL;DR

- **核心論證(生物學類比)**:人腦演化出視覺皮質、前額葉等分區,重點不是位置,而是「**決策系統的架構必須反映決策所在環境的複雜度與結構**」。自然世界的一級公民是影像、聲音、動作;商業世界的一級公民是**價格、供給、需求**——但在 language-centric 的 agentic workflow 裡,這些概念不是一級公民。
- **Market model 是什麼**:與 LLM 用同樣的深度學習技術,但訓練資料不同——LLM 訓練於文本、視覺模型訓練於影像、large world model 訓練於物理環境資料,**market model 訓練於市場環境的動態資料**。它的基本單位不是 token 也不是像素,而是**機率 voxel**:在(交易時間 × 交割時間 × 產品屬性 × 客群屬性 × …)的高維格點上,某事件(成交、取消、競品調價)發生的機率。
- **可解釋性不是額外功能**:market model 有 attention layer,可以「看進它的腦袋」。案例:年中有新競爭者入場(黃色),模型依各競爭者屬性重新分配注意力權重。
- **輸出是一張需求地形圖**:切片後以自身價格為 x 軸、競品價格為 y 軸,可讀出期望需求、**equilibrium line**(買方無感的無差異線)、以及不同市場的競爭強度差異(有的市場競爭幾乎無影響,有的「每一分錢都有差」)。
- **決策 = 在會變動的 reward landscape 上爬山**:每個山丘是一個 **decision regime**;現實改變時,系統要知道何時該從 regime A 換到更高的 regime B。A/B 測試顯示平均約 **7%** 的營收提升(統計顯著)。
- **實作結論(Hadar)**:把 forecasting 與 constrained optimization 包成 tool,以 Claude Agent SDK 建立「revenue manager + 三個 sub-agent(市場動態、定價政策、QA)」的階層,並用 PostToolUse hook 記錄 **grounding**(agent 是否真的用了這些工具)。
- **對照實驗最關鍵的發現不是誰算得準,而是誰知道自己不知道**:配備工具的 agent 的 QA analyst 用 `evaluate_forecast` 標記出某產品預測不確定性過高,回報 revenue manager 後重新派工——六個產品最後只 ship 五個價格,第六個留給人。純 LLM agent **全部照 ship**,因為它根本沒有評估不確定性的機制。

### 討論主題與雙方立場

#### 主題一:為什麼 language-centric 架構不足以做商業決策(Uri,約 00:54–01:04)

Uri 的背景先立信:三十多年做量化決策系統,曾任演算法交易公司的 AI 部門負責人,學術背景是**計算神經科學博士**。他說今天 NASDAQ 等資本市場已有極高比例的成交量來自演算法,而當年那些決策靠的正是「預測未來市場動態」的模型。但資本市場逐漸變成**拚速度**的遊戲,而他一直更想要的是「**靠聰明而不是靠快**做對決定」——所以轉向了非資本市場。

他的論證從生物學出發:人腦花了數億年演化出處理不同自然資料的專門區域——視覺皮質處理視覺、前額葉負責規劃,還有處理聲音、味覺、觸覺的區域。「重點不是每個區域的**精確位置**」,而是這件事顯示:**決策系統的架構,必須反映決策所在環境的複雜度與結構。**

對照今天商業場域的 agentic workflow:中心是一個語言模型,外面包著 harnessing 層,或許加上一些視覺模型。LLM 極其強大,但它**主要是被訓練來生成與處理文本的**。自然世界與腦結構之間有對應關係——影像、聲音、動作是自然世界的一級公民,也就被投射進腦的結構裡。但商業世界看不到這種對應:商業世界的核心概念是**價格、供給、需求**,而它們在這套決策系統裡**不是一級公民**。

因此 Fetcherr 的立場是:**語言模型不足以做量化決策**。一個真正的量化決策系統需要能「感知市場」(market sensation)、預測未來市場動態、模擬多種情境、在情境中選擇並最佳化決策並執行,還要能**量化評估每個決策的 reward**。LLM 與 harness 層依然必要,但**最優決策仰賴的是直接在商業環境動態上訓練出來的工具**。

#### 主題二:market model 的內部結構(Uri,約 01:04–01:10)

- **與其他深度模型的關係**:技術與層別相同,差別在訓練資料。LLM ← 文本;視覺模型 ← 影像/影片;**large world model ← 物理環境的真實或模擬資料**;**market model ← 市場環境的資料**。
- **基本單位的類比**:LLM 的基本概念是進出模型的 **token**;視覺模型是高 × 寬 × 色深的**三維張量**,每格是代表光強度的像素。market model 則是**維度高得多**的結構——維度包含交易時間、交割時間、產品屬性、客群屬性等等;每個組合上的 voxel **不是視覺的而是機率性的**,代表某事件發生的機率:一筆成交、一次取消、一次競品調價。
- **完整 pipeline**:從多來源**整合資料** → 餵給 market model → 訓練後**預測未來市場動態** → 用預測**模擬多種未來情境** → 選定其中一個情境 → **把決策注入企業系統**。
- **資料層**:企業自有的專有資料(如歷史交易),再用外部世界**加值**——事件、資本市場資料、天氣,任何有預測力的資訊都能整合進來餵給模型。
- **可解釋性**:market model 也是深度學習系統、含 attention layer,所以可以像看 LLM 一樣「看進它的腦袋」。案例:某客戶的資料中已知**年中有新競爭者進入市場**(圖上以黃色表示),他們想知道模型對這件事投注多少注意力——結果模型很聰明地依據新舊競爭者各自的屬性,**按重要性重新分配了注意力**。

#### 主題三:怎麼讀 market model 的輸出(Uri,約 01:10–01:18)

輸出是多維的,而工程師是人類,一次只看得懂兩三、四個維度,所以得**切片**:固定住某個特定產品、某類客戶、某個交易時間與交割時間,只留下少數維度來玩。

典型切片是:**x 軸 = 我們自己的定價,y 軸 = 競品的定價,顏色 = 期望需求**。這張圖**由模型自動產生**——它從歷史資料就知道怎麼量化期望需求。讀法很直覺:

- **藍色區**=期望需求低,對應我們價格高於或遠高於競品的區域。
- **紅色區**=期望需求高,對應相反情況。
- 兩者之間是 **equilibrium line**:買方對這個價差**不在意**的無差異線。

在不同位置切片,就能看出模型眼中不同市場的差異:某個市場**競爭影響極低**;另一個市場的 equilibrium line **右移了 50 個價格單位**,意思是我們的產品在該市場的**感知價值較高**;還有的市場**對比度很高**,代表競爭激烈到「**每一分錢都有差**」。

需求曲面也會隨時間變。他們拉了一個航空定價的案例,把需求曲面的變化對照**燃油價格**——今年四月燃油價格上漲時,模型預測的需求也隨之受到影響。

**從預測到決策**:有了預測就能用**商業場域的 digital twin** 模擬每個定價政策的期望 reward。簡化案例把決策政策視為兩個參數,每個組合對應一個期望 reward(例如營收)。關鍵在於這些預測是**持續進行**的,會反映不斷流入的新資料——而資料流入會改變 **reward landscape**,因為現實一直在變。企業想要的是永遠站在山頂;這張地形圖底下藏著好幾座山丘,**每座山丘就是一個 decision regime**,當現實改變、regime B 的山比 regime A 高時,系統要知道該搬過去。

**驗證**:每次部署都做 A/B——在部分市場上線作為 target group,對照一組相關的 control group。結果反覆顯示統計顯著的營收提升:營收分布明顯右移,**平均約 7%**。

他把整套工具的意義定位為:**把決策產業從「靠通用 harness 工程」的做法,推向真正企業級、真正可靠的 agent operations。**

#### 主題四:數學基礎——forecaster + optimizer(Hadar,約 01:19–01:27)

Hadar 承接的方式是:先把「為什麼 LLM 會在高風險量化決策上失手」講到數學層級。

任何有意義的商業決策都要**配對兩種能力**:

1. **Forecaster / predictor**:告訴你市場或商業目標會怎麼變。數學上是 **point forecast**——從時間 t 往未來的 horizon 預測你在乎的訊號(這裡是需求)。輸入包含:已知的過去(過去需求與其分布)、**covariates / exogenous variables**(產品當時的表徵、對應價格)、**static features**(產品 ID 等不隨時間變的屬性),以及**已知的未來**(預期假期、近期高信心天氣、星期幾等時間特徵)。
   - 換掉 output head,point forecast 就變成**分布預測**:因為企業想知道不確定性、想用信心區間思考。可以是參數化的神經分布,也可以用 **quantile** 描述不確定性。
2. **Optimization process**:拿預訓練好的機率 forecaster,在給定 reward `u`、context `s`(過去資訊、價格訊號、靜態資訊)與**可行動作集合**(怎麼定價、配多少庫存)之下,找出最大化目標的動作。例如動作 = 價格、目標 = 營收 = 需求 × 價格:把**反事實價格**連同完整 context 餵進去,看對應需求如何,再最佳化。
   - **永遠有 hard/soft constraints**:價格不得超出上下界;連續幾期的定價不能有太高變異;還有**順序約束**——經濟艙的票價絕不可以高於商務艙。

**為什麼 naive agent 會失敗**,理由和這些工具存在的理由是同一個:它可能沒有能在 out-of-distribution 情境下泛化的 forecaster,或者根本沒有任何堪用的 forecaster(「如果我丟給 Claude Code 一句『預測價格會怎麼走』,我會說它大概會覺得有點困難」);而且它也沒有一個能穩定套用約束、最大化商業目標的最佳化流程。

#### 主題五:把能力接進 harness(Hadar,約 01:30–01:42)

他直接展示可執行的程式碼路徑:

- **Market model 預訓練設定**:Ray 超參搜尋設定、input size、內部隱藏層大小、learning rate;以及特徵集合(已知過去 / 已知未來 / 靜態)。航空客戶的例子裡,static features 是艙等、航線方向等。損失用 distribution-based loss,自訂深度網路吃一段 **look-back window**、預測分布到 horizon。他順帶提到這套與 Andrej Karpathy 的 auto research 完全相容——但**他們刻意不放手讓它自動搜**,因為預訓練模型要的是一致性與保證。術語則沿用開源時序框架 **Nixtla**(他強調雙方沒有合作關係,純粹推薦其最佳實務)。
- **推論輸出**:載入 checkpoint 與特徵選擇/編碼,forward pass 產出 **quantile forecast**(第 10、50、90 分位)。重點觀念:談需求時要看的**不是單一需求值,而是需求在不同價格點的變化**——也就是 econometrics 101 的 **demand curve**。再從中做聚合:整個 horizon 的平均、營收(價格 × 需求)、不確定性衡量;而對需求取**高階導數**就得到 **elasticity**(彈性)以及營收極大值的位置。
- **約束下的最佳化**:一個裝著價格約束的 data class(需求上下界、max step 讓連續期的定價變動不超過門檻),一個在最佳化過程中套用約束的私有函式;呼叫 market model 的 forward pass 取得 horizon 上的需求分布,用 `scipy.optimize.minimize_scalar`,再用 helper 模擬 horizon 上的營收。他用一張圖示意:營收地形上有一條**硬約束底線**,原本的全域極大在 A,加上約束後只能落在**局部極大 B**——並提醒現實的營收地形「很少這麼漂亮,也很少可微」。
- **包成 tool**:用 **Claude Agent SDK**(他強調「我們並不是跟 Claude 合作」,只是這套的功能對熟悉 Claude Code 的人最好懂)。`predict_market_dynamics` 這個 tool 以 Pydantic 風格結構描述設定,輸入先被驗證,才去呼叫真正的預測(抽象在 `capabilities.py`),回傳結構化輸出——quantile、elasticity 等。每個能力都照這樣包一個專屬 tool。
- **MCP 與工具分群**:Claude SDK 對 MCP server 提供抽象。一組是 **data capabilities**(GCP bucket,讓 agent 去撈真實歷史市場資料),另一組是 **fetcherr capabilities** MCP——把前述工具薄薄包一層 server。最後分成三群:data tools、large market model tools(市場動態預測 + 最佳化)、evaluation tools。
- **Sub-agent 階層**:一個 analyst factory 加一個 analyst initializer,定義**三個 sub-agent + 一個 orchestrator**。Orchestrator 是 **revenue manager**,有自己的 system prompt;三個分析師分別負責**市場動態**、**定價政策**,以及一個 **QA analyst**——負責確認預測與政策是否合理。他強調這些是**完全可執行的程式碼**。
- **Hook 與 grounding**:用 **PostToolUse** hook matcher 攔截工具呼叫後的時點,做自訂行為,記錄他們稱為 **grounding** 的東西——**agent 在推理過程中,到底有沒有真的用上這些工具**。最後全部塞進 `ClaudeAgentOptions`:revenue manager 的 system prompt、allowed tools、MCP server、sub-agents、hooks,再加一個簡單的 query loop 做輸出記錄。

#### 主題六:對照實驗「Is the price right?」(Hadar,約 01:43–01:52)

**設定**:兩個 agent 問同一個問題。

- **A:純 Claude Code harness**——有推理、有網路存取、能自己寫程式跑程式,「想幹嘛就幹嘛」。
- **B:Fetcherr 的 market model agent**——多了上述能力工具,其餘幾乎相同。

**題目**(客戶真實資料,已匿名化):年對年,某市場某產品的**需求下降 22%**,同期**價格上漲超過 60%**。這合理嗎?**答案並不顯然**——你可以說是漲價導致需求下降,但需求下降也可能是別的原因造成的。

**過程觀察**:兩者都產出了含思考過程的 markdown 與一份建議 CSV(漲/降價、幅度多少)。

- 純 Claude agent 一路 bash:寫 Python script、跑統計、用它最愛的 pandas,產出關於歷史資料、模式、相關性的 CSV。做了相當多事。
- Market model agent 則是**大量使用工具**,並把工具結果再聚合:解析結果、建產品清單、彙整最佳化結果。純以工具呼叫次數看,它用得多得多。

**最有價值的發現**——把工具呼叫按分析師分群後,他們看到:配備工具的 agent 在預測某個產品的需求時,**識別出該預測的不確定性偏高**(可能是歷史資料不夠)。這是 **QA analyst** 的功勞:他用 `evaluate_forecast` 工具把這件事**標記出來**,上報給老闆 revenue manager,revenue manager 再把 price analyst **重新派到那個市場的子集**上——這就是圖上那個工具呼叫的尖峰。

**結果**:在一個有六個產品的市場,Fetcherr 這組分析師建議 **ship 五個價格**,第六個(不確定性高的那個)**標記出來留給 revenue manager 處理**,並寫進 rationale 與建議書。而沒有工具的 agent **全部照 ship**——它根本沒有評估不確定性的機制。

**放大看單一產品**(當時定價 $1,100):

- **純 LLM agent**:建議**漲價 $200**。
- **Fetcherr agent**:建議**降價約 $250**。

同一份資料、不同推理、**方向與幅度都完全相反**的結論。

**Fetcherr agent 的推理鏈**:呼叫 market model,發現在該價位**彈性絕對值大於 1**,因此建議降價;在**無約束**設定下,最佳點會落到彈性最大的 **$828**。(彈性 = 價格變動百分之一會造成需求變動百分之幾。)它自己寫下的 rationale:「這條航線的需求是有彈性的,每降價 1% 帶來約 **1.4%** 更多訂位,在營收上足以抵過票價的下降。」接著 revenue manager 呼叫價格最佳化工具,因為**有約束**、而且要看整組出發日期,無法真的坐在極大值上,最後落在 **$863**;過程中它還識別出該出發日**有假期**,指出在假期需求可能更高的情況下,把需求跨價格平均可能會低估、應該定得更高。最終 revenue manager 把 $828 與 $863 收斂、四捨五入,**ship 出 $850**——估計為該產品帶來**超過 6% 的營收提升**。

**純 LLM agent 的失敗模式**:它「真的很努力了」,但**把相關當成了因果**。它在彼此未必相關的市場之間做相關性分析,**從未固定單一產品、以反事實方式改變價格**。它的原話:「需求彈性在這個日期區間可以忽略,相關性接近零,所以把價格下限拉高幾乎沒有需求毀損的風險。」它據此錯誤地判定漲價不會傷需求。但彈性是真實存在的——在無偏的營收估計下,這個決定的結果是約 **−8% 的營收**。

#### 主題七:整體架構的收斂觀點(Hadar,約 01:52–01:54)

他把整條 pipeline 收成幾條原則:

- **一個 manager** 跑迴圈、審視、彙整。
- **有專長的 sub-agent** 分工;**各自有各自的工具**;**不共享 context**,才不會被相似的工具搞混。
- **一個無偏的 QA 機制**,能檢查同儕 sub-agent 產出的成果。
- **關鍵是:它們全都使用量化能力**——數學在那裡、公式在那裡實作。revenue manager **知道自己不是這方面的專家,所以把事情委派出去**,才能給出可靠的答案。
- 再加上 **grounding**,你才看得見過程中到底發生了什麼。

最終立場:**LLM 負責 orchestration 與 agentic harness 的開發,是很強的;但真正的力量來自知道何時、以及如何把工作委派給值得信任的能力。LLM 編排,capabilities 承擔保證(guarantees)。**

### 金句

> "The architecture of such a decision-making system needs to reflect the complexity and the structure of the environment in which the decisions are made."(約 01:01,Uri)

從腦科學導出的整場核心原則。

> "The main concepts in the business world are concepts like price, like supply, like demand. And these concepts are not the first class citizens in this decision-making system."(約 01:03,Uri)

為什麼 language-centric 架構在商業決策上先天不足。

> "While the large language model orchestrates, the capabilities … those are the ones that carry the guarantees."(約 01:53,Hadar)

整場 workshop 的一句話總結。

## English Notes

A paired keynote and workshop: Uri Yerushalmi builds the argument (why LLMs are insufficient for quantitative decisions, and what a market model is), then Hadar Sharvit takes it down to the mathematics, the code, and a head-to-head experiment.

### TL;DR

- **The core argument is neuroanatomical**: the brain evolved specialized regions, and what matters isn't where they sit but the principle — **a decision system's architecture must reflect the complexity and structure of the environment it decides in**. In the natural world, images, sound, and movement are first-class citizens. In the business world, the first-class concepts are **price, supply, and demand** — and in a language-centric agentic workflow they are not first-class at all.
- **What a market model is**: same deep-learning machinery as everything else, different training data. LLMs train on text, vision models on images, large world models on physical-environment data, and **market models on market dynamics**. Its atom is neither a token nor a pixel but a **probabilistic voxel** on a high-dimensional grid (transaction time × delivery time × product attributes × customer class × …), giving the probability of an event — a transaction, a cancellation, a competitor repricing.
- **Interpretability comes for free**: market models have attention layers, so you can peek into the brain. In one case a new competitor entered mid-year and the model redistributed attention across competitors by their attributes.
- **The output is a demand landscape**: slice it with own price on x and competitor price on y and you can read expected demand, the **equilibrium line** where buyers are indifferent, and how competitive each market is (in some, competition barely registers; in others "every cent matters").
- **Decision-making is hill-climbing on a moving reward landscape**: each hill is a **decision regime**, and when reality shifts the system must know to move from regime A to a higher regime B. A/B tests show a statistically significant revenue uplift averaging around **7%**.
- **The implementation (Hadar)**: wrap forecasting and constrained optimization as tools, build a revenue-manager orchestrator over three sub-agents (market dynamics, pricing policy, QA) with the Claude Agent SDK, and use a PostToolUse hook to log **grounding** — whether the agent actually used the tools.
- **The most revealing result isn't accuracy, it's knowing what you don't know**: the equipped agent's QA analyst flagged one product's forecast as too uncertain via `evaluate_forecast`, escalated to the revenue manager, and got the price analyst re-dispatched — shipping five of six prices and leaving the sixth for a human. The vanilla agent shipped all six, because it had no mechanism for evaluating uncertainty at all.

### Discussion Threads

#### Thread 1: Why a language-centric architecture can't carry business decisions (Uri, ~00:54–01:04)

Uri establishes credibility first: three-plus decades building quantitative decision systems, formerly head of the AI division at an algorithmic trading firm, with a PhD in computational neuroscience. A very large share of volume on NASDAQ and other capital markets is now algorithmic, and back then those decisions rested on models predicting future market dynamics. But capital markets drifted into a **speed** contest, and what he always wanted was to decide well **by being smart, not by being fast** — which is why he moved to markets that aren't capital markets.

The argument starts in biology. Over hundreds of millions of years the brain evolved regions specialized for different kinds of natural data: visual cortex for vision, prefrontal cortex for planning, others for sound, taste, and touch. "What's important is not the exact location of each of these regions" — what's important is what it demonstrates: **the architecture of a decision-making system needs to reflect the complexity and structure of the environment in which decisions are made.**

Compare that with agentic workflows making business decisions today. At the center sits a language model, wrapped in harnessing layers and perhaps some visual models. Those language models are extremely powerful — but they are trained **primarily to generate and process text**. There is a correspondence between the natural world and the structure of the brain that decides in it: images, sound, and movement are first-class citizens of the natural world and are projected into the structure of the decision-maker. In the business world that correspondence is missing. The central concepts are **price, supply, and demand**, and they are not first-class citizens of a language-centric system.

Hence Fetcherr's position: **language models are not enough for quantitative decisions.** Such a system needs market sensation, forecasting of future market dynamics, simulation of scenarios, selection and optimization among them, action, and quantitative evaluation of each decision's reward. LLMs and harness layers remain essential — but **the optimal decisions depend on tools trained directly on the dynamics of the business environment.**

#### Thread 2: Inside the market model (Uri, ~01:04–01:10)

- **Relation to other deep models**: same techniques, same kinds of layers — the training data is the tweak. LLMs ← text; vision models ← images and video; **large world models ← real or simulated physical-environment data**; **market models ← market-environment data**.
- **The atomic unit**: an LLM's basic concept is the **token** going in and out. A vision model's is a **3D tensor** — image height × width × color depth — where each cell is a pixel representing light intensity. A market model is far more multi-dimensional: dimensions include transaction time, delivery time, product attributes, customer-class attributes, and more. Each combination holds a voxel that is **not visual but probabilistic** — the probability of an event occurring: a transaction, a cancellation, a competitor repricing.
- **The pipeline**: consolidate data from many sources → feed the market model → once trained, predict future market dynamics → use those predictions to simulate future scenarios → pick one → inject the right decision into enterprise systems.
- **The data layer**: proprietary enterprise data such as historical transactions, enriched from the outside world — events, capital markets data, weather, anything with predictive power.
- **Interpretability**: because the market model is a deep-learning system with attention layers, you can peek into its brain the same way you would an LLM. In one customer's data they knew a new competitor joined the market mid-year (shown in yellow) and wanted to see how much attention that entrance drew. The model was smart enough to redistribute attention across competitors according to their attributes and importance.

#### Thread 3: Reading the market model's output (Uri, ~01:10–01:18)

The output is multi-dimensional; humans can hold two, three, maybe four dimensions at once, so you **slice the cube** — fix a specific product, customer type, transaction time, and delivery time, and vary only a few dimensions.

The canonical slice puts **own price on x, competitor price on y, and expected demand as the surface**. These plots are **generated automatically** — the model already knows how to quantify expected demand from historical data. Reading them is intuitive:

- **Blue** = low expected demand, where our price is higher or significantly higher than the competitor's.
- **Red** = high demand, the opposite case.
- Between them the model finds an **equilibrium line** — where buyers don't really care about the difference.

Slicing elsewhere reveals what the model thinks of different markets: one where competition has very low impact; one where the equilibrium line shifts right by 50 price units, meaning our product's perceived value there is higher; and one that's far more competitive, with higher contrast, "where every cent matters when making the pricing actions."

The demand surface also moves over time. In an airline pricing case they tracked it against **fuel prices** — when fuel prices rose around April this year, predicted demand shifted accordingly.

**From prediction to decision**: with predictions in hand, a **digital twin** of the business arena simulates the expected reward of each pricing policy. In a simplified case the policy is two parameters, and every combination has an expected reward such as revenue. Crucially these predictions run **continuously** and reflect data flowing into the market model — and that inflow reshapes the **reward landscape**, because reality changes all the time. The business wants to sit on the peak of the hill. Several hidden hills lie under that surface, and **each hill is a decision regime**; when reality changes such that regime B's hill is higher than regime A's, the system needs to know to move.

**Validation**: each deployment goes out on a subset of markets as the target group, compared against a correlated control group. Repeatedly, these systems show statistically significant revenue uplift — the revenue distribution shifted right by roughly **7% on average**.

He frames the whole toolset as what bridges the decision-making industry's transition **from practices based on general harness engineering to genuinely enterprise-grade, reliable agent operations**.

#### Thread 4: The mathematics — forecaster plus optimizer (Hadar, ~01:19–01:27)

Hadar picks up by taking "why LLMs struggle with high-stakes quantitative decisions" down to the math.

Any meaningful business answer pairs **two capabilities**:

1. **A forecaster** telling you how the market or business objective will move. Formally a **point forecast**: from time t, predict the signal you care about (here, demand) out to a horizon. Inputs include the known past (past demand and its distribution), **covariates / exogenous variables** (a product's representation and associated price), **static features** invariant in time (product IDs and properties), and information **known into the future** (expected holidays, near-term weather at high confidence, calendar features like day of week).
   - Swap the network's output head and the point forecast becomes a **distribution**, because businesses want to reason about uncertainty and confidence — either a parameterized neural distribution or uncertainty expressed via **quantiles**.
2. **An optimization process** that takes the pre-trained probabilistic forecaster and, given a reward `u` to maximize or minimize, a context `s` (past information, price signals, static features), and a **feasible action set** (how to price, how much inventory to allocate), finds the action maximizing the objective over the horizon. With price as the action and revenue as the objective (demand × price), you feed a **counterfactual price** plus the full context into the horizon and see the associated demand.
   - There are always **hard and soft constraints**: prices must stay within bounds; consecutive pricing decisions must not swing wildly; ordering must hold — an economy ticket must never be priced above business class.

**Why naive agents fail** is the same reason these tools exist: they may lack a forecaster that generalizes out of distribution, or lack any usable forecaster at all ("if I were to give Claude Code a query, predict how the price is going to look, I would argue it's going to find it a bit difficult"), and they certainly lack an optimization process that consistently applies constraints while maximizing a business objective.

#### Thread 5: Plugging the capabilities into a harness (Hadar, ~01:30–01:42)

He walks through runnable code:

- **Market model pre-training config**: Ray hyperparameter tuning, input size, internal hidden sizes, learning rate, plus feature sets (known past, known future, static). In an airline client's case the static features are cabin, flight direction, and so on. A distribution-based loss serves as criterion for a custom deep network consuming a **look-back window** and predicting a distribution into the horizon. He notes this is fully compatible with Andrej Karpathy's auto research — but they deliberately don't let it run loose, because for a pre-trained model they want consistency and guarantees. Terminology follows the open-source time-series framework from **Nixtla**, which he recommends (no commercial relationship — he just thinks they do best practices).
- **Inference output**: load a pre-trained checkpoint plus feature selection and encoding of numerical and categorical features, run a forward pass, and get a **quantile forecast** (10th, 50th/median, 90th). The key conceptual point: with demand you don't care about a demand *value* but about **how demand differentiates across price points** — the demand curve from econometrics 101. From there come aggregations: mean over the horizon, revenue (price × demand), uncertainty measures — and **higher-order derivatives of demand give elasticity** and locate the revenue maximum.
- **Constrained optimization**: a data class for price constraints (lower/upper demand bounds, a max step so consecutive price policy values don't exceed a threshold), and a private function applying constraints during optimization. The market model's forward pass supplies the demand distribution across the horizon; `scipy.optimize.minimize_scalar` does the work; a helper simulates revenue into the horizon. His illustration: a revenue landscape with a hard constraint floor, where the global maximum at A becomes unreachable and the constrained optimum settles at local maximum B — with the caveat that real revenue landscapes are "rarely this nice" and rarely differentiable.
- **Wrapping capabilities as tools**: built on the **Claude Agent SDK** (he's explicit that they aren't working with Claude — it's just the most legible framing for a Claude Code-familiar audience). The `predict_market_dynamics` tool takes a Pydantic-style config so inputs get validated before invoking the real prediction (abstracted in a `capabilities.py`), returning structured output exposing quantiles, elasticity, and more. Every capability gets its own designated tool.
- **MCP and tool clustering**: the SDK abstracts MCP servers. One is **data capabilities** — GCP buckets, so the agent can fetch real historical market data. The other is a **fetcherr capabilities** MCP, a thin server wrapping the tools. They cluster into data tools, large market model tools (market-dynamics prediction and optimization), and evaluation tools.
- **Sub-agent structure**: an analyst factory plus an analyst initializer define **three sub-agents and one orchestrator**. The orchestrator is a **revenue manager** with its own system prompt; the analysts cover market dynamics, pricing policy, and **QA** — the last making sure predictions and policies are sensible. All of it is fully runnable code.
- **Hooks and grounding**: a **PostToolUse** hook matcher catches the moment after a tool fires, enabling custom behavior that logs what they call **grounding** — whether, during its reasoning, the agent actually used the tools they defined. Everything assembles into `ClaudeAgentOptions`: the revenue manager's system prompt, allowed tools, MCP server, sub-agents, and hooks, plus a simple query loop for logging results.

#### Thread 6: The head-to-head, "Is the price right?" (Hadar, ~01:43–01:52)

**Setup**: two agents, same question.

- **A: a plain Claude Code harness** — reasoning, web access, able to write and run its own code, "it could do whatever the hell it wants."
- **B: Fetcherr's market-model agent** — the same, plus the capabilities that let it understand the market.

**The question** (real, anonymized client data): year over year, demand for a specific product in a specific market fell **22%** while prices for that product rose **more than 60%**. Is that sensible? The answer is not trivial — you might say demand fell because price rose, but demand could have fallen for some other reason entirely.

**What they did**: both produced markdown rationales and a recommendation CSV — raise or lower the price, and by how much.

- The vanilla Claude agent bashed away: wrote Python scripts, ran statistics, used pandas ("his favorite tool"), and produced CSVs covering historical data, patterns, and correlations for that product and market. It did quite a lot.
- The market-model agent used its capabilities extensively and then aggregated the results — parsing outputs, building product lists, aggregating optimization results. Taken at face value, it made far more tool calls.

**The most interesting finding** came from clustering tool calls per analyst: while predicting demand, the equipped agent **identified high uncertainty in one product's forecast**, possibly because the historical data wasn't substantial enough. This was the **QA analyst's** doing — it flagged the issue using the `evaluate_forecast` tool and escalated to its boss, the revenue manager, who re-dispatched the price analyst on that subset of the market. That's the spike visible in the tool-call chart.

**The outcome**: in a market with six products, the Fetcherr analysts recommended **shipping five prices** and flagged the sixth — the uncertain one — for the revenue manager, writing it into the rationale and the recommendations. The unaided agent **shipped everything**; it had no mechanism to evaluate uncertainty.

**Zooming into one product** priced at $1,100 at that moment:

- **Vanilla agent**: recommend a price **increase of $200**.
- **Fetcherr agent**: recommend a price **decrease of about $250**.

Same data, different reasoning, and conclusions that differ in both magnitude and direction.

**The Fetcherr agent's chain**: it invoked the market model and found that at this price the **absolute elasticity exceeds 1**, so it recommended a decrease; in an unconstrained setup the optimum fell at **$828**, where elasticity is maximal. (Elasticity being how much a percentage price change moves demand.) Quoting its own rationale: "Demand on the route is elastic — every 1% price reduction yields about 1.4% more bookings, more than offsetting the fare reduction in revenue terms." The revenue manager then invoked the price optimization tool; because it was constrained and had to look across the entire set of departure dates, it couldn't sit where the maximum truly lies and settled at **$863**, noting in its rationale that a holiday falls on that departure date — so averaging demand across price in that market could understate what should be charged. It reconciled $828 and $863, rounded for simplicity, and shipped **$850** — an estimated **6%-plus revenue uplift** on that product.

**How the vanilla agent failed**: it was trying its best, but it **confused correlation for causation**. It ran correlation analysis across markets that don't necessarily correlate with each other, and never fixed a specific product to vary the price counterfactually. In its own words: "demand elasticity is negligible … correlation of nearly zero. So raising the floor carries near-zero demand destruction risk." Elasticity, unfortunately for it, is a real thing — and in an unbiased revenue estimation the decision came out at roughly **−8% revenue**.

#### Thread 7: The architecture, summarized (Hadar, ~01:52–01:54)

The end-to-end shape, distilled:

- **One manager** runs the loop, reviews, and aggregates.
- **Specialized sub-agents** split the work, each with its own tools, **not sharing context** so they don't get confused by similar tools.
- **An unbiased QA mechanism** able to check its counterparts' assets.
- **Crucially, all of them use quantitative capabilities** — that's where the mathematics lives and where the formulas are implemented. The revenue manager knows it isn't the expert here and **delegates** in order to give a meaningful, reliable answer.
- **Grounding** makes the whole process visible after the fact.

The closing position: there is great power in combining LLM orchestration and agentic harness development with knowing **when and how to delegate** to capabilities you can trust. **The LLM orchestrates; the capabilities carry the guarantees.**

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Market Model / Large Market Model (LMM) | Fetcherr 訓練於市場動態(而非文本)的深度模型,量化決策的核心 | Fetcherr's deep model trained on market dynamics rather than text; the core of their quantitative decisions | 已部署於航空等產業客戶 |
| 機率 voxel / probabilistic voxel | market model 的基本單位:高維格點上某事件發生的機率 | The market model's atom: probability of an event on a high-dimensional grid | 對照 LLM 的 token 與視覺模型的 pixel |
| Digital twin | 用來模擬各定價政策期望 reward 的商業場域孿生體 | Twin of the business arena used to simulate each pricing policy's expected reward | |
| Decision regime | reward landscape 上的一座山丘;現實改變時系統需切換 regime | A hill on the reward landscape; the system switches regimes as reality shifts | |
| Nixtla | 開源時序預測框架,Hadar 沿用其術語並推薦 | Open-source time-series framework whose terminology he follows and recommends | 他明確表示雙方無合作關係 |
| Claude Agent SDK | 用來建構 tool / sub-agent / hook 的 harness | The harness used for tools, sub-agents, and hooks | 他明確表示「we're not working with Claude」 |
| MCP servers | data capabilities(GCP bucket)+ fetcherr capabilities(能力工具的薄包裝) | data capabilities (GCP buckets) + fetcherr capabilities (thin wrapper over the tools) | |
| `evaluate_forecast` | QA analyst 用來標記預測不確定性的工具 | The tool the QA analyst used to flag forecast uncertainty | 實驗中最關鍵的差異點 |
| `scipy.optimize.minimize_scalar` | 約束下最佳化的實作 | Used for the constrained optimization | |
| Andrej Karpathy's auto research | Hadar 說其 pre-training 設定與之相容,但刻意不採用 | Their pre-training config is compatible with it, but they deliberately don't use it | 需要一致性與保證,故不放手自動搜 |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Fetcher / Fcher | Fetcherr |
| Urieli / Uri Eli | Uri Yerushalmi |
| Hadar Sharvit(尚可)/ "former director" | Hadar Sharvit(議程職稱 Director of Deep Learning) |
| Nyxla | Nixtla |
| cloud / clot / cloud code / cloud agent SDK / cloud SDK | Claude / Claude Code / Claude Agent SDK |
| pyantic | Pydantic |
| scypi minimize scaler | `scipy.optimize.minimize_scalar` |
| coariantss | covariates |
| Andre Karpathy | Andrej Karpathy |
| "verified by the Asian P4 invoking" | "validated by the agent before invoking" |
| market modal | market model |
| unaded agent | unaided agent |
| MC MCP | MCP |
| threedimensional tensors | three-dimensional tensors |
| econometric 101 | econometrics 101 |

## 待確認 / To Verify

- **Hadar Sharvit 的職稱**:官網議程寫 Director of Deep Learning(frontmatter 以此為準);但 Uri 介紹他為 "VP of large market model and machine learning",Hadar 本人自述「former director of deep learning,now entering VP of the market model」——三者不一致,可能是演講當下正在轉任。/ Title discrepancy: the agenda says Director of Deep Learning (used in frontmatter), Uri introduced him as "VP of large market model and machine learning," and Hadar described himself as a former director of deep learning now moving into the VP role. Likely a transition in progress.
- **NASDAQ 演算法成交量比例**:字幕為 "almost 20% 90%",明顯是自動字幕吃掉數字(推測原句約為 80–90%),需看影片確認。/ The algorithmic-volume share of NASDAQ — captions garble it as "almost 20% 90%"; likely 80–90%, needs verification from the video.
- **A/B 測試的約 7% 營收提升**:講者說是「反覆出現的統計顯著結果」,但未說明樣本範圍(單一客戶 vs 全部部署)。/ The ~7% average revenue uplift is described as repeatedly statistically significant, but the sample scope (one client vs all deployments) wasn't stated.
- **Andrej Karpathy 的 "auto research"**:指涉的專案/工具名稱與連結待查證。/ Exact project or tool referred to as Karpathy's "auto research."
- **實驗中兩個 agent 的底層模型與版本**未說明(只說是 Claude Code harness)。/ The underlying model and version used for both agents in the experiment was not stated beyond "Claude Code harness."
- **$828 / $863 / $850 與 6%、−8% 的營收估計**皆為 Fetcherr 內部估算,無公開出處。/ The $828 / $863 / $850 prices and the +6% / −8% revenue estimates are Fetcherr's own internal estimates with no public source.
