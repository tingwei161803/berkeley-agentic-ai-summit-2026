---
title: "Accelerated Computing for Agentic AI"
title_zh: "為 Agentic AI 而生的加速運算"
speaker: "Jonathan Cohen"
affiliation: "VP of Applied Research, Nvidia; Academy Scientific and Technical Award Winner"
type: talk
stage: Plenary
date: 2026-08-01
session: "Session 1: Agentic AI Infrastructure & Platform"
video: "https://www.youtube.com/watch?v=gKdeLQd_LIQ&t=4420s"
video_range: "01:13:40–01:23:10"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 1st - Morning Session [DownSub.com].srt"
status: draft
tags: [infrastructure, agent-harness, nemotron, nvidia, heterogeneous-computing]
---

# 為 Agentic AI 而生的加速運算(Accelerated Computing for Agentic AI)

**一句話總結**:agent 就是「機率性的 LLM」外面包上「確定性的電腦科學」——而包住它的那一層(harness、工具、政策、沙箱、異質硬體)決定了系統實際的表現,NVIDIA 用 NeMo Agent Toolkit 與 NOOA harness 把這層工程化。
**One-line summary**: An agent is a probabilistic LLM wrapped in deterministic computer science — and the wrapper (harness, tools, policy enforcement, sandboxes, heterogeneous hardware) is what determines how the system actually performs, which is what NVIDIA's NeMo Agent Toolkit and NOOA harness set out to engineer.

## 中文筆記

### TL;DR

- **Agent = LLM + 電腦科學**。LLM 是我們目前唯一能解開某些數十年懸而未決問題的方法,但它是機率性、非確定性的;軟體則相反——確定、可檢視狀態、可下斷言。**agent 就是把兩者結合起來**:拿機率模型的智慧,包上資料結構、演算法與幾十年累積的可靠軟體工程。
- **底層平台在硬體與軟體兩層都是異質的**:部分工具跑 GPU、部分跑 CPU;複雜的儲存階層、agent 與 sub-agent 之間有 scope 的資料傳遞、越來越複雜的通訊模式、沙箱與 secure enclave;再加上大模型、小模型、微調模型與外部 API 上的專有模型混用。NVIDIA 的答案是 **NVIDIA / NeMo Agent Toolkit**。
- **Harness 和模型一樣重要**。他的團隊做的 **NOOA(NVIDIA Object-Oriented Agents)** 把 agent 就寫成一個 Python 物件:方法內容寫成 `...`(ellipsis)就等於告訴 LLM「這塊你來填」,於是 agent 能寫出方法、呼叫自己寫的方法、修改自己的方法,並把需要記住的東西直接存成物件狀態;資訊用**傳參考**而不是壓成字串塞進 context。結果:同樣分數只用一半 token,CyberGym 上取得數一數二的成績,harness 帶來的提升相當顯著。

### 重點整理

#### Agent 的來歷與定義:LLM 加上電腦科學(約 01:13–01:17)

- ChatGPT 開啟現代 AI 時代時,大家想像的是「人對 LLM 說話」,模型也許能碰某個資料庫——本質是 chat。
- 今天想的是完整的自主系統:許多模型(開放權重與專有混用)、工具、基礎設施、記憶系統、context 管理、生 sub-agent 的能力、資安基礎設施;而發起互動的**可能是人,也可能不是人**。
- 所以什麼是 agent?**agent 不只是一個 LLM,而是被「基礎設施」包住的 LLM**——這裡的基礎設施指的是讓 LLM 真的能做事的軟體:在 API 之間 marshalling 資料、型別檢查、規則式的政策強制執行。「而我們用來包住 LLM、把它變成 agent 的這一整套東西,另一個名字叫做**電腦科學**。」
- 為什麼這是個好主意:LLM 極其強大,是我們**唯一**知道能解開一大類數十年未解問題的方法;但它們是機率性、非確定性的,這恰好是軟體的反面——軟體大致上是確定的,可以理解、可以檢視狀態、可以下斷言。
- 於是 agent 是兩者的結合:取用機器學習模型的智慧,包上確定性、資料結構與演算法的力量,以及我們花幾十年學會的「怎麼把軟體做得可靠」。
- (他開場時投影片也載入了舊版本,現場笑場——延續了 Dawn Song 稍早的插曲。)

#### 異質平台與 NVIDIA Agent Toolkit(約 01:17–01:20、01:22)

典型 agent 的組成:管理送進 LLM 的 prompt 的機制、讓 LLM 存取工具並檢查權限的基礎設施——而這些現在跑在越來越複雜的硬體基質上:

- 部分軟體跑在 GPU 等加速運算基礎設施,部分跑在 CPU;儲存階層很複雜。
- 有 agent 與 sub-agent;有需要在系統之間傳遞的 **scoped 資料**;通訊模式越來越複雜;沙箱、secure enclave 等等。
- **平台在硬體與軟體兩層都是異質的**,更別提模型的組合:大模型、小模型、你自己微調並特化過的模型、外部 API 上的通用專有模型。

NVIDIA 把這一整套叫做 **NVIDIA Agent Toolkit**,包含:

- **部署**:從 Kubernetes 到託管基礎設施、computer-use agents。
- **加速工具(CUDA-X)**:例如計算流體力學、解微分方程、DNA 定序儀資料的次級分析——都是有加速解法的電腦科學任務,現在被 agentic 化成 agent 可呼叫的工具。
- **開放權重模型**:Nemotron(通用模型家族)、機器人與 physical AI 的領域模型、BioNeMo(生物預測模型)。
- **執行與治理**:能部署與執行各種模型的基礎設施;把系統包起來、確保 AI 不做你不想要的事的沙箱環境;以及**盡可能高效地跑完這一切**。
- **知識回流**:捕捉流進流出系統的知識,拿來 post-train 出在你關心的任務上特化的模型。他把「離線改進 AI 的能力(例如用 RL 做 post-training)」也算進基礎設施本身——常見用法是把小模型特化到某任務上,做得和大得多的通用模型一樣好。
- **其他元件**:NIM 與 Dynamo(部署)、NeMo Relay(捕捉 trace)、Switchyard(routing 演算法)、**blueprints**(開源參考實作,示範怎麼把這些拼起來解特定任務,例如建一個 OpenClaw、或 AIQ 這類研究助理 agent)、**OpenShell**(執行期防火牆,控制 agent 與外界之間的存取)。這些已被許多合作夥伴部署採用。

#### Harness 很重要:NOOA(約 01:20–01:22)

- 他特別想談 agentic 系統與 LLM 之間的**介面**,也就是大家說的 **agent harness**。「The harness really matters.」LLM 封裝了大量智慧,但 harness 決定你能取出多少。
- 他的團隊近期做的是 **NOOA(NVIDIA Object-Oriented Agents)**,GitHub 上有(演講中掃 QR code)。核心想法非常簡單:**agent 就是一個 Python 物件**。
  - 你用 Python 寫 agent;方法的內容寫成特殊的 **ellipsis(`...`)語法**,等於對 LLM 說「這塊由你填程式碼」。
  - 於是 agent 能**自己修改自己**:呼叫它寫出來的方法、修改自己的方法;判斷「這是我需要記住的資訊」就直接存成 Python 物件的狀態;把某個計畫或解題方式編碼成一個方法,之後再呼叫。
  - 另一個關鍵想法:**傳參考而不是傳字串**——因為全都是 Python 物件,不必把資訊壓縮成字串塞進超長 context。
- 結果(細節見 tech report):相對於單純用 LLM、甚至相對於其他 agent harness 都有顯著提升;例如**同樣分數只用一半 token**,以及 **CyberGym 上數一數二的成績**——harness 帶來的提升在這個案例上很可觀。

### 金句

> "Another word for all of this stuff that we surround our large language model with that makes it into an agent is computer science."(約 01:15)

整場演講的定義句。

> "They're the only method we know of to solve all sorts of problems that were previously unsolved … But at the same time they're probabilistic and they're non-deterministic. This is precisely the opposite of software."(約 01:15–01:16)

為什麼 agent 必須是「機率 + 確定」的混血。

> "Agentic AI workloads are significantly more complicated, heterogeneous, and expensive computationally than anything we've ever seen before."(panel 中補充,約 01:41)

同一位講者在稍後 panel 上對硬體含意的總結。

## English Notes

### TL;DR

- **An agent is an LLM plus computer science.** LLMs are the only known method for solving whole classes of long-unsolved problems, but they are probabilistic and non-deterministic — precisely the opposite of software, which is deterministic, inspectable, and assertable. An agent marries the two.
- **The platform underneath is heterogeneous at both hardware and software levels**: some tools run on GPUs, some on CPUs; storage hierarchies are deep; agents spawn sub-agents with scoped data; communication patterns keep getting more complex; sandboxes and secure enclaves surround everything — plus a mix of large, small, fine-tuned, and externally-hosted proprietary models. NVIDIA's answer is the **NVIDIA / NeMo Agent Toolkit**.
- **The harness matters as much as the model.** His group's **NOOA (NVIDIA Object-Oriented Agents)** makes an agent a plain Python object: a method body written as `...` tells the LLM to fill it in, so the agent writes its own methods, calls them, modifies them, and keeps what it needs as object state. Information is passed **by reference** rather than compacted into strings in a giant context. Results: the same score at half the tokens, and among the strongest CyberGym scores — a significant lift from the harness alone.

### Key Points

#### Where agents came from, and what one is (~01:13–01:17)

- When ChatGPT kicked off the modern AI era, these systems were things a human talked to — an LLM, maybe with access to a database. Fundamentally, chat.
- Today the picture is a complete autonomous system: many models (open-weight and proprietary), tools, infrastructure, memory systems, context management, the ability to spawn sub-agents, and security infrastructure — kicked off by a request that may or may not come from a human.
- So what is an agent? **Not just an LLM, but an LLM surrounded by what he calls infrastructure** — the software that lets the LLM actually do things: marshalling data between APIs, type checking, rule-based enforcement of policies. "Another word for all of this stuff … is computer science."
- Why that's a good idea: LLMs are incredibly powerful and are the only method we know of for solving all sorts of previously unsolved problems. But they are probabilistic and non-deterministic, the opposite of software, which we can understand, inspect, and make assertions about. An agent takes the intelligence from the probabilistic model and surrounds it with determinism, data structures, algorithms, and decades of learning about how to make software reliable.
- (His deck also loaded an out-of-date version on stage, which got a laugh — the morning's running joke, started by Dawn Song.)

#### A heterogeneous platform and the NVIDIA Agent Toolkit (~01:17–01:20, 01:22)

A typical agent has a way of managing the prompts fed to the LLM and infrastructure that lets the LLM reach tools and check permissions. All of it now runs on an increasingly complicated hardware substrate: some software on accelerated computing infrastructure like GPUs, some on CPUs, with deep storage hierarchies, agents and sub-agents, scoped data passed between systems, increasingly complex communication patterns, sandboxes, and secure enclaves. The platform is **heterogeneous at both hardware and software levels** — not to mention the collection of models: large, small, fine-tuned and specialized, and general-purpose proprietary models hosted externally on an API.

NVIDIA's version of this platform is the **NVIDIA Agent Toolkit**:

- **Deployment**: Kubernetes through hosted infrastructure, plus computer-use agents.
- **Accelerated tools (CUDA-X)**: computational fluid dynamics, differential equation solvers, secondary analysis of DNA sequences from sequencing instruments — computer-science tasks with accelerated solutions, now exposed agentically so an agent can call them.
- **Open-weight models**: Nemotron (the general-purpose family), domain models for robotics and physical AI, and BioNeMo (predictive models for biology).
- **Runtime and governance**: the ability to deploy and run all of these models, sandbox environments that surround the system to ensure the AI isn't doing something you didn't want, and running all of it efficiently.
- **Knowledge capture**: capture what flows in and out of the system and use it to post-train a model specialized for the task you care about. He counts this offline improvement loop — often RL post-training that makes a small model as good at a specific task as a much larger general model — as part of the infrastructure itself.
- **Other components**: NIM and Dynamo for deployment, NeMo Relay for trace capture, Switchyard for routing, **blueprints** (open-source reference implementations showing how to pull the pieces together for a specific task, such as building an OpenClaw or AIQ, a research assistant agent), and **OpenShell**, essentially a firewall controlling access between an agent and the outside world. Much of this is deployed and adopted by NVIDIA partners.

#### The harness matters: NOOA (~01:20–01:22)

- The interface between the agentic system and the LLM — the **agent harness** — is where he wanted to spend time. The LLM encapsulates a lot of intelligence; the harness determines how much of it you get.
- His group's recent work is **NOOA (NVIDIA Object-Oriented Agents)**, on GitHub (a QR code on the slide). The idea is simple: **an agent is just a Python object.**
  - You write the agent in Python, and a method body written with the special **ellipsis (`...`)** syntax tells the LLM "fill this block in with code."
  - The agent can therefore **modify itself**: call methods it has written, rewrite its own methods, decide that a piece of information is worth storing and hold it as state on the object, and encode a plan or a solved approach as a method to call later.
  - Another important idea: **pass by reference instead of by string.** Because everything is a Python object, you don't compact information into strings stuffed into a very large context.
- Results (details in the tech report): significant lift over a bare LLM and over other agent harnesses — for example the **same score using half the tokens**, and **among the strongest CyberGym scores**, where the harness contributed a substantial share of the result.

### Quotes

> "Another word for all of this stuff that we surround our large language model with that makes it into an agent is computer science." (~01:15)

The talk's definitional line.

> "They're the only method we know of to solve all sorts of problems that were previously unsolved … But at the same time they're probabilistic and they're non-deterministic. This is precisely the opposite of software." (~01:15–01:16)

Why an agent has to be a probabilistic/deterministic hybrid.

> "Agentic AI workloads are significantly more complicated, heterogeneous, and expensive computationally than anything we've ever seen before." (from the panel, ~01:41)

His own summary of the hardware consequence, delivered shortly afterwards.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| NVIDIA Agent Toolkit | NVIDIA 的 agentic 平台總稱:部署、加速工具、模型、追蹤、routing、blueprints、執行期治理 | NVIDIA's agentic platform: deployment, accelerated tools, models, tracing, routing, blueprints, runtime governance | 官方名稱為 NVIDIA NeMo Agent Toolkit / officially the NVIDIA NeMo Agent Toolkit |
| NOOA(NVIDIA Object-Oriented Agents) | 把 agent 寫成 Python 物件的 harness;`...` 方法體交由 LLM 填寫,支援自我修改與傳參考 | Agent harness where an agent is a Python object; a `...` method body is completed by an LLM loop; supports self-modification and pass-by-reference | <https://github.com/NVIDIA-NeMo/labs-OO-Agents> |
| Nemotron | NVIDIA 的開放權重通用模型家族 | NVIDIA's open-weight general-purpose model family | 主持人提到 Nemotron-based 系統近期在 IMO 拿到等同金牌的分數 / a Nemotron-based system reportedly scored at gold-medal level at the IMO |
| BioNeMo | 生物領域的預測模型 | Predictive models for biology | 逐字稿聽成 "biono" |
| CUDA-X | 加速工具集(CFD、微分方程、DNA 定序次級分析等),已 agentic 化 | Accelerated tool collection (CFD, differential equations, DNA secondary analysis), exposed agentically | |
| NIM / Dynamo | 模型部署技術 | Model deployment technology | |
| NeMo Relay | 捕捉 trace 的整合層 | Integration layer for capturing traces | |
| Switchyard | LLM 流量的 routing 演算法 / proxy | Routing algorithms / proxy for LLM traffic | <https://github.com/NVIDIA-NeMo/Switchyard> |
| OpenShell | 執行期防火牆,控制 agent 與外界的存取 | Runtime firewall controlling access between agent and the outside world | |
| Blueprints | 開源參考實作(例:建 OpenClaw、AIQ 研究助理 agent) | Open-source reference implementations (e.g., building an OpenClaw, or AIQ, a research assistant agent) | AIQ 的正式名稱待確認 / official name of AIQ to verify |
| CyberGym | Berkeley RDI 的資安 benchmark,被用來展示 harness 效果 | Berkeley RDI's cyber benchmark, used to demonstrate the harness's lift | 同日 Dawn Song 開場亦提及 / also cited in Dawn Song's opening |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| John Cohen | Jonathan Cohen |
| Invidia | NVIDIA |
| neatron / neotron | Nemotron |
| biono | BioNeMo |
| NIMS | NIM |
| Nemo relay / switchyard | NeMo Relay / Switchyard |
| open claw | OpenClaw |
| chat GBT | ChatGPT |
| cyber gym | CyberGym |
| sub aents | sub-agents |
| ellipsus notation | ellipsis (`...`) notation |
| post-rain | post-train |
| Nemo object-oriented agents | NVIDIA Object-Oriented Agents (NOOA) |

## 待確認 / To Verify

- 「AIQ」的正式名稱與定位(可能是 NVIDIA 的 AI-Q research assistant blueprint;NeMo Agent Toolkit 前身亦曾稱 AgentIQ/AIQ,兩者需區分)。/ Official name and scope of "AIQ" (possibly NVIDIA's AI-Q research assistant blueprint; the NeMo Agent Toolkit was also formerly called AgentIQ/AIQ — these need disambiguating).
- NOOA 在 CyberGym 上的實際分數與「同分一半 token」的具體對照組,演講未給數字,需查 tech report。/ NOOA's actual CyberGym score and the exact baseline for the "half the tokens" claim — no numbers were given; check the tech report.
- 主持人介紹提到的「Nemotron-based 系統在 IMO 取得金牌等同分數」的正式公告。/ Official announcement for the Nemotron-based IMO gold-medal-equivalent result mentioned in the introduction.
- 他所說 blueprints 中「building an open claw」指的是 NemoClaw 還是通用的 OpenClaw 參考實作。/ Whether "building an open claw" refers to NemoClaw specifically or a generic OpenClaw reference implementation.
