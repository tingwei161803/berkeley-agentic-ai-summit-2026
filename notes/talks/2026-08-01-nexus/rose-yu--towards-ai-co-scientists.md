---
title: "Towards AI Co-Scientists: Agentic AI for Scientific Discovery"
title_zh: "邁向 AI 共同科學家:用 Agentic AI 做科學發現"
speaker: "Rose Yu"
affiliation: "Professor, UC San Diego; CEO/Co-Founder, GistFlow"
type: talk
stage: Nexus
date: 2026-08-01
session: "Session 1: AI for Science"
video: "https://www.youtube.com/watch?v=LB7IkZhEYic&t=4285s"
video_range: "01:11:25–01:20:09"
transcript: "tmp/[English (auto-generated)] Nexus Stage - August 1st - Morning Session [DownSub.com].srt"
status: draft
tags: [ai-for-science, physics-guided-ai, climate, uncertainty-calibration, formal-methods]
---

# 邁向 AI 共同科學家:用 Agentic AI 做科學發現(Towards AI Co-Scientists: Agentic AI for Scientific Discovery)

**一句話總結**:物理世界一次打破了 agentic 系統的三個基本假設——工具很貴、環境有守恆律、事件稀有且高度不確定;Rose Yu 的解法是把物理定律直接寫進 agent 的推理引擎,做出能自適應地在「內部推理」與「跑幾天的模擬」之間切換的科學家。
**One-line summary**: The physical world breaks three assumptions agentic systems are built on at once — tools are expensive, environments obey conservation laws, and the interesting events are rare and highly uncertain — so Yu grounds agents in physical law and lets them adaptively trade internal reasoning against simulations that take days.

## 中文筆記

### TL;DR

- **問題設定**:要的不是 chatbot,而是能在物理宇宙裡推理、並帶出開放式發現的研究夥伴。
- **物理世界打破的三個假設**:(1) 有物理定律、對稱性、守恆律要當 guardrail;(2) 模擬昂貴到要跑幾天甚至幾週,可是它偏偏就是驗證 agent 用的 world model;(3) 真正有意思的事件稀有且不確定性巨大,agent 說「100% 會下雨」時就得真的是 100%。
- **配方叫 physics-guided AI**(她在 PNAS 寫過一篇論文闡述):把微分方程(模擬的建構單元)與對稱性(物理宇宙的支配原則)當成 agent 的接地,再把它們接進開放式的 agentic 推理迴圈。
- **成果橫跨四個領域**:氣候問答準確率 2×;用 Lean 與 Isabelle 的形式化驗證器拿下 PutnamBench 第一(把解題率從 50% 推到 70%,勝過 ByteDance 的專有系統);分子動力學評估下的藥物設計結合能改善 18–35%;以及首個 agentic 天氣科學家,把氣象學家兩週的分析壓到幾小時。

### 重點整理

#### 三個被物理世界打破的假設(約 01:12–01:15)

她的實驗室(UC San Diego 的 spatiotemporal machine learning lab)做的是**物理世界的機器學習演算法**。過去幾年一直困擾她的問題是:**怎麼做出真正能幫你做研究的 AI co-scientist——不是 chatbot,而是能在物理宇宙裡推理、進而導向開放式發現的夥伴?**

要回答這題,得先看清楚「AI for science 遇上物理世界」有什麼獨有的難處:

1. **物理定律、對稱性、守恆律**。這些東西在物理世界裡是硬約束,問題是怎麼把這類 guardrail 建進現在的 agentic 系統。
2. **模擬非常昂貴**。物理科學常用第一原理數學模型建出的模擬:模擬 50 年後的氣候變遷、模擬疾病在數十億人口中的傳播、模擬材料或生物系統裡原子之間的交互作用。這些**動輒跑幾天甚至幾週才拿得到回饋**——可是當我們想用這類模擬當 world model 來驗證 agent 時,agent 要怎麼跟這種環境互動?
3. **稀有事件與不確定性**。真正有用、有意思的事件通常是稀有的,而且帶著巨大的不確定性。**怎麼把這種不確定性校準好,讓 agent 說「我 100% 確定明天會下雨」的時候,它真的就是 100% 正確?**

她的判斷是:**這三件事全都打破了我們對 agentic 系統的常見假設**。

由此推導出需求:agent 要能在**內部推理**與**可能跑好幾天的昂貴模擬**之間自適應地來回切換;要把物理定律**烘進推理引擎**裡;還要能正確校準不確定性。做法上就是自適應的 tool use,加上把形式化推理工具整合進可驗證的環境。

#### Physics-guided AI:配方與成果(約 01:15–01:18)

她把這幾年累積下來的做法稱為 **physics-guided AI**,並在 **PNAS** 寫了一篇論文闡述她認為正確的路線:**用物理定律為 agent 接地**。具體的接地素材有兩類——**微分方程**(模擬的建構單元)與**對稱性**(物理宇宙的支配原則);把它們接進開放式的 agentic 推理迴圈。

她說這個配方確實有效,並列了幾個已經在做的領域:

- **氣候科學**:為理解氣候變遷衝擊而建的 AI scientist,用自適應推理迴圈讓 agent 在**很快的記憶檢索**與**很貴的氣候模式推估**之間做取捨,結果在氣候相關推理任務上得到 **2 倍準確的問答結果**。
- **形式化數學**:建立能運用 **Lean** 與 **Isabelle** 中形式方法的 verifier 來接地推理引擎、證明數學定理。他們在 **PutnamBench**(最難的形式化定理證明 benchmark 之一)拿到**第一名**,把解題率從 **50% 推到 70%**,勝過 ByteDance 的專有解法。
- **藥物設計**:由分子動力學模擬器評估的設計,結合能(binding energy)**改善 18–35%**。

**具體案例:agentic 天氣科學家。** 她展示了一個叫「Deferris」(拼寫待確認)的 agent,定位是**第一個 agentic 天氣科學家**。它能讀進龐大且高度數值化的氣象資料、在**平行程式執行環境**中生成並執行程式碼、編排從氣候模擬器到天氣預報器的一整排工具,最後寫出一份報告來理解野火、地震等極端事件的衝擊。**這種分析氣象科學家通常要做上幾週,agent 幾個小時就完成。**

#### 從實驗室到實體經濟(約 01:18–01:20)

最近他們投入不少研究在為實體科學打造「物理接地」的 agent,而現在要把它帶進真實世界:她創辦了一家新創(她本人擔任 CEO),把同一套配方從實驗室搬到物理世界,部署能自動做**預測、模擬、what-if 情境與可行動洞見**的 agent,用來支撐**供應鏈與營運**——她稱之為實體經濟的關鍵基礎建設。

demo 的問法是純自然語言:假設你是晶片製造商,**如果颱風打中東南亞,我們該怎麼理解它對航運路線與交貨前置時間的衝擊,又該怎麼最佳化與緩解對業務的潛在中斷?** agent 會做自適應研究找出所有受影響的航線,估算對前置時間與到貨的中斷程度,並在**幾小時內**給出緩解方案。

### 金句

> "How can we build an AI co-scientist that actually helps you with research, not as chatbot but as partners that can reason in a physical universe and then lead to open-ended discoveries?"(約 01:12:48)

整場的問題陳述:夥伴,不是聊天機器人。

> "…when the agent says I'm 100% sure that tomorrow is going to rain, then we know it's actually 100% correct."(約 01:14)

物理世界對 agent 的額外要求:不只要答對,還要把「有多確定」講對。

## English Notes

### TL;DR

- **The framing**: not a chatbot, but a research partner that can reason inside a physical universe and lead to open-ended discovery.
- **Three assumptions the physical world breaks**: (1) there are laws of physics, symmetries, and conservation laws that must act as guardrails; (2) simulations are so expensive they run for days or weeks — and yet they're exactly the world models you'd use to verify an agent; (3) the interesting events are rare and carry enormous uncertainty, so when an agent says it's 100% sure it will rain, that had better be true.
- **The recipe is physics-guided AI**, described in her PNAS paper: ground agents in differential equations (the building blocks of simulations) and symmetries (the governing principles of the physical universe), then loop that grounding into open-ended agentic reasoning.
- **Results across four areas**: 2× more accurate climate question answering; #1 on PutnamBench using Lean and Isabelle verifiers, lifting solve rate from 50% to 70% and beating ByteDance's proprietary solution; 18–35% better binding energies in drug design under molecular dynamics evaluation; and the first agentic weather scientist, compressing a couple of weeks of analysis into a couple of hours.

### Key Points

#### Three broken assumptions (~01:12–01:15)

Yu directs the spatiotemporal machine learning lab at UC San Diego, building machine learning algorithms for the physical world. The question that's been nagging at her for years: **how do you build an AI co-scientist that genuinely helps with research — not as a chatbot, but as a partner that can reason in a physical universe and lead to open-ended discoveries?**

Answering it means being clear about what makes AI for science distinctive once the physical universe is involved:

1. **Laws of physics, symmetries, and conservation laws.** These are hard constraints in the physical world, and the question is how to build that kind of guardrail into today's agentic systems.
2. **Simulations are expensive.** Physical sciences lean on simulations built from first-principles mathematical models — how climate changes over 50 years, how a disease spreads through billions of people, how atoms interact in materials and biological systems. These **take days or weeks to return feedback**, and yet they're precisely what you'd want as the world model for verifying an agent. How does an agent interact with an environment like that?
3. **Rare events and uncertainty.** The events worth caring about are rare and carry enormous uncertainty. **How do you calibrate that uncertainty so that when an agent says it's 100% sure it will rain tomorrow, it's actually 100% correct?**

All three, she argues, **break the common assumptions behind agentic systems**.

What follows is a requirements list: agents that adaptively interleave **internal reasoning** with **simulations that may run for days**; laws of physics baked into the reasoning engine; properly calibrated uncertainty. In practice that means adaptive tool use plus integrating formal reasoning tools into a verifiable environment.

#### Physics-guided AI: the recipe and the results (~01:15–01:18)

She calls the recipe her group has built up over the years **physics-guided AI**, and wrote a **PNAS** paper laying out what she takes to be the right approach: **ground agents in the laws of physics**. Two grounding substrates — **differential equations**, the building blocks of simulations, and **symmetries**, the governing principles of the physical universe — looped into open-ended agentic reasoning.

The recipe works, and she ran through where:

- **Climate science**: an AI scientist for understanding climate change impacts uses an adaptive reasoning loop so the agent can trade **fast retrieval from memory** against **expensive climate model projections**, producing **2× more accurate** question-answering results on climate reasoning tasks.
- **Formal mathematics**: verifiers leveraging formal methods in **Lean** and **Isabelle** ground the reasoning engine for theorem proving. They ranked **#1 on PutnamBench**, one of the hardest formal theorem-proving benchmarks, lifting solve rate **from 50% to 70%** and beating ByteDance's proprietary solution.
- **Drug design**: designs evaluated by molecular dynamics simulators showed **18–35% more favorable binding energies**.

**The concrete example: an agentic weather scientist.** She showed an agent — transcribed as "Deferris," spelling unconfirmed — billed as **the first agentic weather scientist**. It reads huge volumes of highly numerical weather data, generates and runs code in a **parallel code execution environment**, orchestrates a wide range of tools from climate simulators to weather forecasters, and writes a report on the impact of extreme events like wildfires and earthquakes. **Analysis that typically takes weather scientists a couple of weeks now takes a couple of hours.**

#### From the lab to the physical economy (~01:18–01:20)

Having done a lot of research on physics-grounded agents for physical science, they now want to take it to the real world. She has launched a startup — she's the CEO — applying the same recipe outside the lab: deploying agents that automatically produce **forecasting, simulation, what-if scenarios, and actionable insights** to support **supply chain and operations**, which she frames as the critical infrastructure of the physical economy.

The demo query is plain natural language. Imagine you're a chip manufacturer: **if a typhoon hits Southeast Asia, how should we understand the impact on shipping lanes and lead times, and how do we optimize and mitigate the potential disruptions to the business?** The agent runs adaptive research to find every affected lane, estimates the disruption to lead-time arrival, and produces a mitigation plan **in a couple of hours**.

### Quotes

> "How can we build an AI co-scientist that actually helps you with research, not as chatbot but as partners that can reason in a physical universe and then lead to open-ended discoveries?" (~01:12:48)

The framing for the whole talk: a partner, not a chat interface.

> "…when the agent says I'm 100% sure that tomorrow is going to rain, then we know it's actually 100% correct." (~01:14)

The physical world's extra demand: be right about how confident you are, not just about the answer.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Physics-guided AI | 用微分方程與對稱性為 agent 接地的整體配方 | Overall recipe for grounding agents in differential equations and symmetries | 她在 PNAS 發表論文闡述 / laid out in her PNAS paper |
| 氣候 AI scientist / climate AI scientist | 自適應在記憶檢索與昂貴氣候模式推估之間取捨 | Adaptively trades memory retrieval against expensive climate model projections | 氣候推理問答準確率 2× / 2× accuracy on climate reasoning QA |
| PutnamBench(Lean / Isabelle verifier) | 以形式方法接地推理引擎解數學定理 | Grounding the reasoning engine with formal-method verifiers to prove theorems | 第一名,解題率 50% → 70%,勝過 ByteDance 專有系統 / ranked #1, 50% → 70%, beating ByteDance's proprietary solution |
| Agentic 天氣科學家 / agentic weather scientist | 讀氣象資料、平行執行程式、編排氣候模擬器與預報器,產出極端事件衝擊報告 | Reads weather data, runs code in parallel, orchestrates simulators and forecasters, writes extreme-event impact reports | 逐字稿作 "Deferris",拼寫待確認;兩週 → 幾小時 / name unconfirmed; weeks → hours |
| GistFlow(她的新創 / her startup) | 把 physics-guided agent 帶到供應鏈與營運:預測、模擬、what-if、可行動洞見 | Brings physics-guided agents to supply chain and operations: forecasting, simulation, what-if, actionable insight | 公司名依官網議程;逐字稿聽作 "Just Flow" / company name per the official agenda; heard as "Just Flow" |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Just Flow | GistFlow |
| spatial temporal machineing lab | spatiotemporal machine learning lab |
| ling and Isabel | Lean and Isabelle |
| putnam bench | PutnamBench |
| bidance | ByteDance |
| PNAS National Science of Academy | PNAS(Proceedings of the National Academy of Sciences) |
| a gentic / gentic system | agentic system |
| shipping lengths | shipping lanes |

## 待確認 / To Verify

- **天氣 agent 的名稱**:逐字稿作 "Deferris",查不到對應專案,拼寫與正式名稱待確認。/ The weather agent's name, transcribed as "Deferris," could not be matched to any public project.
- **PNAS 論文**的正式標題與年份未提及。/ The PNAS paper's title and year weren't given.
- **PutnamBench 排名**(50% → 70%、勝過 ByteDance)的排行榜快照時間點未說明,無法核對。/ The PutnamBench leaderboard snapshot behind the 50% → 70% claim wasn't dated, so it couldn't be checked.
- **藥物設計 18–35% 結合能改善**的比較基線未指明。/ The baseline for the 18–35% binding-energy improvement wasn't specified.
- **GistFlow** 的產品名稱與公開資訊未查證(演講時剛創立)。/ GistFlow's product naming and public materials couldn't be verified; the company had just launched.
