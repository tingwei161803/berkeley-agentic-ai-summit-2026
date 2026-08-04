---
title: "Self Optimizing Agents"
title_zh: "會自我最佳化的 Agent"
speaker: "Ori Goshen"
affiliation: "Co-Founder & CEO, AI21 Labs"
type: talk
stage: Atlas
date: 2026-08-02
session: "Session 1: Enterprise AI"
video: "https://www.youtube.com/watch?v=LGW_6P1CMC8&t=1086s"
video_range: "00:18:06–00:35:44"
transcript: "tmp/[English (auto-generated)] Atlas Stage - August 2nd - Morning Session [DownSub.com].srt"
status: draft
tags: [cost-optimization, inference, pareto-frontier, model-routing, agent-ops]
---

# 會自我最佳化的 Agent(Self Optimizing Agents)

**一句話總結**:Agent 上了生產線之後,真正的瓶頸是「在前沿以合理成本運作」;而模型、檢索、scaling、模型組合、執行策略構成的組態空間大到人工搜不完,所以最佳化必須自動化、可觀測,而且能在新模型出現時自動重新適配。
**One-line summary**: Once agents reach production the binding constraint is operating economically at the frontier, and the configuration space — models, retrieval, scaling, model portfolios, execution strategies — is far too large to search by hand, so optimization has to be automated, observable, and robust to the next model release.

## 中文筆記

### TL;DR

- **產業風向已經轉了**:「token maxing 基本上結束了,現在大家談的是 token efficiency」。真正的問題變成「每一塊錢投資能換到多少客戶成效」。
- **客戶的痛點很一致**:「這個 agent 我們對品質很滿意,但如果每一個 PR、每一通電話、每一筆訂位、每一筆交易都跑它,成本高到不可行。」
- **組態空間有四層**,每一層都能推出新的 Pareto frontier:模型與檢索策略 → scaling(垂直/水平)→ 模型組合(portfolio)→ 執行策略(串接、升級、提早停止)。
- **模型組合是最反直覺的一層**:不同模型覆蓋空間的不同區域,只要好好量測 co-variance 與各模型的貢獻,「全部一起用會大於個別使用的總和」;在他們的實驗中約可**用同樣品質換到約 50% 的成本**。
- **為什麼一定要自動化**:搜尋空間太大、人工一定漏掉機會;而且新模型每隔一陣子就出、定價會變、流量與任務分布也會漂移——手動調一次就過期了。

### 重點整理

#### 問題:從實驗走向生產後,經濟性成為主瓶頸(約 00:19–00:21)

過去幾個月他看到許多 AI 系統從實驗階段真正進入生產、開始規模化部署,而這帶來一組新的挑戰,最明顯的一個就是**如何在前沿以可負擔的成本運作**。

他說客戶反覆講同一句話:我們有個 agent,對它的表現和整體品質都滿意,但如果要把它套到**每一個** PR、每一通電話、每一筆訂位、每一筆交易上,成本會高到不可行。

所以產業的重心變了——「token maxing 基本上結束了,大家現在講的是 token efficiency」。真正該問的問題是:**每單位 token 投資能換到最好的表現嗎?每一塊錢投資能換到最好的真實客戶成效嗎?**

他用一張圖說明目標:黑線是某公司(圖上以 Coinbase 為例)的 token 用量,長條是成本、依模型拆分。企業想達到的狀態是**讓用量繼續往上、但把成本曲線從用量曲線上「脫鉤」**。

典型的最佳化流程是:拿一個 agent → 準備數種組態 → 實驗 → 找出 Pareto frontier(一組可選的操作點)→ 選一個 agent 候選 → 從那裡開始演化系統。多數團隊心裡都有一個目標操作區間(成本 × 品質),但要進到那個區間並不容易。

#### 組態空間的四個維度(約 00:23–00:33)

他形容組態空間是個「漫畫式」的龐然大物:模型本身與模型權重可以換、模型選擇在今天百家爭鳴的情況下差異極大,再加上 **harness**——工具規格、prompts、skills、程式碼、外圍 scaffold——可動的零件多到本身就是個難題。

**維度一:模型 × 檢索策略。** 以 **BrowseComp**(deep research benchmark,因為答案就在給定語料中所以可驗證)為例,他們把不同模型配上不同檢索組態(dense retrieval、sparse retrieval、late interaction)逐一標到圖上。實驗結果是 **GPT-5 家族搭配 late-interaction 檢索**,以及 **MiniMax**,構成當時的 Pareto frontier——你會在這兩個選項之間挑。他說這是最基本的一步,多數團隊上線前都會做。

**維度二:scaling / 執行策略。**
- **垂直**:thinking token 的量、迴圈迭代次數、各種 fix-repair loop。
- **水平**:產生多個候選,再選擇或合併(best-of-n:同一個模型平行 rollout,挑最好的一個)。

同一個 benchmark 上,原本較便宜但品質較低的 MiniMax,**經過水平 scaling 之後可以達到前一張圖上最高品質候選的水準**。GPT-5 也在品質對成本上有所提升。結論是:光是加上 scaling 這個維度,可選的運行方式就多了一整層。

**維度三:模型組合(portfolio / ensemble)。** 不只從同一個模型生成候選,而是**從不同模型**生成——可搭配調整過的 prompt 與工具定義——再把這些輸出合成最佳結果。他把這稱為產業從 **token maxing 走向 model maxing**。

關鍵觀察是:不同模型覆蓋空間中的不同區域,只要你**認真量測 co-variance 與每個模型的貢獻**,就能拿到很大的好處——「全部模型一起用的總和,大於分別使用它們」。套上 portfolio 策略之後會浮現一條**新的 Pareto frontier**,而且這些配比**可以按任務學出來,不必人工找**。他報告的數字是:相較先前的 state-of-the-art 設定,在**大致相同的品質下成本約少 50%**;把「準確度 vs 成本」換成「準確度 vs 延遲」,原理完全一樣。

**維度四:執行策略。** 呼叫這些模型的**串接方式**還可以再變:升級(escalation)策略、優先呼叫哪個模型、設定不同的停止門檻——這些都會影響表現。他換到另一個 benchmark(字幕聽作 "three rebench",見待確認)展示這一層對**成本與延遲**權衡的影響:

- **單純 best-of-n**:跑完所有候選,最後挑最好的。
- **cascading(串聯)**:從最弱的模型開始往上走,一旦對結果有足夠信心就停 → **省成本**。
- **平行 + 提早停止**:不省成本,但省延遲 → **優化速度**。

也就是說,在**同樣的品質水準**上,你可以靠切換執行策略去挑你要的成本/延遲取捨。

他最後給了一個很具體的類比:法律工作是一群 junior intern 做粗活 → associate 綜合出論點 → partner 下最終判斷。同樣的層級結構可以套到寫程式上——**用弱模型產生大量 rollout,用較強的模型為這些 rollout 補上更相關的資訊,最後由一個非常強的模型(他說 "a Fable level model")產出最終 patch 與決策**。結果是品質更好,而且**比直接用前沿模型便宜約 3 倍**。

#### 為什麼一定要自動化(約 00:33–00:35)

所有這些策略都是**可以學出來的**,但搜尋空間實在太大,人工調校一定會漏掉很多最佳化機會。更關鍵的是**環境會變**:新模型隨時會出、定價會調整、流量與任務分布也會隨時間漂移。這些都得跟著處理,所以手動搜索這個空間並不實際。

AI21 的做法是提供一套企業用的工具組:接手一個**既有的** agent——不管它用什麼框架、什麼 runtime、哪些模型——在**生產環境中、對齊真實生產流量**去最佳化它,讓它能持續演化到最好的性價比,並符合客戶自己的偏好。

他把自動化最佳化該有的三個性質收在結尾:**efficient**(過程本身要有效率)、**observable**(人要能看到不同取捨並自己選)、**future-proof**(新模型上市或分布漂移時容易調整)。相關研究每隔幾週會發在他們的部落格。

### 金句

> "Token maxing is basically over now. Everybody's speaking about token efficiency."(約 00:20:43)

一句話定調整場演講:效率取代規模,成為前沿部署的主題。

> "Moving from token maxing to model maxing."(約 00:27:49)

不是把單一模型榨到極限,而是把多個模型的長處榨出來。

> "The sum of all using all models is greater than using them separately."(約 00:28)

模型組合這一層之所以值得做的理由——差異化的覆蓋範圍本身就是可利用的資源。

## English Notes

### TL;DR

- **The industry's framing has flipped**: "token maxing is basically over — everybody's speaking about token efficiency." The real question is best real customer outcome per dollar invested.
- **Customers all say the same thing**: the agent's quality is fine, but running it on *every* PR, call, booking, or transaction would be prohibitively expensive.
- **The configuration space has four layers**, each capable of exposing a new Pareto frontier: model and retrieval strategy → scaling (vertical and horizontal) → model portfolios → execution strategy (chaining, escalation, early stopping).
- **The portfolio layer is the counter-intuitive one**: different models cover different regions of the space, so if you measure covariance and each model's contribution carefully, the sum of using all models beats using them separately — worth roughly 50% cost reduction at comparable quality in their experiments.
- **Why it must be automated**: the search space is too large to cover by hand, and it keeps moving — new models ship, prices change, and traffic and task distributions drift, so any hand-tuned configuration is already stale.

### Key Points

#### The problem: economics becomes the binding constraint in production (~00:19–00:21)

Over the past few months he has watched AI systems move from experimentation into production and start deploying at scale, which introduces a new set of challenges — the most obvious being how to operate economically at the frontier.

What he hears from customers, repeatedly: we have this agent, we're satisfied with how it functions and its overall performance, but if we wanted to apply it to every PR, every call, every booking, or every transaction, it would be prohibitively expensive.

Hence the shift in focus. The question worth asking is how to get the best possible performance per token invested, or the best real customer outcome per dollar invested. His illustrating chart plots one company's token usage (Coinbase in the example) as a line against cost as bars broken down per model; the state enterprises want is for usage to keep climbing while the cost curve decouples from it.

The typical optimization flow: take an agent, try several configurations, experiment, discover the Pareto frontier of operating points, select an agent candidate, and evolve the system from there. Most teams have a target operating zone in cost and quality — getting there is easier said than done.

#### Four dimensions of the configuration space (~00:23–00:33)

He describes the space as a caricature of levers: the model itself and its weights, model selection in a world where models have very different capability and performance profiles, and then the harness — tool specifications, prompts, skills, code, and the surrounding scaffold. That's a lot of moving parts before you begin.

**Dimension one: model × retrieval strategy.** Using **BrowseComp** — a deep-research benchmark that is verifiable because the answer is contained in the given corpora — they mapped candidates across models and retrieval configurations (dense, sparse, and late-interaction retrieval). Empirically, the **GPT-5 family with late-interaction retrieval** and **MiniMax** formed the Pareto frontier; you'd choose between those two. He notes this is the basic step most teams already perform before going to production.

**Dimension two: scaling and execution strategy.** Vertically, you can vary thinking tokens, loop iterations, or fix-repair loops. Horizontally, you generate multiple candidates and select or merge — best-of-n rolls the same model out in parallel and picks the winner. On the same benchmark, MiniMax (the cheaper, lower-quality option) reaches the quality of the top single-shot candidate once horizontally scaled, and GPT-5 also improves on quality relative to cost. The point is that adding this dimension opens a whole extra layer of viable operating points.

**Dimension three: model portfolios.** Rather than generating candidates from one model, generate them from *different* models — potentially with adjusted prompts and tool definitions — and combine the outputs into the most optimal result. He frames this as the industry moving **from token maxing to model maxing**.

The underlying observation: different models cover different areas of the space, so being diligent about measuring covariance and each model's contribution buys a lot. "The sum of all using all models is greater than using them separately." Applying a portfolio strategy exposes a new Pareto frontier, and the mixing proportions can be **learned per task** rather than discovered manually. His headline number: about **50% less cost for roughly the same quality** compared to the previous state-of-the-art setting. Swap cost for latency and the same principle holds.

**Dimension four: execution strategy.** How you chain the calls matters: escalation strategies, which model to prioritize, and stopping thresholds. Moving to a different benchmark for variety (heard as "three rebench" in the captions — see To Verify), he showed the impact on cost/latency trade-offs:

- **Plain best-of-n**: run all candidates, then pick the best.
- **Cascading**: start with the weakest model and work up, stopping once you're confident enough in the result — saves cost.
- **Parallel with early stopping**: doesn't save cost, but saves latency — optimizes for speed.

At the same quality level, you pick the execution strategy that matches whether you care more about speed or cost.

His closing example is a hierarchy analogy from legal work: many junior interns do the busy work, an associate synthesizes a thesis, and a partner makes the final call. The same shape applies to coding — **have a weaker model generate many rollouts, a stronger model enrich those rollouts with more relevant information, and a very strong model (he said "a Fable level model") produce the final patch and decision**. The result is better quality at roughly **3x cheaper** than using a frontier model throughout.

#### Why this has to be automated (~00:33–00:35)

All of these strategies are learnable, but the search space is huge and manual tuning will miss many optimization opportunities. More importantly, the environment keeps moving: a new model arrives, pricing changes, traffic and task distribution shift over time. Manually searching this space isn't practical.

AI21's answer is an enterprise toolkit that takes an *existing* agent — whatever framework, runtime, or models it uses — and optimizes it in production, aligned to that customer's production traffic, so it can continuously evolve toward the best price-performance according to the customer's own preferences.

He closed with three properties automated optimization needs: **efficient**, **observable** (so people can see the trade-offs and select among them), and **future-proof** (easy to adjust when a new model lands or the distribution shifts). Their research on the topic is posted to the company blog every few weeks.

### Quotes

> "Token maxing is basically over now. Everybody's speaking about token efficiency." (~00:20:43)

The framing for the whole talk: efficiency, not scale, is now the frontier-deployment story.

> "Moving from token maxing to model maxing." (~00:27:49)

Not squeezing a single model harder, but harvesting what several models are each good at.

> "The sum of all using all models is greater than using them separately." (~00:28)

The justification for the portfolio layer — differentiated coverage is itself an exploitable resource.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| AI21 Labs | 總部位於 Tel Aviv 的 AI lab,講者為共同創辦人暨 CEO | AI lab based in Tel Aviv; the speaker is co-founder and CEO | |
| BrowseComp | Deep research benchmark;答案含於給定語料,因此可驗證 | Deep-research benchmark; verifiable because answers live in the given corpora | 演講中主要的實驗場 / main experimental testbed |
| Late-interaction retrieval | 與 dense / sparse 並列的第三種檢索策略,在 BrowseComp 上表現最好 | Third retrieval strategy alongside dense and sparse; best-performing on BrowseComp | 搭配 GPT-5 家族構成 Pareto frontier |
| MiniMax | 較便宜、單次品質較低的模型;水平 scaling 後可追上最高品質候選 | Cheaper, lower single-shot quality; matches the top candidate once horizontally scaled | 字幕誤植為 "miniax" |
| AI21 企業 agent 最佳化工具組 | 接管既有 agent,依生產流量持續最佳化性價比 | Enterprise toolkit that optimizes an existing agent against production traffic | 演講中未點名產品名稱 / not named in the talk(見待確認) |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Ori Gosian / Ory Gosh / Orie | Ori Goshen |
| browse comp | BrowseComp |
| miniax | MiniMax |
| GP5 / GPT5 | GPT-5 |
| para frontier / parader frontier | Pareto frontier |
| prohibitly expensive | prohibitively expensive |
| co-variance | covariance |
| three rebench | 待確認(可能為 SWE-rebench)/ to verify (possibly SWE-rebench) |

## 待確認 / To Verify

- 第二個 benchmark(字幕作 "three rebench")的正確名稱。發音上最接近的公開 benchmark 是 **SWE-rebench**(arXiv:2505.20411,持續更新、去汙染的 SWE agent benchmark),但無法從逐字稿確認,需看投影片。/ The second benchmark, heard as "three rebench" — phonetically closest public benchmark is SWE-rebench (arXiv:2505.20411), but this needs slide confirmation.
- AI21 用來做 agent 最佳化的產品名稱:講者只說 "a suite / a toolkit",未點名。AI21 官網對外的 agent 最佳化產品為 **Maestro**,但無法確認演講中指的是否為同一個。/ AI21's optimization product was never named on stage; their public offering is Maestro, but the mapping is unconfirmed.
- 「約 50% 成本下降」與「約 3x 便宜」的實驗設定細節(基準設定、模型組合比例)只在投影片上,逐字稿未念出。/ Experimental details behind the ~50% cost reduction and ~3x cheaper figures were on slides only.
- Coinbase 用量/成本圖表的出處與時間區間未說明。/ Source and time window of the Coinbase usage-vs-cost chart were not stated.
