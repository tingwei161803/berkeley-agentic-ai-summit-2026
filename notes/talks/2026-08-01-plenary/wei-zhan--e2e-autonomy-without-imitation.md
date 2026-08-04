---
title: "E2E Autonomy Without Imitation"
title_zh: "不靠模仿的端到端自動駕駛"
speaker: "Wei Zhan"
affiliation: "Chief Scientist, Applied Intuition"
type: talk
stage: Plenary
date: 2026-08-01
session: "Session 4: Robotics & World Models"
video: "https://www.youtube.com/watch?v=Tcn5Yb2K0h4&t=10922s"
video_range: "03:02:02–03:08:45"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [autonomous-driving, reinforcement-learning, self-play, world-models, closed-loop]
---

# 不靠模仿的端到端自動駕駛(E2E Autonomy Without Imitation)

**一句話總結**:把「學會開車」與「學會看」拆開——先用零人類示範的大規模 self-play RL 練出駕駛專家(TerraZero),再把它的 latent 與動作蒸餾給端到端模型(TerraTransfer)——就能在訓練配方裡完全不用 imitation,仍拿下閉環端到端駕駛的 SOTA。
**One-line summary**: Decouple learning to drive from learning to see — train a driving expert with large-scale self-play RL and zero human demonstrations (TerraZero), then distill its latents and actions into an end-to-end model (TerraTransfer) — and you reach state-of-the-art closed-loop end-to-end driving with no imitation anywhere in the recipe.

## 中文筆記

### TL;DR

- **典範正在從 AV 2.0 換到 AV 3.0**:L2++ ADAS 已經收斂到「imitation learning 為底的端到端」並量產,領先者再用開環 RL 做 post-training;下一代預期是**在能反應式生成周遭行為與畫面的 world model 裡做閉環 RL**——也就是從 AV 2.0 的開環 scaling 轉向 **AV 3.0 的閉環 scaling**。
- **他們的作法是拆成兩階段**:phase 1「learn to drive」用 **TerraZero**(self-play RL 框架,吞吐量遠高於既有駕駛模擬器)在**零人類示範**下累積等效 **25 個世紀的駕駛經驗**;phase 2「learn to see」用 **TerraTransfer** 把這個 self-play 專家的 latent 與動作,在離線資料集的同一批駕駛情境上對齊給端到端模型。
- **關鍵論點**:self-play 閉環 RL 搭配 reactive world model **不只是 post-training 技巧,而是很強的 pre-training 技巧**;而 RL 框架與 world model 的**吞吐量**會是這條路線的決勝因素。

### 重點整理

#### 為什麼是「不靠模仿」(約 03:02–03:04)

開場定位:端到端自動駕駛是**真實世界中第一個被大規模量產的 physical AI**,而他要談的是一件**與主流有點反直覺**的事——只用強化學習、不靠模仿,來增強這種自動駕駛。

Applied Intuition 的自我介紹:涵蓋汽車、卡車、農業、礦業、營建等垂直產業的 physical AI 技術供應商,提供 autonomy stack、OS、模擬工具與更廣義的 physical AI 基礎設施;**估值 150 億美元、超過一千名工程師**;同時在 RL 與 world model 上做前沿研究並在頂會發表(含得獎論文)。

典範現況與趨勢:

- **現在**:L2++ ADAS 已收斂到 imitation learning 為底的端到端方案並量產,部分領先者再用**開環 RL** 做 post-training,把安全性與魯棒性推上一級。
- **接下來**:下一代自動駕駛預期會在一個**能反應式(reactively)生成周遭行為與視覺的 world model** 裡,用**閉環 RL** 訓練。這就是 **AV 2.0 開環 scaling → AV 3.0 閉環 scaling** 的典範轉移。

Applied 一直在打造**高吞吐量的 reactive world model**,支撐端到端自動駕駛的大規模閉環 RL,而且這條路已經拿到很好的成績。但他要問的是:**有沒有更聰明的做法?** 他們的答案是**把「學會開車」和「學會看」解耦**。

#### Phase 1:learn to drive — TerraZero(約 03:04–03:07)

**TerraZero** 是他們的 self-play RL 框架,**吞吐量遠高於其他 SOTA 的駕駛模擬器與 self-play 框架**。他們只用了一些公開資料集的地圖多樣性,就能取得**等效 25 個世紀的駕駛經驗,且零人類示範**;而且只要 scale GPU 算力與地圖多樣性,這個數字**還能再往上兩到三個數量級**。

成果:TerraZero 訓練出的 policy 在多個**閉環 planning benchmark**(vector-based)上達到 state-of-the-art,**相對於 imitation learning 為底的 planner 有明顯優勢**,尤其是在那些**尚未飽和、只收錄 corner case** 的 benchmark(例如 **InterPlan**)上。它能在各種困難駕駛情境中做出理想動作,並在全球不同城市間展現 **zero-shot 泛化**。

(他也順帶呼應了前一場:Michael 剛剛給了一個 self-play 賦能自駕賽車的好例子,而他要給的是 self-play 賦能**城市道路駕駛**的例子。)

#### Phase 2:learn to see — TerraTransfer(約 03:07–03:08:45)

**TerraTransfer** 的做法是:用一個從 self-play 訓練出來的專家(也就是 TerraZero)去**教**另一個端到端自動駕駛模型。具體是在**離線資料集裡的同一批駕駛情境上,同時對齊兩者的 latent 與動作**。

這樣得到的端到端自動駕駛——**訓練配方裡完全沒有 imitation**——在**閉環端到端駕駛 benchmark** 上取得 state-of-the-art,相對其他 imitation-based 方法有明顯優勢,並在各種**刻意構造的困難駕駛情境**中展現出「意外地魯棒」的駕駛行為。

**Key takeaways:**

1. 自動駕駛典範正朝**閉環 scaling(AV 3.0)** 移動。
2. **端到端模型與 vector-based planner 都能靠純 self-play / 閉環 RL 的訓練配方達到 SOTA,不需要 imitation。**
3. 搭配 reactive world model 的 self-play 閉環 RL **不只是 post-training 技巧,更是很強的 pre-training 技巧**。
4. **RL 框架與 world model 的吞吐量**,會是這種閉環 scaling 典範的決勝因素。

### 金句

> "End-to-end autonomy … is the first massively productionized physical AI in the real world."(約 03:02:05)

在一整場談「機器人還在 pre-ChatGPT 時刻」的 session 裡,這是唯一一場談「已經量產」的技術。

> "25 centuries of driving experience with zero human demonstrations."(約 03:05)

一句話說明 self-play 相對於路測資料的規模差距。

> "They are not just some post-training technique, actually they are very powerful pre-training techniques."(約 03:08:20)

他最想扭轉的認知:閉環 RL 不是最後一哩的修飾,而是主訓練手段。

## English Notes

### TL;DR

- **The paradigm is shifting from AV 2.0 to AV 3.0.** L2++ ADAS has converged on imitation-learning-based end-to-end stacks in mass production, with leading players adding open-loop RL post-training. The next generation is expected to train with **closed-loop RL inside a world model that reactively generates surrounding behavior and visuals** — open-loop scaling giving way to **closed-loop scaling**.
- **Their approach splits the problem in two.** Phase 1, "learn to drive," uses **TerraZero**, a self-play RL framework with far higher throughput than existing driving simulators, accumulating the equivalent of **25 centuries of driving experience with zero human demonstrations**. Phase 2, "learn to see," uses **TerraTransfer** to align the self-play expert's latents and actions into an end-to-end model over the same driving cases from an offline dataset.
- **The central claim**: self-play closed-loop RL with a reactive world model is **not merely a post-training technique but a powerful pre-training one** — and the **throughput** of the RL framework and the world model is the decisive factor for this paradigm.

### Key Points

#### Why "without imitation" (~03:02–03:04)

He framed the talk around end-to-end autonomy as **the first massively productionized physical AI in the real world**, and set out to argue something **counterintuitive relative to the mainstream**: enhancing that autonomy with reinforcement learning alone, without imitation.

Applied Intuition's positioning: a premier physical AI technology provider across verticals including cars, trucks, agriculture, mining, and construction, supplying the autonomy stack, OS, simulation tools, and broader physical AI infrastructure. **A $15 billion valuation company with over a thousand engineers**, also doing cutting-edge research on RL and world models with publications (including award-winning papers) at top venues.

Where the paradigm stands, and where it's heading:

- **Today**: the L2++ ADAS paradigm has converged on imitation-learning-based end-to-end systems in mass production, with some leading players adding **open-loop RL** post-training to push safety and robustness to the next level.
- **Next**: end-to-end autonomy is expected to be trained with **closed-loop RL inside a world model** that can **reactively** generate surrounding behavior and visuals. That's the shift from **AV 2.0 open-loop scaling to AV 3.0 closed-loop scaling**.

Applied has been building the **high-throughput reactive world model** that supports large-scale closed-loop RL for end-to-end autonomy, and the paradigm already performs well. But his question was whether there's **an even smarter way** — and their answer is to **decouple learning to drive from learning to see**.

#### Phase 1: learn to drive — TerraZero (~03:04–03:07)

**TerraZero** is their self-play RL framework, **much faster and higher-throughput than other state-of-the-art driving simulators and self-play frameworks**. Using only some public datasets for map diversity, it obtains the equivalent of **25 centuries of driving experience with zero human demonstrations** — and that number can be scaled **two to three orders of magnitude higher** simply by scaling GPU compute and map diversity.

The results: policies trained by TerraZero achieve state of the art on various **closed-loop planning benchmarks** (vector-based), setting **a clear edge over imitation-learning-based planners**, especially on non-saturated, corner-case-only benchmarks such as **InterPlan**. The policy handles a range of challenging driving scenarios with desirable actions and shows **zero-shot generalization across global cities**.

(He connected back to the previous talk: Michael had just given a good example of self-play powering autonomous racing; his is an example of self-play powering autonomous *urban* driving.)

#### Phase 2: learn to see — TerraTransfer (~03:07–03:08:45)

**TerraTransfer** trains an end-to-end autonomy model taught by an expert trained from self-play — namely TerraZero. Concretely, they **align both the latents and the actions of the two models on the same driving cases from an offline dataset**.

The resulting end-to-end autonomy — with **no imitation anywhere in its training recipe** — obtains state-of-the-art driving performance on **closed-loop end-to-end driving benchmarks**, a clear edge over other imitation-based methods, handling a variety of intentionally constructed challenging scenarios with what he called surprisingly robust driving behavior.

**Key takeaways:**

1. The autonomy paradigm is shifting toward **closed-loop scaling (AV 3.0)**.
2. **Both end-to-end and vector-based planners can reach state of the art with a self-play / closed-loop RL training recipe alone — no imitation.**
3. Self-play closed-loop RL with a reactive world model is **not just a post-training technique; it's a very powerful pre-training technique**.
4. The **throughput** of the RL framework and the world models can be the **decisive factor** for this closed-loop scaling paradigm.

### Quotes

> "End-to-end autonomy … is the first massively productionized physical AI in the real world." (~03:02:05)

In a session premised on robotics being pre-ChatGPT, this was the one talk about technology already in mass production.

> "25 centuries of driving experience with zero human demonstrations." (~03:05)

The scale gap between self-play and road-test data, in one number.

> "They are not just some post-training technique, actually they are very powerful pre-training techniques." (~03:08:20)

The perception he most wants to change: closed-loop RL isn't last-mile polish, it's the main training method.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| TerraZero | self-play RL 框架,零人類示範累積等效 25 個世紀駕駛經驗;閉環 planning benchmark SOTA | Self-play RL framework; 25 centuries of driving experience with zero human demonstrations; SOTA on closed-loop planning benchmarks | phase 1「learn to drive」/ the "learn to drive" phase |
| TerraTransfer | 把 self-play 專家的 latent 與動作對齊給端到端模型,訓練配方完全無 imitation | Aligns a self-play expert's latents and actions into an end-to-end model; no imitation in the recipe | phase 2「learn to see」/ the "learn to see" phase |
| InterPlan | 只收錄 corner case、尚未飽和的閉環 planning benchmark | Non-saturated, corner-case-only closed-loop planning benchmark | TerraZero 在此對 imitation-based planner 拉開差距 / where TerraZero's edge is clearest |
| Applied Intuition | 涵蓋車、卡車、農業、礦業、營建的 physical AI 技術供應商 | Physical AI technology provider across cars, trucks, agriculture, mining, construction | 估值 150 億美元、逾千名工程師 / $15B valuation, 1000+ engineers |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Wei Jean / Ray / Way | Wei Zhan |
| terra zero / terror zero | TerraZero |
| terror transfer | TerraTransfer |
| interplan | InterPlan |
| cell play / selflay | self-play |
| close reinforcement learning / closable scaling / close super RL | closed-loop reinforcement learning / closed-loop scaling |
| Engine autonomy | End-to-end autonomy |
| ADA system | ADAS |
| local motion | locomotion |
| Acura and the CPR booth(panel 段) | ICRA and the CVPR booth(待確認 / to verify) |

## 待確認 / To Verify

- 主持人介紹他時提到「co-director of Berkeley DeepDrive」,官網議程僅列 Applied Intuition 職稱;此處 frontmatter 以議程為準。/ The host also introduced him as co-director of Berkeley DeepDrive; the official agenda lists only the Applied Intuition title, which is what frontmatter uses.
- 他提到的閉環端到端駕駛 benchmark 具體名稱,演講中未逐一報出(除 InterPlan 外)。/ Beyond InterPlan, the specific closed-loop end-to-end driving benchmarks were not individually named.
- panel 中他提到一家未具名公司的 R&D 車輛在擁擠街道連續一小時零接管、算力僅 Tesla HW4 的 1/7;無法查證。/ In the panel he cited an undisclosed company achieving one hour of intervention-free driving in dense streets on 1/7 the compute of Tesla HW4 — unverifiable.
