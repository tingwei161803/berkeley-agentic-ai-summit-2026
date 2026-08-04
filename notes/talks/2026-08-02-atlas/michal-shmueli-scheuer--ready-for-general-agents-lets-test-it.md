---
title: "Ready for General Agents? Let's Test It."
title_zh: "準備好迎接 general agent 了嗎?來測測看"
speaker: "Michal Shmueli-Scheuer"
affiliation: "Distinguished Engineer, AI Benchmarking and Evaluation, IBM Research"
type: talk
stage: Atlas
date: 2026-08-02
session: "Session 2: Agent Evaluation & Benchmarks"
video: "https://www.youtube.com/watch?v=-7AJJLwYW1Q&t=785s"
video_range: "00:13:05–00:27:52"
transcript: "tmp/[English (auto-generated)] Atlas Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [evaluation, benchmarks, general-agents, leaderboard, open-weights]
---

# 準備好迎接 general agent 了嗎?來測測看(Ready for General Agents? Let's Test It.)

**一句話總結**:Bitter Lesson 說通用終將勝過專用,agent 也不例外;但要證明一個 agent 真的「通用」,得先解決 agent 介面、環境介面、研究者介面三重標準化問題——IBM 用一層 Unified Protocol 中介層(Exgentic)做到不改 agent 也不改 benchmark 的任意組合評估,結果顯示 general agent 已能與各任務榜首的 domain-specific agent 打成平手。
**One-line summary**: The bitter lesson says generality wins, agents included — but proving an agent is general first requires standardizing three interfaces (agent, environment, researcher). IBM's answer is a Unified Protocol mediation layer (Exgentic) that lets any agent run any benchmark unmodified, and the resulting leaderboard shows general agents are already competitive with the top domain-specific agent on each task.

## 中文筆記

### TL;DR

- **論點**:延續 Sutton 的 bitter lesson——過去 NLP 從 summarization / extraction 這類 domain-specific 模型走向通用 LLM,agent 也會從今天的 domain-specific agent(金融、客服)走向 **general agent**:領域知識不再編碼在 agent 裡,而是留在環境端,agent 靠適應力探索新任務。
- **評估的真正瓶頸是標準化**,不是指標:每個 benchmark 對 agent 的期待不同、每個 agent 對環境的要求不同、每個研究者都自己寫一份 agent×benchmark 的黏合程式碼——不可能 scale。
- **解法是 Unified Protocol 中介層**:agent 用它原本的協定、benchmark 也用它原本的協定,中間做轉換,基於 task / context / actions 三個共通原語。兩邊都不用改。框架叫 **Exgentic**,產出 **Open (General) Agent Leaderboard**。
- **主要發現**:模型的影響大於 harness;general agent 未經任何再工程,就與各任務榜首的 domain-specific agent 相當;成績相近的 agent 成本可以差非常多。
- **開放權重模型的兩個警訊**:平均落後閉源模型,且在沒訓練過的任務(如 AppWorld)直接崩掉;更關鍵的是**對 harness 極度敏感**——Kimi 最佳 harness 與最差 harness 差 18%,換 harness 就必須重測。而且「open weights 比較便宜」在成本-品質圖上並不成立。

### 重點整理

#### 從 bitter lesson 推到 general agent(約 00:13–00:16)

本場基於三篇論文(ICLR、ICML,以及希望很快的 NeurIPS)。從 Richard Sutton 的 bitter lesson 出發:**通用性終究勝過 domain-specific 做法**。機器學習史如此,語言模型史也如此——大家一開始做 summarization、extraction 這類單一任務模型,最後全部收斂到能做所有任務的大模型。

今天的 agent 停在對應的「domain-specific」階段:金融 agent、客服 agent。她(以及一些同行)從歷史推論:未來屬於 **general agent**。

定義上的區分很關鍵:
- **Domain agent**:領域知識**編碼在 agent 內部**,知識就位後 agent 才能開始跟環境互動。
- **General agent**:agent 內部沒有領域知識,**一切都在環境端**;評估的是 agent 探索與適應新任務的能力。理想上同一個 general agent 可以換到不同環境而不必為每個環境重做工程。

因此評估的問題也變了:不再是單一任務的表現,而是**跨許多環境與任務的表現**。

好處:一個 general agent 對應多種 use case,不必養 100 個 domain-specific agent;改進集中化(memory、search 一改,所有 use case 受益);仍然可以客製,但起點是一個更好、更穩健的 agent。

她也誠實列出反方觀點(ICML 的 position paper 有詳細兩方論述):domain-specific agent 控制力更強、更有效率、更可預測;給 general agent 更多自主性會帶來難以預見的風險;還有人主張該通用的是**模型**而不是 agent。

#### 真正的瓶頸:三個介面都沒有標準(約 00:17–00:20)

要宣稱一個 agent 是通用的,就得證明它在不同環境與任務上都能運作——也就是得評估。而這件事一點都不 trivial,問題出在標準化,分三層:

1. **Agent 介面**:每個 benchmark 對 agent 的預期行為都不一樣。
2. **環境介面**:每個 agent 對環境要提供什麼資訊的假設都不一樣。
3. **研究者介面**:每個研究者為每一組 agent×benchmark 自己寫一份實作。

她強調這裡跟前一場(LLMArena)的情境相反:這裡談的是由學生與各種社群努力開源出來的 benchmark。而檢視現有框架,**沒有任何一個同時支援 multi-protocol benchmark、multi-protocol agent、agent 隨插即用、以及跨差異極大任務的通用性**。

#### 解法:Unified Protocol 與 Exgentic(約 00:20–00:21)

他們的框架 **Exgentic** 引入一層**中介層(mediation layer)**,稱為 **Unified Protocol**:agent 繼續用它原本的協定,benchmark 也繼續用它開發時的協定,框架負責在兩者之間做轉換。**benchmark 不改,所以維持原本設計意圖;agent 也不動。** 轉換建立在他們觀察到的三個共通原語:**task、context、actions**。

有了這層,就能把「任何 agent harness × 任何模型 × 任何 benchmark」做**笛卡兒積**,產出 **Open (General) Agent Leaderboard**:agent 欄、model 欄、各任務欄、平均成功率,再加上**成本**,並畫出 Pareto frontier——你可以依需求選點:要準就貴,能接受差一點就選便宜模型。

#### 從榜上讀到的發現(約 00:21–00:26)

1. **General agent 真的能不改就適應**:平均而言,大多數 agent 能完成所有被丟進去的任務類型。
2. **模型影響最大**:品質主要由模型驅動,但 agent harness 也有可觀影響。
3. **General vs domain-specific**:每個任務都取該任務榜上最強的 domain-specific agent,對比最強的 general agent——結果相當接近,而且 general agent 完全沒有做任何再工程。
4. **分數相近不代表行為相近**:有些 agent 又快又便宜,有些燒掉大量預算,最後兩者都答錯。理解這些差異很重要。
5. **開放權重模型不夠可靠**:平均落後閉源模型(圖上為 Kimi 與 DeepSeek);在某些它們大概沒訓練過的任務上直接崩潰——她舉的例子是 **AppWorld**,五個 agent harness 平均下來都做不好。
6. **開放權重模型對 harness 極度敏感**:Kimi 配最佳 harness 與配最差 harness 相差 **18%**。含意很實際:**閉源模型換 harness 相對安全,開放權重模型換 harness 就必須重新評估**。另一個方向的例子:OpenAI 的 agent harness 搭 Claude 與 Gemini 會拉高成績,但搭開放權重模型直接歸零——**不是任何模型都能配任何 harness**。
7. **開放權重模型不見得便宜**:她特別回應了當天其他場次「開放權重比較便宜」的說法——看成本-品質圖,它們是**有競爭力**,但不是便宜。

#### Traces 與下一步(約 00:26–00:27)

跑 Exgentic 時所有 traces 都以 OpenTelemetry 格式收集,已開源上架 Hugging Face,超過 10K 條完整 trace 可供研究。

下一步:**Exgentic V2**——從 V1 學到教訓後改走另一條路,以 **Kubernetes 與 Docker 的原語**為基礎;此外還在做 **agentic inference platform 的評估**,以及 **AI-native system evaluation** 這個新題目。

### 金句

> "Generality ultimately wins over domain-specific approaches."(約 00:13)

她把 bitter lesson 從模型層推到 agent 層,這是整場的論證起點。

> "We are not changing anything in the benchmark, so they work as they intended. And similarly, we are not touching the agents."(約 00:20)

Unified Protocol 的設計哲學:標準化不是要求所有人改用同一個介面,而是在中間做轉換。

> "You cannot just change the harness and assume that you will get the same quality for the open weights model."(約 00:25)

18% 的 harness 差距,對任何打算「換個 harness 省錢」的團隊都是警訊。

## English Notes

### TL;DR

- **The thesis**: extend Sutton's bitter lesson from models to agents. NLP moved from summarization/extraction models to general LLMs; agents will move from today's domain-specific agents (finance, customer care) to **general agents**, where domain knowledge lives in the environment rather than inside the agent.
- **The real bottleneck is standardization, not metrics**: every benchmark expects a different agent, every agent expects different information from the environment, and every researcher writes bespoke glue for each agent × benchmark pair. That does not scale.
- **The fix is a Unified Protocol mediation layer**: agents keep their own protocol, benchmarks keep theirs, and the framework translates between them using three shared primitives — task, context, actions. Neither side is modified. The framework is **Exgentic**; it produces the **Open (General) Agent Leaderboard**.
- **Headline findings**: the model dominates quality more than the harness; unmodified general agents are competitive with the best domain-specific agent on each task; agents with near-identical scores can differ enormously in cost.
- **Two warnings about open-weight models**: they trail closed models on average and collapse on tasks they likely weren't trained for (e.g. AppWorld), and — more consequentially — they are **highly harness-sensitive**: Kimi's best harness beats its worst by 18%. "Open weights are cheap" also doesn't survive the cost-quality plot.

### Key Points

#### From the bitter lesson to general agents (~00:13–00:16)

The talk draws on three papers (ICLR, ICML, and hopefully NeurIPS). Starting from Richard Sutton's bitter lesson — generality ultimately beats domain-specific engineering — she traces the same arc through language models: everyone began with task-specific models for summarization and extraction, and everything converged on big general models.

Agents today sit at the domain-specific stage. Her definitions matter for the rest of the talk: in a **domain agent**, the domain knowledge is encoded inside the agent, and only once it's encoded can the agent work with the environment. In a **general agent**, no domain-specific knowledge lives in the agent; it all sits on the environment side, and what you evaluate is the agent's ability to explore and adapt to new tasks. The payoff is an agent that works across environments without per-environment re-engineering — so evaluation shifts from performance on a single task to performance across many environments and tasks.

The upside: one general agent covers many use cases instead of a hundred domain-specific ones; improvements to memory or search are centralized and benefit every use case; you can still customize, but from a better and more robust starting point.

She also presents the opposing view fairly, pointing at the ICML position paper for both sides in detail: domain-specific agents give more control, more efficiency, and more predictability; more autonomy for a general agent introduces unforeseen risk; and some argue that it's the **model** that should be general, not the agent.

#### The bottleneck: three unstandardized interfaces (~00:17–00:20)

Claiming an agent is general requires showing it works across environments and tasks — which requires evaluation, and that turns out to be far from trivial. The obstacles are standardization at three interfaces: the **agent interface** (each benchmark expects the agent to behave differently), the **environment interface** (each agent expects different information), and the **researcher interface** (everyone implements their own code per agent–benchmark combination).

She notes the contrast with the preceding LLMArena talk: here the benchmarks are open-sourced by students and community efforts. Surveying existing frameworks, **not one** supports multi-protocol benchmarks, multi-protocol agents, agent plug-and-play, and generality across genuinely different tasks all at once.

#### Unified Protocol and Exgentic (~00:20–00:21)

**Exgentic** introduces a **mediation layer** they call the **Unified Protocol**. The agent keeps the protocol it ships with; the benchmark keeps the protocol it was developed with; the framework transforms between them. Nothing in the benchmark changes, so benchmarks behave as intended, and nothing in the agent is touched. The translation rests on three primitives shared across benchmarks and agents: **task, context, and actions**.

This makes a full Cartesian product possible — any agent harness × any model × any benchmark — published as the **Open (General) Agent Leaderboard**: agent column, model column, per-task columns, average success, plus **cost**, with a Pareto frontier so you can pick the configuration that matches your accuracy/price tolerance.

#### What the leaderboard showed (~00:21–00:26)

1. **General agents adapt with no modification**: on average, most of them handle every task type thrown at them.
2. **The model matters most**: quality is driven mainly by the model, though the agent harness has a visible effect.
3. **General vs. domain-specific**: taking the top domain-specific agent per task from that task's leaderboard and comparing against the top general agent, the general agents are quite competitive — with no re-engineering at all.
4. **Similar scores, very different behavior**: some agents fail fast and cheap, others fail after burning a lot of money. Both are wrong answers, but the cost profile matters.
5. **Open-weight models are not generally reliable**: behind closed models on average (Kimi and DeepSeek in the plot), and on tasks they likely weren't trained for they sink outright — her example was **AppWorld**, where they underperformed averaged across all five agent harnesses.
6. **Open-weight models are far more harness-sensitive**: Kimi with its best harness beats Kimi with its worst harness by **18%**. The practical implication is that swapping harnesses is relatively safe for closed models but requires re-evaluation for open-weight ones. The reverse case also appeared: OpenAI's agent harness lifted results with Claude and Gemini but crashed to zero with open-weight models — you can't pair any model with any harness.
7. **Open-weight models are not necessarily cheap**: responding to a claim from another session that day, she pointed at the cost-quality plot — they are *competitive*, not cheap.

#### Traces and what's next (~00:26–00:27)

Every Exgentic run collects traces in OpenTelemetry format. They're open source on Hugging Face — more than 10K full traces available for study.

Next: **Exgentic V2**, a somewhat different approach informed by V1, built on **Kubernetes and Docker primitives**. Alongside it, they're working on evaluating **agentic inference platforms** and on **AI-native system evaluation**.

### Quotes

> "Generality ultimately wins over domain-specific approaches." (~00:13)

The bitter lesson, lifted from the model layer to the agent layer — the premise the whole talk rests on.

> "We are not changing anything in the benchmark, so they work as they intended. And similarly, we are not touching the agents." (~00:20)

The design philosophy of the Unified Protocol: standardize by translating in the middle, not by making everyone adopt one interface.

> "You cannot just change the harness and assume that you will get the same quality for the open weights model." (~00:25)

The 18% best-vs-worst harness gap is a warning for anyone planning to swap harnesses to cut costs.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Exgentic | IBM Research 的 general agent 評估框架,核心為 Unified Protocol 中介層 | IBM Research's general-agent evaluation framework built around the Unified Protocol mediation layer | www.exgentic.ai;V2 將以 Kubernetes/Docker 原語重建 / V2 to be rebuilt on Kubernetes & Docker primitives |
| Unified Protocol | agent 與 benchmark 之間的轉換層,基於 task / context / actions 三原語 | Translation layer between agent and benchmark protocols; primitives are task, context, actions | 雙方皆不需修改 / neither side is modified |
| Open (General) Agent Leaderboard | agent harness × 模型 × benchmark 的笛卡兒積榜,含成功率與成本 | Cartesian-product leaderboard over harness × model × benchmark, with success rate and cost | 附 Pareto frontier / includes a Pareto frontier |
| General Agent Evaluation(論文) | 支撐本場的論文之一 | The paper underpinning the talk | arXiv 2602.22953;另發表於 ICLR 2026 Workshop on Agents in the Wild / also at the ICLR 2026 Agents in the Wild workshop |
| ICML position paper | 正反雙方論述 general vs domain-specific agent | Position paper laying out both sides of the general-vs-domain-specific debate | 講者建議直接閱讀原文 / she recommends reading it directly |
| AppWorld | 互動式 coding agent benchmark,開放權重模型在此表現崩潰 | Interactive coding-agent benchmark where open-weight models collapsed | Stony Brook NLP,ACL 2024 best resource paper |
| Agent traces on Hugging Face | Exgentic 執行產生的完整 trace,OpenTelemetry 格式 | Full Exgentic run traces in OpenTelemetry format | 10K+ 條,開源 / 10K+ traces, open source |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Mikael / Michal | Michal Shmueli-Scheuer |
| Genetik / Exagentic | Exgentic |
| upward application | AppWorld |
| Kimmy | Kimi |
| Dipsy | DeepSeek |
| auto format(traces 格式) | OTel / OpenTelemetry format |
| the L Arena | LLMArena(前一場講者)/ the previous speaker's LLMArena |
| Richard Sutton's bitter lesson | 正確,無需更正 / correct as heard |

## 待確認 / To Verify

- 三篇論文(ICLR / ICML / NeurIPS 投稿中)各自的完整標題;搜尋僅確認其一為 "General Agent Evaluation"(arXiv 2602.22953)。/ Full titles of all three papers; only "General Agent Evaluation" (arXiv 2602.22953) was confirmed.
- Kimi 最佳 vs 最差 harness 的 18% 差距——是絕對百分點還是相對差,字幕未區分。/ Whether the 18% best-vs-worst harness gap is absolute percentage points or a relative difference.
- 榜上納入的五個 agent harness 具體是哪五個(字幕僅提到「五個 harness」與 OpenAI 的 agent harness)。/ The identity of the five agent harnesses (only "five harnesses" and "the OpenAI agent" were named aloud).
- 「開放權重模型在某任務歸零」的那組實驗細節(哪個 harness × 哪些模型)。/ Details of the configuration where open-weight models scored zero.
- Exgentic 名稱的正式大小寫寫法(官網為 exgentic.ai)。/ Official capitalization of "Exgentic".
