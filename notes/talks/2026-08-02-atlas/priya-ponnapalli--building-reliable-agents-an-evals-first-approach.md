---
title: "Building Reliable Agents: An Evals-First Approach"
title_zh: "打造可靠的 agent:以 eval 為先的方法"
speaker: "Priya Ponnapalli"
affiliation: "SVP of Engineering, Enterprise AI, Scale AI"
type: talk
stage: Atlas
date: 2026-08-02
session: "Session 2: Agent Evaluation & Benchmarks"
video: "https://www.youtube.com/watch?v=-7AJJLwYW1Q&t=1675s"
video_range: "00:27:55–00:39:32"
transcript: "tmp/[English (auto-generated)] Atlas Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [evaluation, enterprise, reliability, agents, production]
---

# 打造可靠的 agent:以 eval 為先的方法(Building Reliable Agents: An Evals-First Approach)

**一句話總結**:企業級 agent 用的是隨機性技術、卻要交付確定性的商業結果,「大致正確」等於責任風險;Scale 的解法是把評估切成 L0 商業成果 → L1 任務成功 → L2 元件 → L3 診斷四層,彼此獨立但因果相連,並把 eval 當成客戶真正的長期資產。
**One-line summary**: Enterprise agents use inherently stochastic technology to deliver deterministic business outcomes, so "mostly right" is a liability. Scale's answer is a four-layer eval framework — L0 business outcomes, L1 task success, L2 components, L3 diagnostics — kept separate but causally linked, with the eval suite treated as the customer's most durable asset.

## 中文筆記

### TL;DR

- **問題設定**:企業與受監管產業的 agent,錯 5% 就是責任風險——客戶發票上的錯誤數字、法遵申報裡的錯誤陳述、寫壞一個下游有上千系統依賴的 production 資料庫。她引用當天早上被提到的 MIT 研究:95% 的 AI pilot 進不了 production。
- **評估對象變了**:不是評模型輸出的文字,而是評一個隨時間展開、與真實環境互動的**系統**——模型 + prompt + 工具 + orchestration + 環境(production API、知識庫、檔案、企業流程)。要清楚區分**哪些元件可調、哪些是給定的**。
- **四層 eval 框架**:L0 商業成果(北極星 KPI)、L1 任務成功(黑盒,迭代的操作核心)、L2 元件評估(打開黑盒看子任務)、L3 診斷(解釋 L1/L2 為何失敗)。常見失敗模式:團隊花太多時間優化 L2/L3,卻沒讓 L1 一起變好。
- **設計原則**:能用確定性演算的就不要交給 agent。油井 casing 案例中,agent **從不計算任何數字、也不驅動流程**,所以數值保真度依設計即為 100%,評估問題被壓縮成「問答品質 + 文件完整正確與否」。
- **eval 是活資產、也是護城河**:模型可以隨時換掉,eval suite 留下來——這才是客戶投資的 IP,讓他們能一路搭上基礎模型進步的浪。

### 重點整理

#### 為什麼企業 agent 的「大致正確」不夠(約 00:28–00:30)

Scale 的使命是為世界上最重要的一些決策打造可靠的 AI 系統。她點出這件事本質上的張力:**你用的是本質隨機的技術,卻要交付確定性的商業結果。**

支撐這個觀點的背景:90% 的 frontier labs 使用 Scale 的 data engine;他們替政府(含美國國防部與 Defense Innovation Unit)以及醫療、金融、電信等受監管產業的企業建 AI 應用。與日常生產力用的 consumer/prosumer agent 不同,這些場景**可靠性就是一切**——例如與 Mayo Clinic 合作把 agent 帶進病患照護,目標字面上就是救命,沒有出錯空間。

她引用當天早上提到的 MIT 研究:95% 的 AI pilot 沒能進到 production。在企業情境下,agent 即使只錯 5%,那也是責任問題:客戶發票上的錯誤數字、法遵申報中的錯誤陳述、寫壞一個上千個下游系統依賴的 production 資料庫。

Scale 對每個上線 agent 有 **8 道工程關卡**(涵蓋資料隱私、正確的存取控制與 authZ/authN 等);本場專注在其中的「嚴謹 evals」。

#### 評的是系統,不是模型(約 00:30–00:31)

相對於模型 benchmark,企業 agent 的評估有個本質轉變:**agent 是一種系統能力**,它隨時間展開、在真實環境中互動。你評的不再是模型與它輸出的文字,而是端到端系統:模型、prompt、工具、orchestration,以及環境——在企業裡環境包含 production API、知識庫、各種檔案、以及該企業既有的商業流程。

她強調一個實用的區分:**哪些元件可以調、哪些是給定的**;好的 eval 設計會把兩者分開。

#### 四層評估框架(約 00:31–00:33)

框架的核心是把**商業對齊、黑盒評估、可除錯性**三件事分層放,彼此保持獨立但因果相連:

- **L0 商業成果**:北極星 KPI,agent 實際帶來的價值——結案率、每張工單成本、分析師省下的時間。
- **L1 任務成功**:把 agent 當黑盒,只問任務是否完成。例如:退款金額是否正確?案件記錄的最終狀態是否正確?**這是 agent 評估的操作核心**,也是團隊實際迭代、試不同做法、看分數變化的那一層。
- **L2 元件評估**:打開黑盒看子任務——抽取相關事實、選對欄位、產生正確的記錄變更。
- **L3 診斷**:除錯與最佳化所需的「為什麼」,解釋 L1/L2 為何失敗。

四層形成一條鏈。她點名一個常見失敗模式:**團隊花大量時間優化 L3 診斷與 L2 元件,卻沒有確認 L1 也跟著改善**。

#### 案例一:油井 casing 設計(約 00:33–00:36)

Scale 協助一家大型石油公司改善油井設計,其中包括 casing(套在井外的鋼管)設計。原本流程是**數週的循環**:工程師跑上百次模擬、翻閱埋在 PDF 與各種資料庫裡的標準規範。

Agent 的設計刻意分成兩塊:

1. **確定性核心**:工程師仍然主導,用可信的物理模擬器跑模擬;結果**以確定性方式**對照公司標準檢查;最終由工程師審核與批准安全的井設計。
2. **Casing design agent**:跟在工程師旁邊,從上百次模擬中抽取正確的 context,回答工程師提問並附上逐條引用(claim-level citation),最後產出井設計文件,也就是 **Basis of Design(BOD)**。

關鍵設計決策:**agent 從不計算任何數字,也不驅動任何流程**——因此數值保真度依設計即為 100%。整個 eval 問題於是被壓縮成:agent 回答工程師問題的品質如何?產出的 BOD 是否完整且正確?

套回四層框架:
- **L0** = 每年由領域專家(SME)簽核的 BOD 數量
- **L1** = agent 的設計與回答是否完整、正確、可直接進審查
- **L2** = 檢索與 context 管理
- **L3** = 術語、grounding 保真度、recall

作法:與 SME 一起建 eval、校準 grader;由於 SME 的時間永遠是瓶頸,他們**用合成方式擴充 SME 的樣板,再請 SME 驗證**。在 L1 正確性上做 hill climbing 的成果:**術語精確度 83% → 100%**、**主張精確度(claims precision)68% → 90%**。這贏得了客戶端井設計工程師的信任,目前進入**有限的 production rollout**——繼續蒐集 production trace、評分、演進 eval set、再改進 agent。

她順勢帶出整場最強的一句主張:**eval 是活資產,而且是最持久的資產**。模型可以換、agent 的設計可以換,eval suite 留下來持續驗收——這是客戶真正投資的 IP 與護城河,讓他們能一直搭上基礎模型進步的浪。

#### 案例二:財務盡職調查(約 00:36–00:37)

與一家四大會計/專業服務事務所合作,建了一個財務盡職調查 agent,把分析師取得**經人工驗證的洞察**所需的時間從 **4–6 週壓到 2 天**。同樣套用四層框架,L0 定義為「取得人工驗證洞察的總時間」,同樣經過建 eval、迭代 L1 正確性,同樣走向有限 production rollout。她補了一句實務觀察:**eval 資料量不足往往是最大瓶頸之一**,而有限的 production rollout 正是補資料、演進 eval suite 的好機會。

#### 流程化與收尾原則(約 00:37–00:39)

Scale 內部對每個 agent 都會開一次 **eval design review**,由 forward deployed engineering 團隊與企業客戶及政府單位共同進行;他們用一張 **performance maturity matrix** 當作每個 agent 的 eval 計分卡,**計分卡沒有全綠就不出貨**。

收尾原則:
- 你評的是**系統**,不只是模型。
- 用**混合 grader**:能確定性判斷的就確定性判斷,必要時才用模型當 grader,校準與高風險場景則用人工審查。
- 把 eval 當**活資產**,隨時間長大。
- 「evals first is how mostly right becomes production-ready.」

### 金句

> "You have technology that is inherently stochastic, and you are trying to deliver deterministic business outcomes using this."(約 00:28)

一句話說完企業 AI 的核心張力,也是整套 eval 框架存在的理由。

> "The agent never computes any number or drives any workflow. So, by design, numerical fidelity is 100%."(約 00:35)

最好的可靠性設計不是評出來的,是**架構上讓錯誤不可能發生**;剩下的才交給 eval。

> "Evals are living assets … they are the most durable asset."(約 00:36)

模型會被換掉,eval suite 不會——這是她給企業客戶的核心建議。

> "Evals first is how mostly right becomes production-ready."(約 00:39)

## English Notes

### TL;DR

- **The framing**: in enterprise and regulated industries, an agent that's wrong 5% of the time is a liability — a wrong number on a customer invoice, a misstatement in a compliance filing, a bad write to a production database thousands of systems depend on. She cites the MIT study referenced that morning: 95% of AI pilots never reach production.
- **What you evaluate changes**: not a model and its output text, but a **system** unfolding over time in a real environment — model, prompts, tools, orchestration, and environment (production APIs, knowledge bases, files, business workflows). Good eval design separates tunable components from given ones.
- **A four-layer framework**: L0 business outcomes (North Star KPIs), L1 task success (black box; the operational center you iterate on), L2 component evals (open the box, look at sub-tasks), L3 diagnostics (the "why" behind L1/L2 failures). Common failure mode: optimizing L2/L3 without moving L1.
- **Design principle**: anything that can be deterministic shouldn't go through the agent. In the oil-well casing case the agent never computes a number or drives a workflow, so numerical fidelity is 100% by construction and the eval problem shrinks to answer quality and document completeness.
- **Evals are living assets and a moat**: you can swap the model at any time; the eval suite is what customers actually invest in, and it's what lets them ride the wave of foundation-model improvements.

### Key Points

#### Why "mostly right" fails in the enterprise (~00:28–00:30)

Scale's mission is to build reliable AI systems for some of the world's most important decisions, and the tension is structural: inherently stochastic technology, deterministic business outcomes.

The credentials behind the approach: 90% of frontier labs use Scale's data engine, and Scale builds AI applications for governments — including the US Department of Defense and the Defense Innovation Unit — and for enterprises in regulated industries like health care, finance, and telco. Unlike consumer and prosumer agents used for day-to-day productivity, reliability is the whole game here. Their work with the Mayo Clinic on bringing agents into patient care is a case where, in her words, the goal is literally saving lives.

She cites the MIT study mentioned in that morning's talk — 95% of AI pilots never reach production — and makes the enterprise version of the point concrete: an agent that's wrong 5% of the time produces a wrong number on a customer invoice, a misstatement in a compliance filing, or a bad write to a production database with thousands of downstream dependents.

Every production agent at Scale passes **eight engineering gates**, covering data privacy, correct access-control frameworks with authZ and authN in place, and more. This talk covers one of them: rigorous evals.

#### You are evaluating a system (~00:30–00:31)

Relative to model benchmarking, enterprise agent evaluation shifts because an agent is a **system capability**. It unfolds over time and interacts with a real environment, so what's under test is the end-to-end system: model, prompts, tools, orchestration, and environment — where in an enterprise the environment means production APIs, knowledge bases, files, and the business workflows already present at that company. The useful distinction, and one good eval design preserves, is which components can be tuned and which are given.

#### The four-layer framework (~00:31–00:33)

The framework keeps business alignment, black-box evaluation, and debuggability separate but causally linked:

- **L0 — business outcomes**: the North Star KPIs and the value the agent actually drives — resolution rate, cost per ticket, analyst time saved.
- **L1 — task success**: treat the agent as a black box and ask whether it completed the task. Was the refund issued for the correct amount? Is the case record in the correct final state? This is the operational center of agent evaluation and the layer teams iterate against.
- **L2 — component evals**: open the box and look at sub-tasks — extracting the relevant facts, choosing the right fields, producing the right record changes.
- **L3 — diagnostics**: the "why" behind failing L1 and L2 metrics; what you need for debugging and optimization.

These form a chain, and the common failure mode she calls out is teams spending most of their time optimizing L3 diagnostics and L2 components without confirming L1 is improving too.

#### Case study 1: oil well casing design (~00:33–00:36)

Scale is helping a top oil company design wells better, including the casing — the steel pipe that goes around the well. Designing it is normally a multi-week loop in which an engineer runs hundreds of simulations and consults standards buried in PDFs and libraries.

The agent design has two deliberately separated halves. First, a **deterministic core**: the engineer stays in charge, runs the simulations with trusted physics-based simulators, results are checked deterministically against company standards, and the engineer makes the final call on approving safe well designs. Second, a **casing design agent** that follows along, extracts the right context from hundreds of simulations, answers the engineer's questions with claim-level citations grounded in the agent's interaction, and finally drafts the well design document — the Basis of Design (BOD).

The load-bearing architectural choice: **the agent never computes any number or drives any workflow**, so numerical fidelity is 100% by design. That collapses the eval question down to how well the agent answers the engineer's questions and generates complete, correct BODs.

Mapped onto the framework: L0 is the number of annual BODs signed off by subject-matter experts; L1 is whether the agent's answers and documents are complete, correct, and review-ready; L2 covers retrieval and context management; L3 covers terminology, grounding fidelity, and recall.

They build the evals with SMEs and calibrate the graders. Because SMEs are bottlenecked on time, they synthetically expand SME templates and have the SMEs validate the additional data. Hill-climbing on L1 correctness took **terminology precision from 83% to 100%** and **claims precision from 68% to 90%**. That earned the confidence of the customer's well design engineers, and the agent is now in a limited production rollout, collecting additional production traces, scoring them, evolving the eval sets, and improving from there.

This leads to her strongest claim: **evals are living assets, and the most durable asset there is**. You can always swap out the model or redesign the agent and test against the same suite. That suite is the IP moat customers invest in, and it's what lets them ride on top of the wave of foundation model improvements.

#### Case study 2: financial due diligence (~00:36–00:37)

With a top-four professional services and accounting firm, Scale built a financial due diligence agent that takes analysts from four to six weeks down to two days to reach the same human-validated insights. Same framework — L0 defined as total time to human-validated insights, evals built, L1 correctness hill-climbed, and a production rollout where every run teaches them something. She adds a practical note: having sufficient eval data is often one of the biggest bottlenecks, and limited production rollouts are a good opportunity to collect more and evolve the suite.

#### Process and closing principles (~00:37–00:39)

Every agent built at Scale gets an **eval design review**, run with a forward deployed engineering team that partners with enterprises and government agencies. A **performance maturity matrix** serves as the eval scorecard for each agent, and **nothing ships until the scorecard is all green**.

Closing principles: you're evaluating systems, not just models; use hybrid graders — deterministic wherever possible, model-based where necessary, human review for calibration and high-stakes use cases; treat evals as living assets that grow over time; and "evals first is how mostly right becomes production-ready."

### Quotes

> "You have technology that is inherently stochastic, and you are trying to deliver deterministic business outcomes using this." (~00:28)

The central tension of enterprise AI in one sentence, and the reason the whole framework exists.

> "The agent never computes any number or drives any workflow. So, by design, numerical fidelity is 100%." (~00:35)

The best reliability wins are architectural — make the error impossible, then evaluate what's left.

> "Evals are living assets … they are the most durable asset." (~00:36)

Models get swapped out; the eval suite doesn't.

> "Evals first is how mostly right becomes production-ready." (~00:39)

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Scale 四層 eval 框架 / Layered eval framework | L0 商業成果 → L1 任務成功 → L2 元件 → L3 診斷 | L0 business outcomes → L1 task success → L2 components → L3 diagnostics | 三件事分層但因果相連 / separate but causally linked |
| 8 engineering gates | 每個上線 agent 必過的工程關卡 | Gates every production agent must clear before shipping | 字幕僅提到資料隱私與存取控制兩項 / only privacy and access control were named |
| Performance maturity matrix | 每個 agent 的 eval 計分卡,全綠才出貨 | Eval scorecard per agent; ship only when all green | 由 eval design review 把關 / gated by the eval design review |
| Casing design agent | 油井 casing 設計輔助 agent,產出 Basis of Design | Well-casing design agent producing the Basis of Design document | agent 不算數字、不驅動流程 / never computes numbers or drives workflows |
| 財務盡職調查 agent / Financial due diligence agent | 四大專業服務事務所案例,4–6 週 → 2 天 | Top-four professional services firm; four-to-six weeks down to two days | 同樣走有限 production rollout / also in limited production rollout |
| MIT study(95% of AI pilots) | 當天早上場次引用的研究,95% AI pilot 進不了 production | Study cited that morning: 95% of AI pilots never reach production | 講者未給出處,待確認 / no citation given in the talk |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Priya Ponapalli | Priya Ponnapalli |
| odd Z and odd then | authZ and authN |
| e-vals | evals |
| cloth-level citations | claim-level citations(依上下文推定,待確認)/ inferred from context, to verify |
| wealth designs engineers | well design engineers |
| multi-week hop | multi-week loop |
| BODs | Basis of Design (BOD) |

## 待確認 / To Verify

- 「claim-level citations」的實際用字(字幕聽成 "cloth-level");也可能是 "clause-level"。需看投影片。/ The actual wording behind "cloth-level citations" — likely "claim-level", possibly "clause-level"; check the slides.
- 8 道 engineering gates 的完整清單,講者只點名了資料隱私與存取控制。/ The full list of the eight engineering gates.
- 95% AI pilot 失敗的 MIT 研究出處(常被引用的是 MIT NANDA 的 State of AI in Business 報告,但講者未指名)。/ Citation for the MIT 95% figure (commonly the MIT NANDA "State of AI in Business" report, but she didn't name it).
- 石油公司與四大事務所客戶名稱皆未公開。/ Neither the oil company nor the accounting firm was named.
- L3 指標「terminology、grounding fidelity、recall」的精確定義與量測方式未展開。/ Precise definitions of the L3 metrics were not given.
