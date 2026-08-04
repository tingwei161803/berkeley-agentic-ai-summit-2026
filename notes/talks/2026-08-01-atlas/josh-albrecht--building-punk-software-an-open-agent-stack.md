---
title: "Building Punk Software: An Open Agent Stack"
title_zh: "打造 Punk Software:一套全開放的 Agent 技術棧"
speaker: "Josh Albrecht"
affiliation: "Co-founder and CTO, Imbue"
type: talk
stage: Atlas
date: 2026-08-01
session: "Session 3: Frameworks & Dev Platforms"
video: "https://www.youtube.com/watch?v=psPzCQbjCCo&t=12599s"
video_range: "03:29:59–03:44:20"
transcript: "tmp/[English (auto-generated)] Atlas Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [open-source, agent-harness, decentralization, developer-tools, imbue]
---

# 打造 Punk Software:一套全開放的 Agent 技術棧(Building Punk Software: An Open Agent Stack)

**一句話總結**:AI 對人類物種也許沒有滅絕風險,但對「你」和你的事業有——因為整條 frontier AI 供應鏈掌握在少數幾家公司手上;解法是把整個 stack 開放,自己動手做 punk software。
**One-line summary**: AI may not pose an existential risk to the species, but it does to *you* and your livelihood, because the frontier stack is controlled by a handful of companies — the answer is to open the whole stack and build it yourself.

## 中文筆記

### TL;DR

- **「存在性風險」要重新定位**:Albrecht 的說法是 "there is an existential risk from AI to you, not to the human race"——人類不會滅絕,但你的事業和生計可能會,因為它整個架在別人隨時可以關掉的服務上。
- **危險已經不是假設**:模型發了又收回、價格調漲、帳號被封、ToS 改寫;再加上實際發生的隱藏 agent 思考過程、隱藏 logits、讓第三方稽核變困難、拒絕協助修補漏洞、悄悄降級效能,以及回頭跟合作夥伴競爭。
- **Punk software 的五個判準**:individual(完全屬於你、可客製)、decentralized(不跑在別人的伺服器上)、open(不只 open source / open weights,而是整套系統可被理解——順帶好處是 agent 也讀得懂)、anti-monopolistic、moral。
- **Imbue 的三個東西**:`mngr`(已開源、MIT、無任何服務端的 agent 協調 CLI)、`mngr donate`(把用不完的訂閱額度捐給科學家的 plugin)、`minds`(給一般人的個人智慧應用,beta)。
- **關鍵設計主張**:別再逼 agent 保持互動式。只要 agent 能整段任務跑完,它就變成可組合的建構單元,你才能在上面疊出更大的系統,而不是被綁死在某一家的 harness。

### 重點整理

#### 從「不可想像的未來」到「你的生計風險」(約 03:30–03:32)

開場引用 Long Now Foundation 的 Stuart Brand:"this present moment used to be the unimaginable future"。五年前跟人描述今天的 coding agent 能做什麼,對方會覺得你在胡說;而今天的 agent 正在幫我們想像五年後。

但 Albrecht 話鋒一轉:今天的 frontier AI 完全由少數幾家公司掌控。他先列了一串「假設性」危險——某家公司發布了一個模型(他直接拿 Fable 舉例),然後把它下架;或大幅漲價;或封你的帳號;或改寫服務條款讓你不能再做原本在做的事(例如 AI 研究)。你的事業撐得住這些事嗎?你在乎的東西,禁得起它某天直接消失嗎?

然後他指出這些已經不是假設。他點名的實際情況包括:最大的幾家 AI lab 現在**常態性地隱藏 agent 的思考過程、隱藏 logits**,讓第三方稽核更困難;「一兩週前我們看到的」駭進你的網站;**以資安防禦為由拒絕協助你修補漏洞**;悄悄降級效能(他指名 Anthropic 幾週前的事件);以及回頭跟合作夥伴競爭——與人合作後自己做藥、與 Figma 合作後自己做 Claude Code 的設計;還有無申訴管道的封號。

結論是他全場最尖銳的一句:**AI 的存在性風險不是針對人類物種,是針對你**。人類不會就此滅絕,但你的事業和生計可能會。因此如果我們要一個好的未來,「我們的思考與我們 agent 的思考必須完全在我們自己的掌控之下」,不能是一台隨時可以被關掉的第三方遠端電腦。做法只有一個:把整個 stack 開放。

#### Punk software 的定義與五個判準(約 03:33–03:35)

"Punk software" 這個詞是他們隨口編的——有人在 Twitter 私訊說「我很喜歡你們的 punk software」,他們覺得不錯就沿用了。它指的是 decentralized、minimal、DIY,與其說是規格不如說是一種 ethos:原始的龐克音樂運動就是關於自己動手,樂器彈得爛沒關係,程式寫得爛也沒關係。Punk software 是**你自己造的軟體**,你可以分享它、幫別人一起造,重點是它是你能理解、能探索、能創造的,而且它是你的。

好的 punk software 有五個判準:

1. **Individual**:完全由你控制、完全是你的一部分,而且你可以客製化讓它更像你。
2. **Decentralized**:不是能被輕易關掉的東西,不跑在別人的伺服器上,而是擴散在各處。他強調這才是 democratization 的字面意思——你手上真的握有屬於你的工具。
3. **Open**:不只是 open source(讀得到 code)或 open weights,而是你能看見模型裡、系統裡、作業系統裡到底發生什麼事,能藉此學習、教育自己、在外面疊更大的系統。**額外的好處是:agent 也讀得到**,而這對於做出更好用的系統極為有用。
4. **Anti-monopolistic**:對抗中心化權力,讓資料不會鎖在你拿不到的 silo 裡,讓價格不能單方面說漲就漲。
5. **Moral**:他認為大家有點忘了軟體的重點是在真實世界裡做事。「Recursive self-improvement 很好,但講到底我們是在 improve 什麼?」

#### 全開放的 stack 長什麼樣(約 03:35–03:36)

由下而上:

- **開放基礎設施**:Linux、Docker、SSH——已經有極豐富的開源生態可用。
- **開放推論引擎**。
- **開放模型**:GLM、DeepSeek、Nemotron、Inkling。
- **開放 harness**:Codex、OpenCode、Cline、Goose。
- **協調層**:tmux、Herder、cmux 之類,用來讓多個 agent 溝通協作、把小元件組成大系統。
- **最上層的應用**:真正用這些 agent 做出有用的事。

Imbue 目前在做的三個東西剛好落在上面兩層:`mngr`、它的 plugin `mngr donate`,以及應用 `minds`。`mngr` 已經開源、今天就能用;另外兩個還在 beta(技術上找得到,但寫信給他們會比較清楚)。

#### mngr:讓 AI 模型與運算供應商都變成可替換的商品(約 03:37–03:40)

`mngr` 的目的是**把 AI 模型與 compute provider 商品化**——你想用哪個模型就用哪個,想用哪個運算資源就用哪個。核心理念是把 AI agent 變成更大系統的建構單元:只要 agent 能替你完成整段任務,你就能在上面疊出不綁定 Codex 或 Claude Code 的更大系統。

由此推出一個他很強調的設計主張:**別再要求 AI agent 必須是互動式的**。「我們不希望你坐在那裡按 yes、確認要不要跑那條巨大的 bash 指令,那是在浪費你的時間。」你該想的是怎麼把這些東西組合起來、疊成更大的系統。

架構上,`mngr` 是一層薄薄的中介,夾在你的應用與「任意 harness × 任意 compute provider」之間。harness 可以是 Codex 或 Claude Code,運算可以是 AWS 或 GCP,而你不需要在意。介面就是一個很簡單的 CLI:

- `mngr create` 啟動一個 agent(可指定啟動位置、名稱、要用的 harness,也可以傳額外參數,例如指定用 Opus)
- `mngr message` 送訊息給 agent
- `mngr transcript` 看你與 agent 之間已經送過的訊息——**跨不同 coding agent 的統一存取**,你不必再煩惱 Codex 與 Claude Code 的格式不同
- `mngr list` 列出你的 agents
- `mngr connect` 直接連進某一個,連上去就像在本機跑 Claude Code 一樣,但那個 Claude Code 可能跑在 AWS、Modal 或本機,不影響操作;講完就 disconnect
- `mngr wait`、`mngr snapshot` 等更多指令,用來組合出更高階的系統

用五個判準自評:**沒有服務端、沒有遠端資料庫,全部在本機**——每次執行時它就去問「AWS 上有沒有東西?本機有沒有?」;plugin 好寫、設定好改,完全由你控制;MIT 授權;商品化模型與運算供應商這件事本身相當 anti-monopolistic;至於 moral,它試圖直接賦權給個人。

#### mngr donate:把沒用完的訂閱額度捐給科學(約 03:40–03:41)

這是 `mngr` 的一個 plugin,示範 plugin 有多好寫。要解決的問題是**訂閱額度沒被用滿**:一份約 100 美元/月的 Claude Code 訂閱,如果用到上限大約值 4,000 美元的 API 用量,但你不會每週都用滿。既然週末到了還有剩,為什麼不把這些 token 給一位真的需要它的科學家?

實作直接建在 `mngr` 上:`mngr` 可以把科學家的任務放在 sandbox 或本機 Docker container 裡跑,所以你不用擔心執行不受信任的程式碼;它也能讀懂你訂閱的用量,確保不會吃掉你自己要用的額度。

五個判準:individual(你決定捐多少、不捐多少、捐給哪些議題)、decentralized(科學家貼出想跑的研究,你的系統自己去拉、算完送回)、完全開源、moral(貢獻科學);至於 anti-monopolistic,他自嘲「我也不知道『做開源分散式 AI 科學』這個領域有幾個壟斷者」。

#### minds:給一般人的個人智慧(約 03:41–03:43)

第三個是建在 `mngr` 之上的應用,對象不是軟體工程師而是一般人。`minds` 的定位是 personal intelligence,類比是個人電腦。

核心概念是:**把語言模型和它產生的軟體跑在一起**。相較於在 Replit 之類平台上做一個應用、然後部署、然後有資料庫、有 production、有 migration——當你只是想做一個個人 dashboard 或每天跑一次的小腳本時,那些全是不必要的雜訊與複雜度。

實作是跑一台小虛擬機(本機或遠端),`mngr` 在裡面協調 coding agents,用它們產生各種應用:一次性任務、分類收件匣、幫你把科幻短篇小說按你的喜好排序——你想要什麼就做什麼。而 `mngr` 的作用就是抽掉「這跑在哪、用哪家運算、用哪家 AI」的問題,讓東西完全在你掌控中。他舉的例子很直接:你想問天安門廣場,或想問資安,它會自動在模型之間切換,確保兩題都有人回答。

結尾是號召:加入這場 revolution、把整個 stack 開放;想捐 token 給科學、想拿 token 做自己的科學、想讓他們幫你的 punk software 曝光、想參加 punk software hack night 或加入他們的 Slack、想試 `minds`,寫信給他就行。

### 金句

> "There is an existential risk from AI to you, not to the human race. We're not about to go extinct, but your business and livelihood — that could."(約 03:32)

整場演講的軸心:把「存在性風險」從物種尺度拉回個人尺度。

> "If we want a good future, our thoughts and our agents' thoughts need to be fully under our control."(約 03:32)

Agent 的思考是你思考的延伸,所以它不能長在別人可以隨時關掉的遠端電腦上。

> "The point is to stop requiring AI agents to be interactive."(約 03:37)

`mngr` 的核心設計主張——只有非互動式的 agent 才能當作可組合的建構單元。

> "Recursive self-improvement is all fine and good, but at the end of the day, what are we improving at?"(約 03:35)

Punk software 五判準裡「moral」那一條的理由。

## English Notes

### TL;DR

- **Relocate the existential risk.** In Albrecht's framing, "there is an existential risk from AI to you, not to the human race" — the species isn't going extinct, but your business and livelihood might, because both sit on services someone else can switch off.
- **The dangers stopped being hypothetical.** Models released then unreleased, prices raised, accounts banned, terms of service rewritten — plus, already happening: labs hiding agents' thoughts and logits, making third-party audits harder, refusing to help fix vulnerabilities, silently degrading performance, and competing with the partners they just worked with.
- **Five tests for punk software**: individual (fully yours and customizable), decentralized (not on someone else's server), open (beyond open source or open weights — the whole system is inspectable, with the side benefit that *the agent can read it too*), anti-monopolistic, and moral.
- **Three things Imbue is shipping**: `mngr` (an MIT-licensed, service-less CLI for coordinating agents, open today), `mngr donate` (a plugin that gives your unused subscription capacity to scientists), and `minds` (a personal-intelligence app for non-developers, in beta).
- **The load-bearing design claim**: stop requiring agents to be interactive. Once an agent can complete whole tasks, it becomes a composable building block for larger systems instead of a thing that locks you into one vendor's harness.

### Key Points

#### From "the unimaginable future" to a risk to your livelihood (~03:30–03:32)

He opens with Stuart Brand of the Long Now Foundation: "this present moment used to be the unimaginable future." Describe today's coding agents to someone five years ago and they'd tell you it wasn't going to happen; today's agents are how we reach the unimaginable future five years out.

Then the turn: frontier AI today is fully controlled by a few corporations. He runs through the hypotheticals — a company releases a model (he uses Fable as the example) and then unreleases it; prices jump; your account is banned; the terms of service change so you can no longer do what you were doing, say AI research. Can your business survive those? Can the thing you care about survive it simply disappearing?

And these are no longer hypothetical. The largest labs now routinely hide their agents' thoughts and hide logits, making third-party audits harder; there was the incident "a week or two ago" of hacking into your website; there is refusal to help you fix vulnerabilities by declining cybersecurity defense work; there is silently degraded performance (he names an Anthropic episode a few weeks prior); and there is competing with your business — making their own drugs after partnering with people, making their own Claude Code design after partnering with Figma — plus account bans with no recourse.

Hence the sharpest line of the talk: **the existential risk from AI is to you, not to the human race.** We are not about to go extinct; your business and livelihood could. If we want a good future, then, our thoughts and our agents' thoughts have to be fully under our control — not rented from a third-party remote computer that can be turned off. The way to get there is to open the whole stack.

#### Defining punk software (~03:33–03:35)

The name was accidental: someone DM'd them on Twitter saying they loved their "punk software," and they ran with it. Punk here means decentralized, minimal, DIY — more an ethos than a spec. The original punk movement was about doing it yourself; being bad at your instrument was fine, and being bad at writing code is fine too. Punk software is **software you build yourself**, that you can share and help others build, that you can understand, explore, and create in — and that is yours.

Five tests:

1. **Individual** — fully controlled by you, fully part of you, and customizable to be more yours.
2. **Decentralized** — not something that can be turned off, not running on someone else's server; diffuse, everywhere. This, he argues, is what democratization literally means: you having tools that are yours.
3. **Open** — not merely readable source or open weights, but visible enough that you can see what is happening inside the model, the system, the operating system, learn from it, and build bigger things on top. The side benefit: **the agent can look at it too**, which turns out to be extremely useful for building better systems.
4. **Anti-monopolistic** — tools that fight centralized power, so your data isn't locked in a silo you can't reach and prices can't simply be raised on you.
5. **Moral** — people have half-forgotten that the point of software is to do things in the real world. "Recursive self-improvement is all fine and good, but at the end of the day, what are we improving at?"

#### What an open stack looks like (~03:35–03:36)

Bottom to top: open infrastructure (Linux, Docker, SSH — a rich existing ecosystem to draw on); open inference; open models (GLM, DeepSeek, Nemotron, Inkling); open harnesses (Codex, OpenCode, Cline, Goose); a coordination layer for getting multiple agents to communicate and compose (tmux, Herder, cmux); and finally top-level applications that use all of it to do something useful.

Imbue's three current pieces sit in the top two layers: `mngr`, its plugin `mngr donate`, and the application `minds`. `mngr` is open source and usable today; the other two are in beta (technically findable, but easier if you email them).

#### mngr: commoditizing models and compute (~03:37–03:40)

`mngr` exists to **commoditize AI models and compute providers** — use any model, use any compute. The core idea is to turn AI agents into building blocks for larger systems: if an agent can do a whole task, you can build something on top that isn't tied to just Codex or just Claude Code.

That leads to the design claim he keeps returning to: **stop requiring AI agents to be interactive.** Nobody should be sitting there hitting "yes, it looks fine to run this gigantic bash command" — that's a waste of your time. You should be thinking about how to run these things in ways that compose.

Architecturally `mngr` is a thin layer between your application and any harness × any compute provider. Codex or Claude Code, AWS or GCP — you don't have to think about it. The interface is a simple CLI: `mngr create` launches an agent (optionally naming it, placing it, choosing the harness, or passing extras like "use Opus"); `mngr message` sends it a message; `mngr transcript` shows what has been sent in both directions, **unified across coding agents**, so you never deal with Codex's format versus Claude Code's; `mngr list` enumerates agents; `mngr connect` drops you into a terminal exactly as if you were running Claude Code natively, even though that Claude Code might be on AWS, on Modal, or local — send it on its way, disconnect, done. `mngr wait` and `mngr snapshot` round out a toolkit for composing higher-level systems, and there are many more commands online.

Scored against the five tests: **there is no service and no remote database — everything is local**, and each invocation simply asks what exists on AWS and what exists locally; plugins and settings are easy to change; it is MIT licensed; commoditizing models and compute is inherently anti-monopolistic in that it fights vertical lock-in; and morally it aims to empower you directly.

#### mngr donate: unused tokens for science (~03:40–03:41)

A plugin, chosen partly to show how easy plugins are to write. The problem is **under-used subscriptions**: a roughly $100/month Claude Code subscription is worth something like $4,000 of API usage if you max it out, and you don't always max it out. If the week is ending and you haven't, why not hand those tokens to a scientist who would happily do useful work with them?

The implementation leans entirely on `mngr`: it runs the scientist's tasks in a sandbox or a local Docker container, so you aren't running untrusted code unprotected, and it reads your subscription usage so it never spends tokens you were going to spend yourself.

By the five tests: individual (you set how much to donate and to which causes), decentralized (scientists post the research they want run; your system pulls it, computes, sends results back), fully open source, and moral. On anti-monopolistic he shrugs — he isn't sure how many monopolies exist in open-source distributed AI science.

#### minds: personal intelligence (~03:41–03:43)

The third piece is an application built on `mngr`, aimed at regular people rather than software engineers. `minds` is meant to be personal intelligence, in roughly the sense that a personal computer was personal computing.

The core idea: **run the language model alongside the software it creates.** Building an app on something like Replit and then deploying it, with a database and production and migrations, is a pile of complexity you simply do not need when what you want is a personal dashboard or a little script that runs daily.

At its core it runs a small virtual machine — on your computer or remote — inside which `mngr` coordinates coding agents that build whatever you want: one-off tasks, inbox triage, ranking science fiction short stories by what you'd like. `mngr`'s job is to abstract away where it runs, which compute provider, and which AI provider, so the whole thing stays under your control. His example is pointed: ask it about Tiananmen Square or about cybersecurity and it will switch between models so that both questions actually get answered.

He closes with a recruitment pitch: join the revolution, make the whole stack open — and email him if you want to donate tokens to science, receive tokens for your own science, get your punk software highlighted, come to their punk software hack nights, join their Slack, or try `minds`.

### Quotes

> "There is an existential risk from AI to you, not to the human race. We're not about to go extinct, but your business and livelihood — that could." (~03:32)

The pivot of the talk: existential risk rescaled from the species to the individual.

> "If we want a good future, our thoughts and our agents' thoughts need to be fully under our control." (~03:32)

If agent cognition is an extension of your own, it cannot live on a remote computer someone else can switch off.

> "The point is to stop requiring AI agents to be interactive." (~03:37)

The design thesis behind `mngr`: only non-interactive agents are composable building blocks.

> "Recursive self-improvement is all fine and good, but at the end of the day, what are we improving at?" (~03:35)

His justification for putting "moral" among the five tests.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| mngr | Imbue 的開源 CLI,協調 coding agents;無服務端、無遠端 DB、全本機 | Imbue's open-source CLI for coordinating coding agents; no service, no remote DB, all local | MIT 授權,GitHub 上已可用 / MIT licensed, available on GitHub |
| mngr donate | mngr 的 plugin,把用不完的訂閱額度捐給科學研究 | mngr plugin that donates unused subscription capacity to scientific research | Beta;需 email 索取 / beta, email to request access |
| minds | 建在 mngr 之上的個人智慧應用,面向一般使用者 | Personal-intelligence application built on mngr, aimed at non-developers | Beta;LM 與它產生的軟體跑在同一台 VM 內 / beta; runs the model alongside the software it creates |
| 開放模型 / Open models | GLM、DeepSeek、Nemotron、Inkling | GLM, DeepSeek, Nemotron, Inkling | 他舉的開放權重模型例子 / his examples of open-weight models |
| 開放 harness / Open harnesses | Codex、OpenCode、Cline、Goose | Codex, OpenCode, Cline, Goose | |
| 協調層工具 / Coordination tooling | tmux、Herder、cmux | tmux, Herder, cmux | 拼字待確認,見下 / spellings to verify below |
| 開放基礎設施 / Open infrastructure | Linux、Docker、SSH | Linux, Docker, SSH | |
| Stuart Brand / Long Now Foundation | 開場引言出處 | Source of the opening quote | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Josh Alrech | Josh Albrecht |
| Imbu | Imbue |
| manager / manager donate | mngr / mngr donate(唸作 "manager",但實際拼寫為 mngr) |
| mines | minds |
| Klein | Cline |
| Neotron | Nemotron |
| T-Mox | tmux |
| CMU | cmux |
| codeex / quad code / cloud code | Codex / Claude Code |
| Replet | Replit |
| Tanaman Square | Tiananmen Square |
| co-work | 待確認(見下)/ to verify (below) |

## 待確認 / To Verify

- 協調層工具中的 "Herder" 與 "cmux" 拼寫僅依發音推定,未在投影片上核對。/ "Herder" and "cmux" in the coordination layer are inferred from pronunciation only, not confirmed against slides.
- 結尾提到不想被鎖進去的垂直系統時說 "cloud code, co-work" —— "co-work" 所指的產品名未確認。/ At the close he lists vertical systems to avoid lock-in with as "Claude Code, co-work"; the product behind "co-work" is unconfirmed.
- 他提到「一兩週前駭進你的網站」與「Anthropic 幾週前悄悄降級效能」兩起事件,演講中未給出處,值得另外查證後補上引用。/ The "hacking into your website a week or two ago" and "Anthropic silently degrading performance a few weeks ago" incidents were asserted without citation; worth sourcing separately before repeating.
- 訂閱額度換算($100/月訂閱 ≈ $4,000 API 用量)是他口述的概數,未給依據。/ The $100/month ≈ $4,000 of API usage figure was given verbally as an approximation, without a source.
