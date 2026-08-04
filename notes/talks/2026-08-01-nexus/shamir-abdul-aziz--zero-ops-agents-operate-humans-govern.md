---
title: "Zero Ops - Agents Operate, Humans Govern"
title_zh: "Zero Ops:agent 執行,人類治理"
speaker: "Shamir Abdul Aziz"
affiliation: "Principal Product Manager, Microsoft"
type: talk
stage: Nexus
date: 2026-08-01
session: "Session 2: Coding & Web Agents"
video: "https://www.youtube.com/watch?v=ZIRc3EpzQJs&t=2443s"
video_range: "00:40:43–00:46:03"
transcript: "tmp/[English (auto-generated)] Nexus Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [devops, sre, governance, enterprise, observability]
---

# Zero Ops:agent 執行,人類治理(Zero Ops - Agents Operate, Humans Govern)

**一句話總結**:Zero Ops 不是把人從維運中移除,而是把維運從人身上移除——模型是可換的,但你的 context、治理與工具不是,而唯有可稽核、可回滾、可用證據佐證的治理,才能讓企業真的敢把 agent 放到規模上跑。
**One-line summary**: Zero Ops isn't about removing humans from operations — it's about removing operations from humans. Models are swappable; your context, governance, and tools are not. And only auditable, roll-back-able, evidence-backed governance gets enterprises to deploy agents at scale.

## 中文筆記

### TL;DR

- **口號翻轉**:數十年來是人在操作軟體系統(dashboard、metrics、alert、automation,近期加上 Copilot),但主體仍是人;Zero Ops 要把主體換成 agent,人退到治理位。
- **一句定義**:Zero Ops 不是 removing humans from operations,而是 **removing the operations from humans**。
- **護城河不是模型**:模型可換、且每天在變好;不可換的是你的 source code、production telemetry、institutional knowledge,以及你給系統的 skills 與 tools。
- **成熟度是 crawl / walk / run / fly**,而 fly 不只是「agent 會執行」,而是 agent 執行完自己驗證結果,再把**結果**交給人類覆核——這就是 outcome-based engineering:人審的是結果,不是每一個 diff。
- **規模數字**:Microsoft 內部以 Azure SRE Agent 部署超過 5,000 個 agent,處理 150 萬件 incident,其中約 22 萬件完全自動化。

### 重點整理

#### 五分鐘的自我示範(約 00:41)

他開場就說:「顯然在 agentic AI 裡,壓縮是一門真功夫」——他要用五分鐘把 Microsoft 過去兩年建 agent、跑 agent 的所有心得講完,並承諾守住五分鐘。(最後也真的做到了。)

要翻轉的現況是:數十年來我們建 dashboard、metrics、alert、automation,最近再加上 Copilot 幫忙做事——但**操作者始終是人**。Zero Ops 講的就是怎麼把這個關係翻過來。

#### 一頁投影片的四個結論(約 00:42)

1. **Zero Ops 的定義**:不是把人從維運中移除,而是把維運從人身上移除。人被「升級」去做更有影響力的事——創新、治理。
2. **模型可換,context / governance / tools 不可換**。模型每天都在變好,所以不要把資源押在模型上,押在後三者。
3. **光靠模型給不了你可用的 agent**:你得能治理它、控制它,並給它正確的 context。企業喜歡拿到的智能,但**如果他們無法控制這份智能,你就贏不到他們的信任**。
4. **信任要有可驗證的指標**:你必須能驗證 agent 做了什麼、產出的結果是什麼。

#### Crawl / walk / run / fly:什麼叫「fly」(約 00:43–00:44)

Zero Ops 是一個目的地,路上有階段。關鍵在於最後一階的 **fly 不等於「agent 會執行動作」**,而是「你允許 agent 去做某件事、它自己驗證結果、再把結果交給人類驗證」。

他給的例子很具體:某個 API 因為效能變慢而出現 regression。

- **只是及格**:agent 開一個 PR。開 PR 很容易。
- **這才是 fly**:agent 開了 PR,**還把 PR 部署到測試環境、驗證 regression 確實消失、效能回到正常**,然後才把這整份結果交出來。

這就是他說的 **outcome-based engineering**——人類不再逐行審 diff,而是審**結果**。

#### Context 是一切,治理是門票(約 00:44–00:45)

- **模型不是你的護城河**。你的護城河是:source code、production telemetry、institutional knowledge,以及你提供給系統的 skills 與 tools。把這些準備好,agent 才能真的自動化並完成工作。
- **企業要能信任 agent,需要五件事**:audit(稽核)、control(控制)、evaluate(評估)、roll back with confidence(有信心地回滾)、**prove with evidence**(用證據證明 agent 做的事是對的)。沒有這些,企業不會放行。
- 還需要 **permissions** 與 metrics:metrics 用來驗證結果,permissions 是企業願意規模化部署 agent 的前提。

#### 規模驗證:Azure SRE Agent(約 00:45–00:46)

他強調這些能力**不需要從零自建**——前面講的全部都已內建在產品裡。Microsoft 內部的實績:

- 部署超過 **5,000 個 agent**(企業層級),使用者包含 Microsoft 內部一些最大的工程團隊。
- 處理 **150 萬件 incident**。
- 其中約 **22 萬件 incident 完全自動化**。

結論公式:**context + governance + metrics 三者到位,才算真正達成 Zero Ops**。

### 金句

> "This is not about removing humans from operations. It's about removing the operations from humans."(約 00:42)

整場五分鐘的核心定義。

> "Enterprises love the intelligence they get out of it. But if they cannot control the intelligence, then you're not going to earn their trust."(約 00:42)

企業採用的瓶頸從來不是模型能力,而是可控性。

> "Humans are not reviewing every diff, they're reviewing the outcome."(約 00:44)

outcome-based engineering 的一句話定義。

## English Notes

### TL;DR

- **The inversion**: for decades humans have operated software systems — dashboards, metrics, alerts, automation, and lately Copilot — but the operator was always a human. Zero Ops makes the agent the operator and moves humans to governance.
- **The definition**: Zero Ops is not removing humans from operations; it's **removing the operations from humans**.
- **The moat isn't the model**: models are swappable and improve daily. What isn't swappable is your source code, production telemetry, institutional knowledge, and the skills and tools you hand the system.
- **Maturity is crawl / walk / run / fly**, and "fly" isn't merely execution — the agent acts, validates its own outcome, and hands the *outcome* to humans for review. That's outcome-based engineering: humans review outcomes, not every diff.
- **Scale evidence**: Microsoft has deployed 5,000+ agents internally on Azure SRE Agent, processing 1.5 million incidents, roughly 220,000 of them fully automated.

### Key Points

#### A five-minute talk about compression (~00:41)

He opened by noting that "in agentic AI, compression is a thing" — he had five minutes to distill two years of building and running agents at Microsoft, and he intended to honor them. (He did.)

The status quo he wants to flip: for decades we've built dashboards, metrics, alerts, and automation, and more recently used Copilot to get work done — but **the operator has always been a human**.

#### Four conclusions on a single slide (~00:42)

1. **What Zero Ops means**: not removing humans from operations, but removing operations from humans — bumping humans up to higher-impact work like innovation and governance.
2. **Models are swappable; context, governance, and tools are not.** Models get better every day, so invest in the parts that don't turn over.
3. **Models alone can't give you a useful agent.** You need to govern it, control it, and feed it the right context. Enterprises love the intelligence they get — but **if they can't control that intelligence, you won't earn their trust**.
4. **Trust requires verifiable metrics** that let you validate what the agent did and what outcomes it produced.

#### Crawl, walk, run, fly — and what "fly" actually means (~00:43–00:44)

Zero Ops is a destination with a journey attached, and the last stage is the interesting one. "Fly" is **not** just the agent doing something — it's the agent doing something, validating the outcome itself, and providing that outcome for humans to validate.

His example: an API has a performance regression.

- **Table stakes**: the agent opens a PR. Opening a PR is easy.
- **Fly**: the agent opens the PR, **deploys it to a test environment, validates that the regression is gone and performance is back to normal**, and only then hands the result over.

That's **outcome-based engineering** — humans aren't reviewing every diff, they're reviewing the outcome.

#### Context is everything; governance is the entry ticket (~00:44–00:45)

- **The model is not the moat.** The moat is your source code, your production telemetry, your institutional knowledge, and the skills and tools you provide to the system. With those in place, agents can genuinely automate work end to end.
- **To trust agents, an enterprise needs five things**: to audit, control, evaluate, roll back with confidence, and **prove with evidence** that what the agent did was the right thing. Without these, enterprises simply won't go ahead.
- **Permissions and metrics** round it out: metrics validate the outcome, and without a permissions story enterprises won't deploy agents at scale.

#### Proof at scale: Azure SRE Agent (~00:45–00:46)

He stressed that none of this has to be built from the ground up — everything he described is baked into the product. Microsoft's internal numbers:

- **5,000+ agents** deployed at enterprise level, used by some of the largest engineering teams at Microsoft.
- **1.5 million incidents** processed.
- Roughly **220,000 incidents** fully automated.

The closing formula: when context, governance, and metrics come together, that's when you achieve Zero Ops.

### Quotes

> "This is not about removing humans from operations. It's about removing the operations from humans." (~00:42)

The core definition of the whole five minutes.

> "Enterprises love the intelligence they get out of it. But if they cannot control the intelligence, then you're not going to earn their trust." (~00:42)

The adoption bottleneck was never model capability — it's controllability.

> "Humans are not reviewing every diff, they're reviewing the outcome." (~00:44)

Outcome-based engineering in one line.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Azure SRE Agent | Microsoft 的 SRE agent 產品,內建 context / governance / metrics 能力 | Microsoft's SRE agent product with context, governance, and metrics built in | 演講中的規模案例:5,000+ agents、150 萬 incident、22 萬自動化 |
| Copilot | 他用來對比的「人仍是操作者」階段 | Cited as the stage where humans are still the operator | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Azure S sur agent | Azure SRE Agent |
| C-pilot | Copilot |
| I've been interested with five minutes | I've been entrusted with five minutes(語意推定 / inferred) |
| aentic AI | agentic AI |
| 1.5 millions incidents | 1.5 million incidents |

## 待確認 / To Verify

- 5,000+ agents / 150 萬 incident / 約 22 萬件自動化——皆為投影片上的 Microsoft 內部數字,未見公開出處。/ The 5,000+ agents, 1.5M incidents, and ~220K automated figures come from his slide (Microsoft internal); no public source located.
- 「crawl / walk / run / fly」四階段是否為 Microsoft 官方對外的成熟度模型名稱,待查。/ Whether "crawl / walk / run / fly" is a published Microsoft maturity model or his own framing.
