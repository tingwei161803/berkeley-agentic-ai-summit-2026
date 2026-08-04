---
title: "From Models to Agents to Discovery: Building the Full Stack of Agentic AI"
title_zh: "從模型到 agent 到科學發現:打造 agentic AI 的完整堆疊"
speaker: "Saurabh Tiwary"
affiliation: "Vice President, Google DeepMind"
type: talk
stage: Plenary
date: 2026-08-01
session: "Session 1: Agentic AI Infrastructure & Platform"
video: "https://www.youtube.com/watch?v=gKdeLQd_LIQ&t=3744s"
video_range: "01:02:24–01:12:30"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 1st - Morning Session [DownSub.com].srt"
status: draft
tags: [infrastructure, tpu, agent-platform, ai-for-science, google-deepmind]
---

# 從模型到 agent 到科學發現:打造 agentic AI 的完整堆疊(From Models to Agents to Discovery: Building the Full Stack of Agentic AI)

**一句話總結**:採用率與每次互動的算力同時暴衝,逼得整個堆疊(TPU → 模型 → 資料 → agentic 安全 → 平台 → 端到端解法)必須協同最佳化;而這一切最終指向的是「autonomous discovery loop」——把原本要數年的研究週期壓縮到數小時到數天。
**One-line summary**: Adoption and per-interaction compute are exploding at the same time, forcing co-optimization across the whole stack — TPUs, models, data, agentic security, platform, end-to-end solutions — and all of it points at an autonomous discovery loop that compresses research cycles from years into hours and days.

## 中文筆記

### TL;DR

- **兩條曲線同時往上**:採用率暴增(Kaggle 的 5-Day AI Agents Intensive 課程 150 萬人報名),而 **agentic 任務的推論算力比非 agentic 高 10–100 倍**;Google 現在每月處理 **3.2 quadrillion(千兆)tokens**——一 quadrillion 約等於「地球上每人一本小說」,所以是每人三本。
- **必須全棧協同最佳化**:AI Hypercomputer(CPU/GPU/TPU)→ 前沿研究與模型 → 資料 → agentic 安全與防禦 → 平台 → 端到端 agentic 解法。TPU 第八代首次拆成 **8t(訓練)與 8i(推論)**:8t 單 pod 121 FP4 exaflops(約前代 3 倍),8i 單 pod 11.6 exaflops(前代 10 倍)。
- **終局是 autonomous discovery loop**:資料攝取(文獻、蛋白質資料庫、實驗紀錄)→ 假說生成(AI co-scientist 辯論假說)→ 模擬(AlphaGenome、AlphaFold 秒級驗證)→ 執行(AlphaEvolve、Gemini Robotics 跑濕實驗)→ 回饋。**原本要數年的研究週期,可以壓到數小時到數天**,而且不只生物學。

### 重點整理

#### 規模數字與整個堆疊(約 01:02–01:07)

- 三四年前是單體 chatbot,現在是半自主/自主 agent。採用面的代表數字:Kaggle 去年秋天辦的 5-Day AI Agents Intensive 線上課程,**150 萬人報名**。
- 成本面:**agentic 任務所需的推論算力,是非 agentic 工作負載的 10 到 100 倍**。也就是採用率在漲、每次互動的複雜度也在漲。
- 結果:Google 每月處理 **3.2 quadrillion tokens**。他給的直覺換算是「一 quadrillion 大約是地球上每人一本小說」,所以 Google 每月生成的 token 約等於為全世界每個人寫三本小說。
- 要接住這個機會,堆疊由下而上是:
  1. **AI Hypercomputer**(CPU、GPU、TPU)
  2. 世界級研究與**前沿模型**
  3. **資料**——模型/agent 要做有意義的事就需要它
  4. **agentic 安全與防禦**——agent 開始做有意義的事,機會與風險同時放大
  5. **平台**——讓人能便宜、有效率地重用上述能力
  6. **端到端 agentic 解法**——真的替你做事的東西
- 「跨整個堆疊的協同最佳化」是從 AI 中榨出最大價值的必要條件。
- **TPU**:十年以上的投入,液冷與共享記憶體等創新一路累積。最新一代是 TPU v8,而且**第一次把主線拆開**——8t 給訓練、8i 給推論(他當場呼應了 Peter DeSantis 前一場的說法)。對比目前的主力世代 Ironwood:
  - 訓練側:單 pod **121 FP4 exaflops**,約為前代的 3 倍;記憶體頻寬也有 2x、4x 級的跳躍。
  - 推論側:單 pod **11.6 exaflops**,比前代跳 **10 倍**,記憶體側同樣顯著提升(因為推論需求成長極快)。
- 這些 TPU 訓練了 Gemini 家族(Pro / Flash / Flash-Lite)、影像與影片生成(Veo、Imagen)、world model(Genie)、AlphaFold、AlphaGo,以及 **AlphaChip——用來設計下一代 TPU**。「effectively TPUs designing for TPUs」。現在也有不少其他公司用 TPU 訓練自家模型。

#### Agent 平台的四個問題:build / scale / govern / optimize(約 01:07–01:09)

有了硬體與模型之後還需要平台,因為「建 agent 不是寫個 prompt 就好」。四個關鍵問題:

1. **Build**:存取各種模型、Agent Development Kit、用來建 agent 的 AI Studio。
2. **Scale**:managed runtime,讓你從單一 agent instance 擴到數百萬個 agent。
3. **Govern**:因為 agent 開始做有意義的事,需要 **agent identity、agent registry、agent gateway**,確保 agent 在正確的邊界內運作。關鍵設計:**agent 用的身分系統要和使用者分開**,因為 agent 能做的事可能超出使用者本身能做的範圍。
4. **Optimize**:上線後要靠 tracing、simulation、evaluation、observability 持續改進。

Google 自己也在這個堆疊上建東西:生物(AlphaFold、AlphaGenome)、數學(AlphaEvolve、AlphaProof)、物理與化學(GNoME、fusion 相關工作——見待確認)、氣候與永續(AlphaEarth、WeatherNext)。

實際影響的例子:
- **AlphaFold**:塑膠污染(設計能分解塑膠的酵素)、抗生素抗藥性、結構生物學;特別是**被忽視疾病**——很多疾病因為經濟誘因不足,藥廠不願投入,AlphaFold 把探索藥物設計的成本與門檻壓下來,這有實質影響。也用於瘧疾疫苗與藥物遞送。
- **AlphaEvolve**:通用最佳化器。Google 內部大量用於資料中心最佳化;外部客戶用於路徑最佳化、量子錯誤更正,以及電商改進需求預測模型——形態差異極大的應用,各自都有顯著改善。

#### 從模型到 agent 到 discovery:autonomous discovery loop(約 01:10–01:12)

隨著模型持續變強,這一切指向的是**自主發現迴圈**。以生物學為例(但框架是通用的),各個積木已經到位:

- **資料攝取**:agent 已能消化大量文獻;AlphaFold 有龐大的蛋白質資料庫,再加上實驗紀錄。
- **假說生成**:**AI co-scientist** 能辯論不同假說、生成新解法。
- **建模/模擬**:用 AlphaGenome、AlphaFold 在**數秒內**模擬假說並看到效果。
- **執行**:透過 AlphaEvolve 與 **Gemini Robotics** 跑濕實驗,資料再回饋進迴圈。

結果:**從資料輸入到產出成果、原本以年計的研究週期,可以在數小時到數天內完成**。生物學只是其中一段,這會影響幾乎所有人類發現的面向。

### 金句

> "One quadrillion is one novel per person on this earth. So in a way Google generated tokens which are equivalent to three novels for every person in this world."(約 01:03)

3.2 quadrillion tokens/月 的直覺換算。

> "It's effectively TPUs designing for TPUs."(約 01:07)

AlphaChip 用 TPU 訓練、又用來設計下一代 TPU。

> "A research cycle which used to take years … can now be done in hours and days."(約 01:12)

Autonomous discovery loop 的主張。

## English Notes

### TL;DR

- **Two curves rising together**: adoption is exploding (Kaggle's 5-Day AI Agents Intensive drew 1.5 million registrations) while **agentic tasks need 10–100× more inference compute** than non-agentic workloads. Google now processes **3.2 quadrillion tokens per month** — roughly three novels' worth of text for every person on Earth.
- **The whole stack has to be co-optimized**: AI Hypercomputer (CPUs/GPUs/TPUs) → frontier research and models → data → agentic security and defense → platform → end-to-end agentic solutions. The eighth TPU generation splits the line for the first time into **8t (training)** and **8i (inference)**: 121 FP4 exaflops per 8t pod (~3× the prior generation) and 11.6 exaflops per 8i pod (10× the prior generation).
- **The destination is an autonomous discovery loop**: ingest literature, protein databases, and experimental logs → generate and debate hypotheses with an AI co-scientist → simulate in seconds with AlphaGenome and AlphaFold → execute via AlphaEvolve and Gemini Robotics wet-lab runs → feed results back. **Research cycles that took years collapse into hours and days**, and biology is only the first example.

### Key Points

#### Scale numbers and the stack (~01:02–01:07)

- Three or four years ago the interface was a singleton chatbot; today it's semi-autonomous or autonomous agents. On the adoption side: Kaggle's 5-Day AI Agents Intensive online course last fall drew **1.5 million registrations**.
- On the cost side: an **agentic task costs 10–100× more inference compute** than a non-agentic workload. Both adoption and per-interaction complexity are climbing at once.
- The result at Google's scale: **3.2 quadrillion tokens processed per month**. His intuition pump — one quadrillion is about one novel per person on Earth, so Google's monthly output is roughly three novels for everyone alive.
- The stack that has to catch this opportunity, bottom to top:
  1. **AI Hypercomputer** — CPUs, GPUs, TPUs
  2. World-class research and **frontier models**
  3. **Data**, so models and agents can do anything meaningful
  4. **Agentic security and defense**, because meaningful agent actions create risk as well as opportunity
  5. **A platform**, so these capabilities are reusable cheaply and efficiently
  6. **End-to-end agentic solutions** that actually do things for you
- Co-optimization across the entire stack is what extracts maximum value from AI.
- **TPUs**: over ten years of investment, with innovations like liquid cooling and shared memory. The newest generation, TPU v8, **splits the line for the first time** — 8t for training, 8i for inference (he explicitly picked up DeSantis's point from the previous talk). Against Ironwood, today's workhorse generation:
  - Training: **121 FP4 exaflops per pod**, roughly 3× the previous generation, with 2× and 4× jumps in memory bandwidth.
  - Inference: **11.6 exaflops per pod**, a **10× jump**, plus significant memory-side gains — because inference demand is rising very fast.
- These TPUs train the Gemini family (Pro, Flash, Flash-Lite), image and video generation (Veo, Imagen), the Genie world model, AlphaFold, AlphaGo, and **AlphaChip, which designs the next generation of TPUs** — "effectively TPUs designing for TPUs." A number of other companies now train on TPUs as well.

#### The agent platform's four problems: build, scale, govern, optimize (~01:07–01:09)

Hardware and models aren't enough, because "building agents is not just like writing a prompt."

1. **Build** — access to all model types, the Agent Development Kit, an AI Studio for building agents.
2. **Scale** — a managed runtime that takes you from a single agent instance to millions.
3. **Govern** — as agents start doing meaningful things you need **agent identity, agent registry, and agent gateway** to keep agents inside the right confines. The key design point: **an agent's identity system is separate from the user's**, because agents can do things beyond what the user can.
4. **Optimize** — once in production, tracing, simulation, evaluation, and observability let you keep improving.

Google also builds on top of this stack: biology (AlphaFold, AlphaGenome), mathematics (AlphaEvolve, AlphaProof), physics and chemistry (GNoME and fusion work — see To Verify), climate and sustainability (AlphaEarth, WeatherNext).

Impact examples:
- **AlphaFold** in plastic pollution (designing plastic-degrading enzymes), antibiotic resistance, structural biology, and especially **neglected diseases** — conditions pharma underinvests in for lack of economic incentive, where lowering the cost and difficulty of exploring drug designs has material impact. Also malaria vaccine work and drug delivery.
- **AlphaEvolve**, a general-purpose optimizer, used heavily inside Google for data center optimization and externally for route optimization, quantum error correction, and e-commerce demand forecasting — very different application shapes, each with large improvements.

#### The autonomous discovery loop (~01:10–01:12)

As models keep improving, the building blocks assemble into a self-driving research loop. The slide used biology, but the pattern generalizes:

- **Ingestion** — agents that digest large volumes of literature, plus AlphaFold's protein database and experimental logs.
- **Hypothesis generation** — an **AI co-scientist** that debates hypotheses and generates novel solutions.
- **Modeling** — AlphaGenome and AlphaFold simulate hypotheses and show effects **in seconds**.
- **Execution** — AlphaEvolve and **Gemini Robotics** run wet-lab tests and feed the data back into the loop.

The payoff: a research cycle from data input to product outcome that used to take years can now be done in hours and days — across almost every facet of human discovery, not just biology.

### Quotes

> "One quadrillion is one novel per person on this earth. So in a way Google generated tokens which are equivalent to three novels for every person in this world." (~01:03)

How to feel 3.2 quadrillion tokens a month.

> "It's effectively TPUs designing for TPUs." (~01:07)

AlphaChip trains on TPUs and designs the next ones.

> "A research cycle which used to take years … can now be done in hours and days." (~01:12)

The claim the autonomous discovery loop rests on.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| AI Hypercomputer | Google 的整合式 AI 基礎設施(CPU / GPU / TPU) | Google's integrated AI infrastructure spanning CPUs, GPUs, TPUs | |
| TPU 8t / TPU 8i | 第八代 TPU,首次拆成訓練(8t)與推論(8i)專用晶片 | Eighth-gen TPU, first split into training (8t) and inference (8i) chips | 8t:121 FP4 exaflops/pod;8i:11.6 exaflops/pod |
| Ironwood(TPU v7) | 目前的主力世代,作為 v8 的比較基準 | Today's workhorse generation, the baseline for the v8 comparison | |
| Gemini(Pro / Flash / Flash-Lite) | Google 的前沿模型家族 | Google's frontier model family | |
| Veo / Imagen | 影片與影像生成模型 | Video and image generation models | |
| Genie | World model,他形容為「全新而令人興奮的空間」 | World model; described as a new and exciting space | |
| AlphaFold | 蛋白質結構預測;附帶大型蛋白質資料庫 | Protein structure prediction, with a large protein database | 用於塑膠污染、抗藥性、被忽視疾病、瘧疾疫苗、藥物遞送 |
| AlphaGenome | 基因體模型,用於秒級假說模擬 | Genomics model used for second-scale hypothesis simulation | |
| AlphaGo / AlphaChip | AlphaChip 用於設計下一代 TPU | AlphaChip designs the next generation of TPUs | 「TPUs designing for TPUs」 |
| AlphaEvolve | 通用最佳化器;內部用於資料中心最佳化,外部用於路徑最佳化、量子錯誤更正、需求預測 | General-purpose optimizer: data center optimization internally; route optimization, quantum error correction, demand forecasting externally | |
| AlphaProof | 數學方向的 agentic 解法 | Mathematics-side agentic solution | |
| AlphaEarth / WeatherNext | 氣候與永續;WeatherNext 為世界級天氣預測模型 | Climate and sustainability; WeatherNext is a world-class weather prediction model | |
| AI co-scientist | 能辯論假說、生成新解法的研究 agent | Research agent that debates hypotheses and generates novel solutions | |
| Gemini Robotics | 在 discovery loop 中負責執行(含濕實驗) | Executes in the discovery loop, including wet-lab runs | |
| Agent Development Kit (ADK) / AI Studio | 建 agent 的開發工具 | Developer tooling for building agents | |
| Agent identity / registry / gateway | 治理層元件;agent 身分與使用者身分分離 | Governance-layer components; agent identity is separate from the user's | |
| Kaggle 5-Day AI Agents Intensive | 2025 年 11 月與 Google 合辦的線上課程,150 萬人報名 | Online course with Google, November 2025; 1.5M registrations | <https://www.kaggle.com/learn-guide/5-day-agents> |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Sarb / Sar | Saurabh (Tiwary) |
| Vert.Ex AI | Vertex AI |
| Project Touring | Project Turing |
| C GPUs and TPUs | CPUs, GPUs and TPUs |
| Xaflops / extra flops | exaflops |
| alpha fold / alpha genome / alpha evolve / alpha earth | AlphaFold / AlphaGenome / AlphaEvolve / AlphaEarth |
| imagine | Imagen |
| VO | Veo |
| genie | Genie |
| alpha chip / alpha proof | AlphaChip / AlphaProof |
| weather next | WeatherNext |
| AI coscientists | AI co-scientist |
| genome fusion | GNoME + fusion(推測,見待確認)/ inferred, see To Verify |
| co-op optimization | co-optimization |
| agent development kit | Agent Development Kit (ADK) |

## 待確認 / To Verify

- 物理與化學那一欄的「genome fusion」:發音與語意都指向 **GNoME**(材料/化學探索)加上 DeepMind 的**核融合電漿控制**工作,但需要對照投影片確認實際列了哪些項目。/ "genome fusion" in the physics-and-chemistry column most likely means **GNoME** plus DeepMind's **fusion plasma control** work, but the slide should be checked for what was actually listed.
- TPU 8t / 8i 的其他規格(pod 晶片數、HBM 容量、互連頻寬)演講中未提;若要補充需引用 Google Cloud 官方資料。/ Other TPU 8t/8i specs (chips per pod, HBM, interconnect) weren't mentioned in the talk; cite Google Cloud material if adding them.
- 「managed runtime」「AI Studio」對應的正式產品名(可能是 Vertex AI Agent Engine / Google AI Studio),演講中只用泛稱。/ Official product names behind "managed runtime" and "AI Studio" (possibly Vertex AI Agent Engine / Google AI Studio); the talk used generic terms.
- Google「每月 3.2 quadrillion tokens」的官方出處。/ Official source for the 3.2-quadrillion-tokens-per-month figure.
