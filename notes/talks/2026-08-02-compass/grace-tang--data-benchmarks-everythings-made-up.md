---
title: "Data Benchmarks: Where Everything's Made Up and the Points Don't Matter"
title_zh: "資料 Benchmark:一切都是編的,分數也不重要"
speaker: "Grace Tang"
affiliation: "AI @ Hex"
type: talk
stage: Compass
date: 2026-08-02
session: "Session 4: Agent Evaluation & Benchmarks"
video: "https://www.youtube.com/watch?v=1UrriPJRSPU&t=9819s"
video_range: "02:43:39–02:49:08"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [benchmarks, data-analytics, realism, evaluation, synthetic-environments]
---

# 資料 Benchmark:一切都是編的,分數也不重要(Data Benchmarks: Where Everything's Made Up and the Points Don't Matter)

**一句話總結**:好的 frontier benchmark 有一個共同點——題目對 agent 和對人類都是真的難;但資料分析領域的公開 benchmark 大多是選擇題、Kaggle 練習題和規格不清的偽問題,和分析師的日常工作幾乎無關,所以 Hex 自己蓋了一間完全虛構、但夠髒夠真的公司 Shorelane 來測。
**One-line summary**: Great frontier benchmarks share one trait — the problems are genuinely hard for agents *and* for people. Public data-analytics benchmarks are mostly multiple-choice questions, Kaggle exercises, and underspecified pseudo-questions that look nothing like an analyst's day job — so Hex built its own entirely fictional but convincingly messy company, Shorelane, to test against.

## 中文筆記

### TL;DR

- **論點只有一句**:agent 應該在「與最終部署環境同等真實」的環境裡被測試。而資料分析是 frontier benchmark 裡**被模型化得最差的領域之一**。
- **三個公開 benchmark 的具體病灶**:DSBench 的「真實資料任務」其實是財務建模選擇題和 Kaggle 的 Scrabble 拼字謎題;Spider 2 的英文描述過度規定,實質是把英文翻成 WHERE 子句的翻譯/指令遵循任務,不是分析;DABstep 的「哪個國家詐欺最多」根本沒說是看**詐欺率**還是**詐欺量**——規格不清,而真正的分析師會給你一張圖。
- **Hex 的做法是 Shorelane**:一間完全合成的公司,帶著真實企業會有的語意陷阱、髒資料、schema migration 與不完整的文件;任務是分析師日常會接到的**工單**,評分看的是**整條思考鏈、工具使用效率、以及分析本身**。

### 重點整理

#### 好的 frontier benchmark 長什麼樣(約 02:44–02:45)

Grace Tang 在 Hex 做 AI research。Hex 是 AI 資料分析平台,她大部分時間在想辦法讓 LLM 把資料分析與資料科學做得更好——「這件事真的很難」——因此 eval 與實驗佔了他們思考的很大一塊。

她的開場是一句吐槽:最近每次看到新的公開資料 benchmark,感受都一樣——**「一切都是編的,分數也不重要。」**

她的主張很簡單,也呼應了當天很多講者:**我們應該在「與最終部署同等真實」的環境裡測試 agent。** 而她要說明的是:**資料領域在 frontier benchmarking 裡被模型化得特別差。**

先看好的長什麼樣。她舉了三個例子:從零重建一個常見 codebase(沒有網路,只有文件)、經營一間販賣機生意最後直接看你賺多少、以及那種**看似簡單卻困難、人類只有約 30% 能解**的網路搜尋題。

這些優秀的 frontier benchmark 有什麼共同點?**它們測的是我們真正在乎 agent 能做到的真實世界行為;而且題目對 agent 難,對人也難。**

#### 資料分析領域的三個反例(約 02:45–02:47)

**DSBench**:去年 OpenAI 用 DSBench 宣布他們的 agent 在「真實資料任務」上大幅超越人類表現。那些「真實任務」實際上是什麼?**一堆關於財務建模的選擇題**——「你能寫出這段 SQL 嗎?」「你該用哪個 Excel 公式?」——再加上一堆公開的 Kaggle 專案,**包括一個 Scrabble 拼字謎題**。她的評語:「資料分析師會告訴你,他們的日常工作不長這樣。如果你的工作長這樣,我很遺憾。」

**Spider 2**(她提到 Scale 的 Emily 稍早也講過 text-to-SQL):主要問題是**它其實沒在測分析**。仔細看,那些英文描述非常具體、非常規定性,你基本上是在**把英文對應成 WHERE 子句**——這是翻譯任務或指令遵循任務。而且外部知識的策展也不夠嚴謹——**「連運動項目都搞錯了。」**

**DABstep**:一個很知名的資料集。題目看起來很直接:選擇題,「詐欺最多的國家是哪個?」問題是,**你真的把資料拉出來看,會發現這題根本規格不清**——它沒說你要看的是**詐欺率**還是**詐欺量**。而真正的分析師產出的可能是一張圖表,而**那張圖可以說更完整、也更正確**。

她補了一句避免誤會:「我不想踩別人的成果,他們投入了很多心力。」但整體而言,同樣的主題一再浮現(她列了九項,多到念不完):**不真實、評分過於嚴苛、不是紮根在現實裡的。**

#### Shorelane:自己蓋一間夠髒的公司(約 02:47–02:48)

於是 Hex 建了 **Shorelane**。她一開口就自嘲呼應講題:**「Shorelane 完全是編出來的,分數一樣不重要。我不是說我們解決了這個問題,但它挺酷的,而且我們試著處理了前面那些真實性問題。」**

**Shorelane Commerce** 是一間**完全合成的 B2B SaaS 公司**,帶著真實企業裡會出現的**語意陷阱**。它很髒:有 **schema migration**,有**不完整的文件**。

任務端則是讓 agent 處理**現實中分析師或分析 agent 真的會接到的工單**。評分看三件事:**整條思考鏈(train of thinking)、工具使用效率、以及實際進行的分析本身。**

#### 沒講完的下半題(約 02:48)

她最後拋出一個因時間不足而只能點到為止的問題:**這些 eval 仍然是被凍結在某個時間點的。我們要怎麼讓資料分析(agent)從自己的錯誤中學習?**

更多內容在 hex.tech;她也提到職缺頁面歡迎接洽。

### 金句

> "We should be testing these agents in environments that have the same level of realism as their eventual deployments."(約 02:44)

整場的論點。

> "What do all of these great frontier benchmarks have in common? … The problems are hard for agents and they're hard for people as well."(約 02:45)

好 benchmark 的判準,一句話。

> "Data analysts will tell you that this is not what their work looks like on the day-to-day. If this is what your work looks like, I'm sorry."(約 02:46)

全場笑點,但也是對 DSBench「真實任務」最直接的反駁。

> "These evals are still suspended in a moment in time. How can we allow data analytics to learn from their mistakes?"(約 02:48)

她留下的開放問題:靜態 eval 之後呢?

## English Notes

### TL;DR

- **One thesis**: agents should be tested in environments with the same level of realism as their eventual deployments — and data analytics is **a uniquely poorly modeled field in frontier benchmarking**.
- **Three concrete diagnoses.** DSBench's "realistic data tasks" turn out to be multiple-choice financial-modeling questions and Kaggle exercises including a Scrabble word puzzle. Spider 2's prescriptive English makes it a translation / instruction-following task — mapping English onto WHERE clauses — not analytics. DABstep's "top country for fraud" never says whether it means fraud *rate* or fraud *volume*; it's underspecified, and a real analyst would answer with a chart.
- **Hex's answer is Shorelane**: a fully synthetic company carrying the semantic pitfalls a real business has — messy data, schema migrations, incomplete documentation — where agents work realistic analyst tickets and are scored on **their whole train of thinking, tool efficiency, and the analytics itself.**

### Key Points

#### What a good frontier benchmark looks like (~02:44–02:45)

Tang does AI research at Hex, an AI data analytics platform. Most of her time goes into getting LLMs to do data analytics and data science better — "which is really hard" — so eval and experimentation occupy a large share of the team's thinking.

Her opener was a jab: lately, every new public data benchmark leaves her with the same impression — **everything's made up and the points don't matter.**

Her thesis echoes several other speakers that day: **test agents in environments as realistic as where they'll be deployed.** What she wanted to show is that **data is unusually badly modeled in frontier benchmarking.**

First, the good examples. She cited three: rebuilding a common codebase from scratch with no internet and only docs; running a vending machine business and simply evaluating profit at the end; and those deceptively simple web search questions that **humans solve only around 30% of the time.**

What do those great frontier benchmarks share? **They test real-world behavior we actually care about agents performing, and the problems are hard for agents and hard for people alike.**

#### Three counterexamples from data analytics (~02:45–02:47)

**DSBench.** Last year OpenAI used DSBench to report that their agent surpassed human performance by a significant margin on "realistic data tasks." What do those realistic tasks look like? **A pile of multiple-choice exam questions about financial modeling** — can you write the SQL, which Excel formula should you use — plus a set of public Kaggle projects **including a Scrabble word puzzle.** Her verdict: "data analysts will tell you this is not what their work looks like on the day-to-day. If this is what your work looks like, I'm sorry."

**Spider 2** (she noted Emily from Scale had raised text-to-SQL earlier). The main problem is that **it isn't really testing analytics.** The English is very specific and very prescriptive; you're essentially **mapping English onto WHERE clauses** — a translation or instruction-following task. And the external knowledge isn't carefully curated either — **"it's the wrong sport."**

**DABstep.** A well-known set. A question looks perfectly straightforward: multiple choice, what's the top country for fraud? The problem is that **once you pull the actual data, the question is fundamentally underspecified** — it never says whether you're looking at fraud *rate* or fraud *volume*. A real data analyst might produce a chart instead, and **arguably that's more complete and more correct.**

She added a caveat against being misread: "I don't want to dunk on everyone's work, they've done a lot of hard work here." But the same themes keep emerging — nine of them, too many to read aloud — and the gist is that they're **not realistic, the grading is harsh, and it isn't grounded in reality.**

#### Shorelane: building a company messy enough to be real (~02:47–02:48)

So Hex built **Shorelane**, which she introduced with the talk's own punchline: **"Shorelane is completely made up. The points don't matter either. I'm not saying we figured it out, but it is pretty cool, and we try and address some of these realism issues."**

**Shorelane Commerce** is a **fully synthetic B2B SaaS company** carrying the kind of **semantic pitfalls that occur in a real business.** It's messy: it has **migrations** and **incomplete documentation.**

On the task side, agents work **realistic tickets that an analytics agent — or an analytics person — would genuinely get in real life.** Scoring covers three things: **the entire train of thinking, tool efficiency, and the actual analytics being performed.**

#### The half she ran out of time for (~02:48)

Her closing gesture was toward the unfinished part: **these evals are still suspended in a moment in time. How do we let data analytics agents learn from their mistakes?**

More at hex.tech; she also pointed at their careers page.

### Quotes

> "We should be testing these agents in environments that have the same level of realism as their eventual deployments." (~02:44)

The thesis of the talk.

> "What do all of these great frontier benchmarks have in common? … The problems are hard for agents and they're hard for people as well." (~02:45)

A one-line test for whether a benchmark is worth anything.

> "Data analysts will tell you that this is not what their work looks like on the day-to-day. If this is what your work looks like, I'm sorry." (~02:46)

The room's biggest laugh, and also the most direct rebuttal of DSBench's "realistic tasks."

> "These evals are still suspended in a moment in time. How can we allow data analytics to learn from their mistakes?" (~02:48)

The open question she left behind: what comes after static evals?

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Shorelane / Shorelane Commerce | Hex 建構的完全合成公司環境,用於資料分析 agent 評估 | Hex's fully synthetic company environment for evaluating data analytics agents | Hex 部落格另有更詳細的環境描述(合成 Snowflake warehouse、注入的資料品質問題、每日推進的時鐘)/ Hex's blog describes the environment in more detail |
| DSBench | 資料科學 benchmark,被點名任務不真實 | Data science benchmark, criticized for unrealistic tasks | OpenAI 曾用它宣稱超越人類表現 / cited by OpenAI to claim superhuman performance |
| Spider 2 | text-to-SQL benchmark,被點名實質是翻譯/指令遵循任務 | Text-to-SQL benchmark, criticized as a translation / instruction-following task | |
| DABstep | 資料分析 benchmark,被點名題目規格不清 | Data analytics benchmark, criticized as underspecified | |
| Hex | AI 資料分析平台 | AI data analytics platform | hex.tech |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| a random set(主持人誤讀下一位講者)| Arindam Sett(下一場講者 / next speaker) |
| hex.te | hex.tech |
| evolves | evals |
| sellable by humans | solvable by humans |
| B2B SAS | B2B SaaS |
| dabstep | DABstep |
| spider 2 | Spider 2 |

## 待確認 / To Verify

- 她舉的三個「好 benchmark」中,第一個(從零重建 codebase、無網路只有文件)的正式名稱——字幕聽作 "program bench",未能確認。/ The first of her three "good benchmark" examples (rebuild a codebase from scratch, no internet, docs only) — captions give "program bench"; name unconfirmed.
- 販賣機經營 benchmark 與「人類僅約 30% 可解」的網路搜尋 benchmark 的正式名稱(演講中未點名)。/ Formal names of the vending-machine business benchmark and the web-search benchmark humans solve ~30% of the time — not named on stage.
- 她投影片上「九項主題」的完整清單(她說太多念不完)。/ The full list of the nine recurring themes on her slide, which she skipped reading aloud.
- Shorelane 的公開程度:是否開源、是否有公開 leaderboard。/ Whether Shorelane is open-sourced or has a public leaderboard.
- 她稱 Shorelane Commerce 為「B2B SaaS」,Hex 部落格則描述為 B2B2C 辦公用品平台,說法需核對。/ She called Shorelane Commerce a "B2B SaaS" company; Hex's blog describes it as a B2B2C office-supplies platform — the descriptions need reconciling.
