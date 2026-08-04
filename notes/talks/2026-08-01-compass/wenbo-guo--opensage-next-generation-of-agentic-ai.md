---
title: "OpenSage: Next Generation of Agentic AI"
title_zh: "OpenSage:下一代 Agentic AI"
speaker: "Wenbo Guo"
affiliation: "Assistant Professor, UCSB"
type: talk
stage: Compass
date: 2026-08-01
session: "Session 2: Frameworks & Dev Platforms"
video: "https://www.youtube.com/watch?v=AO0RXP-fVZQ&t=236s"
video_range: "00:03:56–00:13:51"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [agent-framework, adk, self-programming, ctf, benchmarks]
---

# OpenSage:下一代 Agentic AI(OpenSage: Next Generation of Agentic AI)

**一句話總結**:今天的 agent 框架都要人先把 topology、工具集、記憶結構寫死,這正是十年前深度學習時代被淘汰的「feature engineering」;OpenSage 只給最小 scaffold,讓 agent 自己長出 sub-agent、自己寫工具與記憶——這是他們口中的 agent 2.0。
**One-line summary**: Every agent framework today makes a human pre-specify topology, toolset, and memory structure — which is exactly the "feature engineering" deep learning made obsolete a decade ago. OpenSage ships only a minimal scaffold and lets the agent spawn its own sub-agents, write its own tools, and design its own memory: what the speaker calls agent 2.0.

## 中文筆記

### TL;DR

- **問題**:現行 agent 開發是「先把系統設計定好再建 agent」——預先指定 topology、工具集、記憶結構。但長程複雜任務中,agent 會需要臨時 spawn sub-agent、發現手上工具不夠、需要自己造工具;寫死等於直接壓縮 generalizability。
- **類比**:這就像 10–20 年前的 feature engineering——把人的 inductive bias 塞進模型,反而限制了搜尋空間。深度學習的答案是「直接餵原始資料讓模型自己找」;OpenSage 對 agent 做同一件事:**只提供最小 scaffold,讓 AI 自己蓋 agent**。
- **成績**:發表時(約 2026 年 2 月)在多個 coding 與 security benchmark 上勝過 Claude Code 與 Codex;更亮眼的是拿去打 **DEF CON 2026 資格賽**——15 題非互動題解出 7 題、共取得 8 個 flag,足以擠進歷來參賽隊伍前五,並贏過所有宣稱不用或少用 AI 的人類隊伍。
- **下一步**:agent 蓋好只是第一步,**模型必須與 agent 共同演化**——現有最強模型還沒學會怎麼幫自己蓋 agent(想 spawn 新 agent 卻失敗);因此要同時做 agent 框架、模型訓練、以及專為 agent trajectory 設計的 inference stack。

### 重點整理

#### Agent 1.0 的天花板:什麼都預先寫死(約 00:04–00:06)

Guo 先描述現況:大家建 agent 的方式,是**在動工前就把 agent structure、agent topology、工具集與記憶結構全部定好**,「就像寫軟體一樣,你很清楚自己要蓋什麼,有一份明確的系統設計,然後才讓 agent 去跑」。

問題出在長程複雜任務。執行途中,agent 可能需要自己 spawn sub-agent;也可能發現「我手上這組工具不夠,我得發明新工具才能完成」。**只要這些東西是預先寫死的,agent 的能力與泛化性就被硬生生綁住**。

#### 從 feature engineering 到 agent 2.0(約 00:06–00:08)

他用機器學習史來類比。10–20 年前設計模型的第一步是 feature engineering:從原始資料裡想辦法抽特徵——那其實是把人類知識、也就是 **inductive bias** 加進模型。後來大家發現這一步不必要:直接把深度網路餵原始資料,模型自己會找出來,而且**少了 inductive bias 的約束,模型能在更大的搜尋空間裡找到更好的解**。

OpenSage 的問句就是把這件事套到 agent 上:如果我們不做那些手工「feature engineering」(預先指定 workflow、topology、工具集),而是**只搭一組最小 scaffold,讓 agent 自己蓋自己的 agent**,會怎樣?具體來說,給 agent 一組起始工具,讓它沿途可以自行 spawn sub-agent、設計自己的 workflow topology、寫自己的工具、甚至設計自己的記憶。

實作上他們重寫了整個 ADK(agent development kit),使 agent 能在執行過程中探索自己的 topology 與工具。他展示了一張 OpenSage 與 Google 等 frontier ADK 的能力對照表——正因為這些自由度是現有 ADK 給不了的,他們才稱之為 **agent 2.0**(現有框架是 agent 1.0)。

#### 實測:benchmark 與 DEF CON(約 00:09–00:12)

- **Benchmark**:主要測 coding 與數個 security 相關 benchmark。發表當時(約今年二月)對比 Claude Code 與 Codex,在 SWE-bench、SWE-bench Pro 等既有 benchmark 上勝過所有現有 agent 框架。他自己補充這些數字已經有點過時,OpenSage 仍在演進。
- **DEF CON 2026 資格賽**:他形容這是攻擊性資安界的奧運,通常要一隊職業 hacker 連戰 48 小時,有些隊伍甚至上百人。由於主辦方不允許 AI 提交答案,他們是**在比賽同步開放題目時平行跑**。15 題非互動題中解出 7 題;事後分析另有 4 題「差一點,再給一小時應該能解」。總計取得 **8 個 flag**,足以名列歷來所有參賽隊伍的**前五**,並且**贏過所有宣稱沒用或少用 AI 的隊伍**。
- 更關鍵的是 trace 顯示的行為:OpenSage 為了解題**連續跑了五、六個小時,spawn 出上千個 sub-agent**——證明它真的會依任務難度自行擴張 topology。

#### 收尾:模型與 agent 必須共同演化(約 00:12–00:13)

蓋出 agent 只是第一步,**模型這顆腦袋同樣關鍵**。他們的觀察是:即使搭配最新模型,模型**還沒完全學會怎麼幫自己蓋 agent**——有時模型想 spawn 一個新 agent,實際上卻失敗。

因此他們往一個更全局的框架走:用新的 agent 去訓練模型,把模型訓練成更會 spawn 自己的 agent、更會寫自己的工具;同時因為 **agent trajectory 與純 QA 任務的形態完全不同**,他們也在開發新的 agent inference framework。

最後的訊息:AI agent 的未來是**把自由度打開,讓 AI 對「最終構成 agent 的一切」做更多探索**;人類要提供的是有意義的 scaffolding、夠強的模型,以及最有效率的 inference framework。

### 金句

> "What about we just build a minimal set of scaffold that enable the agent to build its own agent?"(約 00:07)

一句話講完 OpenSage 的設計哲學。

> "We want something like AI build AI — agent build agents."(約 00:07)

> "This is the AI-only agent that's able to beat a team of professional hackers that didn't use AI in their competition."(約 00:11)

DEF CON 資格賽的結論——純 AI 隊伍已經打贏不用 AI 的職業人類隊伍。

## English Notes

### TL;DR

- **The problem**: today you design the whole system before you build the agent — topology, toolset, and memory structure are all pre-specified. But on complex long-horizon jobs an agent needs to spawn sub-agents mid-run and often discovers its given tools aren't enough. Freezing all of that upfront caps generalizability.
- **The analogy**: this is feature engineering circa 2006–2016 — injecting human inductive bias and shrinking the model's search space. Deep learning's answer was to feed raw data and let the model figure it out. OpenSage does the same for agents: **ship a minimal scaffold and let AI build the agent.**
- **Results**: at release (~February 2026) OpenSage beat Claude Code and Codex on coding and security benchmarks; more striking, it was run against the **DEF CON 2026 qualifiers** — 7 of 15 non-interactive challenges solved, 8 flags total, good enough for a top-five finish among all teams that ever played, and it beat every team claiming no or low AI use.
- **What's next**: building the agent is step one; **the model has to co-evolve with it**. Even the latest models haven't fully learned to build their own agents (they try to spawn sub-agents and fail), so the work now spans the framework, model training, and an inference stack designed for agent trajectories.

### Key Points

#### The ceiling of agent 1.0: everything is decided upfront (~00:04–00:06)

Guo opened with how agents get built today: the agent structure, topology, toolset, and memory structure are all fixed before any code runs — "it's like you build a software, you know exactly what you want to build, you have a clear system design, and then we let the agent run the job."

That breaks down on long-horizon work. Mid-execution an agent may need to spawn its own sub-agent, or realize the tools it was handed aren't sufficient and that it needs to invent new ones. **If all of that is pre-specified, you have constrained the agent's capability and generalizability.**

#### From feature engineering to agent 2.0 (~00:06–00:08)

The framing comes from ML history. Ten or twenty years ago, step one in building a model was feature engineering — extracting features from raw inputs, which really means baking human knowledge, or **inductive bias**, into the model. Then the field discovered that step was unnecessary: train a deep network on raw data and it figures the features out itself, and **without the inductive-bias constraint it searches a much larger space for better solutions.**

OpenSage asks the same question about agents. Skip the manual feature engineering — the pre-specified workflow, topology, and toolset — and instead **build a minimal scaffold that lets the agent build its own agent**: give it some initial tools, and let it spawn sub-agents, design its own workflow topology, write its own tools, and even design its own memory along the way.

Concretely, they redesigned the whole ADK (agent development kit) so the agent can explore its own topology and author its own tools during execution. A comparison slide put OpenSage against Google's and other frontier ADKs on exactly these capabilities — and because no existing ADK offers that freedom, they call it **agent 2.0**, with today's frameworks as agent 1.0.

#### Evidence: benchmarks and DEF CON (~00:09–00:12)

- **Benchmarks**: evaluated mainly on coding plus several security benchmarks. At release (~February this year) it outperformed all existing agent frameworks against Claude Code and Codex on SWE-bench, SWE-bench Pro, and others. He noted the numbers are already dated — OpenSage keeps evolving.
- **DEF CON 2026 qualifiers**: he described it as the Olympics of offensive security, normally requiring a team of professional hackers working 48 hours, sometimes hundreds of them. Since the organizers don't allow AI submissions, the team ran **in parallel with the live competition**. Of 15 non-interactive challenges, it solved 7; post-hoc analysis showed 4 more were close enough that another hour might have cracked them. **8 flags total** — enough for a **top-five** placing among all teams that have ever competed, and enough to **beat every team that claimed no or low AI usage**.
- The behavior in the traces is the real point: OpenSage ran **five to six hours continuously and spawned thousands of sub-agents** to get there, demonstrating that it genuinely scales its own topology to task difficulty.

#### Closing: the model has to co-evolve (~00:12–00:13)

The agent is only the first step; **the brain matters too**. Their observation running OpenSage on the latest models is that **the model hasn't fully figured out how to build its own agent** — it tries to spawn a new agent and the attempt fails.

That pushes them toward an end-to-end picture: use new agents to train the model, train the model to spawn its own agents and write its own tools better, and — because **agent trajectories look nothing like pure QA tasks** — build new agent inference frameworks as well.

The closing message: the future of AI agents is about opening up the freedom for AI to explore everything that ultimately constitutes the agent. What humans should supply is meaningful scaffolding, a powerful model, and the most efficient inference framework.

### Quotes

> "What about we just build a minimal set of scaffold that enable the agent to build its own agent?" (~00:07)

The whole design philosophy in one sentence.

> "We want something like AI build AI — agent build agents." (~00:07)

> "This is the AI-only agent that's able to beat a team of professional hackers that didn't use AI in their competition." (~00:11)

The DEF CON headline.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| OpenSage | 讓 LLM 自行生成 agent topology、工具集與階層式記憶的 ADK | ADK that lets an LLM self-generate agent topology, toolsets, and hierarchical memory | 論文 *OpenSage: Self-programming Agent Generation Engine*(arXiv 2602.16891);GitHub `opensage-agent/opensage-adk`;官網 opensage-agent.ai |
| DEF CON 2026 CTF Qualifiers | 攻擊性資安領域最具指標性的 CTF 資格賽 | The flagship qualifier CTF in offensive security | 演講中 OpenSage 與正賽同步平行跑,取得 8 flags |
| SWE-bench / SWE-bench Pro | Coding agent 標準 benchmark | Standard coding-agent benchmarks | 字幕聽成 "several bench" / "swen pro" |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Wimbleu / Wimbo | Wenbo (Guo) |
| UCS Barbara | UCSB (UC Santa Barbara) |
| open sage / open s / open stage | OpenSage |
| a genti / aentic | agentic |
| agent design cookie | agent development kit (ADK) |
| cloud code / codeex | Claude Code / Codex |
| several bench / swen pro | SWE-bench / SWE-bench Pro |
| Defcon 2026 qualification game | DEF CON 2026 CTF Qualifiers |
| industrial bias | inductive bias |
| span (its own agent) | spawn |

## 待確認 / To Verify

- 講者自述除 UCSB 外還是某處的 research scientist,字幕作 "Met Times SL",聽起來像 Meta Superintelligence Labs (MSL),需確認。frontmatter 依官網議程僅列 UCSB。/ He mentioned a second affiliation transcribed as "Met Times SL", plausibly Meta Superintelligence Labs — needs confirmation; the frontmatter follows the official agenda (UCSB only).
- 第三個 benchmark 字幕作 "dialops gym",拼法與正確名稱待確認(可能是某個 security/DevOps 類 gym benchmark)。/ A third benchmark was transcribed as "dialops gym" — correct name unknown.
- 「解出 7 題」與「取得 8 個 flag」數字不一致,講者未說明,照原話記錄。/ "Solved seven" vs "retrieved eight flags" is inconsistent in the talk itself; recorded as spoken.
- OpenSage 發布時間他說「about February this year」,對照 arXiv 編號 2602 相符,但正式發布日期待查。/ He dated the release to "about February this year", consistent with the arXiv ID (2602); exact release date unverified.
