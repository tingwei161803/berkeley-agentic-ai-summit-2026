---
title: "Personal AI and Continual Learning: New Frontiers in Agentic AI"
title_zh: "Personal AI 與持續學習:Agentic AI 的新前沿"
speaker: "Igor Babuschkin"
affiliation: "Co-Founder/CEO, River AI"
type: talk
stage: Plenary
date: 2026-08-02
session: "Session 2: Frontier Research"
video: "https://www.youtube.com/watch?v=I2PosBXwoPI&t=2563s"
video_range: "00:42:43–00:53:44"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [personal-ai, memory, personalization, continual-learning, lora]
---

# Personal AI 與持續學習:Agentic AI 的新前沿(Personal AI and Continual Learning: New Frontiers in Agentic AI)

**一句話總結**:coding agent 之所以成功是因為有可驗證的獎勵,而下一個大方向 personal AI 沒有——他把它拆成五個尚未解決的難題(RL、個人化、記憶、隱私安全、成本),並主張這同時是一個把 AI 的控制權還給個人的機會窗口。
**One-line summary**: Coding agents worked because rewards were verifiable; personal AI has no such luxury. He breaks the gap into five unsolved problems — RL for the use case, personalization, memory, privacy/security, and cost — and argues the same shift is a rare chance to hand control of AI back to the individual.

## 中文筆記

> 他上台時投影片系統掛掉,他一邊說「我可以完全即興」一邊繼續講,約一分鐘後投影片才恢復。演講最後他補了一句:**「順帶一提,這整份東西是我的 personal agent 寫的,因為我今天有點懶。」**

### TL;DR

- **coding agent 的成功是可驗證獎勵的成功**:agent 寫程式 → unit test 驗證 → 給 reward → 整套 RL 工具鏈就能把它推到極強。問題是,**下一個領域沒有 unit test。**
- **他看到的三個方向**:科學發現與自我改進、自動化整個經濟、以及他個人最投入的 **personal AI**——一個 24/7 陪著你、深刻理解你、會主動找你的數位實體,可能成為繼 PC / 手機 / 網際網路之後的下一個計算典範。
- **五個還沒解決的硬問題**:(1) 直接為 personal AI 做 RL(今天的 personal agent 其實是 coding agent 硬套過來的);(2) 個人化;(3) 記憶與長 context(任務可能橫跨數天);(4) 隱私與安全(prompt injection——你的敵人傳一串字給你的 agent 就把它接管了);(5) **成本**(24/7 跑,一個月輕易上看數千美元)。
- **記憶的兩種哲學**:in-context(存電話號碼、過去對話這種離散事實)vs. 權重層更新(存「使用者偏好」「他寫 email 的語氣」這種隱性知識)。兩邊各有做不到的事,**所以兩種都需要**。
- **也是一次奪回控制權的機會**:mainframe → PC → 手機的路線上,雲端 AI 其實是往回走一步(裝置不是你的、推論不是你的)。personal AI 有機會把模型權重與私人資料放回你家裡的裝置上。

### 重點整理

#### coding agent 之後是什麼?(約 00:43–00:46)

他的起點是今年最明顯的事實:**coding agent 有巨大的經濟吸引力**,你可以只靠「提供 coding agent」就撐起一家超賺錢的科技公司。原因很單純——**coding 有 verifiable reward**:agent 寫出程式,unit test(或其他可驗證方式)判斷對錯,給出 reward 訊號,然後 RL 的整套工具就能把 agent 推到極強。而且大家都同意 coding 是那種「要往別的領域走之前,先解掉的基礎積木」。

那接下來呢?他看到三個方向:

1. **科學發現**——agent 越來越聰明,可能改進自己、發現更好的演算法、提升自身智慧(呼應同場前兩位講者)。
2. **自動化經濟**——把 agent 帶進經濟的所有環節,每家公司都自動化自己的工作。
3. **Personal AI**——他個人最投入的方向。

他描述的 personal AI 不是聊天機器人,是**每個人都有一個陪伴自己的數位實體**:深刻理解你、能主動找你、讓你的生活更順、更快樂。**這可能就是下一個計算典範**——PC、手機、網際網路之後,是「深刻理解你並協助你的數位實體」。

現況他也講得很誠實:已經有 **OpenClaw** 這類早期的 personal AI 系統,但玩過的人都知道**離大眾市場還很遠**——你得自己折騰不少、還得好好維護。

#### 五個沒解決的問題(約 00:46–00:48)

1. **要直接為 personal AI 做 RL。** 今天的 personal AI 系統,說穿了常常是 coding agent 硬泛化到 personal AI 的使用情境。這件事得認真解。
2. **個人化。** 如果一個 agent 24/7 在背景自主做事,它最好非常清楚該怎麼幫你。
3. **記憶與長 context。** 有些任務會橫跨一整天甚至好幾天。
4. **隱私與安全。** 他舉的例子最有畫面:**想像你的朋友——或你的敵人——傳一串字給你的 personal agent,就此接管它、拿走你所有的祕密。** 這必須擋掉。
5. **成本。** 把 agent 24/7 在背景跑掉的 token 加總起來,**一個月很容易就到數千美元**,對大多數人來說根本負擔不起。

#### 順帶的機會:把控制權還給個人(約 00:48–00:49)

他把這件事放進計算史的脈絡:mainframe → 個人電腦 → 智慧手機,控制權一路往個人手上走;而**雲端 AI 是往回退了一步**——實體裝置不是你的,做推論的能力也不是你的,控制權集中在提供 LLM API 的公司手上。

**personal AI 有機會回到那個 regime**:你家裡或辦公室裡有一台實體裝置,裡面裝著模型權重、存著你的私人資料——更安全、對隱私更好。他講得很有分寸:**這不是必然會發生,但這是一個機會,讓我們可以蓋一個真正對個人有利的東西。**

#### 研究方向一:agent 記憶的兩種哲學(約 00:49–00:50)

- **In-context 記憶**:記憶是一個 agent 可以存取的系統,資訊主要以 token / 文字的形式流動。適合取回一個電話號碼、一段過去的對話。
- **權重層更新**:直接改模型本身。

兩邊的弱點正好互補:**權重層很難存住「某個電話號碼」「某人的名字」這種個別事實;而 in-context 這邊很難存住隱性知識**——我的使用者偏好是什麼?他寫 email 的風格是什麼?我能不能模仿?這些東西太難寫進一個文字檔。**所以他的結論是兩種都需要**,並在投影片上列了兩派各自的研究論文。

#### 研究方向二:個人化的兩種做法(約 00:50–00:51)

問題是:怎麼讓模型不只對齊「整個使用者群體」,而是對齊**它正在服務的那一個人**。他認為這對「agent 能可靠地代表你、在背景替你把事情做成」是關鍵。

- **被動**:觀察使用者在做什麼,善用他日常生活中產生的所有資料。
- **主動**:主動探問使用者的偏好,或直接對他的回饋做最佳化——我說「這個好、那個不好」,系統就更新權重或更新 prompt,讓它越來越適合我。

#### 研究方向三:基礎設施——multi-tenant LoRA 與本地硬體(約 00:51–00:53)

personal AI 可能需要一整套跟今天不同的工具與新部署的基礎設施。他點出兩個現在就有用的方向:

**Multi-tenant LoRA。** 以前要訓練模型得更新全部權重,而現在動輒上兆參數。LoRA adapter 只佔權重的一小部分、訓練時只動那一小塊,於是 post-training 與 RL 都能做得更有效率——**甚至打開「未來每個使用者一個客製化微調模型」的可能性**,也能用來做 continual learning 的實驗。River AI 自己蓋了一套 multi-tenant LoRA 系統並已釋出。

**本地硬體。** 把推論從資料中心搬到你手上、家裡或辦公室的裝置。今天才剛開始有人探索,**最佳化本地推論還有大量低垂的果實**,他認為本地推論總有一天可能與資料中心推論分庭抗禮。**最大的瓶頸是模型容量**:怎麼把上兆參數塞進小小的 form factor、又怎麼在不把家裡烤熟的前提下高效推論。今天要做到這件事得一整櫃 GPU,他希望未來只要一台裝置。

最後他推薦了自家的 `river.ai/api`(multi-tenant LoRA 系統,可用來做 post-training / RL 研究與 continual learning 實驗),然後丟下那句「這整份東西是我的 personal agent 寫的,因為我今天有點懶」。

### 金句

> "Imagine that your friend — or your enemy — texts your personal AI agent a string that then allows them to take it over, and they can get all your secrets."(約 00:47)

prompt injection 在 personal AI 情境下的具體長相。

> "Cloud AI is sort of a step away from giving the individual control. You don't have the physical device. You don't have the means for doing inference."(約 00:48)

他為什麼把 personal AI 同時當成一個所有權議題。

> "By the way, this whole thing was written by my personal agent, because I was pretty lazy today."(約 00:53)

演講的最後一句話。

## English Notes

> The slides failed as he took the stage. He offered to improvise the whole talk and kept going for about a minute until they came back. His closing line: "By the way, this whole thing was written by my personal agent, because I was pretty lazy today."

### TL;DR

- **Coding agents succeeded because rewards are verifiable**: the agent writes code, a unit test judges it, the reward signal feeds RL, and the whole reinforcement-learning toolbox makes the agent extremely powerful. The catch: the next domain has no unit test.
- **Three directions he sees**: scientific discovery and self-improvement, automating the economy, and — his own passion — **personal AI**: a digital entity that accompanies you, understands you deeply, and reaches out proactively. Possibly the next computing paradigm after the PC, the phone, and the internet.
- **Five unsolved problems**: (1) running RL for the personal-AI use case itself (today's personal agents are coding agents generalized sideways); (2) personalization; (3) memory and long context, for tasks spanning days; (4) privacy and security, e.g. prompt injection; (5) **cost** — an agent running 24/7 easily reaches thousands of dollars a month.
- **Two philosophies of memory**: in-context (discrete facts — a phone number, a past conversation) versus weight-level updates (implicit knowledge — preferences, the style someone writes emails in). Each fails where the other works, so you need both.
- **Also a window to hand control back**: along the mainframe → PC → smartphone arc, cloud AI is a step backwards. Personal AI could put the model weights and your private data on a device in your own home.

### Key Points

#### What comes after coding agents? (~00:43–00:46)

He starts from the year's most visible fact: coding agents have enormous economic appeal — you can build an extremely profitable company purely on serving them. The reason is structural. **Coding has verifiable rewards**: the agent writes code, a unit test or equivalent decides whether it was right, that becomes a reward signal, and RL takes it from there. Everyone agrees coding is one of the fundamental building blocks you solve before moving to other domains.

So what's next? Three directions: scientific discovery and self-improvement (echoing the two speakers before him), automating the economy, and personal AI.

His picture of personal AI isn't a chatbot. It's a digital entity that accompanies each of us, understands us deeply, proactively reaches out, and makes life happier and smoother. He's willing to call it a candidate for the next computing paradigm after the personal computer, the mobile phone, and the internet.

He's candid about where it stands: early systems like **OpenClaw** exist, but anyone who has played with them knows there's no mass-market appeal yet — you have to tinker, and you have to maintain them carefully.

#### The five unsolved problems (~00:46–00:48)

1. **RL for the personal-AI use case.** Today's personal AI systems are frequently coding agents generalized into a use case they weren't trained for.
2. **Personalization.** An agent running 24/7 in the background, acting autonomously, had better understand precisely how to help you.
3. **Memory and long context**, because tasks can span a full day or several.
4. **Privacy and security.** His example lands: imagine a friend — or an enemy — texting your personal agent a string that takes it over and hands them all your secrets.
5. **Cost.** Add up the tokens an always-on background agent consumes and you reach thousands of dollars a month, which is prohibitive for most people.

#### The ownership opportunity (~00:48–00:49)

He places this in the arc of computing: mainframes → personal computers → smartphones moved control toward the individual, and **cloud AI is a step back the other way** — you don't own the physical device and you don't own the means of inference, so control sits with the companies serving LLM APIs.

Personal AI is a chance to return to that regime: a physical device in your home or office holding the model weights and storing your private data — more secure, better for privacy. He's careful about the claim: it isn't guaranteed, but it's an opportunity to build something genuinely for the benefit of the individual.

#### Direction 1: two philosophies of agent memory (~00:49–00:50)

- **In-context memory**: a memory system the agent queries, with information moving as tokens or text. Good for retrieving a phone number or a past conversation.
- **Weight-level updates**: changing the model itself.

Their weaknesses are complementary. At the weight level it's genuinely hard to store an individual fact like a phone number or someone's name. In the in-context world it's hard to store implicit knowledge — what my user's preferences are, what style they write their emails in, whether I can imitate it. That's very hard to specify in a text file. His conclusion: we need both, and his slides list research papers pursuing each.

#### Direction 2: two approaches to personalization (~00:50–00:51)

The problem is aligning the model not with the whole user population but with the individual it serves — which he considers essential if the agent is going to reliably represent you and get things done in the background.

- **Passive**: observe what the user does and leverage the data they generate in the course of their life.
- **Active**: probe the user about their preferences, or optimize directly against their feedback — I say "this was good, this wasn't," and the system updates weights or prompts accordingly.

#### Direction 3: infrastructure — multi-tenant LoRA and local hardware (~00:51–00:53)

Personal AI may need a different toolset and newly deployed infrastructure. Two directions are useful today:

**Multi-tenant LoRA.** Training used to mean updating all the weights, which now number in the trillions. LoRA adapters represent a small fraction of the weights and are the only thing modified during training, which makes post-training and RL far more efficient — and opens up **one custom fine-tuned model per user**, plus continual-learning experiments. River AI has built and released its own multi-tenant LoRA system.

**Local hardware.** Moving inference from the data center to a device in your hand, home, or office. People are only starting to explore this, and there's a lot of low-hanging fruit in optimizing local inference; he thinks it might one day rival data-center inference. The bottleneck is model capacity: fitting trillions of parameters into a small form factor and running inference efficiently without overheating your house. Today that takes a whole rack of GPUs; he's hoping for a single device.

He closes with a plug for `river.ai/api` — and the line about his personal agent having written the talk.

### Quotes

> "Imagine that your friend — or your enemy — texts your personal AI agent a string that then allows them to take it over, and they can get all your secrets." (~00:47)

Prompt injection, rendered concrete in the personal-AI setting.

> "Cloud AI is sort of a step away from giving the individual control. You don't have the physical device. You don't have the means for doing inference." (~00:48)

Why he treats personal AI as an ownership question as much as a capability one.

> "By the way, this whole thing was written by my personal agent, because I was pretty lazy today." (~00:53)

The last line of the talk.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| River AI | 他的新公司,目標是讓每個人對自己的 AI 有更多控制與所有權 | His new company: give each individual more control and ownership over their AI | `river.ai/api` |
| River AI multi-tenant LoRA | 他們自建並已釋出的 multi-tenant LoRA 系統,用於高效 post-training / RL 與 continual learning | Their own released multi-tenant LoRA system for efficient post-training/RL and continual learning | panel 中他把它與 Tinker 並列為「民主化的工具」(約 01:18) |
| OpenClaw | 他點名的早期 personal AI 系統之一 | One of the early personal-AI systems he names | |
| LoRA adapters | 只更新一小部分權重的微調方法,是 multi-tenant 個人化模型的技術前提 | Fine-tuning that updates only a small fraction of weights; the enabler for per-user models | |
| WaveNet / StarCraft agents / xAI | 他自我介紹中的經歷(DeepMind → OpenAI → xAI → River AI) | His background, per his self-introduction | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Ego Babushkin / Igor Babushkin | Igor Babuschkin |
| RAI / RiverAI / river AI | River AI |
| Laura / Laura adapters | LoRA / LoRA adapters |
| giving the indigo control | giving the individual control |
| continue learning | continual learning |
| personal air systems | personal AI systems |
| Deepmind | DeepMind |
| XAI | xAI |
| massive economic appeal（原文 "know massive"） | 語助詞誤植,語意為 massive economic appeal |

## 待確認 / To Verify

- 他點名的第二個早期 personal AI 系統,字幕作 "**Hermes agent**",無法確認是哪一個專案(Nous Research 的 Hermes?其他同名系統?)。/ The second early personal-AI system he names is transcribed as "Hermes agent" — the actual project is unidentified.
- 投影片上列出的 memory 與 personalization 研究論文清單,逐字稿沒有唸出來,需看影片畫面補上。/ The memory and personalization papers are only on the slides; the transcript doesn't name them.
- 「一個月輕易數千美元」的成本估算是他的口頭估計,未給計算依據。/ The "thousands of dollars a month" figure is a spoken estimate with no stated basis.
- River AI multi-tenant LoRA 系統的釋出形式(開源?API-only?)講者未說明。/ He doesn't specify how the multi-tenant LoRA system was released (open source? API only?).
