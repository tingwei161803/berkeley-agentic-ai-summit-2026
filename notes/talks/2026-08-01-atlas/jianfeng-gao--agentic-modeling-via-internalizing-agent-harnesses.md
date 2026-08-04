---
title: "Agentic Modeling via Internalizing Agent Harnesses"
title_zh: "把 Agent Harness 內化進模型:Agentic Modeling 的新典範"
speaker: "Jianfeng Gao"
affiliation: "Technical Fellow & Corporate Vice President, Microsoft Research"
type: keynote
stage: Atlas
date: 2026-08-01
session: "Session 1: Foundational Capabilities"
video: "https://www.youtube.com/watch?v=WeriQic-QW0&t=80s"
video_range: "00:01:20–00:17:35"
transcript: "tmp/[English (auto-generated)] Atlas Stage - August 1st - Morning Session [DownSub.com].srt"
status: draft
tags: [agentic-modeling, rl-environments, post-training, microsoft-research, open-source]
---

# 把 Agent Harness 內化進模型:Agentic Modeling 的新典範(Agentic Modeling via Internalizing Agent Harnesses)

**一句話總結**:語言模型本身只是個「說話的人」,是外掛的 agent harness 讓它變成「做事的人」;下一步是把 harness 的能力用 post-training 蒸餾回模型本身,而 harness 之於 agentic modeling,就等同於網路資料之於 pre-training。
**One-line summary**: A language model is a talker; the agent harness is what turns it into a doer — and the next step is distilling the harness's capabilities back into the model itself, because harnesses are to agentic modeling what internet data was to pre-training.

## 中文筆記

### TL;DR

- **三個關鍵詞**:agentic modeling(把 talker 變成 doer)、agent harness(模型外面那層硬寫死的程式碼與模組)、internalization(把 harness 的能力蒸餾進模型)。
- **Agentic modeling 需要三個元件**:agent harness(資訊層 / 執行層 / 回饋層)、environment(RL 環境,agent 在裡面互動並產生 trajectory)、trainer(用 trajectory 做 mid-training 與 post-training)。
- **新的資料飛輪**:harness 產生 trajectory → trajectory 訓練出更會做事的模型 → 更好的模型讓我們蓋出更好的 harness。「Harness 之於 agentic modeling,就像網路資料之於 pre-training。」
- **開源瓶頸不在 harness,在 environment**:社群的基礎建設多半在改善 harness 本身,但沒人能同時跑幾十萬個 agent 產生訓練資料。**Orchard** 就是為了補這個洞。
- **三個對應的研究成果**:環境端 **Orchard**(核心是 Kubernetes-native 的 Orchard Env)、harness 端 **EvoLib**(test-time learning,靠會演化的知識庫而非改參數)、trainer 端 **GFlowRL**(把 policy learning 定義成 distribution matching 而非 reward maximization)。
- **成本效率是 China(訓練端)的關鍵字**:不只要服務便宜,更要 sample-efficient——用少量樣本就能訓起來。

### 重點整理

#### 三個名詞的定義(約 00:02)

- **Agentic modeling**:把大型語言模型轉化成能與環境互動、完成複雜任務的自主 agent。「大型語言模型的刻板印象基本上是個 talker——它好像什麼都知道,但你叫它幫你做事就很困難。」agentic modeling 就是把 talker 變成 doer 的過程。
- **Agent harness**:因為語言模型做不了很多事,你得在模型外面包一層 harness。「某種意義上 harness 就是一堆程式碼」,能處理現在的模型處理不了的事。我們平常講的 AI agent,通常就是「一個或多個語言模型 + harness」的組合。
- **Internalization**:把 agentic 能力從 harness 蒸餾到語言模型裡。這些能力包括 memory、context management、tool use、planning,一般透過 supervised learning 或 RL 的 mid-training / post-training 達成。

#### Agentic modeling 的三個元件(約 00:04–00:08)

Gao 用一張三色圖拆解整個系統:

1. **Agent(harness,左側)**——他的 lab 不自己蓋大模型,因為太耗資源。Microsoft 有專責的 **MAI** 團隊做自家大模型(最近釋出十幾個模型),另外也跟 OpenAI 等公司有合約取得前沿模型,再加上 **Azure AI Foundry** 可以託管數百到數千個開源模型。Lab 真正的焦點是「發展做出 harness 的使能技術」。Harness 是一層層硬寫死的模組(不是模型本身):
   - **Information layer**:memory、context management,以及給模型呼叫的大量 tools 與 skills。
   - **Execution layer**:prompt builder、action parser、decomposition 模組、error recovery 機制。
   - **Feedback layer**(他強調「最重要」):收集 agent 產生的所有 trajectory,回頭用 post-training 精煉底層模型。**這是 agentic modeling 的關鍵。**
2. **Environment(RL environment / RLE)**——AI agent 與外部世界互動、執行任務並產生 trajectory 的地方。
3. **Trainer**——用產生的 trajectory 透過 post-training / mid-training 把 agentic 能力灌進模型。最重要的方法是 RL 以及各種蒸餾變體(on-policy distillation、reverse-KL 類演算法)。**成本效率是重點**:不只要 serving 便宜,更希望訓練是 sample-efficient 的。

#### 新典範:harness 就是新的訓練資料(約 00:08)

「我們正見證 AI modeling 的新典範:**harness 之於 agentic modeling,就像網路資料之於模型 pre-training**。」

當整個產業與社群每天都在蓋 AI agent 與 harness,一個新的資料飛輪就浮現了:從 harness 蒸餾 agent 能力 → 得到更會做事的模型 → 這些模型幫我們蓋出更好的 agent → 產生更精緻的 trajectory 資料、解更複雜的任務 → 循環繼續。Harness 與模型一起前進。

MSR 進行中的 agentic 研究基本上就對應到這三格:綠色(harness 的建模技術,如 memory management、test-time learning)、藍色(環境服務,平行託管大量 RL 環境)、黃色(trainer)。

#### 專案一:Orchard——開源的 agentic modeling 環境生態系(約 00:11–00:15)

- **問題**:agentic 開放研究卡在基礎建設。早期做訓練只要有網路就不缺資料;agentic modeling 不一樣,你需要一個能**同時跑幾十萬個 agent**的環境來產生 trajectory。研究社群的基礎建設多半用來改善 harness 本身,而不是能平行託管各種 agent 的環境。
- **Orchard**:開源、可規模化的 agentic modeling 生態系。核心是 **Orchard Env**——一個 Kubernetes-native 的環境服務,提供 sandbox 生命週期的可重用 primitives。
- **比喻**(現場即興的好比喻):Orchard Env 就像 agent 的作業系統 runtime,負責 orchestration 與虛擬化,管理 sandbox 裡的 container image,對 agent 曝露乾淨的介面。「就像這場會議的主辦方——作業系統相當於這棟樓,提供所有水電設施;如果把每個 workshop 看成一個 agent,主辦方把每個 workshop 安排進特定房間,那就是一個 RL 環境的 pod;最後主辦方再把所有 workshop 的結果收集回來分享。Orchard Env 就是整場會議的主辦方。」
- **三個示範 recipe**:**Orchard-SWE**(軟體工程 agent)、**Orchard-GUI**(GUI 導航)、**Orchard-Claw**(個人助理)。
- **結果**:Orchard-SWE 蒸餾約 10 萬條 trajectory,在 SWE-bench Verified 上拿到 **73%**——「以這個模型的尺寸來說,已經超越很多開源模型」。
- 他當場預告論文、程式碼與資料「下週」釋出。(實際上論文為 arXiv 2605.15040,Orchard Env 在論文中的定義是 "lightweight Kubernetes-native environment service"。)

#### 專案二:EvoLib——會演化的知識庫式 test-time learning(約 00:15–00:16)

Memory 很重要,但我們通常把 memory 當成「原始經驗的儲存」——而原始經驗不等於學習。「我收集了一堆過去的經驗,卻不知道怎麼用這些經驗解新問題。人類的學習不是這樣的:我從來不會回想起過去經驗的所有細節,我只記得**重要的部分**——我要避免的失敗、我學會一次之後希望能重複套用的新技能。」EvoLib 就是設計來模擬這種人類學習方式的:讓模型跨一連串任務累積、重用並演化知識,而不更新參數。

#### 專案三:GFlowRL——把 policy learning 當成分布匹配(約 00:16–00:17)

他希望這能成為目前主流 RL 方法(GRPO、PPO)之外的另一種選擇。**核心差異:在這個 RL 設定下,policy learning 被定義成 distribution matching,而不是 reward maximization。** 具體來說,模型會**按照 reward 的比例去抽樣解法**,而不是一味往最高 reward 收斂。結果是解出更大的多樣性,同時是更具成本效益的訓練方法。

(時間不夠,他在此收尾:「我得停在這裡了,有問題歡迎會後找我。」)

### 金句

> "The portrait of the large scale language model is mainly a talker. It seems that the model knows everything, but it's really difficult if you ask it to do something for you. So agentic modeling is the process where we want to turn this talker to a doer."(約 00:02)

整場演講的出發點:talker → doer。

> "Harness is like the training data to agentic modeling, just like the internet data to model pre-training."(約 00:08)

這是整場最重要的一句類比——它把「蓋 harness」重新定義成「生產訓練資料」。

> "Human learning is different. I never recall all the details of my previous experience. I only remember what matters."(約 00:16)

EvoLib 的動機:memory 不該只是經驗的倉庫,而該是被萃取過的技能與教訓。

## English Notes

### TL;DR

- **Three definitions up front**: *agentic modeling* (turning a talker into a doer), *agent harness* (the hardcoded module layers wrapped around the model), and *internalization* (distilling the harness's capabilities into the model itself).
- **Agentic modeling needs three pieces**: the harness (information / execution / feedback layers), the environment (an RL environment where agents act and emit trajectories), and the trainer (mid- and post-training on those trajectories).
- **A new data flywheel**: harnesses generate trajectories → trajectories train models that are better at *doing* → better models let us build better harnesses. "Harness is like the training data to agentic modeling, just like the internet data to model pre-training."
- **The open-research bottleneck is the environment, not the harness**: community infrastructure has focused on improving harnesses, but nobody can run hundreds of thousands of agents in parallel to produce training data. **Orchard** exists to close that gap.
- **One project per layer**: **Orchard** for environments (built on the Kubernetes-native Orchard Env), **EvoLib** for the harness (test-time learning via an evolving knowledge library rather than parameter updates), and **GFlowRL** for the trainer (policy learning as distribution matching rather than reward maximization).
- **Cost efficiency is the training-side keyword**: not just cheap serving, but *sample efficiency* — training a capable model without a mountain of samples.

### Key Points

#### Defining the three terms (~00:02)

- **Agentic modeling** transforms large-scale language models into autonomous agents capable of complex tasks through interaction with an environment. The stereotype of an LLM is a *talker*: it seems to know everything, but ask it to *do* something and things fall apart. Agentic modeling is the process of turning that talker into a doer.
- **Agent harness**: since the model itself can't do much, you couple it with a harness — "in some sense, a harness is a bunch of code" that handles what current models can't. What we call an AI agent is usually the combination of one or more language models plus the harness.
- **Internalization**: distilling agentic capabilities out of the harness and into the model — memory, context management, tool use, planning — typically via supervised learning or RL during mid- and post-training.

#### The three components of agentic modeling (~00:04–00:08)

1. **The agent / harness.** Gao's lab does not build frontier models — too resource-intensive. Microsoft's dedicated **MAI** team builds in-house models (a dozen or so released recently), contracts with OpenAI and others supply frontier models, and **Azure AI Foundry** hosts hundreds to thousands of open-source models. The lab's focus is the enabling technology for *harnesses*, which are layers of hardcoded modules rather than models:
   - **Information layer**: memory and context management, plus the tools and skills the model can call.
   - **Execution layer**: prompt builder, action parser, decomposition modules, error-recovery mechanisms.
   - **Feedback layer** — the one he calls most important: it collects every trajectory the agents generate so those trajectories can refine the underlying model through post-training. **This is the crux of agentic modeling.**
2. **The environment** (an RL environment, or RLE): where agents interact with the external world, perform tasks, and emit trajectories.
3. **The trainer**: uses those trajectories to imbue agentic capability through post- and mid-training. The key methods are RL and distillation variants (on-policy distillation, reverse-KL algorithms). Cost efficiency matters on both ends — cheap serving, but above all *sample-efficient* training.

#### The new paradigm: harnesses are the new training data (~00:08)

Put together, this is a new paradigm of AI modeling in which the harness plays the role internet data played for pre-training. As the industry builds new agents and harnesses every single day, a data flywheel emerges: distilling agentic capability from harnesses yields models that are more capable of doing things; those models help us build better agents; better agents generate more sophisticated trajectory data by solving harder tasks; and the loop continues as harness and model advance together.

MSR's ongoing agentic research maps onto exactly those three boxes: green (modeling technology for harness engineering — memory management, test-time learning), blue (environment services hosting many RL environments in parallel, the source of training data), and yellow (the trainer).

#### Project 1: Orchard — an open ecosystem for agentic modeling environments (~00:11–00:15)

- **The gap**: open research on agentic modeling is constrained by infrastructure. In the early days of pre-training, an internet connection was all you needed for data. Agentic modeling is different — you need an environment that can run hundreds of thousands of agents simultaneously to produce trajectory data at scale. Community infrastructure so far has mostly gone into improving harnesses, not into environments that host many different agents in parallel.
- **Orchard** is an open-source ecosystem for scalable agentic modeling. At its core is **Orchard Env**, a Kubernetes-native environment service offering reusable primitives for sandbox lifecycle management.
- **His analogy**, improvised on stage: Orchard Env is an operating-system runtime for AI agents — an orchestration and virtualization layer managing container images inside sandboxes and exposing a clean interface. "It's like the organizers of this conference. The operating system in this context is the building — it provides all the facilities. If you view each workshop as an agent, the organizers did a great job putting each workshop in a particular room; that room is the RL environment, the pod. And afterwards the organizers collect all the results and share them back. Orchard Env is the organizer of this whole conference."
- **Three demonstration recipes**: **Orchard-SWE** (software engineering), **Orchard-GUI** (navigation), and **Orchard-Claw** (personal assistant).
- **Result**: Orchard-SWE distilled roughly 100k trajectories and reached **73% on SWE-bench Verified**, beating many open-source models despite the model's small size.
- He said the paper, code, and data would be released "sometime next week" (published as arXiv 2605.15040).

#### Project 2: EvoLib — test-time learning with an evolving library (~00:15–00:16)

Memory matters, but we usually treat it as a store of *raw* experience — and raw experience isn't learning. "I collected a lot of experience previously; I have no idea how to use this experience to solve new tasks. But human learning is different. I never recall all the details of my previous experience. I only remember what matters — the failures I try to avoid, the new skills I learned once and hopefully can apply multiple times in the future." EvoLib is designed to simulate that: accumulate, reuse, and evolve knowledge across a sequence of tasks without touching parameters.

#### Project 3: GFlowRL — policy learning as distribution matching (~00:16–00:17)

Gao's hope is that this becomes a genuine alternative to the dominant RL methods (GRPO, PPO). **The key difference: policy learning is defined as distribution matching rather than reward maximization.** Concretely, the algorithm samples solutions *in proportion to the reward they were assigned* instead of collapsing onto the single highest-reward mode. That unlocks far greater solution diversity and, he argues, turns out to be more cost-effective to train.

He ran out of time here and closed by inviting questions offline.

### Quotes

> "The portrait of the large scale language model is mainly a talker. It seems that the model knows everything, but it's really difficult if you ask it to do something for you. So agentic modeling is the process where we want to turn this talker to a doer." (~00:02)

The premise of the whole talk.

> "Harness is like the training data to agentic modeling, just like the internet data to model pre-training." (~00:08)

The load-bearing analogy: building a harness *is* manufacturing training data.

> "Human learning is different. I never recall all the details of my previous experience. I only remember what matters." (~00:16)

The motivation for EvoLib: memory should be distilled skills and lessons, not a warehouse of transcripts.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Orchard | 開源、可規模化的 agentic modeling 框架與生態系 | Open-source framework/ecosystem for scalable agentic modeling | arXiv 2605.15040;github.com/microsoft/Orchard |
| Orchard Env | Orchard 核心的 Kubernetes-native 環境服務,提供 sandbox 生命週期 primitives | Lightweight Kubernetes-native environment service at Orchard's core; reusable sandbox-lifecycle primitives | 講者比喻為「AI agent 的 OS runtime」/ "an OS runtime for AI agents" |
| Orchard-SWE | 軟體工程 agent recipe,蒸餾約 10 萬條 trajectory | Software-engineering agent recipe; ~100k distilled trajectories | SWE-bench Verified 73%(論文另列 RPR-based RL 69.7%)|
| Orchard-GUI | GUI/網頁導航 agent recipe | Vision-language computer-use / navigation agent recipe | |
| Orchard-Claw | 個人助理 agent recipe | Personal-assistant agent recipe | 逐字稿聽成 "crow / crawl" |
| EvoLib | test-time learning 框架:靠會演化的知識庫累積與重用技能,不更新參數 | Test-time learning with an evolving library of skills and reflective insights; no parameter updates | arXiv 2605.14477(Weijia Xu 等,含 Jianfeng Gao)|
| GFlowRL | 把 policy learning 定義成 distribution matching 的 RL 方法,按 reward 比例抽樣 | Distribution-matching RL for LLMs; samples in proportion to reward instead of maximizing it | Microsoft Research;定位為 GRPO / PPO 的替代方案 |
| MAI | Microsoft 自建大型語言模型的專責團隊 | Microsoft's dedicated in-house frontier-model team | 講者提到「最近釋出十幾個模型」 |
| Azure AI Foundry | 託管數百至數千個開源模型的模型商店 | Model store hosting hundreds to thousands of open-source models | 逐字稿聽成 "Asia foundry" |
| SWE-bench Verified | 軟體工程 agent 的標準 benchmark | Standard benchmark for software-engineering agents | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Jen Ga / Jen Hun / Jang | Jianfeng Gao |
| agenting modeling / analytic modeling / agit modeling / engineic modeling / aging modeling | agentic modeling |
| Asian honey / aging harness / agent honey | agent harness |
| our chart / orchard / okra / ultra / or chart | Orchard |
| ultra ev / ultra environment / or chart Evar | Orchard Env |
| okra swing / okra eval | Orchard-SWE |
| ultra GUI | Orchard-GUI |
| crow / crawl | Orchard-Claw |
| evolve lab / involving libraries | EvoLib(Evolving Library) |
| GRO IO / GRO I am | GFlowRL |
| GP or PO | GRPO / PPO |
| sing coet native | (lightweight) Kubernetes-native |
| Asia foundry | Azure AI Foundry |
| we bench verified | SWE-bench Verified |
| distillering / distating | distilling |
| reverse care divergence | reverse-KL divergence |
| the key for the China | the key for the trainer(語音辨識錯誤,語境為 trainer)|
| expirations | (on-policy) distillation |

## 待確認 / To Verify

- Orchard-SWE 的 SWE-bench Verified 分數:講者口說「70… 73%」,論文摘要為 69.7%(RPR-based RL)與 73.0%(value-model reranking),筆記採 73%,但需確認他投影片上引用的是哪一個。/ Gao said "70… 73%"; the paper reports 69.7% (RPR-based RL) and 73.0% (value-model reranking) — confirm which number his slide showed.
- 蒸餾 trajectory 數量「約 100,000」為口述數字,未在投影片上驗證。/ The "~100,000 distilled trajectories" figure is from speech only.
- MAI 團隊「最近釋出十幾個模型」的具體型號未提及。/ He didn't name the dozen-or-so MAI models.
- GFlowRL 是否即為投影片上的名稱(逐字稿聽成 "GRO IO"),已由「distribution matching / 按 reward 比例抽樣 / GRPO 替代方案」三個特徵交叉比對到 Microsoft Research 的 GFlowRL,但仍建議看投影片確認。/ GFlowRL was matched by three cross-checking features; confirm against the slide.
