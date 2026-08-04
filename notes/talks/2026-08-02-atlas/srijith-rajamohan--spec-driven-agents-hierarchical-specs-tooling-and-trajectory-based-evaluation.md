---
title: "Spec-Driven Agents: Hierarchical Specs, Tooling, and Trajectory-Based Evaluation"
title_zh: "Spec 驅動的 agent:階層式規格、工具設計與基於軌跡的評估"
speaker: "Srijith Rajamohan"
affiliation: "Head of AI Research, Redis"
type: talk
stage: Atlas
date: 2026-08-02
session: "Session 2: Agent Evaluation & Benchmarks"
video: "https://www.youtube.com/watch?v=-7AJJLwYW1Q&t=2378s"
video_range: "00:39:38–00:50:09"
transcript: "tmp/[English (auto-generated)] Atlas Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [evaluation, trajectory, tool-design, knowledge-organization, reliability]
---

# Spec 驅動的 agent:階層式規格、工具設計與基於軌跡的評估(Spec-Driven Agents: Hierarchical Specs, Tooling, and Trajectory-Based Evaluation)

**一句話總結**:替 Redis Query Engine 建診斷 agent 的實戰經驗——真正把指標推動的不是換更強的模型,而是重組工具(setup vs discretionary)與知識(診斷 playbook = router + handbooks);而且大多數失敗模式只有看軌跡才看得見,看最終答案完全看不出來。
**One-line summary**: Lessons from building a diagnostic agent for the Redis Query Engine — what moved the needle wasn't a stronger model but restructuring the tools (setup vs. discretionary) and the knowledge (a diagnostic playbook of router plus handbooks); and most failure modes are invisible in the final answer and only show up in the trajectory.

## 中文筆記

### TL;DR

- **軌跡比最終答案重要**:他們看到的多數失敗模式(重複讀取、回頭、死路搜尋、不一致)在最終結果上完全看不出來,只有檢查 trajectory 才能發現;而且低效軌跡不只浪費 token,還因為 context 耗盡而**反過來拉低正確率**。
- **工具不是越多越好**:把工具拆成 **setup tools(啟動時一定呼叫)** 與 **discretionary tools(模型視問題自行決定)**;把一部分工具移到啟動階段,等於強制一次「新人 onboarding」,讓模型在解題時面對的選擇集變小,**軌跡一致性顯著提升**。
- **tool overload 是真的**:他們的 full 工具集是 minimal 的超集(多了現成的便利工具),結果**更慢、品質還略差**。真正重要的是 **tool orthogonality / separability**——只要 agent 分不清該叫 B 還是 C,就是問題。
- **知識重組成 diagnostic playbook**(router + handbooks,router 把 symptom 映到 problem type 再路由到 handbook):相較直接讀原始文件,全面改善,**token 總量降 43%、總錯誤率降 48%**,連指令遵循都變好。
- 一句金句:「唯一比一個不能用的系統更糟的,是一個偶爾能用的系統。」正確性重要,**一致性同樣重要**。

### 重點整理

#### 問題背景:Redis Query Engine 的診斷與修復 agent(約 00:40–00:41)

他們替 Redis Query Engine 建了一個 AI 診斷與修復 agent,主要服務對象是客戶支援團隊。Redis 本身有相當完整的工具與文件,但實際情況是**很多複雜查詢最後一路升級到開發團隊**,顯然不是可持續的做法;這個 agent 的目標就是攔下其中一大部分,縮短客戶的 time-to-solution。

技術上的困難在於:**不像 SQL,LLM 對 Redis 查詢的參數化知識(parametric knowledge)相當有限**,而且經常出錯;加上許多查詢本身高度依賴上下文——agent 必須判斷「這個查詢缺了什麼」。因此他們建的是一個帶 skills 與 tools、跑 **clarify → diagnose → confirm** 迴圈的 agent,以換取可靠性。

#### 學到的第一課:最終結果不夠看(約 00:41–00:43)

三個觀察:

1. **只評最終結果往往不足**——「怎麼走到那裡」的軌跡影響很大。
2. **正確性重要,一致性同樣重要**。他的說法是:「唯一比一個不能用的系統更糟的,是一個只是偶爾能用的系統。」
3. **低效的 Redis 查詢本身很貴**,而他們吃了一次苦頭才發現:這些低效軌跡在下游也更容易出錯,原因是長度/context 耗盡。

換更前沿、更強的模型當然能解掉一部分問題,但**真正推動指標的是重組知識、以及重組 agent 取用資訊的方式**——確保 agent 有足夠資訊知道如何辨識、如何取用、以及何時該用。

#### 四類失敗模式(約 00:42–00:44)

前三類關於最終結果,第四類關於軌跡:

- **Correctness**:結果錯誤。可能是路徑錯、讀錯指標等,本質是 hallucination。
- **Completeness**:只診斷出問題的一部分,其他未解——這是他們最常遇到的問題之一。
- **Usefulness**,又分兩種:
  - 給了**太多或太籠統**的資訊,使用者被資訊淹沒,實際上不可行動。
  - 給的建議**違反語意意圖**——他舉的例子很精準:使用者問「我的查詢為什麼慢」,agent 回「減少搜尋詞的數量」。技術上正確,但完全沒有服務到使用者的目的。
- **Efficiency**:重複讀取、回頭、死路搜尋,浪費 token;而且如前所述,**這也會負面影響正確率**。

他強調:**這些多半只有看軌跡才會浮現,在最終結果裡看不到。**

#### 介入一:工具架構——setup tools vs discretionary tools(約 00:44)

第一個維度是重新檢視 tool architecture。他們把工具分成兩類:

- **Setup tools**:啟動時一律呼叫。
- **Discretionary tools**:由模型依當下問題自行決定呼叫。

他用的比喻很好懂:就像你到一個新職位會先經歷 onboarding——有人告訴你這裡發生什麼事、誰負責什麼、該找誰。**setup tools 就是這段 onboarding**,提供足夠 context 讓 agent 知道如何正確前進、正確使用 discretionary tools、以及何時該用。

#### 介入二:把知識組織成 diagnostic playbook(約 00:44–00:45)

第二個維度是知識庫的組織方式。可以直接餵原始文件,但他們發現重組成 **diagnostic playbook** 效果更好。playbook 就是 **一個 router + 一組 handbooks**:router 的結構是「symptom → problem type → 路由到某個或某組 handbook」。

他點出一個關鍵的使用者行為事實:**使用者不會拿著「症狀」來找你,他們拿的是「困擾」。把困擾映射到症狀是 agent 的工作,而讓 agent 容易做到這件事是我們的工作。** playbook 就是為此存在。

#### 實驗結果(約 00:45–00:48)

兩個介入分開評估,量測 end-to-end latency、tool call 次數、與結果品質。

**工具架構**:

| 設定 Setup | 說明 | 結果 |
|---|---|---|
| Baseline | 自動生成的工具集 | 慢,品質可議 |
| Minimal | 由領域知識設計的最小工具集 | 基準 |
| Full | minimal 的**超集**(例如除了 `get_shard_info`,再加上現成的 `get_slowest_shard`) | **沒有更好——更慢,品質還略差** |
| Setup tools | 就是 minimal,但把一部分工具移到啟動時呼叫 | 總指標與 minimal 相近,但**軌跡一致性明顯較佳** |

他從 full 的結果導出兩個結論:**tool overload 確實存在**,而且更重要的是 **tool orthogonality(或說 separability)很關鍵——只要 agent 在某個時點無法判斷該呼叫 B 還是 C,就是問題**。

setup tools 與 minimal 在總指標上相近,直到他們**鑽進軌跡本身**:沒有 setup tools 的 minimal,軌跡遠遠更不一致,出現多得多的獨特序列。當然不是每個獨特序列都有問題,但其中一些會是。**結論:減少 LLM 在任一時點需要做的決策,就能降低變異、提升一致性**;setup tools 透過強制一段 onboarding context 達成這件事。

**知識組織(playbook vs 原始文件)**,分兩組指標:
- 答案品質:answer grounding、specificity
- 軌跡品質:first-pass success、dead-end rate

結果**全面改善**,並且 **token 總量下降 43%**、**總錯誤率下降 48%**;最後一列顯示連**指令遵循**也變好了。他的總結是:**讓 agent 更容易取用資訊,不只降低成本,也降低「遺忘」,因而提升可靠性。**

#### 未竟與收尾(約 00:48–00:50)

還有沒做好的地方。他點名 **recursive self-improvement**(本次峰會的共同主題之一)是很適合套用在這裡的方向,可望再往上推;但目前已經看到多數常見失敗模式減少。

三個帶走的重點:

1. **量測軌跡,不只量測最終答案**——他們看到的許多問題根本不會出現在最終結果裡。
2. **盡可能把知識結構化**,讓 agent 容易辨識與取用。
3. **檢視你的工具**,分清楚哪些是**必備的 baseline context**、哪些是**可自行斟酌的探索性 context**。

最後一句:如果你能同時做到結果的 correctness、completeness、usefulness,加上有效率的軌跡,你的 agent 就更有機會達到 production 級的可靠度。

### 金句

> "The only thing worse than a system that doesn't work is something that just works occasionally."(約 00:41)

一致性不是正確性的附屬品,在生產環境裡它本身就是一級指標。

> "Telling a user who asked why my query is slow to reduce the number of search terms is technically correct, but it doesn't actually serve the purpose at all."(約 00:43)

「技術上正確但違反語意意圖」——一個最終答案評分幾乎抓不到的失敗模式。

> "Most of these things can only be resolved by looking at the trajectory. They don't show up in the final result."(約 00:44)

整場的核心論點。

## English Notes

### TL;DR

- **Trajectories beat final answers**: most of the failure modes they found — repeated reads, backtracking, dead-end searches, inconsistency — are invisible in the final result and only surface in the trajectory. Inefficient trajectories don't just waste tokens; through context exhaustion they actively hurt accuracy.
- **More tools is not better**: split tools into **setup tools** (always called at startup) and **discretionary tools** (called by the model as needed). Moving a subset to startup forces an "onboarding" pass, shrinks the decision set the model faces mid-problem, and measurably tightens trajectory consistency.
- **Tool overload is real**: their *full* tool set was a superset of *minimal* with convenience tools pre-baked, and it was slower with marginally worse quality. What matters is **tool orthogonality / separability** — if the agent can't tell whether to call B or C, that's a problem.
- **Restructuring knowledge into a diagnostic playbook** (a router mapping symptom → problem type → handbooks) beat reading the raw guides across the board, with a **43% reduction in total tokens** and a **48% reduction in total error rate**, plus better instruction following.
- One line worth keeping: "the only thing worse than a system that doesn't work is something that just works occasionally."

### Key Points

#### The problem: a diagnostic and remediation agent for the Redis Query Engine (~00:40–00:41)

They built an AI diagnostic and remediation agent for diagnosing issues with the Redis Query Engine, primarily to help the customer support team. Redis ships a rich tool suite and extensive documentation, but in practice many complex queries were escalating all the way to the development team — not sustainable. The agent exists to unblock a good fraction of those and shorten customers' time to solution.

What makes this hard: unlike SQL, an LLM's parametric knowledge of Redis queries is fairly limited and often wrong. Many of these queries are also context-dependent — the agent must work out what's actually missing from a query. So they built an agent with skills and tools running a **clarify → diagnose → confirm** loop to make it more reliable.

#### First lesson: the final result isn't enough (~00:41–00:43)

Three observations. Evaluating the final result alone is insufficient — how you get there matters a lot. Correctness matters, but so does consistency: "the only thing worse than a system that doesn't work is something that just works occasionally." And inefficient Redis queries are expensive — the lesson learned the hard way was that they're also more error-prone downstream, because of length and context exhaustion.

A more capable frontier model resolves some of this, but what actually moved the needle was restructuring the knowledge and how the agent accesses information — making sure the agent has enough to know how to identify information, how to access it, and when to use it.

#### Four failure modes (~00:42–00:44)

Three concern the final result, one concerns the trajectory:

- **Correctness** — the result is simply wrong: wrong paths, misread metrics. These are hallucinations.
- **Completeness** — it diagnosed only part of the issue and left the rest unresolved. One of the more common failures they saw.
- **Usefulness**, in two flavors: giving too much or too generic information, so it isn't actionable and the user is overwhelmed; or giving advice that **violates semantic intent**. His example: telling a user who asked "why is my query slow?" to reduce the number of search terms is technically correct but doesn't serve the purpose at all.
- **Efficiency** — repeated reads, backtracking, dead-end searches, wasting tokens and, as noted, hurting accuracy too.

And most of these only resolve by looking at the trajectory; they don't show up in the final result.

#### Intervention 1: tool architecture (~00:44)

Split tools into **setup tools**, always called at startup, and **discretionary tools**, called by the model based on the problem it's solving. His analogy: starting a new role, you go through onboarding where they teach you what's happening, who's doing what, who to talk to. Setup tools are that onboarding — enough context for the agent to proceed correctly, use the discretionary tools correctly, and know when to use them.

#### Intervention 2: the diagnostic playbook (~00:44–00:45)

Rather than feeding raw documents, they reorganized the knowledge base into a **diagnostic playbook**: a router plus a set of handbooks. The router maps a symptom to a problem type and routes to one or more handbooks.

The observation underneath it: users don't arrive with a symptom, they arrive with a concern. Mapping concerns to symptoms is the agent's job; making that easy for the agent is the team's job — which is exactly what the playbook is for.

#### Results (~00:45–00:48)

Both interventions were studied separately, measuring end-to-end latency, number of tool calls, and result quality.

On **tool architecture**: the baseline used an automatically generated tool set and performed poorly — slow, with debatable quality. *Minimal* and *full* were both informed by their domain knowledge of how the Redis Query Engine works, with *full* a superset of *minimal*: where minimal gives you `get_shard_info` and expects you to post-process to find the slowest shard, full also ships `get_slowest_shard` so you just call it. Full did not perform better — it was slower with marginally worse quality. Two conclusions: tool overload is very much a real thing, and **tool orthogonality (or separability) matters** — at any point, if the agent can't determine whether it should call B or C, that's a problem.

The *setup tools* configuration is just *minimal* with a subset moved to startup time, so the agent chooses among a smaller set while solving. Setup tools and minimal looked similar on aggregate metrics — until they drilled into the trajectories. Without setup tools, trajectories were far more inconsistent, with many more unique sequences. Not every unique sequence is an issue, but some are. The takeaway: **reducing the decisions the LLM has to make at any point reduces variance and improves consistency**, and forcing an onboarding context via setup tools achieves that.

On **knowledge organization**, metrics split into answer quality (answer grounding, specificity) and trajectory quality (first-pass success, dead-end rate). Playbooks beat raw guides across the board, with a **43% reduction in total tokens** and a **48% reduction in total error rate**; the last row of the table also showed better instruction following. His framing: making it easier for the agent to access information reduced cost *and* reduced forgetfulness, which is what improved reliability.

#### Open work and takeaways (~00:48–00:50)

Not everything works as they'd like. He flags **recursive self-improvement** — a recurring theme at the summit — as a prime candidate for pushing performance further, though they already see a reduction in the common failure modes.

Three takeaways: measure the trajectory, not just the final answer, because many of the issues never surface in the final result; structure knowledge so it's easy for an agent to identify and access; and audit your tooling to separate mandatory baseline context from discretionary or exploratory context. If you can get correctness, completeness, and usefulness in the result plus efficient trajectories, you're far more likely to have a production-reliable agent.

### Quotes

> "The only thing worse than a system that doesn't work is something that just works occasionally." (~00:41)

Consistency isn't a side effect of correctness — in production it's a first-class metric.

> "Telling a user who asked why my query is slow to reduce the number of search terms is technically correct, but it doesn't actually serve the purpose at all." (~00:43)

A failure mode that final-answer grading almost never catches.

> "Most of these things can only be resolved by looking at the trajectory. They don't show up in the final result." (~00:44)

The thesis of the talk.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Redis Query Engine 診斷 agent | 為客服團隊建的診斷與修復 agent,跑 clarify → diagnose → confirm 迴圈 | Diagnostic and remediation agent for customer support, running a clarify → diagnose → confirm loop | 未公開發布,演講中未給名稱 / no product name given |
| Setup tools / discretionary tools | 啟動必呼叫 vs 模型自行決定的兩類工具 | Always-called-at-startup vs. model-selected tools | 目的是縮小模型的即時決策空間 / shrinks the model's in-flight decision space |
| Diagnostic playbook | router(symptom → problem type)+ handbooks | A router (symptom → problem type) plus a set of handbooks | 取代直接餵原始文件 / replaces feeding raw documents |
| `get_shard_info` / `get_slowest_shard` | 用來說明 minimal 與 full 工具集差異的例子 | The example used to contrast the minimal and full tool sets | full 多了現成便利工具但表現更差 / full's convenience tool made things worse |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Sreejit Rajmohan / Srijit | Srijith Rajamohan |
| Reddit square engine | Redis Query Engine |
| Reddits square engine works | Redis Query Engine works |
| data rates(軌跡品質指標) | dead-end rate(依上下文推定,待確認)/ inferred from context, to verify |
| this spectrum of an agent | 字幕殘缺;語意為「帶 skills 與 tools 的 agent」/ garbled; meaning is "an agent with skills and tools" |

## 待確認 / To Verify

- 軌跡品質指標的正確名稱:字幕聽成 "first pass success and data rates",第二項推定為 dead-end rate,需看投影片。/ The trajectory-quality metric heard as "data rates" — inferred as dead-end rate; check the slides.
- 官網議程標題中的 **hierarchical specs** 在演講中並未以該詞出現;現場對應的內容應是 diagnostic playbook(router + handbooks)這個階層式知識結構,但講者未明說兩者等同。/ The agenda title's "hierarchical specs" was never used verbatim; the closest delivered content is the diagnostic playbook (router + handbooks), but the speaker never equated the two.
- 43% token 下降與 48% 錯誤率下降的資料集與比較基準(相對於 raw guides,但樣本數未提)。/ Dataset and baseline behind the 43% token and 48% error-rate reductions; sample sizes weren't stated.
- 講者自述「till recently I headed AI research at Redis」,與議程職稱 Head of AI Research, Redis 略有時態差異。/ He said he "until recently" headed AI research at Redis, slightly at odds with the agenda's present-tense title.
- 使用的模型與 agent 框架未具名。/ Neither the underlying model nor the agent framework was named.
