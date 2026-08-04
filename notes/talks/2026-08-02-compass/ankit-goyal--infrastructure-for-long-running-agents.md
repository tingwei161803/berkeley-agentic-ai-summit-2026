---
title: "Infrastructure for Long-Running Agents"
title_zh: "長時間執行 Agent 的基礎設施"
speaker: "Ankit Goyal"
affiliation: "Principal Staff Software Engineer, LinkedIn"
type: talk
stage: Compass
date: 2026-08-02
session: "Session 3: Enterprise AI"
video: "https://www.youtube.com/watch?v=1UrriPJRSPU&t=4117s"
video_range: "01:08:37–01:14:30"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [enterprise, ml-infrastructure, sandboxing, gpu, agent-platform]
---

# 長時間執行 Agent 的基礎設施(Infrastructure for Long-Running Agents)

**一句話總結**:LinkedIn 把 agent 當成「跟其他任務一樣的一種任務」放進 ML 平台,但因為 agent 產生的程式碼不可信、且會在幾分鐘內丟出上百個 job,平台在 UX、compute、trust 三個面向都被迫重新設計——結果是六個月內實驗量成長 100%。
**One-line summary**: LinkedIn treats an agent as just another job on its ML platform, but because agent-written code is untrusted and agents launch hundreds of jobs in minutes, the infrastructure had to be rethought along three axes — UX, compute, and trust — and experiment volume doubled in six months.

## 中文筆記

### TL;DR

- **三個已在生產環境創造價值的 agent**:把 400+ 個 TensorFlow 模型遷移到 PyTorch 的 model generation agent、掃描叢集低使用率作業並自動最佳化的 performance optimization agent,以及工程師只要定義目標就會自主做架構搜尋與超參數調校的 autonomous research agent。
- **Agent 進來之後,基礎設施的三個位移**:UX(重點從「好用的抽象」轉向「設計 agentic workflow 與護欄」,因為程式碼已由 LLM 產生)、compute(從少量長跑 job 變成短時間內上百個 job,幾分鐘的排程延遲不再能被攤平)、trust(人寫的程式碼預設可信,agent 寫的不行)。
- **對抗長程漂移的做法是 harness-as-code**:每個階段用程式碼定義各自的職責,**scorer 與 evaluator 也一律寫成程式碼**,避免 agent reward hacking 或偏離路徑;再加上 checkpoint / restore 讓 agent 自行從失敗中復原。

### 重點整理

#### 生產中的三個 agent 與它們共用的生命週期(約 01:09–01:10)

LinkedIn AI Platforms 團隊目前有三類已產出實質商業價值的 agent:

1. **Model generation agent**:LinkedIn 生產環境跑著 400+ 個以 TensorFlow 撰寫的模型,團隊要把它們遷移到 PyTorch。難的地方不是翻譯程式碼,而是**確保新模型的表現不低於既有模型**——那些線上模型往往是工程師花數月甚至數年人工調校出來的。
2. **Performance optimization agent**:在叢集裡巡找低使用率的作業,做 profiling 與 benchmarking,搭配團隊多年累積的知識庫做最佳化,再對各團隊發出 review request。
3. **Autonomous research agent**:建立在前兩者之上;工程師只需定義目標,agent 就自主執行架構掃描或超參數調校來最佳化該目標。

三者共用同一套生命週期:工程師寫下目標 → agent 形成假設 → 生成程式碼 → 在 GPU 上執行 → 評估結果 → 回頭迭代。**這個迴圈會連續自主跑上數小時甚至數天,期間沒有人介入。**

#### 三個基礎設施位移:UX、compute、trust(約 01:10–01:12)

- **UX**:過去平台的重心是提供豐富抽象,讓工程師好寫 ML pipeline、訓練迴圈與資料存取。這些仍然重要,但那些程式碼**今天是 LLM 寫的**;使用者的注意力已經轉移到「怎麼組 agentic workflow」與「怎麼設護欄讓 agent 不偏離原本任務」。
- **Compute**:工程師過去只會啟動有限數量的長跑 job,幾分鐘的排程延遲可以被整段訓練時間攤平。**Agent 卻能在極短時間內丟出上百個 job**,長度從幾分鐘到數天不等。
- **Trust**:人類工程師寫的程式碼本質上是被信任的;**agent 生成的程式碼必須在高度受限的環境中執行**。

#### 平台設計:agent 就是一種任務,只是不可信(約 01:12–01:13)

在 LinkedIn 的基礎設施裡,**agent 就是一個普通任務**——使用者撰寫 agent 的方式與撰寫 PyTorch / TensorFlow job 相同。差別只有一點:agent 的程式碼不可信,所以它跑在高度受限的環境裡——**沒有 egress、拿不到憑證**,所有通訊都經由 proxy、並以該 agent 自己的身分進行。

針對長程執行的漂移問題,他們採用 **harness-as-code**:自然語言 prompt 在長時間執行下表現不佳,所以每個階段都用程式碼定義、各有明確職責;更關鍵的是 **scorer 與 evaluator 也定義在程式碼裡**,避免 agent reward hacking 或偏離路徑。周邊還有一整套任務與 memory 管理生態(同型 / 異型 agent 之間如何交換學到的東西),以及 human-in-the-loop 互動用的通知機制。因為 agent 會跑很久,他們也做了**穩健的 checkpoint 與 restore**,讓 agent 能自主從失敗中復原,不需人介入。

上百個 job 同時湧入也壓垮了原本充滿抽象層的 control plane——抽象的成本在 agent 規模下會累加。於是他們自建了一套 control plane,**維持一池溫熱的 GPU pod** 以提供極低延遲的 job 啟動;同樣地,這池 pod 也是高度受限的:無 egress、資料唯讀、以非特權模式執行。

#### 成效與下一步(約 01:13–01:14)

- 叢集中的**實驗數量在過去 6 個月成長 100%**。
- 持續投資 evaluation,好讓實驗真的能轉成生產價值。
- 正在投入**專用任務的 SLM(小型語言模型)**,以及 **GPU 共享技術**——GPU 越做越大,但不是所有任務都大到能吃滿一顆 GPU。

結語:agent 的意義是「take more shots at the goal」——射門次數越多,模型改進越多,最終轉化成更好的會員體驗與商業價值。

### 金句

> "The agent code is untrusted. So it runs in a highly restricted environment like no egress, no access to credentials, and all the communication goes via our proxies using the agent's own identity."(約 01:12)

「Agent 就是普通任務」這句話唯一的例外,就是信任邊界。

> "The goal with agents for us is to take more shots at the goal."(約 01:14)

不是取代工程師,而是把實驗吞吐量拉高一個量級。

## English Notes

### TL;DR

- **Three agents already delivering production value**: a model generation agent migrating 400+ production TensorFlow models to PyTorch; a performance optimization agent that hunts low-utilization jobs in the cluster and optimizes them; and an autonomous research agent where an engineer defines an objective and the agent runs architecture sweeps and hyperparameter tuning on its own.
- **Agents forced three infrastructure shifts**: UX (from rich authoring abstractions toward designing agentic workflows and guardrails, since the code itself is now LLM-written), compute (from a handful of long-running jobs to hundreds launched within minutes, where scheduling latency no longer amortizes), and trust (human code is trusted by default; agent code is not).
- **Harness-as-code is their answer to long-horizon drift**: every stage is defined in code with its own responsibilities, and crucially **the scorers and evaluators are code too**, so agents can't reward-hack or wander off — backed by checkpoint/restore so agents recover from failures without a human.

### Key Points

#### Three production agents and their shared lifecycle (~01:09–01:10)

LinkedIn's AI Platforms team runs three classes of agent that have already delivered significant business value:

1. **Model generation.** LinkedIn runs 400+ production models written in TensorFlow and wants them on PyTorch. The hard part isn't translation — it's **guaranteeing the generated models perform on par with or better than what's deployed**, given those deployed models were hand-tuned by engineers over months or years.
2. **Performance optimization.** An agent that scans the cluster for low-utilization jobs, profiles and benchmarks them, optimizes them against a knowledge base the team accumulated over years, and files review requests to the owning teams.
3. **Autonomous research.** Built on top of the other two: an engineer defines an objective, and the agent autonomously runs architecture sweeps or hyperparameter tuning against it.

All three share a lifecycle: engineer states an objective → agent forms a hypothesis → generates code → runs it on GPUs → evaluates the outcome → iterates. **This loop runs continuously and autonomously for hours or even days with no human intervention.**

#### Three shifts: UX, compute, trust (~01:10–01:12)

- **UX.** The platform historically invested in rich abstractions so engineers could write ML pipelines, training loops, and data access easily. Those still matter, but **that code is now written by an LLM**; users' attention has shifted to composing agentic workflows and setting guardrails so agents don't deviate from the original task.
- **Compute.** Engineers used to launch a limited number of long-running jobs, where a couple of minutes of scheduling delay amortized over the training run. **Agents launch hundreds of jobs in a very short window**, ranging from minutes to days in length.
- **Trust.** Code written by human engineers is inherently trusted; **agent-generated code needs a very constrained environment**.

#### The platform: an agent is just a job — an untrusted one (~01:12–01:13)

In their infrastructure, **an agent is just like any other task** — users write agents the same way they'd write a PyTorch or TensorFlow job. The one difference is trust: agent code runs in a highly restricted environment with **no egress and no access to credentials**, with all communication routed through proxies under the agent's own identity.

Against long-horizon drift they use a **harness-as-code** approach: natural-language prompts don't hold up when agents run for long periods, so each stage is defined in code with its own responsibilities — and more importantly, **the scorers and evaluators are defined in code as well**, so agents can't reward-hack or diverge from the intended path. Around that sits an ecosystem for task and memory management (how agents share learnings with other agents of the same or different type) plus notifications for human-in-the-loop interactions. Because these agents run for a long time, they also built robust **checkpointing and restore** so agents autonomously recover from failures.

The volume of jobs also became a bottleneck in the control plane, which had been designed with a lot of abstraction — and abstraction costs add up once agents start launching many jobs. So they built a custom control plane maintaining a **warm pool of GPU pods** for very low-latency job launches. That pool is equally locked down: no egress, read-only data access, running fully unprivileged.

#### Impact and what's next (~01:13–01:14)

- **The number of experiments in the cluster grew 100% over the last six months.**
- Continued investment in evaluation, so that experiments translate into real production value.
- Ongoing work on **SLMs for specialized tasks** and **GPU sharing techniques**, since GPUs keep getting bigger while not every task is big enough to saturate one.

His closing frame: agents let you "take more shots at the goal" — more shots means more model improvements, which means better member experience and business value.

### Quotes

> "The agent code is untrusted. So it runs in a highly restricted environment like no egress, no access to credentials, and all the communication goes via our proxies using the agent's own identity." (~01:12)

The one place where "an agent is just another job" stops being true: the trust boundary.

> "The goal with agents for us is to take more shots at the goal." (~01:14)

Not replacing engineers — raising experiment throughput by an order of magnitude.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| LinkedIn AI Platforms | 講者所屬團隊,負責承載這些 agent 的 ML 基礎設施 | The speaker's team; owns the ML infrastructure hosting these agents | 內部平台,無公開名稱 / internal platform, no public name given |
| Harness-as-code | 用程式碼定義 agent 各階段與 scorer / evaluator 的做法 | Defining each agent stage — and the scorers/evaluators — in code rather than prompts | 講者描述的做法,非產品名 / a described practice, not a product name |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Anka Goyle | Ankit Goyal |
| ser requests | review requests(依語境 / from context) |
| longunning | long-running |

## 待確認 / To Verify

- 自訂 control plane 與 warm GPU pod 機制是否有對外公開的名稱或工程部落格文章。/ Whether the custom control plane / warm GPU pod design has a public name or engineering blog post.
- 「實驗數量成長 100%」的基準線與計數方式(是 job 數還是 experiment 數)未說明。/ The baseline and counting method behind the "100% growth in experiments" figure.
- 400+ TensorFlow 模型遷移到 PyTorch 的專案完成進度未提及。/ How far along the TensorFlow-to-PyTorch migration actually is.
