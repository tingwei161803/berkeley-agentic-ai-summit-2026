---
title: "Intelligence + Continual Learning = Expertise"
title_zh: "智慧 + 持續學習 = 專業"
speaker: "Yu Su"
affiliation: "CEO, NeoCognition; Associate Professor, OSU"
type: talk
stage: Compass
date: 2026-08-01
session: "Session 3: Foundational Capabilities"
video: "https://www.youtube.com/watch?v=AO0RXP-fVZQ&t=8481s"
video_range: "02:21:21–02:33:54"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [continual-learning, expertise, world-models, enterprise-ai, agents]
---

# 智慧 + 持續學習 = 專業(Intelligence + Continual Learning = Expertise)

**一句話總結**:智慧(解題能力)與專業(在特定環境中累積的、情境化的可靠競爭力)是**兩條正交的軸**;現代社會由數以百萬計、各有其「局部物理定律」的微世界構成,靜態模型壓縮不了,所以必須靠 continual learning 在工作中長出專業——而這條軸,將是下一個 scaling 維度。
**One-line summary**: Intelligence (the capacity to solve problems) and expertise (accumulated, situated competence in a specific environment) are largely **orthogonal axes**; modern society is millions of micro-worlds each with its own local physics, which no static model can compress, so expertise has to be grown on the job through continual learning — and that axis, not raw intelligence, is the next dimension for scaling.

## 中文筆記

### TL;DR

- **開場的三個怪現象**:AI 已經聰明到能解開懸而未決的重大數學問題,但在企業裡的擴散遠比預期慢;既然模型這麼聰明,為什麼還需要一整批 forward deployed engineers 才部署得動(人類換工作可不需要 FDE)?為什麼 90% 的價值歸於 infra 與 model 層,application 層拿不到 10% 還常常負毛利?
- **現代版的 Moravec 悖論**:1980 年代的版本是「難的事簡單、簡單的事難」——AI 擅長符號推理,卻學不會人類毫不費力的移動與感知。今天的版本換成了**日常的數位工作**。他的假設:社會不是一個統一世界,而是**數百萬個微世界**,每個職業、每間公司都有自己獨特的局部物理——結構、約束、affordance、動態——太異質也太動態,靜態模型壓縮不進去。
- **智慧 ≠ 專業**。智慧是「給我問題陳述與脈絡,我在巨大的解空間裡搜索、必要時開一百個 sub-agent 找出解答」;專業是「在特定環境的特定工作上,可靠、高效、有判斷力地交出超群表現」。智慧是**擴張性**的(搜索、燒 token);專業是**收縮性**的(形成捷徑與領域結構,壓縮搜索空間)。
- **從有界的智慧得到無界的專業**:若把智慧當 x 軸、專業當 y 軸,兩者大致正交。有智慧沒有 continual learning,得到的是「世界上最聰明的新手」——只會用生智慧硬闖每個問題,這就是大家 token 帳單爆炸的原因。continual learning 演算法決定的是**斜率**。若存在一個「逃逸智慧」門檻,越過之後配上夠強的持續學習,就能得到近乎無限的專業——這意味著市場的強烈分岔:前沿模型繼續追智慧,而世界上 90–95% 的工作也許現在的模型就夠聰明了,缺的只是持續學習。

### 重點整理

#### 三個怪現象(約 02:21–02:23)

他先宣告這是一場相當概念性的演講,只講三個概念:intelligence、expertise,以及 continual learning 如何橋接兩者。他認為這是今天最重要的概念問題之一,而且能解釋 AI 前沿一連串的怪現象:

1. AI 已經聰明到**當天早上才有 lab 宣布解開了 10 個懸而未決的重大數學問題**,但它在企業世界的擴散遠比所有人預期得慢。
2. 我們看到 **forward deployed engineers**(FDE)與部署公司爆炸性成長。但如果 AI 這麼聰明,為什麼需要 FDE 幫忙部署?它們不該自己部署自己嗎?**人類換到一份新工作,不需要一個 FDE 來教。** 那到底缺了什麼?
3. 價值分配:**90% 的價值流向 infra 與 model 層,application 層拿不到 10%,而且常常在負毛利下營運**。這顯然不是生態系的穩定均衡,怎麼解?

#### Coding 是特權世界,離開它就不行了(約 02:23–02:25)

他把當前這代 agent 稱為 **language agents**——以語言作為推理與溝通的媒介是它們的定義性特徵。它們已經找到第一個大眾市場:**coding**。最好的證據就是 Anthropic 那條眾所皆知的營收曲線。

但 coding 之所以成為第一個大眾市場,很大程度是因為它**本來就已經是一個語言化的世界**:一切都已經符號化表示、記錄與維護得很好,對 language agents 來說是完美的溫床。

離開這個特權世界呢?就沒那麼順了。他引用 **MIT NANDA** 的報告——企業導入 AI 遭遇大量問題(那是去年的資料,95% 這個數字可以爭論,但方向上是對的);以及各種光怪陸離的 agent 失敗模式。也因此(據他轉述)有人去年上 Dwarkesh 的 podcast 主張:**2025 不是 agent 元年,而是 agent 十年的開端**,並特別點名 computer use 與 continual learning 這兩個挑戰。

他的診斷:這是 **Moravec 悖論的現代版**。1980 年代的原版說,對 AI 而言難事易、易事難——擅長數學與 coding 這類符號推理,卻學不會對人類毫不費力的移動與感知。今天,難的變成了**日常的數位工作**。

為什麼?他的假設是:現代社會**不是一個統一的世界,而是由數百萬個微世界組成**。每個職業不同、每家公司不同——每家公司都很特別,**這正是它們存在的理由**。每個環境有它自己的局部物理:結構、約束、affordance、動態。太異質、太動態,任何試圖把它壓縮成單一靜態表徵的靜態模型都做不到。所以你必須**在工作中持續學習,長出專門化的專業**。

#### 智慧與專業的區別(約 02:25–02:29)

- **Intelligence**(限定在 LLM/LRM 語境):**解決問題的能力**。給我問題陳述、給我脈絡,我會在巨大的解空間裡推理,可能開出上百個 sub-agent,替你找出一個解。
- **Expertise**:**累積的、情境化的競爭力**——在**特定環境的特定工作**上,可靠、高效、帶著判斷力地交出超群表現。

專業裡到底裝了什麼?他借認知科學的文獻回答:在工作中形成專業,本質是**持續形成關於該工作、該領域的新心智表徵**,而它會以多種方式顯現:

- **看見的東西不一樣**:面對一份當機系統的冗長 bug report,專家與實習生看到的完全不同——專家會很快定位到可能的失效點。
- **看見深層結構而非表面模式**。
- **知道一切都是有條件的**:每條規則都附帶一堆前提條件,你得學會規則何時成立;也得學會例外在哪、什麼時候可以為了現實而彎折規則。
- **判斷力與品味**——最近大家常談的這件事,也源自專業。

所以大致可以把專業想成一個 **world model**:那個微世界的模型,以多種形式顯現,成為感知、推理與決策的基礎。

兩者最有意思的對比在於「方向」:**智慧是擴張性(expansive)的**——它在飛行中尋找脈絡、擴大搜索,而且因為**無法從過去累積**,所以吞掉海量的 token(他說 NeoCognition 自己每月燒掉數百萬美元的 token)。**專業是收縮性(contractive)的**——它是形成捷徑、形成領域有效結構的過程,目的是**縮小搜索空間**。

#### Continual learning 的統一定義(約 02:29–02:30)

他說 continual learning 是個很令人困惑的詞,先給一個統一定義:

> **持續學習是把「經驗」自適應地壓縮成「可重用的結構」以供「未來行為」使用的過程。**

四個要素都很重要,看到任何持續學習的工作都該逐一追問:講的是**什麼樣的經驗**?**怎麼壓縮**?壓成**什麼結構**?那個結構**怎麼被用在未來行為**上?其中 **adaptivity** 尤其關鍵:**你過去壓縮了什麼,應該決定你未來怎麼壓縮。**

#### 核心論點:從有界智慧得到無界專業(約 02:30–02:32)

他自認這是全場最重要也最有意思的部分。把 **intelligence 當 x 軸、expertise 當 y 軸**,兩者**大致正交**:

- 你可以拿到更聰明的模型,但**沒有持續學習,你得到的是「世界上最聰明的新手」**——只會用生智慧暴力硬闖每一個問題。**這就是為什麼每個人的 token 帳單都在爆炸。**
- 不同的持續學習演算法,本質上是在**設定你這條學習曲線的斜率**。

如果目標是「很強的持續學習演算法 → 很強的專家型 agent」,那麼由此可以推出他認為最有意思的未來:**unbounded expertise from bounded intelligence**。假設智慧存在一個門檻,姑且叫 **escape intelligence**;一旦越過它,再加上夠強的持續學習演算法,我們就能得到幾乎無限的專業——至少對世界上 90% 或 95% 的工作而言夠好了。

若成真,意味著**市場的強烈分岔**:前沿實驗室繼續打造更聰明的模型(那也有很多用例),但對其餘 90–95% 的工作,我們**可能不需要更聰明的模型,現有模型也許就夠了,缺的只是持續學習**。他認為這會造成非常有趣的市場動態。

#### 結尾:專業是下一個 scaling 維度(約 02:32–02:33)

他明確表態:**scaling 專業的目標不是取代人類勞動力,他不相信 job displacement 那套敘事**。他認為我們現在處於**專業的嚴重短缺**中:

- 在理想世界裡,每個人都想要**專屬的醫療照護、專屬的財務顧問、專屬的家教**。
- 每間公司都想建立**自己的、在地的人機共學迴路(local human–AI learning loop)**,知識與 IP 在其中累積。
- 一旦專業變得充裕,**很多問題的門檻會被降低到「值得做」的那一側**,從而在社會上創造出大量新機會。

### 金句

> "Humans don't need an FDE to teach us how to do a job."(約 02:22)

如果模型真的那麼聰明,為什麼部署它需要一整個 forward deployed engineer 產業?這句話把整場演講的問題意識立起來。

> "Every company is special. That's why they exist."(約 02:25)

微世界假設的核心:企業的獨特性不是雜訊,而是它存在的理由——也因此無法被壓縮進單一靜態模型。

> "If you can get more intelligent models, but if you don't have continuous learning, then it will become what I call the world's smartest novice."(約 02:31)

「世界上最聰明的新手」——本場最傳神的一個標籤,也直接解釋了 token 帳單問題。

> "Unbounded expertise from bounded intelligence."(約 02:31)

全場的核心命題,也是他對市場分岔的預言。

## English Notes

### TL;DR

- **Three puzzles up front**: AI just solved a batch of long-open major math problems, yet its diffusion into enterprises is far slower than anyone expected; if models are this smart, why does deploying them require an entire industry of forward deployed engineers (a human starting a new job doesn't need an FDE); and why does ~90% of the value accrue to the infra and model layers while the application layer takes under 10%, often at negative margin?
- **A modern Moravec's paradox.** The 1980s version: hard things are easy and easy things are hard — AI excels at symbolic reasoning but can't do the mobility and perception humans find effortless. Today's version is everyday *digital work*. His hypothesis: society isn't one unified world but **millions of micro-worlds**, each with its own local physics — structures, constraints, affordances, dynamics — too heterogeneous and too dynamic for any static model to compress.
- **Intelligence ≠ expertise.** Intelligence is the capacity to solve a stated problem by searching a giant solution space (possibly spinning up hundreds of sub-agents). Expertise is accumulated, situated competence: acting reliably, efficiently, and with judgment on a particular job in a particular environment. Intelligence is **expansive** (it searches, and it burns tokens because it can't accumulate); expertise is **contractive** (it forms shortcuts and domain structure that shrink the search space).
- **Unbounded expertise from bounded intelligence.** Plot intelligence on x and expertise on y and they're largely orthogonal. Smarter models with no continual learning give you "the world's smartest novice" brute-forcing every problem — which is why everyone's token bill is exploding. The continual learning algorithm sets the *slope*. If there's an intelligence threshold ("escape intelligence"), crossing it plus strong continual learning yields near-unlimited expertise — good enough for maybe 90–95% of the world's jobs, implying a sharp bifurcation of the market.

### Key Points

#### Three puzzles (~02:21–02:23)

He flags the talk as conceptual: three concepts — intelligence, expertise, and how continual learning bridges them — which he thinks is one of the most important conceptual questions right now, and which explains several bizarre observations at the AI frontier:

1. AI is now smart enough that **a lab announced solving ten long-open major math problems that very morning**, yet enterprise diffusion is much slower than expected.
2. There's an explosion of **forward deployed engineers** and deployment companies. If the models are this smart, shouldn't they deploy themselves? **Humans don't need an FDE to be taught how to do a job.** So what's missing?
3. Roughly **90% of the value accrues to infra and model layers**; the application layer gets under 10%, often at negative margin. That's not a stable equilibrium for the ecosystem.

#### Coding is a privileged world (~02:23–02:25)

He calls this generation **language agents** — using language for reasoning and communication is their defining trait — and notes they've found their first mass market in coding, best seen in Anthropic's revenue ramp.

Coding got there first largely because it's **already a linguistic world**: everything is already represented symbolically, well recorded, and well maintained. Perfect substrate for language agents.

Outside that privileged world, things go badly. He cites the **MIT NANDA** report on enterprise AI deployment problems (last year's data; the 95% figure is arguable but directionally right), and the zoo of bizarre agent failure modes — which is why (as he recounts) someone went on the Dwarkesh podcast last year to argue **2025 wasn't the year of agents but the start of the decade of agents**, calling out computer use and continual learning specifically.

His diagnosis: a **modern Moravec's paradox**, with everyday digital work in the role that mobility and perception played in the 1980s. Why? Because modern society is not one unified world but millions of micro-worlds. Every profession differs, every company differs — **every company is special, that's why they exist** — and each environment has unique local physics too heterogeneous and dynamic to compress into one static representation. So you have to keep learning on the job to form specialized expertise.

#### Intelligence versus expertise (~02:25–02:29)

**Intelligence** (in the LLM/LRM sense): the capacity to solve problems. Give it the problem statement and context, and it reasons through a gigantic solution space, possibly spinning up hundreds of sub-agents, to find you a solution.

**Expertise**: accumulated and situated competence — the ability to act reliably, efficiently, and with judgment to deliver superior performance on a particular job in a particular environment.

Drawing on cognitive science, expertise is the process of continually forming new mental representations about a job and a domain, which manifest in several ways: you **see differently** (an expert scanning a long crash report locates the plausible failure points immediately, an intern doesn't); you see **deep structure rather than surface patterns**; you know **everything is conditional** — every rule carries preconditions to learn, plus exceptions where you can bend the rule against reality; and **judgment and taste**, much discussed lately, come from here too. Roughly: expertise is a **world model** of that micro-world, and it underwrites perception, reasoning, and decision-making.

The sharpest contrast is directional. Intelligence is **expansive**: it looks for context on the fly, expands its search, and because it can't accumulate from the past, it consumes enormous quantities of tokens (NeoCognition, he notes, burns millions of dollars in tokens). Expertise is **contractive**: forming shortcuts and effective structures of the domain that reduce the search space.

#### A unifying definition of continual learning (~02:29–02:30)

Continual learning is a confusing term, so he offers one definition:

> **Continual learning is the process of adaptive compression of experience into reusable structures for future behavior.**

All four elements matter, and any continual-learning work should be interrogated on each: *what experience*, *how compressed*, *into what structure*, *used how for future behavior*. Adaptivity is especially important — what you compressed in the past should determine how you compress in the future.

#### The core claim (~02:30–02:32)

Put intelligence on the x-axis and expertise on the y-axis; they're largely orthogonal. More intelligence without continual learning yields **the world's smartest novice**, brute-forcing every problem with raw intelligence — hence the exploding token bills. Different continual-learning algorithms set the **slope** of your learning.

From which follows the future he finds most interesting: **unbounded expertise from bounded intelligence**. Suppose there's an intelligence threshold — call it **escape intelligence**. Cross it, add a strong continual learning algorithm, and you get near-unlimited expertise, or at least good enough for 90–95% of the world's jobs.

That would mean a **strong bifurcation of the market**: frontier labs keep building more intelligent models, with plenty of use cases for them, but for the other 90–95% of jobs we may not need smarter models at all — current ones may be good enough, and what's left is continual learning.

#### Closing: expertise as the next scaling dimension (~02:32–02:33)

Explicitly: the goal of scaling expertise is **not to replace human labor** — he doesn't believe the job-displacement narrative. He thinks we're in a severe **shortage of expertise**. In an ideal world everyone gets personal health care, a personal financial advisor, personal tutoring. Every company gets to build its own **local human–AI learning loop** where knowledge and IP accrue. And making expertise abundant lowers the friction on many problems, pushing them across the threshold of being worth doing at all — which creates a great deal of new opportunity in society.

### Quotes

> "Humans don't need an FDE to teach us how to do a job." (~02:22)

The framing question of the whole talk: if the models are that smart, why is there a forward-deployed-engineer industry?

> "Every company is special. That's why they exist." (~02:25)

The micro-worlds hypothesis in one line — corporate idiosyncrasy isn't noise, it's the reason the company exists, and it's why a single static model can't absorb it.

> "If you can get more intelligent models, but if you don't have continuous learning, then it will become what I call the world's smartest novice." (~02:31)

The talk's most memorable label, and a direct explanation of the token-bill problem.

> "Unbounded expertise from bounded intelligence." (~02:31)

The central thesis, and his prediction of a bifurcated market.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| NeoCognition | 講者共同創辦並擔任 CEO 的 AI 研究實驗室,做持續學習與專家型 agent | Speaker's AI research lab; continual learning and expert agents | 2026 年 4 月以 $40M 種子輪 出隱身 / emerged from stealth April 2026 with a $40M seed |
| MIT NANDA 企業 AI 報告 / MIT NANDA enterprise AI report | 指出企業 AI 導入大量失敗;講者說 95% 這數字可爭論但方向正確 | Reported widespread enterprise AI pilot failure; he grants the 95% figure is arguable but directionally right | 字幕聽成 "the Netherland project" |
| Dwarkesh podcast(「decade of agents」論點) | 主張 2025 不是 agent 元年而是 agent 十年的開端,點名 computer use 與 continual learning | The "not the year of agents, the decade of agents" argument, calling out computer use and continual learning | 字幕聽成 "dash podcast";講者未指名受訪者 / speaker didn't name the guest |
| Moravec's paradox | 1980 年代命題:對 AI 而言難事易、易事難 | 1980s claim that hard things are easy for AI and easy things are hard | 字幕聽成 "Maravx paradox" |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Yu (只念了名) | Yu Su |
| Neocognition | NeoCognition |
| the Netherland project | MIT NANDA(企業 AI 報告)/ the MIT NANDA report |
| dash podcast | Dwarkesh (podcast) |
| Maravx paradox | Moravec's paradox |
| four deployed engineers / FDs | forward deployed engineers / FDEs |
| language village world | linguistic world |
| a language agents ... "continue learning" | continual learning |
| word model | world model |
| hoggenous | heterogeneous |
| printing conditions | preconditions |
| acrewance | accrual / accrue |

## 待確認 / To Verify

- 開場提到「今天早上剛宣布解開 10 個懸而未決的重大數學問題」——字幕作 "open just came out",實驗室名稱與事件細節待查證。/ The lab and event behind "this morning [they] came out with solving 10 other major math problems".
- Dwarkesh podcast 上主張「decade of agents」的受訪者姓名(講者說 "to a degree that last year went on the dash podcast",字幕嚴重失真,人名不可辨)。/ The guest who argued for the "decade of agents" — the name is unrecoverable from the captions.
- 他跳過的那頁「open questions」投影片內容(講者說 "I'll skip this one, these are some open questions we can answer")。/ Contents of the skipped open-questions slide.
- Anthropic 營收曲線的具體出處/數字(講者只以投影片指涉)。/ Source for the Anthropic revenue ramp chart.
