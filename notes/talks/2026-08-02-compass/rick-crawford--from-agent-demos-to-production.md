---
title: "From Agent Demos to Production: How Postman Is Building Reliable AI Agent Infrastructure"
title_zh: "從 Agent Demo 到 Production:Postman 如何打造可靠的 AI Agent 基礎設施"
speaker: "Rick Crawford"
affiliation: "Field CTO, Postman(官網議程列為 Ankit Sobti, Co-Founder & CTO, Postman;現場為代講)"
type: talk
stage: Compass
date: 2026-08-02
session: "Session 2: AI Systems"
video: "https://www.youtube.com/watch?v=1UrriPJRSPU&t=819s"
video_range: "00:13:39–00:22:56"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [enterprise, multi-agent, guardrails, sales, autonomy]
---

# 從 Agent Demo 到 Production:Postman 如何打造可靠的 AI Agent 基礎設施(From Agent Demos to Production: How Postman Is Building Reliable AI Agent Infrastructure)

> **講者說明**:官網議程列出的講者是 Ankit Sobti(Co-Founder & CTO, Postman),但直播中主持人介紹、以及演講內容的口吻,都指向由 Postman 的 Field CTO **Rick Crawford** 代為發表(已查證 Rick Crawford 確為 Postman Field CTO)。本篇以實際講者為準。
> **Speaker note**: The official agenda lists Ankit Sobti (Co-Founder & CTO, Postman), but the MC's introduction and the talk's framing indicate it was delivered by Postman Field CTO **Rick Crawford** (independently verified as a Postman Field CTO). This note follows the actual speaker.

**一句話總結**:Postman 用企業銷售流程當試驗場,發現多 agent 架構會同時放大成本與混亂,真正的解法是「先蓋一個懂全域知識的 monolith agent,再往上疊 hallucination 防線、領域 persona、策略內容、以及以職務為界的授權層」,並用 help → recommend → act → own 這條 autonomy curve 決定每個場景該讓 agent 走多遠。

**One-line summary**: Postman used its own enterprise sales process as the testbed and found that a swarm of agents compounds both cost and confusion; the fix was to build one monolith agent that knows the whole domain and then layer a hallucination guard, domain personas, human-owned strategic content, and role-scoped authorization on top — with a help → recommend → act → own autonomy curve deciding how far the agent goes in each scenario.

## 中文筆記

### TL;DR

- **微服務的教訓在 agent 上重演**:hackathon 產出的一堆專用 agent,帶來的是 compounding cost 與 compounding confusion——agent 之間的交接與測試才是真問題。這其實是 decomposition 問題,而不是「再多做一個 agent」能解的。
- **結果越 deterministic,agent 越可靠**:win-loss agent 能說出「這筆生意輸在報價太高」而且人類可以逆推驗證;但同一個 agent 被問「怎麼開發潛在客戶」就會脫軌,產出無法判斷對錯。**要挑輸出可被回推驗證的問題來自動化。**
- **知識 ≠ 策略,對的答案不等於能用的答案**:agent 被問「該賣給哪個 persona」永遠回答 procurement——技術上不算錯,實務上會被客戶笑出會議室。策略性內容必須由擁有它的團隊(業務放 account plan、field engineering 放 solution play)人工餵進去。

### 重點整理

#### 問題:為什麼選企業銷售流程,以及 hackathon 揭露的三個核心問題(約 00:13:39–00:17:45)

Postman 原本是「開發流程 agent-first」的組織,但想進一步做出**能在營運中做決策的 runtime agent**。做完原型後,CEO 與董事會的興奮反而帶來更難的問題:怎麼衡量?怎麼管理?怎麼確保交付的東西維護得下去?ROI 與 runbook 就是在這一步冒出來的。

選定的題目是**企業銷售**:流程定義清楚(從發掘機會到續約),但跨很多團隊,而這些團隊之間**很難把上下文交接乾淨**;底下又是一大群系統,資料之間的關係難以釐清。結果是一個不透明的流程,每一步都在掉 context。

於是辦了 hackathon(約 00:15:52),工程師在 30 小時內做出一堆 agent——畫出來就是一團系統、連線與 agent 的亂麻。其中真正有價值的是 **win-loss agent**。從這裡歸納出三個核心問題:

1. **輸出越 deterministic,agent 表現越好**(約 00:16)。win-loss agent 能回答「這個客戶為什麼流失」,而人可以從它給的理由往回推——「嗯,報價太高,所以這筆輸了」,合理。但同一個 agent 被問「產生 leads 的最佳方式是什麼」就開始脫軌,產出無從判斷對錯。另外,模型越複雜、推理品質越好,但**理解那些結果的難度也同步上升**。
2. **這是個會複利的問題**(約 00:17:13)。做過微服務架構的人會認得這個形狀:A2A、agent 社群……最後拿到的是 **compounding cost 與 compounding confusion**,agent 之間的 handoff 與測試變成更大的難題。
3. **這其實是 decomposition 問題**(約 00:17:31)。他們一個個造 agent,卻沒意識到這些 agent 全都屬於**同一個 domain**(現場點名 Martin Fowler 的設計模式)。真正的難處是系統之間的介面與 context 的交接。

#### 解法:四層框架(約 00:18:00–00:20:45)

**第一層 — monolith agent**(約 00:18:00)。地基是一個掌握整個銷售流程知識的單一 agent:Salesforce、Gong 通話與逐字稿都進來,可以問出很有意思的問題與答案。它是很好的 co-pilot 與答案產生器,但**灰色地帶會開始編**;它是很強的通才,可是面對專門問題資訊太雜,給不出對的結果。

**第二層 — decomposition,兩個關鍵零件**(約 00:18:42)。
- **Hallucination layer**:除非你清楚知道資訊來源,否則不要給建議;如果沒有來源,就得解釋你為什麼得到這個結論。**兩件事都做不到的輸出,直接忽略。**
- **Domain-specific agents**:這不是寫程式的工作,而是 prompt——「我是業務,我平常會做這些事」,agent 就以那個 persona 回答問題。輸出變銳利、幻覺大幅減少,**但變成「自信地答錯」**。

**第三層 — 策略內容由人負責**(約 00:19:35)。知識與智能不等於策略。問業務 agent「該賣給哪個 persona?」——它每次都答 procurement。真去跟客戶說「我要賣給你們的採購部門」,會被笑出會議室。所以他們找出**擁有策略內容的團隊**來負責餵資料:業務團隊放 account plan,field engineering 放 solution play。輸出開始有策略相關性。

**第四層 — 以職務為界的授權**(約 00:20:20)。此時他們手上是一個懂整個組織的 super agent,卻沒有任何控制。除了「這是不是真的」之外,還得加一層:「**這份內容跟提出請求的職務有關嗎?**」所以去問 CTO agent,它不會把全公司 P&L 倒給你——它會把你的 context 與職務納入考量,只回你該看的部分。

#### Agent autonomy curve 與複利效應(約 00:20:50–00:22:56)

**Autonomy curve** 的核心是:每個階段,決策由人還是 agent 做?而且有**兩個**決策要分開看——誰提出請求,以及誰決定何時把結果推上去。

- **Help**:兩個決策都在人身上——我提問,我分析結果。
- **Recommend**:agent 開始接手其中一部分。
- **Act**:**最大的 step change 在這裡**——在 guardrail 範圍內,agent 同時做兩件事。
- **Own**:大家都在往這裡走——長時間執行、擁有整個生態系的 agent。

效果超出預期地好:建一個 agent 從「30 小時 hackathon」變成「幾個小時」——有了框架,有人只要進來設好 guardrail,再接上既有的知識體。消費端也從一小群使用者擴散到全公司。**開發時間與受益人數兩邊同時複利。**

還有一個沒預期到的行為改變:業務知道自己產出的 context 與提出的問題會直接餵養 agent 的價值之後,**discovery 做得更多、內容品質也更好**。

最後他們也把這些學到的東西做成平台:能衡量產出的 outcome、有一份可用 agent 的 catalog 讓團隊「聘用與解僱」,並看清每個 agent 在成本與投資報酬上的實際影響(約 00:22:42)。

### 金句

> "The more deterministic the outcome, the better the agent was."(約 00:16:20)

挑題目比調 prompt 重要:輸出能被人逆推驗證的場景,才是 agent 該先進的地方。

> "Don't recommend something unless you have a clear understanding of where you're getting that information from."(約 00:18:42)

Hallucination layer 的一句話規格。

> "It sharpened the output and it stopped doing a lot of the hallucinations, but it was confidently wrong. Knowledge and intelligence does not mean strategy."(約 00:19:25)

Persona 解決了幻覺,卻解決不了「沒有策略」——那是必須由人擁有的資產。

## English Notes

### TL;DR

- **The microservices lesson repeats itself with agents.** The pile of specialized agents from their hackathon produced compounding cost *and* compounding confusion — the handoffs and testing between agents were the real problem. It was a decomposition problem, not something one more agent could fix.
- **The more deterministic the outcome, the more reliable the agent.** Their win-loss agent could say "we lost this deal because our price was too high," and a human could reason backwards to check it. Ask the same agent how to generate leads and it went off the rails, producing output nobody could validate. **Automate the questions whose answers can be verified in reverse.**
- **Knowledge is not strategy.** Asked which persona to sell to, the agent said "procurement" every single time — not technically wrong, but it would get you laughed out of the customer's room. Strategic content has to be supplied by the teams that own it: account plans from sales, solution plays from field engineering.

### Key Points

#### Why enterprise sales, and the three problems the hackathon exposed (~00:13:39–00:17:45)

Postman already ran agent-first *development*, but wanted **runtime agents that make decisions** inside the business. Prototypes generated real excitement from the CEO and the board — and with it the harder questions: how do I measure this, manage this, and make sure what we ship stays maintainable? That is where ROI models and runbooks entered the picture.

They picked **enterprise sales** because the process is well defined (from identifying an opportunity to renewing the deal) yet spans many teams — and those teams struggle to hand off context to each other. Underneath sits a swarm of systems whose data relationships are hard to untangle. The net effect is an opaque process that leaks context at every step.

So they ran a hackathon (~00:15:52). In 30 hours engineers produced a mass of agents — drawn out, a tangle of systems, connections, and agents. The one that stood out was a **win-loss agent**, and from it came three core problems:

1. **The more deterministic the outcome, the better the agent performed** (~00:16). The win-loss agent could explain why an account was lost, and a human could work backwards from that reasoning and sanity-check it. Ask it "what's the best way to generate leads?" and it drifted, producing results nobody could judge as right or wrong. Separately, a more complex model reasoned better — but understanding its results got correspondingly harder.
2. **It is a compounding problem** (~00:17:13). Anyone who has built microservices recognizes the shape: A2A, agent communities, and then compounding cost plus compounding confusion, with handoffs and testing between agents becoming the dominant difficulty.
3. **It is a decomposition problem** (~00:17:31). They kept building individual agents without noticing that all of them belonged to the *same domain* (he name-checked Martin Fowler here). The interfaces between the systems and the handoff of context were the real challenge.

#### The four-layer solution (~00:18:00–00:20:45)

**Layer 1 — the monolith agent** (~00:18:00). The foundation is a single agent that understands the whole sales process: Salesforce, Gong calls, transcripts. It answers genuinely interesting questions and makes a great co-pilot — but in gray areas it starts making things up, and as a generalist facing specialized questions it simply has too much information to give the right answer.

**Layer 2 — decomposition, two pieces** (~00:18:42).
- A **hallucination layer**: don't recommend anything unless you clearly understand where the information came from; if you don't have it, explain why you reached that result. Output that can do neither is discarded.
- **Domain-specific agents**, which are not a coding task at all — they are prompts ("I'm a seller, here's what I typically do") that make the agent answer in that persona. This sharpened output and killed most of the hallucination, **but left it confidently wrong**.

**Layer 3 — humans own the strategy** (~00:19:35). Knowledge and intelligence are not strategy. Asked which persona to sell to, the sales agent answered "procurement" every time; walking into a customer and announcing you're selling to their procurement organization would get you laughed out of the room. The fix was to identify the teams that own strategic content and put them in charge of contributing it — sales adding account plans, field engineering adding solution plays. Outputs became strategically relevant.

**Layer 4 — role-scoped authorization** (~00:20:20). At this point they had a super agent that understood the entire organization and no controls at all. Beyond "is this true?" they added "**is this content related to the job that's requesting it?**" — so the CTO agent won't hand over the company's P&L; it factors in your context and job role and returns only what is relevant to you.

#### The agent autonomy curve and compounding value (~00:20:50–00:22:56)

The **autonomy curve** asks, at each stage, whether the human or the agent makes the decision — and there are *two* decisions to separate: who requests the information, and who decides when to promote the result.

- **Help** — the human does both: I ask the question, I analyze the result.
- **Recommend** — the agent starts taking over part of it.
- **Act** — **the biggest step change**: within guardrails, the agent does both sides of the equation.
- **Own** — where everyone is heading: long-running agents that own the entire ecosystem.

The payoff surprised them. Building an agent went from a 30-hour hackathon to a matter of hours: with the framework in place, someone sets up guardrails and builds on the existing body of knowledge. Consumption spread from a select audience to the whole organization. **Value compounded on both axes — development time and number of people benefiting.**

There was also an unplanned behavioral shift: once salespeople understood that the context they create and the questions they ask feed the agents' underlying value, they did more discovery and produced better-quality content.

Finally, they turned the learnings into a platform: measure the outcomes, keep a catalog of available agents that teams can "hire and fire," and see each agent's real impact in both cost and return on investment (~00:22:42).

### Quotes

> "The more deterministic the outcome, the better the agent was." (~00:16:20)

Choosing the problem matters more than tuning the prompt: start where a human can verify the answer in reverse.

> "Don't recommend something unless you have a clear understanding of where you're getting that information from." (~00:18:42)

The hallucination layer, specified in one sentence.

> "It sharpened the output and it stopped doing a lot of the hallucinations, but it was confidently wrong. Knowledge and intelligence does not mean strategy." (~00:19:25)

Personas fixed hallucination but couldn't manufacture strategy — that stays a human-owned asset.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Win-loss agent | Hackathon 產出中最有價值的 agent,解釋案子輸贏原因 | The standout agent from the hackathon: explains why deals were won or lost | 內部 agent / internal agent |
| Monolith agent | 掌握整個銷售 domain 知識的地基 agent | Foundation agent holding the whole sales domain's knowledge | 內部 agent / internal agent |
| Hallucination layer | 無明確來源就不建議、否則須解釋推理;兩者皆無則忽略輸出 | Guard requiring a clear source, or an explanation of the reasoning; otherwise the output is ignored | 內部機制 / internal mechanism |
| Agent autonomy curve | help → recommend → act → own 四階段的自主度光譜 | Four-stage autonomy spectrum: help → recommend → act → own | 演講核心框架 / the talk's central framework |
| Salesforce / Gong | Monolith agent 接入的資料來源(CRM 與通話錄音/逐字稿) | Data sources feeding the monolith agent (CRM and call recordings/transcripts) | 逐字稿 "Salesforce gone calls" |
| A2A | 被點名為多 agent 通訊的代表,對應到微服務的複利問題 | Cited as the agent-to-agent communication analogue of the microservices compounding problem | |
| Martin Fowler(decomposition pattern) | 用來說明「這是 decomposition 問題」的設計模式參照 | Design-pattern reference used to frame the decomposition problem | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Impostman | in Postman |
| gone calls | Gong calls |
| agents community agents | agent-to-agent / agent communities |
| discreet | discrete(講者當場改口為 deterministic) |
| rooting | routing(此處為口誤脈絡,實際語意為 handoff) |
| longunning | long-running |

## 待確認 / To Verify

- **講者身分**:官網議程列 Ankit Sobti(Co-Founder & CTO),但主持人介紹的是 Rick Crawford(Field CTO),已查證 Rick Crawford 確為 Postman Field CTO。若協調者採「議程優先」原則,此檔需改名為 `ankit-sobti--...`。/ The agenda lists Ankit Sobti but the MC introduced Rick Crawford (verified as a Postman Field CTO). If the agenda-first rule is applied, rename this file to `ankit-sobti--...`.
- 演講最後提到的 Postman agent 平台產品名稱未在逐字稿中出現,需看投影片補上。/ The name of the Postman agent platform mentioned at the end never appears in the transcript; check the slides.
- Autonomy curve 四階段的官方用詞:逐字稿為 "help / recommendations / act / own",正式命名待確認。/ The official wording of the four autonomy-curve stages.
