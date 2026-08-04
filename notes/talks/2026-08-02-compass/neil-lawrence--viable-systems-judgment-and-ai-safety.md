---
title: "Viable Systems, Judgment, and AI Safety"
title_zh: "可存續的系統、判斷力,與 AI 安全"
speaker: "Neil Lawrence"
affiliation: "Chief Scientist and Co-founder, Trent AI"
type: talk
stage: Compass
date: 2026-08-02
session: "Session 1: AI Safety"
video: "https://www.youtube.com/watch?v=l8GS08n-25Q&t=2719s"
video_range: "00:45:19–00:50:09"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 2nd - Morning Session [DownSub.com].srt"
status: draft
tags: [accountability, governance, cybersecurity, delegation, enterprise-ai]
---

# 可存續的系統、判斷力,與 AI 安全(Viable Systems, Judgment, and AI Safety)

**一句話總結**:電腦很會做帳(accounting),但完全不會負責(accountability)——它關不進監獄、不會難堪、不會丟工作;把「帳」和「責任」分開,你就把人推進一個「看不懂帳卻要簽字」的位置,而這正是 agentic AI 在企業現場真正卡住的地方。
**One-line summary**: Computers do accounting extremely well and accountability not at all — they can't be jailed, embarrassed, or fired. Separate the accounts from the accountability and you strand a human who doesn't understand the accounts but still has to sign them off, which is exactly where agentic AI is stalling in enterprises.

## 中文筆記

### TL;DR

- **現場的 AI safety 其實是問責問題**:不是 Lovedeep 講的那種「可稽核」意義上的 accountability,而是**有人要站出來說「這是我簽的,我負責」**。而且這個壓力不只來自 EU AI Act,更來自**不願拿自己事業去賭一個他們看不懂的 agent 的企業客戶**。
- **Good Regulator Theorem 是雙向的**:1970 年 Conant 與 Ashby 的定理說,**要委派權力,你必須擁有被委派對象的良好模型**;反過來也一樣,**被委派者也必須擁有委派者的良好模型**,才知道什麼時候該把問題浮上來。若你把權力委派給一個大到你根本不理解它會怎麼解題的模型,你就完了。
- **Agentic debt**:把這種「沒有判斷力的權力下放」寫進公司的工作流系統,就是在**囤積下游的麻煩**——你不再理解自己的系統怎麼運作。Trent 的做法是反過來:**不取代工程師,而是支援那些真正要負責的資安工程師**。

### 重點整理

#### Accounting 不等於 Accountability(約 00:46–00:47)

Lawrence 一開場先鋪了 Trent AI 橫跨美歐的定位(他自己在紐澤西出生、住在英國),然後直接切進他在客戶端看到的真相:**AI safety 在地面上長什麼樣子?它是一個問責問題。**

> Accounting is in the numbers. Accountability is in the human authority and the judgment.

而問題在於:

> 電腦把 accounting 做得非常好,但它們**不會 accountability**。它們**不是社會意義上可問責的**:它們**不能被送進監獄、不會難堪、不會丟掉工作**。而我們的社會完全建立在那種形式的問責之上。

由此推出他認為最關鍵的一道裂縫:

> 如果你把**人類的帳(accounts)**和**問責(accountability)**分開,你就把人放進一個**看不懂帳、卻要為問責站台**的處境。**這就是我們必須橋接的鴻溝。**

他也點出這個壓力的來源比法規更廣:「不只來自 EU AI Act,更是來自客戶,來自企業客戶——那些不願意拿自己的生意去賭一個他們不理解的 AI agent 的人。」而且他對未來的判斷相當篤定:「我不知道十年後的世界會是什麼樣子,但我可以告訴你什麼**不會**消失」——問責不會消失。

#### Good Regulator Theorem:委派權力的前提(約 00:47–00:48)

現況等於**在沒有判斷力的情況下下放權力(devolve authority without judgment)**。他搬出 1970 年 Roger Conant 與 Ross Ashby 的 **Good Regulator Theorem** 來說明為什麼這行不通:

> 如果我要委派權力,**我必須擁有那個被委派對象的良好模型**。

他的例子:如果我叫實習生去幫我泡咖啡,我必須有把握這位實習生會用合理的方式做這件事——**他不會跑去駭進 NSA 來取得最佳咖啡配方,他就只是去泡一杯咖啡。**

而且定理是**雙向**的:**被委派者也必須擁有委派者的良好模型**,這樣他才知道**什麼時候該把問題浮上來**——「咖啡機沒咖啡了,我不知道怎麼處理」之類的。

放到 agentic AI:

> 如果你把權力委派給一個大到、龐雜到你根本不理解它會怎麼解決這個問題的模型,**你就完了(you're stuffed)。**

他強調這不是理論擔憂,而是他們實際看到的問題:**你不能用那種方式委派權力。**

#### Agentic debt,以及 Trent 的做法(約 00:48–00:50)

避開這個處境的理由是它會製造 **agentic debt**:

> 如果你把這個東西寫進公司的工作流系統裡,你就是在**囤積下游的麻煩**。你不再理解自己的系統是怎麼運作的。

Trent 的切入點是資安——他們創立時就判斷這會是這個問題的**第一戰線**。而他們進到企業後聽到的話很一致:

> 我們不要你替我們做資安。我們要你**支援我們的資安工程師**做他們的工作,因為他們正在被淹沒。

(他順帶舉了 Apple 關掉 bug bounty 制度作為工程師負荷的例證。)關鍵是:**那些資安工程師,才是在企業裡真正負責的人。**

所以他劃出一條清楚的界線:

- **可以做的**:用 agentic AI 系統去**支援**資安工程師。
- **絕對不能做的**:走進去說「這是一套你沒看過、也不理解的系統,現在請你簽字負責、承擔部署責任」——**那是徹底的災難。**

最後他把開場那個「歐洲 vs 美國」的對比收回來:要橋接「everything everywhere all at once」與「not here, not now」這兩個世界,方法是**跟客戶對話**;而他看到 agentic AI 現在最大的問題之一,就是**這種對話遠遠不夠**。

> 所以當我們部署的時候,要記得:**accountability is king。**

### 金句

> "Accounting is in the numbers. Accountability is in the human authority and the judgment."(約 00:46)

他自己在用的那句座右銘,也是整場的軸。

> "They are not socially accountable. They can't be sent to jail. They can't be embarrassed. They can't lose their job. And our society is entirely based on that form of accountability."(約 00:47)

為什麼「讓 AI 負責」在字面上就不成立。

> "If you're delegating authority to a model that is so large and so big that you don't understand how it's going to solve the problem, you're stuffed."(約 00:48)

Good Regulator Theorem 用在前沿模型上的直接推論。

> "Accountability is king."(約 00:50)

全場最後一句。

## English Notes

### TL;DR

- **On the ground, AI safety is an accountability problem** — not accountability in the auditability sense Lovedeep Gondara used, but in the sense that **a person has to stand up and say "I'm signing that off, that's my responsibility."** The pressure isn't only the EU AI Act; it comes from enterprise customers unwilling to risk their business on agents they don't understand.
- **The Good Regulator Theorem cuts both ways.** Conant and Ashby (1970): to delegate authority you must hold **a good model of the entity you're delegating to** — and the delegate must hold a good model of the delegator, so they know when to surface problems. Delegate to a model so large you don't understand how it will solve the problem and, in his words, you're stuffed.
- **Agentic debt**: wire judgment-free delegation into company workflow systems and you are **storing up downstream trouble** — you no longer understand how your own systems operate. Trent's answer is to invert it: don't replace engineers, **support the security engineers who actually carry the accountability**.

### Key Points

#### Accounting is not accountability (~00:46–00:47)

After setting up Trent AI as a company straddling the US and Europe (he was born in New Jersey and lives in the UK), Lawrence went straight at what he sees in customer engagements: **what does AI safety look like on the ground? It's an accountability problem.**

> Accounting is in the numbers. Accountability is in the human authority and the judgment.

And the trouble is:

> Computers do accounting very, very well, but they don't do accountability well. They are **not socially accountable**. They **can't be sent to jail. They can't be embarrassed. They can't lose their job.** And our society is entirely based on that form of accountability.

Which produces the gap he cares about:

> If you separate the human accounts from the accountability, you put the human in a situation where **they don't understand the accounts and they can't stand up for the accountability**. And that's the gap we've got to bridge.

He was equally clear that this pressure is broader than regulation: it isn't just the EU AI Act, "that's coming from customers, from enterprise customers, people who are not willing to risk their business on the back of AI agents they don't understand." And on the ten-year horizon: "I don't know what the world's going to be like in 10 years' time … but I can tell you what's *not* going away."

#### The Good Regulator Theorem: the precondition for delegating (~00:47–00:48)

The status quo amounts to **devolving authority without judgment**. He reached for Roger Conant and Ross Ashby's 1970 **Good Regulator Theorem** to explain why that fails:

> If I'm going to delegate authority, **I have to have a good model of the entity I'm delegating authority to.**

His illustration: if I tell an intern to make me coffee, I need a good sense that they'll do it sensibly — **that they won't go away and hack the NSA to get the optimal coffee recipe, they'll just make me a coffee.**

And it runs in both directions: **the delegate must have a good model of who's delegating to them**, so they know when to surface a problem — the machine's run out of coffee, I don't know how to deal with that.

Applied to agentic AI:

> If you're delegating authority to a model that is so large and so big that you don't understand how it's going to solve the problem, **you're stuffed.**

Not a theoretical worry, he stressed, but what they genuinely see arising: **you cannot delegate authority that way.**

#### Agentic debt, and what Trent actually builds (~00:48–00:50)

The reason to avoid that situation is that it creates **agentic debt**:

> If you build that into your workflow systems in companies, **you are storing up downstream trouble.** You don't understand how your own systems are operating.

Trent's entry point is cybersecurity — when they set up, their first read was that this would be the **first front** of the problem. What they hear inside companies is consistent:

> We don't want you to do our cybersecurity for us. We want you to **support our security engineers** in doing their job, because they're becoming overwhelmed.

(He offered Apple switching off its bug bounty system as evidence of that overload.) The point being: **those security engineers are the people who are accountable within the business.**

So the line he draws is sharp:

- **What you can do**: use agentic AI systems to *support* security engineers.
- **What you absolutely cannot do**: walk in and say "here's a system you don't understand and have never seen before, and you now have to sign it off and take responsibility for deploying it." **That's absolutely disastrous.**

He closed by returning to the Europe/US contrast he opened with: the way to bridge "everything everywhere all at once" and "not here, not now" is **by talking to customers** — and one of the challenges he sees in agentic AI is that **there isn't enough of that.**

> So when we deploy, we have to remember: **accountability is king.**

### Quotes

> "Accounting is in the numbers. Accountability is in the human authority and the judgment." (~00:46)

The line he says he sticks with, and the axis of the talk.

> "They are not socially accountable. They can't be sent to jail. They can't be embarrassed. They can't lose their job. And our society is entirely based on that form of accountability." (~00:47)

Why "let the AI be accountable" fails at the level of definition.

> "If you're delegating authority to a model that is so large and so big that you don't understand how it's going to solve the problem, you're stuffed." (~00:48)

The Good Regulator Theorem, applied directly to frontier models.

> "Accountability is king." (~00:50)

The last line of the talk.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Good Regulator Theorem | Conant 與 Ashby 1970 年的定理:要調節/委派一個系統,必須擁有該系統的良好模型 | Conant & Ashby (1970): to regulate or delegate to a system you must hold a good model of it | 講者強調它是**雙向**的,委派方與被委派方都需要 |
| Agentic debt | 講者提出的概念:把「無判斷力的權力下放」寫進工作流,等於囤積下游技術債 | His coinage: wiring judgment-free delegation into workflows stores up downstream debt | 對照 technical debt |
| Trent AI | 講者共同創辦的公司,以資安為第一戰線,支援(而非取代)資安工程師 | His company; cybersecurity as the first front, supporting rather than replacing security engineers | 議程職稱為 Chief Scientist and Co-founder |
| EU AI Act | 問責壓力的來源之一,但講者強調客戶壓力更大 | One source of accountability pressure — though he stressed customer pressure matters more | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Trend AI / Tren | Trent AI |
| Love Deep | Lovedeep (Gondara) |
| George uh Roger Conant | Roger C. Conant |
| Ross Ashby | W. Ross Ashby |
| Aentic AI / a Gentic AI | agentic AI |
| EUAI act | EU AI Act |

## 待確認 / To Verify

- **「Apple 關掉 bug bounty 制度」**:講者以此作為資安工程師負荷過重的例證,但這項說法未在本次筆記中查證,建議核實。/ He cited Apple switching off its bug bounty system as evidence of engineer overload; this claim was not independently verified here.
- **開場的歐美對比**:自動字幕把 "everything everywhere and all at once" 與 "something somewhere but not right now" 的歸屬弄混,無法確定哪句對應美國、哪句對應歐洲(依語意最可能是美國 = everything everywhere all at once,歐洲 = not here, not now)。/ The captions garble which side of the Atlantic each phrase belongs to.
- **「viable systems」**:講題出現的 viable systems(可能指 Stafford Beer 的 Viable System Model)在這段逐字稿中未被明確展開。/ The "viable systems" of the title — possibly Stafford Beer's Viable System Model — was not explicitly developed in the delivered talk.
