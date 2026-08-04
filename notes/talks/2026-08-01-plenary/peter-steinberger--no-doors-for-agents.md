---
title: "No Doors for Agents"
title_zh: "沒有為 agent 開的門"
speaker: "Peter Steinberger"
affiliation: "Creator of OpenClaw, OpenAI"
type: talk
stage: Plenary
date: 2026-08-01
session: "Session 2: Future of Software Engineering"
video: "https://www.youtube.com/watch?v=gKdeLQd_LIQ&t=9292s"
video_range: "02:34:52–02:47:35"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 1st - Morning Session [DownSub.com].srt"
status: draft
tags: [agents, openclaw, form-factor, local-first, tooling]
---

# 沒有為 agent 開的門(No Doors for Agents)

**一句話總結**:今天的世界——從會議平台到作業系統到 API——全都是為人類開的門,agent 只能偽裝成人類擠進去;但這不是壞消息,因為「造門」正是現在最好玩、最有價值的工程工作。
**One-line summary**: Everything — meeting platforms, operating systems, APIs — has doors built for humans, so agents have to sneak in disguised as one; that's not a complaint but an invitation, because building the doors is the fun part.

## 中文筆記

### TL;DR

- **文字框是 AI 的「電視上播廣播節目」階段**。每個新媒介都從模仿舊媒介開始;text box 讓十億人用得上 AI,但那不是最終形態。終端機、super app、agent OS、sidebar 都被試過,他認為答案是**隱形的、常駐背景、隨處可喚起的 agent**。
- **真正難的不是「產出」,是「在場」**。做會議紀錄早就被一千個產品解決了;難的是讓 agent 進到房間裡——連作業系統都還沒有為 agent 開的門,他得靠一個要重開機才能裝的音訊驅動,把系統聲音導給 agent。
- **agent 常駐的前提是它是「你的」**。他要知道自己的記憶存在哪裡,所以 agent 跑在自己的硬體上、或跑在自己握有金鑰的雲端盒子裡,並且能按任務挑模型。這是 OpenClaw 交給非營利基金會的理由。

### 重點整理

#### 開場:一個偽裝成人類去開會的 agent(約 02:36)

他用一個本週發生的真事開場:他的 agent 參加了一場會議——**有自己的帳號、自己的瀏覽器,會聽系統音訊,而且是偽裝成人類進去的**,因為「在 2026 年,沒有為 agent 開的門」。他強調今天是以 OpenClaw 作者的身分講(「我戴的是 claw 帽,不是 OpenAI 那頂」),而且坦承他的 agent 現在還是會卡住——「軟體還是很難」。

他從十一月以來的願景沒變過:**一個永遠開著、永遠在想的 agent,它隱藏複雜度,讓生活變簡單。**

#### 形態之爭:我們還在「電視播廣播」的階段(約 02:37–02:40)

- 在場的人是全世界玩 agent 最前面的一群;但他的非技術朋友用 AI 的方式**就像用 Google——在框裡打字,文字回來**。
- 他的類比:**電視剛出現時,人們把廣播節目搬上電視,真的就是有人對著鏡頭念廣播稿**,因為沒人懂這個新媒介。**「文字框就是 AI 的『電視上播廣播』階段。」** 公平地說,它讓十億人用得上 AI。
- 但人類比文字框有表現力得多——我們看、我們說、我們聽、我們感覺。要走到最終形態,只能大量嘗試(他說自己最好的點子都來自玩技術、看遍各種形態)。
- 他逐一點評已經試過的形態:
  - **終端機**:agent 浪潮居然從終端機開始。他愛終端機,但**大多數人一輩子沒開過**。
  - **super app**:那為什麼是 app?不如是作業系統——agent OS?聽起來很棒,但**kernel 是真實存在的東西,而且永遠會有 legacy app**。
  - **sidebar**:業界目前的答案。他直言**「我不想要 Gmail 裡的 Gemini sidebar」**——那個 agent 對我系統的其他部分一無所知,而且不是我能控制的東西。
- 他的傾向:**最好的 agent 也許是隱形的**,永遠在背景、我可以在任何地方喚起它,而且**留給我還能當人的空間**——有時候我就是想打開一份文件自己打字。
- 更遠的目標是 Jarvis:不管我在哪個房間,它知道我家裡的裝置並且能用;它知道我在哪台電腦上,**需要動手時可以接管螢幕**;透過手錶、眼鏡,它能看見我看見的東西。零件已經在了——browser use、computer use、canvas、能同時說與聽的語音模型、以及影像(還沒真正即時,但會到)。

#### 難的是「在場」,不是「產出」(約 02:41–02:42)

回到開場那場會議:為什麼要偽裝?**因為「把筆記整理出來」早就解決了,有一千個產品在做。真正難的是「人在房間裡」——那件事沒有門。**

而且卡關的不只是會議平台。**為了給 agent 一個聲音,他的做法是裝一個把系統音訊導進去的音訊驅動,安裝說明白紙黑字寫著「你必須重新開機」。連作業系統都還沒有為 agent 開的門。**

他描述他真正想要的行為:討論到一個沒人知道答案的問題,**agent 注意到了,於是分身出一份自己去查,本體繼續留在對話裡**——「因為 harness 某種意義上就只是軟體,agent 可以複製自己。它永遠不必在『聽』和『做』之間二選一。」查完之後**它不打斷,它等到合適的時機才加入對話**。「我覺得那會非常自然。那就是一個同事會做的事。」

#### 工具、遞迴,以及「這到底算 agent 還是軟體」(約 02:42–02:45)

常有人問他這場演講是講 agent 還是講軟體——**「這不是同一件事嗎?」**

- 他做了一堆小工具,笑說**「我大部分工具是為我的 agent 做的,也就是為我自己做的」**,因為資料合併之後才變有趣:Discord 告訴他大家愛哪個功能,GitHub 告訴他哪裡壞掉。
- **GitHub 的 API 很好,但那是為人類設計的;在 agent 的規模下它會壞掉。** 所以他自己做了一個工具,現在他的 agent 在本地對 **11 萬則 issue 與 PR** 做全文檢索。Twitter 至少可以匯出封存檔,但那是一座 JSON 山,所以他也做了工具。有些服務最近把 key 搬到 agent 跟不上的地方,結果只是讓他的 agent 多花一點時間拿到資料,順便**更有動力自己做一個**。
- 兩個他很喜歡的社群案例:
  - 有人請 Claude 幫他的 Samsung 環繞音響做一個 CLI。**它 root 了手機、裝了對應的 app、逆向工程、把每一個隱藏控制項都挖出來——而他只是想把音量調小。**
  - 另一個人把 Codex 指向他的攝影棚燈,**AI 告訴他該買哪塊開發板,兩天後他有了一個開源控制器**。當事人原話:「我完全不知道它在幹嘛,但它幹得很好。」
- 結論:**「開源也好、閉源也好,沒有東西擋得住一個帶著 agent 的、下定決心的人。」**
- 而且**這件事會遞迴**:我們用 agent 蓋軟體,用 agent 蓋 agent。第一個 agent 是手寫的,現在 agent 蓋 agent,**軟體就是 agent**。「我們到底在蓋什麼?我不知道。」他知道的是:**小的塞得進一個 session,大的可能需要自己的工廠——而 factory 這種體驗已經開始真的能用了。「編譯器當年也花了一段時間。」**

#### 「這樣不會很毛嗎?」——所有權才是答案(約 02:45–02:47)

大家禮貌地會問:一個永遠在旁邊、永遠在聽的 agent,不會很毛嗎?

**「如果它不是你的,也許會。」** 那東西握著他的記憶,而他「骨子裡非常歐洲」——**他要知道他的記憶在哪裡**。所以他的 agent 跑在自己的硬體上;或者跑在雲端一個他握有金鑰的盒子裡。**而且可以按任務挑模型**:寫軟體要前沿模型;比較私人的東西,也許用一個永遠不離開房間的本地模型更好。有硬體就跑 open weights,沒有就挑一個你信任的供應商。

**「重點是選擇權。這就是為什麼 OpenClaw 活在一個非營利基金會裡。」**

收尾他講了二月在舊金山發生的 **ClawCon**——一場關於他的專案、但**不是他辦的**研討會。他是去當客人的,而整個房間都是 builder,大家興奮得不得了,因為**「AI 突然變成他們可以擁有、可以改的東西,感覺像是他們的」**。「那就是我要的未來。不需要適合所有人,但適合的人會愛死它——我就是其中一個。」

最後一句:**「agent 還是沒有門。而這是好事,因為造門才是好玩的部分。」**

### 金句

> "It went disguised as a human because in 2026, there are no doors for agents."(約 02:36)

整場演講的題眼:今天所有介面都是為人類開的,agent 只能假扮成人。

> "The text box is AI's radio-on-TV phase."(約 02:38)

新媒介先模仿舊媒介——聊天框不是 AI 的最終形態,只是過渡期。

> "I don't want the Gemini sidebar in Gmail. The agent knows nothing about the rest of my system, and it's not something I control."(約 02:39)

對「每個產品塞一個 sidebar」這個業界共識的直接否定。

> "Getting notes out is easy. That's solved. … But actually being in the room is what's hard, what has no door."(約 02:41)

價值不在輸出,在存取權。

> "It never has to choose between listening and working."(約 02:42)

agent 相對人類助理的結構性優勢:它可以複製自己。

> "GitHub has a good API, but it's built for humans. At agent scale, it breaks."(約 02:43)

為人類設計的 API 在 agent 規模下失效,是現在最具體的「沒有門」。

> "Nothing stops a determined human with an agent."(約 02:44)

閉源、無文件、無 API 都不再是護城河。

> "I'm very European at heart. I want to know where my memories are."(約 02:45)

常駐 agent 的隱私問題,他的答案是所有權而不是政策。

> "There's still no doors for agents, and that's good, because building doors is the fun part."(約 02:47)

收尾:把整個缺口重新框成機會。

## English Notes

### TL;DR

- **The text box is AI's radio-on-TV phase.** Every new medium starts by imitating the old one. Terminals, super apps, agent OSes, and sidebars have all been tried; his bet is on an **invisible, always-background agent you can invoke anywhere** — one that leaves you room to still be a human.
- **The hard part isn't output, it's presence.** Meeting notes are a solved problem with a thousand products. Getting the agent *into the room* is what has no door — down to the OS level, where giving his agent a voice meant installing an audio driver whose install instructions say "you must reboot."
- **An always-on agent is only acceptable if it's yours.** He wants to know where his memories live, so his agent runs on his own hardware or in a cloud box he holds the keys to, picking a model per task. That's the reasoning behind putting OpenClaw in a nonprofit foundation.

### Key Points

#### Cold open: an agent that went to a meeting disguised as a human (~02:36)

He opened with something that happened that week. His agent attended a meeting — **its own account, its own browser, listening to system audio, and disguised as a human** — because "in 2026, there are no doors for agents." He noted he was speaking as OpenClaw's creator, not in his OpenAI capacity ("I'm wearing my claw hat"), and was upfront that his agent still sometimes stops: "software is still hard."

His vision hasn't changed since November: **an agent that's always on, always thinking, that hides complexity and makes life easier.**

#### Form factors: we're still putting radio shows on television (~02:37–02:40)

- The room is about as far along on agents as anyone in the world. But his non-technical friends **use AI like Google**: type a question in a box, text comes back.
- The analogy: when television was new, they put radio shows on TV — **people literally read radio scripts on camera**, because nobody understood the new medium yet. **"The text box is AI's radio-on-TV phase."** To be fair, it made AI usable for a billion people.
- Humans are more expressive than a text box — we see, talk, hear, feel. Getting to the final form requires trying a lot of things; he gets his best ideas playing with technology and surveying form factors.
- His verdict on each attempt so far:
  - **The terminal.** The whole agent wave started there, of all places. He loves the terminal, but **most people have never opened one**.
  - **The super app.** Why an app? Why not an operating system — agent OS? Sounds great, but **kernels are real, and there will always be legacy apps**.
  - **The sidebar.** The industry's current answer. His blunt take: **"I don't want the Gemini sidebar in Gmail."** That agent knows nothing about the rest of his system and isn't something he controls.
- Where he lands: **maybe the best agents are invisible** — always in the background, invocable anywhere, and leaving space to still be human. Sometimes he just wants to open a document and type.
- The longer arc is Jarvis: it shouldn't matter what room he's in; it knows the devices in his home and can use them; it knows which computer he's on and **can take over the screen when the job needs hands**; through a watch or glasses it could see what he sees. The pieces exist — browser use, computer use, canvas, voice models that talk and listen simultaneously, and video (not quite real time, but getting there).

#### Presence, not output, is the hard part (~02:41–02:42)

Back to the meeting: why the disguise? **Because getting notes out is solved — a thousand products do it. Actually being in the room is what's hard, and that has no door.**

And it isn't only the meeting platforms. **To give his agent a voice, the setup is an audio driver that pipes system audio through it, and the install instructions literally say you have to reboot. Even the operating system has no doors for agents yet.**

The behavior he actually wants: the group is discussing something, nobody knows the answer, **the agent notices and spins off a copy of itself to go find out while the original stays in the conversation** — "because the harness is just software, in a way, and the agent can clone itself. It never has to choose between listening and working." When the answer comes back, **it doesn't interrupt; it waits for the moment that fits.** "That's what a colleague would do."

#### Tools, recursion, and whether this is even about agents (~02:42–02:45)

People ask whether the talk is about agents or about software. **"How is it not really the same thing?"**

- He's built a lot of small tools, joking that **"I built most of the tools for my agent, which means I built them for myself"** — data gets more interesting when you combine it. Discord tells him which features people love; GitHub tells him where things break.
- **GitHub has a good API, but it's built for humans. At agent scale, it breaks.** So he built a tool, and now his agent has local full-text search over **110,000 issues and PRs**. Twitter at least lets you export your archive, but it's a mountain of JSON, so he built a tool for that too. When services move their keys somewhere agents can't follow, all it achieves is making his agent take a bit longer — and **motivating him to build his own**.
- Two community stories he loves:
  - Someone asked Claude to build a CLI for his Samsung surround system. **It rooted the phone, installed the vendor app, reverse-engineered it, and extracted every hidden control** — the guy just wanted to turn the volume down.
  - Someone else pointed Codex at his studio lights. **It told him which dev board to buy, and two days later he had an open-source controller.** His words: "I have no idea what it's doing, but it's doing a great job."
- The conclusion: **"closed source, open source — nothing stops a determined human with an agent."**
- And **it gets recursive**: we build software with agents, we build agents with agents. The first agent was written by hand; now agents build agents, and **software is agents**. "What are we even building? I don't know." What he does know: **the small ones fit in a session; the big ones might get their own factory — and the factory experiences are starting to actually work. "Compilers took a while too."**

#### "Isn't that creepy?" — the answer is ownership (~02:45–02:47)

Everyone is polite enough to ask: an agent that's always there, always listening — isn't that creepy?

**"Maybe, if it's not yours."** The thing holds his memories, and he's "very European at heart" — **he wants to know where his memories are**. So his agent runs on his hardware, or in a cloud box he holds the keys to. **And he picks a model per task**: the frontier for building software; for something personal, maybe a local model that never leaves the room. Have the hardware, run open weights; don't, pick a provider you trust.

**"It's about choice. That's why OpenClaw lives in a nonprofit foundation."**

He closed on **ClawCon** in San Francisco in February — a conference about his project that **he didn't organize**. He went as a guest, and the room was full of builders who were thrilled because **"AI was suddenly something they could own, they could change. It felt like theirs."** "That's the future I want. It doesn't need to be for everyone. The people it's for are going to love it — I'm one of them."

Final line: **"There's still no doors for agents, and that's good, because building doors is the fun part."**

### Quotes

> "It went disguised as a human because in 2026, there are no doors for agents." (~02:36)

The thesis: every interface is built for humans, so agents have to impersonate one.

> "The text box is AI's radio-on-TV phase." (~02:38)

New media imitate old media first. Chat is a transitional form, not the final one.

> "I don't want the Gemini sidebar in Gmail. The agent knows nothing about the rest of my system, and it's not something I control." (~02:39)

A direct rejection of the industry's current default answer.

> "Getting notes out is easy. That's solved. … But actually being in the room is what's hard, what has no door." (~02:41)

The value isn't in the output; it's in the access.

> "It never has to choose between listening and working." (~02:42)

The structural advantage an agent has over a human assistant: it can fork itself.

> "GitHub has a good API, but it's built for humans. At agent scale, it breaks." (~02:43)

The most concrete "missing door" available today.

> "Nothing stops a determined human with an agent." (~02:44)

Closed source, no docs, and no API have stopped being moats.

> "I'm very European at heart. I want to know where my memories are." (~02:45)

His answer to the privacy problem is ownership, not policy.

> "There's still no doors for agents, and that's good, because building doors is the fun part." (~02:47)

Reframing the entire gap as the opportunity.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| OpenClaw | 他創建的開源個人 AI agent 框架,現由自有非營利基金會託管 | The open-source personal AI agent framework he created, now stewarded by its own nonprofit foundation | 主持人介紹稱數月內累積逾 20 萬 GitHub stars / introduced as passing 200,000+ GitHub stars in a few months |
| PSPDFKit | 他先前在奧地利創辦的 PDF SDK 公司,零外部融資、覆蓋逾十億裝置、九位數出場 | His earlier Austrian PDF SDK company: no outside funding, more than a billion devices, nine-figure exit | 主持人介紹內容 / from the host's introduction |
| ClawCon | 2026 年二月在舊金山舉行的 OpenClaw 社群研討會,由社群自行發起 | Community-run OpenClaw conference held in San Francisco in February 2026 | 他以來賓身分出席,非主辦 / he attended as a guest, not an organizer |
| 自建 GitHub 全文檢索工具 / custom GitHub full-text search tool | 讓 agent 在本地檢索 11 萬則 issue 與 PR,繞開為人類設計的 API 限制 | Gives his agent local full-text search over 110,000 issues and PRs, around the human-shaped API | 未提及工具名稱 / tool name not given |
| 自建 Twitter 封存檔工具 / custom Twitter archive tool | 把可匯出但難用的 JSON 封存檔轉成 agent 可用的資料 | Turns the exportable-but-unwieldy JSON archive into something an agent can use | 未提及工具名稱 / tool name not given |
| 系統音訊驅動 / system-audio driver | 讓 agent 聽見會議聲音的做法;安裝需重開機,他用來說明「OS 也沒有為 agent 開門」 | How he gets meeting audio into the agent; the reboot-required install is his example of the OS having no agent doors | 未提及具體驅動名稱 / specific driver not named |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| PSDFKit | PSPDFKit |
| Open Club / OpenC | OpenClaw |
| OpenI | OpenAI |
| the gin sidebar | the Gemini sidebar |
| pipes sa through it | pipes system audio through it |
| a mountain of Jason | a mountain of JSON |
| deaf board | dev board |
| Clawcon | ClawCon |
| the factory experience are starting | the factory experiences are starting |

## 待確認 / To Verify

- Samsung 環繞音響案例中「It installed Smart Syncs」的正確 app 名稱(疑為 SmartThings,但字幕不清,未硬猜)。/ The app in the Samsung surround-system story ("installed Smart Syncs") — likely SmartThings, but the caption is unclear and this is not confirmed.
- 「one by I really loved recently moved his keys somewhere my agents can follow」整句嚴重失真,推測是某個服務把 API 金鑰搬到 agent 無法取用的位置;服務名稱待看影片確認。/ The garbled line about a service moving its keys "somewhere my agents can('t) follow" — which service is unclear.
- 他說「On Lex this year, I predicted that 80% of the apps will disappear」——應指 Lex Fridman Podcast,集數與確切措辭待查。/ The "80% of apps will disappear" prediction was made "on Lex" (presumably the Lex Fridman Podcast) — episode and exact wording unverified.
- OpenClaw GitHub star 數:主持人現場說「逾 20 萬」,公開資料另有 21 萬+ 的說法,以哪個時點為準待定。/ OpenClaw star count: the host said 200,000+; public sources also cite 214,000+, depending on the date.
- 他自建的 GitHub 檢索工具與 Twitter 封存工具是否有公開名稱與 repo。/ Whether his custom GitHub search and Twitter archive tools have public names or repos.
