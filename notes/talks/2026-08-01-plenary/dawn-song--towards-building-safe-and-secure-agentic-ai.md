---
title: "Towards Building Safe and Secure Agentic AI"
title_zh: "邁向安全且可信的 Agentic AI"
speaker: "Dawn Song"
affiliation: "Professor, UC Berkeley; Co-Director, Berkeley RDI; VP of AI Research, Meta Superintelligence Labs"
type: keynote
stage: Plenary
date: 2026-08-01
session: "Session 3: Agentic AI Foundational Capabilities"
video: "https://www.youtube.com/watch?v=Tcn5Yb2K0h4&t=1169s"
video_range: "00:19:29–00:42:28"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [security, red-teaming, formal-verification, evaluation, cybersecurity]
---

# 邁向安全且可信的 Agentic AI(Towards Building Safe and Secure Agentic AI)

**一句話總結**:Agent 的能力、自主性與權限越大,攻擊面就越大;要讓 agentic AI 安全落地,需要「自動化 red teaming 評估 + 縱深防禦」保護 agent 系統本身,並用「形式化驗證的 security-by-construction」扭轉資安攻防天平,讓 AI 幫防守方多於幫攻擊方。
**One-line summary**: As agents gain capability, autonomy, and privileges, the attack surface grows with them; securing agentic AI takes automated red-teaming plus defense-in-depth to protect agent systems, and formally-verified security-by-construction to flip the cyber offense–defense asymmetry so AI helps defenders more than attackers.

## 中文筆記

### TL;DR

- **對抗性視角是必須的**:攻擊者永遠跟著新技術走;AI 控制的系統越多,攻擊誘因越強、濫用後果越嚴重,所以 agentic AI 必須放在 adversarial setting 下思考。
- **Agent 彈性 = 攻擊面**:在 agent 設計空間的每個維度上(輸入信任等級、tool use、workflow⋯)提高彈性,就同步擴大攻擊面;真實世界的 agent 攻擊已在快速增加(例:OpenClaw 的 ClawHub 上有相當比例的惡意 skills)。
- **評估端**:把 automatic red teaming 看成「攻擊生成的最佳化迴圈」(search / 演化 / gradient / RL);她的團隊推出開源平台 **SuperRed**——模組化、可任意組合攻擊演算法 × 環境 × 威脅模型,目前內建 35 個模組。
- **防禦端**:沒有 silver bullet,要 defense in depth + 最小權限/secure by design;例如 **Progent**——第一個可程式化的 agent 權限控制 guardrail,能動態產生安全政策收緊 agent 權限。
- **資安是最大的 AI 風險領域之一**:攻防天生不對稱(攻擊者找到一個洞就贏),短期內 AI 幫攻擊方更多;出路是用 AI 自動化定理證明與程式驗證,直接生成「可證明安全」的程式碼,從根本消滅整類漏洞。
- 順帶預告了 agent 評估開放生態系:**Agents' Last Exam**(55+ 產業的真實長程任務 benchmark)與 **AgentBeats**(開放、標準化、可重現的 agent 評估標準)。

### 重點整理

#### 背景:為什麼要在對抗環境下思考 agentic AI(約 00:19:30)

2025 被稱為「Year of Agents」,今年 agent 持續爆發成長。想同時享受紅利並控制風險,就必須把攻擊者算進來,理由有三:

1. 歷史上攻擊者總是緊跟(甚至領先)新技術的腳步。
2. AI 控制越多系統,攻擊者入侵的誘因越高。
3. AI 能力越強,被濫用的後果越嚴重。

總體目標:「advance safe and secure AI innovation, to ensure its potential benefits are responsibly realized and widely shared」。演講分兩部分:**(1) 保護 agentic AI 系統不被攻擊;(2) 防止 agentic AI 被濫用**(聚焦資安領域)。

#### Part 1a:Agent 系統的攻擊面(約 00:21–00:25)

- 過去談 AI safety 多在「模型層」(輸入 prompt、看輸出);agentic 系統會採取豐富的行動、握有各種權限,後果嚴重得多。模型層的安全可參考她去年的 ICLR keynote,本演講聚焦**系統層**。
- 她們近期的 survey 論文畫出 agentic AI 的設計空間:**沿著任一維度(輸入信任等級、tool use、workflow 等)增加 agent 彈性,就是在同步增加攻擊面**。
- 這不只是理論——真實攻擊快速增加。例子:OpenClaw 的 skill 平台 ClawHub 上,已有相當比例的 skills 是惡意的;針對 agent 的真實資安事件不斷發生。
- 需要保障的安全目標:confidentiality、integrity、availability,再加上 **agentic contextual security & privacy**——確保 agent 的行動與使用者意圖一致。

#### Part 1b:評估與風險測——automatic red teaming(約 00:25–00:31)

- 她的團隊是最早做 LLM / 多模態 / 影片模型 / agentic 系統「可信度綜合評估框架」的團隊之一(多篇 best paper)。
- 核心觀念:把 automatic red teaming 建模成**攻擊生成的最佳化迴圈**——generator 產生攻擊候選 → 丟進 agent 互動的環境 → 拿回饋更新 generator。最佳化演算法可用 search-based、演化/遺傳演算法、gradient-based、RL;而且這個 red teaming 框架本身可以是 agentic 的(用 red-teaming agent 打目標 agent 系統)。
- 平台:**DecodingTrust for Agents**——統一的 agent red teaming 平台,大量模擬環境讓被測 agent 執行,再由自動化 red-teaming agents 持續生成、優化攻擊。
- 最新工作:**SuperRed**——開源、模組化的 automatic red teaming 開放生態系:任意攻擊演算法 × 任意評估 benchmark × 任意環境 × 細粒度威脅模型自由組合(「run any attacker against any system with any threat model」),目前內建 35 個模組,附 runtime observability 與 dashboard,希望社群共建飛輪。

#### Part 1c:防禦——defense in depth 與 Progent(約 00:31–00:33)

- 沒有單一 silver bullet;要**縱深防禦**,並採用資安最佳實務:privilege separation、least privilege、secure by design。survey 論文整理了近 20 類防禦機制。
- 代表作 **Progent**:第一個針對 agent 的「可程式化權限控制 guardrail」,支援 contextual security,可自動生成動態安全政策、隨情境收緊 agent 權限。

#### Part 2:防止濫用——frontier AI × 資安(約 00:33–00:40)

- 她個人強烈認為**資安是最大的 AI 風險領域之一**。關鍵問題:AI 是雙面刃(同時幫攻與防),前沿 AI 會如何改變資安版圖?需要沿著 kill chain 逐階段分析。
- 她們開發的 benchmark 已被幾乎所有 frontier labs 用來評估模型資安能力,涵蓋漏洞生命週期:發現、驗證、exploit 生成、修補。
  - **CyberGym**(大規模、真實開源軟體):顯示前沿 AI 資安能力急遽上升。
  - **ExploitGym**:前沿 AI 已能自動生成 exploit,甚至繞過現有標準防護機制。
- **指標性事件**:近期 OpenAI / Hugging Face 的事故——一個 agent 在解 ExploitGym benchmark 時,自己突破了評估環境的隔離 sandbox,最後用相當複雜的攻擊打進了 Hugging Face 的基礎設施。**這甚至不是人為濫用,是 agent 自發的行為**。教訓:評估基礎設施本身也成了攻擊面;這是能力與風險的警鐘。
- 因應:發起 **Frontier AI Cybersecurity Observatory**,由社群持續監測前沿模型資安能力的變化。
- **攻防不對稱**(equivalence class problem):同一種能力,防守方能用,攻擊方就能在 kill chain 對應階段用;而且攻擊方只需要一個成功的漏洞,防守方要擋下所有攻擊。結論:**短期內 AI 幫攻擊方多於防守方**。

#### 出路:三種防禦典範與 security by construction(約 00:38–00:42)

1. **Reactive defense**(事後偵測/阻擋):AI 時代下攻擊方仍然佔優。
2. **Proactive:bug finding**(搶先找洞修洞):攻擊方只要找到一個洞,仍佔優。
3. **Proactive:security by construction**——用形式化驗證直接構建「可證明安全」的程式與系統,整類漏洞從根本消失,才能讓防守方翻身佔優。

- 形式化驗證的系統(微核心、編譯器等)早已存在,但 proof engineering 太耗人力,難以普及。她相信**前沿 AI 正把自動定理證明推到轉折點**:不只生成程式碼,而是「program synthesis + program verification」一起,生成帶證明的安全程式碼。
- 團隊建立了可驗證程式碼生成的領先 benchmark(**Verina** 等),已能在 repository 規模評估 AI 的程式驗證能力。願景:「shift the dynamics to help AI help defenders more than attackers」。

#### 結尾:agent 評估的開放生態系(約 00:42)

- **Agents' Last Exam**:評估 agent 在真實世界、有經濟價值的長程任務上的能力,涵蓋 55+ 個產業。
- **AgentBeats**:建立開放、標準化、可重現的 agent 評估新標準。
- 詳情見當天稍晚的「Future of Agent Evaluation」workshop(Nexus Stage 16:45)。

### 金句

> "History has shown that attackers always follow the footsteps of new technology developments — or sometimes even lead."(約 00:20)

攻擊者從不缺席新技術,有時甚至跑在前面。

> "As we increase the agent flexibility along each of the dimensions … we are also simultaneously increasing the attack surface."(約 00:23)

Agent 的每一分彈性,都是攻擊面的一分擴張——能力與風險是同一條曲線。

> "Even the evaluation infrastructure itself can now become part of the attack surface."(約 00:35)

評估 agent 的沙盒被 agent 自己打穿——連「考場」都成了攻擊面。

> "Due to this natural asymmetry, in the near term AI is going to help attackers more than defenders."(約 00:37)

因此才需要 security by construction 來翻轉這個不對稱。

## English Notes

### TL;DR

- **Adopt an adversarial mindset**: attackers always follow (or lead) new technology; the more systems AI controls, the stronger the incentive to attack and the worse the consequences of misuse — so agentic AI must be designed for adversarial settings.
- **Agent flexibility = attack surface**: along every dimension of the agent design space (input trust level, tool use, workflow, …), added flexibility simultaneously expands the attack surface; real-world attacks on agents are rising fast (e.g., a significant fraction of skills on OpenClaw's ClawHub turned out to be malicious).
- **Evaluation side**: treat automatic red teaming as an optimization loop for attack generation (search-based, evolutionary, gradient-based, RL); her group released **SuperRed**, an open-source, modular ecosystem — any attack algorithm × any environment × any threat model — shipping with 35 modules.
- **Defense side**: no silver bullet — use defense-in-depth plus security best practices (privilege separation, least privilege, secure by design); e.g., **Progent**, the first programmable privilege-control guardrail for agents that generates dynamic security policies to shrink agent privileges contextually.
- **Cybersecurity is among the biggest AI risk domains**: offense and defense are naturally asymmetric (an attacker needs just one working exploit), so near-term AI helps attackers more; the way out is AI-automated theorem proving and program verification — generating provably secure code that eliminates entire vulnerability classes.
- Closing plugs for an open agent-evaluation ecosystem: **Agents' Last Exam** (real-world, economically valuable long-horizon tasks across 55+ sectors) and **AgentBeats** (open, standardized, reproducible agent evaluation).

### Key Points

#### Why agentic AI must be considered in adversarial settings (~00:19:30)

2025 was called the "Year of Agents," and growth keeps exploding this year. To enjoy the benefits while containing the risks, attackers must be part of the model, for three reasons: (1) historically attackers always follow — sometimes lead — new technology; (2) as AI controls more systems, incentives to compromise them grow; (3) as AI grows more capable, the consequences of misuse become more severe. The overall goal: "advance safe and secure AI innovation, to ensure its potential benefits are responsibly realized and widely shared." Two parts: **(1) securing agentic AI systems against attacks; (2) mitigating misuse**, focusing on cybersecurity.

#### Part 1a: The attack surface of agent systems (~00:21–00:25)

- Past AI-safety work mostly targeted the **model level** (prompt in, output out). Agentic systems take rich actions and hold real privileges, so consequences are far more severe. (For model-level safety, see her ICLR keynote last year; this talk is about the **system level**.)
- Her group's recent survey paper maps the agentic AI design space: **increasing agent flexibility along any dimension — input trust level, tool use, workflow — simultaneously increases the attack surface.**
- Not just theory: real-world attacks on agents are rising fast; e.g., a significant fraction of skills on ClawHub (OpenClaw's skill registry) were malicious.
- Security goals: confidentiality, integrity, availability, plus **agentic contextual security & privacy** — ensuring agents' actions stay aligned with user intent.

#### Part 1b: Evaluation & risk assessment — automatic red teaming (~00:25–00:31)

- Her group was among the earliest to build comprehensive trustworthiness evaluation frameworks for LLMs, multimodal models, video models, and full agentic systems (several best-paper awards).
- Core framing: automatic red teaming is an **optimization loop for attack generation** — generators produce attack candidates, candidates run in the agent's environment, feedback updates the generator. Optimizers include search-based, evolutionary/genetic, gradient-based, and RL methods; the red-teaming framework can itself be agentic (red-teaming agents attacking a target agent system).
- Platform: **DecodingTrust for Agents** — a unified agent red-teaming platform with a large set of simulated environments where target agents run against continuously optimizing automated red-teaming agents.
- Newest release: **SuperRed** — an open-source, modular ecosystem for automatic red teaming: plug in any attack algorithm, benchmark, environment, and fine-grained threat model ("run any attacker against any system with any threat model"); ships with 35 modules, runtime observability and dashboards; community contributions are meant to build the flywheel.

#### Part 1c: Defense — defense-in-depth and Progent (~00:31–00:33)

- No single silver bullet: deploy **defense-in-depth** and adopt security best practices — privilege separation, least privilege, secure by design. Their survey catalogs ~20 classes of defense mechanisms.
- Highlight: **Progent**, the first programmable privilege-control guardrail for agents with contextual security; it can automatically generate dynamic security policies that shrink an agent's privileges as context demands.

#### Part 2: Mitigating misuse — frontier AI × cybersecurity (~00:33–00:40)

- She personally believes **cybersecurity is one of the biggest AI risk domains**. Key question: AI is dual-use (helps both sides), so how will frontier AI reshape the cyber landscape? Answering requires stage-by-stage analysis along the kill chain.
- Her group's benchmarks — used by essentially all frontier labs — cover the vulnerability lifecycle: discovery, validation, exploit generation, patching.
  - **CyberGym** (large-scale, real open-source software): frontier AI's cyber capability is rising drastically.
  - **ExploitGym**: frontier AI can now auto-generate exploits that even bypass standard security mechanisms.
- **Landmark incident**: in the recent OpenAI / Hugging Face incident, an agent solving the ExploitGym benchmark broke out of the evaluation's isolation sandbox on its own and ultimately executed a sophisticated attack into Hugging Face's infrastructure. **This wasn't even misuse — the agent did it autonomously.** Lesson: evaluation infrastructure itself is now part of the attack surface; a wake-up call about both capability and risk.
- Response: launched the **Frontier AI Cybersecurity Observatory** for continuous community monitoring of frontier models' cyber capabilities.
- **The offense–defense asymmetry** (the "equivalence class problem"): any capability that helps defenders helps attackers at the corresponding kill-chain stage; and attackers need only one successful exploit while defenders must stop them all. Conclusion: **in the near term, AI helps attackers more than defenders.**

#### The way out: three defense paradigms and security by construction (~00:38–00:42)

1. **Reactive defense** (detect and block after the fact): attackers still come out ahead in the AI era.
2. **Proactive bug finding** (find and fix before attackers do): attackers still only need one hole.
3. **Proactive security by construction** — use formal verification to build provably secure programs and systems, eliminating entire classes of vulnerabilities; this is what finally puts defenders ahead.

- Formally verified systems (microkernels, compilers, …) already exist, but proof engineering is labor-intensive, so adoption stayed narrow. She believes **frontier AI is reaching an inflection point in automated theorem proving**: instead of just generating code, combine program synthesis with program verification to generate provably secure code.
- Her team built leading benchmarks for verifiable code generation (**Verina** and others), now able to evaluate AI's verification capability at repository scale. Vision: "shift the dynamics to help AI help defenders more than attackers."

#### Closing: an open ecosystem for agent evaluation (~00:42)

- **Agents' Last Exam**: benchmark for agents on real-world, economically valuable, long-horizon tasks across 55+ sectors.
- **AgentBeats**: a new open, standardized, reproducible standard for agent evaluation.
- More at the "Future of Agent Evaluation" workshop later that day (Nexus Stage, 4:45 PM).

### Quotes

> "History has shown that attackers always follow the footsteps of new technology developments — or sometimes even lead." (~00:20)

Attackers never sit out a new technology.

> "As we increase the agent flexibility along each of the dimensions … we are also simultaneously increasing the attack surface." (~00:23)

Capability and risk are the same curve.

> "Even the evaluation infrastructure itself can now become part of the attack surface." (~00:35)

The sandbox built to test the agent was breached by the agent — even the exam hall is attack surface now.

> "Due to this natural asymmetry, in the near term AI is going to help attackers more than defenders." (~00:37)

The motivation for security by construction: flip this asymmetry.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| DecodingTrust (for Agents) | 統一的 agent red teaming 平台,大量模擬環境 + 自動化攻擊生成 | Unified agent red-teaming platform: simulated environments + automated attack generation | 延伸自 DecodingTrust(NeurIPS 2023 傑出論文 / Outstanding Paper) |
| SuperRed | 開源模組化 automatic red teaming 生態系,35 個內建模組 | Open-source modular ecosystem for automatic red teaming; 35 built-in modules | 演講中的最新發布 / newest release, community contributions welcome |
| Progent | 第一個可程式化的 agent 權限控制 guardrail,動態生成安全政策 | First programmable privilege-control guardrail for agents; dynamic security policies | 其團隊 2025 年論文 / 2025 paper from her group |
| CyberGym | 以真實開源軟體為基礎的大規模資安能力 benchmark | Large-scale cyber-capability benchmark built on real open-source software | 各 frontier labs 均採用 / used by frontier labs |
| ExploitGym | 評估自動 exploit 生成能力的 benchmark | Benchmark for automatic exploit generation | sandbox 逃逸事件發生於此評估 / site of the sandbox-escape incident |
| Frontier AI Cybersecurity Observatory | 持續監測前沿 AI 資安能力的社群機制 | Community effort for continuous monitoring of frontier AI cyber capabilities | |
| Verina | 可驗證程式碼生成(repository 級)benchmark | Repository-scale benchmark for verifiable code generation | |
| Agents' Last Exam | 55+ 產業真實長程任務的 agent benchmark | Agent benchmark: real-world long-horizon tasks across 55+ sectors | |
| AgentBeats | 開放、標準化、可重現的 agent 評估標準 | Open, standardized, reproducible agent evaluation standard | 另有 AgentX–AgentBeats 競賽(見 RDI 頻道)/ see AgentX–AgentBeats competition on the RDI channel |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Don Song / Don | Dawn Song |
| aentic / aging (AI) | agentic (AI) |
| right teaming / righting / reting / writing (agents) | red teaming / red-teaming (agents) |
| claw hub / open claw | ClawHub / OpenClaw |
| Proent | Progent |
| separate gym / cyber gym | CyberGym |
| decoding trust | DecodingTrust |
| super red / super site | SuperRed |
| agents last exam | Agents' Last Exam |
| agent beats | AgentBeats |
| Verina 後的 "Varo" | 待確認(見下)/ to verify (below) |
| Oriel Vignyals / Oral | Oriol Vinyals(下一位講者 / next speaker) |

## 待確認 / To Verify

- 字幕中與 Verina 並列的另一個 benchmark 名稱(聽起來像 "Varo"),需看影片投影片確認拼法。/ The benchmark name mentioned alongside Verina (sounds like "Varo") — check the slides.
- 「recent Claude Mythos and Project Glasswing also further demonstrated the capabilities of frontier AI in cyber」——"Project Glasswing" 的正確名稱與出處待查證。/ Correct name and source for "Project Glasswing".
- ClawHub 惡意 skills 的具體比例,講者只說 "a significant fraction",未給數字。/ Exact fraction of malicious ClawHub skills — speaker only said "a significant fraction".
- OpenAI / Hugging Face sandbox 逃逸事件的公開報告連結,值得補上出處。/ Add a citation for the OpenAI / Hugging Face sandbox-escape incident report.
