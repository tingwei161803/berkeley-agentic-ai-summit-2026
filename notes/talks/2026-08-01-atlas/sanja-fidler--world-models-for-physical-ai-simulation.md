---
title: "World Models for Physical AI Simulation"
title_zh: "用於 Physical AI 模擬的世界模型"
speaker: "Sanja Fidler"
affiliation: "Associate Professor, University of Toronto; Former VP of AI Research, Nvidia"
type: keynote
stage: Atlas
date: 2026-08-01
session: "Session 1: Foundational Capabilities"
video: "https://www.youtube.com/watch?v=WeriQic-QW0&t=1069s"
video_range: "00:17:49–00:32:35"
transcript: "tmp/[English (auto-generated)] Atlas Stage - August 1st - Morning Session [DownSub.com].srt"
status: draft
tags: [world-models, physical-ai, simulation, autonomous-driving, video-generation]
---

# 用於 Physical AI 模擬的世界模型(World Models for Physical AI Simulation)

**一句話總結**:機器人開發的瓶頸不是模型而是模擬——真實機器人只能以物理時間跑,而生成式世界模型能在 GPU 上以超即時速度「想像」出無限多的長尾場景;過去一年這項技術從「5 秒影片要跑 5 分鐘」變成「即時互動」,現在連消費級顯示卡都跑得動。

**One-line summary**: The bottleneck in robotics isn't the policy, it's simulation — real robots run at physical time, while generative world models can *imagine* unlimited long-tail scenarios on GPUs faster than real time; in one year this went from "5 seconds of video per 5 minutes of GPU time" to real-time interactive, and now runs on a consumer GPU.

## 中文筆記

### TL;DR

- **開場說明**:她昨天才宣布離開 Nvidia,現在的身分是 University of Toronto 的「平民」(civilian);Nvidia 大方讓她把投影片帶走,所以講的仍是 Nvidia 的工作。
- **這場不談 agentic AI,談 world models**——她認為這是六年來最讓她興奮的技術,而且「已經在轉角了」。
- **模擬是機器人學的基礎建設**:LLM 評估只要 sample 一段文字;機器人評估必須把 policy 部署到真實機器人上閉環跑。真機受限於**物理時間**且要買很多台;虛擬機器人只受限於**計算時間**,而計算會越來越快,擴張只需加 GPU。
- **模擬技術的三代**:(1) 圖學+美術手工建模——測 SF 某條街要一兩個月的美術工時;(2) 2020 年起的 NeRF / Gaussian splatting——從真實錄影直接重建成模擬環境,內容問題被解決,Nvidia 曾靠此**每天跑 200 萬次自駕模擬**;(3) 生成式 world models——純資料驅動,可以「幻想」出從沒錄到的長尾場景。
- **她定義的 world model 是「互動式」的**:不是 text-in / 5 秒影片 out,而是有人或機器人軟體在迴圈裡,每一格畫面都由模型即時生成。這就是 **OmniDreams**,而且它跑即時。
- **一年的進展曲線**:2025 年 3 月,5 秒片段要 5 分鐘 GPU 時間;2026 年 3 月,即時互動;兩個月後的 CVPR(6 月),已經能在 RTX 5090 這種消費級卡上跑——「等於一個可以裝進背包的遊戲引擎」。
- **最讓她興奮的結果**:把**生產環境的 driving policy** 直接插進這個生成世界裡開,policy 把模擬世界跟真實世界搞混了——這代表畫質已經達到「可用」的門檻。

### 重點整理

#### 從 ChatGPT 到 agentic AI 再到 physical AI(約 00:18–00:19)

她把 AI 的演進切成三段:2022 年 ChatGPT 讓全世界第一次真正認識 AI(「連我媽都知道 ChatGPT」);現在是 agentic AI 的時代,人人都在用 agent(「我無法想像沒有 agent 的生活」);下一個斷點是 **physical AI**——智慧下放到邊緣、進到各行各業的機器人裡,可能發生在未來十年甚至更久,取決於你要的是哪種機器人。

她在 Nvidia 的團隊聚焦在其中一種機器人:**自駕車**,今天就用它當例子;但通用機器人才是當下最熱、最被期待「一台做很多事」的方向。

#### 機器人軟體的世代演進(約 00:20)

以車為例:非常簡單的視覺 → 手寫規則 → 每個環節(感知、預測、規劃)都用機器學習 → 最近的 end-to-end 系統(sensor 進、規劃軌跡出)→ 正在來的新世代:**利用大規模預訓練的 foundation model**,帶著「世界如何運作」的龐大知識與各種真實世界難以蒐集的 corner case,而且會推理。「大家真的認為 foundation model 是解決最後一哩 corner case 的 game changer。」

#### 為什麼模擬是機器人的基礎建設(約 00:21–00:23)

- **LLM 的開發迴圈**:訓練很多模型,要評估好壞就 sample 一段文字來看,必要時還找人互動評估對話。
- **機器人的開發迴圈**:軟體(機器人的大腦)必須部署到真實機器人上**閉環**執行任務,再由人觀察表現。(她用網路上抓的 Skild AI pick-and-place 影片示範。)
- **替代方案**:讓虛擬機器人在雲端的 digital twin 裡做同樣的 pick-and-place,一樣能得到「哪個 policy 比較好」的良好訊號,而且可以更可規模化地訓練。
- **關鍵論點**:真機路線的上限是**物理時間**——現實世界沒辦法跑得比物理時間快,要測很多場景就得買很多台機器人;雲端路線的上限是**計算時間**——電腦越來越快,可以跑得比真實時間更快,而且是靠跨 GPU 擴張而不是靠買機器人。「所以這是一條可規模化得多、多、多的 pipeline。」
- 結論:「我真的不認為沒有非常非常好的模擬,你能發展出機器人學。」

#### 模擬的三個世代(約 00:23–00:25)

1. **圖學時代**:美術師手刻 3D asset、寫行為模型、寫 ray tracing 方程式。能用,但極度耗時——「如果我想在舊金山某條街測我的車,那就是一到兩個月的美術工時去做那個 digital twin。」
2. **NeRF / Gaussian splatting(2020 年左右)**:完全改變賽局。可以從真實機器人的錄影直接得到模擬環境(雖然受限於重建、只能重現錄到的東西)。**內容問題被解決了**:真實錄影 → 模擬環境 → 部署新版軟體 → 跑新的閉環 rollout。做法是重建表面(供碰撞偵測)+ splats(空間中的外觀 blob,決定不同視角怎麼 render)。**在 Nvidia,他們靠這套每天跑 200 萬次自駕軟體模擬。**
3. **生成式 world models**:重建法受限於「你錄到了什麼」,但機器人的難題正好在長尾——那些極難見到、卻必須測試與訓練的情況。所以重點是**想像**這些困難案例。World model 是純資料驅動的 AI,沒有人在手工做內容,上限只剩資料;於是你可以幻想新場景、寫出任何你想像得到的困難 edge case。

#### 生成式 world model 能做什麼(約 00:26)

- **極端場景生成**:惡劣天候、完整生成的車禍場景(「那支影片裡沒有人受傷,那是完全生成的事故」)——正是你想拿來測軟體的情況。
- **改變視角 ≈ 改變 embodiment**:從低底盤跑車換到卡車視角,可以跨不同車型測試,「超級重要」。
- **編輯**:生成模型很容易做、重建法很難做的事——直接下 text prompt 就能用各種方式改寫場景。

#### 她心中的 world model:互動式(約 00:26–00:27)

「我今天講的 world model 有一個特定架構,而且它是**互動式**的。不是輸入文字、輸出五秒影片;而是迴圈裡有一個使用者或一套機器人軟體。」

第一個使用者是她「最喜歡的人」——模型一做出來,她就跑去對方辦公室,讓他拿真的方向盤試開。那個 demo 裡,人在開車,而**你看到的每一格畫面都是 world model 完全生成的**。這個模型叫 **OmniDreams**,而且附帶紅利:**它跑即時**。

「模擬一定要即時嗎?不一定。它只需要有非常高的 throughput——但即時是很棒的紅利。」

#### 怎麼做出來的(約 00:27–00:29)

四個步驟:

1. **Base model**:一個預訓練的影片生成模型(通常是 diffusion),吃幾張雜訊 frame、denoise 成幾秒影片——**雙向 attention**。預訓練資料是大量公開網路資料。
2. **Domain post-training**:轉進特定機器人領域(例如 AV),而且不只是「路上發生的事」,是**機器人捕捉到的路上發生的事**——通常不只一台相機,而是多台。
3. **改架構讓它互動**:改成 **causal** 架構,一格一格生成而不是一次一小段影片,並把 action 放進迴圈。
4. **效率**:diffusion 通常要很多步,太慢;把它蒸餾成極少步的模型,再用書上所有技巧做即時實作——這就是 **FlashDreams**,已經釋出,而且可以掛在不同架構的 world model 上。

Demo:有人在開車,右邊是實際被操作的方向盤,而每一格畫面都不是真實世界,全是生成的。物理只有很簡單的地面物理——確保車一直貼在地面、能開過減速丘;但沒有對路面以外更複雜的場景做碰撞偵測,所以「你可以直接開進一間餐廳,沒問題」。

#### 技術演進速度:一年的曲線(約 00:30)

- **2025 年 3 月**:生成 5 秒片段要大約 5 分鐘 GPU 時間。「顯然不實用。」
- **2026 年 3 月**:快轉一年,**即時互動**。
- **2026 年 6 月(CVPR)**:再兩個月,他們讓它跑在 **RTX 5090** 這種消費級 GPU 上。「基本上就是一個可以裝進背包的遊戲引擎。」

「這就是我說『已經在轉角了』的意思。」

#### 結果與那個「最讓我興奮」的時刻(約 00:30–00:32)

- 只給一段 text prompt 或一張 first frame,就能得到複雜得多的目標場景。「圖學引擎做不到,現象太多太雜;重建法也很難生成出來。」
- **多感測器**:必須同時生成機器人身上的多個感測器輸出。
- **編輯同一個環境**:改天候、改光照條件;畫面裡那條綠色軌跡,是**機器人 policy 在這個生成世界裡開出來的**。
- **關鍵時刻**:「我對這個結果超級興奮,因為我們把**生產環境的 policy** 插進去,它就在這個世界裡開起來了。它把這個模擬世界跟真實世界搞混了——那基本上代表你的品質門檻已經到了你真正需要的水準。」
- **長尾的證明**:她請團隊生成一些酷例子——「Nvidia 從來沒有在路上拍到過大象,但我們可以生成它」,這正好證明了長尾那一點。
- **結尾 demo**:左邊是真人在開,每一格都是生成的;右邊那個轉動的方向盤,是**機器人軟體**在操作,在這個三相機的 world model 裡開車。

### 金句

> "I actually no longer [work at] Nvidia. I just announced it yesterday. … Today I'm a civilian [at] University of Toronto and I'll let you speculate about my next steps."(約 00:18)

演講第一句話就是新聞。

> "In the real world we cannot run faster than the physical time. … On the other hand we're bounded by compute time — computers are getting better and better, we can actually run faster than real time, and we just scale across GPUs instead of robots."(約 00:22)

整場的核心論證:機器人的規模化路徑必須離開物理時間。

> "It's confusing this simulated world with the real world, which basically means that your quality bar is at the level that you actually need."(約 00:31)

判斷模擬「夠不夠好」的最務實標準:生產環境的 policy 分不出差別。

> "Even though Nvidia has never captured an elephant on the road, we can actually generate it."(約 00:31)

長尾問題的一句話說明。

## English Notes

### TL;DR

- **Opening news**: she announced her departure from Nvidia the day before; she's now "a civilian at University of Toronto" and invited the room to speculate about her next steps. Nvidia let her keep most of the deck, so the work shown is Nvidia's.
- **Not a talk about agentic AI** — about world models, the technology she's found most exciting for six years and which is now "around the corner."
- **Simulation is robotics' foundational infrastructure.** Evaluating an LLM means sampling text; evaluating a robot means deploying the policy on hardware in closed loop. Real robots are bounded by *physical time* and require buying more robots; virtual robots are bounded by *compute time*, which keeps getting cheaper and scales across GPUs.
- **Three generations of simulation**: (1) handcrafted graphics — one to two months of artist time to build a digital twin of a single San Francisco street; (2) NeRF and Gaussian splatting from ~2020 — real capture straight to simulation environment, which solved the content problem and let Nvidia run **two million autonomous-driving simulations per day**; (3) generative world models — purely data-driven, able to hallucinate the long tail nobody ever recorded.
- **Her definition of a world model is interactive**: not text in, five seconds of video out, but a human or a robotic policy in the loop with every single frame generated live. That system is **OmniDreams**, and it runs in real time.
- **The one-year curve**: March 2025, five seconds of video per five minutes of GPU time; March 2026, real-time interactive; two months later at CVPR, running on an RTX 5090 — "literally a game engine you can have in a backpack."
- **Her favorite result**: dropping the **production driving policy** into the generated world and having it drive — the policy confuses the simulated world with the real one, which is exactly the quality bar you need.

### Key Points

#### From ChatGPT to agentic AI to physical AI (~00:18–00:19)

Three eras: ChatGPT in 2022, when AI reached the masses for the first time ("my mom knew about ChatGPT"); today's agentic AI, which she can no longer imagine working without; and the next break point, **physical AI**, where intelligence moves to the edge and into robots across industries — perhaps a decade out, depending on which robot you're waiting for. Her group at Nvidia focused on one particular robot, the autonomous vehicle, which serves as the running example; general-purpose robotics is the hot upcoming field.

#### Generations of robot software (~00:20)

For a car: simple vision → hardcoded driving rules → machine learning at every stage (perception, prediction, planning) → recent end-to-end systems that map sensor data to a planned trajectory → and the emerging generation built on large pre-trained foundation models, which carry vast knowledge of how the world works, cover corner cases that are nearly impossible to collect in the real world, and can reason. The field genuinely believes foundation models are the game changer for that last mile of corner cases.

#### Why simulation is the infrastructure (~00:21–00:23)

The LLM development loop is cheap: train models, sample text, evaluate, sometimes with a human in the loop for conversation. The robotics loop is not: the robot's brain must be deployed on real hardware in closed loop and observed (she showed a Skild AI pick-and-place clip pulled from the internet). The alternative is a virtual robot in a cloud digital twin doing the same pick-and-place — which gives a genuinely useful signal about which policy is better, and scales training far more cheaply.

The argument that carries the talk: real-world development is bounded by physical time, and there's no running faster than physics, so scaling scenario coverage means buying more robots. Cloud development is bounded by compute time — and compute keeps getting faster than real time, and scales across GPUs instead of robots. "So it's a much, much, much more scalable pipeline." Her conclusion: you cannot develop robotics without really, really good simulation.

#### Three generations of simulation (~00:23–00:25)

1. **Graphics**: artists carved out 3D assets, wrote behavior models, wrote the ray-tracing equations. It worked, but testing a car on a specific San Francisco street cost one to two months of artist time to build that digital twin.
2. **NeRF and Gaussian splatting (~2020)**: a complete game changer, because you could go from a real-world recording captured on a robot straight to a simulation environment — with the restriction that reconstruction only gives you what was actually observed. Pipeline: capture → surface reconstruction for collision checking → splats (little appearance blobs in space) telling you how to render new viewpoints. At Nvidia, this powered **two million autonomous-driving simulations per day**.
3. **Generative world models**: reconstruction is bounded by what you recorded, and robotics lives in the long tail — the stuff that's so hard to see and that you most need to test and train on. So it's all about *imagining* the hard cases. World models are purely data-driven AI, no human crafting content, so the only limit is data.

#### What generative world models buy you (~00:26)

- **Hard scenarios on demand**: rough weather, a fully generated collision ("no one got hurt in that video — it was a completely generated accident"), exactly the cases you want to test software against.
- **Viewpoint changes ≈ embodiment changes**: going from a low sports car to a truck, which matters enormously for testing across vehicles.
- **Editing**: trivial with generative models and much harder with reconstruction — a text prompt is enough to rewrite the scenario.

#### The specific architecture: interactive (~00:26–00:27)

"There's a specific architecture I have in mind when I talk about world models today, and it's interactive." Not text in, five seconds of video out — there is a user or a robotic policy in the loop.

Her first user was "my favorite human": as soon as the model was working, she walked into their office and had them try it with a real steering wheel. A human drives, and every single frame is generated by the world model. That model is **OmniDreams**, and the bonus is that it runs real time. "Does simulation need to run real time? Not necessarily — it just needs really high throughput. But real time is a great bonus."

#### How it's built (~00:27–00:29)

1. **Base model**: a pre-trained video generation model, typically diffusion — noisy frames denoised into a few seconds of video, with bidirectional attention, pre-trained on vast publicly available internet data.
2. **Domain post-training**: adapt to a specific robotic domain such as AV — and not just "stuff that happens on the road" but stuff *as captured by a robot*, which usually means many cameras rather than one.
3. **Make it interactive**: switch to a **causal** architecture that generates frame by frame with actions in the loop, rather than short video snippets at a time.
4. **Make it efficient**: distill the many-step diffusion model down to a few steps, then apply every trick in the book for a real-time implementation. That stack is **FlashDreams**, which has been released and can be plugged into different world-model architectures.

In the demo, physics is deliberately minimal — ground physics only, so the car stays on the ground and rides over speed bumps, but there's no collision checking beyond the road surface, so "you can actually go through a restaurant, no problem."

#### The one-year trajectory (~00:30)

March 2025: five-second clips at roughly five minutes of GPU time each — clearly impractical. March 2026: real-time interactive. June 2026 at CVPR, two months later: running on an **RTX 5090**, a consumer-grade GPU — "literally a game engine that you can have in a backpack." That slope is why she says the technology is around the corner.

#### Results, and the moment she cared about most (~00:30–00:32)

From a text prompt or a single first frame you get scenes far more complex than a graphics engine could produce — too many simultaneous phenomena — and that reconstruction techniques struggle to generate too. The model produces the **multiple sensor streams** a real robot carries. Editing the same environment changes weather and lighting, and the little green trajectory on screen is the **robot's own policy driving through the generated world**.

That was her favorite result: they plugged in the **production policy** and it drove. "It's confusing this simulated world with the real world, which basically means that your quality bar is at the level that you actually need." And on the long tail: "Even though Nvidia has never captured an elephant on the road, we can actually generate it." The closing demo showed a person driving on the left while on the right the *robotic software* turns the wheel, driving inside a three-camera world model — every frame generated, all in real time.

### Quotes

> "I actually no longer [work at] Nvidia. I just announced it yesterday. … Today I'm a civilian [at] University of Toronto and I'll let you speculate about my next steps." (~00:18)

The talk opened with news.

> "In the real world we cannot run faster than the physical time. … On the other hand we're bounded by compute time — computers are getting better and better, we can actually run faster than real time, and we just scale across GPUs instead of robots." (~00:22)

The core argument: robotics scales only by leaving physical time behind.

> "It's confusing this simulated world with the real world, which basically means that your quality bar is at the level that you actually need." (~00:31)

The most practical test of whether a simulator is good enough: the production policy can't tell.

> "Even though Nvidia has never captured an elephant on the road, we can actually generate it." (~00:31)

The long-tail problem in one sentence.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| OmniDreams | Nvidia 的即時互動式生成世界模型,用於自駕閉環模擬 | Nvidia's real-time interactive generative world model for closed-loop AV simulation | arXiv 2606.03159;已開源(github.com/nv-tlabs/omni-dreams);外部資料顯示其 base model 為 Cosmos diffusion,並在 21k 小時駕駛資料上做 mid/post-training |
| FlashDreams | 互動式自迴歸影片 / world model 的高效能推論與服務函式庫 | High-performance inference & serving library for interactive autoregressive video and world models | github.com/NVIDIA/flashdreams;可掛在不同 world model 架構上 |
| NeRF / Gaussian splatting | 2020 年起讓「真實錄影 → 模擬環境」成為可能的重建技術 | Reconstruction techniques that turned real capture into simulation environments from ~2020 | Nvidia 靠此每天跑 200 萬次自駕模擬 |
| Skild AI | 講者引用的真實機器人 pick-and-place 示範影片來源 | Source of the real-robot pick-and-place clip she showed | 逐字稿聽成 "Skilled AI",拼法待確認 |
| RTX 5090 | 消費級 GPU,CVPR(2026/6)時 world model 已能在其上執行 | Consumer-grade GPU running the world model as of CVPR (June 2026) | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Sonia Diddler / Sonia | Sanja Fidler |
| invidia / Invidia | Nvidia |
| Chad GPT | ChatGPT |
| nerf agotion splats | NeRF / Gaussian splats |
| unifor splat | (uniform) splats |
| omnidreams | OmniDreams |
| flash dreams | FlashDreams |
| birectional | bidirectional |
| den noiseise / dnoising | denoise / denoising |
| gamecher | game changer |
| an navie / a navy | AV(autonomous vehicle) |
| reconstruction tag / construction tech | reconstruction tech |
| posturing | post-training |

## 待確認 / To Verify

- 「my favorite human」是誰:她說模型一做好就去對方辦公室、用真方向盤試開,字幕在此漏字("my favorite human at was actually our first user"),推測是 Nvidia 內部的人,但**未確認**。/ Who "my favorite human" is — the caption drops the name; likely someone at Nvidia, unconfirmed.
- "Skilled AI" 的正確公司名(推測為 Skild AI,做通用機器人 foundation model),需看投影片確認。/ Correct spelling of the robotics company (likely Skild AI) — check the slide.
- 「每天 200 萬次模擬」的年份與範圍(是重建式模擬時代的數字,對應約 2024–2025)。/ The year/scope of the "two million simulations per day" figure — it belongs to the reconstruction era.
- OmniDreams 的 base model 在演講中只說是「a pre-trained video generation model」,未點名 Cosmos;表中的 Cosmos 資訊來自論文而非演講。/ She didn't name Cosmos on stage; that attribution comes from the paper, not the talk.
- 「5 秒片段 / 5 分鐘 GPU 時間」的 GPU 型號與 batch 條件未說明。/ The GPU model and batching behind the "5 seconds per 5 minutes" figure were not stated.
