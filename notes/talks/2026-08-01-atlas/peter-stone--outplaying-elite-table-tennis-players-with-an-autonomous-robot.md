---
title: "Outplaying Elite Table Tennis Players with an Autonomous Robot"
title_zh: "用自主機器人擊敗頂尖桌球選手"
speaker: "Peter Stone"
affiliation: "Chief Scientist, Sony AI; Professor, UT Austin"
type: keynote
stage: Atlas
date: 2026-08-01
session: "Session 2: Robotics & World Models"
video: "https://www.youtube.com/watch?v=psPzCQbjCCo&t=863s"
video_range: "00:14:23–00:28:53"
transcript: "tmp/[English (auto-generated)] Atlas Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [robotics, reinforcement-learning, event-based-vision, sim-to-real, sony-ai]
---

# 用自主機器人擊敗頂尖桌球選手(Outplaying Elite Table Tennis Players with an Autonomous Robot)

**一句話總結**:Sony AI 的 Ace 是第一個在官方規則下、面對面擊敗職業排名選手的自主機器人——證明 AI agent 已經能在「需要毫秒級即時決策的物理空間任務」上達到專家水準,而做到這件事靠的是感知、強化學習與硬體三者同時被推到極限,而非任何單點突破。
**One-line summary**: Sony AI's Ace is the first autonomous robot to beat professionally ranked players head-to-head under official rules — proof that AI agents can now reach expert-level performance at fast, real-time decision-making in physical space, and it took perception, reinforcement learning, and custom hardware pushed to their limits together, not any single breakthrough.

## 中文筆記

### TL;DR

- **這是第一次有機器人在「一對一對抗、官方規則」下打贏職業選手**。先前的里程碑(Gran Turismo 的 GT Sophy、無人機競速)要嘛不是物理世界,要嘛不是面對面對抗。
- **成果來自三個同步推進的貢獻**:高速感知系統(9 台定位球體 XYZ 的相機 + 3 台 event-based 相機追旋轉)、控制端的強化學習、以及為了速度重新設計的客製化硬體。
- **RL 只負責最底層的 skill**:給定來球,手臂要怎麼揮才能打到想要的落點與旋轉。上層的 tactics(打哪裡)與 strategy(整局怎麼打)不在這一層。
- **動作空間是關鍵工程難題**:6 自由度手臂 + 2 自由度底座的可達點集合極不直觀,他們把它映射成一個「任意一點都可行」的 hyper cube,再交給 MPC 控制器執行。
- **硬體用最佳化「減重」**:把結構穩定性用不到的質量全部拿掉,比原始設計輕 5 公斤,才能做到每 0.8 秒以 20 m/s 擊球一次的職業級節奏。
- **目前的極限很誠實**:球速已略快於職業選手,但旋轉還不夠;能不能打贏世界冠軍不知道;用人形機器人做到這件事「還非常遙遠」。

### 重點整理

#### 開場:UT Austin、Sony AI,以及貫串一切的研究問題(約 00:14–00:16)

Stone 同時來自 UT Austin 與 Sony AI。他提到兩週後將接任 UT Austin 新成立的 School of Computing 首任院長(整併三個系),他也是 Texas Robotics 的創始主任;今年 11 月 CoRL(Conference on Robot Learning)將在該校舉行。他順帶介紹了幾件學校的事:機器人設施設在舊的女子體操館裡、機器學習實驗室、他深度參與的 AI 倫理計畫 **Good Systems**,以及公開的 AI 素養課程 **Essentials of AI for Life and Society**(非本科生也能修)與一萬美元的線上碩士。

貫串他多年研究的一個問題:**「自主智慧體在有隊友與/或對手的即時動態場域中,能學到什麼程度?」**(to what degree can autonomous intelligent agents learn in the presence of teammates and/or adversaries in real-time dynamic domains?)這條線索串起 RoboCup 機器人足球(目標是 2050 年讓人形機器人隊擊敗世界盃冠軍)、RoboCup@Home 的通用服務型機器人、Gran Turismo 的 **GT Sophy**(四年前的 Nature 封面,第一個在即時控制任務上擊敗頂尖人類的 AI agent),以及與 Joydeep Biswas 合作、在 Austin 步道上處理社交情境的導航研究。

他也趁機宣傳幾天前才公開的 **Oopsie Data**:一個社群共建的**機器人失敗**資料集。「大多數資料集都在收集機器人成功的樣本」,這個計畫反過來收集失敗與次佳行為,歡迎各實驗室貢獻自己的 rollout 與失敗標註。

#### 為什麼是桌球:遊戲作為 AI 基準的下一格(約 00:19–00:20)

遊戲長期是 AI 的 benchmark,但過去的里程碑多半是**回合制**(西洋棋、圍棋、撲克)。即時控制方面,GT Sophy 是第一個在即時控制任務上勝過頂尖人類的例子;而第一個在**真實世界**勝過頂尖人類的是 Davide Scaramuzza 實驗室的無人機競速(同樣登上 Nature 封面),但那不是面對面的對抗設定。

桌球則同時具備**一對一對抗**與物理即時性,從 1980 年代中期起就一直是機器人研究的動機題目。他特別提到 Google 曾有一支影片(下一位講者 Vincent Vanhoucke 參與其中),機器人在**合作式**對打中表現很好——但在此之前,**沒有任何機器人能在奧運規則下擊敗專家級選手**。

Ace 的研究由 Sony AI 蘇黎世的 **Peter Dürr** 領軍(Stone 強調「他應該拿走絕大部分功勞」),團隊規模很大,成果登上 4 月 23 日的 Nature 封面。

#### 比賽設定:幾乎沒有讓步的奧運規則(約 00:20–00:22)

- 選手活動區域與正規比賽相同。
- **機器人必須自己發球**——這在過去的系統中常被省略。它有一個小杯子把球拋起來再發球。
- 唯一的讓步是**基於安全,不允許人類選手越過球網**;其餘實質上就是奧運規則。
- 對手是一位曾兩度拿下奧運銀牌、世界排名最高到第 5 的女子選手(對戰當時排名約第 11)。

#### 系統設計:感知、RL、硬體三管齊下(約 00:21–00:26)

**感知**:機器人四周共 9 台相機負責取得球的 XYZ 座標,另有 3 台 **event-based 的注視控制相機**追蹤球的旋轉。球上**沒有任何人工標記**,靠球身原有的 logo 判斷旋轉。他放了一段從機械臂視角、大幅放慢的影片:「大多數機器人影片你要加速播放,這支要放慢才看得清楚。」

**控制**:核心問題是「球飛過來時,手臂要怎麼動,才能在指定落點與旋轉下擊到球」。他把這一層稱為 **skill**,與 **tactics**(要把球打去哪)、**strategy**(這一分、這一局要怎麼打)區分開來;**他們的 RL 絕大部分在最底層的 skill 這一層**。

訓練主要在**物理知情的模擬器(physics-informed simulator)**裡進行,模擬器的噪聲模型、球分布模型與物理模型都由真實世界資料建立。演算法用**非對稱 actor-critic**:critic 拿到真實狀態、actor 只拿到有噪聲的狀態,最後上場的是 actor。

一個關鍵的技術難點是**動作空間**:6 個旋轉關節的手臂加上底座在 XY 平面的 2 個自由度,末端執行器能到達的點集合形狀非常反直覺。他們找到方法把它映射到一個 **hyper cube**,使得「這個立方體裡的任何一點都是可行的動作」,他們稱為 feasible action for optimal control;RL agent 選定目標後,再由 **model predictive controller** 驅動末端執行器去達成。

**硬體**:機器人是為此客製的,用最佳化流程把「結構穩定性不需要的質量」全部拿掉,比原始設計**減重 5 公斤**,才能達成職業級要求——**每 0.8 秒、以 20 m/s 的速度擊球一次**。

**發球庫**:用演化演算法生成一組**多樣化**的發球(下旋、上旋、不同落點),避免被對手預測;每一分由機器人挑一個發球執行,之後才交給標準的 RL 控制器打完這一分。

他放了一段很能說明反應速度的影片:機器人本來要打正手,球擊中球網後彈道改變,它立刻調整、把手臂往反方向揮回去,仍然把球救回去。

#### 結果與尚未解決的問題(約 00:26–00:28)

Nature 論文收錄到 2025 年 12 月的結果,當時是**贏一些、輸一些**的大學級選手階段(結果表中紅色為敗、綠色為至少贏下一局,標 T 者為職業級選手)。約一個月前發布的 blog 則涵蓋今年春天的成績:**擊敗了曾世界排名第 5 的女子選手,以及曾排名第 99 的男子選手**——真正的職業級對手。

球速數據顯示,2026 年 4 月的擊球速度**略快於職業人類選手**,但**旋轉仍不及**職業選手。男子職業選手擊球更重,他們同樣贏下了對戰。

總結:**這是 AI agent 第一次在「需要快速即時決策的物理空間任務」上達到專家水準。** 仍然開放的問題有三個:

1. 機器人能打贏世界冠軍嗎?不知道。
2. 職業選手能靠這台機器人提升自己嗎?**已經有實例**——有職業選手從中得到自己原本不會嘗試的擊球構想。
3. 換成人形機器人做得到嗎?「我認為我們離那還非常遠。」

他最後預告同日 15:10 主舞台 Sony AI 的 Michael Spranger 會再談 Ace 與 GT Sophy 等專案。

### 金句

> "The first robot that can beat a professional athlete at their own sport."(約 00:14)

他自己對這項成果的一句話定位。

> "The only concession that we make to this being a robot is that we don't allow the player to cross the net for safety reasons, but otherwise it's effectively regulation Olympic rules."(約 00:22)

「唯一的讓步」——這句話是整個結果可信度的關鍵:機器人得自己發球、在正規場地、按正規規則打。

> "For the first time, we've shown that AI agents can reach expert level performance in tasks that require fast real-time decision-making in physical space."(約 00:28)

不是「機器人會打桌球」,而是「即時物理決策的專家水準」這個更一般的宣稱。

## English Notes

### TL;DR

- **First robot to beat professionally ranked players head-to-head under official rules.** Earlier milestones were either not physical (GT Sophy in Gran Turismo) or not head-to-head adversarial (drone racing).
- **Three contributions had to land together**: a high-speed perception stack (9 cameras for ball XYZ plus 3 event-based cameras tracking spin), reinforcement learning for control, and custom hardware redesigned for speed.
- **RL operates only at the lowest "skill" layer** — given an incoming ball, how to swing to hit a target location and spin. Tactics (where to aim) and strategy (how to play the point or match) sit above it.
- **The action space was the hard engineering problem**: the reachable set for a 6-DoF arm on a 2-DoF base is deeply counterintuitive, so they map it onto a hypercube where *every* point is a feasible action, then hand execution to an MPC controller.
- **The hardware was optimized by subtraction**: strip every gram not needed for structural stability, 5 kg lighter than the original design — the only way to hit at 20 m/s every 0.8 seconds.
- **Honest about the ceiling**: ball speed now slightly exceeds professional humans, but spin does not; beating a world champion is an open question; doing this on a humanoid is "still very far."

### Key Points

#### Framing: the research question behind two decades of work (~00:14–00:16)

Stone splits his time between UT Austin and Sony AI. In two weeks he becomes the head of UT Austin's new School of Computing (merging three departments); he founded Texas Robotics, and CoRL is hosted there this November. Side notes: the robotics facility lives in the old women's gymnasium, the **Good Systems** ethical-AI initiative, a public AI-literacy course (*Essentials of AI for Life and Society*), and a $10,000 online master's.

One question unifies his career: **to what degree can autonomous intelligent agents learn in the presence of teammates and/or adversaries in real-time dynamic domains?** That thread runs through RoboCup soccer (the 2050 goal of a humanoid team beating the World Cup champions), RoboCup@Home service robots, **GT Sophy** — the Nature cover four years ago, the first AI agent to beat the world's best humans at a real-time control task — and social navigation on Austin's hike-and-bike trails with Joydeep Biswas.

He also plugged **Oopsie Data**, announced days earlier: a community-sourced dataset of **robot failures**. Most robotics datasets only capture successes; this one collects real failed and suboptimal rollouts, and he asked the audience to contribute.

#### Why table tennis (~00:19–00:20)

Games have been AI's benchmark for decades, but the classic milestones are turn-taking (chess, Go, poker). GT Sophy was the first real-time control task where AI beat the best humans; the first *real-world* case was drone racing from Davide Scaramuzza's lab (also a Nature cover), but that was not head-to-head competitive.

Table tennis is both one-on-one adversarial and physically real-time, and has motivated robotics research since the mid-1980s. Stone showed a Google video — the next speaker, Vincent Vanhoucke, was involved — of a robot rallying well in a *cooperative* setting. But no robot had beaten expert players under Olympic rules.

The work was led by **Peter Dürr** at Sony AI ("he deserves the lion's share of the credit"), with a large team, and made the cover of Nature on April 23.

#### The match setup (~00:20–00:22)

Regulation player area. **The robot serves its own ball** — often skipped in prior systems — using a cup that tosses the ball up. The single concession to it being a robot: for safety, the human cannot cross the net. Otherwise, effectively Olympic rules. The opponent shown is a two-time Olympic silver medalist who peaked at world No. 5 and was ranked around No. 11 at the time of the match.

#### System: perception, RL, hardware (~00:21–00:26)

**Perception.** Nine cameras around the rig recover the ball's XYZ position; three **event-based gaze-control cameras** track spin. There is **no artificial marker on the ball** — spin is read off the printed logo. A wrist-mounted camera view, heavily slowed down, shows the tracking: "most robot videos you see sped up a lot; this one you have to slow down."

**Control.** The core problem is how to move the arm as the ball arrives, given a desired target and spin. Stone calls that a **skill**, distinct from **tactics** (where to place the ball) and **strategy** (how to play the point or the match); **the RL lives almost entirely at the skill level.**

Training runs mostly in a **physics-informed simulator** whose noise model, ball distribution model, and physics model are all built from real-world data. The learner is an **asymmetric actor-critic**: true state to the critic, noisy state to the actor, and the actor is what deploys.

The subtle piece is the **action space**. With six revolute joints and two base joints in the XY plane, the set of reachable end-effector poses is awkward; they found a mapping onto a **hypercube in which every point is a feasible action** ("feasible action for optimal control"). A **model predictive controller** then drives the end effector to the target the RL agent picks.

**Hardware.** The robot is custom-built, with an optimization pass stripping out all mass not needed for structural stability — **5 kg lighter than the original design** — because professional-level play means **hitting the ball at 20 m/s every 0.8 seconds**.

**Serves.** An evolutionary process produced a **library of diverse serves** (backspin, topspin, varied placement) so the robot isn't predictable; it picks one to start the point, then the standard RL controller takes over for the rally.

A striking clip: the robot commits to a forehand, the ball clips the net and changes trajectory, and it reverses its swing mid-motion and still returns the ball.

#### Results and open questions (~00:26–00:28)

The Nature paper covers results through December 2025, when the robot was winning some and losing some against university-level players (red = losses, green = won at least one game, T = professional). A blog released about a month before the talk covers this spring: **wins over a woman formerly ranked No. 5 in the world and a man formerly ranked No. 99** — genuine professionals.

By April 2026 the robot hits **slightly faster than professional humans but still imparts less spin**. Male professionals hit harder than the female professionals; the robot beat them too.

Summary: **for the first time, AI agents reach expert-level performance in tasks requiring fast real-time decision-making in physical space.** Three open questions: can it beat a world champion (unknown); can pros use the robot to improve their own game (yes — some professionals have already picked up shot ideas they wouldn't otherwise have tried); and could this be done on a humanoid ("we're still very far from that").

He closed by pointing to the 3:10 PM main-stage talk from Sony AI's Michael Spranger, covering Ace and GT Sophy.

### Quotes

> "The first robot that can beat a professional athlete at their own sport." (~00:14)

His own one-line framing of the result.

> "The only concession that we make to this being a robot is that we don't allow the player to cross the net for safety reasons, but otherwise it's effectively regulation Olympic rules." (~00:22)

The credibility of the whole result rests on this line: the robot serves, on a regulation court, under regulation rules.

> "For the first time, we've shown that AI agents can reach expert level performance in tasks that require fast real-time decision-making in physical space." (~00:28)

The claim is not "a robot plays table tennis" — it's expert-level real-time physical decision-making as a general capability.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Ace | Sony AI 的自主桌球機器人,擊敗職業排名選手 | Sony AI's autonomous table tennis robot that beats professionally ranked players | Nature 封面 2026-04-23;Peter Dürr 領軍 / Nature cover, led by Peter Dürr — [ace.ai.sony](https://ace.ai.sony/) |
| GT Sophy | Gran Turismo 的端到端 RL 賽車 agent,第一個在即時控制任務擊敗頂尖人類的 AI | End-to-end RL racing agent for Gran Turismo; first AI to beat top humans at a real-time control task | 約四年前的 Nature 封面 / Nature cover ~4 years ago |
| Oopsie Data | 社群共建的機器人**失敗**資料集 | Community-sourced dataset of real robot **failures** | 演講前幾天才公開 / announced days before the talk — [oopsie-data.com](https://oopsie-data.com/) |
| RoboCup / RoboCup@Home | 機器人足球與家用服務機器人競賽 | Robot soccer and home service robot competitions | 2050 目標:人形機器人隊擊敗世界盃冠軍 / 2050 goal: humanoid team beats World Cup champions |
| Good Systems | UT Austin 的倫理 AI 計畫 | UT Austin's ethical AI initiative | |
| Essentials of AI for Life and Society | UT Austin 公開的 AI 素養課程 | UT Austin's public AI-literacy course | 任何人可修 / open to anyone |
| CoRL 2026 | Conference on Robot Learning,2026 年 11 月於 UT Austin | Conference on Robot Learning, November 2026 at UT Austin | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Peter Dur | Peter Dürr(Sony AI 蘇黎世 / Sony AI Zürich) |
| Jody Biswas | Joydeep Biswas(UT Austin) |
| Dvita Scaramutza | Davide Scaramuzza(UZH) |
| oopsy data | Oopsie Data |
| Robocop | RoboCup |
| endeector | end effector |
| gshian splatting(其他場次亦出現)| Gaussian splatting |
| Mika Springer | Michael Spranger(疑為 / likely,見待確認) |

## 待確認 / To Verify

- 主導 Oopsie Data 的博士後研究員,字幕聽成 "Klaus Vulkar",正確拼法待查。/ The postdoc leading Oopsie Data — heard as "Klaus Vulkar", correct spelling unverified.
- 字幕稱 Sony AI 主舞台講者為 "Mika Springer, president of Sony AI",疑為 Michael Spranger,職稱亦待官網議程確認。/ The Sony AI main-stage speaker, heard as "Mika Springer, president of Sony AI" — likely Michael Spranger; title needs confirming against the agenda.
- 對戰職業選手的姓名演講中未點名(僅描述「兩屆奧運銀牌、曾世界第 5」);外部報導提到 Miu Hirano 與 Miyuu Kihara,但無法確認影片中是哪一位。/ Stone did not name the opponents on stage; press coverage mentions Miu Hirano and Miyuu Kihara, but the specific player in the video cannot be confirmed from the transcript.
- 「擊球速度 20 m/s、每 0.8 秒一次」是講者口述的職業級門檻;Nature 相關報導引用的是 19.6 m/s 線速度,兩者是否為同一指標待對照論文。/ The "20 m/s every 0.8 seconds" figure is as spoken; press coverage of the Nature paper cites 19.6 m/s linear velocity — whether these are the same metric needs checking against the paper.
