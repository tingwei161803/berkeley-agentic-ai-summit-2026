---
title: "Scaling Sidewalk Autonomy with World Models"
title_zh: "用世界模型擴展人行道自主性"
speaker: "Bolei Zhou"
affiliation: "Associate Professor, UCLA; Chief AI Scientist, Coco Robotics"
type: talk
stage: Atlas
date: 2026-08-01
session: "Session 2: Robotics & World Models"
video: "https://www.youtube.com/watch?v=psPzCQbjCCo&t=3885s"
video_range: "01:04:45–01:13:53"
transcript: "tmp/[English (auto-generated)] Atlas Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [sidewalk-robots, world-models, sim-to-real, gaussian-splatting, coco-robotics]
---

# 用世界模型擴展人行道自主性(Scaling Sidewalk Autonomy with World Models)

**一句話總結**:人行道自主性的瓶頸不是模型不夠多,而是**沒辦法在部署前公平評估它們**;而解法是把真實世界的影片當成「原始碼」,重建成可互動的模擬環境,再從一支影片長出多個「數位表親」來訓練與評估。

**One-line summary**: The bottleneck in sidewalk autonomy isn't a shortage of models — it's having no fair way to evaluate them before deployment; the fix is to treat real-world video as source code, reconstruct it into interactive simulation, and grow many "digital cousins" from a single clip for training and evaluation.

## 中文筆記

### TL;DR

- **人行道自主性比道路自主性更難的地方在於約束**:單一 RGB 相機、有限算力與電力,卻要處理各種天候光照、與行人及動物做**社交合宜**的互動(例:繞過躺在人行道上的狗而不踩到牠的尾巴)。
- **評估才是瓶頸**:sidewalk foundation model 已經很多(他的實驗室與其他實驗室都有),但**部署前要怎麼公平比較?** 他們先做了 **SidewalkBench**(建在 NVIDIA Omniverse / Isaac Sim 上),但圖形引擎的視覺真實感不足,仍有 scene-to-real gap。
- **解法是把真實影片當原始碼**:**Vid2Sim**(CVPR)把人行道影片重建成 Gaussian splatting,再放進物理引擎,得到資料驅動的模擬;在其中用 RL 訓練後可**零樣本遷移**到真實世界,因為訓練與部署之間**沒有視覺落差**。
- **一支影片不能只長出一個環境**:**UrbanVerse** 從單支影片抽出 **scene graph**,替換不同物件實例,產生多個**digital cousins**(相對於一對一的 digital twin);同時釋出 **10 萬個帶正確尺度的 3D 資產**。
- **成果**:**FlowPilot** 用單一 RGB 相機輸出 waypoint 完成真實人行道導航;並且能**跨載體遷移而不必微調**——已在足式機器人上驗證,正在推進輪足機器人與電動輪椅。「未來我們不只能自主外送食物,也能自主載送人。」

### 重點整理

#### 問題:人行道自主性是另一種自主性(約 01:05–01:07)

他先開了個玩笑:台上前面幾位分別來自 UC Berkeley、UC San Diego,加上他的 UCLA——「不如來辦一個 UC AI Summit?」

接著把場景拉開:大家熟悉的是**道路自主性**(前一位講者剛談過),全尺寸車輛在城市裡跑;但都市環境裡還有另一種自主性,他稱為 **sidewalk autonomy**。Coco Robotics 是一家做**最後一哩食物外送**的新創,有**數百台機器人**在跑這個任務。

跟道路自主性相比,人行道的處境更雜:

- 要非常小心地在人行道上導航、避開障礙物碰撞;
- 要處理**所有**天候與光照條件;
- 人行道**本來就是為人設計的**,所以機器人必須與行人、動物等動態 agent 做**社交合宜**的互動。他放了自己很喜歡的一段影片:一隻狗躺在人行道上,機器人必須非常小心地繞過去、**不能壓到狗的尾巴**,同時完成導航任務。

而且機器人工作在**算力與電力受限**的環境:「我們只被允許用單一 RGB 相機來做導航。」

#### 瓶頸:模型很多,但沒辦法在部署前評估(約 01:07–01:09)

近年人行道導航的 AI 模型不少,主要靠**模仿學習**從人類示範中學,他的實驗室與其他實驗室都貢獻了一些;這些模型訓練在影片示範上,跨條件泛化得不錯。

但問題來了:**面對這麼多不同的 sidewalk foundation model,真實世界部署前要怎麼 benchmark 它們?**

他們的第一步是 **SidewalkBench**:在模擬中評估導航策略,環境用 **NVIDIA Omniverse 與 Isaac Sim** 建。它能比較不同模型如何與人互動、如何避免碰撞。**但仔細看就會發現,圖形引擎建出來的模擬仍然缺乏視覺真實感**——跟真實部署之間存在 scene-to-real gap,而這個 gap 會讓評估不公平。

#### 解法一:把真實影片當原始碼(Vid2Sim)(約 01:09–01:10)

他們的解法是**從真實世界影片建構世界模擬**:「我們想把真實世界影片當成 source code,用它來建這個評估 benchmark。」

**Vid2Sim**(發表於 CVPR)的流程:拿一段在人行道上行走的影片 → 從影片建 **Gaussian splatting 重建** → 把 splat 放進**物理引擎** → 得到資料驅動的模擬環境 → 在其中訓練與評估人行道機器人。

他放的 demo 顯示用**強化學習**在其中訓練 agent,訓練完的模型可以**零樣本遷移到真實世界**——原因很直接:**訓練環境與部署環境之間幾乎沒有視覺落差。** 有了這種環境,就能評估各種人行道導航策略在不同情況下的表現。

#### 解法二:從一支影片長出多個環境(UrbanVerse)(約 01:10–01:12)

但這種影片重建有個限制:**一支影片只能重建出一個環境**。理想上我們希望從同一支影片產生多種變化。

這是 **UrbanVerse** 的動機:從單支影片產生多個 **digital cousins**。他把兩個概念分清楚:**digital twin** 是一支影片對應一個模擬環境;**digital cousins** 則是同一來源長出的多種變體。做法是用電腦視覺技術從輸入影片中**抽出 scene graph**,再**替換不同的物件實例**,就能生出不同版本的環境,每個都能拿來訓練與評估。

UrbanVerse 已公開釋出,同時釋出一個**大規模 3D 資產庫:10 萬個帶有正確尺度的資產**。

他們也建了**用模擬做後訓練**的流程:先用影片以模仿學習訓練模型,再把模型放進模擬環境中做後訓練,**提升它的互動性與反事實推理能力**。

#### 成果:FlowPilot 與跨載體遷移(約 01:12–01:13)

累積這些進展後的近期成果是 **FlowPilot**:在真實世界用**單一 RGB 相機**完成人行道導航。機器人只有一台 RGB 相機,模型輸出 **waypoint**,控制器執行下一個點。展示中機器人能處理困難的人行道場景——避開障礙物、與行人適當互動。

另一個他認為很令人興奮的方向是**跨載體(cross-embodiment)遷移或部署**:既然有了人行道導航的 foundation model,他們的研究能**在不微調的情況下**把模型遷移到不同的機器人本體。示範影片顯示模型在**足式機器人**上運作良好;還有許多進行中的研究要遷移到其他人行道機器人,例如**輪足機器人**與**電動輪椅**。

他的結語:「所以未來我們不只能自主外送食物,**我們也能在人行道上自主載送人。**」benchmark 與程式碼都已在他們的網頁上釋出。

### 金句

> "We want to use real world videos as a source code to build up this evaluation benchmark."(約 01:09)

把影片當「原始碼」,是整場方法論的核心比喻。

> "There is no visual gap between the training environment and the deployment."(約 01:10)

零樣本遷移為什麼成立的一句話解釋。

> "In the future, not only we can autonomously deliver the food, we can also autonomously deliver the people on the sidewalk."(約 01:13)

跨載體遷移的終點:從外送包裹到載送人。

## English Notes

### TL;DR

- **What makes sidewalks harder than roads is the constraint budget**: a single RGB camera, limited compute and battery, yet the robot must handle all weather and lighting and interact in a **socially compliant** way with pedestrians and animals — including navigating around a dog lying on the sidewalk without stepping on its tail.
- **Evaluation is the bottleneck**, not model supply. Plenty of sidewalk foundation models exist (from his lab and others), but there was no fair way to compare them before deployment. Their first attempt, **SidewalkBench**, is built on NVIDIA Omniverse and Isaac Sim — but graphics-engine simulation still lacks visual realism, leaving a scene-to-real gap.
- **The fix is to treat real video as source code**: **Vid2Sim** (CVPR) reconstructs sidewalk footage into Gaussian splats, drops them into a physics engine, and yields data-driven simulation. RL agents trained there **transfer zero-shot** to the real world because there is essentially no visual gap between training and deployment.
- **One video shouldn't yield only one environment**: **UrbanVerse** extracts a **scene graph** from a single clip and swaps in different object instances to produce many **digital cousins** (as opposed to a one-to-one digital twin), alongside a released library of **100,000 correctly-scaled 3D assets**.
- **The payoff**: **FlowPilot** does real-world sidewalk navigation from a single RGB camera by emitting waypoints, and the policy **transfers across embodiments without fine-tuning** — demonstrated on legged robots, with wheeled-legged robots and electric wheelchairs in progress.

### Key Points

#### Sidewalk autonomy is its own problem (~01:05–01:07)

He opened with a joke about the lineup — UC Berkeley, UC San Diego, and his own UCLA: "How about having a UC AI summit?"

Most people know **road autonomy**, which the previous speaker had just covered: full-size vehicles running around cities. But urban environments have a second kind of autonomy he calls **sidewalk autonomy**. Coco Robotics runs last-mile food delivery with **hundreds of robots** doing this today.

Compared to road autonomy, sidewalks bring harder settings: careful navigation and collision avoidance in tight space; all weather and lighting conditions; and — because sidewalks were designed for people — the requirement to interact in a **socially compliant** way with dynamic agents including pedestrians and animals. His favorite clip shows a dog lying across the sidewalk, with the robot threading past **without stepping on the dog's tail.**

And all of it under compute and battery constraints: "we're only allowed to use a single RGB camera to do the navigation."

#### The bottleneck: many models, no way to evaluate before deployment (~01:07–01:09)

Recent years have produced many sidewalk navigation models, largely via **imitation learning** from human demonstrations — some from his lab, some from others. Trained on video demonstrations, they generalize well across conditions.

That creates the problem: **given so many different sidewalk foundation models, how do you benchmark them before real-world deployment?**

Their first answer was **SidewalkBench**, evaluating navigation policies in simulation, with environments built in **NVIDIA Omniverse and Isaac Sim**. It compares how models interact with people and avoid collisions. But look closely and the graphics-engine simulation **still lacks visual realism** — a scene-to-real gap that makes the comparison unfair.

#### Fix 1: real video as source code — Vid2Sim (~01:09–01:10)

Their solution is to create world simulation from real-world video: "we want to use real world videos as a source code to build up this evaluation benchmark."

**Vid2Sim**, published at CVPR, takes a video of walking on a sidewalk, builds a **Gaussian splatting reconstruction** from it, and turns those splats into a **physics engine** environment — a data-driven simulation in which sidewalk robots can be trained and evaluated.

The demo shows an agent trained there with reinforcement learning transferring **zero-shot to the real world**, for a direct reason: **there is no visual gap between the training environment and the deployment.** With those environments in hand, different sidewalk navigation policies can be evaluated across cases.

#### Fix 2: many environments from one video — UrbanVerse (~01:10–01:12)

Video reconstruction has a limitation: **one video reconstructs exactly one environment.** Ideally you want several variations from the same footage.

Hence **UrbanVerse**, which creates multiple **digital cousins** from a single video. He distinguishes the terms: a **digital twin** is one video mapping to one simulation environment; **digital cousins** are variations from the same source. The method uses computer vision to **extract a scene graph** from the input video, then plugs in different object instances to create environment variants, each usable for training and evaluation.

UrbanVerse is publicly released, together with a **large-scale 3D asset library of 100,000 assets with correct scales.**

They also built a **simulation post-training pipeline**: train the model on videos via imitation learning first, then place it in the simulated environments for post-training that improves **interactivity and counterfactual reasoning.**

#### The payoff: FlowPilot and cross-embodiment transfer (~01:12–01:13)

**FlowPilot** is the recent result: real-world sidewalk navigation from a **single RGB camera**. The model outputs **waypoints** and the controller executes the next one. In the demo the robot handles challenging sidewalk navigation — avoiding obstacles and interacting appropriately with pedestrians.

The direction he finds most exciting is **cross-embodiment transfer**: with a sidewalk navigation foundation model in hand, they can transfer the model across robot embodiments **without fine-tuning**. The demo shows it working well on **legged robots**, with ongoing work on other sidewalk platforms including **wheeled-legged robots** and **electric wheelchairs**.

His closing line: "In the future, not only can we autonomously deliver the food, we can also autonomously deliver the people on the sidewalk." Benchmark and code are released on their lab page.

### Quotes

> "We want to use real world videos as a source code to build up this evaluation benchmark." (~01:09)

The central metaphor of the whole methodology.

> "There is no visual gap between the training environment and the deployment." (~01:10)

Why zero-shot transfer works, in one sentence.

> "In the future, not only we can autonomously deliver the food, we can also autonomously deliver the people on the sidewalk." (~01:13)

Where cross-embodiment transfer is headed: from parcels to passengers.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| SidewalkBench | 人行道視覺導航的模擬 benchmark,建於 Omniverse / Isaac Sim | Simulation benchmark for sidewalk visual navigation, built on Omniverse / Isaac Sim | arXiv 2606.16953 |
| Vid2Sim | 從單目影片重建可互動 3D 模擬環境,支援 RL 訓練與零樣本 sim2real | Real2sim pipeline turning monocular video into interactive 3D simulation for RL navigation | CVPR 2025;arXiv 2501.06693 — [metadriverse.github.io/vid2sim](https://metadriverse.github.io/vid2sim/) |
| UrbanVerse | 從單支影片抽 scene graph 產生多個 digital cousins;附 10 萬件 3D 資產 | Scene-graph extraction from a single video to produce many digital cousins; ships 100k 3D assets | 資產庫另稱 UrbanVerse-100K / asset library also referred to as UrbanVerse-100K |
| FlowPilot | 單目 RGB、無地圖的人行道導航策略,輸出 waypoint | Mapless monocular sidewalk navigation policy emitting waypoints | 在 Coco Robotics 平台上做真實世界驗證 / validated on Coco Robotics hardware — [vail-ucla.github.io/FlowPilot](https://vail-ucla.github.io/FlowPilot/) |
| Coco Robotics | 最後一哩食物外送機器人公司,數百台機器人在營運 | Last-mile food delivery robot company running hundreds of robots | 講者任 Chief AI Scientist / he serves as Chief AI Scientist |
| NVIDIA Omniverse / Isaac Sim | SidewalkBench 的模擬底層 | The simulation stack underneath SidewalkBench | 逐字稿誤聽為 "media omniverse and isoxaxing" |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Ble Joe / Blet / Boley Joe | Bolei Zhou |
| Koko robotics | Coco Robotics |
| sidework foundation models | sidewalk foundation models |
| media omniverse and isoxaxing | NVIDIA Omniverse and Isaac Sim |
| V2 | Vid2Sim |
| gion splants / gshian splatting | Gaussian splatting / Gaussian splats |
| urban versse | UrbanVerse |
| flow pilot | FlowPilot |
| lagged robots | legged robots |
| social professor | associate professor |
| last male delivery | last-mile delivery |

## 待確認 / To Verify

- Vid2Sim 的發表年份:講者說「last year… published at the CVPR」,但外部資料顯示為 **CVPR 2025**,與「去年」的口語表述需再對照。/ He said "last year… published at CVPR", but external sources list it as **CVPR 2025** — reconcile with the spoken timeline.
- UrbanVerse 資產庫「10 萬個資產」的正式名稱與釋出授權條款。/ The formal name and licensing of the "100,000 assets" library.
- 跨載體遷移「不需微調」的具體評估數據,台上未給。/ No quantitative results were given for the zero-fine-tuning cross-embodiment claim.
- 他提到「我的實驗室貢獻了一些模型」但未點名是哪些 sidewalk foundation model。/ He referenced models from his own lab without naming them.
