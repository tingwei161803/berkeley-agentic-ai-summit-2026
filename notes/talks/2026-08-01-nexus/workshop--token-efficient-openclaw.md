---
title: "Building a Token-Efficient OpenClaw Agentic System"
title_zh: "打造 token 高效的 OpenClaw Agentic 系統"
speaker: "Mahdi Ghodsi、Satya Devineni、Eda Zhou"
affiliation: "AI Solutions Architect, AMD;Product Application Engineer, AMD;Software Development Engineer, AMD"
type: workshop
stage: Nexus
date: 2026-08-01
session: "Session 1: AI for Science"
video: "https://www.youtube.com/watch?v=LB7IkZhEYic&t=5163s"
video_range: "01:26:03–02:20:25"
transcript: "tmp/[English (auto-generated)] Nexus Stage - August 1st - Morning Session [DownSub.com].srt"
status: draft
tags: [openclaw, model-routing, local-llm, kv-cache, amd]
---

# 打造 token 高效的 OpenClaw Agentic 系統(Building a Token-Efficient OpenClaw Agentic System)

**一句話總結**:agentic 工作把計價單位從「每秒 token 數」推向「每個完成任務的成本」,而降低那個成本的兩把刀是**分層快取**(別重算上一輪算過的東西)與**模型路由**(別把找檔案的請求送去前沿模型)。
**One-line summary**: Agentic work moves the unit of account from tokens per second to cost per finished task, and the two levers that lower it are tiered caching — stop recomputing what the last turn already computed — and model routing — stop sending "find me a file" to a frontier model.

## 中文筆記

> 形式:前 10 分鐘為 AMD 的簡報(原講者為 AMD 副總,因故未到,由 Mahdi Ghodsi 代講),其後約 40 分鐘為現場動手工作坊,由 Mahdi Ghodsi 與 Satya Devineni 帶領,現場另有 TA 協助。以下依主題整理。

### TL;DR

- **計價單位變了**:chat 是有界任務(prompt → response → 結束);agentic 是無界的(規劃、呼叫工具、看結果、不滿意再來一次),同一份工作可能幾秒也可能幾小時。因此該報的指標是**每個成功完成任務的成本與時間**,不是 tokens/sec。
- **這打壞三件事**:預算(同一個服務,兩個使用者的成本可能差 10–100 倍——他們自己年初編的全年算力預算幾週就燒光了)、最佳化目標(從 flops 變成 memory-bound 的全系統問題)、以及計分卡本身。
- **一切都回到快取**:每一輪都在重算上一輪算過的東西。三條戰線同時做——模型層(Kimi K3 的 93 層中有 69 層是 KDA 線性注意力,固定大小的遞迴狀態而非不斷長大的 KV cache)、GPU serving 層(HBM → CPU DRAM → SSD → pooled memory 的分層快取,P99 TTFT 從 17.3 秒降到 5.4 秒)、CPU 層(tokenization 快取:1.7 秒 → 0.09 毫秒)。
- **反直覺的一課**:快取命中率從 88.5% **降到** 87.5%,但 TTFT 快了 3 倍——因為命中率不是使用者體驗,完成任務的時間才是。
- **工作坊主軸**:用 OpenClaw 做 **mixture of models**(而非 mixture of experts),依成本、品質、隱私三個理由把請求路由到本地或雲端模型;四種難度遞增的路由方式一路做到 Lemonade Router 的語意路由。

### 主題與內容

#### 主題一:從 tokens 到 outcomes——為什麼計價單位變了(約 01:27–01:31)

聽起來理所當然但後果昂貴的一件事:**AI chat 是有界任務**——使用者送出 prompt、拿到回應、人讀完,結束。**Agentic AI 不是**:同一個查詢進去之後,agent 會規劃、也許呼叫工具、看結果、可能不滿意再叫一次,甚至展開一整張 agent 的圖。**同樣一份工作,可能是幾秒,也可能是幾小時。**

這對規劃容量或編列團隊預算的人來說是根本性的改變:過去是按「席次」把使用者掛到模型或服務上;現在**一個使用者可能幾秒就結束,另一個可能跑幾小時**,兩者所需算力是完全不同的數量級。

他點名這會打壞三件事:

1. **預算**。同一個服務,兩個人的成本可能差 10 倍或 100 倍。他直說這大概就是他們副總把這頁放進來的原因——他們在年初編了整年的團隊算力預算,**幾週就燒完了**,而且整個產業都在發生同一件事。
2. **最佳化目標**。過去大家執著於 flops 與 tokens/sec、GPU 夠不夠快;現在 multi-turn agent run 讓 context 長得飛快,問題變成**整個系統的、而且大量是 memory-bound 的**。
3. **計分卡**。tokens/sec 已經說明不了什麼,因為重點是**完成的任務**,不是單次回應。

#### 主題二:三條戰線上的同一個原則——快取(約 01:31–01:38)

原則一句話:**每一輪都在重複上一輪已經做過的工作**。跑到第 12 輪時,你其實還在重算前 11 輪算過的東西,只為了處理第 12 輪多出來的一點內容。答案很明顯——**別重算,把它留著**。這件事做了好幾年,但 agentic 讓它的重要性完全不同。他們在**模型、GPU stack、CPU** 三條線上並行處理,以下例子來自與 Moonshot AI 就 **Kimi K3** 的 day-zero 支援合作。

- **模型層**:KV cache 每來一次回應就長大一次,大模型可以長到數百 GB,不可能全放進 HBM(GPU 最快的記憶體)。Kimi K3 的做法是:**93 層裡有 69 層用 KDA(Kimi Delta Attention)**——帶遞迴層的線性注意力,那些層計算的 token 量是固定的。在 AMD **MI355** 上(一個節點八張 GPU、每張 288 GB)實測**只用了約 15.5 GB**。
- **GPU serving 層**:如果每個請求的 cache 都要放在 HBM,資料中心的經濟性不成立。他們對新模型重做了**分層快取**:**HBM → CPU 的 DRAM → SSD → pooled memory**。關鍵洞見是 agentic run 有**大量閒置時間**(agent 送出任務後在等工具或 CPU 的結果),所以要讓 eviction 發生時 GPU 仍然忙著;分層之後,模型準備好跑下一步時 prefix 已經就緒。成績:**P99 的 time-to-first-token 從 17.3 秒降到 5.4 秒,約 3.2 倍**。
- **CPU 層**:agentic 讓 CPU 變得重要得多——大量計算發生在那裡,工具呼叫與執行都可以更有效率。他舉的例子是 **tokenization 也可以快取**:只算新的部分就得到**固定 0.09 毫秒**,而整份重算是 **1.7 秒**。

**最反直覺的一頁**:很多人報快取命中率,但他們的例子裡命中率**從 88.5% 掉到 87.5%**。乍看變糟了,但前面說的 TTFT 快了三倍——因為**如果你還是得重算第一個 token,那 88.5% 並不代表什麼**。結論:**該報的是每次成功執行的成本與時間,不是 tokens/sec、也不是命中率**。

#### 主題三:mixture of models 與它的三個理由(約 01:41–01:47)

工作坊的主軸是把「routing」從模型內部搬到模型之間。他先鋪背景:多數開發者聽到 routing 想到的是 MoE(mixture of experts)——1991 年 Geoffrey Hinton 團隊那篇早期論文,2017 年在大得多的模型上重新探索並帶出 sparse gating 等技術,至今仍是主流方向。**但同一個 routing 想法可以把端點從「expert」換成「model」**,這就是這天要做的 **mixture of models**。

三個理由:

1. **成本**——「不是每個 token 都值得那個最好的前沿模型」。找一個檔案、跑一個簡單指令,沒必要送去 Fable 5。
2. **品質**——需要時再升級(escalate),也可以讓專門模型處理專門任務。
3. **隱私與安全**——他個人電腦上有大量私人檔案,「我不想我的社會安全號碼出現在別人的訓練資料裡」,那就留在本機。

他也點名這不是 AMD 的原創,學界早有探索:**FrugalGPT**(2023)用一個模型判斷小模型的回應,滿意就留、不滿意才升級到雲端模型,宣稱省下 98% 總成本且結果與當時的 GPT-4 相當;**RouteLLM**(Berkeley)則改成**先用 router 決定該用哪個模型**,同樣顯示 2 倍以上的成本節省;再往下就是**語意路由**——把進來的請求 embed 成向量,依你定義的規則用餘弦相似度分類該送去哪個模型。

**硬體與環境**:本地模型跑在 **AMD Ryzen AI「Halo」box**(Ryzen AI Max+ 395,市面可買的小型機),CPU/iGPU/NPU 共用 **128 GB 統一記憶體**,低精度下可跑到約 2,000 億參數等級;需要升級時走 **Fireworks AI**,其後端是 AMD **MI355** GPU。本地推論用 AMD 自研的 **Lemonade**(桌面 app 下載模型即可跑,語意路由內建),Lemonade 的一位創辦人 Krishna 也在現場。

**OpenClaw 的角色**:當天的 agentic runtime。他形容它「今年稍早爆紅,現在大概是最熱門的開源軟體」,創辦人也在會場。工作坊只用到它的 agent 建立機制:**每個 agent 有自己的 workspace**,裡面是一批 `.md` 設定檔(例如 `SOUL.md`、`AGENTS.md`)與 `openclaw.json`(模型設定與權限)。主辦方預先建好三個 agent:`local-brain`(接本地模型)、`cloud-brain`(接雲端 Kimi)、`smart-router`。

#### 主題四:四層路由,由淺入深(約 01:47–02:06)

1. **手動 `/model` 切換**。任何用過 coding agent 的人都會,最簡單。
2. **一個模型一個專屬 agent**。現場有人問「為什麼不用一個大 agent 就好?」答案是**規則、權限與 context 都能按 agent 分開設定**——例如規定「雲端 agent 永遠不准碰我的個人檔案」。示範:把 `cloud-brain` 的本地檔案權限關掉並重啟 gateway 後,叫它讀一份財務 CSV,它回「我沒有本地檔案系統的存取權」;切到 `local-brain` 同樣的指令則正常讀出。
3. **自動升級路由**。改 `smart-router` 這個 agent 的 `SOUL.md`,規定**每則回應都必須以 `CLOUD` 或 `LOCAL` 其中一行開頭**,並給出分類規則(要寫程式 → cloud;要讀檔案 → local)。示範兩則:「什麼是四年 vesting、一年 cliff?」→ 分類 LOCAL,本地模型回答;「寫一個計算貸款利息的 Python function」→ 分類 CLOUD,轉去 Fireworks 模型。實作上升級是**開一個帶雲端模型的 sub-agent**,把 context 傳過去、等它回來再取結果。
4. **Lemonade Router 的語意路由**(Satya Devineni 主講)。架構是:prompt → OpenClaw → 本機的 Lemonade Router → 依判斷分流:敏感問題走小型本地模型、複雜問題走雲端 Kimi K2.6、既複雜又敏感則走較大的本地模型。

#### 主題五:語意路由實作——三個 agent、三種規則(約 02:06–02:19)

情境設定是「你在管一家新創」:員工到職離職、福利、財務、法務。每個 agent 用 OpenClaw 的 **skills**(`skills/` 資料夾下的 `SKILL.md`)界定資料來源、輸出期待、可以做與不可以做的事。

- **HR admin agent —— LLM-as-router**。`employees.csv` 裡有 SSN、email、電話等 PII。先用雲端模型做到職,資料就外流了;改用 `user.hr-admin-router` 之後,routing prompt 只有一句話:「看到任何 PII 就送本地模型,其餘送 Fireworks」。同樣的到職請求就由本地模型完成,**零資料離開機器**。Lemonade dashboard(`localhost:1305`)可以看到本地模型被載入,以及 TTFT、TPS 等指標。
- **Benefits agent —— 關鍵字與規則路由**。對 `benefits-handbook.md` 做 RAG。規則是:出現 401k、vesting 等關鍵字**且** prompt 短於 400 字元 → 本地;涉及比較、分析、benchmarking,或 prompt 長於 800 字元 → 雲端 Kimi K2.6。兩則示範分別命中兩條規則,而使用者完全不需要自己切模型。
- **Finance agent —— 語意相似度 + LLM 分類器**。對 CSV 做資料分析。用 embedding 模型計算輸入 prompt 與預先定義概念之間的**餘弦相似度**(0–1 分):「what is our current burn rate」對應到 "simple metric lookup",門檻 > 0.6 → 本地;多來源分析則對應 "deep modeling",此處**兩條規則任一觸發就升級**——LLM 分類器判定為 complex 且分數 > 0.5,或語意相似度 > 0.72 → 雲端。

**挑戰與收尾**:最後留約 10 分鐘讓與會者解一道題,規則是**用最少 token 完成**(本地、雲端、Lemonade Router 隨你選),排行榜計分、AMD 周邊當獎品。線上參加者可透過表單申請 AMD Developer Program 的免費算力額度,之後以 email 收到專屬連結跟做同一份工作坊。

### 金句

> "So the winner is whoever finishes the most tasks per dollar."(約 01:38:29)

一句話定義 agentic 時代的計分卡。

> "…not every token deserves that best frontier model out there. If for example you're looking for a file or looking for simple command, you don't need to send that to your Fable 5."(約 01:44:37)

mixture of models 的全部理由,濃縮成一句。

## English Notes

> Format: a 10-minute AMD deck (originally prepared by an AMD VP who couldn't attend, delivered by Mahdi Ghodsi), followed by roughly 40 minutes of hands-on workshop led by Mahdi Ghodsi and Satya Devineni with TAs on the floor. Organized by theme below.

### TL;DR

- **The unit of account changed.** Chat is a bounded task: prompt in, response out, done. Agentic work is unbounded — plan, call a tool, inspect the result, dislike it, call again — so the same job might take seconds or hours. The metric to report is **cost and time per successful run**, not tokens per second.
- **This breaks three things**: budgeting (two users of the same service can differ 10–100× in cost — their own team burned a full year's compute budget in a few weeks), the optimization target (from flops to a memory-bound whole-system problem), and the scorecard itself.
- **It all comes back to caching**: every turn repeats work the last turn already did. Three fronts at once — model level (69 of Kimi K3's 93 layers use KDA linear attention with a fixed-size recurrent state instead of a growing KV cache), GPU serving stack (tiered HBM → CPU DRAM → SSD → pooled memory, taking P99 TTFT from 17.3s to 5.4s), and CPU (cached tokenization: 1.7s → 0.09ms).
- **The counterintuitive lesson**: cache hit rate went **down** from 88.5% to 87.5% while TTFT improved 3× — because hit rate isn't the user experience, finished tasks are.
- **The workshop's through-line**: use OpenClaw to build a **mixture of models** (not experts), routing requests to local or cloud models for reasons of cost, quality, and privacy — through four escalating routing techniques, ending in Lemonade Router's semantic routing.

### Themes

#### Theme 1: From tokens to outcomes — why the unit of account changed (~01:27–01:31)

Something that sounds obvious and turns out to be expensive: **AI chat is a bounded task** — the user sends a prompt, gets a response, reads it, done. **Agentic AI isn't.** The same query goes in, but the agent plans, maybe calls a tool, looks at the result, maybe doesn't like it and calls again, maybe spins up a whole graph of agents. **The same work could be seconds or could be hours.**

For anyone planning capacity or a team budget, this is a structural change. Previously you bought seats and assigned users to models or services. Now **one user might take seconds and another might take hours**, and the compute those two need differs by orders of magnitude.

Three things break:

1. **Budgeting.** Two people on the same service can differ 10× or 100× in cost. He suspected that's why his VP put the slide in: they budgeted a full year of compute for the team at the start of the year and **blew through it in a few weeks** — and it's happening across the industry.
2. **The optimization target.** Everyone used to obsess over flops, tokens per second, and whether the GPU was fast enough. Now multi-turn agent runs grow context so fast that it's a **whole-system, largely memory-bound** problem.
3. **The scorecard.** Tokens per second doesn't tell you much when what matters is the **finished task**, not one response.

#### Theme 2: One principle across three fronts — caching (~01:31–01:38)

The principle in a sentence: **every turn repeats work from the last turn.** By turn 12 you're still recomputing all 11 previous turns just to handle what's new in turn 12. The obvious answer is not to redo it. People have been doing this for years, but agentic work changes its weight. They attack it on three fronts — **models, the GPU stack, and the CPU** — with examples from their day-zero **Kimi K3** collaboration with Moonshot AI.

- **Model level**: the KV cache grows with every response, reaching hundreds of gigabytes for large models — impossible to keep in HBM, the GPU's fastest memory. Kimi K3's approach: **69 of its 93 layers use KDA (Kimi Delta Attention)**, linear attention with recurrent layers, so those layers compute over a fixed token budget. On AMD **MI355** (one node, eight GPUs, 288 GB each) their experiment used **only ~15.5 GB**.
- **GPU serving stack**: keeping every request's cache in HBM makes the data center economics untenable. They redesigned **tiered caching** around the new model: **HBM → CPU DRAM → SSD → pooled memory**. The key observation is that agentic runs have **a lot of idle time** — the agent fires a task and waits on a tool call or CPU work — so when eviction happens you want the GPU still busy. With tiering, the prefix is ready when the model is ready to run. Result: **P99 time-to-first-token from 17.3s to 5.4s, roughly 3.2×**.
- **CPU side**: agentic workloads make CPUs far more relevant — a lot of compute happens there, and tool calls and execution can be made much more efficient. His example: **tokenization can be cached too**, giving a flat **0.09 ms** when you only compute what's new versus **1.7 s** to recompute everything.

**The counterintuitive slide**: plenty of people report cache hit rate, and in their example it went **down**, from 88.5% to 87.5%. At first glance that's worse — but TTFT improved 3×, because **88.5% doesn't mean much if you still have to compute the first token.** Conclusion: **report cost and time per successful run, not tokens per second and not hit rate.**

#### Theme 3: Mixture of models, and the three reasons for it (~01:41–01:47)

The workshop's through-line is moving routing from inside the model to between models. He set up the background: most developers hear "routing" and think MoE — the notable early paper from Geoffrey Hinton's team in 1991, revisited in 2017 on a far larger model where sparse gating and better expert-selection gating emerged, still state of the art today. **But the same routing idea works with models, rather than experts, as the endpoints** — the **mixture of models** they'd be building.

Three reasons:

1. **Cost** — "not every token deserves that best frontier model." Finding a file or running a simple command doesn't need to go to Fable 5.
2. **Quality** — escalate when it's needed, and use specialized models for tasks they handle well.
3. **Privacy and security** — he has plenty of personal files on his machine and doesn't want his social security number showing up in someone's training data, so it stays local.

He was explicit that none of this is AMD's idea. **FrugalGPT** (2023) used a judge model on the small model's response, keeping it if satisfactory and escalating to a cloud model otherwise, claiming 98% total cost savings with results comparable to GPT-4 at the time. **RouteLLM** (from Berkeley) moved the decision up front — a router picks the model before inference — showing over 2× cost savings. Then **semantic routing**: embed the incoming request and classify the resulting vector against your rules using cosine similarity.

**Hardware and environment**: the local model runs on an **AMD Ryzen AI "Halo" box** (Ryzen AI Max+ 395, purchasable as a small-form-factor machine), with CPU, iGPU and NPU sharing **128 GB of unified memory** — enough to serve models up to roughly 200B parameters at lower precision. Escalation goes to **Fireworks AI**, served on AMD **MI355** GPUs. Local inference uses AMD's own **Lemonade** (desktop app, download a model and go, semantic routing built in); one of Lemonade's founders, Krishna, was in the room.

**OpenClaw's role**: the agentic runtime for the day. He described it as having gone hugely popular earlier in the year and being probably the most popular open-source software right now, with its founder also at the conference. The workshop uses only its agent-creation mechanics: **each agent gets its own workspace** containing `.md` config files (`SOUL.md`, `AGENTS.md`) and `openclaw.json` for models and permissions. Three agents were pre-built: `local-brain` (local model), `cloud-brain` (cloud Kimi), and `smart-router`.

#### Theme 4: Four levels of routing (~01:47–02:06)

1. **Manual `/model` switching.** Anyone who's used a coding agent knows it; simplest possible.
2. **A dedicated agent per model.** An attendee asked why not just use one big agent. The answer: **rules, permissions, and context can be set per agent** — e.g. "the cloud agent must never touch my personal files." Demo: after disabling local-file access for `cloud-brain` and restarting the gateway, asking it to read a financial CSV returned "I don't have access to the local file system"; switching to `local-brain` and issuing the same command printed the report fine.
3. **Automatic escalation routing.** Edit the `smart-router` agent's `SOUL.md` so **every response must begin with exactly one of two lines — `CLOUD` or `LOCAL`** — plus classification rules (write code → cloud; read a file → local). Two demos: "what does a four-year vesting schedule with a one-year cliff mean?" classified LOCAL and answered locally; "write a Python function to calculate loan interest payments" classified CLOUD and routed to the Fireworks model. Under the hood, escalation **spawns a sub-agent** carrying the cloud model, passes it the context, and waits for it to return.
4. **Lemonade Router's semantic routing** (Satya Devineni's section). Architecture: prompt → OpenClaw → Lemonade Router running locally → sensitive questions to a small local model, complex questions to cloud Kimi K2.6, complex-and-sensitive to a larger local model.

#### Theme 5: Semantic routing in practice — three agents, three rule types (~02:06–02:19)

The scenario: you're running a startup — onboarding and offboarding, benefits, finance, legal. Each agent is scoped by OpenClaw **skills** (a `SKILL.md` in the `skills/` folder) that point at data sources, state output expectations, and specify what the agent is and isn't authorized to do.

- **HR admin agent — LLM-as-router.** `employees.csv` holds PII: SSNs, emails, phone numbers. Onboarding an employee through the cloud model leaks all of it. Switching to `user.hr-admin-router` applies a one-line routing prompt — "if you see any personally identifiable information send it to a local model; for anything else, send it to Fireworks" — and the same onboarding request completes locally with **zero data leaving the machine**. The Lemonade dashboard at `localhost:1305` shows the local model loading, plus TTFT, TPS, and other metrics.
- **Benefits agent — keyword and rule routing.** RAG over `benefits-handbook.md`. Rules: keywords like 401k or vesting **and** a prompt under 400 characters → local; comparison, analysis, or benchmarking questions, or prompts over 800 characters → cloud Kimi K2.6. Two demos hit the two rules, with the user never switching models.
- **Finance agent — semantic similarity plus an LLM classifier.** Data analysis over CSVs. An embedding model computes **cosine similarity** (scored 0–1) between the input prompt and predefined concepts: "what is our current burn rate" maps to *simple metric lookup* with a threshold above 0.6 → local. Multi-source analysis maps to *deep modeling*, where **either of two rules triggers escalation** — an LLM classifier labeling the question complex above 0.5, or a semantic score above 0.72 → cloud.

**Challenge and wrap-up**: roughly 10 minutes at the end for attendees to solve a task using **the fewest tokens possible** — local, cloud, or Lemonade Router, their choice — scored on a leaderboard with AMD swag as prizes. Virtual attendees could request free compute credits through the AMD Developer Program form and receive a personal link by email to follow the same workshop later.

### Quotes

> "So the winner is whoever finishes the most tasks per dollar." (~01:38:29)

The agentic-era scorecard in one line.

> "…not every token deserves that best frontier model out there. If for example you're looking for a file or looking for simple command, you don't need to send that to your Fable 5." (~01:44:37)

The entire case for mixture of models, compressed.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Kimi K3(Moonshot AI) | 93 層中 69 層採 KDA 線性注意力,遞迴狀態固定大小而非成長的 KV cache | 69 of 93 layers use KDA linear attention — a fixed-size recurrent state instead of a growing KV cache | 2.8T 參數 MoE、1M context;AMD 提供 day-zero 支援 / 2.8T-param MoE with 1M context; AMD provided day-zero support |
| KDA(Kimi Delta Attention) | 帶遞迴層的線性注意力,固定 token 計算量 | Linear attention with recurrent layers and a fixed token compute budget | MI355 上實測記憶體約 15.5 GB / measured ~15.5 GB on MI355 |
| 分層快取 / tiered caching | HBM → CPU DRAM → SSD → pooled memory,利用 agentic run 的閒置時間 | HBM → CPU DRAM → SSD → pooled memory, exploiting agentic runs' idle time | P99 TTFT 17.3s → 5.4s(≈3.2×)/ P99 TTFT 17.3s → 5.4s (~3.2×) |
| Lemonade / Lemonade Router | AMD 自研本地 LLM server,內建 rule / classifier / 語意相似度 / LLM-as-router 四種路由策略 | AMD's local LLM server with rule, classifier, semantic-similarity, and LLM-as-router policies built in | dashboard 在 `localhost:1305`;創辦人之一 Krishna 在場 / dashboard at `localhost:1305`; co-founder Krishna present |
| OpenClaw | 工作坊使用的 agentic runtime;每個 agent 有 workspace、`SOUL.md`/`AGENTS.md` 與 `openclaw.json` | The workshop's agentic runtime; each agent has a workspace with `SOUL.md`/`AGENTS.md` and `openclaw.json` | 講者稱其為「目前最熱門的開源軟體」/ described as "the most popular open source software out there right now" |
| FrugalGPT(2023) | 用 judge 判斷小模型回應,不滿意才升級雲端;宣稱省 98% 成本 | Judge the small model's answer and escalate only if unsatisfied; claimed 98% cost savings | 講者引為 mixture-of-models 的學界先例 / cited as academic prior art |
| RouteLLM(Berkeley) | 事前用 router 決定該用哪個模型,顯示 2 倍以上成本節省 | A router picks the model up front; over 2× cost savings | 同上 / same |
| AMD Ryzen AI Max+ 395(“Halo” box) | CPU + iGPU + NPU 共用 128 GB 統一記憶體,低精度下可跑約 200B 參數模型 | CPU, iGPU, and NPU sharing 128 GB unified memory; runs models up to ~200B params at lower precision | 工作坊的本地模型主機 / the workshop's local model host |
| AMD Instinct MI355 | 一節點八張、每張 288 GB;Fireworks AI 用它服務雲端模型 | Eight per node at 288 GB each; Fireworks AI serves the cloud model on them | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Mati Goodsy / Maddie / Mari | Mahdi Ghodsi |
| Satia / Satio | Satya Devineni |
| Kim K3 / Kimmy K3 / Kimik2.6 | Kimi K3 / Kimi K2.6 |
| KDA、Kimmy delta attention | KDA(Kimi Delta Attention) |
| HPM | HBM(High Bandwidth Memory) |
| AMDMI 355 / MI 355 | AMD Instinct MI355 |
| open claw / opencloud / open cloud / openclaw(混用) | OpenClaw |
| opencloud.json / open cloud JSON | `openclaw.json` |
| solar MD / soul MD / MD 檔 | `SOUL.md` |
| Lemonate / Lemonade(混用) | Lemonade |
| Jeff Henon | Geoffrey Hinton |
| frugal GPT / GPD4 | FrugalGPT / GPT-4 |
| route LLM | RouteLLM |
| Quen 3.635B / quen 3.59B | Qwen 3(版本待確認 / version to verify) |
| coine similarity | cosine similarity |
| Ryzen AI Halobox / AMX 395 | Ryzen AI Max+ 395 |
| rack / rag(混用) | RAG |

## 待確認 / To Verify

- **本地模型的確切版本**:字幕在同一段裡出現 "Quen 3.635B"、"quen 3.59B"、"Quen 3.635B" 等多種寫法,推測是 Qwen 3 系列的兩個尺寸(較小的路由/分類模型與較大的本地模型),但參數規模無法確認。/ The local model versions are ambiguous — the transcript gives several spellings suggesting two Qwen 3 sizes (a smaller router/classifier and a larger local model), but the parameter counts can't be confirmed.
- **原講稿作者**:字幕稱 AMD 副總為 "Ramen" / "Ram",姓名未確認。/ The AMD VP who prepared the deck is transcribed as "Ramen" / "Ram"; name unconfirmed.
- **第三位議程講者 Eda Zhou** 在逐字稿中未被點名;講者提到一位穿龍蝦裝的同事擔任 TA,是否為同一人待確認。/ Eda Zhou, listed on the agenda, is never named in the transcript; a colleague in a lobster costume is mentioned as a TA, but the identification is unconfirmed.
- **1991 年 MoE 論文**:講者說「Jeff Henon 和他的團隊」,應指 Jacobs、Jordan、Nowlan、Hinton 的 mixture-of-experts 工作;2017 年那篇「超過一兆參數」的說法與公開紀錄不符(2017 sparsely-gated MoE 約 137B),需查證他實際指的是哪一篇。/ The 1991 MoE reference is presumably Jacobs, Jordan, Nowlan & Hinton; his "over one trillion parameters" claim for the 2017 revisit doesn't match the public record (the 2017 sparsely-gated MoE was ~137B) — which paper he meant needs checking.
- **FrugalGPT 省下 98% 成本**的數字為講者轉述,未核對原論文。/ The 98% cost-saving figure for FrugalGPT is as stated on stage, not checked against the paper.
- **工作坊環境的公開版本**:線上索取算力的表單與後續連結未出現在逐字稿可查證的形式。/ The form and follow-up link for virtual attendees' compute credits aren't recoverable from the transcript.
