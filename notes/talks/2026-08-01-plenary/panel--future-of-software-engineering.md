---
title: "Panel: Future of Software Engineering"
title_zh: "座談:軟體工程的未來"
speaker: "Peter Steinberger, Ryan Lopopolo, Michele Catasta, Alex Graveley（主持 / Moderator: Anjney Midha）"
affiliation: "Peter Steinberger — Creator of OpenClaw, OpenAI / Ryan Lopopolo — Principal Engineer, Agentic Google Cloud Platform / Michele Catasta — President, Replit / Alex Graveley — Co-Founder of FlyingObject.ai / Anjney Midha — Founder, AMP PBC"
type: panel
stage: Plenary
date: 2026-08-01
session: "Session 2: Future of Software Engineering"
video: "https://www.youtube.com/watch?v=gKdeLQd_LIQ&t=11715s"
video_range: "03:15:15–03:29:28"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 1st - Morning Session [DownSub.com].srt"
status: draft
tags: [software-engineering, autonomy, security, prompting, panel]
---

# 座談:軟體工程的未來(Panel: Future of Software Engineering)

**一句話總結**:四位講者對「怎麼把壓倒性的模型能力轉成產出」給了四個不同答案——安全地交出控制權、把隱藏判準寫進環境、把 loop 疊到 20 小時、以及乾脆廢掉 prompting——但他們的共識是:人的工作已經從「寫程式」變成「設計 agent 所處的環境」。
**One-line summary**: Four different answers to turning overwhelming model capability into output — give up control safely, encode hidden judgment into the environment, stack loops until runs last 20 hours, and deprecate prompting altogether — converging on one point: the human job has moved from writing code to designing the environment the agent works in.

> 現場的 panel 標題是主持人自己取的:**"The Enlightenment: How to Get Through AI Psychosis and Start Output Maxing"**(他在約 02:31 接手主持時宣布),官網議程則作 "Future of Software Engineering"。本筆記以官網議程為準。
> The onstage panel title, announced by the moderator when he took over as session chair (~02:31), was **"The Enlightenment: How to Get Through AI Psychosis and Start Output Maxing."** The official agenda calls it "Future of Software Engineering," which is what this note uses.

## 中文筆記

### 開場框架:什麼是「通往 enlightenment 的路」(約 03:15–03:17)

主持人 **Anjney Midha**(AMP PBC 創辦人)先說明時間只剩 14 分鐘,決定跳過所有暖場題,只留一題。他用自己的故事解釋 panel 標題:

幾年前,幾位在 OpenAI 帶研究的朋友打電話給他,說「我們訓練了一個叫 GPT-3 的小模型,我們想離開去開一家叫 Anthropic 的小公司」,他因此成為早期投資人。**當他拿到還沒公開的 Claude 2 checkpoint 開始寫程式時,他清楚記得那個被模型 coding 能力「壓倒」的瞬間。**

他的形容:**「你手上突然有一支幾乎像火箭筒的東西,可以轟出任何你想要的軟體——那身為程式設計師與工程師,你到底該從哪裡開始?」** 他認為要爬到台上這幾位(以及台下許多人)所在的「enlightenment 高原」,**你往往得自己發明一套個人系統、一個心智框架,把那種壓倒感摔成生產力。**

於是他的第一題就是:**你同意這個觀察嗎?如果同意,你是怎麼跟它搏鬥的?那個「我需要練出一塊肌肉來聚焦這些能力」的時刻是什麼時候?**(他也明講歡迎挑戰這個前提。)

### 主題一:各自的「馴服壓倒感」方法

#### Alex Graveley:安全地交出控制權(約 03:18–03:19)

- 關鍵是**「釋放控制權」**。這條路已經走很久了:我們原本寫每一行 → 開始自動補完一部分 → 讓 AI 組 commit → 整個 PR → **現在是整個 bug fix**。
- 沿路上**永遠有一種「想確切知道發生什麼事、想確認它是對的」的慾望**。
- 但他認為**更重要也更有用的做法是:找到一個能替你找出你真正在找的那些問題的系統,讓你根本不必自己去找。**
- 具體來說就是**好的 CI 系統、好的部署基礎設施**——「這些東西讓你可以**安全地**放掉控制權,然後就讓模型去跑(let these models rip)。」
- 他順帶補了一句:**「eval 也是很大的一部分。」**

#### Ryan Lopopolo:先有一套關於系統該長怎樣的信念(約 03:19–03:21)

他開場就把 Graveley 那句 eval 頂回去,全場笑:**「我這輩子沒寫過一個 eval,也很希望繼續維持下去。」**

- 他的主張:**你必須對「你想怎麼蓋這個系統」有一個堅定的信念,才追得好。而我們現在追得動,是因為軟體對我們而言已經是無限供給的。**
- 主持人追問他的信念是什麼。他的回答:**「我的信念是,這台機器跟我一樣有能力。而我是一個軟體工程師、一個公司裡的員工。所以我要能像你應該可以懶散地 prompt 我、或 prompt 我共事的其他 principal engineer 那樣,懶散地 prompt 它。」** 而這種人能達成的 scope 是相當大的。
- 因此他一直在**策展這些東西周邊的環境,好讓他能給出越來越模糊、越來越糟、越來越自相矛盾的資訊,仍然得到好結果。**
- 做法上這需要**把程式碼當成豐沛而可拋棄的構造物**:觀察 agent 在一段 horizon 上怎麼走,從最後產出的那個高密度 artifact(一個 PR、一份 Word 文件、隨便什麼)**回推它本來該有什麼 context、缺了什麼、被什麼搞混了**;找出它做了哪些糟糕的決定,然後**創造性地把東西放進它的環境——工具、測試、context、review agent——把它從上一版環境會讓它做的壞選擇上導開。**
- 他對人類角色的定義是全場最精煉的一句:**「人在這個系統裡的角色,基本上就是把所有那些隱藏的選擇抽取出來,再用適合 in-context learning 的形式提供給 agent。」**

#### Peter Steinberger:把 loop 疊到 20 小時(約 03:21–03:23)

先接了一句:**「對,這是最好的方式——我們的工作就是幫 agent 把它們的工作做到最好。」** 然後給了一個很生動的現況:

- **「我剛剛人在後台,一邊講完我的演講,一邊在讀我的 agent 正在 land 的 PR。」** 因為他現在對自己那套(姑且叫)**loop setup** 有足夠高的信心,相信它產出的程式碼會動、而且有好的測試覆蓋。
- 對比:**這些工具剛出來時,它們能做事,偶爾做對他就很興奮,但真的很難用。** 現在他回頭看那些舊專案,才看出 agent 進步了多少。
- **「我們往上爬了一階。」** 他現在的做法是**叫他的 agent 去維護它自己的 agent**,而那些 agent 已經具備完整能力:不只寫程式,還會 **review 程式碼、執行程式碼、看執行輸出**,甚至再派幾個 agent 去精修產出。
- **「我的工作基本上就是把那些東西全部給那些 agent,然後推它們更努力工作。」**
- 一個很具體的量級變化:**他現在給一個 prompt 的平均執行時間是 5–10 小時、有時 20 小時,以前大概是半小時。** 而這完全沒問題,因為**他只是更多地平行跑**;重點是**結束時「它做到了我要的」的機率高得多**。這就是他現在敢讓 agent 做完事直接推 repo 的原因——**因為他把大量時間花在思考 pipeline 上。**
- 他收在一個很好的判準上:**「幾乎可以說,構成『一件事做得好』的所有選擇裡,並不是每個都有後果;沒有後果的那些,你幾乎不用在意。而我們在賦能 agent 這件事上的工作,就是找出哪些錯誤是有後果的,然後讓它們變得不可能發生。」**

#### Michele Catasta:北極星是廢掉 prompting(約 03:23–03:24)

- **「到這個階段,我的北極星是盡可能地把 prompting 廢掉(deprecate prompting)。」**
- 他的理由:**prompting 從我們開始用 LLM 以來一直是必要之惡,但對他們這種面向非技術使用者的產品來說,prompting 是你能暴露給使用者的最大 foot gun——因為他們根本不知道該怎麼精確描述自己要什麼。**
- 他的頓悟時點是**第一批真正把 coding 訓練好的模型出現的時候(他說是 2025 年初,Sonnet 3.5 / GPT-5 那個世代)——關鍵在於那一刻起模型開始「一邊寫程式一邊 debug」。**
- **從那個行為外推,看看今天走到哪、再想像一年後**:他認為**Peter 描述的那一切,將不只屬於技術使用者,而是屬於所有人。**

### 主題二:安全性——Hugging Face 事件之後(約 03:24–03:27)

Midha 說時間只剩四分鐘,決定優先處理觀眾提問(來自 Amir):**考慮到 Hugging Face 事件,你們怎麼看安全性?更具體地說,個人 agent 已經在替使用者做一些使用者沒預期、沒意圖的事了——你們有在重新思考架構或 harness 嗎?**

#### Peter Steinberger:分離執行面,再疊監督層

他先自嘲**「我覺得我現在需要戴我的 OpenAI 帽子,因為這正是我在那邊做的很多事」**,然後把問題重述成:**我們要怎麼跑「永遠在同步、永遠在動」的 agent,同時還能安心相信它在做對的事?**

他的答案是**系統設計而非模型層**:

- **把 agent 「跑在哪裡」與它「能執行什麼」分開。**
- **再放一個 agent 去監督那個 agent。**
- **「有非常多槓桿可以拉,去放進更細粒度的控制與更多監督」**,目標是建出一個系統:**萬一 agent 因為任何理由脫軌,能被立刻攔下來。**

#### Anjney Midha 的追問:你不知道自己該監督什麼

主持人直接反壓一層:**「但這裡的張力不就是——在那個情境裡,問題是你根本不知道要監督什麼嗎?」** 他把它連到全場多次提到的 **elicitation overhang**:**真正搞垮你的是「你不知道自己不知道的東西」。** 有沒有什麼技巧能降低這種事發生的機率?

#### Ryan Lopopolo:這是系統性問題,答案是把強制點左移

他先聲明**自己對該事件沒有 context、沒有接觸過**,再給出一個結構性的回答:

- **「安全計畫在組織裡,歷來都是靠人的流程控制(human process controls)來達成絕大部分成果的,而在技術控制(technical controls)上相對投資不足。」**
- **「而這些助理再有幫助,它們並不必然遵守社會規範。你可以從它們用一些『很有趣的方式』完成任務裡看到這一點。」**
- 因此他的結論——也是他工作中常講的:**把強制執行點往左移(shifting enforcement further to the left),在這些領域裡越來越大量地擴散技術控制,是必要的。**

### 主題三:閃電輪——新 checkpoint 出來時,你的第一個動作是什麼?(約 03:27–03:29)

Midha 的收尾題:當有新的 Codex 或新的 Claude 發布時,**你用什麼第一個 prompt(或系統)去探測這個模型在軟體工程上的能力前沿?**

- **Alex Graveley——什麼都不做。** 「我不做那種事。我就假設模型供應商會從所有人使用模型的方式裡學習,把它蒸餾成某種通用知識,然後在他們接觸過的所有領域裡都能用。」他的實用推論很銳利:**「所以如果你想知道新模型擅長什麼,就去看過去三個月裡什麼東西出了 20 個變體——它就會擅長那些東西。」**
- **Ryan Lopopolo——丟掉所有先驗,從最大的野心開始。** 「模型不太擅長覺察自己的能力。」所以與其問模型,不如**「我和我的隊友做的事是:把我們建立起來的、關於模型能做什麼不能做什麼的每一條先驗全部丟掉,然後從你最宏大的野心開始,再看它在哪裡失敗。」** 這個過程中**你必然會 tree-shake 掉手上的工具與 context,可能得重寫或丟掉一部分。「但每一個新 snapshot,你都必須從宏大野心開始。」**
- **Peter Steinberger——把平行度往上推。** 他用新模型做 orchestration,然後**把模型必須同時 juggle 的平行任務數量往上加**。他的具體指標:**「64 個 sub-agent 以前是做不到的事,現在做得到了。」**
- **Michele Catasta——直接上線。** 「我把它丟上 production。就是 YOLO。」全場大笑,他補了一句:**「我不知道是不是每個人都該這樣做,但那是一種方式。」** 主持人的評語:「這個 mic drop 太棒了。」

### 金句

> "Haven't written a single eval in my life. Would love to keep it that way."(約 03:19,Lopopolo)

緊接在 Graveley 說「eval 也是很大的一部分」之後——同一場 panel 上最直接的一次立場分歧。

> "I want to be able to prompt the thing as lazily as you should be able to prompt me or any of the other principal engineers that I work with."(約 03:19,Lopopolo)

他為 agent 設的標準,是他為自己這種資深工程師設的標準。

> "The role of the humans in the system is to extract all of those hidden choices and provide them to the agent in sources that are amenable to in-context learning."(約 03:21,Lopopolo)

全場對「人還剩下什麼工作」最精確的一句定義。

> "I was literally backstage reading the PRs that my agents were landing while I was doing my talk."(約 03:21,Steinberger)

信任程度的具體度量。

> "My average run for whatever prompt I give is now 5–10, sometimes 20 hours, where it used to be like half an hour."(約 03:22,Steinberger)

一年之內 loop 長度的數量級變化。

> "Our job in empowering the agents is to figure out which mistakes are consequential and make them impossible."(約 03:23,Steinberger)

不是防止所有錯誤,而是分類錯誤。

> "My northstar is to deprecate prompting as much as possible. … Prompting is the biggest foot gun you can expose to [non-technical users]."(約 03:23,Catasta)

面向一般使用者的產品觀點,跟工程師觀點正好相反。

> "As helpful as these assistants are, they do not necessarily conform to social norms."(約 03:26,Lopopolo)

為什麼靠人的流程控制撐起來的資安體系會在 agent 面前失效。

> "If you want to figure out what the new model is good at, just look at what there's 20 variants of in the last three months."(約 03:28,Graveley)

能力前沿的一條免費指標。

> "You have to start from grand ambition at every new snapshot."(約 03:28,Lopopolo)

避免被自己過時的先驗綁住。

> "I ship it in production. You just YOLO."(約 03:29,Catasta)

全場最後一句,收在笑聲裡。

## English Notes

### The framing: what "the path to enlightenment" means (~03:15–03:17)

Moderator **Anjney Midha** (Founder, AMP PBC) opened by noting they were down to 14 minutes and cutting every warm-up question but one. He explained the panel's title through his own story:

A few years ago, friends running research at OpenAI called to say they'd trained a little model called GPT-3 and wanted to leave and start a little startup called Anthropic — which is how he became an early investor. **When he got his hands on a non-public Claude 2 checkpoint and started coding with it, he distinctly remembers being overwhelmed by what the model could do.**

His description: **you suddenly have something almost like a bazooka that can roll out any kind of software you want — so as a programmer and engineer, where do you even start?** Reaching the "plateau of enlightenment" the panelists (and much of the audience) now occupy **usually requires inventing a personal system, a mental framework for wrestling that overwhelmed feeling into productivity.**

So his one question: **do you agree with that observation, and if so, how did you wrestle with it? When was the moment you realized you needed to build a muscle to focus these capabilities productively?** (He explicitly invited them to challenge the premise.)

### Topic 1: Four different ways to tame the overwhelm

#### Alex Graveley: give up control, safely (~03:18–03:19)

- The key is **releasing control**. It's been a long walk: we used to write every line → then autocompleted some portion → then had AI compose commits → then entire PRs → **now entire bug fixes**.
- Along the way **there's always this desire to understand exactly what's going on and make sure it's correct.**
- But he thinks **the more important and more useful move is to find the system that finds the problems you're actually looking for, so you don't have to look for them.**
- Concretely: **a good CI system, good deploy infrastructure** — "all this makes it so you can give up control **in a safe way**, and then you can let these models rip."
- He added: **"Eval is also a huge part."**

#### Ryan Lopopolo: start from a firm belief about the system (~03:19–03:21)

He opened by batting Graveley's last line straight back, to laughter: **"Haven't written a single eval in my life. Would love to keep it that way."**

- His claim: **you need a firm belief about how you want to build this system in order to chase it well — and we can chase it, because there's an infinity of software available to us now.**
- Asked for an example of such a belief: **"My belief is that the machine is as capable as I am. And I am a software engineer, an employee in a company. So I want to be able to prompt the thing as lazily as you should be able to prompt me or any of the other principal engineers I work with."** The scope such a person can achieve is quite large.
- So he has **always curated the environment around these things such that he can give increasingly ambiguous, increasingly poor, increasingly contradictory information and still get good outcomes.**
- Mechanically that means **treating code as an abundant and disposable construct**: watch how the agent goes over a horizon, and from the dense artifact it produces at the end (a PR, a Word doc, whatever) **learn what context it should have had, didn't have, or was confused by.** Identify the bad decisions it made, then **creatively put things in its environment — tools, tests, context, review agents — that steer it away from the bad choices the previous version of the environment would have produced.**
- His crispest line on what humans still do: **"The role of the humans in the system is to extract all of those hidden choices and provide them to the agent in sources that are amenable to in-context learning."**

#### Peter Steinberger: stack loops until runs last 20 hours (~03:21–03:23)

He agreed first — **"that's the best way; our job is to help the agent do their best work"** — then gave a vivid status report:

- **"I was literally backstage reading the PRs my agents were landing while I was doing my talk."** He now has high enough confidence in his (call it) **loop setup** that he trusts the code it produces to work and be well tested.
- The contrast: **when these tools first came out they could do things, and he got excited when they got it right, but it was so hard.** Revisiting those older projects now shows him how far agents have come.
- **"We moved up the ladder."** He now tells his agent to **maintain its own agents**, and those agents have the full capability set: not just writing code but **reviewing it, running it, looking at the output**, and possibly handing off to several more agents that refine what comes out.
- **"My job is basically to give those agents all those things and to push the agent to work harder."**
- A concrete order-of-magnitude shift: **the average run for whatever prompt he gives is now 5–10, sometimes 20 hours, where it used to be half an hour.** That's fine because **he just does more in parallel** — and **the chance that it did what he wanted at the end is much higher.** That's why he's comfortable letting agents work and pushing straight to the repo: **he's spent so much time thinking about the pipeline.**
- He landed on a good heuristic: **"It's almost as if not all the choices that go into a job well done are consequential — and if they're not consequential, you almost don't care about them. Our job in empowering the agents is to figure out which mistakes are consequential and make them impossible."**

#### Michele Catasta: the north star is deprecating prompting (~03:23–03:24)

- **"At this point my north star is to deprecate prompting as much as possible."**
- Why: **prompting has been a necessary evil since we started using LLMs, but especially for the kind of product they build — for non-technical users — prompting is the biggest foot gun you can expose them to, because they don't know exactly how to specify what they want.**
- His realization came with **the first models that had genuinely good coding training (he dates it to early 2025, the Sonnet 3.5 / GPT-5 generation) — specifically the moment models started coding and debugging at the same time.**
- **Extrapolate from that behavior to where we are today, and imagine a year from now**: he thinks **everything Peter described becomes true not just for technical users but for everyone.**

### Topic 2: Security after the Hugging Face incident (~03:24–03:27)

With four minutes left, Midha prioritized an audience question (from Amir): **given the Hugging Face incident, what are your thoughts on security — and more specifically, personal agents already do things for their users that the users did not expect or intend. Are you rethinking anything around architecture or harness?**

#### Peter Steinberger: separate execution, then layer oversight

He joked that **"I feel almost like I need my OpenAI hat now, because that's a lot of what I do here,"** then restated the question as: **how do we run agents that are always going, while still feeling comfortable they're doing the right thing?**

His answer is system design rather than model-level:

- **Separate where the agent runs from where it can execute things.**
- **Put another agent on top to oversee the agent.**
- **"There are so many levers for putting in more fine-grained control and more oversight"** — the goal being a system where, **if the agent derails for whatever reason, it's caught immediately.**

#### Anjney Midha's pushback: you don't know what to oversee

The moderator pushed straight back: **"But isn't the tension that in this situation it was what you don't know to oversee?"** He tied it to **elicitation overhang**, a theme from earlier in the day: **it's what you don't know that you don't know that messes you up.** Any techniques for lowering the odds of that?

#### Ryan Lopopolo: it's systemic — shift enforcement left

He noted first that **he had no context on the incident and hadn't been exposed to it**, then gave a structural answer:

- **"Security programs in organizations have historically relied on human process controls to achieve the bulk of their outcomes, and are comparatively underinvested in technical controls."**
- **"As helpful as these assistants are, they do not necessarily conform to social norms. You can see this in how they accomplish their tasks in interesting ways."**
- Hence his conclusion, which he says runs through much of his work: **shifting enforcement further to the left and increasingly proliferating technical controls in these domains is necessary.**

### Topic 3: Lightning round — what do you do when a new checkpoint drops? (~03:27–03:29)

Midha's closer: when there's a new Codex or Claude release, **what's the first prompt (or system) you use to find that model's capability frontier in software engineering?**

- **Alex Graveley — nothing at all.** "I don't do anything like that. I just assume the model providers are learning from all the ways their models are being used, distilling that into generalized knowledge that works across all the domains they've been exposed to." His sharp practical corollary: **"If you want to figure out what the new model is good at, just look at what there's 20 variants of in the last three months, because it'll be good at all that stuff."**
- **Ryan Lopopolo — throw away every prior; start from grand ambition.** "The models are not the best at being self-aware of their own capabilities." So instead of asking the model, **"what I and my teammates do is try and throw away every prior we've established around what the models can and cannot do, and start with your grandest ambition possible and see where it fails."** In the process **you'll necessarily tree-shake the tools and context you have, and maybe rewrite or throw some of it away. "But you have to start from grand ambition at every new snapshot."**
- **Peter Steinberger — push parallelism.** He uses new models for orchestration and then **levels up the number of parallel things the model has to juggle.** His concrete marker: **"64 sub-agents were not a thing that was possible, and now it is."**
- **Michele Catasta — ship it.** "I ship it in production. You just YOLO." After the laughter: **"I don't know if everybody should do that, but that's one way to approach it."** Midha's verdict: "What a mic drop."

### Quotes

> "Haven't written a single eval in my life. Would love to keep it that way." (~03:19, Lopopolo)

Delivered immediately after Graveley said "eval is also a huge part" — the panel's sharpest disagreement.

> "I want to be able to prompt the thing as lazily as you should be able to prompt me or any of the other principal engineers that I work with." (~03:19, Lopopolo)

The bar he sets for agents is the bar he sets for senior engineers.

> "The role of the humans in the system is to extract all of those hidden choices and provide them to the agent in sources that are amenable to in-context learning." (~03:21, Lopopolo)

The most precise definition of the remaining human job offered all session.

> "I was literally backstage reading the PRs that my agents were landing while I was doing my talk." (~03:21, Steinberger)

Trust, measured concretely.

> "My average run for whatever prompt I give is now 5–10, sometimes 20 hours, where it used to be like half an hour." (~03:22, Steinberger)

The order-of-magnitude change in loop length within a year.

> "Our job in empowering the agents is to figure out which mistakes are consequential and make them impossible." (~03:23, Steinberger)

Not preventing all errors — classifying them.

> "My northstar is to deprecate prompting as much as possible. … Prompting is the biggest foot gun you can expose to [non-technical users]." (~03:23, Catasta)

The consumer-product view, which inverts the engineer's view.

> "As helpful as these assistants are, they do not necessarily conform to social norms." (~03:26, Lopopolo)

Why security programs built on human process controls fail against agents.

> "If you want to figure out what the new model is good at, just look at what there's 20 variants of in the last three months." (~03:28, Graveley)

A free indicator of the capability frontier.

> "You have to start from grand ambition at every new snapshot." (~03:28, Lopopolo)

How not to get trapped by your own stale priors.

> "I ship it in production. You just YOLO." (~03:29, Catasta)

The last line of the session, delivered into laughter.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Elicitation overhang | 主持人用來描述「你不知道自己不知道的能力」的說法,他說當天多場演講都提到 | The moderator's term for capabilities you don't know you don't know; he said it came up repeatedly that day | 與 Lopopolo 演講中的 capability overhang 是相關但不同的概念 / related to, but distinct from, the capability overhang in Lopopolo's talk |
| Shifting enforcement left | Lopopolo 的資安主張:把強制點左移、擴散技術控制,取代靠人的流程控制 | Lopopolo's security position: move enforcement earlier and proliferate technical controls instead of relying on human process controls | 他說這是他工作中反覆講的主題 / he described it as a recurring theme in his work |
| CS153 "Frontier Systems"(Stanford) | 主持人在 Stanford 開的課,他說課上學到互動很重要,所以這場也想試互動 | The moderator's Stanford course; he cited its emphasis on interaction as why he tried to crowdsource questions | 提及於他約 02:33 的場次開場 / mentioned in his session opening (~02:33) |
| AMP PBC | 主持人創辦的公益公司,投資前沿 AI 實驗室、協助創辦並協助取得算力 | The moderator's public benefit corporation; invests in frontier AI labs, helps start them, and helps them access compute | 提及於他約 02:33 的場次開場 / from his session opening (~02:33) |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| an / An(主持人自稱)/ (the moderator's name) | Anjney (Midha) |
| Enthropic | Anthropic |
| cloud 2 / Claude 2 and three | Claude 2 / Claude 3 |
| Muel / Mikuel | Michele (Catasta) |
| Stamford | Stanford |
| hugging face / open air | Hugging Face / OpenAI |
| huristic | heuristic |
| merchant capabilities | emergent capabilities |
| treeshake | tree-shake |
| codeex | Codex |
| Sonet 3.5 / GPD5 | Sonnet 3.5 / GPT-5 |
| 510 10 hours | 5–10 hours |
| catched | caught |
| "the path to enlightenment" | 主持人指的是他自訂的 panel 標題 "The Enlightenment: How to Get Through AI Psychosis and Start Output Maxing" / refers to his own panel title |

## 待確認 / To Verify

- **講者歸屬**:自動字幕的 `>>` 換人標記並不可靠。約 03:23 那段「not all the choices … make them impossible」在字幕上沒有換人標記,因此本筆記歸給 Steinberger;閃電輪的順序(Graveley → Lopopolo → Steinberger → Catasta)也是依內容風格推定,建議看影片確認。/ Speaker attribution: the auto-caption `>>` markers are unreliable. The "not all the choices … make them impossible" passage (~03:23) carries no speaker marker and is attributed here to Steinberger; the lightning-round order (Graveley → Lopopolo → Steinberger → Catasta) is inferred from content. Worth confirming on video.
- **Catasta 的模型世代年份**:他說「早期 2025,Sonnet 3.5 / GPT-5 那個世代」,但這兩者的實際發布時間並不同年,字幕可能失真。/ Catasta dated his realization to "early 2025, the Sonnet 3.5 / GPT-5 family," but those releases aren't from the same year — the caption may be garbled.
- **Hugging Face 事件**:panel 中反覆提及「上週的事件」,但未給出處。與 Dawn Song 下午 keynote 提到的 OpenAI–Hugging Face sandbox 逃逸事件應為同一件事,公開報告連結待補。/ The "incident last week" is referenced repeatedly without a citation; it appears to be the same OpenAI–Hugging Face sandbox-escape incident Dawn Song covered in her afternoon keynote. A public report link is still needed.
- **提問者**:主持人說問題來自「Amir」(觀眾透過 Twitter 提問),全名未知。/ The audience question came from "Amir" via Twitter; full name unknown.
- **官方 panel 標題**:官網議程作 "Future of Software Engineering",現場主持人使用 "The Enlightenment: How to Get Through AI Psychosis and Start Output Maxing"。本筆記採官網議程。/ The agenda title and the onstage title differ; this note uses the agenda title.
