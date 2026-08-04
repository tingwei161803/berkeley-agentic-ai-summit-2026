---
title: "Robotics: Endgame"
title_zh: "機器人學的終局"
speaker: "Jim Fan"
affiliation: "Director of Robotics & Distinguished Scientist, Nvidia"
type: talk
stage: Plenary
date: 2026-08-01
session: "Session 4: Robotics & World Models"
video: "https://www.youtube.com/watch?v=Tcn5Yb2K0h4&t=8509s"
video_range: "02:21:49–02:35:25"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [robotics, scaling-laws, world-models, egocentric-data, agentic-ai]
---

# 機器人學的終局(Robotics: Endgame)

**一句話總結**:LLM 靠兩條 scaling curve(神經網路 scaling law + agentic auto-research)把煉金術變成數學,機器人學至今還停在煉金術階段——出路是把同樣兩條曲線疊起來:world action model 決定地板,physical auto research 抬高天花板。
**One-line summary**: LLMs escaped alchemy by riding two scaling curves — the neural scaling law and agentic auto-research — while robotics is still stuck in the alchemy era; the way out is to stack the same two curves, letting world-action models set the floor and physical auto-research raise the ceiling.

## 中文筆記

### TL;DR

- **「Two curves is all you need」**:第一條是 neural scaling law(算力/資料進去,loss 下來,可預測到能在花錢之前先算出成果);第二條是今年才落地的 **agentic scaling**——x 軸仍是訓練算力,但計價單位換成 token,模型靠成群 agent 自己跑實驗來自我改進。兩條可以接起來:**agentic scaling starts where foundation scaling ends**。
- **模型面**:把預訓練的 video diffusion 模型改成同時解碼未來影片與動作,得到 **World Action Model (WAM)**——機器人先「做夢」預測接下來幾秒的畫面再據以行動,被推倒也能即時重新規劃、重新做夢。再用 **test-time training (TTT)** 把原生 context 拉長 1000 倍到 8,000 個 time step(約 5 分鐘的「肌肉記憶」),解鎖部署後持續學習與 in-context 模仿人類。
- **資料面**:teleop VR 頭盔那一套「中世紀刑具」根本不 scale;要的是 Tesla FSD 那種「資料收集隱沒到背景」的飛輪。**EgoScale** 因此把 99.9% 的訓練放在人類第一人稱影片上——20,000 小時野生影片預訓練 + 50 小時動捕手套 + 4 小時 teleop(<0.1%),直接從像素映射到 22 自由度靈巧手,並發現 dexterity 的 log-linear scaling law。
- **Agentic 面**:模擬器和控制堆疊說到底都是程式碼,所以可以「抄 LLM 的作業」——把機器人變成 coding environment,讓 coding agent 團隊操作真實機器人做 **physical auto research**(自動 reset 場景 / 自動改策略 / 自動評估),把任務從 0% 爬到 99%;**ASPIRE** 則不更新權重,而是累積會複利成長的技能庫,並能 sim-to-real 與跨 embodiment 遷移。

### 重點整理

#### 兩條曲線:機器人學為何還在煉金術時代(約 02:21:49–02:23)

開場拉回 2017 年的 NeurIPS:Ali Rahimi 上台說「machine learning has become alchemy」——他是對的,當時什麼都不嚴謹,大家都在憑感覺,東西看起來會動但沒人說得準,未來又模糊又脆弱。九年後的今天,LLM 那群人已經在 speedrun AGI 了,而且是踩在字面上就叫 Mythos 的神話生物背上。

煉金術怎麼變成數學的?兩條曲線。

1. **Neural scaling law**:算力與資料進去,loss 下來,而且可預測到「還沒花一塊錢就能預測會拿到什麼」。這條曲線是數兆美元投資該往哪裡流的指路明燈。
2. **Agentic scaling**(今年才落地):x 軸仍是訓練算力,但換算成一種新貨幣——token。這是 auto research:模型靠愈來愈多 agent 自己跑實驗來自我改進,而 capability 是 LLM 的最終 boss 戰。

漂亮的地方在於這兩條不是分開的,可以**疊起來**:agentic scaling 從 foundation scaling 結束的地方開始。當初的煉金術,如今是能外推到近未來、最可靠的一條曲線。

然後是他的自白:身為在 LLM 派對裡的機器人研究者,他覺得很孤單、很被冷落。原因是**機器人學還卡在煉金術時代**——在搞清楚「要 scale 什麼、scale 之後會發生什麼」之前,是走不出去的。接下來分兩塊講:模型,以及資料策略。

#### 模型:從 AI 影片廢料到 World Action Model(約 02:23–02:26)

數位 AI 的第一個預訓練典範是 next word prediction。他本來以為第二個典範會是什麼光榮的東西,結果我們給它取的名字叫 **AI video slop**。他自己可以看胖貓彈斑鳩琴看一整天(這是網路的巔峰),但沒人會認真看待這件事,直到我們搞清楚:**這些 video world model 其實在內部學會了模擬物理**。

Nvidia **Cosmos 3** 生成的影片顯示,模型單靠「預測下一團像素」就學到了重力、浮力、反射、碰撞;甚至湧現出解視覺謎題的能力——Cosmos 會在像素空間裡把模擬往前跑來解左邊那題;而右邊那個他最喜歡:**Cosmos 發現只要你沒在看,幾何就是可選的**。

怎麼把 world model 變成對機器人有用的東西?一種新的 policy 模型:畫面右上角那格**不是真實相機影像**,而是機器人在「做夢」——預測接下來幾秒會發生什麼,然後在夢的基礎上行動。這讓 policy 很魯棒:你去干擾它、把東西撞倒,它會即時重新規劃、重新做夢。做法是拿預訓練的 video diffusion 模型,讓它**同時解碼未來的影片與動作**,這類新模型稱為 **world action model (WAM)**。

但這些模型只夢得到幾秒鐘,真實任務需要更長的記憶。於是他們加了一項技術,把原生 context 長度拉長 **1000 倍到 8,000 個 time step**,約等於**五分鐘的肌肉記憶**。這技術叫 **TTT(test-time training)**:在模型內部嵌一個小模型,推論時訊號流進來會對這個小核心走梯度步,不斷把看過的歷史壓縮進 fast weights。也就是說,**機器人在部署之後還能繼續學**。影片裡是全自動、一鏡到底地把一台車從零組裝起來。

它同時解鎖了**向人類的 in-context learning**:人類示範如何把電路板重組成機器人沒見過的新樣子,機器人以這段長影片為 prompt(大量 token 塞在 context 裡)忠實模仿。這也開出一個新的 scaling 軸:**context scaling**——效能隨 time step 拉到 8,000 穩定上升,比先前 SOTA 高三個數量級。

#### 資料:EgoScale 與 dexterity 的 scaling law(約 02:26–02:29)

過去三年是 teleop VR 頭盔的黃金年代,那些複雜的裝備「看起來像中世紀刑具」——業界投入巨量資源、無數痛苦,做的卻是一件**根本上不 scale** 的事。

對照組是 Tesla:你開 Tesla 的時候就在替全世界最大的實體資料飛輪供料,而且**你根本沒感覺**——資料上傳是個 ambient process。機器人操作也需要一個 FSD 等價物:**讓資料收集淡入背景、退出迴圈**,才能有機化地捕捉各行各業人類靈巧度的全貌。

所以他們全押在**人類第一人稱影片**上,搭配細緻標註(細緻語言、手部姿態)。**EgoScale** 的訓練配方是 99.9% 來自人類第一人稱影片:

- **20,000 小時**高品質野生影片預訓練
- fine-tune 只用 **50 小時**動捕手套資料
- 加 **4 小時** teleop——**佔訓練混合不到 0.1%**

成果是一個全自動 policy,**直接從像素(眼睛的視角)映射到 22 自由度的擬人靈巧手**,只要少量示範就能做撲克牌分類這類靈巧任務,或操作針筒這類長程任務。

最後再送一條 scaling law:他們發現了 **dexterity 的 neural scaling law**——投入的人類影片量與最佳 loss 之間是乾淨的 log-linear 數學關係。目標是把它推到 100 萬、1000 萬、有一天 1 億小時,並期待這條律持續外推。

至此第一部分完成:x 軸是算力,y 軸是機器人能力,展示了**如何用梯度下降在感測資料上端到端地 scale 機器人基礎模型**。

#### Agentic:把機器人變成 coding environment(約 02:29–02:33)

要把這條曲線再往前推,想法很簡單:**所有模擬器與機器人控制堆疊,說到底都只是程式碼**。這讓人興奮,因為我們終於可以**抄 LLM 的作業**——把機器人學變成一堆 coding environment(吃進馬達動作、吐出感測訊號),而幾十年累積的機器人函式庫與感知堆疊,現在都能當成 **agentic tools** 整合進來。

他帶大家看夜晚的實驗室:裡面沒有人,只聽得到馬達嗡嗡和 GPU 轉動,像「博物館驚魂夜」——機器人全都活過來,用程式碼互相溝通,擺弄控制堆疊、在真實機器人上跑實驗,甚至上網讀論文。(他們發現自家機器人讀了很多 Sergey 的論文,所以「謝謝 Sergey 貢獻我們的 agentic token 預算」。)

做法是給一組 coding agent 一支機器人艦隊和一個很簡單的目標:**在安全限制下盡快解決任務,而且不能出錯**。每個機器人站台試一個不同的研究想法。要讓這個迴圈成立需要三件事:**自動 reset 實體場景、自動改進 policy、自動評估**。三者都到位之後,agent 能把任務從 0% 一路爬到 **99% 成功率**。這是他們第一次嘗試 **physical auto research**。(他跟團隊說夢想是「大家一起放假,老闆都不會發現,因為只要讀 agent 的報告就好」;團隊回他:「小心你許的願。」)

反向也成立:不是解單一任務,而是讓機器人在模擬與真實世界裡嘗試大量任務時**自主發現技能**。近期的 **ASPIRE** 就是這種新型 continual learning:**它不更新模型的權重矩陣**,而是學一個**隨時間複利成長的技能庫**,把「機器人實務工作者的 know-how」沉澱下來。這也解鎖另一條 scaling law:x 軸仍是訓練算力但以 token 計,y 軸是**已驗證技能的數量**。而且 ASPIRE 學到的技能能 **sim-to-real**、甚至**跨 embodiment** 遷移。所以:**compute = tokens = skills**。

整條曲線於是完整:**Total robot intelligence = foundation intelligence + agentic intelligence。World action model 決定地板,physical auto research 抬高天花板。**(他補了句黃仁勳式的結語:「the more you buy, the more you save」。)

#### 終局:physical Turing test 與 2040(約 02:33–02:35:25)

對他而言,**解決機器人學 = 在夠廣的任務範圍上通過 physical Turing test**:你分不出這件事是人做的還是機器人做的。聽起來簡單,但這是 AI 下一個、甚至可能是最後一個大挑戰。(他當場自嘲:看剛才機器人「掛掉」的樣子,我們還有得忙。)

最後一條 scaling law 是時間軸:從 AlexNet 的第一次前向傳播到今天的 Opus / Mythos / GPT 系列,已經 14 年;再加 14 年就是 **2040**。他認為**人類非常不擅長「感受」scaling 曲線**——回頭看它是平的,往前看幾乎是垂直的。

**Physical AGI 會先是慢慢地、然後突然地發生**;但在那之前,我們得先找出治理這個領域的指導原則與 scaling law,好把機器人學習從**煉金術變成化學**。

### 金句

> "Two curves is all you need."(約 02:22:20)

呼應 "Attention is all you need" 的句式;整場演講的骨架。

> "Agentic scaling starts where foundation scaling ends."(約 02:23)

兩條曲線不是替代關係,是接力。

> "Cosmos finds that if you're not looking, geometry is optional."(約 02:24)

講 world model 湧現物理理解時最好笑也最尖銳的一句——它學到的是「被觀測時的物理」。

> "Total robot intelligence equals foundation intelligence plus agentic intelligence. World action model sets the floor and physical auto research raises the ceiling."(約 02:33:50)

他自己說「如果今天只帶走一頁,就是這頁」。

> "Physical AGI will happen gradually and then suddenly."(約 02:35:05)

> "Turn the practice of robot learning from alchemy to chemistry."(約 02:35:15)

收尾扣回開場的 Ali Rahimi。

## English Notes

### TL;DR

- **"Two curves is all you need."** The first is the neural scaling law — compute and data in, loss down, predictable enough to forecast the result before spending a dollar. The second landed this year: **agentic scaling**, where the x-axis is still training compute but the currency is tokens, and models self-improve via swarms of agents running their own experiments. The two stack: **agentic scaling starts where foundation scaling ends.**
- **On the model side**: take a pretrained video diffusion model and have it jointly decode future video *and* actions, yielding a **World Action Model (WAM)** — the robot dreams the next few seconds and acts on the dream, replanning and re-dreaming on the fly when perturbed. **Test-time training (TTT)** then stretches the native context 1000× to 8,000 timesteps (~5 minutes of "muscle memory"), unlocking post-deployment learning and in-context imitation of humans.
- **On the data side**: teleop VR rigs ("medieval torture devices") fundamentally don't scale. What's needed is the Tesla FSD property — data collection fading into the background. **EgoScale** puts 99.9% of training on human egocentric video: 20,000 hours of in-the-wild pretraining, 50 hours of mocap-glove fine-tuning, 4 hours of teleop (<0.1% of the mix), mapping pixels straight to 22-DoF humanlike dexterous hands — and yields a log-linear scaling law for dexterity.
- **On the agentic side**: simulators and control stacks are just code, so you can copy homework from LLMs — turn robotics into coding environments and let teams of coding agents run **physical auto research** on real hardware (auto-reset, auto-improve, auto-evaluate), climbing a task from 0% to 99%. **ASPIRE** goes further: it doesn't update weights at all, but grows a compounding skill library that transfers sim-to-real and across embodiments.

### Key Points

#### Two curves, and why robotics is still alchemy (~02:21:49–02:23)

He opened at NeurIPS 2017, where Ali Rahimi took the stage and declared that machine learning had become alchemy. He was right: nothing was rigorous, everyone was vibing, things seemed to work but nobody could tell for sure, and the future felt fuzzy and fragile. Nine years later the LLM crowd is speedrunning AGI on the back of mythical beings literally named Mythos.

What ended the alchemy? Two curves.

1. **The neural scaling law** — more compute and data in, loss down, so predictable you can forecast the outcome before spending a single dollar. This curve is the guiding light for how trillions of dollars of investment should flow.
2. **Agentic scaling**, which only landed this year. The x-axis is still training compute, but measured in a new currency: tokens. This is auto-research, where models self-improve with more and more agents running experiments on their own — and capability is the final boss fight for LLMs.

The beautiful part is that these are not separate curves. **Agentic scaling starts where foundation scaling ends**, so what began as alchemy is now the most reliable curve extrapolating into the near future.

Then the confession: as a roboticist at the LLM party, he feels lonely and left out — because **robotics is stuck in the age of alchemy**, and won't get out until the field figures out what to scale and what happens at scale. The rest of the talk covers two things: the model and the data strategy.

#### Model: from AI video slop to World Action Models (~02:23–02:26)

The first pretraining paradigm for digital AI was next-word prediction. He expected the second to be something glorious; instead the name we gave it is **AI video slop**. He can watch fat cats playing banjo all day — peak internet — but nobody takes it seriously until we recognize that **these video world models are learning to simulate physics internally.**

Videos from Nvidia **Cosmos 3** show the model picking up gravity, buoyancy, reflection, and collision purely from predicting the next blob of pixels at scale. An emergent property: it can solve visual puzzles, running simulation forward in pixel space. And his favorite: watch closely, and **Cosmos finds that if you're not looking, geometry is optional.**

How do you turn that into something useful for robotics? A new kind of policy model. The feed in the upper right corner is not a real camera — it's the robot **dreaming** what will happen over the next few seconds in video, then acting on top of that. The policy is robust: perturb it, knock things over, and it replans and re-dreams on the fly. Mechanically, you take a pretrained video diffusion model and have it **jointly decode video and action into the future** — a **world action model (WAM)**.

These models only dream a few seconds ahead, and real tasks need longer memory. So they added a technique that extends the model's native context length **1000× to 8,000 timesteps — five minutes of muscle memory**. The technique is **TTT (test-time training)**: embed a tiny model inside the model, and at inference, as incoming signals flow in, take gradient steps on that tiny core, continually compressing the observed history into fast weights. In effect, **the robot keeps learning after deployment.** The demo is fully autonomous, single-shot: a robot assembling a car from scratch.

It also enables **in-context learning from humans**: a person demonstrates how to reconfigure a circuit board into a novel arrangement the robot has never seen, and conditioned on that long video prompt — a lot of tokens in context — the robot imitates faithfully. That opens a new scaling axis, **context scaling**: performance rises reliably out to 8,000 timesteps, three orders of magnitude beyond prior state of the art.

#### Data: EgoScale and a scaling law for dexterity (~02:26–02:29)

The last three years were the golden era of teleop VR headsets — complex rigs that look like medieval torture devices, absorbing enormous industry investment and no small amount of suffering, in service of something that **fundamentally does not scale**.

The contrast is Tesla: when you drive one, you're feeding the biggest physical data flywheel in the world, and the beautiful part is **you don't even notice** — the upload is an ambient process. Robot manipulation needs an FSD equivalent: **data collection has to fade into the background and stay out of the loop**, so we can organically capture the full glory of human dexterity across all walks of life.

Hence the all-in bet on human egocentric video with detailed annotations (fine-grained language, hand poses). **EgoScale** puts 99.9% of training on human egocentric video:

- **20,000 hours** of high-quality in-the-wild video for pretraining
- fine-tuning on only **50 hours** of mocap-glove data
- plus **4 hours** of teleop — **less than 0.1% of the training mix**

The result is a fully autonomous policy mapping **directly from pixels (the eyes' view) to 22-DoF humanlike dexterous hands**, performing dexterous tasks like sorting poker cards and long-horizon tasks like manipulating a syringe from only a handful of demonstrations.

And one more scaling law: they found a **neural scaling law for dexterity** — a clean log-linear relationship between the volume of human video and optimal loss. The hope is to push it to 1 million, 10 million, and someday 100 million hours, and for the law to keep extrapolating.

That completes part one: x-axis compute, y-axis robot capability, showing **how to scale robot foundation models end to end by gradient descent on sensory data**.

#### Agentic: turning robots into coding environments (~02:29–02:33)

To carry the curve further, a simple idea: **all the simulators and the robot control stack are, after all, just code.** That's exciting because it means we can finally **copy homework from LLMs** — turn robotics into a set of coding environments that take motor actions as input and emit sensory signals, with decades of robotics libraries and perception stacks integrated as **agentic tools**.

He takes the audience to the lab at night: no humans inside, just motors humming and GPUs spinning — Night at the Museum, but the robots come alive. They talk to each other through code, tinker with the control stack, run experiments on real hardware, and go online to read papers. (They found their robots read a lot of Sergey's papers, so: "thank you, Sergey, for contributing to our agentic token budget.")

The setup gives a team of coding agents a robot fleet and one simple goal: **solve a task as fast as possible subject to safety constraints, and make no mistakes.** Every robot station tries a different research idea. Closing that loop needs three things: **auto-reset of a physical scene, auto-improvement of the policy, and auto-evaluation.** Get those right and the agents hill-climb a task from 0% all the way to **99% success**. This is their first attempt at **physical auto research**. (His dream: the whole team takes a holiday and the boss doesn't notice, because they just read the agents' reports. His team's reply: be careful what you wish for.)

The reverse direction works too: instead of solving one task, let robots **autonomously discover skills** while attempting a huge variety of tasks in simulation and the real world. Recent work called **ASPIRE** enables a new kind of continual learning that **does not update the model's weight matrices** — instead it learns a **skill library that compounds over time**, capturing the know-how a robotics practitioner would accumulate. That unlocks yet another scaling law: x-axis training compute measured in tokens, y-axis the **number of validated skills**. ASPIRE's learned skills transfer sim-to-real and even across embodiments. So: **compute = tokens = skills.**

That completes the full curve: **Total robot intelligence = foundation intelligence + agentic intelligence. The world action model sets the floor; physical auto research raises the ceiling.** (Closing in Jensen Huang mode: "the more you buy, the more you save.")

#### Endgame: the physical Turing test and 2040 (~02:33–02:35:25)

To him, solving robotics means **passing the physical Turing test across a wide range of tasks** — you can't tell whether a human or a robot did it. Deceptively simple, but this is the next, if not the final, grand challenge for AI. (Deadpan, after a robot demo glitched on stage: judging by how the robot just went out, work is cut out for us.)

The last scaling law of the day is the calendar. It has been 14 years from AlexNet's first forward pass to the Opus, Mythos, and GPT-class models of today. Add another 14 and you land on **2040**. His view: **humans are terrible at feeling the scaling curve** — looking backwards it seems flat, looking forward it is almost vertical.

**Physical AGI will happen gradually and then suddenly.** But first the field needs its guiding principles and scaling laws, so robot learning can move **from alchemy to chemistry**.

### Quotes

> "Two curves is all you need." (~02:22:20)

Echoing "Attention is all you need"; the skeleton of the whole talk.

> "Agentic scaling starts where foundation scaling ends." (~02:23)

The two curves are a relay, not a substitution.

> "Cosmos finds that if you're not looking, geometry is optional." (~02:24)

The sharpest line about what video world models actually learn: physics-when-observed.

> "Total robot intelligence equals foundation intelligence plus agentic intelligence. World action model sets the floor and physical auto research raises the ceiling." (~02:33:50)

His designated "if you take away only one page from my talk" slide.

> "Physical AGI will happen gradually and then suddenly." (~02:35:05)

> "Turn the practice of robot learning from alchemy to chemistry." (~02:35:15)

The closing callback to Ali Rahimi.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Ali Rahimi, NeurIPS 2017 | 「machine learning has become alchemy」的來源演講 | The talk that declared machine learning had become alchemy | 全場的開場與收尾框架 / the talk's opening and closing frame |
| Nvidia Cosmos 3 | Nvidia 的 world foundation model,示範從像素預測中湧現重力、浮力、反射、碰撞與視覺解謎 | Nvidia's world foundation model; demonstrates gravity, buoyancy, reflection, collision and visual puzzle-solving emerging from next-pixel prediction | 作為 WAM 的骨幹 / serves as the WAM backbone |
| World Action Model (WAM) | 由 video diffusion 模型同時解碼未來影片與動作的新型 policy 模型 | New policy model class: a video diffusion model jointly decoding future video and actions | 機器人「做夢再行動」,被干擾能即時重新規劃 / the robot dreams then acts, replanning under perturbation |
| TTT (test-time training) | 在模型內嵌小模型,推論時走梯度步壓縮歷史,把 context 拉長 1000 倍到 8,000 timesteps | Embeds a tiny model inside the model, taking gradient steps at inference to compress history; extends context 1000× to 8,000 timesteps | 約 5 分鐘肌肉記憶;解鎖部署後持續學習與 in-context 模仿 / ~5 min of muscle memory |
| EgoScale | 99.9% 訓練在人類第一人稱影片:20,000 小時野生影片 + 50 小時動捕手套 + 4 小時 teleop;像素直接映射到 22-DoF 靈巧手 | 99.9% of training on human egocentric video: 20,000 h in-the-wild + 50 h mocap gloves + 4 h teleop; pixels straight to 22-DoF dexterous hands | 發現 dexterity 的 log-linear scaling law / yields a log-linear scaling law for dexterity |
| ASPIRE | 不更新權重的 continual learning:累積可複利成長、可 sim-to-real 與跨 embodiment 遷移的技能庫 | Continual learning without weight updates: a compounding skill library that transfers sim-to-real and cross-embodiment | 開出「token → 已驗證技能數」的 scaling law / opens a tokens-to-validated-skills scaling law |
| Physical auto research | coding agent 團隊 + 機器人艦隊,靠自動 reset / 自動改策略 / 自動評估把任務爬到 99% | Coding agents plus a robot fleet; auto-reset, auto-improve, auto-evaluate hill-climbs a task to 99% success | 「實驗室的夜晚」demo / the "night at the museum" lab demo |
| Tesla FSD | 資料收集淡入背景的範例,他心中機器人操作該學的資料飛輪 | The model for ambient data collection — the flywheel robot manipulation needs | Panel 中他也把 FSD 選為最驚豔的 demo / he also names FSD as his favorite recent demo in the panel |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| a new conference in 2017 | NeurIPS 2017 |
| LOM folks | LLM folks |
| Methos | Mythos(Claude Mythos) |
| world action models or webs / WHM / wham | world action models (WAMs) |
| TDT | TTT (test-time training) |
| ego scale / Eagle Scale | EgoScale |
| tallyop / teleyop | teleop |
| Aspire | ASPIRE |
| skating law / scalating law / neuroscalating law | scaling law / neural scaling law |
| physical touring test | physical Turing test |
| feeding the scaling curve | feeling the scaling curve |
| Alexnet | AlexNet |
| Isaac Sim(panel 段) | Isaac Sim(正確 / correct as heard) |

## 待確認 / To Verify

- 「Opus, Methos, GPD souls of today」中的 "GPD souls" 指哪個 OpenAI 模型版本,自動字幕無法還原。/ Which OpenAI model "GPD souls" refers to in "Opus, Mythos, GPD souls of today" — the auto-caption is unrecoverable.
- ASPIRE 的官方全名在不同來源有兩種寫法(arXiv 標題為 "Agentic /Skills Discovery for Robotics",部分報導寫 "Agentic Skill Programming through Iterative Robot Exploration"),以論文為準。/ ASPIRE's expanded name appears in two forms across sources; defer to the arXiv paper title.
- 「99% success rate」的 physical auto research 是哪一項任務,演講中未指名。/ The specific task hill-climbed to 99% in the physical auto research demo was not named.
