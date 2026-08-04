---
title: "How Agentic AI Is Rewriting the Rules of AI Infrastructure"
title_zh: "Agentic AI 如何改寫 AI 基礎設施的規則"
speaker: "Tushar Krishna"
affiliation: "Associate Professor, Georgia Tech; CEO, InfraVana"
type: talk
stage: Compass
date: 2026-08-02
session: "Session 2: AI Systems"
video: "https://www.youtube.com/watch?v=1UrriPJRSPU&t=2883s"
video_range: "00:48:03–00:53:01"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [inference-serving, heterogeneity, benchmarking, tokenomics, full-stack]
---

# Agentic AI 如何改寫 AI 基礎設施的規則(How Agentic AI Is Rewriting the Rules of AI Infrastructure)

**一句話總結**:今天的推論服務堆疊是為 chatbot 時代造的——單模型、靜態執行路徑、請求彼此獨立、硬體同質;而 agentic 工作負載帶來的 dynamism 與 heterogeneity 讓整個堆疊出現「兆級的選擇組合」,選錯的機率極高、代價更高,唯一的出路是**跨全棧一起最佳化**,而前提是先能量測。

**One-line summary**: Today's inference serving stacks were built for the chatbot era — one model at a time, static execution paths, independent requests, homogeneous hardware — while agentic workloads bring dynamism and heterogeneity that open up trillions of cross-dependent choices where the odds of choosing wrong are high and the cost of choosing wrong is higher; the only way out is optimizing across the whole stack, which first requires being able to measure it.

## 中文筆記

### TL;DR

- **現有推論堆疊是 chatbot 時代的產物**:一次跑一個模型、為靜態執行路徑最佳化、假設每個請求彼此獨立、硬體基本同質(GPU)。Agentic 工作負載打破了每一條假設。
- **兩個不可逆的趨勢:dynamism 與 heterogeneity**。前者是多模型、tool call、動態波動的需求、互相依賴的任務、以及工作流層級的最佳化;後者是 CPU 加上各種為不同任務段最佳化的專用硬體。而 agentic 工作流的運算量比非 agentic **高出 10 到 100 倍**——所以中間那層軟體堆疊只會更關鍵。
- **兆級選擇 + 快速演化的元件 = 幾乎一定會選錯**。一端是 agent 應用在意的 end-to-end SLO,另一端是資料中心的 infra 目標,中間是跨層相依的巨大選擇空間。他的結論:**只優化堆疊的一部分不會有用,唯一的路是跨全棧最佳化**——而 "you can't optimize what you cannot measure",所以 benchmark 與模擬工具(Chakra、ASTRA-sim)是前置條件。

### 重點整理

#### Tokenomics:軟體堆疊為什麼變成瓶頸(約 00:48:03–00:49:30)

Tushar Krishna 開場先自嘲:「現在是 1:45,官方上這個 session 已經該結束了,但我身為教授的超能力就是能在 5 分鐘內衝完任意數量的投影片。」

他的框架是 **tokenomics** 的新時代(約 00:48:35):我們把 AI 工作流餵進 AI 系統,產出的是 token。於是大家開始在意 **tokens per second、tokens per watt、tokens per dollar**。在這個生態裡,一端是工作流、另一端是硬體,而**夾在中間的軟體堆疊,對 token efficiency 變得極其關鍵**。

問題是,今天在外面跑的那些推論服務堆疊,基本上都是**為 chatbot 時代打造的**(約 00:49:02),特徵很一致:

- 通常**一次只跑一個模型**;
- 針對**靜態執行路徑**做最佳化;
- 假設**每個請求彼此獨立**;
- 大量 kernel 層最佳化;
- 硬體**基本上是同質的**(絕大多數是 GPU)。

#### Agent 改變了什麼:兩個不可逆的趨勢(約 00:49:30–00:50:30)

1. **Dynamism**(約 00:49:33):多個模型、tool call、動態波動的需求、互相依賴的任務,以及大量**工作流層級**的最佳化機會。
2. **Heterogeneity**(約 00:49:49):他特別點名前面幾位講者也談得很好——現在已經大量使用 **CPU** 處理任何非 LLM 的部分,除此之外還有各式各樣為任務不同段落而特化、最佳化的硬體。

再加上一個放大係數(約 00:50:11):他引用前一天 Google 的一場演講,**agentic 工作流的運算量比非 agentic 工作流高出 10 到 100 倍**。所以中間那層軟體堆疊只會**更加關鍵**。

#### 兆級的選擇空間,以及「量不到就優化不了」(約 00:50:30–00:52:30)

把整件事拆開看:從 workload 一路往下到 model layer、software、hardware,**每一層都有大量的選擇與最佳化機會**。抽象之後,一端是 end-to-end 的 **SLO**(agent 應用在意什麼就是什麼),另一端是資料中心高效運作所需的 **infra 層目標**。

於是你面對的是:**跨層相依的空間、兆級的選擇、多樣的 SLO、以及快速演化中的元件**(約 00:51:00)。他的判斷很直接——**在這種條件下選錯幾乎是必然的,選錯的機率非常高,而選錯的代價更高。**

那要怎麼在這麼複雜的生態裡榨出 token efficiency?他引用那句名言:「**you can't optimize what you cannot measure**」(約 00:51:22)。過去多年,他與學術界和產業界密切合作,把 AI 系統從硬體到軟體到工作負載的端到端堆疊摸清楚;也與 benchmark 與標準化組織合作制定 API,讓各種 benchmark 與工具可以互換使用,並因此獲得廣泛採用。他特別點名兩個成果:

- **Chakra**(約 00:51:51):與 **MLCommons** 一起啟動的計畫,幾週前剛在 **MLSys** 發表——這是一套**針對分散式 AI 平台的 benchmark 方法論**。
- **ASTRA-sim**(約 00:52:02):研究分散式 AI 網路的**模擬平台**。

而從 hyperscaler、硬體廠商、OEM 到測試廠商,一路合作下來反覆浮現的同一個結論是:**取得效率的唯一方法是跨全棧最佳化;只優化堆疊的一部分不會有用。**

#### 收尾:InfraVana(約 00:52:30–00:53:01)

這也帶到他個人現在最興奮的事:他們剛創立 **InfraVana**,做的是一個**自動化、同時感知 agent 與硬體的全棧最佳化器**。他說相對於目前市面上最先進的推論框架,**已經看到大幅的加速**,更多細節等他們走出 stealth 再說。

最後他歡迎大家在會場找他或寫信,並「正式宣布這個 session 結束」。

### 金句

> "You can't optimize what you cannot measure."(約 00:51:22)

他整套 benchmark / 模擬工作的出發點,也是為什麼 Chakra 與 ASTRA-sim 是前置條件而不是副產品。

> "It's kind of almost inevitable that you would go wrong when you pick something, and the chances of going wrong are actually very high and the cost of going wrong is even higher."(約 00:51:05)

兆級選擇空間裡,「選對」不是靠經驗,而必須靠系統化的搜尋與量測。

> "The only way to get efficiency is optimizing across the stack — optimizing just parts of the stack will not work."(約 00:52:15)

從 hyperscaler 到 OEM 一致回饋的結論,也是 InfraVana 的立論基礎。

## English Notes

### TL;DR

- **Today's inference stacks are chatbot-era artifacts**: one model at a time, optimized for static execution paths, each request assumed independent, hardware essentially homogeneous. Agentic workloads break every one of those assumptions.
- **Two inevitable trends: dynamism and heterogeneity.** Dynamism means many models, tool calls, fluctuating demand, interdependent tasks, and workflow-level optimization; heterogeneity means CPUs plus a growing set of hardware specialized for different parts of the task. And agentic workflows involve **10–100× more computation** than non-agentic ones — which makes the middle software layer more decisive, not less.
- **Trillions of choices plus rapidly evolving components means you will pick wrong.** End-to-end SLOs on one side, infrastructure objectives on the other, and a cross-dependent choice space in between. His conclusion: **optimizing parts of the stack will not work; only full-stack optimization does** — and since "you can't optimize what you cannot measure," benchmarking and simulation tooling (Chakra, ASTRA-sim) are prerequisites rather than by-products.

### Key Points

#### Tokenomics and why the software stack became the bottleneck (~00:48:03–00:49:30)

Krishna opened by acknowledging the clock: "We're at 1:45, I know it's officially the end of this session — my superpower as a professor is I can rush through any number of slides in 5 minutes."

His frame is the era of **tokenomics** (~00:48:35): we feed AI workflows into AI systems and tokens come out, so the metrics that matter have become **tokens per second, tokens per watt, tokens per dollar**. In an ecosystem with a workflow on one end and hardware on the other, **the software stack in the middle becomes crucial to token efficiency**.

The problem is that most inference serving stacks in production today were built **for the chatbot era** (~00:49:02), and share a consistent profile:

- typically **one model at a time**;
- optimized for **static execution paths**;
- each request assumed **independent**;
- heavy kernel-level optimization;
- **primarily homogeneous hardware** — GPUs, for the most part.

#### What agents change: two inevitable trends (~00:49:30–00:50:30)

1. **Dynamism** (~00:49:33): many models, tool calls, dynamically fluctuating demand, interdependent tasks, and a lot of **workflow-level** optimization opportunity.
2. **Heterogeneity** (~00:49:49): he credited earlier speakers for covering this well — there is already heavy use of **CPUs** for anything that isn't an LLM, plus a range of hardware specialized and optimized for different parts of the task.

Then the amplifier (~00:50:11): citing a Google talk from the previous day, **agentic workflows involve 10–100× more computation** than non-agentic ones. Which makes the software stack in the middle matter even more.

#### Trillions of choices, and "you can't optimize what you cannot measure" (~00:50:30–00:52:30)

Demystify the picture and you find, all the way down from workload to model layer to software to hardware, **enormous numbers of choices and optimization opportunities at every level**. Abstracted, one end is end-to-end **SLOs** — whatever the agent application cares about — and the other is **infrastructure-level objectives** for running data centers efficiently.

What you actually face is a **cross-dependent space, trillions of choices, diverse SLOs, and rapidly evolving components** (~00:51:00). His read is blunt: under those conditions **going wrong is close to inevitable, the chances of going wrong are very high, and the cost of going wrong is higher still.**

So how do you extract token efficiency from that ecosystem? He reached for the standard line: **"You can't optimize what you cannot measure"** (~00:51:22). Over many years he has worked with academic and industry partners to understand the end-to-end AI systems stack from hardware to software to workloads, and worked closely with benchmarking and standardization bodies to define APIs so that benchmarks and tools interoperate — which has driven wide adoption. Two results he called out:

- **Chakra** (~00:51:51), an initiative started with **MLCommons** and released a few weeks earlier at **MLSys**: a benchmarking methodology for distributed AI platforms.
- **ASTRA-sim** (~00:52:02): a simulation platform for studying distributed AI networks.

Across everyone he has worked with — hyperscalers, hardware vendors, OEMs, test vendors — the same finding keeps surfacing: **the only way to get efficiency is optimizing across the stack; optimizing just parts of it will not work.**

#### Closing: InfraVana (~00:52:30–00:53:01)

That leads to what he is personally most excited about: they have just started **InfraVana**, building an automated, **agent-aware and hardware-aware full-stack optimizer**. He reports already seeing massive speedups over state-of-the-art inference frameworks, with more to come once they emerge from stealth.

He closed by inviting questions at the conference or by email, and officially called the session to a close.

### Quotes

> "You can't optimize what you cannot measure." (~00:51:22)

The premise behind all of his benchmarking and simulation work, and why Chakra and ASTRA-sim are prerequisites rather than side projects.

> "It's kind of almost inevitable that you would go wrong when you pick something, and the chances of going wrong are actually very high and the cost of going wrong is even higher." (~00:51:05)

In a trillion-choice space, picking correctly stops being a matter of experience and becomes a matter of systematic search and measurement.

> "The only way to get efficiency is optimizing across the stack — optimizing just parts of the stack will not work." (~00:52:15)

The consistent finding from hyperscalers through OEMs, and the thesis InfraVana is built on.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Chakra (MLCommons) | 分散式 AI 平台的 benchmark 方法論,以標準化 execution trace 為核心 | Benchmarking methodology for distributed AI platforms, built on standardized execution traces | 已查證:MLCommons Chakra,2026 年 5 月 MLSys 發表(arXiv 2605.11333) |
| ASTRA-sim | 研究分散式 AI 網路的開源模擬平台,原生支援 Chakra trace | Open-source simulator for distributed AI networks, with native support for Chakra traces | 已查證:Georgia Tech 主導的分散式 AI 模擬器 |
| InfraVana | 講者新創:自動化、agent 與硬體雙感知的全棧最佳化器 | His new company: an automated, agent-aware and hardware-aware full-stack optimizer | 演講時仍在 stealth,公開資料有限 / still in stealth, little public information |
| Tokenomics | 用來描述「工作流進、token 出」的新時代與其指標體系 | Framing for the "workflows in, tokens out" era and its metrics | tokens/second、tokens/watt、tokens/dollar |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Duchar Krishna | Tushar Krishna |
| Infana / Infraana | InfraVana |
| tokconomics | tokenomics |
| hetrogenity | heterogeneity |
| Astrasim | ASTRA-sim |
| MLS | MLSys |
| SLOs's | SLOs |
| cross-d dependent | cross-dependent |

## 待確認 / To Verify

- 「agentic 工作流比非 agentic 多 10–100 倍運算量」的來源:講者說是前一天 Google 的一場演講,未指明講者或場次。/ Source for the 10–100× compute claim — he attributed it to a Google talk the previous day without naming the speaker or session.
- 「已看到相對於 state-of-the-art 推論框架的大幅加速」未給具體數字或對照對象。/ No concrete numbers or named baselines for InfraVana's claimed speedups.
- 演講中提到「幾週前在 MLSys 發表 Chakra」——需確認指的是 Chakra 的哪一版或哪一篇成果。/ Which Chakra release or paper the MLSys mention refers to.
