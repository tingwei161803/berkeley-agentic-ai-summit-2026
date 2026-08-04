---
title: "Off-the-Shelf AI Hit a Wall. Here's What HubSpot Did to Solve It."
title_zh: "現成的 AI 撞牆了:HubSpot 怎麼解"
speaker: "Duncan Lennox"
affiliation: "Chief Product & Technology Officer, HubSpot"
type: talk
stage: Plenary
date: 2026-08-02
session: "Session 1: Enterprise AI"
video: "https://www.youtube.com/watch?v=UdS3iisKhCk&t=3054s"
video_range: "00:50:54–01:04:30"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 2nd - Morning Session [DownSub.com].srt"
status: draft
tags: [enterprise, hubspot, agent-harness, context-engineering, evaluation]
---

# 現成的 AI 撞牆了:HubSpot 怎麼解(Off-the-Shelf AI Hit a Wall. Here's What HubSpot Did to Solve It.)

**一句話總結**:HubSpot 三年前發現現成的 co-pilot 撐不住自家規模,於是自建 harness、把公司自己的 context 灌進去,結果工程團隊的 AI 採用率從 80% 走到 100%、速度提升 51%→60%、可靠度不降反升;更意外的是,這些「怎麼用 AI 做東西」的教訓,幾乎原封不動變成了「該替客戶做什麼東西」。
**One-line summary**: Three years ago HubSpot found off-the-shelf co-pilots couldn't hold up at their scale, so they built their own harness and backfilled their own context into it — engineering adoption went 80% → 100%, velocity gains 51% → 60%, and reliability went *up*, not down; the unexpected part was that everything they learned about building *with* AI turned into what they needed to build *for* customers.

## 中文筆記

### TL;DR

- **三個教訓**:(1) 有彈性的基礎設施(自建 harness、可換模型的抽象層);(2) 完整且可信的 context;(3) 到客戶所在的地方去(meet customers where they are)。
- **不強迫,用數據說服**:他們沒有規定工程師必須用 AI。最大的阻力是工程師擔心可靠度受損——所以他們拿數據證明可靠度**維持中性**,後來甚至**上升**。
- **模型選擇不是二選一,而是三維權衡**:quality、latency、cost,**且是這個優先順序**。因為每一項 go-to-market 任務對這三者的價值主張都不同——大宗低風險任務可以先做成本優化,高風險任務(例如會直接接觸「客戶的客戶」的動作)則不能妥協。
- **context 的難點不是塞不塞得下**:不只是 context window 上限或 context drift,更是一個 **overfitting 問題**——丟太多、品質差、對當下任務不夠具體的 context,結果反而更爛。
- **共用平台會複利**:「任何人建的每一個 agent,都會讓所有 agent 更好」,因為它同時貢獻了 context 與平台能力本身。
- **放棄把客戶鎖在自家 UI**:深度整合進 Claude、Gemini、ChatGPT,讓客戶在他們原本工作的地方就能用到 HubSpot 的 agent 平台與 context;自家 web / mobile UI 與 Breeze assistant 維持完整功能對等。

### 重點整理

#### 背景與問題(約 00:52–00:53)

HubSpot 上個月剛過 20 週年,做的是 go-to-market 平台——服務中小企業與部分大型企業的行銷、業務、客服團隊。今天有超過 **300,000 家企業**、約 **140 個國家**、橫跨數十個產業在用,所以他們看得到各種規模與地區公司的實況。

客戶現在問的問題,關鍵在多出來的那個副詞:「我到底要怎麼**真的**用 AI 轉型?」——不是跑試點、不是玩玩,而是為公司**大規模交付真實價值**。他們三年多的結論是:**工具與工具鏈只是起點,不夠;怎麼做才是差別所在。**

而且有個意外收穫:他們一開始問的是「怎麼用 AI 換一種方式做開發」,結果這些教訓大量適用於「該替客戶做什麼、怎麼在客戶的旅程上接住他們」。

#### 教訓一:有彈性的基礎設施(約 00:53–00:59)

**撞牆點**:2023 年左右他們從 code assist 往早期 co-pilot 走,但**現成系統撐不住他們的規模**——當時每天約 **100 萬次 build**、超過 **10,000 個微服務**(現在更多)。問題核心是:模型很懂一般的 coding 問題,但**不懂他們的業務與工作方式**。選擇是等工具廠商追上,或自己下去解——他們選了後者。

做法:

- 在 MCP 非常早期就建了一批 **MCP 整合**,把環境知識直接帶進 co-pilot。
- 很早就建了現在會叫做 **agent execution platform / agent harness** 的東西:容器化架構,能輕鬆開出 sandbox 讓測試迴圈**全自動跑、不需人介入**,對工程師來說很輕量,對可靠度與資安來說也安全。
- **不強制使用 AI**。他們想讓工程師自己被說服。最大的阻力是可靠度——平台對 go-to-market 團隊與客戶是 mission-critical,工程師擔心生成的程式碼會拖垮它。於是他們**拿數據說話**:早期使用區域的資料顯示可靠度**維持中性**;而今天,可靠度其實是**上升**的。
- 成果(三年前):約 **80% 採用率**、整體生產力與速度提升約 **51%**。他特別說明這是**複合指標**,刻意不只看 PR 數或程式碼行數,以免過度轉向單一指標。

**外推到客戶端的教訓**:不能依賴單一廠商或單一模型家族。模型不只一直在進步(有點像賽馬),更重要的是它們**在不同領域是參差的(jagged)**;套到 go-to-market 這種很具體的領域,不同模型、不同尺寸、不同廠商各有勝場,**right tool for the right job**。

所以他們很早就需要能跑 eval、對模型與尺寸做 A/B test 的能力。而判準不是單純的「品質」或「eval 分數」,而是 **quality、latency、cost 三者的組合,而且是這個優先順序**。因為他們替數百種 go-to-market 任務建 agent,每一種任務對這三者的價值主張都不同:有些是低風險的大宗流程,品質門檻仍高但成本優化很早就很重要;有些則是高風險——特別是 HubSpot 平台要去跟**客戶的客戶**互動的時候。

於是他們建了**抽象層**(今天會叫它 agent harness),2026 年的版本比 2023 年成熟得多。它讓他們在底層直接換模型、跑 eval、做回歸測試與比較;而且刻意設計成**讓 feature team 完全不必碰底下的管線**——團隊自己建 eval、對多個模型跑、換進換出而不出現回歸,全程不需要理解底層。

**收斂成一句話:共用地基要先做,不要最後做。** 精實或求快的直覺會讓人「一套 stack 打天下」,但他們的經驗相反:**前期花在 harness 上的力氣,換來的是對自己命運的掌控權**——能做 eval、能換模型、能改 agentic loop 的跑法。而且今天做這件事容易多了,市面上有很多好方案(他點名 Fireworks)。

#### 教訓二:完整且可信的 context(約 00:59–01:02)

當他們從 co-pilot 走到**自主的 coding agent**,agent 需要理解 codebase、慣例與整個環境;而他們有十年份的自建工具鏈。這裡**連 MCP 都不夠**——要讓 coding agent 理解 build chain 的一切,他們投入大量心力在**回填 context**,這才是從前沿模型身上多榨出效能的關鍵。

**context 很難,而且難在意想不到的地方**:不只是撞到 context window 上限或處理 context drift,更是一個 **overfitting 問題**——如果你只是丟一大堆 context,而品質不好、對當下任務不夠具體,結果反而更差。把這件事做對,本身就是一項值得養成的技能與平台能力。

- **內部成果**(2025 年初):**96% 的工程師在用 AI**,速度提升 **60%**。
- **客戶端**:go-to-market 旅程上有大量不同任務與 agent(prospecting agent、customer support agent⋯),**在對的時間給對的 context** 能顯著改善品質、效能與成本。最具體的例子:一個「demo 後續追蹤信」的 agent,**六個月內**從「業務約三分之二的時候需要改寫(調整語氣或修正錯誤)」變成「約三分之二的時候直接原封不動寄出」。

他的總結:**AI 懂世界懂得很多,但你需要一個懂你的世界的平台。** 而那些資料,大多只存在你公司內部,不在外面的世界裡,因此也不在模型裡。

#### 教訓三:到客戶所在的地方去(約 01:02–01:04)

**對內**:共用工具、共用原語、建在共用平台上。「**任何人建的每一個 agent,都會讓所有 agent 更好**」,因為它同時貢獻了整體 context 與 agent 平台本身。成果:

- **100% 的工程師**用 agentic coding 開發
- 程式碼行數 **+73%**
- PR 首次回饋時間 **-90%**
- 速度上升的同時,**品質與可靠度也在上升**

**對外**:身為 SaaS 廠商,歷史上你會想著「怎麼把客戶留在我的 UI 裡」——**他們完全放掉了這件事**。真正要交付的價值是「讓我們建立的智慧,在客戶工作的任何地方都不可或缺」。所以他們**深度整合進 Claude、Gemini 與 ChatGPT**,讓客戶在那些地方就能拿到 HubSpot agent 平台的完整能力與 context。當然很多客戶仍選擇用 web / mobile UI 或自家的 **Breeze assistant**——這幾條路線維持**完整的功能對等**。

**結語**:地基沒打好,曲線會 plateau;地基一旦到位,就會出現**複利式的威力**,不只改變團隊怎麼做東西,也放大了能交付給客戶的價值。

### 金句

> "AI knows a lot about the world, but you need a platform that knows your world."(約 01:01)

整場最凝練的一句——context engineering 的商業版本。

> "Do that first, not last."(約 00:58)

指共用地基(harness、eval、抽象層)。他明說這與「先求 MVP、單一 stack 打天下」的直覺相反。

> "Every agent anybody builds makes all agents better."(約 01:02)

共用平台的複利效果:每個 agent 都同時貢獻 context 與平台能力。

> "It's not a matter of just hitting a context window limit or dealing with context drift. It's also the fact that there's effectively an overfitting problem."(約 01:00)

對 context engineering 難點最精準的診斷:多不等於好。

## English Notes

### TL;DR

- **Three lessons**: (1) flexible infrastructure — build your own harness and a model-swappable abstraction layer; (2) comprehensive and trustworthy context; (3) meet customers where they are.
- **They never mandated AI — they brought data.** The biggest blocker was engineers worrying that generated code would hurt reliability, so they showed the data: reliability stayed neutral, and today it's actually *improving*.
- **Model choice is a three-way tradeoff, in priority order: quality, latency, cost.** Every one of the hundreds of go-to-market tasks they build agents for has a different value proposition across those three — bulk low-stakes work makes cost optimization matter early; high-stakes work (especially anything touching a customer's customer) does not.
- **The hard part of context isn't capacity.** Beyond context-window limits and context drift there's an **overfitting problem**: dumping in a lot of context that isn't high quality or specific enough to the task at hand makes results worse.
- **A shared platform compounds**: "every agent anybody builds makes all agents better," because each one contributes both to overall context and to the platform itself.
- **They gave up on keeping customers inside their own UI**, integrating deeply into Claude, Gemini and ChatGPT so customers get the full agent platform and context wherever they already work — with full parity against the web/mobile UIs and their own Breeze assistant.

### Key Points

#### Context and the question customers actually ask (~00:52–00:53)

HubSpot just turned 20 last month. They build a go-to-market platform for largely small and medium-sized businesses plus enterprises — software for marketing, sales and service teams across the full go-to-market journey. Over **300,000 businesses** in about **140 countries** across dozens of industries depend on it, which gives them a wide view of what's actually happening at different scales and in different regions.

The question they hear is defined by one inserted word: "How do I **actually** transform with AI?" Not run pilots, not play around — deliver real value at scale. Three-plus years in, their finding is that **the tools and tool chains are just a starting point; how you approach it makes the difference.**

And the unexpected part: they started by asking how to *build differently with* AI, and most of those learnings turned out to apply to what they needed to *build for* customers.

#### Lesson 1: flexible infrastructure (~00:53–00:59)

**Where they hit the wall.** Around 2023 they moved past code assist into early co-pilots — and off-the-shelf systems couldn't work at their scale: roughly **a million builds a day** across **10,000+ microservices** at the time (more now). The core issue was that models understood coding problems generally but didn't understand enough about their business and how they work. They could wait for the tooling companies to catch up, or dive in themselves. They chose to dive in.

What they built:

- A set of **MCP integrations** in the very early days of MCP, bringing knowledge of their environment directly into the co-pilots.
- What they'd now call an **agent execution platform / agent harness**: a containerized approach making it easy to spin up sandboxes where test loops run **entirely automated, without human intervention** — lightweight for engineers, and safe from both a reliability and a security standpoint.
- **No mandate.** They deliberately didn't require engineers to use AI; they wanted engineers to see how different and powerful the experience is and adopt it themselves. The big blocker turned out to be reliability concerns — the platform is mission-critical for go-to-market teams and customers, and engineers feared regression. So they **brought data**, showing from the early adoption areas that reliability stayed neutral. Today, reliability is actually *increasing* as a result of how they code.
- Result three years ago: about **80% adoption** across thousands of engineers, and roughly a **51% improvement** in productivity and velocity — deliberately a **composite metric**, because they don't want to over-rotate on any single one like PRs or lines of code.

**What generalized to customers**: you can't depend on a single vendor or model family. Models keep improving — it's a bit of a horse race — but more importantly they're **jagged across different areas**. Applied to something as specific as go-to-market, different models, sizes and vendors win in different places: right tool for the right job.

So they were early to needing evals and A/B tests across models and sizes — and the criterion isn't simply "quality" or an eval score, but a mix of **quality, latency and cost, in that order of priority**. Each of the hundreds of go-to-market tasks they build agents for weighs those three differently: some are low-stakes bulk processes where the quality bar is still high but cost optimization matters very early; others are high-stakes, particularly when the HubSpot platform is about to do something that interacts with **one of their customers' customers**.

Hence the **abstraction layer** — today they'd call it an agent harness, far more sophisticated in 2026 than in 2023. It lets them swap models under the hood, run evals, and do regression tests and comparisons. Crucially it was built so **feature teams never touch the plumbing**: they create their evals, run them against a variety of models, and swap models in and out without regressions, with no involvement in any of the underlying machinery.

**The takeaway: do the shared foundation first, not last.** When you're trying to move fast or reach MVP, there's a temptation to use a single stack for everything. Their experience runs counter to that — the energy invested up front in harnesses buys **much more control over your own destiny**: the ability to run evals, swap models, and change how an agentic loop runs. It's also far easier to do today; he names Fireworks as one of the companies doing great work here.

#### Lesson 2: comprehensive and trustworthy context (~00:59–01:02)

Moving from co-pilots to **autonomous coding agents**, the agents needed to understand the codebase, the conventions and the environment — against a decade of homegrown tooling. Here they had to **get beyond even MCP**, letting coding agents understand everything about how the build chain worked. Most of the effort spent extracting more effectiveness from even frontier models went into **backfilling that context**.

**And getting context right is hard.** It's not just hitting a context-window limit or dealing with context drift; there's effectively an **overfitting problem** — throw in too much context whose quality and task-specificity aren't good and you get poor results. Getting that right turned out to be a skill worth building and a genuinely valuable platform capability.

- **Internally** (early 2025): **96% of engineers using AI**, at a **60% improvement** in velocity.
- **For customers**: across the go-to-market journey there are many different agents — prospecting, customer support and more — and **delivering the right context at the right time** drives significantly better quality, performance and cost. The sharpest example: an agent that drafts the follow-up outreach email after a sales demo went, in about **six months**, from a rep needing to edit it about two-thirds of the time to a rep sending it unedited about two-thirds of the time.

His summary: **AI knows a lot about the world, but you need a platform that knows your world** — and most of that data exists only inside your business, not out in the world and therefore not in the models.

#### Lesson 3: meet customers where they are (~01:02–01:04)

**Internally**, this meant shared tools, shared primitives, one shared platform: "**every agent anybody builds makes all agents better**," because each one contributes both to overall context and to the agent platform itself. Results:

- **100% of engineers** using agentic coding to build at HubSpot
- **+73%** lines of code
- **−90%** time to first feedback on PRs
- velocity rising while quality — and reliability — rose too

**Externally**, as a SaaS vendor you'd historically think about how to keep customers inside your own UI. **They let go of that entirely.** The value to deliver was making the intelligence they build indispensable wherever customers work — so they integrate deeply into **Claude, Gemini and ChatGPT**, putting the full power of their agent platform and context right where the customer already is. Many customers still choose the web or mobile UIs, or their own **Breeze assistant**, and they maintain full parity across all of them.

**Closing**: without the foundational pieces, things plateau. Once they're in place you get compound interest — value that shows up both in how the teams build and in what they can deliver to customers.

### Quotes

> "AI knows a lot about the world, but you need a platform that knows your world." (~01:01)

The most compressed line of the talk — context engineering stated as a business proposition.

> "Do that first, not last." (~00:58)

On the shared foundation (harness, evals, abstraction layer). He's explicit that this cuts against the lean/MVP instinct to use one stack for everything.

> "Every agent anybody builds makes all agents better." (~01:02)

Why the shared platform compounds: each agent contributes context *and* platform capability.

> "It's not a matter of just hitting a context window limit or dealing with context drift. It's also the fact that there's effectively an overfitting problem." (~01:00)

The most precise diagnosis of why context engineering is hard: more is not better.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| HubSpot | go-to-market 平台,300,000+ 企業客戶、約 140 國,2026 年 7 月屆滿 20 週年 | Go-to-market platform, 300,000+ businesses in ~140 countries; 20th anniversary in July 2026 | |
| Breeze | HubSpot 自家的 AI assistant | HubSpot's own AI assistant | 與 Claude / Gemini / ChatGPT 整合維持功能對等 / full parity with the Claude / Gemini / ChatGPT integrations |
| Agent harness(自建) | 讓底層可換模型、跑 eval 與回歸測試的抽象層,feature team 不需碰管線 | In-house abstraction layer for swapping models, running evals and regression tests without feature teams touching plumbing | 2023 年就有雛形,2026 年版本成熟許多 / first built in 2023, far more sophisticated by 2026 |
| MCP | 早期用來把自家工具鏈知識帶進 co-pilot | Used early to bring their tool-chain knowledge into co-pilots | 後來發現「連 MCP 都不夠」/ they later had to get beyond even MCP |
| Fireworks | 他點名在 agent 基礎設施領域做得很好的公司 | Named as doing great work in the agent-infrastructure space | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| trustworthy worthy | trustworthy |
| spin spin up | spin up |
| gotom market / go to market | go-to-market |
| chatgpt | ChatGPT |
| breeze assistant | Breeze assistant |
| eval(單複數混用) | evals |
| gro | grok(理解,動詞) |

## 待確認 / To Verify

- 「約 80% 採用率 / 51% 速度提升」「96% / 60%」「100% / +73% lines of code / −90% time to first feedback」等數字,均為講者口述,未見投影片來源,建議對照影片畫面確認。/ All adoption and velocity figures are spoken numbers; cross-check against the slides on video.
- 「一天約一百萬次 build、超過 10,000 個微服務」為 2023 年當時的數字,現值講者僅說「更多」。/ The million-builds-a-day and 10,000-microservices figures are from 2023; he only says the current numbers are higher.
