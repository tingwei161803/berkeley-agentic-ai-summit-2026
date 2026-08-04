---
title: "Solving Quantum Science Problems with SMART: A Self-evolving Multi-Agent Research Tree"
title_zh: "用 SMART 解決量子科學問題:自我演化的多智能體研究樹"
speaker: "Andrew Schoen"
affiliation: "Partner, NEA(本場由 UC Berkeley 的 Mingu Kang 代為報告 / presented on his behalf by Mingu Kang, UC Berkeley)"
type: talk
stage: Nexus
date: 2026-08-01
session: "Session 1: AI for Science"
video: "https://www.youtube.com/watch?v=LB7IkZhEYic&t=2869s"
video_range: "00:47:49–01:03:11"
transcript: "tmp/[English (auto-generated)] Nexus Stage - August 1st - Morning Session [DownSub.com].srt"
status: draft
tags: [ai-for-science, quantum-computing, multi-agent, neutral-atoms, benchmark]
---

# 用 SMART 解決量子科學問題:自我演化的多智能體研究樹(Solving Quantum Science Problems with SMART: A Self-evolving Multi-Agent Research Tree)

**一句話總結**:科學發現的 agent 系統需要的不是更長的 loop,而是一棵會自己重組的研究樹——SMART 用 planner/worker/verifier 三件組構成節點、讓樹隨探索改寫自己,在中性原子量子電腦的原子搬運問題上把重排時間壓低 25–83%。
**One-line summary**: Agentic systems for discovery don't need longer loops, they need a research tree that rewrites itself — SMART builds nodes from planner/worker/verifier triples, lets the tree restructure as agents explore, and cuts atom-rearrangement time on neutral-atom quantum computers by 25–83%.

## 中文筆記

> 註:議程上的講者為 Andrew Schoen(Partner, NEA),因故未能出席,現場由 UC Berkeley 的 Mingu Kang 代為報告;他在台上說明這是與 Daniel Lee、Andrew Schoen 的共同工作。本場投影片在演講進行超過一半後才接上,前段由講者口述。

### TL;DR

- **為什麼從量子科學下手**:它是「strategic Everest」——極度跨領域(數學、物理、資工、工程、材料)、要求極端嚴謹(任何一個環節錯了實驗根本不會動)、而且品質落差極大(高品質研究稀有,專家對 AI slop 高度警戒)。翻過這座山,系統就有機會帶動任何領域。
- **SMART = Self-evolving Multi-Agent Research Tree**:節點由 planner / worker / verifier 三種 agent 組成;verifier 的輸出餵給 tree planner agent,由它設計下一步的 workflow tree。節點可以是目標也可以是任務,每一步可被 split、merge、select 或 add。
- **成績單**:在 OpenAI 的科學推理 benchmark「Frontier Science」上,alpha 原型的準確率最高,而成本只有次佳系統(codex 5.5)的 1/5——低成本來自底層用 GLM 5.1,高準確率來自 agent 編排;在準確率 × 成本的平面上定義了 Pareto frontier。
- **真實問題**:中性原子量子電腦的原子分配與路由。四個 benchmark 電路上,SMART 解法把重排時間降低 25% 到 83%。ablation 顯示不同電路要靠不同策略組合(graph state 電路光靠利用電路結構就 −83%;QPE exact 電路則要參數調整 + A* 重新設計才 −25%,結構完全幫不上忙)——**這種互補性正是多智能體框架的價值所在**。

### 重點整理

#### 為什麼從量子科學開始:介面才是真正的問題(約 00:48–00:55)

他們要建的是能**編排任何前沿科學研究**的 agentic 系統,而第一個目標領域選了量子科學。

動機從他自己的研究經驗來:量子研究是不折不扣的跨領域堆疊——物理、化學、數學、硬派工程、材料。理想上一個人要懂完整條 stack,才能把不同層的想法連起來、真正端到端 co-design,那才是造量子電腦的最佳方式。但現實是資源永遠不夠,而且**真正的問題出在介面**:一個研究者是某一層的專家,另一個是另一層的專家,交接非常困難。他看到的 AI 機會就在這裡:**讓 AI 掌握所有層的脈絡,去促成這些交接**。

他把科學發現拆成三根支柱:

1. **Intelligence** —— 綜合知識,跑「規劃 → 執行 → 驗證」的序列。
2. **Computation** —— 模擬大型系統、在巨大解空間上做最佳化。
3. **Validation** —— 做真正的實驗,拿預測去撞現實。

願景是一個能在這三根支柱之間**跑完整迴圈**的 agentic 系統。

而量子科學是「strategic Everest」,理由有三:(a) 極度困難且跨領域;(b) **要求極端嚴謹**——除非每一個環節都正確,量子實驗根本不會動;(c) 量子研究的**品質落差極大**,高品質研究非常稀有,而專家對 AI slop 高度警戒。爬過這座山,他們相信這套 agentic 系統就有能力在任何領域帶出科學發現。

他也給了一頁量子計算複習:qubit 不是 bit——bit 是 0 或 1(像擲硬幣),qubit 可以是 0 與 1 的疊加態,落在球面上任一點;量子物理讓我們取得 qubit(例如取原子的兩個穩定電子能階);量子硬體平台讓我們完全控制量子物理來運算——投影片上是一組用雷射控制的原子陣列。

#### SMART 的三個設計原則與樹狀架構(約 00:55–00:58)

他們的前提是:**變革性的科學發現會來自人機協作**。由此推出三個設計原則:

1. **workflow tree 會隨著 agent 探索而不斷被更新**。
2. 系統要**結構化但同時保有彈性**。
3. agent 要**自主,但人類隨時可以介入**。

這意味著需要一套跟「loop engineering」完全不同的 agent 系統——loop engineering 被廣泛用在比科學發現簡單得多的任務上。

於是有了 **SMART(Self-evolving Multi-Agent Research Tree)**。主要特徵是一棵樹,每個節點由 **planner、worker、verifier** 三種 agent 構成;verifier 的輸出餵回 **tree planner agent**,由它設計下一步的 workflow tree。節點可以是一個 goal 也可以是一個 task;下一步時,task 可以被 **split、merge、select 或 add**。

UI 部分他強調人類介入的必要性——「研究裡總會發生無法預期的事,就像投影片不出來或筆電當機」,所以要留彈性讓人介入;另一個介面讓研究者去探查 agent 產出的結果,關鍵功能是**管理 context、選擇模型、追蹤成本**。

**Benchmark**:市面上科學發現的 agentic 系統很多,SMART 的優勢在於**同時 steerable 與 adaptive**,正是「結構化 + 彈性」設計的結果。他們拿 alpha 原型跟前沿模型與系統比,用的是 OpenAI 做的科學推理 benchmark **Frontier Science**。結果:**原型準確率最高,成本只有次佳系統(codex 5.5)的 1/5**;低成本來自底層模型用 **GLM 5.1**,高準確率來自 agent 編排。畫成準確率(y)× 成本(x)的二維圖,SMART 明確定義了 Pareto frontier——而這還只是原型。

#### 實戰:加速中性原子量子電腦(約 00:58–01:03)

**問題**:量子計算的重點就是算得更快,所以他們要壓低 wall-clock time——具體是加速中性原子上的量子電路執行。

電路裡水平線是 qubit,上面施加 quantum gate;藍色的 entangling gate 靠把兩個 qubit 原子搬到很近的距離、放進 **entanglement zone** 來執行。所以在 **zoned architecture** 的中性原子量子電腦上跑一段電路,流程是:先把 qubit 原子分配到 **storage zone** 的槽位,再把原子在 entanglement zone 之間搬進搬出來執行 entangling gate。

但原子不能任意搬:因為是用雷射光束搬運,存在硬約束——例如**定義某一塊原子的行與列,不能跨越另一塊的行與列**。

於是問題成形:**給定量子電路與 zoned architecture,如何在滿足原子移動約束的前提下,找到讓重排時間最小的 qubit 原子分配與路由方案?** 解空間極其龐大,而且對中性原子量子電腦非常重要——所以被選為 SMART 的第一個實戰題。

**結果**:四個 benchmark 量子電路上(數字越低越好),SMART 的解法相對 state-of-the-art 把重排時間降低了 **83% 到 25%**。

**Ablation 才是重點**:多個 agent 探索了不同策略,而**不同電路是被不同的策略組合改善的**。左邊的 graph state 電路,**光靠利用電路本身的結構就減少 83%**;右邊的 QPE exact 電路,那 25% 來自**參數調整加上 A\* 重新設計的組合**,而利用結構在這裡**完全沒有幫助**。他的結論:正是這種策略之間的互補性,讓多智能體框架這麼有力。

流程上,agent 先探索不同策略,然後任務被 split、merge……直到找出更好的解。他也放了原子重排的模擬影片:SMART 的解法明顯在利用某種結構,而 state-of-the-art 基線沒有,所以耗時長得多。

**下一步**:量子科學裡還有其他極有意思也極困難的問題可以用 SMART 攻,例如**錯誤更正(error correction)**——那會是「打造能帶來變革性科學發現的 agent」的下一個試煉場。

### 金句

> "Quantum science demands extreme rigor. Unless every single piece is correct, the quantum experiments simply would not work."(約 00:53)

為什麼量子是最好的照妖鏡:它不接受 AI slop。

> "So once we climb the strategic Everest, then we believe that the agentic system will be capable of leading scientific discoveries in any domain."(約 00:54:46)

先挑最難的山爬,而不是先挑好爬的。

> "…different circuits are improved by different combinations of strategies. … So really this complementarity of different strategies is what makes the multi-agent framework so powerful."(約 01:00)

多智能體不是為了更多算力,而是為了策略的互補。

## English Notes

> Note: the scheduled speaker, Andrew Schoen (Partner, NEA), couldn't attend; Mingu Kang of UC Berkeley presented on his behalf, describing it as joint work with Daniel Lee and Andrew Schoen. The slides didn't come up until well past the halfway point, so the first stretch was delivered from memory.

### TL;DR

- **Why start with quantum science**: it's the "strategic Everest" — deeply multidisciplinary (math, physics, CS, engineering, materials), demanding of extreme rigor (get any one piece wrong and the experiment simply doesn't work), and huge in quality delta (high-quality research is rare and experts are acutely wary of AI slop). Climb that, and the system should carry over to any domain.
- **SMART = Self-evolving Multi-Agent Research Tree**: each node is a planner / worker / verifier triple; verifier output feeds a tree planner agent that designs the next step's workflow tree. Nodes are goals or tasks, and at each step tasks can be split, merged, selected, or added.
- **Scorecard**: on OpenAI's Frontier Science reasoning benchmark, their alpha prototype hit the highest accuracy at one-fifth the cost of the second-best system (codex 5.5) — cheap because GLM 5.1 is the underlying model, accurate because of the agent orchestration. It defines the Pareto frontier on the accuracy-versus-cost plane.
- **Real problem**: qubit allocation and routing on neutral-atom quantum computers. Across four benchmark circuits, SMART's solutions cut rearrangement time by 25% to 83%. Ablations show different circuits need different strategy combinations (a graph-state circuit gets −83% from circuit structure alone; a QPE exact circuit gets −25% from parameter tuning plus an A\* redesign, with structure contributing nothing) — **and that complementarity is the argument for a multi-agent framework**.

### Key Points

#### Why quantum first: the handoffs are the real problem (~00:48–00:55)

The goal is an agentic system that can **orchestrate any frontier research in science**, starting with quantum.

The motivation comes from his own experience. Quantum research is a genuinely multidisciplinary stack — physics, chemistry, math, hard engineering, materials. Ideally one person would know the whole stack and connect ideas across layers to co-design end to end, which would be the optimal way to build a quantum computer. But resources are always short and, more importantly, **the interfacing is the real problem**: one researcher is an expert in one layer, another in a different layer, and the handoffs are genuinely hard. That's where he sees AI's promise — **an AI holding the context of every layer and facilitating the handoffs**.

He frames scientific discovery as three pillars:

1. **Intelligence** — synthesize knowledge, run the plan / work / verify sequence.
2. **Computation** — simulate large systems, optimize over vast solution spaces.
3. **Validation** — run real experiments, test predictions against reality.

The vision is an agentic system that closes the loop across all three.

Quantum science is the strategic Everest for three reasons: it's very challenging and multidisciplinary; it **demands extreme rigor** — unless every single piece is correct, the experiment simply won't work; and the **quality delta is massive** — high-quality research is rare and experts are very concerned about AI slop. Climb that, and they believe the system can lead discoveries anywhere.

His one-slide quantum refresher: a bit is 0 or 1, like a coin flip, while a qubit can be in a superposition anywhere on a sphere; quantum physics gives access to qubits (e.g. two stable electronic energy levels of an atom); and a quantum hardware platform gives full control over that physics — in this case an array of atoms manipulated with lasers.

#### SMART's three design principles and tree architecture (~00:55–00:58)

Their premise is that transformative discovery will come from **human–AI collaboration**, which yields three design principles:

1. The **workflow tree keeps getting updated** as the agents explore.
2. The system is **structured but also flexible**.
3. Agents are **autonomous but humans can intervene at any time**.

That requires something different from the "loop engineering" widely used for tasks far simpler than scientific discovery.

Hence **SMART (Self-evolving Multi-Agent Research Tree)**: a tree whose nodes each consist of **planner, worker, and verifier** agents, with verifier outputs feeding a **tree planner agent** that designs the next step's workflow tree. A node can be a goal or a task, and at the next step a task can be **split, merged, selected, or added**.

On the interface, he made the case for human intervention concretely — "in research, unpredictable things always happen, just like slides not appearing or the laptop crashing." A second interface lets researchers probe what agents produced, with **context management, model choice, and cost tracking** as the key features.

**Benchmark**: plenty of agentic systems for scientific discovery exist; SMART's advantage is being **both steerable and adaptive**, which follows directly from the structured-plus-flexible design. They compared their alpha prototype against frontier models and systems on **Frontier Science**, a scientific reasoning benchmark from OpenAI. The prototype achieved **the highest accuracy at one-fifth the cost of the second-best system (codex 5.5)** — low cost from using **GLM 5.1** underneath, high accuracy from orchestrating the agents. Plotted as accuracy versus cost, SMART defines the Pareto frontier — and this is only the prototype.

#### The real problem: speeding up neutral-atom quantum computers (~00:58–01:03)

**The setup**: quantum computing is about computing faster, so the target is wall-clock time — specifically, executing quantum circuits faster on neutral atoms.

In a circuit, horizontal lines are qubits with quantum gates applied; the blue entangling gates are performed by bringing two qubit atoms close together inside an **entanglement zone**. So running a circuit on a **zoned-architecture** neutral-atom machine means first allocating qubit atoms to slots in the **storage zone**, then shuttling atoms in and out of the entanglement zone to perform entangling gates.

The catch: atoms can't be moved arbitrarily. Because lasers do the moving, constraints apply — for instance, **the rows and columns defining one block of atoms cannot cross the rows and columns of another block**.

The problem: **given a quantum circuit and a zoned architecture, what is the optimal allocation and routing of qubit atoms that minimizes rearrangement time while satisfying the movement constraints?** The solution space is vast and the answer genuinely matters for neutral-atom machines — which is why they picked it as SMART's first target.

**Results**: across four benchmark circuits (lower is better), SMART's solutions achieved **83% to 25% lower rearrangement time** than the state of the art.

**The ablations are the interesting part.** Multiple agents explored different strategies, and **different circuits were improved by different combinations of them**. For the graph-state circuit on the left, rearrangement time dropped **83% by using the structure of the circuit alone**. For the QPE exact circuit on the right, the 25% reduction came from **parameter tuning combined with an A\* redesign**, and using structure **didn't help at all**. His conclusion: this complementarity across strategies is exactly what makes the multi-agent framework powerful.

Procedurally, agents explore different strategies and then tasks are split, merged, and so on until a better solution emerges. He also showed a simulation video of the rearrangement: SMART's solution clearly exploits some structure while the state-of-the-art baseline doesn't, so the baseline takes far longer.

**Next**: quantum science has other tremendously interesting and difficult problems for SMART — **error correction** among them — as the proving ground for agents that lead to transformative discovery across frontier domains.

### Quotes

> "Quantum science demands extreme rigor. Unless every single piece is correct, the quantum experiments simply would not work." (~00:53)

Why quantum is the honest test: it doesn't accept AI slop.

> "So once we climb the strategic Everest, then we believe that the agentic system will be capable of leading scientific discoveries in any domain." (~00:54:46)

Pick the hardest mountain first, not the most climbable one.

> "…different circuits are improved by different combinations of strategies. … So really this complementarity of different strategies is what makes the multi-agent framework so powerful." (~01:00)

Multi-agent isn't about more compute — it's about strategies that complement each other.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| SMART | Self-evolving Multi-Agent Research Tree:節點含 planner/worker/verifier,tree planner 依 verifier 輸出重繪工作樹 | Self-evolving Multi-Agent Research Tree: planner/worker/verifier nodes, with a tree planner redrawing the workflow from verifier output | 演講時為 alpha 原型 / alpha prototype at the time of the talk |
| Frontier Science | OpenAI 製作的科學推理 benchmark,用於比較 SMART 與前沿系統 | Scientific reasoning benchmark from OpenAI used to compare SMART against frontier systems | 名稱依逐字稿 / name per transcript |
| GLM 5.1 | SMART 原型底層使用的模型,是低成本的來源 | The underlying model in the SMART prototype; the source of its low cost | |
| codex 5.5 | benchmark 上準確率次佳的系統,成本為 SMART 的 5 倍 | Second-best system on the benchmark, at 5× SMART's cost | 名稱依逐字稿 / name per transcript |
| Zoned architecture(中性原子 / neutral atoms) | storage zone 存放 qubit 原子、entanglement zone 執行 entangling gate 的架構 | Architecture with a storage zone holding qubit atoms and an entanglement zone where entangling gates execute | SMART 第一個實戰題的舞台 / the setting for SMART's first applied problem |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Andrew Shawn / Andrew Sha | Andrew Schoen |
| Mingu Kong | Mingu Kang |
| in EA / EA | NEA(New Enterprise Associates) |
| smart / smarts | SMART |
| Asian system / aentic / agendic | agentic system |
| chronoscience | quantum science |
| cubit / cubid | qubit |
| neutrum | neutral atom |
| a star redesign | A\* redesign |
| QPE exact(字幕正確) | QPE exact(quantum phase estimation) |

## 待確認 / To Verify

- **SMART 的所屬單位/新創名稱**未在演講中說明,也查不到公開論文或 repo。/ The organization or startup behind SMART was never named on stage, and no public paper or repo could be found.
- **Frontier Science benchmark**(據稱由 OpenAI 製作)無法在公開資料中確認。/ The "Frontier Science" benchmark attributed to OpenAI could not be confirmed publicly.
- **codex 5.5** 與 **GLM 5.1** 的正式版本名稱未查證。/ Exact product names for "codex 5.5" and "GLM 5.1" unverified.
- 共同作者 **Daniel Lee** 的單位未說明。/ Co-author Daniel Lee's affiliation wasn't given.
- 四個 benchmark 量子電路的完整清單只點名 graph state 與 QPE exact 兩個。/ Only two of the four benchmark circuits (graph state, QPE exact) were named.
- 比較對象「state-of-the-art」指的是哪一套具體 compiler / 演算法未指明。/ The specific state-of-the-art compiler or algorithm used as the baseline wasn't identified.
