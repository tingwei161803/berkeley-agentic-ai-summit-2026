---
title: "The Agentic Web and the Bazaar Era of AI"
title_zh: "Agentic Web 與 AI 的市集時代"
speaker: "Ramesh Raskar"
affiliation: "Professor, MIT"
type: talk
stage: Compass
date: 2026-08-01
session: "Session 2: Frameworks & Dev Platforms"
video: "https://www.youtube.com/watch?v=AO0RXP-fVZQ&t=831s"
video_range: "00:13:51–00:23:54"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [agentic-web, nanda, decentralization, marketplace, infrastructure]
---

# Agentic Web 與 AI 的市集時代(The Agentic Web and the Bazaar Era of AI)

**一句話總結**:AI 正從少數大廠量產、我們被動消費的「工廠時代」轉向邊緣模型遍地開花的「市集時代」;當網路上有數十億個 agent 時,真正的問題不是誰的模型最強,而是**誰來蓋 agent 的基礎設施——因為蓋的人就會擁有它**。
**One-line summary**: AI is shifting from a factory era — a few large companies mass-producing what we consume — to a bazaar era of edge models running everywhere. Once billions of agents are on the open web, the decisive question isn't whose model is best but **who builds the infrastructure, because whoever builds it will own it**.

## 中文筆記

### TL;DR

- **時代轉換**:AI 的「工廠時代」(大廠量產、我們消費)正因 edge AI、小模型、跑在自己機器上的東西而轉向 **bazaar era(市集時代)**;對應到運算史,就是從 mainframe 走向 PC。
- **不是 agents for e-commerce,而是 commerce because of agents**:他用 Sarah 與 Dr. John 的醫療情境說明——醫生在開放網路上出價 100 美元求解,全球數十億 agent 甦醒、組成 coalition、協作解題,最後約 10 個 agent 分掉這 100 美元。醫生取用的不是某個超強醫療模型,而是**一個以 marketplace 形式存在的智能網路**。
- **四個瓶頸**:要讓 agentic web 維持像今天網際網路一樣開放(而非 iOS/Android、Facebook/Twitter 那樣的圍牆花園),必須解決 (1) 類 DNS 的名稱結構、(2) passports / certification、(3) interoperability、(4) attestation。這是 MIT **Project NANDA** 的任務。
- **三個研究題**:agent 的 DNS;**knowledge pricing**(資料、模型、推論、算力都需要定價,他形容是「非常漂亮的數學問題」);**co-learning**(機器互學——會結盟、談判、競爭,甚至背叛,「agent 之間的權力遊戲」)。
- **視角翻轉**:別再只想 agents for X(coding、browsing、shopping),要開始想 **X for agents**——給 agent 的基礎設施、算力、保險、醫療、教育。

### 重點整理

#### 工廠時代 → 市集時代(約 00:14)

過去一段時間 AI 處在 **factory era**:少數大公司大量生產產品,我們只負責消費。但因為 edge AI、小模型、以及愈來愈多東西跑在自己機器上,**很快就會轉向 bazaar era**。MIT 這邊很多工作就是在想:當開放網路上有數十億、甚至數兆個 AI agent 時,「internet of AI agents」會長什麼樣?

#### 動機情境:Sarah、Dr. John 與那 100 美元(約 00:15–00:16)

德州鄉間的 Sarah 有胸痛與共病,從醫生那裡得不到好答案。她的醫生 Dr. John 可以到開放網路上說:「**出 100 塊,有誰能解 Sarah 的問題?**」

這時全世界數十億 agent 醒過來,心想「或許我能分到這 100 塊裡的一小塊」——它們去看相關健康條件的資料、開始訓練模型、彼此組成 coalition 協作;最後可能十來個 agent 一起把問題解掉,這 10 個分走那 100 美元,其餘的就散去。Dr. John 拿到的是一個「**像 Expedia 那樣的答案**」。

Raskar 強調這裡發生的事情的性質:「這不是 agents for e-commerce,**這是因為有 AI agent 才可能發生的 commerce**。」而且 Dr. John 並不是去存取某個厲害的醫療 AI 模型,他是**接進了一張智能的網路,而那張網路以 marketplace 的形式提供**。

#### 從 internet of agents 到 agentic web:NANDA(約 00:17–00:19)

現在有些公司已經在「可信邊界內」用 agent,但很快就會走到 agent 與**信任邊界之外**的 agent 協作、談判。不過那還只是給極客用的連線層——就像從 internet 走到 World Wide Web,還需要 HTML、瀏覽器、URL 這些東西。

**Project NANDA** 起源於 MIT,他當場的說法是 "AI agents in decentralized architecture";Nanda 在梵文中意為喜悅,也是他妹妹的名字。

他認為最貼切的類比是**高頻交易**:高頻交易之所以成立,是因為有 registry、每個商家/股票都經過預先資格認定、有一定程度的價格透明、有處理詐欺的機制。**這些東西全都得為 internet of AI agents 重新蓋一遍。**

接著是他對 OpenClaw 的評語:「OpenClaw 很棒,但它只是單向的、只表現得像一個工具——**我沒辦法呼叫你的 OpenClaw agent**,就像一支只能打出去、永遠不能接聽的電話。」它是單向 agent,不是雙向 agent。

於是關鍵問題浮現:誰來蓋這套基礎設施?更麻煩的是——**蓋的人也會擁有它**。所以我們會走向 agentic web 的圍牆花園,還是一個開放、有活力、中立、安全且可擴展的 web?這就是 NANDA 的使命。

**四個瓶頸**:(1) 類 DNS 的結構、(2) passports 與 certification、(3) interoperability、(4) attestation。他說 MIT 這個團隊在這個空間已經做了 11、12 年——從 AlexNet 之後就開始想「當數十億個 AI 系統彼此互動時會發生什麼」。

#### 三個研究問題(約 00:20–00:21)

1. **Agent 的 DNS**。
2. **Knowledge pricing**:資料、模型、推論、算力都必須被定價,「就像我們雇一個人時能算出他的薪水一樣」。他形容這是「一個非常漂亮的數學問題,來跟我們聊」。
3. **Co-learning**:過去 14 年是機器學習的黃金期,但接下來重點是 **machine co-learning**——兩個 agent 如何互相學習。而且不只是買賣服務與交易,agent 會**組成 coalition、談判、為資源競爭**,會有結盟也會有背叛,「agent 之間的權力遊戲」。

#### 生態系:NANDA Town、NandaHack 與國家級部署(約 00:21–00:23)

Web 早期需要一個起點——那時是 Yahoo,它創造了一個安全的空間讓人探索 web 是什麼。所以他們做了 **NANDA Town**(掛在 MIT 網站上),是一個沙盒,任何人都能把企業 agent、payments、memory 帶進來,在這個高度異質的系統裡探索,也有 ethical hacker 在裡面;他說推進得非常快。

另外有一系列由不同組織贊助的 hackathon,叫 **NandaHack**。

**國家規模**:在印度他們推出了名為「Duth」(意為 messenger)的計畫,涉及 **15 億個 agent**,**沒有企業把持**,跑在當地既有的身分與支付軌道上;**波士頓市**也和他們一起啟動了 Boston agent initiative,做 civic agents。

最後的視角翻轉:今天大家都在想 agents for X——agents for coding、browsing、debugging、shopping。**我們該把它翻過來**:services for agents、infrastructure for agents、compute for agents、insurance for agents、healthcare for agents、education for agents——社會裡我們為人做的每一件事,都得為 agent 再做一次。

### 金句

> "It's not like agents for e-commerce — this is commerce that's possible because of AI agents."(約 00:16)

整場演講的定位:重點不是把 agent 塞進既有電商,而是只有 agent 才做得出來的新交易形態。

> "OpenClaw is great, but it's only … a tool. I cannot call your OpenClaw agent. It's like having a telephone that can only make calls outside but can never receive calls."(約 00:18)

單向 vs 雙向 agent——他認為這正是 agentic web 還沒到來的證據。

> "Whoever builds this infrastructure will also own it."(約 00:18)

NANDA 存在的理由。

> "Intelligence will be discovered, intelligence will be priced, and intelligence will be coordinated at scale."(約 00:23)

open agentic commerce 的三個前提。

## English Notes

### TL;DR

- **Era shift**: AI's factory era — a handful of companies mass-producing, the rest of us consuming — is giving way to a **bazaar era** driven by edge AI, small models, and things running on your own machine. In computing terms: mainframe to PC.
- **Not agents for e-commerce, but commerce because of agents**: in his Sarah / Dr. John scenario, a doctor posts a $100 bounty on the open web, billions of agents wake up, form coalitions, and roughly ten of them solve it together and split the money. The doctor isn't calling one great health model; he's tapping a **network of intelligence exposed as a marketplace**.
- **Four bottlenecks**: to keep the agentic web as open as today's internet — rather than the walled gardens of iOS/Android or Facebook/Twitter — you need (1) a DNS-like structure, (2) passports and certification, (3) interoperability, and (4) attestation. That's MIT's **Project NANDA**.
- **Three research problems**: DNS for agents; **knowledge pricing** (data, models, inference, and compute all need prices — "a very beautiful mathematical problem"); and **co-learning** (agents forming coalitions, negotiating, competing, betraying — "game of thrones among agents").
- **Flip the framing**: stop thinking only about agents for X (coding, browsing, shopping) and start thinking **X for agents** — infrastructure, compute, insurance, healthcare, and education for agents.

### Key Points

#### Factory era to bazaar era (~00:14)

For some time AI has been in a **factory era**: a few large companies produce products in quantity and we consume them. Thanks to edge AI, small models, and workloads moving onto your own machine, we're shifting to the **bazaar era**. Much of his group's work at MIT is about what the internet of AI agents looks like once billions — maybe trillions — of them are on the open web.

#### The motivating scenario: Sarah, Dr. John, and $100 (~00:15–00:16)

Sarah, in rural Texas, has chest pain and a comorbidity and isn't getting good answers from her doctors. Her doctor, John, goes onto the open web and says: **"For a hundred bucks, can somebody solve the problem for Sarah?"**

Billions of agents worldwide wake up thinking they might claim a slice of that $100. They look at data relevant to the condition, start training models, form coalitions, and collaborate. Eventually a handful — say ten — solve it together, those ten split the $100, and everyone else disappears. Dr. John gets back what Raskar calls "an Expedia-like answer."

The framing matters: "It's not agents for e-commerce — **this is commerce that's possible because of AI agents**." And Dr. John isn't accessing one amazing health model; he's tapping into a **network of intelligence, available as a marketplace**.

#### From the internet of agents to the agentic web: NANDA (~00:17–00:19)

Some companies already run agents inside trusted boundaries. Soon agents will collaborate and negotiate with agents well outside those boundaries. But that's still just plumbing for geeks — going from the internet to the World Wide Web took HTML, browsers, and URLs.

**Project NANDA** started at MIT; on stage he glossed it as "AI agents in decentralized architecture." *Nanda* means joy in Sanskrit, and is also his sister's name.

His closest analogy is **high-frequency trading**, which works because there's a registry, every merchant and stock is pre-qualified, there's some price transparency, and there are mechanisms for fraud detection. **All of that has to be built again for the internet of AI agents.**

Then a pointed aside about OpenClaw: it's great, but it behaves only as a tool — "**I cannot call your OpenClaw agent.** It's like having a telephone that can only make calls outside but can never receive calls." One-way, not bidirectional.

Which raises the question of who builds this infrastructure, and the more troubling corollary: **whoever builds it will also own it.** Walled gardens for the agentic web, or something open, vibrant, neutral, safe, and scalable? That's NANDA's mission, organized around **four bottlenecks**: a DNS-like structure, passports and certification, interoperability, and attestation. His group has been in this space for 11 or 12 years, thinking since AlexNet about what happens when billions of individual AI systems interact.

#### Three research problems (~00:20–00:21)

1. **DNS for agents.**
2. **Knowledge pricing** — data, models, inference, and compute all need to be priced, "just the way when you hire a candidate we can figure out their salary." He calls it a very beautiful mathematical problem and openly recruits collaborators.
3. **Co-learning** — the last 14 years were a great run for machine learning; the next stretch is **machine co-learning**, how two agents learn from each other. And not just buying services and transacting: agents will form coalitions, negotiate, and compete for resources, with alliances and betrayals — "the game of thrones among agents."

#### Ecosystem: NANDA Town, NandaHack, and nation-scale deployments (~00:21–00:23)

The web needed a starting point, and that was Yahoo — a safe space to explore what the web even was. So they built **NANDA Town**, a sandbox off the MIT website where anyone working on enterprise agents, payments, or memory can bring their piece into a deliberately heterogeneous system, ethical hackers included. He says it's moving very fast.

There's also **NandaHack**, a hackathon series sponsored by various organizations.

At **nation scale**: in India they launched a program called *Duth* ("messenger"), covering **1.5 billion agents** with **no corporate capture**, running on the identity and payment rails the country already has. The **City of Boston** is also launching a Boston agent initiative around civic agents.

The closing reframe: today everyone thinks about agents for X — coding, browsing, debugging, shopping. **Flip it.** Services for agents, infrastructure for agents, compute for agents, insurance for agents, healthcare for agents, education for agents. Everything society does for people has to be done for agents too.

### Quotes

> "It's not like agents for e-commerce — this is commerce that's possible because of AI agents." (~00:16)

The whole thesis: not agents bolted onto existing commerce, but transactions only agents make possible.

> "OpenClaw is great, but it's only … a tool. I cannot call your OpenClaw agent. It's like having a telephone that can only make calls outside but can never receive calls." (~00:18)

One-way versus bidirectional agents — his evidence that the agentic web hasn't arrived yet.

> "Whoever builds this infrastructure will also own it." (~00:18)

The reason NANDA exists.

> "Intelligence will be discovered, intelligence will be priced, and intelligence will be coordinated at scale." (~00:23)

The three preconditions for open agentic commerce.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Project NANDA | MIT 發起、為 internet of AI agents 建立 discovery / identity / interoperability / attestation 基礎設施 | MIT-founded effort building discovery, identity, interoperability, and attestation infrastructure for the internet of AI agents | 官方展開為 Networked AI Agents in Decentralized Architecture;講者現場說 "AI agents in decentralized architecture" |
| NANDA Town | 讓任何人帶入企業 agent、payments、memory 的異質沙盒 | Heterogeneous sandbox where anyone can bring enterprise agents, payments, or memory | 掛在 MIT 網站上 / hosted off the MIT site |
| NandaHack | NANDA 生態系的 hackathon 系列 | Hackathon series for the NANDA ecosystem | 字幕作 "nandaack.mmedia.mmit.edu",應為 nandahack.media.mit.edu(待確認) |
| Duth(印度)| 印度國家級 agent 計畫,名稱意為「messenger」,涵蓋 15 億 agent | India's nation-scale agent program; the name means "messenger", covering 1.5 billion agents | 拼法待確認(可能為 Doot / दूत)|
| Boston agent initiative | 與波士頓市合作的 civic agent 計畫 | Civic-agent initiative with the City of Boston | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Romesh Rascar | Ramesh Raskar |
| bizarre era | bazaar era |
| Nanda / project Nanda | NANDA / Project NANDA |
| Nandatown | NANDA Town |
| Asians / Asian(多處)| agents / agent |
| at a stationation | attestation |
| wall gardens | walled gardens |
| open hive | open web |
| coorbidity | comorbidity |
| birectional | bidirectional |
| openclaw | OpenClaw |
| alexnet | AlexNet |

## 待確認 / To Verify

- 他結尾說 "come join us at nanda.edu",這不是有效網域,實際入口待確認(可能是 projectnanda.org 或 nanda.media.mit.edu)。/ He closed with "nanda.edu", which is not a valid domain — the actual entry point needs confirming.
- NandaHack 網址字幕作 "nandaack.mmedia.mmit.edu",推測為 nandahack.media.mit.edu,需確認。/ The NandaHack URL was garbled in the captions.
- 印度計畫名稱字幕作 "Duth",意為 messenger;正確拼法待確認。/ The India program was transcribed as "Duth"; correct spelling unconfirmed.
- 「1.5 billion agents」是規劃涵蓋人口對應的 agent 數還是已部署數量,講者未說明。/ Whether the 1.5 billion figure is deployed agents or target population coverage was not specified.
- NANDA 縮寫他現場說 "AI agents in decentralized architecture",與公開資料的 "Networked AI Agents in Decentralized Architecture" 略有出入。/ His on-stage gloss of the acronym differs slightly from the published expansion.
