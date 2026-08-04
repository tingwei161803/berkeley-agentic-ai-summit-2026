---
title: "Real-World Reasoning Agents"
title_zh: "面向真實世界的推理 Agent"
speaker: "Trevor Darrell"
affiliation: "Professor, UC Berkeley"
type: talk
stage: Atlas
date: 2026-08-01
session: "Session 2: Robotics & World Models"
video: "https://www.youtube.com/watch?v=psPzCQbjCCo&t=2641s"
video_range: "00:44:01–00:54:49"
transcript: "tmp/[English (auto-generated)] Atlas Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [vision-language-models, tactile-sensing, dexterous-manipulation, world-models, bair]
---

# 面向真實世界的推理 Agent(Real-World Reasoning Agents)

**一句話總結**:要讓 agent 真正在物理世界裡運作,它得會**看**(看得出兩張圖之間那個關鍵的小差異)、會**摸**(靠觸覺即時反應而不只是視覺規劃),還得會**在抽象層次上推理運動**(預測 SE(3) 位姿軌跡,而不是預測每一個像素)。

**One-line summary**: For agents to work in the physical world they need to *see* (catch the one small difference between two images that matters), *feel* (react to touch in real time rather than plan from vision alone), and *reason about motion abstractly* (predict SE(3) pose trajectories instead of every pixel).

## 中文筆記

### TL;DR

- **今天 VLM 的視覺編碼器是「無狀態」的**:每張圖獨立編碼,兩張只差一點點的圖會得到同一個 caption。他們的 **Stateful Visual Encoder** 在編碼器中層加入跨圖注意力,專門保留「狀態改變」這種太小而被抹掉的訊號。
- **觸覺是被低估的模態**:foundation model 很會推理、規劃、行動,但**不會反應(react)**。**T-Rex** 用 slow-fast 的雙/多程序架構加上觸覺感測,做到剝撲克牌、擠牙膏、憑觸感辨識麻將牌、鎖孔轉鑰匙、拿真雞蛋、鎖燈泡而不捏破。
- **World model 不必預測每個像素**:**World Motion Model** 是建在 **SE(3) 位姿軌跡**上的世界模型——把場景中每個物件/剛體部位當一個參考框、把 6-DoF 位姿 tokenize 後沿時間堆疊,用去噪訓練,可以做未來預測、動作條件預測、inpainting/運動規劃與 retargeting。

### 重點整理

#### 看:Stateful Visual Encoders(約 00:44–00:47)

他先承接 Vanhoucke 的演講:「Vincent 的演講是我這場完美的前導,我不用再花時間解釋我為什麼對 physical AI 有興趣。」

問題起點很具體:**我們已經有看得見的 agent,但它們其實常常看得不好。** 今天 VLM 與 agentic VLM 裡的視覺編碼器,是為「網路影像任務」設計的,對 physical AI 任務——甚至對**精細**的網路視覺任務——都未必合適。

他放了兩張圖:分別丟進同一個視覺編碼器、同一個 LLM,**得到一模一樣的 caption**;而台下觀眾自己也得來回比對很久才看得出差別。「而**來回比對**正是我們今天不允許視覺編碼器與 VLM 做的事。」

他們的做法簡單到「novel 得讓你意外」:在編碼器的**中間層**允許**跨圖權重**(cross-image attention),專門調成能偵測那些小到無法被正常表示保留的**狀態改變**。有了這個 change encoder,模型才能給出提到「什麼變了」的細緻 caption,或判斷網頁介面上某個小方框有沒有被打勾——而不必用暴力方式硬做。

論文比較了多種建構方式,在幾類真實任務上都有顯著改善:**醫學影像的縱向報告生成、影像編輯控制、以及遙測影像的變化偵測**。

#### 摸:T-Rex(約 00:47–00:51)

第二條線是操作。「我們想像人一樣操作真實世界的東西。這是 physical AI 現在最大的挑戰——機器人一般做不到這些事。我們希望能把燈泡鎖上去,而且它會亮。」

他的判斷:**現在的 foundation model 很會 reason、plan、act,但還不太會 react;而觸覺仍是被低估的模態。** 真正做機器人的人都知道這件事,但不少「AI 的 roboticist」會覺得靠 scaling 就能繞過去、不必真的理解真實世界的動態力學——「我不確定那是對的。」

他的立論是:人的智慧是雙程序的,我們需要的 agentic 系統應該是**雙程序甚至三程序**——一個 **slow-fast 架構**。**T-Rex**(與 NVIDIA 的同事合作)把這些想法一起實作:它同時是一個**資料集/資料收集方法**與一個**架構**,具備多程序/雙程序架構、觸覺感測與反應能力。

它學的是「什麼時候該根據觸感改變施力」:偵測滑動並在東西快掉下去時抓住、或只施加剛好足夠的壓力把一張牌從整副牌裡剝出來。平台是雙 Shadow Hand,頭部與手腕都有相機,畫面右下角即時顯示觸覺感測讀數。

展示的任務都是先前**沒有觸覺反應式策略就做不到**的:把牙膏從管子裡擠出來(「我們還沒要求機器人刷牙,也許下次」)、從一疊杯子裡分出兩個、**靠摸凹痕辨識是三種麻將牌中的哪一種**、抓鑰匙插進鎖孔並轉動、用滴管吸球擠出剛好的液量、從整副牌抽出一張、以及把燈泡鎖上去而不捏破。他特別強調:**前面示範用的蛋是真的生雞蛋,不是水煮蛋。**

他認為**資料集本身可能是這個計畫最重要的產出物**。

#### 推理:World Motion Models(約 00:51–00:54)

第三條線是「怎麼在很抽象的層次上做 3D 推理」。

他的切入點是一個對比:我們現在有很厲害的世界模型能**逐像素預測未來影片**,很棒——「但如果我只是想在車輪經過時調整上面某個東西、或像 F1 維修站那樣鎖緊輪上的一顆螺栓,**我不需要預測樹在做什麼**,我甚至不需要預測車子大部分的部位在做什麼。我要預測的是那個輪子的 affordance、幾何、以及它隨時間怎麼移動。」

於是有了 **World Motion Model**:一個建在**動態 3D 世界軌跡**上的模型,更精確地說是**建在 SE(3) 軌跡(也就是位姿)上的世界模型**。他的論點是:**物理世界有非常大一部分可以被抽象成剛體參考框隨時間的運動**,而這是第一個足夠一般的框架,能在這個表示上做預測、補完,以及後續的 MPC。

做法:把 **6 自由度的位姿 frame tokenize**,沿時間堆疊,並使用**多個參考框**——場景中每個物件或身體的每個剛體部位各對應一個。訓練方式是對序列做**去噪**;推論時可以

- 給定過去預測未來,
- 給定過去做**動作條件**的未來預測,
- 做 inpainting 或運動規劃,
- 做 retargeting、求解動力學等等。

架構是一個高效率的 transformer。示範包含用文字驅動機器人學出解某個任務的運動軌跡(直接生成,或搭配 motion predictive control),以及在 OMOMO 資料集上生成人與物件互動——為了完成對物件的操作任務,需要生成人形的整體運動;他們的模型在該資料集上優於 baseline,手與物件互動的情況也類似。

他總結說,這場給的是 BAIR 三個計畫的 teaser——分別對應**看、摸、以及在運動層次上推理真實世界**;World Motion Model「很快會上 arXiv」。

### 金句

> "We already have agents that can see, but they actually don't always see that well."(約 00:44)

整場第一個問題意識:能看 ≠ 看得好。

> "You probably didn't realize those two images were actually different… and that's exactly what we don't allow most visual encoder architectures to do."(約 00:45)

人類要來回比對才看得出差異,而我們卻不給編碼器這個機會。

> "Current foundation models can reason, they can plan, they can act, but they're still not so good at reacting."(約 00:48)

reason / plan / act / **react** ——最後一個是觸覺要補上的缺口。

> "I don't need to predict what the trees are doing."(約 00:51)

不必逐像素預測世界,才是 world motion model 的動機。

## English Notes

### TL;DR

- **Today's VLM visual encoders are stateless**: each image is encoded independently, so two nearly identical images produce the same caption. Their **Stateful Visual Encoder** adds cross-image attention in the encoder's middle layers, tuned specifically to preserve small state changes that would otherwise be attenuated away.
- **Touch is the underappreciated modality.** Foundation models reason, plan, and act well but still don't *react*. **T-Rex** pairs a slow-fast multi-process architecture with tactile sensing to peel a card off a deck, squeeze toothpaste, identify mahjong tiles by feel, insert and turn a key, handle raw eggs, and screw in a light bulb without cracking it.
- **A world model doesn't have to predict pixels.** The **World Motion Model** operates over **SE(3) pose trajectories**: tokenize 6-DoF pose frames, stack them over time with one reference frame per object or rigid body part, train by denoising, and get future prediction, action-conditioned prediction, inpainting/motion planning, and retargeting.

### Key Points

#### Seeing: Stateful Visual Encoders (~00:44–00:47)

He opened by crediting the previous talk — "Vincent's talk was the perfect precursor to mine, so I don't have to spend any time explaining why I'm interested in physical AI."

The problem is concrete: **we have agents that can see, but they don't always see well.** The visual encoders in today's VLMs and agentic VLMs are designed for internet vision tasks, and are not always well suited to physical AI tasks — or even to precise internet vision tasks.

His demonstration: two images run through the same encoder and LLM produce **the same caption**, and the audience themselves had to look back and forth to spot the difference. "And that's exactly what we don't allow most visual encoder architectures and VLMs to do."

Their fix is "so simple you'd be surprised it's novel": allow **cross-image weights in the encoder's middle layers**, tuned specifically to detect changes too small to survive in a normal representation. With that change encoder, the model can caption *what changed*, or tell whether a small box in a web interface has been checked — without a brute-force approach.

The paper compares several ways to build this, and reports significant improvements on **longitudinal medical report generation, image-editing control, and geospatial change detection.**

#### Feeling: T-Rex (~00:47–00:51)

"We want to manipulate things in the real world the way people can — a huge challenge of physical AI right now. Robots generally can't do these things. We want to be able to screw a light bulb in and have it turn on."

His diagnosis: current foundation models **reason, plan, and act, but are still not good at reacting**, and tactile remains an underappreciated modality. Real roboticists know this; a lot of "AI roboticists" assume you can scale your way out of it without understanding dynamic forces in the real world — "I'm not sure that's right."

Human intelligence is dual-process, so agentic systems should be dual- or triple-process: a **slow-fast architecture**. **T-Rex**, in collaboration with colleagues at NVIDIA, embodies all of this — it is both a dataset/data-collection effort and an architecture with multi-process control, tactile sensing, and reactivity.

What it learns is *when to change force based on what it feels*: adjusting for slip to catch something about to fall, or applying just enough pressure to peel one card off a deck. The platform is two Shadow Hands with head- and wrist-mounted cameras, with the tactile sensor readout visible in the lower-right tile of the demo video.

The demonstrated tasks were previously impossible without tactile reactive policies: squeezing toothpaste out of a tube ("we did not actually yet ask the robot to brush its teeth — maybe next time"), separating two cups out of a stack, **identifying which of three mahjong tile types it holds purely from the feel of the indentations**, inserting a key into a lock and twisting it, squeezing a pipette bulb to dispense the right amount of liquid, extracting a card from a deck, and screwing in a light bulb with enough pressure not to crack it. He noted the eggs shown earlier were **real eggs, not hard-boiled.**

He suggested the **dataset may be the single most important artifact** of the project.

#### Reasoning: World Motion Models (~00:51–00:54)

The framing is a contrast with pixel-space world models. We now have impressive models that predict every pixel of the future — wonderful — "but if I just want to adjust something on that wheel as it goes by, or tighten a bolt on the wheel like an F1 pit crew, **I don't need to predict what the trees are doing.** I don't even need to predict what much of the car is doing. I want to predict the affordance, or the geometry, or how that wheel is moving over time."

Hence the **World Motion Model**: a model of dynamic 3D world trajectories — more precisely a world model **over SE(3) trajectories**, i.e. poses. His claim is that **much of the physical world can be abstracted as the motion of rigid frames evolving over time**, and this is the first sufficiently general framework for predicting and completing over that representation (and eventually running MPC on it).

Mechanically: **tokenize the 6-DoF pose frame**, stack it over time, with **multiple reference frames** — one per object or per rigid portion of a body in the scene. Train by **denoising sequences**. At inference, predict the future given the past, predict the future conditioned on actions, inpaint or motion-plan, retarget, or solve for dynamics. The backbone is an efficient transformer.

Demos included text-driven generation of robot motion trajectories to solve a task, either directly or via motion predictive control, and human-object interaction on the OMOMO dataset — generating whole-body humanoid motion to perform a manipulation task on an object, where their model outperforms baselines, with similar results for hand-object interaction.

He closed by describing the talk as a teaser for three BAIR projects that **see, feel, and reason in motion about the real world**; World Motion Models "will be on arXiv soon."

### Quotes

> "We already have agents that can see, but they actually don't always see that well." (~00:44)

Seeing is not the same as seeing well.

> "You probably didn't realize those two images were actually different… and that's exactly what we don't allow most visual encoder architectures to do." (~00:45)

Humans need to look back and forth to catch the difference; encoders are never given the chance.

> "Current foundation models can reason, they can plan, they can act, but they're still not so good at reacting." (~00:48)

Reason / plan / act / **react** — the last is what tactile sensing supplies.

> "I don't need to predict what the trees are doing." (~00:51)

The motivation for modeling motion instead of pixels, in one line.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Stateful Visual Encoders (SVE) | 在視覺編碼器中層加入跨圖注意力,保留細微狀態改變 | Cross-image attention in the encoder's middle layers to preserve small state changes | arXiv 2606.04433;UC Berkeley — [statefulvisualencoders.github.io](https://statefulvisualencoders.github.io/) |
| T-Rex | Tactile-Reactive Dexterous Manipulation:觸覺反應式靈巧操作的資料集與架構 | Dataset + architecture for tactile-reactive dexterous manipulation | arXiv 2606.17055;UC Berkeley × NVIDIA(外部資料另列 Stanford)/ also lists Stanford — [tactile-rex.github.io](https://tactile-rex.github.io/) |
| World Motion Model | 建在 SE(3) 位姿軌跡上的世界模型,以去噪訓練,支援預測/規劃/retargeting | World model over SE(3) pose trajectories, trained by denoising; supports prediction, planning, retargeting | 演講時尚未上 arXiv(「will be on arXiv soon」)/ not yet on arXiv at talk time |
| Shadow Hand | T-Rex 使用的靈巧手平台(雙手) | The dexterous hand platform used in T-Rex (two hands) | 逐字稿誤聽為 "sharper hand" / heard as "sharper hand" |
| OMOMO | 人與物件互動的運動資料集,用於 World Motion Model 示範 | Human-object interaction motion dataset used in the World Motion Model demos | 逐字稿聽成 "ammono",拼法待確認 / heard as "ammono", spelling to verify |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Trevor Daryl | Trevor Darrell |
| sharper hand | Shadow Hand |
| Bear | BAIR(Berkeley AI Research) |
| BLMs | VLMs |
| dnoising | denoising |
| endeector | end effector |
| ammono data set | OMOMO dataset(待確認 / to verify) |

## 待確認 / To Verify

- 人與物件互動示範所用的資料集,字幕聽成 "ammono",推測為 **OMOMO**,需看投影片確認。/ The human-object interaction dataset heard as "ammono" — likely **OMOMO**, needs slide confirmation.
- World Motion Model 的正式論文名稱與 arXiv 編號(演講當下尚未公開)。/ The formal paper title and arXiv ID for World Motion Models (not public at talk time).
- T-Rex 的合作單位:他台上只提 NVIDIA,論文另列 Stanford,實際列名以論文為準。/ He credited only NVIDIA on stage; the paper also lists Stanford — defer to the paper.
