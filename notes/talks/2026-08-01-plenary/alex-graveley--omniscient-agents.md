---
title: "Omniscient Agents"
title_zh: "全知 agent"
speaker: "Alex Graveley"
affiliation: "Co-Founder of FlyingObject.ai; Co-creator GitHub Copilot & Perplexity Computer"
type: talk
stage: Plenary
date: 2026-08-01
session: "Session 2: Future of Software Engineering"
video: "https://www.youtube.com/watch?v=gKdeLQd_LIQ&t=11155s"
video_range: "03:05:55–03:15:15"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 1st - Morning Session [DownSub.com].srt"
status: draft
tags: [autonomy, self-directed-agents, observability, agent-primitives, product-development]
---

# 全知 agent(Omniscient Agents)

**一句話總結**:agent 之所以還需要人在迴圈裡,是因為它看得到的東西太少;把整間公司發生的事全部收進來、再給它操作真實系統的權限,agent 的 scope 就能從「寫 PR」一路爬到「自己決定該做什麼產品」。
**One-line summary**: Agents still need a human in the loop because of how little they can see; ingest everything a business produces and give them control over live systems, and their scope climbs from writing PRs to deciding what product should exist in the first place.

## 中文筆記

### TL;DR

- **今天的 agent 是一堆 primitive 的堆疊**——執行層、資產產出、orchestration(sub-agent、skills、memories、排程、loop)、live data。你從零做 agent 就得把每一個都自己實作一遍。
- **真正的瓶頸是「你的注意力」**。agent 不太知道該做什麼、對「下一步」的建議常常很糟,所以人必須在迴圈裡指揮;而這條信任階梯已經爬了很久:**tools → commits → 單一 PR → 多個 PR(loop)→ features → projects → 整個產品**。
- **推動 scope 上升的是兩條軸:insight(能取得什麼資料、以什麼形式)與 control(能對資料與線上系統做什麼)。** 方向是**從「看見程式碼」走到「看見整間公司」**。

### 重點整理

#### 問題設定:agent 被它看得到的東西限制住了(約 03:07)

他先自我介紹:GitHub Copilot 與 Perplexity Computer 的主導者,剛創辦新公司 FlyingObject 來做這場演講的主題。

**「傳統上,agent 一直被它能看見與能存取的東西所限制。而我們認為,正是這一點使得『人必須在迴圈裡』成為必要。」** 他要的是**讓人更少地待在迴圈裡,或至少能把迴圈裡不同的部分外包給 agent。**

#### 今天的 agent 是一堆 primitive(約 03:07–03:09)

如果你要從零做一個 agent,下面每一項都得自己實作:

- **執行層(execution layer)**:跑在本機或 sandbox 裡,附帶一堆操作檔案、執行指令、跑 CLI 的能力。
- **資產產出(asset creation)**:文件、網站,而 **PR 也是一種資產形式**——大家正在努力讓 agent 把這件事做好。
- **Orchestration primitives**(他說細節不重要,重要的是它們各自解決什麼):
  - **sub-agent**:有跟 parent 不同的 context,這件事本身有用。
  - **skills**:填補權重沒有以你想要的方式表達出來的那些空缺。
  - **memories**:讓 agent 能從過去學習。
  - **排程任務(scheduled tasks)**:需要重複發生、或按時間表跑的事。
  - **loops**:目標導向的執行——**個別任務壓縮成一個 loop,而 loop 在目標達成前不會結束。**
- **Live data**:web search、browser control、computer control、MCP、API,諸如此類。

**「這就是 agent 今天的位置。」**

#### 瓶頸是你的注意力(約 03:09–03:10)

這些東西的共同點是:**你仍然在控制這些 agent**。agent 不太知道該做什麼,**它對「下一步做什麼」的建議常常很糟**,所以人必須在迴圈裡指揮。

**結果是:瓶頸變成你——一個「使用 agent 的工程師」——的注意力。** 你在管理 loop、同時跑一堆平行的東西、判斷哪些出錯了哪些順利;你大致知道發生什麼事,你可以停掉、可以 fork、可以重啟。

#### 信任階梯:我們一直在往上爬(約 03:10–03:11)

他指出**今天做這件事的方式,跟一年前已經很不一樣了——agent 自我導向的方式變了**。我們其實一直在**往上爬一座複雜度階梯**:

1. **只有 tools**:我們信任 agent 呼叫正確的工具。
2. **commits**:開始信任 agent 做 commit。
3. **整個 PR**:開始信任 agent 產出完整的 PR。
4. **多個 PR**(現在的位置):信任 agent 為了達成 loop 型的目標而連續產出多個 PR。
5. **features**(他認為的下一級):一個 feature 可能包含**跑實驗、看即時資料、檢查 exception、檢查使用者情緒、把接觸到這個功能的人分群**,以檢驗它是否影響你的主要目標——例如留存率或營收。
6. **projects**:一組能服務產品中某個需求的 features 集合。
7. **whole products**(頂端):**你對一個自我導向的 agent 用很高階的方式描述你要做的產品,它就去做出來、部署、迭代,自己搞清楚需要哪些 feature(也許是別處根本不存在的),試幾種不同做法,以這種方式自我導向。**

#### 兩條軸:insight 與 control(約 03:12–03:13)

**每往上爬一級,都需要新一輪的模型迭代、或大得多的 agent harness 複雜度。** 那要怎麼讓 scope 持續上升?他認為共通點是兩條軸:

- **Insight**:**agent 能取得什麼資料,以及以什麼形式取得**,好讓它能從中導出洞見。
- **Control**:**它對那些資料與線上系統動手的能力。**

方向因此是**從「看見程式碼」走到「看見整間公司」**。這樣才能開始搞清楚:**真正的商業目標是什麼?為了達成這些目標,應該存在哪些產品、哪些功能?** 他強調**現在這件事完全靠人去想、去猜——而他們要的是讓 AI 有能力做這件事。**

而產品開發週期的另一半同樣需要 control:**跑實驗、部署變更、監控線上系統、視需要擴展這些系統。** 兩條軸加起來,就是 agent 的 scope 正在成長的方向。

(他在此處說了一句 "sorry I'm out of time",最後兩節講得較快。)

#### 開放問題(約 03:13–03:14)

- **處理大量資料**:一般而言你會想**把一間公司內部發生的所有事都 ingest 並索引起來**。
- **壓縮知識**:把那些知識**壓縮成 agent 真的能用的形式**。
- **Triggers**:要有觸發機制。
- **Agent 之間互相感知與協調**:如果你要**同時跑大量實驗、而且可能沒有人在迴圈裡**,agent 必須彼此知道對方存在並有效協調。
- **最難的一點:有時候你根本不知道自己在優化什麼目標函數。**

#### 收尾(約 03:14–03:15)

**「我們想做的是把整個系統圈起來、捕捉一切;把 macro context 交給 agent,讓它們能在完整的覺知下運作;再給它們正確的 primitive,讓它們能部署變更、監控那些變更、並擴展那些變更,以達成商業目標。」** 他承認**這會是一個往上爬複雜度堆疊的過程**,但他認為那就是方向。想試早期版本可以上 FlyingObject 的候補名單,或在 Twitter 上找他。

### 金句

> "Traditionally agents have been sort of limited by what they can see and access. And we think that this necessitates having a human in the loop."(約 03:07)

整場的因果假設:人在迴圈裡是「視野不足」的症狀,不是原因。

> "Today's agents are a pile of primitives."(約 03:07)

從零做 agent 的現況:每一塊都得自己補。

> "The bottleneck becomes your attention as an agent-using engineer."(約 03:09)

跟同場 Ryan Lopopolo 的「三種稀缺資源」直接呼應。

> "We started with just tools. … Where we are now is trusting the agent to make multiple PRs."(約 03:10)

自主度的實際計量單位是「你願意信任的 artifact 大小」。

> "The axes that drive scope are insight and control."(約 03:12)

他對「怎麼把 agent 的 scope 往上推」的核心答案。

> "We're moving from seeing the code to seeing the entire business."(約 03:12)

「Omniscient」的具體定義。

> "Sometimes you don't even know the objective function you're optimizing."(約 03:14)

自我導向 agent 最難的一個開放問題。

## English Notes

### TL;DR

- **Today's agents are a pile of primitives** — execution layer, asset creation, orchestration (sub-agents, skills, memories, scheduling, loops), and live data. Build one from scratch and you implement every single one yourself.
- **The real bottleneck is your attention.** Agents don't quite know what to do and their suggestions for what's next are often bad, so a human stays in the loop directing them. The trust ladder has been climbing for a while: **tools → commits → a single PR → multiple PRs (loops) → features → projects → whole products.**
- **Two axes drive scope: insight (what data the agent can access, and in what form) and control (what it can do to that data and to live systems).** The direction of travel is **from seeing the code to seeing the entire business.**

### Key Points

#### The framing: agents are limited by what they can see (~03:07)

He introduced himself as lead on GitHub Copilot and Perplexity Computer, having just started FlyingObject to work on exactly this topic.

**"Traditionally agents have been sort of limited by what they can see and access. And we think that this necessitates having a human in the loop."** The goal is to **get the human less into the loop, or at least able to farm off different pieces of their loop to agents.**

#### Today's agents are a pile of primitives (~03:07–03:09)

Build an agent from scratch and you have to implement all of these yourself:

- **Execution layer** — running locally or in a sandbox, with commands for manipulating files, running commands, and running CLIs.
- **Asset creation** — documents, websites, and **PRs as another form of asset** that everyone is working to make agents good at.
- **Orchestration primitives** (he noted the details matter less than what each one does):
  - **Sub-agents** with different context from the parent.
  - **Skills** to fill gaps the weights don't express the way you want.
  - **Memories** so the agent can learn from the past.
  - **Scheduled tasks** for things that recur or run on a schedule.
  - **Loops** — goal-directed running, where **individual tasks compress into a loop that doesn't end until the goal is achieved.**
- **Live data** — web search, browser control, computer control, MCPs, APIs, all of it.

**"This is where agents are today."**

#### The bottleneck is your attention (~03:09–03:10)

What's common across all of it is that **you're still controlling these agents.** The agent doesn't quite know what to do, **its suggestions for what to do next are often bad**, so a human directs.

**The result: the bottleneck becomes your attention as an agent-using engineer.** You're managing loops, running things in parallel, tracking what's going wrong and what's going well. You have a sense of what's happening; you can stop things, fork things, restart things.

#### The trust ladder we keep climbing (~03:10–03:11)

He noted **the way we do this today is quite different from a year ago — the way agents self-direct has changed.** We've been **walking up a complexity hierarchy**:

1. **Just tools** — we trusted the agent to call the right tool.
2. **Commits** — we started trusting the agent to make commits.
3. **Entire PRs.**
4. **Multiple PRs** — where we are now, trusting the agent to produce several PRs to accomplish looped goals.
5. **Features** — his next rung. A feature might involve **running an experiment, looking at live data, checking for exceptions, checking user sentiment, and segmenting who's exposed to the feature** to see whether it moves your primary objectives, like retention or revenue.
6. **Projects** — collections of features serving a need in your product.
7. **Whole products** — at the top, **you describe at a very high level the product you want to a self-directed agent, and it goes and makes it, deploys it, iterates on it, figures out which features it needs (maybe ones that don't exist anywhere else), tries a few different things, and self-directs that way.**

#### Two axes: insight and control (~03:12–03:13)

**Each level up required either new model iterations or much more agent harness complexity.** So how do you enable increasing scope? He argues it comes down to two axes:

- **Insight** — **what data the agent has access to and in what form**, so it can derive insights.
- **Control** — **its ability to operate on that data and on live systems.**

Which means **moving from seeing the code to seeing the entire business.** Only then can you start to work out **what the actual business objectives are, and which products or features should exist to accomplish them.** Right now, **that's up to people to figure out and take guesses at — and what they want is for AI to be able to do it.**

The other half of the product development cycle needs control just as much: **running experiments, deploying changes, monitoring live systems, and scaling them as needed.** Together, those are the two axes along which agent scope grows.

(He noted "sorry, I'm out of time" here and moved quickly through the last two sections.)

#### Open problems (~03:13–03:14)

- **Processing lots of data** — generally you want to **ingest and index everything that happens inside a business.**
- **Compression** — turn that knowledge into **something usable by your agent.**
- **Triggers.**
- **Agents aware of each other** — if you're running lots of experiments simultaneously, **potentially with no human in the loop**, agents need to know about each other and coordinate effectively.
- **The hardest one: sometimes you don't even know the objective function you're optimizing.**

#### Closing (~03:14–03:15)

**"What we want to do is enclose the entire system, capture everything. Give the macro context to agents so that they can operate with full awareness, and give the right primitives to those agents so they can deploy changes, monitor those changes, and scale those changes to accomplish those business goals."** He acknowledged **it will be a process as we walk up this complexity stack**, but that's the direction he thinks we're headed. Early versions are behind a FlyingObject waitlist; otherwise he's on Twitter and would love to talk.

### Quotes

> "Traditionally agents have been sort of limited by what they can see and access. And we think that this necessitates having a human in the loop." (~03:07)

The causal premise of the whole talk: humans in the loop are a symptom of limited visibility, not a cause.

> "Today's agents are a pile of primitives." (~03:07)

The state of building an agent from scratch: every piece is yours to supply.

> "The bottleneck becomes your attention as an agent-using engineer." (~03:09)

Directly echoes Ryan Lopopolo's three scarce resources from earlier in the same session.

> "We started with just tools. … Where we are now is trusting the agent to make multiple PRs." (~03:10)

Autonomy measured in the size of artifact you're willing to trust.

> "The axes that drive scope are insight and control." (~03:12)

His core answer for how to push agent scope upward.

> "We're moving from seeing the code to seeing the entire business." (~03:12)

What "omniscient" actually means here.

> "Sometimes you don't even know the objective function you're optimizing." (~03:14)

The hardest open problem for self-directed agents.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| FlyingObject | 他新創的公司,主題就是這場演講講的 omniscient agents;早期版本開放候補名單 | His new company, built around the omniscient-agents thesis; early versions behind a waitlist | 官網議程作 FlyingObject.ai;他口頭說 "Flying Object",主持人說 "Flying Objects" / agenda says FlyingObject.ai; he said "Flying Object" onstage, the host said "Flying Objects" |
| GitHub Copilot | 他共同創造的產品;主持人稱其為最早把 AI coding 帶進 production 的 agent 之一 | Co-created; the host called it one of the first agents to take AI coding into production | 主持人介紹內容 / from the host's introduction |
| Perplexity Computer | 他參與的 Perplexity computer 產品 | The Perplexity computer product he worked on | 官網議程列為 co-creator / listed as co-creator on the agenda |
| Agent primitives(執行層、sub-agent、skills、memories、scheduled tasks、loops、live data) | 他盤點的「今天做 agent 必須自己實作的一整組零件」 | His inventory of what you must implement yourself to build an agent today | 他強調細節不重要,重要的是各自解決什麼 / he stressed the details matter less than the function |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Alex Gravely | Alex Graveley |
| Flying Objects | FlyingObject(官網議程作 FlyingObject.ai)/ FlyingObject (FlyingObject.ai per the agenda) |
| omnicient | omniscient |
| MCPS | MCPs |
| sub aents | sub-agents |

## 待確認 / To Verify

- 演講中未提及 FlyingObject 的產品名稱或候補名單網址(只說 "there's a wait list on flying object")。/ No product name or waitlist URL was given onstage — only "there's a waitlist on FlyingObject."
- 他口中的「omniscient agents 是一個新品類」是否已有對外發表的定義文件或部落格。/ Whether there is a published write-up defining "omniscient agents" as a category.
- 他對「一年前的自我導向方式不同」所指的具體時間點與產品世代未說明。/ He didn't specify which product generation he meant by "the way we did it maybe a year ago."
- 他在時間不足下略過的內容(約 03:12 起說 "sorry I'm out of time"),投影片上可能還有未被口述的細節。/ He ran out of time around 03:12; slides may contain material he skipped.
