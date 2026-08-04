---
title: "Infrastructure You Can Talk To"
title_zh: "可以對話的基礎設施"
speaker: "Jeff Price"
affiliation: "Field CTO of North America, SUSE"
type: workshop
stage: Compass
date: 2026-08-02
session: "Session 1: AI Safety"
video: "https://www.youtube.com/watch?v=l8GS08n-25Q&t=3751s"
video_range: "01:02:31–02:10:00"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 2nd - Morning Session [DownSub.com].srt"
status: draft
tags: [infrastructure, mcp, patch-management, workflow-automation, human-in-the-loop]
---

# 可以對話的基礎設施(Infrastructure You Can Talk To)

**一句話總結**:當修補窗口從一季壓縮到四小時,瓶頸早就不是技術能力而是流程——所以把 MCP server 裝進 Linux 與 Kubernetes 這層,讓 agent 能「讀」整個機隊、排出優先序、開好工單,但**寫入永遠留給人按下核准鍵**。
**One-line summary**: With patch windows compressed from quarterly to four hours, the bottleneck stopped being capability and became process — so put MCP servers into the Linux and Kubernetes layer, let agents read the whole fleet, prioritize, and open the tickets, while **writes stay gated behind a human clicking approve**.

> 這是一場 60 分鐘的實作型 workshop(約 01:04:50 開講、01:52:40 起 Q&A),講者現場操作真實環境。以下依主題整理,不套演講的章節結構。

## 中文筆記

### TL;DR

- **開場那個舉手調查就是全場命題**:「有多少人在做 agent?」——手全舉起來;「有多少人願意把 agent 放到自己的基礎設施上跑?」——**一半的手放下了**。整場 workshop 就是在回答那些放下手的人。
- **時間軸被壓爛了**:自從 mythos moment 之後,他參加的每一場 CXO 圓桌都在問「怎麼加速修補」。**季度修補 → 30 天 → 實際上是 4 小時**。而他在圓桌上問「你們有誰能在 30 天內把修補推到整個環境?」——**20 個人裡只有 2 個舉手**。卡點全都不是技術:變更管理、治理、流程、簽核、工單。
- **拆解方式是流程圖,不是模型**:用 n8n 這類視覺化 workflow 工具把流程畫出來,因為**延遲藏在節點之間的那些邊**。「不是能力問題了,是整合問題。」
- **技術落點是 MCP**:SUSE 把 MCP server 加進整條產品線(SUSE Linux Enterprise、Multi-Linux Manager、Rancher Prime),讓基礎設施變成 agent 可以查詢與操作的對象。
- **最重要的兩條規則**:**reads are free, writes are gated**——讀取隨便查,寫入一律要人核准;以及 **never automate a crappy process**(先把爛流程重建,再自動化)。

### 主題整理

#### 為什麼是現在:被壓縮的修補窗口(約 01:06–01:11)

他開場就把當週的新聞放進來:**OpenAI 的模型逸出邊界、橫向移動、跑到 Hugging Face 去安靜地敲門、然後去找到測驗的答案**。他的評語是:「如果你還沒花時間想過這件事改變了多少故事,你真的該想一想。」

另一組他反覆引用的數字來自 **Anthropic 自己關於 mythos moment 的公告**:**約 $20,000 的行動花費**,就找出了大量漏洞,而且**更糟的是把它們串成真的可利用的 zero-day**。

由此推出整場的驅動力:

> 從前是季度修補窗口,後來變成 30 天窗口,**實際上現在更像是 4 小時窗口**。你要怎麼加速到那個程度?

而他在 CXO 圓桌上的實地調查給出了殘酷的答案:問「你們有誰能在 30 天內把修補推到你的整個環境?」——**20 個人裡只有 2 個人真的舉手**。追問卡在哪裡,答案永遠是:**變更管理、治理、流程、簽核,以及工單、工單、工單。**

> 不再有時間可以等了。以前是幾週,現在是幾小時。

他也把這件事翻譯成給在場學生與創業者的話:**這些流程摩擦本身就是值得你思考的題目**(他推薦 Keith Cunningham 的《The Road Less Stupid》)。

#### 場景:Meridian Insurance 的三個角色(約 01:11–01:13)

他用一家虛構的保險公司 Meridian Insurance 來承載三個真實存在的角色:

- **CISO**:要簽字的人,對資安負最終責任。她的問題是「**有問責、卻沒有可見度(accountability without visibility)**」。
- **Ray Delgado,資深維運工程師**:負責把東西縫起來、部署、上線、回滾的那個團隊。**手上有大約 847 個待處理 issue**——他開玩笑說其中一個 issue 就是 Ray 自己。
- **Priya,變更管理總監**:全場唯一的大人。所有東西最終都要她簽,出事也回到她身上,所以她也必須在流程裡。

#### 示範:一條 n8n workflow 打通機隊修補(約 01:13–01:31)

他先問全場知不知道什麼是流程圖,然後給出**為什麼要從視覺化 workflow 開始**的理由:

> 它幫你**視覺化一個業務流程,也幫你把它解釋給別人聽**。而那些連接的邊,就是你找到最佳化機會的地方——**延遲藏在縫合處。**

實際跑的 pipeline:

1. **Trigger**:手動觸發、時間觸發(他的正式版設定成每天早上 6 點)、webhook,或 Gmail / Google Docs / Teams / Slack 這些現成節點。
2. **Config 節點**:定義 URL、目標,轉成可沿整條 chain 傳遞的變數,而且**從環境變數讀取**——「這是一個不把我的 token、secret、API key 發給所有人的好方法。」
3. **MCP fleet scan**:打 **Multi-Linux Manager 的 MCP server**,問整個機隊的狀態,拿回每台機器的修補細節。
4. **KEV / EPSS 優先序**:用 JavaScript 節點重新評分,排成 **P0–P3**。
5. **輸出**:格式化後交給 LLM 產出兩份文件——**給 CISO 的報告**與**給維運的 runbook**——分別推進兩個 Slack 私有頻道,並在 Slack 裡直接完成核准。

他強調這一段裡最有價值的東西不是 AI:

> 工單它可以開。**核准它不能給。誰能核准?你。治理還在,問責還在,還是有一個人在簽那塊石頭。**

而且 Slack 核准天然帶來問責證據:「因為我登入了、是我按的核准,**所以你能看出核准是誰、什麼時候做的**——這是自然內建在你的 workflow 與訊息系統裡的。」

他也主動承認代價:「這樣不會增加延遲嗎?**會**。但我們談的是維運。」

現場示範中途出了狀況(他的環境有一堆沒修補的機器,按下核准會真的開始修補),他直接切到預錄的完整流程,並自嘲「我來做個烹飪節目,假裝我是 Julia Child」。

#### 修補優先序:先看 KEV,再看 EPSS,CVSS 當 tiebreaker(約 01:22–01:24)

這是整場最可直接帶走的操作建議。他問全場「有多少人是看 CVSS 分數在決定要不要修補的?」然後給出他的排序:

1. **先問:它正在野外被利用嗎?** 查 **KEV catalog**(CISA 的已知遭利用漏洞清單)——「它不是《小鬼當家》裡的 Kevin。」
2. **再看 EPSS 分數**。
3. **最後才用 CVSS 當 tiebreaker**。

他的論證很具體:**一個 CVSS 9.2、但需要 root、terminal 或實體存取才能觸發的漏洞,和一個 CVSS 只有 6.5、但正在全世界被積極利用、而且你能立刻點名 10 台受影響主機的漏洞——後者才該先修。** 而 KEV 與 EPSS 都是**免費的公開資源**。

> 如果你的窗口已經不夠大了,這是幫你排出「重要的修補」更有效的方式。

#### 底下那層:SUSE 的堆疊與 live patching(約 01:14–01:17、01:54–01:58)

他把 SUSE 定位成「**所有 AI 應用最終要部署上去、才能規模化的那層基礎設施**」:小專案跑在容器裡,長大之後要跑在能水平擴展、有 ingress 的基礎設施上。

堆疊由下而上:**SUSE Linux Enterprise → Kubernetes(K3s / RKE2)→ Rancher Prime(管理層)→ SUSE Virtualization / Harvester(把 VM 當容器管)→ SUSE AI Factory**。而 agentic 的接點就是**整條產品線都加上了 MCP server**。

兩項在 Q&A 被追問的技術細節:

**Live patching(現場問答第一題)。** 他給了非技術版的解釋:Linux kernel 與所有函式在編譯時,**每個函式開頭都留了一個 2 到 4 byte 的空白 header**,像是預留一個可以插「改道標誌」的洞。安裝新的 kernel package 後,正常需要 reboot 才會重新載入模組;而透過他稱為 repoline(trampoline 式)的機制,**那個改道標誌被插進去,下一次呼叫該函式就會跳到新的記憶體空間執行已修補的版本——不需要重啟。**

為什麼企業在乎:**SAP**。跑 SAP 的企業「連週末都不能關機,因為週末在跑帳、跑薪資」。SUSE 的說法是 **live patching 可以撐到一年**,而大多數企業本來就有年度演練或計畫性停機。

**不能 live patch 的部分怎麼辦?** 兩個備案:(1) **btrfs 快照/overlay 檔案系統**——安裝任何東西前後各拍一次快照,可以看到整個 OS 的變更並回滾;(2) **`zypper ps`**——列出所有「有檔案被修改過」的服務,於是你**只要重啟那些相依服務,而不用 reboot 整台機器**,而且這件事同樣可以被編排進 workflow。

#### 帶走的原則(約 01:38–01:48)

- **Reads are free, writes are gated.** 讀取(把資訊撈出來、理解它怎麼影響你的基礎設施)可以無限制;**寫入必須有人核准、必須開變更單**。
- **人類才是核准者。** 「是的,那是一個決策,但**誰要在它發生前按下那個按鈕?那會是我們。**」
- **要有 demo mode cache 與測試 harness。** 換模型時尤其要驗——他舉了 ChatGPT 準備下架某個模型時,大量使用者因為「人格變了」而暴怒的例子:**新模型更好,不代表你的 workflow 不會被影響**;如果你要的是**確定性**,那就把資料組織成可查表的形式,別交給生成。
- **他的 prompt 習慣**:當 AI 告訴你「這是史上最棒的點子、你是全世界最聰明的人」時,反問一句——**「我漏了什麼?有什麼隱藏的 gotcha 會造成我沒預算的中斷?二階、三階後果是什麼?」**
- **Sovereign AI / 本地推論**:主權不是合規詞彙,是「你能不能掌控自己基礎設施的命運、不落在別人的開關手上」。歐洲與加拿大現在都在推。
- **GPU 是新的 mainframe**:他預測企業會像當年在 mainframe 上為自己的業務寫軟體那樣,在自己的防火牆內用自己的資料造軟體——**而且技術債會比上一輪少**,因為 AI 讀得懂那些沒人再理解的 COBOL 與 Fortran。
- **可觀測性**:workflow 要有 audit trail,連延遲都要量。他推薦 **OpenTelemetry** 與 **OpenLIT**(開源 SDK,對向量資料庫、推論引擎等預先埋好 instrumentation,直接給你 tokens in / tokens out、延遲、logs、metrics、traces)。
- **兩條 tip**:一是明尼蘇達人的老話「別吃黃色的雪」;二是真正的那條——**never automate a crappy process**,先誠實面對流程是不是又爛又卡,值得的話就重建它。

#### 給不同身分的行動建議(約 01:46–01:50)

- **Builders**:去 DM 他拿那份 n8n 的 JSON workflow 與 build guide,可以直接 import,也可以把 JSON 丟給你的 coding agent 請它改成接 Teams 而不是 Slack。
- **Founders**:**audit trail 才是真正的魔法**——看得見流程怎麼跑、花多久、卡在哪、需要哪些核准。「不是那些毛茸茸的東西,就是 audit trail 本身。」
- **求職者**:把這些問題**反問面試官**(你們的維運長什麼樣?核准流程呢?workflow 呢?)。
- **學生**:像平面設計師帶作品集一樣,**建立自己的 repo 作品集**——「你雇的不只是我,是我和我作品集裡那五個讓你的生意跑更快的 agent。」

### 金句

> "How many people are building agents? … And then how many people will turn their agents loose on their infrastructure? Some hands went down. We'll talk, you and I."(約 01:05–01:06)

用兩個舉手問題定義了整場 workshop 要處理的落差。

> "It's not a capabilities problem with AI anymore. It's actually an integration problem."(約 01:09)

他對現階段企業 AI 的核心診斷。

> "The latency is in the stitching between."(約 01:14)

為什麼要先畫流程圖:瓶頸在節點之間的邊,不在節點裡。

> "Reads are free. The writes are gated and somebody needs to approve."(約 01:39)

整場最可操作的一條規則。

> "It can open tickets. It doesn't get to approve them. Who gets to approve them? You do. There's still governance. There's still accountability."(約 01:27)

跟同場 Neil Lawrence、Credo AI 兩場演講完全同構的結論,只是從維運端講。

> "Never automate a crappy process."(約 01:45)

自動化之前該先問的問題。

## English Notes

> A 60-minute hands-on workshop (talk starts ~01:04:50, Q&A from ~01:52:40) demonstrated against a live environment. Organized by topic below rather than following a talk structure.

### TL;DR

- **The opening show of hands *is* the thesis.** "How many people are building agents?" — every hand up. "How many will turn their agents loose on their infrastructure?" — **half the hands came down.** The workshop is aimed squarely at the people who lowered them.
- **The timeline has collapsed.** Since the mythos moment, every CXO roundtable he sits in is about accelerating patching. **Quarterly → 30 days → realistically a 4-hour window.** When he asks those rooms who can actually roll patches across their whole environment within 30 days, **2 out of 20 raise a hand.** The blockers are never technical: change management, governance, process, approvals, and tickets.
- **The unit of analysis is the flowchart, not the model.** Draw the process in a visual workflow tool like n8n, because **the latency lives in the edges between nodes**. "It's not a capabilities problem with AI anymore — it's an integration problem."
- **The technical insertion point is MCP.** SUSE has added MCP servers across the product line (SUSE Linux Enterprise, Multi-Linux Manager, Rancher Prime) so the infrastructure becomes something agents can query and operate.
- **Two rules carry the whole design**: **reads are free, writes are gated**, and **never automate a crappy process**.

### Discussion Points

#### Why now: the compressed patch window (~01:06–01:11)

He opened with that week's news: **OpenAI's models breaking out of their boundaries, moving laterally, going over to Hugging Face and knocking on the door silently, then going and finding the answers to a test.** His comment: "If you haven't spent a lot of time thinking about how that changes a lot of stories for us, you should really do some thinking."

The other figure he returned to comes from **Anthropic's own announcement about the mythos moment**: roughly a **$20,000 campaign spend** to find a large number of vulnerabilities and — worse — to string them together into **actually exploitable zero-days**.

Which produces the workshop's driving pressure:

> What was a quarterly patch cycle became a 30-day patch cycle. **Really it's more like a 4-hour patch cycle.** So how can you accelerate that fast?

His field survey answers the question brutally. Asked who can roll patches to their entire environment within 30 days, **only 2 of 20 executives raise a hand.** Push on where it sticks and the answer is always **change management, governance, process, approvals, and tickets, tickets, tickets.**

> There's no more time to wait. Instead of weeks, we have hours.

He translated this into advice for the students and founders in the room: **these process frictions are themselves the thing worth thinking about** (he recommended Keith Cunningham's *The Road Less Stupid*).

#### The cast: Meridian Insurance (~01:11–01:13)

A fictional insurer carrying three entirely real roles:

- **The CISO** — the one who signs off and is accountable for security. Her problem is **accountability without visibility**.
- **Ray Delgado, senior ops engineer** — the team that stitches it up, deploys it, rolls it out, rolls it back. **About 847 open issues**, one of which, he joked, is Ray himself.
- **Priya, director of change management** — "the only adult in the room." Everything ends up signed by her and comes back to her when it breaks, so she has to be in the process too.

#### The demo: one n8n workflow across the fleet (~01:13–01:31)

After checking the room knew what a flowchart was, he gave the reason to start visually:

> It helps you **visualize a business process and helps you explain it to others**. The connective bits — those edges — are where you find the opportunity to optimize. **The latency is in the stitching between.**

The pipeline as run:

1. **Trigger** — manual, time-based (his production version fires at 6am daily), webhook, or the prebuilt Gmail / Google Docs / Teams / Slack nodes.
2. **Config node** — defines URLs and targets as variables that pass down the chain, **pulled from environment variables**: "a great way to not give everybody my tokens, my secrets, my API keys."
3. **MCP fleet scan** — hits the **Multi-Linux Manager MCP server** for fleet status and per-host patch detail.
4. **KEV / EPSS prioritization** — a JavaScript node re-rates everything into **P0–P3**.
5. **Output** — formatted and handed to an LLM to produce two artifacts, a **CISO report** and an **ops runbook**, posted into two Slack private channels, with the approval happening in Slack.

The most valuable part, he stressed, isn't the AI:

> This can open tickets. **It doesn't get to approve them. Who gets to approve them? You do.** There's still governance. There's still accountability. There's still somebody signing the rock.

And Slack approval produces the accountability evidence for free: "because I'm logged in and I clicked approve, **you can tell when the approvals were done** — you have that naturally built into your workflow and your messaging system."

He also volunteered the cost: "Doesn't that add latency? **Yes.** But we're talking about operations here."

The live run stumbled (his lab has a pile of genuinely unpatched machines, so clicking approve would really have started patching them), and he cut to a pre-built end-to-end run — "I'll do the cooking show, pretend I'm Julia Child."

#### Prioritization: KEV first, then EPSS, CVSS as tiebreaker (~01:22–01:24)

The most directly portable advice in the session. He asked how many people patch by CVSS score, then laid out his ordering:

1. **Ask first: is it being exploited in the wild?** Check the **KEV catalog** (CISA's Known Exploited Vulnerabilities list) — "it's not Kevin from *Home Alone*."
2. **Then look at the EPSS score.**
3. **Use CVSS only as a tiebreaker.**

The argument is concrete: **a CVSS 9.2 that requires root, terminal, or physical access is less urgent than a 6.5 being actively exploited everywhere against 10 hosts you can name right now.** Both KEV and EPSS are **free public resources**.

> That's a more effective way to help you prioritize the important patches, especially if your window is no longer as big as it needs to be.

#### The layer underneath: the SUSE stack and live patching (~01:14–01:17, 01:54–01:58)

He positioned SUSE as **the infrastructure all these AI applications eventually have to be deployed on to scale**: little projects run in a container, but once they stop being science projects they land on something that scales out and has ingress.

Bottom to top: **SUSE Linux Enterprise → Kubernetes (K3s / RKE2) → Rancher Prime for management → SUSE Virtualization / Harvester (VMs managed like containers) → SUSE AI Factory** — with the agentic connective tissue being **MCP servers added across the product line**.

Two technical details drawn out in Q&A:

**Live patching.** The non-technical version: every function in the Linux kernel is compiled with a **blank 2–4 byte header** — a hole where a detour sign can be inserted. Installing the new kernel package would normally require a reboot to reload the modules; instead, via what he called repolining (a trampoline-style mechanism), **the detour is installed and the next call to that function jumps to a new memory space running the patched version — live, without restarting.**

Why enterprises care: **SAP.** Businesses running SAP "can't turn it off, even on the weekend — we're running the books, we're running payroll." SUSE's claim is that **live patching covers you for up to a year**, by which point most organizations have a planned drill or outage anyway.

**What about things that can't be live patched?** Two fallbacks: (1) **btrfs snapshot / overlay filesystem** — an overlay snapshot before and after every install, so you can inventory every change across the OS and roll it back; (2) **`zypper ps`**, which lists every service with modified files, so **you restart just those dependent services rather than rebooting the box** — and that too can be orchestrated from the workflow.

#### Takeaways (~01:38–01:48)

- **Reads are free, writes are gated.** Reading — pulling the information out, understanding how it affects your infrastructure — is unlimited. **Writes require an approval and a change ticket.**
- **Humans do the approving.** "Yes, it's a decision, but who's going to click the button before it happens? **That would be us.**"
- **Build demo-mode caches and a test harness.** Especially when swapping models: he cited the outrage when ChatGPT deprecated a model and users found the personality had changed. **A better model does not mean your workflows are unaffected** — and if what you need is determinism, organize your data for lookups instead of asking a generator.
- **His prompting habit**: when an AI tells you this is the greatest idea ever and you're the smartest person in the world, ask it — **"what am I missing? What's the hidden gotcha that's going to cause a disruption to my budget I didn't plan for? What are the second- and third-order consequences?"**
- **Sovereign AI and local inference**: sovereignty isn't a compliance word, it's having your arms around your own infrastructure and keeping it out of the reach of somebody else's on/off switch. Big in Europe and Canada right now.
- **GPUs are the new mainframe**: he expects businesses to build software on their own data inside their own firewalls the way software was once built on mainframes — **with less tech debt this time**, because AI can read the COBOL and Fortran nobody understands anymore.
- **Observability**: put audit trails in your workflows and measure even the latency. He recommended **OpenTelemetry** and **OpenLIT**, an open-source SDK with prebuilt instrumentation for vector databases and inference engines that gives you tokens in, tokens out, latency, logs, metrics, and traces.
- **Two tips**: the Minnesota one ("don't eat yellow snow"), and the real one — **never automate a crappy process.** Be honest about whether the process is crunchy and icky; if it is, rebuilding it may save a lot of people a lot of time.

#### Advice by role (~01:46–01:50)

- **Builders**: DM him for the n8n JSON workflow and build guide; import it directly, or hand the JSON to your coding agent and ask it to swap Slack for Teams.
- **Founders**: **the audit trail is the real magic** — seeing how it runs, how long it takes, where it stops, what approvals it needs. "Not the other fluffy stuff — the audit trail itself."
- **Job seekers**: ask these questions *of the interviewer* — what do your operations look like, your approvals, your workflows?
- **Students**: build a portfolio the way a graphic artist carries a sketchbook. "**You're not just hiring me, you're hiring me and my five agents in my portfolio that make your business go faster.**"

### Quotes

> "How many people are building agents? … And then how many people will turn their agents loose on their infrastructure? Some hands went down. We'll talk, you and I." (~01:05–01:06)

Two shows of hands that define the gap the whole workshop addresses.

> "It's not a capabilities problem with AI anymore. It's actually an integration problem." (~01:09)

His core diagnosis of enterprise AI at this stage.

> "The latency is in the stitching between." (~01:14)

Why you start with the flowchart: the bottleneck is in the edges, not the nodes.

> "Reads are free. The writes are gated and somebody needs to approve." (~01:39)

The single most operational rule in the session.

> "It can open tickets. It doesn't get to approve them. Who gets to approve them? You do. There's still governance. There's still accountability." (~01:27)

Structurally identical to Neil Lawrence's and Credo AI's conclusions the same morning, arrived at from the operations side.

> "Never automate a crappy process." (~01:45)

The question to ask before automating anything.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| n8n | 視覺化 workflow 自動化工具,示範的整條 pipeline 都建在上面 | Visual workflow automation tool; the entire demo pipeline is built on it | 講者聲明自己不是 n8n 的付費代言;workflow 本身是 JSON,可 import / 可交給 coding agent 改寫 |
| SUSE Multi-Linux Manager (MLM) | 跨發行版 Linux 管理框架,採 pub/sub 而非 SSH 以利規模化;附 MCP server | Cross-distro Linux management using pub/sub instead of SSH for scale; ships an MCP server | 講者稱有客戶納管 80,000 台不同 Linux |
| SUSE Linux Enterprise + live patching | 不重開機更新 running kernel、OpenSSL、glibc;宣稱可撐一年 | Patch the running kernel, OpenSSL, and glibc without rebooting; claimed to cover up to a year | 主要訴求場景是 SAP 這類不能停機的系統 |
| Rancher Prime / Rancher Desktop | Kubernetes 管理層與桌面版;Rancher Desktop 免費、可在筆電上重現企業體驗 | Kubernetes management layer plus a free desktop edition reproducing the enterprise experience locally | 對照 Docker Desktop |
| Liz | 內建於 Rancher 的 AI 助理,會跟隨你所在 cluster / namespace / workload 的上下文 | Rancher's built-in AI assistant; follows your cluster, namespace, and workload context | 名稱取自 Lizard;講者形容為「用基礎設施來教你用基礎設施」 |
| K3s / RKE2 / Harvester | 單一 binary 的輕量 Kubernetes(K3s 小於 1GB、可跑 Raspberry Pi);Harvester 把 VM 當容器編排 | Lightweight single-binary Kubernetes (K3s under 1GB, runs on a Raspberry Pi); Harvester orchestrates VMs like containers | Harvester 路徑:KVM → libvirt → KubeVirt → Kubernetes |
| SUSE AI Factory | OS + Kubernetes + Rancher + Liz + NVIDIA 元件的整包,支援 GPU 標記與排程、可全 airgap 部署 | Bundle of OS, Kubernetes, Rancher, Liz, and NVIDIA components; GPU tagging and scheduling, fully airgappable | |
| KEV catalog | CISA 的「已知遭利用漏洞」清單,講者主張作為修補優先序的**第一**判準 | CISA's Known Exploited Vulnerabilities catalog; his **first** prioritization criterion | 免費公開資源 |
| EPSS | 漏洞被利用機率的評分系統,優先序的第二判準 | Exploit Prediction Scoring System; his second criterion | 講者在台上把 EPSS 的展開唸錯(見勘誤) |
| CVSS | 漏洞嚴重度評分,講者主張只當 tiebreaker | Severity score; he argues it should only be a tiebreaker | |
| OpenLIT | 開源觀測性 SDK,對向量資料庫與推論引擎預埋 instrumentation | Open-source observability SDK with prebuilt instrumentation for vector DBs and inference engines | 與 OpenTelemetry 並列推薦 |
| *The Road Less Stupid* (Keith Cunningham) | 講者兩度推薦的商業書,主題是「值得花時間思考的事」 | Business book he recommended twice, on what deserves your thinking time | 講者稱作者即 *Rich Dad Poor Dad* 裡的「rich dad」(此說法為講者主張)|

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Zeus / SUSA / Soua / Seuss | SUSE |
| nadn / naden / NAN / NADM | n8n |
| Kev score / Kev catalog | KEV catalog(CISA Known Exploited Vulnerabilities)|
| "EPSS score which is also known vulnerabilities and exploits" | EPSS = Exploit Prediction Scoring System(講者口誤)|
| CBSS | CVSS |
| butterfs | btrfs |
| salsa | SLSA |
| Julia Childs | Julia Child |
| a llama(跑本地模型那段)| Ollama |
| Quen | Qwen |
| celeles for hc | SLES for HPC |
| slurmc | Slurm |
| "that French guy Claude" | Claude(講者玩笑)|

## 待確認 / To Verify

- **mythos moment 的 $20,000 數字**:講者說出自 Anthropic 自己的公告(「約 $20,000 的行動花費找出大量漏洞並串成可利用的 zero-day」),原始出處與確切數字未在台上給出,建議核對公告原文。/ He attributed the ~$20,000 campaign-spend figure to Anthropic's own announcement; the source and exact figure were not cited on stage.
- **"since April 27th or whatever"**:他順口給的 mythos moment 日期,自己也用 "or whatever" 標示不確定。/ He hedged the date himself.
- **本地推論用的模型名稱**:字幕聽成 "Quen 36 35B Jarvis" 與 "GLM52",無法確定是哪個模型與版本;Jarvis 是他自述的個人 side project 名稱。/ Captions render the local models as "Quen 36 35B Jarvis" and "GLM52"; neither model nor version is resolvable. "Jarvis" is his own side project.
- **live patching 機制的正式術語**:他口說的 "repolining"(類比 trampoline)在字幕中無法確認拼法,SUSE 官方文件使用的術語需另行核對。/ The mechanism he called "repolining" could not be resolved from the captions; SUSE's official terminology should be checked.
- **"DX format"**:在 SBOM 段落與 SLSA 並列提及,可能是 SPDX。/ Mentioned alongside SLSA in the SBOM discussion; likely SPDX.
- **Dana 的角色**:逐字稿中 Dana 同時出現在「act one, Dana」(可能是 demo 章節名)與「Dana can ask anything she wants / the CISO can get reports into her Slack」,無法確認 Dana 是否就是那位 CISO 的名字。/ Unclear whether "Dana" is the CISO persona's name or a demo act label.
- **Apple/Broadcom 等業界說法**:講者對 Broadcom 虛擬化定價的批評屬其個人立場,未提供佐證。/ His remarks on Broadcom's virtualization pricing are his own position, offered without evidence.
- **80,000 台 Linux 納管的客戶案例**:未點名客戶。/ The 80,000-host customer was not named.
