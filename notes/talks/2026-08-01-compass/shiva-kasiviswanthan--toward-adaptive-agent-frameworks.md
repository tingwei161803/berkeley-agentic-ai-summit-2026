---
title: "Toward Adaptive Agent Frameworks"
title_zh: "邁向自適應的 Agent 框架"
speaker: "Shiva Kasiviswanthan"
affiliation: "Principal Applied Scientist, Amazon Web Services"
type: talk
stage: Compass
date: 2026-08-01
session: "Session 2: Frameworks & Dev Platforms"
video: "https://www.youtube.com/watch?v=AO0RXP-fVZQ&t=1434s"
video_range: "00:23:54–00:29:58"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [adaptive-agents, budget-aware, parallel-reasoning, continual-learning, aws]
---

# 邁向自適應的 Agent 框架(Toward Adaptive Agent Frameworks)

**一句話總結**:今天的 agent 已經很會 plan 與用工具,但它們的**執行策略是寫死的**;要進到 mission-critical 場景,agent 得學會在預算約束下決定下一步(constrained MDP)、學會平行探索多條推理路徑,並能持續適應新任務而不遺忘舊的。
**One-line summary**: Today's agents plan and use tools well, but their **execution policy is hard-coded**. For mission-critical deployment, agents need to learn what to do next under an explicit budget (a constrained MDP), learn to explore several reasoning paths in parallel, and keep adapting to new tasks without forgetting old ones.

## 中文筆記

### TL;DR

- **三個研究問題**:(1) agent 該如何在固定運算預算下分配資源?(2) 如何讓 agent 推理得更好?(3) 如何讓 agent 隨時間演化?他的團隊在 AWS 做大規模雲端維運的 monitoring / observability agent,這三題是他們認為要走進 mission-critical 場景必須先解的。
- **Budget-aware adaptive execution**:今天多數 agent 的執行策略靠 prompt 或啟發式寫死;他們把它形式化成 **constrained Markov decision process**——在預算(latency / cost / token 皆可)約束下最大化期望效用,並**學出**執行策略。實測比常用的 scalar reward model 更好,而且**更 sample-efficient**(達到同樣能力所需的迭代次數顯著更少)。
- **Parallel reasoning**:讓模型平行探索多條推理路徑,且這些路徑是**在訓練期學到的、不是推論期才展開**,最後由一個 coordinated reasoning 步驟收斂成單一答案。在數學與程式 benchmark 上,pass@1 到 pass@k 都優於強 baseline,**k=1 時效果特別突出**。
- **Continual adaptation**:第三個方向是有原則的 post-training 方案,讓 agent 適應新任務時**不遺忘先前學會的東西**。

### 重點整理

#### 出發點:agent 已經很強,但還不夠可靠(約 00:24–00:25)

Kasiviswanthan 開場說明他與團隊在 AWS 做的是大規模雲端維運的 monitoring 與 observability agent。今天的 agent 在 planning、tool execution、資訊檢索、迭代求解上都已經相當能幹;但當它們被部署到**更 mission-critical 的應用**時,AWS 認為有幾個關鍵研究問題必須先解決:

1. Agent 該**如何分配運算資源**?想像你有固定的運算預算,要讓 agent 把它用在刀口上。
2. 如何讓 agent **推理得更好**——有效率地探索多條路徑再下決策。
3. 如何讓 agent **隨時間演化**?Agent 不該是靜態的,而要持續適應、愈做愈好。

本場聚焦前兩題,第三題結尾簡述。

#### 方向一:budget-aware adaptive execution(約 00:25–00:27)

今天絕大多數 agent 的**執行策略是固定的**——由 prompt 或某個局部啟發式定義。他們的目標是讓 agent **把執行策略學起來**。

抽象化之後:agent 有一段 context,要決定下一個最佳動作(重新檢索資訊、用工具、驗證結果、更新記憶……),而關鍵約束是**預算**——agent 必須在執行工具的同時尊重這個預算。這在形式上可以寫成一個 **constrained Markov decision process**:在某個運算預算的約束下最大化期望效用。預算可以是 latency、成本、token,任何你想用的定義。

有效嗎?有。他展示兩張圖:一張顯示這些自適應 agent 學到的執行策略**優於實務上常用的 scalar reward model**;另一張顯示它同時**更 sample-efficient**——要達到同樣的能力水準,所需樣本數顯著更少。

#### 方向二:parallel reasoning(約 00:27–00:28)

今天的模型基本上沿著**單一推理路徑**走。他們探索的方向是讓模型**平行探索多條推理路徑**——關鍵在於這些平行路徑是**在訓練期學到的,而不是推論時才展開**;最後由一個 coordinated reasoning 步驟把多條路徑收斂成一個答案。

在數學推理與程式 benchmark 上都拿到穩定的好結果:從 pass@1 到 pass@k 都勝過很強的 baseline,**k=1(只取一個答案)時的結果尤其亮眼**。

#### 方向三與收尾:continual adaptation(約 00:29)

第三個方向是 **continual model / agent adaptation**:找出有原則的 post-training 方案,讓 agent 能適應新任務。主要挑戰是**學新任務時不能忘掉舊的**。他認為解開這三個方向,就能催生下一代的 frontier agent。

## English Notes

### TL;DR

- **Three research questions** his team at AWS is working on, motivated by monitoring and observability agents for large-scale cloud operations: how should an agent allocate compute; how do we make agents reason better; and how do agents evolve over time.
- **Budget-aware adaptive execution**: most agents today have a fixed execution policy defined by a prompt or a local heuristic. They formalize it as a **constrained Markov decision process** — maximize expected utility subject to a computational budget (latency, cost, tokens, whatever you like) — and *learn* the policy. It beats the scalar reward model commonly used in practice and is markedly **more sample-efficient**.
- **Parallel reasoning**: let the model explore multiple reasoning paths in parallel, with those paths **learned during training rather than unrolled at inference time**, then coordinated into a single answer. Consistent gains on math and coding benchmarks from pass@1 through pass@k, with **k=1 the standout**.
- **Continual adaptation**: principled post-training schemes that adapt to new tasks **without forgetting** what was learned before.

### Key Points

#### Starting point: capable agents aren't yet dependable ones (~00:24–00:25)

Kasiviswanthan works on AI agents for monitoring and observability in large-scale cloud operations at AWS. Today's agents are already good at planning, tool execution, retrieving information, and iterating toward a solution. But as they get deployed into **mission-critical applications**, AWS sees critical research questions that need answers first:

1. How should an agent **allocate computational resources** given a fixed budget?
2. How do we make agents **reason better** — efficiently exploring multiple paths before deciding?
3. How do agents **evolve over time**, rather than staying static?

The talk covers the first two and closes on the third.

#### Direction 1: budget-aware adaptive execution (~00:25–00:27)

Most agents run a **fixed execution policy** you define with a prompt or a heuristic. The goal is to have agents **learn** that policy instead.

Abstractly: the agent holds some context and must pick the best next action — re-retrieve information, use a tool, verify results, update memory — and the binding constraint is a **budget** it must respect while executing tools. That formulation is a **constrained Markov decision process**: maximize expected utility subject to a computational budget, where the budget can be latency, cost, tokens, or any other notion.

Does it work? Two plots say yes. One shows adaptive agents learning a better execution policy than the scalar reward model commonly used in practice; the other shows the approach is **more sample-efficient** — reaching the same level of competence takes significantly fewer iterations.

#### Direction 2: parallel reasoning (~00:27–00:28)

Models today follow a **single reasoning path**. Their work lets models explore **multiple reasoning paths in parallel**, and the important detail is that those parallel paths are **learned during training, not spun up at inference time**. A coordinated reasoning step at the end collapses the multiple paths into one answer.

Tested on mathematical reasoning and coding benchmarks, the results consistently beat strong baselines from pass@1 through pass@k — and are **especially impressive at k=1**, the single-shot case.

#### Direction 3 and wrap-up: continual adaptation (~00:29)

The third thread is **continual model or agent adaptation**: principled post-training schemes that adapt to new tasks, where the main challenge is not forgetting what was previously learned. Solving all three, he argues, is what gets us to the next generation of frontier agents.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Constrained MDP 形式化 / Constrained MDP formulation | 把 agent 執行策略學習寫成「在運算預算約束下最大化期望效用」 | Framing execution-policy learning as maximizing expected utility subject to a compute budget | 演講未點名論文 / no paper named on stage |
| Parallel reasoning(訓練期學習的多路徑推理) | 多條推理路徑於訓練期學得,推論時由 coordinated reasoning 收斂為單一答案 | Multiple reasoning paths learned at training time, coordinated into one answer | 演講未點名論文 / no paper named on stage |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Shivakashnatan | Shiva Kasiviswanthan(依官網議程 / per the official agenda) |
| constraint marker decision process | constrained Markov decision process |
| scale riser word model | scalar reward model |
| competition budget / competitional budget | computational budget |
| precinct paths | reasoning paths |
| par reasoning | parallel reasoning |
| postraining | post-training |
| principal postraining schemes | principled post-training schemes |

## 待確認 / To Verify

- 官網議程的姓名拼法為 "Shiva Kasiviswanthan";AWS 公開資料中此研究者通常拼作 **Shiva Prasad Kasiviswanathan**,建議日後核對正名。frontmatter 目前依議程。/ The agenda spells the name "Shiva Kasiviswanthan"; AWS publications generally use **Shiva Prasad Kasiviswanathan**. The frontmatter follows the agenda pending confirmation.
- 兩個方向都只展示了結果圖,未點名對應論文或開源專案。/ Both directions were shown as result plots only, with no paper or repo named.
- 對照基線他說的是 "scalar reward model"(字幕作 "scale riser word model"),此處為推定;實際基線名稱待確認。/ The baseline was transcribed as "scale riser word model", read here as "scalar reward model" — worth confirming against the slides.
