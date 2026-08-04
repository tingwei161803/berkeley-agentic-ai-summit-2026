---
title: "AIDaR: AI Data Readiness Evaluations Framework"
title_zh: "AIDaR:AI 資料就緒度評估框架"
speaker: "Arindam Sett"
affiliation: "Principal ML Engineer, Genentech"
type: talk
stage: Compass
date: 2026-08-02
session: "Session 4: Agent Evaluation & Benchmarks"
video: "https://www.youtube.com/watch?v=1UrriPJRSPU&t=10148s"
video_range: "02:49:08–02:54:38"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [data-readiness, evaluation, life-sciences, data-infrastructure, agentic-ai]
---

# AIDaR:AI 資料就緒度評估框架(AIDaR: AI Data Readiness Evaluations Framework)

**一句話總結**:Agent 不是在真空中運作的,它跑在一層資料之上;當你的 agent 評估分數難看,問題往往不在 prompt 也不在模型,而在那層為 dashboard 和報表而生、根本不是為 agent 準備的資料——所以評估 agent 的同時,也必須評估資料層的就緒度。
**One-line summary**: Agents don't perform in a vacuum — they run on top of a data layer. When your agent's eval scores look bad, the cause is often neither the prompt nor the model but a data layer built for dashboards and reporting rather than for agents. So evaluating agents requires evaluating data readiness alongside them.

## 中文筆記

### TL;DR

- **單一論點**:在評估 agent 的同時,**必須一併評估底層資料層的就緒度**。這是他整場只想講的一件事。
- **Genentech 的真實踩坑過程**:被要求建 agentic 系統 → 選資料集 → 工程師做兩個月 → 一跑 eval 表現很差 → 翻遍各種最佳實踐部落格、調 prompt、期待更好的模型,全都沒用。**最後才發現問題在資料層**——那層資料是為 data warehousing、報表與 dashboard 設計的,不是為 agent 設計的。
- **五個維度的評估框架**(他強調仍在演進中):data quality、semantics & metadata、access & governance、structural readiness、generalizability。其中 structural readiness 的具體反例是 **entity-attribute-value(EAV)資料模型**——對在其上跑 agent 非常不友善。

### 重點整理

#### 問題:我們調錯了東西(約 02:50–02:52)

Arindam Sett 是 Genentech 的 principal machine learning engineer,專注在 agentic AI、生命科學領域的 scientific AI、AI 資料就緒度,以及 agent 評估。

他說整場只有**一個論點**:**當我們在評估 agent 的時候,也必須評估底層資料層的就緒度。**

接著他講了一個很多人會有共鳴的過程。在 Genentech,他們被要求建立一套 agentic 系統:選定一些資料集 → ML/AI 工程師投入 → 花了幾個月把框架組起來 → **然後跑評估,表現很差**。

於是開始找原因:翻遍 LangChain 的部落格、各種框架的部落格,**該套用的最佳實踐都套用了**,還是不行;接著去調 prompt engineering,再接著期待更好的模型出現。

**最後他們才意識到:agent 不是在真空中運作的。它跑在一層資料之上,而那層資料本身也是需要被檢視的東西。**

他給的具體例子:有一個資料層,**它的取向是 dashboard 與報表**。他們在上面架了 agent,表現就是不好——回頭看才發現,**那層資料當初是為 data warehousing、報表與 dashboard 而設計的**,不是為 agent。

#### AIDaR:五個維度(約 02:52–02:53)

由此他們發展出這套 **AI 資料就緒度評估框架**(他強調目前仍在演進),包含五個維度:

| 維度 | 檢查什麼 |
|-----|---------|
| **1. Data quality** | 資料在技術上有多健全——**完整性(completeness)、一致性(consistency)、新鮮度(freshness)** |
| **2. Semantics & metadata** | 這個資料集有沒有 metadata?以 PostgreSQL 為例:**有沒有 table 與 column 的註解?有沒有一份承載該資料脈絡的說明?** |
| **3. Access & governance** | **agent 到底能不能存取到相關資料?** |
| **4. Structural readiness** | 資料模型的結構是否適合 agent。他們踩到的坑是資料模型採用了 **entity-attribute-value(EAV)** 的概念——**對在其上跑 agent 非常不利** |
| **5. Generalizability** | 這個資料層是否具有一般性、**能不能撐得住 happy path 以外的情況** |

#### 社群與 workshop(約 02:53–02:54)

他們最近有一個 **NeurIPS workshop 在 Paris 獲得接受**(他在台上順道恭喜了 Scale AI 也拿到 workshop——即前面 Chenguang Wang 提到的 Agents in the Wild)。

workshop 的目的是**把兩群人聚在一起**:正在**為 agentic AI 打造資料基礎設施**的人,以及正在**為 agentic AI 建立評估與 benchmark** 的人。

他也強調這是一項真正的協作成果——Genentech 內部、加上外部的學界、業界與社群共同促成。

### 金句

> "The agents are not performing in a vacuum. They are working on top of a data layer, and the underlying data layer is something we need to also look at."(約 02:51)

整場唯一的論點,也是他最想留下的一句。

> "We went to all the LangChain blogs … hopefully we actually applied the best practices, but it wasn't performing. Then we looked into prompt engineering, we looked for hope for the better models."(約 02:51)

evals 表現差時的標準除錯順序——而他的重點是:這個順序漏掉了最下面那一層。

## English Notes

### TL;DR

- **A single argument**: while evaluating agents, **you must also evaluate the readiness of the underlying data layer.** That was the whole talk.
- **A real Genentech failure loop**: mandated to build an agentic system → pick datasets → engineers work for a couple of months → evals come back poor → read every best-practice blog, tune prompts, hope for better models, none of it helps. **The problem turned out to be the data layer** — built for data warehousing, reporting, and dashboards, not for agents.
- **A five-dimension framework** (explicitly still evolving): data quality, semantics & metadata, access & governance, structural readiness, and generalizability. His concrete structural-readiness counterexample is an **entity-attribute-value (EAV) data model**, which is deeply unfriendly to running agents on top of it.

### Key Points

#### The problem: tuning the wrong layer (~02:50–02:52)

Sett is a principal machine learning engineer at Genentech, focused on agentic AI, scientific AI in life sciences, AI data readiness, and agent evaluations.

He said he had **one argument** for the whole talk: **as we evaluate agents, we also need to evaluate the readiness of the underlying data layer.**

Then came a sequence many in the room would recognize. At Genentech they were mandated to build an agentic system: choose some datasets, put ML and AI engineers on it, spend a couple of months assembling the framework — **and then run the evals, which came back performing poorly.**

So the hunt began. They went through the LangChain blogs and other framework blogs, **applied what they believed were the best practices**, and it still wasn't performing. Then they moved on to prompt engineering. Then to hoping for better models.

**What they realized only later: agents don't perform in a vacuum. They work on top of a data layer, and that underlying data layer is something you have to examine too.**

His concrete example: one data layer was **oriented toward dashboarding and reporting.** They put an agent on top of it and performance was poor — and looking back, that layer had been designed for **data warehousing, reporting, and dashboards**, not for agents.

#### AIDaR: the five dimensions (~02:52–02:53)

Out of that came their **AI data readiness evaluations framework** — which he was careful to describe as still evolving — with five dimensions:

| Dimension | What it checks |
|-----------|----------------|
| **1. Data quality** | How technically sound the data is: **completeness, consistency, freshness** |
| **2. Semantics & metadata** | Does the dataset have metadata? For a PostgreSQL database: **are there table and column comments, or anything carrying the context of that data?** |
| **3. Access & governance** | **Can the agent access the relevant data at all?** |
| **4. Structural readiness** | Whether the data model's shape suits agents. Their example: a data model built around the **entity-attribute-value (EAV)** pattern, which **is not conducive to running agents on top of it** |
| **5. Generalizability** | Whether the data layer generalizes — **can it go beyond the happy path?** |

#### Community and workshop (~02:53–02:54)

They recently had a **NeurIPS workshop accepted in Paris** (he paused on stage to congratulate Scale AI on their workshop too — the Agents in the Wild workshop mentioned earlier by Chenguang Wang).

The workshop's purpose is to **bring two communities together**: people **building data infrastructure for agentic AI**, and people **building evaluations and benchmarks for agentic AI.**

He closed by noting this was genuinely collaborative work — within Genentech plus academia, industry, and the outside community.

### Quotes

> "The agents are not performing in a vacuum. They are working on top of a data layer, and the underlying data layer is something we need to also look at." (~02:51)

The single claim of the talk.

> "We went to all the LangChain blogs … hopefully we actually applied the best practices, but it wasn't performing. Then we looked into prompt engineering, we looked for hope for the better models." (~02:51)

The standard debugging order when evals disappoint — and his point is that this order skips the bottom layer entirely.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| AIDaR(AI Data Readiness Evaluations Framework) | 五維度的資料就緒度評估框架,仍在演進中 | Five-dimension data readiness evaluation framework, still evolving | 講題採用 AIDaR 縮寫,但演講中他僅口述完整名稱 / the acronym appears in the agenda title; on stage he used the full name only |
| NeurIPS workshop(Paris) | 集結 agentic AI 資料基礎設施與評估/benchmark 兩個社群 | Convenes the agentic-AI data infrastructure and evaluation/benchmark communities | NeurIPS 2026 確為多地舉辦(Sydney / Atlanta / Paris),Paris 場 workshop 為 12/12–13 / NeurIPS 2026 is multi-site with Paris workshops on Dec 12–13 |
| Entity-Attribute-Value (EAV) | 被點名不利於 agent 運作的資料模型結構 | Data model pattern called out as unfriendly to agents | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| a random set / Orindam | Arindam Sett |
| Janentech / genetic / gentech | Genentech |
| agenti / agentic ro | agentic |
| langin blogs | LangChain blogs |
| new rips / newix workshop | NeurIPS workshop |
| scali | Scale (AI) |
| agency / agent uh AI data agency evaluations framework | AI data readiness evaluations framework |

## 待確認 / To Verify

- AIDaR workshop 的正式名稱與網址(他只請聽眾掃 QR code,未口述網址)。/ Official name and URL of the workshop — he pointed at a QR code without reading out the address.
- 他提到的第二類部落格來源(字幕聽作 "py blogs",可能是 PyTorch 或 LlamaIndex 等)。/ The second blog source he cited (captions give "py blogs" — possibly PyTorch, LlamaIndex, or similar).
- 五個維度的正式命名與定義是否有公開文件可對照。/ Whether the five dimensions' formal names and definitions are documented publicly.
- AIDaR 縮寫的正式展開方式(議程寫作 AI Data Readiness Evaluations Framework)。/ The official expansion of the AIDaR acronym as printed.
