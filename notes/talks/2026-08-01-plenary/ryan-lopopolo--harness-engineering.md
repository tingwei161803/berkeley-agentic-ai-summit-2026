---
title: "Harness Engineering: How to Build Software When Humans Steer and Agents Execute"
title_zh: "Harness Engineering:當人類掌舵、agent 執行時,軟體該怎麼蓋"
speaker: "Ryan Lopopolo"
affiliation: "Principal Engineer, Agentic Google Cloud Platform; Previously Led Dark Factory at OpenAI"
type: talk
stage: Plenary
date: 2026-08-01
session: "Session 2: Future of Software Engineering"
video: "https://www.youtube.com/watch?v=gKdeLQd_LIQ&t=10071s"
video_range: "02:47:51–02:56:55"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 1st - Morning Session [DownSub.com].srt"
status: draft
tags: [harness-engineering, autonomy, context-engineering, capability-overhang, org-design]
---

# Harness Engineering:當人類掌舵、agent 執行時,軟體該怎麼蓋(Harness Engineering: How to Build Software When Humans Steer and Agents Execute)

**一句話總結**:模型的能力遠超過它今天能對世界造成的影響(capability overhang),差距不在智力而在 context、工具與信任;harness engineering 就是把人力從「寫程式」轉去「把隱藏的判斷標準寫進 agent 的環境」,而這件事的原則跟怎麼帶好一個組織幾乎一樣。
**One-line summary**: Models are far more capable than they are able to side-effect into the world — the gap is context, tools, and trust, not intelligence; harness engineering means redirecting human effort from writing code to encoding the hidden standards into the agent's environment, and it turns out to follow the same principles as running a good organization.

## 中文筆記

### TL;DR

- **Capability overhang**:即使模型與 harness 都固定不動,模型的智力仍遠超過它能實際「作用於世界」的程度。缺的不是聰明,是**它不知道對操作者而言什麼叫「局部與全域的好」**,也沒有足夠 context 去取得完整自主權。
- **他從 2025 年 6 月起就沒寫過任何程式碼,他的團隊也一樣——寫程式是「不被允許的活動」**。人唯一被允許做的事,是讓 agent 去做他們工作中該做的部分。
- **實作變便宜之後,稀缺的是三樣東西:人的時間、模型的 context window、以及雙方的注意力**。所以要「無情地追蹤自己的時間」,找出你反覆在做的事,然後想辦法讓自己不必再做——這個自我改善迴圈就是 agent 自主度的成長曲線。

### 重點整理

#### 開場更正與 capability overhang(約 02:49–02:50)

主持人介紹他為 OpenAI 技術人員、Dark Factory 專案負責人;他上台第一句就更正:**「兩週前起我在 Google。」**(並聲明以下是個人觀點,不代表 Google。)

他先定義 harness engineering:**即使把模型與包裹它的 harness 都固定住,我們今天仍處在 capability overhang——模型的能力與智力,遠遠超過它們有辦法對世界產生作用(side effect into the world)的程度。** 原因不是模型不夠聰明,而是:

- **它們不知道對操作者而言,「局部的好」和「全域的好」長什麼樣。**
- 它們沒有足夠的 context,無法在被部署的組織裡取得完整自主權。

因此人類的角色是**把 agent 牽引進真實世界的管家**:給它工具、context、guard rail、教練式回饋,以及信任,好讓它做完我們要它做的那份工作的全貌。

#### 一年多前的賭注:禁止人類寫程式(約 02:50–02:52)

他站上這個講台的理由是一個一年多前的判斷:**最早那批 reasoning model 就已經有能力做完他的全職工作。** 他用行動下注——**2025 年 6 月起他不再做自己的工作,從此沒寫過任何程式碼,他團隊裡的任何人也沒有;那是不被允許的活動。人被允許做的唯一一件事,就是讓 agent 去做他們工作中需要被做掉的部分。**

2025 年六七月的模型弱得多,這個命題困難得多——**當時他沒辦法讓模型讀 Slack 並代他回應 page**,工具使用、能力與複雜編排的水準都還不到。做法是**往下鑽:把任務 double click、double click、再 double click,直到觸底碰到一件模型做得到的事**;再沿著堆疊往回組裝這些能力時,**你就永久地為「agent 可靠且安全地作用於世界的能力」累積了價值**。而當一群人以這種方式協作在同一個 agent 上,**你會拿到每個人身上最好的那一部分**。

這就是他說「軟體的建造方式已經改變」的實質意涵:**你可以拿任何能力等級的 agent,透過寫程式來解決它執行方式上的問題——因為程式碼現在是免費的**,模型在產出程式碼這件事上能力尖峰極高。

但在實作變得豐沛的世界裡,仍有幾塊稀缺區需要持續投資,才能讓 agent 在長時間尺度上保持連貫。**「即使模型已經這麼先進,你今天說『幫我做一門十億美元的生意』,另一端也不會出現一個連貫的東西。它們甚至還在跟販賣機搏鬥。」** 人的專業就是用來**約束我們允許機器進入的潛在空間與物理空間範圍**,確保長期持續往正確方向前進。他把這個問題一般化成:**要怎麼持續演化一個 artifact——不管它是 codebase、一份 Word 文件,還是一整個 Confluence 規模的組織知識 wiki?**

#### 三種近期稀缺資源(約 02:53–02:55)

1. **人的時間**。這其實是我們至今建構組織方式的地基:你看到 platform team 或 central dashboard,本質上都是**把稀缺的人力集中起來,產出高槓桿、能賦能整個組織的東西**。同樣的約束在 agent 世界依然成立。
   - 他反覆講的一句實務原則:**人(或團隊)在跟 agent 互動時,必須無情地追蹤自己的時間,辨識出自己實際上都在做什麼**——是在跟 agent 一來一回擬計畫?是在 review code?是在退回 slop?**辨識出來,然後想辦法讓自己不必再做那件事。**
   - **這個自然的自我改善迴圈,就是 agent 自主度的成長機制**,允許越來越複雜、越來越自主、越來越平行的工作。
2. **模型的 context window**。這是組出一個模型時的地基性限制。**context window 會變大、auto compaction 會變好,但「單一 trajectory 在長程工作上的連貫性」始終是你必須放在心上的東西。**
3. **注意力(人的與模型的)**。兩邊都會被約束,這是世界的必然事實。**所以「任務與工作要怎麼結構化」必須考慮人與模型能否聚焦、避免注意力被許多互相競爭的關注點打散。**

他給了一個很具體的個人啟發式:**「如果我發現我需要介入超過三次,那我大概要倒楣了。」** 有時他仍會刻意讓自己倒楣一次,目的是**看出 agent 究竟漏掉了什麼**,然後把那件事**反向傳播回他為 agent 布置的環境**,讓下次 reroll 這個任務時,agent 能在需要的當下就拉到正確的 context,不必分散注意力。

#### Harness engineering 就是 onboarding(約 02:56)

他把整場收在一個類比上:**談怎麼蓋出好的平行自主 agent 系統,我們一直繞回怎麼蓋出好組織,因為兩者的原則高度重疊。**

想想 onboarding 是什麼:**你雇用的是一般能力很強的人,但他們不會知道在你這個脈絡下「好」長什麼樣子。**

所以——**把那些構成「在你這裡算是好工作」的非功能性需求(non-functional requirements)整套顯性化出來,就是 harness engineering 的核心;而在背景中、以及透過工具來策展 context 以約束 agent 的工作方式,就是追求一個結構良好的 agent harness 的意義。**

### 金句

> "The models are far more capable and far more intelligent than they are able to side effect into the world today."(約 02:49)

Capability overhang 的定義:瓶頸在「作用於世界的能力」,不在智力。

> "I haven't written any code since then, and neither has anyone on my teams. It's just not a permitted activity."(約 02:50)

他不是在建議,是在報告一個已經跑了一年多的政策。

> "Code is free to produce now."(約 02:52)

這是他所有其他主張的前提。

> "You can say 'make me a billion dollar business' and you will not end up with something coherent at the other end. They are still struggling to operate vending machines."(約 02:52)

對長程連貫性的誠實定位——同時說明為何人的約束仍然必要。

> "They must be incredibly ruthless by tracking their time … identify what they are doing and then figure out ways to make it so they don't do that."(約 02:53)

harness engineering 最可操作的一條規則。

> "If I find I need to intervene more than three times with an agent, I'm probably going to have a bad time."(約 02:55)

一個好用的停損訊號:超過三次介入,問題出在環境不是這一次的 prompt。

> "You're hiring generally capable humans, but they don't necessarily know what good looks like for you in this context."(約 02:56)

agent harness 與員工 onboarding 是同一個問題。

## English Notes

### TL;DR

- **Capability overhang**: even holding the model and its containing harness constant, models are far more capable than they are able to side-effect into the world. What's missing isn't intelligence — it's that **they don't know what local and global good looks like to their operators**, and lack the context for full autonomy inside the organizations they're deployed in.
- **He hasn't written code since June 2025, and neither has anyone on his teams — writing code is "not a permitted activity."** The only thing humans are permitted to do is get the agent to do the parts of their job that need doing.
- **Once implementation is abundant, three things stay scarce: human time, the model's context window, and attention on both sides.** So track your own time ruthlessly, identify what you keep doing, and engineer your way out of doing it — that self-improvement loop *is* how agent autonomy grows.

### Key Points

#### An opening correction, and the capability overhang (~02:49–02:50)

The host introduced him as a member of technical staff at OpenAI leading a project called Dark Factory. His first line onstage was a correction: **"as of two weeks ago I am at Google"** — with a disclaimer that the talk was his own view, not Google's.

He then defined harness engineering: **even keeping the model and its containing harness constant, we are in a capability overhang — the models are far more capable and far more intelligent than they are able to side-effect into the world today.** The gap isn't intelligence:

- **They don't know what local and global good looks like to their operators.**
- They don't have the context to have full autonomy within the organizations where they're deployed.

So the human role is stewardship — **giving agents the tools, context, guardrails, coaching, and trust necessary to fulfill the fullness of the job we want them to do.**

#### The bet: humans aren't allowed to write code (~02:50–02:52)

His reason for being onstage is a call he made more than a year ago: **the earliest reasoning models were already capable of doing his full job.** He put money where his mouth was — **as of June 2025 he stopped doing his job, hasn't written any code since, and neither has anyone on his teams. It's simply not a permitted activity. The only thing humans are permitted to do is get the agent to do the parts of their job that need doing.**

In June/July 2025 the models were much weaker and the proposition much harder — **he couldn't get a model to read Slack and respond to pages on his behalf**; tool use, capability, and complex orchestration weren't there. The method was to drill down: **double-click into the task, and double-click, and double-click, until you bottom out on something the model can do.** Reassembling those capabilities back up the stack **permanently accrues value to the agent's ability to reliably and safely side-effect into the world.** And when teams of people collaborate on a single agent this way, **you get the best parts of everyone.**

That's what he means when he says the way we build software has changed: **you can take an agent at any capability level and solve problems with how it executes by writing code — because code is free to produce now.** Models spike very highly at producing it.

But in a world where implementation is abundant, a few scarce areas still need investment so the agent coheres over long timelines. **"It is not the case today, even with models as advanced as they are, that you can say 'make me a billion dollar business' and end up with something coherent at the other end. They are still struggling to operate vending machines."** Human expertise exists to **constrain the regions of latent and physical space we permit the machine to enter**, keeping the system tracking in the right direction over time. He generalizes the problem as: **what does it mean to continuously evolve an artifact — a codebase, a Word document, or a Confluence-sized wiki of an organization's knowledge?**

#### Three near-term scarce resources (~02:53–02:55)

1. **Human time.** This is foundational to how we've built organizations so far: platform teams and central dashboards exist to **concentrate a scarce pool of human labor into high-leverage things that empower an organization.** The same constraint holds with agents.
   - His most quotable operating rule: **humans interacting with agents must be incredibly ruthless about tracking their time and identifying what they find themselves doing** — going back and forth one-on-one to put a plan together, reviewing code, rejecting slop — **and then figure out ways to stop doing it.**
   - **That self-improvement loop is what increases the autonomy of the agent side of the system**, permitting more complex, more autonomous, and more parallel work over time.
2. **Model context window.** A foundational limitation of what it means to put a model together. **Context windows may grow and auto-compaction may improve, but coherence over long-horizon work within a single trajectory remains something you have to keep in mind.**
3. **Attention — human and model.** Both will be constrained; that's a necessary fact of the world. **So the way we structure tasks and work has to account for humans and models being able to focus rather than scattering attention across many competing concerns.**

A concrete heuristic: **"if I find I need to intervene more than three times with an agent, I'm probably going to have a bad time."** Sometimes he'll deliberately go through the bad time anyway — to learn **where the agent failed to account for what he needed** — and then **back-propagate that into the environment he provisions for the agent**, so the next time he rerolls the task it pulls the right bits of context exactly when needed instead of scattering its attention.

#### Harness engineering is onboarding (~02:56)

He closed on the analogy the whole talk keeps returning to: **discussions of good parallel autonomous agentic systems keep landing back on how to build good organizations, because the principles for empowering humans in a complex organization apply to empowering agents.**

Think about onboarding: **you're hiring generally capable humans, but they don't necessarily know what good looks like for you in this context.**

So — **surfacing the collections of non-functional requirements that go into making good local work for you is the name of the game of harness engineering; and curating context, in the background and via tools, to constrain how the agent works is what chasing a well-constructed agent harness means.**

### Quotes

> "The models are far more capable and far more intelligent than they are able to side effect into the world today." (~02:49)

The definition of capability overhang: the bottleneck is side-effecting into the world, not intelligence.

> "I haven't written any code since then, and neither has anyone on my teams. It's just not a permitted activity." (~02:50)

Not a recommendation — a report on a policy that's been running for over a year.

> "Code is free to produce now." (~02:52)

The premise underneath everything else he argues.

> "You can say 'make me a billion dollar business' and you will not end up with something coherent at the other end. They are still struggling to operate vending machines." (~02:52)

An honest calibration on long-horizon coherence, and why human constraint is still load-bearing.

> "They must be incredibly ruthless by tracking their time … identify what they are doing and then figure out ways to make it so they don't do that." (~02:53)

The most actionable rule in harness engineering.

> "If I find I need to intervene more than three times with an agent, I'm probably going to have a bad time." (~02:55)

A useful stop signal: past three interventions, the problem is the environment, not this prompt.

> "You're hiring generally capable humans, but they don't necessarily know what good looks like for you in this context." (~02:56)

Agent harnesses and employee onboarding are the same problem.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Harness engineering | 他提出的框架:人類透過目標、約束與回饋掌舵,agent 執行 | His framing: humans steer via goals, constraints, and feedback while agents execute | 主持人介紹稱他是 OpenAI 這套思路的作者 / the host credited him as the author of OpenAI's thinking on it |
| Dark Factory | 他在 OpenAI 主持的專案(現已離職至 Google) | The project he led at OpenAI (he has since moved to Google) | 演講中未展開內容 / not elaborated on in the talk |
| ChatGPT code interpreter / record / connectors | 他在 OpenAI 帶過工程的職場產品 | Workplace products he led engineering on at OpenAI | 主持人介紹內容 / from the host's introduction |
| Capability overhang | 模型能力遠超過它能對世界產生作用的程度 | Models being far more capable than they can side-effect into the world | 整場的核心概念 / the talk's central concept |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Ryan Leopollo | Ryan Lopopolo |
| Chad GPT | ChatGPT |
| acrudeed | accrued |
| cohhere | cohere |
| a confluent sized wiki | a Confluence-sized wiki |
| Soy here | (語意不明的口頭插入)/ (unclear verbal aside) |

## 待確認 / To Verify

- **職稱衝突**:主持人介紹他為 OpenAI 技術人員兼 Dark Factory 負責人,他上台自述「兩週前起在 Google」;官網議程作「Principal Engineer, Agentic Google Cloud Platform; Previously Led Dark Factory at OpenAI」。本筆記採官網議程。/ The host introduced him as at OpenAI; he corrected onstage that he had joined Google two weeks earlier. The official agenda title (used here) reflects the Google role.
- 「They are still struggling to operate vending machines」是否在影射某個具體 benchmark 或實驗(如長程 agent 的販賣機經營評測),演講中未指名。/ Whether the vending-machine remark references a specific benchmark or experiment — he didn't name one.
- Dark Factory 專案的公開資料與範圍:演講中僅由主持人帶過,未說明內容。/ Public details and scope of the Dark Factory project — only mentioned in the introduction, never described.
- 他提到的「OpenAI's thinking on harness engineering」是否有公開文件可引用。/ Whether OpenAI's published writing on harness engineering exists as a citable document.
