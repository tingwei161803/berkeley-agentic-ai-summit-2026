---
title: "When Language Models Learned to Reason"
title_zh: "當語言模型學會推理的那一刻"
speaker: "Giambattista Parascandolo"
affiliation: "Research Fellow, OpenAI"
type: talk
stage: Atlas
date: 2026-08-01
session: "Session 1: Foundational Capabilities"
video: "https://www.youtube.com/watch?v=WeriQic-QW0&t=1958s"
video_range: "00:32:38–00:41:12"
transcript: "tmp/[English (auto-generated)] Atlas Stage - August 1st - Morning Session [DownSub.com].srt"
status: draft
tags: [reasoning, test-time-compute, openai, history]
---

# 當語言模型學會推理的那一刻(When Language Models Learned to Reason)

**一句話總結**:他拿出四、五年前 OpenAI 內部最早討論 reasoning 的原始投影片,展示當年那個「模型多想一會兒也給不出更好答案」的世界,以及讓團隊決定放手擴張的第一批證據——原來是幾張數馬鈴薯袋子的醜投影片。
**One-line summary**: He dug out the actual four-to-five-year-old internal slides from OpenAI's earliest discussions of reasoning — back when giving a model more time produced the identical answer — and showed the humble evidence that convinced the team to scale it up: some ugly slides about counting bags of potatoes.

## 中文筆記

### TL;DR

- **這場演講全部用四到五年前的原始內部投影片**——「有句話說,沒有什麼比昨天的報紙更不新鮮」,而這些投影片又老又醜,因為當初根本不是為了公開報告做的。他形容這是一趟「時光旅行」,去看看當年做 reasoning 是什麼感覺。
- **核心圖像:把「難度」的二維輪盤加上第三個軸——thinking time。** Pre-training 只讓已解問題的圓圈從中心往外緩慢擴張,永遠碰不到最難的問題;reasoning 是問「能不能讓這個圓柱體隨時間往外長」。
- **決定性的早期證據**:只是在 prompt 裡不斷加上「一步步想、把過程寫出來、確認沒有錯」,模型輸出的文字長度就變長,而**準確率隨著輸出長度上升**。這條曲線就是後來一切的起點。

### 重點整理

#### 為什麼要看老投影片(約 00:33)

「這些投影片有五年了,每一張都是四到五年前的。」他要展示的是 OpenAI 內部**最早期**談 reasoning 的簡報,「這不是在談未來」。投影片很醜,因為它們從來就不是為了這種場合準備的,只是很久以前給團隊看的東西——「把它當成某種時光旅行,看看那時候做 reasoning 是什麼樣子」。

#### 什麼是 reasoning:那個轉三維的輪盤(約 00:34–00:36)

當年他們的思考方式是這樣的:

- 想像一個彩色輪盤,代表所有問題的空間。**角度代表主題**(AI、數學、物理、生物…),**離圓心的距離代表難度**。
- 當時他們在 pre-train GPT-2、3、4,能解的問題圈子就從中心往外擴張,把各主題都覆蓋一點點,並隨著規模成長解出稍微難一點的問題。
- **關鍵疑問是:那些真正困難的問題,什麼時候才會被解開?** 他舉 Andrew Wiles 為例:證出費馬最後定理的人想了七年——但他不是同時解決所有問題,他是花七年解**一個**問題,而大多數困難問題都是這種形狀。所以「單純把模型 pre-train 得更博學」這條路,看起來不太可能把圓圈擴張到覆蓋所有最難的問題。
- **那人類怎麼做?我們會思考、會推理。能不能給模型同樣的能力?**
- 於是投影片做了一個花招:把輪盤傾倒、推到畫面一側,騰出**第三個軸:thinking time**。問題就變成——「怎麼讓這些圓柱體隨著時間往外長?」
- **今天聽起來也許可笑,但當年確實如此**:你給模型更多時間,它會給你一模一樣的答案,因為幾毫秒就吐完了,它不知道拿多出來的時間做什麼。
- 還有個現實限制:Andrew Wiles 想了七年,而當時模型的 context 只有幾千、也許 8,000 個 token——「8,000 個 token 你能做什麼?頂多幾秒鐘的 reasoning。」就算真的讓它會推理,這怎麼可能發生?

#### 第一批證據:如果我們就直接叫它想一想呢?(約 00:37–00:40)

另一個當年沒有答案的問題是:**reasoning 的載體(substrate)是什麼?** 花掉 test-time compute 的方式有很多種,例如用 recurrent network 在內部多跑幾步。結果**文字**的效果非常好。

他接著展示自己加入 OpenAI 後第一個專案的探索——**在模型從未被訓練去思考的情況下,單純要求它思考會發生什麼**。這是給團隊信心去擴張規模的其中一塊拼圖。

三個例子(「以今天的標準很蠢,但正好看出短短時間內我們走了多遠」):

1. **馬鈴薯**:問 GPT-3 有 29 袋馬鈴薯再加 17 袋之類的題目,模型回答「46 公斤馬鈴薯」——完全錯。加上「先想一想再回答」,模型不會立刻給答案,而是先吐一段文字,然後**至少有時候**會答對——相較於原本的「從不」。
2. **樂器**:「我有一支單簧管、一台鋼琴、一隻狗,我有幾件樂器?」模型說 1,錯。拆解成一步步後,模型推理出「狗不是樂器、單簧管是樂器、但鋼琴不是」——**還是 1**。於是再加上「也請一步步拆解」讓它想得更久一點,才終於答對。
3. **數東西**:一張椅子、一台音箱、一個烤箱…模型說 20,正解是 14。當年可以直接查模型輸出「14」的機率——**2%**,基本上等於永遠不會。加上「一步步拆解」後,模型逐項數出一長串,答案就變好了。

#### 把直覺變成量化曲線(約 00:39–00:40)

他展示了最早的兩張量化圖:

- **第一張**:不斷疊加 prompt 指令(「一步步想」→「拆解開來」→「我真的要你把所有工作都做完、把過程全寫出來、確認沒有錯誤」),模型從幾乎解不出題,變成能解越來越多題。
- **第二張(他說順序放錯了,應該跟前一張一起看)**:模型生成解法的**平均長度**。一開始只叫它解題幾乎什麼都不輸出;隨著指令疊加——還得用「First,」開頭這種小技巧,免得模型又想直接給答案,而是進入「接下來會是一長串待辦事項」的模式——「有了第一點,就一定會有第二、第三點,那就多輸出一些文字吧」。
- **結論**:模型輸出的文字量增加,準確率就跟著上升。

「從那之後很多人做了這個方向,我們做了一個大專案,然後還有很多元件現在還不能談。但就是這樣——非常卑微的開端,眾多開端之一。我覺得在這一堆談未來的演講之中,讓大家看看這個,可能挺有意思的。」

### 金句

> "There's this saying that there's nothing more stale than yesterday's newspaper. Well, these slides are five years old."(約 00:33)

開場白,也是整場的框架:刻意反其道而行,講最不新鮮的東西。

> "There was a time where you would give a model more time to think and it would give you the exact same answer, because after a few milliseconds you would get the answer and it would not know what to do with the extra time."(約 00:36)

一句話標記了那條分水嶺——今天聽起來荒謬,但這就是起點。

> "Very humble beginnings — one of many. I thought it was interesting maybe for you guys to see this in the midst of these talks about the future."(約 00:41)

## English Notes

### TL;DR

- **The entire talk runs on four-to-five-year-old internal slides.** "There's this saying that there's nothing more stale than yesterday's newspaper" — and these are ugly, because they were never meant to be presented anywhere. He framed it as time travel: what it felt like to work on reasoning back then.
- **The central picture: add a third axis — thinking time — to a two-dimensional wheel of problems.** Pre-training only pushes the solved-problem circle outward from the center and never reaches the hardest problems; reasoning asks whether that cylinder can grow *over time* instead.
- **The evidence that justified scaling it up** was embarrassingly simple: stack prompt instructions telling the model to think step by step and show its work, watch the output get longer, and watch accuracy rise *with* output length. That curve started everything.

### Key Points

#### Why old slides (~00:33)

These are the earliest internal presentations OpenAI had when it started work on reasoning — explicitly not a talk about the future. The slides are ugly because they were team-internal artifacts from a long time ago. Think of it as time travel to see what working on reasoning used to look like.

#### What reasoning is: the wheel that tilts into 3D (~00:34–00:36)

The framing at the time: picture a colorful wheel covering the space of all problems, where the **angle** is the subject (AI, math, physics, biology) and the **radial distance** is difficulty. As they pre-trained GPT-2, 3, and 4, the circle of solvable problems expanded outward from the middle, covering every subject a little and solving slightly harder problems as scale grew.

The nagging question was when the genuinely hard problems would fall. His example: Andrew Wiles thought about Fermat's Last Theorem for seven years — and crucially, he wasn't solving everything at once; seven years bought him *one* problem, and most hard problems have that shape. Something about "just pre-train models to be better at general knowledge" seemed unlikely to ever expand the circle to cover the hardest problems.

So: what do humans do? We think. We reason. Can we give models the same capability? The slide then does something fancy — tilt the wheel into 3D, push it to the side of the screen, and open up a third axis that didn't exist before: **thinking time**. The question becomes how to grow those cylinders outward given more time.

Two things about that era are worth remembering. First, "it might look a bit ridiculous today, but there was a time where you would give a model more time to think and it would give you the exact same answer" — the answer arrived after a few milliseconds and the model had no idea what to do with the extra time. Second, the practical ceiling: Wiles thought for seven years, and the models had a context of a few thousand tokens, maybe 8,000. What can you do with 8,000 tokens? At most a few seconds of reasoning. Even granting that they'd learn to reason, how was this ever supposed to happen?

#### The first evidence: what if we just ask them to think? (~00:37–00:40)

Another open question was what substrate reasoning would use. There are many ways to spend test-time compute — a recurrent network taking many internal steps, for instance. Text turned out to work really well.

He then showed his first project after joining OpenAI: a small exploration of what models could do when simply *asked* to think, despite never having been trained to. It was one of the pieces that gave the team confidence to scale things up.

Three examples, silly by today's standards but useful for measuring the distance traveled:

1. **Potatoes.** Ask GPT-3 about 29 bags of potatoes plus 17 more, and the model answers "46 kilos of potatoes" — plainly wrong. Add "let's think about it before getting the answer," and instead of an immediate answer you get some extra text first, and then, at least *sometimes*, the right answer — compared to never.
2. **Instruments.** "I have a clarinet, a piano, a dog. How many musical instruments do I have?" The model says one. Break it down step by step and the model reasons that a dog isn't an instrument, a clarinet is — but a piano isn't. Still one. Only after adding another instruction to break it down further does it get there.
3. **Counting.** A chair, an amp, an oven, and a long list of things: the model says 20, the answer is 14. Back then you could check the model's probability of outputting 14 — it was **2%**, essentially never. Add "let's think about it, break it down step by step," and you get a long enumeration and a better answer.

#### Turning intuition into a curve (~00:39–00:40)

Two plots, the earliest quantitative evidence. The first: keep stacking prompt instructions — think step by step, break it down, "I really want you to do all the work and show all your work and make sure there are no mistakes" — and a model that could barely solve problems solves more and more.

The second (which he noted should have appeared alongside the first): the **average length of generated solutions**. Asked plainly to solve, the model produced almost nothing. As instructions accumulated — including the trick of forcing the output to start with "First," so the model wouldn't immediately blurt an answer but instead adopt the mindset that a long list was coming ("if there's a first, there must be a second and a third, so let's output a lot of text") — length grew. And as the amount of text the model output increased, its accuracy went up.

"Since then lots of other people worked on this, we did a big project, and then lots of other components we can't talk about yet. But — very humble beginnings, one of many."

### Quotes

> "There's this saying that there's nothing more stale than yesterday's newspaper. Well, these slides are five years old." (~00:33)

The opening line and the frame for the whole talk.

> "There was a time where you would give a model more time to think and it would give you the exact same answer, because after a few milliseconds you would get the answer and it would not know what to do with the extra time." (~00:36)

One sentence that marks the dividing line — absurd today, and exactly where this started.

> "Very humble beginnings — one of many. I thought it was interesting maybe for you guys to see this in the midst of these talks about the future." (~00:41)

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Andrew Wiles / Fermat's Last Theorem | 用來說明「困難問題的形狀」:七年只解一題 | Used to illustrate the shape of hard problems: seven years buys you one | 字幕誤植為 "Andrea Wilds" / "Andrew Wild" |
| GPT-2 / GPT-3 / GPT-4 | 當年 pre-training 擴張「可解問題圈」的世代 | The pre-training generations expanding the circle of solvable problems | GPT-3 是三個 prompt 範例的實驗對象 |
| "Let's think step by step" | 早期靠 prompt 誘發推理的作法;他展示的是 OpenAI 內部平行的探索 | The early prompt-elicited reasoning trick; he showed OpenAI's internal parallel exploration | 他未點名任何外部論文 / he cited no external paper by name |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Gian Batista Parisand Doyo | Giambattista Parascandolo(現場暱稱 GB)|
| Andrea Wilds / Andrew Wild | Andrew Wiles |
| for mass theorem | Fermat's Last Theorem |
| Malo said one | the model said one |
| a client is | a clarinet is |
| finalizer | final answer |
| recurring network | recurrent network |

## 待確認 / To Verify

- 三個 prompt 範例的確切題目文字(馬鈴薯袋數、物品清單)由自動字幕還原,數字可能有誤;「29 袋 + 17 袋 → 46 公斤」與「答案 14 / 模型答 20 / 機率 2%」需對照投影片。/ Exact wording and numbers of the three prompt examples come from auto-captions; verify against the slides.
- 「a big project」指的是哪個專案他未點名(語境上指向 OpenAI 的 reasoning 模型系列),不做推測。/ He didn't name "the big project"; not guessing.
- 投影片上兩張量化圖的 benchmark 與 y 軸定義未說明。/ The benchmark and y-axis definition of the two quantitative plots were not stated.
