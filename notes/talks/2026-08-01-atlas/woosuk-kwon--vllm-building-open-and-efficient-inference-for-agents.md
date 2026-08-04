---
title: "vLLM: Building Open and Efficient Inference for Agents"
title_zh: "vLLM:為 Agent 打造開放且高效的推論引擎"
speaker: "Woosuk Kwon"
affiliation: "Co-Founder & CTO, Inferact"
type: talk
stage: Atlas
date: 2026-08-01
session: "Session 3: Frameworks & Dev Platforms"
video: "https://www.youtube.com/watch?v=psPzCQbjCCo&t=13461s"
video_range: "03:44:21–04:00:55"
transcript: "tmp/[English (auto-generated)] Atlas Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [vllm, inference, kv-cache, parallelism, open-source]
---

# vLLM:為 Agent 打造開放且高效的推論引擎(vLLM: Building Open and Efficient Inference for Agents)

**一句話總結**:Agent 幾乎沒有改變推論的 API,卻徹底改變了 API 底下的一切——vLLM 因此沿三條軸線重寫自己:workload-aware 的模型平行化、動態分層的 KV cache,以及能吃下地球上任何一種運算的多硬體後端。
**One-line summary**: Agents barely changed the inference API but changed everything underneath it — so vLLM is rebuilding along three axes: workload-aware model parallelism, dynamic hierarchical KV cache, and enough hardware backends to turn any compute on earth into tokens.

## 中文筆記

### TL;DR

- **API 沒變,底下全變了**:`vllm serve` 給的仍是 OpenAI / Anthropic 相容端點,agent framework 開箱即用;真正被 agent 改寫的是引擎內部。
- **三條壓力軸線**:模型變大(Kimi K3、DeepSeek V4 這類 trillion 級模型逼你認真做 model parallelism)、context 變長(數百輪對話、上看 1M token,絕不能重算前幾輪)、token 需求爆炸(成長速度快過 GPU 供給)。
- **平行化沒有萬用解**:vLLM 支援七種平行化(含訓練世界沒有的 decode context parallelism),但正確答案取決於模型架構 × 叢集配置 × workload 形狀。實測中「16 GPU 上的 TP × PP × EP 組合」明顯打敗直覺的單機 8-way TP。
- **Hybrid 模型讓記憶體切分變成動態問題**:full attention 的 KV 隨 context 線性成長,linear attention(如 Kimi Delta Attention)則是每個序列固定大小的 state。vLLM 用共用記憶體池 + 各自的 allocator 動態再平衡,取代靜態切分。
- **Token 經濟學翻轉了**:模型夠聰明時,一個 token 的價值遠超過生成它的成本,於是需求無上限而地球上的 GPU 不夠用——vLLM 的答案是 10+ 種硬體後端的 plugin 架構。

### 重點整理

#### vLLM 現況與兩種用法(約 03:45–03:47)

Kwon 自介為 vLLM 的 co-creator,以及圍繞 vLLM 成立的新創 Inferact 的共同創辦人。vLLM 是開源的 LLM 推論引擎,目標是讓 LLM 推論「efficient and effortless」;大約三年前在 UC Berkeley 他讀博期間開始,至今持續高速成長,GitHub 星數在演講前不久突破約 88k。他強調這是一個橫跨學界與業界的高度協作專案,主要貢獻者包括 Red Hat、NVIDIA、AMD、Google、Moonshot,以及 Inferact 自己,並已被廣泛部署在生產環境。

兩種用法:

- **離線批次**:Python 的 `LLM` class,給它一個 Hugging Face 模型名稱、呼叫 `generate` 就結束。模型載入、最佳化、排程、記憶體管理與 GPU 利用全部在底下自動處理。
- **線上服務**:`vllm serve` 一行指令起一個 OpenAI 相容端點;Anthropic API 也支援,因此任何會講這兩種 API 的 agent framework 都能直接接上。

他接著點出全場的樞紐:**這個 API 跟幾年前其實差不多,為 agent 幾乎沒改變**;為 agent 大改的是 API 底下的一切。

#### Agent 施加的三條壓力(約 03:47–03:49)

1. **更大的模型**:前沿 agent 模型如 Kimi K3、DeepSeek V4 都是 trillion 級參數,逼所有人認真面對 model parallelism。他把這視為機會——它讓我們能用很多有創意、各有取捨的方式去切模型。
2. **更長的 context**:agent session 動輒數百輪,可以到一百萬 token,而且 context 在整個 session 內只增不減。因此管理前幾輪的 KV cache 對效能極為關鍵,**推論框架絕對不能重算前一輪的 token**,否則就是大量重複計算與浪費。
3. **巨大的 token 需求**:agent 越聰明越能幹,可以部署的場景就趨近無限,需求實質上沒有上限,而且**成長速度快過 GPU 供給**。vLLM 的對策是把高效推論擴展到更多種硬體後端,好把所有能用的算力都拿來產 token。

#### 軸線一:平行化沒有普世贏家(約 03:49–03:53)

為了服務這麼大的模型,vLLM 今天支援七種主要平行化:tensor、pipeline、data、expert、sequence,以及兩種 context parallelism。其中一種是訓練世界不存在的 **decode context parallelism**——圍繞 KV cache 做的平行化。作為通用引擎,vLLM 有效率地實作了全部,也支援它們的混合。

但他說這還不夠。**關鍵在於這些平行化必須針對目標模型架構、目標叢集配置與目標 workload 形狀被正確選擇與調校,沒有 universal winner。**

他用一個真實案例說明調校長什麼樣:在 B200 GPU 上、以 prefill/decode 分離的部署方式跑 DeepSeek 模型的 prefill 階段(這批 GPU 只負責 prefill)。最直覺的部署是單機 8-way tensor parallelism——最標準、最簡單。但**實測的勝出組合完全不同**:改成跨 16 顆 GPU、由 tensor parallelism × pipeline parallelism × expert parallelism(再加上 sequence parallelism)組成的配置作為一個模型 replica,得到明顯更低的 TTFT(首 token 延遲)與明顯更高的每 GPU 吞吐。

原因他快速帶過:pipeline parallelism 讓長 prefill 序列的不同 chunk 之間也能平行;sequence parallelism 讓通訊與計算有更多重疊機會;expert parallelism 相較 8-way TP 給出更好的 GEMM(矩陣乘法)形狀。結論是在 agentic 時代,你需要正確的洞見與效能模型來設定這些參數,而 **vLLM 提供的是讓你能玩遍所有平行化的共同基底**。

#### 軸線二:KV cache——從靜態切分到動態再平衡(約 03:53–03:58)

現代 LLM 的一個關鍵特徵是它們是 **hybrid 模型**:全域注意力層與更高效的注意力機制(sliding window,或 Kimi Delta Attention 這類 linear attention)交錯排列。這正是 1M context 之所以可行的原因——純粹的 global attention 在百萬 context 下記憶體開銷太大。

理論上很漂亮,實務上製造出真正的系統難題:**不同注意力型別的層,記憶體行為完全不同**。full attention 的 KV cache 隨 context 線性成長;linear attention(KDA)則是每個序列維持固定大小的 state,與實際 context 長度無關。那 GPU 記憶體該怎麼在兩者之間切?

直覺解是**靜態切分**——保留 x% 給 full attention、y% 給其餘。可行,但問題是最佳切分點取決於 batch size 與 context 長度,而這兩者在推論過程中一直變動。

vLLM 的解法是**動態切分**:用一個共用的 GPU 記憶體池,每種記憶體行為不同的注意力型別各自擁有一個 allocator,從共用池取用。full attention 的 allocator 按 token 數向池中請求;KDA 的 allocator 因為是 linear attention,一次為整個序列配一個大 block;兩者之間有邏輯動態共享同一塊記憶體空間。實際效果是**引擎自動在兩者之間再平衡,不浪費任何 GPU 記憶體**,使用者不必操心不同注意力型別的記憶體切分。

但只管好 GPU 記憶體裡的 KV cache 還不夠。agent session 的特徵是**又長壽又斷斷續續**:模型產出一些 token,然後停下來等 tool call、有時等人類回覆,然後再繼續。在這些等待期間,KV cache 得被放在某處。vLLM 的抽象是 **KV connector**:把閒置的 KV cache 存到外部記憶體(CPU 記憶體或磁碟),需要時再取回。他坦言他們在這個抽象的設計上花了很多力氣,要確保它能跟 Mooncake 這類第三方函式庫良好協作,也要能配合 prefill/decode 分離這種 KV 搬移本身就很動態複雜的機制——KV 得在 prefill instance 與 decode instance 之間、以及 prefill instance 與 Mooncake 這類分散式 KV 儲存池之間移動。做好這層基礎設施的目的很單純:**在多輪 agent session 裡,只要儲存空間允許,就永遠不重算前幾輪的 token。**

#### 軸線三:硬體——把地球上的算力都變成 token(約 03:58–04:00)

Kwon 認為 token 的經濟學正在翻轉:模型越聰明,**一個 token 的價值就遠超過生成它的成本**,於是需求自然爆炸,而世界上老實說沒有足夠的 GPU 來供應。問題因此變成:我們能不能有效率地用上地球上所有可用的算力來產 token?

vLLM 的答案是今天支援 10 種以上的硬體後端。NVIDIA GPU 顯然是主力,但也涵蓋 Google TPU、AMD GPU 以及業界其他多種晶片;它們以 **plugin 結構**接進 vLLM,共用核心、各自客製硬體相關部分。他指出這在推論領域特別合理,因為**推論的 API 已經高度標準化**——使用者仍然用同一套 OpenAI 或 Anthropic API,只是底下換了另一種硬體在產 token。

他因時間關係跳過細節投影片,但留下 TL;DR:把新硬體帶起來、讓它高效支援新模型,這件事**因為 coding agent 而正在變得比較容易**,但另一方面它仍然需要幾乎從頭重做整套推論堆疊,團隊正在積極處理。

總結一頁:agentic 時代從三條軸線施壓,vLLM 各給一個答案——大模型用 workload-aware 的 model parallelism、長 context 用動態且分層的 KV cache、爆炸的 token 需求用多樣的硬體後端;而且**今天講的全部都是開源的**。

### 金句

> "The API itself is pretty much similar to a few years ago … What has changed a lot for agents is everything underneath it."(約 03:47)

整場演講的框架:agent 革命發生在 API 之下。

> "There's no universal winner."(約 03:50)

平行化策略沒有預設正解,只有針對模型 × 叢集 × workload 的正解。

> "As models get smarter, the value of a token far exceeds the cost of generating it … and honestly there are not enough GPUs in the world to serve it."(約 03:58)

多硬體後端不是相容性功能,而是供給側的必然。

## English Notes

### TL;DR

- **The API didn't change; everything under it did.** `vllm serve` still hands you an OpenAI- (and Anthropic-) compatible endpoint that any agent framework speaks out of the box. Agents rewrote the engine, not the interface.
- **Three axes of pressure**: bigger models (trillion-parameter agent models like Kimi K3 and DeepSeek V4 force serious model parallelism), longer context (hundreds of turns, up to a million tokens, with recomputation strictly forbidden), and unbounded token demand growing faster than GPU supply.
- **Parallelism has no universal winner.** vLLM supports seven kinds, including a decode context parallelism that doesn't exist in training — but the right choice depends on model architecture × cluster setup × workload shape. In one real case a TP × PP × EP configuration across 16 GPUs beat the obvious single-host 8-way TP baseline on both TTFT and per-GPU throughput.
- **Hybrid models turn memory partitioning into a dynamic problem.** Full attention's KV cache grows linearly with context; linear attention (e.g. Kimi Delta Attention) keeps a fixed-size state per sequence. vLLM replaces static partitioning with one shared pool, per-attention-type allocators, and automatic rebalancing.
- **Token economics have flipped**: once models are smart enough, a token is worth far more than it costs to generate, so demand is effectively unbounded and there aren't enough GPUs on earth — hence a plugin architecture spanning 10+ hardware backends.

### Key Points

#### Where vLLM stands, and the two ways to use it (~03:45–03:47)

Kwon introduces himself as a co-creator of vLLM and co-founder of Inferact, the startup built around it. vLLM is an open-source LLM inference engine whose goal is to make LLM inference "efficient and effortless." It started roughly three years ago at UC Berkeley during his PhD and has grown fast ever since — around 88k GitHub stars as of shortly before the talk. He stresses that it is a highly collaborative project across academia and industry, with major contributors including Red Hat, NVIDIA, AMD, Google, and Moonshot alongside Inferact, and that it is widely deployed for production inference.

Two entry points. Offline batch inference goes through the Python `LLM` class: pass a Hugging Face model name, call `generate`, done — model loading, optimization, scheduling, memory management, and GPU utilization are all handled underneath. Online serving is a single `vllm serve` command yielding an OpenAI-compatible endpoint; Anthropic APIs are supported too, so any agent framework that speaks either works out of the box.

Which sets up the hinge of the talk: **that API looks much as it did a few years ago — agents barely changed it. What agents changed enormously is everything underneath.**

#### The three pressures agents apply (~03:47–03:49)

First, **large models**. Frontier agent models — Kimi K3, DeepSeek V4 — are around a trillion parameters, forcing everyone to get serious about model parallelism. He frames this as opportunity: it opens many creative ways to shard a model, each with different trade-offs.

Second, **long context**. Agent sessions run for hundreds of turns, up to a million tokens, and context only grows over a session. Managing the KV cache of prior turns is therefore critical, and the engine **must never recompute tokens from a previous turn** — otherwise you get enormous duplicated computation and wasted compute.

Third, **enormous token demand**. As agents get smarter and more capable there are near-infinite places to deploy them, so demand is effectively unbounded — and growing faster than GPU supply. vLLM's response is to make efficient inference work on many more hardware backends so that all available compute can be turned into tokens.

#### Axis 1: no universal winner in parallelism (~03:49–03:53)

vLLM today supports seven main kinds of parallelism: tensor, pipeline, data, expert, sequence, and two flavors of context parallelism — one of which, **decode context parallelism**, is parallelism around the KV cache and has no analogue in training. As a general-purpose engine, vLLM implements all of them efficiently, and mixtures of them.

That, he says, is not enough. **These parallelisms must be selected and tuned for the target model architecture, the target cluster setup, and the target workload shape. There is no universal winner.**

The worked example: prefill for a DeepSeek model on B200 GPUs in a disaggregated serving setup, where this pool of GPUs only does prefill. The most straightforward deployment is single-host 8-way tensor parallelism — standard and simple. The winning configuration is nothing like it: a combination of tensor, pipeline, and expert parallelism (plus sequence parallelism) spread across 16 GPUs per model replica, delivering substantially lower TTFT and substantially higher per-GPU throughput than the 8-way TP baseline.

Why: pipeline parallelism enables parallelism across chunks within a long prefill; sequence parallelism enables more communication–computation overlap; and expert parallelism yields better GEMM shapes than 8-way tensor parallelism. The takeaway is that in the agentic era you need the right insight and performance model to configure this correctly — and vLLM's contribution is the **common substrate on which you can play with all of these parallelisms**.

#### Axis 2: KV cache, from static partitioning to dynamic rebalancing (~03:53–03:58)

A defining property of modern LLMs is that they are **hybrid**: global attention layers interleaved with cheaper mechanisms such as sliding-window or linear attention (Kimi Delta Attention being his example). That interleaving is what makes million-token context feasible at all, since global attention alone consumes too much memory at that scale.

Elegant in theory, genuinely hard in practice, because **layers of different attention types have completely different memory behavior**. Full attention's KV cache grows linearly with context; a linear-attention layer like KDA keeps a fixed-size state per sequence regardless of actual context length. So how should GPU memory be carved between them?

The straightforward answer is **static partitioning** — reserve x% for full attention, y% for the rest. It works, but the optimal split depends on batch size and context length, both of which move continuously during inference.

vLLM's answer is **dynamic partitioning**: one shared GPU memory pool, with each attention type getting its own allocator drawing from it. The full-attention allocator requests from the pool by token count; the KDA allocator, being linear attention, allocates one large block for the entire sequence; and logic between them shares the same memory space dynamically. The engine **rebalances automatically so no GPU memory is wasted**, and the user never has to reason about the split.

Managing KV cache within GPU memory isn't sufficient, though. Agent sessions are **long-lived and intermittent**: generate some tokens, then wait — for tool calls, sometimes for a human — then continue. During those waits the KV cache has to live somewhere. vLLM's abstraction is the **KV connector**, which stores idle KV cache in external memory (CPU memory or disk) and brings it back on demand. He notes real design effort went into making that abstraction work with third-party libraries like Mooncake and with mechanisms like prefill/decode disaggregation, where KV movement is itself dynamic and complex — cache has to move from prefill instances to decode instances, and from prefill instances to a distributed KV storage pool. The purpose of all that infrastructure is one guarantee: **in a many-turn agent session, as long as storage allows, never recompute tokens from previous turns.**

#### Axis 3: hardware — turning all the compute on earth into tokens (~03:58–04:00)

Kwon argues the economics of tokens are flipping: as models get more intelligent, **the value of a token far exceeds the cost of generating it.** Demand explodes accordingly, and honestly there are not enough GPUs in the world to serve it. So the question becomes: can we use all available compute on earth to generate tokens efficiently?

vLLM's answer is 10+ hardware backends today. NVIDIA GPUs are the major focus, but Google TPUs, AMD GPUs, and various other industry chips are supported through a **plugin structure** that shares vLLM's core while customizing hardware-specific parts. This makes particular sense in inference, he argues, because **the API layer is already standardized** — you keep using the same OpenAI or Anthropic API while different silicon generates the tokens underneath.

He skips the detail slides for time, leaving the TL;DR: bringing up new hardware and making it efficiently support new models **is getting easier because of coding agents**, but it still requires retaking the entire inference stack from the ground up, and the team is actively working on it.

Summary: the agentic era stresses inference along three axes, and vLLM answers each — large models with workload-aware model parallelism, long context with a dynamic and hierarchical KV cache, exploding token demand with diverse hardware backends. Everything shown is open source.

### Quotes

> "The API itself is pretty much similar to a few years ago … What has changed a lot for agents is everything underneath it." (~03:47)

The framing device for the whole talk: the agent revolution happened below the API.

> "There's no universal winner." (~03:50)

Parallelism has no default answer, only an answer for a given model × cluster × workload.

> "As models get smarter, the value of a token far exceeds the cost of generating it … and honestly there are not enough GPUs in the world to serve it." (~03:58)

Multi-backend support is not a compatibility nicety; it is a supply-side necessity.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| vLLM | 開源 LLM 推論引擎,2023 年起於 UC Berkeley;約 88k GitHub stars | Open-source LLM inference engine, started at UC Berkeley ~3 years ago; ~88k GitHub stars | 貢獻者含 Red Hat、NVIDIA、AMD、Google、Moonshot、Inferact / contributors include Red Hat, NVIDIA, AMD, Google, Moonshot, Inferact |
| Inferact | 圍繞 vLLM 成立的新創,講者為共同創辦人兼 CTO | Startup built around vLLM; the speaker is co-founder and CTO | |
| Decode context parallelism | 圍繞 KV cache 的平行化,訓練世界不存在 | Parallelism around the KV cache; has no counterpart in training | vLLM 七種平行化之一 / one of vLLM's seven parallelism types |
| KV connector | 把閒置 KV cache 卸載到 CPU 記憶體或磁碟並取回的抽象層 | Abstraction for offloading idle KV cache to CPU memory or disk and retrieving it | 與 prefill/decode 分離協同運作 / interoperates with prefill/decode disaggregation |
| Mooncake | 分散式 KV cache 儲存池,vLLM 的 KV connector 與之整合 | Distributed KV cache storage pool integrated with vLLM's KV connector | 逐字稿作 "moon key" / "Moon Cake" |
| Kimi Delta Attention (KDA) | Kimi K3 採用的 linear attention 機制,是 hybrid 模型記憶體行為差異的代表 | The linear-attention mechanism in Kimi K3; his example of divergent memory behavior in hybrid models | Moonshot AI |
| Kimi K3 / DeepSeek V4 | 演講中舉例的 trillion 級前沿 agent 模型 | Trillion-parameter frontier agent models cited as examples | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Wusak Quan / Usok / Wuk | Woosuk Kwon |
| Infirect / Infact | Inferact |
| VLM / EDLM VLM / VM | vLLM(自動字幕把 LLM 與 vLLM 混淆)|
| deepse pro / deep 4 | DeepSeek(V4)|
| Kimmy K3 | Kimi K3 |
| KDA / sighting window | Kimi Delta Attention / sliding window |
| moon key | Mooncake |
| Redhead | Red Hat |
| TTFP | TTFT (time to first token) |
| accessor parallelism | expert parallelism |
| reccast | requests |
| disagregation / disegration | disaggregation |

## 待確認 / To Verify

- B200 prefill 案例的精確平行化度數(逐字稿把 "two-way tensor parallel × … pipeline parallel × eight-way …" 講得含糊,只能確定總計 16 GPU / replica、由 TP × PP × EP 組成)。/ The exact parallelism degrees in the B200 prefill case — the transcript garbles the numbers; only "16 GPUs per replica, TP × PP × EP" is reliable.
- 案例中的 DeepSeek 模型是哪一個版本(字幕作 "deepse pro",可能是 DeepSeek V4 Pro)。/ Which DeepSeek variant the B200 case used (transcript "deepse pro", possibly DeepSeek V4 Pro).
- 88k GitHub stars 為講者口述的近期數字,未指定日期。/ The 88k GitHub stars figure was stated verbally as "pretty recently," without a date.
- 「10 種以上硬體後端」的完整清單未在演講中列出(僅明確提到 NVIDIA、Google TPU、AMD)。/ The full list of "more than 10 hardware backends" was not enumerated; only NVIDIA, Google TPU, and AMD were named.
