---
title: "Enterprise AI - Agent Governance"
title_zh: "企業 AI:Agent 治理"
speaker: "Rao Surapaneni"
affiliation: "VP/GM, AI Search & Specialized AI, Google Cloud"
type: talk
stage: Plenary
date: 2026-08-02
session: "Session 1: Enterprise AI"
video: "https://www.youtube.com/watch?v=UdS3iisKhCk&t=1602s"
video_range: "00:26:42–00:41:39"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 2nd - Morning Session [DownSub.com].srt"
status: draft
tags: [enterprise, governance, agent-identity, security, google-cloud]
---

# 企業 AI:Agent 治理(Enterprise AI - Agent Governance)

**一句話總結**:企業裡的 agent 採用卡在「個人生產力」與「CTO 高規格自建」兩個極端之間,中間那一大片沒被解鎖的原因不是模型不夠強,而是缺少治理——而治理的三根柱子是 visibility、control、security,落地方式是給每個 agent 一個真正的身分,並把權限檢查從靜態設定改成隨任務與情境判斷的 runtime 檢查。
**One-line summary**: Enterprise agent adoption is stuck between two bookends — personal-productivity agents and high-code agents built by the CTO org — and the vast middle stays locked not because models are too weak but because governance is missing; the three pillars are visibility, control and security, and the way to deliver them is to give every agent a real identity and move permission checks from static configuration to task- and context-aware runtime enforcement.

## 中文筆記

### TL;DR

- **企業採用的兩個書擋**:一端是個人生產力 agent(找資訊、代做小事),另一端是 CIO/CTO 組織自建、跑完整安全掃描與審核流程的 high-code agent。兩端都動得起來,**中間那一大片才是還沒解鎖的**。
- **為什麼中間卡住**:兩個書擋之所以可行,是因為 agent 都在**沿用使用者身分**行動,企業既有的 IAM 自然生效。一旦 agent 被分享出去、或多個 agent 跨部門協作,「誰的權限」就崩解了——我把能讀薪資的 agent 分享給權限更低的同事會怎樣?反過來,分享給權限更高的同事又會怎樣?
- **治理三問**:visibility(這其實是新的 shadow IT——員工從網路上下載一個 skill 就用,你看得到嗎?)、control(least agency:查假期餘額可以、改薪資不行,而且要細到任務層級)、security(能不能主動降低風險、偵測惡意行為?出事誰負責——**你能開除一個 agent 嗎?**)。
- **Google Cloud 的解法是把 agent 塞進既有的企業流程,而不是另建一套**:為每個 agent **鑄造專屬身分(agent identity)**,於是 IAM、存取控制、kill switch 全部沿用;像員工在 LDAP 有 ID 一樣**註冊每個 agent**;靜態與 runtime 都要可觀測。
- **關鍵轉變:從靜態權限到 runtime 權限檢查。** 使用者入職一次設好權限就結束;agent 不行,查假期餘額和寫入薪資資料庫必須被區分。由 **Agent Gateway + IAM** 在任務發生的當下做檢查;**Model Armor** 在 runtime 做非確定性的政策分析(prompt injection、PII 外洩),再加上離線的異常稽核。
- **結論**:投資治理不是踩煞車,而是油門——「better governance unlocks more agent autonomy」。

### 重點整理

#### 現況:技術跑得快,組織走得慢(約 00:27–00:29)

他先講了一個對照:還記得手機曾經不准帶進企業、不能連內部系統嗎?現在 AI 面對的是**更大的問號**,但解法已經在路上了。

談新技術時,大家花很多時間討論「這技術是什麼、會顛覆什麼」,接著是「我能拿它做出什麼產品」,但**很少人想 day two**——部署完之後怎麼營運、怎麼管理。技術 × 產品 × 營運三者的交集,才是真正拉高採用率的甜蜜點。

企業客戶的問題在這幾年明顯換了三次:三、四年前是「證明給我看 AI 真的有用」;很快變成「教我怎麼用、怎麼做成產品」;現在他跟資深主管談的都是「**我知道我會大規模部署,幫我管理這個規模**」。

#### 兩個書擋,以及中間那片空白(約 00:29–00:30)

- **一端**:個人生產力產品——快速找到資訊、代為執行動作,個人或企業場景都有。
- **另一端**:CIO / CTO 組織自建的 high-code agent,走完整測試、安全掃描與審核流程,再部署給組織使用。

兩端都在動:員工端由個人生產力驅動,組織端由新投資驅動。但**中間有一大片還沒被解鎖**,原因就是治理。

#### 框架:把 agent 當實習生(約 00:30–00:31)

這是他建議產品設計時採用的心智模型。實習生進公司,你信任他做某些事、但不會給全部權限,同時也期待他交付成果。一個好的實習生會告訴你三件事:

1. **我交付了什麼**
2. **我需要幫忙的地方** → 這就是你的 human in the loop
3. **我解不開的地方** → 這就是你的 error analysis

而管理者這一端要能給回饋。**每一次 human-in-the-loop 的互動,都是一次擷取殘餘知識、讓下一輪自動化更好的機會**;error analysis 同理。把這些回饋迴路內建進組織,agent 的專業度會長得非常快。

他預期的終局:**每一項任務、每一位員工,都配有一支 agent 大軍**——可能是我的個人 agent,可能是替我做事的 agent,也可能是取代「去問那位專家同事」這個動作的 agent。

#### 治理缺口一:agent 分享時的權限落差(約 00:31–00:32)

現在能運作的兩個書擋,**都是因為 agent 用的是使用者身分**——使用者能存取什麼,agent 就存取什麼,企業既有的身分與存取管理自然覆蓋。

但當我建了一個 agent 並分享給同事:

- **我的權限比較高**:agent 會碰到同事看不到的資料。直接拒絕存取很容易,但那就給了同事一個壞掉的 agent。
- **同事的權限比較高**(他稱這是更棘手的情況):我把一個「更新薪資資訊」的 agent 給了權限更高的人,他就真的能改了。

#### 治理缺口二:跨部門的多 agent 協作(約 00:32–00:33)

例子:一個合約生成 agent 掌握定價方案與折扣資格;業務團隊有另一個 agent 在看客戶帳戶。兩者若能協作直接生成完美合約,組織鏈上的人工交接就少很多。但一旦跨越部門穀倉,問題就變成:**哪些資料會被曝光、哪些功能會被曝光、彼此被允許做到哪裡?**

#### 蒸餾出的三個需求:visibility / control / security(約 00:33–00:35)

企業現況是同時跑多個 LLM、不同 agent 做不同事用不同模型,底下再接一堆 MCP、API endpoint 與 CLI。要用一致的方式管理這一切,CIO 與資安長問的就是三件事:

- **Visibility**:「我花了大把時間解決 shadow IT,現在這根本是 **shadow AI**。員工從網路上下載一個他喜歡的 skill 拿來內部用,我怎麼知道?它又在存取什麼?」
- **Control**:如何限制到 **least agency**?查我的假期餘額可以;更新假期餘額我或許能接受風險;但**絕不允許自主 agent 更新薪資資訊**。這需要理解任務本身、理解資料限制,再做細粒度控制。
- **Security**:如何主動降低風險、偵測惡意行為?而且未必是 agent 失控——「以前出事大家怪實習生,現在怪 agent」,但**究竟誰要負責?組織裡做壞事會被開除,那你能開除一個 agent 嗎?**

他強調:要真正解鎖 agent 自主性,必須同時處理**技術、流程與人的心態**。

#### Google Cloud 的治理堆疊(約 00:35–00:41)

底層是 **Gemini Enterprise** agent 平台(可低代碼 / 無代碼建 agent),治理則是被當成基礎建材、可組合的多個模組:

1. **身分是一切的起點**。過去控制點是使用者身分;新世界裡他們**為每個在企業內運作的 agent 鑄造專屬身分**。這樣做的意義在於:企業現有的 IAM 流程可以無縫套用——你能識別一個 agent、能對它拉 kill switch、能用現有 IAM 管它的存取控制。
2. **註冊(registry)**:就像每位員工在 LDAP 目錄裡有 ID,每個 agent 也要註冊,才知道它有哪些控制、存取與權限。
3. **可觀測性**:不只在 agent 被鑄造出來的當下靜態檢查,**runtime 也要觀測**。
4. **前後端接點**:agent 可透過各種介面曝光(chat、Slack 等),後端接到各式資料源——能不能接得到,同樣回到身分。
5. **從靜態權限到 runtime 權限檢查**(他認為這是真正的新東西):使用者入職時設定一組權限就結束了,但 agent 需要**情境感知、任務感知**的權限。「查假期餘額」和「對薪資資料庫做寫入」是完全不同的兩件事,所以要在**任務正在發生的當下**判斷。他們用 **Agent Gateway** 搭配 IAM 授權來做這件事。
6. **Model Armor**:在 IAM 這種一次設定好的政策之上,加一層**非確定性的企業政策分析**——檢查 prompt injection、驗證 PII 是否洩漏、什麼東西正被帶出模型或資料。runtime 之外還要有離線檢查來找異常活動。
7. **沿用既有的 API 安全機制**:幾乎每家公司在「從內部資料庫走向行動裝置 / 面向消費者的 app」時,就已經在 API 層解決過「把身分綁定到可存取資料」這個問題。這些底層原語直接拿來用。

**收尾**:「用你既有的基礎設施,但上面要加一些特調醬料。投資治理,會讓你在這條 agentic 旅程上跑得更快。」

### 金句

> "You could not bring your own device into the enterprise and connect it to your enterprise systems. Think of what it took to get over that hump — and we are in an even bigger question mark at this point in AI."(約 00:27)

用 BYOD 的歷史類比:企業對新技術的抗拒是可以被跨越的,但這次的問號更大。

> "It used to be the case when something went wrong people would blame it on the intern. Now people blame it on an agent. But ultimately who's actually accountable for it? … With an agent, can you fire an agent?"(約 00:34)

全場最尖銳的一問——組織的問責機制建立在「做壞事會被開除」上,而 agent 不在這個機制裡。

> "The best context is the smallest context that gets the job done."(約 01:28,panel 環節)

他在後續 panel 回答 sovereign AI 時說的,可視為這場演講的補注:資料不一定要進模型,你可以在主權環境裡用前沿模型。

> "Investing in governance will actually help you accelerate as you go through this agentic journey."(約 00:41)

演講的結論句,也是他的招牌主張「better governance unlocks more agent autonomy」的另一種說法。

## English Notes

### TL;DR

- **Two bookends of enterprise adoption**: individual-productivity agents on one end, high-code agents built and vetted by the CIO/CTO org on the other. Both work today; **the wide middle is what's still locked**.
- **Why the middle is stuck**: both bookends work because the agent acts under the *user's* identity, so existing enterprise IAM already covers it. The moment you share an agent, or orchestrate agents across departments, that breaks — what happens when I share a salary-updating agent with a colleague who has *higher* access than me?
- **Three governance questions**: visibility (this is the new shadow IT — an employee downloads a skill off the internet and runs it internally; can you see it, and what is it touching?), control (least agency: checking my vacation balance is fine, writing to the salary database is not — and the distinction has to be made at task granularity), and security (can you proactively reduce risk and detect malicious activity? and who is accountable — **can you fire an agent?**).
- **Google Cloud's approach is to fit agents into existing enterprise process rather than build a parallel one**: mint a distinct **agent identity** for every agent so IAM, access control and kill switches all carry over; register each agent the way every employee has an ID in LDAP; observe both statically and at runtime.
- **The key shift is from static permissions to runtime permission checking.** A user's permissions are set once at onboarding; an agent's cannot be. **Agent Gateway** plus IAM evaluates authorization as the task happens, **Model Armor** runs non-deterministic policy analysis at runtime (prompt injection, PII leakage, exfiltration), and offline audits look for anomalies.
- **Conclusion**: governance is the accelerator, not the brake — "better governance unlocks more agent autonomy."

### Key Points

#### The gap between technology speed and organizational speed (~00:27–00:29)

He opens with an analogy: remember when mobile devices weren't allowed into the enterprise and couldn't connect to internal systems? AI is a bigger question mark than that — but implementations that make autonomous production agents possible are already arriving.

With any new technology, a lot of air time goes to *what is this and what will it disrupt*, then to *what can I build with it*. Almost nobody thinks about **day two** — once it's deployed, how do I operate and manage it? The sweet spot across technology, product and operations is what actually drives adoption.

Customer questions have turned over three times in a few years: "prove to me AI works" → "help me understand how to use it and build a product" → today, from senior leaders, "**I know I'm deploying at scale; help me manage it in operations.**"

#### Two bookends, and the unlocked middle (~00:29–00:30)

On one end, products that help individual productivity — find information fast, take actions on it. On the other, high-code agents built by the CIO/CTO org, put through proper testing, security scans and approval cycles, then deployed organization-wide. Employee productivity drives one end; new organizational investment drives the other. Between them sits a wide swath still waiting to be unlocked.

#### The framing: treat an agent like an intern (~00:30–00:31)

An intern joins; you trust them with some things but not full access, and you still expect delivery. A great intern tells you three things at the end of the day: **what they delivered**, **what they needed help with** (that's your human in the loop), and **what they couldn't solve** (that's your error analysis).

The manager's side of the loop matters too: feedback that helps the intern — or the agent — improve on exactly the cases that needed intervention. **Every human-in-the-loop interaction is an opportunity to capture residual knowledge and improve automation for the next cycle**, and the same goes for error analysis. Build those loops into the organization and agents gain expertise very rapidly.

Where this goes: **every task and every employee backed by an army of agents** — a personal agent, an agent doing work you'd otherwise do, or an agent standing in for the specialist coworker you'd have asked.

#### Governance gap #1: agency mismatch when agents are shared (~00:31–00:32)

The two working bookends work because the agent inherits the user's identity: what the user can reach, the agent can reach, and the enterprise's existing access wiring just applies.

Sharing breaks it in both directions. If I have higher access than my colleague, denying access is easy but hands them a broken agent. Trickier still is the reverse: I build an agent that updates salary information and hand it to a colleague whose access is *higher* than mine — now it actually works.

#### Governance gap #2: multi-agent orchestration across silos (~00:32–00:33)

A contract-generation agent knows pricing schemes and which discounts a customer qualifies for; a sales agent is working the account with the end customer. If those two orchestrate, you get the right contract with far fewer human handoffs. But crossing the silo boundary raises the real questions: **what data gets exposed, what functionality gets exposed, and what are you allowing each side to do?**

#### The distilled requirements: visibility, control, security (~00:33–00:35)

Enterprises already run multiple LLMs, different agents doing different things on different models, over a mix of MCP servers, API endpoints and CLIs. Handling all of it uniformly comes down to three questions CIOs and CSOs are asking:

- **Visibility** — "I spent a lot of time solving for shadow IT. Now this is essentially **shadow AI**. How do I know an employee isn't simply downloading a skill they like off the internet and using it internally? And what is it accessing?"
- **Control** — how do I restrict to **least agency**? An agent can check my vacation balance; I might accept the risk of it updating the balance; I do *not* want an autonomous agent updating salary information. That requires understanding the task, the data restrictions, and fine-grained control over both.
- **Security** — how do I proactively reduce risk and detect malicious activity? And note it need not be a rogue agent: "it used to be that when something went wrong people blamed the intern; now people blame an agent." Organizational norms rest on the idea that doing bad things gets you fired — **can you fire an agent?**

Unlocking full autonomy means solving the technology, the process, *and* the people mindset together.

#### Google Cloud's governance stack (~00:35–00:41)

The base is the **Gemini Enterprise** agent platform (low-code / no-code agent building), with governance as a set of composable building blocks:

1. **Everything starts with identity.** The user identity used to be the control point; now they **mint an identity for every agent operating in the enterprise**. That means existing identity and access management processes work seamlessly: you can identify an agent, pull a kill switch on it, and manage its access controls through the IAM solution you already have.
2. **Registration** — like every employee having an ID in the LDAP directory, every agent is registered so you know its controls, accesses and permissions.
3. **Observability** — not just statically at minting time, but at runtime.
4. **Surfaces and back ends** — expose the agent through whatever front end (chat, Slack, and so on) and connect it to any data source, with identity again gating what it can reach.
5. **From static permissions to runtime permission checking** — the genuinely new part. A user's permissions are generally set once at onboarding; here you need **context-aware, task-aware** permissions. Checking a vacation balance and writing to the salary database are different acts, so the check has to happen while the task is being performed. That's what their **Agent Gateway** does, coupled with IAM authorization.
6. **Model Armor** — on top of IAM policies that are set once, a layer doing **non-deterministic analysis of enterprise policies**: checking for prompt injection, verifying PII isn't leaking, watching what's being exfiltrated out of the model or the data. Alongside runtime checks, offline analysis looks for anomalous activity.
7. **Reuse API-layer security** — almost every company already solved "tie identity to what data this user can see" at the API layer when they went from internal databases to mobile and consumer-facing apps. Those primitives carry straight over.

**Closing**: use the infrastructure you already have, add the special sauce on top — and investing in governance will accelerate the agentic journey, not slow it.

### Quotes

> "You could not bring your own device into the enterprise and connect it to your enterprise systems. Think of what it took to get over that hump — and we are in an even bigger question mark at this point in AI." (~00:27)

The BYOD analogy: enterprises have crossed this kind of chasm before, but this one is wider.

> "It used to be the case when something went wrong people would blame it on the intern. Now people blame it on an agent. But ultimately who's actually accountable for it? … With an agent, can you fire an agent?" (~00:34)

The sharpest question in the talk — organizational accountability rests on consequences that don't apply to agents.

> "The best context is the smallest context that gets the job done." (~01:28, during the panel)

His answer on sovereign AI, and a useful footnote to this talk: data doesn't have to enter the model — you can do a great deal inside a sovereign environment using a frontier model.

> "Investing in governance will actually help you accelerate as you go through this agentic journey." (~00:41)

The closing line, and another phrasing of his mantra: better governance unlocks more agent autonomy.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Gemini Enterprise | Google Cloud 的企業 agent 平台,支援低代碼 / 無代碼建構 | Google Cloud's enterprise agent platform with low-code / no-code building | 治理堆疊的底座 / the base of the governance stack |
| Agent Gateway | 在任務執行當下做 runtime 權限檢查,搭配 IAM 授權 | Runtime permission checking at task execution time, coupled with IAM authorization | |
| Model Armor | 對企業政策做非確定性分析:prompt injection、PII 洩漏、資料外流 | Non-deterministic analysis of enterprise policies: prompt injection, PII leakage, exfiltration | Google Cloud 產品 / Google Cloud product |
| Agent identity | 為每個 agent 鑄造專屬身分,讓既有 IAM / kill switch 直接適用 | Minting a distinct identity per agent so existing IAM and kill switches apply | 講者被介紹為 agent identity 領域的先行者 / he was introduced as a pioneer in agent identity |
| A2A (Agent2Agent) | agent 之間溝通協作的開放協定,Google 發起、Linux Foundation 維護 | Open protocol for agent-to-agent communication; initiated by Google, maintained by the Linux Foundation | 講者為共同創建者 / he is a co-creator |
| AP2 (Agent Payments Protocol) | 以加密簽章 mandate 做可驗證的代理付款授權 | Verifiable agent payment authorization via cryptographically signed mandates | 講者為共同創建者 / co-creator |
| UCP (Universal Commerce Protocol) | 開源的 agentic commerce 標準,Google 與 Shopify、Etsy、Target 等合作 | Open standard for agentic commerce, built by Google with Shopify, Etsy, Target and others | 講者為貢獻者 / he is a contributor |
| MCP | agent 連接工具與資料源的協定,演講中作為既有生態的一部分帶過 | Protocol for connecting agents to tools and data sources; referenced as part of the existing stack | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Ralph / Ral Sur Panini | Rao Surapaneni |
| octa | Okta |
| AAL cycles | approval cycles |
| least agency(語意正確,保留) | least agency(least privilege 的 agent 版說法) |
| xfilled | exfiltrated |
| MCPS | MCP servers |
| AM process / IM policies | IAM process / IAM policies |
| ghat | chat |
| perto chart | Pareto chart |
| sacrosang | sacrosanct |

## 待確認 / To Verify

- 主持人介紹中提到他是 "co-creator of A2A, AP2, contributor to UCP, **ARD**" ——「ARD」對應的協定名稱查不到,待確認。/ The protocol heard as "ARD" in the introduction could not be identified.
- 主持人稱他 "recognized as a pioneer in agent identity in Okta 2026 Identity 25" ——該榜單的正式名稱待確認。/ Formal name of the Okta "Identity 25" 2026 list.
- Agent Gateway 是否為 Google Cloud 的正式產品名(或僅為架構層描述),待確認。/ Whether "Agent Gateway" is a formal Google Cloud product name or an architectural layer description.
