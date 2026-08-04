---
title: "From Training to Evaluation: Open Recipes for Building Agentic AI at Scale AI"
title_zh: "從訓練到評估:Scale AI 打造 Agentic AI 的開放配方"
speaker: "Chenguang Wang"
affiliation: "Assistant Professor, UC Santa Cruz; Research Advisor, Scale AI"
type: talk
stage: Compass
date: 2026-08-02
session: "Session 4: Agent Evaluation & Benchmarks"
video: "https://www.youtube.com/watch?v=1UrriPJRSPU&t=7870s"
video_range: "02:11:10–02:24:04"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [post-training, rubric-based-rl, benchmarks, swe-agents, computer-use]
---

# 從訓練到評估:Scale AI 打造 Agentic AI 的開放配方(From Training to Evaluation: Open Recipes for Building Agentic AI at Scale AI)

**一句話總結**:RL 過去只在「可驗證領域」(數學、程式碼)有效,而 rubric-based reward 把開放領域的評分準則轉成可驗證訊號,讓 RL 走進科學與開放任務;同一套思維反過來也重塑評估——SWE-Atlas、drug discovery bench、合成長程 computer-use 任務,而訓練與評估之間的失敗模式回饋,是一個應該永遠轉下去的飛輪。
**One-line summary**: RL used to work only in verifiable domains like math and code; rubric-based rewards turn open-ended grading criteria into verification signals, pushing RL into science and open-ended tasks — and the same idea reshapes evaluation (SWE-Atlas, a drug discovery bench, synthetically generated long-horizon computer-use tasks), with failure modes flowing back into training as a flywheel meant to run forever.

## 中文筆記

### TL;DR

- **RL 的下一個邊界是「不可驗證領域」**:coding 和數學有 ground truth,可以直接判對錯;但 frontier labs 真正在乎的科學、開放式任務沒有 verifier。Scale AI 的做法是把評分準則(rubric)轉成驗證訊號,做出**基於 rubric 的 ranking-based reward model**,並用它推進 GRPO,在開放式任務上看到實質改善。
- **Online rubrics 是自然的延伸**:訓練中 policy 一直在變好,rubric 也該跟著變。比較 reference policy 與 current policy,找出目前 reward 沒抓到的東西、生成更好的 rubric 併回 reward model——講者說這條線和近期 recursive self-improvement 的趨勢高度一致。
- **SWE-bench 類 benchmark 太乾淨**:真實工程師不是看完 issue 就吐一個 patch,而是要寫單元測試、來回翻 repo、自問自答才知道下一步做什麼。因此 Scale 推出 **SWE-Atlas**,目前已被 frontier labs 廣泛採用。
- **CLI vs MCP 的爭論可能是假議題**:他們的結論是——**只要模型夠強(近期的 Claude 4.8、GPT-5.5/5.6 等級),而且後端相同,工具介面就不重要**,模型會自己學會用最好的那個介面。
- **Computer-use benchmark 太貴,那就合成**:以既有高品質 benchmark 為基底,生成更長程、更困難、更貼近真實的任務。效果是把 OSWorld 上 80%+ 的 SOTA 打回 **約 30%**——證明高品質的真實世界資料集是可以合成出來的。
- **最後的框架:訓練 ↔ 評估的飛輪**。從 post-training 的洞見去蓋更好的 RL 環境,從評估的失敗模式去改進 post-training 演算法。

### 重點整理

#### 定位與 Scale AI 背景(約 02:12–02:13)

Chenguang Wang 是 UC Santa Cruz 的助理教授,同時是 Scale AI 的 research advisor,與前一場的 Emily Xue 密切合作。他只有 10 分鐘,所以 post-training 只快速帶過,重點放在 evaluation,以及兩者之間的綜效。

Scale AI 的使命是「為世界上最重要的決策打造可靠的 AI 系統」,2016 年創立,目前規模相當大,在美國與其他國家設有辦公室。

#### Post-training:從 RLHF 走向 rubric-based RL(約 02:13–02:15)

Scale 目前的 post-training 研究主軸,是**從 RLHF 移動到 rubric-based RL**。這個判斷來自他們替 frontier labs 提供資料服務的實務——這是 post-training 真正重要的一塊。

挑戰有三層:**如何設計有效的 reward、如何把 reward 用進 RL、以及如何在 RL 訓練過程中讓 reward 本身變得更好**。相關成果發表在今年的 ICLR、ICML,也投了 NeurIPS。

具體上,他們用 rubric-based reward 的範式**推進了 GRPO 的邊界**,除了效能提升,也從訓練與資料的互動中萃取出配方——如何把「資料 ↔ RL」這個飛輪轉起來。

#### 為什麼 rubric-based reward 是關鍵(約 02:15–02:17)

他特別強調這一點:

**過去 RL 的主流戰場是「可驗證領域」(verifiable domains)**——coding、數學。這些領域你能明確知道答案是對是錯,有 ground-truth verification。

**但真實世界、frontier labs 真正在乎的,大多是沒有 verifier 的開放領域**——科學,或各種個人任務。所以必須找出方法讓 RL 在這些 open-ended domain 上運作。

他們的做法是建立一套範式:**把評估準則(criteria)轉換成驗證訊號**。由此建出的新 reward model 有一個關鍵差異——**它不是單純判斷「哪個回應比較好、哪個比較差」,而是基於 rubric 的 ranking**,因此能規模化到真實世界情境。

他們建了一條可靠的 pipeline:**從簡單的 rubric 起步,逐步養出高品質的 rubric,再把它用在 RL 階段**,並在開放式任務上觀察到實質的改善。

#### Online rubrics:reward 也要跟著 policy 進化(約 02:17–02:18)

這是第一項工作的自然延伸。核心觀察是:**訓練過程中 policy 一直在變,而且越變越好**——那麼固定的 rubric 就會逐漸跟不上。

做法是:同時持有一個 **reference policy** 與一個 **current policy**,找出**目前 reward 沒有捕捉到的東西**,據此生成更好的 rubric(**online rubric**),再把它整合回 reward model。這樣能訓出更好、對下游任務更 robust 的模型。

他指出這條「online rubric 演化」的路線,**與近期 self-improvement / recursive self-improvement 的研究趨勢高度一致**。

#### 評估:SWE-Atlas 與真實工程的樣子(約 02:18–02:20)

評估是 Scale 的主戰場:把訓練得到的洞見與客戶對話的洞見,轉成給 frontier 模型用的全球 leaderboard。

**SWE agents 的問題**:大家熟悉的 SWE-bench、SWE-bench Pro 的形式是——GitHub 上有一段問題的文字描述,agent 生成一個 patch 去修好原 repo 的 bug。

但他直接點出這與現實的落差:**真實世界髒得多**。工程師不是只看 PR 和 issue 就生出一個 patch;你得**寫單元測試**,有時候得**來回翻 repo、自己提問再自己回答**,才知道下一步該做什麼。

因此他們釋出了新的 benchmark **SWE-Atlas**,他說目前已被 frontier labs 廣泛採用。

#### 專業推理與 AI for Science(約 02:20–02:21)

- **HLE(Humanity's Last Exam)**:專業推理的代表性 benchmark,各家模型仍在持續 hill climbing。
- **Drug discovery bench**:目標是建構真實的醫療照護環境,由專家生成真實的藥物發現任務,**從概念出發,一路走到交付出藥物**。近期已釋出 preprint。

#### 工具介面之爭:CLI vs MCP(約 02:21)

這是一個現場很有共鳴的結論。他們研究「哪種工具介面比較好」,得到的高階結論是:

**一旦模型變得夠強——像近期的 Claude 4.8、GPT-5.5 或 5.6 這個等級——介面就不重要了。** 模型會自己學會盡可能用上最好的工具介面。前提是**你給它相同的後端**。換句話說,爭論 CLI 還是 MCP,可能問錯了問題。

#### Computer-use agents:用合成把 benchmark 變難(約 02:21–02:22)

benchmark computer-use agent 的困難在於**成本極高**——多模態模型、驗證細節多。

他們的解法是:**以既有的高品質 benchmark 為基底,合成生成更長程、更困難、更貼近真實的任務**。

效果非常明顯:**原本 OSWorld 上新版 Opus 的 SOTA 在 80% 以上,被壓回約 30%**。這證明了他的論點——**真實世界的資料集是可以合成出來的,而且能保持高品質**。

#### 收尾:訓練與評估的飛輪(約 02:22–02:23)

最後一張技術投影片講的是綜效:

- 從 **post-training 的洞見** → 打造更好的 **RL 環境**
- 從 **評估的失敗模式** → 改進 **post-training 演算法**

「希望這個迴圈可以永遠跑下去」——兩邊同時得到更好的 eval 與更好的訓練成果。

#### 結語與 workshop 預告(約 02:23)

Scale 目前與各家 frontier labs、政府、企業合作,也涉足 robotics 的 physical AI。

最後宣傳:第三屆 **Agents in the Wild** workshop 已獲 NeurIPS 接受,投稿截止在當月底;他是核心籌辦人之一,講者陣容包含 Dawn Song、Joshua 與 Jav(後兩位姓氏字幕不清)。

### 金句

> "In many real world cases where Frontier Labs really care about … it's not a verifiable domain. So we need to find out a way to make it work for those open-ended domains."(約 02:15)

整場 post-training 部分的動機:RL 必須離開數學與程式碼的舒適圈。

> "Once a model becomes really capable … the model will learn to use the best tool interface possible. So that really doesn't matter — unless you give the same backend."(約 02:21)

CLI vs MCP 之爭的降溫劑:能力夠強時,介面不是瓶頸,後端才是。

> "We can pretty much bring down the performance of the original OSWorld … from something definitely beyond 80% to something like 30%."(約 02:22)

合成的長程任務,直接把 computer-use 的 SOTA 打回原形。

## English Notes

### TL;DR

- **RL's next frontier is the non-verifiable domain.** Math and code have ground truth, so correctness is checkable; the science and open-ended tasks frontier labs actually care about have no verifier. Scale AI's answer is to turn grading criteria (rubrics) into verification signals, producing a **ranking-based reward model built from rubrics**, and using it to push GRPO forward with measurable gains on open-ended tasks.
- **Online rubrics are the natural extension.** The policy keeps improving during training, so the rubric should too: compare a reference policy against the current policy, find what the current reward is missing, generate better rubrics, and fold them back into the reward model. Wang notes this lines up closely with the recursive self-improvement research trend.
- **SWE-bench-style benchmarks are too clean.** A real engineer doesn't read an issue and emit a patch — they write unit tests, go back and forth through the repo, and ask and answer their own questions to work out the next step. Hence **SWE-Atlas**, which he says frontier labs have widely adopted.
- **The CLI vs MCP debate may be the wrong question.** Their finding: **once a model is capable enough (recent Claude 4.8, GPT-5.5/5.6 tier) and the backend is the same, the tool interface stops mattering** — the model learns to use whatever is best.
- **Computer-use benchmarks are expensive, so synthesize.** Building on existing high-quality benchmarks, they generate longer-horizon, harder, more realistic tasks — knocking the OSWorld state of the art from above 80% down to roughly **30%**, evidence that high-quality realistic datasets can be constructed synthetically.
- **The closing frame is a training ↔ evaluation flywheel**: post-training insights build better RL environments; evaluation failure modes improve post-training algorithms.

### Key Points

#### Positioning and Scale AI background (~02:12–02:13)

Wang is an assistant professor at UC Santa Cruz and a research advisor at Scale AI, working closely with Emily Xue (the previous speaker). With only 10 minutes, he covered post-training briefly and spent most of the talk on evaluation and the synergy between the two.

Scale AI's mission is to build reliable AI systems for the world's most important decisions. Founded in 2016, now large, with offices in the US and other countries.

#### Post-training: from RLHF to rubric-based RL (~02:13–02:15)

Scale's current post-training research thrust is **moving from RLHF to rubric-based RL** — a direction that came out of providing data services to frontier labs, where it emerged as genuinely important.

Three layers of challenge: **how to design an effective reward, how to use that reward with RL, and how to make the reward itself better during RL training.** Results have appeared at ICLR and ICML this year, with NeurIPS submissions pending.

Concretely, they **pushed the boundary of GRPO** using a rubric-based reward paradigm — improving performance, and extracting recipes for spinning the data ↔ RL flywheel.

#### Why rubric-based rewards are the key move (~02:15–02:17)

This was the point he most wanted to land.

**RL's traditional battleground has been verifiable domains** — coding, math. There you know whether an answer is true or false; you have ground-truth verification.

**But most of what matters in the real world, and to frontier labs, is open-ended and has no verifier** — science, or personal tasks of all kinds. So a way had to be found to make RL work in those domains.

Their approach: set up a paradigm that **turns evaluation criteria into verification**. The reward model built this way has one crucial difference — **it isn't just distinguishing a better response from a worse one; it ranks, based on rubrics** — which is what lets it scale to real-world scenarios.

The pipeline: **start simple, gradually build a very high-quality rubric, then use it in the RL phase** — with improvements observed on open-ended tasks.

#### Online rubrics: rewards that evolve with the policy (~02:17–02:18)

A natural extension of the first work. The observation is that **the policy keeps changing and improving during training**, so a fixed rubric progressively falls behind.

The method: hold a **reference policy** alongside the **current policy**, identify **what the current reward is failing to capture**, generate a better rubric from that gap (an **online rubric**), and integrate it back into the reward model — yielding a better-trained model that's more robust on downstream tasks.

He flagged that this online-rubric evolution **aligns closely with the recent self-improvement / recursive self-improvement line of work.**

#### Evaluation: SWE-Atlas and what real engineering looks like (~02:18–02:20)

Evaluation is Scale's main focus: turn insights from training and customer conversations into worldwide leaderboards for frontier models.

**The problem with SWE agent benchmarks**: SWE-bench and SWE-bench Pro give you a text description of a problem from GitHub and ask the agent to produce a patch that fixes the bug in the original repo.

His objection is that **the real world is far messier**. Engineers don't just read the PR and the issue and emit a patch — you have to **write unit tests**, and sometimes **go back and forth through the repo, asking questions and answering them** before you know what to do next.

So they released **SWE-Atlas**, which he says is now widely adopted by frontier labs.

#### Professional reasoning and AI for science (~02:20–02:21)

- **HLE (Humanity's Last Exam)** as the representative professional-reasoning benchmark, with model families still hill-climbing on it.
- **A drug discovery bench**: building a genuine healthcare environment where experts generate real drug-discovery tasks that run **from the initial concept all the way to delivering the drug**. A preprint was released recently.

#### The tool interface debate: CLI vs MCP (~02:21)

A conclusion that clearly resonated in the room. Their high-level finding on which tool interface is better:

**Once the model becomes capable enough — the recent Claude 4.8, GPT-5.5 or 5.6 tier — the interface stops mattering.** The model learns to use the best available tool interface on its own. The caveat: **you have to give it the same backend.** In other words, arguing CLI versus MCP may be the wrong question.

#### Computer-use agents: making benchmarks harder by synthesis (~02:21–02:22)

Benchmarking computer-use agents is hard because it's **very expensive to run** — multimodal models, plus a long tail of verification details.

Their answer: **take existing high-quality benchmarks as a base and synthetically generate longer-horizon, more challenging, more realistic tasks from them.**

The effect is dramatic: **on OSWorld, where a new Opus version's state of the art sits comfortably above 80%, the generated tasks drove it down to about 30%.** Evidence for his claim that realistic datasets can be constructed synthetically while staying high quality.

#### Closing: the training–evaluation flywheel (~02:22–02:23)

His last technical slide was about synergy:

- From **post-training insights** → build better **RL environments**
- From **evaluation failure modes** → improve **post-training algorithms**

"Hopefully this can run forever" — with both better evals and better training results falling out of the loop.

#### Wrap-up and workshop plug (~02:23)

Scale works with frontier labs, governments, and enterprises, and is active in robotics and physical AI.

He closed by promoting the third edition of the **Agents in the Wild** workshop, accepted at NeurIPS, with a submission deadline at the end of that month. He is one of the core organizers; the panelist lineup includes Dawn Song plus two speakers whose surnames the captions garble (heard as "Joshua" and "Jav").

### Quotes

> "In many real world cases where Frontier Labs really care about … it's not a verifiable domain. So we need to find out a way to make it work for those open-ended domains." (~02:15)

The motivation for the entire post-training half: RL has to leave the comfort of math and code.

> "Once a model becomes really capable … the model will learn to use the best tool interface possible. So that really doesn't matter — unless you give the same backend." (~02:21)

A cooling agent for the CLI-vs-MCP argument: at sufficient capability, the interface isn't the bottleneck; the backend is.

> "We can pretty much bring down the performance of the original OSWorld … from something definitely beyond 80% to something like 30%." (~02:22)

Synthetically generated long-horizon tasks strip computer-use agents back down to size.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| SWE-Atlas | Scale 推出的 SWE agent benchmark,涵蓋 issue 修補以外的真實工程流程 | Scale's SWE agent benchmark covering real engineering work beyond issue resolution | 已開源(scaleapi/SWE-Atlas),含 Codebase QnA、Test Writing、Refactoring 三個 leaderboard / open-sourced with three leaderboards |
| SWE-bench / SWE-bench Pro | 作為對照的既有 SWE benchmark | Prior SWE benchmarks cited as the contrast | |
| HLE (Humanity's Last Exam) | 專業推理 benchmark | Professional-reasoning benchmark | 字幕聽作 "hie" / heard as "hie" |
| Drug discovery bench | 真實藥物發現任務的 agent benchmark,已有 preprint | Agent benchmark of real drug-discovery tasks; preprint released | Scale Labs 有 "DrugDiscoveryBench: Can Coding Agents Assist Early-Stage Drug Discovery?"(2026/06/30),應為同一項工作但未於演講中點名 / likely the same work, not named on stage |
| OSWorld | 被用來合成更難任務的 computer-use benchmark 基底 | Computer-use benchmark used as the base for synthesizing harder tasks | |
| GRPO | 被 rubric-based reward 推進的 RL 演算法 | The RL algorithm advanced with rubric-based rewards | |
| Agents in the Wild(第三屆 / 3rd edition) | NeurIPS workshop,講者為核心籌辦人 | NeurIPS workshop; speaker is a core organizer | 投稿截止當月底 / deadline end of the month |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Jen Wuang Wang / Chinua | Chenguang Wang |
| University of Santa California, Santa Cruz | UC Santa Cruz |
| Rubik's / Rubik / rubik | rubric / rubrics |
| gRPO | GRPO |
| su bench / sway bench / sway agents | SWE-bench / SWE agents |
| su atlas | SWE-Atlas |
| hie | HLE (Humanity's Last Exam) |
| two use / two interface | tool use / tool interface |
| marty model | multimodal |
| OS world | OSWorld |
| cloud 4.8 | Claude 4.8 |
| GPT 4 5 5.5 or 5.6 | GPT-5.5 / GPT-5.6 |
| I clear / SML | ICLR / ICML |
| new rips | NeurIPS |
| agency in the wild | Agents in the Wild |
| Don | Dawn Song |
| RL freeze / RL phrase | RL phase |

## 待確認 / To Verify

- 藥物發現 benchmark 的正式名稱(演講未點名;Scale Labs 於 2026/06/30 發布 DrugDiscoveryBench,需確認是否為同一項)。/ Formal name of the drug discovery bench — not named on stage; Scale Labs published DrugDiscoveryBench on 2026-06-30, needs confirming as the same work.
- rubric-based reward 與 online rubrics 兩篇論文的正式篇名與發表場次(他只說 ICLR / ICML / NeurIPS 投稿中)。/ Formal titles and venues of the rubric-based reward and online rubric papers.
- Agents in the Wild workshop 的 panel 講者「Joshua」與「Jav」的全名。/ Full names of the "Joshua" and "Jav" panelists.
- 演講結尾「see you guys at Sly」的地名(NeurIPS 2026 舉辦地),字幕不清。/ The venue name at the end ("see you guys at Sly") — the NeurIPS 2026 location, garbled in the captions.
- CLI vs MCP 結論所依據的實驗與是否有公開報告。/ The experiment behind the CLI-vs-MCP conclusion and whether it is published.
