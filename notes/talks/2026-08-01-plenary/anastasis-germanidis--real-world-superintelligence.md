---
title: "Real-World Superintelligence"
title_zh: "真實世界的超級智慧"
speaker: "Anastasis Germanidis"
affiliation: "Co-Founder/Co-CEO, Runway"
type: talk
stage: Plenary
date: 2026-08-01
session: "Session 4: Robotics & World Models"
video: "https://www.youtube.com/watch?v=Tcn5Yb2K0h4&t=10070s"
video_range: "02:47:50–03:01:25"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [world-models, video-generation, robotics, simulation, evaluation]
---

# 真實世界的超級智慧(Real-World Superintelligence)

**一句話總結**:數學與程式碼之所以進步神速,是因為我們有可以無限便宜地跑 rollout 的沙盒;真實世界沒有,而影片是最通用的那個沙盒——所以 Runway 的路線是「用預測下一幀來預測世界」,再把它變成即時、可互動、以動作為條件的學習型模擬器。
**One-line summary**: Math and code advanced so fast because we have sandboxes where rollouts are effectively free; the real world has none, and video is the most general candidate — so Runway's bet is to predict the world by predicting the next frame, then turn that into a real-time, interactive, action-conditioned learned simulator.

## 中文筆記

### TL;DR

- **落差的成因是沙盒,不是智力**:coding LLM 能解的任務時間跨度每年翻倍,但同一批模型仍然搞不定「經營一台販賣機」這種事。差別在於程式與數學有可以近乎無限 scale 的 rollout 沙盒,真實世界的 rollout 又慢又貴。
- **影片是最通用的模態**:它最豐富、能教物理、能涵蓋各種時間與空間尺度的科學觀測,也能記錄數位世界的介面操作。所以 Runway 押注「pixel / 下一幀預測」是訓練世界表徵的正確 auxiliary task,而且 **bitter lesson 在影片模型上同樣成立**——算力上去,物理準確度可預測地上去。
- **從影片模型到可用的模擬器要再走三步**:(1) 把雙向 diffusion 基座轉成 autoregressive/causal 再蒸餾到即時,取得可互動與 counterfactual 探索能力;(2) 從「靜態環境導航」推進到「多 agent 在世界中採取動作」;(3) 專門化成 **GWM Robotics**——action-conditioned 影片模型,讓 policy 評估可大規模 scale,並成為未來在 world model 內做 RL 的基礎。
- **一個容易被忽略的關鍵**:world model 必須**會模擬失敗**。傳統影片模型有強烈的「成功偏誤」(生成射門進球比沒進容易),但要拿來評估 policy,錯誤動作就必須可靠地失敗。

### 重點整理

#### 為什麼真實世界的進步沒跟上(約 02:48–02:49)

他從一張大家都熟悉的圖開始:coding LLM 能解決的**任務時間跨度每年翻倍**。語言領域、尤其是 coding agent 的進展驚人。但存在一個反差:數學與程式的進展**沒有等比例地轉移到「與不可預測的真實世界互動」的任務**上。我們每天聽到某個未解猜想被推翻,但 LLM 仍然會在「有效經營一門販賣機生意」這種基本任務上失敗。

他認為原因在於我們**怎麼訓練**這些模型:對 coding 與數學,我們奢侈地擁有可以近乎無限規模運行的沙盒,rollout 要多少有多少;但我們在意的大量真實世界問題,**沒有一個可以輕易大量跑 rollout 的模擬器**,而在真實世界裡跑 rollout 既慢又貴。

#### 為什麼是影片(約 02:49–02:52)

解法自然導向 world model。多數人是從 2010 年代 David Ha 的論文認識這個概念的,但這個想法其實可以追溯到 20 世紀中葉的認知科學,以及早期 model-based RL:**人類的運作方式就是不斷在腦中預測與試演**——在真的動手之前先理解行動的後果,用來規劃。要讓 agent 也這麼做,就需要一個「經驗的模擬器」。

而要 bootstrap 這樣的模擬器,**影片是我們手上最通用的模態**:

- 它是最豐富的真實世界情境來源;
- 它能教物理,也能教人類在乎的所有任務;
- 它的通用性還不只是「人類尺度、相機拍下來的畫面」——影片可以表示**各種時間與空間尺度的科學觀測**;
- 它也能捕捉**數位世界**的觀測,這在要教 agent 操作各式介面時特別重要。

所以 Runway 的路線是:**用預測下一幀來預測世界**。他們相信 pixel / frame prediction 是在巨大規模上訓練出強大世界表徵的正確 auxiliary task,之後這些表徵可以拿去做各種下游任務。

品質到哪了?他連放三組影片,每組一真一假,請全場指認。事後說明:他們做過 **1,000 人的使用者研究,能穩定分辨的參與者不到 10%**。如果你長期浸在影片生成裡、又盯著看很久,你還是分得出來,但已經越來越難。**從品質角度,我們已經跨過「騙過人類感知」的門檻。**

這是過去十年不斷加大算力與資料規模的結果。他列了里程碑:**Gen-2** 是他們幾年前發布的第一個 text-to-video 模型,**Gen-4.5** 是 Runway 目前最新的模型——在模擬物理、動態運動、以及「看起來像真實世界影片」的能力上有巨幅提升。

#### 從創作品質到物理正確(約 02:52–02:54)

創作用的影片生成進步了,有多少能轉化成 physical AI 需要的東西?**相當多**。影片生成可以模擬大量**長尾情境**——那些用別的方法幾乎不可能或極度昂貴才能模擬的情況。

而且這件事可以量測。已有很好的 benchmark 能在多種物理內容類別上比對真實影片與生成影片:**solid mechanics、fluid dynamics、thermodynamics、optics**。即便標準拉高到「不只是看起來合理,而是物理上正確」,結果仍然是**算力規模上升,模型的物理表現可預測地變好**。換句話說,**bitter lesson 在影片模型上完全適用**,而且在他們訓練過的所有影片模型上都可預測地重現。

#### 讓模型變成模擬器:即時、可互動、多 agent(約 02:54–02:57)

要讓這些模型對真實世界真的有用,下一階段是**即時與可互動**。無論你想在影片模型上蓋模擬器還是蓋 policy 模型,這對機器人等場景都是關鍵。

Runway 的做法是:拿基座影片模型——原本是**雙向(bidirectional)的 diffusion 模型**——把它改成 **autoregressive 且 causal**,再做一階段**蒸餾讓它即時**。這讓模型變成可互動的,能輕易探索 counterfactual:「我做動作 A 相對於動作 B 會怎樣?」畫面隨你採取的動作即時生成。

同時有兩條持續推進的軸:**通用性(generality)** 與**彈性(flexibility)**。他把演進畫成一條線:David Ha 原始論文的 world model 訓練在特定賽車遊戲上;接著是自駕影像這類窄領域專用的 world model(生成道路、路上移動的車);再到去年發布的 **Genie** 那種高擬真但**大致是靜態環境的導航**。而他們聚焦的是:**怎麼讓 world model 真的動態起來**——不只是在靜態世界裡導航,而是**在世界裡採取動作**,而且理想上是**多個 agent 同時採取動作**。示範中就是同時指揮兩個不同 agent,並模擬其結果。

#### GWM Robotics:把 policy 評估搬進世界模型(約 02:57–03:01)

他們釋出的 world model 變體中,有一個是專門給機器人的:**GWM Robotics**,一個 action-conditioned 影片模型,用來模擬**單臂或雙臂機器人**動作的結果。

- 很多情況下,這些模型生成的 rollout **和真實 teleop 資料難以分辨**;
- 它能模擬**布料等非剛體物體**的細緻互動;
- 帶來的直接價值是**讓評估變得可大規模 scale**:拿任何 policy 模型(可以是 VLA 或其他),預測某個動作的結果,再把結果餵回 policy;
- 而且**對得上真實世界**:拿像 **π0.5** 這樣的 policy,用同一批動作分別在真實 teleop 資料與 world model 內 rollout,**任務成功率在真實與模擬之間有很好的相關性**。於是評估 policy 的速度可以大幅拉高。
- 未來這也是**在 world model 內做 RL** 的良好基礎,把互動 scale 得比真實世界快得多。

最後是一個他特別強調、也最容易被忽略的點:**world model 必須能模擬失敗**。傳統影片模型有強烈的**成功偏誤**——生成「某人成功進球」的影片比生成沒進的容易得多。但如果你要用它評估 policy 好不好,你就需要**當 policy 做錯動作時,它會可靠地失敗**。

結語:world model 的終極目標是把**投入其中的觀測數量**極大化。他們相信**學習型模擬器(learned simulators)**是更可 scale 的路——在那些「手工撰寫傳統模擬器極為困難」或「在真實世界執行動作、蒐集資料極為昂貴」的情境裡,尤其如此。

### 金句

> "For coding and for math we have this luxury of having sandboxes that we can run at effectively infinite scale."(約 02:49)

一句話定位了真實世界 AI 的瓶頸:不是模型不夠聰明,是沒有便宜的 rollout。

> "Our approach at Runway has been predicting the world by predicting the next frame."(約 02:50:30)

整場的路線宣言。

> "The bitter lesson really applies to video models."(約 02:53:30)

物理正確度隨算力可預測地提升,不是靠架構先驗。

> "A lot of traditional video models have this bias towards success."(約 03:00:20)

最反直覺的一點:能生成漂亮成功畫面的模型,恰恰不適合拿來評估 policy。

## English Notes

### TL;DR

- **The gap is about sandboxes, not intelligence.** The time horizon of tasks a coding LLM can solve has doubled every year, yet the same models still fail at running a vending machine business. Code and math have rollout sandboxes that scale essentially for free; real-world rollouts are slow and expensive.
- **Video is the most general modality**: the most abundant source of real-world scenarios, it teaches physics, spans scientific observations at many temporal and spatial scales, and even captures the digital world's interfaces. So Runway's bet is that pixel/next-frame prediction is the right auxiliary task for learning world representations — and **the bitter lesson applies to video models**: more compute predictably buys better physics.
- **Three more steps turn a video model into a usable simulator**: (1) convert the bidirectional diffusion base into an autoregressive, causal model and distill it to real time, unlocking interactivity and counterfactual exploration; (2) move from static-environment navigation to multiple agents taking actions in the world; (3) specialize into **GWM Robotics**, an action-conditioned model that makes policy evaluation scalable and lays the groundwork for RL inside the world model.
- **The easily-missed requirement**: a world model has to **simulate failure**. Traditional video models carry a strong success bias (a video of a goal going in is easier to generate than one missing), but to evaluate a policy you need wrong actions to reliably fail.

### Key Points

#### Why real-world progress lags (~02:48–02:49)

He opened with the graph everyone knows: the **time horizon of software tasks a coding LLM can solve has doubled every year**. Progress in the language domain, and especially with coding agents, has been incredible. Yet there's a contrast — that progress in math and code **does not transfer as well to tasks that involve interacting with the unpredictable real world**. We hear daily about some open conjecture being disproven, and meanwhile LLMs still fail at rudimentary tasks like running a vending machine business effectively.

The reason, he argues, comes down to **how effectively we train those models**. For coding and math we have the luxury of sandboxes we can run at effectively infinite scale, so rollouts scale trivially. For most real-world problems we care about, **there is no simulator we can easily run at scale**, and scaling rollouts in the real world is slow and expensive.

#### Why video (~02:49–02:52)

The natural response is world models. Most people know the concept from David Ha's paper in the 2010s, but the idea goes back to mid-20th-century cognitive science and early model-based RL: **humans constantly predict and try things out in their heads**, understanding the outcome of actions before taking them, and that's what enables planning. To do this with agents, you need a simulator of experience.

To bootstrap such a simulator, **video is the most general modality available**:

- it's the most abundant source of real-world scenarios;
- it can teach physics and essentially all the tasks humans care about;
- its generality goes beyond human-scale camera footage — video can represent **scientific observations across many temporal and spatial scales**;
- and it captures **digital-world observations**, which matters enormously if you want agents that work with the variety of interfaces we use every day.

So Runway's approach has been **predicting the world by predicting the next frame** — treating pixel and frame prediction as the right auxiliary task to train at massive scale, producing models with powerful world representations usable for many downstream tasks.

How good is the quality? He ran three real-versus-generated pairs with the audience. Then the reveal: in a **user study with 1,000 participants, reliably fewer than 10% could tell them apart**. If you live in video generation and stare long enough you can still call it, but it's getting harder. **On quality, we've crossed the threshold where it's easy to fool human perception.**

That came from a decade of increasing compute and data scale. The milestones: **Gen-2**, their first text-to-video model released a few years ago, through to **Gen-4.5**, Runway's latest — a massive improvement in simulating physics, producing dynamic motion, and generally feeling like plausible real-world video.

#### From creative quality to physical accuracy (~02:52–02:54)

How much of the creative-video progress translates into what physical AI needs? Quite a lot. Video generation can simulate a great many **long-tail scenarios** that are basically impossible or incredibly expensive to simulate otherwise.

And it's measurable. Good benchmarks now compare real to generated video across many categories of physics content — **solid mechanics, fluid dynamics, thermodynamics, optics**. Even on the stricter bar of whether the video is physically *accurate* rather than merely plausible, **increasing compute scale reliably improves the physics of these models**. In other words, **the bitter lesson really applies to video models**, and they've seen it hold predictably across every video model they've trained.

#### Making it a simulator: real-time, interactive, multi-agent (~02:54–02:57)

The next stage toward real-world usefulness is making the models **real-time and interactive** — critical for robotics whether you want to build a simulator or a policy model on top of a video model.

Their approach: take the foundation video model, which is a **bidirectional diffusion model**, make it **autoregressive and causal**, then run another **distillation stage to make it real-time**. That makes the model interactive and lets you explore counterfactuals easily — if I take this action versus that one, what happens? — with frames generated on the fly from the actions you take.

Two axes keep advancing: **generality** and **flexibility** of world models. He traced the arc: David Ha's original world model was trained on one particular racing game; then came narrow-domain world models for things like self-driving footage (generating roads and cars moving along them); then last year's **Genie**, high fidelity but mostly **static-environment navigation**. Their focus has been on making world models genuinely **dynamic** — not just navigating a static world, but **taking actions in it, and ideally with multiple agents**. The demo instructs two different agents simultaneously and simulates the outcome.

#### GWM Robotics: moving policy evaluation inside the world model (~02:57–03:01)

One of the released world model variants is robotics-specific: **GWM Robotics**, an action-conditioned video model that simulates the outcomes of actions for **single-arm or bimanual robots**.

- In many cases the generated rollouts are **very difficult to tell apart from ground-truth teleop data**.
- It simulates fine-grained interactions with **cloth and other non-rigid objects**.
- The immediate payoff is **making evaluation far more scalable**: take any policy model — a VLA or otherwise — predict the outcome of an action, and feed that back into the policy.
- And it **matches the real world**: take a policy like **π0.5**, roll out identical actions against ground-truth teleop data and inside the world model, and task success correlates well between simulation and reality. That massively speeds up how fast you can evaluate policy models.
- Looking forward, this is also a strong foundation for **doing RL inside the world model**, scaling interactions far faster than reality allows.

He closed on the point most likely to be overlooked: **world models must be able to simulate failure.** Traditional video models carry a **bias toward success** — it's much easier to generate a video of someone scoring a goal than missing one. But if you want to evaluate how well a policy works, you need the model to **reliably fail when the policy performs the wrong actions**.

The ultimate goal of world models is to increase the number of observations you can put into them. He believes **learned simulators** are a far more scalable path to building environments where agents can train — especially where hand-authoring a traditional simulator is very difficult, or performing the actions and gathering data in the real world is very expensive.

### Quotes

> "For coding and for math we have this luxury of having sandboxes that we can run at effectively infinite scale." (~02:49)

The bottleneck for real-world AI in one line: not model intelligence, but the cost of a rollout.

> "Our approach at Runway has been predicting the world by predicting the next frame." (~02:50:30)

The thesis statement of the talk.

> "The bitter lesson really applies to video models." (~02:53:30)

Physical accuracy improves predictably with compute, not with architectural priors.

> "A lot of traditional video models have this bias towards success." (~03:00:20)

The most counterintuitive point: the very models that produce beautiful successful footage are the wrong ones for evaluating a policy.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Runway Gen-2 | Runway 幾年前發布的第一個 text-to-video 模型 | Runway's first text-to-video model, released a few years ago | 影片品質演進的起點 / start of the quality timeline he showed |
| Runway Gen-4.5 | Runway 目前最新的基座影片模型,物理模擬與動態運動大幅提升 | Runway's latest base video model; large gains in physics simulation and dynamic motion | GWM 系列建立在其之上 / the GWM family is built on top of it |
| GWM Robotics | 針對機器人的 action-conditioned 影片世界模型,模擬單臂/雙臂動作結果 | Robotics-specific action-conditioned video world model for single-arm and bimanual outcomes | 用於可 scale 的 policy 評估與未來的 world-model 內 RL / for scalable policy evaluation and future in-model RL |
| David Ha 的 World Models 論文 | 2010 年代讓多數人認識 world model 概念的論文 | The paper that introduced most people to world models in the 2010s | 他指出概念本身可追溯至 20 世紀中的認知科學與 model-based RL / he notes the concept predates it |
| Genie | 去年發布、高擬真但以靜態環境導航為主的 world model | Last year's world model: high fidelity, mostly static-environment navigation | 作為「通用性/彈性」演進軸上的參照點 / a reference point on the generality axis |
| π0.5 (pi 0.5) | 用來驗證 world model 內外任務成功率相關性的 policy 模型 | The policy model used to show sim-vs-real task-success correlation | Physical Intelligence 的模型 / from Physical Intelligence |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Anastasis Germanis / Anastasio | Anastasis Germanidis |
| gen 2 / gen 4.5 | Gen-2 / Gen-4.5 |
| GWM robotics | GWM Robotics |
| pi 0.5 | π0.5 |
| RILL / model based RL | model-based RL |
| birectional | bidirectional |
| auto reggressive | autoregressive |
| VA / VAS | VLA / VLAs |
| many nons of reliability(panel 段) | many nines of reliability |

## 待確認 / To Verify

- 「時間跨度每年翻倍」那張圖的原始出處,演講中只說「大家應該都熟悉這張圖」而未具名。/ The source of the doubling-time-horizon chart was not cited on stage.
- 用來比對真實與生成影片物理正確性的 benchmark 名稱,演講中僅稱 "some really great benchmarks"。/ The physics benchmarks used to compare real versus generated video were not named.
- 1,000 人使用者研究的完整方法與發表出處。/ Full methodology and publication venue for the 1,000-participant user study.
