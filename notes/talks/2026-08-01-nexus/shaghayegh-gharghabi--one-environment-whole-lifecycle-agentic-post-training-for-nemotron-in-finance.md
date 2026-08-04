---
title: "One Environment, Whole Lifecycle: Agentic Post-Training for Nemotron in Finance"
title_zh: "同一個環境貫穿整個生命週期:Nemotron 金融領域的 Agentic 後訓練"
speaker: "Shaghayegh Gharghabi"
affiliation: "Deep Learning Scientist, NVIDIA"
type: talk
stage: Nexus
date: 2026-08-01
session: "Session 3: Agentic AI in Finance & Healthcare"
video: "https://www.youtube.com/watch?v=ZIRc3EpzQJs&t=8603s"
video_range: "02:23:23–02:30:45"
transcript: "tmp/[English (auto-generated)] Nexus Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [finance, post-training, synthetic-data, nemotron, open-source]
---

# 同一個環境貫穿整個生命週期:Nemotron 金融領域的 Agentic 後訓練(One Environment, Whole Lifecycle: Agentic Post-Training for Nemotron in Finance)

**一句話總結**:NVIDIA 金融推理團隊要開源的不是一個 checkpoint,而是整條後訓練流水線——而且合成資料生成、SFT 與 RL 全部跑在**同一個環境、同一套工具與格式**上,把「訓練與推論不一致」這個問題從架構層消掉。
**One-line summary**: NVIDIA's finance reasoning team is open-sourcing not a checkpoint but the whole post-training pipeline — and by running synthetic data generation, SFT, and RL inside **one shared environment with the same tools and the same format**, they design the train/inference mismatch problem out of existence.

## 中文筆記

### TL;DR

- **要開源的是整條流水線,不是模型權重**:資料、SDG recipe、訓練 recipe、環境、orchestration 全部公開,讓別人能自己再生成資料、再訓一次。
- **金融任務難在「多輪 + 工具 + 長文件 + 數學 + 引用」全都要**:一題「算 US Steel 2024 年的存貨周轉率」就要求模型知道公式、知道去 SEC 抓哪一份表單、看懂結構化與非結構化混雜的長文件、做財務計算,最後還要**指出答案根據文件的哪一段**。現況是最佳閉源模型約 64%、開源約 60%,更難的新 benchmark 上最佳僅 58%。
- **關鍵設計是「單一共用環境」**:SDG、SFT、RL 共用同一組工具與同一種格式,不必再操心一致性。成果是 Qwen 系列微調後約 +11%、Nemotron 約 +7%,且在不損失準確度的前提下**少用 25% token**。

### 重點整理

#### 目標:開源的是「orchestra」而不是 checkpoint(約 02:23–02:25)

講者所屬團隊在 NVIDIA 做的是**金融領域推理模型的後訓練**,底座是 Nemotron。她開場就把目標講清楚:目標是釋出一個做金融推理的開源模型,但**「不只是分享一個 checkpoint 讓大家載下來跑」**——要分享的是整條 pipeline:資料公開、生成資料用的 recipe 與 pipeline 公開、模型公開、環境公開。用她的話說,是把整個過程的「orchestra」都交出來,讓別人可以用他們的 recipe 自己生資料。

#### 為什麼金融特別難:一題存貨周轉率的拆解(約 02:25–02:27)

金融問題要答對,模型得走完一整條 **multi-turn reasoning**:呼叫多個工具、做網頁搜尋、抓取不同的 SEC filing;而這些檔案又長又複雜,結構化與非結構化資料混在一起。模型不只要讀懂,還要**在這些文件上做財務數學**,最後**引用文件中哪一段支撐了答案**。

她用的例子是:**「計算 US Steel 2024 年的存貨周轉率(inventory turnover)」**。模型必須:

1. 知道 turnover 的計算公式;
2. 判斷需要哪一種 filing、哪一份表單,以及該從哪個工具(web、SEC)取得;
3. 呼叫後對文件做抽取與理解;
4. 套公式算出結果;
5. **引用**——指出是文件的哪一部分支持這個答案,才能確認答案有據可查。

現況數字說明差距有多大:在一個近期發布的知名金融 benchmark 上,**最佳閉源模型約 64%,開源模型只有約 60%**;而在更近期發布、更複雜的金融 benchmark 上,**目前最佳表現只有 58%**。

#### 四項貢獻與成效(約 02:27–02:29)

她把團隊貢獻歸成四根柱子:

1. **兩條 SDG(合成資料生成)pipeline**:document-based SDG 與 template-based SDG。
2. **公開資料**:超過 **100 萬筆**資料,現在就可以取用。
3. **用自家資料訓練模型**:走 SFT recipe 與 RL recipe,模型表現有明顯提升。
4. **Pipeline 原生支援帶 tool calling 的 RL 微調**,而且全部在同一條 pipeline 裡。

此外她提到已有**兩家金融機構客戶**在用。金融資料的安全性是硬需求,而這條 pipeline**可以完全離線執行、不需連網**,已達 enterprise-ready。

成效數字:用他們的資料與 pipeline 微調後,**Qwen 系列模型約提升 11%,Nemotron 約提升 7%**;而且在**不損失準確度**的前提下,**token 用量減少 25%**——她的註解是 "less token, less cost, better life"。

#### 核心設計:單一共用環境(約 02:28–02:29)

整條流程由 **NVFlow** 統一編排:合成資料生成、模型微調、評估、RL 訓練都在同一條 pipeline 上完成。

而她特別點名團隊做的一個**重要決定**:**shared single environment**。意思是 SDG、SFT、RL 三個階段全部使用**同一組工具、同一種格式**,因此不必再擔心各階段之間的一致性問題。這正是講題「One Environment, Whole Lifecycle」的意思。

收尾是邀請合作:程式碼與資料全部公開,歡迎聯繫。

### 金句

> "It's not just sharing a checkpoint so everyone can load it and run the model — but we want to share the whole pipeline."(約 02:24)

開源的單位從「模型」提升到「流程」。

> "All the synthetic data generation, SFT tuning, RL tuning — all of them use the same tools, same format. So no need to be worried about being consistent."(約 02:29)

一致性不是靠紀律維持,而是靠架構保證。

## English Notes

### TL;DR

- **The artifact being open-sourced is the pipeline, not the weights**: the data, the SDG recipes, the training recipes, the environment, and the orchestration are all released so others can regenerate the data and retrain themselves.
- **Finance is hard because it demands everything at once** — multi-turn reasoning, tool calls, long mixed structured/unstructured filings, financial math, and a citation back to the supporting passage. A question like "calculate the inventory turnover for US Steel in 2024" exercises all five. Today the best closed model sits around 64% and open models around 60%; on a newer, harder finance benchmark the best result is only 58%.
- **The load-bearing design choice is one shared environment**: SDG, SFT, and RL all run against the same tools in the same format, so consistency is structural rather than a discipline problem. Result: roughly +11% on Qwen models and +7% on Nemotron after fine-tuning, with **25% fewer tokens** at no accuracy cost.

### Key Points

#### The goal: releasing the orchestra, not a checkpoint (~02:23–02:25)

Gharghabi's team at NVIDIA works on **post-training reasoning models for finance** on top of Nemotron. She set the goal out front: release an open-source model that does financial reasoning — but explicitly **not just a checkpoint that people load and run**. The whole pipeline goes out: open data, the recipe and pipeline used to generate that data, the model, and the environment. Her framing was that they want to share the entire "orchestra" of the process, so that others can generate their own data using the same recipe.

#### Why finance is genuinely hard: unpacking one inventory-turnover question (~02:25–02:27)

Answering a finance question correctly requires a full **multi-turn reasoning** trajectory: calling multiple tools, running web search, retrieving different SEC filings. Those filings are long and complex, mixing structured and unstructured content. The model must not only read them but perform **financial math** over them, and then **cite which part of the document supported the answer**.

Her worked example: **"calculate the inventory turnover for US Steel in 2024."** The model has to know the turnover formula; identify which filing and which form it needs, and from which tool (web, SEC); extract and understand the retrieved documents; compute the formula; and cite the supporting evidence so the answer can be confirmed as grounded.

The gap to close is large. On a well-known recently released finance benchmark, the **best closed model reaches roughly 64%** and the **best open-source model roughly 60%**. On a newer, more complicated finance benchmark, the **best current performance is only 58%**.

#### Four contributions and the numbers (~02:27–02:29)

She grouped the team's work into four pillars:

1. **Two synthetic data generation (SDG) pipelines**: document-based SDG and template-based SDG.
2. **Publicly released data**: more than **one million** samples, available now.
3. **Models trained on that data** using their own SFT and RL recipes, with substantial measured improvement.
4. **RL fine-tuning with tool calling supported natively**, all inside the same pipeline.

She also noted **two financial-institution customers** already using it. Security is a hard requirement for finance data, and the pipeline **runs entirely without internet access**, which she described as enterprise-ready.

Results: fine-tuning with their data and pipeline gave roughly **+11% on Qwen models and +7% on Nemotron models**, and — without losing accuracy — **25% lower token usage**. Her gloss: "less token, less cost, better life."

#### The core design: one shared environment (~02:28–02:29)

Everything is orchestrated under **NVFlow**: synthetic data generation, model fine-tuning, evaluation, and RL training all run through a single pipeline.

The decision she singled out as important is the **shared single environment**: SDG, SFT, and RL tuning all use **the same tools and the same format**, so there is nothing to keep manually in sync. That is exactly what the talk title means by "One Environment, Whole Lifecycle."

She closed with an invitation to collaborate — code and data are all public.

### Quotes

> "It's not just sharing a checkpoint so everyone can load it and run the model — but we want to share the whole pipeline." (~02:24)

The unit of open-sourcing moves from the model to the process.

> "All the synthetic data generation, SFT tuning, RL tuning — all of them use the same tools, same format. So no need to be worried about being consistent." (~02:29)

Consistency enforced by architecture rather than by discipline.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Nemotron | NVIDIA 的開源模型家族,本演講後訓練工作的底座 | NVIDIA's open model family; the base for this post-training work | <https://github.com/NVIDIA-NeMo/Nemotron> |
| NVFlow | 端到端編排 SDG → 訓練(SFT/RL)→ 評估的工作流框架,建於 NeMo 生態系之上 | Workflow orchestration framework for end-to-end SDG, training (SFT/RL), and evaluation, built on the NeMo ecosystem | 字幕聽為 "NV flow";<https://github.com/NVIDIA/nvflow> 上有 finance recipe |
| Document-based SDG / Template-based SDG | 團隊釋出的兩條合成資料生成 pipeline | The team's two synthetic data generation pipelines | 貢獻四柱之一 / first of the four pillars |
| 金融後訓練資料集 / finance post-training dataset | 超過 100 萬筆公開資料 | Over one million publicly released samples | 確切資料集名稱與連結待確認 / exact dataset name and link to verify |
| Shared single environment | SDG / SFT / RL 共用同一組工具與格式的設計決策 | Design decision: SDG, SFT, and RL share the same tools and format | 講題核心 / the talk's central claim |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Shia Gagabi / Gaggabi | Shaghayegh Gharghabi |
| neotron / neos model | Nemotron |
| coin model | Qwen model |
| SG / two SG pipeline | SDG(synthetic data generation)|
| SFD recipe | SFT recipe |
| oral training | RL training |
| NV flow | NVFlow |
| multi-term reasoning | multi-turn reasoning |
| sec filing | SEC filing |
| site / cite 混用 | cite |

## 待確認 / To Verify

- 演講引用的兩個金融 benchmark 名稱(最佳閉源 64% / 開源 60%;更難的那個最佳 58%)——逐字稿只說「one of the famous benchmark」,未報名稱。/ Names of the two finance benchmarks cited (64%/60%, and the harder one at 58%) — the transcript says only "one of the famous benchmark".
- 100 萬筆以上公開資料集的正式名稱與 Hugging Face 連結。/ Official name and Hugging Face link for the 1M+ sample dataset.
- +11%(Qwen)/ +7%(Nemotron)的具體模型尺寸與評測基準未說明。/ The exact model sizes and evaluation benchmark behind the +11% / +7% figures.
- 兩家金融機構客戶未具名。/ The two financial-institution customers were not named.
