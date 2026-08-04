---
title: "Trustworthy Multi-Agent AI Systems for Healthcare: Challenges & Lessons Learned"
title_zh: "醫療領域的可信多 Agent AI 系統:挑戰與經驗教訓"
speaker: "Krishnaram Kenthapadi"
affiliation: "Chief Scientist, Oracle Health"
type: talk
stage: Nexus
date: 2026-08-01
session: "Session 3: Agentic AI in Finance & Healthcare"
video: "https://www.youtube.com/watch?v=ZIRc3EpzQJs&t=6852s"
video_range: "01:54:12–02:08:05"
transcript: "tmp/[English (auto-generated)] Nexus Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [healthcare, multi-agent, guardrails, evaluation, clinical-ai]
---

# 醫療領域的可信多 Agent AI 系統:挑戰與經驗教訓(Trustworthy Multi-Agent AI Systems for Healthcare: Challenges & Lessons Learned)

**一句話總結**:醫療 agent 的價值不在於模型多強,而在於把醫師從電子病歷的行政負擔中解放出來——而要真的落地,關鍵是領域知識(semantic knowledge graph)、雙向 guardrails、以及一套「線下評估會失效」的評估方法論。
**One-line summary**: The value of a healthcare agent lies not in model strength but in giving clinicians their time back from EHR paperwork — and shipping one hinges on domain knowledge encoded as a semantic knowledge graph, two-sided guardrails, and an evaluation methodology that assumes offline metrics will not survive contact with production.

## 中文筆記

### TL;DR

- **問題定義先於技術**:美國醫療的痛點是醫師短缺、80% 臨床人員 burnout、每次門診 15 分鐘裡醫師大半時間盯著螢幕,連帶造成每年約 40 萬件可預防死亡,以及約 1 兆美元的行政成本。Oracle Health 的 Clinical AI Agent 就是針對「把時間還給醫師」這一件事設計的。
- **架構重點在 orchestrator 與 guardrails**:一句「show me the recent labs」背後要判斷查結構化資料還是非結構化病歷、要不要帶入 UI 與病人脈絡、該用推理模型還是一段 deterministic Python;input/output 兩側都要 guardrail(病人端問診特別要能辨識醫療急症並升級)。
- **醫療的評估與別的領域不一樣**:離線評估的假設在線上常不成立(病人分佈會漂移);而且 **recall 極度重要**——病人摘要漏掉一項醫療相關資訊,不是體驗變差,是病人安全事故。

### 重點整理

#### 為什麼是醫療:被行政工作吃掉的臨床時間(約 01:56–01:59)

講者先花了幾分鐘鋪陳問題規模,而不是講模型:

- 臨床人力短缺,加上 burnout 與行政負擔——早在 COVID 之前的調查就顯示約 **80% 的臨床人員處於 burnout 狀態**,導致離職或計畫離開整個醫療產業。
- 病人能分到的看診時間持續縮短,典型只有 15 分鐘左右,而醫師在這段時間裡還得花一大塊在電腦前,而不是看著病人。
- 這些因素疊加系統性問題,結果是**光美國每年約 40 萬件可預防死亡**;同時醫療成本持續上升,美國約有 **1 兆美元**與行政負擔相關。

他的結論很直接:這不可持續。AI 在醫療其實已經在快速被採用,真正的問題是「怎麼用它降低行政負擔與 burnout,而且是**以可信的方式**做到——病人安全、法規遵循」。

#### Clinical AI Agent 與 multi-agent orchestrator(約 01:59–02:04)

Oracle Health 已上線的產品 **Clinical AI Agent**,能力是逐層堆上去的:

1. 在病人與醫師同意下,聆聽問診對話並自動生成病歷(medical notes)。
2. 在此之上自動擷取醫囑(X 光、檢驗、用藥等 orders)。
3. 再往前一步,在醫師看診「之前」就準備好摘要——這位病人為什麼來、病歷中哪些部分相關。

設計原則是 **voice-first、多模態、跨裝置**(手機、web、桌機),而且同時吃**醫師偏好(provider context)**與**病人脈絡(patient context)**,並盡可能主動——例如新的檢驗報告進來時,主動建議下一步的照護路徑。

核心元件是 **multi-agent orchestrator**。以「show me the recent labs」這種看似簡單的查詢為例,系統得決定:

- 要查**結構化**紀錄(檢驗數值)還是**非結構化**資料(病歷文字)?
- 要帶入哪些 UI 脈絡與病人脈絡?怎麼支援多輪對話?
- 更複雜的查詢(「Samantha 現在吃的藥有沒有副作用?」「根據她的病史與新報告,最佳處置是什麼?」)要調用工具庫與技能庫中的哪一個?

Orchestrator 之外還有兩層:

- **Guardrails 在輸入與輸出兩側都要有**。輸入側在**面向病人**的場景特別關鍵——敏感查詢、需要升級處理的醫療急症必須被正確攔截;輸出側則檢查 agent 回覆。
- **延遲與成本必須被壓住**:做 caching、平行計算,並在 runtime 決定這個查詢該路由到複雜推理模型、較簡單的語言模型,還是一段確定性的 Python 就夠了。這個 runtime 決策同時省下延遲與成本。

#### 從單一應用到「多 agent 醫療系統」,以及會出什麼錯(約 02:04–02:07)

再往上一層,是整個醫療體系的 multi-agent 化:利害關係人包含病人、醫師、行政、payer 端;系統包含 EHR;任務涵蓋搜尋、文件摘要、醫療編碼(medical coding)等。這些 agent 之間要如何互動,是開放問題。

他點名兩類最容易踩雷的地方:

- **評估**:離線評估的結果**不一定能轉移到線上**——可能是假設不再成立,也可能是病人分佈改變了。而且要把商業指標對應到可量測、可迭代的 applied science 指標。
- **Omission(漏訊息)**:呈現病人摘要時,**recall 極度重要**,這點和網頁搜尋等場景不同。摘要中漏掉一項醫療上相關(medically pertinent)的資訊,直接就是病人安全問題。

醫療影像的例子展示了另一種設計:胸部 X 光判讀的任務,用一個 orchestrated agent 加上一組**依臨床工作流程設計的 sub-agents**——對應放射判讀常用的 **ABCDE** 系統(airway、breathing 等)。這些 sub-agents **平行執行**,再由一個 synthesizer 整合彼此**可能互相衝突**的結果,決定最終判讀。

#### 收尾的四點經驗(約 02:07)

1. **先懂領域**,不要只盯著模型開發;資料驗證與評估方法論同等重要。
2. **和臨床人員一起迭代**:理解需求、早期版本先出來、根據回饋修。
3. **前沿模型不懂醫療的細節**:必須把領域與任務知識編碼進 **semantic knowledge graph** 與 **semantic data layer**。
4. **信任與安全是硬需求**:他們內部跑一套稱為 "AI review for health" 的審查流程。

### 金句

> "Our goal is to reduce the time doctors spend entering data or searching patient records or typing notes, and instead spend more time interacting with the patient — which is the reason they came to the profession in the first place."(約 01:59)

整場演講的動機不是「AI 能做什麼」,而是「醫師為什麼當醫師」。

> "If you miss something which is medically pertinent in the summary, that can lead to patient safety."(約 02:05)

在醫療場景,recall 不是體驗指標,是安全指標。

## English Notes

### TL;DR

- **The problem statement comes before the technology.** US healthcare is squeezed by clinician shortage, ~80% clinician burnout (documented even pre-COVID), and 15-minute visits in which the doctor spends much of the time facing a screen — contributing to roughly 400,000 preventable deaths a year and about $1T in administrative cost. Oracle Health's Clinical AI Agent is aimed squarely at giving clinicians their time back.
- **The hard parts are the orchestrator and the guardrails.** A query as plain as "show me the recent labs" requires deciding between structured and unstructured retrieval, folding in UI and patient context, and routing at runtime between a reasoning model, a cheaper LM, or plain deterministic Python. Guardrails sit on both the input and output sides — the input side matters most in patient-facing settings, where medical emergencies must be escalated rather than answered.
- **Healthcare evaluation has its own failure mode.** Offline results frequently do not transfer online because assumptions break or the patient distribution shifts. And unlike web search, **recall dominates**: an omission of medically pertinent information in a patient summary is a patient-safety incident, not a quality regression.

### Key Points

#### Why healthcare: clinical time eaten by paperwork (~01:56–01:59)

Kenthapadi opened on the size of the problem rather than on models. Clinician shortage compounds with burnout and administrative overhead — surveys from before the COVID pandemic already put roughly **80% of clinicians in burnout**, driving them to quit their practice or leave healthcare altogether. Meanwhile patients get less time: a typical visit runs about 15 minutes, much of which the provider spends looking at a computer rather than at the patient. Together with other systemic factors, this contributes to something on the order of **400,000 preventable deaths per year in the US alone**, and healthcare costs keep climbing — roughly **$1 trillion** in the US is tied to administrative burden.

His framing: this is not sustainable, AI is already being adopted rapidly across healthcare, and the open question is how to use it to cut administrative overhead and burnout **in a trustworthy manner** — patient safety intact, regulations followed.

#### Clinical AI Agent and the multi-agent orchestrator (~01:59–02:04)

Oracle Health's shipped product, **Clinical AI Agent**, layers capability upward: first automatically capturing medical notes by listening to the doctor–patient conversation (with consent from both), then capturing orders placed by the doctor (X-rays, labs, medications), then moving *ahead* of the visit — summarizing why the patient is here and what parts of the record are relevant before the doctor walks in.

The product is **voice-first and multimodal**, works across mobile, web, and desktop, and conditions on both **provider context** (physician preferences) and **patient context** (reason for visit, history). It aims to be proactive: when a new lab report arrives, it suggests the next best step in the care pathway.

The **multi-agent orchestrator** is the core component. Even for a simple-looking query, the orchestrator must decide whether to search structured records or unstructured notes, incorporate UI and patient context, and support multi-turn conversation — and for harder questions ("are there side effects of the medications Samantha is taking?", "what is the best course of action given her history and the new labs?") pick the right item out of a library of tools and skills.

Two other layers wrap it:

- **Guardrails on both sides.** The input side matters especially when the surface is patient-facing rather than doctor-facing: sensitive queries and medical emergencies requiring escalation must be handled appropriately. Output-side guardrails check the agent's response.
- **Latency and cost containment.** Caching, parallel computation, and a runtime routing decision — complex reasoning model vs. simpler language model vs. deterministic Python — that saves both latency and cost.

#### From one application to a multi-agent healthcare system, and what goes wrong (~02:04–02:07)

Scaling beyond a single application means a multi-agent *healthcare system*: patients, doctors, administrators, and payer-side stakeholders; systems including the EHR; tasks spanning search, document summarization, and medical coding. How all those agents interact with one another is the open design problem.

Two failure classes he called out:

- **Evaluation.** What works offline may not translate online, either because the assumptions no longer hold or because the patient distribution has shifted. Business metrics also need to be mapped onto applied-science metrics that can actually be measured and iterated on.
- **Omissions.** When presenting a patient summary, recall is extremely important — unlike web search. Missing something medically pertinent is a patient-safety failure.

A medical-imaging example showed a different shape of the same idea: for chest X-ray interpretation, an orchestrated agent sits above sub-agents **modeled on clinical workflows** — following the **ABCDE** system used in imaging (airway, breathing, and so on). The sub-agents run **in parallel**, and a synthesizer reconciles their potentially **conflicting** outputs into a final read.

#### Four closing lessons (~02:07)

1. **Understand the domain** — don't focus only on model development; data validation and evaluation methodology carry equal weight.
2. **Iterate with clinicians**: understand their needs, get an early version out, refine on feedback.
3. **Frontier models lack healthcare-specific nuance** — encode domain and task knowledge into a **semantic knowledge graph** and a **semantic data layer**.
4. **Trust and safety are non-negotiable**; his team runs an internal process he described as "AI review for health."

### Quotes

> "Our goal is to reduce the time doctors spend entering data or searching patient records or typing notes, and instead spend more time interacting with the patient — which is the reason they came to the profession in the first place." (~01:59)

The motivation is framed around why clinicians entered medicine, not around what AI can do.

> "If you miss something which is medically pertinent in the summary, that can lead to patient safety." (~02:05)

In clinical settings recall is a safety metric, not a quality metric.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Oracle Health Clinical AI Agent | Oracle Health 已上線的臨床 agent:環境語音記錄病歷、自動擷取醫囑、看診前摘要 | Oracle Health's shipped clinical agent: ambient note capture, automatic order capture, pre-visit summarization | 演講中提到有 live demo 連結 / a live demo link was shown on slide;產品頁 <https://www.oracle.com/health/clinical-suite/clinical-ai-agent/> |
| Multi-agent orchestrator | 決定結構化 vs 非結構化檢索、工具/技能選擇、runtime 模型路由 | Decides structured vs. unstructured retrieval, tool/skill selection, and runtime model routing | Clinical AI Agent 的核心元件 / core component of the product |
| ABCDE 影像判讀子 agent | 依胸部 X 光臨床流程(airway、breathing…)拆出平行 sub-agents,再由 synthesizer 整合衝突結果 | Parallel sub-agents modeled on the ABCDE chest X-ray workflow, reconciled by a synthesizer | 醫療影像案例 / medical-imaging case study |
| Semantic knowledge graph / semantic data layer | 把醫療領域與任務知識編碼進系統,補前沿模型缺的醫療 nuance | Encodes domain and task knowledge that frontier models lack | 收尾四點經驗之一 / one of the closing lessons |
| Agentic systems tutorial | 團隊在一場 ACM 會議上發表的 agentic 系統 tutorial,整理了「會出什麼錯」 | Tutorial his team presented at an ACM conference, cataloguing agentic failure modes | 會議全名待確認 / exact venue name to verify |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Krishnaram Kintapati / Krishna Ram | Krishnaram Kenthapadi |
| chief science scientist | Chief Scientist |
| clinical agent / clinical AI agent | Oracle Health Clinical AI Agent |
| multi- aent / aent | multi-agent / agent |
| medical nodes | medical notes |
| god rails | guardrails |
| explanability | explainability |
| multimodel | multimodal |
| patient phasing / doctor phasing | patient-facing / doctor-facing |

## 待確認 / To Verify

- 「tutorial that we presented at the ACM conference on agentic systems and AI」——會議正式名稱與 tutorial 連結待查證。/ The exact name of the ACM conference and a link to the tutorial.
- 「AI review for health」是否為 Oracle 內部正式流程名稱,拼法待確認。/ Whether "AI review for health" is the official internal process name at Oracle.
- 投影片上 Clinical AI Agent live demo 的連結網址未在逐字稿中出現。/ The live-demo URL shown on slide is not captured in the transcript.
- 80% burnout、40 萬件可預防死亡、1 兆美元行政成本三個數字的原始出處(講者只說是 surveys / estimates)。/ Primary sources for the 80% burnout, 400K preventable deaths, and $1T administrative cost figures — the speaker cited them as surveys/estimates only.
