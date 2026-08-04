---
title: "A Society of Agents: Trust at Machine Speed, from Bits to Atoms"
title_zh: "Agent 的社會:從位元到原子,以機器速度建立信任"
speaker: "Alex Obadia"
affiliation: "Programme Director, Advanced Research & Invention Agency (ARIA)"
type: talk
stage: Compass
date: 2026-08-02
session: "Session 1: AI Safety"
video: "https://www.youtube.com/watch?v=l8GS08n-25Q&t=2097s"
video_range: "00:34:57–00:45:11"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 2nd - Morning Session [DownSub.com].srt"
status: draft
tags: [multi-agent, cryptography, funding, coordination, pluralism]
---

# Agent 的社會:從位元到原子,以機器速度建立信任(A Society of Agents: Trust at Machine Speed, from Bits to Atoms)

**一句話總結**:英國 ARIA 用 £50M 的 Scaling Trust 計畫,押注在「不同主人的 agent 如何在對抗環境下、以機器速度、無需中介地互相協調」——並且刻意把這套基礎設施做成開源公共財,因為他們認為技術單一化(monoculture)會讓人類整體對衝擊更脆弱。
**One-line summary**: ARIA's £50M Scaling Trust programme funds the research and infrastructure that lets agents with *different owners* coordinate securely at machine speed without intermediaries — and insists the stack be an open-source public good, because monoculture would leave humanity less resilient to shocks and erode our agency over time.

## 中文筆記

### TL;DR

- **ARIA 是什麼**:英國版 DARPA,「差別是我們沒有那個 D」——不碰國防,其他都做。成立三年、約 16 個計畫,每個約 £50–70M,涵蓋製造、更好的晶片、從免疫系統不同部位切入的疫苗、神經科技等。
- **Scaling Trust 要解的問題**:資助能讓 agent **協調**的研究與基礎設施。協調具體指三件事:**找到交易或互動的對手方、進行複雜的協商、以及執行協議**。前提設定是**對抗性的 multi-agent / multi-principal 環境**——不是單一擁有者底下的多 agent,而是**不同擁有者、代表不同主體**的 agent 互動。
- **關鍵設計立場**:要**程式化**(因為要跑在機器速度上,所以規模化時不放人在迴圈裡)、要**人人可用**、要**沒有中介**(明確的目標是限制基礎設施裡的系統性咽喉點),而且要**橫跨數位與實體世界**(agent 也可以是具身的)。技術上押注 programmable cryptography 與安全硬體的近期進展。
- **Agent 能做人做不到的事**:兩個 agent 可以靠安全硬體進入一個「房間」,互相揭露資訊,並**承諾若交易不成就從記憶中刪除該資訊**——人類只能用 NDA 近似,agent 可以程式化地做到。
- **為什麼堅持開源與 plurality**:避免滑向 monoculture。理由不是「多元本身好」,而是**單一化會讓人類在文化與技術上都對衝擊更不具韌性,並隨時間侵蝕我們的能動性**。
- **計畫三塊**:協調堆疊(數位 + 實體,已資助包含 Berkeley 在內的首批團隊)、支撐堆疊的**基礎理論**(自主協定生成、formal AI security、把密碼學根信任搬到實體世界)、以及一個**開放給大眾的大型測試場**,做成競賽,紅隊也互相競爭。

### 重點整理

#### ARIA 與 Scaling Trust 的框架(約 00:35–00:37)

ARIA(Advanced Research + Invention Agency)是英國的 R&D 資助機構,資助全球的 R&D 登月計畫。對照 DARPA 最好懂,不同在於:

> The difference with DARPA is we don't have the D. So we don't do anything defence related, but we do everything else.

特徵:以影響力為導向、高風險胃納、每個計畫追一個雄心目標,單一計畫規模約 £50–70M。成立三年,目前約 16 個計畫,橫跨製造、晶片、疫苗(從免疫系統的不同部位切入)、神經科技等領域。Obadia 是 Programme Director,負責其中的 **Scaling Trust**。

他也直說這場演講的目的有兩層:告訴大家 ARIA 正在資助什麼、以及**想聽聽現場對這個 thesis 的意見**(他在 Q&A 前明講「如果有任何質疑,我很樂意聽」)。

Scaling Trust 目前是**£50M、為期三年**的計畫。要資助的是讓 agent 能協調的研究與基礎設施,而「協調」被拆成三個具體能力:

1. agent 能不能**找到**需要交易、或非交易目的互動的**對手方**?
2. 能不能進行**足夠複雜的協商**?
3. 能不能**執行協議**?

而**「安全地」做這些事**之所以重要,是因為他們設定的場景是**對抗性環境下的 multi-agent、multi-principal 系統**——這裡他劃了一條清楚的界線:**不是單一擁有者底下的多 agent 系統**,而是不同擁有者、代表不同主體(principal)的 agent 彼此互動。所以其中一些 agent 可能是敵對的,可能存在**資訊不對稱**,可能目標不同。

#### 四個設計約束(約 00:38–00:39)

- **程式化(programmatically)**:因為希望這件事在**機器速度**上運作,所以規模化之後**不會、也不打算把人放在迴圈裡**。
- **人人可用、沒有中介**:他說這其實是一個關於**未來系統拓樸**的主張——**要限制這套基礎設施裡存在的系統性咽喉點(systemic choke points)**。
- **橫跨數位與實體**:他們把 agent 也視為可具身的,所以基礎設施必須延伸到實體世界,讓包含實體元素的互動也能安全進行。
- **技術賭注**:密碼學與安全硬體的新進展,特別是被稱為 **programmable cryptography** 的趨勢,加上安全硬體與技術堆疊其他部分的最新發展。他明說這些進展**鬆動了前一場演講(Gondara)提到的那些張力**——至少 trade-off 空間變了,我們可以落在空間中不同的點上。

#### 為什麼值得做:新市場,以及只有 agent 做得到的事(約 00:39–00:40)

他先承認現狀:**今天的 agent 堆疊還不夠成熟,把 agent 放出去替我們做事非常困難**,而且前面幾場已經看過各種攻擊的分類法。

但他對兩件事很興奮:

**(1) 新市場。** 類比是密碼學在現代數位社會的落地——**它間接讓電子商務這類東西得以存在**,我們今天的數位社會就站在那些建構元件之上。如果協調基礎設施能延伸到實體世界,可能會長出延伸到實體世界的新市場。

**(2) agent 獨有的能力。** 他給的例子非常具體:

> 兩個 agent 可以靠安全硬體進入一個所謂的「房間」。它們可以彼此揭露資訊,並且**承諾:如果這筆交易沒談成,就把資訊從記憶裡刪掉**。這是我們人類只能用 NDA 之類的東西去*近似*的事,但 agent 可以**程式化地**做到。

#### 開源、plurality,與對 monoculture 的警戒(約 00:40–00:41)

價值上的堅持有三:**開源、對所有人開放、沒有中介**。目標是讓**多個模型、多種心智能夠共存**——這個概念一般被放在 **pluralism / plurality** 的脈絡下討論。

他要避免的是**滑向 monoculture**:所有人都用同一套堆疊,而且**我們的偏好也間接被塑造成同一個樣子,社會的多樣性因此減少**。他特別強調這個論證不是「為了多元而多元」:

> 我們認為那會讓我們作為人類,在**文化上與技術上都更不具備抵禦衝擊的韌性**,而且**隨著時間侵蝕我們的能動性**。

正因如此,他們認為這套東西**應該以公共財的形式被建造**,而這也是 ARIA 願意用 grant 而非其他形式資助的理由。

#### 計畫的三層結構(約 00:41–00:44)

**第一層:協調堆疊(coordination stack)。** 分數位與實體兩側,已經資助了第一批團隊:

- 數位側,**包含 Berkeley 的團隊**,研究方向如:agent 如何**推理安全性**、如何**自主生成協定**、如何與複雜的安全系統互動,以及 agent 如何進行**複雜的協商推理**。
- 實體側,例如**更容易被 agent 互動、且具防篡改性的新型感測器**——而且已經有人在嘗試破解它們。

**第二層:支撐堆疊的基礎理論。** 他的判斷很直接:

> 我們看到的很多研究,如果你是從理論計算機科學和資安這些領域出身,會覺得**非常經驗性**。

所以他們要確保那個(可能是由經驗性方式收斂出來的)堆疊,**底下有理論支撐**——把既有的形式化安全思維應用到 AI 這個目前抗拒被完全形式化的新領域。他點名了幾個興奮的方向:**autonomous protocol generation、formal AI security、以及把密碼學概念搬到實體世界**(他提到量子密碼學與 physically unclonable function 這類把信任根從傳統密碼學換到實體世界的嘗試)。

**第三層:開放的大型測試場。** 即使有了堆疊、也有理論保證「沒有一個逼近中的不可能性結果、我們不是在完全的黑暗中工作」,**這仍然需要被測試**——因為這終究是 multi-agent、multi-principal 系統,堆疊必須被壓力測試。

- **任何人都可以提交自己的 agent**;可以測他們的堆疊,也可以**帶自己的堆疊**來。
- **做成競賽**:參賽者競爭勝出,而**紅隊也在競爭誰是最好的紅隊**。
- 要量測的是:**在對抗壓力下,安全 agentic 協調的 state of the art 到哪裡**。
- 同時要看**會湧現出什麼**:「我們人類可以決定需要什麼樣的堆疊,但正如我們多次看到的,湧現行為有時會揭露 agent 獨有的新能力」——所以測試場本身與任務都必須**夠開放式(open-ended)**。
- 對這條 AI safety 軌道最相關的一點:**理解存在哪些失效模式**。很多這類行為會是 out of distribution,而理解失效模式有助於釐清**需要什麼樣的安全要求,也許還有監管**。

最後的計畫近況:已經資助了一些團隊,並正與 **Google DeepMind、Cooperative AI Foundation、Schmidt Sciences** 合作一個**於 8 月 8 日截止**的徵案,資助標的包含他提到的沙盒與測試場等。

### 金句

> "The difference with DARPA is we don't have the D."(約 00:36)

一句話講完 ARIA 的定位。

> "We don't care about the single owner multi-agent systems. This is about different owner, different agents that are representing different principals."(約 00:37)

整個計畫最關鍵的問題設定:真正困難的是「不同主人的 agent」。

> "Two agents can enter a quote-unquote room using secure hardware … they can commit to deleting the information from their memory if the deal doesn't go through. These are things that as humans we can only approximate with, for example, NDAs."(約 00:40)

不是「agent 做得比人快」,而是「agent 做得到人做不到的事」。

> "We want to avoid a slide towards monoculture … it makes us as humanity less resilient to shocks both culturally and technologically, and erodes our agency over time."(約 00:41)

把 plurality 從價值觀主張轉成韌性論證。

## English Notes

### TL;DR

- **What ARIA is**: the UK's DARPA equivalent — "the difference with DARPA is we don't have the D," so no defence work, everything else. Three years old, around 16 programmes at roughly £50–70M each, across manufacturing, better chips, vaccines targeting different parts of the immune system, and neurotechnologies.
- **What Scaling Trust funds**: research and infrastructure that lets agents **coordinate**, meaning three concrete capabilities — find counterparties to trade or interact with, negotiate in sophisticated ways, and enforce agreements. The setting is deliberately **adversarial multi-agent, multi-principal**: not many agents under one owner, but agents with *different* owners representing *different* principals.
- **The design constraints**: programmatic (it must run at machine speed, so no humans in the loop at scale), available to everyone, **without intermediaries** — an explicit claim about system topology, aimed at limiting systemic choke points — and spanning digital *and* physical, since agents can be embodied. The technical bet is on programmable cryptography and recent advances in secure hardware.
- **What only agents can do**: two agents can enter a "room" backed by secure hardware, disclose information to one another, and **commit to deleting it from memory if the deal falls through** — something humans can only approximate with NDAs.
- **Why open source and plurality**: to avoid sliding into monoculture. The argument isn't diversity for its own sake — monoculture makes humanity **less resilient to shocks, culturally and technologically, and erodes our agency over time**.
- **Three programme layers**: the coordination stack (digital and physical, with first teams already funded including at Berkeley), the fundamental theory underpinning it, and a large **public test bed run as a competition**, red teams included.

### Key Points

#### ARIA and the shape of Scaling Trust (~00:35–00:37)

ARIA — the Advanced Research + Invention Agency — is a UK R&D funding agency that funds R&D moonshots worldwide. The DARPA comparison is the fastest way in, with one difference:

> The difference with DARPA is we don't have the D. So we don't do anything defence related, but we do everything else.

Impact-focused, high risk appetite, focused programmes chasing an ambitious goal, each around £50–70M. Three years old, roughly 16 programmes so far, spanning manufacturing, better chips, vaccines built on different parts of the immune system, and neurotechnologies. Obadia is the Programme Director for **Scaling Trust**.

He was explicit that the talk had two purposes: describe what ARIA is funding and already funds, and **get the room's opinion on the current thesis** — he offered before Q&A that he was happy to hear any scepticism.

Scaling Trust is currently a **£50M, three-year programme**. It funds the research and infrastructure that lets agents coordinate, where coordination decomposes into three capabilities:

1. Can agents **find the counterparties** they need to trade or otherwise interact with?
2. Can they **negotiate in sophisticated ways**?
3. Can they **enforce agreements**?

Doing this *securely* matters because the setting is **multi-agent, multi-principal systems under adversarial conditions** — and here he drew a firm boundary: **not single-owner multi-agent systems**, but agents with different owners representing different principals. Some of those agents may be adversarial; there may be information asymmetry; goals may differ.

#### Four design constraints (~00:38–00:39)

- **Programmatic.** Because this has to move at **machine speed**, they explicitly do not want humans in the loop at scale.
- **Available to everyone, without intermediaries.** He framed this as a claim about the **topology of the future system**: limit the systemic choke points that exist in the infrastructure.
- **Digital and physical.** Agents can be embodied, so the infrastructure must extend into the physical world and support secure interactions that include physical elements.
- **The technical bet**: new developments in cryptography and secure hardware — particularly the trend dubbed **programmable cryptography** — which he argued **break some of the tensions raised in the previous talk** (Gondara's), or at least shift the trade-off space so different points in it become reachable.

#### Why it's worth doing: new markets, and agent-only capabilities (~00:39–00:40)

He conceded the state of play first: **today's agent stack is not mature, and it is very hard to send agents off to do things for us**; earlier talks had already walked through taxonomies of potential attacks.

Two things excite him:

**New markets.** The analogy is cryptography in modern digital society — it indirectly **enabled things like e-commerce to exist**, and today's digital society stands on those building blocks. Extend coordination infrastructure into the physical world and new markets that reach into physical space become plausible.

**Things agents can do that humans cannot.** His example was concrete:

> Two agents can enter a quote-unquote room using secure hardware. They can disclose information to one another and **commit to deleting the information from their memory if the deal doesn't go through**. These are things that as humans we can only approximate with, for example, NDAs — that with agents we can do programmatically.

#### Open source, plurality, and the case against monoculture (~00:40–00:41)

Three commitments: **open source, open to all, no intermediaries**. The aim is a system where **many models and many minds can coexist** — the concept people usually discuss under **pluralism or plurality**.

What he wants to avoid is a **slide towards monoculture**, where everyone runs the same stack and, indirectly, **our preferences get shaped the same way and society loses diversity**. He was careful that this is not an aesthetic preference:

> We think it makes us as humanity **less resilient to shocks, both culturally and technologically**, and **erodes our agency over time**.

That is why they believe this should be built as a **public good**, and why ARIA is glad to fund it through grants.

#### The programme's three layers (~00:41–00:44)

**Layer 1: the coordination stack.** Digital and physical, with a first set of teams already funded:

- On the digital side, **including teams at Berkeley**, working on how agents **reason about security**, **autonomously generate protocols**, interact with sophisticated security systems, and reason about **negotiation** in sophisticated ways.
- On the physical side, for example **new sensors that are easier for agents to interact with and tamper-resistant** — and people are already trying to break them.

**Layer 2: the theory that underpins the stack.** His diagnosis was direct:

> A lot of the research that we see feels very empirical to us, at least if you come from theoretical computer science and these fields of security.

So they want the stack — which may well be arrived at empirically — to have **theory underneath it**: applying formal security thinking to a field of AI that currently resists being fully formalized. The directions he named: **autonomous protocol generation**, **formal AI security**, and **carrying cryptographic concepts into the physical world** (he pointed at quantum cryptography and physically unclonable functions as attempts to swap the roots of trust used in traditional cryptography into physical substrates).

**Layer 3: a massive public test bed.** Even with a stack and with theory assuring you that "there's no looming impossibility result and we're not working completely in the dark," **it still has to be tested**, because this is ultimately a multi-agent, multi-principal system and the stack needs stress.

- **Anyone can submit their agents.** They can test the funded stack, or **bring their own**.
- **Run as a competition**: teams compete to win, and **red teams compete to be the best red teams**.
- What it measures: **the state of the art in secure agentic coordination under adversarial pressure**.
- What else it looks for: **what emerges**. "We as humans can decide what stack is needed, but as we've seen many times, emergent behaviours sometimes reveal new things that agents can uniquely do" — so both the test bed and its tasks must be **open-ended enough**.
- Most relevant to this safety track: **understanding what failure modes exist**. Much of this behaviour will be out of distribution, and understanding the failure modes informs **what safety requirements — and perhaps regulation — are needed**.

Programme status: several teams funded, and a call in partnership with **Google DeepMind, the Cooperative AI Foundation, and Schmidt Sciences** **closing on 8 August**, funding among other things the sandboxes and test beds described.

### Quotes

> "The difference with DARPA is we don't have the D." (~00:36)

ARIA's positioning in one line.

> "We don't care about the single owner multi-agent systems. This is about different owner, different agents that are representing different principals." (~00:37)

The programme's defining problem framing: the hard case is agents with different masters.

> "Two agents can enter a quote-unquote room using secure hardware … they can commit to deleting the information from their memory if the deal doesn't go through. These are things that as humans we can only approximate with, for example, NDAs." (~00:40)

Not "agents do it faster than humans" but "agents do what humans cannot."

> "We want to avoid a slide towards monoculture … it makes us as humanity less resilient to shocks both culturally and technologically, and erodes our agency over time." (~00:41)

Plurality reframed from a values claim into a resilience argument.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| ARIA (Advanced Research + Invention Agency) | 英國 R&D 資助機構,資助全球登月型研究;約 16 個計畫,每個 £50–70M | UK R&D funding agency backing moonshots worldwide; ~16 programmes at £50–70M each | 成立三年;不做國防 / three years old, no defence work |
| Scaling Trust | £50M、三年期計畫,資助 agent 安全協調的研究與基礎設施 | £50M three-year programme funding research and infrastructure for secure agent coordination | 官網另有 Scaling Trust Arena(競賽平台)之名,演講中未點名 |
| 開放測試場 / open test bed | 開放公眾提交 agent 的大型競賽式測試場,紅隊同場競技 | Public competition-style test bed; anyone can submit agents, red teams compete too | 演講中稱 "a massive test bed that is open to the public" |
| Programmable cryptography | 講者押注的密碼學趨勢,與安全硬體共同鬆動安全 / 自主的 trade-off | The cryptography trend he's betting on, which with secure hardware shifts the security/autonomy trade-off | 明確回應前一場 Gondara 提到的性質衝突 |
| Physically unclonable functions | 把信任根從傳統密碼學搬到實體世界的方向之一 | One route to swapping cryptographic roots of trust into physical substrates | 與量子密碼學並列提及 |
| 合作徵案 / joint call | 與 Google DeepMind、Cooperative AI Foundation、Schmidt Sciences 合作,8 月 8 日截止 | Joint call with Google DeepMind, Cooperative AI Foundation, Schmidt Sciences; closes 8 August | 資助沙盒與測試場等 |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Alex Oadia | Alex Obadia |
| Arya | ARIA |
| Deep Mind | Google DeepMind |
| "50 million pound … so about $7 million" | £50M 約合 $67M(字幕金額錯誤)/ caption figure is wrong |
| texonomy | taxonomy |
| erodess | erodes |
| physically inclinable functions | physically unclonable functions |
| multi- aent | multi-agent |
| principles(指 multi-principal 那段)| principals |

## 待確認 / To Verify

- **£50M 的美元換算**:講者說「50 million pound, so about $7 million」——£50M 約合 $67M,字幕或口誤其一;金額以 £50M 為準。/ £50M ≈ $67M, not $7M; take the sterling figure as authoritative.
- **測試場的正式名稱**:演講中只稱 "a massive test bed";ARIA 官方資料另有 Scaling Trust Arena 的名稱,但講者未在台上使用,故不併入內文。/ He only said "test bed"; ARIA materials refer to a Scaling Trust Arena, but he did not use the name on stage.
- **已獲資助的 Berkeley 團隊名稱與 PI**:講者只說 "some teams at Berkeley",未點名。/ He said "some teams at Berkeley" without naming them.
- **ARIA 計畫總數**:講者說 "about 16 programmes so far",為口頭近似值。/ "About 16" was a spoken approximation.
