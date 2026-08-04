---
title: "Opportunities and Challenges for Long-Horizon Agents"
title_zh: "長程 Agent 的機會與挑戰"
speaker: "Jerry Tworek"
affiliation: "CEO, Core Automation; Former VP of Research at OpenAI"
type: talk
stage: Plenary
date: 2026-08-01
session: "Session 3: Agentic AI Foundational Capabilities"
video: "https://www.youtube.com/watch?v=Tcn5Yb2K0h4&t=4245s"
video_range: "01:10:45–01:23:10"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [long-horizon-agents, reinforcement-learning, credit-assignment, value-functions, continual-learning]
---

# 長程 Agent 的機會與挑戰(Opportunities and Challenges for Long-Horizon Agents)

**一句話總結**:RL 之所以還沒把 agent 的工作時長從 12 小時推到 12 個月,不是因為錢不夠,而是因為單一 reward 配上長軌跡讓**學習訊號隨 horizon 平方衰減**,加上一天只跑得出兩個 gradient step——這才是長程 agent 真正的瓶頸,而 value function 與 continual learning 是兩條可能的出路。
**One-line summary**: What stops RL from pushing agents from 12 hours to 12 months isn't money — it's that a single reward over a long trajectory makes the **learning signal decay quadratically in horizon length**, compounded by getting only two gradient steps a day; value functions and continual learning are the two plausible ways out.

## 中文筆記

### TL;DR

- **問題的起點是一個很具體的觀察**:他自己 Codex session 的中位數大約 10 分鐘、平均約 20 分鐘。「為什麼不能更久?」——這是今天 AI 研究者最該問的問題之一。
- **我們才剛進入 agent 時代一年多**。他認為 **o3 是第一個真正 agentic 的模型**,去年四月才發布;模型自那時起進步巨大,但可改進的空間更大。
- **RL 解決了「軌跡越長、出錯機率指數上升」的老問題**:規模化 RL 後找到的配方讓模型能從自己的錯誤中恢復、在自己的軌跡上訓練,於是「想得越久、表現越好」——test-time compute 與 token maxing 的時代。今天最好的前沿模型讀數大約是**能連續工作 12 到 16 小時**。
- **但繼續砸錢不會自動延長到無限**,有兩個硬障礙:
  - **經濟學是平方級的**:採樣長度 n 的軌跡成本正比於 n(有 quadratic attention 還更高),而現代 RL 只給整條軌跡一個 reward、幾乎沒有 token 級的 credit assignment,所以**每個 token 拿到的資訊約 1/n**——學習訊號隨 horizon 平方衰減。線性還好,平方很殘酷。
  - **延遲**:採一條 12 小時軌跡就要 12 小時,一天做得出兩個 gradient step,一週約 14 個、一個月約 60 個。**這不是一個快的訓練方法,而現在沒有人有時間。**
- **今天的長程能力大多是 harness 黏出來的**(`/goal`、plan mode、sub-agents),而這些**不是模型原生的、無法被反向傳播、也沒有被訓練**——「機器學習的歷史一向是:能被 backprop 的東西會贏過不能的」。
- **兩條出路**:value function(如果有人做出來,長程問題就解了,但他抱持相當程度的懷疑——找到好的 value function 常常比解原問題還難)與 **continual learning**(從另一端解:七年的迴圈每天重跑,但每天跑的不是同一個模型)。

### 重點整理

#### 從「我的 Codex session 只有 10 分鐘」開始(約 01:10–01:12)

長程 agent 顯然是當下 AI 研究的前沿之一。他的切入點非常具體:**看自己 Codex session 的統計,中位數大約 10 分鐘,平均值大約 20 分鐘。為什麼不是更久?為什麼 agent 沒辦法幫我工作更長的時間?** 他認為這是今天 AI 研究者非常值得問的問題。

先說明顯的部分:**我們已經活在 agent 時代,但非常早期。** 在他心中,**o3 是第一個真正 agentic 的模型,而那是去年四月才發布的**——所以我們才剛進入 agent 時代一年多一點。模型很早期,自 o3 以來進步巨大,但**還有更多改進空間**;產品在進步、採用在來、很多事情都還沒搞清楚。而這正是這個美好時代給我們的機會:去把這些事情弄清楚,供後面幾十年的 agent 普及使用。

**什麼構成一個 agent?** 這是個很模糊的詞,他列了幾個組件:agent **使用工具**(因為 agent 應該能代表我行動);agent 多半是 **async** 的(我交代一件事,它就去做);agent 通常是 **goal-oriented**(你給高階目標,agent 把空白填起來);agent 通常**跨越長時間**工作(不是每五分鐘來回一次)。

#### RL 如何解掉「指數失敗率」(約 01:12–01:15)

一旦拉長 agent 的工作時間,就會撞上一個很明顯的觀察:**我們訓練的神經網路每一步都是機率性的、都會犯錯,所以隨著軌跡長度增加,出錯的機率是指數成長的。** 這正是多年來我們做不出 agent 的一大原因——神經網路會脫軌。這也是 RL 文獻裡的經典假設,以及**我們為什麼需要 RL**。

轉捩點發生在他和團隊**把 RL 規模化到越來越大的算力**時,終於找到一個配方,能訓練模型**從自己的錯誤中恢復、在自己的軌跡上訓練**——模型突然開始能解越來越難的任務。他們看到兩件事:

1. 顯而易見的:**投入越多算力,能力就在演算法圖上等比例提升**。
2. 更關鍵、也是近年機器學習最重要的心智轉變之一:**模型想得越久、花在任務上的 token 越多,表現就越好**。也就是說,RL 訓出來的模型不只沒有掉進「軌跡越長失敗率越高」的陷阱、能從中恢復,還能**有生產力地持續思考更久**。本質上:**軌跡越長,結果越好**。我們進入了 test-time compute 與 token maxing 的時代。

接著是那張大家都很熟的圖:**agent 能替我們工作多久**。自從開始規模化 RL,這條線不斷創新高,**今天最好的前沿模型讀數大約在 12 小時、16 小時**。

#### 為什麼「繼續砸錢」不會自動成立(約 01:15–01:18)

那問題來了:**也許就這樣了?我們有了 RL,它有效,砸很多錢繼續 scale,就能得到想要工作多久就多久的 agent?** 他的答案是:不幸的是有問題,我們還沒完成。

**障礙一:經濟學是平方級的。**
- 採樣一條長度為 n 的軌跡,成本大致正比於 n(有 quadratic attention 的話甚至更高一點,但先當作每個 token 成本固定、線性看待)。
- 但今天的 RL 演算法怎麼運作?**它給整條軌跡指派單一 reward**——現代 RL 幾乎沒有把 reward 分配到特定 token 的 credit assignment 方法。
- 所以你用一個 reward 涵蓋 n 個 token 的軌跡,**每個 token 得到的資訊量大約是 1/n,而這條軌跡的成本是 n**——**學習訊號隨著 horizon 長度平方衰減**。
- 如果是線性的,那還算合理:「要 agent 工作兩倍久,就多花兩倍錢」,這個交易可以接受。**但如果是平方的,就相當殘酷。** 大實驗室今天很擅長砸大錢訓練模型,但這個平方成本讓 scaling 比乍看之下困難得多。

**障礙二:延遲,而且更難。** 因為即使 AI 領域湧入越來越多投資,**沒有人有時間**。想像你要採一條 12 小時的 agent 軌跡:採樣就要 12 小時,然後你走一個 gradient step 去強化成功的軌跡,拿到更新後的權重,再採下一條 12 小時軌跡——**一天做得出兩個 gradient step,一週大約 14 個,一個月大約 60 個。這不是一個快的訓練方法。** 所以針對非常長的軌跡與長程思考做訓練,**比很多人以為的要難得多**。

#### 現在的長程能力,其實是 harness 黏出來的(約 01:18–01:19)

領域裡大部分的進展、以及我們之所以有能長時間思考的 agent,通常是因為**我們在模型上面套了某種 harness**:既然 agent 很擅長短程任務,而事實上**很多長程工作可以由一連串更小的事情成功地黏起來**。

- Codex 和 Claude Code 裡都有的 **`/goal`**——非常強大:我們設一個固定目標,模型盡可能跑久,然後回頭檢視自己、繼續做下去。
- 還有 **plan mode**、**sub-agents**,各式各樣的方式。

但關鍵在於:**這些都不是模型原生的,沒有被反向傳播,也沒有被訓練進去**——它們只是利用了模型處理短期目標的能力,再堆疊出更長的時間跨度。你可以做得很成功,**但機器學習的歷史一向是:能被 backprop 的東西,終究會贏過不能被 backprop 的東西。**

**Auto-research 就是現成的反例。** 幾乎每一次 auto-research rollout 的故事都是:**早期進展很快,越往後走就停滯、就卡住**。他說到目前為止,**用今天的模型還沒看過任何特別成功的 auto-research rollout**。研究本質上就是高度序列、長程的任務,而今天的模型很難把小尺度的思考黏成大尺度的研究專案——auto-research 正是最能看見這個侷限的地方。

#### 人類是怎麼學會長程的?(約 01:19–01:21)

他反過來問:**人類是怎麼掌握追求長程目標的?** 最有名的例子是 **Andrew Wiles 花了七年只做一件事——證明費馬最後定理**,而且成功了。**我們要怎麼訓練模型去做七年的專案?**

他順手問了 ChatGPT:人類是從哪個時刻開始發展長期規劃的?得到的答案是——從我們能做任何有意義的長期規劃至今,**大約經過 10,000 個世代的人類,期間大約有 1,200 億人**。所以也許答案就是:**10,000 個 gradient step、1,200 億條軌跡**,這就是讓長程規劃優化到人類水準所需要的量。而且**梯度下降比演化更 sample-efficient**,所以我們或許還有餘裕——這是值得思考、值得回頭檢視的事。

#### 兩條研究出路(約 01:21–01:23)

**(1) Value function。** 這絕對是能幫上忙的方向:**如果我們有了好的 AI research value function,會非常有幫助。** 但他也給了誠實的評估:在對大型語言模型做 RL 時,我們基本上**把 value function 丟掉了,而大家發現這樣也一樣有效**。Value function 是非常非常難的問題,他對這方面能有多少進展**抱持相當程度的懷疑**——**很多時候,找到一個好的 value function 比解掉你原本想解的問題還難**。但如果有人真的把 value function 搞定了,**那我們就沒問題了,想解多長的長程問題都可以。**

**(2) Continual learning。** 這是從另一端攻進同一個問題:**我們在迴圈中更新模型**。如果有一個七年的長迴圈——「來證明這個定理」——你每天重複同一件事,**但你不是用同一個模型在重複**:模型會在新資料上更新,每天學到東西、變得更好。他認為 **continual learning 很有機會把我們帶過這一關**。問題在於怎麼做——**這是一個未解問題,也是一個值得解的問題。**

#### 收尾:值得投入的方向(約 01:22–01:23)

如果你在找「此時此刻該做什麼研究」,他認為**長程 agent 絕對是有效選項之一**。當我們拿到這項技術,就能**讓 agent 去解困難的研究問題,也能讓 agent 去經營公司**——那是非常長程、也非常有經濟價值的任務。而從使用者的角度:**如果我要把事情委派給一個 agent,我不想每 30 分鐘就得告訴它該做什麼;我要它能長時間代表我行動。**

研究還沒做完,還有非常多工作要做,而目標是:**能為我們持續跑下去、並隨時間持續變好的 agent。**

### 金句

> "If I look at my Codex session, my median is around 10 minutes. If I look at the mean, it's around 20. Why is it not more?"(約 01:10)

整場演講從一個極其具體的個人統計出發。

> "o3 was the first really agentic model, and that model was released in April last year. So we are just barely more than a year in the era of agents."(約 01:11)

給這個時代一個明確的起算點。

> "You get one reward for a trajectory of n tokens … which means your learning signal decays quadratically in the length of your trajectory."(約 01:16)

長程 agent 最核心的技術障礙,一句話說完。

> "You were able to do full two gradient steps in a day. … That means like 60 gradient steps a month. It is not a very fast training method."(約 01:17)

延遲問題比成本問題更難繞過。

> "The history of machine learning has always been that whatever we can back propagate through wins with things that we cannot."(約 01:18)

對「用 harness 黏出長程能力」這條路的長期判決。

> "Very often finding a good value function is much harder than solving the problem we are trying to solve."(約 01:21)

他對 value function 路線保持懷疑的理由。

## English Notes

### TL;DR

- **The talk starts from a very concrete observation**: his own Codex sessions have a median of about 10 minutes and a mean of about 20. "Why is it not more?" is, he argues, one of the most worthwhile questions for AI researchers today.
- **We are barely a year into the era of agents.** In his view **o3 was the first genuinely agentic model**, released last April; models have improved vastly since, with far more still to come.
- **RL solved the old "failure probability grows exponentially with trajectory length" problem.** Scaling RL produced a recipe that lets models recover from their own mistakes and train on their own trajectories, so *the more the model thinks, the better it performs* — the test-time-compute and token-maxing era. Today's best frontier readouts land around **12 to 16 hours of continuous work**.
- **But throwing more money at it doesn't extend that indefinitely.** Two hard barriers:
  - **The economics are quadratic.** Sampling a length-*n* trajectory costs ~*n* (more with quadratic attention), while modern RL assigns a single reward to the whole trajectory with essentially no token-level credit assignment — so **information per token is ~1/n** and the learning signal decays quadratically in horizon. Linear would be fine; quadratic is brutal.
  - **Latency.** Sampling a 12-hour trajectory takes 12 hours, so you get two gradient steps a day, ~14 a week, ~60 a month. **That is not a fast training method, and nobody has time.**
- **Today's long-horizon behavior is mostly glued together by the harness** (`/goal`, plan mode, sub-agents) — none of it native to the model, backpropagated through, or trained. "Whatever we can backpropagate through wins over what we cannot."
- **Two ways out**: value functions (if someone cracks them, long horizons are solved — but he's skeptical, since finding a good value function is often harder than solving the original problem) and **continual learning** (attacking from the other side: run the seven-year loop daily, but not with the same model each day).

### Key Points

#### Starting from "my Codex sessions are only 10 minutes" (~01:10–01:12)

Long-horizon agents are clearly one of the frontiers of AI research right now, and his way in is unusually concrete: **the median of his Codex sessions is around 10 minutes, the mean around 20. Why is it not more? Why aren't agents working for him for longer?** He thinks that is a very worthwhile question for AI researchers to be asking today.

Start with the obvious: **we already live in the era of agents, but we are very early in it.** In his mind **o3 was the first really agentic model, and it was released only last April** — so we are just barely more than a year in. The models are early; they have improved vastly since o3, and **there are much larger improvements still to be had.** Products are improving, adoption is coming, and a lot is not figured out — which is the opportunity these times hand us, for the decades of agent proliferation ahead.

**What makes an agent an agent?** A fuzzy term, but his pieces: agents **use tools**, because an agent should be able to act on your behalf; agents are most likely **async** — you tell it something and it goes off and does the work; agents are usually **goal-oriented**, where you specify something high-level and the agent fills in the blanks; and agents work **over long horizons of time**, not back-and-forth every five minutes.

#### How RL dissolved the exponential-failure problem (~01:12–01:15)

Extend the time an agent works and you hit an obvious observation: **the neural networks we train are probabilistic at every step and they make failures, so the chance that something goes wrong grows exponentially with trajectory length.** That was a very big reason we couldn't have agents for many years — the networks got off the rails. It's the classical assumption from the RL literature, and **the reason we need reinforcement learning at all.**

The moment came when he and his team **scaled RL to larger and larger amounts of compute** and finally found a recipe that trained models **to recover from their own mistakes and train on their own trajectories** — and suddenly the models started succeeding at harder and harder tasks. Two things followed:

1. The obvious one: **spend more compute, and capability improves proportionally** on the algorithmic plot.
2. The important one, and one of the biggest shifts in machine learning in recent years: **the more the model thinks — the more tokens it spends on a task — the better performance gets.** RL-trained models not only avoided the exponentially-increasing failure trap and learned to recover from it, they could **keep thinking productively for longer and longer.** Essentially: **the longer your trajectory, the better your results.** We entered the era of test-time compute and token maxing.

Then comes the plot everyone thinking about agents knows: **how long agents can work for us.** Since RL scaling began it keeps reaching new heights, with **the latest readouts around 12 hours, 16 hours for some of the best frontier models today.**

#### Why "just keep spending" doesn't carry you (~01:15–01:18)

So maybe this is it — we have RL, it works, throw a lot of money at it and get agents that work for whatever length of time we want? Unfortunately there are problems. We are not done.

**Barrier one: the economics are quadratic.**
- Sampling a trajectory of length *n* costs roughly proportional to *n* (slightly more with quadratic attention, but treat per-token cost as fixed for a second).
- But how do today's RL algorithms work? **They assign a single reward for that trajectory.** There aren't really any credit-assignment methods in modern RL that attribute that reward to specific tokens.
- So one reward covers a trajectory of *n* tokens, meaning **information per token is roughly 1/n while the trajectory costs n** — **your learning signal decays quadratically in the length of your horizon.**
- If it were linear, that would be pretty okay: to train agents to work twice as long, spend twice as much money. That's a reasonable trade. **Quadratic is brutal.** The big labs today are very good at spending a lot of money training models, but the quadratic cost makes scaling considerably harder than it looks at first sight.

**Barrier two: latency, which is even harder.** For all the investment flowing into AI, **no one has time.** Imagine sampling a 12-hour agent trajectory: it takes 12 hours, then you take a gradient step to reinforce the successful trajectories, then you sample another 12-hour trajectory. **Two full gradient steps in a day. Roughly 14 a week. Roughly 60 a month. That is not a very fast training method.** Training for very long trajectories and long-horizon thinking is meaningfully harder than many realize.

#### Today's long horizons are harness-glued (~01:18–01:19)

Most of the progress in the field — and the reason we have agents that can think for a long time at all — usually comes from **putting some kind of harness on top of the model.** Agents are very good at short-horizon tasks, and the truth is that **a lot of long-horizon work can be glued together very successfully from smaller things.**

- **`/goal`** in Codex and in Claude Code is very powerful: fix a goal, the model runs for however long it can, revisits itself, and continues.
- There's also **plan mode**, **sub-agents**, and various other ways.

The catch: **none of this is native to the model. It is not backpropagated through. It is not trained.** These mechanisms merely exploit the model's ability to work on short-term goals and stack them into longer spans. You can be very successful this way — **but the history of machine learning has always been that whatever we can backpropagate through wins over the things we cannot.**

**Auto-research is the ready-made counterexample.** The story of almost every auto-research rollout is that **you get a lot of progress pretty early, and then further along it stalls and stops.** He hasn't yet seen any particularly successful auto-research rollout with today's models. Research is inherently a hard-serial, long-horizon task, and today's models can't easily glue short-horizon thinking into larger-scale research projects — auto-research is exactly where you see it.

#### How did humans master long horizons? (~01:19–01:21)

He inverts the question. Famously, **Andrew Wiles spent seven years working on a single goal — proving Fermat's Last Theorem — and succeeded.** How do we train models to do seven-year projects?

He asked ChatGPT when humans started developing long-term planning, and got: roughly **10,000 generations of humans** since we could do any significant long-term planning, and roughly **120 billion people** in that time. So maybe that's it — **10,000 gradient steps and 120 billion trajectories** is what it takes to optimize long-horizon planning as well as humans do. And **gradient descent is more sample-efficient than evolution**, so perhaps we have even more room. Something to think about and revisit.

#### Two research directions (~01:21–01:23)

**(1) Value functions.** Definitely a direction that can help: **if we got good value functions for AI research, it would be extremely helpful.** But he is honest about the state of things: when doing RL on large language models we basically **threw out value functions, and everyone saw it works just as well.** Value functions are a very, very hard problem, and he holds **a fair amount of skepticism** about how much progress can be made — **very often, finding a good value function is much harder than solving the problem you were trying to solve.** But if someone figures out value functions, **we're good: we can solve long-horizon problems as long as we'd like.**

**(2) Continual learning.** This attacks the same problem from the other side: **update the model through the loop.** If you have a long, seven-year loop — "let's prove this theorem" — you repeat the same thing every day, **but not with the same model**: the model updates on new data, learns something each day, and improves. He thinks **continual learning could get us through this very well.** The question is how — **it is an unsolved problem, and one worth solving.**

#### Closing: worth working on (~01:22–01:23)

If you're looking for what to work on right here and now in this age of machine learning, **long-horizon agents is absolutely one of the valid choices.** When we get that technology we'll be able to **put agents to work on hard research problems, and have them run companies** — very long-horizon and very economically valuable tasks. And from the user's side: **if I want to delegate to an agent, I don't want to be telling it what to do every 30 minutes; I want it acting on my behalf for long periods of time.**

The research isn't done. There's much work to do, and the objective is **agents that can keep going for us and keep getting better over time.**

### Quotes

> "If I look at my Codex session, my median is around 10 minutes. If I look at the mean, it's around 20. Why is it not more?" (~01:10)

The whole talk grows out of one personal statistic.

> "o3 was the first really agentic model, and that model was released in April last year. So we are just barely more than a year in the era of agents." (~01:11)

A dated starting line for the era.

> "You get one reward for a trajectory of n tokens … which means your learning signal decays quadratically in the length of your trajectory." (~01:16)

The core technical barrier for long-horizon agents, in one sentence.

> "You were able to do full two gradient steps in a day. … That means like 60 gradient steps a month. It is not a very fast training method." (~01:17)

Latency is harder to engineer around than cost.

> "The history of machine learning has always been that whatever we can back propagate through wins with things that we cannot." (~01:18)

His long-run verdict on harness-glued long-horizon behavior.

> "Very often finding a good value function is much harder than solving the problem we are trying to solve." (~01:21)

Why he stays skeptical of the value-function route.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| o3 | 他認為的第一個真正 agentic 的模型,2025 年 4 月發布 | In his view the first genuinely agentic model, released April 2025 | 用來標定 agent 時代的起點 / used to date the era of agents |
| Codex | OpenAI 的 coding agent;他用自己的 session 統計開場 | OpenAI's coding agent; his own session stats open the talk | median ~10 min / mean ~20 min |
| `/goal` | Codex 與 Claude Code 皆有的指令:設定固定目標,模型持續跑並自我回檢 | Slash command in both Codex and Claude Code: fix a goal, the model runs and revisits itself until done | harness 層的長程機制,非模型原生 / harness-level, not native to the model |
| Plan mode / sub-agents | 其他把短程能力堆成長程的 harness 手法 | Other harness techniques stacking short-horizon ability into long horizons | 同樣不被 backprop / likewise not backpropagated through |
| Andrew Wiles / 費馬最後定理 | 人類長程目標的代表案例:七年單一目標 | The canonical human long-horizon case: seven years on one goal | 用來提問「怎麼訓練七年專案的模型」 / framing the seven-year-project question |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Jerry Tore / Tvorek | Jerry Tworek |
| 03 | o3 |
| codec session / codeex | Codex session / Codex |
| cloud code | Claude Code |
| slashgoal | `/goal` |
| Andrew wild | Andrew Wiles |
| fermatas theorem | Fermat's Last Theorem |
| Chad GPT | ChatGPT |
| the mold / malls(panel 段) | the model / models |
| analytical things(panel 段) | unethical things(推測 / inferred) |

## 待確認 / To Verify

- 「120 trajectories」:上下文為「10,000 個世代、1,200 億人」,對應的應是 **120 billion trajectories**,字幕疑似漏掉 "billion"。/ The transcript says "120 trajectories" where the context (10,000 generations, 120 billion people) implies **120 billion trajectories** — "billion" appears to have been dropped.
- 「12 小時、16 小時」的 agent 工作時長讀數出自投影片上的圖(疑似 METR 式的 time-horizon 曲線),來源未在口頭點名。/ The 12h/16h readouts come from a slide (apparently a METR-style time-horizon curve); the source was not named aloud.
- 演講中未點名的「plot a lot of people thinking about agents are very familiar with」具體出處。/ The specific provenance of the widely-known time-horizon plot he referenced.
- panel 段他說 "the mold can do analytical things to get reward",語意上應為 unethical/unintended,字幕不清。/ In the panel he says "the mold can do analytical things to get reward"; semantically this should be unethical/unintended — captions unclear.
