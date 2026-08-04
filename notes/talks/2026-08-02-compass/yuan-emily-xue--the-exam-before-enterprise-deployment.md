---
title: "The Exam Before Enterprise Deployment"
title_zh: "企業部署前的那場考試"
speaker: "Yuan (Emily) Xue"
affiliation: "Head of Enterprise AI, Scale AI"
type: talk
stage: Compass
date: 2026-08-02
session: "Session 4: Agent Evaluation & Benchmarks"
video: "https://www.youtube.com/watch?v=1UrriPJRSPU&t=7119s"
video_range: "01:58:39–02:11:10"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [enterprise, evaluation, deployment-readiness, human-oversight, benchmarks]
---

# 企業部署前的那場考試(The Exam Before Enterprise Deployment)

**一句話總結**:現有 benchmark 量的是「天花板」——模型離人類智慧頂點還差多遠,而且刻意不讓自己被刷爆;企業要的卻是「部署就緒度」——這個 use case 今天能不能上線、要花多少人力監督成本才能撐到 99% 可靠度,以及隨著模型變好那筆成本怎麼降。可靠度是約束,不是可以交換的變數。
**One-line summary**: Today's benchmarks measure a *ceiling* — how far models are from the top of human intelligence — and are deliberately kept from saturating; enterprises need the opposite measurement, *deployment readiness*: can this use case ship today, what human-oversight cost buys the 99% reliability it requires, and how does that cost fall as models improve. Reliability is a constraint, not a tradeable variable.

## 中文筆記

### TL;DR

- **Benchmark 開發者和企業買家對「低分」的感受完全相反**:benchmark 分數低,模型開發者覺得興奮(有努力空間);企業主管看到 text-to-SQL benchmark 天花板只有 60–70% 只會困惑——「大家都說 agent 這麼聰明了,為什麼做不到 99%?」而 benchmark 之所以不讓自己飽和,是因為一旦飽和就沒人用了。
- **兩件事要分開**:現有 benchmark 量的是 **capability**(面向模型開發者,模型互相競爭);企業採用需要的是 **deployment readiness**(這個 use case 能不能部署、要付出什麼才能部署)。
- **五個評估 primitive**:答案可信嗎(grounding:citation precision + 證據涵蓋率/recall)、有沒有遵守內規(policy compliance)、agent 知不知道自己不知道(信心校準 + abstention)、寫入操作是否可回復(rollback policy)、以及人力監督的經濟性。
- **醫療案例最有代表性**:agent 該查檢驗數值裡的 creatinine 上升來判斷急性腎損傷,結果它抄捷徑直接讀電子病歷的診斷紀錄。**答案可能對,流程卻違反臨床規定**——這是純看答案正確率永遠抓不到的失敗。
- **改善路徑不是把分數從 60% 推到 90%,而是經濟結構的變化**:初期需要重度人力監督,隨模型變好,達成同樣可靠度所需的每任務成本下降。**可靠度不能交換,能交換的是「人與 agent 怎麼協作」的政策**。

### 重點整理

#### 講者背景與問題設定(約 01:59–02:00)

Xue 現在在 Scale AI 負責企業內的 AI 功能,大量接觸企業客戶。加入 Scale AI 之前,她在 Google 待了 11 年,是 Gemini 團隊的核心成員;除了參與 Gemini 開發,**與本場最相關的經歷是她組建團隊為 Gemini 做 cloud agent benchmark**。

她的前提很簡單:AI 的價值必須落地成生產力、產生真實經濟影響,而**只要 AI 停在 demo 與 pilot,這件事就不會發生**。所以整場演講就談一件事:從 pilot 走到 production,中間的把關決策是什麼?核心問題只有一句——**「這個 agent 能不能可靠地部署到我的組織裡做有用的工作?」**

#### Benchmark 量的是天花板,企業要的是地板(約 02:00–02:02)

現在外面有數百個 benchmark。但如果你仔細看,會發現**它們量的都是「天花板」**:模型當下能力與人類智慧頂點之間的差距。

這造成一種奇特的視角錯位:

- **benchmark 開發者**的客戶是模型開發者。分數低,他們反而興奮——代表有 gap、有空間、有事情可做。
- **企業買家**看到同一個分數,反應完全相反。

她分享了一個 text-to-SQL 的真實案例:企業主管無法理解,既然大家都說 agent 現在這麼聰明,為什麼你的 agent 做不到 99% 可靠度?研究員於是把 text-to-SQL 的 benchmark 拿給他們看——**頂尖成績也只有 60–70%**。

而這個天花板是刻意的:**benchmark 不希望自己飽和,一旦飽和就沒人用了**。但企業的現實需求恰恰是把那個數字推到 95–99%。

這就是落差所在:**現有 benchmark 測的是 capability,是面向開發者的競技場;企業採用需要的是 deployment readiness——這個 use case 準備好上線了嗎?要讓它上線需要付出什麼?**

#### 企業買家真正會問的五個問題(約 02:02–02:03)

1. **今天有什麼是能上 production 的?** 我手上有一串優先事項,哪些難、哪些相對已經可以部署?
2. **我要怎麼量化「就緒度」?** 就緒是個概念,怎麼變成數字,又怎麼信任這個數字?
3. **如果有落差,怎麼補?** 假設是 90%,不管怎麼量的,我不可能拿 90% 上線面對客戶,我需要 99.9%。這 10% 怎麼補?
4. **人力監督政策該怎麼訂?** 現實裡永遠有 human oversight,問題是「用什麼樣的監督政策」才能撐到目標可靠度。
5. **成本划得來嗎?** 這邊燒 token,那邊付人力,加起來我這個 AI 專案到底有沒有省到錢?

歸納成一份 **readiness profile**:qualification(資格認定)、risk envelope(風險邊界)、oversight policy(監督政策)、improvement path(改善路徑)。

#### 五個評估 primitive(約 02:04–02:07)

**1. 答案可信嗎?——grounding**

沒什麼祕密,就是 grounding:答案裡的每一條資訊,**citation precision** 夠不夠?它有沒有 grounded 在某個來源上?反過來還有 **recall** 問題:證據資料庫裡該涵蓋的東西,有沒有漏掉?

**2. 有沒有遵守內部政策?——policy compliance**

很多時候 agent 給了正確答案,但**它有沒有照我的內規做事**?

她舉了一個醫療客戶的具體案例:任務是為臨床安全事件做品質稽核,要準確辨識**急性腎損傷**。臨床規定的做法是:**看檢驗數據,看 creatinine 的上升幅度**。

但部署後他們發現,**agent 變聰明了,它抄了捷徑**——它沒有去檢驗數據裡撈 creatinine,而是直接去讀電子病歷系統裡的臨床紀錄與診斷紀錄,從那裡判斷這個病人有沒有急性腎損傷。

**它沒有遵守臨床環境指定的作業流程。** 這是一個必須被處理的問題,而且只看最終答案對不對永遠測不出來。

**3. Agent 知不知道自己不知道?**(她說這是她最愛的問題)

兩件相關的事:

- **信心校準(confidence calibration)**:agent 常說「我有 60% 把握」,但它真的在 60% 的情況下答對嗎?自稱的信心必須對照現實校準。
- **更重要的是 abstention 政策**:如果它不知道,我們得給它一個政策——**什麼時候該停下來不給答案、該說「我需要人接手」、該把案子轉出去**。

**4. 寫入操作(write operations)**(約 02:07)

這是 agent 系統與傳統企業系統交界的地方。重點不只是你自己系統的安全與可靠——而是**當 agent 的操作真的打進企業系統時**:你怎麼變更狀態?**這個變更可回復嗎?rollback 政策在哪裡?**

**5. 人力監督的經濟性(oversight economics)**

如果流程裡有人力監督,人 + agent 合起來,這筆帳到底划不划算。

#### 把 primitive 收進框架:三個互動介面(約 02:07–02:09)

這是他們**即將發布的 benchmark**(當月推出)所採用的切分方式,依「agent 系統與外界互動的介面」來組織:

| 介面 Surface | 互動性質 | 要驗證什麼 |
|-------------|---------|-----------|
| **1. 讀取 / 供人審閱** | 取得資訊交給人類審查 | 答案是否可信;搭配 human review policy |
| **2. 寫入企業系統** | agent 系統變更企業系統狀態 | 變更是否可回復、可信;是否 privacy-preserving、不外洩資訊 |
| **3. 開放對話** | 直接面對企業的終端客戶 | 輸入來自開放空間的使用者,可能是惡意的或規格不清的;你要如何**引導對話**達成目標 |

最後由一份 **deployment profile** 回答一整組(七個)問題。

#### 結論:改善路徑是經濟學,不是分數(約 02:09–02:11)

她最想強調的兩點:

**第一,企業要的不是一個分數。** 企業真正想知道的是兩件事:(a) **這個 use case 準備好了嗎?** (b) **經濟結構長什麼樣——我要付多少成本、建立什麼樣的人力監督政策,才能達到我需要的可靠度?**

**第二,改善路徑不是分數的改善。** 不是「我把分數從 60% 拉到 80%、90%」,而是**經濟結構的改變**:一開始你需要很重的人力監督;隨著模型品質提升,**你為同一個任務付出的成本會持續下降**。

她給出全場最鋒利的一句框架:**我們被可靠度約束住了,而可靠度不是可以拿來交換的東西。可以交換的是「政策」——人與 agent 要怎麼以可信的方式一起工作。**

### 金句

> "When the benchmark is saturated, people don't use it anymore."(約 02:01)

一句話解釋了為什麼企業永遠在公開 benchmark 上看到令人失望的天花板——那個天花板是設計出來的。

> "The agent has become smart. It does a shortcut."(約 02:05)

急性腎損傷案例的核心:agent 的「聰明」正是它繞過臨床規定的方式。答案對,流程錯。

> "Does the agent know what it doesn't know?"(約 02:06)

她自己說這是她最喜歡的問題:拆成信心校準與 abstention 政策兩件事。

> "We are constrained by reliability. Reliability is not something you can trade off. What is trade-off is what's the policy."(約 02:10)

整場演講的結論句。

> "Don't only ask how intelligent the agent is. Ask what it's ready to do, under what constraint, what's the risk, and what's the cost."(約 02:10,最後一張投影片)

## English Notes

### TL;DR

- **A low benchmark score means opposite things to benchmark builders and enterprise buyers.** Model developers see a low score and get excited — there's a gap, there's work to do. An executive who sees that the best text-to-SQL benchmarks top out at 60–70% is simply baffled: everyone says agents are brilliant now, so why can't mine hit 99%? Benchmarks stay unsaturated on purpose, because a saturated benchmark stops being used.
- **Two different measurements.** Existing benchmarks measure **capability** — developer-facing, models competing against each other. Enterprise adoption needs **deployment readiness**: can this use case ship, and what does shipping it take?
- **Five evaluation primitives**: can we trust the answer (grounding — citation precision plus evidence recall), does it comply with internal policy, does the agent know what it doesn't know (confidence calibration plus abstention), are write operations recoverable (rollback policy), and does the oversight economics work.
- **The healthcare example is the sharpest one.** The agent was supposed to identify acute kidney failure by reading lab measurements and checking the rise in creatinine. Instead it took a shortcut and read the diagnosis notes in the EMR. **The answer may be right and the process still violates clinical policy** — a failure mode that pure answer-accuracy will never surface.
- **The improvement path is economic, not a score.** It isn't 60% → 80% → 90%. It's that you start with heavy human oversight and, as model quality improves, the cost of hitting the same reliability target falls. **Reliability is a constraint you can't trade away; what you trade is the policy for how humans and agents work together.**

### Key Points

#### Background and framing (~01:59–02:00)

Xue leads AI functionality for enterprise at Scale AI and spends much of her time with enterprise customers. Before Scale she spent 11 years at Google as a core member of the Gemini team — and, most relevant to this talk, **built the team that produced Gemini's cloud agent benchmark**.

Her premise: AI's value has to land as productivity and real economic impact, and **that will not happen while AI stays in demos and pilots**. So the talk is about the gating decision between pilot and production, which reduces to one question: **can this agent be reliably deployed to do useful work inside our organization?**

#### Benchmarks measure the ceiling; enterprises need the floor (~02:00–02:02)

There are hundreds of benchmarks out there. Look closely and **they all measure a ceiling** — the gap between what a model can do now and the top of human intelligence.

That creates a perspective mismatch:

- **Benchmark developers** serve model developers as their customers. A low score is exciting: it means headroom.
- **Enterprise buyers** see the identical number and react in the opposite direction.

Her anecdote comes from a text-to-SQL use case. Executives couldn't understand why the agent wasn't at 99% reliability when everyone insists agents are so smart now. So the researchers showed them the text-to-SQL benchmarks — where the state of the art is **60–70%**.

And that ceiling is deliberate: **nobody wants their benchmark to saturate, because a saturated benchmark gets abandoned.** But the enterprise need is precisely to push that number to 95–99%.

Hence the gap: **current benchmarks measure capability, a developer-facing competition; enterprise adoption needs deployment readiness — is this use case ready, and what will it take to get it there?**

#### The five questions enterprise buyers actually ask (~02:02–02:03)

1. **What is ready for production today?** I have a list of priorities — which are hard, which are relatively deployable?
2. **How do I measure readiness?** Readiness is a concept; how do I quantify it, and how do I trust the result?
3. **If there's a gap, how do I fill it?** Say it's 90%, however that was measured. I cannot put 90% in front of customers; I need 99.9%. What closes the remaining slice?
4. **What's the human oversight policy?** There is always human oversight in reality; the question is which policy gets me to my target.
5. **Does the cost work?** Tokens on one side, humans on the other — is my AI initiative actually saving money?

Together these form a **readiness profile**: qualification, risk envelope, oversight policy, and improvement path.

#### Five evaluation primitives (~02:04–02:07)

**1. Can we trust the answer? — grounding.** No secret here: for every piece of information in the answer, what's the **citation precision** — is it grounded in a source? And the mirror-image **recall** question: does the answer cover everything the evidence base should have produced, or did it miss something?

**2. Policy compliance.** Often the agent gives a correct answer — but **does it follow my internal policy?**

Her concrete case came from a healthcare customer doing quality auditing for clinical safety events, where the task was to accurately identify **acute kidney failure**. Clinical policy specifies the method: **look at the labs, look at the rise in creatinine.**

What they observed in deployment was that **the agent got smart and took a shortcut** — instead of retrieving creatinine values from lab measurements, it read the clinical and diagnosis notes in the electronic medical record system and decided from there.

**It did not follow the process the clinical environment specified.** That's a real problem to address, and answer-level accuracy alone will never catch it.

**3. Does the agent know what it doesn't know?** (Her favorite question.) Two related pieces:

- **Confidence calibration**: an agent will happily say it's 60% confident — but is it actually right 60% of the time? Self-claimed confidence has to be calibrated against reality.
- **More importantly, an abstention policy**: when it doesn't know, it needs a rule for **when to stop answering and hand off to a human.**

**4. Write operations (~02:07).** This is where the agent system meets traditional enterprise systems. The concern isn't only your own system's security and reliability — it's what happens **when the agent's operations reach into the enterprise system**: how do you mutate state, **is it recoverable, and where is the rollback policy?**

**5. Oversight economics.** With humans in the loop alongside the agent, does the combined economics actually make sense?

#### Organizing the primitives: three interaction surfaces (~02:07–02:09)

This is the structure used in **their upcoming benchmark** (shipping that month), organized by the surface where the agent system meets the outside world:

| Surface | Nature of interaction | What to verify |
|---------|----------------------|----------------|
| **1. Read / information for human review** | Retrieve information for a human to review | Is the answer trustworthy; paired with a human review policy |
| **2. Write into enterprise systems** | Agent system mutates enterprise system state | Is the change recoverable and trustworthy; is it privacy-preserving and non-leaking |
| **3. Open conversation** | Facing the enterprise's end customers directly | Input comes from open-space users and may be malicious or underspecified; how do you **steer the conversation** toward your goal |

A **deployment profile** then answers a full set of seven questions.

#### Closing: the improvement path is economics, not score (~02:09–02:11)

Two points she wanted to leave the room with.

**First, enterprises don't want a number.** They want two things: **(a) is this use case ready?** and **(b) what does the economics look like — what cost, and what human oversight policy, buys the reliability I need?**

**Second, the path to improvement is not score improvement.** It isn't "I moved the score from 60% to 80% to 90%." It's **an economic change**: initially you need heavy human oversight, and over time, as model quality improves, **the cost you pay for the same task keeps falling.**

Her sharpest framing: **we are constrained by reliability, and reliability is not something you can trade off. What you trade off is the policy — how humans and agents work together in a trustworthy way.**

### Quotes

> "When the benchmark is saturated, people don't use it anymore." (~02:01)

One line explaining why enterprises keep seeing disappointing ceilings on public benchmarks — the ceiling is by design.

> "The agent has become smart. It does a shortcut." (~02:05)

The heart of the acute kidney failure case: the agent's cleverness is exactly how it routed around clinical policy. Right answer, wrong process.

> "Does the agent know what it doesn't know?" (~02:06)

Her favorite question, decomposed into confidence calibration and an abstention policy.

> "We are constrained by reliability. Reliability is not something you can trade off. What is trade-off is what's the policy." (~02:10)

The thesis sentence of the talk.

> "Don't only ask how intelligent the agent is. Ask what it's ready to do, under what constraint, what's the risk, and what's the cost." (~02:10, final slide)

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Scale AI 企業部署就緒度 benchmark | 演講中預告、當月發布的 benchmark,以三個互動介面組織評估 | Upcoming enterprise deployment-readiness benchmark organized around three interaction surfaces | 演講時尚未發布,名稱未提 / unnamed and unreleased at talk time — see To Verify |
| Gemini cloud agent benchmark | 講者在 Google 時組建團隊建立的 agent benchmark | Agent benchmark her team built at Google | 背景經歷 / cited as background |
| Text-to-SQL benchmarks | 用來說明「benchmark 天花板 60–70%」的例子 | Cited to illustrate the 60–70% benchmark ceiling | 未點名特定 benchmark(下一場 Grace Tang 提到 Spider 2)/ no specific benchmark named (Grace Tang's following talk names Spider 2) |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Emily Zu | Yuan (Emily) Xue |
| skill AI | Scale AI |
| Jamnai team | Gemini team |
| cryotin | creatinine |
| acutic kidney failure | acute kidney failure |
| electronic micros system | electronic medical record (EMR) system |
| rate operations / right operations | write operations |
| upstain | abstain |
| evaluation services / vulnerability(指三個介面)| evaluation surfaces |
| cloud agent benchmark(Google 時期)| 見待確認 / see To Verify |

## 待確認 / To Verify

- 即將發布的 Scale AI 企業 benchmark 正式名稱(演講中只說「this week / this month」推出)。/ Official name of the upcoming Scale AI enterprise benchmark (she only said it ships "this week / this month").
- 她在 Google 建立的「cloud agent benchmark」正式名稱與是否公開。/ The formal name of the Gemini "cloud agent benchmark" she built at Google, and whether it is public.
- deployment profile 所回答的七個問題的完整清單(她因時間關係說「就照投影片讀」,未逐條念出)。/ The full list of the seven questions in the deployment profile — she skipped reading them aloud for time.
- 醫療客戶案例的可引用出處(Scale Labs 有相關的 patient safety event triage benchmark 論文,但需確認是否為同一項工作)。/ A citable source for the healthcare case; Scale Labs has published work on patient safety event triage benchmarking, but whether it is the same effort needs confirming.
