---
title: "Agentic AI Applications for Mental Health: From Chatbots to Clinical Orchestration"
title_zh: "心理健康的 Agentic AI 應用:從聊天機器人到臨床流程協作"
speaker: "Venkat Bhat"
affiliation: "Associate Professor; Director, AI for Mental Health (AI-M) Program, University of Toronto"
type: talk
stage: Nexus
date: 2026-08-01
session: "Session 3: Agentic AI in Finance & Healthcare"
video: "https://www.youtube.com/watch?v=ZIRc3EpzQJs&t=7685s"
video_range: "02:08:05–02:23:23"
transcript: "tmp/[English (auto-generated)] Nexus Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [mental-health, clinical-trials, multi-agent, healthcare, evaluation]
---

# 心理健康的 Agentic AI 應用:從聊天機器人到臨床流程協作(Agentic AI Applications for Mental Health: From Chatbots to Clinical Orchestration)

**一句話總結**:一位精神科醫師兼臨床試驗研究者的立場——在模擬環境裡表現良好的 multi-agent 系統只是第一步,心理健康領域真正缺的是隨機對照試驗;全世界用生成式 AI 工具做的 RCT 到現在只有一到兩個。
**One-line summary**: A psychiatrist and clinical trialist's position — a multi-agent system that performs well in simulation is only step one; what mental health actually lacks is randomized controlled trials, and worldwide there is still only about one (going on two) RCT of a generative-AI-based tool.

## 中文筆記

### TL;DR

- **他的研究流程是三段式**:選定一個可能可自動化的臨床工作流程 → 建 single/multi-agent 系統,並用「bot 扮演使用者」在 sandbox 模擬驗證 → **接著跑兩到三年的臨床試驗**。第三段才是他和多數 AI 演講者最大的差別。
- **成果橫跨四個領域**:臨床照護(自動產生 PHQ/GAD-7 等量表、multi-agent 做 DSM 診斷式訪談)、醫學教育(加速住院醫師取得臨床能力)、研究(systematic review 與 meta-analysis 的局部自動化)、品質改善(從虛擬看診的多模態資料估計醫病關係)。
- **兩個負面但重要的發現**:(1) 逼 agent 執行 motivational interviewing 時,**複雜度超過某個水準後 agent 就失守,連 guardrail 都守不住**;(2) 高 / 低安全 guardrail 對「agent 被使用者如何感知」有顯著影響。而全世界生成式 AI 工具的 RCT 只有一到兩個——證據嚴重不足。

### 重點整理

#### 立場與方法論:我是臨床試驗研究者(約 02:08–02:11)

講者自我定位很明確:他是**精神科醫師與 clinician scientist**,任職於多倫多大學,主持 **AI for Mental Health (AI-M) Program**;同時是 **Temerty Centre for AI Research and Education in Medicine(T-CAIREM)** 底下的全國心理健康 community of practice lead——該中心串連了加拿大各大學,他負責的是心理健康這一塊。

他進入這個領域的動機是:AI 的許多進展本來就是從人腦運作方式來的——**deep learning 對應皮質(cortical)表徵,reinforcement learning 對應皮質下(subcortical)**。他約三分之一的研究是在**反向工程這些系統**(可解釋性方向,當天沒講);另外三分之二是**心理健康臨床工作流程的自動化**,也就是這場演講的主題。

他的標準流程是:

1. 找出一個有機會自動化的臨床工作流程。
2. 開發自動化系統(single agent 或 multi-agent),用**一個 bot 扮演終端使用者**,在 sandbox 環境做模擬,證明它可行。
3. **跑臨床試驗**——這是他強調與當天多數講者最大的不同。他在憂鬱症、PTSD、焦慮症(含預防端),近期也在心理健康與阿茲海默症領域主持試驗。

他跑試驗的理由很實際:某個工作流程上 agent 「不劣於人類」還不夠。還有變革管理、服務流程重新設計等一整套生態系變動要發生,所以他們用 mixed methods 去看「就算它有效,要真的被採用還需要什麼」,並把**成本效益**納入評估。

#### 三四年前的那張基石投影片(約 02:12)

大約三四年前,當自主性等級開始往上走,他的團隊就在想:這對心理健康的臨床照護意味著什麼?於是提出了 **collaborative / assistive / semi-autonomous agents** 的分類,並在 human-in-the-loop 框架下界定人的角色。這張圖是整場演講反覆回扣的座標系。

他也點出現實:**AI scribe 是臨床人員唯一普遍認得、而且已在使用的生成式 AI 應用**;其他每一類都還需要相當多證據。

#### 四個領域的實作(約 02:13–02:20)

**臨床照護**——把他自己的門診從初診 intake 到出院整條流程用 agent 自動化,每一段都已發表,現正往臨床試驗推進。兩個具體例子:

- **Measurement-based care**:心理健康缺少「糖尿病的血糖、高血壓的血壓」這種客觀量測。臨床上用的是 **PHQ**、**GAD-7** 這類量表,但**過去二十多年一直很難讓這些量表被確實填寫**。他們的做法是:拿非結構化資料(可以想成 ambient scribe 的輸出)自動生成量表分數,並在臨床人員沒有收集到相關資訊時主動提示。這套目前正透過醫院端的 **Epic** 進入試驗。
- **多 agent 診斷式訪談**:把操作化的 DSM(即 **SCID** 這套工具)拆成 multi-agent——一個 agent 負責問診、另一個負責監督(**在該模組完成前不允許進入下一個模組**)、遵循 SCID 內部的 skip logic,再加一個 orchestrator / diagnoser。用 bot 扮演帶有各種複雜 DSM 診斷的病人測試,表現良好,現已進入臨床試驗。試驗**刻意定位在輕到中度症狀**——他們清楚重度精神病、重度憂鬱或阿茲海默症患者無法使用這類工具。

**醫學教育**——他直接承認 deskilling(能力退化)是**正當的擔憂**,需要用別的方式處理。他們選的切角相反:訓練一位臨床醫師要 **10 年**(4 年醫學院 + 4 到 6 年住院醫師訓練),**能不能用 agentic AI 加速能力(competency)的取得?** 做法是依加拿大與美國各自的專科委員會標準,拆解出住院醫師結訓前應具備的能力,再建一個 multi-agent 系統:一個 bot 扮病人、一個 bot 扮臨床醫師、一個 bot 扮想練習訪談技巧的住院醫師——因為住院醫師學會臨床訪談(臨床醫師的核心技能)的方式,就是反覆做、報告給主治、拿回饋。他們正與**七個規模最大的臨床訓練專案**合作部署:一組照現行方式訓練,另一組加上這套系統,看能力取得是否能從五年縮到三、四年。另有一個變體是幫住院醫師學習心理治療的基本原則,如 **CBT** 與 **motivational interviewing**。

他對此保持懷疑:「我是從臨床試驗的懷疑角度來的——這些東西大多不會照我們想的方式運作,但**少數真的成立的,會有變革性的影響**。」

**研究**——他做了 5 到 10 年的 systematic review 與 meta-analysis,判斷「再過幾年我就不會自己做了,我們會有 **living systematic reviews and meta-analyses**」。策略不是端到端自動化,而是**鎖定 pipeline 中的特定環節**。動機很具體:研究助理光是比對文獻抽取的錯誤就要花數小時甚至數週。量化端有一篇論文,質性端(thematic analysis)也做了對照——比較傳統質性分析得到的主題與生成式 AI 得到的主題。**底線仍是 human-in-the-loop**。同樣的思路也用在 **EEG 分析**的資料處理上。

**品質改善**——疫情期間臨床人員轉為虛擬看診,他們想知道:虛擬情境下的醫病關係本質是什麼?做法是多模態:用多種資料流與非結構化資料去產生 **Working Alliance Inventory**——這是醫病關係品質的代理指標。這項工作也正在逐步進入臨床試驗。

#### 兩個限制性發現,與證據的匱乏(約 02:20–02:22)

- **複雜度上限**:他們研究 agent 直接提供治療的各個環節時,強迫 agent 執行 **motivational interviewing**,結果發現**複雜度超過某個水準之後,agent 就做不到了,而且會失去它的 guardrails**。
- **Guardrail 影響感知**:比較低安全 guardrail 與高安全 guardrail 的設定,結果顯示 **guardrail 強度對「agent 被如何感知」有顯著影響**。
- **證據面**:他掃了全世界在這個領域的進展,結論是——儘管這些 agent 的可能性被講得很大,**用生成式 AI 工具做的隨機對照試驗目前只有一個,加上去年那個 bot 才要變成兩個**。他的收尾就是這句:臨床試驗有迫切且關鍵的需求,而這正是他團隊大量投入的方向。

### 金句

> "It's not enough if at that particular workflow the agent is non-inferior to the human doing the task. There are a lot of other ecosystem changes."(約 02:13)

「不劣於人類」只是入場券,不是採用的理由。

> "Most of these things are not going to work — at least in the way we think it would work — but the few things which would work will have a transformative effect."(約 02:17)

一個臨床試驗研究者對 agentic AI 的期望值設定。

> "In spite of all the possibilities for what these agents could do, there's only one randomized control trial — now coming to two."(約 02:21)

演講的落點:能力的敘事遠遠跑在證據之前。

## English Notes

### TL;DR

- **His pipeline has three stages**: pick a clinical workflow that might be automatable → build a single- or multi-agent system and validate it in a sandbox with a **bot playing the end user** → then **run a two-to-three-year clinical trial**. That third stage is what separates him from most AI speakers.
- **Work spans four domains**: clinical care (auto-generating PHQ/GAD-7 scales; a multi-agent DSM diagnostic interview), medical education (accelerating residents' competency attainment), research (partial automation of systematic reviews and meta-analyses), and quality improvement (estimating the therapeutic alliance from multimodal virtual-visit data).
- **Two negative-but-important findings**: (1) when forced to deliver motivational interviewing, agents **fail past a certain complexity threshold and lose their guardrails**; (2) low vs. high safety guardrails significantly change how the agent is *perceived*. And worldwide there is still only about one RCT (going on two) of a generative-AI-based tool — the evidence base is thin.

### Key Points

#### Where he stands: a clinical trialist first (~02:08–02:11)

Bhat introduced himself as a **psychiatrist and clinician scientist** at the University of Toronto who leads the **AI for Mental Health (AI-M) Program**, and who serves as national mental-health community-of-practice lead within the **Temerty Centre for AI Research and Education in Medicine (T-CAIREM)** — a centre that brings universities across Canada together, with mental health as his slice of it.

His entry point into the field was that much of AI's development traces back to how the brain works: **deep learning maps to cortical representation, reinforcement learning to subcortical**. About a third of his program reverse-engineers these systems (interpretability work, not covered in this talk); the other two-thirds automates clinical workflows in mental health.

The standard paradigm: identify a workflow that might be automatable, build the automation (single agent or multi-agent), show in a sandboxed simulation — with a bot playing the end user — that it works, and then run clinical trials. He runs trials across depression, PTSD, anxiety (including on the prevention side), and more recently mental health and Alzheimer's.

His reason for insisting on trials is practical: it isn't enough for the agent to be **non-inferior** to a human on that workflow. Change management, service redesign, and other ecosystem changes have to happen too, so his group uses mixed methods to ask what adoption would actually require even for an efficacious tool — and folds in **cost-benefit**, which he called a critical factor.

#### The cornerstone slide from three or four years ago (~02:12)

As autonomy levels started climbing three or four years ago, his group asked what that would mean for clinical care in mental health, and landed on a taxonomy of **collaborative, assistive, and semi-autonomous agents** inside a human-in-the-loop model, with the human's role defined per tier. He returned to this slide repeatedly as the organizing frame.

His reality check: **the AI scribe is the one generative-AI application clinicians identify with and actually use**. Everything else in the taxonomy still needs a lot of evidence.

#### Four domains of implementation (~02:13–02:20)

**Clinical care.** They automated his own clinic end to end — from intake through discharge — with agents at each stage, each published, each now moving toward trials. Two examples:

- **Measurement-based care.** Mental health lacks the equivalent of blood sugar for diabetes or blood pressure for hypertension; clinicians use scales like the **PHQ** or **GAD-7**, and for over two decades it has been genuinely hard to get them completed. Their system takes unstructured data (think of the output of an ambient scribe) and generates the scales, and prompts clinicians when the underlying information hasn't been collected. This is moving into trials through **Epic** at their hospital sites.
- **Multi-agent diagnostic interviewing.** They took the operationalized DSM — the **SCID** instrument — and built a multi-agent system around it: one agent asks the questions, another oversees and **won't let the interview advance to the next module** prematurely, the system follows the SCID's skip logic, and an orchestrator/diagnoser sits on top. With a bot playing patients carrying all kinds of complicated DSM diagnoses, it performed well; it is now in clinical trials, **deliberately positioned for mild-to-moderate symptoms** — someone with severe psychosis, severe depression, or Alzheimer's is not going to be able to use it.

**Education.** He granted that **deskilling is a legitimate concern** that needs addressing in its own right, then framed the opposite question: training a clinician takes **10 years** (four of medical school, four to six of residency) — can agentic AI accelerate the attainment of competencies? They decomposed the competencies residents are expected to reach by end of training, per the respective Canadian and US boards, then built a multi-agent system: a bot as the patient, a bot as the clinician, and a bot as the resident practicing interviewing — because clinical interviewing, the core skill, is learned by doing it repeatedly, presenting, and getting feedback. They are working with **seven of the largest clinical training programs** to deploy it in a two-arm design: current training vs. current training augmented, testing whether competencies can be reached in three or four years instead of five. A variant helps residents learn the basic principles of psychotherapy — **CBT** and **motivational interviewing** — by interviewing a simulated patient within that framework.

He stayed skeptical throughout: most of these things will not work the way we think they will, but the few that do will be transformative.

**Research.** After 5–10 years of doing systematic reviews and meta-analyses, he expects to stop doing them himself within a couple of years, replaced by **living systematic reviews and meta-analyses**. The approach is not end-to-end automation but **specific points inside the pipeline** — motivated by research assistants spending hours or weeks reconciling extraction errors across publications. They published on the quantitative side and repeated the exercise on the qualitative side (thematic analysis), comparing themes from conventional qualitative analysis against generative-AI-derived themes. The bottom line remains **human-in-the-loop**. The same idea is applied to data processing for **EEG analysis**.

**Quality improvement.** During the pandemic clinicians moved to virtual assessments, and his group wanted to characterize the patient–physician relationship in that setting. The approach was multimodal: several data streams and unstructured data feeding a prediction of the **Working Alliance Inventory**, the standard proxy for relationship quality. That work is gradually moving into clinical trials.

#### Two limiting findings, and the missing evidence (~02:20–02:22)

- **A complexity ceiling.** Studying whether agents can deliver therapy components, they forced an agent to conduct motivational interviewing and found that **past a certain level of complexity it cannot perform the task and loses its guardrails**.
- **Guardrails shape perception.** Comparing low-safety against high-safety guardrail conditions showed that guardrail strength has a **significant effect on how the agent is perceived**.
- **The evidence gap.** Surveying what the world is doing in this space, he closed on the point that despite everything these agents could in principle do, **there is only one randomized controlled trial — now becoming two, with the bot from last year — of generative-AI-based tools**. Clinical trials are the critical need, and that is where his team invests.

### Quotes

> "It's not enough if at that particular workflow the agent is non-inferior to the human doing the task. There are a lot of other ecosystem changes." (~02:13)

Non-inferiority is the entry ticket, not the adoption case.

> "Most of these things are not going to work — at least in the way we think it would work — but the few things which would work will have a transformative effect." (~02:17)

A clinical trialist's prior on agentic AI.

> "In spite of all the possibilities for what these agents could do, there's only one randomized control trial — now coming to two." (~02:21)

The talk's landing point: the capability narrative is far ahead of the evidence.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| AI for Mental Health (AI-M) Program | 講者在多倫多大學主持的計畫,聚焦心理健康臨床工作流程自動化 | Bhat's program at the University of Toronto, focused on automating mental-health clinical workflows | <https://ai.psychiatry.utoronto.ca/> |
| T-CAIREM | Temerty Centre for AI Research and Education in Medicine,串連加拿大各大學;講者為全國心理健康 community of practice lead | Temerty Centre for AI Research and Education in Medicine at U of T; Bhat leads the national mental-health community of practice | 字幕誤聽為 "temporary center" / heard as "temporary center" |
| PHQ / GAD-7 | 憂鬱與焦慮的標準自評量表;團隊從非結構化資料自動生成分數 | Standard depression and anxiety rating scales; the team auto-generates scores from unstructured data | 正推進 Epic 內的臨床試驗 / moving into trials through Epic |
| SCID(operationalized DSM) | DSM 診斷訪談工具;拆成問診 agent + 監督 agent + orchestrator/diagnoser 的 multi-agent 系統 | The structured DSM diagnostic interview instrument, rebuilt as a multi-agent system (interviewer + overseer + orchestrator/diagnoser) | 字幕記為 "the skid";已進入試驗,定位輕到中度症狀 / in trials, scoped to mild-to-moderate |
| Working Alliance Inventory | 醫病關係品質的標準代理指標;團隊用多模態資料流估計 | Standard proxy for the therapeutic alliance; estimated from multimodal data streams | 虛擬看診品質改善研究 / virtual-visit quality-improvement study |
| Living systematic reviews & meta-analyses | 局部自動化的證據合成,非端到端;量化與質性(thematic analysis)兩端都做過 | Partially automated evidence synthesis (not end-to-end), on both quantitative and qualitative (thematic analysis) sides | 仍為 human-in-the-loop / still human-in-the-loop |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Vin Katpot | Venkat Bhat |
| temporary center for AI in medicine | Temerty Centre for AI Research and Education in Medicine (T-CAIREM) |
| the skid / this kit | the SCID (Structured Clinical Interview for DSM) |
| GAD 7 | GAD-7 |
| multi- aent / aentic | multi-agent / agentic |
| deskkilling | deskilling |
| efiral(?) | 逐字稿雜訊,無對應詞 / transcript noise |

## 待確認 / To Verify

- 「there's only one randomized control trial, now coming to two, with the bot last year」——這個「the bot」指的是哪一個生成式 AI 治療聊天機器人的 RCT,名稱與出處待查證。/ Which generative-AI therapy chatbot RCT "the bot" refers to.
- 七個參與部署的臨床訓練專案名單未在演講中列出。/ The seven clinical training programs deploying the education system were not named.
- 演講提到的多篇論文(intake agents、SCID multi-agent、motivational interviewing 複雜度上限、guardrail 感知研究)均未給出標題,需另行對照 AI-M Program 出版清單。/ None of the cited papers were named on the transcript; cross-check against the AI-M Program publication list.
- 心理治療訓練 multi-agent 系統與診斷訪談系統是否為同一套系統的變體,講者敘述略過細節。/ Whether the psychotherapy-training system is a variant of the diagnostic-interview system.
