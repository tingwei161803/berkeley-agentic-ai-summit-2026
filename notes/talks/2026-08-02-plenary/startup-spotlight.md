---
title: "Startup Spotlight"
title_zh: "新創聚光燈"
speaker: "Startup Spotlight"
affiliation: "Featured Startups: Narada AI, cognee, Nimblemind, AgntID, RELAI, Headroom, Founding Dev, ArmorIQ, Keenable AI, H Company, Ludo Robotics, Nimble"
type: misc
stage: Plenary
date: 2026-08-02
session: "Startup Spotlight"
video: "https://www.youtube.com/watch?v=I2PosBXwoPI&t=10793s"
video_range: "02:59:53–04:12:52"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [startups, demo, infrastructure, agent-security, memory]
---

# 新創聚光燈(Startup Spotlight)

**一句話總結**:12 家 agentic AI 新創的收官場,主題分布本身就是一張生態系地圖——**記憶與 context 的效率**(cognee、Headroom)、**執行期治理**(AgntID、ArmorIQ)、**agent 的持續學習與驗證**(RELAI、Nimble)、以及**繞過 API 直接操作既有介面**(Narada、H Company)。
**One-line summary**: The summit's closing session — 12 agentic AI startups whose topic distribution is itself an ecosystem map: memory and context efficiency (cognee, Headroom), runtime governance (AgntID, ArmorIQ), continual learning and verification (RELAI, Nimble), and driving existing interfaces directly instead of waiting for APIs (Narada, H Company).

## 中文筆記

### TL;DR

- Berkeley RDI 把「社群與創業」列為三大核心支柱之一。今年春天成立了 **Berkeley Xcelerator** 春季梯次,收了 **8 家**橫跨 agentic AI 全端的早期公司;這場再加上業界的 **4 家**早期公司,共 12 家上台。
- **最擁擠的兩個賽道是 context 與 access control**:cognee 與 Headroom 都在賣「別再把垃圾塞進 context window」;AgntID 與 ArmorIQ 則不約而同地主張**驗證通過不等於行為對齊**,要在執行期比對「agent 的意圖 / 計畫」與「它實際要做的動作」。
- **OpenAI / Hugging Face 事件被至少兩家新創直接拿來當市場論據**(AgntID、以及 developer platforms 座談的延伸討論),顯示這件事已經變成 agent 安全類產品的共同錨點。
- **「不必等 API」是另一條主線**:Narada AI 與 H Company 都主張企業工作流碎片化是設計使然,與其等每個流程都被 API 化,不如讓 agent 直接從前端操作既有介面(含 legacy 綠屏、Citrix、遠端桌面)。
- 收尾後還有 MLK 大樓的海報場次與 reception。

### 12 家新創

#### 1. Narada AI(約 03:01:32–03:10:30)

**Dave Park**(CEO 暨共同創辦人;Stanford CS 博士期間創辦第一家公司 Coverity)介紹一個**專為企業應用與工作流打造的 agentic 自動化平台**。核心論點:HR、IT、財務裡還手動的多半不是 copilot 型小任務,而是 **ERP 測試、跨資料孤島的資料驗證與對帳、訂單/發票/帳單對帳**這類長程流程;因為很多步驟沒有 API,只能透過 UI 視覺推理再點擊、輸入、捲動,而傳統腳本與 bot 一遇介面變動就壞,通用模型則在雜亂的生產環境中(登入問題、斷線、逾時、設定變更、CRM 重複紀錄)遲早幻覺。

他們的三個做法:(1) 用專有技術**自動測繪客戶的應用與介面設定**,只憑自然語言流程描述或螢幕錄影就動態生成貼合該環境的 agent;(2) 把「agent 為何與在哪裡失敗」的學習轉成**策展過的測試環境與合成資料**,訓練能從真實例外中復原的 harness;(3) 用他們主導的 **LLM Compiler** 規劃與執行框架,把長程任務拆成細顆粒步驟,每一步都有單元測試、例外處理、guardrail 與 self-healing。同一套測繪機制也用來**優化高流量工作負載**:路徑學會之後,後續數千筆訂單或帳單能以更少算力、更快更準地跑完。團隊有 UC Berkeley 的 **Kurt Keutzer** 與 **Amir Gholami**(在 UC Berkeley AI lab 主導 Narada 背後的研究)。案例:跨 23 國比對競品車型選配與定價(數百步);一位客戶有 **4,000 個沒有 API 的帳單入口網站**。提供數天內完成的免費 PoC。

#### 2. cognee(約 03:10:39–03:15:55)

創辦人 **Vasilije**(自稱 Vess,從柏林飛來)講的是**開源 AI memory 層**。他把問題定義成「**能不能在任何 harness、任何模型上加一個 self-improvement 迴圈,而不必 token maxing**」——而且這**不是 agent 問題,是資料問題**:agent 產生的資料量是人類的 100 倍,同時企業還有 CRM 與資料孤島要接進來一起推理。

cognee 坐在你的資料與 agentic workflow 之間,把資料**攝取、結構化、處理成 graph 與 vector 的組合表示**,他形容像千層麵——一層層疊上意義、互相交叉連結、持續演化。要處理的性質包括:版本、時間性、不同 agent 帶著不同記憶的並發讀寫、衝突解決、時間戳、以及「某個當下這句話指的是什麼」的後設表示。他用代名詞消解舉例(「他」在不同日子指不同人),延伸到 revenue、財政年度這類業務名詞的定義歧異。技術上跑在 Postgres 上,每個 agent / team / tenant 都能有自己的資料庫,開源版即支援;有 Claude Code plugin、API 與 CLI,並有 Rust、TypeScript、Java 版本。數據:年初至今 GitHub star 從約 1 萬成長到 **3 萬**,SDK 每月約 800 萬次執行、上月約 17–18 萬次下載;在記憶 benchmark 上取得業界頂尖分數,相較 context stuffing **節省 86% token**。

#### 3. Nimblemind(約 03:16:01–03:22:00)

共同創辦人暨 CEO 談**醫療照護的 agent**。切入點是產能與行政成本:全球臨床人力都不足,而光是美國,**不直接產生照護的行政任務就佔約 25% 的醫療支出,約 6,000 億至 1 兆美元**。他指出多數人把 copilot 和 LLM 丟進這些流程,卻少了三個要素:**可預測、結構化、一致的任務執行**;**系統性的 human in the loop**(把低信心的決策明確暴露給專家);以及**目標導向的工作流**。

Nimblemind 把三者合起來做「端到端的醫療知識工作」:跨越醫療院所裡龐雜的系統找出相關資訊、理解 context 與例外、完成多步驟工作流並標出需要人介入之處,最後回傳**可追溯的輸出**。技術路線是**專科專用的小模型**(腫瘤科、病理科、放射科、腎臟科等),組合成一個 system of experts。案例:與 **SingHealth** 合作的論文,掃過 200 萬份以上病理報告尋找被遺漏的 H. pylori 與胃炎案例——人工做這件事約需**每 1 萬份報告 82 小時**,他們**省下 99% 以上的時間**,準確度高於院內可接受門檻,整件事在一週內完成。公司約兩年半、創投支持、約 100 家客戶,提供可整合的 API 與白標,並新增讓非技術使用者自建工作流的功能。

#### 4. AgntID(約 03:22:12–03:27:18)

第三次創業的創辦人(前一家資安新創被 **Fortinet** 收購,更早是 distinguished engineer)講**AI agent 的執行期存取控制**。他用一個刻意簡化的例子開場:prompt 是「summarize Google Doc A」——那麼 agent 只該讀 doc A,如果它太熱心去翻 doc B 就擋掉;意圖是「讀」,如果它去改或刪就擋掉;你說的是 Google Docs,如果它跑去呼叫 Dropbox 的工具就擋掉。

問題為什麼存在:agent 之前的應用**工作流固定、工具已知,存取權在設計階段就預先定義好**;而用 agent 的全部意義就在於它能推理、動態決定下一步,並在**執行期**透過 MCP 等協定發現工具——所以**存取權必須在執行期評估**。他們的產品給的是「**just-for-task runtime access**」:只給這個任務需要的權限、只在需要的時候給、只在執行期給,**agent 永遠拿不到全面性權限**。做法是兩段收窄——先做**意圖評估**(超出原始意圖就擋),再做**政策評估**(客戶自己寫的政策),最後還能做 **scoped credential derivation**(token exchange 換一個更小的 token)給 agent 去呼叫 MCP 或 CLI。runtime 部署在客戶自己的環境、夾在 agent 與 MCP/工具之間,資料不外流、延遲也低。他明確把 OpenAI / Hugging Face 事件當成論據:那是個有多個失效點的複雜案例,但**未授權的工具呼叫是其中之一,而那一段 AgntID 擋得住**。定位是賣給基礎設施買家(identity、security、DevOps),對開發者依賴極低,並與既有 IAM / IGA 與 agent 編排系統(LangGraph、Vertex AI)互補。產品自 **2026 年 3 月**起可用,pre-seed,已有大型企業客戶。收尾:「軟體的未來是 agentic,而正因為是 agentic,**存取控制的未來就是 runtime**。」

#### 5. RELAI(約 03:27:23–03:33:08)

**Soheil Feizi**(創辦人暨 chief scientist,馬里蘭大學電腦科學副教授)講 **Verifiable Continual Learning(VCL,可驗證的持續學習)**。他先拆解現況的兩種做法都不行:一種是**人工檢查**——看到 agent 行為出錯就叫 coding agent 去改目標 agent,「這是憑感覺(vibe-based)的,你不知道改動有沒有效,也不知道它有沒有在其他樣本上造成隱性 regression」;另一種是 prompt / harness optimizer——但那些**只在你有 benchmark 時適用,而不是 agent 的真實 log**,而且容易 shortcut learning 與 overfitting。

RELAI 的三段式:(1) 把 agent 行為的每一個信號變成**可重播的學習環境**,讓行為能被模擬與評估——「這就是驗證的基礎,因為現在所有東西都可測試」;(2) 做**整體的根因分析**,找出「最小且持久的改動」;(3) 交給 **lifelong agent optimizer**,其中內建 **in-loop regression control**,在不產生 regression 的前提下改進 agent,而且要夠有效率讓這個迴圈能頻繁執行。使用上是幾個指令:在 agent 的 repo 裡 `init` 掃描並生成 learning harness(一次性),用一個指令建出含 learning persona、mock 工具、verifier 與 evaluator 的學習環境,再 `optimize` 給定 rollout 預算——**產出是一個 pull request**,你能看到 agent harness、agent memory 等處的改動與改動理由。示範情境是客服 agent 面對多輪對話中要求未授權退款的對抗性使用者。評測用 **Terminal-Bench 的持續學習版本**:第一階段 12 個 hard task、第二階段 10 個,測「優化會不會複利」;meta-harness 與 GA 等方法比 baseline 略好,但**不是無法持續進步就是出現從第一階段到第二階段的負遷移**,而 RELAI 相對 baseline 與這些方法都有顯著改善。「**每個失敗都變成一個測試,每個改動都被量測,每個改進都被驗證。**」現場給了 RDI 2026 promo code 換 500 美元額度。

#### 6. Headroom(約 03:33:15–03:38:14)

創辦人(Headroom Labs,前 Netflix 推薦系統基礎設施)開場就丟出定位句:「**Agent 沒有推理問題,它有 context 問題。**」起源是他們用 Claude Code 除錯 GPU 問題時發現,**90% 的 context 花在讀跟 prompt 無關的垃圾**——於是判定「今天 context 被資料填滿的方式從根本上是壞的」。

Headroom 是一個**本地 proxy**(pip install,跑在你的筆電上):你在用 Claude Code、Codex、Cursor 或任何 agentic harness 時,它會在資料送進模型之前攔截每一次 tool call、每一次 RAG、每一個 MCP server 的回傳,**辨識資料型別(JSON、程式碼、純文字)並移除膨脹的部分**。關鍵差異是**壓縮是可逆的**:壓掉之後留一個麵包屑給 LLM,告訴它「如果你需要原文,這裡有一個可以呼叫的 tool」——因此在大幅節省的同時保住準確度。數據:coding agent 上壓掉約 **15%** 的 token,data agent 上 **60%**,以 SWE-bench 等 benchmark(涵蓋 code search、除錯、triage 等情境)量測**幾乎沒有準確度損失**。用法就是 `headroom wrap claude`。傳播數據:首次發布 **7 個月**、上個月與這個月都是 **GitHub 排名第一的 repo**、**6.4 萬 star**、**200 萬以上開發者**、**250 位以上活躍貢獻者**;他把 6 月 1 日的曲線起飛歸因於「公司開始意識到 **token maxing 不再重要,重要的是 value maxing**」。壓縮只是楔子,真正要建的是 **context intelligence**:讓一個 agent 的 context 能被新的 agent 直接接手使用(context sharing),而今天做這件事的方式是 markdown 檔——他們想改掉這個原語,用一份**開放的 context 管理規格**來承載知識圖譜、治理與 provenance。

#### 7. Founding Dev(約 03:38:35–03:42:45)

**Talha**(二次創業,上一家募了 270 萬美元、服務過 100 多家企業含 GitLab 與 Scale AI)的主張很直接:**幫公司用自己的工具取代昂貴臃腫的 SaaS 訂閱**。他引的數字是企業每年花 **20 萬美元**租軟體——而且講的不是大企業(大企業是幾百萬),是小型的家庭式商號。Founding Dev 是一個單一平台,用來建置與取代那些訂閱、**省下 70% 成本**,也能建任何內部 dashboard,更重要的是**當成經營公司的作業系統**。

他點出與通用 code builder 的差別:那些適合小軟體,但要做**合規等級的 SaaS 工具**(電子簽核、HR 工作流、Salesforce/HubSpot 類)就不行;而且就算你建出來了,軟體生命週期、部署與管理仍然難以承擔。案例是猶他州的教育顧問 Johanna:原本一年花 **13.5 萬美元**在 SaaS 訂閱、外包開發內部工具、以及外包做各 SaaS 之間的整合;現在一個平台建置、部署、管理所有工具,不必操心部署、uptime 或生命週期,而且把公司知識集中在一處之後,甚至能直接在平台內為客戶產出影片;省下的 70% 拿去做行銷,最近談下 30 個新學區。定價每月 2,000–7,000 美元(依用量與工具數)。**第一天就獲利**,ARR 接近 50 萬美元,每月增加約 10 萬美元 ARR。

#### 8. ArmorIQ(約 03:42:49–03:48:05)

二次創業的創辦人開場一句話定調:「**有身分、通過驗證,不代表你是對齊的。**」今天在生產環境跑的每個 agent 都有某種身分——有登入或身分軌道,甚至通過了資安檢查——**但它們仍然會做出不被允許的行動**。而隨著 agent 從簡單任務走向複雜的長程工作(tool call、API call、生成 sub-agent、編排其他 agent、甚至做搬動資產的商務交易),整個資安生態系卻仍然建立在「authentication 是唯一原則」這個前提上。

他因此把問題重新表述:**要問的不是「這個 agent 通過驗證了嗎」,而是「為什麼我的 agent 正在採取這些行動」**。他們稱之為 **intent governance(意圖治理)**——對照今天已經相對成熟的 identity governance。架構上是一個**自適應的執行期控制層**,坐在 agent、LLM、政策系統與各種操作面之間:在 agent 側對接標準框架(LangChain、Langfuse 等),**擷取 agent 的計畫並與政策比對**,一旦計畫違反政策就在它碰到操作面之前擋下——操作面可以是 MCP gateway、API、CLI 工具,或其他 sub-agent。他強調願景不是「幫同一扇門再加一把鎖」,而是把這一層做成獨立的 substrate,他稱為 **intent assurance protocol**,不只看意圖,也涵蓋 agent 後續的所有行動。產品約 **4 個月前**推出,約 **2.6 萬名開發者**在用,企業版客戶包含 Intuit。

#### 9. Keenable AI(約 03:48:17–03:53:28)

創辦人(前 **Yandex Search** CEO;共同創辦人曾是 Amazon web search 的主要科學家——「這是我們的第三個搜尋引擎」)講**給 AI 用的網頁搜尋與 web query language**。他的開場觀察很好:你問 AI 任何隨機問題,答案都完美;但**你問一個你自己真的懂的問題,答案就變得很普通**——不是錯,是非常平均。他拿自己最愛的問題示範:「最好的 search API 是什麼?」——出來一張漂亮的表格、清楚的 winner、充分的理由,「看起來像剛從商學院畢業」,因為**缺的是 benchmark 與資料,那是一個完全沒有根據卻又極度自信的推薦**。原因是 LLM 就是在這類內容上訓練出來的優秀摘要機器,對每一個細緻的主題,結果都是平均值。

他的解法是模型應該**在執行期與訓練期都搜尋得多得多**,再對搜尋結果推理,才能產出專家等級的答案。但瓶頸是經濟性:ChatGPT 大約每三則訊息發一次查詢,約等於**每生成 5,000 token 一次搜尋查詢,相當於每一美元裡有 20 美分**,而且慢。更關鍵的是 **agent 的搜尋方式和人不一樣**:人很懶,agent 有目標、不懶,會生成非常具體的查詢並使用引號、站台與日期篩選——**而世界上所有索引都是為人類查詢流量優化的**。Keenable 因此重新設計索引結構,並建立**持續理解 agent 如何尋找資訊的自我學習迴圈**,對外提供 web search API(search 與 fetch 端點)與 **WebQL**——「把網際網路當成資料庫來操作」。他的示範問題是「**最便宜且有現貨的 H100 是哪個?**」:難在「有現貨」,因為答案通常是 contact sales;丟進 WebQL 之後它會掃過相關頁面、抽出價格、抽出使用者回饋,並找出「某人確實從這家供應商拿到 GPU」的證據與日期。現場提供 web search API 免費額度,WebQL 開放候補至八月底。

#### 10. H Company(約 03:53:31–03:58:50)

**Louis**(負責美國市場進入)介紹一家**有 forward deployed engineer 的 frontier AI lab**,客戶是大型企業:把雜亂破碎的營運轉成「受治理的 AI 執行」,建置並部署能端到端完成複雜工作的 agentic 系統。差異化來自兩年前創立時的研究方向——**VLM(vision language model)**:這些模型能看螢幕與使用者介面、對其推理,並驅動 agent 直接在上面操作。因此**他們的 agent 不需要 API 或 connector**,而是像人一樣從前端操作電腦,橫跨桌面、網頁、legacy 系統與任何螢幕。今年稍早他們宣布**在最新的 computer use benchmark 上超越其他 frontier lab,且成本只有十分之一**;募資方面是 **2.2 億美元的種子輪**(當時歐洲最大),夥伴包括 Accel 與 Amazon。

他的論證核心是**computer use 是一種基礎技術,和 RPA 本質不同**:RPA 是在靜態環境裡執行腳本,而 computer use 能理解 context、適應 UI 變動、動態行動。這件事之所以重要,是因為**企業工作的碎片化是設計使然**——HR、採購、供應鏈,全是彼此不通的 ERP 與 CRM;與其等每一條工作流被重建成 API,H 直接在既有的介面層工作,**改變了自動化的經濟結構**。最後他主張企業戰場上光有 autonomy 不夠,要贏得靠 **control 與 sovereignty**:安全部署、可追溯、對資料 / 模型 / 執行的控制權,加上可觀測性與人在迴圈——「這就是 demo 與生產系統的差別」。收尾:「企業競賽已經不是誰的模型最聰明,因為每個人都會有強大的模型;**真正稀缺的是能在企業系統的雜亂現實裡運作的、可控的、自主的、有能力的 AI**。」(個人註腳:他上次站上這個舞台是八年前自己的柏克萊畢業典禮,「go Bears」,而當時校園談的全是加密貨幣。)

#### 11. Ludo Robotics(約 03:58:53–04:04:03)

研究團隊分布在 **Palo Alto 與首爾**,過往作品包括 **PUBG**、**PUBG Ally**(第一個以語音與玩家一起玩遊戲的 AI agent)、**Raon**(同尺寸下 state-of-the-art 的語音語言模型),以及一些 coding agent 背後的技術。他們的框架是:機器人可以在兩個維度上聰明——**物理上聰明**與**社交上聰明**,而今天兩者都還不夠好。一個物理上聰明但社交上愚笨的機器人在工廠裡(多半在圍籠裡)很有用;但**反過來呢**?

> 如果我們拿現在這個物理能力水準的機器人,給它真正好的社交智能,會怎樣?它們能走動、能搬東西——如果它們還能跟人說話、理解人與社會,大概就能開始做一些很了不起的事。想像一個人形機器人幫你遛狗,或去接你的小孩、幫他背沉重的書包,一路上還聊得挺開心。

所以 Ludo 選了與多數人相反的路徑:**先把社交智能加到現有機器人上**。產品是 **Ludo 0.1**——一個提升現有機器人社交智能的 agentic 系統,由一個 **40 億參數的本地 vision language model** 控制:VLM 負責感知、推理與決定呼叫哪個工具,工具包含 VLA(動作)、導航與語音。示範一:一個在洗碗的男子請機器人拿一罐可口可樂給 Chloe,隨即更正「我記錯她的偏好了,拿百事」;機器人找人、導航、抓取、放置到桌上,並說明「Jake 請我把這個拿給你」。示範二:有人請它去看水滾了沒、衣服洗好了沒;它走去廚房與洗衣機、回來報告「衣服洗好了但水還沒滾」,對方說「那我先去摺衣服」,它回答「抱歉我還不會摺衣服——**如果我們下一輪募資順利,我可能會變得挺厲害的**」。下一步是 **Ludo 1.0**,一個原生就把對話與動作放進同一個模型的 foundation model,預計今年稍晚發布。兩地都在招募。

#### 12. Nimble(約 04:04:09–04:10:00)

最後一家講**給企業 AI 的專家級自我學習網頁搜尋 agent**。論點是:模型的通用知識很強,所以我們得把外部 context 灌進去;而**當我們從通用智慧走向專用智慧、要模型做更具體專門的事情時,網頁搜尋系統本身也必須專用化**。他們的迴圈是規劃 → 搜尋 → 微調模型 → 得到結果 → 用記憶系統自我學習與優化。

差別在哪:通用檢索可以回答「最近哪個模型在 benchmark 上贏了」;但專用工作要的是**一份實體清單加上所有參數、而且要即時**,這需要大量平行搜尋並取回最相關的資訊。所以他們不用「模型丟出一個查詢、拿回資訊」的單一通用檢索系統,而是把它拆成專用元件:建清單、驗證資訊、語意查詢、呼叫各種特定工具——**這些工具的組合才是專用搜尋系統的樣子**。應用橫跨領域:一般查詢要更高準確度;研究者要模型在蛋白質領域最強;保險與法遵的人要模型是該領域專家。他們學到的關鍵是:要把這類系統規模化,**必須訓練更小的檢索演算法**——把領域專業建成知識表示,嵌進 **1B 與 2B 的專用小模型**,由它們針對使用者 context 取回資訊,而不是每次都動用超大模型(否則 deep research 會把大量 chunk 灌爆 context)。架構結合**記憶狀態**與**自我學習演算法**,同時建出檢索系統與該領域專屬的索引,再搭配**即時 headless browser** 去網路上抓所需資訊。成果是準確度與效能雙升、token 效率也更好。以一支 API 提供。

### 金句

> "Agents don't have a reasoning problem. They have a context problem."(約 03:34,Headroom)

除錯 GPU 問題時發現 90% 的 context 是垃圾,於是有了這家公司。

> "The future of software is agentic. And because it's agentic, the future of access control is runtime."(約 03:27,AgntID)

工具在執行期才被發現,權限就不可能在設計期定完。

> "Identity and authentication doesn't mean you're aligned."(約 03:42,ArmorIQ)

從 identity governance 到 intent governance 的一句話論證。

> "Every failure becomes a test, every change is measured, and every improvement is verified."(約 03:32,RELAI)

Verifiable continual learning 的定義。

> "Sorry, I can't help with the folding yet. If we close our next funding round, I might actually be pretty good at it."(約 04:03,Ludo Robotics 示範影片中的機器人)

全場最好的 demo 台詞。

## English Notes

### TL;DR

- Community and entrepreneurship is one of Berkeley RDI's three core pillars. This spring RDI ran the **Berkeley Xcelerator** spring cohort with **eight** early-stage companies spanning the agentic AI full stack; four more early-stage industry companies joined them here, for twelve presentations in total.
- **The two most crowded lanes are context and access control.** cognee and Headroom are both selling "stop stuffing garbage into the context window." AgntID and ArmorIQ independently argue that **passing authentication doesn't mean being aligned**, and both compare the agent's stated intent or plan against what it is actually about to do — at runtime.
- **The OpenAI / Hugging Face incident has become a shared market anchor** for agent-security products; AgntID cited it directly as a failure mode its product would have caught.
- **"Don't wait for the API" is the other through-line.** Narada AI and H Company both argue enterprise work is fragmented by design, and that rather than waiting for every workflow to be rebuilt around APIs, agents should drive the existing interface layer directly — including legacy green screens, Citrix, and remote desktops.
- The session closed the summit, followed by a poster session and reception in the MLK building.

### The Twelve

#### 1. Narada AI (~03:01:32–03:10:30)

**Dave Park** (CEO and co-founder; started his first company, Coverity, out of his Stanford CS PhD) presented an **agentic automation platform purpose-built for enterprise applications and workflows**. The premise, drawn from hundreds of customer meetings: what's still manual in HR, IT, and finance isn't copilot-shaped work but **long-horizon processes** — ERP testing, data validation and reconciliation across silos, order/invoice/bill reconciliation — spanning legacy applications, SaaS portals, and the web. Because APIs are limited for many steps, the work requires operating through the UI: reasoning visually about what's on screen, then clicking, typing, scrolling. Hard-coded scripts and bots break whenever an interface changes; general-purpose models eventually hallucinate against the real exceptions of messy production environments (login issues, dropped connections, timeouts, configuration changes, duplicate CRM records that all qualify).

Three responses: (1) proprietary techniques that **automatically map a customer's application and interface configurations**, generating agents on the fly from a natural-language process description or even a screen recording; (2) turning their learnings about where and why agents fail into **curated test environments and synthetic data**, used to develop harnesses that recover from real-world exceptions; (3) an agentic planning and execution framework from their own research, the **LLM Compiler**, which decomposes long-horizon tasks into granular steps with unit testing, exception handling, guardrails, and self-healing at each one. The same mapping machinery also **optimizes high-volume workloads**: once the execution path through an interface is learned, the next thousands of orders or claims run with far less compute at higher speed and accuracy. The team includes UC Berkeley's **Kurt Keutzer** and **Amir Gholami**, who led the research behind Narada at the UC Berkeley AI lab. Examples: speccing competitor car models, options, and pricing across 23 countries (hundreds of steps per task); a customer with **4,000 billing portals with no API support**. They deliver free PoCs within days.

#### 2. cognee (~03:10:39–03:15:55)

Founder **Vasilije** ("Vess," in from Berlin) presented an **open-source AI memory layer**. He framed the problem as: **can we add a self-improvement loop to any harness and any model without token maxing?** — and insisted it is **a data problem, not an agentic one**. Agents produce a hundred times more data than humans, agentic workflows are data-intense and generate enormous context, and meanwhile the traditional systems, CRMs, and data silos also need to be connected and reasoned over.

cognee sits between your data and your agentic workflows, ingesting, structuring, and processing data into combined **graph and vector representations** — he likens it to lasagna, layering meanings on top of each other, cross-connecting them, and constantly evolving them. The properties it has to handle: versioning, temporality, concurrent reads and writes by different agents with different memories, conflict resolution, timestamps, and meta-representations of what something meant at a given point in time. His illustration is pronoun resolution ("him" refers to different people on different days), extended to business terms whose definitions drift — revenue, fiscal year. Architecturally it runs on **Postgres**, and each agent, team, or tenant can have its own database, all supported in the open source. There's a Claude Code plugin, an API and CLI, and Rust, TypeScript, and Java versions; run it as a server to share data between agents, users, and teams. Numbers: GitHub stars up from roughly 10,000 to **30,000** since the start of the year, around **8 million SDK runs a month** and roughly 170–180,000 downloads last month, top scores on a standard memory benchmark, and **86% token savings** versus context stuffing.

#### 3. Nimblemind (~03:16:01–03:22:00)

The co-founder and CEO presented **AI agents for healthcare**, opening on capacity and administrative cost: there are not enough clinicians and trained staff to see and treat everyone, and in the US alone **administrative tasks — work not aligned to actually delivering care — account for about 25% of spending, roughly $600 billion to $1 trillion.** Healthcare has also grown far more complex than the one-to-one doctor–patient relationship of fifty or sixty years ago: care pathways, genetics and lifestyle, plus billing systems, coding, and payer authorizations.

His diagnosis of why copilots and LLMs dropped into these workflows fall short: they miss three ingredients — **predictable, structured, consistent task execution**; **systematic human-in-the-loop** that exposes low-confidence decisions to experts when appropriate; and **objective-driven workflows**. Nimblemind combines all three to automate what he calls end-to-end healthcare knowledge work: find the relevant information across the myriad systems inside a provider, understand context and exceptions, complete the multi-step workflow while flagging what needs a human, and return a **traceable output**. The technical bet is **specialty-specific small models** — oncology, pathology, radiology, nephrology and more — combined into a system of experts, matching how healthcare is actually practiced. Their case study, a paper with **SingHealth**: scanning over two million pathology reports for missed cases of H. pylori and gastritis. A human would need roughly **82 hours per 10,000 reports**; Nimblemind saved **over 99% of the time**, at accuracy well above the internal acceptability threshold, and delivered it in under a week. The company is about two and a half years old, venture-backed, with around 100 customers worldwide, scalable APIs, white-labeling for health tech companies, and a new feature letting non-technical users at providers build and ship their own workflows.

#### 4. AgntID (~03:22:12–03:27:18)

A third-time founder (his last cybersecurity startup was acquired by **Fortinet**; previously a distinguished engineer) presented **runtime access control for AI agents**. His deliberately oversimplified opening example: the prompt is "summarize Google Doc A." The agent should only look at doc A — if it gets overeager and starts reading doc B, block it. The intent was to *read* — if it starts updating or deleting, block that too. You said Google Docs — if it makes a tool call into Dropbox, block it.

Why the problem exists at all: before agents, applications had **fixed workflows and known tools**, so all access was predefined at design time. The whole point of using agents is that they reason and decide the next action dynamically, discovering tools **at runtime** via MCP and other protocols — so **access has to be evaluated during execution**. AgntID's product provides **just-for-task runtime access**: only the access needed for this task, only while it's needed, only at runtime, so **agents never receive blanket permissions**. It narrows in two stages — **intent evaluation** (block anything outside what the agent is trying to do) then **policy evaluation** (customer-written policies) — and can finish with **scoped credential derivation**, a token exchange yielding a smaller token the agent then uses for its MCP or CLI call. The runtime deploys inside the customer's own environment, sandwiched between agents and MCP/tools, so customer data stays private and latency stays low. He invoked the OpenAI / Hugging Face incident directly: a much more complicated example with multiple points of failure, but **an unauthorized tool call was one of them, and that part AgntID could have stopped**. Positioning: sold to infrastructure buyers — identity, security, DevOps — with very little developer dependency, bring-your-own MCP/CLI/skills (no catalog of their own), and complementary to existing IAM, IGA, and agent orchestration systems like LangGraph and Vertex AI. Available since **March 2026**, pre-seed, with large enterprise customers. His close: "The future of software is agentic. And because it's agentic, **the future of access control is runtime.**"

#### 5. RELAI (~03:27:23–03:33:08)

**Soheil Feizi** (founder and chief scientist; associate professor of computer science at the University of Maryland) presented **Verifiable Continual Learning (VCL)**. The goal of continual learning is to keep improving an agent from its own experience *without regression*, and that improvement can happen in the model layer, the harness layer, or the memory layer. He dismissed both current approaches: **manual inspection** — you see a failure and ask a coding agent to change the target agent — is "vibe-based," and it's unclear whether the change is effective or whether it created hidden regressions on other samples; **prompt or harness optimizers** only apply when you have benchmarks rather than real logs from the agent, and are prone to shortcut learning and overfitting.

RELAI's engine has three stages: (1) turn every signal from agent behavior into **replayable learning environments** that simulate and evaluate those behaviors — "this becomes the foundation of verification, because now everything becomes testable"; (2) run **holistic root cause analysis** to find the smallest durable change; (3) hand that to a **lifelong agent optimizer with in-loop regression control**, improving the agent without creating regressions, efficiently enough that the loop can run frequently. In practice it's a few commands: initialize inside your agent repo and it scans the repo and creates a learning harness (a one-time job); one command creates a rich learning environment from a described scenario or a failed log with feedback, including learning personas, mocked tools, and verifiers/evaluators; then `optimize` with a rollout budget improves the agent and **opens a pull request** showing the changes and the reasons for them across harness, memory, and other aspects. His demo scenario: a customer support agent facing an adversarial user in a multi-turn conversation pushing for an unauthorized refund. For systematic evaluation they built a **continual-learning version of Terminal-Bench** in two phases — 12 hard tasks, then 10 — to test whether optimizers compound. Meta-harness and GA methods improve slightly over baseline, but on inspection they either stop improving or show **negative transfer** from phase one to phase two; RELAI shows significant improvement over both the baseline and those methods. "**Every failure becomes a test, every change is measured, and every improvement is verified.**" Available today at relai.ai, with an RDI 2026 promo code good for $500 in credits.

#### 6. Headroom (~03:33:15–03:38:14)

The founder of Headroom Labs (previously at Netflix on recommendation infrastructure) opened with the positioning line: "**Agents don't have a reasoning problem. They have a context problem.**" The origin story: debugging GPU problems with Claude Code, they found **90% of the context was spent reading garbage that wasn't important to the prompt** — which convinced them that the way context gets filled with data today is fundamentally broken.

Headroom is a **local proxy** — pip install a package and it runs on your laptop. When you use Claude Code, Codex, Cursor, or any agentic harness, it inspects all data before it reaches the model and **removes the bloat**, detecting whether what's flowing through is JSON, code, or flat text. The differentiator is that the compression is **reversible**: it squashes something but leaves a breadcrumb, telling the LLM that if it needs the original, here is a tool call it can make — which preserves accuracy while still delivering large savings. Results: about **15% token compression on coding agents and 60% on data agents**, benchmarked against SWE-bench and others across code search, debugging, and triaging a codebase, with almost no accuracy loss. Usage is `headroom wrap claude`. Traction: **seven months** from first release, the **number one GitHub repository** last month and this month, **64,000 GitHub stars**, **2 million+ developers**, and **250+ active contributors**; he attributes the June 1st hockey stick to a culmination of factors, mostly companies realizing that **token maxing is no longer important — it's all about value maxing**. Compression is only the wedge; the goal is **context intelligence** — letting one agent's context be picked up and operated on by a new agent. Today that's done with markdown files, and they want to replace that primitive with an **open spec for context management between agents**, which would enable knowledge graphs, governance, and provenance. "As agents scale, context is the bottleneck, and we are the layer that makes it efficient."

#### 7. Founding Dev (~03:38:35–03:42:45)

**Talha** (second-time founder; raised $2.7M for his last company and worked with 100+ businesses including GitLab and Scale AI) pitched **replacing expensive, bloated SaaS subscriptions with a company's own tools**. His number: businesses spend **$200,000 per year renting software** — and he means small mom-and-pop shops, not large enterprises, which spend millions. Founding Dev is a single platform to build and replace those subscriptions at **70% lower cost**, to build any internal dashboards, and — most importantly to him — **to run the business as an operating system**.

The gap versus generic code builders: those are fine for small software, but not for **compliance-grade SaaS tools** (e-signing, HR workflows, Salesforce- or HubSpot-class systems), and even if you build something, the software lifecycle, deployment, and ongoing management are hard to carry. His customer example is Johanna, an education consultant in Utah, previously spending **$135,000 a year** on SaaS subscriptions, dev shops for internal tools, and the same dev shops for integrations between them. Now she gets one platform to build, deploy, and manage everything, never worries about deployment, uptime, or lifecycle, and — with all her company knowledge assembled in one place — even creates customer videos from inside the platform. She saved 70%, put it into marketing, and recently closed 30 new school districts. Pricing runs $2,000–$7,000 per month depending on usage and number of tools. **Profitable since day one**, close to $500K ARR, adding roughly $100K in ARR per month.

#### 8. ArmorIQ (~03:42:49–03:48:05)

A second-time founder opened with the thesis: **having an identity and passing authentication doesn't mean you're aligned.** Every agent running in production today has some identity — a login or identity rails, and it has probably passed some security checks — **and yet agents still take actions they were not allowed to take.** Meanwhile agents are moving from simple tasks to complex long-running work: making tool calls and API calls, spawning sub-agents, orchestrating other agents, even executing commerce transactions that move assets. The whole security ecosystem still rests on authentication as its single organizing principle.

So he reframes the question: **not "is the agent authenticated?" but "why are my agents taking the actions they are taking?"** They call the answer **intent governance**, as distinct from identity governance, which in his view is essentially a solved problem. Architecturally, ArmorIQ is an **adaptive runtime control layer** sitting between the agent, the LLMs, the policy systems, and the surfaces it acts on. On the agent side it interfaces with standard frameworks (LangChain, Langfuse), **captures the agent's plan, and matches that plan against the policies** the agents run under; if the plan violates a policy, the action is stopped before it touches a surface — an MCP gateway, an API, a CLI tool, or other sub-agents. The vision is explicitly not "another lock for the same door" but a separate substrate he calls an **intent assurance protocol**, covering not just the intent but every subsequent action the agent takes. The product launched about **four months ago**, with roughly **26,000 developers** on the platform and enterprise customers including Intuit.

#### 9. Keenable AI (~03:48:17–03:53:28)

The founder — previously CEO of **Yandex Search**, with a co-founder who was the main scientist behind Amazon web search ("this is our third search engine") — presented **web search and a web query language for AI**. His framing observation is sharp: ask AI any random question and the answer is perfect; **ask a question you actually understand deeply and the answer is average.** Not wrong — average. His favorite demo question is "what is the best search API?", which returns a beautiful table with use cases, a clear winner, and justification: "it looks like this AI just went to business school," because **what's missing is benchmarks and data — it's an absolutely ungrounded and absolutely confident recommendation.** The cause is that LLMs are excellent summarization machines trained on exactly that kind of content, so for each nuanced topic the result regresses to average.

The fix is that models should **search far more at runtime and during training**, then reason over what they find. The bottleneck is economics: ChatGPT makes roughly one query per three messages — about **one search query per 5,000 generated tokens, or 20 cents per dollar** — and it's slow. And **agents search differently from humans**: humans are lazy, agents have a goal and are not, generating very specific queries and using quotes, site filters, and date filters — while every index in the world was optimized for human query traffic. Keenable innovates on index structures and builds a **self-learning loop that continuously learns how agents seek information**, exposing a web search API with search and fetch endpoints plus **WebQL**, a web query language whose premise is that **you operate on the internet as if it were a database**. His example: "**what is the cheapest available H100?**" — nuanced because of *available*, since the answer is usually "contact sales." In WebQL it scans the relevant pages, extracts prices, extracts feedback, and finds evidence that somebody actually obtained GPUs from that provider, with a date — an important signal that it will work. Free access to the search API, and a WebQL waitlist open through the end of August.

#### 10. H Company (~03:53:31–03:58:50)

**Louis**, who leads US go-to-market, introduced a **frontier AI lab with forward deployed engineers** serving large enterprises, helping them turn messy fragmented operations into governed AI execution at scale — building and deploying agentic systems that remove bottlenecks, automate complex work, and complete tasks end to end. The differentiation traces to the research direction they chose when founded two years ago: **VLMs — vision language models** that can see screens and user interfaces, reason over them, and power agents that act directly on them. As a result **their agents don't need APIs or connectors**; they navigate computers the way humans do, through the front end, across desktop, web, legacy systems, and any screen. Earlier this year they announced **breaking the computer-use frontier by topping the latest benchmark ahead of other frontier AI labs at one-tenth the cost**, and they raised a **$220 million seed round**, the largest in Europe at the time, with partners including Accel and Amazon.

His core argument is that **computer use is a foundational technology, categorically different from RPA**: RPA executes scripts in static environments, while computer use understands context, adapts to UI changes, and acts dynamically. That matters because **enterprise work is fragmented by design** — HR, procurement, supply chain, all ERPs and CRMs that don't talk to each other. Rather than waiting for every workflow to be rebuilt around APIs, H works directly through the existing interface layer, **changing the economics of automation**. Finally, he argued that autonomy alone doesn't win the enterprise: you win with **control and sovereignty** — secure deployment, traceability, control over data, models, and execution, plus observability and keeping humans in the loop. "That is the difference between a demo and a production system." His close: the enterprise race is no longer about who has the smartest model, since everyone will have access to powerful models; what's scarce is **controllable, autonomous, capable AI that works in the messy reality of enterprise systems**. (A personal footnote: the last time he stood on that stage was eight years earlier for his own Berkeley graduation — "go Bears" — when campus was all about crypto and Bitcoin, certainly not AI.)

#### 11. Ludo Robotics (~03:58:53–04:04:03)

A research team based in **Palo Alto and Seoul**, whose past work includes **PUBG**, **PUBG Ally** (the first AI agent that plays games alongside players using voice communication), **Raon** (state-of-the-art speech language models at their parameter size), and technology behind coding agents. Their framing: robots can be smart in two different ways — **physically smart** and **socially smart** — and right now we have neither at a high level. A physically smart but socially dumb robot is useful in factories, mostly in caged setups. But what about the other way around?

> What if we take the current robots with the current level of physical capacity and give them really good social intelligence? They can walk around well, they can carry things around. If they can talk to people and understand people and society, they can probably start doing something very amazing. Imagine a humanoid who can walk your dogs, or pick up your kids, carrying their heavy backpacks and having some fun conversation walking back.

So Ludo deliberately takes the opposite path from most of the field: **improve social intelligence on today's robots first.** The product is **Ludo 0.1**, a research release — an agentic system for improving the social intelligence of current robots, controlled by a **4-billion-parameter local vision language model**. The VLM handles perception and reasoning and decides which tool to call; the tools include VLA (the robot uses its body), navigation, and speech. Demo one: a man doing the dishes asks the robot to bring Chloe a Coca-Cola, then corrects himself — "I remembered her preference wrong, bring her Pepsi" — and the robot finds the person, navigates, picks and places the can on the table, and explains "Jake asked me to bring you this." Demo two: asked to check whether the water is boiling and whether the laundry is done, the robot goes to the kitchen and the washer, comes back, and reports "the laundry is finished but the water isn't boiling yet"; when the person says they'll fold the laundry while they wait, it answers, "**Sorry, I can't help with the folding yet. If we close our next funding round, I might actually be pretty good at it.**" Next up is **Ludo 1.0**, a foundation model natively designed to do conversation and action in a single model, to be released later this year. Hiring in both offices.

#### 12. Nimble (~04:04:09–04:10:00)

The closing presentation covered **expert-level, self-learning web search agents for enterprise AI**. The argument: models are very good at general information, so we infuse external context — and as we move from general intelligence toward specialized intelligence, wanting models to do more specific things, **web search systems must specialize too**. Their loop runs planning → searching → fine-tuning the model → results → a memory system for self-learning and optimization.

The contrast: a general retrieval system answers "what's the latest model winning a benchmark" fine. But specialized work wants **a list of entities with all their parameters, in real time** — which requires running many searches in parallel and pulling the most relevant information. So instead of one general retrieval system where the model emits a query and gets information back, they decompose it into specialized components: building the list, validating that information, semantic queries, and invoking specific tools — and **the combination of those tools is what a specialized search system actually is**. Applications span domains: better accuracy on general queries; a researcher who needs the model to be the best at proteins; someone in insurance or compliance who needs domain expertise. What they learned in practice is that scaling these systems requires **training smaller retrieval algorithms**: they build a knowledge representation of the domain expertise and embed it into **1B and 2B models specialized for that domain**, which retrieve for the user's context, instead of using an extremely large model that would flood the context with chunks during deep research. The architecture combines a **memory state and a self-learning algorithm** that builds both the retrieval system and the domain-specific index, paired with **real-time headless browsers** that fetch what's needed from the web. The result is better accuracy and better performance and token efficiency across verticals. Available through a simple API.

### Quotes

> "Agents don't have a reasoning problem. They have a context problem." (~03:34, Headroom)

> "The future of software is agentic. And because it's agentic, the future of access control is runtime." (~03:27, AgntID)

> "Identity and authentication doesn't mean you're aligned." (~03:42, ArmorIQ)

> "Every failure becomes a test, every change is measured, and every improvement is verified." (~03:32, RELAI)

> "Sorry, I can't help with the folding yet. If we close our next funding round, I might actually be pretty good at it." (~04:03, the robot in Ludo Robotics' demo video)

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Berkeley Xcelerator | Berkeley RDI 的新創加速器,今年春季梯次收 8 家 agentic AI 全端公司 | Berkeley RDI's startup accelerator; this spring's cohort had 8 agentic AI companies across the stack | rdi.berkeley.edu/xcelerator;字幕作 "Berkeley accelerator" |
| LLM Compiler | Narada 共同創辦人主導的 agentic 規劃與執行框架,支援平行 function calling | Agentic planning and execution framework from Narada's co-founders, for parallel function calling | 開源技術,Narada 平台的基礎 |
| cognee | 開源 AI memory 層:graph + vector,跑在 Postgres 上 | Open-source AI memory layer combining graph and vector representations on Postgres | 有 Claude Code plugin;Rust / TypeScript / Java 版本 |
| Terminal-Bench(持續學習版) | RELAI 用來測「優化會不會複利」的兩階段評測 | The two-phase continual-learning variant RELAI built to test whether optimizers compound | 12 + 10 個 hard task |
| Headroom | 本地 proxy,可逆壓縮送進模型的 context | Local proxy that reversibly compresses context before it reaches the model | `headroom wrap claude` |
| WebQL | Keenable 的 web query language,把網際網路當資料庫查詢 | Keenable's web query language: operate on the internet as if it were a database | 候補至八月底 |
| Ludo 0.1 / Ludo 1.0 | 提升現有機器人社交智能的 agentic 系統;1.0 為對話與動作合一的 foundation model | Agentic system for social intelligence on today's robots; 1.0 is a foundation model unifying conversation and action | 1.0 預計今年稍晚發布 |
| Raon | KRAFTON 的語音語言模型系列,Ludo 團隊過往作品 | KRAFTON's speech language model family; prior work by the Ludo team | 字幕作 "Rayon" |
| PUBG Ally | 第一個以語音與玩家一起玩遊戲的 AI agent | The first AI agent that plays games with players via voice communication | Ludo 團隊過往作品 |
| Fortinet | AgntID 創辦人前一家資安新創的收購方 | Acquirer of the AgntID founder's previous cybersecurity startup | 字幕作 "Forinet" |
| SingHealth | Nimblemind 病理報告論文的合作機構 | Nimblemind's partner on the pathology report study | 字幕作 "Singh Health";**待確認** |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Narata AI / NAR / NATO | Narada AI |
| Coverarity | Coverity |
| Kurt Quitzer | Kurt Keutzer |
| Amir Golami | Amir Gholami |
| Cognney / Cogni | cognee |
| Vess | Vasilije(cognee 創辦人) |
| agent ID / agent.ai | AgntID |
| Forinet | Fortinet |
| Rei / Reli / Rely / Trilai | RELAI |
| Sel Fez | Soheil Feizi |
| terminal bench | Terminal-Bench |
| Hatroom / headroom | Headroom |
| SWEBench | SWE-bench |
| Funing Deep / funing dev / founding de | Founding Dev |
| Docuine | DocuSign(**待確認**) |
| Bamboo HR | BambooHR |
| Armor IQ / armorq.ai | ArmorIQ / armoriq.ai |
| into it | Intuit |
| Kino AI / Kinable | Keenable AI |
| age company / each company | H Company |
| Axel | Accel |
| Nvidia animatron coalition | NVIDIA Nemotron(**待確認**) |
| Lud Robotics / Luda / Ludy 0.1 / Ludium 0.1 | Ludo Robotics / Ludo 0.1 |
| Rayon | Raon |
| VA / VALA / VLAM | VLA / VLM |
| Nimbo / nibbleway.com | Nimble / nimbleway.com |
| Singh Health | SingHealth(**待確認**) |
| Berki RDI | Berkeley RDI |
| Berkeley accelerator | Berkeley Xcelerator |

## 待確認 / To Verify

- **講者姓名**:多位創辦人的姓名在自動字幕中嚴重失真,本文僅在能可靠比對到公開資料時具名(Dave Park、Vasilije、Soheil Feizi、Talha、Louis),其餘以公司名代稱。Nimblemind 的 CEO(字幕作 "Pisa News")、AgntID 的創辦人(字幕作 "Sundar Kesh")、Headroom 的創辦人(字幕作 "Tjis Chopra")、ArmorIQ 的創辦人(字幕作 "Rahm",共同創辦人 "Kathan"、"Viva")、Keenable 的創辦人(字幕作 "Andre Stysiskin",共同創辦人 "Matias")均**待確認**。/ Several founders' names are badly mangled in the auto-captions; only reliably cross-checked names are used. The Nimblemind CEO, AgntID founder, Headroom founder, ArmorIQ founders, and Keenable founders all need verification.
- **cognee 的數字前後不一**:開場說「過去 90 天拿到近 8,000 個 GitHub star、開源 Python SDK 產生 800 萬則 memory」,後段說「年初至今從約 1 萬成長到 3 萬 star、SDK 每月 800 萬次執行」。本文採後段數字,但兩組數字需比對官方資料。/ cognee's figures are internally inconsistent between the opening and closing of the talk; the later set is used here, but both need checking against official sources.
- **cognee 的記憶 benchmark 名稱**(字幕作 "beam")待確認正確拼法。/ The memory benchmark cognee benchmarked on (heard as "beam") needs its correct name.
- **Nimblemind 的合作機構與研討會**:"Singh Health" 應為 SingHealth(待確認);"DIH"(10 月 8 日,舊金山)與 "Sale" 兩個研討會名稱待確認,"ML4H" 與 NeurIPS 可信。/ "Singh Health" is likely SingHealth (verify); the "DIH" (Oct 8, San Francisco) and "Sale" conference names need verification. ML4H and NeurIPS are reliable.
- **Narada 的網域**:講者給的信箱是 dave@nar.ai / info@nar.ai,但公司網站為 narada.ai;需確認實際使用哪一個。/ The emails given were @nar.ai while the company site is narada.ai; verify which is in use.
- **Narada 的投資人**:字幕作 "Venshukla at Monavista Capital",推測為 Monta Vista Capital 的 Venk Shukla,**待確認**。/ Heard as "Venshukla at Monavista Capital," likely Venk Shukla of Monta Vista Capital — to verify.
- **Headroom 的開放規格名稱**(字幕作 "open context / open spec for context management")待確認正式名稱。/ Headroom's open spec for inter-agent context management needs its formal name.
- **H Company 的 NVIDIA 聯盟**(字幕作 "Nvidia animatron coalition")推測為 Nemotron 相關,**待確認**。/ The NVIDIA coalition H Company mentioned (heard as "animatron") is likely Nemotron-related — to verify.
- **Ludo Robotics 提到的 coding agent 技術**「meta harness」與「terminal cur」名稱待確認。/ The coding-agent technologies Ludo cited ("meta harness," "terminal cur") need verification.
- **Founding Dev 的產品類比**「Docuine」應為 DocuSign,**待確認**。/ "Docuine" is presumably DocuSign — to verify.
- 各家的 traction 數字(GitHub star、開發者數、ARR、客戶數、募資金額)均為講者現場口述,未經第三方查核。/ All traction figures — GitHub stars, developer counts, ARR, customer counts, funding — are as spoken on stage and unverified by third parties.
