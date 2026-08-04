---
title: "Panel: Robotics & World Models"
title_zh: "座談:機器人與世界模型"
speaker: "Sergey Levine, Jim Fan, Michael Spranger, Anastasis Germanidis, Wei Zhan（主持 / Moderator: Guru Chahal）"
affiliation: "Sergey Levine — Co-Founder, Physical Intelligence; Professor, UC Berkeley / Jim Fan — Director of Robotics & Distinguished Scientist, Nvidia / Michael Spranger — President, Sony AI / Anastasis Germanidis — Co-Founder/Co-CEO, Runway / Wei Zhan — Chief Scientist, Applied Intuition / Guru Chahal — Partner, Lightspeed Venture Partners"
type: panel
stage: Plenary
date: 2026-08-01
session: "Session 4: Robotics & World Models"
video: "https://www.youtube.com/watch?v=Tcn5Yb2K0h4&t=11327s"
video_range: "03:08:47–03:35:50"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [robotics, world-models, panel, reinforcement-learning, forecasting]
---

# 座談:機器人與世界模型(Panel: Robotics & World Models)

**一句話總結**:五位講者在「影片模型到底懂不懂物理」「VLA 是不是被 WAM 取代」上分歧明顯,但在「該爭的不是架構而是資料與環境」以及「機器人的商業起飛點落在 2 到 10 年之間」上意外收斂。
**One-line summary**: The five panelists split sharply on whether video models really understand physics and whether VLAs are being replaced by world-action models, yet converged on two things — the argument that matters is about data and environments rather than architecture, and that robotics' commercial takeoff lands somewhere between two and ten years out.

## 中文筆記

### 場次背景(約 03:08:47)

主持人 **Guru Chahal**(Lightspeed Venture Partners 合夥人)在 session 開場(約 02:09:26)時就定了調:Lightspeed 從 Anthropic、Mistral、SSI、Reflection 到 Dexterity、Skild 等機器人公司都長期投資,而**普遍看法是機器人仍處在「pre-ChatGPT 時刻」**——他同意這個判斷,但認為**轉折點可能比多數人以為的更近**。

他刻意跳過「請各位定義什麼是 world model」這個開場題(理由:那會吃掉接下來 20 分鐘),也拒絕採用「一題輪流答一輪」的形式,而是從五場演講裡挑出**立場可能有落差的點**直接開戰。

### 議題一:光靠生成影片,模型就會內建物理理解嗎?(約 03:10–03:12)

**Anastasis Germanidis(正方,原始主張者)**:這主要是**經驗結論**——把模型 scale 上去,再量測它在各種物理相關任務上的表現。他們的方法論是:**要引入 inductive bias,就把它引入在訓練資料裡,不要引入在架構裡**。所以他們刻意讓一切直接從像素學,不加任何 3D 先驗;到某個規模之後,幾何一致性就相當好,而這也是可量測的。他看不出有什麼**根本理由**讓這條路停止 scale。

**Jim Fan(補充但收窄)**:雖然 Guru 說不要定義,他還是先給一個以便討論落地:**world model 是「以動作為條件、預測下一個感測狀態」的模型**。在這個定義下,**影片只是方便,而且影片只是其中一種感測器——它叫 RGB camera**。但機器人系統上可以有不只一台 RGB camera,而且還有大量其他感測器。他認為**今天的 world model 討論漏掉太多模態**:除了影片,還有**觸覺、力、慣性量測**,這些都要放進模型才談得上對動態演化的**整體性**模擬。結論:「影片方便、影片好 scale、影片很豐富,**但那不是故事的全部**。」

**Sergey Levine(最強反對意見)**:如果你生成的是「人看了覺得很讚」的影片,**非常容易落入一種狀況:影片對人來說很好看,卻沒有反映模型模擬物理 counterfactual 的能力**。關鍵在於:給模型一個 prompt 時,它**不需要**預測「真實物理系統在這個情境下、做了這個動作之後會怎樣」;它只需要產生一個**在你看來符合這個 prompt** 的結果。**這意味著模型可以自己選怎麼把場景擺好,好讓結果看起來漂亮——而這個選擇權非常關鍵。**但你若要在真實世界規劃與行動,你得處理**你實際所在的情境、你實際採取的計畫、以及可能產生的 counterfactual 後果**。

他的例子非常直接:**拿很好的駕駛資料訓練模型,然後問它「如果我開進一棟建築物會怎樣」——它多半會生成建築物變形成一條漂亮道路、而你正愉快地開在上面。**這件事已經有人真的做過,結果就是這樣。所以答案是:「**是的,模型可以處理物理;但你要非常小心,別讓它把你騙了。**」而問題的根源如 Anastasis 所說在資料——只是**「拿來生成好看影片的資料」不等於「拿來學 counterfactual 的資料」**。

### 議題二:VLA 已死、未來是 world-action model 嗎?(約 03:12–03:16)

**Jim Fan**:「取決於你在哪個抽象層級工作。」用 system 1 / system 2 來切:

- **System 1**(快速反應的運動技能):**WAM 很有希望**。很多物理常識——例如「怎麼抓一個杯子」——**從第一性原理來看就很難逐幀用語言 token 拆解描述**。
- **System 2**(推理、寫程式、工具呼叫):他主張 **Opus、GPT 這些模型其實就是 VLA**——它們是 agentic 的、會採取行動。而且**今天用 VLA 的人比用 WAM 的人多**,因為 VLA 還服務其他目的,包括他演講裡談的 **agentic scaling**:這些模型能透過感知理解世界、呼叫工具,協助 auto research。

結論:不覺得會有一方完全取代另一方,**真正的分野是抽象層級**。

**Sergey Levine(認為題目本身問錯了)**:「這是**你**問我們的好問題,但對**研究者問自己**來說可能是錯的問題」——因為它**把模型擺在資料之前**。要做出真正好的基礎模型,關鍵是**能有生產力地吃下大量非常多樣的資料**,而影片資料是其中很好的一種。事實上,**現在真正好的 VLA 都是拿大量影片資料訓練的**,只是那發生在 web-scale 預訓練階段、用來訓練理解 backbone。

所以正確問法不是「要 VLA 還是要影片」,而是「**怎麼用上最多的資料**」;在那之上才是 inductive bias 的問題,而如他引用的說法:「**inductive bias 是偽裝過的訓練資料**」——**在小規模測試時 inductive bias 的效果可能很大,一旦 scale 上去就溶解掉了**。真正該做的是:盡可能利用最多資料來源,然後**務實地決定模型該有哪些輸出**,好把這些資料用起來。

**Michael Spranger(從應用端補兩點)**:

1. **語言在他們的任務上幫助有限**:賽車和桌球,語言其實沒那麼有用。認知科學裡有個經典區分——**declarative vs procedural knowledge**;你可以描述怎麼騎腳踏車,但那裡面的資訊量很少,**你得真的去騎、去學那個物理**。
2. **視覺不是永遠可得**:視覺當然是很好的 condition 對象,但有些應用做不到。例如遊戲出貨給消費者、場上有 20 個 agent 在賽車時,**沒辦法從 20 個視角各渲染一次**——PlayStation 上的算力大部分要留給玩家自己的畫面。

所以這些**不是 yes/no 的問題**,而是「你關心的 domain 是什麼?要解什麼?下游應用是什麼?」他同意大型基礎模型能捕捉視覺與語言知識、在很多情況下極有幫助,但**我們仍然需要把當下真正在意的東西蒸餾出來,再出貨給消費者。**

**Anastasis Germanidis(補一刀)**:整體正在朝 **omni-model** 收斂——能同時預測視覺、音訊、文字等模態。所以呼應 Sergey:重點是**你在預訓練階段把模型專門化在什麼上面**——資料混合偏向低階運動規劃,還是偏向高階推理?**這不是「WAM 還是 VLA 架構」的問題,而是「你把模型容量分配給了什麼」的問題**,而那才是決定性因素。

**Guru 的收束**:「這不是二選一,真的是看使用情境,兩邊都有很有意思的適用範圍。」

### 議題三:真實世界的 RL 要佔多少?vs 模擬與數位資料(約 03:16–03:22)

**Wei Zhan(先分應用)**:

- **自駕**:他們更在意**行為**與**視覺**兩種模態,而這兩者相對容易從真實世界資料 scale 起來、再以可 scale 的方式注入合成世界。現況是**多數量產端到端 ADAS 的領先者主要仍靠真實世界資料,合成資料用在 post-training 階段**;但趨勢很清楚——**大規模合成資料對讓自動駕駛更魯棒、更安全的角色會越來越關鍵**。
- **機器人**:就他目前的理解,**locomotion 與 whole-body tracking 這類任務,RL 方法非常有用、甚至主導**;但像**靈巧操作**這種複雜任務,**既難以造出捕捉關鍵物理屬性的高擬真合成世界,也難以定義好的 reward function** 來閉環訓練 policy。所以在這個時間點,**behavior cloning / imitation 仍然主導**。

**Sergey Levine(拆成供給面與需求面)**:他認為**未來會和現在非常不同**。

- **現在**:機器人學處在 **bootstrap 階段**——我們還在搞清楚,要讓機器人模型好到能真的靠端到端學習來使用,需要什麼條件。
- **未來**:我們不會永遠停在 bootstrap 階段。終將到達一個狀態:**部署在外的機器人數量,像今天路上的車一樣多**;那時會有**極為充沛的、機器人自主與世界互動所產生的資料**,而**能利用這些真實世界資料的 RL 方法將極端重要**。
- **另一個理由**:隨著 imitation learning 方法越做越好,挑戰會越來越集中在**最後那一段落差**——**怎麼從 98% 成功率的 policy 走到 100%?** 那裡 **domain gap 非常關鍵**,因為你需要每件事都完全對齊。所以那裡**也會需要真實世界的 RL**。

但他明確補上時間判斷:「**我認為那是未來會發生的事,不是今天的狀態**——Wei 對現況的總結我認為非常精準。」

**Jim Fan(抄 LLM 的作業,列三種環境)**:「great scientists invent, greater scientists copy.」他一直在看 LLM 那邊在做什麼,而**他們現在不只是在造資料,是在造環境**——重點是取得數以百萬計的 coding environment、在裡面做 RL,才得到今天的 Mythos 與 GPT 系列。**他們不是靠 imitation learning 走到這裡的,最終是靠 RL。** 所以機器人也要造環境,而環境有三個選項:

1. **真實世界**:「Sergey 和 π 那邊做了非常出色的工作」,絕對重要——**物理完美,因為它就是真實世界**。
2. **傳統模擬器**(如 Isaac Sim):瓶頸**不是模擬速度**(模擬其實跑得非常快),而是**資產、環境、任務**——過去需要大量美術人員手工製作。但現在有一類叫 **real-to-sim** 的配方,他認為極有潛力:**自動掃描真實世界並搬進傳統模擬器**,讓你既 data-driven、又能倚賴快速的古典物理求解器。
3. **World model 當神經模擬器**:影片 world model 一個很務實的用法,就是把它當成**由資料寫成的神經模擬器**——吃進動作、生成影片與感測狀態。缺點是**跑得很慢**,優點是**多樣性極大**(world model 能負擔多少就有多少)。

結論:機器人的 RL 最終會**橫跨這三種選項**,使用不同類型的算力、面對不同的限制;他希望大家用更**整體性**的方式看待這件事。

### 議題四(快問快答):最近看過最驚豔、且不是自家的 demo(約 03:22–03:27)

| 講者 Speaker | 選擇 Pick | 理由 Why |
|---|---|---|
| Anastasis Germanidis | **Induction Labs 的 Photon-1** | 一種基於**螢幕錄影**的 world model(「數位版的 world model」)。他們**完全只用螢幕錄影**訓練,不靠常見的文字監督,卻在 computer use 上做到與某個小型 Gemini 模型競爭的水準,**而且少了一個數量級的算力**。Guru 的吐槽:「這件事說明的與其說是模型,不如說是我們在螢幕前做的工作的本質。」 |
| Jim Fan | **Tesla FSD** | 「一個已經有數百萬人買來每天用的機器人。」他從去年開始開 Tesla,最新版本讓他驚豔——尖峰時段、超級擁擠的車道也能協商得非常好,近乎像人,有時甚至比他自己開得好。這給他很大希望:**一旦把實體資料飛輪轉起來,相對幾年前就是量子躍遷**,也正是他演講中強調「資料收集必須淡入背景、不能有侵入性」的原因。 |
| Michael Spranger | **General Intuition 的 Rocket League world model** | 不是機器人,但約兩週前的突破:這個 world model **能一致地渲染同一個世界裡四個不同玩家的視角**。傳統 world model 大多是「我與世界、我的動作與世界」;這解鎖了**多 agent / 多玩家互動**的未來。他認為這很重要,因為**機器人領域常常只想著任務表現(舉杯子、鎖螺絲),但世界裡充滿其他 agent**——人或 AI,我們都得和他們互動。他原本以為這要再等 6 到 12 個月。 |
| Sergey Levine | **Boston Dynamics Atlas 的後空翻**(附帶教訓) | 那支影片當年爆紅,是因為機器人後空翻**沒站穩落地**、接著出現一連串怪異不自然的動作,但**最後站住了**;當時 CES 前後很多人拿它跟 Unitree 那些完美後空翻對比、嘲笑 Boston Dynamics 出問題。但**做機器人的人看了會知道,Boston Dynamics 那支其實厲害得多——因為它沒有倒**:發生了很糟糕的事、它抓狂了,但它站住了,而且那是一台 **170 公斤**的機器人,比輕量的 Unitree 機器人重得多、複雜得多。**教訓:機器人的 demo 永遠不是表面看到的那樣**——挑戰通常不在你看到的畫面裡,而在**泛化程度、系統處理陌生情境與失敗的能力,以及背後所有的複雜度**。很容易被 demo 誤導,而沒意識到真正難的問題在哪。 |
| Wei Zhan | **Tesla FSD**,加兩個 | 他也附議 FSD(已接管他大部分日常里程)。另外他在一家不能具名的公司的 R&D 車上體驗到:**在有大量行人、單車與各種困難狀況的超擁擠街道,連續一小時零接管**,而**車上算力只有 Tesla HW4 等級的七分之一**,感測器配置也更簡單。機器人這邊,他今年在會議展場看到一家中國新創,大力推進**合成資料**的使用邊界,做**可泛化的 zero-shot pick-and-place**——直接讓觀眾把任意物品丟到桌上讓它處理。 |

### 議題五(快問快答):機器人的「Claude Code 時刻」是哪一年?(約 03:27–03:35)

Guru 的定義:LLM 的第一個 **ChatGPT 時刻**之後,還有一個 **Claude Code 時刻**——**第一個商業使用情境真正起飛、直接衝上去**的那一刻。他要一個數字,外加一兩個字的應用領域。

| 講者 Speaker | 數字 Number | 領域與理由 Domain & reasoning |
|---|---|---|
| Wei Zhan | **約 3 年** | 除了大規模第一人稱與第三人稱視角資料外,還需要**能被良好 grounding 並與之關聯的必要物理模態**也補齊;這類資料累積需要時間,是機器人基礎模型取得該能力的關鍵之一。 |
| Sergey Levine | **3 年** | (先強調數字是**在聽到 Wei 的答案之前就選好的**。)但他**說不出是哪個領域**——而關鍵正在這裡:**要有夠通用的模型,把探索不同應用的門檻大幅拉低**,讓社群能集體盡可能多地試遍各種可能性,才會撞上那個解答。**通用模型是前提,不是結果。** |
| Michael Spranger | **2 年** | (先開玩笑說「我也說 3 年」被起鬨,才改口 2。)領域會在**工業區塊**,因為那是**半結構化 domain**、資料可得性較好——可能是倉儲、可能是製造。他認為**技術大致已經到位,問題更多在找到對的經濟模型**、對的資料輸入、以及真能部署的環境。相對地,**把大型機器人放進家庭有安全問題,時程更遠**。這些半結構化環境的做法是:量身裁切使用情境、引入通用模型,再結合**現場訓練或模擬訓練**。 |
| Jim Fan | **最早 2030 / 2035 / 2040** | 最早 2030;**2035 年機器人數量會超過 iPhone**;**不晚於 2040 解決所有機器人問題**——個人機器人、工業機器人,全部。 |
| Anastasis Germanidis | **2–3 年(窄場景)/ 5–10 年(家庭)** | 家用機器人的不確定區間很寬。他同意 Michael:**很窄的企業使用情境**——物流、工廠——**接下來兩三年就會看到部署**;但要處理**家庭的複雜度、並在「很多個 9」的可靠度下自主運作**,他認為 **5 到 10 年比較合理**。 |

**Michael 的補充上界(非技術論證)**:「我可以給一個上界嗎?**對某些經濟體,我們必須在 10 年內解決這件事**。」以日本大型製造企業為例——**任何產業、60% 的勞動力都是 50 歲以上,10 年後他們全都會離開職場。**

**Guru 的收束**:「所以邊界就是**2 到 10 年**。我們就在那之前解決它吧。」

### 金句

> "If you train a model on really good driving data and then you ask what happens if I drive into a building, it'll probably produce the building morphing into a beautiful road and you're driving happily down the road. And people have actually done this and that's exactly what happens."(約 03:11:40)

Sergey 對「影片模型懂物理」最有力的反例。

> "Yes, the model can handle physics. You have to be very careful not to let it fool you."(約 03:12)

同上的結論句,語氣是「不是不能用,是別被騙」。

> "Video is one of the sensors. It's called an RGB camera."(約 03:11)

Jim Fan 把影片從「世界的表徵」降格回「一種感測器」,順勢帶出觸覺、力、慣性等被忽略的模態。

> "Inductive bias is train data in disguise."(約 03:13:30)

Sergey 引述的說法:小規模看起來很有效的架構先驗,scale 上去就溶解了。

> "Great scientists invent, greater scientists copy."(約 03:19:30)

Jim Fan 的方法論宣言,接著就是「LLM 現在不是在造資料,是在造環境」。

> "With robots the demo is never quite what meets the eye."(約 03:29:50)

Sergey 從 Atlas 後空翻影片提煉的教訓:真正的挑戰不在 demo reel 裡。

> "For some economies — and this is not a technical argument — we're going to have to solve it in 10 years."(約 03:35:05)

Michael 從日本製造業人口結構給出的硬性上界。

## English Notes

### Setting (~03:08:47)

Moderator **Guru Chahal** (Partner, Lightspeed Venture Partners) had set the session's frame at the top (~02:09:26): Lightspeed has invested across the AI stack from Anthropic, Mistral, SSI, and Reflection through robotics companies like Dexterity and Skild, and **the common view is that robotics is still in its pre-ChatGPT moment** — a view he broadly shares, while arguing **the inflection point may be closer than most people realize**.

He deliberately skipped the opening "define a world model" question (it would eat the next twenty minutes) and refused the go-down-the-line format, instead pulling out points from the five talks where **the panelists' stances looked like they might diverge**.

### Topic 1: Does generating video alone give a model an understanding of physics? (~03:10–03:12)

**Anastasis Germanidis (the original claim)**: this is mainly an **empirical conclusion** from scaling the models and measuring how they perform on physics-related tasks. Their methodology: **if you want to introduce inductive biases, introduce them in the data you train on, not in the architecture.** So they very intentionally learn everything directly from pixels with no 3D priors, and it has worked well — past a certain scale you get good geometric consistency, which is also measurable. He sees no **fundamental reason** it won't keep scaling.

**Jim Fan (agrees, then narrows it)**: despite Guru's ban, he offered a definition to ground the discussion — a **world model is a model that predicts the next sensory state conditioned on actions**. Under that definition, **video is convenient, and video is one of the sensors: it's called an RGB camera.** But a robot can have more than one RGB camera, and many other sensors besides. He argues **today's world-model discussion is missing modalities**: beyond video there is **tactile, force, and inertial sensing**, and all of it needs to go into these models for a genuinely **holistic** simulation of how dynamics evolve. "Video is convenient, video is easy to scale, it's abundant — **but that's not the full story.**"

**Sergey Levine (the strongest pushback)**: if you generate videos that people find compelling, **it is very easy to end up with video that looks great to humans while not reflecting the model's ability to simulate the physical counterfactuals you actually care about.** The crux: when you give a model a prompt, it **doesn't have to** predict what will happen to a real physical system if it does something. It only has to produce a result that, to you, looks like a good reflection of the prompt. **Which means the model gets to choose how to set everything up so it looks good — and that choice is enormously important.** Whereas if you need to plan and act in the real world, you must handle the actual situation you're in, the actual plan you're making, and whatever counterfactual effects follow.

His example is blunt: **train a model on really good driving data, then ask what happens if you drive into a building, and it will probably produce the building morphing into a beautiful road with you driving happily down it. People have done this, and that is exactly what happens.** So the answer is: **yes, the model can handle physics; you just have to be very careful not to let it fool you.** And as Anastasis said, it comes down to data — it's just that **the data that produces really great video is not the data that produces counterfactuals.**

### Topic 2: Is the VLA era over — is it all world-action models now? (~03:12–03:16)

**Jim Fan**: it depends on the level of abstraction you work at. Splitting by system 1 / system 2:

- **System 1** (fast, reactive motor skills): **WAM is very promising.** A lot of physical common sense — how do you grasp a cup — is, from first principles, **very difficult to break down and describe frame by frame in language tokens.**
- **System 2** (reasoning, coding, tool calling): he argues **Opus and the GPTs are actually VLAs** — these models are agentic and they take actions. And **more people use VLAs than WAMs today**, because VLAs also serve other purposes, including the **agentic scaling** he covered in his talk: models that understand the world through perception, call tools, and help with auto-research.

He doesn't see one completely replacing the other. **It's about the abstraction level you operate at.**

**Sergey Levine (thinks the question is subtly wrong)**: "It's the right question for *you* to ask *us*, but maybe the wrong question for a researcher to ask themselves" — because it **puts the model before the data**. The key to a really good foundation model is being able to **productively ingest lots of very diverse data**, and video is one great source of it. In fact, **most VLAs that are actually good are trained on lots of video data** — it just happens in a web-scale pretraining phase that trains the understanding backbone.

So the right question isn't VLA-or-video, it's **how do you use the most data**. On top of that sits inductive bias, and as the saying he quoted goes, **"inductive bias is training data in disguise"** — **its effect may be large when you test at small scale, but it dissolves away once you scale up.** What we should actually do is leverage as many data sources as possible, then be **pragmatic about what outputs the model needs** in order to leverage them.

**Michael Spranger (two points from the application side)**:

1. **Language isn't all that helpful for their tasks.** For racing and table tennis, you can *describe* the skill but there's very little information in the description. Cognitive science's classic distinction between **declarative and procedural knowledge** applies: to ride a bike you have to actually do it and learn the physics.
2. **Vision isn't always available.** Vision is a great thing to condition on, but in some applications you can't. Ship a game to a customer with 20 agents racing and **you cannot render from 20 different viewpoints** — most of the PlayStation's compute goes to rendering for the player.

So these **aren't yes/no questions**: what domain do you care about, what are you solving, what's the downstream application? Large foundation models that capture visual and language knowledge are often extremely helpful, but **you still need to distill the thing you actually care about in a given moment and ship it to a consumer.**

**Anastasis Germanidis (adding on)**: there's broad convergence toward **omni-models** that predict visual, audio, and text modalities alike. So, to Sergey's point, it comes down to **what you specialize the model on during pretraining** — is the data mix biased toward low-level motion planning or high-level reasoning? **It's less about WAM-versus-VLA architecture and more about what you dedicate the model's capacity to** — and that's the important factor.

**Guru's summary**: "It's not an either-or. It really is use-case dependent, and both have interesting applicability."

### Topic 3: How much real-world RL versus the digital world? (~03:16–03:22)

**Wei Zhan (separates by application)**:

- **Autonomous driving**: they care more about **behavior** and the **visual modality**, and both are relatively easy to scale from real-world data and inject into a synthetic world. Today, **most leading players in productionized end-to-end ADAS rely mainly on real-world data, with synthetic data used in post-training** — but the trend is clear that **large-scale synthetic data will play an increasingly key role** in making autonomy robust and safe.
- **Robotics**: at this point, for **locomotion and whole-body tracking**, RL-based methods are very useful and even dominant. But for complex tasks like **dexterous manipulation**, it's hard both to build a high-fidelity synthetic world capturing the key physics attributes and to define a good reward function for closed-loop training. So **behavior cloning and imitation-based methods still dominate there.**

**Sergey Levine (splits supply side from demand side)**: the future will look very different from the present.

- **Now**: robotics is in the **bootstrap stage** — still figuring out what it would take for robot models to be good enough to be usable with end-to-end learning.
- **Later**: we won't be bootstrapping forever. Eventually there will be **as many robots deployed as there are vehicles on the road today**, and therefore **very plentiful data from robots interacting with the world autonomously** — at which point **RL methods that can consume real-world data will be tremendously important.**
- **A second reason**: as imitation learning methods keep improving, the challenge increasingly becomes **bridging the last gap — how do you go from a 98% successful policy to 100%?** There the **domain gap really matters**, because everything has to line up perfectly. So **real-world RL will be needed there too.**

But he timestamped it explicitly: **"that's what's coming in the future; I don't think that's the state today"** — calling Wei's account of the present an excellent summary.

**Jim Fan (copy the LLM homework; three environment options)**: "Great scientists invent, greater scientists copy." He watches what the LLM people are doing, and **they're not just creating data anymore — they're creating environments.** It's about acquiring millions of coding environments and doing RL in them; that's how we got today's Mythos and GPT-class models. **Not through imitation learning — eventually through reinforcement learning.** Robotics needs to build environments too, and there are three options:

1. **The real world.** "Sergey and π have done exceptional work over there." Absolutely important — **the physics is perfect because it *is* the real world.**
2. **Classical simulators** (Isaac Sim and the like). The bottleneck **isn't simulation speed** — simulation runs very fast — **it's the assets, environments, and tasks** that used to require armies of artists. But **real-to-sim** recipes now look super promising: **automatically scan the world and transport it into a classical simulator**, so you're data-driven while still leaning on a fast classical physics solver.
3. **World models as neural simulators.** A very practical use of a video world model is as a **data-programmed neural simulator**: take actions as input, generate video and sensor states, use it as an environment. It **runs very slowly**, but it has **a huge amount of diversity** — as much as a world model can afford.

Ultimately robotics RL will run **across all three options**, using different types of compute under different constraints. He'd like to see a more holistic approach.

### Topic 4 (rapid fire): Most amazing recent demo — not from your own company (~03:22–03:27)

| Speaker | Pick | Why |
|---|---|---|
| Anastasis Germanidis | **Photon-1, from Induction Labs** | A world model built on **screen recordings** — a digital world model of sorts. They trained it **entirely on screen recordings**, without the text supervision usually leveraged for computer-use models, and reached performance competitive with one of the small Gemini models on computer use **with an order of magnitude less compute**. Guru's aside: "That says more about the nature of the work we do on a screen than anything else." |
| Jim Fan | **Tesla FSD** | "A robot that millions of people already buy and use daily." He's been driving a Tesla since last year and was amazed by the latest versions — rush hour, super crowded lanes, and the policy negotiates almost humanlike, sometimes better than he would drive himself. That gives him hope: **once you spin the physical data flywheel you get a quantum leap** versus a couple of years ago. It's exactly why his talk stressed that data collection must fade into the background and stay non-intrusive. |
| Michael Spranger | **General Intuition's Rocket League world model** | Not robotics, but a breakthrough roughly two weeks old: the world model **renders four different player views of the same world consistently.** Traditional world models are "me and the world, my actions in the world"; this unlocks a **multi-agent / multiplayer** future. He thinks that matters because **robotics often thinks purely about task performance — lifting a cup, screwing something — while the world is full of other agents**, people or AIs, that we'll have to interact with. He'd expected this six to twelve months out. |
| Sergey Levine | **The Boston Dynamics Atlas backflip** (with a moral) | The video went viral because the robot **doesn't quite stick the landing**, freaks out into a weird unnatural motion, and then **stays upright**. Around CES, with humanoid demos everywhere, people mocked it and pointed at Unitree robots doing perfect backflips. But **roboticists looked at it and realized the Boston Dynamics video is far more impressive precisely because it doesn't fall**: something horrible happens, it freaks out, and it stays up — on a **170 kilogram** robot, much heavier and more complex than the lightweight Unitree machines. **The lesson: with robots, the demo is never quite what meets the eye.** The challenge is usually not what's in the demo reel — it's the degree of generalization, the system's ability to handle unfamiliar situations and failures, and all the complexity behind it. It's easy to be misled by a demo and miss where the genuinely hard problems are. |
| Wei Zhan | **Tesla FSD**, plus two more | He echoed FSD, which now covers most of his daily mileage. He also rode in the R&D car of a company he can't name that sustained **an hour of driving in super crowded streets full of pedestrians and cyclists with zero driver intervention** — on **one-seventh the onboard compute of Tesla's HW4** and a simpler sensor suite. On the robotics side, at a conference booth this year he saw a Chinese startup pushing the boundary on **synthetic data**, doing generalizable **zero-shot pick-and-place** with audience members throwing arbitrary objects onto the table. |

### Topic 5 (rapid fire): What year is robotics' "Claude Code moment"? (~03:27–03:35)

Guru's framing: LLMs had a ChatGPT moment, and then a **Claude Code moment** — the point where the **first commercial use case genuinely takes off and rockets.** He wanted a number, plus a word or two on the use case.

| Speaker | Number | Domain & reasoning |
|---|---|---|
| Wei Zhan | **~3 years** | Beyond large-scale egocentric and third-person data, we also need the **necessary physics modalities, well grounded and associated with it**, to be filled in. Accumulating that data takes time and is one of the gating factors for robot foundation models. |
| Sergey Levine | **3 years** | (He noted he picked the number *before* hearing Wei's answer.) But **he doesn't know the area** — and that's the point: what's needed are **models general enough to radically lower the barrier to exploring different applications**, so the community can collectively get through as many possibilities as possible and arrive at the answer. **The general model is the precondition, not the outcome.** |
| Michael Spranger | **2 years** | (He first joked "three years," got heckled, and dropped to two.) The area will be **industrial**, because it's a **semi-structured domain** with better data availability — warehousing, manufacturing. He thinks the **technology is more or less there**; it's more a question of finding the right **economics**, data inputs, and environments where you can actually deploy. **Large robots in the home are further out for safety reasons.** The recipe for semi-structured environments: tailor the use case, bring in general models, combine with on-site or simulation training. |
| Jim Fan | **2030 / 2035 / 2040** | Earliest 2030; **more robots than iPhones by 2035**; **all of robotics solved no later than 2040** — personal robots, industrial robots, everything. |
| Anastasis Germanidis | **2–3 years (narrow) / 5–10 years (home)** | The uncertainty bar for household robotics is wide. He agrees with Michael that **very narrow enterprise use cases** — logistics, the factory — will see deployment in the next two or three years. But handling **the complexity of a home and operating autonomously at many nines of reliability** looks more like **5 to 10 years.** |

**Michael's upper bound (an explicitly non-technical argument)**: "Can I give an upper bound? For some economies **we're going to have to solve it in 10 years.**" Take large Japanese corporations in manufacturing, or any industry: **60% of the workforce is 50 or older, and in 10 years they will all be gone.**

**Guru's close**: "So those are the bounds. Two to ten. Let's solve it by then."

### Quotes

> "If you train a model on really good driving data and then you ask what happens if I drive into a building, it'll probably produce the building morphing into a beautiful road and you're driving happily down the road. And people have actually done this and that's exactly what happens." (~03:11:40)

Sergey's sharpest counterexample to video-models-understand-physics.

> "Yes, the model can handle physics. You have to be very careful not to let it fool you." (~03:12)

The conclusion of that exchange — not "don't use it," but "don't be fooled by it."

> "Video is one of the sensors. It's called an RGB camera." (~03:11)

Jim Fan demoting video from "a representation of the world" back to "one sensor," and using it to surface tactile, force, and inertial modalities.

> "Inductive bias is train data in disguise." (~03:13:30)

Sergey's borrowed line: architectural priors that look powerful at small scale dissolve once you scale.

> "Great scientists invent, greater scientists copy." (~03:19:30)

Jim Fan's methodological credo, immediately followed by "the LLM folks aren't creating data anymore, they're creating environments."

> "With robots the demo is never quite what meets the eye." (~03:29:50)

Sergey's moral from the Atlas backflip: the real challenge isn't in the demo reel.

> "For some economies — and this is not a technical argument — we're going to have to solve it in 10 years." (~03:35:05)

Michael's hard upper bound, argued from Japanese manufacturing demographics rather than from capability curves.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Photon-1 (Induction Labs) | 完全以螢幕錄影訓練的 world model,computer use 表現可與小型 Gemini 競爭,算力少一個數量級 | World model trained entirely on screen recordings; competitive with a small Gemini model on computer use at an order of magnitude less compute | Anastasis 的「最驚豔 demo」/ Anastasis's pick |
| General Intuition — Rocket League world model | 能一致渲染四個玩家視角的多 agent world model | Multi-agent world model rendering four consistent player views | Michael 的選擇,約座談前兩週發布 / Michael's pick, released about two weeks prior |
| Tesla FSD | 被 Jim 與 Wei 同時點名的實體資料飛輪範例 | The physical data flywheel example named by both Jim and Wei | |
| Boston Dynamics Atlas | 後空翻沒站穩卻沒倒的爆紅影片;170 公斤 | The viral backflip that misses the landing but stays upright; 170 kg | Sergey 用來說明「demo 不是表面看到的那樣」/ Sergey's illustration that demos mislead |
| Unitree | 影片中被拿來對比、做出完美後空翻的輕量人形機器人 | The lightweight humanoids doing perfect backflips in the comparison | |
| Isaac Sim | Jim 舉的傳統模擬器代表;瓶頸在資產而非模擬速度 | Jim's example of a classical simulator; the bottleneck is assets, not simulation speed | |
| real-to-sim | 自動掃描真實世界搬進古典模擬器的配方 | Recipes that automatically scan the real world into a classical simulator | Jim 認為極有潛力 / Jim calls it super promising |
| Lightspeed 投資組合 / portfolio | Anthropic、Mistral、SSI、Reflection;機器人有 Dexterity、Skild | Anthropic, Mistral, SSI, Reflection; in robotics, Dexterity and Skild | 主持人開場提及 / from the moderator's opening |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Guru Chahel / Duru | Guru Chahal |
| Lightseed Venture Partners | Lightspeed Venture Partners |
| Enthropic | Anthropic |
| Mistrol | Mistral |
| Skilled | Skild |
| pre-hat GPD moment | pre-ChatGPT moment |
| clawed code moment / clot code moment | Claude Code moment |
| VA / VAS | VLA / VLAs |
| WHM / wham / whams | WAM / WAMs (world action models) |
| methos | Mythos |
| Udantry / unitry | Unitree |
| many nons of reliability | many nines of reliability |
| induction labs / Photon one | Induction Labs / Photon-1 |
| general intuition | General Intuition |
| Mika | Michael (Spranger) |
| Wei Jean / Ray / Way | Wei Zhan |
| Anastasio | Anastasis (Germanidis) |
| Ike(“as Ike used to say”) | 待確認 / to verify |

## 待確認 / To Verify

- Sergey 引用「inductive bias is train data in disguise」時提到的人名,字幕聽成 "Ike",無法確認是誰。/ The person Sergey credits for "inductive bias is training data in disguise" — the caption renders it "Ike"; attribution unconfirmed.
- Wei 提到的中國新創,字幕聽成 "Sudu",做 zero-shot 可泛化 pick-and-place;公司名待查。/ The Chinese startup Wei mentions doing zero-shot generalizable pick-and-place — caption renders it "Sudu"; company name unconfirmed.
- 同段的展場名稱,字幕為 "the Acura and the CPR booth",推測為 ICRA 與 CVPR,需影片確認。/ The conference booths in the same anecdote read as "the Acura and the CPR booth" — likely ICRA and CVPR, needs video confirmation.
- Wei 提到「算力僅 Tesla HW4 的 1/7、可連續一小時零接管」的公司未具名,無法查證。/ The unnamed company achieving one hour of intervention-free driving at 1/7 the compute of Tesla HW4 cannot be verified.
- Anastasis 引用的 Photon-1 對照模型,他說是「Gemini 或某個小型 Gemini 模型」,未確定具體版本。/ The exact Gemini variant Photon-1 was compared against was left vague on stage.
