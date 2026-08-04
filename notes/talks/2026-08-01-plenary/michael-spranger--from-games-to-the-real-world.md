---
title: "From Games to the Real World: How Reinforcement Learning Is Powering Performance and Fun"
title_zh: "從遊戲到真實世界:強化學習如何同時撐起效能與樂趣"
speaker: "Michael Spranger"
affiliation: "President, Sony AI"
type: talk
stage: Plenary
date: 2026-08-01
session: "Session 4: Robotics & World Models"
video: "https://www.youtube.com/watch?v=Tcn5Yb2K0h4&t=9375s"
video_range: "02:36:15–02:47:15"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [reinforcement-learning, robotics, games, sim-to-real, product]
---

# 從遊戲到真實世界:強化學習如何同時撐起效能與樂趣(From Games to the Real World: How Reinforcement Learning Is Powering Performance and Fun)

**一句話總結**:Sony AI 花五、六年把同一套 RL「agent factory」從 Gran Turismo 賽車推到出貨產品、再推到擊敗職業選手的桌球機器人——證明在 LLM 與 world model 之外,RL 仍是把高度專精任務推到超人水準最可靠的路。
**One-line summary**: Sony AI spent five to six years carrying one reinforcement learning "agent factory" from Gran Turismo racing agents into a shipped product and then into a table tennis robot that beats professionals — evidence that amid the LLM and world-model excitement, RL remains the most reliable route to superhuman performance on narrow, competitive tasks.

## 中文筆記

### TL;DR

- **同一套基礎設施、三個階段**:2022 年 Nature 封面的 Gran Turismo 賽車 agent → 整合進遊戲、變成第一個**直接為 AI 體驗付費**的 Power Pack → 用完全相同的 agent factory 做出擊敗職業選手的桌球機器人。
- **Gran Turismo 之所以是好 benchmark,是因為它一次要求三件事**:physical realism(賽車是在失控邊緣、有時還要越過那條線)、tactics(對手會反制,所以要學會試探與欺敵)、sports etiquette(不能撞人,但不夠兇又會被超掉)。三者用一個 end-to-end RL 系統同時解。
- **他的核心主張**:LLM 很好、world model 很好,但**別忘了 RL**——它有能力打造在模擬與真實世界都達到超人水準的高度專精 policy;最終解決 physical intelligence 靠的是這幾種技術的組合,不是其中一種取代另一種。

### 重點整理

#### Gran Turismo:三個維度同時解(約 02:36–02:39)

故事從 2022 年說起,團隊在那年拿下這個專案的第一個 Nature 封面。Gran Turismo 是一個 30 年歷史的 PlayStation 系列,由山內一典(Kazunori Yamauchi)主導,他真正想重現的是「賽車的體感」——所以這遊戲並不好玩,你得真的把駕駛技術磨出來才享受得到。

第一步就是用 RL 做出能擊敗頂尖選手的 agent。他放了一段真實競賽影片,問全場能不能分辨兩台車哪台是 AI:**答案是灰色車是 AI,白色車是 Gran Turismo 世界冠軍**——分不出來,正是因為他們刻意把這個 AI 做成有競爭力、但同時**像人**的駕駛。

Gran Turismo 作為 benchmark 特別有意思,因為它同時要求三件事:

1. **Physical realism**:遊戲建立在高擬真物理引擎上,重現車輛物理特性、有些還是真實賽道。要賽車,先得精通開車;而**賽車本身就是在控制的邊緣、有時甚至要越過那條邊緣去推極限**。
2. **Tactics**:賽道上不只你一個。你對對手做一個動作,對手會反制,所以你得學會**欺敵、試探對手**。
3. **Sports etiquette**:賽車是一種「協作又競爭的舞蹈」——你不該撞別人的車,但你又必須開得很兇,否則就是被超車、輸掉比賽。

他們用一個 end-to-end 系統同時解掉這三件事,方法是 RL:遊戲當環境,輸入可以是視覺或類似自駕車的 state representation,agent 在遊戲裡採取動作,再拿 reward——快且能超車就好,撞到別的車就壞,在賽道上沒有推進也壞。**光是這樣就足以訓練出在 Gran Turismo(以及其他遊戲)裡高度專精、能力極強的 AI。**

基礎設施上他們大量與 PlayStation 合作:遊戲只跑在 PlayStation 上,所以必須用 PlayStation 的雲端基礎設施才拿得到需要的算力規模。研究做完之後訓練其實很快:**開 15 分鐘就能跑完一圈,約 24 小時能得到一個相當不錯的駕駛,幾天可以訓練出超人 policy。**

超人長什麼樣?在 Dragon Trail Seaside 賽道的計時賽裡,有個叫「chicane of death」的彎——**沒有任何人類駕駛是用 agent 這種方式過這個彎的**。另一段影片展示的則是戰術層次:白色車是人、彩色車是 AI,AI 為了拿到更好的入彎與出彎路線,**先戰術性地讓出位置**,然後在出彎時完成一次雙超車。這些細膩的取捨也完全是學出來的。

#### 不只快,還要好玩;以及出貨(約 02:39–02:42)

超人不是終點——他們真正在意的是**做出「好玩」的 agent**。現場播了一位高階賽車手的訪談:她說最有意思的是看 AI 走的路線,有些彎她習慣先出寬再切回來,AI 卻整段貼著內線;她也學到了優先順序——比如一號彎她煞車比 AI 晚,但 AI 的出彎快很多,下一個彎就被甩開,「我以前沒注意到,看了 AI 才想說,喔,好,那我應該這樣做。」

因為底層是 RL,換個目標就換一種行為:把目標從「跑最快」改成「盡可能燒胎」,就得到**超人級的甩尾 agent**。

而作為 Sony 的一部分,他們有機會把這些東西送到數百萬人手上。Nature 論文之後,團隊做了很多輪迭代把技術整進遊戲裡,**論文發表六個月後**技術已經進到遊戲中;最終成果是他非常自豪的 **Power Pack**——**Gran Turismo 史上第一個付費 Power Pack,人們直接為一個 AI 體驗付錢**。因為這個 AI 的體驗夠像人,比賽可以更長、更有趣,Polyphony Digital 於是圍繞這項新能力打造了整個 Power Pack。

#### 從賽車到桌球:同一座工廠(約 02:42–02:47)

今年推出的成果是把**完全同一套技術搬到桌球**。桌球和賽車在結構上高度相似:真實世界的 physical realism、戰術、以及一個要打敗你的對手。換句話說,他們展示的是一座能解「高度專精的競爭性任務」的 **agent factory**。

桌球的難點:球快到「眨眼就過去」;**球的旋轉才是職業與業餘的主要差別——球每分鐘約 9,000 轉,速度可達每小時 100 公里**。你得精通這個物理技巧,同時對面還有個人正想贏你。

他們用一個**自製的桌球模擬器**訓練 policy,再**原封不動搬到真實機器人上**去和職業選手對打。影片是機器人擊敗一位非常成功的頂尖選手平野美宇(Miu Hirano)。中間有個關鍵片段會慢動作播放:**球打到球網**——這是訓練時沒有預見、也無法訓練的狀況;這個完全 end-to-end 訓練、沒有任何寫死程式的 policy,必須在幾分之一秒內、在微秒等級改掉原本的計畫。

而且他們已經有飛輪了:如果機器人因為某個沒見過的戰術輸給某位選手,**就用那場比賽的資料連夜重訓 policy,隔天讓機器人反過來擊敗他**。

結論回到主張:LLM 很好,world model 很好,但**不要忘了 RL**,以及它在模擬與真實世界中打造超人專精 policy 的能力;最終能解決 physical intelligence 這個大問題的,是這些技術的組合。

### 金句

> "I'll challenge you to tell me which of those two cars is driven by an AI versus a human."(約 02:37:30)

灰色車是 AI,白色車是世界冠軍——這個「分不出來」本身就是設計目標,而不是副作用。

> "Racing itself is really at the edge of control. It's sometimes going over this edge of control and pushing the limits."(約 02:38:20)

賽車不是「開得穩」,是刻意在失控邊界上操作——這也是它作為物理 benchmark 的價值所在。

> "I think world models are great. We should not forget about reinforcement learning."(約 02:46:45)

放在一整場 world model 主題 session 中間,這句是刻意的逆風發言。

## English Notes

### TL;DR

- **One infrastructure, three stages**: the 2022 Nature-cover Gran Turismo racing agent → integration into the game as the first Power Pack people **pay directly for an AI experience** → the very same agent factory producing a table tennis robot that beats professionals.
- **Gran Turismo is a good benchmark because it demands three things at once**: physical realism (racing lives at the edge of control, and sometimes past it), tactics (opponents counter your moves, so you must learn to probe and deceive), and sports etiquette (don't crash into people, but drive timidly and you get overtaken). One end-to-end RL system solves all three.
- **His core argument**: LLMs are great and world models are great, but **don't forget RL** — its ability to produce highly specialized superhuman policies in both simulation and the real world is what will, in combination with the rest, actually solve physical intelligence.

### Key Points

#### Gran Turismo: three axes at once (~02:36–02:39)

The story starts in 2022 with the team's first Nature cover for this project. Gran Turismo is a 30-year-old PlayStation title led by Kazunori Yamauchi, whose real interest is recreating the *sensation* of racing — which is why it isn't an easy game: you have to genuinely hone your driving to enjoy it.

Step one was an RL agent that beats the best drivers. He played footage from an actual competition and challenged the room to say which of the two cars was the AI. **It was the gray car; the white one was a Gran Turismo world champion.** You can't tell, and that's by design — they deliberately built an AI that is competitive *and* humanlike.

Gran Turismo makes an unusually interesting benchmark because it combines three demands:

1. **Physical realism.** The game is built on a physics engine that faithfully reproduces vehicle dynamics, in some cases on real-world tracks. To race, you first have to master driving — and **racing itself sits at the edge of control, sometimes deliberately over it.**
2. **Tactics.** You're not alone on the track. Make a move on an opponent and they counter, so you have to learn to deceive and to probe.
3. **Sports etiquette.** Racing is a collaborative-and-competitive dance: you're not supposed to crash into other cars, yet you must drive aggressively or you'll simply be overtaken and lose.

They trained one end-to-end system for all three with reinforcement learning: the game is the environment, inputs range from visual to state representations similar to an autonomous car's, the agent acts in the game, and reward follows the obvious shape — fast and overtaking is good, crashing into cars is bad, failing to make progress on the track is bad. **That alone suffices to build highly specialized, extremely capable AIs in Gran Turismo and other titles.**

Infrastructure meant heavy collaboration with PlayStation: the game only runs on PlayStation, so they had to use PlayStation cloud infrastructure to reach the compute scale required. Once the research was done, training was fast: **15 minutes of driving gets you around the track, about 24 hours yields a really nice driver, and a few days produces a superhuman policy.**

What superhuman looks like: on a time trial at Dragon Trail Seaside there's a corner they call the "chicane of death," and **no human driver has taken it the way the agent does**. A second clip shows the tactical layer: white cars human, colored cars AI. The AI **deliberately trades away position** to set up a better entry, then completes a double overtake on the exit. Those subtle trade-offs are entirely learned.

#### Not just fast, but fun — and then shipped (~02:39–02:42)

Superhuman isn't the goal. They care about building agents that are **fun**. He played an interview with a high-end human racer: the most interesting part for her was watching the AI's racing lines — corners where she went wide and cut back in, the AI took tight all the way around. She also learned about prioritization: into turn one she braked later than the AI, but the AI got a far better exit and beat her to the next corner. "I didn't notice that until I saw the AI, and I was like, oh, okay, cool, I should do that instead."

Because the substrate is RL, changing the objective changes the behavior: swap "go fast" for "burn as much tire as you can" and you get **superhuman drifting agents**.

And as part of Sony, they get to ship to millions. After the Nature paper the team iterated hard on integration — **within six months the technology was in the game** — culminating in something he's very proud of: the **Power Pack**, the **first ever paid Power Pack for Gran Turismo, where people pay directly for an AI experience.** Because the experience is so humanlike, races can be longer and more fun, and Polyphony Digital built a whole Power Pack around the new capability.

#### From racing to table tennis: the same factory (~02:42–02:47)

This year's result takes **exactly the same technology to table tennis**. Structurally table tennis rhymes with racing: real-world physical realism, tactics, and an opponent trying to beat you. What they're demonstrating is a **factory for agents that solve highly specialized competitive tasks**.

The difficulty: the ball crosses the table literally in the blink of an eye, and **spin — not speed — is the main difference between professional and amateur play, at roughly 9,000 rotations per minute with speeds up to 100 km/h.** You must master that physical skill while someone across the table is trying to beat you.

They train the policy in a **custom table tennis simulator**, then bring it onto the real robot **without any changes** and play professionals. The footage shows the robot beating Miu Hirano, a highly successful top player. One clip slows down at the crucial moment: **the ball clips the net** — something they did not foresee and could not train for. Within fractions of a second, this fully end-to-end policy (no programming involved) has to revise its plan at microsecond resolution.

They also have a flywheel now: when the robot still loses to a player because of an unforeseen tactic, **they retrain the policy overnight on that match's data and the robot then beats that player.**

The closing argument returns to the thesis: LLMs are great, world models are great, but **don't forget reinforcement learning** and its ability to build highly specialized policies that hit superhuman capacity in simulation and the real world. Solving physical intelligence will take the combination.

### Quotes

> "I'll challenge you to tell me which of those two cars is driven by an AI versus a human." (~02:37:30)

Gray car AI, white car world champion. The indistinguishability is the design target, not a side effect.

> "Racing itself is really at the edge of control. It's sometimes going over this edge of control and pushing the limits." (~02:38:20)

Racing isn't driving steadily; it's operating deliberately at the boundary of control — which is exactly what makes it a physics benchmark.

> "I think world models are great. We should not forget about reinforcement learning." (~02:46:45)

Delivered in the middle of a session themed on world models — a deliberate counter-current.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| GT Sophy (Gran Turismo Sophy) | Sony AI 的 Gran Turismo 賽車 RL agent,2022 年登上 Nature 封面 | Sony AI's RL racing agent for Gran Turismo; 2022 Nature cover | 由 Sony AI、Polyphony Digital 與 Sony Interactive Entertainment 合作 / joint work with Polyphony Digital and SIE |
| Gran Turismo 7 Power Pack | 內建新一代 Sophy 的付費 DLC;Gran Turismo 史上第一個付費 Power Pack,直接為 AI 體驗收費 | Paid DLC featuring the new Sophy; the first paid Power Pack for Gran Turismo, monetizing an AI experience directly | 演講中他最自豪的產品化成果 / the productization milestone he highlights |
| Dragon Trail Seaside | 展示超人單圈的賽道,含被稱作 "chicane of death" 的彎 | The circuit used for the superhuman time-trial demo, home to what he calls the "chicane of death" | |
| Sony AI 桌球機器人 / table tennis robot | 用自製模擬器訓練、無修改移轉到真機的 end-to-end policy,已擊敗多位職業選手 | End-to-end policy trained in a custom simulator and transferred to hardware unchanged; has beaten multiple professionals | Sony AI 公開資料中此專案名為 Ace(演講中未提及此名稱)/ Sony AI's public materials call the project Ace; the name was not said on stage |
| Miu Hirano(平野美宇) | 影片中被機器人擊敗的頂尖桌球選手 | The top-ranked table tennis player beaten in the demo footage | 兩屆奧運銀牌、前世界排名第五 / two-time Olympic silver medalist, former world No. 5 |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Mika Spranganger / Mika | Michael Spranger |
| Sony Ei | Sony AI |
| GT Sophie | GT Sophy |
| Yamochi | Kazunori Yamauchi(山內一典) |
| PDI | Polyphony Digital(PDI = Polyphony Digital Inc.) |
| Gruntism / Gran Turismo | Gran Turismo |
| dragon side se dragon trail seaside | Dragon Trail Seaside |
| Mu Hilano | Miu Hirano(平野美宇) |
| world LLMs are great | world models are great(講者口誤/字幕混淆 / speaker slip or caption confusion) |

## 待確認 / To Verify

- 開場對戰影片中「white car」的 Gran Turismo 世界冠軍姓名,字幕聽成 "Muchian",未能確認。/ The Gran Turismo world champion driving the white car — the caption renders it "Muchian"; name unconfirmed.
- 分享賽車線心得的女性高階賽車手姓名,演講中未具名。/ The high-end racer interviewed about learning racing lines from the AI was not named.
- 桌球機器人在演講中未報出專案代號;此處的 "Ace" 取自 Sony AI 公開資料,非講者原話。/ The table tennis project was not named on stage; "Ace" here comes from Sony AI's public materials, not the talk.
