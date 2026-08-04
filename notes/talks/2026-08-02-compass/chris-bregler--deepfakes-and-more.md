---
title: "Deepfakes and More: How Agents with New Tools Can Mitigate and Provide More Context"
title_zh: "Deepfake 與更多:Agent 如何用新工具緩解問題並提供脈絡"
speaker: "Chris Bregler"
affiliation: "Senior Director / Distinguished Scientist, Google DeepMind; Academy Scientific and Technical Award Winner"
type: keynote
stage: Compass
date: 2026-08-02
session: "Session 1: AI Safety"
video: "https://www.youtube.com/watch?v=l8GS08n-25Q&t=0s"
video_range: "00:00:00–00:15:55"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 2nd - Morning Session [DownSub.com].srt"
status: draft
tags: [deepfakes, media-integrity, provenance, information-quality, google-deepmind]
---

# Deepfake 與更多:Agent 如何用新工具緩解問題並提供脈絡(Deepfakes and More: How Agents with New Tools Can Mitigate and Provide More Context)

**一句話總結**:真正的資訊戰場不在「這張圖是不是 AI 生的」——超過一半的問題案例像素完全沒被動過,騙人的是脈絡;所以 Google 把重心從 deepfake detector 移到「查脈絡的 agent」(Backstory),並主張根因其實是社會科學問題,不是純技術問題。
**One-line summary**: The real information battle isn't "is this pixel fake" — in over half the harmful cases the pixels are untouched and the lie lives in the context; so Google is shifting from deepfake detectors to context-investigating agents (Backstory), and argues the root causes are social-scientific, not purely technical.

## 中文筆記

> 註:直播畫面在講者開場約一分鐘後才切入,本篇筆記自 00:00:00 開始,講題的自我介紹前段未入鏡。

### TL;DR

- **趨勢被誤讀了**:deepfake 自 2018 起確實成長,但 Google 追蹤的問題影像中,**約一半的案例像素完全沒有被修改**——造假的是脈絡(cheapfake / out-of-context),對這類內容跑 deepfake detector 會忠實地回答「這是真的」,完全無用。
- **問題該換一個**:不要問「這是真的還是假的」,要問「**這可信嗎?脈絡是什麼?**」。
- **偵測是軍備競賽,但沒輸**:標準做法(蒐集 Stable Diffusion 等生成圖 + 真圖訓練判別器)必須不斷追新模型;Google 另有一條路線,反推 prompting 與 noise map,對新模型較具不變性。八年前資安理論界預測社群「六個月內會輸掉這場軍備競賽」,八年後還沒發生。
- **兩種 provenance 並行**:inferred provenance(反向圖片搜尋、全網索引,Google 15 年前就做了)與 asserted provenance(C2PA 密碼學帳本、SynthID 隱形浮水印)。後者正在起飛但覆蓋率仍小,所以兩者都需要。
- **Agent 是把這些訊號縫起來的方式**:**Backstory** 幾年前開始開發,去年夏天釋出 v1,近期釋出 v2——它不只跑生成偵測,而是把來源、歷史、上下文全部查一遍,把記者原本要花數小時到數天的調查壓縮到幾秒。
- **根因是社會科學**:Bregler 明確說「根因不只是技術問題」,並指向 UC Berkeley 的社會學傳統(Arlie Hochschild 的 deep story 研究)與 AI 輔助的 reframing / bridging / deliberation(Habermas Machine、Polis),目標是「holistically 改善社會健康」而不只是即時擋下一則違規內容。

### 重點整理

#### Google 的定位:資訊品質 + AI 安全前沿(約 00:00–00:02)

Google 1999 年成立時的使命——「整理全世界的資訊,讓所有人都能取用」——今天依然有效,但現在有兩條線:**原本的資訊品質**(讓網路上最準確、最可信的資訊浮上來),以及**新的 AI 安全前沿**。

一份 Reuters 的研究顯示:**即使你追求準確、追求品質,大眾對線上媒體的信任仍持續下滑**。各國差異很大——芬蘭信任度最高,Google 所在的位置在中間。Bregler 提到他聽說芬蘭從幼稚園就開始做資訊素養教育,而其他地方的人沒那麼有批判性。

Google 的做法是三個支柱,其中最基礎的是**媒體素養(media literacy)**:過去十年產品上那些小小的「三個點」按鈕,以及現在 AI Mode 裡的「了解更多」,核心理念是——**Google 不仲裁真相(we don't arbitrate the truth),而是把最強的工具交給使用者自己判斷**。

#### 數據:deepfake 不是最大的問題(約 00:02–00:03、00:07–00:09)

Bregler 引用 Nick Dufour 與同事發表的追蹤研究。Google 與合作夥伴長期追蹤被使用者認為有問題的視覺與文字資訊:

- deepfake 自 2018 年爆紅,但一直到近期實際佔比都不高;圖上藍線是 deepfake,黃線與紅線是**非 deepfake**,而後者才是量體。
- 例子:伊朗方面用 Photoshop 把假飛彈合成進真飛彈照片裡——這是十年前就有的手法,不需要 GenAI。
- **當同一張圖 scale 到 100% 來看,GenAI 仍然只是一小塊。真正最大的問題是:一半的案例像素完全沒有被修改。**

三個他現場示範的案例:

1. 一段爆炸影片被宣稱發生在伊朗、或發生在加薩——實際上是 **2020 年某港口化肥倉庫的意外爆炸**。跑 deepfake detector 會說「這是真的」,因為它真的是真的。
2. 「俄羅斯戰機飛越基輔」——實際上是十年前莫斯科閱兵的畫面。
3. 淹水街道上的鯊魚:他開玩笑說「只要你看到鯊魚或海豚,大概根本不用 deepfake detector,那八成是假的」;實際上鯊魚是南非海岸一位鯊魚研究者約二十年前拍的真照片,街景則是另一個地方,兩張被疊在一起。

這些正是調查記者要花數小時甚至數天寫深度文章才能拆解的東西,**在規模上做這件事非常難**。

#### 偵測研究:如何跳出軍備競賽(約 00:04–00:07)

標準 deepfake 偵測流程是:蒐集大量生成圖(Stable Diffusion 等)與大量真圖,訓練一個判別器/agent。問題是下週出一個新的 GenAI 模型,明年出一萬個,你就得建立一條不斷更新的 workflow——這是純粹的軍備競賽。

Bregler 的團隊也做「**如何待在軍備競賽之外**」的研究,例如**反向工程 prompting 與 noise map**,目標是對未見過的新模型(zero-day)更具不變性。

> 八年前資安理論界就預測「我們社群會在六個月內輸掉這場軍備競賽」——八年過去了,還在等。工具箱仍然很大。

實務上:**大量內部偵測器與訊號刻意不公開**,以免給對手資訊;但 Google 與 YouTube 的所有介面背後都有這些偵測器。另外幾項:

- **身分保護服務**:創作者或一般使用者若擔心被 deepfake,現在有服務會主動告警「我們認為有人剛剛 deepfake 了你」。
- **選舉政策**:Google 是最早針對選舉廣告中使用 GenAI 訂定政策的平台。
- **偵測 API**:在 I/O 上與 Cloud 團隊合作推出,目前幾乎所有公司都在測試,可申請成為 trusted partner 使用 Google 的內部偵測器。

他順帶點出一個學術界的錯位:**deepfake detection 競賽非常熱門,大量博士生把所有時間投進去,但戰場其實在別處。**

#### 兩種 provenance(約 00:09–00:10)

- **Inferred provenance(推斷式)**:從內容本身回推來源與脈絡。Google 15 年前就發明了反向圖片搜尋,並索引整個網路。使用者收到朋友傳來的「UFO 照片」,圈選後丟給 Google,回應不是「這是假的」,而是「這張圖在別的地方被標記為一朵雲」。
- **Asserted provenance(宣稱式)**:近三年 Google 主導並與其他負責任的業者合作,包括 **C2PA 標準**(Adobe、Microsoft 等業界共同採用)與 **SynthID 隱形浮水印**。Google 的手機拍照時會用密碼學帳本標記「這是一張真實影像」;若之後修掉反光,C2PA 會透明地附註「這是在真實影像上疊加的 GenAI 功能」。

Asserted provenance 正在起飛,但**覆蓋率還小**,所以不依賴 provenance 的偵測器仍然必要。這是一個很大的混合體——**你還是得到處看,才能知道到底發生了什麼事**。這正是 agent 的切入點。

#### Backstory:把所有訊號交給 agent(約 00:10–00:12)

Google 幾年前開始建這個 agent,**去年夏天釋出 v1,近期釋出 v2**,它會把所有來源、所有訊號一起拉進來。

示範案例:社群媒體上有人宣稱「這些加州學生去春假旅遊並汙染了那座湖」。Backstory 不會只跑一個生成偵測器(那不夠),它會去查:學生真的有去那座湖春假嗎?有。他們有汙染湖嗎?沒有。

回到鯊魚那張圖:GenAI detector 會說「不是 GenAI」;Backstory 會告訴你這是一隻真鯊魚,約二十年前由南非海岸的一位鯊魚研究者拍攝,而那條街不在邁阿密颶風現場,兩者是疊上去的。

> GenAI(偵測)在這上面沒用,但它會給你完整的脈絡,你和 agent 一起可以在幾秒內完成調查,而不是花上幾小時或幾天。

現場呼籲:掃 QR code 上網站**註冊成為 trusted tester**;另外 Google 在全球辦資訊素養活動示範怎麼用。評估報告即將發表——他開玩笑說「我當然不會告訴你另外那些模型是誰,當然我們是最好的」。

#### Agent 安全與 Google 的流程(約 00:13)

呼應 Dawn Song 當天早上的 keynote,Google 對 agentic 流程有既定的工作流:**針對 agent 的特定產品政策 → 上線前測試 → 為安全而工程設計 → 持續監控 → 對外合作**。

整體姿態可以這樣分:媒體素養(非常前瞻)、負責任生成(非常前瞻)、AI 安全(非常前瞻)、事後政策執法(反應式)。他形容反應式工作「像在急診室或當消防員,你只是在滅症狀」,所以團隊同時很用力地處理**根因**。

#### 根因是社會科學,不是純技術(約 00:14–00:15)

這是他特別想在 Berkeley 講的一點:

> 根因不只是技術問題,也不只是「偵測這是壞的、那是好的」。根因是社會科學。

他提到近期在 UC Berkeley 與 Raka Ray、Caitlin Rosenthal 等教授合辦的 workshop,並說自己是 Berkeley 社會學家 **Arlie Hochschild** 的粉絲——她從 Berkeley 到路易斯安那州 Lake Charles 做田野,研究當地人對世界、對現實、對「美國夢」的不同理解,以及為什麼他們沒能實現西岸這裡定義的美國夢,寫成了 **deep story** 的研究。

前瞻方向:**社會科學 × AI**。Google 已經發表論文也有系統在跑——如果 AI **reframing、bridging、deliberation** 對你有意義,那就是他說的東西(他點名 **Habermas Machine** 與 **Polis**)。目標是:

> 我們想要 holistically 改善社會的健康,而不只是防止此時此刻的某一則政策違規。

最後他點名在場的團隊成員(Reena Jana,負責 trust & safety 的安全工作流;Amnes Sud,前述反推 prompting/noise map 論文的作者之一),表示團隊在這條安全軌道上投入很深。

### 金句

> "We don't arbitrate the truth."(約 00:02)

Google 的自我定位:不當真相仲裁者,而是把最強的判讀工具交給使用者。

> "Half of the cases are where the pixels are not modified at all. You're not lying with the pixels. You're lying with the context. And your deepfake detectors are completely useless."(約 00:08)

整場演講的核心數據與核心反轉。

> "It's not — you should ask 'is this fake or real?' You should actually ask 'is this trusted? What's the context?'"(約 00:07)

問題換了,工具就得換:從 detector 換成 investigating agent。

> "Security theoreticians eight years ago already predicted we as a community will lose the arms race in six months. I'm still waiting for that. It's eight years later."(約 00:06)

對「偵測必敗論」的溫和反駁。

> "The root causes is not a technical problem alone … the root causes is social science."(約 00:14)

給 Berkeley 聽眾的收尾:資訊生態的真正修復需要社會科學一起上桌。

## English Notes

> Note: the livestream joins roughly a minute into the talk; these notes start at 00:00:00 and the opening self-introduction is off-camera.

### TL;DR

- **The trend line is widely misread.** Deepfakes have grown since 2018, but across the problematic imagery Google tracks, **roughly half the cases involve pixels that were never touched** — the lie is in the context (cheapfakes, out-of-context reuse). Run a deepfake detector on those and it will faithfully answer "real," which is worse than useless.
- **Change the question.** Not "is this fake or real" but "**is this trusted, and what's the context?**"
- **Detection is an arms race, but not a lost one.** The standard recipe (train a discriminator on Stable Diffusion output plus real images) demands a treadmill of retraining as new generators ship. Bregler's group also researches how to *stay out* of the race — e.g., reverse-engineering prompting and noise maps for zero-day invariance. Security theorists predicted eight years ago that the community would lose the race within six months; eight years on, he's still waiting.
- **Two kinds of provenance, both needed.** Inferred provenance (reverse image search over a full web index, which Google shipped 15 years ago) and asserted provenance (C2PA cryptographic ledgers, SynthID invisible watermarks). Asserted provenance is taking off but still covers a small slice, so detection that doesn't depend on provenance remains essential.
- **Agents are how you stitch the signals together.** **Backstory** — started a few years ago, v1 released last summer, v2 just released — pulls every source and signal to answer the context question, compressing an investigation that would take a journalist hours or days into seconds.
- **The root causes are social-scientific.** Bregler pointed at Berkeley's own sociology tradition (Arlie Hochschild's *deep story* fieldwork) and at AI-assisted reframing, bridging, and deliberation (the Habermas Machine, Polis), with the goal of improving societal health holistically rather than blocking one policy violation this hour.

### Key Points

#### Google's position: information quality plus the AI safety frontier (~00:00–00:02)

Google's 1999 mission — organize the world's information and make it accessible to everyone — still holds, but it now runs on two tracks: the original **information quality** problem (surface the most accurate, trusted information on the web) and the new **AI safety frontier**.

A Reuters study he cited makes the uncomfortable point that **trust in online media keeps declining even when you are accurate and even when you strive for quality**. It varies sharply by country — Finland tops the trust ranking; Google's own position sits in the middle. He noted hearing that Finland teaches information literacy starting in kindergarten, while elsewhere audiences are simply less critical.

Google's answer rests on three pillars, the most foundational being **media literacy**: the little three-dot "about this" affordances shipped across products over the last decade, and now the "know more" surfaces inside AI Mode. The governing principle: **"We don't arbitrate the truth."** Give society the most powerful tools and let it form its own view.

#### The data: deepfakes are not the biggest problem (~00:02–00:03, 00:07–00:09)

Drawing on tracking work published by Nick Dufour and colleagues, who monitor visual and textual content that users flag as problematic:

- Deepfakes became culturally huge from 2018, but actual volume stayed modest until recently. On the chart, the blue curve is deepfakes; the yellow and red curves — the **non**-deepfakes — carry the mass.
- Example: Iranian outlets Photoshopping a fake missile in among real ones, a technique that predates GenAI by a decade.
- **Rescaled to 100%, GenAI is still a small fraction. The dominant category is content where the pixels were never modified at all.**

Three live examples:

1. An explosion video claimed to be from Iran, or from Gaza — actually a **2020 accident at a port fertilizer depot**. Run a deepfake detector and it reports "real," because it *is* real.
2. "Russian aircraft over Kyiv" — actually a Moscow military parade ten years earlier.
3. A shark on a flooded street. His aside: "Whenever you see a dolphin or shark, you probably don't even need a deepfake detector — it's most likely fake." In fact the shark is a genuine photo taken by a shark researcher off the South African coast roughly twenty years ago, and the street is somewhere else entirely; the two were composited.

Unpicking each of these is what a well-trained investigative journalist spends hours or days doing. **Doing it at scale is the hard part.**

#### Detection research: escaping the arms race (~00:04–00:07)

The standard workflow — collect a pile of generated images and a pile of real ones, train a discriminator — breaks the moment a new generator ships next week, and ten thousand ship next year. That is a pure treadmill.

His group also researches **how to stay outside the arms race**, for instance by reverse-engineering the prompting and noise maps behind generated images, aiming for invariance to models nobody has seen yet (a "zero-day" property).

> Security theoreticians predicted eight years ago that the community would lose this arms race within six months. Eight years later, the toolbox is still deep.

Operationally, **many internal detectors and signals are deliberately unpublished** so adversaries learn less, but every Google and YouTube surface has them running. Three further items:

- **Identity protection**: creators and everyday users worried about being deepfaked can now get an alert — "we think somebody just deepfaked you."
- **Election policy**: Google was first to set policy for GenAI use in election advertising.
- **A detection API**, announced at I/O with the Cloud team; nearly every company is trialling it, and you can apply for trusted-partner access to Google's internal detectors.

He flagged an academic misallocation along the way: **deepfake-detection competitions absorb enormous PhD-student effort, but the battle is somewhere else.**

#### Two kinds of provenance (~00:09–00:10)

- **Inferred provenance**: work backwards from the content to its origin and context. Google invented reverse image search 15 years ago and indexes the whole web. A friend sends you a "UFO" photo; you circle it, send it to Google, and the answer isn't "fake" or "real" — it's "this was also labeled as a cloud."
- **Asserted provenance**: over the last three years Google has led and partnered on **C2PA** (with Adobe, Microsoft, and the rest of the industry) and **SynthID** invisible watermarking. Google phones stamp captured images through a crypto ledger as real; touch up a glare afterwards and C2PA transparently records that a GenAI feature was applied on top of a real image.

Asserted provenance is lifting off, but **coverage is still the smaller part**, so provenance-independent detectors remain necessary. It is a big mix — **you still have to look everywhere to know what's really going on.** Which is where agents come in.

#### Backstory: handing every signal to an agent (~00:10–00:12)

Google started building this agent a few years ago, **released v1 last summer, and just released v2**. It ingests all sources and all signals.

Demo: a social post claiming Californian students went on spring break and polluted a lake. Backstory doesn't just run a generative detector — that isn't enough. It checks whether the students actually went to that lake (yes) and whether they polluted it (no).

Back to the shark: a GenAI detector says "not GenAI." Backstory says this is a real shark, photographed off the South African coast about twenty years ago by a shark researcher, and the street isn't Miami during a hurricane — the two images were overlaid.

> Generative detection does nothing here, but the agent gives you the whole context, and together with it you can investigate in seconds instead of hours or days.

He invited the room to snapshot the slide and **sign up as a trusted tester**, mentioned worldwide information-literacy events demonstrating the tool, and teased forthcoming evaluations — "I'm not telling you what the other models are; of course we're the best."

#### Agent safety and Google's process (~00:13)

Echoing Dawn Song's keynote that morning, Google runs a defined workflow for agentic flows: **agent-specific product policies → pre-launch testing → engineering for safety → continuous monitoring → external partnerships.**

Mapping the overall posture: media literacy (highly proactive), responsible generation (highly proactive), AI safety (highly proactive), after-the-fact policy enforcement (reactive). He described reactive work as feeling like an emergency room or firefighting — you're treating symptoms — which is why the team also doubles down on **root causes**.

#### Root causes are social science, not just technology (~00:14–00:15)

The point he most wanted to make at Berkeley:

> The root causes are not a technical problem alone, and it isn't just detecting "this is bad, this is good." The root causes are social science.

He cited a recent workshop held at UC Berkeley with Raka Ray, Caitlin Rosenthal, and other faculty, and named himself a fan of Berkeley sociologist **Arlie Hochschild**, who went from Berkeley down to Lake Charles, Louisiana to study a community with a different view of the world, of reality, and of what the American Dream is — and why people there don't achieve the version of it defined on the West Coast. That fieldwork produced her work on **deep stories**.

The forward-looking opportunity is **social science × AI**. Google has published papers and has systems running: if AI **reframing, bridging, and deliberation** mean something to you, that's the space — he named the **Habermas Machine** and **Polis**. The goal:

> We want to improve holistically the health of the society, not just prevent some policy violation right now this hour.

He closed by pointing out team members in the room (Reena Jana, who leads the safety workflow from trust and safety; Amnes Sud, a co-author on the prompting/noise-map work), noting how heavily the team is invested in this safety track.

### Quotes

> "We don't arbitrate the truth." (~00:02)

Google's self-positioning: not the referee of truth, but the supplier of the strongest tools for the public to judge.

> "Half of the cases are where the pixels are not modified at all. You're not lying with the pixels. You're lying with the context. And your deepfake detectors are completely useless." (~00:08)

The talk's central datum and central reversal.

> "You should actually ask: is this trusted? What's the context?" (~00:07)

Change the question and the tooling has to change with it — from detector to investigating agent.

> "Security theoreticians eight years ago already predicted we as a community will lose the arms race in six months. I'm still waiting for that. It's eight years later." (~00:06)

A gentle rebuttal to detection defeatism.

> "The root causes is not a technical problem alone … the root causes is social science." (~00:14)

The closing appeal to a Berkeley audience: fixing the information ecosystem needs social science at the table.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Backstory | Google 的影像脈絡調查 agent,彙整來源、歷史與訊號回答「這可信嗎」 | Google's image-context investigation agent; aggregates sources, history, and signals to answer "is this trusted" | v1 去年夏天釋出、v2 近期釋出;可申請 trusted tester / v1 last summer, v2 just released; trusted-tester signup |
| C2PA | 跨業界的內容來源與真偽宣告標準(密碼學帳本) | Cross-industry content provenance standard backed by a cryptographic ledger | Adobe、Microsoft 等共同採用;Google 手機拍照即帶標記 |
| SynthID | Google 的隱形浮水印技術 | Google's invisible watermarking for generated media | 與 C2PA 互補的 asserted provenance 手段 |
| 反向圖片搜尋 / Reverse image search | inferred provenance 的基礎,Google 15 年前發明 | Foundation of inferred provenance; invented by Google 15 years ago | 不判定真假,而是回報「這張圖還被標記成什麼」 |
| Habermas Machine | AI 輔助審議 / 尋找共識的系統 | AI-assisted deliberation system for finding common ground | 講者點名為「社會科學 × AI」方向的代表 |
| Polis (pol.is) | 開源的大規模意見蒐集與共識發現平台 | Open-source platform for large-scale opinion gathering and consensus finding | 講者與 Habermas Machine 並列提及 |
| Google 偵測 API / detection API | 與 Cloud 團隊在 I/O 推出,開放申請 trusted partner | Launched with the Cloud team at I/O; trusted-partner applications open | 背後是不公開的內部偵測器 |
| 身分保護告警 / identity protection alerts | 主動通知使用者「你可能被 deepfake 了」 | Proactively alerts users that they may have been deepfaked | 對創作者與一般使用者開放 |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Nick Duour / Nick Dufour | Nick Dufour |
| Sinsky (deep fake) | Zelensky(澤倫斯基)|
| Keefe | Kyiv(基輔)|
| Chennai(伊朗那段)| GenAI |
| Genai / geni / geny | GenAI |
| assertive providence / prevalence | asserted provenance |
| in inferred provenence | inferred provenance |
| synth ID | SynthID |
| Arley Hookshield | Arlie Hochschild |
| Rockar Ray | Raka Ray(UC Berkeley,待確認拼法)|
| Caitlyn Rosenthal | Caitlin Rosenthal(UC Berkeley) |
| Habamas machine | Habermas Machine |
| polace | Polis (pol.is) |
| Reena Janna | Reena Jana(待確認)|
| backstory | Backstory(產品名) |
| futurep proof zero day | future-proof / zero-day |

## 待確認 / To Verify

- **2020 港口化肥倉庫爆炸**:講者只說「a fertilizer depot in a port in 2020 blew up by accident」,未點名地點。時空條件與 2020 年貝魯特港硝酸銨爆炸相符,但講者本人沒說,不硬填。/ He never named the port; the description matches the 2020 Beirut ammonium-nitrate explosion but he did not say so.
- **Reuters 研究的正式名稱與年份**:應為 Reuters Institute Digital News Report 系列,但講者未指明版本。/ Likely the Reuters Institute Digital News Report, edition unspecified.
- **Nick Dufour 等人的 prevalence 論文正式標題**:未在演講中念出。/ Exact title of the Dufour et al. prevalence paper was not stated.
- **"Amnes Sud"** — 現場點名的共同作者姓名拼法無法從字幕確定。/ Name of the co-author present in the room could not be resolved from the auto-captions.
- **"Reena Janna"** — 應為 Google 的 Reena Jana,但未查得其現職為 trust & safety safety-workflow lead 的公開佐證。/ Almost certainly Reena Jana at Google, but her stated role could not be independently confirmed.
- **Backstory v2 的釋出日期與功能差異**:講者只說「just released version two」。/ Release date and v1→v2 delta not stated.
- **反推 prompting / noise map 的論文標題**:現場僅口頭描述。/ Title of the prompt/noise-map reverse-engineering paper was not given.
