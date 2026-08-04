---
title: "Measuring API Agent Reliability for Long-Horizon Tasks in Production"
title_zh: "衡量 API Agent 在生產環境長程任務中的可靠度"
speaker: "Zelin Wan"
affiliation: "Senior AI Engineer, Postman"
type: talk
stage: Compass
date: 2026-08-02
session: "Session 4: Agent Evaluation & Benchmarks"
video: "https://www.youtube.com/watch?v=1UrriPJRSPU&t=8644s"
video_range: "02:24:04–02:34:28"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [benchmarks, api-agents, long-horizon, evaluation, synthetic-data]
---

# 衡量 API Agent 在生產環境長程任務中的可靠度(Measuring API Agent Reliability for Long-Horizon Tasks in Production)

**一句話總結**:單一 API 任務上所有模型都拿 88–97%,看起來問題已解決;但把同樣的任務串成互相依賴的長鏈,分數立刻掉到 44–73%——任務本身沒有變難,是**早期的一個小錯會被後續步驟放大成整份報告的崩潰**,而這正是「回答問題」與「執行任務」的差別。
**One-line summary**: On single API tasks every model scores 88–97%, which looks like a solved problem; chain those same tasks into a dependent sequence and scores collapse to 44–73%. The tasks didn't get harder — **one small early mistake gets amplified downstream into a broken result**, which is exactly the difference between answering and executing.

## 中文筆記

### TL;DR

- **單一任務的高分是假象**:APIFlow-Bench 上,即使是輕量模型在單一 API 任務也有 88–97% 通過率;一旦串成依賴鏈,同樣的子任務組合起來只剩 44–73%。**難度沒變,變的是錯誤會不會被繼承**。
- **把 API 工作拆成七種失敗模式分別評分**:authentication、discovery、schema repair、multi-step execution、error recovery、pagination、statefulness。分開評分才知道模型**為什麼**失敗——step 3 沒存狀態害 step 15 失敗,和 pagination 處理不好,是完全不同的病。
- **合成任務必須設「硬性關卡」才可信**:三道 gate——self-testing(空白提交與被破壞的證據都必須失敗)、solvability(frontier 模型試 10 次至少過 3 次才收)、golden replay(把各子任務的參考答案串起來重放,整條鏈必須全過)。
- **確定性 validator 與 LLM validator 兩者都要**:兩個確定性驗證器(環境最終狀態 + 最終答案)決定 leaderboard 分數;LLM validator 不計分,專門標記可疑的通過案例交給人審。**驗證器錯了,模型的真實能力就永遠測不出來。**

### 重點整理

#### 問題:企業把商業邏輯包在 API 裡,現在把 agent 接了上去(約 02:24–02:26)

Zelin Wan 是 Postman 的工程師,這場介紹他們的 benchmark **APIFlow-Bench**。

企業用 AI agent 執行長程任務時,已經在面對一個具體問題:**agent 在早期犯的一個小錯,會讓整件事整個失敗**。而工程師實際在做的事情長這樣——把一個 build job 接到 monitoring API、建立一筆紀錄、或從 rate limit 中復原。這些任務類型就是 benchmark 的取材來源。

他們的核心發現非常乾脆:

| 任務型態 | 模型表現 |
|---------|---------|
| 單一 API 任務 | **88%–97%**(連輕量模型都很好) |
| 串成長程依賴鏈 | **44%–73%** |

他強調關鍵:**任務本身沒有變難。是當後面的任務依賴前面任務的結果時,模型才開始失敗。**

在企業裡,大量商業邏輯被包在 API 中,而現在我們正把 AI agent 接進這些 API。**AI 造成的一個小錯,會在後期變成一個大問題。**

所以真正的問題不是「模型能不能回答問題」——那件事大家都知道可以了。真正的問題是:**AI agent 能不能在一條長程依賴鏈上一路保持正確?這就是「回答」與「執行」的差別。**

#### 七種失敗模式,分開評分(約 02:27)

一兩種 failure mode 不夠,他們要的是**能涵蓋真實 API 工作的最小集合**。因此把 API 工作拆成七種失敗模式,**各自獨立評分**:

1. authentication(認證)
2. discovery(探索)
3. schema repair(schema 修復)
4. multi-step execution(多步驟執行)
5. error recovery(錯誤復原)
6. pagination(分頁)
7. statefulness(狀態保持)

為什麼要分開?他舉 statefulness 的例子:**agent 在第 3 步更新了某個東西,而第 15 步只有在 agent 當初確實存下那個更新時才會成功。** 一個在 statefulness 上失敗的模型,和一個在 pagination 上失敗的模型,失敗原因完全不同。分開評分,才能告訴你**模型為什麼失敗**,而不只是失敗了。

#### 任務生成 pipeline 與 fixer agent(約 02:27–02:29)

他們用內部資料近似真實使用者的 workflow,建出一套**模擬的企業 API 生態系**(模仿真實公司的 API),再在上面生成任務。

pipeline 從 step 0 的「企業 API 生態系生成」開始,接著九個步驟逐一生成任務。**每個生成的任務都要通過驗證**:

- 用 frontier 模型對每個任務嘗試 **10 次**,**至少通過 3 次**才保留。
- 理由很實際:**用語言模型生成的任務,有些根本無解**。你不會想拿一堆無解任務去評估 frontier 模型,然後宣稱那就是模型的極限。
- 任務沒通過驗證怎麼辦?把**嘗試的 transcript 與程式碼餵給一個 fixer agent**,由它修正任務,再跑一次那 10 次嘗試。若持續失敗,就整個丟掉重新生成。

#### Harness 與三個 validator(約 02:29–02:30)

benchmark 由四塊組成:一套 API 生態系、蓋在上面的任務、**一個共用 harness**、以及為每次 trial 評分的 grader。

- **Harness**:設計了 **7 個工具**,作用在 **5 種不同的 entity**。每個任務、每次 trial 都跑在同一個 harness 上,差別只在生態系與 grader 不同。
- **三個 validator**:
  - **兩個確定性 validator**——一個檢查**環境的最終狀態**,一個檢查 **agent 給出的最終答案**。這兩個決定 leaderboard 上看到的 pass rate。
  - **一個 LLM validator**——**不計入分數**,用途是標記「可疑的通過」,交給人類複核。

#### 三道 gate:讓生成的任務值得信任(約 02:30–02:31)

每道 gate 擋掉任務生成過程中不同類型的失敗:

1. **Self-testing**:**空白提交必須永遠失敗**;而拿參考答案但把證據破壞掉,**也必須失敗**。否則就代表任務本身或 validator 有問題。
2. **Solvability**:就是前面提到的——frontier 模型試 10 次、至少 3 次通過才收。
3. **Golden replay**:建構鏈式任務時,**把各子任務的參考答案全部串起來、接進這條鏈式任務,結果必須全部通過**。這樣才能確認組出來的最終鏈是正確的、如預期運作的。

#### 實驗規模與結果(約 02:31–02:32)

- **467 個任務**,最終產出 20 步的長鏈任務
- **19 個模型**,每個模型每個任務跑 **5 次 trial**
- 合計約 **44,000 次 trial**,**所有 transcript 都公開在 leaderboard 上**
- 下一版計畫擴增任務數量與鏈的長度

**Leaderboard 結果**(20 步鏈式任務):**GPT-5.5 居首**;橘色長條是開源模型,紫色是閉源模型。他提到 leaderboard 在演講當週剛更新,**已納入 Kimi K3 與 Fable 5**。

**一個有意思的發現**:此時此刻,**開源模型已經逼近閉源模型的頂端集團**——在他們的 bench 上,GLM 與 Qwen 3.7 拿下第二與第三名。

#### 三個 takeaway(約 02:32–02:33)

1. **單一任務已經無法區分模型**。所有模型(包括輕量模型)在 solo 任務上都拿高分,**看不出差距**——這正是他們建構鏈式測試去逼出極限的原因。他們反覆看到:**模型在早期犯一個極小的錯,那個小錯到後面就變成一份壞掉的報告。**
2. **生成合成任務時,一定要用硬性 gate 確保任務可信**。例如「10 次嘗試至少 3 次通過」;再加上 **golden replay** 確認你的參考答案真的能跑。他也鼓勵大家自己發展更多方法。
3. **確定性 validator 與 LLM validator 兩者都需要**。而且建立 validator / grader 時**務必 human-in-the-loop 持續打磨**——因為**一個錯的 validator,永遠測不出模型的真實能力**。

blog 與 leaderboard 都在 blog.postman.com。

### 金句

> "So the task itself didn't get harder. But if the later task is depend on the results of the previous task … then that's where the model start to fail."(約 02:26)

整場的核心診斷:崩潰的來源是依賴,不是難度。

> "The real problem is: can the AI agent stay correct across a long horizon of dependent chain tasks? That's the difference between answering and executing."(約 02:26)

> "We don't want to generate a bunch of unsolvable tasks and then use those to evaluate frontier models and claim that's the limit of the models."(約 02:28)

合成 benchmark 的誠實原則:先證明題目有解,再用它下結論。

> "A wrong validator cannot reveal the true performance of the models."(約 02:33)

驗證器本身也需要被驗證。

## English Notes

### TL;DR

- **High single-task scores are an illusion.** On APIFlow-Bench even lightweight models pass 88–97% of single API tasks; chain the same subtasks into a dependent sequence and the score falls to 44–73%. **The difficulty didn't change — what changed is whether errors get inherited.**
- **API work is decomposed into seven failure modes, graded separately**: authentication, discovery, schema repair, multi-step execution, error recovery, pagination, and statefulness. Separate grading is what tells you *why* a model failed — failing to persist state at step 3 so step 15 breaks is a completely different illness from mishandling pagination.
- **Synthetic tasks need hard gates to be trustworthy.** Three of them: self-testing (a blank submission and a sabotaged-evidence reference answer must both fail), solvability (a frontier model gets 10 attempts and the task is kept only if at least 3 pass), and golden replay (concatenate every subtask's reference answer into the chain and the whole thing must pass).
- **You need both deterministic and LLM validators.** Two deterministic validators — final environment state and final answer — produce the leaderboard score; the LLM validator doesn't score but flags doubtful passes for human review. **A wrong validator can never reveal a model's true performance.**

### Key Points

#### The problem: enterprise logic lives in APIs, and agents are now wired into it (~02:24–02:26)

Wan, an engineer at Postman, presented their benchmark **APIFlow-Bench**.

Enterprises running AI agents on long-horizon tasks already face a concrete failure: **a small mistake the agent makes early can fail the entire task.** And the work engineers actually do looks like this — connecting a build job to a monitoring API, creating a record, recovering from a rate limit. Those task shapes are what the benchmark draws from.

The headline finding is blunt:

| Task shape | Model performance |
|-----------|------------------|
| Single API task | **88%–97%** (even lightweight models do well) |
| Long dependent chain | **44%–73%** |

His emphasis: **the task itself didn't get harder. Models start failing precisely when a later task depends on an earlier task's result.**

In the enterprise, a great deal of business logic is wrapped in APIs, and AI agents are now being wired into those APIs. **A small AI-caused error becomes a big problem later on.**

So the real question isn't whether a model can answer questions — everyone knows it can. It's **whether an AI agent can stay correct across a long horizon of dependent chained tasks. That's the difference between answering and executing.**

#### Seven failure modes, graded separately (~02:27)

One or two failure modes isn't enough; they wanted **a minimal set that covers real API work.** So API work is broken into seven failure modes, each **graded on its own**:

1. authentication
2. discovery
3. schema repair
4. multi-step execution
5. error recovery
6. pagination
7. statefulness

Why separate? His statefulness example: **the agent updates something at step 3, and step 15 only works if that update was actually saved back at step 3.** A model that fails on statefulness fails for entirely different reasons than one that fails on pagination. Grading them apart is what tells you **why** a model failed rather than just that it did.

#### Task generation pipeline and the fixer agent (~02:27–02:29)

They approximate real user workflows using internal data and build a **simulated enterprise API ecosystem** that mimics a real company's APIs, then generate tasks on top of it.

The pipeline starts at step zero with enterprise API ecosystem generation, then walks through nine steps generating tasks one at a time. **Every generated task passes through validation:**

- A frontier model attempts each task **10 times**; the task is kept only if **at least 3 attempts pass.**
- The reasoning is practical: **some LLM-generated tasks simply aren't solvable at all.** You don't want to evaluate frontier models on a pile of unsolvable tasks and then claim you've found the limit of those models.
- When a task fails validation, **the trial transcript and code go to a fixer agent**, which repairs the task, and the 10 trials rerun. If it keeps failing, the task is discarded and regenerated from scratch.

#### The harness and three validators (~02:29–02:30)

The benchmark is four pieces: an API ecosystem, tasks built on it, **one shared harness**, and graders that score each trial.

- **Harness**: **7 tools** operating on **5 different entity types**. Every task and every trial runs on the same harness — only the ecosystem and graders differ.
- **Three validators**:
  - **Two deterministic** — one checks the **final state of the environment**, one checks the **final answer the agent produced**. These two generate the pass rate you see on the leaderboard.
  - **One LLM validator** — **not part of the score**, used to flag doubtful passes so a human can review them.

#### Three gates for trustworthy generated tasks (~02:30–02:31)

Each gate catches a different failure of the generation process:

1. **Self-testing**: a **blank submission must always fail**, and taking the reference answer while sabotaging the evidence **must also fail**. Otherwise something is wrong with the task or the validator.
2. **Solvability**: the frontier model's 10 attempts with a minimum of 3 passes, as above.
3. **Golden replay**: when building a chain task, **concatenate all the reference answers from each subtask, append them into the chain, and the whole thing must pass** — confirming the assembled chain is correct and behaves as intended.

#### Scale and results (~02:31–02:32)

- **467 tasks**, yielding 20-step long-chain tasks
- **19 models**, **5 trials** per model per task
- Roughly **44,000 trials** total, with **every transcript published on the leaderboard**
- Next version will expand both task count and chain length

**Leaderboard results** on the 20-step chain tasks: **GPT-5.5 on top**; orange bars are open-source models, purple are closed. He noted the leaderboard had been refreshed that week to include **Kimi K3 and Fable 5**.

**One notable finding**: as of now, **open-source models are approaching the top group of closed models** — on their bench, GLM and Qwen 3.7 land in second and third place.

#### Three takeaways (~02:32–02:33)

1. **Single tasks no longer separate models.** Everything, including lightweight models, scores high on solo tasks, so **the gap stays invisible** — which is exactly why they built chain tests to find the ceiling. What they saw repeatedly: **a model makes one tiny mistake early, and that tiny mistake becomes a broken report later.**
2. **When generating synthetic tasks, always use hard gates.** For instance, 10 trials with at least 3 passes; plus golden replay to verify your reference answer actually works. He encouraged the audience to invent more of their own.
3. **You need both deterministic and LLM validators**, and when building a validator or grader, **keep a human in the loop polishing it** — because **a wrong validator cannot reveal the true performance of the models.**

Blog and leaderboard are at blog.postman.com.

### Quotes

> "So the task itself didn't get harder. But if the later task is depend on the results of the previous task … then that's where the model start to fail." (~02:26)

The core diagnosis: the collapse comes from dependency, not difficulty.

> "The real problem is: can the AI agent stay correct across a long horizon of dependent chain tasks? That's the difference between answering and executing." (~02:26)

> "We don't want to generate a bunch of unsolvable tasks and then use those to evaluate frontier models and claim that's the limit of the models." (~02:28)

The honesty principle for synthetic benchmarks: prove the question is answerable before drawing conclusions from it.

> "A wrong validator cannot reveal the true performance of the models." (~02:33)

The validator itself needs validating.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| APIFlow-Bench | Postman 的企業 API agent benchmark,含 20 步依賴鏈任務與公開 leaderboard | Postman's enterprise API agent benchmark with 20-step dependent chain tasks and a public leaderboard | blog.postman.com/apiflow-bench;公開 leaderboard 與全部 trial transcripts / public leaderboard plus full trial transcripts |
| APIFlow-Bench 逐筆 transcripts | 全部 trial 的原始紀錄 | Raw transcripts for every trial | GitHub: postmanlabs/apiflow-bench-transcripts |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Jayen Juan / "this is one" | Zelin Wan |
| API flow bench | APIFlow-Bench |
| the line model | the light model |
| pagionation / pagenation | pagination |
| the stiffness / Stephan | statefulness |
| greater / gradient | grader / grade |
| gay(第二道關卡)| gate |
| subtage the evidence | sabotage the evidence |
| readerboard / leadable | leaderboard |
| GBD 5.5 | GPT-5.5 |
| Kim K3 | Kimi K3 |
| Fab Five | Fable 5 |
| GRM | GLM |
| QN 3.7 | Qwen 3.7 |
| synced task | synthetic task |
| hard / hart(gate)| hard gate |
| 467 t test | 467 tasks |

## 待確認 / To Verify

- 「467 tasks across 13 …」中的「13」所指為何(字幕聽作 "13 general world",可能是 13 條通用 workflow)。/ What the "13" refers to in "467 tasks across 13 …" (captions give "13 general world", possibly 13 general workflows).
- 467 個任務中依賴鏈與獨立子任務的拆分比例(公開資料顯示為 226 條依賴鏈 + 241 個獨立子任務,演講中未說明)。/ The chain-vs-standalone split of the 467 tasks — public materials indicate 226 dependent chains plus 241 standalone subtasks, not stated on stage.
- 開源模型第二、三名的正式型號(字幕聽作 "GRM" 與 "QN 3.7 plus")。/ Exact model identifiers for the second- and third-place open-source models (captions give "GRM" and "QN 3.7 plus").
- 演講當週更新後的 leaderboard 模型總數與 trial 總數(演講引用的是發布時的 19 模型 / 約 44,000 trials)。/ Post-update model and trial counts — the talk quotes the launch figures of 19 models and ~44,000 trials.
