---
title: "An Optimization Perspective on Recursive Self-Improvement"
title_zh: "從最佳化視角看遞迴自我改進"
speaker: "Ian Fischer"
affiliation: "Co-CEO, Poetiq"
type: talk
stage: Compass
date: 2026-08-01
session: "Session 3: Foundational Capabilities"
video: "https://www.youtube.com/watch?v=AO0RXP-fVZQ&t=7811s"
video_range: "02:10:11–02:21:20"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [recursive-self-improvement, optimization, meta-systems, benchmarks, agent-harness]
---

# 從最佳化視角看遞迴自我改進(An Optimization Perspective on Recursive Self-Improvement)

**一句話總結**:真正的 RSI 需要「遞迴」與「自我」同時成立;把 LLM 當成系統的一個零件、而非改進的唯一目標,就能用「會自我最佳化的最佳化器」在每一步只花一次 inference(而非一次訓練)的成本下做到真正的複利式自我改進。
**One-line summary**: Real recursive self-improvement requires both the *recursive* and the *self* to hold; treating the LLM as one component of a broader system rather than the sole improvement target lets you build self-optimizing optimizers whose every RSI step costs one inference run instead of one training run.

## 中文筆記

### TL;DR

- **RSI 的定義要嚴格**:*Recursive* = 每一步的改進驅動下一輪改進;*Self* = 系統改進的是它自己,不是別的目標。兩者缺一不可。常見用法同時「太寬鬆」(把普通的迭代最佳化叫 RSI)又「太嚴苛」(認為只有改 LLM 參數才算 RSI)。
- **從 LLM-centric 轉向 systems-oriented**:把 LLM 只當成更大系統中的一個元件,能打開大量原本看不到的改進空間,而且更快更便宜。Poetiq 的迴路每一步只需要一次 inference run,而不是重新訓練一個 LLM。
- **Self-optimizing optimizers**:拿一個通用最佳化器(不依賴 gradient 等特化訊號、只要求目標能給出可測量的回饋),先用它最佳化任務目標——那還只是普通迭代最佳化;把它**指向最佳化器自己**,就成了 RSI。條件只有兩個:最佳化器要是通用的,而且要能回報自己的表現。
- **結果**:這套 meta system 全自動(零人工介入)在多個公開 benchmark 上刷到 SOTA;其中一半的 benchmark 是用**比前紀錄保持者更舊、更便宜的模型**達成的。他們因此宣稱「benchmarks are dead」——不是說 benchmark 沒用,而是在一個真正會遞迴自我改進的系統面前,靜態 benchmark 的價值有限。

### 重點整理

#### 什麼才算 RSI(約 02:11–02:13)

Poetiq 是 Ian Fischer 與共同創辦人約一年半前創立的新創,**整間公司只做遞迴自我改進**——「building AI that improves itself」。團隊 10 位科學家與工程師,主要來自 Google DeepMind,以及 Apple、Microsoft、Amazon、ByteDance。早期成果在 reasoning、knowledge extraction 與 coding 上都刷出 SOTA。

他對 RSI 三個字逐字拆解:

- **Recursive**:每一步產出的改進,要能驅動下一輪的改進。
- **Self**:系統改進的對象**就是它自己**,不是某個外部目標。
- **Improvement**:這個沒什麼好講的,大家都在做某種形式的 improvement。

他刻意咬文嚼字,是因為業界對 RSI 的用法同時犯了兩個相反的錯:一邊**太寬鬆**——把單純的迭代改進迴路叫作 RSI;一邊**太嚴苛**——認為只有更新 LLM 參數才算 RSI。後者的問題在於,一個智慧系統裡**還有很多其他零件可以被有效改進**。

為什麼 RSI 重要?因為真正的 RSI **改進會複利(compound)**,而人類驅動的改進不會——原因很直白:人類不會在改進模型的過程中自己也變得越來越聰明,但 RSI 系統會。

#### 版圖:兩軸四象限(約 02:13–02:16)

他用兩個軸畫出 RSI 的地景:y 軸是成本(上便宜、下昂貴),x 軸是「是不是真的 RSI」(左邊是普通迭代最佳化,右邊才是 RSI)。

- **右下(貴但真 RSI)**:資金最雄厚的一群——Anthropic、OpenAI、Google 都投入大量資源,也就是一般人講 RSI 時想的那種 LLM-centric 路線。是真 RSI,但**每一步都要從頭訓練一個 LLM**。
- **右上(便宜且真 RSI)**:Poetiq 自己放在這裡,而且說這不是隨便放的——他們的迴路確實會複利,而每一步 RSI **只要一次 inference run**。鄰居包括 Darwin Gödel Machine 與 SICA(兩者主要針對 coding),以及會用自己生成的資料訓練的 MiniMax harness——都是真 RSI 也都便宜,只是比他們的做法窄。

換個切法就是:**下半是 LLM-centric,上半是 systems-oriented**——後者把 LLM 只當成一個應該被改進的更大系統的元件。從 LLM-centric 轉到 systems-oriented,會打開大量原本會錯過的改進可能,而且通常更快更便宜。

他接著點評兩種當紅路線:

- **Anthropic 的「AI that builds itself」**:拿一版 Claude 放進 Claude Code,然後「人類 + Claude Code」一起改進 Claude。這是**部分 RSI**——Claude 既是被改進的東西也是改進者的一部分,但迴路裡有人類,他不算(Anthropic 自己也不算)。修法很簡單:**把人拿掉**;他認為 Anthropic 已經在往那走,而且那大概也是他們擔心的事。
- **Automated AI scientist / auto research**:生成假設 → 實作 → 量測 → 寫論文 → 論文丟回知識庫。這**通常不是 RSI**,因為它針對的不是自己系統的某個部分。修法也簡單:把最佳化目標指向迴路裡用的那個 LLM——但這樣做會比現在大多數 automated AI scientist 貴得多。

#### Poetiq 的做法:self-optimizing optimizers(約 02:16–02:19)

拆成三步:

1. **從一個通用最佳化器出發**。「通用」的定義是:不依賴 gradient 這類特化訊號,只需要最佳化目標給出**可測量的回饋**。這比 hill climbing 之類的 black-box optimizer 還要更一般,因為回饋甚至不必是量化的。
2. **拿它去最佳化一個目標**。回饋可以很任意:accuracy、cost 這類標準指標,也可以是 rubric evaluations 或 reasoning targets 這類非典型訊號。到這裡**還不是 RSI**,只是標準的迭代最佳化。
3. **把這個通用最佳化器指向最佳化器自己**。現在是「最佳化器最佳化著那個正在最佳化目標的最佳化器」——**這才是 RSI**。

要讓一個最佳化器能最佳化自己,只需要兩個條件:它是通用最佳化器,而且它能提供關於自身表現的回饋。因為起點就是通用最佳化器,而任何最佳化器都能回報自己的表現,所以這裡沒有障礙。他特別澄清:**這跟說「最佳化器是 Adam 或 SGD」完全不同,那樣是行不通的。**

這就是他們稱為 **Poetiq meta system** 的東西:它是 RSI,而且他們用它最佳化一切——meta system 最佳化的每一個任務,都會回過頭幫助它把自己最佳化得更好、成為更強的最佳化器。既然是通用最佳化器,就可以指向 meta system 自身的任何部分,也可以指向任何可量測的任務:benchmark、客戶資料等等。

#### 實證結果與「benchmarks are dead」(約 02:19–02:21)

他們有一篇 blog post 主張 **benchmarks are dead**。他澄清這不是說 benchmark 沒用,而是:**在一個真正會遞迴自我改進的系統面前,靜態 benchmark 的價值相當有限**——因為他們能全自動地在「每一個他們打開來跑的 benchmark」上拿到 SOTA。全自動意味著**零人工介入**,而且通常很快。

投影片上的成績表裡,他認為最有意思的一點是:這些 benchmark 橫跨許多他們**從未接觸過的領域**,而其中**一半的 SOTA 是用比前紀錄保持者更舊、更便宜的模型**取得的——而前紀錄通常是 Fable 5。

接下來的方向是不再聚焦 benchmark,轉向與多個領域的早期客戶合作。他留下的觀點:**AI 的下一次相變,會來自一個能發明自己改進方式的系統**;Poetiq 刻意用「最佳化視角看 RSI、並用它去最佳化一切(包括最佳化器本身)」來為這次相變撒一張非常大的網。

### 金句

> "Recursive means that the new improvements at each step are going to drive the next round of improvements. And self — the system really is going to improve itself, not some other target."(約 02:11)

整場演講的定義基準線,後面所有的分類都建立在這句話上。

> "Humans don't become inexorably smarter while improving models, but RSI systems can."(約 02:12)

一句話解釋為什麼 RSI 的改進會複利而人類驅動的不會。

> "In the case of Anthropic, we can just get rid of the humans. They've kind of indicated that that's where they're headed and that's maybe something that they're worried about."(約 02:16)

把 Claude Code 迴路變成純 RSI 的「修法」,以及對此的一句冷處理。

> "The next phase transition in AI is going to come from a system that invents its own improvements."(約 02:20)

收尾的核心主張。

## English Notes

### TL;DR

- **Be strict about the definition.** *Recursive* means each step's improvements drive the next round; *self* means the system improves itself, not some other target. Common usage is simultaneously too permissive (calling ordinary iterative loops RSI) and too restrictive (insisting only LLM parameter updates count).
- **Shift from LLM-centric to systems-oriented.** Treating the LLM as one component of a broader system opens up improvement possibilities you'd otherwise miss — and tends to be faster and cheaper. Poetiq's loop costs one inference run per step, not one training run.
- **Self-optimizing optimizers.** Start with a general-purpose optimizer (no specialized signals like gradients; it only needs measurable feedback from the target). Point it at a task and you have plain iterative optimization. Point it at *itself* and you have RSI. The only two requirements: the optimizer must be general-purpose, and it must report feedback on its own performance.
- **Results**: the meta system sets state-of-the-art fully automatically — zero human intervention — across public benchmarks, and on half of them it did so using **older, cheaper models than the previous record holder**. Hence their claim that "benchmarks are dead" — not useless, but of limited value in the presence of a genuinely self-improving system.

### Key Points

#### What actually counts as RSI (~02:11–02:13)

Poetiq is a roughly 18-month-old startup built entirely around recursive self-improvement — "AI that improves itself." Ten scientists and engineers, mostly ex-Google DeepMind, plus Apple, Microsoft, Amazon, ByteDance. Early results set state-of-the-art on reasoning, knowledge extraction, and coding.

He unpacks the acronym deliberately, because two of the three letters do all the work. *Recursive*: improvements at each step drive the next round. *Self*: the target of improvement is the system itself. *Improvement*: everyone's doing some version of that.

The pedantry has a purpose. Common usage is **too permissive** — labeling standard iterative improvement loops as RSI — and **too restrictive** — insisting RSI only counts when you're updating an LLM's parameters. The latter misses that a lot of other pieces of an intelligent system can be improved quite effectively.

Why does it matter? Because real RSI **compounds**, and human-driven improvement doesn't: humans don't get inexorably smarter while improving models, but RSI systems do. That's why he calls it the most important frontier in AI research and the shortest path to superintelligence.

#### The landscape: two axes (~02:13–02:16)

Y-axis: cheap at the top, expensive at the bottom. X-axis: not-really-RSI on the left, genuine RSI on the right.

- **Lower right (expensive, genuine RSI)**: where the best-funded efforts live — Anthropic, OpenAI, Google. This is the LLM-centric picture most people have of RSI. Genuine, but every step requires training an LLM from scratch.
- **Upper right (cheap, genuine RSI)**: where Poetiq places itself, and not arbitrarily — their loop does compound, and each RSI step costs only an inference run. Neighbors: Darwin Gödel Machine and SICA (both primarily targeting coding), and the MiniMax harness (trains on some of its own generated data). All genuine and cheap, just narrower.

The same split read horizontally: the bottom half is LLM-centric, the top half is systems-oriented — viewing the LLM as just a component of a broader system worth improving.

He then diagnoses two prominent approaches:

- **Anthropic's "AI that builds itself"**: put a version of Claude inside Claude Code, then humans + Claude Code improve Claude. **Partial RSI** — Claude is both the thing improved and part of the improver, but there are humans in the loop and he doesn't count them (neither does Anthropic). The fix: remove the humans, which he thinks is where they're headed and maybe what they're worried about.
- **The automated AI scientist / auto-research pattern**: generate a hypothesis → implement it → measure it → write a paper → file it in a knowledge store. **Usually not RSI**, because it isn't targeting a piece of its own system. The fix is equally simple — target the LLM used inside the loop — but that makes it far more expensive than what most people run today.

#### Poetiq's approach: self-optimizing optimizers (~02:16–02:19)

1. **Start with a general-purpose optimizer** — one that relies on no specialized signals like gradients, requiring only measurable feedback from the target. This is more general even than black-box optimizers like hill climbing, because the feedback need not be quantitative.
2. **Point it at an optimization target.** Feedback can be conventional (accuracy, cost) or unusual (rubric evaluations, reasoning targets). This is still just iterative optimization.
3. **Point it at the optimizer itself.** Now the optimizer is optimizing the optimizer that's optimizing the target — and *that* is RSI.

Two requirements only: general-purpose, and able to report on its own performance. Since every optimizer can do the latter, there's no obstacle. He's explicit that this is very different from saying the optimizer is Adam or SGD — that would not work.

The result is the **Poetiq meta system**. Every task it optimizes helps it optimize itself into a more powerful optimizer, and because it's general-purpose it can be aimed at any part of the meta system as well as at any measurable task — benchmarks, customer data, whatever.

#### Empirical results and "benchmarks are dead" (~02:19–02:21)

Their blog post declaring benchmarks dead isn't a claim that benchmarks are useless — it's that in the presence of a properly recursive self-improving system, *static* benchmarks have limited value, because the system gets state-of-the-art fully automatically on every benchmark they've turned it on. Zero human interventions, usually quite quickly.

The most interesting detail in the results table: the benchmarks span a wide variety of domains they'd never worked on before, and on **half of them they hit SOTA using older, cheaper models than the previous record holder** — which was typically Fable 5.

What's next: less benchmark focus, more work with early customers across a variety of domains. His closing framing: the next phase transition in AI will come from a system that invents its own improvements, and Poetiq is deliberately casting a wide net for it by taking the optimization perspective on RSI and using it to optimize everything, optimizers included. (He also noted they're hiring.)

### Quotes

> "Recursive means that the new improvements at each step are going to drive the next round of improvements. And self — the system really is going to improve itself, not some other target." (~02:11)

The definitional baseline the whole taxonomy rests on.

> "Humans don't become inexorably smarter while improving models, but RSI systems can." (~02:12)

Why RSI compounds and human-driven improvement doesn't.

> "In the case of Anthropic, we can just get rid of the humans. They've kind of indicated that that's where they're headed and that's maybe something that they're worried about." (~02:16)

The one-line fix that turns the Claude Code loop into pure RSI, delivered dryly.

> "The next phase transition in AI is going to come from a system that invents its own improvements." (~02:20)

The closing thesis.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Poetiq | 講者共同創辦的新創,專做遞迴自我改進;核心產品是 Poetiq meta system | Speaker's startup, entirely focused on RSI; core product is the Poetiq meta system | 由 Ian Fischer 與 Shumeet Baluja(皆前 Google DeepMind)創立 / founded by Ian Fischer & Shumeet Baluja, both ex-Google DeepMind |
| Poetiq meta system | 會自我最佳化的通用最佳化器,每步 RSI 只需一次 inference | Self-optimizing general-purpose optimizer; one inference run per RSI step | 演講核心 / the talk's central construct |
| "Benchmarks are dead" blog post | 主張靜態 benchmark 在真 RSI 系統前價值有限 | Blog post arguing static benchmarks have limited value against a real RSI system | 詳見 poetiq.ai / see poetiq.ai |
| Anthropic "AI that builds itself" | Claude 放進 Claude Code,人類 + Claude Code 改進 Claude;講者評為「部分 RSI」 | Claude inside Claude Code, humans + Claude Code improving Claude; he calls it partial RSI | |
| Darwin Gödel Machine | 便宜且真 RSI,但主要針對 coding | Cheap, genuine RSI, primarily targeting coding | 字幕聽成 "Darwin Girdle machines" |
| SICA | 同上,自我改進的 coding agent | Same quadrant; self-improving coding agent | 字幕聽成 "Sika";全名待確認 / spelling of full name to verify |
| MiniMax harness | 會用自己生成的資料訓練的 harness | A harness that trains on some of its own generated data | 字幕聽成 "Miniax" |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Bodic / Poetic / PUDK | Poetiq |
| Darwin Girdle machines | Darwin Gödel Machine |
| Sika | SICA |
| Miniax harness | MiniMax harness |
| by dance | ByteDance |
| cloud / cloud code | Claude / Claude Code |
| Google Deep Mind | Google DeepMind |
| soda | SOTA (state of the art) |
| atom or SGD | Adam or SGD |

## 待確認 / To Verify

- **SICA** 的正確全稱與出處(字幕作 "Sika",語境為與 Darwin Gödel Machine 並列的便宜 RSI coding 系統)。/ Full name and source for "SICA".
- 投影片上的 benchmark 成績表細節(哪些 benchmark、用了哪些模型)——逐字稿只提到「一半用了更舊更便宜的模型」與「前紀錄通常是 Fable 5」。/ The specifics of the results table — the transcript only gives the aggregate claim.
- 「benchmarks are dead」blog post 的正確標題與連結。/ Exact title and URL of the "benchmarks are dead" post.
