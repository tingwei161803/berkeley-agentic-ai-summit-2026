---
title: "Reasoning as Control: Adaptive Test-Time Compute for Planning Agents"
title_zh: "把推理當成控制:給規劃型 agent 的自適應 test-time compute"
speaker: "Furong Huang"
affiliation: "Associate Professor, University of Maryland"
type: talk
stage: Compass
date: 2026-08-01
session: "Session 3: Foundational Capabilities"
video: "https://www.youtube.com/watch?v=AO0RXP-fVZQ&t=9235s"
video_range: "02:33:55–02:45:45"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [test-time-compute, self-improvement, decoding-control, self-reflection, workflow-optimization]
---

# 把推理當成控制:給規劃型 agent 的自適應 test-time compute(Reasoning as Control: Adaptive Test-Time Compute for Planning Agents)

**一句話總結**:自我改進不該只被當成「模型能力」;基礎模型正在變成 **runtime 的決策者**,而 agentic 系統的自我改進可以發生在三個層級——thinking(token 級解碼控制)、action(真正的自我反思而非模仿更強模型)、workflow(從 workflow bank 中即時挑選拓撲)——這三層都能在不重訓模型的前提下改進。
**One-line summary**: Self-improvement is usually framed as a model capability, but the model is only one layer; foundation models are increasingly **runtime decision makers**, and a self-improving agentic system can be improved at three levels — thinking (token-level decoding control), action (genuine self-reflection rather than imitating a stronger model), and workflow (retrieving a topology from a pre-computed bank at test time) — all without retraining the model.

## 中文筆記

### TL;DR

- **重新框定自我改進**:大家談 self-improvement 時多半框成模型能力(模型改進自己的推理、從自己的輸出學習、獲得新技能)。但**模型只是其中一層**——最終被部署的是一整個 agentic 系統,模型周圍那一大圈基礎設施同樣是很有意思的改進層,對垂直應用尤其關鍵。
- **runtime 決策有階層**:從最底層的 thinking choices / token control,到每一步的 action control,再到最高層的 workflow control。這三層都可以最佳化,而且都可以**在不訓練模型的前提下**做。
- **三個層級的具體做法**:(1) **Thinking**——用 reward 訊號在解碼時把模型「向早期就導正」,從 Transfer Q* 到 token-level reward model,把成本降低數個數量級,可做 weak-to-strong 引導與即時多目標對齊;(2) **Action**——「genuine self-reflection」:不模仿更強模型的反思,而是強迫模型自己判斷此刻哪個動作更好、並說明為什麼,實質上是在建 world model;(3) **Workflow**——不做「one-for-all」也不做「one-for-each」,而是預先建一個 **workflow bank**,test time 再即時挑選。

### 重點整理

#### 重新框定:自我改進不只是模型的事(約 02:34–02:36)

她開場就把講題往「**self-improving agentic systems**」拉。一般談 self-improvement,框的是模型能力:模型能改進自己的推理、開始從自己的輸出學習、進而習得新技能。但她認為**模型只是一層**——最終要被部署的是一個 agentic 系統,模型外圍還有大量基礎設施:模型怎麼被建造、怎麼被部署。那也是一個很值得理解的改進層,而且**對垂直應用可能更重要**——當你在自己的環境、自己的企業、自己的應用領域裡使用語言模型時。

接著她拆解 agentic 系統拿到一個任務後實際發生的事:從環境觀察到狀態轉移 → 觀察經過思考流程 → 最後做出決策(每個時刻決定當下最該做什麼)。因為任務通常很複雜,你會把它**分解給多個 agent**、**指派角色**、**設計 workflow**(她說現在大家叫這個「loop engineering」);而 workflow 裡的每個 agent,每個時間步都要決定動作,而每個動作決策前都得走一遍思考流程、產出一段 reasoning trace。

於是 runtime 就出現了一個**決策階層**:

1. 最底層:**thinking choices 與 token control**
2. 中層:**action control**(每個決策時間步)
3. 最上層:**workflow control**

她的主張:**基礎模型正越來越成為 runtime 的決策者**。自我改進的 agentic 系統,不只可以改進模型能力,也可以改進基礎設施——改進模型在 runtime 怎麼被部署,跨 thinking、跨 action、跨 workflow。

#### 層級一:Thinking — 解碼時的 steering(約 02:36–02:40)

起點是 **steering 問題**:有一個 reward model,希望把 LLM 導向特定 reward。熟悉數學的人知道這有**封閉解**,而這個封閉解對「對齊」這個複雜問題給了一個很短的答案:**拿 base model 的輸出,加上一個額外的 steering 訊號**,而這個 steering 訊號無非就是「某個最佳策略下的 trajectory reward」的某種形式。

從自迴歸的 next-token 取樣角度看,實務上就是:看著語言模型的輸出,用一個**可以從企業自有資料學來的外部訊號**去引導它。

但這裡有個**落差**:你真正想要的是**盡可能早**在生成過程中就 steer,而你手上的 reward model 是 **trajectory-level** 的——它評的是完整回應,支撐不了 next-token 級的引導。

- **Transfer Q***:先接受這個限制,做 auto-completion 再正確地使用 reward model。做法是對的,但**太慢**——在她的學術環境裡用 A6000 GPU,生成 500 個 token 要 **14 小時**,基本上不可行。
- **近期工作(token-level reward model)**:設計一個特定的 reward 模型族、做出 **token 級的 reward**,把成本**降低數個數量級**。結果她形容為 phenomenal:可以做任意的 runtime steering、**完全不需要訓練模型**;可以做 **weak-to-strong guidance**(用很小的模型引導很大的模型);還可以做**多目標對齊**——不同目標之間即時依使用者需求調整。

#### 層級二:Action — genuine self-reflection(約 02:40–02:42)

思考終究是為了服務行動,那麼怎麼做決策?

Agentic 系統常用 **imitation learning**(從專家示範蒸餾),但這常掉進 **stuck loop** 問題:agent 反覆嘗試同樣的動作直到終止或耗盡 token 預算。

於是有人轉向 world model 訓練,具體做法之一是**模仿 self-reflection**。她點出這件事的矛盾:**當你在「模仿」自我反思時,你並不是在用自己反思——你是在模仿一個更強的模型教你怎麼反思**。這確實比 imitation learning 好,但結果並不令人滿意。

她們做了一件很簡單的事,稱為 **genuine self-reflection**:不模仿更強的模型怎麼想、怎麼反思,而是**強迫模型自己去反思——在這個時間點,哪個動作更好**。你可以把這理解成在建一個 **world model**:模型在建立「什麼狀態下哪個動作更好」的心智模型,而且**同時被強迫理解為什麼**。

結果她說「worked really phenomenally」:能同時改進 imitation learning 與 reinforcement learning,**out-of-distribution 表現顯著提升**,也大幅超越先前的 SOTA。她認為最酷的一點是:**它會外溢到一般推理能力**——僅僅透過理解「agent 在特定環境裡怎樣運作得更好」,這種看似與一般推理無關的 critical learning,卻神奇地提升了一般推理能力。

#### 層級三:Workflow — 一個可即時檢索的 workflow bank(約 02:42–02:45)

最上層是**自主決定 agent 角色、最佳化 agent 拓撲**,也就是 workflow 最佳化。她舉了一個 agentic safety 應用的固定 workflow 為例:它運作得很好,但問題是——**能不能設計一個框架,讓一個 meta designer 在 query 進來時,為這個特定任務生出最好的 agentic 框架、最好的 harness?而且是自主地做?**

既有的兩條路線:

- **One-for-all**:為特定任務找出世界上最好的那一個 workflow。
- **One-for-each**:為進來的**每一個 query** 各自設計最好的 flow,追求適應性。

她們的取徑是「基礎模型式的哲學」:**兩者都不做**。而是**在訓練時預先計算一批 workflow、建成一個 workflow bank**,部署時**即時適配**到具體 workflow,藉此取得效率。結果顯示效能有顯著提升。

(她在此坦言現場投影片渲染出了問題,說會分享渲染正確的版本。)

#### 總結(約 02:45)

自我改進的 agentic 系統有**三個 runtime 決策層級**,而重點都是:在**有限預算**下聰明地分配運算資源——

1. 如何**盡可能早**地導正思考流程,免得走完一段又長又錯的思考;
2. 如何做 **action control**;
3. 如何做 **workflow control**。

### 金句

> "Foundation models are actually more and more becoming a runtime decision maker."(約 02:36)

整場演講的軸心:模型不只是被訓練出來的能力,更是部署時每一層決策的執行者。

> "This is not actually self-reflection — when you are trying to self-reflect, you're not actually using yourself to reflect, you are actually mimicking some stronger model which teaches you how to reflect."(約 02:41)

對「模仿式自我反思」的一句到位的拆穿,也是 genuine self-reflection 的動機。

> "You're doing it right, but you're doing it way too slow."(約 02:39)

對 Transfer Q* 的自我評價——500 個 token 要跑 14 小時,方法正確但工程上不可用。

## English Notes

### TL;DR

- **Reframing self-improvement.** It's usually framed as a *model* capability — the model improves its reasoning, learns from its own output, acquires new skills. But the model is one layer. What actually gets deployed is an agentic system, and the infrastructure around the model is an equally interesting layer to keep improving — possibly *more* important for vertical applications.
- **Runtime decisions form a hierarchy**: low-level thinking choices and token control, then per-step action control, then high-level workflow control. All three can be optimized, and all three without retraining the model.
- **Three concrete lines of work**: (1) **Thinking** — steer decoding with a reward signal as early as possible; from Transfer Q* to a token-level reward model that cuts cost by orders of magnitude, enabling weak-to-strong guidance and real-time multi-objective alignment; (2) **Action** — "genuine self-reflection," forcing the model to judge which action is better *and why* rather than mimicking a stronger model's reflection, which is effectively building a world model; (3) **Workflow** — neither one-for-all nor one-for-each, but a pre-computed **workflow bank** adapted at test time.

### Key Points

#### The reframe (~02:34–02:36)

She opens by redirecting the topic toward **self-improving agentic systems**. When people talk about self-improvement they frame it as a model capability. But the model is just one layer; at the end of the day an agentic system gets deployed, and there's a lot of infrastructure around the model — how it's built, how it's served — that's a very interesting layer in its own right, and possibly more important for vertical applications where you're using a language model inside your own environment and domain.

She then walks through what happens in an agentic system given a task: observe a state transition from the environment → run it through a thinking process → make a decision about the best action right now. Because these tasks are complicated, you decompose them across agents, assign roles, and design a workflow — what she notes people now call **loop engineering**. Each agent in the workflow decides an action per timestep, and each action decision requires generating a reasoning trace.

That produces a **hierarchy of runtime decision making**: low-level thinking choices and token control → action control at each timestep → high-level workflow control. Her framing: **foundation models are increasingly runtime decision makers**, so a self-improving agentic system can improve the model's capability *and* how the model is deployed at runtime across thinking, actions, and workflows.

#### Level 1: Thinking — steering at decode time (~02:36–02:40)

Start from the **steering problem**: you have a reward model and want to steer an LLM to align with that specific reward. The math gives a closed-form solution, and it's a remarkably short answer to a complicated alignment question: take whatever the base model gives you and **add a steering signal**, where that signal relates to a trajectory reward under some optimal policy.

From an autoregressive next-token sampling perspective this reduces to: look at the language model's output and steer it with an external signal you can learn from your own corporate data.

The discrepancy: you want to steer **as early as possible** in generation, but reward models are **trajectory-level** — designed to score complete responses, not partial ones.

- **Transfer Q\*** takes the honest route: do the auto-completion and use the reward model correctly. Right idea, far too slow — on an academic A6000, generating 500 tokens takes **14 hours**. Basically impossible.
- A more recent work designs a specific reward model family giving a **token-level reward**, cutting cost by **orders of magnitude**. That unlocks arbitrary runtime steering with **no model training at all**, **weak-to-strong guidance** (a very small model guiding a very large one), and **multi-objective alignment** where objectives adapt in real time to user need.

#### Level 2: Action — genuine self-reflection (~02:40–02:42)

Thinking exists to serve action, so how is the decision made?

Agentic systems are commonly learned via **imitation learning**, distilling from expert demonstrations — which frequently hits the **stuck loop** failure: the agent retries the same actions until termination or budget exhaustion.

The natural next move is world-model training, and one popular version is imitating self-reflection. Her objection is sharp: **that isn't self-reflection at all** — you're not using yourself to reflect, you're mimicking a stronger model that teaches you how to reflect. It works better than imitation learning, but the results aren't satisfying.

So they did something simple, **genuine self-reflection**: rather than imitating how stronger models think and reflect, force the model itself to do the reflection — *which action is better at this point* — **and to understand why**. That's effectively a world model: a mental model of which action is better under which state.

It "worked really phenomenally": improvements over both imitation learning and reinforcement learning, significant gains **out of distribution**, and performance well beyond prior state of the art. The part she finds most interesting is that it **generalizes to general reasoning** — this kind of critical learning bears no obvious relation to general reasoning capability, yet it magically improves it.

#### Level 3: Workflow — a bank you retrieve from (~02:42–02:45)

The top layer: autonomously deciding agent roles and optimizing agent topology. Her example is a fixed workflow for an agentic-safety application that works well — but can you design a framework where a **meta designer** produces the best agentic framework and harness for each incoming query, autonomously?

Two existing routes: **one-for-all** (find the single best workflow in the world for the task) and **one-for-each** (design the best flow per query, maximizing adaptability).

Their answer takes a foundation-model philosophy: neither. **Pre-compute a bank of workflows** at training time, then **adapt to the specific workflow at test time**, efficiently. The results show significant performance improvement. (She flagged live that the slide wasn't rendering correctly and offered to share a corrected version.)

#### Wrap-up (~02:45)

Three levels of runtime decision making in a self-improving agentic system, all about allocating compute intelligently under a limited budget: steer the thinking process as early as possible so you don't run a long process in the wrong direction; control the action; and control the workflow.

### Quotes

> "Foundation models are actually more and more becoming a runtime decision maker." (~02:36)

The talk's axis: the model isn't just a trained capability, it's the thing making decisions at every deployment layer.

> "This is not actually self-reflection — when you are trying to self-reflect, you're not actually using yourself to reflect, you are actually mimicking some stronger model which teaches you how to reflect." (~02:41)

The puncture that motivates genuine self-reflection.

> "You're doing it right, but you're doing it way too slow." (~02:39)

Her verdict on Transfer Q*: 14 hours for 500 tokens is methodologically correct and practically unusable.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Transfer Q* | 用 baseline 模型估計最佳 token 級 value function 的原理式解碼對齊法;正確但極慢 | Principled decoding for LLM alignment using baseline models to estimate the optimal token-level value function; correct but very slow | arXiv 2405.20495 |
| Token-level reward model(近期工作) | 設計 reward 模型族做 token 級 reward,成本降數個數量級,支援 weak-to-strong 與多目標對齊 | Reward model family giving token-level rewards; orders-of-magnitude cheaper; weak-to-strong guidance and multi-objective alignment | 疑為 GenARM(arXiv 2410.08193),講者未報名稱,待確認 / likely GenARM — not named in the talk |
| Genuine self-reflection | 強迫模型自行判斷哪個動作更好與為什麼,而非模仿更強模型的反思 | Forces the model to judge which action is better and why, instead of mimicking a stronger model's reflection | 論文名稱待確認 / paper title to verify |
| Workflow bank | 訓練時預算一批 workflow,test time 即時挑選;介於 one-for-all 與 one-for-each 之間 | Pre-computed bank of workflows adapted at test time; between one-for-all and one-for-each | 論文名稱待確認 / paper title to verify |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Fuang Hong | Furong Huang |
| ajinky / agendic / a gentic | agentic |
| transfer Q star | Transfer Q* |
| auto reggressive | autoregressive |
| a loop engineering("a" 為贅字) | loop engineering |
| premputee | pre-compute |

## 待確認 / To Verify

- **token-level reward model** 那篇「very recent work」的論文名稱(語境高度符合 GenARM,但講者未在逐字稿中報出名稱)。/ Title of the "very recent work" on token-level rewards — context matches GenARM but the name isn't spoken.
- **genuine self-reflection** 的論文名稱與 benchmark(講者只描述方法與結果)。/ Paper title and benchmarks for genuine self-reflection.
- **workflow bank** 工作的論文名稱;講者提到的 "one for all" / "one for each" 是否為特定論文的名稱亦待確認。/ Paper title for the workflow bank work; whether "one for all" and "one for each" refer to named papers.
- 講者展示 workflow 範例時提到的 agentic safety 應用具體為何(投影片渲染失敗,現場未細講)。/ The agentic-safety application used as the fixed-workflow example — the slide failed to render.
