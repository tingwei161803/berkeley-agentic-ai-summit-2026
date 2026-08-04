---
title: "Observability Is Not Governance: Building a Runtime Trust Plane for Agentic AI"
title_zh: "可觀測性不等於治理:為 Agentic AI 打造 Runtime Trust Plane"
speaker: "Jon-Rav Shende"
affiliation: "Chief Technology Officer, Thales Group"
type: talk
stage: Nexus
date: 2026-08-01
session: "Session 4: Secure Agentic AI"
video: "https://www.youtube.com/watch?v=ZIRc3EpzQJs&t=9045s"
video_range: "02:30:45–02:47:22"
transcript: "tmp/[English (auto-generated)] Nexus Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [governance, security, identity, runtime, enterprise]
---

# 可觀測性不等於治理:為 Agentic AI 打造 Runtime Trust Plane(Observability Is Not Governance: Building a Runtime Trust Plane for Agentic AI)

**一句話總結**:看得見 agent 在做什麼,不等於能對它做什麼;真正的治理要盯的不是 agent 而是**控制路徑(control path)**,在執行提交之前用 declared vs observed 的差異、identity/policy/risk/evidence 四個維度做即時裁決。
**One-line summary**: Being able to see what an agent is doing is not the same as being able to do something about it; real governance watches the **control path** rather than the agent, and adjudicates every execution commit in real time against declared-vs-observed variance across identity, policy, risk, and evidence.

## 中文筆記

### TL;DR

- **一句話拆穿業界的混用**:observability 和 governance 在業界被交替使用,但 observability 只回答「發生了什麼」,治理要回答「**我們能不能對它做點什麼**」。兩者互補、不可互相取代。
- **要治理的對象是 control path,不是 agent**:控制路徑是動態的,所以要在其中埋 hook,即時評估哪裡可能出錯、預測會出什麼錯、定義出錯時的 outcome,再據此建立風險控制。
- **實作核心是 declared vs observed**:他們先為環境中每個 agent 建立「declared authority」契約資料庫(該做什麼、碰哪些系統、呼叫哪些工具),上線後比對實際觀測值,把差異分成 **allowed / approved / drift / control failure** 四類——**control failure 才是最重要的指標**,drift 本身未必是壞事,重點是知道 delta。

### 重點整理

#### 起點:一次 audit 把整個專案叫停(約 02:31–02:36)

Thales 的工作是建構安全架構與框架,涵蓋自家內部系統與終端使用者將使用的系統。促發他思考的事件,是他所說的「上週或前一週,一個 agent 決定做它自己想做的事」。由此延伸出三個問題:**我們的 agent 在做什麼?我們怎麼治理它們?在營運環境中我們該擔心哪些挑戰?**

他先給了兩個產業數字:

- Gartner 的預測是,企業大量部署 agent 與 ML+LLM 系統,而其中**超過 40% 會在 2027 年前失敗**(Gartner 原文的說法是「被取消」,原因包含成本失控、商業價值不明、風險控制不足)。
- 另一份調查(他明確說「這不是產業 benchmark,是一份 survey」):只有 **14.4%** 的組織真的從安全角度在看這件事。

然後是那個讓全場工程師會心一笑的故事:工程師被要求 build it、ship it、get it out the door,然後 audit 進來踩煞車。他自己就遇過——audit 檢查了 agent 的權限與 entitlement,結論是「**看起來它們想做什麼就能做什麼**」。專案被迫停下、重新設計,跟 identity 團隊合作建立身分,並確保這些身分帶有 **signed intent**:一份定義「這個 agent 應該根據它該交付的成果做哪些事」的契約。

#### AI 之前 vs AI 之後:線性環境的終結(約 02:36–02:38)

AI 之前的環境是**線性**的:使用者 → SaaS → 商業系統。我們知道系統被要求做什麼、使用者在做什麼,因此能在這些節點外圍套上治理控制與安全指標。

今天則是使用者、agent 或兩者一起工作:一個使用者發出請求,那個請求可以呼叫 agent、呼叫模型,再加上 orchestration——結果是**整個生態系在即時、同時地自己活了起來**。

因此他們在 Thales 從三個層面著手:**execution、runtime governance、evidence layer**。理由是:沿用線性流程、線性治理模型、軟體時代的基本測試與內嵌 QA,今天**不夠**——因為工作流是並行發生的,功能綁在這些工作流上,而**有時候我們根本不確定誰對這些工作流中的功能負責、誰要當責**。

於是需要建立一個交易(transaction)紀錄的資料庫:這些交易執行時造成什麼影響、如何根據影響建立風險指標,再由此構成 **evidence layer**。

#### Sub-agent 的權限繼承問題(約 02:38–02:39)

底層依 **human request** 與 **delegated authority** 切分。他和團隊最在意的問題是:當我們把權限與 entitlement 指派給一個 sub-agent 時,**那個 sub-agent 是不是照它該有的方式在行動?** 如果它是代表另一個 agent 行動,而且**繼承了主 agent 的權限、entitlement 與授權——這件事該發生嗎?**

他的回答與現場共識一致:不該。但他隨即點出落差:「**在座這群人是有限的,產業比我們大得多。我看到的挑戰是,大家為了 build and ship 在跳過步驟——一旦跳過,我們就把自己暴露在風險裡。**」

#### 核心論點:observability ≠ governance(約 02:39–02:42)

因為有 evidence layer,他們**看的不是 agent,而是 control path**。控制路徑是動態的,所以必須在其中埋 hook,才能即時評估哪裡可能出錯、預測會出什麼錯、定義出錯時的 outcome,並針對它建立風險控制。

接著是整場的核心:

- **Observability 很好**——我們看得到正在發生什麼。**但我們能對它做什麼嗎?這才是問題。**
- 談治理時,我們知道有事情正在發生(因為模型正在執行),但真正要做的是**評估控制路徑,並基於某個 outcome 在控制路徑上施加治理**。
- 而那個 outcome 的存在是為了**強制執行決策**,那些決策綁定在 **identity、policy、authorization** 三者上。有了資料就能建 **decision matrix**,再在執行路徑上依控制路徑的風險施加控制。
- 結論:**observability 加 governance,兩者不可互相取代,必須並行運作。**

#### Declared vs observed 與 runtime trust plane(約 02:42–02:46)

實作上,他們為環境中所有 agent 建了一份契約與資料庫,定義每個 agent**在做什麼、與什麼互動、呼叫哪些工具、牽動哪些系統**——這就是 **declared authority**。

系統跑起來之後,結果不出所料:**出現了 variance**,實際行為與 declared state 不符。於是他們對 variance 做分析,建在他們的 **runtime trust plane** 上,比較 **declared vs observed**,搭配 identity、delegation、policy、risk 的指標以及前述 evidence layer。

他在這裡丟出第二個反直覺論點:**drift 未必是壞事,重點是我們要知道 delta。** 他們把 explained variance 分成四類:

1. **shown / allowed**(已宣告、允許)
2. **approved**(經核可)
3. **drift**(漂移)
4. **control failure**(控制失效)

他問全場哪個最重要,答案是 **control failure**。

工程環境上,他們用四個 constraint 收斂,包含 **ephemeral agents**、觀測到的 **drift**,以及**延遲**——他在此點名前面 Oracle 醫療講者的說法,延遲直接影響成本。由這些資料建出一條 **containment path**,核心是一個**明確定義的 kill switch**,可執行的動作有:**quarantine(隔離)、roll back(回滾)、取得次級授權(secondary authorization)、或直接停止**。

最後是執行前的裁決機制:對「agent 發出的 function」與「decision proposal」,他們在 runtime trust plane 上評估一個 envelope——涵蓋 **authority、policy、risk、evidence** 四個維度——**通過才允許 execution commit**。而且會標上風險分類:**低風險自動執行,高風險需要人類核可**。

他總結:他們建的是一份即時運作、橫跨所有邊界的 **record of trust**,從 identity 一路涵蓋到 action。時間用盡前他提到環境中還有一個「**guardian agents**」的概念,只留了一句「之後再聊」。

### 金句

> "Observability is good. We can see what's happening, right? But can we do something about it? That's the question."(約 02:40)

整場演講的題目就是這句話的展開。

> "We are a finite group. Over in larger industry, the challenge I'm seeing is people are skipping steps because we need to build and ship. And if we build and ship, we open ourselves up to risk."(約 02:39)

在座懂的人不代表產業會做——這是治理落差的真正來源。

> "Drift is not necessarily bad. We need to know the delta."(約 02:43)

治理的目標不是消滅偏差,而是讓偏差可分類、可裁決。

## English Notes

### TL;DR

- **A blunt correction of industry vocabulary**: observability and governance get used interchangeably, but observability only answers "what happened." Governance has to answer "**can we do something about it?**" The two are complementary and neither substitutes for the other.
- **The object of governance is the control path, not the agent.** The control path is dynamic, so you need hooks into it to assess in real time where something could go wrong, predict what could go wrong, define an outcome for when it does, and build risk controls against that.
- **The implementation is declared vs. observed.** They built a contract database of **declared authority** for every agent in the environment (what it does, what it touches, which tools it calls), then compared it against runtime observations and classified the variance as **allowed / approved / drift / control failure**. **Control failure is the metric that matters** — drift by itself isn't necessarily bad; knowing the delta is the point.

### Key Points

#### Where it started: an audit that stopped the project (~02:31–02:36)

Thales builds security architectures and frameworks covering both their own internal systems and systems their end users will run. What set Shende off was, in his words, "what happened last week or the week before, where an agent decided to do its own thing." That produced three questions: **what are our agents doing, how are we governing them, and what should we be concerned about in an operating environment?**

He grounded it in two numbers:

- Gartner's forecast that as enterprises deploy agents and ML+LLM systems at scale, **over 40% will fail by 2027**. (Gartner's own wording is that over 40% of agentic AI projects will be *canceled* by end of 2027, citing escalating costs, unclear business value, and inadequate risk controls.)
- A survey — he was explicit it is a survey, not an industry benchmark — showing only **14.4%** of organizations are approaching this from a security perspective.

Then the story that landed with a room full of engineers. Engineers are told to build it, ship it, get it out the door. Then audit arrives and pulls the brakes. It happened to him: audit checked the agents' privileges and entitlements and reported that **they could just do anything they wanted**. The team had to stop, re-engineer, work with the identity team, build identities, and ensure those identities carried a **signed intent** — a contract defining what the agent should be doing based on the outcomes it is supposed to deliver.

#### Before and after AI: the end of the linear environment (~02:36–02:38)

Before AI the environment was **linear**: user → SaaS → business systems. We knew what we were asking systems to do and what users were doing, so we could wrap governance controls and security metrics around those points.

Today a user, an agent, or both work together: a user issues a request, that request calls agents and models, orchestration layers on top — and the result is an **entire ecosystem taking on a life of its own, in real time, simultaneously**.

Thales's response works across three layers: **execution, runtime governance, and an evidence layer**. The rationale: following linear processes, a linear governance model, the basic testing we do for software, and embedded QA is **not enough today**, because workflows occur in tandem, functions are tied to those workflows, and **sometimes we aren't sure who is responsible or accountable for those functions**.

That drives the need for a database of transactions: records of what executed, what the impact was, how to build risk metrics from that impact, and from there the **evidence layer**.

#### The sub-agent privilege-inheritance problem (~02:38–02:39)

Underneath, everything is subdivided by **human request** and **delegated authority**. The concern he and his team keep returning to: when privileges and entitlements are assigned to a sub-agent, **is that sub-agent acting as it should?** If it acts on behalf of another agent and **inherits the primary agent's privileges, entitlements, and authorizations — should that be happening?**

His answer matched the room's: it should not. But he immediately named the gap — this room is a finite group, industry is much larger, and the challenge he sees is people skipping steps because they need to build and ship, which is exactly how risk gets in.

#### The core argument: observability ≠ governance (~02:39–02:42)

Because of the evidence layer, **they watch the control path rather than the agent**. The control path is dynamic, so hooks into it are required to assess in real time where something could go wrong, predict what could go wrong, define an outcome when it does, and build risk controls against that.

Then the thesis:

- **Observability is good** — we can see what's happening. **But can we do something about it? That's the question.**
- When we talk about governance, we know something is occurring because the model is executing; what's needed is to **assess the control path and apply governance on that control path based on an outcome**.
- That outcome exists to **enforce decisions**, and those decisions are bound to **identity, policy, and authorization**. With that data you build a **decision matrix**, then enforce controls within the execution path based on risk to the control path.
- Conclusion: **observability plus governance — not replaceable, not substitutes, they work in tandem.**

#### Declared vs. observed and the runtime trust plane (~02:42–02:46)

In practice they built a contract and a database of every agent in their environment, defining what each was doing, what it interacted with, what tools it called, and what systems it engaged — the **declared authority**.

Once everything was running, the predictable happened: **variances**, behavior that was not what they had declared. So they built variance analysis across their **runtime trust plane**, comparing **declared vs. observed** alongside metrics from identity, delegation, policy, and risk, plus the evidence layer.

His second counterintuitive point landed here: **drift is not necessarily bad — we need to know the delta.** They categorized explained variance into four buckets:

1. **shown / allowed**
2. **approved**
3. **drift**
4. **control failure**

Asked which mattered most, the room got it right: **control failure**.

The engineering environment was constrained on four constraints, among them **ephemeral agents**, observed **drift**, and **latency** — he credited the Oracle healthcare speaker earlier for the point that latency feeds directly into cost. From that data they built a **containment path** engineered around a defined **kill switch** with four actions: **quarantine, roll back, obtain secondary authorization, or stop**.

Finally, the pre-execution adjudication: for a **function issued by an agent** plus a **decision proposal**, they evaluate an envelope on the runtime trust plane across **authority, policy, risk, and evidence** before allowing an **execution commit** — tagged with risk categories, where **low risk auto-executes and high risk requires human approval**.

He summed up what they built as a **record of trust** running in real time across the top boundaries, covering everything from identity to action. Out of time, he mentioned one more concept in their environment — **guardian agents** — and left it at "we can talk about that later."

### Quotes

> "Observability is good. We can see what's happening, right? But can we do something about it? That's the question." (~02:40)

The talk title, unpacked in one line.

> "We are a finite group. Over in larger industry, the challenge I'm seeing is people are skipping steps because we need to build and ship. And if we build and ship, we open ourselves up to risk." (~02:39)

The people in the room knowing better is not the same as industry doing better.

> "Drift is not necessarily bad. We need to know the delta." (~02:43)

Governance aims to make deviation classifiable and adjudicable, not to eliminate it.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Runtime trust plane | 比對 declared vs observed、綜合 identity/delegation/policy/risk/evidence 的即時治理層 | Real-time governance layer comparing declared vs. observed across identity, delegation, policy, risk, and evidence | Thales 內部建置 / built internally at Thales |
| Declared authority(契約資料庫)| 記錄每個 agent 該做什麼、碰哪些系統、呼叫哪些工具的契約 | Contract database of what each agent should do, touch, and call | variance 分析的基準線 / the baseline for variance analysis |
| Signed intent | 綁在 agent identity 上、定義其應交付成果的契約 | A contract bound to the agent's identity defining the outcomes it should deliver | audit 事件後與 identity 團隊共同導入 / introduced with the identity team after the audit |
| Variance 四分類 | shown/allowed、approved、drift、control failure;control failure 為最關鍵指標 | shown/allowed, approved, drift, control failure — control failure is the key metric | |
| Containment path / kill switch | 四種處置:quarantine、roll back、secondary authorization、stop | Four actions: quarantine, roll back, secondary authorization, stop | |
| Execution commit envelope | 依 authority / policy / risk / evidence 裁決是否放行,低風險自動執行、高風險需人類核可 | Adjudicates each commit across authority, policy, risk, evidence; low risk auto-executes, high risk needs human approval | |
| Gartner 預測 | 超過 40% 的 agentic AI 專案將在 2027 年底前被取消 | Gartner: over 40% of agentic AI projects will be canceled by end of 2027 | <https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027> |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| John Rav Shendi | Jon-Rav Shende |
| Thalis Group / thalis | Thales Group |
| security architects | security architectures |
| evaluance layer | evidence layer |
| decision ma matrix | decision matrix |
| effiral agents | ephemeral agents |
| explained variants | explained variance |
| guardian angels | guardian agents(講者當場自行更正 / self-corrected on stage)|

## 待確認 / To Verify

- 「上週或前一週那個 agent 決定做它自己想做的事」——講者未指名事件;需對照當時公開的 agent 資安事件報導確認。/ The agent incident "last week or the week before" was never named; cross-check against publicly reported agent incidents from that period.
- 「14.4% 的組織從安全角度看待 agent」的調查來源未說明。/ Source of the 14.4% security-posture survey.
- 工程環境的**四個 constraint** 只清楚點到 ephemeral agents、drift、latency 三項,第四項未在逐字稿中出現。/ Only three of the four engineering constraints (ephemeral agents, drift, latency) are recoverable from the transcript.
- 「guardian agents」是否為 Thales 內部名稱或引用外部既有概念,講者因時間不足未展開。/ Whether "guardian agents" is a Thales-internal name or a borrowed industry term — he ran out of time.
