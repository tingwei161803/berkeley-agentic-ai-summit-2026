---
title: "Evals: The Engine for Agent Improvement"
title_zh: "Eval:驅動 Agent 改善的引擎"
speaker: "Aayush Agrawal"
affiliation: "Product Lead, Uber"
type: talk
stage: Compass
date: 2026-08-02
session: "Session 4: Agent Evaluation & Benchmarks"
video: "https://www.youtube.com/watch?v=1UrriPJRSPU&t=10854s"
video_range: "03:00:54–03:07:22"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [evaluation, platform-engineering, production-agents, tracing, observability]
---

# Eval:驅動 Agent 改善的引擎(Evals: The Engine for Agent Improvement)

**一句話總結**:每個 agent 團隊都理性地決定「先上線,eval 之後再說」,結果全都被困在事後補 eval、事後查為什麼壞掉的迴圈裡;Uber 平台團隊花一年把 eval 變成預設值——tracing 從第一天就開、starter kit 直接送到 Slack、用 CLI 讓產品團隊也能擁有 eval——並且把提問從「你的 eval 有沒有 90%?」換成「**你真的信任你的 eval 嗎?**」
**One-line summary**: Every agent team rationally decides to ship first and think about evals later, and every one of them ends up trapped in a loop of retrofitting evals and forensically reconstructing why the agent broke. Uber's platform team spent a year making evals the default — tracing on from day one, starter-kit evaluators pushed into Slack, CLI experiences that let product teams own the process — and replaced the question "is your eval above 90%?" with "**do you actually trust your eval?**"

## 中文筆記

### TL;DR

- **問題不是團隊不想做 eval,是摩擦力**:每個團隊都想要高品質的 production agent,但都選擇「先把 agent 上線,eval 之後再想」——這在要驗證 PMF 的當下是**完全理性的決定**。代價是掉進「事後補 eval + 事後查為什麼壞掉」的無盡迴圈。平台團隊的工作就是把這些摩擦點一個個消掉。
- **四個介入手段**:(1) 第一天就在**每個環境**開 tracing;(2) 用 agent 的建構脈絡與文件自動推薦 **starter kit evaluator**,並直接推播到 **Slack**;(3) 用 **CLI 與 skills** 把 eval 從工程專屬變成產品團隊也能擁有的東西;(4) **換掉敘事**——這一項沒有工具可以解。
- **最好的說服素材是一個失敗案例**:語音叫車的離線 eval 有 95%+,但 production eval 顯示**每個 session 的輪數異常偏高**。追下去發現:乘客要去 SFO,**背景有人說了一句「我想吃 pizza」**,agent 把它當成輸入,開始把人導向最近的 pizza 店。
- **終點是把 eval 從「分數」變成「引擎」**:traces → 失敗被**自動分類** → 自動提出對 agent 與 evaluator 的修改建議 → 團隊只要 accept / reject。**分數是你已經知道的事;引擎是持續讓 agent 往客戶在乎的方向靠攏。**

### 重點整理

#### 開場的三個舉手題(約 03:01)

Aayush Agrawal 是當天 Compass Stage 的壓軸。他先用三個問題暖場:

1. 今天有誰搭過 Uber?(少數人舉手)
2. **更重要的:誰真的為 production 的 agent 寫過 eval?**(他稱這些人為 real builders)
3. **最後一題,你要為這件事感到驕傲:那些 eval 有沒有告訴你什麼、進而改變了你出貨產品的方式?**

他要指出的正是這條分界線:**把 eval 當成一個打勾項目,和 eval 真的改變你的產品方向,是兩件事。** 而讓每一個 agent 團隊都能做到後者,**正是 Uber 花了一年多在做的事**。

#### 背景:Uber 的 agent platform(約 03:02)

Uber 正在整個生態系中出貨 agent——**對外**(例如用語音叫車)與**對內**都有。在企業規模上支撐這一切的,是他所管理的 **Uber agent platform**,底下有一系列元件,讓 agent 團隊不必操心基礎設施。這場談的是其中的 eval。

#### 診斷:一個理性的決定,一個必然的迴圈(約 03:02–03:03)

他觀察到跨團隊的共同模式:**每個團隊都想要高品質的 production agent,但每個團隊都做了同一件事——「我先把 agent 上線,eval 之後再說。」**

他很公允地指出**這是非常理性的決定**:他們當下要證明的是 product-market fit,他們只想知道這東西到底行不行。

**但代價是:他們接著就被困在一個無情的迴圈裡——事後補 eval,事後回頭拼湊那個 agent 到底為什麼壞掉。**

平台團隊的結論是:存在**真實的摩擦點**,阻止團隊更早進入有 eval 的狀態。**那就把它變成零摩擦。**

#### 四個介入:讓 eval 成為預設值(約 03:03–03:05)

**1. Tracing 從第一天、每個環境開始**

(他也提到這點當天很多講者都講過。)只要開發一啟動,**每個環境**就都有 tracing。這給了團隊建立後續評估的**地基**:你可以就這樣把 agent 蓋起來、跟它 vibe 一下、丟出去,而**它一路怎麼變化的所有資訊都已經在那裡了**,不是之後要回頭補的東西。

**2. Starter kit evaluator,直接送到 Slack**

有了資料之後,新的卡點是:**團隊不知道怎麼開始寫 eval**——不知道最好的寫法是什麼,也不知道該寫在哪裡。

平台的做法是:利用**這個 agent 是怎麼被建構的脈絡、以及它的文件**,推導出**最適合的 starter kit evaluator**,然後**把這些洞見直接推播給 builder 的 Slack**。

他舉的例子很具體:「我不知道 LLM judge 是什麼,**但我知道 tool contradiction 是什麼意思,而且我可以因此做出修改。**」

**3. CLI:把 eval 從工程手上釋放出來**

他點出一個關鍵差異:**agent 的 eval 和 QA 測試非常不同,它們不是純工程的東西。**

但必須把這個落差補起來,好讓**離客戶最近的團隊——產品與客服團隊——有能力理解這些 eval**。**CLI 體驗真正民主化了這件事**:透過**建構管理 eval 的 skills**,他們看到**產品團隊能夠擁有整個流程**。

**4. 換掉敘事(這一項沒有工具可以解)**

最後一項是他明說「我們沒辦法用工具繞過」的:**改變大家對「eval 是要做什麼用的」的認知。**

他們把團隊的提問從「**你的 eval 有沒有 90% 以上?**」換成:

- **你真的信任你的 eval 嗎?**
- **因為 eval 告訴你的事,你對 roadmap 做了什麼改變?**
- **你更新資料集的速度有多快?你的資料集是不是已經五個月沒動、跟現在的產品早就對不上了?**

**成果:出貨更快,而且在產品生命週期中更早抓到問題。**

#### 案例:語音叫車與那份 pizza(約 03:05–03:06)

Uber 即將推出**乘客語音叫車**。他們的 eval 抓到了這樣一件事:

- **離線 eval 分數是 95% 以上**,看起來很好。
- 但 **production eval 顯示:每個 session 的輪數(turns per session)遠高於平均。**

深入追查後發現:有一位乘客正要叫車去 **SFO**,但**背景有人說了一句「欸我想吃 pizza」**——**agent 把這句話當成了輸入,開始把乘客改導向最近的 pizza 店。**

由此他們意識到:**agent 必須理解真正的意圖(true intent),並且要有 no-op——在不該聽的時候就不要聽。**

他強調這個發現之所以可能,是因為**同時有 eval,也有產品團隊在迴圈裡。**

#### 終局:從 eval-as-default 到 eval-as-engine(約 03:06)

Uber 的演進路徑是:透過上述介入讓 **eval 成為預設值**,而現在他們正往下一階段走——**eval 是一台引擎**:

**traces → 失敗被自動分類 → 自動提出對 agent 與對 evaluator 的修改建議 → 團隊 accept / reject → 改善回饋迴圈。**

他的結尾對比很清楚:

> **一邊是一個 eval metric——一個關於你已經知道的事情的分數;另一邊是一台引擎,持續幫你把 agent 調校到客戶真正在乎的方向。**

「這就是讓你在 Uber 的每一趟行程都感覺神奇的原因。」

### 金句

> "That's the difference between having eval as a checkbox versus an eval actually changing your product direction."(約 03:01)

開場三個舉手題要問出來的那條線。

> "They said that, hey, let me just ship the agent and I'll think about eval. And it was a very rational decision."(約 03:02)

他不責怪團隊——他把它當成平台要解的摩擦力問題。

> "We changed teams' narratives from 'hey, is your eval 90% plus?' to 'do you actually trust your eval?'"(約 03:04)

唯一一個沒有工具可以解的介入。

> "Is your data set five months old and not really up to date with your product?"(約 03:05)

Eval 資料集會腐爛,而腐爛的資料集會給你一個令人安心的假分數。

## English Notes

### TL;DR

- **The problem isn't that teams don't want evals — it's friction.** Every team wanted high-quality production agents, and every team said "let me just ship the agent and I'll think about eval later" — **a perfectly rational call** when you're trying to prove product-market fit. The cost is getting caught in a relentless loop of retrofitting evals and reconstructing why the agent broke. The platform team's job was to remove those friction points one by one.
- **Four interventions**: (1) tracing on from day one in **every environment**; (2) automatically derived **starter-kit evaluators** pushed straight into **Slack**; (3) **CLI experiences and skills** that move eval ownership out of engineering and into product teams; (4) **changing the narrative** — the one thing no tool could fix.
- **The best evidence was a failure.** Voice ride-booking had a 95%+ offline eval, but the production eval showed **turns per session running way above average.** The cause: a rider booking to SFO while **someone in the background said "hey, I want pizza"** — and the agent took it as input and started rerouting them to the nearest pizza place.
- **The destination is turning eval from a score into an engine**: traces → failures **automatically categorized** → proposed updates to the agent and the evaluators → teams accept or reject. **A score tells you about something you already know; an engine continuously moves the agent toward what the customer cares about.**

### Key Points

#### Three shows of hands (~03:01)

Agrawal closed out the Compass Stage. He warmed up the room with three questions:

1. Who took an Uber today? (a few hands)
2. **More importantly: who has actually written an eval for an agent in production?** — "let's see who the real builders are."
3. **And the last one, which you should be proud of: did those evals tell you something that changed the way you shipped your product?**

That third question is the dividing line: **treating eval as a checkbox versus an eval that actually changes your product direction.** Getting every agent team to the second state **is what Uber spent over a year on.**

#### Context: the Uber agent platform (~03:02)

Uber ships agents across its ecosystem — **externally** (booking a ride by voice) and **internally**. Powering all of it at enterprise scale is the **Uber agent platform**, which he manages, with a range of components so agent teams don't have to worry about infrastructure. This talk is about the eval piece.

#### The diagnosis: a rational decision and an inevitable loop (~03:02–03:03)

The pattern he saw across every team: **everyone wanted high-quality production agents, and everyone did the same thing — "let me just ship the agent and I'll think about eval later."**

He's fair about it: **it was a very rational decision.** They were trying to prove product-market fit; they wanted to see whether the thing even worked.

**But it caught them in a relentless loop of retrofitting evals later and trying to figure out why that agent broke.**

The platform team's conclusion was that there were **true friction points** stopping teams from reaching that state earlier — so make it frictionless.

#### Four interventions to make eval the default (~03:03–03:05)

**1. Tracing from day one, in every environment.**

(He noted this had come up across the day's talks.) The moment first development starts, tracing is on in **every single environment**. That gives teams the **foundation** for everything else: build an agent, vibe with it, send it out, and **all the information about how it's been changing over time is already there** rather than something to retrofit.

**2. Starter-kit evaluators, delivered in Slack.**

Once teams had data, the next blocker was that **they didn't know how to start developing an eval** — not the best way to write one, and not where.

So the platform used **the context of how the agent was built plus its documentation** to work out **the best starter-kit evaluators**, and **sent those insights directly to the builders in Slack.**

His illustration: "I don't know what an LLM judge is, **but I do know what it means to have a tool contradiction, and make a change because of that.**"

**3. CLI experiences to get eval out of engineering's hands.**

He drew a sharp distinction: **evals for agents are very different from QA tests — they're not purely engineering.**

That gap had to be bridged so **the teams closest to the customer — product and customer teams — could understand them.** **CLI experiences really democratized that**: by **building skills that manage the eval**, product teams were able to own the entire process.

**4. Changing the narrative — the one they couldn't tool their way out of.**

The last intervention was, in his words, something they couldn't build a tool away for: **changing what people believe an eval is for.**

They shifted teams from asking "**is your eval 90% plus?**" to:

- **Do you actually trust your eval?**
- **What have you changed about your roadmap because your evals told you that?**
- **How quickly have you been able to update your datasets? Is your dataset five months old and not really up to date with your product?**

**The result: shipping faster, and catching issues much earlier in the product lifecycle.**

#### The pizza case (~03:05–03:06)

Uber is launching **rider voice booking** soon, and their evals surfaced this:

- The **offline eval was 95%+** — looks great.
- But the **production eval showed the number of turns per session running way above average.**

Digging in, they found a customer trying to book a ride to **SFO** while **somebody in the background said "hey, I want pizza."** **The agent took that as an input and started rerouting them to the nearest pizza place.**

The lesson: **the agent needed to understand true intent, and to have no-ops for when it shouldn't be listening at all.**

He stressed that this was only possible because **they had both evals and the product teams in the loop.**

#### The endgame: from eval-as-default to eval-as-engine (~03:06)

Uber's arc: these interventions made **eval the default**, and now they're moving to the next stage — **eval as an engine**:

**traces → failures automatically categorized → proposed as updates to the agent and to the evaluators → teams accept or reject → an improvement feedback loop.**

His closing contrast:

> **On one side, an eval metric — a score for something you already know. On the other, an engine that helps you continuously improve agents, tuned toward what the customer cares about.**

"That's what makes each of your trips magical at Uber."

### Quotes

> "That's the difference between having eval as a checkbox versus an eval actually changing your product direction." (~03:01)

The line his three opening questions were designed to draw.

> "They said that, hey, let me just ship the agent and I'll think about eval. And it was a very rational decision." (~03:02)

He doesn't blame the teams — he treats it as a friction problem for the platform to solve.

> "We changed teams' narratives from 'hey, is your eval 90% plus?' to 'do you actually trust your eval?'" (~03:04)

The one intervention no tool could deliver.

> "Is your data set five months old and not really up to date with your product?" (~03:05)

Eval datasets rot, and a rotten dataset hands you a reassuring but meaningless score.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Uber agent platform | 支撐 Uber 內外部 agent 的企業級平台,講者管理其產品 | Enterprise platform powering Uber's internal and external agents; the speaker is its product lead | 內含 tracing、eval 等元件 / includes tracing and eval components |
| Rider voice booking | 即將推出的語音叫車功能,pizza 案例的來源 | Upcoming voice ride-booking feature; source of the pizza anecdote | 演講時尚未上線 / not launched at talk time |
| Eval starter kit(evaluators) | 依 agent 建構脈絡自動推薦、推播到 Slack 的入門 evaluator | Starter evaluators derived from each agent's build context and pushed to Slack | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Aayush Agawal | Aayush Agrawal |
| no ops | no-ops |
| get proposed as sol as updates | get proposed as updates |
| an LLM judges | an LLM judge |
| pizza space | pizza place |
| evolution(指 eval 的演進)| evolution(語意正確,唯與 session 名 "Evaluation" 易混)|

## 待確認 / To Verify

- Uber agent platform 是否有對外公開名稱或技術部落格可引用。/ Whether the Uber agent platform has a public name or engineering blog post to cite.
- 「managed eval 的 skills」與 CLI 體驗的具體形態(是否為 Claude Code 式的 skills,演講中未說明)。/ The concrete form of the "skills that manage the eval" and the CLI experiences — not specified on stage.
- 自動失敗分類(traces → categorized failures → proposed updates)所用的技術棧與是否對外開放。/ The stack behind automatic failure categorization and whether any of it is externally available.
- 語音叫車 95%+ 離線 eval 的評分口徑。/ What the 95%+ offline eval actually measured.
