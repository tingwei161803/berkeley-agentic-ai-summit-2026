---
title: "Enterprise AI"
title_zh: "企業 AI:為什麼 eval 是部署的瓶頸"
speaker: "Adarsh Hiremath"
affiliation: "Co-CEO, Mercor"
type: talk
stage: Plenary
date: 2026-08-02
session: "Session 1: Enterprise AI"
video: "https://www.youtube.com/watch?v=UdS3iisKhCk&t=2499s"
video_range: "00:41:39–00:50:54"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 2nd - Morning Session [DownSub.com].srt"
status: draft
tags: [enterprise, evaluation, mercor, agentic-eval, data]
---

# 企業 AI:為什麼 eval 是部署的瓶頸(Enterprise AI)

**一句話總結**:每家公司都想「擁有自己的智慧」,但不管你是訓練自家模型還是替前沿模型打造 harness,共同的前提都是一套好的 eval;而大多數企業 AI 專案進不了 production,正是因為沒有辦法衡量 ground truth,只能靠猜測與軼事在迴圈裡打轉。
**One-line summary**: Every company now wants to own its own intelligence, but whether you train your own model or engineer a harness around a frontier one, the common prerequisite is a good eval — and most enterprise AI projects never reach production precisely because there is no way to measure ground truth, leaving teams guessing and iterating on anecdotes.

## 中文筆記

### TL;DR

- **「擁有自己的智慧」有兩條路**:訓練自己的模型(如 Cursor 的 Composer,再用 Cursor 自家資料與基礎設施微調),或用前沿模型 + 為自家產品打造極好的 harness。**兩條路的共同前提都是一套非常好的 eval。**
- **失敗的迴圈長這樣**:沒有系統性方法找出 agent 機會 → 猜一個起點 → 臆測 agent 該有的行為 → 部署 → 在 sandbox 大致試一下、假設它可以動 → 靠零星或軼事式的失敗來改。這正是多數企業 AI 用例進不了 production 的原因。
- **agentic eval 的五個組成**(從 Mercor 的前沿 benchmark **APEX** 移植到企業情境):**task**(agent 到底在做什麼)、**trajectory**(它的推理與呼叫過程)、**artifact**(它產出的東西)、**world / context**(它穿行的環境)、**rubric / verifier**(評分標準)。
- **人的判斷在打分那一步不可取代**——這是 Mercor 商業模式的核心信念之一。
- **eval 的四層價值**:(1) 系統性、量化地找出公司裡最該部署 agent 的前五個領域;(2) 真的把 agent 部署下去並教會它「什麼叫做好」;(3) 持續學習的地基——失敗可以往上 triage 到 skills file 保證不再犯,也可以拿來 post-train 防止回歸;(4) **資料變現**——task / trajectory / context / artifact / rubric 這整套骨架,對前沿實驗室的訓練來說是極有價值的資料。

### 重點整理

#### Mercor 的起點與 2026 的轉向(約 00:42–00:44)

他 19 歲、Harvard 二年級時創辦 Mercor,從 Harvard 輟學;共同創辦人是高中辯論隊隊友(其中一位是他當年的辯論搭檔)。

公司最早是**把資料賣給 AI 實驗室**。驅動這件事的核心洞察是:模型已經進步到「標註一張圖裡有沒有停止標誌」不再是重點,問題變成「能不能讓模型更會做工程、更會做醫療任務、更會做法律」——**這需要非常高階的人類專業知識**,以及把資料結構化成適合 agentic 典範(RL 環境與 gym)的能力。

但 2026 年 Mercor 的主戰場是**企業**,這點很多人不知道。他的分層是:最底層是實驗室;上面是 neolabs;再上面是應用層公司與新創(他點名 Harvey 與 Cursor);最上面是一般企業。**這四層全都想擁有自己的智慧**、把它應用到整家公司、訓練自己的模型——而他們需要的東西根本是同一套:**訓練與 eval**。

#### 擁有自己的智慧:兩條路,一個共同前提(約 00:44–00:45)

1. **訓練自己的模型**。他舉 Cursor 為例:Cursor 訓練了自家的 Composer 模型(現在是相當好的 coding model),並能用 Cursor 的資料與基礎設施持續微調。
2. **採用前沿模型,然後為產品或用例打造非常好的 harness**。很多公司走這條。

**兩條路的共同線索是:你需要一套非常好的 eval。** 這就是 Mercor 切入的位置,而且直接建立在他們替實驗室做的工作與前沿 benchmark **APEX** 之上。

#### 為什麼企業 AI 進不了 production(約 00:45–00:46)

不論是訓練外部 agent 用的模型,還是在公司內部部署 agent,**最大的問題是沒有辦法衡量 ground truth 或成功**。於是形成他稱為「猜謎迴圈」的東西:

> 沒有系統性方法辨識產品裡的 agent 機會 → 隨便猜一個起點 → 臆測 agent 的行為 → 部署 → 在 sandbox 之類的地方試一下、假設它大概能動 → 根據零星觀察到的、軼事性的失敗來改進。

「這個迴圈真的非常糟」,所以他們主張**eval-driven 的企業 AI 部署**。

#### 什麼是 agentic eval:五個組成(約 00:46–00:48)

eval 是個被過度使用的詞,所以他直接從 APEX 的定義往企業情境延伸。跟實驗室合作時,新的前沿模型出來,他們會在許多領域的許多任務上跑 benchmark;agentic 用例裡模型往往要跑上百個 turn,而他們**分析整條 trajectory 來找出模型在哪裡失敗、為什麼失敗**。

同一套結構可以搬到企業:

| # | 組成 | 問的問題 |
|---|------|----------|
| 1 | **Task** | agent 實際上在做什麼? |
| 2 | **Trajectory** | 它用了什麼推理與理由? |
| 3 | **Artifact** | 它實際產出了什麼? |
| 4 | **World / Context** | 這個 agent 穿行的是什麼環境? |
| 5 | **Rubric / Verifier** | 怎麼判斷做得對不對? |

**實例(投資銀行任務)**:banker 對模型說「更新這份併購模型,顯示這筆交易如何影響雙方公司」。人工做的話,你會進 Excel、打開某份 merger model、進 data room、拿回饋、發現弄錯再查、最後產出模型。要讓 agent 做這件事,你需要對上述每一步都有可觀測性:

- **task** = 更新 merger model
- **trajectory** = agent 呼叫的所有工具(找到 merger model、更新交易條款、建表⋯)
- **artifact** = 帶正確引註的試算表版 merger model
- **verifier** = 主觀標準(輸出是什麼、是否符合風格指引)+ 客觀標準(這東西到底對不對)

**在打分這一步,人類智慧非常重要**——這是他們公司的核心信念。

#### eval 帶給企業的四件事(約 00:48–00:50)

1. **診斷機會**:eval 是成功部署 agent 的瓶頸,但同時也是找出機會的工具。如果你替每個部門都建了 eval、把任務與 ground truth 的 rubric 對映清楚,「要在公司哪五個地方部署 agent」就會變成一個**系統性、可量化**的答案,而不是猜。
2. **實際部署**:把「什麼叫做好」教給 agent,自動化流程。
3. **持續學習的地基**:agent 在某個 eval 上失敗時,可以把失敗原因**往上 triage 到 skills file**,確保它不再發生;更進一步,可以拿這些失敗去 post-train 模型,確保不會回歸。
4. **資料變現**(他們正與多家領先企業推進的方向):前沿實驗室非常想讓模型在真實企業情境下表現良好,而**task + trajectory + context + artifact + rubric 這整套骨架,就是模型訓練層級極有價值的資料**。

(他在後續 panel 補充了這件事的商業面:這類「commodity workflow」資料經過匿名化與身分清洗、放進 RL 環境後,對一般企業通常是零成本方案,而 Mercor 能替他們創造七到八位數的變現。)

### 金句

> "Most of these enterprise AI use cases never reach production … just because there's no way to actually measure ground truth or success."(約 00:45)

整場演講的論點起點。

> "What you need is a task … the trajectory … the actual artifact … the actual world … and then the last thing is a rubric or a verifier."(約 00:47)

agentic eval 的五件套,也是他後來在 panel 上再講一次的定義。

> "If you build an eval for every single one of your departments and a proper mapping of these tasks and what ground truth looks like in the rubric, it's very very logical that you could come up with like the top five areas in your company where you should deploy agents."(約 00:49)

eval 不只是驗收工具,更是機會探勘工具——這是他最反直覺的一點。

## English Notes

### TL;DR

- **Two paths to owning your intelligence**: train your own model (Cursor's Composer, fine-tuned on Cursor's own data and infrastructure), or adopt a frontier model and engineer a very good harness around it. **Both paths share one prerequisite: a really good eval.**
- **The failure loop**: no systematic way to identify agent opportunities → guess where to start → speculate on agent behavior → deploy → try it in a sandbox and assume it works → improve based on failures that are anecdotal or incidentally observed. That loop is why most enterprise AI use cases never reach production.
- **Five components of an agentic eval** — carried over from Mercor's frontier benchmark **APEX** into enterprise settings: **task** (what is the model actually doing), **trajectory** (its reasoning and tool calls), **artifact** (what it produces), **world / context** (the environment it traverses), and **rubric / verifier** (how it gets graded).
- **Human judgment is load-bearing at the grading step** — a core belief behind Mercor's business.
- **Four things evals unlock**: (1) systematically and quantitatively identify the top areas in a company where agents should be deployed; (2) actually deploy agents and teach them what "good" looks like; (3) a foundation for continuous learning — triage a failure up to the skills file so it never recurs, or post-train on it so the model doesn't regress; (4) **data monetization** — the task/trajectory/context/artifact/rubric scaffolding is extremely valuable training data at the foundation-model level.

### Key Points

#### Where Mercor started, and the 2026 pivot (~00:42–00:44)

He started Mercor at 19, in his second year at Harvard, and dropped out to run it; his co-founders were high-school debate teammates, one of them his actual debate partner.

The company began by **selling data to AI labs**. The driving realization: models had gotten sophisticated enough that annotating whether an image contains a stop sign was no longer the point. The question became "can we make the model better at engineering, at medical tasks, at legal?" — which demands **genuinely sophisticated human expertise**, plus the ability to structure that data for the agentic paradigm, in RL environments and gyms.

But Mercor's main focus in 2026 — which he notes not many people know — is **enterprise**. His layering: labs at the base; then the neolabs; then applied-layer companies and startups (he names Harvey and Cursor); then the average enterprise. **All four layers want to own their own intelligence**, apply it across the company and train their own models, and they need fundamentally the same offering: **training and evals**.

#### Owning your intelligence: two paths, one prerequisite (~00:44–00:45)

1. **Train your own model.** Cursor is his example: they trained their own Composer model — now a genuinely good coding model — and can fine-tune it with Cursor's data and infrastructure.
2. **Adopt a frontier model and engineer a harness** that's excellent for the specific product or use case. Plenty of companies are doing this.

**The common thread: you need a really, really good eval.** That's where Mercor enters, building directly on the work it does with the labs and on its frontier benchmark **APEX**.

#### Why enterprise AI stalls before production (~00:45–00:46)

Whether you're training a model for an external agent or deploying agents internally, the blocker is the same: **there's no way to measure ground truth or success.** What results is a guessing loop —

> no systematic way to identify agent opportunities in your product → guess where to start → speculate on the agent's behavior → deploy → try it in a sandbox, assume it roughly works → improve based on failures that are largely observed or anecdotal.

"This loop is really really bad," hence their case for an **eval-driven approach** to enterprise AI deployment.

#### What an agentic eval is: five components (~00:46–00:48)

"Eval" is an overloaded term, so he builds from APEX's definition outward. Working with the labs, when a frontier model ships they benchmark it across many tasks in many domains; for agentic use cases the model runs over hundreds of turns, and they **analyze the whole trajectory to find where and why it fails**.

The same structure transfers to the enterprise:

| # | Component | The question it answers |
|---|-----------|------------------------|
| 1 | **Task** | What is the model actually doing? |
| 2 | **Trajectory** | What reasoning and rationale is the agent using? |
| 3 | **Artifact** | What is it actually producing? |
| 4 | **World / Context** | What environment is the agent traversing? |
| 5 | **Rubric / Verifier** | How do you grade it? |

**A worked example (investment banking)**: a banker prompts the model to "update this merger model to show how the deal affects both companies." Done by hand you'd open Excel, pull up a specific merger model, go into a data room, get feedback, discover something is wrong, look it up, then produce the model. Deploying an agent to do that requires observability over every one of those steps:

- **task** = update the merger model
- **trajectory** = the tools the agent calls (found the merger model, updated deal terms, built the tables …)
- **artifact** = the merger model in a spreadsheet with the right citations
- **verifier** = subjective criteria (what the output is, whether it meets stylistic guidelines) plus objective criteria (is the thing actually correct)

And **human intelligence matters enormously at that grading step** — core to how they think about the business.

#### Four things evals do for an enterprise (~00:48–00:50)

1. **Diagnose the opportunity.** Evals are the bottleneck to deploying agents successfully, but they also tell you *where* to deploy. Build an eval for every department, with a proper mapping of tasks and what ground truth looks like in the rubric, and the top areas for agent deployment fall out **systematically and quantitatively** instead of being guessed.
2. **Actually deploy** — teach the agent what good looks like in your company and automate the process.
3. **Foundation for continuous learning.** When an agent fails an eval, you can **triage the reason up to the skills file** so it never happens again, and you can post-train a model on those failures so it never regresses.
4. **Data monetization** — an effort they're running with a number of leading companies. Labs badly want models that perform in real enterprise contexts, and the scaffolding — task, trajectory, context, artifact, rubric — is exactly the data that's valuable for training at the foundation-model level.

(In the panel afterward he added the commercial shape of this: for "commodity workflows," Mercor anonymizes the data, scrubs identity, puts it in an RL environment useful to labs, and it's typically a no-cost option for the company because they can generate seven or eight figures by monetizing it.)

### Quotes

> "Most of these enterprise AI use cases never reach production … just because there's no way to actually measure ground truth or success." (~00:45)

The premise the whole talk hangs on.

> "What you need is a task … the trajectory … the actual artifact … the actual world … and then the last thing is a rubric or a verifier." (~00:47)

The five-part definition of an agentic eval, which he repeats verbatim on the panel.

> "If you build an eval for every single one of your departments and a proper mapping of these tasks and what ground truth looks like in the rubric, it's very very logical that you could come up with like the top five areas in your company where you should deploy agents." (~00:49)

His most counterintuitive claim: evals aren't just an acceptance gate, they're the prospecting tool.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Mercor | 講者共同創辦的公司,2023 年 1 月成立;從賣專家資料給實驗室,轉向企業訓練與 eval | The speaker's company, founded Jan 2023; from selling expert data to labs to enterprise training and evals | 主持人介紹時提到 20 億美元營收年化與 200 億估值 / introduced with a $2B revenue run rate and $20B valuation |
| APEX | Mercor 的前沿 benchmark,評估模型能否完成高經濟價值的知識工作 | Mercor's frontier benchmark measuring whether models can do economically valuable knowledge work | 涵蓋投銀、顧問、法律、基層醫療等領域;另有 APEX-Agents、APEX-Accounting / spans investment banking, consulting, law, primary care; also APEX-Agents and APEX-Accounting |
| Cursor Composer | Cursor 自訓的 coding model,可用自家資料與基礎設施微調 | Cursor's own coding model, fine-tunable with their data and infrastructure | 講者用來舉例「訓練自己的模型」/ his example of training your own model |
| Harvey | 法律領域的應用層 AI 公司,演講中作為「applied layer」例子 | Applied-layer legal AI company, cited as an example | |
| RL environments / gyms | 把專家資料結構化成 agentic 訓練環境的形式 | Structuring expert data into agentic training environments | Mercor 早期與實驗室合作的產物 / from their lab work |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Adar Hiramath / Adarth / Adar | Adarsh Hiremath |
| Merur / Meror / Ror / Merore / Merkor | Mercor |
| Kurser | Cursor |
| eval(單複數混用) | evals |
| geni projects | GenAI projects |
| FTEEs | FTEs |

## 待確認 / To Verify

- 逐字稿說 Cursor 訓練 Composer 是「in collaboration with SpaceX」——這句聽起來明顯有誤,合作對象待確認,**不做臆測**。/ The transcript says Cursor trained Composer "in collaboration with SpaceX", which is almost certainly a mis-transcription; the actual collaborator is unverified and deliberately not guessed.
- 「neolabs」是否為講者慣用詞或有特定所指(相對於 frontier labs 的一批新興模型公司),待確認。/ Whether "neolabs" is his own coinage or refers to a specific set of companies.
- 主持人介紹的「2 billion revenue run rate、20 billion valuation」數字出處待補。/ Source for the $2B run-rate and $20B valuation figures cited in the introduction.
