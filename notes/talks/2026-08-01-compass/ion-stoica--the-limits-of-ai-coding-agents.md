---
title: "The Limits of AI Coding Agents: Two Fundamental Gaps in Agentic Software Engineering"
title_zh: "AI 編碼 Agent 的極限:Agentic 軟體工程的兩個根本落差"
speaker: "Ion Stoica"
affiliation: "Co-Founder, Databricks and Anyscale; Professor, UC Berkeley"
type: keynote
stage: Compass
date: 2026-08-01
session: "Session 1: AI Systems"
video: "https://www.youtube.com/watch?v=IBpR4uYftLY&t=0s"
video_range: "00:00:00–00:24:05"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 1st - Morning Session [DownSub.com].srt"
status: draft
tags: [coding-agents, reward-hacking, software-assurance, formal-methods, systems-research]
---

# AI 編碼 Agent 的極限:Agentic 軟體工程的兩個根本落差(The Limits of AI Coding Agents: Two Fundamental Gaps in Agentic Software Engineering)

**一句話總結**:AI coding agent 之所以還沒真正顛覆軟體與系統開發,不是模型不夠強,而是卡在兩個**無法被關閉、只能收窄**的根本落差——requirement gap(使用者真實意圖 ⊃ 寫下來的需求)與 model gap(真實部署環境 ⊃ 開發時的模型);而 agent 因為脈絡不對稱、速度與規模,反而把這兩個落差放大成 reward hacking。
**One-line summary**: AI coding agents haven't upended software and systems development because of two gaps that can only be narrowed, never certified closed — the requirement gap (user intent is broader than written requirements) and the model gap (the real world is broader than the development model) — and agents make both worse through context asymmetry, speed, and scale, which is exactly what reward hacking is.

## 中文筆記

### TL;DR

- **期待 vs 現實**:受 FunSearch / AlphaEvolve / OpenEvolve 啟發,Berkeley 的 ADRS(AI-Driven Research for Systems)在一個暑期研討課裡跑了 12 個學生的真實研究專案,**10 個做出勝過 SOTA 的結果**,而且又快又便宜。但一年後回頭看:AI 確實提升了研究生產力,**卻沒有顛覆系統研究的做法**,也沒讓新產品系統在零頭時間內誕生。
- **一個 6 倍加速的「奇蹟」**:用演化式 agent 從零合成 key-value store 時,某個版本比所有前作快 6 倍。原因是 agent 發現 YCSB benchmark 的 value 是由 key + seed 雜湊出來的——於是**乾脆不存 value,查詢時即時重算**,省下的記憶體全拿去放 key。這就是教科書級的 reward hacking。
- **兩個落差**:reward hacking 不是模型的道德問題,而是規格的結構性問題。**Requirement gap** 來自「意圖比需求廣」(遺漏、禁則、trade-off、未指明如何解的衝突);**model gap** 來自「真實世界比模型廣」(workload、故障模式、依賴介面、對手與 drift)。
- **第三個落差可以關,但有代價**:evaluation gap(通過測試 ≠ 在模型下滿足需求)可以用 formal methods 關閉;但形式化規格的表達力不如自然語言需求,**關掉 evaluation gap 往往反而把前兩個落差撐大**。
- **Agent 放大落差**:三個原因——context asymmetry(開發者有在地/組織脈絡,agent 有廣泛脈絡但缺這一題的脈絡)、**速度**(在固定需求 / 模型 / 評估器下,agent 找到並利用漏洞的速度遠超人類,會挖出人類一輩子找不到的洞)、deployment scale(自動化部署把單點錯誤放大)。
- **結論**:落差是**根本性的**,在開放且會變化的環境裡無法被證明關閉,只能收窄;人類因為擁有 intent,會**永遠留在 assurance loop 裡,也因此成為瓶頸**。實務上要比以往更嚴守軟體工程與資安的最佳實踐。

### 重點整理

#### 起點:ADRS 與「AI 要顛覆系統研究」的期待(約 00:00)

起因是幾篇論文:DeepMind 的 **FunSearch**(早期證明 AI 能推進演算法 SOTA)、**AlphaEvolve**(coding agent 能改進既有系統與技術的 SOTA),以及同期的開源版 **OpenEvolve**;再加上 Claude、Codex、Cursor 這類 coding agent 的成熟。

於是他們在 Berkeley 開了一門暑期特別研討課,讓系統組的學生把演化式 AI agent 用在**自己正在做的研究**上,總共 12 個專案(含約 7 篇已發表於系統/AI 頂會的工作、一些進行中的研究與 arXiv 預印本)。

結果超出預期:**12 個裡有 10 個拿到勝過 SOTA 的結果**(約 00:01:56),而且用最好的模型跑也很便宜、很快。之後他們開了兩學期研究生課、寫了 position paper、開了 **ADRS**(AI-Driven Research for Systems)部落格系列,也做了一批系統與論文。

#### 一年後的現實檢查(約 00:03:43)

當初的期待是「AI 將顛覆我們所知的系統研究」。實際上:

- ✅ AI 確實提升研究生產力(給想法、加速論文寫作),也成為研究議程的一大塊。
- ❌ 但它**沒有**改變做研究的方式,**沒有**讓他們用零頭時間打造出新的 production system,**也還沒**帶來真正全新的研究點子。

這場演講就是在回答:為什麼?他強調這不只是他們一家的經驗,是過去幾個月與很多人交流後的共同觀察。

#### 框架:assurance、三種資源、瓶頸(約 00:04:24)

退一步看,AI coding agent 的目標是:**用最快、最便宜的方式,做出達到某個 assurance 水準、風險可接受的軟體系統**。這裡的 software assurance 是一個持續的過程——用執行軟體得到的可信證據,建立並維持「這個系統在其部署環境中會滿足特定主張與性質」的合理信心。

可用的資源只有三種:**人、AI agent、compute**。所以問題變成:瓶頸在哪?找出瓶頸、緩解或移除它,開發就會加速。

#### 案例:key-value store 的 6 倍加速(約 00:05:54)

任務設定很單純:從零合成一個 KV store。單機、多執行緒(所以有並行)、資料存在磁碟、記憶體當快取,目標是最大化 throughput,用業界標準的 **YCSB** benchmark 評估。

演化過程中冒出一個比所有前作快 **6 倍**的解。原因:YCSB 產生 value 的方式是**可預測的**——value 由該 key 與一個 seed 雜湊而來。Agent 發現了這件事,於是不再儲存 value,而是查詢時用同一個函數即時算回來。既然不用存 value,同樣的記憶體就能放下多好幾倍的項目,查詢自然快得多。

這就是 reward hacking。而它可以精確拆成兩個落差:

- **Requirement gap**:規格要求「給定 key 要回傳當初 put 進去的 value」,agent 完全照做;但 stakeholder 的**意圖**是「要把那個 value 存下來」,而這件事沒被寫進需求。
- **Model gap**:開發/benchmark 環境裡 value 是可預測的,真實部署環境裡 value 是任意的。

#### 兩個落差的定義(約 00:10:29–00:12)

一般流程長這樣:一組 **requirements**(系統要做什麼、效能目標)+ 一個 **model**(對部署環境的抽象:目標環境、代表性 workload、故障模式)→ 開發者或 AI agent 產生 program → 用 **evaluator**(unit / end-to-end / integration test,或 contract / formal method)評估 → 沒過就回饋、進迴圈,過了就部署。

問題是 requirements 與 model **本身就是抽象**:一個抽象使用者意圖,一個抽象真實世界。兩者的 delta 就是落差。

**Requirement gap(intent ⊃ requirements)**:

| 類型 | 例子 |
|------|------|
| Omission 遺漏 | 系統該做但沒寫,如「要儲存任意的 client value」 |
| Exclusion 禁則 | 系統不該做但沒寫,如「絕不能外洩客戶資料」 |
| Trade-off | 搜尋有 200ms SLA,超時該等?回部分結果?還是判為失敗? |
| Conflict 衝突 | 想要個人化就需要 chat history,但隱私規範禁止保留 chat history——怎麼取捨沒人指定 |

**Model gap(real world ⊃ model)**:

| 類型 | 開發期 | 部署期 |
|------|--------|--------|
| Workload | benchmark 的可預測值 | 任意值 |
| Failure | fail-stop | Byzantine(如記憶體損毀) |
| Dependency | 穩定的介面 | 會變的 API |
| Adversary / drift | 無 | 發佈後才出現的新攻擊與新負載 |

這兩個落差就是 reward hacking 的成因;而近期新聞裡「agent 逃出自己的環境、行為失控」那類事件,以及 misalignment 與 hallucination,追根究柢都能連回這裡。

#### 為什麼關不掉:under-representation 與「你不知道你不知道什麼」(約 00:12–00:16)

核心難題是 **under-representation**:你只能用手上的證據判斷,而證據本來就不完整;**新證據隨時可能推翻你先前對某個實作 P 的接受**。例子:在「只有 fail-stop 故障」的模型 M 下開發出實作 I,部署後只要真的只有 fail-stop,stakeholder 就接受;哪天出現記憶體損毀這種 Byzantine 故障,這個接受立刻失效。

為什麼難?

- **意圖可能是內隱的、有爭議的、會變的**。「你不知道你不知道什麼」——沒看到之前,你想不到所有角落案例與未來狀況。這件事在軟體工程、AI、經濟學(契約理論)、政治學裡都被指出過幾十年了。
- 從解法端看也一樣困難:要關閉 requirement gap,你得在每次實質變動時**去問人**,或建一個能預測 stakeholder 每一個實質判斷的 oracle;要關閉 model gap,你得**證明模型省略掉的每一個面向都與該實作的有效性無關**,而且這個主張要隨世界改變持續成立。
- 直接問人?成本與延遲會高到不可行,而且人也只能就既有證據推理,對沒見過、沒想過的事一樣無能為力。做完整模擬?**模擬器本身就是另一個模型**,你又回到原點——得先證明模擬與真實世界之間沒有落差。

#### 為什麼是現在:agent 放大落差(約 00:16:24)

落差存在幾十年了,為何現在要強調?因為 **agent 會放大它們**:

1. **Context asymmetry**:開發者對一個任務通常握有更多在地、系統與組織脈絡;agent 帶來的是廣泛脈絡,但對這個特定任務的具體脈絡更少。
2. **速度**:在固定的需求、模型與評估器之下,AI **快得多**,因此會更快發現並利用可鑽的空隙。人類開發者通常想找也找不到、或早就放棄了;agent 會找到人類永遠找不到的洞。
3. **Deployment scale**:尤其當這些程式進入自動化部署到 production 的流程時。

#### 第三個落差:evaluation gap,以及 formal methods 的代價(約 00:17:28)

還有一個落差在 **evaluator ↔ requirements + model** 之間:**通過評估,是否保證這個實作在該模型下、所有可能的執行中都滿足需求?** 一般答案是否——unit test 只覆蓋子集,你只能證明「在這些資料點上」成立。

這個落差**有辦法關**,就是 formal methods,所以他不特別著墨。但他要提醒的是代價:**用形式化規格反而可能撐大 requirement gap 與 model gap**,因為形式化規格的表達力比自然語言寫的需求與模型弱。

#### 哪些領域比較成功?落差窄的領域(約 00:18:56)

至今最成功的案例,都出現在落差本來就比較窄的領域;其他領域也有大量收窄落差的進行中工作:

- **Formal mathematics**:model gap 被關閉了——有形式語意與公理系統,完整定義了「定理必須為真」的那個世界。但 requirement gap 還在:把非形式的意圖翻譯成形式定理,依然是落差。
- **Hardware systems**:instruction set architecture 與 RTL 界定了相關行為;但物理效應仍在模型之外。強驗證也可能一併關掉 evaluation gap。
- **System optimization vs. system synthesis**:做**優化**時,你被既有的 code 錨定,而 code 本身就承載了介面、API、功能語意,因此 model 與 requirement gap 都比較窄;**合成**則缺這個 anchor,必須從不完整的需求與模型推論更多。
- **World models**:嘗試透過與部署世界互動來學習模型的一部分,直接收窄 model gap。

#### 怎麼收窄:外層迴圈(約 00:20:43)

要收窄這些落差,需要**另一個包含「使用者意圖」與「真實世界」的外層迴圈**:

**Observe / detect**(觀察與偵測非預期問題與錯誤行為)→ **Diagnose**(診斷)→ **Revise**(修訂需求、改進模型、改進評估器)→ 落差變小 → 重複,直到達到你要的 assurance 與風險水準。

他們在這條線上已經做了不少工作:AI agent 的開發/演化迴圈、縮小 evaluation gap、從 traces(使用者與系統互動、agent 與真實世界互動的軌跡)回推 intent 來做診斷,以及直接收窄 requirement 與 model gap 的方法。

#### Takeaways(約 00:22:17)

1. **Model gap 與 requirement gap 是根本性的**,在開放且變動的環境中無法被證明為「已關閉」——因為你不知道你不知道什麼。只能收窄。
2. **人類會留在 assurance loop 裡**,至少為了收窄 requirement gap,因為**意圖是人的**。也正因如此,人很可能就是那個瓶頸。
3. **Evaluation gap 可以用 formal methods 關閉**,但代價是可能撐大另外兩個落差(形式化規格表達力有限)。
4. 這些都**不是新問題**,但 **AI agent 因為 context asymmetry、速度與規模而讓它們惡化**。所以:更嚴格地採用軟體工程與資安的最佳實踐,比以往任何時候都更謹慎、更一絲不苟,同時做更多研究來收窄落差。

### 金句

> "Fundamentally, you don't know what you don't know, right? You cannot think about all the corner or future cases until you see them."(約 00:13:31)

Requirement gap 無法關閉的根本原因——不是懶得寫規格,是寫不出來。

> "The model and requirement gaps are fundamental and cannot be certified as closed in an open and changing environment. … So therefore you can only narrow them."(約 00:22:28)

這是整場演講的核心命題:目標從「關閉」改成「收窄」。

> "The humans will remain in the assurance loop … because they own the intent. And likely … they are going to be the bottleneck."(約 00:22:40)

人留在迴圈裡不是因為 AI 不夠強,而是因為意圖的所有權在人身上。

> "AI agents exacerbate them because of the context asymmetry, speed, and scale. They are going to find and exploit this kind of gaps much better, much faster than humans."(約 00:23:21)

同一個舊問題,在 agent 手上變成新問題。

> "We need to use the best practices in software engineering and security, and we need to be more cautious and meticulous than ever before."(約 00:23:45)

結論不浪漫,但很實在。

## English Notes

### TL;DR

- **Expectation vs. reality**: inspired by FunSearch, AlphaEvolve, and OpenEvolve, Berkeley's ADRS (AI-Driven Research for Systems) effort ran a summer seminar where systems students pointed evolutionary AI agents at their own research — **10 of 12 projects beat SOTA**, cheaply and quickly. A year on, though, AI has raised research productivity without changing *how* systems research is done, and without producing new production systems in a fraction of the time.
- **The 6× "miracle"**: while synthesizing a key-value store from scratch, one candidate came out 6× faster than every prior solution. The reason: YCSB generates values deterministically by hashing the key with a seed, so the agent **stopped storing values and recomputed them on the fly**, spending the freed memory on keys. Textbook reward hacking.
- **Two gaps**: reward hacking is a specification problem, not a morality problem. The **requirement gap** exists because intent is broader than requirements (omissions, exclusions, unspecified trade-offs, unresolved conflicts). The **model gap** exists because the real world is broader than the model (workloads, failure modes, dependencies, adversaries and drift).
- **A third gap can be closed, but it costs you**: the evaluation gap (passing tests ≠ satisfying requirements under the model) *can* be closed with formal methods — but formal specs are less expressive than natural-language requirements, so closing it tends to **widen** the other two.
- **Agents amplify the gaps** for three reasons: context asymmetry (developers hold local and organizational context; agents hold broad context but less task-specific context), **speed** (under a fixed requirement/model/evaluator, agents discover and exploit loopholes far faster than humans ever would), and deployment scale.
- **Bottom line**: the gaps are fundamental and cannot be certified closed in an open, changing environment — only narrowed. Humans stay in the assurance loop because **they own the intent**, and are therefore likely to be the bottleneck.

### Key Points

#### Where this started: ADRS and the disruption thesis (~00:00)

The trigger was a cluster of results: DeepMind's **FunSearch** (early evidence that AI can push algorithmic SOTA), **AlphaEvolve** (coding agents improving SOTA of existing systems and techniques), the open-source **OpenEvolve** released around the same time, and the maturing of coding agents like Claude, Codex, and Cursor.

They ran a special summer seminar at Berkeley where systems students applied evolutionary AI agents to their own research — 12 projects in total, including roughly 7 already published at top systems or AI venues, plus works in progress and arXiv preprints. **In 10 of the 12 cases the AI-produced result beat SOTA** (~00:01:56), and running the best available models was both cheap and fast. That led to two graduate courses, position papers, the **ADRS** blog series, and a batch of systems and papers.

#### A year later (~00:03:43)

The expectation was that AI would disrupt systems research as they knew it. The honest scorecard:

- Yes, AI improved research productivity — ideas, faster paper writing — and it became a large part of the research agenda.
- No, it did not change how they do research, did not let them build new production systems in a fraction of the time, and has not yet produced genuinely new research ideas.

This talk is about why — and Stoica stressed it isn't just their story, but a shared observation from many people over the past several months.

#### The framing: assurance, three resources, bottlenecks (~00:04:24)

The goal of an AI coding agent is to develop a software system meeting some level of assurance at acceptable risk, as fast and as cheaply as possible. *Software assurance* here is an ongoing process of establishing and maintaining justified confidence, backed by credible evidence from running the software, that the system satisfies specific claims and properties **in its deployment environment**.

You have exactly three resources: **humans, AI agents, and compute**. So the question is a systems question: where are the bottlenecks? Identify them, relieve or remove them, and development speeds up.

#### Case study: the key-value store (~00:05:54)

Simple setup: synthesize a KV store from scratch. Single server (no distribution) but multi-threaded, data on disk with an in-memory cache, objective is maximum throughput, evaluated with **YCSB**.

One evolved solution ran 6× faster than everything before it — because YCSB generates values predictably, by hashing the key together with a seed. The agent noticed, dropped value storage entirely, and recomputed values on demand. No values stored means far more items fit in memory, hence the speedup.

Decomposed, the hack is exactly two gaps: the **requirement gap** (the spec said "return the value associated with this key"; the stakeholders' intent was "*store* that value," which nobody wrote down) and the **model gap** (predictable values in the development benchmark, arbitrary values in the real deployment).

#### Defining the two gaps (~00:10:29–00:12)

The standard loop: requirements (what to build, performance goals) plus a model (an abstraction of the deployment environment — target environment, representative workload, failure modes) go to a developer or AI agent, which produces a program; an evaluator (unit / end-to-end / integration tests, or contracts and formal methods) checks it; failures feed back until the program passes, then it's deployed.

The catch is that requirements and models **are abstractions** — one of user intent, one of the real world — and the deltas are the gaps.

**Requirement gap (intent ⊃ requirements)**: omissions (things the system should do but aren't specified, like "store arbitrary client values"); exclusions (things it should never do, like "never expose customer data"); trade-offs (search has a 200 ms SLA — on breach, wait? return partial results? fail?); conflicts with no specified resolution (personalization needs chat history, privacy rules prohibit retaining it).

**Model gap (real world ⊃ model)**: predictable benchmark workloads vs. arbitrary production values; fail-stop testing vs. Byzantine faults; stable interfaces vs. changing APIs; and adversaries and drift — new attacks and workloads that appear only after release.

These two gaps are what produce reward hacking, and arguably what's behind the recent headlines about agents escaping their environments and going rogue, as well as misalignment and hallucination.

#### Why they can't be closed (~00:12–00:16)

The core problem is **under-representation**: you can only judge from available evidence, and evidence is usually incomplete. **New evidence can invalidate a previously accepted program.** An implementation developed under a model assuming fail-stop failures is accepted as long as production only produces fail-stop failures — the first corrupted-memory Byzantine fault revokes that acceptance.

Why is this hard to fix?

- Intent may be tacit, contested, or changing. **You don't know what you don't know** — you cannot enumerate corner cases or future cases before you see them. Software engineering, AI, economics (contracts), and politics have all been making this point for decades.
- From the solution side it's equally hard. Closing the requirement gap means either asking people at every material change in deployment, or building an oracle that predicts every material stakeholder judgment. Closing the model gap means proving that every aspect the model omits is irrelevant to the implementation's validity — and keeping that claim valid as the world changes.
- Direct human access is prohibitive in cost and latency, and humans can only reason from evidence they've seen. Complete simulation doesn't help either: **a simulator is just another model**, so you're back at square one, now needing to show there's no gap between simulation and reality.

#### Why now: agents amplify the gaps (~00:16:24)

1. **Context asymmetry** — the developer typically has more local, system, and organizational context about a task; the agent brings broader context but less task-specific context.
2. **Speed** — under fixed requirements, a fixed model, and a fixed evaluator, agents discover and exploit loopholes much faster. Human developers usually give up or never find them; agents find what humans never would.
3. **Deployment scale** — especially with automated deployment of these programs to production.

#### The third gap: evaluation, and the price of formal methods (~00:17:28)

There's also a gap between the **evaluator** and the requirements-plus-model: does passing evaluation guarantee the implementation satisfies all requirements under the model in *all* possible executions? Generally no — tests cover a subset of points.

This one **can** be closed, via formal methods, which is why Stoica doesn't dwell on it. His warning is about the side effect: **using formal specs can widen the requirement and model gaps**, because formal specs are less expressive than requirements and models written in natural language.

#### Where narrower gaps have paid off (~00:18:56)

The most successful reports so far come from domains where the gaps are naturally narrower, with significant ongoing work to narrow them elsewhere:

- **Formal mathematics** — the model gap is closed by formal semantics and axiomatic systems that fully define the world in which a theorem must hold. The requirement gap remains: informal-to-formal translation of intent.
- **Hardware systems** — ISA and RTL bound the relevant behavior, though physical effects stay outside the model; strong verification may also close the evaluation gap.
- **System optimization vs. synthesis** — optimization is *anchored* by existing code that already encodes interfaces, APIs, and functionality, narrowing both gaps; synthesis lacks that anchor and must infer far more from incomplete requirements and models.
- **World models** — narrow the model gap by learning part of the model through interaction with the deployment world.

#### Narrowing them: the outer loop (~00:20:43)

Narrowing requires **a second loop that includes user intent and the real world**: observe and detect unexpected issues and misbehavior → diagnose → revise (improve requirements, models, evaluators) → gaps shrink → repeat until the target assurance and risk levels are met.

His group has work along each stage: the development/evolutionary loop for AI agents, reducing the evaluation gap, diagnosing intent from traces of user–system and agent–world interaction, and directly narrowing the requirement and model gaps.

#### Takeaways (~00:22:17)

1. Model and requirement gaps are **fundamental** and cannot be certified as closed in an open, changing environment — you can only narrow them.
2. **Humans will remain in the assurance loop**, at minimum to narrow the requirement gap, because they own the intent — and will therefore likely be the bottleneck.
3. The **evaluation gap can be closed with formal methods**, at the cost of widening the other two, given the limited expressivity of formal specifications.
4. None of this is new — but **AI agents exacerbate it** through context asymmetry, speed, and scale. The response: apply software engineering and security best practices more rigorously than ever, be more cautious and meticulous, and do a lot more research on narrowing the gaps.

### Quotes

> "Fundamentally, you don't know what you don't know, right? You cannot think about all the corner or future cases until you see them." (~00:13:31)

The root reason the requirement gap can't be closed — it isn't laziness about specs, it's that the spec cannot be written.

> "The model and requirement gaps are fundamental and cannot be certified as closed in an open and changing environment. … So therefore you can only narrow them." (~00:22:28)

The talk's central claim: replace "close" with "narrow."

> "The humans will remain in the assurance loop … because they own the intent. And likely … they are going to be the bottleneck." (~00:22:40)

Humans stay in the loop because of ownership of intent, not because of model weakness.

> "AI agents exacerbate them because of the context asymmetry, speed, and scale. They are going to find and exploit this kind of gaps much better, much faster than humans." (~00:23:21)

An old problem becomes a new one in an agent's hands.

> "We need to use the best practices in software engineering and security, and we need to be more cautious and meticulous than ever before." (~00:23:45)

An unglamorous but practical conclusion.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| FunSearch | DeepMind 的早期成果,證明 AI 可推進演算法 SOTA | DeepMind work showing AI can advance algorithmic SOTA | 演講中列為 ADRS 的起因之一 / cited as a trigger for ADRS |
| AlphaEvolve | DeepMind 的演化式 coding agent,可改進既有系統/技術的 SOTA | DeepMind's evolutionary coding agent improving SOTA of existing systems | |
| OpenEvolve | AlphaEvolve 的開源版本,同期釋出 | Open-source counterpart of AlphaEvolve released around the same time | |
| ADRS (AI-Driven Research for Systems) | Berkeley Sky Computing Lab 的研究方向與部落格系列 | Research thrust and blog series from UC Berkeley's Sky Computing Lab | https://ucbskyadrs.github.io/ ; https://sky.cs.berkeley.edu/project/adrs/ |
| YCSB | 評估 KV / 雲端儲存 workload 的標準 benchmark | Standard benchmark for KV and cloud-serving workloads | 案例中被 agent reward-hack 的對象 / the benchmark the agent hacked |
| "Barbarians at the Gate: How AI is Upending Systems Research" | ADRS 路線的 position paper | Position paper from the ADRS line of work | arXiv 2510.06189;演講中只說「我們寫了 position papers」,未點名 / he said "we wrote position papers" without naming it |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Alpha Evolve / Open Evolve | AlphaEvolve / OpenEvolve |
| Fun Search | FunSearch |
| ADRS ... AI-driven research for systems | ADRS = AI-Driven Research for Systems(拼寫正確,僅大小寫)|
| "we started in June 2026" | 應為 2025 年 6 月 / should be June 2025(同段落隨即說 "over the summer last summer"、"over the past year")|
| set table marks | stable interfaces(依上下文:穩定介面 vs 會變的 API)|
| Byzantine false | Byzantine faults |
| "fail stop test in" | fail-stop testing |
| "you fully improve some requirements" | (口誤/字幕破碎,語意為 revise the requirements)|

## 待確認 / To Verify

- 開場說的 "we started in June 2026" 與後文的「去年暑假」「過去一年」自相矛盾,推測應為 2025 年 6 月,但仍需對照投影片確認。/ The stated start date "June 2026" contradicts "last summer" and "the past year" later in the same segment; likely June 2025, but confirm against the slides.
- 「約 7 篇已發表於頂會」的確切數字與場次未在字幕中列出。/ The exact count and venues behind "around seven published works" aren't in the captions.
- 演講中提到「我們寫了 position papers」(複數),除 "Barbarians at the Gate" 外是否另有其他篇待查。/ He mentions position paper**s**; whether there are others beyond "Barbarians at the Gate" needs checking.
- 最後列出「我們已做的工作」時快速跳過數張投影片,個別專案名稱未被字幕捕捉。/ He skipped several slides listing his group's own work; those project names never appear in the captions.
