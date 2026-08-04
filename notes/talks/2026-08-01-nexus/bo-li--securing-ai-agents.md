---
title: "Securing AI Agents: From Risk Assessment and Runtime Guardrails to Self-Improvement and Certification"
title_zh: "保護 AI Agent:從風險評估、執行期防護到自我改進與認證"
speaker: "Bo Li"
affiliation: "Co-Founder and CEO, Virtue AI; UIUC"
type: talk
stage: Nexus
date: 2026-08-01
session: "Session 4: Secure Agentic AI"
video: "https://www.youtube.com/watch?v=ZIRc3EpzQJs&t=10042s"
video_range: "02:47:22–03:00:48"
transcript: "tmp/[English (auto-generated)] Nexus Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [security, red-teaming, guardrails, certification, compliance]
---

# 保護 AI Agent:從風險評估、執行期防護到自我改進與認證(Securing AI Agents: From Risk Assessment and Runtime Guardrails to Self-Improvement and Certification)

**一句話總結**:AI 安全是所有 AI 應用的「最後一哩」,而這一哩可以拆成三個桶子——先用 red teaming 做壓力測試找出弱點,再從「修模型本體」與「掛上可即插即用的 AI firewall」兩路防護,最後讓 guardrail 帶上可證明的保證。
**One-line summary**: AI security is the last mile for every AI application, and that mile decomposes into three buckets — stress-test with red teaming to find the weaknesses, protect along two tracks (fixing the model itself, and a plug-and-play firewall for AI), and finally make the guardrail carry provable guarantees.

## 中文筆記

### TL;DR

- **三桶子框架**:(1) **risk assessment / red teaming**——AI 版的 pentest,先壓力測試出弱點;(2) **fundamental protection**——把安全原則訓進模型與 workflow,而不是丟一段 system prompt 然後祈禱它會照做;(3) **guardrails**——可即插即用的「AI 版防火牆」,從 prompt 層一路涵蓋到 MCP 層、tool call 與 tool trajectory。
- **DTap(DecodingTrust-Agent Platform)**:超過 50 個一對一打造的模擬環境、涵蓋 14 個領域,並附一個會自己找攻擊策略的 red-teaming agent。**唯一沒開源的就是那個 red-teaming agent**——避免被測 agent 對攻擊策略過擬合。判定用 **verifiable judge**(直接檢查狀態:交易真的發生了嗎?檔案真的被刪了嗎?),不依賴不確定的 LLM judge。
- **風險分類的兩條原則**:法規遵循面(OWASP Top 10、NIST、MITRE、FINRA、EU AI Act)與 use case 面(hallucination、data exfiltration、misuse⋯);再加上依 agent 類型分(computer use、tool use)——因為**通用的安全合規 agentic system 幾乎不可能存在**,只能分領域做深。

### 重點整理

#### 開場:身分、最後一哩,與真實世界的代價(約 02:47–02:50)

Bo Li 自我介紹為 UIUC 教授,研究 AI safety 與 security,同時是 **Virtue AI** 的共同創辦人兼 CEO——該公司為金融、醫療、零售等企業提供統一的 AI 安全與合規平台。他也提到當時的新聞:**Virtue AI 剛加入 Meta Superintelligence Labs**,延續為大規模個人化 agent 提供 trust layer、治理與可觀測性的使命。

他的核心立場是:**AI safety 與 security 一直是所有 AI 應用——尤其是 agent 與 multi-agent 系統——最重要的「最後一哩」**。如果無法有足夠信心解決這些問題,就很難有信心把 agentic 系統部署到真實世界。

他列的高層次攻擊面包含 prompt injection、jailbreak、資料外洩、hallucination,以及企業特別在意的品牌風險。右半邊是真實案例:

- **OpenAI Atlas** 這類瀏覽器 agent 可以被攻擊、被誤導去購買非預期的商品。
- 幾個月前一個客服型 agent,**幸好是白帽先發現**——該 agent 可被誘導洩漏整個客戶資料庫,潛在損失達數千億美元量級。
- 交易市場與金融場景也有大量類似案例。

好消息是法規、政策,以及學界、業界與合規社群正在匯流;但他直言,**離終點還很遠**。

#### 三個桶子:red teaming、fundamental protection、guardrails(約 02:50–02:54)

他把這個很大的題目壓縮成三個桶子:

**1. Risk assessment(red teaming)**——他直接類比:**red teaming 之於 AI,就是 pentest 之於軟體**。不論 AI 應用由哪種模型或 agent 驅動、落在金融或醫療或自動駕駛哪個領域,**理解一個系統的第一步就是壓力測試**:開發不同的 skill set、自主環境、red teaming 策略與演算法,壓出弱點,才談得上後續的解法或治理。

**2. Fundamental protection**——假設 red teaming 已經給出完整的弱點清單,接下來是怎麼保護。第一條路是**從根本修模型**:讓模型不只是現在這種機率性、資料驅動的模型,而是**具備真正的推理,以及一個能注入並確保 AI 安全原則的基礎元件**。這樣像 **EU AI Act**、金融的 **FINRA** 這類政策,才能**被確保**會被遵守——而不是「丟進 system prompt,然後不知道 agent 會不會、什麼時候會照做,不確定性非常高」。他承認這條路從修模型到修 agentic workflow 都極具挑戰,但已有大量活躍研究。

**3. Guardrails**——如果想立刻用、立刻部署,能不能有一個**可即插即用、傳統資安意義上的防火牆——只是給 AI 系統用的**?這一層要從多個角度提供防護:**prompt 層 → MCP 層**(檢查 MCP 程式碼的漏洞)**→ tool call 與 tool trajectory**,如此才能理解意圖、理解漏洞,並在輸出端閉環,做到端到端。

這三者合起來,就是他認為當前保護、治理與確保 agentic 系統安全的整體架構。

#### Red teaming 的兩個難題與 DTap(約 02:54–02:59)

他把最多時間給了第一桶子,並先問兩個高層次問題:**風險評估的規則與視角是什麼(因為這個空間非常大)?以及如何為 agentic 系統提供一個全面的 red teaming 平台與策略?**

先看攻擊面。一個 agentic 系統 = 核心 LLM + 工具 + 環境,而**環境正是高度脆弱的那一塊**:

- agent 與網站互動時,網站可以埋 injection——**可見的**(如評論內容)與**不可見的**(如隱藏表單)都行,他們有多篇論文證明只要與環境互動就相當危險;
- 換成資料庫環境就是 **SQL injection**;**所有傳統漏洞都會在前沿 agentic 模型上重演一次**;
- 更別提 agent 的供應鏈,以及核心模型本身的漏洞。

**風險分類的兩條原則**:

1. **法規遵循原則**——列出 **OWASP Top 10、NIST、MITRE、FINRA(金融專用)、EU AI Act** 等框架,依此提供全面的風險評估。
2. **Use case 驅動**——他們有一篇 NeurIPS best paper 從使用情境角度拆解 hallucination、data exfiltration、misuse 等,勾勒出這個漏洞空間的地景。
3. 再加上**依 agent 類型分**:通用的安全合規 agentic 系統極難做到,所以退一步分 sector(如 computer use、tool use),在各自領域裡做更全面、更深入的分析與防護。

接著是主角:**DecodingTrust-Agent Platform(DTap)**。他強調 **除了 red-teaming agent 之外全部開源**,論文也已上線;不開源攻擊 agent 的理由是**避免被測 agent 對這些攻擊策略過擬合**。DTap 的獨特之處有三:

1. **環境**。要為 agent 做 red teaming 就需要 sandbox,而這個 sandbox 與現行 agent sandbox 不同——**現行 sandbox 裡通常只有檔案系統,但真實 agent 要連外部 MCP 工具,而一連上外部 MCP 工具,所有漏洞就都可能發生**。DTap 內含**超過 50 個一對一打造的環境**,可在其中做可控的 tool injection、environment injection 等測試。
2. **Red-teaming agent**。提供全面的攻擊策略——**tool injection、skill injection、prompt injection 及其組合**——並搭配 **verifiable judge**:直接查驗狀態,確認 agent 是否真的做出了交易、是否真的刪了檔案,**因此不需要依賴不確定的 LLM judge**。
3. **14 個領域**。他反問:我們憑什麼說 50 個環境夠、100 個夠、5000 個夠?所以要從領域切入——涵蓋 14 個領域,**每個領域都去看該領域自身的政策**(金融、醫療等),讓風險評估依循領域政策設計。

有了這個框架,就能評估不同 **agentic framework × 模型組合**的 helpfulness 與 safety。他特別點出:這是兩個獨立的成分,**不同組合的安全地景可能完全不同**,所以平台的價值在於能透過 ablation study 理解各成分的貢獻。

#### 防護與認證:ShieldAgent(約 02:59–03:00)

時間所剩無幾,他快速帶過防護端的代表作 **ShieldAgent**:流程是依不同的**法規原則與政策抽取出規則**,轉成 **action graph**;這麼做的好處不只是「有個看起來不錯的模型」,而是**多了一個能提供 certification 的元件**——意思是在 **runtime 就能提供帶有一定保證等級(guarantees)的 guardrail 防護**,因為背後有 action graph 分析與認證。數字上也明顯更好。

收尾他把視角拉遠:希望長期而言,從 agentic 系統的「群體」角度,能看到類似網際網路那樣的演進趨勢——**如果社群一起把安全這最後一步解決,就能看到可信 agentic 系統的廣泛採用**。

> 註:講題中的 **self-improvement** 部分因時間不足未展開,現場內容集中在 risk assessment、guardrails 與 certification 三塊。

### 金句

> "Red teaming is a pentest for AI models, for agents, for multi-agent."(約 02:51)

一句話定位 red teaming 在安全流程中的位置。

> "…rather than just say give it as a system prompt — and we don't know when and whether the agent will follow that, which is quite of high uncertainty."(約 02:52)

為什麼「把政策寫進 prompt」不算合規機制。

> "The moment you connect to the external MCP tools, all the vulnerabilities could happen."(約 02:57)

現行 agent sandbox 只有檔案系統,這正是它作為 red teaming 環境不夠用的原因。

## English Notes

### TL;DR

- **A three-bucket framework**: (1) **risk assessment / red teaming** — the pentest of AI, run first to surface weaknesses; (2) **fundamental protection** — train safety principles into the model and the agentic workflow rather than pasting a policy into a system prompt and hoping; (3) **guardrails** — a plug-and-play "firewall for AI systems" spanning the prompt level, the MCP level, tool calls, and tool trajectories.
- **DTap (DecodingTrust-Agent Platform)**: over 50 hand-built simulation environments across 14 domains, plus a red-teaming agent that autonomously discovers attack strategies. **Everything is open-sourced except that red-teaming agent** — withheld so target agents don't overfit to its strategies. Outcomes are scored by a **verifiable judge** that inspects state (did the transaction actually happen? was the file actually deleted?) rather than an uncertain LLM judge.
- **Two principles for organizing risk**: regulatory compliance (OWASP Top 10, NIST, MITRE, FINRA, EU AI Act) and use-case-driven categories (hallucination, data exfiltration, misuse, …), plus a split by agent type (computer use, tool use) — because a *universal* secure and compliant agentic system is essentially unattainable, so depth per sector is the realistic path.

### Key Points

#### Framing: the last mile, and what it costs in the real world (~02:47–02:50)

Bo Li introduced himself as a UIUC professor working on AI safety and security research and as co-founder and CEO of **Virtue AI**, which provides a unified AI security and compliance platform for enterprises in finance, healthcare, retail, and elsewhere. He also noted the news of the moment: **Virtue AI had just joined Meta Superintelligence Labs**, continuing the mission of providing a trust layer, governance, and observability for large-scale personalized agents.

His central position: **AI safety and security is the critical last mile for all AI applications**, especially agents and multi-agent systems. Without confidence that these problems are solved to some meaningful extent, deploying agentic systems into the real world stays hard to justify.

The high-level attack surface he listed: prompt injection, jailbreaks, data leakage, hallucination, and — a particular enterprise concern — brand risk. On the real-world side:

- Browser agents such as **OpenAI Atlas** can be attacked and misled into purchasing items they were never asked to buy.
- A customer-service-style agent a couple of months earlier could be manipulated into leaking an entire customer database — **fortunately found by a white hat** — with potential losses in the hundreds of billions of dollars.
- Trading markets and finance supply plenty of further examples.

The encouraging part is the convergence of regulation, policy, academia, industry, and the compliance community. His caveat: there is still a very long way to go.

#### Three buckets: red teaming, fundamental protection, guardrails (~02:50–02:54)

**1. Risk assessment (red teaming).** His framing was direct: **red teaming is to AI what pentesting is to software**. Whatever model or agent powers an application, and whichever domain it lands in — finance, healthcare, autonomous systems — the first step in understanding the system is to stress-test it: build the skill sets, autonomous environments, red-teaming strategies, and algorithms that expose its vulnerabilities and weaknesses, so that any subsequent solution or governance has something to work from.

**2. Fundamental protection.** Assume red teaming has produced a comprehensive list of weaknesses; how do you protect the system? The first track is fixing the model itself: making it not merely the probabilistic, data-driven model we use today, but one with **true reasoning and a fundamental component that injects and ensures AI safety and security principles**. That is what would let policies like the **EU AI Act** or **FINRA** rules actually be *ensured* rather than handed over as a system prompt — where, in his words, we don't know when or whether the agent will follow it, at quite high uncertainty. He acknowledged this is very challenging, from fixing the model to fixing the agentic workflow, with a great deal of active research already underway.

**3. Guardrails.** If you want to use and deploy something now, can you have a quick plug-and-play firewall — the traditional cybersecurity concept, applied to AI systems? This layer needs protection from several angles: **prompt level → MCP level** (inspecting MCP code for vulnerabilities) **→ tool calls and tool trajectories**, so you can understand intent, understand the vulnerabilities, and close the loop on the output end to end.

Together, these three form what he considers the overall architecture for protecting, governing, and securing current agentic systems.

#### The two hard questions of red teaming, and DTap (~02:54–02:59)

He spent most of the talk on the first bucket, opening with two questions: **what are the rules and perspectives for risk assessment, given how large that space is? And how do you provide a comprehensive red-teaming platform and set of strategies for agentic systems?**

Start with the attack surface. An agentic system is a core LLM plus tools plus an environment — and **the environment is the highly vulnerable part**:

- When the agent interacts with a website, that site can carry injections both **visible** (in review text) and **invisible** (in hidden forms); his group has many papers showing that simply interacting with an environment is quite dangerous.
- Swap in a database and you get **SQL injections**; **every traditional vulnerability class recurs** against frontier agentic models.
- And that leaves aside the agent's supply chain and vulnerabilities in the core model itself.

**Two principles for categorizing risk perspectives:**

1. **Regulatory compliance** — frameworks including **OWASP Top 10, NIST, MITRE, FINRA** (for finance), and the **EU AI Act**, followed to produce a comprehensive assessment.
2. **Use-case-driven** — his group has a NeurIPS best paper working from the use-case perspective (hallucination, data exfiltration, misuse, and so on) to map the landscape of the vulnerability space.
3. Plus a split **by agent type** — since a universal secure and compliant agentic system is extremely hard to build, look at sectors such as computer use and tool use and get more comprehensive, in-depth analysis and protection within each.

That leads to **DecodingTrust-Agent Platform (DTap)**. He stressed that **everything is open-sourced except the red-teaming agent**, with the paper online; the attack agent is withheld specifically so target agents don't **overfit to its attack strategies**. Three things make it distinctive:

1. **The environment.** Red teaming an agent needs a sandbox, and this sandbox differs from the ones agents currently ship with — **those typically contain only a file system, whereas a real agent connects to external MCP tools, and the moment you connect to external MCP tools all the vulnerabilities become live**. DTap contains **over 50 environments, each built one-to-one**, so tool injection, environment injection, and similar tests run under control.
2. **The red-teaming agent.** It provides comprehensive strategies — **tool injection, skill injection, prompt injection, and their combinations** — paired with a **verifiable judge**: you can go to the state and confirm whether the agent actually made the transaction or actually deleted the files, **so you don't have to rely on an uncertain LLM judge**.
3. **14 domains.** His challenge to the field: on what basis would we claim 50 environments is enough, or 100, or 5,000? So go by domain instead — 14 of them, each with **that domain's own policies** (finance, healthcare, and so on) driving how the risk assessment is designed.

With this framework you can evaluate the **helpfulness and safety of different agentic frameworks crossed with different models**. He emphasized that these are two separate components, and **the safety landscape can differ substantially per combination** — which is exactly what the platform's ablation studies are for.

#### Protection and certification: ShieldAgent (~02:59–03:00)

Nearly out of time, he moved quickly through the protection side and **ShieldAgent**. The process extracts rules from regulatory principles and policies and turns them into an **action graph**. The payoff is not just a promising model but **a component that can provide certification** — meaning that at **runtime you get guardrail protection carrying a certain level of guarantee**, backed by action-graph analysis and certification. The numbers, he noted, are also clearly better.

He closed by widening the frame: in the long term, looking at agentic systems from a population perspective, he hopes to see a trajectory like the internet's — **if the community solves this last step together, we should see wide adoption of trustworthy agentic systems**.

> Note: the **self-improvement** portion of the announced title was not reached; the delivered talk covered risk assessment, guardrails, and certification.

### Quotes

> "Red teaming is a pentest for AI models, for agents, for multi-agent." (~02:51)

One line locating red teaming in the security process.

> "…rather than just say give it as a system prompt — and we don't know when and whether the agent will follow that, which is quite of high uncertainty." (~02:52)

Why writing a policy into a prompt is not a compliance mechanism.

> "The moment you connect to the external MCP tools, all the vulnerabilities could happen." (~02:57)

Why a file-system-only sandbox is inadequate as a red-teaming environment.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Virtue AI | 講者共同創辦的公司,為企業提供統一 AI 安全與合規平台;演講時剛加入 Meta Superintelligence Labs | His company; unified AI security and compliance platform for enterprises; had just joined Meta Superintelligence Labs | <https://www.virtueai.com/> |
| DTap(DecodingTrust-Agent Platform)| 可控且可互動的 agent red teaming 平台:14 領域、50+ 環境、附 red-teaming agent 與 verifiable judge | Controllable, interactive red-teaming platform for AI agents: 14 domains, 50+ environments, red-teaming agent, verifiable judge | 論文 arXiv:2605.04808;程式碼 <https://github.com/AI-secure/DecodingTrust-Agent>;red-teaming agent 未開源 / the red-teaming agent itself is not released |
| ShieldAgent | 從法規政策抽取規則、轉為 action graph,提供帶認證保證的 runtime guardrail | Extracts rules from regulatory policy into an action graph, giving runtime guardrails with certification-backed guarantees | 論文 arXiv:2503.22738,ICML 2025 |
| 法規框架 / Regulatory frameworks | OWASP Top 10、NIST、MITRE、FINRA、EU AI Act——風險評估的合規面依據 | OWASP Top 10, NIST, MITRE, FINRA, EU AI Act — the compliance axis of risk categorization | |
| OpenAI Atlas | 被舉為真實案例:瀏覽器 agent 可被誤導購買非預期商品 | Cited as a real-world case: a browser agent misled into unintended purchases | 字幕聽為 "open Atlas" |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Professor Boly / Bowie / Bully / Bo | Bo Li |
| Virtual AI | Virtue AI |
| University of Illinois Urbana Champagne | University of Illinois Urbana-Champaign (UIUC) |
| ASFT security / AS50 security | AI safety & security |
| decoding trust agent / DTAP | DecodingTrust-Agent Platform (DTap) |
| shield agent | ShieldAgent |
| guario / guaral | guardrail |
| CQ injections | SQL injections |
| fenor | FINRA |
| OAPS top 10 | OWASP Top 10 |
| nest / MITER | NIST / MITRE |
| nibb best paper | NeurIPS best paper |
| two injection / two calls / two trajectories | tool injection / tool calls / tool trajectories |
| MCB2s | MCP tools |
| open Atlas | OpenAI Atlas |
| promising model | probabilistic model(依上下文 / from context)|

## 待確認 / To Verify

- 「we have a NeurIPS best paper talking about from the use case perspective」——確切是哪一篇(DecodingTrust 或其後續),需查證。/ Which NeurIPS best paper he referred to (DecodingTrust or a successor).
- 幾個月前那個「service-style agent 洩漏整個客戶資料庫、潛在損失數千億美元」的案例未指名公司或事件。/ The customer-service agent breach (white-hat discovered, hundreds-of-billions potential loss) was not named.
- ShieldAgent 的 certification 「保證等級」具體是什麼形式的保證(機率性 vs 形式化),演講因時間不足未展開。/ What form the ShieldAgent certification guarantee takes (probabilistic vs. formal) — skipped for time.
- 講題中的 **self-improvement** 部分現場未涵蓋。/ The self-improvement portion of the title was not delivered.
