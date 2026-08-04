---
title: "Why Your AI Agent Needs a Wallet: Agentic commerce on Arc with USDC and Nanopayments"
title_zh: "為什麼你的 AI Agent 需要一個錢包:用 USDC 與 Nanopayments 在 Arc 上做 agentic commerce"
speaker: "Harshal Bhangale"
affiliation: "Staff Software Engineer, Circle"
type: workshop
stage: Compass
date: 2026-08-01
session: "Session 1: AI Systems"
video: "https://www.youtube.com/watch?v=IBpR4uYftLY&t=3736s"
video_range: "01:02:16–01:55:41"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 1st - Morning Session [DownSub.com].srt"
status: draft
tags: [payments, stablecoin, x402, agentic-commerce, workshop]
---

# 為什麼你的 AI Agent 需要一個錢包(Why Your AI Agent Needs a Wallet: Agentic commerce on Arc with USDC and Nanopayments)

**一句話總結**:今天 agent 卡住的地方通常不是模型能力,而是**付款**——碰到 paywall 或註冊流程就把控制權交還給人;給 agent 一個有預算上限的錢包,加上 x402 + USDC 的按次微付款,它就能自己買到需要的資源。
**One-line summary**: What stops agents today usually isn't model capability but payment — they hand control back to you the moment they hit a paywall or a signup flow. Give an agent its own budget-capped wallet plus x402 + USDC pay-per-call, and it can buy what it needs on its own.

> 主持人於 **00:55:36** 介紹本場次,現場設備調整後 **01:02:16** 正式開始。以下為工作坊實際內容。
> The MC introduced this session at **00:55:36**; after an A/V setup delay the workshop actually began at **01:02:16**.

## 中文筆記

### 主題一:為什麼是 Circle,以及 agent 到底卡在哪(約 01:02:16–01:07:00)

Bhangale 開場先回答他在 meetup 常被問的問題:「Circle 不是穩定幣公司嗎,跟 agentic AI 有什麼關係?」他的答案很直接:Circle 發行 **USDC**——世界上最大的受監管數位美元——而**「agent 卡住的地方就是付款」**,而 Circle 花了很多年在讓付款更快更便宜。

他的時間軸:2023 年是用 ChatGPT 下 prompt;2024 年開始跑 eval、比較理解 agent 怎麼運作;2025 年是 MCP、skills 與 agent 編排(一個 agent 管一群 agent);**2026 年則是 agent 開始付錢給東西、也付錢給彼此**的一年。

早期數字(他引用的現場說法):**過去 30 天內 agent 為網路上的資訊付了約 2,400 萬美元,其中 98.8% 以 USDC 結算**;跟傳統金融比不算大,但預估到 2030 年 agentic economy 規模會到 **5 兆美元**。

問題的結構在於:**過去 30 年網際網路只為一種顧客而建——人類**。註冊流程、訂閱制、paywall、廣告,全都是為人設計的。現在出現了第二種顧客,而它消費資訊的能力比任何人類高好幾個數量級(一次 deep research 幾秒鐘讀完幾百頁)。碰到 paywall,agent 讀不到,研究品質就掉下來。而 merchant 那邊也開始意識到:與其向這個新客群收訂閱費,不如**按次收一小筆錢**賣單篇文章、單筆資料或單次推論。

### 主題二:為什麼訂閱制與信用卡都行不通(約 01:09:38–01:11:15)

- **「讓 agent 管我的訂閱和 API key 就好」**:可以,但**不 scale**。今天你要任務 X,明天要別的;agent 在研究途中臨時發現一個有價值的資源時,它沒辦法即時訂閱,於是就卡住。
- **「那給它信用卡」**:如果你能接受把卡號交給 agent,技術上可行,但**經濟上不成立**。merchant 對 agent 開的價格是「一分錢等級」,而信用卡手續費是 2.5–3%,高頻小額根本算不過來。

他的結論:**agent 需要的是像網際網路一樣運作的付款——即時、低成本、可程式化、永遠在線**。這就是 Circle Agent Stack 的定位。

### 主題三:上手路徑與 marketplace(約 01:11:15–01:15:00)

在 `agents.circle.com` 一鍵複製一段 prompt,貼進 Claude、Cursor 或你慣用的 coding agent 讓它跑:它會安裝 CLI 與對應 skill、產生一個錢包,並用 OTP 登入。

另一半是**可發現性**:CLI 能瀏覽 Circle 的 **agent marketplace**,目前約有**一千個來自各家供應商的付費 endpoint**,類別包含——

| 類別 | 例子與價格(講者現場所述) |
|------|------|
| 圖片生成 | 約 2 美分一張,不必再為單一模型付訂閱費 |
| 金融分析 | 加密貨幣報價等 |
| 預測市場 | 可以給 agent 一筆錢讓它下注 |
| Social intelligence | 他最愛用的 Reddit endpoint,查一次約 2 美分 |
| Web search | 品質更好的搜尋,價格是零頭 |

### 主題四:現場 demo——開一家咖啡烘焙店(約 01:17:00–01:53:30)

他在 Cursor 裡並排跑兩個 agent:**左邊是沒有錢包的 vanilla agent,右邊裝了 Circle CLI**(模型為 **Opus 5**,低 thinking + fast 模式,為了現場節奏)。他也在 `CLAUDE.md` 裡要求 agent 每一步都回報「做了什麼、花了多少」。任務是「在舊金山開一家咖啡烘焙店」:

1. **命名 + 網域查詢**:左邊用 whois 查;右邊先**列出錢包、確認餘額與預算**,再到 marketplace 找符合需求的網域 endpoint,花 **1 美分**查詢註冊資料,拿到準確的可用性與「每年 20 美元」的價格。他的評語是免費 web search 也查得到類似資訊,但**沒這麼準**。
2. **市場研究**:左邊搜免費網路資料;右邊呼叫 Google Scholar API 取得**付費牆後的學術文獻**,整段花費約 1 美元多。
3. **預算行為(意外亮點)**:其中一個錢包快見底(剩約 7 美分)時,**agent 自己縮減了研究範圍**;他改指向另一個資金較多的錢包才繼續。
4. **設計 logo**:右邊付約 **6 美分**呼叫專門的圖片生成模型直接產出 logo;左邊沒有圖片生成能力,只能慢慢兜出一個 HTML 版本。他前一天試跑時觀察到 agent 的判斷:**因為是公司 logo、品質重要,而貴的模型也只差幾美分,agent 主動選了較貴的模型**。
5. **做傳單 → 寄 email → 打電話**:email endpoint 2 美分、電話 endpoint 54 美分。最後現場真的接到 agent 打來的電話,AI 語音報告了網域可用性與價格、logo 與傳單已寄到信箱、以及豆源建議(Oakland 的 Royal Coffee、Crown Jewel microlots 的價格區間),還反問要不要幫忙註冊網域或做商標檢查。**沒有錢包的 agent 到這一步只能說「這兩件事我做不到,請你自己執行」。**

### 主題五:錢的安全性(約 01:25:59–01:27:30,回應現場提問)

這是他特別強調的設計取捨:**你不是把自己的錢包或資金交給 agent,而是為 agent 建立一個屬於它自己的錢包**。你可以管理一整支 agent 隊伍、各自分配預算,並在 CLI 層設定**每 session、每網站、每日的花費上限**;這些門檻與政策是**以密碼學方式強制執行**的。另外還有黑名單機制,不能與受制裁地址交易。Marketplace 本身也是**人工策展**的——不是任何人都能自行上架 endpoint,他們會實際測試。

### 主題六:底層協定——x402、EIP-3009 與 nanopayments(約 01:40:40–01:48:00)

**x402 的由來**:HTTP 協定的作者當年就設想過付款會發生在 HTTP 之上,所以初版規格裡就留了 **402 Payment Required** 這個狀態碼——但一直是死的,因為沒有可行的支付手段。區塊鏈與穩定幣讓它變得可行:

1. 賣方不再直接拒絕存取,而是回傳 **402** 與付款細節:「請在這條鏈上付 X 數量的 USDC 到這個地址」。
2. Agent(裝了 CLI)解讀這個回應,判斷「這個圖片生成 endpoint 要 2 美分」。
3. Agent 簽署一份 **EIP-3009 授權**(「我授權支付指定地址指定金額」),附在 header 上**重送同一個請求**。
4. 賣方收到帶授權的第二次請求,確認付款已完成或已授權,釋出資源。交易在鏈上結算,**不經過 ACH**。

**Nanopayments 解決 gas 問題**:即使在最便宜的鏈上,單筆 gas 也可能比付款本身還貴(他舉的極端案例是某客戶每次 API 呼叫只付 **5 微美分**)。所以 Circle 在 agent stack 裡另外做了 nanopayments:

- 你先把資金**存進 Gateway 智能合約**;
- 之後只是**簽授權**,賣方不直接把授權送上鏈,而是呼叫 Circle 的 endpoint;
- Circle 即時查看買方餘額(錢就在合約裡)、**扣除並保留**該筆金額,在 **50–100 毫秒**內回傳成功或失敗;
- 累積成千上萬筆授權後,在 **TEE(trusted execution environment)** 中**批次與淨額結算**,最後**以單一筆交易廣播上鏈**。

這樣既能做高頻的次美分付款,又不會用海量微交易塞爆區塊鏈網路。

### 現場問答重點

| 提問 | 回答摘要 |
|------|----------|
| Marketplace 的 endpoint 安全性怎麼把關? | 人工策展 + 實測,不是任何人都能自行上架 |
| 有沒有形式化驗證來保證 guardrail 與計畫的正確性? | 正在做;目前有黑名單/制裁地址阻擋;模型端的判斷取決於 harness,他們持續對自家 skill 做 eval 改進 |
| 怎麼教 agent「錢很難賺、要花得聰明」?(提問者以自己給高中生兒子錢包為類比) | CLI 目前**沒有**內建「挑最便宜」的規則;可以在專案裡加 skill,例如「花超過 5 美元就改找便宜 endpoint」,類似模型用量接近上限時改用便宜模型。實測中 agent 會自行判斷品質與價差 |
| 能不能讓閒置 GPU 上架、讓 agent 自己付運算費? | marketplace 已有可付費的 inference endpoint;歡迎企業來上架 |
| 有沒有做電商(例如買鞋)? | 正在與企業合作推廣。終局是「人類能在網路上買的任何東西,agent 也應該買得到」 |
| 有整合 ACH 嗎? | 沒有,用的是穩定幣;USDC 有多種 on-ramp 管道,入金後再撥給 agent 錢包 |
| 這些交易能接上 ADK 或 MCP 嗎? | 可以 |
| Agent 有記憶嗎?同樣問題能否得到一致答案? | 那是 **agent harness** 的功能(Cursor / Claude Code 的 session 與 memory 檔),Circle CLI 只是「另一個能付款的連接器」 |
| 有試過不同 reasoning level 嗎? | demo 為求速度用 Opus 5 低 thinking + fast;較弱的模型一樣能正確發出這些呼叫,差別在**決策與摘要品質**——因為終究只是個 CLI,連最便宜的模型都懂怎麼用 |

**最後的呼籲**:如果你是賣方或企業,**用幾行程式碼就能把既有 endpoint 包裝成可計費資源並上架 marketplace**。

### 金句

> "The moment they face a paywall … or the moment they are asked to log in or sign up on behalf of you, they give the control back to you. And that's the gap."(約 01:04:06)

整場工作坊的問題陳述。

> "What agents need is payments that work like the internet. Payments that are real-time, low cost, programmable, and always on."(約 01:11:01)

Circle Agent Stack 的設計目標。

> "You're not giving your wallet or your funds to your agent. You're creating a wallet for the agent itself."(約 01:25:59)

回答「把信用卡給 agent 很危險」的關鍵設計取捨。

## English Notes

### Topic 1: Why Circle, and where agents actually get stuck (~01:02:16–01:07:00)

Bhangale opened with the question he keeps getting at meetups: "Circle is a stablecoin company — what's your role in agentic AI?" His answer: Circle issues **USDC**, the world's largest regulated digital dollar, and **the thing agents get stuck at is payments** — which is exactly what Circle has spent years making faster and cheaper.

His timeline: 2023 was prompting LLMs through ChatGPT; 2024 added evals and a better understanding of how agents work; 2025 was MCP, skills, and agent orchestration (agents managing fleets of agents); **2026 is the year agents start paying for things and paying each other**.

The early numbers he cited on stage: in the last 30 days agents paid roughly **$24 million** for information on the internet, with **98.8% settled in USDC** — small next to traditional finance, but the agentic economy is projected at **$5 trillion by 2030**.

The structural problem: for 30 years the internet catered to exactly one kind of customer — humans. Signup flows, subscriptions, paywalls, and ads were all built for them. Now there's a second customer whose capacity to consume information is orders of magnitude higher (a deep-research query reads hundreds of pages in seconds). When it hits a paywall it simply can't get through, and research quality degrades. Meanwhile merchants are realizing that instead of charging this new customer base a subscription, they can charge a fraction of a cent for a single article, a single dataset, or a single inference.

### Topic 2: Why subscriptions and credit cards both fail (~01:09:38–01:11:15)

Giving an agent a handful of subscriptions and API keys works, but doesn't scale: you want task X today and something else tomorrow, and when an agent discovers a valuable resource mid-research it has no way to subscribe on the spot — so it stalls.

Credit cards fail on economics, not just on trust. Merchants are exposing these endpoints to agents at fraction-of-a-cent prices; an agent making high-frequency calls that each cost a penny cannot absorb 2.5–3% card fees.

Hence the framing: **agents need payments that work like the internet — real-time, low cost, programmable, always on.**

### Topic 3: Onboarding and the marketplace (~01:11:15–01:15:00)

At `agents.circle.com` you copy a prompt in one click and hand it to Claude, Cursor, or your coding agent of choice. It installs the CLI and skill, generates a wallet, and prompts for an OTP login.

The other half is discoverability. The CLI browses Circle's **agent marketplace** — roughly a thousand paid endpoints from a range of providers: image generation (~2 cents an image, no model subscription needed), financial analysis such as crypto prices, prediction markets (fund an agent and let it place bets), social intelligence (his favorite is a Reddit endpoint at ~2 cents a query), and higher-quality web search for a fraction of the usual cost.

### Topic 4: The live demo — starting a coffee roastery (~01:17:00–01:53:30)

Two agents side by side in Cursor: a **vanilla agent with no wallet** on the left, an agent with the **Circle CLI** on the right, both running **Opus 5** with low thinking and fast mode for the sake of the room's attention span. He had also edited `CLAUDE.md` so the paying agent reports what it did and what it spent at every step.

1. **Naming and domain lookup.** The left agent ran whois. The right agent first listed its wallets and checked its balance and budget, browsed the marketplace for a matching domain endpoint, and paid **1 cent** for an actual registry lookup — accurate availability plus a $20/year price. His own assessment: free web search finds similar information, just not as reliably.
2. **Market research.** The left agent scraped what's free on the web; the right agent called a Google Scholar API to reach paywalled scholarly articles, spending a little over a dollar for the segment.
3. **Budget behavior (the unplanned highlight).** With one wallet down to about 7 cents, the agent **trimmed its own research scope** to stay inside budget. He pointed it at a better-funded wallet to continue.
4. **Logo.** The right agent estimated the cost, then paid about **6 cents** to a specialist image model. The left agent, having no image generation, slowly assembled an HTML mock-up. In a dry run the day before, he watched the paying agent reason that a company logo warrants quality and that the price gap was only a few cents — so it chose the more expensive model on its own.
5. **Flyer, then email and a phone call.** The email endpoint cost 2 cents, the phone endpoint 54 cents. The room then heard an actual inbound call from the agent: an AI voice ran through domain availability and price, confirmed the logo and launch flyer were already in his inbox, gave sourcing advice (Royal Coffee in Oakland, Crown Jewel microlots, with per-pound pricing), and offered to register the domain or run a trademark check. The wallet-less agent got as far as drafting the email and handing both tasks back to the human.

### Topic 5: Securing the money (~01:25:59–01:27:30, answering an audience question)

The key design choice: **you are not handing your wallet or your funds to the agent — you are creating a wallet that belongs to the agent.** You can run a fleet of agents with a separate budget each, and set max spend per session, per site, and per day directly in the CLI, with those thresholds and policies **enforced cryptographically**. Blacklists prevent transacting with sanctioned addresses. The marketplace itself is curated and tested rather than open self-registration.

### Topic 6: The protocol layer — x402, EIP-3009, and nanopayments (~01:40:40–01:48:00)

**x402's origin story**: the authors of HTTP envisioned payments happening over HTTP and reserved status code **402 Payment Required** in the original spec, where it lay dormant for decades because there was no workable settlement rail. Blockchains and stablecoins made it viable:

1. Instead of denying access, the seller returns a **402** with payment details: send X USDC to this address on this chain.
2. The agent, via the CLI, interprets the response — "this image generation endpoint costs 2 cents."
3. It signs an **EIP-3009 authorization** ("I authorize paying this address this amount"), attaches it as a header, and **re-requests the same endpoint**.
4. The seller processes the second request, sees the payment is made or authorized, and releases the resource. Settlement happens on chain — no ACH involved.

**Nanopayments solve the gas problem.** Even on the cheapest chains, per-transaction gas can dwarf the payment itself — one Circle customer is making payments of about **5 micro-cents per API call**. So the agent stack adds nanopayments: deposit funds into the **Gateway smart contract**; sign authorizations as usual; the seller calls Circle's endpoints rather than settling each authorization on chain; Circle checks the buyer's balance in the contract, deducts and reserves it, and returns success or failure in **50–100 ms**; then hundreds and thousands of authorizations are **batched and netted inside a trusted execution environment** and broadcast on chain as a **single transaction**. High-frequency sub-cent payments, without flooding the network.

### Q&A highlights

Marketplace endpoints are curated and tested rather than open self-registration. On formal verification of guardrails: active work in progress; today there are blacklists and sanctioned-address blocking, while the model's own judgment depends on the harness, with continuous evals on the skills Circle ships. On teaching an agent the value of money (asked by an attendee who compared it to giving his high-school-age son a wallet): the CLI has no built-in "pick the cheapest" rule, but you can add project-level skills — e.g. switch to cheaper endpoints past a $5 threshold, the same way you drop to cheaper models near a monthly usage cap. Idle GPUs and self-funded compute: inference endpoints already exist in the marketplace, and enterprises are welcome to list. Commerce (buying shoes): they're working with enterprises on it, and the end goal is that anything a human can buy online should be purchasable by an agent. ACH integration: no — stablecoins, with USDC's many on-ramps funding the agent's wallet. ADK and MCP integration: yes. Memory and answer consistency: a function of the agent harness (Cursor, Claude Code), since the Circle CLI is "just another connector" that happens to pay. Reasoning levels: the demo used Opus 5 on low thinking for speed; weaker models still make the calls correctly, and the difference shows up in decision quality and summaries — it's a CLI at the end of the day, and even the cheapest models understand a CLI.

The closing pitch: sellers can wrap and monetize an existing endpoint in a couple of lines of code and list it on the marketplace.

### Quotes

> "The moment they face a paywall … or the moment they are asked to log in or sign up on behalf of you, they give the control back to you. And that's the gap." (~01:04:06)

The problem statement for the whole workshop.

> "What agents need is payments that work like the internet. Payments that are real-time, low cost, programmable, and always on." (~01:11:01)

The design goal behind Circle's Agent Stack.

> "You're not giving your wallet or your funds to your agent. You're creating a wallet for the agent itself." (~01:25:59)

The answer to "handing an agent your credit card is dangerous."

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Circle Agent Stack | 讓 agent 持有並使用 USDC、發現並支付 x402 服務的全端平台 | Full-stack platform letting agents hold USDC and discover/pay for x402 services | developers.circle.com/agent-stack |
| agents.circle.com | 一鍵取得安裝 prompt 的入口,含 CLI、skill 與 marketplace | One-click onboarding prompt, CLI, skill, and marketplace | 工作坊的操作起點 |
| Circle CLI | agent 用來管理錢包、瀏覽 marketplace、支付 endpoint 的命令列工具 | CLI for wallet management, marketplace discovery, and paying endpoints | 字幕多次誤作 "CircleCI" |
| x402 | 以 HTTP 402 狀態碼為基礎的 agent 付款協定 | Agent payment protocol built on the HTTP 402 status code | 講者引用近 30 天約 $24M 交易量 |
| EIP-3009 | 讓買方離線簽署轉帳授權的以太坊標準 | Ethereum standard for signed off-chain transfer authorizations | `transferWithAuthorization` |
| Nanopayments | 免 gas、次美分、高頻的 USDC 付款機制,經 Gateway 合約 + TEE 批次淨額結算 | Gas-free sub-cent high-frequency USDC payments via the Gateway contract with TEE batching and netting | Circle 公開資料稱最小可至 $0.000001 |
| Arc | Circle 的區塊鏈網路(議程標題中的 "on Arc") | Circle's blockchain network (the "on Arc" in the session title) | 工作坊口頭內容未展開 / not elaborated on stage |
| USDC | 受監管的數位美元,x402 交易的主要結算資產 | Regulated digital dollar; the dominant settlement asset for x402 | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Harsh Il Bengali(主持人介紹)| Harshal Bhangale |
| CircleCI | Circle CLI |
| X402 | x402 |
| "HTTP/2" 的作者設想付款 | HTTP(協定本身,非 HTTP/2)|
| EIP-3009(字幕正確)| — |
| "for the agent Akira" | for the agent era |
| "Fable or Sonic" | Fable or Sonnet(模型名)|
| cloud code | Claude Code |
| agents.circle.com(字幕正確)| — |
| "he has to uh the agent has to like then pay 3%" | 信用卡手續費 2.5–3% |

## 待確認 / To Verify

- 現場說「98.8% settled in USDC」,Circle 公開資料為 **99.8%**(30 天 $24.24M),需確認投影片數字。/ He said "98.8% settled in USDC" on stage; Circle's public figure is **99.8%** on $24.24M over 30 days — check the slide.
- Demo 中呼叫的 endpoint 名稱字幕聽成 "stable domains / stable email / stable phone",供應商名稱待確認。/ The demo endpoints were transcribed as "stable domains / stable email / stable phone"; the provider name needs confirmation.
- 圖片生成用的模型字幕作 "GPT image 2",正確型號待確認(講者當場也把 65 cents 口誤後更正為 6 cents)。/ The image model was transcribed as "GPT image 2"; exact model name to be confirmed (he also misspoke 65 cents before correcting to 6 cents).
- Demo 中的公司名與網域(字幕出現 "Sutro Roasters"、"Bear Ice Coffee"、"bears.coffee.com")互相矛盾,為自動字幕拼錯。/ The demo brand and domain names conflict across the captions ("Sutro Roasters", "Bear Ice Coffee", "bears.coffee.com") — auto-caption artifacts.
- 議程標題點名的 **Arc**,工作坊口頭內容幾乎未展開;Arc 與 nanopayments 的關係需另行查證。/ **Arc** appears in the session title but was barely discussed; its relationship to nanopayments needs separate verification.
- 市場研究步驟的花費字幕作 "117 cents",是否為 $1.17 待確認。/ The market-research step's cost was transcribed as "117 cents" — confirm whether that means $1.17.
