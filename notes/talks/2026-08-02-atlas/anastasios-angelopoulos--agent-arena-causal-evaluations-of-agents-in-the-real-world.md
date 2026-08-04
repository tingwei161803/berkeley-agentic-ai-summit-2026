---
title: "Agent Arena: Causal Evaluations of Agents in the Real World"
title_zh: "Agent Arena:在真實世界中對 agent 做因果評估"
speaker: "Anastasios N Angelopoulos"
affiliation: "Co-Founder/CEO, LLMArena"
type: talk
stage: Atlas
date: 2026-08-02
session: "Session 2: Agent Evaluation & Benchmarks"
video: "https://www.youtube.com/watch?v=-7AJJLwYW1Q&t=48s"
video_range: "00:00:48–00:12:50"
transcript: "tmp/[English (auto-generated)] Atlas Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [evaluation, causal-inference, leaderboard, benchmarks, human-feedback]
---

# Agent Arena:在真實世界中對 agent 做因果評估(Agent Arena: Causal Evaluations of Agents in the Real World)

**一句話總結**:靜態 benchmark 會被 overfit、又跟 production 有分佈落差,唯一不能作弊的裁判是現實世界;Arena 用「每週數百萬筆真實 agentic traces + 隨機化模型做因果推論」,把 treatment effect 而不是分數,做成 agent 排行榜。
**One-line summary**: Static benchmarks get overfit and drift away from production, so the only judge that can't be gamed is reality — Arena randomizes the model inside millions of weekly organic agentic traces and reports causal treatment effects, not scores, as its agent leaderboard.

## 中文筆記

### TL;DR

- **評估哲學**:「唯一重要的裁判是現實」。Arena 不做靜態 benchmark,而是量測模型在部署後對真實使用者的影響,因為要在現實中得分,你就真的得把別人的工作做完。
- **Arena 的基本原理(fundamental principle)**:提供回饋這件事本身必須對使用者有價值。使用者投票給自己偏好的回應後就接著用那個回應繼續對話,所以誠實投票才符合自身利益——這是免費拿到數百萬筆高品質資料的原因。
- **兩種資料**:(1) pairwise preference(一個 prompt、兩個回應、投票);(2) **trace mining**——單一回應但橫跨數天數週的長對話,可挖出任務完成、幻覺率、可導引性、錯誤率、使用者稱讚/抱怨等訊號。
- **規模**:35M 月訪問量,是 2020 年後成立新創的訪問量前十;28% 的流量是軟體工程,等於「每週一千個 SWE-bench 份量」的真實 coding 資料。
- **方法論創新**:agentic thread 中使用者看不到模型,Arena 可以**隨機化模型**來介入系統,因此能做**因果推論**——把 orchestrator / tools 視為 treatment,量測 treatment effect,而不只是相關性排名。

### 重點整理

#### Arena 的評估哲學:唯一的裁判是現實(約 00:01–00:03)

Arena 起源於 Berkeley 的學生專案(他當時師從 Mike Jordan 與 Jitendra Malik,並與 Ion Stoica 合作),後來各家模型實驗室都跑來平台上競爭,才長成一家公司。約 7 週前推出 Agent Arena,已有數百萬使用者在 arena.ai 上使用 agent。

核心主張:靜態 benchmark 有兩個致命傷——**可以被 overfit**,而且**收集資料的分佈和 production 實際發生的事情有落差**。Arena 的做法反過來:量測模型部署後的真實影響。這個訊號不能被 gaming,因為要在現實中做好,你就必須真的完成別人的工作。

#### 兩種資料與「回饋即價值」的飛輪(約 00:03–00:06)

- **Pairwise preference**:一個 prompt、兩個回應、使用者投票。
- **Trace mining**:離開對戰機制,一個 prompt 一個回應,但形成橫跨數天數週的多輪長對話。他舉的例子是一位使用者用波斯語進行了 84 輪對話、600+ 次 tool call,建出一個 RAG 財經知識系統,附完整架構流程圖與一組通過的 160 項測試。

他特別點出一條沒寫在投影片上的「Arena 基本原理」:**提供回饋的動作本身必須把價值還給使用者**。投票之後使用者會帶著自己選的回應繼續聊,所以沒有人有動機亂投——不想毀掉自己的對話,就會誠實投票。這就是不用付錢也能累積數百萬筆高品質資料的原因。

從這些資料中用自動化 pipeline 挖出的訊號包括:任務完成(使用者明確按鈕告知)、幻覺率、可導引性(steerability)、錯誤率、使用者挫折、稱讚與負面情緒。

#### 規模與使用者組成(約 00:05–00:07)

以訪問量計,在 2020 年後成立的新創中 Arena 排進前十,比 xAI、Hugging Face、Manus、Genspark 都大,月訪問 3,500 萬。使用者組成:軟體 28%、科學 17%、金融 12%、數學 10%、法律 6%、醫療 6%,都在跑跨供應商的 agentic workflow。他形容 28% 的軟體流量等於「每週一千個 SWE-bench」份量的真實世界 coding 評估資料。

#### Agent Arena 實際長什麼樣(約 00:07–00:09)

Demo:使用者輸入「下載 Google 2026 Q1 財報電話會議逐字稿並做成 PowerPoint」→ 平台開一台電腦給 agent 用 → agent 上網找逐字稿、下載到 workspace、用 bash 生成 PPT → 使用者可捲動檢視 → 接著說「把它變成一個更有 Google 品牌感的網站」→ agent 再用 bash 做出網站。最後使用者可以按「Yes, my task was successful」。

**每一則使用者訊息都是一次回饋機會**。他半開玩笑地說,那些「Screw you, I hate that response」是意圖非常明確的高品質負面訊號;而在 20 輪對話後補一句「Thank you, good job」則會因為整段 context 被重送而花掉你 10 美元,提醒大家注意花費。

#### 從 Elo 走向因果推論(約 00:09–00:11)

早年 Arena 把 Bradley–Terry / Elo 帶進這個領域;這次是另一個「把老牌統計方法帶進 AI 評估」的例子:**因果推論**。

關鍵在於——在 agentic thread 裡使用者看不到背後是哪個模型,所以 Arena 可以**隨機化模型來介入系統**。有了隨機化,就能把 agent 的 orchestrator 或 tools 當成 **treatment**,量測「換成 Fable 當 orchestrator vs. 用其餘模型的隨機平均當 baseline」的 treatment effect。arena.ai/leaderboard 的預設榜就是這個 agent 榜:本質上是一場跨 agent 各子元件的大型多因子 A/B 實驗。

榜由多個訊號編成,目前約 25 個,包括:任務完成(明確按鈕)、praise vs complaint 比例、幻覺率(把每一條事實主張抽出來,用一批搜尋模型上網驗證真偽)、steerability(使用者抱怨後模型是一次修對,還是使用者得反覆講同一件事)、bash 錯誤復原(會不會犯錯、犯錯後能不能自己救回來)。他強調這些訊號在 benchmark 上看不到——benchmark 上模型幾乎不犯錯,因為都 overfit 了;放到真實使用情境完全是另一回事。

每個訊號各自產生一張 causal effect 榜,附以極限定理算出的信賴區間,並以中央那條灰線(baseline)為基準。再用加權平均把多訊號聚合成單一榜——他指出這正是因果方法的另一個好處:**可以把很多訊號合成一個有意義的總結**。也可以按 cost per task、latency 拆解。

他展示的那版榜(數週前)Fable 在 agent arena 居首,Kimi 緊追。

### 金句

> "Our philosophy on evaluations is that there's only one judge that matters and that's reality."(約 00:02)

現實是唯一無法被 overfit 的評估集。

> "The fundamental principle of Arena is that the act of providing feedback should be value back to the user."(約 00:04)

這條原理解釋了為什麼 Arena 不用付錢就能拿到數百萬筆偏好資料——誠實回饋對使用者自己最有利。

> "If you go look at any benchmark, models are not making errors at all because they've all overfit to them. But here in reality … it's a very different story."(約 00:10)

benchmark 上的零錯誤率,是 overfit 的產物,不是能力的證明。

## English Notes

### TL;DR

- **Evaluation philosophy**: "there's only one judge that matters and that's reality." Arena measures post-deployment impact instead of static benchmark scores, and that signal can't be gamed — doing well in reality means actually finishing real people's jobs.
- **The fundamental principle of Arena**: giving feedback must itself return value to the user. Voting for the better response means you continue the conversation with it, so honest voting is self-interested — that's how millions of high-quality data points come in for free.
- **Two data types**: pairwise preference battles, and **trace mining** — single-response, multi-day/multi-week conversations that can be mined for task completion, hallucination rate, steerability, error rates, praise and complaints.
- **Scale**: 35M monthly visits, top-10 by traffic among startups founded since 2020; 28% of usage is software, which he frames as "the equivalent of a thousand SWE-benches every week" of real-world coding data.
- **Methodological move**: because the model is hidden inside agentic threads, Arena can intervene by **randomizing the model**, which turns the leaderboard into **causal inference** — treating the orchestrator or tools as a treatment and reporting treatment effects rather than correlational scores.

### Key Points

#### Reality as the only judge (~00:01–00:03)

Arena began as a Berkeley student project (he was a PhD student working with Mike Jordan and Jitendra Malik, in collaboration with Ion Stoica), grew as the model labs started competing on the platform, and became a company. Agent Arena shipped about seven weeks before the talk and already serves millions of users on arena.ai.

The argument against static benchmarks is twofold: they can be overfit, and there is a distribution shift between what you can collect a dataset for and what actually happens in production. Arena instead measures post-deployment impact — a signal that resists gaming because succeeding in reality requires actually completing real people's work.

#### Two data types and the feedback flywheel (~00:03–00:06)

Pairwise preference data is the familiar format: one prompt, two responses, a vote. **Trace mining** is the less familiar one: one prompt, one response, but embedded in long multi-turn conversations that run over days and weeks. His example was a user who architected a RAG-based financial knowledge system — an 84-turn conversation over many days, conducted in Persian, with 600+ tool calls, ending in a full architecture flowchart and a passing 160-test suite.

Off the slide track, he stated what he calls the fundamental principle of Arena: **the act of providing feedback should return value to the user**. After voting, the user continues in the chat with the response they preferred, so anyone who doesn't want to wreck their own conversation is incentivized to vote their true preference. That is why millions of high-quality votes arrive without paying annotators.

Automated pipelines mine these traces for task-completion signals (explicit button clicks), hallucination rates, steerability, error rates, user frustration, praise, and negativity.

#### Scale and user mix (~00:05–00:07)

By visits, Arena is top-10 among startups founded since 2020 — bigger than xAI, Hugging Face, Manus, and Genspark — at 35 million monthly visitors. The workload mix: 28% software, 17% sciences, 12% finance, 10% math, 6% legal, 6% medicine, all running cross-provider agentic workflows.

#### What Agent Arena looks like (~00:07–00:09)

In the demo, a user asks for Google's Q1 2026 earnings call transcript to be downloaded and turned into a PowerPoint. Arena spawns a computer; the agent searches the web, downloads the transcript into its workspace, and uses bash to build the deck. The user then asks to convert it into a more Google-branded website, and the agent builds that too. At the end the user can click "Yes, my task was successful."

Every message a user sends is a feedback opportunity. Angry messages are extremely high-intent signal; so is "good job." His aside: appending "thank you, good job" to a 20-turn conversation can cost $10 because the whole context gets resent.

#### From Elo to causal inference (~00:09–00:11)

Arena introduced Bradley–Terry / Elo to this space; the agent leaderboard is a second instance of importing tried-and-true statistics into AI evaluation, this time **causal inference**.

The enabling fact is that users don't see which model is behind an agentic thread, so Arena can intervene by randomizing it. With randomization, the orchestrator or the tools can be treated as a **treatment**, and you can ask what happens if you use Fable as the orchestrator versus a baseline that is a randomized average of the rest. The default leaderboard at arena.ai/leaderboard is exactly this: a large multi-factor A/B experiment across the agent's subcomponents, reported as treatment effects.

Roughly 25 signals feed it, including confirmed task completion, praise-versus-complaint ratio, hallucination rate (every factual claim is stripped out and checked against the web by search models), steerability (does the model land the fix after the first complaint, or does the user keep repeating themselves?), and bash error recovery. His point about why organic data matters: on benchmarks models appear to make no errors at all because they have all overfit; on a real user's actual workload the picture is completely different.

Each signal yields its own causal-effect leaderboard with confidence intervals derived from limit theorems, centered on a gray baseline line. A weighted average aggregates them into one leaderboard — which he flags as another benefit of the causal methodology: it lets you combine many signals coherently. Results can also be broken out by cost per task and latency. On the version shown (a few weeks old), Fable led the agent arena with Kimi close behind.

### Quotes

> "Our philosophy on evaluations is that there's only one judge that matters and that's reality." (~00:02)

Reality is the one evaluation set that can't be overfit.

> "The fundamental principle of Arena is that the act of providing feedback should be value back to the user." (~00:04)

The design principle behind the free data flywheel.

> "If you go look at any benchmark, models are not making errors at all because they've all overfit to them. But here in reality … it's a very different story." (~00:10)

A zero error rate on a benchmark is evidence of overfitting, not of capability.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| arena.ai | Arena 的消費端應用,pairwise 對戰與 agent 使用皆在此 | Arena's consumer app; both pairwise battles and agent usage live here | 演講中示範的即是此站 / the site demoed in the talk |
| Agent Arena | 約 7 週前推出的 agent 使用與評估產品 | Agent product/eval surface launched ~7 weeks before the talk | 使用者可用電腦、bash、瀏覽器完成任務 / agents get a computer, bash, and web access |
| arena.ai/leaderboard | 預設即為 agent 榜,基於 treatment effect | Default view is the treatment-effect-based agent leaderboard | 約 25 個訊號加權聚合 / ~25 signals aggregated by weighted average |
| Bradley–Terry / Elo | Arena 早期引入的成對比較統計方法 | The pairwise-comparison statistics Arena originally brought to this space | 本次以因果推論延伸 / extended here by causal inference |
| SWE-bench | 用來比喻 Arena 每週真實 coding 資料量 | Used as the unit of comparison for Arena's weekly volume of real coding data | 「每週約一千個 SWE-bench」/ "a thousand SWE-benches every week" |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| LM Arena / L Arena | LLMArena(官網議程用字)/ per the official agenda |
| Anastasios(多處拼寫不一) | Anastasios N Angelopoulos |
| Jitendra Malik / Mike Jordan | 正確,無需更正 / correct as heard |
| Manas | Manus |
| Gen Gen Spark | Genspark |
| Kimmy | Kimi |
| sweet benches | SWE-bench |
| anastasia@arena.ai | 疑為 anastasios@arena.ai(待確認)/ likely anastasios@arena.ai (to verify) |

## 待確認 / To Verify

- 公司/品牌正式名稱:官網議程寫 LLMArena,講者口說「Arena」、網站為 arena.ai;三者關係(改名?產品線?)待確認。/ Official brand: the agenda says LLMArena, the speaker says "Arena", the site is arena.ai — relationship between the three needs confirming.
- 簡報中的聯絡信箱第二個地址(字幕聽成 anastasia@arena.ai),需看投影片確認。/ The second contact email shown on the slide.
- Agent Arena 的正式上線日期(講者只說「約 7 週前」)。/ Exact launch date of Agent Arena (he only said "about 7 weeks ago").
- 35M 月訪問量、以及「2020 年後新創前十」的資料來源(投影片有標註來源但字幕未提)。/ Source for the 35M monthly visits and the top-10 ranking shown on the slide.
- 榜上「約 25 個訊號」的完整清單,字幕僅列出其中五、六項。/ Full list of the ~25 leaderboard signals; only five or six were named aloud.
