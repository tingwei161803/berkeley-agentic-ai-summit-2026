---
title: "Build AI Agents That Survive Failure"
title_zh: "打造能從失敗中活下來的 AI Agent"
speaker: "Nikolay Advolodkin"
affiliation: "Senior Staff Developer Advocate, Temporal"
type: workshop
stage: Compass
date: 2026-08-01
session: "Session 2: Frameworks & Dev Platforms"
video: "https://www.youtube.com/watch?v=AO0RXP-fVZQ&t=3584s"
video_range: "00:59:44–02:00:02"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [temporal, durable-execution, workshop, multi-agent, hands-on]
---

# 打造能從失敗中活下來的 AI Agent(Build AI Agents That Survive Failure)

**一句話總結**:把 agent 的商業流程放進 workflow、把所有會失敗的非確定性動作(LLM 呼叫、API、DB 查詢)包成 activity,Temporal 就會替你記住歷史、無限重試、並在故障排除後**像什麼都沒發生過一樣**接著跑下去——現場直接拔掉 weather API 給大家看。
**One-line summary**: Put the agent's business flow in a workflow, wrap every non-deterministic thing that can fail — LLM calls, APIs, database queries — in an activity, and Temporal keeps the history, retries indefinitely, and resumes **as though the failure never happened**. Demonstrated live by pulling the plug on the weather API.

> 主持人於 **00:59:44** 交接;講者的暖場活動自 **01:04:39** 開始,技術內容自 **01:07** 起。工作坊採動手實作形式,以下依主題整理。
> The MC handed over at **00:59:44**; the speaker's icebreaker starts at **01:04:39** and the technical content at **01:07**. This was a hands-on session; notes are organized by topic.

## 中文筆記

### 開場:先讓整個房間站起來(約 01:04:39–01:06)

在連聽了好幾場 AI 演講之後,Advolodkin 一上台先請全場站起來,找兩個人擊掌、看著對方的眼睛說「你超棒的」,然後拍了一段全場歡呼的自拍影片(第一次他嫌太冷淡,要大家再來一次、聲量五倍)。自我介紹:Temporal 的 developer advocate、狗爸爸、直排輪玩家,狗叫 Mia。

他說明工作坊的哲學:**動手做才會記得住,被動聽留不下東西**。原訂四個主題——agentic AI 系統的基礎(並實作一個)、用 agentic framework(OpenAI Agents SDK)蓋、human in the loop、以及 orchestrate micro-agents——他一開始就坦白「大概講不完,但沒關係,結束後我會給你們 GitHub repo」。

### 主題一:什麼是 agentic loop(約 01:07)

LLM 能對我們給它的 context 進行推理,**但它缺的是「資訊不夠時自己去採取行動」的能力**。agent loop 提供的就是這個:讓 LLM 能夠在自身之外行動。

流程是:給定 instruction 與目標(他的例子:「你是旅遊助理,幫我找一班去邁阿密的班機,訂票付款前先跟我確認」)→ 把 context 交給 decision maker(也就是 LLM)→ **LLM 判斷:我的資訊夠不夠?**夠就給最終答案,不夠就呼叫工具。工具由 harness 定義、有時由你定義;**你只負責告訴 LLM 這些工具存在,由 LLM 決定什麼時候用**。拿到工具輸出後再判斷一次,不夠就繼續這個蒐集資訊的迴圈,直到能安心給出答案。

他也現場做了一輪投票,問大家對 Temporal 的熟悉程度——結果大多數人**沒聽過,或聽過但沒用過**。他笑說「那這場對很多人會偏進階」,但承諾會盡量帶。

### 主題二:Temporal 的心智模型(約 01:10:47–01:13)

一句話:**Temporal 讓你「寫程式時假裝失敗不存在」。**

- 你專注在 agent / 分散式系統的**商業邏輯**(他強調:**agent 就是分散式系統**),把它放進一個 **workflow**——也就是你想執行的一連串步驟。
- 然後把**非確定性的步驟**——API 呼叫、LLM 呼叫、資料庫查詢——抽出來,放進所謂的 **activity**。
- 用 SDK 包住這些 activity 之後(Python、TypeScript、Java、Go、Ruby 等主流語言都支援),Temporal 會建立一份**到目前為止所有已執行動作的 history**。
- 一旦發生任何失敗,**它就停在 history 的那個點等待**,等失敗被解決——可能是幾秒、幾分鐘,**也可以是好幾年**。解決之後,它會**像失敗從未發生過一樣**繼續執行後面的操作。
- 而且**這段等待不消耗你的資源**,因為狀態全都記在 history 裡。他提到 Temporal 有 **six nines 的可靠度**。

那什麼會失敗?幾乎所有東西:LLM 呼叫因網路問題失敗(他說**當天早上才被 OpenAI 回了一個 429 rate limit**)、API 呼叫失敗、rate limit、服務掛掉、AWS 掛掉。**把這些包進 activity,Temporal 就能在故障解除後接手。**

### 主題三:動手做——第一個 workflow(約 01:13–01:25)

環境是一個虛擬 lab(免安裝、Docker 容器,開機約 90 秒),分頁包含 worker 終端機、starter 終端機、**Temporal UI**、一個可以**模擬網路故障的 network control panel**,以及程式編輯器。學員在 `exercise/` 資料夾工作,`solution/` 有相同結構的解答。現場有三位 TA 加上後方的 Melanie 支援。

**練習內容**:在 `exercise/tools/workflow.py` 裡把 agent 的建構取消註解。用的是 OpenAI Agents SDK 整合——給名字、給 system prompt、選模型(他說這題用 GPT-4o 就夠了)、給工具。工具本身只是幾個 web request(取座標、取 IP 位置資訊、取天氣),但它們是**以 activity 的形式傳入**,因此自動獲得 Temporal 的 durability。

**執行**:先啟動 **worker**(他解釋 worker 是負責**輪詢 task queue、決定要執行哪些工作**的程序),再跑 starter,送出「What is the weather in Tokyo?」。

**成果**:到 Temporal UI 重新整理,workflow 已完成。他強調這是他自己最喜歡 Temporal 的地方——**可見性**:整條 timeline 一目了然(invoke model activity → get coordinates → invoke model activity → get weather → invoke model activity),每一步都能點進去看 header、輸入與輸出。最後答案是東京 79.6°F、微風。

### 主題四:把它弄壞——durability 的現場證明(約 01:25–01:28)

這是整場最核心的示範。到 **network control panel 把 weather API 關掉**(他舉的情境:你的網路擋掉了、企業政策不准、API 本身掛了、或 AWS 掛了所以連帶掛了),然後重跑「What is the weather in London?」。

在 Temporal UI 裡:

- workflow 進入 **Running** 狀態,而且**會一直維持 Running 直到問題解決**。
- 那個 activity **持續重試**。因為他們沒有明確指定 retry policy,用的是預設值,所以**會永遠重試下去**;而且內建 **automatic backoff 與 backoff coefficient**。他順帶解釋為什麼需要 backoff:你不會希望 LLM 一直狂打 OpenAI API,那很燒資源;打 10 次失敗就等 10 秒,再失敗就等 30 秒——這就是 exponential backoff,**沒有 Temporal 的話這段邏輯得自己寫,而且會寫得很醜**。
- 錯誤訊息顯示 **503 service unavailable**。

接著把 weather API 打開:「想像 AWS 的故障排除了」。幾個瞬間之後 workflow **自動恢復,像失敗從未發生過**——**不需要動任何程式碼**,從失敗發生的那一點精確接續,沒有額外資源被消耗,workflow 正確結束,終端機拿到倫敦的天氣。

### 主題五:自己寫 loop vs 用 SDK(約 01:28–01:30)

他順帶拆穿了 agentic framework 的神祕感:**很多框架把 agentic loop 藏在背後,但它本質上就是一個 `while True` 迴圈**——等待使用者輸入、判斷資訊是否足夠、不夠就呼叫工具或做別的事。

自己寫大概 **50 行**;用 OpenAI Agents SDK 就是 **`runner.run` 一行**,loop 由 SDK 處理。而 `activity_as_tool` 這類包裝則負責替所有被呼叫的工具提供 durability。

### 主題六:為什麼要拆成多個 agent(約 01:36–01:38)

中途他讓現場投票決定接下來講 human in the loop 還是 multi-agent orchestration,**現場選了 multi-agent**,human in the loop 因此跳過(他解釋 human-in-the-loop 就是一個「詢問並等待人類回饋」的工具,可以等核准也可以等資訊——「**ChatGPT 本身就是一種 human in the loop**,它會等你回應才繼續」)。

拆分的理由是 context 的四種病:**context poisoning、distraction、context clash、confusion**。小 workflow 還好,但**流程愈大、資料愈多、塞進去的東西愈多,LLM 就愈難推理**。

### 主題七:三種呼叫 sub-agent 的方式與 Nexus(約 01:38–01:43)

架構是:**personal assistant agent 作為整個流程的入口**(他類比為你的 ChatGPT),由它決定要呼叫 weather agent、F1 agent,或兩個都叫。

呼叫 sub-agent 有三種做法:

1. **當成 activity 呼叫**。
2. **當成 child workflow 呼叫**——主 workflow 啟動一個子 workflow,兩者綁在一起;適合把決策邏輯放進另一個流程。
3. **透過 Nexus**——Temporal 的另一項技術,可依**團隊領域、地區、安全性考量、程式碼需求**做切分,例如你希望某個 agent 用和別的 agent 不同的頻率部署。

他對 Nexus 的解釋是:**把它想成一個 API**。你決定要向另一個團隊或另一個組織暴露哪些 endpoint,對方只能呼叫那些;呼叫方提供 endpoint 與 service 名稱就能呼叫,**背後怎麼實作可以隨時改(升到 v2 之類),而契約不變,呼叫方不必改程式碼**。

### 主題八:多 agent 實作與再次弄壞它(約 01:44–01:52)

**Demo 5 的架構**:personal assistant workflow 收到「下一場 F1 比賽在哪、那裡現在天氣如何?」→ 透過 **Nexus operation** 呼叫 F1 agent(跑在不同檔案、不同 task queue,最終呼叫他們自架的 **F1 MCP server**,再打到 F1 API)→ 資訊回到 personal assistant → 它判斷「還缺天氣」→ 以 **child workflow** 呼叫 weather agent(內部再呼叫 get coordinates 與 get weather 兩個 activity,就是公開 HTTP 請求)→ 彙整後給出最終答案。

實跑結果:下一場是 **8 月 23 日的荷蘭大獎賽**,當地 **64.7°F**。在 Temporal UI 中可以看到兩個 workflow 同時執行,而且 **Nexus link 是可以點進去的**——點進去就是 F1 expert 那個獨立 workflow 的完整執行紀錄。

然後他又把 weather API 關掉重跑:兩個 workflow 都不會完成,**卡點精準落在 weather agent workflow 的 `get_coordinates`**,持續失敗直到問題解決。打開之後兩者都成功結束——他提醒**恢復時間取決於 retry policy 與 exponential backoff**,等久了可能要多等幾秒才會重試。

### 主題九:隨堂測驗與收尾(約 01:31–01:36、01:52–01:59)

他穿插了手機搶答測驗與排行榜,前三名送周邊。幾個值得記的答案:

| 問題 | 答案要點 |
|------|----------|
| 誰決定下一步要做什麼動作? | **LLM 是 decision maker**。我們給 context、告訴它有哪些工具,由它決定資訊夠不夠、接下來要不要再呼叫工具 |
| Demo 2 裡的 loop 是誰寫的? | 我們沒寫 loop,**用的是 OpenAI Agents SDK,loop 在 `runner.run` 裡面** |
| 如果 workflow 有了但工具沒加進 tools 物件會怎樣? | **workflow 照樣啟動、activity 照樣跑**,只是沒有工具可呼叫,所以會回一個無效的答案 |
| 為什麼 LLM 呼叫要包在 activity 裡? | **因為它們是非確定性的**。非確定性的程式碼放 activity 才能被 replay;確定性的商業流程留在 workflow |
| Nexus 相對於在程式碼裡直接 import,多給了什麼? | 它是 **API 契約**;但它**不會**幫你處理額外的操作,namespace 一致性也仍是開發者的責任 |

**收尾**(約 01:58–01:59):時間到被請下台,他只要求兩件事——到 LinkedIn 追蹤他(所有內容會放上去)、以及在 lab 的 feedback 分頁留下**可以據以改進的**回饋(「你可以說我很爛,沒問題,但請告訴我為什麼很爛」)。測驗前三名是 Anton、Henrik、Ming,周邊在後排領。有問題也可以去 Temporal 的 Slack 社群。

## English Notes

### Opening: get the whole room on its feet (~01:04:39–01:06)

After a long block of AI talks, Advolodkin opened by asking everyone to stand, high-five two people, look them in the eye, and tell them they're amazing — then filmed a selfie video of the room cheering (he made them redo it "5x louder"). Introductions: developer advocate at Temporal, dog dad, roller skater, dog named Mia.

His framing: **you retain far more by being hands-on than by listening passively.** The plan was four topics — foundations of agentic AI systems (and building one), building with an agentic framework (OpenAI Agents SDK), human in the loop, and orchestrating micro-agents — and he said upfront they probably wouldn't get through all of it, but the GitHub repo would follow.

### Topic 1: what an agentic loop is (~01:07)

An LLM can reason about the context you give it. **What it lacks is the ability to take action when it doesn't have enough information.** The agent loop supplies exactly that: the capability to act outside itself.

Start with instructions and goals — his example: "you're a travel assistant, find a flight to Miami, ask for confirmation before booking payments." Pass that context to the decision maker, the LLM. **The LLM decides whether it has enough information**: if yes, final answer; if no, call a tool. Tools are defined by the harness or by you; you tell the LLM they exist and **the LLM decides when to use them**. It evaluates the output, and keeps looping to gather information until it can comfortably answer.

A live poll on Temporal familiarity showed most of the room had **never heard of it, or heard of it but never used it** — so he flagged the session as advanced for many attendees and promised to walk them through.

### Topic 2: the Temporal mental model (~01:10:47–01:13)

In one line: **Temporal lets you write code as though failures don't exist.**

- You focus on the **business logic** of your agents and distributed systems — and he was explicit that **agents are distributed systems**. That goes into a **workflow**: the sequence of steps you want to execute.
- You pull out the **non-deterministic steps** — API calls, LLM calls, database queries — into **activities**.
- Wrapping those activities in the SDKs (Python, TypeScript, Java, Go, Ruby, and more) creates a **history** of everything performed up to a given point.
- When any failure occurs, Temporal **pauses at that point in the history and waits** for the failure to be resolved — seconds, minutes, or **years**. When it is, execution proceeds **as though the failure never happened**.
- Waiting **costs no resources**, because it's all recorded in the history. He cited **six nines of reliability**.

What can fail? Nearly everything: LLM calls due to network reliability (**he got a 429 rate limit from OpenAI that very morning**), API calls, rate limits, services going down, AWS going down. **Wrapped in an activity, Temporal picks up once they're resolved.**

### Topic 3: hands-on — the first workflow (~01:13–01:25)

The environment was a browser-based virtual lab: no setup, a Docker container with a ~90-second boot. Tabs for a worker terminal, a starter terminal, the **Temporal UI**, a **network control panel for simulating network failures**, and a code editor. Attendees worked out of `exercise/`, with a mirrored `solution/` folder. Three TAs up front, plus Melanie at the back.

**The exercise**: uncomment the agent construction in `exercise/tools/workflow.py`. It uses the OpenAI Agents SDK integration — give it a name, a system prompt, a model (GPT-4o "is good enough for this one"), and tools. The tools are just web requests (get coordinates, get IP location info, get weather), but they're passed in **as activity tools**, so they inherit Temporal's durability.

**Running it**: start the **worker** — the process that polls the task queue to decide what work to perform — then run the starter, which asks "What is the weather in Tokyo?"

**The payoff**: refresh the Temporal UI and the workflow has already completed. This is what he says he loves most about Temporal — **visibility**. The whole timeline is laid out (invoke model activity → get coordinates → invoke model activity → get weather → invoke model activity), and every step can be opened to inspect headers, inputs, and outputs. The answer: 79.6°F in Tokyo with light wind.

### Topic 4: break it — durability demonstrated live (~01:25–01:28)

The centerpiece demo. In the **network control panel, turn off the weather API** — imagine your network blocks it, your enterprise won't allow it, the API is down, or AWS is down so the API is down. Then rerun with "What is the weather in London?"

In the Temporal UI:

- The workflow goes to **Running** and **stays Running until the problem is resolved**.
- The activity **keeps retrying**. Since no retry policy was specified explicitly, the default applies, which **retries forever**, with **automatic backoff and backoff coefficients** built in. He explained why you want that: you don't want an LLM hammering the OpenAI API, because it costs you resources — 10 calls, wait 10 seconds, 10 more failures, wait 30 seconds. That's exponential backoff, and **without Temporal you'd be writing that logic yourself, and it gets hairy**.
- The last failure reads **503 service unavailable**.

Then turn the weather API back on — "let's imagine AWS had an outage, it's back up." Within moments the workflow recovers **as though no failure ever occurred**: **no code touched**, resumption from exactly where the failure happened, no extra resources consumed, and the terminal gets London's weather.

### Topic 5: rolling your own loop versus the SDK (~01:28–01:30)

He demystified agentic frameworks along the way: **most hide the agentic loop, but it's ultimately a `while True` loop** — wait for user input, decide whether you have enough information to make a decision, call tools if you don't.

Writing it yourself is roughly **50 lines**; with the OpenAI Agents SDK it's **one line of `runner.run`**, with the SDK handling the loop. Wrapping tools as activities is what supplies durability to everything the agent calls.

### Topic 6: why split into multiple agents (~01:36–01:38)

He put the next section to a vote — human in the loop or multi-agent orchestration — and **the room picked multi-agent**, so human in the loop got skipped. (His one-line version: human-in-the-loop is a tool that asks and waits for human feedback, whether an approval or information — "**ChatGPT is a human-in-the-loop type of thing**," waiting for you to respond before proceeding.)

The reason to split: **context poisoning, distraction, context clash, and confusion**, all caused by too much context. It's fine for a small workflow, but **the larger the workflow and the more data you provide, the harder it is for LLMs to reason**.

### Topic 7: three ways to call a sub-agent, and Nexus (~01:38–01:43)

The architecture: a **personal assistant agent as the entry point** to the whole process — your ChatGPT — which decides whether to call the weather agent, the F1 agent, both, or more.

Three ways to invoke sub-agents:

1. **As an activity.**
2. **As a child workflow** — the main workflow starts a child workflow and the two are tied together; good for putting decision-making logic into its own process.
3. **Via Nexus** — Temporal's other technology, which segregates by **team domain, region, security concerns, or code requirements** — for instance when you want one agent deployed at a different cadence than another.

His framing of Nexus: **think of it as an API.** You expose only the endpoints you choose to another team or organization, and they can call only those. The caller supplies the endpoint and service name; **whatever happens behind the scenes can change — move to v2, whatever — while the contract stays the same and the caller never changes their code.**

### Topic 8: the multi-agent build, and breaking it again (~01:44–01:52)

**Demo 5's architecture**: the personal assistant workflow takes "when is the next F1 race and what's the weather there right now?" → calls the F1 agent through a **Nexus operation** (a separate file on a separate task queue, which calls an **F1 MCP server** they host, which calls the F1 APIs) → the result comes back → the assistant decides it still needs weather → calls the weather agent as a **child workflow** (which calls get-coordinates and get-weather activities, both plain public HTTP requests) → assembles the final answer.

The live result: the **Dutch Grand Prix on August 23**, with **64.7°F** on site. The Temporal UI showed two workflows executing, and the **Nexus link is clickable** — following it lands you inside the F1 expert's own workflow with its complete execution record.

Then he killed the weather API again. Neither workflow completes; the failure lands precisely on **`get_coordinates` inside the weather agent workflow** and keeps failing until resolved. Turn it back on and both complete — with the caveat that **restart timing depends on the retry policy and exponential backoff**, so after a long wait it may take extra seconds before the next retry.

### Topic 9: quizzes and wrap-up (~01:31–01:36, 01:52–01:59)

He ran phone-based quizzes with a leaderboard, swag for the top three. The answers worth keeping:

| Question | Key answer |
|----------|------------|
| Who decides which action to perform next? | **The LLM is the decision maker.** We pass context and declare tools; it decides whether it has enough information and what to do next |
| Who wrote the loop in demo 2? | Nobody — **the OpenAI Agents SDK writes it, inside `runner.run`** |
| What happens if the workflow exists but tools weren't added to the tools object? | **The workflow still starts and the activity still runs** — there are just no tools to call, so it returns invalid information |
| Why wrap LLM calls in activities? | **Because they're non-deterministic.** Non-deterministic code goes in activities so it can be replayed; the deterministic business flow stays in the workflow |
| What does Nexus give you that direct imports don't? | It's an **API contract** — but it does **not** give you extra operations, and namespace consistency is still the developer's job |

**Wrap-up** (~01:58–01:59): out of time and being kicked off stage, he asked for two things — follow him on LinkedIn, where all the content will be posted, and leave feedback in the lab's feedback tab, **feedback he can act on** ("you can tell me I suck, no big deal, but please tell me why I suck"). Quiz winners: Anton, Henrik, and Ming, with swag at the back of the room. The Temporal Slack community is there for follow-up questions.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Temporal workflow / activity | workflow 放確定性的商業流程,activity 放非確定性、會失敗的步驟(LLM、API、DB) | Workflows hold deterministic business flow; activities hold non-deterministic, failure-prone steps (LLM, API, DB) | 工作坊的核心心智模型 / the core mental model |
| Temporal worker / task queue | worker 輪詢 task queue、決定要執行哪些待辦工作 | The worker polls the task queue to decide what backlog work to execute | |
| Temporal UI | 逐步檢視 workflow timeline、每個 activity 的輸入輸出與 header | Step-by-step timeline with per-activity inputs, outputs, and headers | 講者最推薦的賣點 / his favorite feature |
| Temporal Nexus | 以 API 契約形式跨團隊/地區/安全邊界呼叫其他 workflow | Calling other workflows across team, region, or security boundaries as an API contract | UI 中的 Nexus link 可點進被呼叫的 workflow |
| OpenAI Agents SDK | 工作坊使用的 agent 框架,`runner.run` 內含 agentic loop | The agent framework used; the agentic loop lives inside `runner.run` | 與 Temporal 有官方整合 |
| F1 MCP server | 由 Temporal 代管、供 F1 agent 呼叫的 MCP server,底層打 F1 API | Temporal-hosted MCP server the F1 agent calls, which in turn hits the F1 APIs | demo 5 使用 |
| Network control panel | lab 內建的網路故障模擬器,可關閉 geolocation / weather 等 API | Built-in lab tool to simulate network failures by disabling APIs | durability 示範的關鍵道具 |
| Temporal Slack community | 後續提問管道 | Follow-up channel for questions | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Nikolai Lotkin | Nikolay Advolodkin |
| temp using temporal | Temporal |
| agenda loop / gentic loop | agentic loop |
| GPT40 | GPT-4o |
| task Q | task queue |
| activity this tool | `activity_as_tool`(推定 / inferred) |
| codeex / cla / cloth code | Codex / Claude / Claude Code |
| runner.run run | `runner.run` |
| get coco coordinates | get coordinates |
| six nines(字幕正確)| — |

## 待確認 / To Verify

- 虛擬 lab 平台字幕作 "instruct environment",聽起來像 **Instruqt**,需確認。/ The lab platform was transcribed as "instruct environment", plausibly **Instruqt** — to confirm.
- 工作坊 GitHub repo 與 lab 網址在字幕中只以口頭「navigate to that URL」帶過,未出現實際網址。/ The workshop repo and lab URLs were only pointed at on screen; no URL appears in the captions.
- 他說 Temporal 有 "six nines of reliability",指的是雲端服務 SLA 還是別的指標,現場未說明。/ He cited "six nines of reliability" without specifying whether that's the cloud SLA or another measure.
- 包裝工具用的 API 字幕作 "activity this tool",推定為 `activity_as_tool`,需對照 repo 確認。/ The tool-wrapping API was transcribed as "activity this tool", inferred here as `activity_as_tool` — check against the repo.
- 現場提到的 TA 名字 "Melanie" 僅為聽寫,未查證。/ The TA name "Melanie" is as transcribed only.
