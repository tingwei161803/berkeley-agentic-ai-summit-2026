---
title: "Earning Autonomy: Governance as Code for the Agentic Enterprise"
title_zh: "掙來的自主權:為 Agentic 企業打造 Governance as Code"
speaker: "Eric Aldana"
affiliation: "Head of Product, Credo AI(代 Navrina Singh 上台 / standing in for Navrina Singh, CEO & Founder, Credo AI)"
type: talk
stage: Compass
date: 2026-08-02
session: "Session 1: AI Safety"
video: "https://www.youtube.com/watch?v=l8GS08n-25Q&t=3384s"
video_range: "00:56:24–01:02:20"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 2nd - Morning Session [DownSub.com].srt"
status: draft
tags: [ai-governance, enterprise, autonomy, agent-harness, policy-as-code]
---

# 掙來的自主權:為 Agentic 企業打造 Governance as Code(Earning Autonomy: Governance as Code for the Agentic Enterprise)

**一句話總結**:企業從來不會讓一個新人第一天就擁有全部權限——實習工程師與交易員都是沿著「掙來的授權階梯」往上爬;但 agent 幾乎在部署當下就拿到全部權限,這是一個設計錯誤,而修法是把治理計畫直接編譯進 agent 的 harness。
**One-line summary**: Enterprises never grant a newcomer full authority on day one — interns and traders climb a ladder of earned authority — yet agents typically receive full authority the moment they're deployed. That's a design error, and the fix is compiling the governance plan directly into the agent's harness.

> **講者異動 / Speaker substitution**:議程列的講者是 Credo AI 創辦人暨 CEO **Navrina Singh**,但她當天無法出席,實際由產品負責人 **Eric Aldana** 代講(他開場即說明:「你們該知道的第一件事是,我不是 Navrina Singh」)。本篇以實際講者記錄。

## 中文筆記

### TL;DR

- **安全與治理是同一份工作**:在不同圈子裡它們常被當成兩個學科,但核心任務相同——**確保 AI 系統的行動符合其背後的人的意圖**。而在大型企業裡,「意圖」從來不是一個人的決定,它是**工程師、業務負責人、法遵與法務、把要求寫進採購合約的客戶、以及訂出有真實罰則的標準的監管與稽核方之間的協調問題**。治理就是這些意圖被調和並被強制落到系統行為上的過程。
- **失落的階梯**:企業讓人自主決策的權限是**掙來的**——實習工程師從有限的 production 權限開始,交易員要掙來自己的投資額度。這些階梯是企業花了多年試錯建起來的,**但對 agent 而言這個階梯基本上還不存在**。
- **can / may / act 三層心智模型**:**can**(capability,模型與其工具技術上做得到什麼,靠 benchmark 衡量)、**may**(authority,在此時此地、以它能取用的資料與工具,它被**允許**做什麼——可界定範圍、可撤銷)、**act**(autonomy,它**不需要等人**就能行使的那部分授權)。
- **現有工具都只覆蓋 can**:security 問的是「攻擊者能不能讓 agent 做壞事」,observability 問的是「它有沒有把工作做好」——兩者都在 can 這一層,**沒有人在處理 may**。
- **落點是 agent 的 harness**:不是 evaluation harness,而是**治理用的 harness**——把治理計畫編成**版本化、可設定的程式碼**,以 skills、hooks、guidance、managed settings 的形式**直接裝在 agent 執行的地方**,而不是放在 MCP、API gateway 或 proxy 上。

### 重點整理

#### Credo AI 的視角:治理是誰的問題(約 00:56–00:58)

Credo AI 是 AI 治理平台,服務對象是**大型企業與政府機關裡對 AI 負責的人**——他強調這不只是建構 AI 的人,更是那些**必須決定哪些 AI 系統夠安全、夠可信,可以建、可以買、可以在組織內部署**的人。

在 AI safety 這條軌道上,他先做了一個接合:

> 看你混哪個圈子、用哪一本術語解碼環,safety 和 governance 常被當成分開的學科。但在核心上,我認為**它們做的是同一份工作**——確保 AI 系統的行動方式符合其背後那些人的意圖。

而在大型企業裡,「意圖」本身就是一個**協調問題**,至少牽涉五方:

- **工程師**——建這個系統的人
- **業務負責人**——定義要解決什麼問題
- **法遵與法務**——決定組織可以接受哪些行動
- **客戶**——現在會把要求直接寫進採購合約
- **監管者與稽核者**——寫出帶有真實罰則的標準

> 所以**治理,就是組織裡這些不同意圖被調和、然後被強制落實到 AI 系統實際行為上的方式**。

#### 缺失的那把梯子(約 00:58–00:59)

他的核心比喻:大型企業讓一個人在有後果的決策上自主行動時,**那份權限是透過某種結構掙來的**。

- 每個實習工程師都**從有限的 production 存取權開始**,隨著資歷上升才逐步取得更多。
- 投資公司的每個交易員,都必須**掙來自己能投資多少的額度**。

這些**掙來的授權階梯(ladders of earned authority)**,是組織花了多年試錯才建立起來的。而:

> 對 agent 來說,這個階梯**在很大程度上還不存在**。**許多 agent 在部署的那一刻就拿到了完整權限——而這是一個設計錯誤**,也是我今天想談的東西。

一句話結論:

> **Capability 可能來自模型,但 autonomy 必須從企業那裡掙得。**

#### use case 這個治理單位被 agent 溶解了(約 00:59)

Credo AI 六年來出貨 AI 治理流程與工具,**治理的單位一直是 use case**——一個 AI 工具,加上它被部署進去的脈絡。例如「一個回答員工公司政策問題的 chatbot」:你可以在它周圍畫出一條非常清楚的邊界。

**但 agent 把這條邊界溶解了。**

> 對一個**能自己規劃步驟**的 agent 來說,什麼叫做一個 use case?它該有哪些 connector 的存取權?哪些資料來源?

而**當 use case 本身模糊掉,你用來治理它的參數也會跟著模糊掉**。這個壓力逼出了新的心智模型。

#### can / may / act(約 00:59–01:00)

- **can — capability**:這個模型與它的工具**技術上做得到**什麼。**Capability 是被 benchmark 出來的。**
- **may — authority**:這個 agent 在**此時此地**、以它能取用的資料與工具,**被允許**做什麼。**Authority 是被界定範圍、且可撤銷的(scoped and revocable)。**
- **act — autonomy**:它**不需要等一個人**就能行使的那部分授權。

在這個框架下,他下了那句關鍵論斷:

> Autonomy **不只是模型的屬性**。它是一種**企業層級的許可,透過證據掙來**。

接著是這套框架真正的診斷價值——**現有的工具堆疊全都停在 can 這一層**:

- **Security** 問的是:攻擊者能不能讓這個 agent 做壞事?
- **Observability** 問的是:它有沒有把自己的工作做好?

> 這些系統都是必要的,但**它們講的都是 can 那一層**——agent 能做什麼、做得好不好。**它們沒有一個真正在處理 may。**

#### 治理系統要做的三件事,以及落點:agent 的 harness(約 01:00–01:02)

一套 AI / agentic 治理系統要能:

1. **Compose(組合)**:吃進 AI 系統與其所在組織的完整脈絡,**產出一份治理計畫**——有哪些風險、要套哪些控制。
2. **Conduct(執行)**:把計畫實際跑起來,無論是透過 **evaluation** 還是 **guardrail**。
3. **Enforce / 留存證據**:把所有這些檢查**留下紀錄**。

而 Credo AI 正在思考的落地方式,是**直接透過 agent 的 harness**——也就是**坐在 agent 與它能碰到的系統之間的那段 runtime 程式碼**。他特別澄清:

> 這不是 evaluation harness,而是一個**治理用的 harness(a governing one)**。

做法是把 compose 出來的治理計畫,**嵌進一組版本化、可設定的程式碼**,由 harness 強制執行。形式上是 **skills、hooks、guidance、managed settings**,而且**直接安裝在 agent 執行的地方——不是 MCP、也不是 API gateway 或 proxy**。

他用一個**被治理的 Claude Code session** 當例子:

- agent 想讀取一個**已核准的 repo** → 系統**放行**。
- agent 想打開一個 **credential store** → **設定直接擋下**。
- 出現一個**風險超過門檻的相依套件** → **升級給 code owner 處理**。

而每一道檢查最終**都必須被浮現出來**,這也是透過同一份設定達成的。

收尾回到那把梯子:

> 我們說 agent 沒有的那把「掙得自主權」的梯子——**這就是它**。一個讓**企業能集體決定 agent 可以做什麼、在 agent 行動的地方強制執行這些決定、並且保留證據**的系統。

### 金句

> "Capability might come from the model, but autonomy must be earned from the enterprise."(約 00:58)

整場的主軸句,也是講題的展開。

> "Many agents receive full authority the moment they're deployed, and that is a design error."(約 00:58)

把「權限給太多」從營運疏失重新定性為**設計錯誤**。

> "None of them are really addressing the *may* piece."(約 01:00)

security 與 observability 的共同盲區診斷。

> "A system where the enterprise can collectively decide what the agents can do, enforce those decisions where the agents act, and keep the proof."(約 01:02)

Governance as code 的一句話規格。

## English Notes

> **Speaker substitution**: the agenda lists Credo AI founder and CEO **Navrina Singh**; she couldn't attend, so Head of Product **Eric Aldana** delivered the talk ("the first thing you should know about me is I am not Navrina Singh"). These notes record the speaker who actually presented.

### TL;DR

- **Safety and governance are the same job.** Different circles treat them as separate disciplines, but both exist to make sure AI systems act the way the people behind them intend. In a large enterprise, intent is never one person's decision — it's a **coordination problem** across engineers, business owners, compliance and legal, customers writing requirements into procurement contracts, and regulators and auditors writing standards with real penalties.
- **The missing ladder.** Enterprises grant autonomy on consequential decisions only through **earned authority**: intern engineers start with limited production access, traders earn their investment limits. Organizations built these ladders over years of trial and error — **and for agents that ladder largely doesn't exist yet.**
- **The can / may / act model.** **Can** is capability — what a model and its tools are technically able to do, established by benchmarks. **May** is authority — what the agent is permitted to do here and now with the data and tools it has, scoped and revocable. **Act** is autonomy — the authority it can exercise without waiting for a person.
- **Today's tooling only covers "can".** Security asks whether an attacker can make an agent do something bad; observability asks whether it's doing its job well. Both live in the *can* layer. **Nothing addresses *may*.**
- **The insertion point is the agent's harness** — not an evaluation harness but a **governing** one: the governance plan compiled into versioned, configurable code as skills, hooks, guidance, and managed settings, **installed directly where the agent runs**, not in an MCP server, API gateway, or proxy.

### Key Points

#### Credo AI's vantage point: whose problem governance is (~00:56–00:58)

Credo AI is an AI governance platform whose users are **the people at large enterprises and government agencies who are accountable for AI** — not just those who build it, but those who have to decide which AI systems are safe and trustworthy to **build, buy, and deploy** across their organizations.

Opening on an AI safety track, he made a joining move:

> Depending on what circles you run in and what jargon decoder ring you're using, safety and governance are often treated as separate disciplines. But at their core, I'd argue **they share the same job** — making sure AI systems act in a way that the people behind them intend.

And in a large enterprise, intent itself is a **coordination problem** across at least five parties:

- **Engineers** building the system
- **Business owners** defining the problem being solved
- **Compliance and legal** deciding what actions the organization is okay with
- **Customers**, who now write requirements into procurement contracts
- **Regulators and auditors**, writing standards that carry real penalties

> So governance is how all of these different intentions get reconciled and then enforced into how an AI system actually behaves.

#### The ladder that doesn't exist yet (~00:58–00:59)

His central analogy: when a large enterprise lets a human act autonomously on consequential decisions, **that authority was earned through some structure.**

- Every intern engineer **starts with limited production access** and earns more as they rise.
- Every trader at an investment firm has to **earn their limits** on what they can invest.

These **ladders of earned authority** were built over years of organizational trial and error. And:

> For agents, that ladder largely **doesn't exist yet**. Many agents **receive full authority the moment they're deployed, and that is a design error** — which is what I want to address today.

Compressed to a line:

> **Capability might come from the model, but autonomy must be earned from the enterprise.**

#### Agents dissolved the use case as a unit of governance (~00:59)

Across six years of shipping AI governance processes and tools, **the unit of governance was the use case** — an AI tool plus the context it's deployed in. A chatbot that answers employees' questions about company policy, say: you can draw a very clear boundary around that.

**Agents dissolve the boundary.**

> What *is* a use case for an agent that can **plan its own steps**? What connectors should it have access to? What data sources?

And **when the use case blurs, the parameters you use to govern it blur too.** That pressure produced the new mental model.

#### Can / may / act (~00:59–01:00)

- **Can — capability**: what a model and its tools are **technically able** to do. **Capability is benchmarked.**
- **May — authority**: what the agent is **permitted** to do **here and now**, with the data and tools it has access to. **Authority is scoped and revocable.**
- **Act — autonomy**: the authority it can exercise **without having to wait for a person**.

Within that framing came the load-bearing claim:

> Autonomy is **not just a model property**. It is an **enterprise permission earned through evidence**.

And then the framework's real diagnostic payoff — **the existing tooling stack all stops at *can***:

- **Security** asks whether an attacker can make an agent do something bad.
- **Observability** asks whether it can do its job well.

> These systems are essential, but **they all speak to that *can* layer** — what the agent is able to do and whether it's doing it well. **None of them are really addressing the *may* piece.**

#### Three jobs for a governance system, landing in the harness (~01:00–01:02)

An AI and agentic governance system needs to do three things:

1. **Compose** — take the full context of the AI system and its organization and **create a governance plan**: which risks apply and which controls need to be applied.
2. **Conduct** — execute that plan, whether through **evaluations** or **guardrails**.
3. **Enforce and keep the record** of all those checks.

The way Credo AI is thinking about landing this is **directly through the agent's harness** — the actual runtime code that sits between the agent and the systems it can touch. He was explicit about the distinction:

> This isn't an evaluation harness — instead it's a **governing** one.

Take the composed governance plan and embed it into a **versioned, configurable set of code that a harness can enforce**: **skills, hooks, guidance, managed settings**, installed **directly where the agent runs — not something like an MCP or an API gateway or proxy.**

His worked example is a **governed Claude Code session**:

- The agent tries to read an **approved repo** → the system **allows** it.
- It tries to open a **credential store** → the **configuration blocks** it.
- A **dependency above a risk threshold** appears → this gets **escalated to the code owner**.

And every one of these checks **needs to be surfaced**, which the same configuration handles.

The close returns to the ladder:

> This ladder for earning autonomy that we said didn't exist for agents — **this is it.** A system where the **enterprise can collectively decide what the agents can do, enforce those decisions where the agents act, and keep the proof.**

### Quotes

> "Capability might come from the model, but autonomy must be earned from the enterprise." (~00:58)

The spine of the talk, and the unpacking of its title.

> "Many agents receive full authority the moment they're deployed, and that is a design error." (~00:58)

Reclassifies over-permissioning from an operational slip to a **design** error.

> "None of them are really addressing the *may* piece." (~01:00)

The shared blind spot of security and observability tooling.

> "A system where the enterprise can collectively decide what the agents can do, enforce those decisions where the agents act, and keep the proof." (~01:02)

Governance-as-code, specified in one sentence.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Credo AI | AI 治理平台,服務大型企業與政府機關中對 AI 負責的角色 | AI governance platform for those accountable for AI in large enterprises and government agencies | 講者稱已出貨 AI 治理流程與工具約六年 |
| can / may / act | 治理 agent 的三層心智模型:capability / authority / autonomy | Three-layer mental model for governing agents: capability, authority, autonomy | 講者提出的核心框架 |
| compose / conduct / enforce | 治理系統要做的三件事:產出治理計畫、執行、留存證據 | The three jobs of a governance system: produce a plan, execute it, keep the record | 逐字稿在此處破碎,第三項名稱待確認 |
| Governing harness | 把治理計畫編成版本化程式碼,以 skills / hooks / guidance / managed settings 裝在 agent 執行處 | Governance plan compiled into versioned code as skills, hooks, guidance, and managed settings at the agent's runtime | 明確排除 MCP、API gateway、proxy 作為落點 |
| 被治理的 Claude Code session | 示範案例:核准 repo 放行、credential store 阻擋、高風險相依升級給 code owner | Worked example: approved repo allowed, credential store blocked, risky dependency escalated to the code owner | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Credto Aai / Credo AAI / CTOAI | Credo AI |
| Nina Singh / Deina | Navrina Singh |
| governis code | governance as code |
| cloud code session | Claude Code session |
| credential score | credential store |
| business owner ers | business owners |

## 待確認 / To Verify

- **治理系統三件事的第三項名稱**:逐字稿在此嚴重破碎(「keep a record of all of those different enforce」),compose 與 conduct 明確,第三項推測為 enforce,需核對投影片。/ The captions break down here; compose and conduct are clear, the third is inferred as "enforce" and needs the slides.
- **「skills、hooks、guidance、managed settings」**:這些名稱與 Claude Code 的既有機制高度吻合,但講者是否指 Credo AI 自有的抽象層、還是直接沿用 harness 原生機制,台上未說明。/ These names map closely onto existing Claude Code mechanisms; whether he meant Credo AI's own abstraction or the harness's native primitives was not stated.
- **產品名稱**:講者全程未點名任何 Credo AI 產品或功能的正式名稱,只描述方法。/ No Credo AI product or feature name was given on stage.
