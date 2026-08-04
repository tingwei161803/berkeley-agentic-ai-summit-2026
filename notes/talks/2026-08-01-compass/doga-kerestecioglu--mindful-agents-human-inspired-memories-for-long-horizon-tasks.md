---
title: "Mindful Agents: Human-Inspired Memories for Long-Horizon Tasks"
title_zh: "Mindful Agents:給長程任務的人類啟發式記憶"
speaker: "Doga Kerestecioglu"
affiliation: "Principal Applied Scientist, Microsoft Corporation"
type: talk
stage: Compass
date: 2026-08-01
session: "Session 3: Foundational Capabilities"
video: "https://www.youtube.com/watch?v=AO0RXP-fVZQ&t=7202s"
video_range: "02:00:02–02:10:10"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [memory, long-horizon, evaluation, streaming-data, agent-infrastructure]
---

# Mindful Agents:給長程任務的人類啟發式記憶(Mindful Agents: Human-Inspired Memories for Long-Horizon Tasks)

**一句話總結**:Agent 沒有人類的儲存限制,反而喪失了「蒸餾記憶」的能力;Microsoft Fabric AI 團隊借用人腦的記憶生命週期(攝取 → 固化 → 遺忘 → 檢索 → 再固化)為長時間執行的串流資料 agent 建記憶,並主張這類系統必須用「保留 / 檢索 / 任務完成」三層 eval 才測得準。
**One-line summary**: Agents have no storage constraint, and that is exactly why they never learned to distill; Microsoft's Fabric AI team borrows the human memory life cycle — ingest, consolidate, forget, retrieve, reconsolidate — to build memory for long-running agents over high-volume streaming data, and argues such systems need three distinct layers of evaluation: retention, retrieval, and task completion.

## 中文筆記

### TL;DR

- **人類記憶好用是因為有限制**:坐火車經過無盡的田野,我們不會記得每一根草,只記得「有意思」的東西——這種蒸餾能力是儲存限制逼出來的演化結果。Agent 沒有這個壓力,於是把所有 trace 都記下來、再摘要摘要再摘要,在需要精確回溯時就崩了。
- **記憶不是儲存,是一條回饋迴路**:ingestion → consolidation(去重合併,類似睡眠)→ forgetting(衰減與干擾)→ retrieval(冷儲存圖譜 + 即時串流混合)→ maturation / reconsolidation(處理新舊記憶衝突)。關鍵是 consolidation 的節奏是**領域相關而非固定時間**的。
- **記憶系統要分三層測**:retention(留下來的東西真的重要嗎,需要標註)、retrieval(建好的記憶能不能撈得出來)、task completion(最貴但最重要——記憶再好,agent 在 harness 裡選擇忽略它就沒用)。

### 重點整理

#### 問題設定:agent 的記憶跟人不一樣(約 02:00–02:02)

講者來自 **Microsoft Fabric AI 團隊**,做的是 real-time intelligence 場景下的長時間執行 agent——資料是高流量的串流資料。

她用一個對照切入:人類有儲存限制,而這個限制**讓我們更擅長蒸餾記憶**。她最近在歐洲搭火車,窗外是無止盡的田野、風車、吃草的動物;我們沒有能力記住每一根草,但我們很擅長只留下可能跟自己有關的有趣片段——這是演化訓練出來的能力。

Agent 沒有這個問題:儲存相對便宜,可以記下每一個 bit、每一條 trace。目前的常見做法是「capture → retrieve → 摘要 → 保留摘要」,於是最後拿在手上的是**摘要的摘要的摘要**。多數情況下堪用,但一旦要檢索非常具體的東西就會失效——而他們要的正是能主動(proactive)處理大量資料的 agent。

#### 記憶生命週期:一條回饋迴路(約 02:02–02:05)

他們把記憶做成一個 **memory life cycle feedback loop**:

1. **Ingestion**:從 observability substrate 攝取全部資料。
2. **Consolidation**:去重、合併,把記憶整理成穩定的候選——概念上類似人的睡眠。但關鍵差異是:**agent 的固化週期是領域相關的,不一定跟時間對齊**。她舉 Formula 1 的例子:比賽當下的 telemetry、賽後、休賽週、整個賽季,四種節奏完全不同。所以「不必然是每天固化一次,但一定要以某種 batch、某種 cadence 處理」。
3. **Forgetting**:透過 decay 與 interference,確保重要的留下、不重要的盡量被忘掉。
4. **Retrieval**:混合式——已知領域的穩定記憶放冷儲存並組織成 graph,同時還有即時進來的串流資料;agent 必須能同時存取兩者,並判斷此刻該用哪一段記憶。
5. **Maturation / Reconsolidation**:檢索時**一定會遇到衝突**(新事件牴觸已固化的舊記憶)。這時要決定:更新圖上的既有 entity、新增一個 entity(確實是重要新資訊)、還是直接丟棄這筆即時資料(它是錯的)。不能無腦一直往圖裡加,否則圖會難以檢索。

#### 評估:天花板、地板,與三層 eval(約 02:05–02:09)

她給了兩個評估案例,分別代表最好與最壞的情境:

- **Retention benchmark(較確定性的一端)**:系統對「什麼重要」有清楚標註。他們調的是固化的頻率與批量,結果在**大約 200 個事件一批**時開始穩定;再疊上遺忘機制,precision 會更好。
- **Retrieval benchmark(較困難的一端)**:用 **LongMemEval**,對話資料、沒有重要性標註——這其實不是他們最理想的場景(他們的假設是「重複執行任務的領域專家」能學出什麼重要),但仍可用來調「壓縮多少 / 最佳儲存大小是多少而不破壞資訊」,本質是壓縮率與準確率的取捨。

由此歸納出記憶系統需要的**三種 eval**:

1. **Retention**:留下的東西是不是真的重要?可以做成快速、確定性的 eval,但需要標籤(他們也有很多工作在改善標籤品質)。
2. **Retrieval**:記憶建得好,還要撈得出來。難以導航的記憶體系「必要但不充分」。
3. **Task completion**:離使用者最近,**最重要也最貴**。你可能給了 agent 最好的記憶,但取決於它在 harness 裡怎麼被暴露,agent 仍可能選擇忽略、任務照樣失敗。長程 agent 的這類 eval 建置與執行成本都很高。

#### 結論與下一步(約 02:09)

- **Logs are not memories.** 長程 agent 需要的不只是可取用的 trace;在這種資料量下要有效率,就必須決定什麼留、什麼不留。
- **領域很重要,而且需要事先宣告**。runtime 才推斷領域會直接影響效率與準確率。
- 下一步:與 **Microsoft Foundry** 團隊合作做端到端 eval;以及 domain learning 與 **graph ontology** ——他們發現圖結構與 ontology 的設計方式,對準確率的影響不亞於前述各個元件。

### 金句

> "Logs are not memories."(約 02:08)

一句話戳破「把所有 trace 存下來就等於有記憶」的錯覺。

> "You might give the best memory to the agent and depending on how it's exposed to the agent in your harness, the agent might choose to ignore it and still might not accomplish the task."(約 02:08)

這就是為什麼 task completion eval 貴也得做——記憶品質與任務成功之間並不是等號。

## English Notes

### TL;DR

- **Human memory works *because* it is constrained.** On a train through endless European fields you don't remember every blade of grass — you remember what might matter to you. That distillation is an evolved response to a storage limit. Agents have no such limit, so they log everything and then summarize summaries of summaries, which breaks down the moment you need something specific.
- **Memory is a feedback loop, not a store**: ingestion → consolidation (dedup/merge, the "sleep" analogue) → forgetting (decay and interference) → retrieval (cold-storage graph *plus* live stream) → maturation/reconsolidation to resolve conflicts. Crucially, consolidation cadence is **domain-dependent, not necessarily temporal**.
- **Three separate evals are required**: retention (is what you kept actually important? needs labels), retrieval (can you get it back out?), and task completion (closest to the user, most expensive, most important — the best memory is worthless if the harness lets the agent ignore it).

### Key Points

#### The setup: agents don't have our constraints (~02:00–02:02)

The speaker is on the **Microsoft Fabric AI team**, working on long-running agents in the real-time intelligence space — high-volume streaming data.

Her framing contrast: human storage constraints are what make humans *good* at distilling memory. Agents get to log every bit and every trace cheaply, so the default pattern becomes capture → retrieve → summarize → keep the summary, recursively. Fine for most cases, but it fails exactly when you need to retrieve something specific — which is what proactive agents over large data volumes need.

#### The memory life cycle (~02:02–02:05)

Five stages, run as a feedback loop:

1. **Ingestion** from the observability substrate.
2. **Consolidation** — dedup and merge into stable candidate memories, loosely analogous to sleep. The difference from humans: consolidation cycles are **domain-dependent and may not be temporal at all**. Her Formula 1 example: race-day telemetry, post-race, off-week, and full-season each imply a different cadence. It need not be daily, but it must happen in some batch at some cadence.
3. **Forgetting** via decay and interference, so the important survives and the rest doesn't.
4. **Retrieval** — hybrid: stable memories live in cold storage organized as a graph for a known domain, while live data keeps streaming in. The agent must reach both and pick the right memory for the moment.
5. **Maturation / reconsolidation** — retrieval *will* surface conflicts between new events and settled memories. The decision is whether to update an existing graph entity, add a new one, or discard the incoming live data as erroneous. Blindly appending makes the graph unretrievable.

#### Evaluation: the ceiling, the floor, and three layers (~02:05–02:09)

Two studies bracketing best and worst case:

- **Retention benchmark** (deterministic end): clean labels for what matters. They tuned consolidation batch size and frequency; things stabilized around **200 events per batch**, with precision improving further once forgetting was layered on.
- **Retrieval benchmark** using **LongMemEval** (hard end): conversational data with no importance labels — not the ideal shape for their domain-expert-doing-repeated-tasks setting, but usable for tuning how much to compress and what the optimal storage size is before compression becomes destructive. It's a compression/accuracy trade-off.

Generalizing, memory work needs three kinds of eval:

1. **Retention** — quick and deterministic, but label-dependent; they have ongoing work on getting better labels.
2. **Retrieval** — necessary but not sufficient: a memory store that's hard to navigate is a memory store you can't use.
3. **Task completion** — closest to the user and therefore the most important, and by far the most expensive to build and run for long-running agents. The harness mediates whether the agent even uses the memory you gave it.

#### Takeaways and what's next (~02:09)

- **Logs are not memories.** At this data volume, efficiency forces you to decide what to keep.
- **Domain matters and needs to be pre-declared**; inferring it at runtime costs you both efficiency and accuracy.
- Next: end-to-end evals with the **Microsoft Foundry** team, plus work on domain learning and **graph ontology** — how you structure the graph and its ontology turns out to affect accuracy as much as any of the individual components.

### Quotes

> "Logs are not memories." (~02:08)

The cleanest rebuttal to "we store all the traces, so we have memory."

> "You might give the best memory to the agent and depending on how it's exposed to the agent in your harness, the agent might choose to ignore it and still might not accomplish the task." (~02:08)

Why the expensive task-completion eval is unavoidable: memory quality does not equal task success.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Microsoft Fabric (Real-Time Intelligence) | 講者所屬團隊,長時間執行 agent 處理高流量串流資料的場景 | Speaker's team; long-running agents over high-volume streaming data | |
| LongMemEval | 評估聊天助理長期互動記憶的 benchmark,用於他們的 retrieval 評估 | Benchmark for long-term interactive memory in chat assistants; used for their retrieval eval | arXiv 2410.10813,ICLR 2025 |
| Microsoft Foundry | 合作進行端到端 agent eval 的團隊 | Partner team for end-to-end agent evaluation | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| DOA | Doga (Kerestecioglu) |
| long map eval | LongMemEval |
| ddup | dedup |
| reconolidation | reconsolidation |
| longunning | long-running |
| in state bunch | 語意不明,疑為 "in that space" 之類 / unclear, likely a mis-transcription |

## 待確認 / To Verify

- Consolidation 穩定的批量:講者先說 500 events,隨即自我更正為 **200 events at a time**(現場說看不清投影片)。以 200 為準,但值得看影片畫面確認。/ She first said 500 events, then corrected herself to 200 — worth checking the slide.
- 「we're working with the foundry Microsoft foundry team on end to end evals uh in state bunch」——後半句字幕不可解,實際措辭待確認。/ The tail of this sentence is garbled in the auto-captions.
- 這套記憶系統是否有公開的專案名稱或論文(逐字稿中未提及)。/ Whether the memory system has a public project name or paper — not mentioned in the talk.
