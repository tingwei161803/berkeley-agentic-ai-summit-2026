---
title: "The Unit Distance Conjecture and AI for Math"
title_zh: "Unit Distance 猜想與 AI for Math"
speaker: "Lijie Chen"
affiliation: "Researcher, OpenAI"
type: talk
stage: Atlas
date: 2026-08-02
session: "Session 3: AI for Math"
video: "https://www.youtube.com/watch?v=-7AJJLwYW1Q&t=3955s"
video_range: "01:05:55–01:17:43"
transcript: "tmp/[English (auto-generated)] Atlas Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [ai-for-math, discrete-geometry, test-time-compute, reasoning, openai]
---

# Unit Distance 猜想與 AI for Math(The Unit Distance Conjecture and AI for Math)

**一句話總結**:推翻 Erdős 1946 年 unit distance 猜想的不是為數學特訓的模型,而是一個沒有 harness、只給一個 prompt 的通用推理模型;它的優勢不是深度,而是**同時精通兩個相距很遠的數學領域**——這正是人類數學家最貴的能力。
**One-line summary**: The Erdős unit distance conjecture from 1946 was disproved not by a math-specialized model but by a general reasoning model with no harness and a single prompt. Its edge wasn't depth — it was simultaneous fluency in two distant mathematical fields, which is exactly the most expensive thing for a human mathematician to acquire.

## 中文筆記

### TL;DR

- **結果本身**:約兩個月前 OpenAI 宣布模型**推翻**了 Erdős 的 unit distance 猜想——構造出單位距離對數超過線性的點集。原猜想問的是:平面上 n 個相異點,距離恰為 1 的點對數是否至多大約線性多。
- **產出方式才是重點**:由一個**沒有為數學特訓**的通用推理模型(基本上就是一版 ChatGPT)在一次硬數學問題的評估中發現;**沒有 harness**——一個 prompt,模型持續思考、視需要用工具(可存取網頁與終端機),最後給出答案。
- **構造的性質**:Erdős 原構造是 n×n 網格加上精心挑選的縮放;新構造是在 L(i) 這個數域上的網格,其中 L 是精心設計的高次實數域。模型在思路中自己講明了直覺:代數量的次數與高度可以極大,而這反而是好事。
- **能力來源**:成功率隨 test-time compute 單調上升;看 CoT 可見模型會自省「這個方向沒進展 / 我剛剛錯了」並自我修正。
- **他對難度的評估**:這個結果約值「頂尖人類的 6 小時」——**但前提是這個人已經精通全部數學**。證明本身不深,難在要同時是很好的代數數論學家與很好的離散幾何學家;而學會一個新領域要兩年。**AI 的獨特優勢就在跨領域廣度**,而不是單點深度。

### 重點整理

#### 問題與結果(約 01:06–01:08)

他開場自嘲這是「比較像昨天的新聞」——投影片是幾週前做的,期間他們又發布了 10 項數學重大未解問題的新證明,但這個發現仍值得回顧。

**Unit distance 問題**敘述極簡單:平面(二維歐氏空間)上任意 n 個相異點,距離大約為 1 的點對最多能有多少?猜想是至多大約線性多。這是 Paul Erdős 在 **1946 年**提出的,是離散幾何的核心問題之一。

約兩個月前他們宣布:**OpenAI 的模型推翻了這個猜想**,構造出點對數超過線性的例子。

#### 這個發現是怎麼產生的(約 01:08–01:09)

這一段是整場最值得記下的部分:

- 由一個**通用推理模型**達成,**不是為數學特別訓練的**;它完全通用,基本上就是一版 ChatGPT。
- 發現於一次**模型評估**過程中——他們拿非常難的數學問題來測模型,因為現在大多數數學 benchmark 都已飽和,必須找難題才能測出能力。
- **完全沒有 harness**:就是給模型一個 prompt,它持續思考、可能用一些工具,然後得到最終答案。模型能存取**網頁與終端機**,所以可以自己查前人做過什麼。

#### 新舊構造的差別(約 01:09–01:10)

- **Erdős 原構造**:一個 n×n 網格,配上精心挑選的縮放,讓其中很多點對距離恰為 1。
- **新構造**:更複雜——是在有理數上的網格,並在數域 **L(i)** 中工作,其中 **L 是一個精心設計的高次實數域**。

他沒有深入細節,但引了模型自己在思路中寫下的直覺:**這些代數對象的次數與高度可以極其巨大,而那其實可以是件好事**——模型正是據此挑出了讓構造成立的那個數域。

#### Test-time compute 與自我修正(約 01:10–01:11)

拿到解之後,他們回頭研究**成功率與投入的 test-time compute 的關係**:投入越多 test-time compute,解對的機率越高。**想更久,確實更可能找到正確解。**

而從 CoT 可以看到:模型能**自省**——意識到自己在某個方向沒有進展、或發現自己犯了錯,然後自我修正並繼續。

#### 如何衡量 AI 的進展(約 01:11–01:13)

他引用 **METR** 的圖:x 軸是年份,y 軸是「該時點 agent 能可靠完成的任務,換算成人類需要多少時間」。這條線大約**每 6 個月翻倍**——不過他也指出 METR 的圖主要落在 coding 領域。

換到數學上做同樣的刻度:
- 約兩年前,模型能解 **AIME**——大致等於一位很好的高中生 20 分鐘。
- 一年後,能解 **IMO** 問題——難得多,約等於頂尖高中生 90 分鐘。
- 再一年後,能解**離散幾何中的長年未解問題**。

#### 6 小時的但書:AI 的優勢是廣度而非深度(約 01:13–01:15)

那 unit distance 這個結果換算成多少人類時間?他的估計是**約頂尖人類的 6 小時**——**但前提是這個人已經精通全部數學**。

理由是:**這個證明並不深**。它的難處在於需要從一個相距很遠的領域取出想法、套回離散幾何。你必須同時是很好的**代數數論**學家與很好的**離散幾何**學家;如果兩邊都很強,大概一兩天就能推到結論。**真正的挑戰是精通兩個相距很遠的領域**——因為學會一個新領域大概要兩年。

所以 AI 在這裡有非常獨特的優勢:**對所有數學領域都有廣泛熟悉度**,而且在許多子領域都有相當水準。這種例子對已經具備正確專長的人來說不需要多少時間,但對必須先學該領域的人就完全是另一回事。unit distance 的進展反映的是**「想更久」× 「更好的領域知識」兩種強度相乘**的效果。

他也給了誠實的但書:**有些數學結果需要數學家在單一主題上深耕數年**,而 AI 是否已經到那個程度,**還不清楚**。

接著:unit distance 之後他們發布了 **5.6**,數學推理非常強,過去兩週已有大量公開結果;而且**就在前一天**又宣布了 10 項數學與理論計算機科學不同領域的新結果。

#### 他對後果的看法(約 01:15–01:17)

- **AI 特別擅長連結相距很遠的研究領域**,unit distance 本身就是例子。數學家會因此被賦能去使用他們較不熟悉領域的想法,因為 AI 能找到相關概念並解釋得很好。
- **數學從來就不只是解題**。他強調:OpenAI 這個 unit distance 解答中最重要的人類輸入,其實是 **Paul Erdős**——是他提出了這個敘述簡單、解答卻極深的漂亮問題。**AI 找到解,而人類理解了它。** 證明發布後,世界各地不同團隊已有至少五、六項後續工作。
- 因為現在很容易找到例子,**「該問哪些深刻問題」這件事的迭代會變得容易得多**。
- **類比**:精確計算曾經是數學很大一部分,計算機與電腦解放了數學家;而自從有了 Codex、AlphaCode 這類 coding 模型,**程式設計師反而花更多時間寫程式**,因為能做的事變多了。他預期數學家也一樣會被賦能去做更多數學——不必再做繁瑣計算,可以專注在高層次的想法,或單純享受過程。

### 金句

> "This is achieved by a general reasoning model which is not trained specifically for math. It's completely general. It's basically a version of ChatGPT."(約 01:08)

這場最重要的一句:突破來自通用能力,不是為數學客製的系統。

> "Essentially there's no harness. You just give the model one prompt and then it keeps thinking about things and maybe use some tools and then it arrives at the final answer."(約 01:08)

在一場滿是 harness 與 orchestration 的峰會上,這句話格外醒目。

> "The challenge is really to master two distinct areas. So, in that sense, AI has this very unique advantage here."(約 01:14)

AI 的優勢不是比人聰明,而是不需要花兩年學一個新領域。

> "The most important human input to the OpenAI solution to unit distance is actually Paul Erdős, who really posed this beautiful question."(約 01:16)

提問仍然是人類的工作;AI 找到解,人類理解它。

## English Notes

### TL;DR

- **The result**: about two months before the talk, OpenAI announced that its model **disproved** Erdős's unit distance conjecture, constructing point sets with more than a linear number of unit-distance pairs. The problem, posed by Erdős in **1946**, asks whether n distinct points in the Euclidean plane can contain at most roughly linearly many pairs at distance one.
- **How it happened matters more**: the discovery came from a **general reasoning model not trained specifically for math** — essentially a version of ChatGPT — during an evaluation on very hard math problems (necessary because most math benchmarks are saturated). **There was no harness**: one prompt, the model keeps thinking, uses tools as needed, with access to the web and a terminal.
- **The construction**: Erdős's original was an n×n grid with a carefully chosen scaling. The new one is a grid over the rationals working in the field L(i), where L is a carefully engineered high-degree real number field. The model's own chain of thought explained the intuition: the degree and height of the algebraic objects can be enormous, and that's actually a good thing.
- **Where the capability comes from**: success probability rises monotonically with test-time compute, and the chain of thought shows the model introspecting — noticing it isn't making progress or has made a mistake, then self-correcting.
- **His difficulty estimate**: roughly **6 hours of top human time — assuming that human already knows all of mathematics.** The proof isn't deep; the hard part is being both a very good algebraic number theorist and a very good discrete geometer, and learning a new area takes about two years. **AI's unique advantage is breadth, not depth.**

### Key Points

#### Problem and result (~01:06–01:08)

He opens by calling this "more like yesterday's news" — the slides were made a couple of weeks earlier, and in the meantime they've released ten more proofs on major open problems — but the discovery is still worth reviewing.

The unit distance problem is simple to state: does every set of n distinct points in the Euclidean plane contain at most roughly linearly many pairs that are distance one apart? Paul Erdős proposed it in 1946, and it's one of the central questions in discrete geometry. Roughly two months before the talk, they announced that an OpenAI model had **disproved** the conjecture, exhibiting a construction with a superlinear number of unit-distance pairs.

#### How the discovery was produced (~01:08–01:09)

This is the part worth writing down. It was achieved by a **general reasoning model, not trained specifically for math** — completely general, basically a version of ChatGPT. It surfaced during a serious evaluation of the model on very hard math problems, which they need because most math benchmarks are saturated and only hard problems still measure ability. And there was **essentially no harness**: one prompt, the model keeps thinking, maybe uses some tools, and arrives at a final answer. It had access to the web and a terminal, so it could look up what had been done before.

#### Old and new constructions (~01:09–01:10)

Erdős's original construction was an n×n grid with a carefully chosen scaling so that many pairs sit at distance one. The new one is more complicated: a grid over the rationals, working in a field L(i) where **L is a carefully engineered high-degree real number field**.

He doesn't go deep into the details, but quotes the model's own stated intuition from its chain of thought: the degree and height of the algebraic objects can be enormous, but that can actually be a good thing — and the model chose the number field on that basis so the construction goes through.

#### Test-time compute and self-correction (~01:10–01:11)

After obtaining the solution, they studied how the model's success probability correlated with the test-time compute spent on the problem: the more compute, the higher the success rate. Thinking longer definitely makes it more likely to find a correct solution. Looking at the chain of thought, the model can introspect — realize it isn't making progress in one direction or that it has made a mistake — then self-correct and keep going.

#### Measuring AI progress (~01:11–01:13)

He borrows **METR**'s plot: years on the x-axis, and on the y-axis the amount of human time a task would take, for tasks the agent can reliably complete at that point in time. The line roughly **doubles every 6 months** — though he notes METR's graph is mostly in the coding domain.

The math version of the same scale: about two years ago models could solve **AIME** problems, maybe 20 minutes for a very good high school student. A year later, **IMO** problems — considerably harder, maybe 90 minutes for top high schoolers. Another year later, a long-standing open problem in discrete geometry.

#### The six-hour caveat: breadth, not depth (~01:13–01:15)

So how much human time is the unit distance result worth? His claim: roughly **6 hours of top human time — assuming that human already knows all of mathematics.**

The reason is that the proof isn't deep. What it requires is taking ideas from a very distinct field and applying them back to discrete geometry. You'd have to be a very good algebraic number theorist *and* a very good discrete geometer; if you're strong in both, it probably takes a day or two to push through to the conclusion. The challenge is mastering two distinct areas — and learning an area takes something like two years.

That's where AI has a genuinely unique advantage: broad familiarity across all mathematical fields, and decent competence in many subfields. Finding this kind of example doesn't require extreme human time if the human already has the right expertise — but it does if they must first learn the area. Progress on unit distance reflects a multiplied effect of both strengths: thinking longer, and better domain knowledge.

He adds an honest caveat: some mathematical results require years of work from a mathematician pushing deeply on one topic, and it's unclear whether we're at that point yet with AI.

After unit distance they released **5.6**, which is very strong at mathematical reasoning, with many public results in the two weeks since; and the day before the talk they announced ten more results across mathematics and theoretical computer science.

#### Consequences as he sees them (~01:15–01:17)

AI is especially good at connecting distant fields of research — unit distance is itself an example. Mathematicians will be empowered to use ideas from fields less familiar to them, because AI can find the relevant ideas and explain them well.

Mathematics was never just problem solving. He makes a point of saying that the most important human input to the OpenAI unit-distance solution was **Paul Erdős**, who posed this beautiful question with a simple statement and a very deep solution. AI found a solution, and a human understood it. Since the release, at least five or six follow-up works have appeared from different groups around the world. Because examples are now easy to find, iterating on *which* deep questions to ask becomes much easier.

His closing analogy: the ability to do precise calculation used to be a big part of math, and calculators and computers empowered mathematicians to do more. Since coding models like Codex and AlphaCode, programmers actually spend *more* time coding, because there's more they can do once empowered. He expects mathematicians will similarly be empowered to do more math — freed from tedious calculation to focus on high-level ideas, or simply to enjoy the process.

### Quotes

> "This is achieved by a general reasoning model which is not trained specifically for math. It's completely general. It's basically a version of ChatGPT." (~01:08)

The load-bearing claim of the talk: the breakthrough came from general capability, not a math-specialized system.

> "Essentially there's no harness. You just give the model one prompt and then it keeps thinking about things and maybe use some tools and then it arrives at the final answer." (~01:08)

A striking sentence at a summit otherwise full of harnesses and orchestration layers.

> "The challenge is really to master two distinct areas. So, in that sense, AI has this very unique advantage here." (~01:14)

The advantage isn't being smarter than a human; it's not needing two years to learn a new field.

> "The most important human input to the OpenAI solution to unit distance is actually Paul Erdős, who really posed this beautiful question." (~01:16)

Posing the question is still human work; AI found a solution and a human understood it.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Erdős unit distance 問題 | 平面上 n 點中距離為 1 的點對數上界問題,1946 年提出 | Upper bound on unit-distance pairs among n points in the plane; posed 1946 | 離散幾何核心問題;現已被推翻 / a central discrete-geometry question, now disproved |
| OpenAI 的 unit distance 證明 | 通用推理模型在評估中發現的反例構造 | The counterexample construction found by a general reasoning model during an eval | 無 harness、單一 prompt、可存取網頁與終端機 / no harness, one prompt, web and terminal access |
| METR time-horizon 圖 | 以「agent 能可靠完成的任務所需人類時間」衡量 AI 進展 | Progress measured as the human time-length of tasks agents can reliably complete | 講者稱約每 6 個月翻倍,主要為 coding 領域 / he cites ~6-month doubling, mostly coding |
| AIME / IMO | 用來替數學能力進展做人類時間刻度 | Used as human-time yardsticks for math capability progress | 分別約 20 分鐘與 90 分鐘頂尖高中生時間 / ~20 and ~90 minutes of top high-schooler time |
| 5.6 | unit distance 之後發布、數學推理非常強的模型版本 | The model version released after unit distance, very strong at mathematical reasoning | 完整名稱待確認 / full model name to verify |
| Codex / AlphaCode | 用來類比「工具讓從業者做更多而非更少」 | Used to argue tools make practitioners do more, not less | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Lisha | Lijie Chen |
| Meter(那張圖) | METR |
| Alpha Code | AlphaCode |
| Paul Erdős(字幕拼寫不一) | Paul Erdős |
| the algebraic variation | algebraic 對象的 degree 與 height(字幕殘缺)/ garbled; refers to the degree and height of the algebraic objects |
| we released 5.6 so | we released 5.6(「so」為口癖)/ "so" is a filler word |

## 待確認 / To Verify

- 「5.6」的完整模型名稱與發布日期(字幕僅有版本號)。/ Full name and release date of the model referred to as "5.6".
- METR 圖的翻倍週期:講者說每 6 個月,METR 公開的數字通常引用為約 7 個月,需核對他引用的是哪一版。/ METR's doubling period: he says 6 months; the commonly cited published figure is ~7 months — check which version of the plot he showed.
- 「前一天宣布的 10 項數學與理論計算機科學結果」的公告來源。/ Source for the ten results announced "yesterday".
- 新構造中 L(i) 與高次實數域的精確敘述(講者刻意略過細節)。/ Precise statement of the L(i) construction — he deliberately skipped the details.
- 「至少五、六項後續工作」的具體論文。/ The specific follow-up papers he referred to.
