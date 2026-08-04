---
title: "Unified Orchestration System for Verifier-Free Evolution"
title_zh: "免驗證器演化的統一編排系統"
speaker: "Ben Athiwaratkun"
affiliation: "Senior Director, Core ML (Turbo), Together AI"
type: talk
stage: Compass
date: 2026-08-02
session: "Session 2: AI Systems"
video: "https://www.youtube.com/watch?v=1UrriPJRSPU&t=2513s"
video_range: "00:41:53–00:47:58"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [evolutionary-search, multi-model, cost-efficiency, arc-agi, scientific-discovery]
---

# 免驗證器演化的統一編排系統(Unified Orchestration System for Verifier-Free Evolution)

**一句話總結**:當演化式探索拿掉外部驗證器之後,單一模型會因為「熵不夠」而讓解答退化;Squeeze Evolve 的解法是**用多個異質模型跑同一條演化迴圈**——難的交給貴模型、易的交給便宜模型,同時修復多樣性與成本兩個問題,在 ARC-AGI 上以更少的演化步數維持 97.5% 準確率並顯著降低單題成本。

**One-line summary**: Strip the external verifier out of evolutionary search and a single model degrades its own solutions — it simply doesn't carry enough entropy. Squeeze Evolve's answer is to run one evolution loop across multiple heterogeneous models, routing hard solutions to expensive models and easy ones to cheap models, which fixes diversity and cost at once: 97.5% on ARC-AGI in fewer evolution steps at meaningfully lower cost per task.

## 中文筆記

### TL;DR

- **問題在「驗證器太貴」**:既有的科學/演算法探索框架多半需要外部驗證器,但在物理科學等領域,評估本身既昂貴又耗時。他們要問的是:**沒有 verification in the loop 的演化系統,上限在哪裡?順便能不能省錢?**
- **單模型演化會自己退化**:用單一模型跑演化,常常反而讓效能變差——因為一個模型的**熵與創造力就是有限**。解法是把演化迴圈變成**多模型**的,用模型異質性本身當作多樣性的來源。
- **難易分流同時買到多樣性與成本效益**:用 **token log-probability 或解答多樣性**當 fitness function,把困難的解交給昂貴模型,把「容易評估與合併」的解交給便宜模型。結果:ARC-AGI 上 10 步演化搭配強模型可達 **97.5%**、約 **$7/題**;把便宜模型混進來後,**只要 2 步演化就能保住同樣準確率**,成本降到約 $5.9/題。

### 重點整理

#### 探索迴圈的四個零件,以及 verifier 的成本問題(約 00:41:53–00:44:20)

Ben Athiwaratkun 講的是 **Squeeze Evolve**——一套用於免驗證器演化(verifier-free evolution)的多模型統一編排系統,應用場景是科學探索。

他先拆解科學探索迴圈的組成(這個拆法取自 **SkyDiscover**),有四個明確零件:

1. **Context builder**:提供問題脈絡,並把想法、指引、以及對過去失敗與成功的反思注入 prompt。
2. **Solution generator**:通常是一個 LLM,可以存取環境——例如執行程式碼,或查網路。
3. **Evaluator**:給分數、給 log、給回饋,以及必要的產出物。
4. **Solution selector**:從解答與 metadata 中挑出樣本解,送回 context builder,進入下一輪迴圈。

問題來了:**既有的探索框架大多需要外部 evaluator/verifier**。在物理科學這類領域,評估既昂貴又耗時。所以他們的研究問題是:**在沒有 verification in the loop 的情況下,演化系統的上限在哪裡?同時能不能把成本壓下來?**

#### 為什麼要多模型:單模型演化的退化(約 00:44:20–00:46:00)

演化系統的另一個典型問題是**解答退化(degradation)**(約 00:44:31)。他講得很直白:如果用**單一模型**跑演化,常常反而讓效能變差,因為**一個模型裡的熵與創造力就是有限的**。他們的解法就是:**用多個模型來處理這個多樣性問題。**

機制上,從前幾代與當代的多個解答/世代中選樣,並指派**機率式的 fitness score**。Fitness function 用的是 **token log-probability,或是解答本身的多樣性**(約 00:45:12)。

分流規則很直接:

- **困難的解 → 交給昂貴模型**(用來提升多樣性)。
- **判定為「夠容易評估與合併」的解 → 交給便宜模型**(約 00:45:47)。

這樣一來,**多樣性與成本效益同時提升**——這正是這套方法的核心設計。

#### 結果:更少步數、同樣準確率、更低成本(約 00:46:00–00:47:58)

**主要數字**(約 00:46:11):完整 pipeline 跑 **10 步演化**、搭配強模型(逐字稿聽為 Gemini 3.1 Pro),在 **ARC-AGI** 上準確率達 **97.5%**,成本約 **$7/題**。而在混入便宜模型(逐字稿聽為 Gemini 3.0 Flash)的情境下,**只要 2 步演化就能保住同樣的準確率**,成本降到約 **$5.9/題**。

**另一個有意思的觀察**:在視覺類任務上,**aggregator 階段不使用視覺元件**反而能顯著提升成本效益。圖表上那條紅色曲線是全程使用強多模態模型的情況——效能確實很高,但累積的每題成本也等比例地高。而在 Squeeze Evolve 的做法裡,結合強模型與較便宜的模型層級後,成本大幅下降,而且**在部分異質配置下甚至能勝過單模型的表現**。

最後他分享兩件落地資訊:這項工作已**整合進 NVIDIA Dynamo**(現場向 NVIDIA 致謝),並且有一個 **Claude Code plugin** 可用。

### 金句

> "If we use a single model to perform evolution, it is often the case degrading the performance, because there's only so much entropy and only so much creativeness in a single model."(約 00:44:35)

多樣性不是調參數調出來的,是靠模型異質性換來的。

> "In the scenario where we use a cheap model in the mix … we're able to retain the same accuracy with only two evolution steps."(約 00:46:25)

混入便宜模型不只是省錢,還把需要的演化步數壓下來了。

> "In the heterogeneous case we're able to outperform the single model scenario."(約 00:47:25)

異質組合的價值不只在成本,有時直接贏過最強的單一模型。

## English Notes

### TL;DR

- **The problem is that verifiers are expensive.** Existing discovery frameworks generally require an external verifier, but in domains like the physical sciences evaluation is both costly and time-consuming. Their question: **what is the upper bound of an evolution system with no verification in the loop — and can it also be cheaper?**
- **Single-model evolution degrades itself.** Running evolution with one model often makes performance *worse*, because a single model carries only so much entropy and creativity. The fix is to make the evolution loop **multi-model**, using model heterogeneity itself as the source of diversity.
- **Routing by difficulty buys diversity and cost efficiency simultaneously.** Using **token log-probabilities or solution diversity** as the fitness function, hard solutions go to expensive models and solutions easy enough to evaluate and combine go to a cheap one. Result: on ARC-AGI, 10 evolution steps with a strong model reach **97.5% at roughly $7/task**; mixing in a cheap model **retains the same accuracy in just 2 evolution steps** at about $5.9/task.

### Key Points

#### Four components of the discovery loop, and the verifier cost problem (~00:41:53–00:44:20)

Ben Athiwaratkun presented **Squeeze Evolve**, a unified multi-model orchestration system for verifier-free evolution, aimed at scientific discovery.

He opened by decomposing the discovery loop — a decomposition taken from **SkyDiscover** — into four distinct components:

1. **Context builder** — supplies problem context and injects ideas, guidance, and reflections on previous mistakes and successes into the prompt.
2. **Solution generator** — an LLM with access to environments such as code execution or web lookup.
3. **Evaluator** — provides scores, logs, feedback, and any necessary artifacts.
4. **Solution selector** — picks sample solutions from the candidates and their metadata to hand back to the context builder for the next loop.

The catch: **prior discovery frameworks generally require an external evaluator or verifier**, and in fields like the physical sciences evaluators are costly and time-consuming. Hence the research question: **what is the upper bound of an evolution system without verification in the loop, and can cost come down too?**

#### Why multiple models: the degradation problem (~00:44:20–00:46:00)

The other characteristic failure of evolution systems is **degradation of solutions** (~00:44:31). His summary was blunt: using a single model to run evolution often degrades performance, because **there is only so much entropy and only so much creativeness in a single model**. Their answer: **use multiple models to attack the diversity problem directly.**

Mechanically, multiple solutions and generations are sampled from previous and current generations and assigned probabilistic fitness scores. The fitness function uses **token log-probabilities or the diversity of the solutions themselves** (~00:45:12).

The routing rule is simple:

- **Difficult solutions → expensive models**, to raise diversity.
- **Solutions judged easy enough to evaluate and combine → a cheaper model** (~00:45:47).

That single split increases **diversity and cost effectiveness at the same time**, which is the design idea at the heart of the method.

#### Results: fewer steps, same accuracy, lower cost (~00:46:00–00:47:58)

**The headline numbers** (~00:46:11): the full pipeline with **10 evolution steps** using a strong model (heard in the captions as Gemini 3.1 Pro) reaches **97.5% accuracy on ARC-AGI** at roughly **$7 per task**. Mixing in a cheap model (heard as Gemini 3.0 Flash), they **retain the same accuracy with only 2 evolution steps** at about **$5.9 per task**.

**A second observation** concerns vision tasks: *not* using the vision component for the **aggregator stage** significantly improves cost effectiveness. The red curve on his chart shows a strong multimodal model used throughout — performance climbs high, but cumulative dollars per problem climb proportionally. Under Squeeze Evolve, combining a powerful model with a cheaper tier cuts cost substantially, and **in some heterogeneous configurations they outperform the single-model scenario outright**.

He closed with two adoption notes: the work has been **integrated into NVIDIA Dynamo** (with a shout-out to NVIDIA), and a **Claude Code plugin** is available.

### Quotes

> "If we use a single model to perform evolution, it is often the case degrading the performance, because there's only so much entropy and only so much creativeness in a single model." (~00:44:35)

Diversity isn't something you tune into a single model; you buy it with heterogeneity.

> "In the scenario where we use a cheap model in the mix … we're able to retain the same accuracy with only two evolution steps." (~00:46:25)

Mixing in the cheap model didn't just cut cost — it cut the number of evolution steps needed.

> "In the heterogeneous case we're able to outperform the single model scenario." (~00:47:25)

The heterogeneous mix isn't only cheaper; sometimes it beats the strongest single model.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Squeeze Evolve | 本演講主題:免驗證器演化的多模型統一編排系統 | The talk's subject: unified multi-model orchestration for verifier-free evolution | 已查證:arXiv 2604.07725,GitHub `squeeze-evolve/squeeze-evolve` |
| SkyDiscover | AI 驅動的科學/演算法探索框架,本講的四零件拆解取自此 | Framework for AI-driven scientific and algorithmic discovery; the four-component decomposition comes from it | 已查證:UC Berkeley Sky Lab 出品 |
| ARC-AGI | 主要評測對象;論文中為 ARC-AGI-V2 | Primary benchmark cited; the paper reports ARC-AGI-V2 | 論文載明 97.5%、$7.74/題(不含程式碼執行) |
| NVIDIA Dynamo | Squeeze Evolve 已整合進去的推論框架 | Inference framework into which Squeeze Evolve has been integrated | |
| Claude Code plugin | 現場提到的可用外掛 | Plugin mentioned as available | 逐字稿 "cloud code plug-in" |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Ben(僅名) | Ben Athiwaratkun |
| squeeze evolve | Squeeze Evolve |
| sky discover | SkyDiscover |
| verifier free | verifier-free |
| ARC AGI | ARC-AGI |
| cloud code plug-in | Claude Code plugin |
| log token probabilities | token log-probabilities(講者當場自我修正) |
| multimodel model | multimodal model |

## 待確認 / To Verify

- 演講中的模型版本:逐字稿聽為 "Gemini 3.1 Pro" 與 "Gemini 3.0 zero flash",自動字幕在版本號上錯誤率高,需看投影片確認。/ Model versions heard as "Gemini 3.1 Pro" and "Gemini 3.0 Flash" — auto-captions are unreliable on version numbers; confirm from slides.
- 講者口述成本為 $7 與 $5.9 每題,論文載明 ARC-AGI-V2 為 $7.74/題,兩者對應關係與是否為同一組實驗待確認。/ He said ~$7 and ~$5.9 per task; the paper reports $7.74/task on ARC-AGI-V2 — confirm whether these are the same experiment.
- ARC-AGI 的版本(V1 或 V2):講者只說 "ARC AGI",論文為 ARC-AGI-V2。/ ARC-AGI version — he only said "ARC AGI"; the paper uses ARC-AGI-V2.
- Claude Code plugin 的名稱與取得位置未在逐字稿中出現。/ The name and location of the Claude Code plugin never appear in the transcript.
