---
title: "Panel: Agentic AI Infrastructure & Platform"
title_zh: "座談:Agentic AI 基礎設施與平台"
speaker: "Peter DeSantis、Saurabh Tiwary、Jonathan Cohen、Chuan Li(主持:Todd Graham)"
affiliation: "Amazon / Google DeepMind / Nvidia / Lambda(主持:Managing Partner, M12)"
type: panel
stage: Plenary
date: 2026-08-01
session: "Session 1: Agentic AI Infrastructure & Platform"
video: "https://www.youtube.com/watch?v=gKdeLQd_LIQ&t=5655s"
video_range: "01:34:15–01:58:00"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 1st - Morning Session [DownSub.com].srt"
status: draft
tags: [infrastructure, panel, neocloud, protocols, agent-platform]
---

# 座談:Agentic AI 基礎設施與平台(Panel: Agentic AI Infrastructure & Platform)

**一句話總結**:四位講者對「agentic 工作負載比我們見過的一切都更複雜、異質、昂貴」有高度共識,分歧則出現在該不該現在就標準化、以及 agentic stack 的利潤最終落在誰手上。
**One-line summary**: The four panelists agree that agentic workloads are more complicated, heterogeneous, and expensive than anything the industry has run before; where they diverge is on whether to standardize now and on where margin in the agentic stack ultimately lands.

**與談人 / Panelists**
- **Peter DeSantis** — SVP, Foundational AI Models, Custom Silicon, Quantum Computing, Amazon
- **Saurabh Tiwary** — Vice President, Google DeepMind
- **Jonathan Cohen** — VP of Applied Research, Nvidia
- **Chuan Li** — Chief Scientific Officer, Lambda
- **主持 / Moderator:Todd Graham** — Managing Partner, M12

## 中文筆記

### 開場框架:從 chat 到 machine speed(約 01:35)

Todd Graham 給的背景:ChatGPT 時代的介面是 chat——一個請求、一個回應、相對短的 context、短爆發式互動。agent 則以 machine speed 運行,有時一跑就是好幾個小時(「你有 12 個 agent 幫你整晚寫程式」),伴隨龐大的工具呼叫量與 token prefill。他問全場:有沒有人設了 agent 跑一整晚、醒來發現 token 額度被自動續購了?——幾乎全場舉手。

### 主題一:今天 agent 工作負載最大的失敗點在哪?(約 01:36–01:39)

- **Chuan Li**:答案就在問題裡。想像把 machine-speed 的車流放上一條為人類駕駛設計的道路——**先壞掉的會是道路容量、紅綠燈與速限**。機會在於**把這些 choke point 變成 checkpoint**。
- **Jonathan Cohen**:癥結是 LLM 這個元件——它們可靠得出人意料,但也會做出出人意料的事、以不可預測的方式行動。所以最大的機會是用**規則式的政策強制執行、更確定性的系統與記憶體系統**把它包起來,讓你對它實際在做什麼更有信心與確定性。
- **Saurabh Tiwary**:這個答案一直在變、也一直在演化。
  - **計算層**:要把 bubble 盡量消掉才能榨出效率。
  - **基礎設施層**:請求來自世界各地,routing 要能削平尖峰,才能以低延遲有效率地使用算力。
  - **語音**正在成為很有意思的互動媒介,它的 profile 跟純文字完全不同——怎麼管理這種使用情境與計算環境的**異質性**是問題。
  - **主權(sovereignty)**需求越來越重要,而它某種程度上**打破了共用雲的哲學**,增加大量工程複雜度。
  - 加上 identity、security,這些正在極快地變成非常大的問題。
- **Peter DeSantis**:「我的答案也是全部。」這從堆疊最上層到 guardrails、到基礎設施、到電力、到跑它的晶片,都是系統問題,而且**每一環都得對**——agent 的潛力很大,但如果做不到高效率,我們只能拿到其中一部分。

**追問:那最該搬的大石頭是什麼?如果有人今天就想動手,你會指向哪裡?**
DeSantis:「我是樂觀主義者,所以我不擔心,我找機會——而我在每一層都看到機會。你剛剛已經聽到 16 個問題和上百個約束了,**挑一個、鑽深、玩得開心**。」(Todd 接梗:「也許明天下午就去蓋一座記憶體廠?」)

### 主題二:agent 工作負載和 LLM 工作負載,硬體該怎麼分化?(約 01:39–01:42)

**Jonathan Cohen** 是主要回答者:

- **context 更多**,而且「這些 context 裡有多少是可快取的」這個比例也變了。
- **異質性**:agent 是「被電腦科學包住的 LLM」,而那些電腦科學很多跑在 CPU 上、可能是多核心 CPU;也有很多跑在 GPU 上,但可能是為**不同種類工作負載**配置的 GPU——不是神經網路推論,而是例如物理模擬。
- 所以跑 agentic 工作負載的資料中心**非常異質**:許多不同的處理元件、多層儲存、複雜的網路拓撲。
- 疊在上面的還有 **security、privacy、sovereignty** 需求。
- 老實說,**業界還不太知道最好的做法是什麼**,因為 agentic AI 還在演化。AI 史上這件事反覆發生:我們以為懂了,然後新東西出現、工作負載完全不同、又更複雜。
- 結論:「**Agentic AI 工作負載比我們見過的任何東西都更複雜、更異質、計算上更昂貴。**」

### 主題三:企業要 workflow-specific 的 agent,答案是 fine-tuning 還是 context engineering?(約 01:41–01:43)

**Saurabh Tiwary** 給了一條由簡到繁的階梯:

1. **先試 context engineering**——這是最簡單的。base LLM 本身的推理能力已經夠強(Gemini 與其他模型皆然),配合長 context window,你可以塞進大量資料讓模型在其上推理;而且模型「在 context 中推理的品質」已經明顯提升。
2. **要真的動模型,從 LoRA 開始**——最容易、最便宜,推論端也很有效率、成本效益好。
3. **再上去才是 full fine-tuning 或某種程度的 post-training**——這時擾動的是模型的**全部權重**,等於你有了一份全新的模型副本,推論的動態也跟著改變,所以貴得多。
4. 極少數非常特殊的合作夥伴才會做真正客製的東西。

他的判斷是前兩層才是主力路徑。

### 主題四:observability / experiment tracking 該放在基礎設施裡還是獨立一層?(約 01:43–01:45)

**Chuan Li**:它**確實是基礎設施**,但和訓練用的環境不同。

- **Environment** 是 agent 行動與學習的地方;**experiment tracker** 則像記憶與量測,放在旁邊。
- 用大腦來類比:**environment 訓練的是第一個大腦**——學習進到模型權重裡,被壓縮、被內化,而且**容量有界**;**experiment tracker 給你第二個大腦**——學習進到 artifact 裡,**沒有上界**。
- 兩者之間有一條路可以接起來:把 system of record 轉成資料集,就能拿去 fine-tune、做 RL 等等。
- 至於該託管在哪:取決於你的資料管控政策。管制嚴格就自己託管;不是問題就用託管服務。但**如果要拿來訓練/微調,就該放得離訓練夠近**。

### 主題五:agentic stack 的利潤durability 在哪?(約 01:45–01:48)

Todd 的問題:我們夾在模型與 agent 產出之間,有 orchestration、sandboxing、runtime、memory、identity、eval——如果現在要進場,該做 memory 還是 sandbox?錢最後會在哪一層被賺走?

- **Peter DeSantis**(插話):「**At the hardware.**」(全場笑)
- **Saurabh Tiwary**:AI 之所以被採用,是因為**結果的品質**、或開發者/建造者的**體驗品質**。商業機會顯然巨大;呼應 Peter 的說法——**問題有一堆,挑一個、鑽到非常深**。只要你把對客戶的承諾交付到夠高的品質,價值就會在那裡被萃取出來。以 memory 為例:重點不是「我在做 memory」,而是**你有沒有給客戶一個有說服力的體驗**,讓他們真的能靠 memory 交付該交付的東西,而不只是「我用了 memory,這裡有些 prompt 被更新了」。這種價值橫跨整個堆疊——硬體層、模型層、agentic 層、應用層都有。而且因為 AI 的熱度與幾乎每家大公司的 CXO 都在想 AI,商業機會非常大,關鍵只在**能不能交付價值**。
- **Chuan Li**:完全同意硬體那一票,但也想補**垂直整合**這一點。因為他來自 neocloud,大家常以為雲運算是 commodity——大體上沒錯,但**雲運算其實非常難**:從土地、電力、資料中心建設,到 HPC 架構、orchestration、軟體與財務,是一整條垂直堆疊。而 agent 這一新層——**你叫它 sandbox、叫它 harness、叫它 system of record 都行**——是要被整合進這條垂直線的新一層。**誰在那一層做得好,誰大概就能保住 margin。**

### 主題六:neocloud vs hyperscaler,各自的優勢在哪?(約 01:48–01:50)

- **Chuan Li**(自陳從 neocloud 角度回答):**市場夠大,容得下多個玩家**,所以他樂於同時當 NVIDIA、Google 與 AWS 的友善同儕。neocloud 不需要什麼都從零自己發明,**打法是「聚焦」**:訓練與推論工作負載本來就塞不進通用運算雲,所以這個領域出現了大量創新——GPU、晶片間的高速互連、專用儲存與 orchestration(如 Kubernetes)。**neocloud 後來加上去的,是把這些選項變成預設值並開放給大眾**,這就是他們建出訓練/推論雲的方式。**現在要對 agent cloud 做同樣的事。**
- **Peter DeSantis**:回到「durable」這個詞——「**我不覺得 neocloud 這個標籤本身特別 durable。**」算力的機會與需求都很巨大;hyperscaler 交付了很多,新進的 neocloud 也切進來做了不少很有意思、很令人印象深刻的事。他不認為會有 80 家 neocloud,但**會看到一些新業者隨時間長得越來越像 hyperscaler**。而站在既有業者的位置,你要確保自己**沒有被「只用一種方式做事」綁死**到吃虧——如果你有成熟的雲業務,就要持續傾聽客戶需要什麼並回應。這就是大與小、既有與新進之間永恆的張力,兩邊各有利弊。

### 主題七:MCP 之外,agent 通訊協定還缺什麼?(約 01:50–01:54)

- **Jonathan Cohen**:需要被解決的是 **agent 階層**的通訊——一個 agent 生 sub-agent、sub-agent 再生 sub-agent,或者一個 agent 生出一整個協作團隊。這裡正在浮現一些通訊模式的最佳實務,而它們**隱含了「對某個共享記憶體的 scope」**:例如我有一個 agent 團隊、他們共享一個工作區,但另一個 agent 沒有存取權。所以需要**新標準來描述這種 scoped shared storage、存取控制與 agent 間的訊息傳遞**。這和過去建的東西不同——過去建的要嘛是 service、要嘛是人類尺度的東西;現在**一個 agent 可以臨時 spawn 十萬個 sub-agent**,而它們全都需要以某種複雜模式通訊。這些標準要被發明、被強制執行、被高效實作。
- **Saurabh Tiwary**:同方向補充——**MCP 給你的是「agent 對資料源」的介面**;還需要的是**多個 agent 彼此對話**,也就是 shared memory 與通訊那條線,例如 **agent-to-agent(A2A)協定**——已經存在,但**還需要更多採用**。另外在商務側,需要 agent 開始支援**支付/商務**,那會打開一個巨大的新機會;Google 有 **ACP(agent commerce protocol)**。這些都需要被生態系更充分吸收。
- **Peter DeSantis**:標準有不同的想法方式。有 **de facto 標準**——某些做法變得非常有效率,產業自然會往那裡走。但他**希望我們在不需要的地方抵抗標準化**:有些地方必須標準化(資安、低階 wire protocol、一堆東西要互通),但 **AI 相當有彈性**,agent 會自己找出有效率的協作方式,我們之後再去找工具與系統讓它更有效率。「希望我們暫時盡可能抵抗低階標準——**我們要的是創新**。」

### 主題八:Lightning round —— 最希望有人在做什麼?會勸他們再想想的又是什麼?(約 01:54–01:57)

- **Chuan Li**:授人以魚 vs 授人以漁。**模型權重、你手上現有的解法,那些是「魚」**——別抱著不放,價值會折舊。**真正有長期複利價值的,是你抵達那裡的方法**:工具、環境、system of record。
- **Jonathan Cohen**:他坦言想不出還有什麼是「該有人做但沒人做」的——**每個他想得到的東西都已經有公司在做了**,垂直的、水平的都各有七家。而這很好:agentic AI 顯然是 AI 的新前沿,從 security 到 storage 到垂直整合領域,都還有巨大的改進與創新空間。
  - **Todd 的補充**:如果你在做某件事,**假設你不是唯一有這個點子的人**——你要非常清楚自己在跟誰競爭、這片海是什麼顏色、進去之後怎麼差異化。
- **Peter DeSantis**:呼應自己 keynote 的主題——在這個狂熱的年代,有個風險是**看到進展就以為問題解決了**;而這枚硬幣的另一面同樣危險:看著模型演化的方式、看著大實驗室的動作,你可能覺得「那裡完全沒有空間了」。**要抗拒這種想法**,因為今天看起來已解的問題,明天又會重新變成未解。「我知道這對你身為 VC 很重要,但我身為技術人深信這一點:**This is very early days.**」
- **Saurabh Tiwary**:給做終端產品/完整 agentic 解法的人一個提醒。既有的業務流程往往是**多年演化出來的多段管線**,而人們常做的是**把 AI「灑」進管線的每一段**——結果 AI 能帶來的好處被**每一段的既有限制卡住**,大幅稀釋。他舉的例子:停車場的車牌辨識——你可以「拍照、去背、然後一堆步驟」,每一步都灑一點 AI。**應該反過來**:看清楚 AI 的核心能力是什麼、而且**永遠站在最新能力上**(能力一直在長,不要用靜態的假設),然後**從頭重新檢視整個業務流程**,問「如果以 AI-native 的方式重建它,它會長什麼樣?」——建那個東西,才會交付顯著的價值。

### 金句

> "The thing that break first are like road capacity, traffic light and speed limit. The opportunity there is how to turn those choke point into a checkpoint." — Chuan Li(約 01:36)

把 machine-speed 的車放上為人設計的道路,先壞的是基礎設施而不是車。

> "Agentic AI workloads are significantly more complicated, heterogeneous, and expensive computationally than anything we've ever seen before." — Jonathan Cohen(約 01:41)

整場 panel 的共識句。

> "An agent can in an ad hoc way spawn 100,000 sub-agents, all of which need to communicate in some complicated pattern." — Jonathan Cohen(約 01:52)

為什麼舊的 service 標準與人類尺度標準都不夠用。

> "I'm not sure the label neocloud is a particularly durable label." — Peter DeSantis(約 01:49)

他不否認新進者的成績,但認為分類本身會消融。

> "Hopefully we resist low-level standards where possible for a while. I think we want the innovation." — Peter DeSantis(約 01:54)

panel 上最明確的一處分歧:該現在標準化,還是先讓它長。

> "This is very early days." — Peter DeSantis(約 01:57)

回到他 keynote 的 day one。

## English Notes

### Framing: from chat to machine speed (~01:35)

Todd Graham set the scene: the ChatGPT moment made chat the primary interface — one request, one response, relatively short context, short bursts. Agents run at machine speed, sometimes for hours ("you've got 12 of them running code overnight for you"), with massive tool volume and token prefill. He asked who had set an agent running overnight and woken up to an auto-refilled token balance. Nearly every hand went up.

### Topic 1: the single biggest failure point in agent infrastructure today (~01:36–01:39)

- **Chuan Li**: the answer is in the question. Put machine-speed traffic on a road designed for human drivers and **what breaks first is road capacity, traffic lights, and speed limits**. The opportunity is turning those choke points into checkpoints.
- **Jonathan Cohen**: the crux is the LLM component — surprisingly reliable, but also capable of surprising and unpredictable behavior. The opportunity is surrounding it with **rule-based policy enforcement, more deterministic systems and memory systems** that give you confidence and certainty about what it's actually doing.
- **Saurabh Tiwary**: the answer keeps changing and evolving. At the **compute layer**, remove as many bubbles as possible for maximum efficiency. At the **infrastructure layer**, requests arrive from all over the world, so routing has to smooth out spikes to keep compute efficient at low latency. **Voice** is becoming an interesting engagement medium with a very different profile from raw text, so managing heterogeneity of both use cases and compute environments is a problem. **Sovereignty** requirements are becoming much more important and in a way break the shared-cloud philosophy, adding significant engineering complexity. Layer identity and security on top, and these are becoming very big problems very quickly.
- **Peter DeSantis**: "My answer is all of it as well." It's a systems problem from the very top of the stack down through guardrails, infrastructure, power, and the chips running it — **and you have to get it all right**, because agents have enormous potential but without efficiency we only capture a fraction of it.

**Follow-up: which is the biggest rock to move — where do you point someone who wants to build today?**
DeSantis: "I'm an optimist, so I don't worry. I look for opportunity, and I see opportunity at every level. You've heard about 16 problems and a hundred constraints — **pick one, go deep, and have fun.**" (Graham, deadpan: "Maybe build a memory manufacturing plant tomorrow afternoon.")

### Topic 2: how should hardware specialize for agent workloads vs. LLM workloads? (~01:39–01:42)

**Jonathan Cohen** carried this one:

- **More context**, and the ratio of what's cacheable versus not changes.
- **Heterogeneity**: an agent is an LLM surrounded by computer stuff, and a lot of that runs on CPUs, possibly multi-core. Plenty also runs on GPUs — but GPUs configured for different kinds of workloads, not neural network inference; a physics simulation, say.
- So a data center running agentic workloads is **very heterogeneous and complicated**, with many processing elements, many storage layers, and complicated network topologies.
- Layered on top: security, privacy, and sovereignty requirements.
- Frankly, **the world still doesn't quite know the best way to do this**, because agentic AI is still evolving. This has happened repeatedly in AI's history — we think we understand it, then a new thing shows up and the workloads look totally different and get more complicated.
- His conclusion: "**Agentic AI workloads are significantly more complicated, heterogeneous, and expensive computationally than anything we've ever seen before.**"

### Topic 3: fine-tuning or context engineering for workflow-specific enterprise agents? (~01:41–01:43)

**Saurabh Tiwary** laid out a ladder from simple to expensive:

1. **Start with context engineering** — the simplest option. Base LLMs already have enough reasoning power (Gemini and others), and with a long context window you can put in a lot of data for the model to reason over. The quality of reasoning over context has improved.
2. **To actually perturb the model, start with LoRA fine-tuning** — cheap, easy, and efficient and cost-effective on the inference side too.
3. **Above that, full fine-tuning or post-training** — here you perturb all of the model's weights, which changes the inference dynamics because you effectively have a brand-new copy of the model, making it much more expensive.
4. Very custom work happens only with a few very special partners.

The first two, in his view, are the primary paths.

### Topic 4: does experiment tracking live inside the infrastructure or in a separate observability layer? (~01:43–01:45)

**Chuan Li**: it's **definitely infrastructure**, but different from the environment people train in.

- The **environment** is where the agent acts and learns; the **experiment tracker** is more like memory and measurement sitting beside it.
- His framing: the environment trains your **first brain** — learning goes into model weights, compressed, internalized, and **capacity-bounded**. The experiment tracker gives you a **second brain** — learning goes into artifacts, and it's **unbounded**.
- There's a path from the second brain back to the first: turn your system of record into a dataset, then fine-tune or run RL on it.
- Where to host it depends on your data containment policy — self-host if requirements are strict, use a managed service if not. But **if you want to use it for training or fine-tuning, it should be close to your training**.

### Topic 5: where is margin durable in the agentic stack? (~01:45–01:48)

Graham's question: sitting between the model and the agent's outcome you have orchestration, sandboxing, runtime, memory, identity, eval — if you're greenfield today, do you go after memory or sandboxes? Where does the money actually get made?

- **Peter DeSantis** (interjecting): "**At the hardware.**"
- **Saurabh Tiwary**: AI got adopted because of the **quality of results** and the quality of the developer/builder experience. The business opportunity is obviously massive, and — echoing DeSantis — **there are tons of problems; pick one and solve it very deeply**. If you deliver on your promise to the customer at high enough quality, the value gets extracted there. Take memory: it isn't about "working on memory," it's about whether you give customers a compelling experience that lets them actually deliver what memory is supposed to enable, rather than "I'm using memory and here are some prompts that got updated." That value exists across the stack — hardware, model, agentic, and application layers. And with almost every CXO at every major company thinking about AI, the opportunity is huge; it comes down to delivering value.
- **Chuan Li**: agrees on hardware, and adds **vertical integration**. Coming from a neocloud, he notes people usually assume cloud computing is a commodity — largely true, but **cloud computing is very hard**: land, power, data center buildout, HPC architecture, orchestration, software, and finance form one vertical stack. The agent layer — **call it sandbox, call it harness, call it system of record** — is a new layer to be integrated into that vertical. **Whoever does a good job there is probably going to keep the margin.**

### Topic 6: neoclouds vs. hyperscalers (~01:48–01:50)

- **Chuan Li**, answering from the neocloud side: the market is big enough for multiple players, so he's happy to be a friendly peer to NVIDIA, Google, and AWS alike. A neocloud doesn't need to invent everything from scratch — **its play is focus**. Training and inference workloads never fit a general-purpose compute cloud, which is why so much innovation happened there: GPUs, fast chip-to-chip interconnect, specialized storage and orchestration like Kubernetes. **What neoclouds added was making those options the default and offering them to the general public.** That's how the training and inference cloud got built, and it's the same thing they now intend to do for the agent cloud.
- **Peter DeSantis**, returning to the word "durable": "**I'm not sure the label neocloud is a particularly durable label.**" Demand for compute is huge; hyperscalers have delivered a lot of it, and there's real space for insurgent neoclouds — they've done impressive, interesting things. He doesn't think there will be 80 neoclouds, but he does expect **some new businesses that look a lot more like hyperscalers over time**. As an incumbent, the thing to guard against is being stuck doing things one way in a manner that disadvantages you — if you have an established cloud business, listen to your customers and respond. That's the perennial tension of big and small, incumbent and insurgent, with pros and cons on both sides.

### Topic 7: what's missing from agent communication protocols beyond MCP? (~01:50–01:54)

- **Jonathan Cohen**: what needs working out is the **hierarchy of agents** — an agent spawning sub-agents spawning sub-agents, or spawning a team that works together. Emerging best practices around communication patterns **imply a scope on some kind of shared memory**: a team of agents might share a workspace that another agent has no access to. So there are **new standards to be developed describing scoped shared storage systems, access, and message passing between agents**. This differs from what we've built before, which was either services or human-scale: now **an agent can, ad hoc, spawn 100,000 sub-agents**, all needing to communicate in some complicated pattern. Those standards have to be invented, enforced, and implemented efficiently.
- **Saurabh Tiwary**, along the same lines: **MCP gives you an interface for an agent to talk to a data source.** What's also needed is multiple agents talking among themselves — shared memory plus communication — which is the direction of the **agent-to-agent (A2A) protocol**, which exists but **needs more adoption**. On the commerce side, agents need to start supporting **payments and commerce**, which opens a huge new opportunity; Google has **ACP (agent commerce protocol)**. These need to be more fully absorbed into the ecosystem.
- **Peter DeSantis**: there are different ways to think about standards. **De facto standards** emerge where things become efficient, and the industry will trend there. But he'd **hope we resist standardizing where we don't need to** in the short term. Some places genuinely need it — security, low-level wire protocols where many things must talk together — but **AI is pretty elastic**, and agents will find efficient ways to collaborate; we'll then have to find the tools and systems that make them more efficient. "Hopefully we resist low-level standards where possible for a while. **I think we want the innovation.**"

### Topic 8: lightning round — what do you hope someone's building, and what would you steer them away from? (~01:54–01:57)

- **Chuan Li**: give someone a fish and you feed them for a day; teach them to fish and you feed them for life. **Model weights and the solution currently in your hand are the fish** — don't hold on to them, the value depreciates. What compounds over the long term is **how you get there**: the tools, the environment, the system of record.
- **Jonathan Cohen**: honestly, he can't name a thing someone should do that nobody is doing — **every single thing he can think of, there's a company doing today**, seven of them vertically and horizontally. And that's great: agentic AI is clearly the new frontier of AI, with tremendous room to improve and innovate from security to storage to vertically integrated domains.
  - **Graham's editorial addition**: if you're building something, **assume you're not the only person with the idea** — you need to really understand who you're competing with, what color the ocean is, and how you'll differentiate when you go in.
- **Peter DeSantis**, echoing his keynote: in these frenetic times there's a risk of looking at the progress being made and thinking a problem is solved. **The other side of that coin is just as dangerous** — watching how the models are evolving and what the large labs are doing, you might conclude there's no space there at all. **Resist that**, because what looks like a solved problem today will be unsolved again. "I know that's important to you as a VC, but I deeply believe this as a technologist: **this is very early days.**"
- **Saurabh Tiwary**, for people building end products or full agentic solutions: an existing business process has often evolved over many years into a multi-stage pipeline, and the common move is to **sprinkle AI into each piece of that pipeline** — at which point the benefit you extract from AI is heavily diminished, because you're thresholded by the limitations of every stage. His trivial example: license plate identification for parking — take image, remove background, and so on down the pipeline, sprinkling AI on each step. **Instead**: look at what AI's core capabilities are, **always stay on the cutting edge** (capabilities keep changing — don't be static), **revisit the entire business process from the ground up**, ask what it would look like if you built it AI-native, and build that. That's what delivers significant value.

### Quotes

> "The thing that break first are like road capacity, traffic light and speed limit. The opportunity there is how to turn those choke point into a checkpoint." — Chuan Li (~01:36)

Put machine-speed traffic on a road built for humans and the road fails before the cars do.

> "Agentic AI workloads are significantly more complicated, heterogeneous, and expensive computationally than anything we've ever seen before." — Jonathan Cohen (~01:41)

The panel's consensus sentence.

> "An agent can in an ad hoc way spawn 100,000 sub-agents, all of which need to communicate in some complicated pattern." — Jonathan Cohen (~01:52)

Why service-shaped and human-scale standards both run out.

> "I'm not sure the label neocloud is a particularly durable label." — Peter DeSantis (~01:49)

He credits the newcomers' work while predicting the category itself dissolves.

> "Hopefully we resist low-level standards where possible for a while. I think we want the innovation." — Peter DeSantis (~01:54)

The clearest disagreement on stage: standardize now, or let it grow first.

> "This is very early days." — Peter DeSantis (~01:57)

Back to the day-one framing of his keynote.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| MCP (Model Context Protocol) | 現行主流協定,提供 agent 對資料源的介面 | The prevailing protocol today; an interface for an agent to talk to a data source | Tiwary 認為它只解決了一半問題 / Tiwary sees it as solving only half the problem |
| A2A(agent-to-agent protocol) | agent 之間互相溝通的協定,已存在但採用不足 | Protocol for agents talking among themselves; exists but under-adopted | |
| ACP(agent commerce protocol) | Google 的 agent 商務/支付協定 | Google's protocol for agent commerce and payments | 正式全名待確認 / exact full name to verify |
| Gemini Enterprise agent platform | 提供 LoRA 訓練等模型客製能力 | Offers model customization capabilities such as LoRA training | Tiwary 提及 / mentioned by Tiwary |
| LoRA fine-tuning | 客製化階梯的第二階,便宜且推論高效 | Second rung of the customization ladder: cheap and inference-efficient | |
| Kubernetes | Chuan Li 舉為 neocloud 領域 orchestration 創新的例子 | Cited by Chuan Li as an orchestration innovation from this space | |
| the_lab.api | Chuan Li 所指的 experiment tracker / system of record | The experiment tracker / system of record Chuan Li refers to | 詳見其 featured talk 筆記 / see his featured talk note |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Peter Dantis | Peter DeSantis |
| Sarb / Sar | Saurabh Tiwary |
| John Cohen | Jonathan Cohen |
| Sean | Chuan Li |
| Invidia / media | NVIDIA |
| neo cloud / neoclouds | neocloud / neoclouds |
| Aentic AI | agentic AI |
| LoRa training | LoRA training |
| agent commerce plat uh protocol | agent commerce protocol (ACP) |
| KAS | Kubernetes(K8s) |
| a li opportunity | a likely opportunity(推測 / inferred) |

## 待確認 / To Verify

- Google「ACP / agent commerce protocol」的正式名稱與規格連結。/ Official name and spec link for Google's "ACP / agent commerce protocol".
- A2A 協定的現行治理單位與版本(演講只說「存在但需要更多採用」)。/ Current governance and version of the A2A protocol (the panel only said it exists and needs more adoption).
- Tiwary 提到的 LoRA 訓練是在哪一個 Google 產品面上提供(字幕作 "Gemini enterprise agent platform")。/ Which Google product surface offers the LoRA training Tiwary described (captions say "Gemini enterprise agent platform").
- Chuan Li 回答 observability 時提到的「all policy area」原文(可能是 on-policy / off-policy RL)。/ The actual phrase behind "all policy area" in Chuan Li's observability answer (possibly on-policy / off-policy RL).
