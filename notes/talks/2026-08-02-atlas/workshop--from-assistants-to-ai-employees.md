---
title: "From Assistants to AI Employees: Designing Agents That Own a Role, Not a Task"
title_zh: "從助理到 AI 員工:設計「擁有一個角色」而非「擁有一項任務」的 Agent"
speaker: "Anushka Pathak, Soham Shah, Eric Victorson"
affiliation: "Product Manager / ML Engineer / Software Engineer, Ema"
type: workshop
stage: Atlas
date: 2026-08-02
session: "Session 1: Enterprise AI"
video: "https://www.youtube.com/watch?v=LGW_6P1CMC8&t=4377s"
video_range: "01:12:57–02:12:36"
transcript: "tmp/[English (auto-generated)] Atlas Stage - August 2nd - Morning Session [DownSub.com].srt"
status: draft
tags: [ai-employees, enterprise-agents, human-in-the-loop, governance, workshop]
---

# 從助理到 AI 員工(From Assistants to AI Employees: Designing Agents That Own a Role, Not a Task)

**一句話總結**:Assistant 是被動、無狀態、由使用者自己扛治理責任的;Ema 主張把 agent 設計成「AI 員工」——由事件與排程主動觸發、以受限權限直接改寫真實系統狀態、跨天跨系統保有記憶、治理內建——而落地時的瓶頸從來不是 agent 能不能做完整份工作,是**與它協作的人類**。
**One-line summary**: Assistants are reactive, stateless, and leave governance to the user; Ema's argument is to design agents as "AI employees" — triggered by events and schedules, acting on real systems under scoped permissions, holding state across days and systems, with governance built in — and the real blocker in deployment is never whether the agent can do the whole job, it's the humans collaborating with it.

> **現場狀況**:這場排定為 hands-on workshop,但平台登入權限直到接近尾聲(約 02:07)才全數開通。主講人 Anushka Pathak 改以「簡報 + 現場 demo + 長時間 Q&A」進行,實際上超過一半的時間是問答。以下依此忠實記錄。/ **What actually happened**: this was scheduled as a hands-on workshop, but platform access didn't roll out until near the end (~02:07). Anushka Pathak pivoted to slides, a live demo, and an extended Q&A that took up more than half the session.
>
> 台上主講為 Anushka Pathak(Ema 創始產品經理);議程列名的 Soham Shah 與 Eric Victorson 與其他工程/ML 同事在場擔任 TA,未上台講述。/ Anushka Pathak presented throughout; the other listed speakers were in the room as TAs.

## 中文筆記

### 主題一:assistant 與 AI employee 的四個分野(約 01:20–01:24)

她先承認「AI employee」這個詞對某些人有點挑釁——為什麼要把它們放進像人類員工一樣的角色?她的回答是,Ema 在 2023 年就創了這個詞,並把以下四點當作**第一性原則**來設計:

| 面向 | Assistant | AI Employee |
|------|-----------|-------------|
| 觸發方式 | **被動**。需要人類觸發,還要人類自己搞清楚它能做什麼、極限在哪、怎麼跟它協作 | **主動**。由事件、系統變更或排程觸發 |
| 行動能力 | 多半只**建議與草擬**;不碰你碰的系統,也沒有同等存取權——你不會給它初階員工或實習生等級的信任 | 直接**在真實系統上動作**,但帶著受限的權限 |
| 狀態 | **無狀態**。你做完一步,把 artifact 貼到 Slack / Teams,再到會議裡來回——**扛狀態的人是你**,不是它 | 跨步驟、跨系統、跨使用者、跨天,持有**持久狀態**;長工期任務可以「六個月後回來問我」 |
| 治理 | 使用者自己扛。你可能裝了公司不允許的 MCP、裝了有資安問題的 skill——出事是使用者的責任 | **內建**。由資安長設定,系統會在你要越界時擋下你,你甚至不需要知道哪些不被允許 |

她補了一個很生活化的觀察:「我們大概都替自己的 AI 道過歉——『抱歉那是 AI 弄錯的,我應該檢查得更仔細』。」

**一個反直覺的數字**:在 Ema 上,builder 建出來的 AI 員工是 **50% 對話式 / 50% API 觸發**,建置比例剛好一半一半;但**超過 90% 的實際呼叫來自自動觸發**。她的類比是:你不會每次都去戳實習生叫他做事,過一陣子他就自己在做了。

### 主題二:平台架構(約 01:25–01:29)

由下而上:

- **部署層**:multi-cloud 與 on-prem(Azure、GCP 等),支援資料落地(data residency)。
- **LLM 層 — EmaFusion**:她說企業客戶「完全不想碰模型排行榜」,不想每週去判斷哪個模型這週在我的任務上比較好。EmaFusion 承擔選模的責任,依照該 AI 員工正在執行的任務,承諾在**最低成本與延遲下拿到最好的準確度**。
- **Builder 平台**:大量**預訓練的領域專用 agent**(例:資料萃取 agent——從 500 頁、內含矛盾與重複的文件中萃取出去重且準確的結構化資料);**生成式 workflow 引擎**,讓 AI 步驟與**確定性步驟**混用(例如開通新系統存取權這種流程你會希望它是確定性的);而 **Ema Autopilot** 會直接幫你生成那些確定性步驟,你只要檢查輸出——**不需要寫程式**。
- **整合層**:支援 MCP,但她特別說明 **Ema 在 MCP 出現之前就自己做了一套 tool protocol**,更快、更受限、也更好設定,所以兩者都給 builder 選。多數人因為 MCP 現成而從它開始,但你也可以直接帶任何 API 進來——REST、SFTP、SOAP 都行。
- **治理層**:內建。互動介面可以是 dashboard、chat、API、語音,甚至 generative UI。
- **預設套件**:針對 employee experience、sales、customer support 等場景預先組好的 AI 員工套件。

**客戶與規模**:2023 年創立,服務 Fortune 2000 客戶,主要自動化 HR、IT、財務等角色;數千個 AI 員工在生產環境運行,數百位外部 builder 在上面開發。**100% 的 AI 員工都會改寫真實系統的狀態**——他們基本沒有「幫我擬一封信然後我自己複製貼上」這種用例。許多公司把 Ema 當**單一操作面板(single pane of glass)**,不用開十個分頁;而那個面板可以就是 Slack 或 Teams,因為它是員工,你在哪就在哪跟它講話。

**具名案例**:Wipro(全球 24 萬名員工,用於員工體驗問答)、Artico(美國頂尖高階獵才公司之一,**time-to-hire 縮短 67%**)、Prime Therapeutics(醫療,背景處理數以千計的 prior authorization)、Hospital for Special Surgery(紐約,病患預約排程)。

### 主題三:建一個 AI 員工的建議流程(約 01:32–01:37)

Ema 有三種 builder:自家 builder 團隊(尤其服務極不技術的客戶,如醫療客戶)、合作夥伴(Wipro、KPMG 等訓練出來的 builder),以及**客戶自己用 Autopilot 建**。三種情況他們都建議走同一套 scoping:

1. **探索與界定**:這個角色實際上需要什麼?把工作**拆解成任務**,再逐一判斷哪些用 AI 做、哪些用確定性流程做、哪些**還是留給人類**。她特別點名一個常見失敗:拿到用例卻**沒有真實的測試資料集**,結果 builder 一邊做一邊自己編測試資料,而他其實不懂那個業務流程。**一定要拿到過去的實際案例。**
2. **整合**:生產用例**一律優先直接用 API**;要用 MCP 也行,但會稍慢、吃掉更多 context,因此也更貴;兩者都沒有的系統才退到 **browser use**;再加上 retrieval 補 context。然後把工作**拆成較小的 agent**,好評估、好維護,也才能把維護責任分派給公司裡不同團隊。
3. **Human-in-the-loop 檢查點**:在受監管產業比較單純,因為有些決策 AI 就是不能做(**臨床決策、下單這類金融市場決策**)。但即使在其他場景,也要找出**人類判斷是關鍵**的位置——例如招募,「你絕對不會想讓 agent 端到端把人招完」。她給了一條很實用的設計原則:**把人類的邊界放在最後那個「改變狀態」的 act 步驟,不要放在 think 步驟**——讓 AI 員工把所有事情都做到人類必須動手的那一刻為止,人類看著它的筆記再決定要不要執行。
4. **訓練 agent 主動求助**:讓它在自己困惑時主動發出 human-in-the-loop 請求。

### 主題四:現場 demo(約 01:37–01:47)

她原本要帶大家建三個 AI 員工:**sourcing**(用 Apollo 搜尋真實候選人)、**screening**(示範 human-in-the-loop:入選之後要先有人類核可才發出),以及一個 **orchestrator**——因為「如果你有 100 個 AI 員工,你不會希望人類得記住哪個員工做什麼、該去找誰。**沒有人想在腦袋裡處理 routing。**」招募人員只跟這一個 orchestrator 對話。

Demo 中值得記下的幾點:

- 她把整段需求貼進 **Ema Autopilot**,批准計畫後,它就自己去建整合、建 AI 員工、產生測試用 CV 與職缺描述,並自行建立 eval 資料集。Autopilot 本身是一個 harness,握有橫跨 Ema 產品基礎設施(治理層、builder 層、UI 層)的數百個工具,也支援自帶工具與 skills——所以 KPMG 這類公司會把自己數十年的財務知識帶進來,agentic 平台的知識則由 Ema 提供。
- **失敗會被學起來**:自我修正的結果會先為該使用者保留,再擴散到整間公司。她說這對留存率影響很大,尤其是自帶工具的情況——「四五個人用過之後,接下來一百個人就會很順」。
- **API key 是刻意做不到的事**:你**無法**把 API key 貼給 Autopilot 讓它去接。他們在來源端就做 PII 與敏感資料**混淆(obfuscation)**,你一貼進聊天就被混淆掉,下游系統拿到的是混淆後的值。她刻意對比:「不像很多 harness,你把 API key 貼進去它就真的能端到端跑起來。」
- 三種 AI 員工形態:chat、**dashboard**(可由 app、API 或排程觸發——就是那 90% 呼叫的來源)、以及 orchestrator。Demo 中的 screening 員工正**停在人類審核的狀態**,審完才會往下跑出 fit score 與信件。

### 主題五:Q&A(約 01:48–02:12)

這場問答的密度高於前面的簡報,以下依主題整理。

**定價(約 01:48、02:10)** — 使用量與**成效**併用。多數 AI 員工是**賣成效**:每一份 sales proposal、每一張客服工單、每一則員工體驗詢問。**與 token 數無關,不是成本加成定價**,而是「這份工作你本來要付一個人多少錢、我們讓他快多少」。所以不同工作的單價差很多,計費指標可高度客製,與客戶一起訂。另一種是純使用量:客戶買一百萬點數,自己愛建什麼建什麼。

**ROI 怎麼量(約 01:50)** — 成本中心的用例很直接:人時減少、原本做這件事的人投入減少。生產力型的用例則從**預測**開始:她舉 2024 年的例子,當時預測一年內會快 15%,結果做了研究後發現**兩個月內就快了 3 倍**,而且對象是在該職位資歷十年的人。另外要看產出面——同樣人數要能多做 20% 的 sales proposal。

**流程會變,怎麼跟上(約 01:51)** — 分兩種:
- **可預期的大改動**:例如 prior authorization 的臨床政策每年更新、有明確發布日。這類基本自助——找 Autopilot 談,Ema 有**版本控制**,跑完 eval 再推出去。
- **無法預期的真實世界漂移**:例如客戶最近兩週開始問新類型的問題。Ema 會**掃過 audit log** 找出改善機會,Autopilot 提出建議修改,並附上**證明有改善、且不會讓既有用例退步的 eval 資料**,最後由人類簽核部署。兩者都是自動化流程。

**能不能進 Zoom / Teams 會議即時互動(約 01:53)** — **還沒做過即時通話**。他們做的是**會後**用逐字稿處理;這個用例目前還沒有客戶提出。

**控制的顆粒度 / 每個 agent 的 reward function(約 01:53–01:55)** — 她認同「人們想要控制到最細的一步」,而這正是**為什麼要有多個 AI 員工、而不是一個包辦全企業的通用 agent**。每個 AI 員工通常由不同的人負責,角色也分開(builder、admin、reviewer、onboarder),權限反映在系統裡。Eval 可以跑在**AI 員工層級**;不需要技術背景,你的控制手段就是把用例講清楚——業務使用者可以很不技術地做(「把去年的工單拿來,我要求在這些工單上至少達到這個表現」),技術型使用者則可以自己帶 eval bed。而在 AI 員工**內部**,有些是自由形式、沒有 workflow,有些切成較小的 block,**同一套 eval 可以跑在 block 層級**——例如只量測、只改善「這個 AI 員工跟 Apollo 這一層」的準確度。

**能不能接進 Slack / Teams(約 01:55)** — 可以,而且很多人就是這樣用。Wipro 用 Teams,也有客戶用 SDK 做成內部網站上的浮動圖示。三者都是 channel;現在**非技術人員也能自己設定,大約十分鐘**。

**為什麼是 multi-cloud(約 01:56)** — 因為金融、醫療這類敏感客戶要求**on-prem**,要部署在他們原本就在的地方,而且要**air-gapped**——Ema 不能對外連任何系統,包括網路與任何外部 API。客戶可能在 GCP 也可能在 Azure,所以他們**從第一天就是 multi-cloud**。也有數十家客戶用 SaaS,那些客戶「就像自己開通 Notion 一樣」不在意部署形態。

**agent 能不能替使用者強制執行資料的 RBAC(約 01:57)** — 可以。整合有兩種連線型態:**shared service auth**(誰問都一樣的存取權),以及多數用例應該採用的 **user-level auth**——你第一次問到需要呼叫某系統(例如 ServiceNow)的問題時,它會要你先登入,之後所有答案都用**你的**憑證取得。這不只限制你能拿到什麼資訊,還讓**下游系統本身也留下 audit log**:某某人要求了這項資訊,因此該資訊經由 Ema agent 提供給她。

**規模上限與工期(約 01:58)** — 單一租戶、單一客戶部署裡她親眼看過 **300、400 個** AI 員工。但她強調**把它們拆開是符合各方利益的**——回到「誰維護、誰負責它持續正常運作並跟上流程」的問題。拆開換來更好的治理與管理。工期方面,有些 workflow **跑好幾天**,例如一筆新供應商採購可能有十道核可——但**卡住的是等人類核可,agent 本身很快**;其他用例則快得多。(成本數字她表示不便透露。)

**怎麼讓 AI 員工「主動」(約 02:00)** — 她現場開了一個測試租戶示範,同時強調「其實沒人在看這些畫面,大家都只跟 Autopilot 講話,這就像在看程式碼」。支援的觸發包括:**webhook**、讓 AI 員工**輪詢**你的系統、直接接系統並設條件(「Salesforce 有新 lead 進來時,去判斷他是不是好人選」)、**監看收件匣**、**排程**(「每天早上寄一封做 X 的信給我」)。設定方式就是寫一句話。

**重複性高的任務會不會一直燒 token,有沒有預建的程式碼 recipe(約 02:01)** — 有,程式碼可以直接作為 workflow 的一部分。但她給的建議路徑更有意思:**不要花幾個月去預先設計**。你可以從一個**空的租戶、零個 AI 員工**開始,每件事都先跟 Autopilot 做;當它發現什麼是重複的,就開始**把那些東西固化下來**——依據真實使用與回饋,建出 agentic 的 AI 員工,或**直接寫成程式碼並維護它**。

**這到底是「整個業務流程外包」還是「任務級自動化」(約 02:02)** — 提問者指出定位講的是 AI 員工(暗示整個流程被外包),但舉的例子多半偏任務。她的回答:**每一個合約與專案的終局都是角色導向的**——最後會收斂成一個你可以對話的介面、或一個自動化,能跨所有任務把整份工作做完。但**採用會慢一點**:你可以建出端到端的 AI 員工,**而阻礙永遠是與它協作的人類**。所以實務上是一個任務一個任務上線——先 sourcing,再篩 CV,再排面試,再到錄取後的 onboarding、offer letter——讓招募團隊慢慢暖身、學會怎麼跟 AI agent 協作。**從一個任務開始,再擴張到那個角色的全貌。**

**人與 AI 員工的比例(約 02:04)** — 在 Ema 上建 AI 員工又便宜又容易,而且**只有在真的產生價值時才計費**,所以很多人會建一堆自動化。但因為 Ema 只服務超大型公司,比例通常是:**200 人的招募團隊,大概只需要 20 個 AI 員工**——**每個 AI 員工的使用強度極高,一天數千次呼叫**。她強調他們**不以 agent 數量為優化目標**。

**拿下 GM 或美國銀行這種大案子之後,實務上怎麼跑(約 02:05)** — 由 Ema 或合作夥伴中那位「agentic 轉型專家」負責讓 AI 員工首次上線並運作良好。這是一個**深度探索**流程:不只跟採購方與團隊主管開 workshop,而是**坐進房間裡、跟著實際做這份工作的人 shadow 數小時甚至數天**,並翻閱他們過去一年的所有工作案例,然後才寫出定義。**流程一旦定義清楚,剩下的就不多了——丟進 Ema Autopilot,幾小時就建好也測好。** 她的結論很值得記:「**你不需要懂 Ema 才能在 Ema 上做出有影響力的東西。你需要的是非常懂那個業務流程。**」也因為如此,很多客戶接著就想自己來:「反正你也是丟進 Autopilot,那我自己來就好,我才是這個招募流程的專家。」

**員工的抗拒怎麼處理(約 02:06)** — 她認為這種抗拒在**兩三年前常見得多**——當時的反應是「為什麼要我評估 AI 的樣本,這不是會影響我自己的飯碗嗎?」。最近兩年變化很大:大家意識到**要保持在職位與產業的頂端就得更快、且具備 AI 能力**,採用 AI 反而讓自己更不可取代、把工作做得更好。現在他們看到的是**熱情**——人們想成為訓練它的那個人、想理解它怎麼運作。她把這稱為 **citizen developers 的崛起**:一輩子沒寫過一行程式,卻真心想把 AI 帶進自己的工作。

**skills 和 AI employee 差在哪(約 02:11,最後一題)** — **skill 是威力較小的 AI 員工版本**,平台上也支援。skill 的好處是他們有一個**模板市集**,方便把東西分享給公司內對的人(AI 員工也適用)。但 AI 員工複雜得多:**有自己的記憶、有確定性與 agentic 混合的步驟、而且針對該用例被嚴格評估**。真正要把東西上線的人通常想要完整的那些頁籤——多少人用過、哪裡出錯、哪裡可以改善、我要自動改善的協助。所以**雖然 skills 存在,多數人還是直接用 AI 員工**。

### 金句

> "You have to be a little scared — you have to govern everything yourself. … And I think we've all apologized for our AI's errors at times."(約 01:21)

Assistant 模式下,治理責任其實落在使用者身上——這是 AI employee 這個設計的出發點。

> "You put a human boundary at the final act step where you're changing the state, and you don't do it at the think step."(約 01:36)

整場最實用的一條 human-in-the-loop 設計原則。

> "You don't have to know about Ema to launch impactful stuff in Ema. You have to know a lot about the business process. That's the expertise you need."(約 02:06)

她對「導入的瓶頸在哪」的完整回答。

> "You can build an AI employee that does everything end to end, but the blocker is always the humans that are collaborating with that AI employee."(約 02:03)

也是整場最誠實的一句:限制不在 agent 的能力,在組織的節奏。

## English Notes

### Theme 1: Four things that separate assistants from AI employees (~01:20–01:24)

She opens by acknowledging that "AI employee" can be a provoking term — why put these things into roles like human employees? Ema coined it back in 2023 and designed against these four first principles:

| Dimension | Assistant | AI Employee |
|-----------|-----------|-------------|
| Triggering | **Reactive**. Needs a human to trigger it, and needs the human to work out what it can do, where its limits are, and how to work with it | **Proactive**. Triggered by events, system changes, or schedules |
| Action | Mostly **suggests and drafts**; often doesn't touch the same systems you do and doesn't have the same access — you wouldn't trust it in the seat you'd trust a junior employee or intern with | **Acts on real systems** directly, under scoped permissions |
| State | **Stateless**. You finish a step, share an artifact into Slack or Teams, go back and forth in meetings — **you** are the one holding state, not the assistant | Holds **persistent state** across steps, systems, users, and days; "come back and ask me about this in 6 months" should work |
| Governance | Yours to carry. You might install an MCP your company doesn't allow, or a skill with security issues — accountability sits with the user | **Built in**. Your chief security officer sets it up and the system stops you before you breach something — you shouldn't even need to know what isn't allowed |

Her aside lands well: "I think we've all apologized for our AI's errors at times — I'm sorry, that was an AI error, I should have checked that better."

**One counter-intuitive statistic**: on Ema, builders build roughly **50% conversational and 50% API-triggered** AI employees — an even split by construction. But **more than 90% of actual invocations are automated**. Her analogy: you don't ping a junior employee or intern every time; after a point they're just doing things, getting progressively more autonomous.

### Theme 2: Platform architecture (~01:25–01:29)

Bottom to top:

- **Deployment**: multi-cloud and on-prem (Azure, GCP, and others), with data residency.
- **LLM layer — EmaFusion**: none of their enterprise customers want to deal with model leaderboards or re-decide weekly which model is doing well on a task they care about. EmaFusion takes ownership of keeping the latest models available and, depending on the task the AI employee is performing, promises the **best accuracy at the lowest cost and latency**.
- **Builder platform**: a library of **pre-trained domain-specific agents** — for instance a data-extraction agent for pulling deduplicated, accurate structured data out of a 500-page document containing contradictions and duplications. A **generative workflow engine** lets you compose those agents alongside **deterministic steps**, because sometimes you don't want AI (granting someone access to a new system should follow a fixed sequence). And **Ema Autopilot** generates those deterministic steps for you — you just check the outputs, so **no coding required**.
- **Integration layer**: MCP is supported, but she notes Ema **built its own tool protocol before MCP existed** — faster, more constrained, simpler to set up — so builders get the choice. Most start with MCP because it's already there, but you can bring any API: REST, SFTP, SOAP, whatever.
- **Governance**: built in. Interaction happens through dashboards, chat, APIs, voice, or generative UI.
- **Pre-configured suites** across all these layers for employee experience, sales, and customer support.

**Customers and scale**: founded 2023, serving Fortune 2000 clients, mostly automating HR, IT, and finance roles end-to-end. Thousands of AI employees in production and hundreds of external builders. **100% of their AI employees change state in real systems** — they essentially don't have "draft me an email and I'll copy it over myself" use cases. Many companies use Ema as a **single pane of glass** rather than opening ten tabs, and that pane can be Slack or Teams, because it's an employee and you talk to it where you already are.

**Named cases**: Wipro (live with 240,000 employees globally for employee-experience questions), Artico (a top US executive search firm; **67% reduction in time-to-hire**), Prime Therapeutics (healthcare; thousands of prior authorizations processed in the background), and Hospital for Special Surgery in NYC (patient appointment scheduling).

### Theme 3: Their recommended process for building an AI employee (~01:32–01:37)

Ema has three kinds of builders: their own builder team (especially for very non-technical clients like healthcare), partners such as Wipro and KPMG whose builders are trained on Ema and take use cases to market, and customers building for themselves with Autopilot. All three are advised to run the same scoping:

1. **Discover and scope.** What does the role actually require? Decompose the job into tasks and decide which to do with AI, which deterministically, and which to **keep with a human**. She calls out a recurring failure: getting a use case **without an actual test dataset**, so the builder invents test data as they go — while not understanding the business process. Get past examples.
2. **Integrations.** For production use cases they always recommend **using the APIs directly**. MCPs work but are slower and consume more context, hence more expensive. Systems with neither fall back to **browser use**, plus retrieval to improve context. Then break the work into **smaller agents** so they're easier to evaluate and maintain, and so maintenance can be delegated to different teams.
3. **Human-in-the-loop checkpoints.** Easier in regulated industries, because some decisions AI simply cannot make — **clinical decisions, or financial market decisions like placing an order**. But even elsewhere, find where human judgment is key: in recruiting, "you do not want agents to be recruiting end to end." Her design rule is the sharpest thing in this section: **put the human boundary at the final act step where state changes, not at the think step** — let the AI employee do everything up to the point where a human has to act, so they can read its notes and decide.
4. **Train the agent to ask.** Teach it to proactively raise human-in-the-loop requests when it's confused.

### Theme 4: The live demo (~01:37–01:47)

The plan was three AI employees: **sourcing** (searching real candidates via Apollo), **screening** (to demonstrate human-in-the-loop — after shortlisting someone, a human approves before anything is sent), and an **orchestrator**, because "if you have 100 AI employees, you don't want humans remembering what each one does or whom to go talk to. **Nobody wants to deal with routing in their heads.**" A recruiter or hiring manager talks to one point of contact.

Worth recording from the demo:

- She pasted the whole requirement into **Ema Autopilot**, approved the plan, and it built the integration, the AI employees, generated test CVs and job descriptions, and produced an eval dataset on its own. Autopilot is a harness with hundreds of tools spanning Ema's product infrastructure — governance, builder, and UI layers — and it accepts your own tools and skills, which is how a firm like KPMG brings decades of finance knowledge while the agentic platform knowledge comes from Ema.
- **Failures get learned.** Self-correction is retained first for that user and then across the whole company. She says this noticeably improves stickiness over a few months, especially with customer-supplied tools: agents may not know how to use them at first, but "four or five people use it, and for the next hundred people it's going to work well."
- **Pasting an API key is deliberately impossible.** You cannot hand Autopilot a key and have it wire things up. They do **PII and sensitive-data obfuscation at source** — the moment you put it in the chat it's obfuscated, and that's what flows downstream. She contrasts this explicitly with "a lot of other harnesses where people just paste API keys and that actually works end to end."
- Three shapes of AI employee: chat; **dashboard** employees invokable via apps, APIs, or schedules (the source of that 90% of invocations); and the orchestrator. The screening employee in the demo sat **paused for human review**, releasing fit scores and the drafted email only after sign-off.

### Theme 5: Q&A (~01:48–02:12)

The Q&A was denser than the presentation. By topic:

**Pricing (~01:48, ~02:10).** Usage- and **outcome**-based. For many AI employees they're selling outcomes: per sales proposal, per customer support ticket, per employee-experience query. It **does not depend on tokens and isn't cost-based pricing** — it's about what you would pay a person in that job and how much faster you're making them, so different jobs cost very differently. Billing metrics are highly configurable and instrumented in tandem with the customer. The alternative is straight usage: someone buys a million credits and builds whatever they want.

**Measuring ROI (~01:50).** For cost-center use cases it's straightforward — fewer hours and less involvement from the humans who used to do the task. For productivity cases they start with a prediction: in 2024 the prediction was 15% faster over the course of the year; studies a couple of months in found people were **3x faster**, even those tenured ten years in the role. You also look at the outcome — 20% more sales proposals with the same headcount.

**Processes that change over time (~01:51).** Two kinds. **Predictable large changes** — prior-authorization clinical policies change annually with a publish date — are fairly self-serve: talk to Autopilot, use Ema's versioning, run your evals, push. **Unpredictable real-world drift** — customers started asking new kinds of questions in the last couple of weeks — is caught by Ema scanning **audit logs** to identify improvement opportunities; Autopilot recommends changes **with eval data showing it's actually better and won't regress past use cases**, and a human signs off on deployment. Both are automated processes.

**Live Zoom/Teams call integration (~01:53).** They **haven't done live call tracking**. They process transcripts right after the call; the use case hasn't come up for them yet.

**Granularity of control / reward functions per agent (~01:53–01:55).** She agrees people want control at the most granular step, and says that's precisely **why you have AI employees rather than one universal agent doing everything**. Each AI employee usually has a different person managing and training it, with distinct roles — builder, admin, reviewer, onboarder — and those permissions are reflected in the system. Evals run at the **AI-employee level**, and you don't have to be technical: your control surface is specifying the use case. Business users do this non-technically ("here are last year's tickets, I want at least this performance across them"); technical users bring eval beds. Within an AI employee, some are free-form with no workflow, while others break into smaller blocks — and **the same evals can run at block level**, e.g. measuring and improving only how well the AI employee works with Apollo.

**Slack / Teams (~01:55).** Yes, and it's how many customers use them. Wipro uses Teams; another customer embeds an SDK as a floating icon on an internal website. All three are channels, and **non-technical people can now set this up in about ten minutes**.

**Why multi-cloud (~01:56).** Sensitive finance and healthcare customers want **on-prem**, deployed where they already are, and **air-gapped** — Ema cannot talk to any system including the web or any external API. Customers sit on GCP or Azure, so they were **multi-cloud from day one**. Dozens of customers are on SaaS and genuinely don't care: "it's like setting up Notion for yourself."

**Enforcing data RBAC for the asking employee (~01:57).** Yes. Integrations support two connection types: **shared service auth**, where access is identical regardless of who asks; and **user-level auth**, which most use cases should use. The first time you ask something requiring a call into, say, ServiceNow, it asks you to log in, and from then on answers come back under **your** credentials. That restricts what information you get *and* leaves an **audit log in the downstream system**: this person requested this information, and it was served to them via an Ema agent.

**Largest scale and workflow duration (~01:58).** She has personally seen **300–400** AI employees in a single tenant in a single customer deployment. But she stresses it's in people's interest to break them up — back to who maintains this, who's responsible for it staying up to date and following the process. Breaking them apart buys better governance and management. Some workflows run **multiple days**: a new vendor procurement might carry ten approvals — but **the agent is quick; you're stuck waiting on the humans doing the approvals**. Other use cases are much faster. (She declined to share cost figures.)

**How do you make an AI employee proactive (~02:00).** She opened a test tenant to show it, while noting "nobody actually looks at these screens — you just talk to Autopilot; this is like looking at the code." Supported triggers: **webhooks**, having AI employees **poll** your systems, connecting directly to systems with conditions ("when there's a new lead added to Salesforce, go figure out if they're a good candidate for us"), **monitoring inboxes**, and **schedules** ("every morning I want an email that does X"). Setting each up is as simple as sending a sentence.

**Repetitive work and pre-built code recipes (~02:01).** Yes — code can be represented as part of workflows. But her recommended path is more interesting: **don't spend months setting this up**. Start with an empty tenant and zero AI employees, working with Autopilot for every task; as it figures out what's repetitive, it **starts codifying** — building agentic AI employees or writing and maintaining straight code, based on real usage and feedback.

**Task automation or true business-process outsourcing (~02:02).** The questioner noted the positioning implies whole-process outsourcing while the examples look task-oriented. Her answer: **the end state for every contract and project is role-focused** — it lands on a single interface you can talk to, or a single automation, that does the entire job across all the tasks. But **adoption starts slower**: you *can* build an AI employee that does everything end to end, and **the blocker is always the humans collaborating with it**. So in practice they launch task by task — sourcing, then screening CVs, then scheduling interviews, then onboarding the candidates you liked and managing the offer letter — which helps the recruiting team warm up and learn to work with AI agents. Start with a task, expand to the full gamut of the role.

**Human-to-AI-employee ratio (~02:04).** Creating AI employees on Ema is easy and cheap, and **you're only charged when you're actually getting value**, so people create plenty of automations. But Ema works only with very large companies, so the ratio skews: a **200-person recruiting team might need about 20 AI employees**, with very high usage each — thousands of invocations per day. They **don't optimize for number of agents**.

**How a big GM- or Bank-of-America-scale deal actually runs (~02:05).** Either someone at Ema or a partner acts as the agentic transformation expert responsible for the AI employees working well and launching the first time. That's a deep discovery process: not just workshops with the buyer and team lead, but **sitting in the room with the person doing the job and shadowing them for hours and days**, plus reviewing all their past work examples from the last year, before writing the definition. **Once the process is well defined, there isn't much left — throw it into Ema Autopilot and in a few hours it's built and tested.** Her conclusion is the line worth keeping: "**You don't have to know about Ema to launch impactful stuff in Ema. You have to know a lot about the business process. That's the expertise you need.**" Which is also why many customers then want to build themselves: if you're just going to put it in Autopilot, I can do that — I'm the expert on this recruiting process.

**Employee resistance (~02:06).** She says that resistance was much more common two or three years ago — "why do you want me to evaluate AI samples when this will probably affect my own role?" That has changed a lot in the last couple of years: everyone has realized you need to be faster and AI-equipped to stay at the top of your job and your industry, and that adopting AI makes you more valuable and better at the work. Now they see excitement — people want to be the ones training it and to understand how it works. She calls this the **rise of citizen developers**: people who have never written a line of code and want to bring AI into their jobs.

**Skills versus AI employees (~02:11, final question).** A skill is **a less powerful version of an AI employee**, and the platform supports them. Their benefit is a strong **template marketplace** making it easy to share things with the right people inside your own company — which works for AI employees too. But AI employees are much more complex: they have **their own memory**, mix deterministic and agentic steps, and are **evaluated very specifically for their use case**. Most people taking something live want all those tabs — how many people used it, where it went wrong, where it can improve, automated improvement help. So although skills exist, **most people prefer using AI employees directly**.

### Quotes

> "You have to be a little scared — you have to govern everything yourself. … And I think we've all apologized for our AI's errors at times." (~01:21)

Under the assistant model, governance accountability quietly lands on the user — the starting point for the whole AI-employee design.

> "You put a human boundary at the final act step where you're changing the state, and you don't do it at the think step." (~01:36)

The most portable human-in-the-loop design rule in the session.

> "You don't have to know about Ema to launch impactful stuff in Ema. You have to know a lot about the business process. That's the expertise you need." (~02:06)

Her complete answer to where the deployment bottleneck sits.

> "You can build an AI employee that does everything end to end, but the blocker is always the humans that are collaborating with that AI employee." (~02:03)

The most candid line of the session: the constraint isn't agent capability, it's organizational pace.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Ema | 2023 年創立於 Mountain View 的企業 AI 員工平台,服務 Fortune 2000 | Enterprise AI-employee platform founded 2023 in Mountain View, serving Fortune 2000 clients | 官方拼法為 Ema(字幕作 "Emma") |
| EmaFusion | 模型融合層,依任務自動選模,承諾最低成本延遲下的最佳準確度 | Model-fusion layer that routes per task for best accuracy at lowest cost and latency | 讓客戶不必追模型排行榜 |
| Ema Autopilot | 會建置、管理、除錯、測試、維護其他 AI 員工的 AI 員工;自然語言即可建置 | An AI employee that builds, manages, debugs, tests, and maintains the other AI employees | demo 主軸 / the demo's centerpiece |
| Ema 自有 tool protocol | 早於 MCP 開發,更快、更受限、更易設定;與 MCP 並存供選擇 | Built before MCP; faster, more constrained, simpler to set up; offered alongside MCP | |
| Apollo | Workshop 中用來做候選人 sourcing 的外部資料來源 | External people-data source used for candidate sourcing in the workshop | apollo.io;現場提供共用測試 API key |
| Wipro | 全球 24 萬名員工上線,用於員工體驗;同時也是 Ema 的 builder 夥伴 | Live with 240,000 employees for employee experience; also a builder partner | 字幕作 "Vipro" |
| Artico Search | 美國頂尖高階獵才公司,time-to-hire 縮短 67% | Top US executive search firm; 67% reduction in time-to-hire | 官方案例另記 30% 成本下降 |
| Prime Therapeutics | 醫療客戶,背景批次處理 prior authorization | Healthcare customer; prior-authorization processing in the background | |
| Hospital for Special Surgery (HSS) | 紐約醫院,病患預約排程 | NYC hospital; patient appointment scheduling | 字幕作 "hospital of special surgery" |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Emma / MMA / MI / MR / M / MI agent | Ema / Ema agent |
| Emma Fusion | EmaFusion |
| Emma Autopilot / Ma Autopilot | Ema Autopilot |
| Aneska / Anushka | Anushka Pathak |
| Vipro | Wipro |
| Artico | Artico Search |
| hospital of special surgery | Hospital for Special Surgery (HSS) |
| app.mr.ai | app.ema.ai |
| Zelerback Hall / Zelerbach Mezzanine | Zellerbach Hall / Zellerbach Mezzanine |
| obiscation / offiscated | obfuscation / obfuscated |
| SAS deployment | SaaS deployment |
| ourback | RBAC |
| service o / user level o | service auth / user-level auth |
| EI employees | AI employees |
| eva / evas | evals |
| Ghat(客戶名) | 待確認 / to verify |

## 待確認 / To Verify

- 講者提到預設套件「come pre-built with like 500,000 AI employees」——這個數字在脈絡下明顯異常(可能是 500 或 50,000,或是口誤),需看投影片確認。/ The "500,000 AI employees" figure for pre-configured suites is implausible in context; needs slide confirmation.
- 她提到的 assistant 使用情境「things like claude co-work」——正確產品名稱待確認。/ The product heard as "claude co-work" needs its correct name confirmed.
- 使用 SDK 浮動圖示的客戶名稱(字幕聽作 "Ghat")。/ The customer name heard as "Ghat" that embeds Ema as a floating SDK icon.
- 議程列名的 Soham Shah 與 Eric Victorson 在錄影中未上台講述(Eric 開場時尚未到場),僅 Anushka Pathak 主講;若需個別歸屬需另行查證。/ Soham Shah and Eric Victorson never presented on the recording (Eric hadn't arrived at the start); only Anushka Pathak spoke.
- 「我們在 MCP 出現前就做了自己的 tool protocol」——該協定未公開命名。/ Ema's pre-MCP tool protocol was not named.
- Ema 免費 self-serve 試用「本月底開放」的確切日期與現況。/ The exact date and current status of the free self-serve trial she said would open at the end of the month.
