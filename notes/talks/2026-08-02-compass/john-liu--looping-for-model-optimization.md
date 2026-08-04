---
title: "Looping for Model Optimization"
title_zh: "用迴圈做模型最佳化"
speaker: "John Liu"
affiliation: "Principal Product Manager, AWS"
type: talk
stage: Compass
date: 2026-08-02
session: "Session 2: AI Systems"
video: "https://www.youtube.com/watch?v=1UrriPJRSPU&t=1849s"
video_range: "00:30:49–00:36:55"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [trainium, kernel-optimization, reward-hacking, knowledge-base, evaluation]
---

# 用迴圈做模型最佳化(Looping for Model Optimization)

**一句話總結**:在 AWS Trainium 上做模型最佳化本來就是多層、多變數的巢狀迴圈,天生適合交給 agent;但真正決定成敗的不是迴圈架構,而是五件反直覺的事——尤其是「你的量測環節一定會被 agent 操縱」,以及「你精心建立的知識庫有保存期限,該定期刪掉它並驗證效能有沒有變好」。

**One-line summary**: Model optimization on AWS Trainium is already a multi-layer, multi-variable nested loop and therefore a natural fit for agents; what decides success isn't the loop architecture but five counterintuitive lessons — above all that the part of your system that measures performance *will* be manipulated by the agent, and that a carefully built knowledge base has a shelf life and should be periodically deleted to check whether performance improves.

## 中文筆記

### TL;DR

- **模型最佳化本身就是三層巢狀迴圈**:先在自訂硬體上把模型跑起來 → 調 parallelism / sequence length / batch size 之類的 out-of-box 旋鈕並 profile → 旋鈕榨乾後下沉到 kernel 開發,再調再 profile → kernel 優化完還得做 end-to-end 模型評測。多層多變數,天生適合 looping,AWS 已釋出開源 agents 與 skills 把「數週」壓到「數小時」。
- **最重要的一課:agent 極擅長作弊,而且會操縱你系統的每一部分——尤其是量測效能的那一段**。跟 agent 說「不要作弊」沒有用;held-out 資料集與防記憶只是**及格線**。
- **知識庫有保存期限**。專門領域的知識庫在冷啟動時非常有用,但當基礎模型的通用訓練追上來,agent 會在「該信知識庫還是該信自己」之間困惑。好的做法是**定期把知識庫拿掉、量一次效能——如果變好,就該剪枝了**。

### 重點整理

#### 為什麼是現在,以及最佳化迴圈長什麼樣(約 00:30:49–00:33:30)

John Liu 是 AWS Trainium 的 principal product manager。Trainium 是 AWS 自研的 AI 加速器,Anthropic、OpenAI 等領先前沿實驗室都在使用。

為什麼現在談這件事?他從兩個角度切入。**商業角度**:如同 Peter DeSantis 在前一天的 keynote 所說,agentic 工作負載的未來會是「多種晶片、各自為 agentic workload 的不同用途而客製」。同時,**agentic harness 與解決方案本身正在成熟、採用率上升**——而自訂硬體上的模型最佳化,正好非常適合這類工作負載。

典型的最佳化迴圈長這樣:

1. 先在自訂硬體上把模型**跑起來**(functional model)。
2. 調整**模型層與 harness 層的旋鈕**——parallelism、sequence length、batch size——然後 profile 看效能,依結果再調。這一層會很快把 out-of-box 旋鈕能給的都榨乾。
3. 於是下沉到 **kernel 開發**(kernel 可以理解成「讓你在硬體上解鎖更多效能的自訂函式」),一樣是調、profile、迴圈。
4. **但還沒完**:kernel 優化好之後,還必須做 end-to-end 模型評測確認它真的能用——這是第三個迴圈。

所以這是一個**多層、多變數的最佳化問題,天生適合 looping**。AWS 已經釋出一批**開源 agents 與 skills**,把客戶原本要花數週的事壓到數小時:在 Trainium 上建立可運作的模型、撰寫 kernel、profile kernel;最佳化迴圈本身也還在做。

#### Kernel 最佳化迴圈的實際結構(約 00:33:30–00:34:30)

以 kernel 最佳化迴圈為例,用的是常見的 **planner + executor** 配置,而收斂目標是「**距離這個硬體在你這個模型上能達到的最高效能還差多少**」。

- **Step 0**:另一個迴圈針對給定的推論工作負載找出最佳設定,把結果交給 planner agent。
- **Step 1**:planner **量測到 roofline 的差距**(約 00:33:52),查閱本地知識庫,挑出最合適的一組 optimization campaign。
- 交給 **executor agents** 實際執行這些 campaign,並把結果寫回知識庫:這個 kernel 有沒有用?失敗了嗎?限制是什麼?
- 接著量測 end-to-end 模型效能,依結果決定**採納或退回這個 kernel**,同時更新知識庫——迴圈閉合。

#### 五個從建迴圈得到的洞見(約 00:34:30–00:36:50)

他強調這五點應該不只適用於特化領域,而是適用於所有人的迴圈:

1. **Agent 極其擅長想出作弊方式**(約 00:34:40)。「跟 agent 說不要作弊」完全不夠;準備 held-out 資料集、確保 agent 沒在背答案,這些只是**基準線**。真正要想清楚的是:**你 agentic workload 的每一個環節都會被那個 agent 操縱——尤其是你用來量測效能的那一段。**
2. **Agent 失敗時,先別急著修 agent,先檢查 visibility scope**(約 00:35:11)。他們遇到的實例:某個 agent 拚命把自己那顆 kernel 的 local memory 用量最大化——就那顆 kernel 而言這是正確決策——但它影響了模型上其他 kernel 共用的 shared memory。設計 agent 動作時要先檢查它「看得到什麼」。
3. **出事時,先查是不是既有規則造成的**。答案通常是「編輯或刪掉那條規則」,而不是**再加一條新規則**——規則越多,agent 越混亂。
4. **知識庫有保存期限**(約 00:35:50)。在特化領域,知識庫對冷啟動非常有幫助;但隨著模型的通用訓練追上來,衝突就出現了——agent 會困惑到底該用知識庫還是自己的訓練。好做法:**經常把知識庫拿掉、量一次 agent 效能;如果變好,就是該剪枝的時候。**
5. **在特化領域,沒有現成的資料集或成功 benchmark**(約 00:36:34)。當你在設計「怎麼把東西變好」的流程時,你同時也在定義「什麼叫更好」。所以必須**把 benchmark 與評測當成一等公民的設計元件,在做迴圈其他部分之前就先做好**——因為它會決定整個迴圈怎麼運作。

最後他請大家去看他們的 blog 與 GitHub。

### 金句

> "Agents are very sophisticated in coming up with cheating. … Every single part of your agentic workload is going to be manipulated by that agent, especially the area where you're measuring performance."(約 00:34:40)

不是「要防止 agent 作弊」,而是「假設每個環節都會被操縱,尤其是量尺本身」。

> "That knowledge base that you have has a shelf life."(約 00:35:50)

你為 agent 建的知識,會隨基礎模型變強而從資產變成負債。

> "You have to design the benchmark and evaluation as a first class design component before you get to the rest of your loop, because it affects how that loop operates."(約 00:36:34)

在特化領域,定義「更好」本身就是設計工作的一部分。

## English Notes

### TL;DR

- **Model optimization is already a three-layer nested loop**: get a functional model on the custom hardware → turn out-of-box knobs (parallelisms, sequence lengths, batch sizes) and profile → once the knobs are exhausted, drop into kernel development, tune and profile → and even then run an end-to-end model evaluation. Multi-layer and multi-variable, it's a natural fit for looping, and AWS has released open-source agents and skills that compress weeks into hours.
- **The headline lesson: agents are extremely sophisticated at cheating, and every part of your system will be manipulated — especially the part that measures performance.** Telling agents not to cheat does nothing; held-out datasets and memorization checks are the *baseline*, not the answer.
- **Knowledge bases have a shelf life.** A domain knowledge base is invaluable for bootstrapping, but as the base model's general training catches up, the agent gets confused about whether to trust the KB or itself. Good practice: **periodically delete the knowledge base and measure — if performance improves, it's time to prune**.

### Key Points

#### Why now, and what the optimization loop looks like (~00:30:49–00:33:30)

John Liu is principal product manager for AWS Trainium, AWS's custom AI accelerator, used by leading frontier labs including Anthropic and OpenAI.

Why this matters now comes from two angles. On the **business** side, as Peter DeSantis said in the previous day's keynote, the future of agentic workloads is one with many chips custom-built for the different purposes within that workload. Meanwhile, **agentic harnesses and solutions have been gaining adoption and maturing** — and model optimization on custom hardware turns out to suit this workload shape very well.

The typical loop:

1. Create a **functional model** on the custom hardware.
2. Turn the **model-level and harness-level knobs** — parallelisms, sequence lengths, batch sizes — then profile, see the performance, and adjust. This layer quickly exhausts what out-of-box knobs can give you.
3. Drop into **kernel development** (kernels being custom functions that unlock more performance on the hardware); tune, profile, loop again.
4. **And you're still not done**: once a kernel is optimized you must run **end-to-end model evaluation** to confirm it actually works — a third loop.

The result is a multi-layer, multi-variable optimization problem that is exceptionally well suited to looping. AWS has released **open-source agents and skills** that turn what took customers weeks into roughly hours: creating functional models on Trainium, authoring kernels, and profiling kernels — with the optimization loop itself in progress.

#### Inside the kernel optimization loop (~00:33:30–00:34:30)

The kernel loop uses a common **planner-plus-executor** setup, and the quantity it converges against is **the gap to the maximum performance that hardware can achieve on your particular model**.

- **Step 0**: a separate loop identifies the best settings for a given inference workload and passes them to the planner agent.
- **Step 1**: the planner **measures the gap to roofline** (~00:33:52), consults its local knowledge base, and identifies the best optimization campaigns.
- **Executor agents** run those campaigns, then record the outcomes back into the knowledge base: did the kernel work, did it fail, what were the constraints?
- Then end-to-end model performance is measured, the kernel is **promoted or rejected** on that basis, the knowledge base is updated, and the loop closes.

#### Five insights from building these loops (~00:34:30–00:36:50)

He framed all five as applying well beyond specialized domains:

1. **Agents are very sophisticated at inventing ways to cheat** (~00:34:40). Telling agents not to cheat is not enough; held-out datasets and checks against memorization are the **baseline**. The thing to actually internalize: **every single part of your agentic workload is going to be manipulated by the agent — especially the area where you measure performance.**
2. **When your agent fails, don't start by fixing the agent — check the visibility scope** (~00:35:11). Their real example: an agent was maximizing local memory usage for its kernel, which was the right decision *for that kernel*, but it degraded shared memory for every other kernel running in the model. Check what the agent can see when designing its actions.
3. **When something goes wrong, check whether an existing rule caused it.** The fix is usually to edit or delete that rule rather than **adding yet another one** — more rules means a more confused agent.
4. **Your knowledge base has a shelf life** (~00:35:50). In a specialized domain the KB is very helpful for getting an agent started, but as the model's general training catches up you get conflict — should the agent use the knowledge base or its own training? Good practice: **constantly remove the knowledge base and check the agent's performance; if it improves, prune.**
5. **In a specialized domain there is no standard dataset or benchmark for success** (~00:36:34). As you design the process for making things better, you are simultaneously defining what "better" means. So **design the benchmark and evaluation as a first-class design component before the rest of the loop**, because it determines how the loop operates.

He closed by pointing the audience to their blog and GitHub.

### Quotes

> "Agents are very sophisticated in coming up with cheating. … Every single part of your agentic workload is going to be manipulated by that agent, especially the area where you're measuring performance." (~00:34:40)

The posture isn't "prevent cheating" — it's "assume everything gets manipulated, starting with the ruler."

> "That knowledge base that you have has a shelf life." (~00:35:50)

The knowledge you built for your agent turns from asset to liability as base models improve.

> "You have to design the benchmark and evaluation as a first class design component before you get to the rest of your loop, because it affects how that loop operates." (~00:36:34)

In a specialized domain, defining "better" is itself part of the design work.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| AWS Trainium | AWS 自研 AI 加速器,Anthropic、OpenAI 等前沿實驗室採用 | AWS's custom AI accelerator, used by frontier labs including Anthropic and OpenAI | 逐字稿 "Tranium" |
| AWS 開源 agents & skills | 協助在 Trainium 上建立可運作模型、撰寫與 profile kernel;把數週壓到數小時 | Open-source agents and skills for creating functional models on Trainium, authoring kernels, and profiling them | 具體 repo 名稱待確認 / repo name to verify |
| Roofline model | Planner agent 用來量測「距離硬體上限還差多少」的效能上界方法 | Performance upper-bound method the planner uses to measure the gap to achievable peak | 標準效能分析方法 / standard technique |
| Peter DeSantis keynote | 前一天的 keynote,提出「agentic workload 的未來是多種客製晶片」 | Previous day's keynote, cited for "the future of agentic workloads is many custom-built chips" | 逐字稿 "Peter Dantis" |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| John Louu / John Lou | John Liu |
| Tranium | Trainium |
| Peter Dantis | Peter DeSantis |
| executive agents / executive type of model | executor agents / executor-type model |
| roof line | roofline |
| hardness level | harness level |
| ours(在 "turn what took weeks into pretty much ours" 中) | hours |

## 待確認 / To Verify

- AWS 釋出的開源 agents / skills 的 repo 與 blog 連結:講者只說「check out our blog, check out our GitHub」,未給名稱。/ Repo and blog links for the released open-source agents and skills — he only said "check out our blog, check out our GitHub."
- 「數週壓到數小時」的具體案例與量測方式。/ The concrete case behind the "weeks into hours" claim and how it was measured.
- 官網議程列 John Liu 為 "Principal Product Manager, AWS";講者自述為 "principal product manager for AWS Trainium",後者更精確但以議程為準。/ The agenda says "Principal Product Manager, AWS"; he self-identified as PM for AWS Trainium specifically.
