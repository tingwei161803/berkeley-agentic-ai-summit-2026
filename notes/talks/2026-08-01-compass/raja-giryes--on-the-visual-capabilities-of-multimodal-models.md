---
title: "On the Visual Capabilities of Multimodal Models"
title_zh: "談多模態模型的視覺能力"
speaker: "Raja Giryes"
affiliation: "Professor, Tel Aviv University"
type: talk
stage: Compass
date: 2026-08-01
session: "Session 3: Foundational Capabilities"
video: "https://www.youtube.com/watch?v=AO0RXP-fVZQ&t=9941s"
video_range: "02:45:41–02:57:05"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [multimodal, spatial-cognition, vlm, mental-imagery, benchmarks]
---

# 談多模態模型的視覺能力(On the Visual Capabilities of Multimodal Models)

**一句話總結**:多模態模型的推理幾乎都發生在 LLM 那一側、視覺端只是外掛,這解釋了它們在空間認知上的長期落後;但兩年間從「接近隨機猜」到「接近滿分」的躍進顯示——**問對問題本身就會驅動進展**,而進展的機制正是模型開始在內部權重裡「想像」視覺中間狀態。
**One-line summary**: In today's multimodal models the reasoning happens almost entirely in the LLM while the vision side is a head bolted on, which explains their long lag on spatial cognition; but the two-year jump from near-chance to near-perfect on several tasks shows that **asking the right question is itself what drives progress** — and the mechanism turns out to be models internally *imagining* visual intermediate states.

## 中文筆記

### TL;DR

- **視角轉換**:當天所有人都在談 coding agent 怎麼延伸;他要談的是**加入新能力**,也就是多模態。「當你現在聽我說話,你不是只看到文字,你看到我、看到一切——我們活在一個多模態的世界。」
- **現代多模態模型的結構性偏斜**:很強的 LLM + 一個「不知從哪找來就接上去」的視覺頭,一起做後訓練。分析下來,**多模態理解的推理幾乎都發生在 LLM 端而非視覺端**;in-context learning 一旦塞太多圖片,模型反而會混亂——因為訓練時主要仰賴語言那一側。
- **空間認知的兩年躍進**:兩年前,frontier model 在 mental rotation、perspective taking、maze completion、shortcut discovery 這些空間認知測驗上幾乎是隨機水準;今年一月的研究說它們大約到了**三歲小孩**的程度;2026 年二月的研究說它們能解人類**約 10 秒**能解完的空間認知任務。而在 perspective taking 上,Opus 4.6 與 Gemini 3.1 已經接近 100%。
- **為什麼會進步**:他與 Apple 同事的近期工作發現,**即使是不能生成影像的模型,也在內部權重中重建視覺中間狀態**——用探針(probe)接上權重就能把它讀出來。而**主動監督模型去「想像」,效能還會再提升**。
- **兩個帶走的訊息**:(1) 提出對的問題對推進科學極其重要;(2) 多模態模型不能只顧文字,**也要練生成視覺的那一半**。

### 重點整理

#### 多模態的老問題:compositionality 與「詞袋」(約 02:46–02:48)

他先致謝並說明角度不同:大家都在談 coding agent,他要談的是**加入新能力**。而他觀察到領域裡一個有趣的規律——**一旦有人開始問對的問題,一兩年內就會開始看到解法**。

早期的例子是 **compositional reasoning**。舊的多模態模型在做影像描述時,如果一張圖是「三隻斑馬和兩隻長頸鹿」,數字與名詞會全部混在一起——模型把所有東西當成一個 **bag of words**,於是組合性就出問題。他的團隊做過多項改進工作:用**樹狀結構**把詞分解、產生更**密集且對齊**的描述,把模型教得更有結構。此後情況確實改善了。

#### 結構性偏斜:推理都在 LLM 那一側(約 02:48–02:50)

接著他們發現這些模型還有別的問題,並用兩項工作分析「模型在理解流程中到底發生了什麼」:

- 一項與同事合作、去年發表於 **ACL** 的工作(關於 entity knowledge 的效能落差):他們想知道多模態模型的推理發生在哪裡。發現是——**所有現代多模態模型的結構,都是一個很強的 LLM,加上一個從某處找來、接上去的視覺頭**;我們投入大量資源訓練 LLM,視覺語言模型的部分則相對隨意,再一起做後訓練。分析下來,**多模態理解的分析工作大部分發生在 LLM 那一側,而不是視覺那一側。**
- 另一項是 **in-context learning** 的分析:LLM 的 ICL 效果很好,但 VLM / 多模態模型有個奇怪現象——**如果 in-context 的示例太長、圖片太多,模型反而開始混亂**。原因同樣是:訓練多模態模型時我們主要依賴語言那一部分。

他的問題:**也許我們需要做一次轉向。**

#### 空間認知:從隨機猜到接近滿分(約 02:50–02:54)

演講聚焦在多模態模型的一項特定能力:**spatial cognition(空間認知)**。

他引用同事兩年前發表的研究「**Does Spatial Cognition Emerge in Frontier Models?**」,該研究對多模態模型施以一系列空間認知測驗:

- **Mental rotation**:給一個形狀,問哪個是同一形狀的旋轉版本。
- **Perspective taking**:例如問「蝙蝠與狗之間的角度是多少」,看模型能否從特定視角作答。
- **Maze completion**:要模型解迷宮。
- **Shortcut discovery**:給模型看一段走過某地的路徑,但不是最短路徑,再要求它走最短路徑。

**兩年前的結論是:所有模型都很糟。** 連 GPT 等 frontier model 都幾乎接近隨機水準,只是略好一點。

但一旦問題被提出來,進展就開始出現:

- **今年一月**,一項名為(字幕作)"baby vision" 的研究做了類似的探索,發現 frontier model 大約到了**三歲小孩**的水準。他調侃:「一年半就長到三歲很不錯,但通常我們希望長慢一點。」
- 另一項工作把「人類解一題要花多久」拿來跟模型比,發現到 **2026 年二月**,frontier model 能解的是**人類約 10 秒能解完**的空間認知任務。以 mental rotation 為例,人類解它是要花一點時間的,所以模型只能解 10 秒級的題目「不算太好,但比以前好」。
- 逐項來看:**perspective taking** 兩年前最好的模型接近隨機,現在 **Opus 4.6 與 Gemini 3.1 幾乎接近 100%**,兩年內的進步非常驚人。**Maze completion** 還沒那麼好,但**就在三個月前**,從接近隨機一躍而上(他舉 GPT-5.4 為例),**shortcut discovery** 也發生了同樣的躍升。

#### 為什麼會進步:模型在內部「想像」(約 02:54–02:56)

那麼問題來了:為什麼會發生這件事?

他與 **Apple** 的同事做了一項近期工作,問的問題是「**多模態模型會夢見電子羊嗎?**(Do multimodal models imagine electric sheep?)」——答案是**會**。

做法:研究多種空間認知任務,在 **open-loop** 設定下——只給模型第一格畫面,然後要模型告訴我們該走哪一步來解這個遊戲。重點是,他們看的是**不能生成影像的模型**(能接收影像但不能產生影像)。**用一個 transformer 接上模型權重做探針(probe)**,結果發現:**模型在內部想像著怎麼解這個問題**。

- 例如問兩個形狀是否為同一個形狀(旋轉後是否重合),可以看到模型在內部權重中**重建了視覺內容**——正是我們人類在心裡旋轉兩個形狀時會做的事。
- 組裝字元(assemble characters)的任務也一樣:模型在內部權重中組裝字元。

**這也許正是這兩年大幅進步的原因:模型開始想像了。** 而他們接著做的是:**主動給模型「想像」的能力並加以監督**,結果**效能又進一步提升**。

#### 兩個結論(約 02:56)

他因時間關係跳過其餘結果,留下兩點:

1. **提出對的問題,對推進科學非常重要。**
2. 對多模態模型而言,**不要只聚焦在文字,也要聚焦在生成視覺的部分**——這對模型的進步幫助很大。

### 金句

> "When you hear me now, you don't just see a text, you see me, you see everything. So we live in a multimodal world."(約 02:46)

一句話說明為什麼在滿場的 coding agent 討論裡,還是需要有人談視覺。

> "You have very strong LLM and a nice visual head attached to it … we found somewhere, we attached to it."(約 02:48–02:49)

對當前多模態架構最不客氣也最傳神的描述——視覺端是外掛,不是共同設計。

> "Nice to grow to become three years old in one and a half year — but usually we want to grow slower."(約 02:52)

對空間認知進步速度的一句冷幽默。

> "Once you start asking the question, you start to see improvement throughout time."(約 02:51)

貫穿全場的主軸:提問本身就是推進器。

## English Notes

### TL;DR

- **A deliberately different angle.** Everyone else was talking about coding agents and how to extend them; he wants to talk about *adding a new capability* — multimodality. "When you hear me now, you don't just see a text, you see me, you see everything. So we live in a multimodal world."
- **The structural skew in today's multimodal models**: a very strong LLM with a visual head found somewhere and attached, trained together in post-training. Analysis shows **most of the reasoning in multimodal understanding happens in the LLM part, not the visual part** — and in-context learning with too many images actually confuses these models, for the same reason.
- **A two-year jump in spatial cognition.** Two years ago frontier models were near chance on mental rotation, perspective taking, maze completion, and shortcut discovery. By January this year they were at the level of a three-year-old child; by February 2026 they could solve spatial tasks that take a human about 10 seconds. On perspective taking, Opus 4.6 and Gemini 3.1 are now near 100%.
- **The mechanism**: recent work with colleagues at Apple probed models that *cannot* generate images and found they **internally reconstruct visual intermediate states** — and explicitly supervising that imagination improves performance further.
- **Two takeaways**: asking the right question is what advances the science; and multimodal models should not focus on text alone — training the generate-the-visual half helps a lot.

### Key Points

#### The old problem: compositionality and the bag of words (~02:46–02:48)

His observation about the field: **once people start asking the right question, solutions start appearing within a year or two.**

An early example is compositional reasoning. Older multimodal models captioning an image of, say, three zebras and two giraffes would jumble the numbers and the names together — treating everything as a **bag of words**, so compositionality broke. His group worked on fixing this: decomposing words into **tree structures**, producing denser and better-aligned captions, teaching the model to be structured. Things improved from there.

#### The structural skew: reasoning lives in the LLM (~02:48–02:50)

Two analyses of what actually happens inside the understanding workflow:

- Work with colleagues on the **performance gap in entity knowledge**, published at **ACL** a year ago, asking where in a multimodal model the reasoning occurs. The finding follows from the architecture: every modern multimodal model is a very strong LLM with a nice visual head attached — we invest heavily in training LLMs, then take some visual language model we found somewhere, attach it, and post-train them together. When you analyze multimodal understanding, **most of the analysis happens in the LLM part, not the visual part**.
- A second analysis of **in-context learning**. ICL is great in LLMs, but in VLMs there's a strange effect: give too long an in-context sequence with too many images and the models **start to get confused** — again because training relies mainly on the language side.

His question: maybe we need a shift.

#### Spatial cognition: from chance to near-perfect (~02:50–02:54)

The talk narrows to **spatial cognition**, starting from colleagues' work two years ago, "**Does Spatial Cognition Emerge in Frontier Models?**", which ran classic spatial-cognition tests on multimodal models:

- **Mental rotation** — given a shape, identify which candidate is the same shape rotated.
- **Perspective taking** — e.g. what is the angle between the bat and the dog, answered from a given viewpoint.
- **Maze completion** — solve the maze.
- **Shortcut discovery** — show the model a walkthrough of a place that doesn't take the shortest path, then ask it to take the shortest path.

**Two years ago, all models were very bad** — frontier models including GPT sat near chance, only slightly better.

Then, once the question was on the table:

- **January this year**, a study the captions render as "baby vision" ran a similar exploration and found frontier models roughly at the level of a **three-year-old child**. His aside: nice to grow to three years old in a year and a half, though usually we'd prefer to grow slower.
- Another work compared how long a human takes to solve each problem against what models can do, finding that by **February 2026** frontier models solve spatial-cognition tasks that take humans **about 10 seconds**. Since mental rotation takes humans real time to work through, being capped at 10-second tasks is "not so great, but better than what we had before."
- Task by task: on **perspective taking**, the best models were near chance two years ago; now **Opus 4.6 and Gemini 3.1 are almost at 100%**. **Maze completion** is still not great, but **just three months ago** it leapt from near chance (his example: GPT-5.4), and **shortcut discovery** did the same.

#### Why: the models are imagining internally (~02:54–02:56)

Recent work with colleagues at **Apple** asked: **do multimodal models imagine electric sheep?** The answer is yes.

They studied a range of spatial-cognition tasks in an **open-loop** setting — show the model only the first frame, then ask what step it should take to solve the game. Critically, they looked at models that **cannot generate images** (they can receive images but not produce them), and **probed the weights with an attached transformer**.

The finding: **the model is internally imagining how to solve the problem.** Asked whether two shapes are the same shape under rotation, the model's internal weights **reconstruct the visual content** — the same thing we do when we mentally rotate two shapes. The same holds for assembling characters.

That may be exactly why the last two years improved so much: models started to imagine. So they went further and **gave the model the ability to imagine and supervised it to do so — and performance improved.**

#### Two closing points (~02:56)

Skipping the remaining results for time, he leaves two:

1. **Asking the right question is very important to advancing science.**
2. For multimodal models, **don't focus on text only — focus on generating the visual part too.** It helps the model improve a lot.

### Quotes

> "When you hear me now, you don't just see a text, you see me, you see everything. So we live in a multimodal world." (~02:46)

Why a room full of coding-agent talks still needs someone talking about vision.

> "You have very strong LLM and a nice visual head attached to it … we found somewhere, we attached to it." (~02:48–02:49)

The bluntest and most memorable description of current multimodal architecture: vision is bolted on, not co-designed.

> "Nice to grow to become three years old in one and a half year — but usually we want to grow slower." (~02:52)

His deadpan on the pace of spatial-cognition progress.

> "Once you start asking the question, you start to see improvement throughout time." (~02:51)

The through-line of the talk: the question itself is the engine.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Does Spatial Cognition Emerge in Frontier Models? | 同事兩年前的研究,系統性評估多模態模型的空間認知(SPACE benchmark) | Colleagues' work from two years ago systematically evaluating spatial cognition in frontier models (the SPACE benchmark) | arXiv 2410.06468;含 mental rotation / perspective taking / maze completion / shortcut discovery |
| Do multimodal models imagine electric sheep? | 與 Apple 同事的近期工作:探測不能生成影像的模型,發現其內部權重重建視覺中間狀態;主動監督「想像」可提升效能 | Recent work with Apple colleagues: probing non-image-generating models reveals internally reconstructed visual states; supervising imagination improves performance | arXiv 2605.09693 |
| 「Performance gap in entity knowledge」(ACL,一年前) | 分析多模態模型的推理發生在 LLM 端而非視覺端 | Analysis showing multimodal reasoning occurs in the LLM rather than the visual component | 講題名稱以逐字稿口述為準,完整標題待確認 |
| Compositional reasoning 相關工作 | 用樹狀結構分解詞、密集對齊 caption,改善「詞袋」問題 | Tree-structured decomposition and denser aligned captions to fix bag-of-words compositionality | 講者團隊多篇工作,未報出個別標題 |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Raja Giris | Raja Giryes |
| multimodel | multimodal |
| special cognition | spatial cognition |
| mess completion | maze completion |
| shortest discovery | shortcut discovery |
| bag of forts | bag of words |
| group positionality | compositionality |
| OPUS 4.6 | Opus 4.6 |
| Germany 3.1 | Gemini 3.1 |
| GPD 5.4 | GPT-5.4 |
| electric ship | electric sheep |
| great lip | great leap |

## 待確認 / To Verify

- **"baby vision"**(2026 年一月、發現 frontier model 約當三歲小孩水準的研究)的正確名稱與出處。/ Correct name and source for the January 2026 study heard as "baby vision".
- 「比較人類解題所需時間」的那篇 2026 年二月工作的名稱。/ Title of the February 2026 work comparing human solve-time against model capability.
- 與同事合作、去年發表於 ACL 的那篇工作的完整標題(逐字稿作 "performance gap in entity knowledge")。/ Full title of the ACL paper.
- 探測實驗中「if two shapes have the same naturality」——"naturality" 應為某個空間認知術語(疑為 chirality / orientation),需看投影片確認。/ The term rendered as "naturality" in the probing experiment likely mis-transcribes a spatial-cognition term.
- 他因時間跳過的其餘結果(講者說 "we have some more results, because of time I will skip them")。/ The results he skipped for time.
