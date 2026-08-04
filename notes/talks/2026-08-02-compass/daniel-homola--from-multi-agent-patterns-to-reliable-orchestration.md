---
title: "From Multi-Agent Patterns to Reliable Orchestration"
title_zh: "從多 Agent 模式到可靠的協調"
speaker: "Daniel Homola"
affiliation: "Lead AI Engineer, BMW Research"
type: talk
stage: Compass
date: 2026-08-02
session: "Session 3: Enterprise AI"
video: "https://www.youtube.com/watch?v=1UrriPJRSPU&t=4470s"
video_range: "01:14:30–01:20:35"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [enterprise, multi-agent, orchestration, evaluation, automotive]
---

# 從多 Agent 模式到可靠的協調(From Multi-Agent Patterns to Reliable Orchestration)

**一句話總結**:handoff、agents-as-tools、routing 這些協調模式最後都收斂到同一個 runtime 決策——「這件事該由誰來做」;可靠的多 agent 系統來自把這個 delegation 決策做得可量測、脈絡感知,並接受它常常沒有唯一正確答案。
**One-line summary**: Handoffs, agents-as-tools, and routing all collapse into the same runtime decision — who should handle this piece of work — so reliable multi-agent systems come from making that delegation decision measurable, context-aware, and tolerant of the fact that there is often more than one right answer.

## 中文筆記

### TL;DR

- **模式只是接線方式,真正的問題是 delegation 決策**。handoff(控制權轉移)、agents as tools(orchestrator 委派並等結果)、routing(classifier 把每一輪分派給專家)——每家企業取的名字不同,但底層都是同一個 runtime choice。
- **Agent delegation ≠ tool selection**。Tool selection 通常拿單一 ground-truth label 來評;但 agent delegation 的**重疊是常態**(多個 agent 都能完成同一個任務),而且判準還包含成本、延遲與使用者體驗。
- **就算實作成 tool call,agent 也不是 tool**:tool call 是有界的,agent delegation 是**無界的**——委派出去等於啟動另一個自主迴圈,它可能推理、反問、卡住、稍後恢復,或永遠不乾淨地返回。
- **因此評估不能只問「最後任務有沒有成功」**:要看路徑是否合理、成本、延遲、使用者體驗;benchmark 應該允許多個可接受的正確選擇,並附帶完整 runtime context。

### 重點整理

#### 用車內語音助理把問題具體化(約 01:15–01:16)

講者背景是 agent 架構(給客戶產品的系統層架構)與 **GUI agent / computer use agent**——像使用者一樣操作螢幕的 agent。(他提到去年在 AI Engineer 研討會有一場談 GUI agent 典範動機的演講,可供延伸。)

他用**車內多 agent 語音助理**當作貫穿全場的例子,裡面有三個 agent:navigation agent(找路線)、car control agent(操作車窗、座椅、空調),以及 GUI agent(透過螢幕操作應用程式)。它們之上是 orchestrator,負責協調執行、有時合併結果。

他的核心主張是:**協調真正難的地方不是模式、不是怎麼在 agent 之間傳遞東西,而是在不斷變動的脈絡下,反覆做出可靠的 delegation 與協調決策。** 常見模式看起來很多——handoff 是控制權轉移給另一個 agent;agents as tools 是 orchestrator 把工作委派給專門 agent 並等待結果;routing 是 classifier 或 router 把每一輪分派給專家——但每家企業各有各的命名,本質是同一件事:**選擇**。

#### 為什麼這不是普通的 tool selection(約 01:17–01:18)

聽起來像是一般的工具選擇,但不是,原因有二:

**一、重疊是常態,ground truth 不唯一。** Tool selection 通常對著單一標準答案評分;但在 agent delegation 裡,「在這個脈絡下誰該處理這件事」常常有多個 agent 都做得到——例如 GUI agent 幾乎能覆蓋其他 agent 的範圍。而且選擇的判準還包含**成本、延遲、以及你想給駕駛或乘客的使用者體驗**。

他的例子:使用者說「play some jazz」。如果螢幕是空的,呼叫 media API 可能最好;但如果螢幕上已經有一首歌或一份播放清單,直接點下去也是完全有效的選擇。相對地,「navigate me to Munich」就很明確屬於 navigation agent。**可靠的系統不該把這種情況硬塞進單一 canonical label,而要用 runtime context 去適應。**

**二、agent 的委派是無界的。** 就算實作成一次 tool call,agent 也不是 tool:**tool call 是有界的,agent delegation 是無界的**。把工作交給另一個 agent,等於啟動一個自主迴圈——它可能推理、要求澄清、卡住、稍後恢復,或永遠不乾淨地返回。所以協調不只是「選能力」,更是在決定**什麼時候放手讓另一個迴圈接管控制權是安全且有用的**。

#### 對評估與組織的意涵(約 01:19–01:20)

既然存在多條有效軌跡,benchmark 就不該只問「最終任務是否成功」,而要納入**路徑是否合理、成本、延遲、想提供的使用者體驗**;資料集也要帶上完整的 runtime context,指標則視情境而定(有時最佳化延遲,有時最佳化人機協作)。

在企業裡怎麼落地:他建議**每個擁有某個 agent 的團隊各自建自己的 benchmark**,然後把多個團隊的 benchmark 組合起來,形成一個涵蓋協作與協調模式的**共享 orchestration / delegation benchmark**。

收尾:模式只是把多 agent 系統的各部分接起來的手段。真正重要的是讓協調路徑與委派決策**可量測、脈絡感知、可靠**。三個要一直問下去的問題:**誰來處理這件事?他們該一起走哪條路?我們怎麼知道結果是好的?**

### 金句

> "A tool call is bounded and the agent delegation is unbounded. So basically delegating to an agent can start an autonomous loop."(約 01:18)

這是「agent 不是 tool」最精確的一句話——差別在控制權是否會回來。

> "The patterns are just the means to connect the pieces of the multi-agent system. What matters is making orchestration paths and delegation decisions measurable, context-aware, and reliable."(約 01:20)

整場演講的結論。

## English Notes

### TL;DR

- **Patterns are just wiring; the real problem is the delegation decision.** Handoff (control transfers to another agent), agents-as-tools (the orchestrator delegates and waits for a result), and routing (a classifier dispatches each turn to a specialist) all reduce to the same runtime choice, whatever each enterprise calls it.
- **Agent delegation is not tool selection.** Tool selection is typically evaluated against one ground-truth label; in agent delegation **overlap is normal** — several agents can legitimately complete the same task — and the criteria include cost, latency, and the user experience you want to deliver.
- **Even implemented as a tool call, agents are not tools**: a tool call is bounded, agent delegation is **unbounded**. Delegating starts an autonomous loop that may reason, ask for clarification, get stuck, resume later, or never return cleanly.
- **So evaluation can't just ask whether the final task succeeded**: it also has to weigh whether the path was reasonable, plus cost, latency, and experience — and benchmarks should admit multiple acceptable choices with full runtime context attached.

### Key Points

#### Grounding the problem in an in-car voice assistant (~01:15–01:16)

His background is agent architecture — system-level architecture for customer-facing agentic products — and **GUI agents (computer-use agents)** that operate screens the way users do. (He points to a talk he gave last year at the AI Engineer conference on why an enterprise would consider GUI agents at all.)

The running example is a **multi-agent in-car voice assistant** with three agents: a navigation agent for routing, a car control agent for windows, seats, and climate, and a GUI agent that drives applications through the screen. Above them sits an orchestrator that coordinates execution and sometimes combines results.

His thesis: **the hard part of orchestration is not the patterns or how you shuttle state between agents — it's making the delegation and coordination choices well, repeatedly, at runtime, under constantly changing context.** The pattern zoo looks large — handoff transfers control to another agent; agents-as-tools has the orchestrator delegate to a specialist and wait; routing dispatches each turn via a classifier — and every enterprise names them differently, but underneath it's the same thing: **a choice**.

#### Why this isn't ordinary tool selection (~01:17–01:18)

**First, overlap is normal and ground truth isn't singular.** Tool selection is usually scored against a single correct label. But for "who should handle this work in this context," multiple agents often can — the GUI agent in particular overlaps nearly everything — and the criteria extend to **cost, latency, and the experience you want to give the person in the driver's or passenger's seat**.

His example: the user says "play some jazz." With an empty screen, the media API may be the best route; but if a song or playlist is already on screen, tapping it is an equally valid choice. Contrast that with "navigate me to Munich," which unambiguously belongs to the navigation agent. **A reliable system shouldn't force these cases into one canonical label — it should use runtime context and adapt.**

**Second, delegation is unbounded.** Even when implemented as a tool call, agents are not tools: **a tool call is bounded; agent delegation is unbounded.** Delegating starts an autonomous loop that may reason, ask for clarification, get stuck, resume later, or never return cleanly. So orchestration isn't just selecting a capability — it's deciding **when it's safe and useful to let another loop take over effectively unbounded control**.

#### Consequences for evaluation and org design (~01:19–01:20)

Because multiple valid trajectories exist, a benchmark shouldn't only ask whether the final task succeeded. It has to account for **whether the path was reasonable, plus cost, latency, and intended user experience**; datasets need the full runtime context attached, and the metric depends on the situation — sometimes you optimize latency, sometimes human-machine collaboration.

For enterprises, his suggestion is organizational: **each team that owns an agent builds its own benchmark**, then teams combine those benchmarks into a **shared orchestration and delegation benchmark** that also covers collaboration and coordination patterns.

Closing: patterns are just the means of connecting pieces. What matters is making orchestration paths and delegation decisions measurable, context-aware, and reliable — so keep asking **who handles this work, what path should they take together, and how do we know it was good?**

### Quotes

> "A tool call is bounded and the agent delegation is unbounded. So basically delegating to an agent can start an autonomous loop." (~01:18)

The sharpest formulation of why agents aren't tools: the question is whether control comes back.

> "The patterns are just the means to connect the pieces of the multi-agent system. What matters is making orchestration paths and delegation decisions measurable, context-aware, and reliable." (~01:20)

The thesis of the talk in one sentence.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| 車內多 agent 語音助理 / In-car multi-agent voice assistant | 貫穿全場的例子:navigation / car control / GUI agent + orchestrator | The running example: navigation, car control, and GUI agents under an orchestrator | BMW Research 情境,未點名為出貨產品 / a BMW Research scenario; not named as a shipping product |
| 講者去年在 AI Engineer 研討會的 GUI agent 演講 / His AI Engineer conference talk on GUI agents | 說明企業為何要考慮 computer use agent 這條路線 | Motivates why an enterprise would adopt the GUI/computer-use agent paradigm | 講題與連結待確認 / exact title and link to verify |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Daniel Humla | Daniel Homola |
| aent / aentic | agent / agentic |
| rooting / rooter | routing / router |
| GU agent | GUI agent |
| engine delegation | agent delegation |

## 待確認 / To Verify

- 講者去年在 AI Engineer 研討會那場 GUI agent 演講的確切講題與連結。/ Exact title and link for his GUI-agent talk at last year's AI Engineer conference.
- 車內語音助理範例是研究原型還是已出貨的 BMW 功能,逐字稿未說明。/ Whether the in-car assistant example is a research prototype or a shipped BMW feature.
- 「每個團隊各建 benchmark 再組合成共享 benchmark」是否已在 BMW 內部實行,或僅為提議。/ Whether the per-team-benchmark composition model is already in practice at BMW or a proposal.
