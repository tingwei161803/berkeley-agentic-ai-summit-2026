---
title: "Making Autonomy Autonomous: Toward Mental Models for Discovery and Intuition"
title_zh: "讓自主變得自主:邁向可供發現與直覺的心智模型"
speaker: "Manmohan Chandraker"
affiliation: "Professor, University of California, San Diego"
type: talk
stage: Atlas
date: 2026-08-01
session: "Session 2: Robotics & World Models"
video: "https://www.youtube.com/watch?v=psPzCQbjCCo&t=3306s"
video_range: "00:55:06–01:04:41"
transcript: "tmp/[English (auto-generated)] Atlas Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [autonomous-driving, ai-scientist, verifiable-research, simulation, human-in-the-loop]
---

# 讓自主變得自主:邁向可供發現與直覺的心智模型(Making Autonomy Autonomous: Toward Mental Models for Discovery and Intuition)

**一句話總結**:physical AI 的 edge case 永遠修不完,所以應該讓 agent 團隊自己跑「發現—實驗—驗證—寫論文」的迴圈;而讓這件事不淪為幻覺的關鍵,是每一個宣稱都能追溯到一次真實的 GPU run、一行真實的程式碼,而人類的角色則從執行者轉為提供**隱性專業知識**與**意圖**的一方。

**One-line summary**: Physical AI's edge cases never run out, so let a team of agents run the discover-experiment-validate-write loop themselves; what keeps that from being hallucination is that every claim traces back to a real GPU run and a real line of code — and the human's role shifts from executor to the source of *tacit expertise* and *intent*.

## 中文筆記

### TL;DR

- **問題設定**:physical AI 活在開放世界,部署後 edge case 無窮無盡,團隊得不斷跑「發現—開發」迴圈修它們,而且**每一次修補都必須有可追溯的釋出證據**。
- **三層迴圈**:**execution loop**(資料、模擬、DevOps 構成的**可驗證基底**)→ **discovery loop**(有根據的 ideation、驗證、可追溯性)→ **intent loop**(隱性專業、心智模型、可信歸因、共演化的夥伴關係)。
- **實證**:一組 agent 只拿到一句輸入(「產生改進 3DGS 以處理行人的點子,在某類 GPU 上測、在真實 benchmark 驗證、跟 baseline 比、發表論文」),就自行完成從選題到寫論文;**投稿 CVPR 2026 workshop 的 4 篇有 3 篇被接受**(被拒的那篇是公式格式問題)。
- **不是「會寫論文的系統」,而是「做可追溯、可驗證科學發現的系統」**:候選方法都是在**已驗證的重現實作**上突變,每個宣稱都能追到真實 log、真實程式碼行、真實 GPU run。

### 重點整理

#### 問題:開放世界的 edge case 修不完,但每次修補都要有證據(約 00:55–00:57)

他的起點是一個大家都會同意的事實:**physical AI 活在開放世界**,部署後不斷冒出 edge case,團隊得進入持續的發現與開發迴圈去修——而且**所有修補都必須帶著可追溯的釋出證據(traceable release evidence)**。

同時,物理世界正在**快速變得可執行(executable)**:CI/CD 框架能持續跑迴圈、agent 能部署程式碼、模擬能補上資料的缺口。這一切指向**自我改進**的未來。

但阻力也很實際:physical stack 很複雜,需要**真實世界的實驗**與大量真實世界知識;而**人的專業存在於靜態資料之外**——它體現在科學構想、專家工作流、以及與系統的物理互動裡。結論是:在物理工作流中做實驗與發現,需要大量算力、資料**與人才**。

他這場要談三件事:讓自主變得自主(與人協作)、**以執行為根據的發現框架**、把**人的意圖**反映進 agentic 工作流,並希望能在 AI 原生經濟中維持人的持續參與。

#### 示範:一句話輸入,一組 agent 交出一篇論文(約 00:57–00:59)

他用一個具體場景說明:某個自駕團隊發現**行人感知**有問題 → 交給模擬團隊 → 團隊判斷行人是細長結構、需要更好的 3D 重建 → 提出新的 Gaussian splatting 方法 → 在真實資料上驗證 → 最後寫成論文或 spec sheet。

「**如果我告訴你,這整個流程是由一組 agent 跑完的呢?**」開發者唯一的輸入是一句話:*產生改進 3DGS 以處理自駕行人的想法,在某個 GPU 家族上測試,在真實 benchmark 上驗證,與 baseline 比較,然後發表論文。*

這組 agent 扮演的角色有明確要求:產出**可驗證的**研究、部署**可執行的**程式碼、提出**以物理世界為根據的**想法,並遵循**可追溯、可驗證的**科學發現流程。

實際流程:輸入進來 → agent 定義要解的任務(這裡選定改進 NVIDIA 的 **OmniRe** 框架)→ 對可能改進的維度提出假設 → 專家 agent 各自啟動一批實驗 → 所有實驗在一個 **ELO 評分的錦標賽**中被驗證或證偽 → ELO 最高的那個想法存活下來,成為新方法,並且**是在真實 GPU 硬體上實作的,所以增益是可量測的** → 最後由 writer 與 reviewer agent 寫成論文。

**效果如何?** 他們挑了幾篇這樣產出的論文,在**取得主辦方同意**的前提下投稿到 CVPR 2026 的一個 physical AI 相關 workshop——「順帶一提,我們不是想鑽系統漏洞」。結果 **4 篇中有 3 篇被接受**,其中一篇獲得高度評價;被拒的那篇有**公式排版問題**,「所以我們認為審稿人在這件事上是對的」。

但他強調重點:**這不是一個「用來發想與寫論文」的系統,而是一個執行可追溯、可驗證科學發現的系統。**

#### 核心:可驗證基底(verifiable substrate)(約 00:59–01:02)

整套東西建立在一個**可驗證基底**上,由三件事構成:

1. **有根據的 ideation**:定義一套 **context-free grammar**,讓產生出來的想法是有根據的。
2. **在已驗證重現實作上突變**:每個候選方法都是在一個**已驗證的重現(verified reproduction)**之上做變異,所以一切都可量測、可驗證、可證偽。
3. **可追溯**:系統做出的每一個宣稱,都能追回一段真實 log、一行真實程式碼、一次真實 GPU run。

那這個基底怎麼建?**反向工程**:假設有一個知識庫、有論文,能不能反過來跑科學流程、把寫出這篇論文的程式碼生出來?他的例子是一篇**從未被公開實作過**的論文(「所以不是 Claude 或 GPT 已經知道這篇」):分析論文 → 判定新想法是什麼、哪些因素帶來相對 baseline 的改進 → 生出程式碼 → 對真實資料做**物理驗證** → 提出改進 → 在真實 benchmark 上與真實資料比較驗證。這就構成了發現可以站上去的可驗證基底。

那麼像自駕這種完整應用,執行迴圈長什麼樣?幸運的是他們這些年在自駕上已經累積了不少 agentic substrate:

- **data agent**:給定一批電腦視覺與機器學習工具,分析各種 edge case。
- **simulation agent**:給定使用者輸入(例如「讓一台車切入或切出」),重建 3D 背景、重建場景中所有動態 agent、部署 diffusion 模型生成新的反應式行為與困難 edge case,再由其他 diffusion 模型做**照片級渲染**。
- **development agent**:吃下 ODD 規格與現有的資料工具、模擬工具,執行 AI 模型的訓練與驗證。

#### 人的角色:從靜態資料到 intent loop(約 01:02–01:04)

「一旦我們有了這些**驅動自主的自主系統**,人的角色是什麼?」

他認為會出現新的迴圈:**資料從靜態走向互動**,我們開始能萃取**隱性專業(tacit expertise)**——那是關於**親身經驗**的把手,而親身經驗驅動的是**心智模型**,讓我們能推理的不只是專家**怎麼做**,還有專家**為什麼那樣做**。

從心智模型出來的**意圖**,接著驅動世界模型;而這些世界模型不再只依賴「聚合後的偏好」,而是帶有**可追溯的貢獻**。歸因機制帶來**可信任的採用**,可信任的採用再帶來**人在迴圈中的持續參與**。

心智模型怎麼建?把前面 discovery pipeline 的**所有 trace 吃進來**,用 claim-backed 的驗證方法轉成**證據(evidences)**,再把證據**蒸餾成信念(beliefs)**,而系統對**每一個信念的使用都帶有歸因**。

成效有兩類:

- **coding 任務**:能解更多任務、解得更好;更重要的是**更少的使用者介入、更少的 memory token、更少的 token 消耗**——這本質上指向更好的「使用者—系統對齊」。
- **物理任務**(例如 Gaussian splatting):心智模型可以採用不同的 **persona**——例如「品質 persona」與「速度 persona」——而這些 persona 是從發現迴圈裡長出來的,並且可被**可控地操縱(controllable steering)**。

總結他自己的三層架構:**execution loops**(資料、模擬、DevOps)構成可驗證基底 → 其上跑 **discovery loops**(有根據的 ideation、驗證、可追溯性)→ 再加上 **intent loops**(隱性專業、心智模型、可信歸因、最終走向共演化的夥伴關係)。

### 金句

> "Now what if I told you that this whole process is something that is run by a team of agents?"(約 00:57)

從「人做研究」翻轉到「agent 做研究」的那一句。

> "Every claim that is made by the system is something that we can trace to a real log or a real line of code, a real GPU run."(約 01:00)

這一句是整套主張的防線:可追溯性把「自動科學」和「自動幻覺」分開。

> "Mental models … allow us to reason about not just how experts act but why experts act."(約 01:03)

隱性專業的價值不在動作本身,而在動作背後的理由。

## English Notes

### TL;DR

- **The setup**: physical AI lives in the open world, edge cases keep arriving after deployment, teams run continuous discovery-and-development loops to fix them — and every fix must ship with **traceable release evidence**.
- **Three nested loops**: the **execution loop** (data, simulation, DevOps → a *verifiable substrate*), the **discovery loop** (grounded ideation, verification, traceability), and the **intent loop** (tacit expertise, mental models, trusted attribution, co-evolving partnerships).
- **The demonstration**: from a single line of developer input — *generate ideas to improve 3DGS for pedestrians in autonomous driving, test on this GPU family, validate on real benchmarks, compare to baselines, publish a paper* — a team of agents ran the whole pipeline. **Three of four submissions to a CVPR 2026 workshop were accepted** (the rejection had equation formatting problems).
- **The point isn't a paper-writing system** but a system doing traceable, verifiable scientific discovery: every candidate method mutates on top of a *verified reproduction*, and every claim traces back to a real log, a real line of code, a real GPU run.

### Key Points

#### The problem: endless edge cases, but every fix needs evidence (~00:55–00:57)

Physical AI lives in the open world. Edge cases arise endlessly after deployment, teams go into continuous discovery and development loops to fix them, and **all of it must be fixed with traceable release evidence.**

Meanwhile the physical world is rapidly becoming **executable**: CI/CD frameworks run loops continuously, agents deploy code, simulation bridges the gap to data. All of this points to a future of self-improvement.

The friction is real, though: physical stacks are complex and require real-world experimentation and real-world knowledge, and **human expertise lives beyond static data** — in scientific ideas, expert workflows, and physical interaction with systems. So experimentation and discovery in physical workflows demand a lot of compute, a lot of data, and a lot of human talent.

His three themes: making autonomy autonomous in collaboration with humans; discovery frameworks **grounded in execution**; and reflecting **human intent** in agentic workflows so people keep participating in AI-native economies.

#### The demonstration: one line in, a paper out (~00:57–00:59)

The scenario: an autonomous driving team observes a pedestrian perception issue → hands it to the simulation team → pedestrians are thin structures, so better 3D reconstruction is needed → the team proposes a new Gaussian splatting method → it's validated on real data → they write a paper or publish a spec sheet.

"**Now what if I told you that this whole process is something that is run by a team of agents?**" The only developer input is one instruction: generate ideas to improve 3DGS for pedestrians in autonomous driving, test on a particular family of GPUs, validate on real benchmarks, compare to baselines, and publish a paper.

The agents' roles carry explicit requirements: produce research that is **verifiable**, deploy code that is **executable**, ground ideas in the **physical world**, and follow a discovery process that is **traceable and verifiable**.

The flow: input arrives → agents define the task to be solved (here, improving NVIDIA's **OmniRe**) → they form hypotheses about dimensions where improvement is possible → specialist agents launch a set of experiments → all experiments are validated or falsified in an **Elo-rated tournament** → the highest-Elo idea survives as a new method, **implemented on real GPU hardware so the gains are measurable** → writer and reviewer agents produce a paper.

How good is it? They submitted several of these papers, **with the organizers' permission**, to a CVPR 2026 workshop on physical AI — "we're not trying to game the system." **Three of four were accepted**, one with high praise; the rejected one had formatting problems with its equations, "so we believe the reviewer, in this case."

The framing matters to him: **this is not a system for ideating and writing papers, it's a system performing traceable and verifiable scientific discovery.**

#### The verifiable substrate (~00:59–01:02)

Everything rests on a **verifiable substrate**, built from three commitments:

1. **Grounded ideation** — a **context-free grammar** constrains the ideas the system can generate.
2. **Mutation on verified reproductions** — every candidate method mutates on top of a verified reproduction, so everything is measurable, validatable, falsifiable.
3. **Traceability** — every claim traces to a real log, a real line of code, a real GPU run.

How do you build it? By **reverse-engineering** the process: given a knowledge repository and papers, can you follow the scientific process backwards to produce the code that wrote the paper? His example uses a paper that **has never been publicly implemented** ("so it's not like Claude or GPT knows about this paper"): analyze the paper → determine the new ideas and the factors that produce improvements over baselines → generate the code → **physically verify** it against real data → suggest improvements → validate on real benchmarks against real data.

For a full application like autonomous driving, the execution loops that build these substrates already exist from years of prior work:

- **Data agents** analyze edge cases given a toolbox of computer vision and machine learning tools.
- **Simulation agents** take user input ("get a car to change lanes, cut in or cut out"), reconstruct the 3D background and all dynamic agents in the scene, deploy diffusion models to generate novel reactive behaviors and challenging edge cases, and use further diffusion models for photorealistic rendering.
- **Development agents** take ODD specs plus the data and simulation tools and run AI model training and validation.

#### The human role: the intent loop (~01:02–01:04)

"Once we have these autonomous systems that are driving autonomy, what does it mean for the role of the human?"

He sees new loops opening up as **data moves from static to interactive**. We begin harnessing **tacit expertise**, which gives a handle on the lived experience behind expert behavior. Lived experience drives **mental models**, which let us reason about **not just how experts act but why they act**.

Intents drawn from those mental models then drive world models that no longer work from aggregated preferences alone but carry **traceable contributions**. Attribution mechanisms enable **trusted adoption**, which enables continuous human participation in the AI loop.

Building the mental models: ingest all traces from the discovery pipelines, convert them into **evidences** via claim-backed verification, distill evidences into **beliefs**, and attach **attribution to every use of every belief**.

Two payoffs. On **coding tasks**: more tasks solved, solved better — and importantly **fewer user interventions, fewer memory tokens, fewer tokens consumed**, which points at better user-system alignment. On **physical tasks** like Gaussian splatting: mental models can adopt different **personas** — a quality persona and a speed persona, say — which emerge from the discovery loop and can be steered controllably.

His summary of the architecture: **execution loops** built on data, simulation, and DevOps form the verifiable substrate; **discovery loops** run on top with grounded ideation, verification, and traceability; and **intent loops** add tacit expertise, mental models, trusted attribution, and eventually co-evolving partnerships.

### Quotes

> "Now what if I told you that this whole process is something that is run by a team of agents?" (~00:57)

The pivot from human research to agent research.

> "Every claim that is made by the system is something that we can trace to a real log or a real line of code, a real GPU run." (~01:00)

The line that separates automated science from automated hallucination.

> "Mental models … allow us to reason about not just how experts act but why experts act." (~01:03)

Tacit expertise is valuable for the reasons behind the actions, not the actions.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| OmniRe | NVIDIA 等單位的城市場景重建框架,agent 選定為改進標的 | Urban scene reconstruction framework (NVIDIA et al.) chosen by the agents as the improvement target | arXiv 2408.16760 — 以 Gaussian 表示建動態神經場景圖 / dynamic neural scene graphs over Gaussians |
| 3DGS (3D Gaussian Splatting) | 示範場景中要改進的重建方法(針對行人這類細長結構)| The reconstruction method the agents were asked to improve, specifically for thin structures like pedestrians | |
| ELO tournament | 用於驗證/證偽候選方法的評分機制,最高分的想法存活 | Rating mechanism used to validate/falsify candidate methods; the highest-rated idea survives | |
| Verifiable substrate | 由 context-free grammar、已驗證重現、可追溯宣稱三者構成的基底 | Substrate built from a context-free grammar, verified reproductions, and traceable claims | 全場的核心概念 / the talk's central concept |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Manmoan Chunractor / man moan | Manmohan Chandraker |
| Omnire | OmniRe |
| gshian splatting | Gaussian splatting |
| tacet expertise | tacit expertise |
| ideiating | ideating |
| OD specs | ODD specs(operational design domain) |
| CVPR26 | CVPR 2026 |

## 待確認 / To Verify

- 投稿的 CVPR 2026 workshop 正式名稱(講中只說「a CVPR26 workshop on physical AI 相關主題」)。/ The exact name of the CVPR 2026 physical-AI workshop the papers were submitted to.
- 這套 agentic discovery 系統本身是否有公開名稱、論文或 repo——台上未點名。/ Whether the agentic discovery system itself has a public name, paper, or repo — never stated on stage.
- 反向工程示範所用的「從未被公開實作過的論文」是哪一篇。/ Which paper was used in the reverse-engineering demo ("never been publicly implemented").
- 「更少 memory token / token 消耗」的具體數字未給。/ No numbers were given for the claimed reductions in interventions and token usage.
