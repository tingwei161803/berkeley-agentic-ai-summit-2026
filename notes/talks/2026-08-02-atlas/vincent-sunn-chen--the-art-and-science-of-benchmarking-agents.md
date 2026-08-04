---
title: "The Art & Science of Benchmarking Agents"
title_zh: "評測 Agent 的藝術與科學"
speaker: "Vincent Sunn Chen"
affiliation: "VP & Founding Member, Snorkel AI"
type: talk
stage: Atlas
date: 2026-08-02
session: "Session 1: Enterprise AI"
video: "https://www.youtube.com/watch?v=LGW_6P1CMC8&t=2786s"
video_range: "00:46:26–00:59:34"
transcript: "tmp/[English (auto-generated)] Atlas Stage - August 2nd - Morning Session [DownSub.com].srt"
status: draft
tags: [benchmarks, evaluation, swe-bench, data-quality, agentic-ai]
---

# 評測 Agent 的藝術與科學(The Art & Science of Benchmarking Agents)

**一句話總結**:我們量測 AI 的能力已經被開發 AI 的能力甩開,而「vibe code 一個 benchmark 換一則漂亮推文」的 bench slop 正在惡化這件事;真正能留下來的 benchmark 需要一個對前沿的下注、一份給社群的路線圖、以及近乎偏執的任務品質控管——Snorkel 的 Senior SWE-Bench 就是照這套原則做的。
**One-line summary**: Our ability to measure AI has been outpaced by our ability to build it, and "bench slop" — vibe-coding a benchmark for a nice Twitter post — makes it worse; benchmarks that last need a thesis about the frontier, a roadmap the community can build on, and near-obsessive task quality control, which is how Snorkel built Senior SWE-Bench.

## 中文筆記

### TL;DR

- **核心問題**:「我們量測 AI 的能力,已經被我們開發 AI 的能力甩開了。」Benchmark 越來越重要——它們在引導研究議程、模型發表與數十億美元的算力投向——但也越來越難建。
- **兩個新病灶**:**bench slop**(快速 vibe code 一個 benchmark、換一則漂亮的推文,但單一任務的品質極差),以及模型在**reward hacking 與欺騙出題者**這件事上同步變強,讓出題變成貓捉老鼠。
- **好 benchmark 的三個條件**:(1) 帶著一個對前沿的**下注**(Terminal-Bench 押注「agent 的未來發生在文字介面」是對的);(2) 為整個領域**設定路線圖**(SWE-Bench 開枝散葉成一整個系列);(3) 認真對待 **researcher UX**——讓別人容易在上面建東西。
- **Senior SWE-Bench 的四個設計**:天然 under-specified 的指令(Slack 訊息、一坨 error log,而不是完整 spec)、長 horizon 且跨服務的任務、可持續從最新開源 repo 補題、以及 **tasteful solve**——除了正確性,還量測 codebase 對齊、實務對齊、相對 Oracle PR 的 bloat。
- **量測的科學**:任務品質(GPQA 那篇附錄談如何用**報酬機制**逼出高品質貢獻)、明確的分類法(MMLU)、難度與 headroom、以及可靠的出題方法論。他們的 QC 是 agentic + 專家 in-the-loop 雙軌,逐題檢查 verifier 的非決定性與偽陽/偽陰。
- **未來三個軸**:環境複雜度與真實度、自主 horizon、以及**輸出複雜度**——從可驗證領域走進法律、醫療這種「好」沒有封閉解的領域。

### 重點整理

#### 問題:量測能力被開發能力甩開(約 00:47–00:51)

他先交代 Snorkel 的來歷:團隊源自 Chris Ré 在 Stanford 的研究群,以及 Alex Ratner 與 Fred Sala 分別在 Washington 與 Wisconsin 的研究群,十多年來聚焦在**以資料為中心(data-centric)** 的前沿 AI 方法。這讓他們現在能以資料與研究夥伴的身分,參與許多開放 benchmark:

- **Agents' Last Exam**(Dawn Song 團隊)——他們協助其中的品質控管機制;
- **Continual Learning Bench**(同樣出自 Berkeley,Sky Lab)(名稱待確認);
- **OSWorld 2.0**;
- **Terminal-Bench** 最近幾個版本(就在演講前幾週出貨)。

接著是整場的核心命題:**我們量測 AI 的能力,已經被我們開發 AI 的能力甩開了。**

他用 coding 舉例說明難度的攀升:HumanEval 幾年前推出時就已經在 95%;而最近那批最難的程式 benchmark 只有 3%。當你沿著複雜度往上爬,**光是「驗證」與「評估」前沿任務本身就變得極度困難**。

同時 benchmark 的重要性也前所未有:它們在引導研究議程、模型發表,以及**數十億美元等級的算力**往哪個山頭爬。

所以他主張:**建 benchmark 本身就是一個非平凡的研究領域。** 兩個具體病灶——

- **Benchmaxing**:模型針對測驗調校,這是真實存在的問題,需要更用心的設計與社群共同貢獻,才能給這個領域有效的標準與量尺。
- **Bench slop**(他自創的說法):你可以很快 vibe code 出一個 benchmark、發一則漂亮的推文,但**單題品質是不合格的**;要做出極高品質的任務需要投入大量心力。

還有第三重壓力:模型能力提升的同時,**它們在 reward hacking、在騙過出題者這件事上也一起變強**,於是建 benchmark 的方法論本身變成一場貓捉老鼠。

他也點出資料形狀的變化:agentic AI 讓資料從單純的 prompt–response 配對、單純的按讚/倒讚回饋,變成**由 RL 環境構成的複雜堆疊**——rubric、verifier、工具,乃至整個模擬日常情境的世界。這讓「量測」本身又更難了一層。

他用一張二維圖說明還有多少空間:**y 軸是 sequence length,也就是自主的長度;x 軸是輸入/輸出與環境的複雜度**。有些任務飽和了,不代表這個領域做完了——例如程式領域,即使近一兩年進展驚人,長尾仍然很長,benchmark 這邊還有大量工作要做。

#### 好 benchmark 的三個條件,與 Senior SWE-Bench 的四個設計(約 00:52–00:56)

他們上個月推出 **Senior SWE-Bench**,與 Princeton 原始的 SWE-Bench 團隊合作。核心論點是:**我們的 agent 已經遠遠超過 junior 工程師的能力,但我們沒有好方法在 senior 這個層級評估它們。**

那麼,講到 senior 工程師你會想到什麼?他的答案是三件事:能接住 under-specified 的需求、能拿著一個模糊問題自己跑起來、以及**有品味(taste)**。這一版就是要處理這三件事。

他先講什麼樣的 benchmark 是有效的:

1. **它本身是一個重要的研究議程**——最好的 benchmark 對前沿有很強的論點,是在**下注**這個領域要往哪走。他認為 Terminal-Bench 團隊做得非常好:幾年前他們押注「agent 的未來會發生在介面上,也就是 LLM 與 agent 已經很擅長的文字介面」——事後看是完全正確的賭注,現在它是**幾乎每一張前沿模型 model card 上都會出現**的 benchmark 之一。
2. **它為領域設定路線圖**——SWE-Bench 幾年前發表後長成了一整個系列,他們很高興能接上這條血脈。好的 benchmark 是好的研究工具,能替後續的同行鋪路。
3. **它認真對待 researcher UX**——怎麼讓別人容易在上面建東西?怎麼設計出對的原語,讓社群成員真的能貢獻?

對應到 Senior SWE-Bench 的四個設計:

- **天然 under-specified 的指令**。你在 Slack 上找一位 senior 或 principal 工程師時,不會給他完整規格文件、不會逐行說明做什麼不做什麼。你給的是 Slack 訊息:「這是一坨 error log,去查一下」,或者「這是我認為的幾條 user story,你想辦法搞定」。他們用專家網路加上一些內部方法來捕捉這個特性。
- **長得多的任務 horizon**。這些任務挑戰的是工程能力,涉及**跨服務的修改**,而不是單一位置的一個 patch;刻意瞄準複雜、長 horizon 的任務。
- **可持續擴充**。不是一次性的努力,而是能**持續從最新的開源 repo 補題**,讓其他研究者可以在上面繼續建。
- **品味(taste)**。他們認為品味與可維護性是現代高品質軟體工程的核心,而這正是當前這一波 benchmark 缺的。於是他們引入 **tasteful solve** 這個概念:不只量測正確性,還量測 **codebase 對齊、實務對齊、相對於 Oracle PR 的 bloat** 等多項指標(細節在部落格與網站上)——也就是**正確性以外的品質**。

#### 量測的科學:從 GPQA、MMLU 到他們自己的 QC(約 00:56–00:58)

他挑了幾個「我最愛的 benchmark 精選集」來說明什麼讓一個 benchmark 成為強力的量尺:

- **任務品質**:GPQA 讓他印象非常深刻,尤其是附錄的其中一頁——那頁談的是**如何用報酬與激勵機制驅動貢獻者**,而這直接帶來了極高的品質。
- **分布控制與明確分類法**:MMLU 定義了一套學術分類法,在當時是非常有企圖心的做法。
- **難度與 headroom**:確保前沿模型還有往上跑的空間。
- **穩健的方法論**:如何取得與建構任務,最終對 benchmark 的有效性至關重要。

他們自己在 Senior SWE-Bench 上實作了非常嚴格的品質控管:**每一題**都經過 agentic 與**專家 in-the-loop** 雙軌的 QC,用來抓 verifier 的**非決定性**與**偽陽性 / 偽陰性**;包括他自己與 Snorkel 幾位資深研究員在內的多位專家,連同專家網路裡的真實在職軟體工程師,逐題「痛苦地」看過,才把可靠性撐起來。

**排行榜結果**(他說就在演講前一週更新,結果三重確認過):在 **tasteful solve** 這個指標上,目前**第一名是三方並列**——Fable、Opus 與另一個模型(字幕聽作 "Soul",待確認)。他認為以 Pareto 效率的角度看這個結果相當值得玩味。排行榜位於 senior-swe-bench.snorkel.ai。

**協作者**:由 Snorkel 共同創辦人 Henry(Henry Ehrenberg)主導,與 Princeton 原始 SWE-Bench 團隊、Karthik 的研究群(名字待確認)、以及 Snorkel 首席科學家 Fred Sala 與 Wisconsin 的幾位夥伴合作。

#### 未來:benchmark 該推的三個軸(約 00:58–00:59)

1. **環境複雜度與真實度**:不只是簡單的 prompt 與 response,而是真實的 codebase 環境、科學計算環境、法務工作流——人們每天實際在裡面工作的真實系統。
2. **自主 horizon**:這些模型自主運作能走多遠,以及在各種情境下如何把人拉進來。
3. **輸出複雜度**:不只是可驗證的領域,還要進入**法律、醫療**這類細膩領域——在那裡,「好」不像數學那樣有一個簡單的封閉解。

**行動呼籲**:Snorkel 正在**資助**一批這類 benchmark(Open Benchmarks Grant),歡迎有相關題目的人合作,入口在 benchmarks.snorkel.ai。

### 金句

> "Our ability to measure AI has really been outpaced by our ability to develop it."(約 00:48:42)

整場演講的問題陳述。

> "What I'll call bench slop — the idea that you can really quickly vibe code a benchmark and get a fancy Twitter post."(約 00:49:50)

這一波 benchmark 通膨最精準的命名。

> "Not only are we measuring correctness, but we're measuring notions of codebase alignment, practice alignment, bloat relative to an Oracle PR."(約 00:55:32)

tasteful solve 的具體內涵——把「品味」變成可量測的東西。

## English Notes

### TL;DR

- **The core problem**: "our ability to measure AI has really been outpaced by our ability to develop it." Benchmarks matter more than ever — they steer research agendas, model releases, and billions in compute — and they keep getting harder to build.
- **Two new pathologies**: **bench slop** (vibe-coding a benchmark quickly and getting a fancy Twitter post while individual task quality is lacking), and models improving at reward hacking and deceiving benchmark builders, which turns methodology into a cat-and-mouse game.
- **Three properties of benchmarks that last**: they carry a **bet on the frontier** (Terminal-Bench's wager that agents' future happens at the text interface was correct); they **set a roadmap** the field builds on (SWE-Bench spawned a whole series); and they take **researcher UX** seriously so others can extend them.
- **Senior SWE-Bench's four design choices**: naturally under-specified instructions (Slack messages and error-log dumps, not a full spec), much longer-horizon multi-service tasks, a design that keeps sourcing from the latest open-source repos, and **tasteful solve** — measuring codebase alignment, practice alignment, and bloat relative to an Oracle PR alongside correctness.
- **The science of measurement**: task quality (GPQA's appendix on how pay and incentive mechanisms produced quality), a concrete taxonomy (MMLU), difficulty and headroom, and a robust sourcing methodology. Their own QC ran every task through both agentic and expert-in-the-loop checks for verifier non-determinism and false positives/negatives.
- **Three axes for the future**: environment complexity and realism, the autonomy horizon, and output complexity — moving past verifiable fields into legal and healthcare, where "good" has no closed-form definition.

### Key Points

#### Measurement has fallen behind development (~00:47–00:51)

He opens with Snorkel's lineage: the team grew out of Chris Ré's group at Stanford plus Alex Ratner's and Fred Sala's groups at Washington and Wisconsin, with a decade-plus focus on data-centric methods for frontier AI. That puts them in a position to partner on open benchmarks as a data and research partner — Dawn Song's **Agents' Last Exam** (where they helped with quality-control mechanisms), a continual-learning benchmark also out of Berkeley's Sky Lab (name to verify), **OSWorld 2.0**, and the most recent versions of **Terminal-Bench**, which shipped in the weeks before the talk.

Then the thesis: our ability to measure AI has been outpaced by our ability to develop it.

Coding illustrates the climb. HumanEval launched several years ago already sitting at 95%; the hardest current programming benchmarks sit around 3%. As you climb the complexity scale, simply *verifying and evaluating* frontier tasks becomes the hard part.

Benchmarks have simultaneously never mattered more — they steer research agendas, model releases, and billions in compute pushed toward hill climbing on particular gaps.

Hence his argument that building benchmarks is a genuine, non-trivial research area. **Benchmaxing** — models tuned to the test — is a real problem requiring more thoughtful design and community contribution. And then there's what he calls **bench slop**: you can quickly vibe-code a benchmark and get a fancy Twitter post out of it, while the quality of the individual tasks is lacking; designing extremely high-quality tasks takes real effort.

A third pressure compounds both: as model capabilities improve, they also improve at reward hacking and at tricking and deceiving benchmark builders, so improving benchmark methodology becomes a cat-and-mouse game.

He also flags a change in the shape of data. Agentic AI moved the field from simple prompt-response pairs and thumbs-up/thumbs-down feedback to a much more complex stack of datasets in RL environments: entire worlds built from rubrics to verifiers to tools, with environments mimicking day-to-day settings. That adds difficulty to measuring these datasets.

His map of the remaining space is two-dimensional: **sequence length — the length of autonomy — on the y-axis, and input/output and environment complexity on the x-axis**. Saturation on some tasks doesn't mean a field is finished; coding has become impressive over the last year or two and still has a long tail and a lot of benchmarking work to do.

#### Three properties of effective benchmarks, and Senior SWE-Bench's design (~00:52–00:56)

They launched **Senior SWE-Bench** the month before the talk, working with the original SWE-Bench team at Princeton. The thesis: agents have moved far beyond junior engineering capability, and there's no good way to evaluate them at the senior level. What do you think of when you think of a senior engineer? Someone who can capture under-specified requirements, take an ambiguous problem and run with it, and has some notion of taste.

The properties he considers essential:

1. **An important research agenda.** The greatest benchmarks have a strong thesis on the frontier — they make a bet on where the field is going. He credits the Terminal-Bench team: years ago they bet that the future of agents would happen at the text-based interface that agents and LLMs already handle well. That bet was correct, and it's now one of the most widely adopted benchmarks, appearing on essentially every frontier model card.
2. **A roadmap for the field.** SWE-Bench, released several years ago, grew into a large series they were happy to contribute to — good benchmarks are research tools that set the stage for colleagues to build on.
3. **Researcher UX.** How do you make it easy for other people to build on top of this, and what primitives let community members actually contribute?

Applied to Senior SWE-Bench:

- **Naturally under-specified instructions.** When you talk to a senior or principal engineer on Slack, you don't hand over a full spec or line-by-line instructions. You send Slack messages: here's a dump of error logs, go investigate; here are a few bullets on the user stories, go figure this out. They captured this working with their expert network plus internal methods.
- **A much longer horizon.** Tasks that challenge engineering skill and involve multi-service changes, not a single localized patch — deliberately targeting complex, longer-horizon work.
- **Built to scale.** Not a one-time effort: it continually sources from the latest open-source repos so other researchers can build on it.
- **Taste.** Taste and maintainability matter in modern high-quality software engineering, and were missing from the current wave of benchmarks. So they introduced the notion of a **tasteful solve**: beyond correctness, measuring codebase alignment, practice alignment, bloat relative to an Oracle PR, and other metrics documented on the blog and website.

#### The science: from GPQA and MMLU to their own QC (~00:56–00:58)

He runs through a "greatest hits" tour of what makes a benchmark a strong measuring tool. **Task quality**: GPQA impressed him, especially an appendix page on how pay incentives and contributor-incentive mechanisms led to very high quality. **Distributional control and a concrete taxonomy**: MMLU's academic taxonomy was ambitious for its time. **Difficulty and headroom**: making sure frontier models still have room to run. And a **robust sourcing methodology** for how you actually build tasks.

Their own QC was rigorous: every single task relied on a suite of both agentic and expert-in-the-loop quality-control methods to catch non-determinism and false positives and false negatives in the verifiers. Multiple experts — including himself and senior Snorkel researchers, alongside their expert network of working software engineers — painstakingly reviewed every task to make the benchmark reliable.

**Leaderboard result**, updated the week before the talk and triple-checked: on the tasteful-solve metric there is currently a **three-way tie for first** between Fable, Opus, and a third model (heard as "Soul" — to verify), which he finds remarkable when you consider the Pareto efficiency curve. It's live at senior-swe-bench.snorkel.ai.

**Collaborators**: led by Snorkel co-founder Henry (Ehrenberg), with the original SWE-Bench team, Karthik's group (name to verify), and Snorkel chief scientist Fred Sala plus colleagues at Wisconsin.

#### Three axes for the future (~00:58–00:59)

1. **Environment complexity and realism** — real codebase environments, scientific computing environments, legal workflows, the actual systems people work in daily, not simple prompts and responses.
2. **The autonomy horizon** — how far models can go working autonomously, and how humans get pulled in across those settings.
3. **Output complexity** — beyond verifiable fields into nuanced ones like legal and healthcare, where the definition of good isn't a simple closed-form solution the way it is in mathematics.

His closing call to action: Snorkel is funding a number of these benchmarks through their open benchmarks grants, and welcomes collaboration at benchmarks.snorkel.ai.

### Quotes

> "Our ability to measure AI has really been outpaced by our ability to develop it." (~00:48:42)

The problem statement for the whole talk.

> "What I'll call bench slop — the idea that you can really quickly vibe code a benchmark and get a fancy Twitter post." (~00:49:50)

The sharpest available name for the current benchmark inflation.

> "Not only are we measuring correctness, but we're measuring notions of codebase alignment, practice alignment, bloat relative to an Oracle PR." (~00:55:32)

What a tasteful solve actually contains — taste turned into something measurable.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Senior SWE-Bench | Snorkel 與 Princeton 原始 SWE-Bench 團隊合作,評估 senior 級軟體工程能力;引入 tasteful solve 指標 | Snorkel × the original Princeton SWE-Bench team; evaluates senior-level SWE capability with a "tasteful solve" metric | senior-swe-bench.snorkel.ai(逐字稿誤作 "seniorbench.snorkele.ai") |
| Snorkel Open Benchmarks Grant | 資助社群建 agentic AI benchmark 的計畫 | Grant program funding community-built agentic AI benchmarks | benchmarks.snorkel.ai(逐字稿誤作 "benchmarks.n.ai") |
| Agents' Last Exam | Dawn Song 團隊的長 horizon 真實任務 benchmark;Snorkel 為資料與研究夥伴,協助品質控管 | Dawn Song's long-horizon real-world benchmark; Snorkel contributed quality-control mechanisms as data and research partner | 見 8/1 Plenary Dawn Song 場 |
| OSWorld 2.0 | Snorkel 參與的 benchmark 之一 | One of the benchmarks Snorkel partnered on | |
| Terminal-Bench | 押注「agent 的未來在文字介面」;現已出現在幾乎每張前沿 model card 上 | Bet that agents' future happens at the text interface; now on essentially every frontier model card | 最近幾版由 Snorkel 參與 |
| GPQA | 以任務品質著稱;附錄記載報酬/激勵機制如何驅動高品質貢獻 | Cited for task quality; its appendix documents how pay incentives produced high-quality contributions | |
| MMLU | 以明確學術分類法達成分布控制,在當時極具企圖心 | Distributional control via a concrete academic taxonomy, ambitious for its time | |
| HumanEval | 幾年前推出即達 95%,用來對照今日最難程式 benchmark 的 3% | Launched years ago at 95%, contrasted with today's hardest programming benchmarks at 3% | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Sweetbench / senior sweeb bench | SWE-Bench / Senior SWE-Bench |
| senior bench | Senior SWE-Bench |
| seniorbench.snorkele.ai | senior-swe-bench.snorkel.ai |
| benchmarks.n.ai | benchmarks.snorkel.ai |
| Fred Salah | Fred Sala |
| Chris Ray's group | Chris Ré's group |
| Don Don's agents last exam | Dawn Song's Agents' Last Exam |
| human eval | HumanEval |
| continue learning bench | Continual Learning Bench(名稱待確認) |
| Carics Group | 待確認,可能為 Karthik (Narasimhan)'s group |
| Soul(第三名模型) | 待確認 / to verify |

## 待確認 / To Verify

- 與 Berkeley Sky Lab 合作的「continue learning bench」正式名稱與連結。/ The official name of the Berkeley Sky Lab continual-learning benchmark he cited.
- 「Harding program benchmarks are at 3%」——這裡的 benchmark 名稱不確定,可能是形容詞("the hardest programming benchmarks")而非專有名詞,需看投影片。/ Whether "Harding program benchmarks" is a benchmark name or simply "the hardest programming benchmarks".
- Senior SWE-Bench 排行榜上與 Fable、Opus 並列第一的第三個模型(字幕聽作 "Soul")。/ The third model tied for first alongside Fable and Opus (heard as "Soul").
- 協作研究群 "Carics Group" 的正確名稱;原始 SWE-Bench 團隊出自 Princeton,推測為 Karthik Narasimhan 的研究群,但未經證實。/ The correct name of the collaborating group heard as "Carics Group"; likely Karthik Narasimhan's Princeton group, unconfirmed.
- Senior SWE-Bench 的題數與公開/私有切分,演講中未念出(公開資料為 100 題、50 公開 50 私有,但應以官方頁面為準)。/ Task count and public/private split were not stated on stage.
