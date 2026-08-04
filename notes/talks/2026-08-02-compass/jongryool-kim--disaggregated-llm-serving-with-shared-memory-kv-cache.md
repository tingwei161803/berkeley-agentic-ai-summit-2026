---
title: "Disaggregated LLM Serving with Shared Memory KV Cache at Rack-Scale"
title_zh: "以機櫃級共享記憶體 KV Cache 實現分離式 LLM 服務"
speaker: "Jongryool Kim"
affiliation: "Senior Director / Head of AI System Infra., SK hynix"
type: talk
stage: Compass
date: 2026-08-02
session: "Session 2: AI Systems"
video: "https://www.youtube.com/watch?v=1UrriPJRSPU&t=2219s"
video_range: "00:36:59–00:41:48"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [kv-cache, disaggregated-memory, cxl, inference, rack-scale]
---

# 以機櫃級共享記憶體 KV Cache 實現分離式 LLM 服務(Disaggregated LLM Serving with Shared Memory KV Cache at Rack-Scale)

**一句話總結**:把一台實體上獨立的記憶體池放進機櫃中央,讓多個節點看到**同一段位址空間**,KV cache 就不必再靠 RDMA 在節點間搬來搬去——prefill 寫一次、decode 直接讀,舊的 KV cache 順便留在池裡供下次重用,同時立刻釋放 GPU HBM 並消除 PCIe 爭用。

**One-line summary**: Put a physically disaggregated memory pool in the middle of the rack so multiple nodes see the *same* address space, and the KV cache no longer has to be shuttled between nodes over RDMA — prefill writes once, decode reads directly, the old KV cache stays in the pool for the next request's reuse, and GPU HBM is freed immediately while PCIe contention disappears.

## 中文筆記

### TL;DR

- **兩種模式,他們押注在後者**:這個實體分離的記憶體池支援 (1) **memory pooling**——每個節點動態配置額外記憶體,但區域彼此隔離;(2) **sharing mode**——多個節點看到同一段記憶體位址空間、能存取同一份資料。SK hynix 感興趣的是 sharing。
- **比 RDMA 更快**:一般節點間搬資料會從 TCP/IP 升級到 RDMA,但**基於共享池記憶體的資料共享比 RDMA 更快**。加上 KV cache 一存進池裡就能**立刻釋放 GPU HBM**——prefill 側或 decode 側就算 OOM,prefill 仍能繼續。
- **三重收益**:更快的節點間資料移動、即時釋放 HBM、以及**消除 KV cache 存取在 GPU 側與網路側 PCIe 頻寬上的爭用**。套用到 agentic AI 服務(需要重用大量 KV cache)後,對比 Mooncake 的 KV cache 方案已看到效能提升——但他強調這是非常初步的數字。

### 重點整理

#### 架構:什麼是「實體分離」的記憶體池(約 00:36:59–00:38:50)

Jongryool Kim 是 SK hynix 的 senior director。他要談的是一種新的記憶體形態:**實體上與伺服器分離的池化記憶體(physically disaggregated pool memory)**。

架構圖上是多台伺服器節點,加上一個獨立的記憶體池機箱,**多台伺服器可以同時使用這個記憶體池**,有兩種模式:

1. **Memory pooling**:每個節點可以動態配置額外記憶體,但**各節點的記憶體區域彼此隔離**。
2. **Sharing mode**:多個節點**看到同一段記憶體位址空間**,因此每個節點都能存取同一份資料。

他明說:「我們對 sharing 這個特性非常有興趣。」——這正是整場演講的技術支點。

他們很快就把這個記憶體池整合進 LLM 服務系統,並在去年多場活動上成功部署與展示。示範架構是四台伺服器跑各種 LLM 服務元件,**機櫃中央放一台 Niagara**(約 00:38:45)——那就是真正的實體池化記憶體。

#### KV cache 怎麼流動,以及為什麼會變快(約 00:38:50–00:40:50)

示範場景是用記憶體池來**傳輸 KV cache**:

- 先做 **prefill**;prefill 完成後必須把 KV cache 送到 **decode** 側。透過兩次記憶體操作(**store 與 load**),KV cache 就送到了 decode 節點。
- 關鍵在於:**舊的 KV cache 會留在記憶體池裡**,所以下一個請求可以直接重用,**不需要任何額外的儲存操作**。

結果是相對於全部重新計算(recompute),以及相對於 NIXL 與 in-server DRAM 為基礎的 KV cache 儲存方案,系統效能都有提升。

但他更在意的是「**為什麼**會有這個好處」,他給了三個理由:

1. **更快的節點間資料移動**。一般不會用 TCP/IP,而會用 **RDMA**——RDMA 很快,但**基於池化記憶體的資料共享比 RDMA 更快**(約 00:39:59),所以 LLM 服務系統的效能得以提升。
2. **可以立刻釋放 GPU HBM**(約 00:40:11)。把 KV cache 卸載到池化記憶體之後,HBM 馬上就能還回去。實務意義是:就算 decode 側或 prefill 側發生 out-of-memory,**prefill 仍然可以繼續做**,因為那份 KV cache 已經上傳到池裡了。
3. **消除爭用**。為了儲存與重用 KV cache,GPU 側與網路側的 PCIe 頻寬都會出現大量爭用;用池化記憶體做資料共享傳輸,就能**把這類額外爭用移除**。

#### 套用到 agentic AI 服務,以及接下來要做什麼(約 00:40:50–00:41:48)

Agentic AI 服務的特性是**必須重用大量 KV cache**,所以他們把這套池化記憶體環境套用到 agentic AI 服務系統上,對比 **Mooncake** 的 KV cache 方案量到了效能提升(約 00:41:11)。他自己主動加註:這是**非常初期的效能數字**。

接下來(約 00:41:20):今年年底前,他正與**約 25 個合作方**協作,準備**五套以上的系統 PoC**,包括 **multimodal serving** 與 **runtime memory management**;目標是用池化記憶體打造真正上線的系統,面向 HPC 等級的國家級系統。

結語:「讓我們看看池化記憶體會怎麼改變 AI 系統。」

### 金句

> "This pooled memory based data sharing is faster than RDMA."(約 00:39:59)

這是整套架構的核心賣點——不是「另一種搬資料的方式」,而是比目前最快的搬法更快。

> "We can release the GPU HBM immediately by offloading the key cache to the pool memory."(約 00:40:11)

KV cache 從「佔住 HBM 的負擔」變成「放在池裡的共用資產」。

> "Let's see how the pooled memory can change the AI system."(約 00:41:45)

演講的收尾,也是這條技術路線目前的狀態:方向明確,證據還在累積。

## English Notes

### TL;DR

- **Two modes, and they're betting on the second.** The physically disaggregated pool supports (1) **memory pooling**, where each node dynamically allocates extra memory but regions stay isolated between nodes, and (2) **sharing mode**, where multiple nodes see the same memory address space and can access the same data. Sharing is what SK hynix cares about.
- **Faster than RDMA.** The usual upgrade path for inter-node data movement is TCP/IP → RDMA, but **pooled-memory-based data sharing is faster than RDMA**. And once the KV cache lands in the pool, **GPU HBM is released immediately** — even if the prefill or decode side hits OOM, prefill can keep going.
- **Three compounding benefits**: faster inter-node movement, immediate HBM release, and **elimination of PCIe bandwidth contention** on both the GPU and network side when storing and reusing KV cache. Applied to agentic AI serving — which must reuse large amounts of KV cache — they measured improvement over a Mooncake-based KV cache, with the caveat that these are very early numbers.

### Key Points

#### The architecture: what "physically disaggregated" means here (~00:36:59–00:38:50)

Jongryool Kim is a senior director at SK hynix, and his subject is a new memory form factor: **physically disaggregated pooled memory** — a memory box that sits apart from the servers themselves.

In the diagram: several server nodes plus a separate memory-pool box that **multiple servers use simultaneously**, in one of two modes:

1. **Memory pooling** — each node dynamically allocates additional memory, but each node's region is **isolated from the others**.
2. **Sharing mode** — multiple nodes **see the same memory address space**, so every node can access the same data.

"We are very interested in this sharing feature," he said plainly — and that's the technical pivot for the whole talk.

They integrated the pool into an LLM serving system quickly and demonstrated the deployment at several events last year. The demo has four servers running LLM serving components, with a **Niagara box in the middle of the rack** (~00:38:45) as the actual physical pooled memory.

#### How the KV cache flows, and why it gets faster (~00:38:50–00:40:50)

The demo scenario uses the pool to **transfer the KV cache**:

- Run **prefill** first; once prefill completes, the KV cache must be delivered to the **decode** side. Two memory operations — a **store** and a **load** — deliver it to the decode node.
- The important part: **the old KV cache stays in the memory pool**, so the next request can reuse it directly with **no additional store operation at all**.

The result is a performance improvement over full recomputation, and over NIXL and in-server DRAM-based KV cache storage.

But he was more interested in **why** the benefit exists, and gave three reasons:

1. **Faster inter-node data movement.** People generally use **RDMA** rather than TCP/IP, and RDMA is fast — but **pooled-memory-based data sharing is faster than RDMA** (~00:39:59), which is where the serving-system speedup comes from.
2. **GPU HBM can be released immediately** (~00:40:11) once the KV cache is offloaded to the pool. The practical consequence: even if the decode side or the prefill side runs out of memory, **prefill can continue**, because that KV cache is already uploaded to the pool.
3. **Contention disappears.** Storing and reusing the KV cache creates heavy contention on PCIe bandwidth on both the GPU side and the network side; routing the transfer through pooled-memory data sharing **removes that additional contention**.

#### Applying it to agentic AI serving, and what's next (~00:40:50–00:41:48)

Agentic AI serving is characterized by having to reuse a **large amount of KV cache**, so they applied the pooled-memory environment to an agentic AI serving system and measured improvement against a **Mooncake** KV cache (~00:41:11). He volunteered the caveat himself: these are very initial performance numbers.

Looking ahead (~00:41:20): by the end of this year, working with roughly **25 collaboration parties**, they are preparing **five more system PoCs**, including **multimodal serving** and **runtime memory management**, aiming to build a real system with pooled memory for HPC-class national systems.

His closing line: "Let's see how the pooled memory can change the AI system."

### Quotes

> "This pooled memory based data sharing is faster than RDMA." (~00:39:59)

The core claim: not an alternative way to move data, but a faster one than today's fastest.

> "We can release the GPU HBM immediately by offloading the key cache to the pool memory." (~00:40:11)

The KV cache stops being an HBM tax and becomes a shared asset sitting in the pool.

> "Let's see how the pooled memory can change the AI system." (~00:41:45)

The talk's closing line, and a fair summary of where the approach stands: direction clear, evidence still accumulating.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Niagara (SK hynix) | 放在機櫃中央的實體池化記憶體裝置,支援 pooling 與 sharing 兩種模式 | SK hynix's physical pooled-memory box placed mid-rack, supporting both pooling and sharing modes | 已查證:SK hynix 的 CXL 分離式記憶體原型(多埠、支援 memory pooling / sharing);演講未明說 CXL |
| Mooncake | 對照組:以 KV cache 為中心的分離式服務架構與其快取層 | Comparison baseline: KVCache-centric disaggregated serving architecture and its cache layer | 逐字稿 "moonake" |
| NIXL | 對照組之一,推論資料傳輸函式庫 | One of the comparison baselines; an inference data-transfer library | 逐字稿 "nxl";名稱待確認 / to verify |
| TraCT | 與本講題幾乎同名的論文:*Disaggregated LLM Serving with CXL Shared Memory KV Cache at Rack-Scale* | Paper with nearly the same title: *Disaggregated LLM Serving with CXL Shared Memory KV Cache at Rack-Scale* | arXiv 2512.18194;演講中未提及名稱,關聯性待確認 / not named on stage, relationship to verify |
| RDMA | 目前節點間資料搬移的主流做法,作為效能對照基準 | The prevailing approach to inter-node data movement, used as the performance reference point | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Jang R Kim / Junior Kim | Jongryool Kim |
| skinex / SKH Highix | SK hynix |
| Rexcale | rack-scale |
| disegregated / disagregated | disaggregated |
| prepare / prefare | prefill |
| keeper cache / cuber cache / key cache | KV cache |
| GPU HPM | GPU HBM |
| realm serving / random serving | LLM serving |
| moonake | Mooncake |
| nxl | NIXL(待確認 / to verify) |
| niagara | Niagara |
| five more system PC | five more system PoCs |
| multimord serving | multimodal serving |
| relate the GPU HPM | release the GPU HBM |

## 待確認 / To Verify

- 逐字稿的 "nxl and nm cache is in server DM based cable cash stoing" 判讀為「NIXL 與 in-server DRAM based KV cache storing」,但 "nm cache" 也可能是另一個專案名,需看投影片。/ The comparison baselines heard as "nxl and nm cache" — read as NIXL and in-server DRAM-based KV cache storage, but "nm cache" could be another project name.
- 講者自述「I also working for the SRC as a cell」——SRC 疑為 Semiconductor Research Corporation,職稱不明。/ He said he also works for "the SRC" in an unclear role; possibly Semiconductor Research Corporation.
- 最後提到的國家級系統:逐字稿為 "for the HPC US-based national system",究竟是美國或韓國的國家級系統待確認。/ The national-scale system mentioned at the end — whether US or Korean is unclear from the transcript.
- 對比 Mooncake 的效能提升幅度未在逐字稿中出現具體數字。/ No concrete numbers for the improvement over Mooncake appear in the transcript.
- Niagara 是 CXL 裝置,但演講逐字稿中未出現 "CXL" 一詞;此資訊來自外部查證。/ Niagara is a CXL device, but "CXL" never appears in the transcript; that detail comes from external verification.
