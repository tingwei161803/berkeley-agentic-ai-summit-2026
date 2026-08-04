---
title: "Constraint-Driven Innovation: A Look at the AI Systems Problem"
title_zh: "約束驅動的創新:AI 系統問題巡禮"
speaker: "Peter DeSantis"
affiliation: "SVP, Foundational AI Models, Custom Silicon, Quantum Computing, Amazon"
type: keynote
stage: Plenary
date: 2026-08-01
session: "Session 1: Agentic AI Infrastructure & Platform"
video: "https://www.youtube.com/watch?v=gKdeLQd_LIQ&t=2543s"
video_range: "00:42:23–01:01:30"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 1st - Morning Session [DownSub.com].srt"
status: draft
tags: [infrastructure, custom-silicon, trainium, inference, systems]
---

# 約束驅動的創新:AI 系統問題巡禮(Constraint-Driven Innovation: A Look at the AI Systems Problem)

**一句話總結**:要讓 AI 兌現承諾,關鍵不是再多一個模型或再快一顆晶片,而是把效率提升一個數量級——而效率只能從「模型與晶片協同設計、且不在中間放抽象層」的全棧系統觀取得;世界處處是約束,那正是這件事有趣的原因。
**One-line summary**: Delivering on AI's promise takes an order-of-magnitude efficiency gain, not one more model or one faster chip — and that gain only comes from treating AI infrastructure as a whole-stack systems problem where models and silicon are co-designed and no layer of indirection sits between you and the hardware.

## 中文筆記

### TL;DR

- **這是 day one**:Amazon 的 day one 文化不是狀態描述而是態度——「不管你過去做出什麼成就,前面還有更多」。DeSantis 認為 AI 現在正處在 day one,不是快做完了。
- **最核心的問題是效率**:要達成大家共同想像的 AI 未來,現有基礎設施得**提升一個數量級**,不是漸進改善。
- **觀察一:不會只有一種晶片**。GPU 是個美麗的意外(它為 graphics 而生),但不是跑今天模型的最優架構;AI 運算的記憶體與計算流是**可預測的**,所以最適合的是 systolic array——這是 Trainium(前身 Inferentia)近十年前就下的賭注。
- **推論工作負載本身就是兩種**:prefill/encoding 極度 compute-bound,autoregressive token generation 極度 memory-bandwidth-bound(每產生一個 token 都要讀過全部權重)。SRAM-heavy 晶片能讓 token generation 快很多,但用電晶體換了記憶體、又難塞下 agentic 需要的超長 context——所以是**補位而非取代**。
- **觀察二:模型與晶片必須同時設計**。模型架構是數億(未來可能數十億)美元、跨年度的投入;晶片從設計到規模化上線要兩到三年。兩條長弧不能各走各的。Amazon 約半年前把內部 foundation model 團隊與晶片開發拉到一起。
- **觀察三:這不是模型問題,也不是晶片問題,是系統問題**。無論你把 performance 定義成準確率、延遲還是吞吐/成本,任何一項的改善都需要對整個堆疊的完整理解。
- **因此刻意不做抽象**:軟體工程的本能是加一層 indirection,但要榨出極致效能就得直接碰硬體——Trainium 公開了完整指令集、開源了 toolchain,並整合 PyTorch 與 vLLM。

### 重點整理

#### 開場:day one 與 AI 樂觀論(約 00:42–00:46)

- 在 Amazon 28 年,day one 是一種「相信並意志出來」的文化:不管過去有多成功,前面還有更多成功。零售起家時說 day one 合理,變成大零售商後說起來有點傻,20 年前開 AWS 時又真的像 day one(公司內部當時都在笑這個雲端玩意)。
- 他自陳是分布右尾的 AI 樂觀主義者,相信 AI 會幫人類解決能源、健康與醫學這類最根本的問題——但**要走到那個未來,必須先解決一批問題,而且是數量級的改善**。
- 最根本的那個問題:**怎麼讓 AI 效率高得多**。這也是為什麼他說我們還在 day one。

#### 觀察一:未來十年不會只有一種晶片或伺服器型別(約 00:47–00:54)

- 回望十年前,幾乎所有工作負載都跑在 CPU 上——Moore's law 持續產出更好的通用處理器,單一 tool chain 帶來槓桿;而在雲之前,支援多種硬體對聚焦本業的公司來說不划算。
- 雲改變了這件事(Amazon 約 12 年前開始興奮於此),把客製硬體的麻煩吸收掉,所以**早在 AI 起飛前 AWS 就在做各種 bespoke 硬體**。AI 來了之後,「AI」底下其實是一整個工作負載生態系,agentic AI 又把這件事推得更快。
- GPU 的地位很特別:它是個 phenomenal chip,徹底改變了浮點與矩陣運算的遊戲規則,是今日模型的起源故事的關鍵一環——但它「是為它名字裡那個東西(graphics)設計的」,**不是**跑今天模型最優的架構。
- Amazon 近十年前就注意到:AI 模型雖然做大量矩陣與浮點運算,但**做的方式相當可預測**;既然記憶體與計算的流動可以預測,就不需要一堆核心配一堆暫存器去隨機存取記憶體。最適合這種形態的是 **systolic array**。
- Trainium(原名 Inferentia,後來長成更大的變體)就是建立在 systolic array 上:拿掉這類工作負載不需要的彈性換效率,同時保留足夠彈性去跑各種 ML 模型。「It's not an ASIC customized for one application. It's an AI accelerator.」
- 但即使 Trainium 是今天最優的架構,一顆晶片也不可能是未來的答案。Amazon 認為訓練還有一到兩個十年的新創新可做,同時 Amazon 與其他人都會投資別的晶片——這讓硬體生態系更有意思。
- **推論管線的兩種工作負載**:
  - **prefill / encoding**:極度 compute-intensive。
  - **autoregressive token generation**:極度 memory-bandwidth-bound,因為每產生一個後續 token 都要存取每一個模型權重。
  - 兩者的硬體 profile 天差地遠。Trainium 兩邊都跑得不錯:高效記憶體流利於 decode、大浮點效能利於 prefill。
- 目前最受矚目的特化方向是用 **SRAM 晶片**(把更多記憶體放上計算晶片,代價是計算容量)加速 token generation。但這是 trade-off:需要更多計算時你已經把電晶體換成記憶體了;需要更多記憶體時本來就塞不進晶片;而 agentic AI 需要**非常非常長的 context**,把 context 搬進搬出 SRAM 遠比在 Trainium 上昂貴。結論:SRAM 與記憶體密集晶片會是推論系統的重要一環,**但是在許多其他晶片的脈絡裡,不是取代品**。

#### 觀察二:模型與晶片必須協同設計(約 00:54–00:57)

- 建一個 AI 模型等於對某個模型架構做**多年、數億美元**的投入;他預期不久後會有模型家族投入數十億美元。這種長期投入的每一步都得有效率。
- 晶片投入是同樣的形狀:以今日領先 AI 處理器的複雜度,從設計到在資料中心規模化上線很容易就是兩到三年。
- 兩條同樣長弧的投資如果各走各的——模型不管一年後硬體會長怎樣、硬體不管兩年後模型要什麼——就是錯的。
- 一個具體切面:**你要把哪些能力放進晶片?**新點子的來源之一是學術界(他說投影片上有一批很重要的 Berkeley 論文)。但不是每個好點子都該進矽晶,不是因為它不好,而是設計選擇的名額有限。**做好硬體的藝術,就是判斷哪些好點子必須進硬體,好讓晶片上市時科學與技術剛好成熟到能用它。**
- Trainium 最新世代加進去的特性正是這樣挑出來的——靈感來自學術界,也來自客戶與內部團隊的研究。
- 約六個月前,Amazon 把內部的 foundational model 團隊與晶片開發拉得更近,這現在是 DeSantis 職掌的重要一塊。

#### 觀察三:AI 基礎設施是系統問題(約 00:57–01:00)

- 「AI infrastructure is not a model problem. It's not a chip problem. It's a systems problem.」——正因為系統彼此高度連動,這是工程師/科學家能碰到最有意思的問題之一,幾乎把電腦科學與工程的每個部分都拉了進來。
- performance 可以定義成更好的準確率、更低的延遲、更好的吞吐與成本;但**任何一種「更好」都需要對每一層堆疊的完整理解**。
- 由此得出一個反直覺的工程決定:身為軟體工程師,他的本能是加一層 indirection 來擴展——對大組織裡的軟體通常是對的,**但要在 AI 系統上追求絕對最佳效能就不是**。你得親手碰整個堆疊:網路、晶片、晶片與網路的硬體指令層能力。
- 所以 Amazon 給客戶最深的硬體存取權:Trainium **公開完整指令集**(很多 Berkeley 學生協助推進了這方面的極限)、**開源 toolchain**(讓外界理解編譯器與軟體堆疊如何運作),並整合 PyTorch 與 vLLM 這類生態關鍵元件。

#### 結尾:約束就是題目(約 01:00–01:01)

世界充滿約束——容量、效能、電力。這正是整件事有意思的原因,也是他此刻對技術與 AI 感到興奮的理由。像這樣把整個堆疊各方的專家聚在一起的場合,是解鎖「理解整個系統」帶來的潛力的關鍵。收尾回到開頭:這趟旅程才剛剛開始,前面的路會比至今看到的更精彩。

### 金句

> "It's always day one."(約 00:44)

不是描述公司規模,是一種刻意維持的態度:不管做出什麼成就,前面還有更多。

> "It's not an ASIC customized for one application. It's an AI accelerator that's been built specifically to optimally run the biggest and broadest range of AI models."(約 00:51)

Trainium 的定位:用 systolic array 拿掉不需要的彈性,但刻意保留跑各種 ML 模型的彈性。

> "The art of building great hardware is understanding which of the great ideas ultimately need to be put into hardware — so that by the time the hardware is in market, the science and the technology is ready to take advantage of that chip."(約 00:57)

兩到三年的晶片 lead time,逼你在論文階段就下注。

> "AI infrastructure is not a model problem. It's not a chip problem. It's a systems problem."(約 00:57)

整場演講的軸心,也是接下來 panel 的共同前提。

> "I have an instinctual desire to put a layer of indirection between things to scale — and that is usually the right way to build software … but it's not the right way to build an AI system if you want to achieve absolute best performance."(約 00:59)

刻意違反軟體工程本能,是 Trainium 公開完整指令集的理由。

> "The world is full of constraints — capacity constraints, performance constraints, power constraints. That's what makes this whole thing so interesting."(約 01:00)

演講標題的出處。

## English Notes

### TL;DR

- **It's day one.** Amazon's day-one culture is an attitude, not a stage: however much you've already succeeded, more is ahead. DeSantis sees AI as squarely in day one, not on the cusp of being finished.
- **The core problem is efficiency.** Realizing the AI future everyone wants requires an **order-of-magnitude** improvement in infrastructure, not incremental gains.
- **Observation 1: no single chip wins the next decade.** The GPU was a happy accident — built for the thing it's named after, graphics — and is not the optimal architecture for today's models. AI models do predictable matrix and floating-point work, so memory and compute flow can be predicted, which is what makes a **systolic array** the right shape. That's the bet behind Trainium (originally Inferentia), placed the better part of a decade ago.
- **Inference is really two workloads**: prefill/encoding is extremely compute-intensive; autoregressive token generation is extremely memory-bandwidth-bound, since every subsequent token touches every model weight. SRAM-heavy chips speed up token generation but trade transistors for memory and struggle with the very long contexts agentic AI needs — so they complement rather than replace.
- **Observation 2: models and chips must be designed in tandem.** A model architecture is a multi-year, hundreds-of-millions-of-dollars commitment (soon billions); a leading AI chip takes two to three years from design to data-center scale. Two long-arc investments cannot be made in isolation from each other. Amazon brought its internal foundation model work closer to chip development about six months ago.
- **Observation 3: this is a systems problem**, not a model or chip problem. Whether you define performance as accuracy, latency, or throughput-and-cost, improving any of them requires understanding every layer of the stack.
- **So Amazon deliberately removes abstractions**: Trainium's full instruction set is exposed, the toolchain is open-sourced, and the stack integrates with PyTorch and vLLM.

### Key Points

#### Opening: day one and AI optimism (~00:42–00:46)

Twenty-eight years at Amazon have made "day one" a familiar phrase — a culture you believe and will into existence, meaning that whatever you've built, more success lies ahead. It made obvious sense in a retail startup that fit in one conference room, felt silly once Amazon was a huge retailer, and felt true again when AWS launched twenty years ago and everyone inside the company was laughing at "this cloud thing."

DeSantis places himself on the far tail of the optimist distribution: he believes AI will help solve fundamental problems like energy, health, and medicine, and that we are seeing only the tip of the iceberg. But getting there requires order-of-magnitude improvements, and the single most fundamental problem is **making AI far more efficient**.

#### Observation 1: no single chip or server type will power the next decade (~00:47–00:54)

- A decade ago essentially everything ran on a CPU. Moore's law kept producing better general-purpose processors, one tool chain gave leverage, and supporting many hardware types made little sense for a company focused on its business.
- The cloud absorbed the pain of custom hardware, which is why AWS was already building bespoke silicon well before AI took off. Then AI arrived — and "AI" is really an ecosystem of workload types, with agentic AI pushing diversity faster still.
- The GPU is a phenomenal chip and a critical part of the origin story of modern models, but it was built for graphics and is not the optimal architecture for the models we run today.
- The insight, noticed the better part of a decade ago: AI models do a lot of matrix and floating-point math, but they do it in a **fairly predictable way**. If you can predict the flow of memory and compute through a chip, you don't need many cores with many registers doing random memory access — you want a **systolic array**.
- Trainium (originally Inferentia, later grown into a larger variant) is built on that architecture: strip out the flexibility these workloads don't need, keep the flexibility that lets it run a broad range of ML models. "It's not an ASIC customized for one application. It's an AI accelerator."
- Even so, one chip won't be the answer. Amazon sees another decade or two of novel innovation in training, and expects both itself and others to invest in additional chips — which makes the hardware ecosystem more interesting.
- **Two workloads inside inference**: prefill/encoding is compute-intensive; autoregressive decode is memory-bandwidth-bound because each token requires reading every weight. Their hardware profiles are radically different. Trainium runs both well — efficient memory flow serves decode, large floating-point throughput serves prefill.
- The specialization getting the most attention now is **SRAM-heavy chips** that trade compute capacity for on-chip memory to accelerate token generation. But the trade-offs bite: you've spent transistors on memory, you can't fit much memory on-chip anyway, and agentic AI needs very long contexts that are expensive to move in and out of SRAM. DeSantis expects such chips to be an important part of inference systems **in the context of many other chips, not as a replacement**.

#### Observation 2: models and chips must be designed in tandem (~00:54–00:57)

- Building an AI model is a multi-year commitment to an architecture costing hundreds of millions of dollars — soon, he suspects, billions for some model families. Every step of that investment needs to be efficient.
- Chip investment has the same shape: two to three years from design to production scale, given the complexity of leading AI processors.
- Developing models without knowing what happens in hardware a year out — or building hardware two years out without understanding model needs — is a mistake. Bringing the model, the system around it, and the silicon together is fundamental.
- A concrete lens: **which capabilities do you put on the chip?** Academia is one source of ideas (he noted a set of important Berkeley papers on the slide). Not every good idea makes it into production — not because it wasn't good, but because you only get so many design choices. "The art of building great hardware is understanding which of the great ideas ultimately need to be put into hardware."
- The features in the latest Trainium generation were selected this way, inspired by academic work as well as customer and internal research. About six months ago Amazon pulled its internal foundational model work closer to chip development, now a major part of DeSantis's remit.

#### Observation 3: AI infrastructure is a systems problem (~00:57–01:00)

- Because these systems are so interconnected, improving performance — however you define it (accuracy, latency, throughput and cost) — demands a complete understanding of every level of the stack. Done well, it draws on nearly every part of computer science and engineering, which is what makes it such a fun place to build.
- This produces a deliberately counterintuitive engineering stance. As a software engineer, his instinct is to insert a layer of indirection to scale — usually right for software, especially in a large organization, **but wrong for an AI system chasing absolute best performance**. There you need hands on the whole stack: the network, the chip, the hardware instruction-level capabilities of both.
- Hence Amazon exposes Trainium's **complete instruction set** (Berkeley students have helped push the limits there), **open-sources the toolchain** so people can see how the compiler and the rest of the software stack work, and integrates with PyTorch and vLLM.

#### Closing: constraints are the point (~01:00–01:01)

The world is full of constraints — capacity, performance, power — and that is exactly what makes this interesting. Events that gather experts from every part of the stack are critical to unlocking what comes from understanding the whole system. He closed where he started: this is the very beginning, and what lies ahead will be far more exciting than what we've seen.

### Quotes

> "It's always day one." (~00:44)

Not a description of company size — a deliberately maintained attitude.

> "It's not an ASIC customized for one application. It's an AI accelerator that's been built specifically to optimally run the biggest and broadest range of AI models." (~00:51)

Trainium's positioning: strip the flexibility you don't need, keep the flexibility you do.

> "The art of building great hardware is understanding which of the great ideas ultimately need to be put into hardware — so that by the time the hardware is in market, the science and the technology is ready to take advantage of that chip." (~00:57)

A two-to-three-year lead time forces you to bet at the paper stage.

> "AI infrastructure is not a model problem. It's not a chip problem. It's a systems problem." (~00:57)

The spine of the talk, and the shared premise of the panel that followed.

> "I have an instinctual desire to put a layer of indirection between things to scale — and that is usually the right way to build software … but it's not the right way to build an AI system if you want to achieve absolute best performance." (~00:59)

Why Trainium's full instruction set is public.

> "The world is full of constraints — capacity constraints, performance constraints, power constraints. That's what makes this whole thing so interesting." (~01:00)

Where the talk's title comes from.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| AWS Trainium | Amazon 自研 AI 加速器,systolic array 架構;完整指令集公開 | Amazon's in-house AI accelerator built on a systolic array; full instruction set exposed | 原名 Inferentia,後長成更大變體 / originally Inferentia, later grown into a larger variant |
| AWS Inferentia | Trainium 的前身 | Trainium's predecessor | |
| Systolic array | 適合可預測記憶體/計算流的架構,Trainium 的基礎 | Architecture suited to predictable memory/compute flow; the basis of Trainium | |
| SRAM-heavy 推論晶片 | 把更多記憶體放上計算晶片以加速 token generation | Chips trading compute for on-chip memory to accelerate token generation | 未點名廠商;DeSantis 視為補位而非取代 / no vendor named; framed as complement, not replacement |
| PyTorch | Amazon 晶片軟體堆疊整合的生態關鍵元件 | Key ecosystem component the Amazon chip stack integrates with | |
| vLLM | 同上 | Same | 逐字稿誤聽為 "L uh BLM" / heard as "L uh BLM" |
| Amazon 開源 toolchain | 編譯器與軟體堆疊開源,供外界理解 | Open-sourced compiler and software stack | 正式名稱待確認 / official name to verify |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Peter Dantis | Peter DeSantis |
| tranium / trrenium | Trainium |
| inferentia | Inferentia |
| L uh BLM | vLLM |
| a Gentic AI / aentic | agentic AI |
| SRAMM | SRAM |
| floatingoint / auto reggressive | floating-point / autoregressive |
| Don | Dawn (Song) |

## 待確認 / To Verify

- Amazon「開源 toolchain」的正式名稱與連結(推測與 AWS Neuron SDK / 其 kernel 介面相關,但演講未點名)。/ Official name and link for the open-sourced Amazon toolchain (likely related to the AWS Neuron SDK / its kernel interface, but not named in the talk).
- 「latest generation」Trainium 指的是哪一代與新增了哪些特性(投影片上有列表,語音未逐項念出)。/ Which Trainium generation "latest generation" refers to and which features were added (listed on a slide, not read aloud).
- 投影片上那批「很重要的 Berkeley 論文」是哪幾篇。/ Which Berkeley papers appeared on the slide.
- 「約六個月前把內部 foundational model 團隊與晶片開發拉近」是否有對應的公開組織異動公告。/ Whether the reorg bringing Amazon's foundational model team closer to chip development was publicly announced.
