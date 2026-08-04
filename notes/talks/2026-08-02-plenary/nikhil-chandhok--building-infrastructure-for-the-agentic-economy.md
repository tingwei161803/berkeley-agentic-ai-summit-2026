---
title: "Building Infrastructure for the Agentic Economy"
title_zh: "為 Agentic 經濟打造基礎設施"
speaker: "Nikhil Chandhok"
affiliation: "Chief Product & Technology Officer, Circle"
type: talk
stage: Plenary
date: 2026-08-02
session: "Session 4: Agentic AI in Finance & Legal"
video: "https://www.youtube.com/watch?v=I2PosBXwoPI&t=7778s"
video_range: "02:09:38–02:17:15"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [finance, stablecoin, payments, agentic-economy, open-architecture]
---

# 為 Agentic 經濟打造基礎設施(Building Infrastructure for the Agentic Economy)

**一句話總結**:現行支付系統的每一條假設(finality、隱私、信任在應用層)都預設「人隨時在旁邊做治理」;當一個 agent 會生出 100 個 sub-agent、每個都需要價值與規則時,這些假設全部斷裂——**穩定幣的可程式化貨幣是唯一能在 agent 尺度上運作的軌道**。
**One-line summary**: Every assumption baked into today's payment rails — finality, privacy, trust living at the application layer — presumes a human is one step away to govern. When one agent spawns a hundred sub-agents that each need value and rules, those assumptions all break. Programmable stablecoin money is the rail that survives at agent scale.

## 中文筆記

### TL;DR

- **穩定幣不再是加密貨幣話題,是法律話題**:美國通過 **GENIUS Act** 之後,穩定幣就是「真錢」;該法有 18 個月的規則制定期,今年底走完,**明年起 Genius 正式生效**,公司和個人可以像用銀行的錢一樣使用穩定幣。
- **今天大多數的 agent 討論都是向內的**;USDC 的特殊之處在於它**活在公開網際網路上**——今天的典型用戶是全球那六十億有手機、卻沒有美元銀行軌道的人。他的賭注是:**agent 也會轉向外面,成為網際網路上的 endpoint,就像網站一樣**。
- **現行支付軌道在 agent 尺度上會斷**,他點名三個斷裂處:(1) **finality**——刷卡要等發卡行清算,是機率性的;放到成千上萬 agent 身上,風險會複利。(2) **隱私**——公開帳本利於稽核,但錢包餘額全公開就沒法做真的經濟活動。(3) **治理**——每一條假設都預設「人在一步之外隨時可介入」。
- **解方是 open architecture**:agent 跑在開放系統上、彼此互通,支付用任何市場上的穩定幣(不只自家的),因為 web 就是這樣長出來的——從 90 年代幾台 NNTP/FTP server 長成今天數不清的網站。

### 重點整理

#### 先把背景講清楚:穩定幣現在是法定意義上的錢(約 02:09–02:11)

他一開場先解釋自己為什麼站在這裡。Circle 是穩定幣發行商;穩定幣是「世界上一種新型態的錢」,根源在加密貨幣(傳統上理解的 Bitcoin、Ethereum 那一套),但**現在它是真的**:美國通過了 **GENIUS Act**,讓任何人都可以像用錢一樣用穩定幣交易。該法有 18 個月的規則制定期,今年底跑完;**明年 Genius 上線,穩定幣就是真公司、真人可以拿來做事的真錢**——就像銀行裡的錢或任何其他形式的錢一樣。USDC 從這個 on-chain 生態系長出來,他預期明年起在美國具備法償地位(**用語待確認,見下**)。

#### USDC 的差異:它活在公開網際網路上(約 02:11–02:12)

他指出當天所有關於 agent 治理與安全的討論都是**向內看**的(inward facing)。USDC 不一樣——它是**活在公開網際網路上的開放貨幣**:

- 美國有 3.3 億人,大多數人拿到美元銀行帳戶與美元支付方式並不困難。
- 但全球有 80 億人,其中約 **60 億人有手機、卻沒有辦法用美元交易**。USDC 做的第一件事就是讓這些人開始能接觸美元。
- 那些美元不住在銀行裡,它們住在鏈上,交易人人看得見。

他的核心賭注:**錢已經從「住在裡面」轉向外面,agent 也會**——agent 會成為網際網路上的 endpoint,就像網站是 endpoint 一樣,而技術一旦到位,大家就會競相打造這些新 agent。

他用 FSD(全自動駕駛)做類比:**FSD 的設計前提是「道路不會改變」;但如果你其實可以重做整套交通系統、重做整個公路網呢?** 這就是 Circle 思考 agent 與 USDC 時的角度。

#### 三個會斷裂的假設(約 02:12–02:16)

**(1) Agent 不會 tap to pay。** 你可以把信用卡交給 agent 說「去用我的卡花錢」。但想像你的 agent 生出 100 個 sub-agent——**每一個都需要價值、需要治理,而且每一個動作都需要可程式化**。現行支付軌道做不到這件事。他點出一個更深的觀察:現實世界裡的商務,甚至像 Android 這種成熟系統,其設計都是繞著「支付能做什麼、不能做什麼」長出來的。穩定幣給的是**可程式化的貨幣**——你可以附上邏輯,而且**不需要 agent 有銀行帳戶、不需要它有信用卡**。所以 agent 生 agent 生 agent,每一層都能有自己的鏈上錢包、自己的規則,而且所有追蹤都在公開處進行。

**(2) Finality 是機率性的。** finality 就是「我付你錢,而這筆交易已成定局」。這件事非常重要:agent 刷信用卡時,商家其實要等發卡行清算資金才拿得到錢——**那不是完全的 finality**。鏈上轉帳則要求錢從 wallet 1 到 wallet 2 是絕對定局的。

> 機率性的 finality 會讓系統裡的風險複利。如果你有數以百萬計的 agent——而在網頁與網站上,agent 數量超過人類這件事今天已經是事實——你不可能承受機率性的 finality。

**(3) 全公開的帳本擋住真實經濟活動。** 目前多數區塊鏈支付發生在公開帳本上,**稽核性極佳,但不利於做真的經濟價值**:如果我的錢包在鏈上完全公開、你看得到我有多少餘額,我很難做真正的經濟活動,因為洩漏的資訊太多。

而這三件事底下還有一條共同的假設:**「信任放在應用層」在 agent 尺度上極度困難**。現行支付系統裡搬動所有價值的每一條假設,都預設**人在一步之外、隨時在場做治理**。

#### 解方:open architecture(約 02:16–02:17)

Circle 的答案是開放架構:

- 所有 agent 跑在**開放系統**上,能與這些系統上的其他 agent 互動。
- 這些互動的支付不只用自家的穩定幣,而是**市場上任何可用的穩定幣**。
- **open by design、也 open by necessity**——因為 web 就是這樣演化的:從 90 年代初幾台 NNTP 與 FTP server,長成今天數不清的網站與網頁。

落地產品在 **agents.circle.com**:有 CLI,是一個以「任務」為單位的市集,**單筆付款可低到百萬分之一分錢**就完成一項任務。人們正在嘗試各種任務——從「幫我跑這個推論」到「做這份研究」、「幫我寫這段程式碼」。

> 所有這些設計都是由 agent 操作、為 agent 服務、屬於 agent 的(operated **by** agents, **for** agents, and **of** agents)。

### 金句

> "Probabilistic finality essentially compounds the risk in the system."(約 02:15)

在人類尺度可以忍受的機率性結算,在 agent 尺度會變成系統性風險。

> "Every assumption in the current payment system... assumes that the human is one step away, is always ready, is present for governance."(約 02:15)

這是他整場演講的軸心:agent 經濟不是把人的支付軌道借給 agent 用,而是要重建一套不預設人在場的軌道。

## English Notes

### TL;DR

- **Stablecoins stopped being a crypto story and became a legal one.** With the **GENIUS Act** passed in the US, stablecoins are real money. The law runs an 18-month rulemaking period that ends at the end of this year; **from next year GENIUS is live**, and companies and people can transact in stablecoins the way they do with bank money.
- **Most agent discussion right now is inward-facing.** USDC's distinguishing property is that it **lives on the public internet** — its typical user today is one of the roughly six billion people worldwide who have a phone but no dollar banking rails. Chandhok's bet: **agents will turn outward too, becoming endpoints on the internet the way websites are.**
- **Today's payment rails break at agent scale**, in three specific places: **finality** (a card payment clears through the issuing bank — that's probabilistic, and probabilistic finality compounds risk across millions of agents), **privacy** (a fully public ledger is great for auditability but leaks your balances, which makes real economic activity impractical), and **governance** (every assumption presumes a human is one step away and present).
- **The fix is open architecture**: agents running on open systems, interacting with other agents on those systems, paying in *any* available stablecoin — open by design and open by necessity, because that's how the web itself evolved from a handful of NNTP and FTP servers.

### Key Points

#### Setting the stage: stablecoins are now legally money (~02:09–02:11)

Chandhok opened by explaining why a stablecoin issuer belongs on an agentic AI stage. Circle issues stablecoins — "a new type of money that exists in the world," rooted in crypto as traditionally understood (Bitcoin, Ethereum) but now real in a legal sense. The US passed the **GENIUS Act**, which made it so anybody can transact with stablecoins just like they transact with money. The law goes through **18 months of rulemaking that ends at the end of this year; by next year GENIUS is live** and stablecoins are money that real companies and real people can use like bank money. USDC came out of that on-chain ecosystem, and he expects it to have legal-tender standing in the US by next year (**wording to verify, below**).

#### What makes USDC different: it lives on the public internet (~02:11–02:12)

He observed that the day's discussion of agent governance and agent security had been **inward-facing**. USDC is the opposite — open money on the public internet:

- Of the 330 million people in the US, most can get a dollar bank account and dollar payment methods easily.
- Of the roughly 8 billion people worldwide, about **6 billion have a phone but no real way to transact in dollars**. Making that possible was USDC's first job.
- Those dollars don't live inside a bank. They live on chain, and the transactions are visible.

His central bet: money has already turned outward, and **agents will turn outward too** — becoming endpoints on the internet much like websites are endpoints, with a race to build them once the tech is right.

His analogy is FSD: **self-driving was designed on the assumption that the roads won't change. What if you could redo the entire transportation system instead?** That's the frame Circle applies to agents and USDC.

#### Three assumptions that break (~02:12–02:16)

**(1) Agents don't tap to pay.** You can hand your agent a credit card and tell it to spend. But imagine your agent spawns a hundred sub-agents: **each one needs value, each needs governance, and each of their actions needs to be programmable.** Existing rails can't do that. His deeper point: much of real-world commerce — and even sophisticated systems like Android — is built around what payments can and cannot enable. Stablecoins give you **programmable money** you can attach logic to, **without the agent needing a bank account or a credit card**. So agents spawning agents spawning agents can each have an on-chain wallet with governing rules, with all the tracking done out in the open.

**(2) Finality is probabilistic.** Finality means: I have paid you, and that transaction is final. When an agent swipes a credit card, the merchant only gets the money after the issuing bank clears the funds — **that is not full finality**. On chain, you want absolute finality when money moves from wallet one to wallet two.

> Probabilistic finality essentially compounds the risk in the system. If you're imagining a future with millions and millions of agents — or more agents than humans, which is already true of web pages and websites today — you cannot have probabilistic finality.

**(3) A fully public ledger blocks real economic activity.** Most blockchain payments happen on a public ledger, which is **great for auditability but bad for real economic value**: if your wallet balance is fully visible on chain, you leak too much information to operate.

Underneath all three sits a shared assumption — that **trust can live at the application layer**, which becomes extremely difficult at agent scale. Every assumption in the current payment system, the system that moves all the value, presumes **the human is one step away, always ready, present for governance**.

#### The fix: open architecture (~02:16–02:17)

Circle's answer:

- Agents run on **open systems** and can interact with other agents on those systems.
- Payments for those interactions happen not just in Circle's stablecoin but in **any stablecoin available in the market**.
- **Open by design and open by necessity** — because that's how the web evolved, from a few NNTP and FTP servers in the early 90s to an innumerable number of websites and pages.

The product is at **agents.circle.com**: there's a CLI, and it's a marketplace of task-based activity where **a payment as low as a millionth of a cent** can get a task done. People are trying everything from "go infer this for me" to "go do this research" to "go write this piece of code."

> All of this is designed to be operated **by** agents, **for** agents, and **of** agents.

### Quotes

> "Probabilistic finality essentially compounds the risk in the system." (~02:15)

What is tolerable at human scale becomes systemic risk at agent scale.

> "Every assumption in the current payment system... assumes that the human is one step away, is always ready, is present for governance." (~02:15)

The axis of the whole talk: an agentic economy doesn't get to borrow the human payment rails — it needs rails that don't presume a human is standing by.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| USDC | Circle 發行的美元穩定幣,活在公開網際網路上 | Circle's dollar stablecoin, living on the public internet | Circle 的核心產品 |
| GENIUS Act | 美國穩定幣立法;18 個月規則制定期於今年底結束,明年生效 | US stablecoin legislation; 18-month rulemaking ends this year, live next year | 講者稱其為穩定幣「變成真錢」的分水嶺 |
| agents.circle.com | Circle 的 agent 產品入口:CLI + 任務市集,支援極小額付款 | Circle's agent surface: CLI plus a task marketplace with sub-cent payments | 字幕作 "agentscircle.com" |
| Circle Payments Network | 座談中他另提到的支付網路(見 panel 筆記) | Payments network he mentions in the panel session | 見 `panel--agentic-ai-in-finance-and-legal.md` |
| Arc | Circle 正在建的區塊鏈,需要 validator 與參與者對齊誘因 | The blockchain Circle is building; needs validators and aligned participants | 同上,座談中提及 |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Nikquille Chanduk / Nquille / to Keel / Nichol / Nikl | Nikhil Chandhok |
| genius act | GENIUS Act |
| agentscircle.com | agents.circle.com |
| N&TP | NNTP |
| payment rates | payment rails |
| FSD(未展開) | Full Self-Driving |

## 待確認 / To Verify

- 講者說 USDC「hopefully by next year 成為 legal tender in the United States」——GENIUS Act 規範的是支付型穩定幣的發行與監理,「legal tender(法償)」是講者的口語用法,正式法律地位待查證。/ The speaker said USDC will "hopefully by next year" be legal tender in the US; GENIUS regulates payment stablecoin issuance and supervision, and "legal tender" appears to be colloquial. Verify the formal status.
- 「as of June last year」與 GENIUS Act 實際簽署時間的對應待核。/ Cross-check "as of June last year" against the GENIUS Act's actual signing date.
- 「payments as low as a millionth of a cent」為口述數字;Circle 官方 nanopayments 文件的最小單位需比對。/ Verify the "millionth of a cent" figure against Circle's published nanopayments minimum.
- 「6 billion of 8 billion people have a phone」為口述估計,未附出處。/ The "6 of 8 billion have a phone" figure is as spoken, with no source given.
