---
title: "Building Frontier Inference and Training Infra for Agent: A Case Study of SGLang and Miles"
title_zh: "為 Agent 打造前沿推論與訓練基礎設施:SGLang 與 Miles 的案例"
speaker: "Banghua Zhu"
affiliation: "Co-Founder, RadixArk"
type: talk
stage: Atlas
date: 2026-08-01
session: "Session 3: Frameworks & Dev Platforms"
video: "https://www.youtube.com/watch?v=psPzCQbjCCo&t=14460s"
video_range: "04:01:00–04:13:55"
transcript: "tmp/[English (auto-generated)] Atlas Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [sglang, reinforcement-learning, inference, kv-cache, open-source]
---

# 為 Agent 打造前沿推論與訓練基礎設施:SGLang 與 Miles 的案例(Building Frontier Inference and Training Infra for Agent: A Case Study of SGLang and Miles)

**一句話總結**:2026 是 agentic infrastructure 之年——推論端的壓力來自 cache 重用率、trillion 級模型與百萬 context,訓練端的壓力則來自環境多樣性與 train–inference mismatch,而 RadixArk 用 SGLang 與 Miles 兩個開源專案分別回應。
**One-line summary**: 2026 is the year of agentic infrastructure — inference is squeezed by cache reuse, trillion-parameter models, and million-token context, while RL training is squeezed by environment diversity and train–inference mismatch; RadixArk answers each with SGLang and Miles.

## 中文筆記

### TL;DR

- **RadixArk 的定位**:讓前沿等級的 AI 基礎設施開放且人人可用,兩根支柱是推論引擎 **SGLang** 與強化學習訓練框架 **Miles**(從 slime fork 並持續共同演化)。
- **推論端三個挑戰**:高 cache 重用率(agentic workload 的成本命脈)、trillion 級模型的部署與分片、1M context 已成常態。
- **對應三組技術**:unified hybrid radix cache + HiCache(把 KV cache 從 HBM 一路往下放到 DRAM 與外部儲存);5D 平行化 + DCP/PCP 與 PD、EPD 分離部署;chunked pipeline parallelism、序列切分與 sparse attention。實測 GLM-5.2 從 day-zero 最佳再拉到約 2.2×,達到每使用者約 500 tokens/s。
- **訓練端三個挑戰**:環境更多樣(甚至需要實驗室實驗才拿得到 reward)、train–inference mismatch(會**無聲地**把你的 RL 變成 off-policy)、吞吐量決定你能做幾次實驗。
- **消除 mismatch 的三個層次**:推論引擎的 deterministic kernel、多輪 agentic chat template 的 token-in-token-out 對齊、演算法層修正(rollout routing replay、truncated masked importance sampling)。

### 重點整理

#### RadixArk、SGLang 與 Miles(約 04:01–04:04)

Zhu 自介為 RadixArk 共同創辦人兼 CTO,也是 Berkeley 博士。RadixArk 的使命是**讓前沿等級的 AI 基礎設施開放且人人可及**,做法是全部在開源裡建:推論端是 SGLang,已在各處被當作生產推論引擎採用;後訓練端是較新的 RL 框架 **Miles**,正逐步被當成前沿級的 post-training 基礎設施使用。

SGLang 生態系的組成:

- **SGLang 核心**:語言模型與視覺語言模型推論
- **diffusion**:較新的專案,做影像與影片生成(以及世界模型類推論)
- **omni**:更近期,鎖定 ASR 與 TTS 等音訊側

整體針對 agentic workload 最佳化,提供**極快的 day-zero 模型支援**與很廣的硬體支援:NVIDIA、AMD、TPU、Trainium、Intel 等。

**Miles** 是企業級 RL 框架,從 **slime** fork 並與之共同演化,在 NVIDIA 與 AMD 最新硬體上加了更多功能。slime 由 Zhipu AI 與社群共同打造,用於他們的 GLM 模型系列訓練,因此已在超大規模生產訓練上經過實戰驗證。Miles 同樣提供**所有開放模型的 day-zero 支援**——Kimi K3、Thinking Machines 的 Inkling、NVIDIA 的 Nemotron 等——模型一發布你就能直接拿 Miles 做訓練與客製、拿 SGLang 做推論。架構上 Miles **原生用 SGLang 當 rollout 階段、用 NVIDIA Megatron 當訓練階段**以取得最佳效能。

採用面:硬體公司、hyperscaler、企業、AI lab(尤其是新 lab)、開發者工具與 neocloud 都在用。生態系合作方面,他們與 Google Cloud 密切合作提升其內部推論堆疊的吞吐,Cloudflare、IBM、xAI、Meta 也都拿 SGLang 當推論引擎後端。

他給整場定調:**2026 是 agentic infrastructure 之年**。推論端需求爆炸且挑戰非常獨特;訓練端則是「每個細節都重要」,還很早期,但每件事都得做對,才能在不傷害模型泛化能力的前提下把它訓起來。

#### 推論端:三個挑戰與 SGLang 的三組答案(約 04:04–04:09)

**挑戰一:高 cache 重用率。** 他以 DeepSeek V4 極低的 cache-hit 價格為例——這類定價假設你真的能達到很高的 cache 重用,而確保高 cache hit rate 直接決定你整體 serving 成本。SGLang 帶來兩項技術:

- **Unified hybrid radix cache**:為近期所有 hybrid 模型設計,確保 prefix cache 在新架構上也能順暢運作。
- **HiCache**:讓 KV cache 從 HBM 往下移到 DRAM、甚至外部儲存,在不同記憶體層之間以最有效率的方式調度。

以 Qwen3-Coder 為具體例子,cache 命中率、TTFT 與吞吐都有大幅改善。

**挑戰二:大模型擴展**,面對一 trillion、三 trillion 甚至更大的模型。標準技術是 5D 平行化(data、tensor、context、pipeline、expert),再加上較新的策略如 DCP 與 PCP。部署策略也在演進:從 colocate 出發,規模變大、prefill/decode 更不平衡時逐步走向 **PD 分離**;視覺語言模型則再多一層 **EPD**——連 encoder 也分離出去。runtime 最佳化方面,投機解碼從 EAGLE 到 MTP,再到 D-Flash 與 DeepSeek 近期提出的 DSpark;排程則有 overlap scheduler,以及他們最近的 spec v2,用來更好地支援推論階段原生的投機解碼加速。

**挑戰三:長 context**,尤其是要撐到 1M context window:

- **Chunked pipeline parallelism**:不再一次送出整段 prefill 序列,而是把長 prompt 切成小 chunk 平行處理。
- **序列/context 切分**:換一個維度切,把序列拆到多顆 GPU 上處理長 context。
- **Sparse attention 最佳化**(HiSparse):用一個 hot buffer 搭配完整 KV 來處理,讓 sparse attention 佔用更少記憶體、換到高得多的吞吐。

綜合這些技術再加上調校,他給的具體數字是:**GLM-5.2 在 day zero 效能就已是最佳,之後累積達成超過 2.2× 的改進,來到每使用者約 500 tokens/s**。

小結時他列出 SGLang 率先在大規模生產中導入的技術:RadixAttention、投機解碼、PD 分離、sparse attention、與 Miles 的原生整合,以及較近期的 D-Flash、DSpark 與 HiSparse。

#### 訓練端:agentic RL 的三個挑戰(約 04:09–04:13)

**挑戰一:環境多樣性大增。** 不只是更多 tool call 與更長 context,有些環境本身就很難執行,甚至需要**實驗室實驗才能拿到 reward 訊號**。對策是與大多數環境供應方密切合作,讓 Miles 原生支援主流開源環境——他點名了 Prime Intellect 的 verifiers、Daytona、NVIDIA NeMo Gym 等。

**挑戰二:train–inference mismatch。** 這是前沿 lab 近期非常熱門的題目,也是 Miles 最大的著力點之一:如果訓練引擎與推論引擎之間有很大的落差,**它會自然而然、而且無聲無息地把你的 RL 變成 off-policy**,傷害整個訓練 run。他列了三個層次的解法:

1. **推論引擎的 deterministic kernel**——這是能讓推論與訓練引擎逐 token 精確對齊的前提。
2. **Chat template 修正**:token-in-token-out,確保多輪 agentic chat template 完全對齊,前幾輪的 token 不會在後續被重新 tokenize 成別的東西。
3. **演算法層修正**:rollout routing replay、truncated masked importance sampling,用來在大規模 RL 下維持訓練穩定。

**挑戰三:吞吐量。** 吞吐越高,你就能用更多不同的實驗更快迭代,GPU 利用率也更好。這一項偏工程:他們為大多數模型提供 day-zero 支援,而且**每個新模型都跑自家的 in-house training run 驗證**——確認 KL 有被控制住、reward 確實往上走,使用者才能直接拿去用而不必擔心。

最後兩項近期投入:

- **全非同步 RL(fully async RL)** 已有相當成熟的支援,把 rollout 與訓練的時間重疊起來、並把兩者分離部署,以最大化 GPU 使用效率(相對於同步做法)。
- **低精度訓練**:rollout 走更低精度、訓練後端搭配某種量化訓練。他們原生支援 8-bit 與 4-bit 的 rollout,並在最近的合作中做到 **NVFP4 原生 rollout 且沒有效能損失**。

### 金句

> "2026 is actually the year of agentic infrastructure."(約 04:04)

他為推論與訓練兩端所有挑戰下的統一標題。

> "If you have very large train–inference mismatch between different engines, then that will naturally and silently turn your RL to be more off-policy and hurt your entire training run."(約 04:10)

Agentic RL 最陰險的失敗模式——它不會報錯,只會讓你的訓練悄悄變差。

## English Notes

### TL;DR

- **RadixArk's mission** is to make frontier-level AI infrastructure open and accessible, built entirely in the open on two pillars: the **SGLang** inference engine and **Miles**, an enterprise RL post-training framework forked from and co-evolving with slime.
- **Three inference challenges**: high cache reuse (the cost lever for agentic workloads), deploying and sharding trillion-parameter models, and million-token context as the new norm.
- **Three answers**: unified hybrid radix cache plus HiCache (moving KV cache from HBM down through DRAM to external storage); 5D parallelism plus DCP/PCP with PD and EPD disaggregated deployment; and chunked pipeline parallelism, sequence splitting, and sparse attention. On GLM-5.2 they went from best-in-class at day zero to a further 2.2× improvement, reaching roughly 500 tokens/s per user.
- **Three training challenges**: far more diverse environments (some requiring lab experiments to produce a reward signal), train–inference mismatch (which **silently** turns your RL off-policy), and throughput, which determines how many experiments you can run.
- **Eliminating mismatch takes three layers**: deterministic kernels in the inference engine, token-in-token-out alignment of multi-turn agentic chat templates, and algorithmic fixes (rollout routing replay, truncated masked importance sampling).

### Key Points

#### RadixArk, SGLang, and Miles (~04:01–04:04)

Zhu introduces himself as co-founder and CTO of RadixArk and a Berkeley PhD. RadixArk's mission is to **make frontier-level AI infrastructure open and accessible to everyone**, and it builds entirely in open source: SGLang for inference, already adopted as a production inference engine widely; and more recently Miles, an RL framework gradually being picked up as frontier-level post-training infrastructure.

The SGLang ecosystem has three parts: the core engine for language and vision-language model inference; **diffusion**, a newer project for image and video generation (and world-model inference); and **omni**, the most recent, targeting ASR and TTS on the audio side. The whole thing is optimized for agentic workloads, with fast **day-zero model support** and broad hardware coverage — NVIDIA, AMD, TPU, Trainium, Intel, and others.

**Miles** is the enterprise-grade RL framework, forked from and co-evolving with **slime**, adding features for the latest NVIDIA and AMD hardware. slime was built by Zhipu AI together with the community for training their GLM model series, so it has been battle-tested on production training at very large scale. Miles likewise offers **day-zero support for all open models** — Kimi K3, Thinking Machines' Inkling, NVIDIA's Nemotron, and so on — so the day a model ships you can train and customize with Miles and serve with SGLang. Architecturally, Miles **natively uses SGLang as the rollout stage and NVIDIA Megatron as the training stage** for best performance.

On adoption: hardware companies, hyperscalers, enterprises, AI labs (especially newer ones), developer tools, and neoclouds are running SGLang and Miles as part of their infrastructure. Ecosystem collaborations include close work with Google Cloud on throughput for their internal inference stack, and Cloudflare, IBM, xAI, and Meta all using SGLang as a backend for their inference engines.

His framing for the rest of the talk: **2026 is the year of agentic infrastructure.** On inference, demand is exploding and the challenges are genuinely unique. On training, every detail matters — it's still early, but everything has to be done right if you want to train the model without hurting its generalization capability.

#### Inference: three challenges, three sets of answers (~04:04–04:09)

**High cache reuse** comes first. He points at DeepSeek V4's very low cache-hit pricing: such pricing presumes you can actually achieve high reuse, and ensuring a high cache hit rate directly determines total serving cost. SGLang brings two things here — a **unified hybrid radix cache**, designed so prefix caching runs smoothly across all the recent hybrid models and new architectures, and **HiCache**, which lets you move KV cache down from HBM to DRAM and even to external storage, scheduling it efficiently across memory tiers. On Qwen3-Coder specifically, cache rate, TTFT, and throughput all improved substantially.

**Large model scaling** comes second, at one trillion, three trillion, and beyond. The standard toolkit is 5D parallelism — data, tensor, context, pipeline, expert — plus newer strategies like DCP and PCP. Deployment strategies are evolving too: teams start colocated, then move toward **PD (prefill/decode) disaggregation** at larger scale and with more imbalanced prefill/decode profiles; for vision-language models there is also **EPD**, which disaggregates the encoder as well. On the runtime side, speculative decoding runs from EAGLE to MTP to D-Flash and DeepSeek's recent DSpark, and scheduling includes an overlap scheduler plus their recent spec v2 for better native speculative-decoding speedup at inference.

**Long context** is third, particularly scaling to a million-token window. **Chunked pipeline parallelism** stops sending the whole prefill sequence at once, chunking long prompts and processing them in parallel. A second, orthogonal dimension of chunking **splits sequences across GPUs**. And **sparse attention optimization (HiSparse)** processes a full KV with a hot buffer, so sparse attention occupies less memory and yields much higher throughput.

Combining all of this with tuning, his concrete result: on **GLM-5.2 the day-zero performance was already best-in-class**, and over time they achieved more than a further **2.2× improvement, reaching up to about 500 tokens/s per user**.

Summarizing the inference half, he lists what SGLang introduced first at large production scale: RadixAttention, speculative decoding, PD disaggregation, sparse attention, native Miles integration, and more recently D-Flash, DSpark, and HiSparse.

#### Training: three challenges in agentic RL (~04:09–04:13)

**Environment diversity** has grown sharply. It is not just more tool calls and longer context — some environments are very hard to execute, and some may even require lab experiments to produce a reward signal. RadixArk's response has been close collaboration with most environment suppliers so Miles natively supports the major open-source environments, among them Prime Intellect's verifiers, Daytona, and NVIDIA NeMo Gym.

**Train–inference mismatch** is a very popular topic in frontier labs right now and one of Miles's biggest focuses. If there is a large mismatch between your training and inference engines, it will **naturally and silently turn your RL more off-policy and hurt the entire training run**. Three layers of fix:

1. **Deterministic kernels in the inference engine** — a prerequisite for exact token-level agreement between inference and training engines.
2. **Chat template fixing** — token-in-token-out, so multi-turn agentic chat templates stay aligned and tokens from prior turns match exactly, with no drift introduced by re-tokenization.
3. **Algorithmic fixes** — rollout routing replay and truncated masked importance sampling, both aimed at stable training at large RL scale.

**Throughput** is the third: higher throughput means faster iteration across more experiments and better GPU utilization. This one is mostly engineering discipline — they provide day-zero support for most models and verify each with their **own in-house training runs**, checking that KL stays controlled and reward actually goes up, so users can adopt the framework without that concern.

Two recent investments close the talk. **Fully asynchronous RL** now has sophisticated, mature support: overlapping rollout with training time and disaggregating the two to make the best use of GPUs, compared against the synchronous case. And **low-precision training**: rollout in lower precision with some form of quantized training on the backend. They natively support 8-bit and 4-bit rollout, and recently worked with a hardware partner to support **NVFP4-native rollout in the RL stage with no performance loss**.

### Quotes

> "2026 is actually the year of agentic infrastructure." (~04:04)

His unifying header for both the inference and training challenges.

> "If you have very large train–inference mismatch between different engines, then that will naturally and silently turn your RL to be more off-policy and hurt your entire training run." (~04:10)

The nastiest failure mode in agentic RL: it never raises an error, it just quietly makes your training worse.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| SGLang | 生產級開源推論引擎(LLM / VLM),另有 diffusion 與 omni 兩個子專案 | Production-grade open-source inference engine (LLM / VLM), plus diffusion and omni sub-projects | 廣泛硬體支援:NVIDIA、AMD、TPU、Trainium、Intel / broad hardware support |
| Miles | 企業級 RL 後訓練框架,從 slime fork 並共同演化 | Enterprise RL post-training framework, forked from and co-evolving with slime | 原生以 SGLang 為 rollout、Megatron 為訓練後端 / SGLang for rollout, Megatron for training |
| slime | Zhipu AI 與社群為 GLM 系列訓練打造的 RL 框架 | RL framework built by Zhipu AI with the community for the GLM model series | Miles 的上游 / Miles's upstream |
| HiCache | 分層 KV cache:HBM → DRAM → 外部儲存 | Hierarchical KV cache across HBM, DRAM, and external storage | |
| Unified hybrid radix cache | 讓 prefix cache 在 hybrid attention 模型上正常運作 | Makes prefix caching work across hybrid-attention architectures | |
| RadixAttention | SGLang 最早在大規模生產導入的前綴快取技術 | SGLang's prefix-caching technique, first at production scale | |
| PD / EPD 分離 | prefill–decode 分離;VLM 再多分離 encoder | Prefill–decode disaggregation; EPD adds encoder disaggregation for VLMs | |
| EAGLE / MTP / D-Flash / DSpark | 投機解碼技術的演進;DSpark 由 DeepSeek 近期提出 | The progression of speculative decoding techniques; DSpark recently introduced by DeepSeek | D-Flash 與 DSpark 拼寫待確認 / spellings to verify |
| HiSparse | sparse attention 最佳化:完整 KV 搭配 hot buffer | Sparse attention optimization: full KV with a hot buffer | |
| RL 環境 / RL environments | Prime Intellect verifiers、Daytona、NVIDIA NeMo Gym | Prime Intellect verifiers, Daytona, NVIDIA NeMo Gym | 另有兩三個名稱聽不清 / two or three further names unintelligible |
| 生態系合作 / Ecosystem partners | Google Cloud、Cloudflare、IBM、xAI、Meta | Google Cloud, Cloudflare, IBM, xAI, Meta | 均以 SGLang 為推論後端 / all use SGLang as an inference backend |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Banga Juke / Bonha | Banghua Zhu |
| Raex Arc / Regisart / Reddisart / Reddit | RadixArk |
| HGLN / HLN / Asha / Ashel / Ashland / Achelan / Helen | SGLang |
| MOS / mouse / smiles | Miles |
| slam | slime |
| triple AI | Zhipu AI |
| GM model series / GM 5 5 5.2 | GLM model series / GLM-5.2 |
| Kim Jam / Kim K3 | Kimi K3 |
| inkling from syncing machine | Inkling from Thinking Machines |
| neotron from avidia | Nemotron from NVIDIA |
| magnetron | Megatron |
| radius cache / radius attention | radix cache / RadixAttention |
| high cache / high spars | HiCache / HiSparse |
| QTFT | TTFT |
| PD desertation / disagregation | PD disaggregation |
| overlapuler | overlap scheduler |
| one qu three coder | Qwen3-Coder |
| draw out routing replay | rollout routing replay |
| truncated mass important sampling | truncated masked importance sampling |
| MVIP4 | NVFP4 |
| hover / open in / agent in | 待確認(見下)/ to verify (below) |

## 待確認 / To Verify

- 投機解碼演進中的 "D-Flash" 與 "DSpark" 兩個名稱僅依發音推定,需看投影片確認拼寫與出處。/ "D-Flash" and "DSpark" in the speculative-decoding progression are inferred from pronunciation; confirm spelling and origin against the slides.
- Miles 原生支援的 RL 環境清單中,字幕的 "hover"、"open in"、"agent in" 三個名稱無法辨識;可辨識的是 Prime Intellect verifiers、Daytona、NeMo Gym。/ Three environment names in the transcript ("hover", "open in", "agent in") are unintelligible; the legible ones are Prime Intellect verifiers, Daytona, and NeMo Gym.
- 「最近與 ___ 合作支援 NVFP4 原生 rollout」的合作對象,字幕作 "humans end",無法確認(NVFP4 為 NVIDIA 格式,但不宜逕自推定)。/ The partner in "recently worked with ___ to support NVFP4-native rollout" is transcribed as "humans end" and cannot be confirmed (NVFP4 is an NVIDIA format, but that is not sufficient to assume the partner).
- 「agent in 被近期某模型的 post-training 使用」該句(字幕 "used by recent communic case post training for crackness")完全無法還原。/ The clause about a recent model's post-training using one of those environments is unrecoverable from the transcript.
- SGLang diffusion 子專案中提到的 "V and wood model" 應為 video / world model,但未確認。/ "V and wood model" under SGLang diffusion is likely video / world model inference, unconfirmed.
