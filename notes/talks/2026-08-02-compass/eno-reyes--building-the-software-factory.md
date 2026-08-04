---
title: "Building the Software Factory"
title_zh: "打造軟體工廠"
speaker: "Eno Reyes"
affiliation: "Co-Founder / CTO, Factory AI"
type: talk
stage: Compass
date: 2026-08-02
session: "Session 3: Enterprise AI"
video: "https://www.youtube.com/watch?v=1UrriPJRSPU&t=3189s"
video_range: "00:53:09–01:08:37"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [enterprise, software-engineering, agent-platform, governance, evaluation]
---

# 打造軟體工廠(Building the Software Factory)

**一句話總結**:每家公司都有一條「訊號 → 分流 → 規劃 → 寫程式 → 驗證 → 部署 → 產生新訊號」的隱性迴圈,但幾乎沒有人把它顯式建模;「軟體工廠」就是把這條迴圈顯式化並交給 agent 自動流動,而人的新角色是建造、治理與持續改良這座工廠。
**One-line summary**: Every software company already runs an implicit loop — signals in, triage, plan, code, validate, ship, new signals out — but almost nobody models it explicitly; the "software factory" makes that loop explicit so signals can flow to deployed software without human intervention, and the new human job is to build, govern, and refine the factory.

## 中文筆記

### TL;DR

- **寫程式不是難的部分**,是最簡單的部分。企業感受不到「100x 生產力」,是因為只把 AI 塞進整條迴圈中很窄的一段,其餘仍是人驅動的同步工作流。
- **軟體工廠的三個設計主張**:model independent(不把工廠押注在單一模型廠商,要把 model layer 商品化才能拿到成本與品質的 Pareto frontier)、你自己是工廠的主權者(支援 on-prem / airgapped)、以及跨所有工作流共用一個 **shared agent core**,而不是為 code review、incident response 各養一套 agent 架構。
- **阻礙 agent 成功的最大瓶頸是環境,不是模型**。最高槓桿的投資是 dev 可重現性、環境乾淨度、linting、type checking、測試品質——也就是「有沒有足夠多的 deterministic verifiable feedback loop 讓 agent 不必問人就能自我收斂」。
- **治理要先於規模化**:agent 一定會拿到危險權限,「不是 if 而是 when」。要像對待人一樣建立分層管控,而且要把護欄拉到「比現在大 10 倍的組織」該有的水準(5 人團隊要用 50 人公司的控管)。
- **量測 outcome,不要量測 token**:看 cycle time、code shelf life、incident time、bug 數;成本用「每次程式變更的成本」這種類比薪資的方式看。

### 重點整理

#### 什麼是軟體工廠:讓隱性迴圈顯式化(約 00:53–00:57)

三年半來這個領域的演進:autocomplete → chatbot → agent → software factory。所謂軟體工廠,是把公司裡本來就存在的一條迴圈畫出來:各種**訊號**流入(客戶回饋、內部 telemetry、主管說「我們要轉向」),被 triage,然後進入 planning,再到寫程式、驗證、shipping、部署,而部署後被監控的軟體又產生新的訊號。

問題在於:這些訊號今天幾乎都是**人在腦袋裡分流**,從來沒有被顯式表示在任何系統裡;planning 也多半散在 Jira / Notion / Confluence 裡且高度非結構化。所以「這個隱性回饋迴圈在每家做軟體的公司都存在,但幾乎沒有任何地方有它的顯式模型」。

由此他點出為什麼很多公司感受不到 AI 帶來的爆炸性生產力:**你只把 AI 用在這條迴圈裡很窄的一段**,其餘仍是「我叫機器做一件事,它回傳給我」的同步 autocomplete 式互動。真正該問的是:怎麼設計一個讓訊號一路流到 deployed software 而**不需要人介入**的系統?(注意:是不需要人「介入」,不是不需要人。)

#### 系統該怎麼設計:三個主張(約 00:57–01:01)

1. **Model independent**:模型廠商會論證「你必須垂直整合、agent harness 必須跟模型綁在一起」——他說經驗上這明顯不成立。你要把 model layer 聚合並商品化,才拿得到成本與品質的真實 Pareto frontier。
2. **你是工廠的主權者**:即使買的是 SaaS,也要能控制它;Factory 提供 on-prem、airgapped 等形式。理由是「你的軟體工廠就是你的公司」,它必須能在任何廠商來來去去之後繼續運作。
3. **Shared agent core**:軟體工廠要覆蓋產品與工程組織裡的每一個動作——code review、security analysis、testing、documentation、incident response。但如果為每個場景養一套高度特化的 agent 架構,就會掉進一種奇怪的 microservice 化;實際上這些工作流在高層次上都是同一件事:**蒐集資訊 → 在電腦系統上行動 → 回報使用者**。變的是 context 與 workflow,不是 agent 本身。

大型組織還要處理 governance:一致性、防止 agent 去 drop 一堆資料表、IT ops。他主張這是 agent 平台的責任,並給了一個評估廠商的具體方法:**去看它有沒有一頁「enterprise controls / organizational controls」,上面有幾條**;如果沒有數以百計的情境,就該再看看別家。他點名 Docker 近期推出的一套 vendor-neutral agent 控制項清單(約 35 條)是不錯的呈現方式。

#### 最大的瓶頸是環境,不是模型(約 01:02–01:04)

他用人類演化打比方:20 萬年前的人跟現在的我們差不多,但今天先進太多——因為我們**徹底改造了周遭的環境**。同理,你可以等模型變強(它大概會),但**改造 codebase 與工程系統才是槓桿最高的事**:dev reproducibility、環境乾淨度、linting、type checking、測試品質。

真正的判準是:**你的組織裡有沒有足夠多的 deterministic verifiable feedback loop,讓 agent 不必諮詢人類就能成功?** 等 code review 來告訴你「這段程式組織得不好」是一回事;有一個確定性訊號直接說出這件事,agent 就能自己 loop、自己驗證直到過關。

至於權限:agent 終究會拿到危險的存取權,「不是 if,而是 when」。所以要像對待人一樣建立分層控管。他的類比是:公司超過 50–75 人之後你會明白,就算 75 個人都極為能幹,**總有一天會有人 drop 掉資料庫**;引入 agent 等於把組織規模放大 10 倍,護欄也要跟著升級——5 人新創要用 50 人公司的控管,50 人公司要用 500 人的。這些都是既有的軟體開發最佳實務,不必重新發明輪子,只要確保它們被強制套用在 agent 上。

#### 人的新角色與量測(約 01:04–01:08)

人的新工作就是**觀察 → 介入 → 迭代改良**這座工廠:哪裡缺護欄就補護欄、agent 在哪裡失敗就補 context、更新 agent 遵循的 workflow。他建議去聽晶圓廠或 industry 4.0 真實工廠的分享——那裡有專職的 process control / loop management 角色,專門看「這裡損失了 10% 資源,去修好工廠的那一段」,然後迭代。軟體系統即將照做一遍。

**Code review 是最好的第一個案例**:建一套系統,讓你有信心把 5% → 10% → 50% → 100% 的 PR 在沒有人工 code review 的情況下合併。這需要什麼樣的系統?他借用自動駕駛的類比(儘管有點黑暗):大家知道**當道路死亡率降到跟人類同級、或低一個數量級時**,我們就願意讓機器上路。驗證也一樣——你要先定義哪些指標(bug 數、incident、MTTR⋯)達標時,可以讓 review 這一步不需要人在迴圈裡。

量測什麼:cycle time、code shelf life、incident time、bug 數。**不要量 token**,它給不了什麼資訊或價值;要看成本就看「每次程式變更的成本」「每個 loop / 每週的成本」,用近似看待人類薪資的方式來看。

**三個帶走的重點**:(1) 投資 agent readiness;(2) govern before you scale——先把治理做好再全公司推廣;(3) 事先想清楚要量測什麼 outcome。

### 金句

> "Coding is just not the hard part. It's basically in fact the easiest part of this problem."(約 00:56)

難的是寫程式周圍的一切;把 AI 只塞進「寫程式」那一格,自然感受不到倍數效應。

> "Your software factory is your company. If you build software, you're basically describing the new version of your business."(約 00:59)

因此工廠的主權必須在自己手上,不能綁死在某個廠商身上。

> "It's not really a matter of if, but just when."(約 01:03)

指 agent 終將拿到危險權限——所以護欄要現在就建,而且要照大 10 倍的組織規格建。

## English Notes

### TL;DR

- **Coding isn't the hard part** — it's the easiest part. Companies don't feel the promised 100x because they've only applied AI to one narrow slice of the loop while everything around it stays a human-driven synchronous workflow.
- **Three design commitments for a software factory**: stay model-independent (commoditize the model layer to reach the real cost/quality Pareto frontier); own and govern your own factory (on-prem and airgapped options matter); and run every surface off a **shared agent core** rather than hyper-specializing a separate architecture per workflow.
- **The environment, not the model, is the binding constraint.** The highest-leverage investment is dev reproducibility, environment cleanliness, linting, type checking, and test quality — i.e., enough deterministic, verifiable feedback loops that agents can converge without consulting a human.
- **Govern before you scale.** Agents will get dangerous access — "not a matter of if, but when." Build layered controls at the level an organization 10x your size would need: a 5-person startup should run 50-person controls.
- **Measure outcomes, not tokens**: cycle time, code shelf life, incident time, bug counts; treat cost as cost-per-change or cost-per-loop, roughly the way you'd think about salary.

### Key Points

#### The software factory: making the implicit loop explicit (~00:53–00:57)

Three and a half years of evolution: autocomplete → chatbots → agents → software factories. A software factory is simply the loop that already exists inside every software company, drawn explicitly: **signals** flow in (customer feedback, internal telemetry, an executive announcing a pivot), get triaged, feed planning, then coding, validation, shipping, deployment — and the deployed, monitored software generates fresh signals.

The trouble is that triage happens **inside people's heads** and is almost never explicitly represented in any real system, and planning is scattered and unstructured across Jira, Notion, or Confluence. As he put it, this implicit feedback loop exists at almost every company building software, and yet an explicit model of it does not really exist anywhere.

That explains the gap between "AGI is six months away, expect 100x" and what teams actually experience: you've only AI-ified one narrow slice, and the rest remains a synchronous, autocomplete-shaped interaction. The real design question is how to build a system where signals flow all the way to deployed software **without human intervention** — which he's careful to distinguish from without humans.

#### How the system should be designed (~00:57–01:01)

1. **Model independence.** Model vendors will argue you must verticalize aggressively and couple the agent harness to the model; empirically he finds that clearly untrue. Aggregate and commoditize the model layer to actually reach the cost/quality frontier.
2. **You are the sovereign of your factory.** Even when buying SaaS, you should control it — hence on-prem and airgapped deployments. The reasoning: your software factory *is* your company, so it has to keep running regardless of which vendors come and go.
3. **A shared agent core.** The factory should span every action in the product and engineering org — code review, security analysis, testing, documentation, incident response. But specializing a distinct agent architecture per surface lands you in an odd microservices trap; at a high level all these workflows are the same thing: gather information, act on computer systems, keep the user informed. What changes is context and workflow, not the agent.

Larger organizations then need governance — consistency, preventing an agent from dropping a bunch of tables, IT ops. He argues that's the agent platform's job, and offers a concrete vendor test: **look for a page listing enterprise or organizational controls, and count them.** If it doesn't cover hundreds of scenarios, keep shopping. He cited Docker's recent vendor-neutral agent control set (~35 controls) as a nice way to present this.

#### The environment is the bottleneck (~01:02–01:04)

His analogy: humans 200,000 years ago were roughly the same animal we are; what changed is that we completely rebuilt the environment around us. Likewise, you can wait for models to improve — they probably will — but **updating the codebase and engineering system around the factory is by far the highest-leverage move**.

The real test: does your organization have **enough deterministic, verifiable feedback loops for agents to succeed without needing to consult a human?** Waiting for code review to say the code is poorly organized is one thing; a deterministic signal saying so lets the agent loop and validate its own work until it passes.

On access: agents will end up with dangerous privileges, and it's not a matter of if but when — so treat them like people and build layered systems of control. Anyone who has built an org past 50–75 people knows that even 75 extremely competent people will eventually include someone who drops the database. Introducing agents is like scaling to an organization 10x larger, so the guardrails need to scale accordingly: a 5-person startup needs 50-person controls, a 50-person company needs 500-person controls. None of this requires reinventing the wheel — it's established software development best practice, now enforced on agents.

#### The new human role, and what to measure (~01:04–01:08)

The human job becomes **observe → intervene → iteratively refine** the factory: spot a missing guardrail and implement it, see where agents fail and add context, update the workflows agents follow. He recommends listening to talks about chip fabs or real Industry 4.0 factories, where dedicated process-control and loop-management roles exist purely to say "we lost 10% of resources to this inefficiency, go fix that part of the factory," then iterate. Software is about to do the same.

**Code review is the natural first case study**: build a system that makes you confident merging 5%, then 10%, 50%, 100% of PRs without human review. What does that system look like? He borrows the self-driving analogy — somewhat dark, but everyone recognizes the moment road fatalities drop to human parity or an order of magnitude below, and we let the thing drive. Validation needs the same: define up front which metrics (bugs, incidents, MTTR) would justify taking the human out of the review step, and have engineers thinking about that inside your company.

What to measure: cycle time, code shelf life, incident time, bug counts. **Do not measure tokens** — it gives you very little information or value. If you want cost, use cost per code change or per loop or per week, treating it roughly the way you treat salary.

**Three takeaways**: (1) invest in agent readiness; (2) govern before you scale; (3) decide in advance which outcomes you'll measure — you can't optimize against something you aren't measuring.

### Quotes

> "Coding is just not the hard part. It's basically in fact the easiest part of this problem." (~00:56)

Everything *around* writing code is where the mess lives.

> "Your software factory is your company. If you build software, you're basically describing the new version of your business." (~00:59)

The argument for sovereignty over your own agent platform.

> "It's not really a matter of if, but just when." (~01:03)

On agents getting dangerous access — build the guardrails now, sized for an org 10x larger.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Factory AI | 講者共同創辦的公司,提供建構「軟體工廠」的平台,支援 SaaS / on-prem / airgapped | The speaker's company; platform for building software factories, offered as SaaS, on-prem, or airgapped | 講者為 Co-Founder / CTO |
| Docker 的 agent 控制項清單 / Docker agent controls | 約 35 條、vendor-neutral 的 agent 平台控制項 | A vendor-neutral set of ~35 agent-platform controls | 條目數與正式名稱待確認 / exact name and count to verify |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Anna Reus | Eno Reyes |
| MTR | MTTR(mean time to recovery/resolution) |
| code reveal | code review |
| "you have an AI CEO or saying like oh AGI's here" | 語意為「聽到 AI 公司 CEO 說 AGI 快來了」/ paraphrase: hearing an AI-company CEO claim AGI is months away |

## 待確認 / To Verify

- Docker 那套「35 個 agent 控制項」的正式名稱與確切條目數:Docker 確有 AI agent runtime governance 框架,但搜尋未能對上「35」這個數字。/ Docker does publish an AI-agent runtime governance framework, but the "35 controls" figure could not be matched to a published document.
- 投影片上「laundry list of controls(security / governance / enablement)」的完整內容——講者明說可以拍照,逐字稿無法還原。/ The full controls checklist on the slide (security / governance / enablement) — he told the audience to photograph it; not recoverable from the transcript.
- 講者提到「上一場的 talk」談 specialized agents 與「上一份 deck 說 you can't optimize what you can't measure」,指的應是同場次前面的講者,未指名。/ He references "the talk just a bit ago" and "the last deck" without naming them.
