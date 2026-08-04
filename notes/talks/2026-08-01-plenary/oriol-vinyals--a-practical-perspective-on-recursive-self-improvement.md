---
title: "A Practical Perspective on Recursive Self-Improvement"
title_zh: "遞迴自我改進的實務觀點"
speaker: "Oriol Vinyals"
affiliation: "VP of Research, Google DeepMind; Gemini tech lead"
type: talk
stage: Plenary
date: 2026-08-01
session: "Session 3: Agentic AI Foundational Capabilities"
video: "https://www.youtube.com/watch?v=Tcn5Yb2K0h4&t=2577s"
video_range: "00:42:57–00:59:03"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [recursive-self-improvement, agents, evaluation, ideation, reinforcement-learning]
---

# 遞迴自我改進的實務觀點(A Practical Perspective on Recursive Self-Improvement)

**一句話總結**:把 RSI 拆成「ideation → implementation → experimentation → evaluation」的研究迴圈後會發現,全世界的努力幾乎都堆在中間兩格,而卡住 RSI 的其實是最外面兩格——評估很難、發想更難,所以 RSI 大概不會像大家想的那麼快到來。
**One-line summary**: Decompose recursive self-improvement into the research loop — ideation, implementation, experimentation, evaluation — and it becomes clear that nearly all current effort sits in the middle two boxes, while the two hard outer ones (evaluation and ideation) are what actually gate RSI; which is why it will likely arrive slower than people expect.

> 議程未列此場講題,標題依演講內容自擬(見「待確認」)。/ The agenda listed no title for this talk; the title above is derived from its content (see "To Verify").

## 中文筆記

### TL;DR

- **Agent 的定義被重新洗牌了**:古典 RL 是「agent ↔ environment」兩個分離的方塊;今天環境和 agent 已經難以拆開,環境是 agent harness 跑在上面的那台機器(且常與使用者共享),腦是 LLM。
- **SI 與 RSI 的實用定義**:self-improvement 是使用者給一個 spec、系統跑數小時到數天、朝一個 fitness function 前進;recursive 只是再多一步——把 harness 程式碼與模型權重本身也視為環境的一部分,允許被修改。
- **現況**:自我改進的例子很多,「真正有影響力的 RSI 例子還沒看到」。
- **瓶頸在兩端**:研究迴圈的四格中,implementation 與 experimentation(coding agent 的強項)進展飛快,ideation 與 evaluation 幾乎原地踏步。
- **評估要往「怎麼改進的」走**:從代理指標(SWE-Bench Pro、MLE-bench、held-out perplexity)→ 直接評估 RSI 能力(PostTrainBench 這類)→ 再進一步評估「用什麼方式達成」:不要作弊,要看到創造力。
- **潑冷水的四個理由**:evaluation 難、ideation 難、物理限制(晶片速度、光速)、以及人類水準本身可能已接近漸近線——「better doesn't mean better」。

### 重點整理

#### 從電玩到「環境長在 agent 裡面」(約 00:43–00:46)

DeepMind 做 agent 做了十幾年,因為 RL 本來就是用 agent 定義自己的。傳統那張圖很單純:agent 與 environment 交換 observation 與 action,agent 由一個神經網路驅動,observation / action 空間固定,環境是電玩。當年常被質疑「遊戲不是真實世界」,但事後看這條技術路線影響巨大;而遊戲有個很好的性質——**它比我們今天的 sandbox 還要更徹底地被隔離**。他們就這樣一路測到 Go、StarCraft,直到「把最複雜的遊戲都打完、沒遊戲可打了」。

今天這張圖被重新洗牌,最深刻的一點是:**環境已經很難跟 agent 拆開,所以他直接把環境畫進 agent 裡面**。環境是一台可能連著網路的機器,agent harness 跑在上面,腦換成大型語言模型——結構上其實和當年那張「為某個遊戲專門訓練的神經網路」沒差多少,但互動的緊密程度已經無法切割。另外和過去不同的是:多了一個會跟 agent 互動的使用者(寫程式、丟一個要跑很久的難題),而且**環境常常和使用者共享**——可能就是你自己那台機器,也可能是雲端 spawn 出來的虛擬機。

#### SI 與 RSI 的實用定義(約 00:46–00:49)

他刻意用這個 agent 的鏡頭來定義 self-improvement 與 recursive self-improvement,因為兩者其實沒差很遠:

- **Self-improvement**:相較於 agent,使用者的互動性低很多。使用者給一個 spec,系統就自己跑幾小時甚至幾天;關鍵是有一個 **fitness function / improvement target**(例如當天早上有人示範的 Tetris 分數)。他強調「這跟 agent 幾乎只差在細節」。
- **Recursive**:再往前想一步——**agent harness 本身的程式碼、甚至 agent 背後的那顆(或那組)LLM,都可以被修改**。這些東西 trivially 可以視為環境的一部分:harness 的程式碼、以及那個你可以上傳到 server 去服務 token 的模型物件。所以 recursive 就是允許環境與 harness 修改自己或修改模型。

值得區分兩個改進空間:**harness space**(compaction 怎麼做、有哪些工具可用等實作細節)與**模型權重本身**(從頭重寫、或 fine-tune)。RSI 的 action space 就是「任何會改動那個物件的動作」。

他的判斷很直白:**真正有影響力的 RSI 例子還沒出現;self-improvement 的例子則已經很常見**。但這件事一定會來,而且對「前沿實驗室自己怎麼做研究、怎麼開發 harness 與 LLM」有很深的後果。

#### 研究迴圈的四格,以及大家都擠在中間兩格(約 00:49–00:51)

要問「一個有腦的 agent 要怎麼做 RSI」,不妨戴上研究者的帽子:一個全能的 RSI 系統要走的流程,和我們多年來為了發論文、推廣技術而玩的那套遊戲沒什麼兩樣。他拆成四格:

1. **Ideation**:吸收所有既有工作與領域知識,判斷哪些想法根本上值得追——這是很重要的推理步驟。
2. **Implementation**:把想法實作出來,可能複雜也可能簡單。
3. **Experimentation**:跑程式、遇到 bug、不 work,可能堅持下去、也可能放棄回頭換想法。
4. **Evaluation**:評估發生了什麼、ideation 階段形成的假設是否被驗證。傳統上接著寫論文,RSI 系統則直接繞回去再跑一圈。

**關鍵觀察:現在絕大部分的努力集中在中間兩格。** Coding agent 有多強大家都知道,implementation 與 experimentation(編譯、除錯、跑實驗)的進展與熱情都很高——這一段大概也因為最貼近使用者互動,所以更像 self-improvement 而非 recursive self-improvement。**另外兩格則遠遠落後。**

#### Evaluation:三個層次(約 00:51–00:55)

他特別花時間講評估,因為他認為社群長期低估了 evaluation 與 data(當年提出新資料集的論文甚至會被視為「應用」而不值得上大會)。要「用比較科學的方式衡量進展」,有三種做法:

**(1) 代理能力 benchmark + hill climbing**——挑一些被認為重要的能力與 benchmark(SWE-Bench Pro、MLE-bench、pre-training 的 held-out perplexity),然後拚命爬坡,期待 RSI 自己 emerge。
- 優點:這正是這幾年訓 LLM 的方式;評估便宜、定義清楚。
- 缺點:**對「真正會不會發展出 RSI」是非常間接的量測**;還有 overfitting 與作弊問題;而且現有 eval 大多只涵蓋中間那兩格。

**(2) 直接評估 RSI 能力本身**——已經有 benchmark 開始出現,例如 **PostTrainBench**(他也提到 Dawn Song 跟他講了另一個,近幾週到幾個月會陸續冒出來)。做法是把評估設計成「內迴圈本身」:給 agent 一個指標、給幾次嘗試,看它能改進多少。
- 優點:量到我們真正在乎的東西,也就是自我改進能力本身。
- 缺點:**現在很貴**(你真的得讓 agent 跑一段時間);而且內迴圈優化的往往是 Tetris 之類的目標,和真正在乎的「幫我把整個前沿實驗室自動化、做出世界最好的模型」相比,**這些評估以今天的形式可能有點 out of distribution**。

**(3) 不只評估改進多少,還要評估「怎麼改進的」**——這是他預期領域會越來越往那走的方向:除了「三小時算力下 Tetris 進步多少」,還要看**沒有作弊、有創造力、展現出某些智能面向**,用比較容易評估的強力 reward model 來打分。

#### Ideation:最被低估、也最難自動化的一格(約 00:55–00:57)

以 ideation 為例:想法要怎麼評估?當你是研討會審稿人,你在找的是 **research taste、novelty、efficiency、elegance、這個技術是否經得起時間考驗**。你可以想像用這幾條寫一些規則、去評估一個 RSI agent 在 ideation 階段的行為——但**現在非常難,而且極度缺乏研究**。要把這條路走通、把自動推理做到可以用 RL 在上面優化,還需要不少時間。

而且說實話,**人類自己也沒多好**:我們有非常昂貴的研討會與審稿流程,但 Transformer 花了好幾年才變成主流;現在越來越紅的 distillation,當年投稿的那個會議直接把它拒了,靠著某種隨機過程過了好幾年才重新被看見「這東西其實有用」。他順帶調侃:在場每個人大概都有一篇自己的「事後看應該要上的酸苦被拒論文」故事——而這正是我們自己設計出來的那套昂貴流程幹的。

#### 遊戲會被玩壞:reward hacking 的老朋友(約 00:57)

他把遊戲拉回來當例子:agent 用和我們預期不同的方式達成目標,並不令人意外——有幾款很有名的遊戲就是被這樣鑽了漏洞。**這件事我們已經看了很多年。**

#### 收尾:RSI 會很猛,但可能沒那麼快(約 00:57–00:59)

- **樂觀面**:RSI 對某些工程與科學任務,**很可能把進展速度拉快 10 倍甚至更多**。
- **要小心的**:目標怎麼設、misalignment、資源重新配置、以及**實驗室的運作方式可能因此改變**——每一步都得走得謹慎。
- **四個「沒那麼快」的理由**:
  1. Evaluation 很難。
  2. Ideation 很難。
  3. **物理限制**:晶片不可能跑得比設計上限更快,連光速——資料在晶片之間傳輸——都是限制。
  4. **人類水準本身可能已接近漸近線**:加上 RSI 也不見得看得到劇烈提升。AlphaGo 相對於「完美的圍棋」到底還差多少?不清楚。另一個例子更貼身:**現在這些模型寫作好到有點惱人,你反而得叫它寫差一點**——所以在某些領域,「更好」不一定真的是更好。

### 金句

> "The environment is hard to disentangle from the agent. So I put the environment inside of the agent."(約 00:45)

古典 RL 那張「agent 與 environment 各一個方塊」的圖,在 agentic 時代已經畫不出來了。

> "I don't think we've seen very impactful actual recursive self-improvement examples yet. Certainly many self-improvement examples."(約 00:48)

RSI 目前還是預期,不是既成事實。

> "Currently a lot of effort is done in the middle two boxes."(約 00:50)

整場演講的核心診斷:大家在做的是實作與實驗,不是發想與評估。

> "It might not come as fast as we thought it would, because first evaluation is very hard and ideation is also very hard."(約 00:57)

來自前沿實驗室內部的降溫發言。

> "Sometimes it's kind of annoying how well these models write and you have to make it look a little bit worse. … Better doesn't mean better."(約 00:58)

有些維度上,人類水準已經是天花板附近,再往上走的邊際價值可能是負的。

## English Notes

### TL;DR

- **The definition of "agent" has been reshuffled.** Classic RL drew agent and environment as two separate boxes; today the environment is so entangled with the agent that Vinyals draws it *inside* the agent — a machine (often shared with the user) running the harness, with an LLM as the brain.
- **Practical definitions**: self-improvement means a user hands over a spec, the system runs for hours or days with little interaction, and optimizes some fitness function. *Recursive* adds one step — the harness code and the model weights themselves count as part of the environment and become modifiable.
- **Status check**: plenty of self-improvement examples exist; "I don't think we've seen very impactful actual recursive self-improvement examples yet."
- **The bottleneck sits at both ends** of the research loop. Implementation and experimentation — coding agents' home turf — are racing ahead; ideation and evaluation have barely moved.
- **Evaluation should move toward measuring *how*, not just *how much***: proxy benchmarks (SWE-Bench Pro, MLE-bench, held-out perplexity) → benchmarks that measure RSI directly (PostTrainBench and friends) → evaluating the manner of improvement, rewarding creativity and penalizing cheating.
- **Four reasons to expect RSI later than the hype suggests**: evaluation is hard, ideation is hard, physical limits (chip speed, speed of light), and human-level performance may already be near an asymptote — "better doesn't mean better."

### Key Points

#### From video games to an environment that lives inside the agent (~00:43–00:46)

DeepMind has been building agents for over a decade, largely because reinforcement learning defines what an agent *is*. The traditional picture was simple: an agent and an environment exchanging observations and actions, the agent powered by a neural net, with fixed observation and action spaces and video games as the environment. The perennial objection was "games aren't the real world," but hindsight says otherwise — and games had one lovely property: **they were sandboxed even more thoroughly than the sandboxes we build today.** They tested on Go, StarCraft and the rest, until "we ran out of games."

Today's picture is reshuffled. The most profound change: **the environment is hard to disentangle from the agent, so he draws the environment inside it.** The environment is a machine, probably with network access, running an agent harness whose brain is an LLM — structurally not that different from the old game-specific neural net, except the interaction is now too tight to separate. Two other changes: a user is now in the loop (coding, or handing over a hard question that runs for a while), and **the environment is often shared with that user** — your own machine, or virtual machines spawned in the cloud.

#### Self-improvement and recursive self-improvement, defined through that lens (~00:46–00:49)

- **Self-improvement** is a nuance on what agents already do. The user is far less interactive: hand over a spec, the process runs for hours or days. Critically there is a **fitness function or improvement target** — the Tetris score demoed that morning being one example. "It's almost a detail" that separates this from an agent.
- **Recursive** is one step further: **the harness code that runs the agent, and the LLM (or set of LLMs) behind its actions, can also be modified.** Both are trivially part of the environment — the harness source, and the model as an object you can upload to whatever serves your tokens. Recursion is simply permitting the environment and harness to modify themselves or the model.

Two improvement spaces are worth distinguishing: **harness space** (compaction, available tools, all the implementation detail) and **the model weights** (rewritten from scratch, or fine-tuned). The action space for recursion is anything that modifies that object.

His read: **no impactful RSI examples yet; plenty of self-improvement ones.** But it is coming, with deep consequences for how frontier labs do the research that produces harnesses and LLMs in the first place.

#### The four-box research loop, and why everyone is crowded into the middle (~00:49–00:51)

To think about how a brain-equipped agent would recursively self-improve, put on a researcher's hat: the process a fully capable RSI system must run is not that different from the game many of us have played for years — publish papers, get techniques adopted. Four boxes:

1. **Ideation** — absorb the prior work, decide which ideas are fundamentally worth pursuing. A crucial reasoning step.
2. **Implementation** — actually build the idea, simple or complex.
3. **Experimentation** — run the code, hit bugs, it doesn't work; persist, or give up and go back to another idea.
4. **Evaluation** — judge what happened and whether the hypothesis from ideation held. Traditionally you then write a paper; an RSI system just loops.

**The observation that anchors the talk: almost all current effort sits in the middle two boxes.** Everyone knows how powerful coding agents have become, so implementation and experimentation (running, compiling, debugging) attract both progress and enthusiasm — probably because that stage is the most interactive with the user, which makes it more self-improvement than recursive self-improvement. **The outer two boxes lag badly.**

#### Evaluation, in three tiers (~00:51–00:55)

He dwells on evaluation because the community has under-weighted evaluation and data for years — proposing a new dataset used to be dismissed as "an application," not worth a top conference. Three ways to measure progress scientifically:

**(1) Proxy capability benchmarks plus hill climbing.** Pick capabilities you believe matter and benchmarks for them — SWE-Bench Pro, MLE-bench, held-out perplexity in pre-training — then climb, hoping RSI emerges.
- Pros: exactly how LLMs have been trained for years; cheap and well-defined.
- Cons: **a very indirect measurement of whether a system will truly develop RSI**; overfitting and cheating; and today's evals mostly cover only the middle two boxes.

**(2) Evaluate the capability we actually care about — RSI itself.** Benchmarks are appearing as the topic gains traction: **PostTrainBench** is one example, and Dawn Song told him about another; expect more over the coming weeks and months. The design is deliberately meta — the evaluation *is* an inner loop: give the agent a metric, a few tries, and measure how much improvement it gets.
- Pros: measures the self-improvement capability directly.
- Cons: **expensive right now** — you literally have to run an agent for a while; and the inner-loop metric is usually something like Tetris, whereas the production question is "automate my whole frontier lab and produce the best model in the world," so **these evaluations may be somewhat out of distribution as they stand.**

**(3) Evaluate *how* the improvement was achieved.** The direction he expects the field to move: not just "how much better at Tetris in three hours of compute" but **no cheating, visible creativity, certain aspects of intelligence** — scored by powerful reward models that are more tractable to evaluate.

#### Ideation: the most underexplored box (~00:55–00:57)

Take ideation as the concrete case. How do you evaluate an *idea*? As a conference reviewer you look for **research taste, novelty, efficiency, elegance, whether the technique will stand the test of time.** You can imagine writing rules against a few of these and automating the scoring of an RSI agent's ideation behavior — but **it is very hard today and severely understudied.** Getting there, and getting the automated reasoning good enough to optimize on top of with RL, will take real time.

And honestly, **humans aren't that good at it either.** We run very expensive conference and review processes, yet Transformers took years to become mainstream, and distillation — increasingly famous now — was rejected from the conference they submitted it to, resurfacing years later through something like a random process. Everyone in the room, he notes, has their own sour story of a rejected paper that in hindsight should have been accepted by this expensive apparatus we built for ourselves.

#### An old friend: agents exploiting the game (~00:57)

He brings games back for one slide: it should surprise no one that agents do things a little differently than we expect. Several famous games have been exploited in unintended ways. **We've been watching this coming for many years.**

#### Closing: enormous, but probably slower than you think (~00:57–00:59)

- **The upside**: RSI will likely increase the speed of progress on certain engineering and science tasks **by 10x or more**.
- **The caution**: be mindful of how goals are set, of misalignment, of resource reallocation, and of the fact that **how labs are run may itself change**.
- **Four reasons it may not arrive as fast as expected**:
  1. Evaluation is very hard.
  2. Ideation is very hard.
  3. **Physical constraints** — chips can't run faster than they're designed to, and even the speed of light bounds how fast data moves around a chip.
  4. **Human performance may already be close to an asymptote**, so adding RSI may not yield a drastic improvement. How good is AlphaGo relative to a perfect game of Go? Unclear. A more everyday example: **these models write so well it's become annoying, and you have to make the output look a little worse.** In some domains, better doesn't mean better.

### Quotes

> "The environment is hard to disentangle from the agent. So I put the environment inside of the agent." (~00:45)

The classic two-box RL diagram no longer survives contact with agentic systems.

> "I don't think we've seen very impactful actual recursive self-improvement examples yet. Certainly many self-improvement examples." (~00:48)

RSI is still a forecast, not a fact on the ground.

> "Currently a lot of effort is done in the middle two boxes." (~00:50)

The diagnosis the whole talk hangs on.

> "It might not come as fast as we thought it would, because first evaluation is very hard and ideation is also very hard." (~00:57)

A cooling note from inside a frontier lab.

> "Sometimes it's kind of annoying how well these models write and you have to make it look a little bit worse. … Better doesn't mean better." (~00:58)

On some axes we're already near the ceiling, and the marginal value of going further may be negative.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| SWE-Bench Pro | 長程軟體工程任務 benchmark,被當作 RSI 的代理指標之一 | Long-horizon software engineering benchmark, cited as an RSI proxy metric | Scale AI 發布 / released by Scale AI |
| MLE-bench | 以 Kaggle 競賽為題的機器學習工程 agent benchmark | ML-engineering agent benchmark built from Kaggle competitions | OpenAI 發布 / released by OpenAI;字幕聽成 "MLB bench" |
| PostTrainBench | 直接評估「agent 能否自動化 LLM post-training」的 benchmark | Benchmark measuring whether LLM agents can automate LLM post-training | 演講中作為「直接評估 RSI」的代表例 / cited as the direct-RSI-evaluation example |
| AlphaGo | 用來說明「人類水準可能已接近漸近線」的例子 | Invoked to illustrate that human-level may already be near an asymptote | DeepMind |
| Distillation(知識蒸餾) | 用來說明人類審稿機制對好想法的誤判 | Used as the example of human review misjudging a good idea (it was rejected) | Vinyals 本人為原論文共同作者 / he co-authored the original paper |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Oriel Vignyals / Oral | Oriol Vinyals |
| Google DeepMine | Google DeepMind |
| MLB bench | MLE-bench |
| SWE pro | SWE-Bench Pro |
| post train bench | PostTrainBench |
| Don | Dawn (Song) |
| tetric / tetries | Tetris |
| asymto | asymptote |
| overfeitting | overfitting |
| ideiation | ideation |
| Europe's 2027(panel 段) | NeurIPS 2027 |

## 待確認 / To Verify

- **講題**:官網議程未列此場標題,本檔標題「A Practical Perspective on Recursive Self-Improvement」為依內容自擬,非官方名稱。/ The agenda lists no title; the one used here is derived from content, not official.
- 他提到 Dawn Song 告訴他「另一個」直接評估 RSI 的 benchmark,未點名;可能是 Dawn Song 演講中的 Agents' Last Exam 或 AgentBeats,但講者未明說。/ The unnamed second RSI benchmark Dawn Song told him about — possibly Agents' Last Exam or AgentBeats from her talk, but he did not say.
- 「幾款很有名的遊戲被 agent 鑽漏洞」的具體遊戲名稱,投影片有影片但字幕未帶出名稱。/ The specific games shown in the reward-hacking slide (video played, names not spoken).
- distillation 被拒的確切會議與年份,講者只說「the conference we submitted at」。/ The exact venue and year distillation was rejected from — he only said "the conference we submitted at."
