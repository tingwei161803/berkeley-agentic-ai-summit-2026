---
title: "Panel: Agentic AI in Finance & Legal"
title_zh: "座談:金融與法務領域的 Agentic AI"
speaker: "Nikhil Chandhok、Faraz Shafiq(主持:Matt Carbonara)"
affiliation: "Nikhil Chandhok — Chief Product & Technology Officer, Circle / Faraz Shafiq — Head of AI, Wells Fargo(主持:Matt Carbonara — Investor, Mayfield)"
type: panel
stage: Plenary
date: 2026-08-02
session: "Session 4: Agentic AI in Finance & Legal"
video: "https://www.youtube.com/watch?v=I2PosBXwoPI&t=9139s"
video_range: "02:32:19–02:59:07"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [finance, legal, evaluation, org-design, moat, panel]
---

# 座談:金融與法務領域的 Agentic AI(Panel: Agentic AI in Finance & Legal)

**一句話總結**:金融與法務不是「更難的 agent 應用」,而是**驗證成本結構完全不同**的應用——可驗證的任務(寫程式)早就自動化了,而信貸決策要五年後才知道對錯;這條驗證軸線決定了什麼會先被 agent 吃掉、什麼會最後才被吃掉。
**One-line summary**: Finance and legal aren't just "harder agent problems" — they have a fundamentally different verification cost structure. Easily verified tasks (coding) automated first; a credit decision may not be verifiable for five years. That verification axis determines what agents take over first and what they take over last.

## 中文筆記

### TL;DR

- **Verifier's Law 是這場的核心框架**(Shafiq):**容易驗證的任務就是 agentic 流程的沃土**。數獨很難解但很好驗證;寫程式有 QA 和測試可以馬上跑。反過來,難驗證的東西 lead time 就長——自駕很難完全驗證某個當下車子做得對不對;而**信用卡或貸款核准的決定是今天做的,驗證可能是五年後那個人違約時才發生**。
- **金融法務其實早就在用 agent**(Chandhok):因為大家都在用 coding agent,而 coding agent 有很棒的性質——**可驗證、可測試**。你可以讀程式碼、可以跑測試套件。財務與法務可以做一樣的事,但**失敗成本高太多**:SOX 合規、準備財報(「我們下週就要財報」)不能出錯,對 agent 的檢視強度會非常驚人。「我們不想只因為 agent 犯了錯就被監管機關叫去問話——他們會究責我們,不是究責 agent。」
- **房貸是 1,100 步的流程**(Shafiq):所以不可能是一個 agent、也不可能全是自建。真正的難題不是協定(A2A 很好用,協定通常不是問題),而是**該為哪個任務抓哪些資料、以及 ServiceNow agent 怎麼跟 Salesforce agent 跟自建 agent 交換正確的 context**。
- **Eval 的異質性比想像更細**(Chandhok):早上有講者說「每個組織對 eval 都很 idiosyncratic」,他要修正成「**組織內每個 team 都很 idiosyncratic**」。他們的做法是把模型、harness、以及輸入以外的變數全部鎖死,再加上 **shadowing**——讓 agent 跟合規分析師同時處理同一筆 inbound,比對兩邊決策,跑成 RL 迴圈。
- **問錯問題是企業最大的浪費**(Shafiq):主管常說「我們有這個大流程,能不能用 AI 讓它更簡單更快更自動?」——**這通常是錯的問法**。對的問法是:用 AI 的「art of the possible」是什麼、能不能重新想像整個體驗,然後從現況倒推過去。他點名一個裂縫:開發者和 PM 個別都說自己效率提升 30%,**但那常常沒有轉譯成工作流層級的提升**。
- **「不會再有 individual contributor」**(Shafiq):Wells Fargo 有 20 萬名員工、大多數是 IC,而 **IC 會變成 agent 的管理者**。IC 習慣端到端擁有工作、不習慣委派;現在你仍然擁有這份工作,但你在委派它。他們正在和 HR 合作推「每個人都會是管理者」這件事。
- **護城河在「硬物理」**(Chandhok):純軟體生意會很難防守(他認為這是廣泛共識)。Circle 的賭注是**網路生意優於軟體生意**——USDC 是穩定幣網路、上面有 Circle Payments Network、還在建 Arc 這條區塊鏈;加上「生意的硬物理」:Arc 有硬的運算問題,發行穩定幣要受 OCC 監理與檢查。軟體是加速器,不是護城河本身。

### 重點整理

#### 主持人開場:Mayfield 的位置(約 02:32)

**Matt Carbonara** 先自我定位:Mayfield 是一支 **57 年**的創投,正在投第 19、20 號基金,總部在灣區;歷史上投過 **700 家以上公司,其中 125 家上市、250 家被併購**。他強調 Mayfield 是「people first」——公司是創業者建的,建公司是馬拉松不是短跑,起伏來時他們不會恐慌。投資階段從 seed / inception 到 Series B,範圍上下貫穿整個 stack:從半導體、光學、交換、模型,到基礎設施軟體、資安、雲、開發工具,一路到應用層。

他給這場的題目:我們剛剛談的這些 agent,**要怎麼用在法務與金融這種高風險領域**?

#### 主題一:高風險領域的 agent 有什麼不一樣(約 02:32–02:36)

**Chandhok** 的第一個觀察是:所有他知道的金融與法務組織**今天都已經在用 agent 了**——因為他們在用 coding agent。而 coding agent 有一個很棒的性質:

> **可驗證性與可測試性。** 你可以進去讀程式碼,判斷它是不是太囉唆、夠不夠囉唆、有沒有設計文件;你可以對它跑一整套測試。

金融與法務可以做一樣的事,但**失敗成本高太多**。他舉自家的例子:如果是 SOX 合規,或有個 agent 的工作是把財報準備好(「我知道這件事是因為我們下週就要財報」),**這是不能出錯的**,對那個 agent 的檢視強度會非常驚人。因此三件事的門檻同時被拉到極高:

1. agent 決策過程的**可稽核性**
2. agent 能碰到的**資料來源**
3. 輸出的**可驗證性**

他的判斷是:**這些會是最後才被自動化的流程之一**——因為公司的存續取決於它把財務做對的能力,以及讓法律暴露面維持在恰當範圍的能力。這在其他職能同樣成立,比如合規:「我們不想只因為 agent 犯了錯就被監管機關叫去問話。他們會究責我們,不是究責 agent。」

**Shafiq** 補上一個他認為非常重要的框架——**Verifier's Law**:

> 容易驗證的任務,就是 agentic 流程的沃土。想想數獨——**很難解,但非常容易驗證**。

所以寫程式很適合(有 QA、有測試,可以很快驗);而**難驗證的東西會更難解、lead time 更長**。自駕就是這樣:很難完全驗證那台車在那個當下做的是不是對的事。銀行更極端:

> 有人來申請信用卡或貸款,某些情況下我們手上資料不多。如果我們根據現有資訊做了錯誤的決定,而那個人違約——**那可能是五年後的事**。給信用的決定是今天做的,驗證在五年後。這變得非常難。

所以他們的篩選邏輯是:**哪些任務真的成熟到 agent 可以超越人類「一直做對」的機率?** 那些就是他們會優先動手的。

#### 主題二:自建 vs 外購,以及 agent 之間怎麼連(約 02:36–02:38)

Carbonara 追問:這套判斷對自建 agent 和外購 agent 是一樣的嗎?

**Shafiq** 的答案是混合:模型與智慧本身**大體上是一樣的**,但 Wells Fargo 有別人沒有的 IP 與資料,所以在某些事情上自建 agent 有優勢。同時,**現成 agent 開箱即用的能力已經強到不用它才不合理**;真正的變數是經濟性——一旦成本下來,它們會變得無所不在。

他認為更大的問題是 **agent 之間怎麼連接**:

> 我舉的房貸流程,是銀行裡一個**大約 1,100 步**的巨大複雜流程。它不會是一個 agent,也不會是一堆自建 agent 而已,而是很多東西的組合。而且不能出現「這個 agent 做得很好但另一個不行」的情況,**因為它們得互相對話與連接**。

尤其在長時間運行的系統上:「你下一個 prompt、拿到一個回應,那很容易,那你會做對。但當你要的東西橫跨數小時、數天、數週,**context 就開始變得曖昧不明**。」

#### 主題三:給創業者的兩個缺口(約 02:38–02:39)

Carbonara 問:那些耗時長、難驗證的事,是不是創業機會?

**Shafiq** 直接點名兩個:

1. **Agentic harness**——「這個概念聽起來太簡單了:一個把所有東西兜在一起、坐在 agent 上面的 harness。但**它極難做好**,尤其是長時間運行的流程。」這是他們正在積極尋找的東西。
2. **跨 agent 的 context 交換**——他強調這些是**產業級的問題,不是 Wells Fargo 的問題**。協定層面其實還好:「A2A 是個很棒的協定,很多組織也在標準 SDK 上面建,協定通常不是問題所在。」問題在於:

> **要為哪個任務抓哪些資料?一個 ServiceNow agent 要怎麼跟 Salesforce agent、跟自建 agent 協作,交換正確的 context 與正確的資訊?** 這非常難做。這是一個很大很大的機會。

#### 主題四:可靠度怎麼量、什麼時候可以上線(約 02:39–02:42)

**Chandhok** 說這件事一定因 use case 而異。他引用當天早上一場關於 eval 的演講——講者說各組織對 eval 都非常 idiosyncratic;他要把顆粒度再切細:

> 我會說**在組織內部,每個 team 對 eval 都是 idiosyncratic 的**。要量什麼、怎麼量、什麼叫「好」,得一個流程一個流程地定義。

Circle 現在正在建可規模化 eval 的框架。他也提醒 **eval 會因為各種理由壞掉**:model drift、資料問題、各式各樣的東西都會讓 agent 的表現改變。所以在已經導入的地方,他們的做法是**把模型、harness、以及輸入以外的所有變數都鎖死**。

另外他們用一種他稱為 **shadowing** 的做法:

> agent 跟人坐在一起——合規分析師接到一筆 inbound,他在做判斷、看資料;我們同時看 agent 會怎麼做,然後評估兩邊差異,把它跑成一個 reinforcement learning 迴圈。

至於 KPI,他坦承還很模糊。他們在試「**token 花費對應到什麼程度的自動化**」,但目前**刻意不去省 token**:讓人盡量用,看能換到多少生產力。而生產力通常以三種形式出現——**每個人產出更多**、少數地方直接是**營收**(規模還小)、或是明顯的**成本節省 / 把原本做 X 的人力挪去做 Y**。「以上皆是。但沒有什麼 rule of thumb 可以說 KPI 或 eval 就該這樣做。」

#### 主題五:工程資源該怎麼分配,以及企業最常問錯的問題(約 02:42–02:46)

Carbonara 問:模型、harness、工作流整合、context、memory——這些工程投入要怎麼權衡?

**Shafiq** 說這正是他花最多時間的地方。他先對比傳統產品開發生命週期:有個想法 → 在 Word 或 PowerPoint 上來回迭代 → 找工程做 Figma 或原型 → 進入開發流程,套架構樣式、做弱點與風險評估。「非常古老、非常仰賴人、非常線性。」

在 agentic 世界他看到兩條路:

- **技術選擇**:memory、基礎設施、要部署在自家雲還是公有雲……
- **商業選擇**——而這才是關鍵。

他在這裡給了另一個創業訊號:**做 frontier intelligence 的公司真的就那幾家**,但**會有一大批公司在做「讓它在企業裡真的能運轉的那台引擎」**,因為企業需要的是安全、治理、合規。

然後是他最強的一句批評:

> 主管通常會說:「我們有這個很大的流程,你能不能用 AI 讓它更簡單、更快、更好、更自動化?」——**這通常是錯的做法。** 對的做法是問:用 AI 的 art of the possible 是什麼?我們能不能**重新想像整個體驗**?然後再想辦法從現在的流程走到那裡。

他把這稱為企業裡的裂縫,並補上一個他和 Chandhok 在後台聊到的觀察:**你去問開發者或 PM,每個人都說自己效率提升了大約 30%**——寫程式比以前快多了。但在某些情況下,**那並沒有轉譯成工作流層級的提升**。

> 缺口在**流程工程**:理解領域、理解特定資料、理解 use case,然後倒推回什麼才是對的架構。因為**架構本身正在變成這裡面比較容易的那個因子**。

#### 主題六:組織設計——人與 agent 的比例(約 02:46–02:50)

**Chandhok** 說 Circle 正在推**讓員工自行發布 agent** 的能力,同時建一個 **agent gateway**:你知道公司裡有哪些 agent、可以在 Slack 裡找到它們並跟它們對話。

但他不認為這是組織設計問題:

> 我不覺得未來會有「專案上的負責人不是人類」這件事。人可以去調用公司裡眾多 agent 中的任何一個、去查 agent gateway——「公司裡有哪些 agent?有什麼財務 agent?有什麼行銷 agent?」——然後把它們組合成某種解法。**我不把它想成 org design 問題,就像我不會告訴我的下屬他們能開幾個 Google Doc。** 他們是在為我們創造成果。

他的焦點因此是三件基礎設施:**能自行發布、能取得資料以便自行發布、有正確的 ACL 讓你能自行發布**,再加上把 agent 之間的溝通搞定。

至於組織會不會變:他認為組織會更有生產力(這是大家共同的體感),**也可能重組,因為職能 A 與職能 B 之間的界線正在變模糊**。真正被問的問題是團隊怎麼組:PM 要不要多做一點 product marketing?product marketing 要不要多做品牌?BD 要不要多做產品?「連業務電話上該有誰都是問題——**也許是我們的 agent 上線去做筆記**。這類效率正在被摸索。但如果講的是老派麥肯錫那種 org design,我們沒在想這件事。」

**Shafiq** 從另一個角度回答「大規模導入 agent 最大的挑戰」。撇開技術挑戰,他丟出一個很有意思的推論:

> **不會再有 individual contributor 了。** 我們銀行有 20 萬名員工,絕大多數是 IC。這代表什麼?代表 **IC 現在會變成 agent 的管理者**。

而問題在於:IC 通常**不習慣委派**——他們習慣端到端擁有一件事、完全負責。但現在你拿到一份工作,你用 ChatGPT 或 Claude 或任何模型去做,**你仍然擁有這份工作,但你在委派它**,而這會成為未來主流的工作方式。

所以他們現在正在做的一件事,是強調**每個人都會是管理者**:

> 就像你給人回饋一樣,你需要有機制去給你的 agent 回饋、去讓你的 agent 成長、從它身上得到更多。這件事非常新,因為**playbook 根本還不存在**——你不習慣一個沒有 IC、全是管理者的世界。

他說他們正在和 HR 團隊合作,想清楚要怎麼推這件事。

#### 主題七:智慧被民主化之後,護城河在哪(約 02:50–02:56)

Carbonara 提到近幾週的討論:智慧正在民主化,連開源模型都越來越逼近 frontier——那使用這些技術的組織,長期的護城河在哪?

**Chandhok** 先自嘲:「我們比 Wells Fargo 小太多了」(他估計 Wells 的工程組織至少大他們兩個數量級)。然後給了兩層答案:

**第一層是速度**,他用噴射背包比喻:

> 你本來就在跟某個人賽跑,而現在你突然可以穿上噴射背包。如果你能駕馭它,你就能取得領先。他們會追上來——他們也會穿上他們的噴射背包。所以**第一件事是確保我和我的組織比別人更早把噴射背包穿上**。

**第二層是生意的形狀**。他同意很多東西會被商品化,而且「**純軟體的生意會很難防守**,我認為這是廣泛共識」。但 Circle 手上有一些硬東西:

> 我們是一家**由網路組成的公司**。USDC 是核心產品,我們把它當成一個穩定幣網路;上面有支付網路,叫 **Circle Payments Network**;我們還在建一條新的區塊鏈叫 **Arc**——它也是網路,因為你需要 validator、需要參與者對齊誘因。

他的主張是:**網路生意優於軟體生意,而軟體是這些網路生意的賦能者**——問題變成「怎麼用軟體去建構軟體賦能的網路」。此外還有他稱為「**生意的硬物理**」的部分:Arc 那邊是硬的運算問題;發行穩定幣本身也很複雜——**你受 OCC 特許、要接受檢查**。他們的策略就是把這些硬物理做到極好,並持續進入同樣是硬物理的鄰接領域,再把軟體當作上面的加速器。

**Shafiq** 接著把「非技術瓶頸」講得更白:

> 銀行業會有很驚人的改變,而**其中很多根本不是技術挑戰**。24/7 交易——為什麼交易在美東時間下午四點就結束?答案大部分**不是技術性的**。技術上要啟用完全不是大問題,是監管機關要確保資金流動受到規範、要保護消費者。

跨境即時到帳同樣如此:「技術上我可以讓錢立刻到位,但**如果另一家銀行要兩天才結帳,這兩天的差額誰付?錢沒到的時候怎麼辦?**」所以是監管要追上來,而新的 use case 會隨著更好的監管一起出現。

他也呼應 Chandhok 那句話,但做了一個他覺得有必要的澄清:

> 軟體那一面會讓我們把生意的「硬體」那一面做得非常好。而我說 hardware 時,**我指的不是 GPU**——我知道這是一場 agentic AI 研討會,但我們**還有 4,000 家分行**。我們仍然相信人與人連結的價值:有人只講西班牙語,他走進來跟一位理專用西班牙語談,一起把他的財務教育計畫做出來。

他認為這些不會消失,**改變的是它們被交付與被消費的方式**。最後他給了一個模型層的預測:今天由 LLM 主導、大家談的是 token 成本;**最終會是 small language model 與 fine-tuned model**,因為那會變得像按一個按鈕一樣簡單——重點會從 LLM 移到**垂直專用的 AI**,而新的 use case 會從那裡長出來。

#### 收尾:五年後會被自動化、但今天你想不到的工作流(約 02:56–02:59)

**Shafiq** 的答案是 **underwriting(核保 / 核貸)**:

> 核保是任何銀行的核心,不管是收入驗證還是房貸驗證,而且是個非常古老的流程。人們會送來各式各樣的文件——你可能拍了一張角度不對、又剛好有光打進來的水電帳單,於是就得有人把它退回去。**這是一個非常複雜的多模態問題。**

他認為這在接下來幾年會變成基本盤;目前卡住的是算力挑戰與經濟性還不到位。他也重申模型層的走向(LLM → small language model / fine-tuned model),並補了一句「**再加上量子,等那個算力可用的時候**」。

**Chandhok** 的答案則轉了個彎:

> 我是 AGI-pilled 的,所以我相信我們會從自己的臥室窗戶看到 AGI。到那個時候,我憑什麼說什麼是解不了的?

但他接著給了本場最好的收尾:

> 那可能是一個**裝滿天才的資料中心**,但人類是拜占庭式的(Byzantine)。人類非常獨特、非常難協調。所以對那些裝滿天才的資料中心來說,**這段日子可能會很寂寞**,因為我們其他人還在想辦法互相協調。我們有非常好的模型,但**我很驚訝要說服人們去做一件事需要花多少力氣,即使那件事客觀上對他們有好處**。有沒有人試過叫爸媽吃藥?或叫小孩吃藥?那客觀上對他們好,他們就是不吃。

> 人類社會還沒準備好直接聽這些裝滿天才的資料中心的。這是我的結論。我希望那些資料中心存在,我也很高興它們在這裡——但**在此刻與我們想像的那個未來之間,我們還有一大堆問題要解**。

### 金句

> "Tasks that are easy to verify are going to be ripe for agentic processes. ... Same thing in banking: the decision to give them credit was today; the verification is five years down the road."(約 02:35,Faraz Shafiq)

Verifier's Law 決定了自動化的順序。

> "We don't want to get hauled in by regulators just because our agent made a mistake. They're going to hold us responsible, not the agent."(約 02:34,Nikhil Chandhok)

責任不會因為執行者是 agent 而轉移。

> "I would say within organizations, each team is idiosyncratic about evals."(約 02:40,Nikhil Chandhok)

Eval 的異質性比「每個組織不一樣」還要細一層。

> "Can you use AI and make it simpler, faster, better, more automated? And that is typically the wrong approach."(約 02:44,Faraz Shafiq)

正確的問法是「art of the possible 是什麼」,然後倒推。

> "There are not going to be any individual contributors. ... The ICs now will be managers of agents."(約 02:49,Faraz Shafiq)

20 萬人的銀行對組織的判斷。

> "It may be a data center full of geniuses, but humans are Byzantine. ... It may be very lonely for those data centers full of geniuses while the rest of us try to coordinate."(約 02:58,Nikhil Chandhok)

模型能力不是瓶頸,人類協調才是。

## English Notes

### TL;DR

- **Verifier's Law framed the whole session** (Shafiq): **tasks that are easy to verify are ripe for agentic processes.** Sudoku is hard to solve and trivial to check; coding has QA and test suites. Hard-to-verify work has a much longer lead time — self-driving is hard to fully verify, and a credit or loan decision made today may only be verified five years later when the borrower defaults.
- **Finance and legal already run on agents** (Chandhok), because everyone uses coding agents — and coding agents have the wonderful property of **verifiability and testability**. The same techniques apply to finance and legal, but **the cost of failure is far higher**: SOX compliance, getting earnings ready ("I know this because we have earnings next week"). Auditability of the agent's decisions, the data sources it can reach, and the verifiability of its output all move to a very high bar. "We don't want to get hauled in by regulators just because our agent made a mistake. They're going to hold us responsible, not the agent."
- **Home mortgage is a ~1,100-step process** (Shafiq), so it will never be one agent and never be entirely homegrown. The hard part isn't the protocol — A2A is good and protocols usually aren't the issue — it's **which data to grab for which task, and how a ServiceNow agent, a Salesforce agent, and a homegrown agent share the right context**.
- **Eval heterogeneity runs deeper than people say** (Chandhok): a morning speaker noted every organization is idiosyncratic about evals; his correction is that **every team within an organization is idiosyncratic**. Circle locks down the model, the harness, and every variable outside the input, and adds **shadowing** — the agent works the same inbound alongside a compliance analyst, and the comparison feeds a reinforcement learning loop.
- **The most expensive enterprise mistake is asking the wrong question** (Shafiq). Leaders say "we have this large process, can you use AI to make it simpler, faster, more automated?" — **typically the wrong approach.** The right question is what the art of the possible looks like with AI, whether the whole experience can be reimagined, and then how to work backwards. His diagnostic: developers and PMs each claim ~30% more efficiency, **and that often fails to translate into workflow-level gains**.
- **"There are not going to be any individual contributors"** (Shafiq). Of Wells Fargo's 200,000 employees, most are ICs — and **ICs become managers of agents.** ICs aren't used to delegating; they own work end to end. Now you still own it but you're delegating it. They're working with HR on rolling out "everyone is a manager."
- **The moat is in the hard physics** (Chandhok). Software-only businesses will be hard to defend — broad consensus, in his view. Circle's bet is that **network businesses beat software businesses**: USDC as a stablecoin network, the Circle Payments Network on top, and Arc, a new blockchain that needs validators and aligned participants. Plus the literal hard parts: real computational problems in Arc, and being chartered by the OCC and subject to exams to issue a stablecoin. Software is the accelerant, not the moat.

### Key Points

#### Moderator framing: where Mayfield sits (~02:32)

**Matt Carbonara** opened with positioning: Mayfield is a **57-year-old venture fund** currently investing out of funds 19 and 20, based in the Bay Area, having backed **over 700 companies — 125 of which went public and 250 of which were acquired**. He emphasized a people-first approach: entrepreneurs build companies, company-building is a marathon not a sprint, and they don't panic through the ups and downs. They invest from seed and inception through Series B, and up and down the stack — semis, optics, switching, and models; infrastructure software; cyber, cloud, and dev tools; all the way to the application layer.

His question for the session: how do you use the agents everyone had been discussing **in high-risk domains like legal and finance**?

#### Theme 1: What's different about high-risk agents (~02:32–02:36)

**Chandhok** started from the observation that every finance and legal organization he knows **is already using agents** — because they're using coding agents. And coding agents have a wonderful property:

> **Verifiability and testability.** You can go in, read the code, decide if it's too verbose or not verbose enough, whether it has design docs — and you can run a test suite against it and make sure the agent is doing what it's supposed to.

You can do the same things in finance and legal, but **the cost of failure is much higher**. His own example: SOX compliance, or an agent whose job is getting earnings ready ("and I know this because we have earnings next week"). **You cannot take a mistake**, and the scrutiny on that agent will be tremendous. Three things move to a very high bar simultaneously:

1. the **auditability** of the agent's decision-making
2. the **data sources** the agent can access
3. the **verifiability** of the output

His conclusion: **these are among the last flows to get automated**, because so much of a company's existence depends on its ability to get finances right and to keep its legal surface area appropriate. The same holds in other functions like compliance: "We don't want to get hauled in by regulators just because our agent made a mistake. They're going to hold us responsible, not the agent."

**Shafiq** added the framework that anchored the session — **Verifier's Law**:

> Tasks that are easy to verify are going to be ripe for agentic processes. Think of Sudoku — the puzzle is **hard to do but very easy to verify**.

Coding qualifies (QA and tests give you fast verification). Things that are **hard to verify are harder to solve and have a longer lead time**. Self-driving is the classic case: it's very hard to fully verify that the vehicle did the right thing at the right moment. Banking is more extreme still:

> Someone submits a credit card or loan application, and in some cases we don't have a lot of data. If we make an incorrect decision based on the information we have and the person defaults, **that may be five years from the decision**. The decision to give them credit was today; the verification is five years down the road. That becomes very hard.

So their filter is: **which tasks are genuinely ripe for agents that will surpass the human probability of being correct?** Those are where they start.

#### Theme 2: Build vs. buy, and how agents connect (~02:36–02:38)

Asked whether the same judgment applies to in-house and third-party agents, **Shafiq** said hybrid. The models and the intelligence are **largely the same** for everyone, but Wells Fargo has IP and data others don't, which gives homegrown agents an edge for specific things. At the same time, **off-the-shelf agents are becoming so powerful out of the box that it doesn't make sense not to use them** — and the real variable is economics: once costs come down, they'll be pervasive.

The bigger question, in his view, is **how agents connect to each other**:

> The home mortgage process I keep coming back to is a very large, very complex, roughly **1,100-step** process in the bank. It will not be one agent, and it's not going to be a collection of homegrown agents either — it'll be a combination of many things. And it can't be that this agent does its job really well while the other one doesn't, **because they need to talk and connect to each other**.

Especially for long-running systems: "You give a prompt, you get a response back — that's easy, you'll be right. But when you want something done over multiple hours or days or weeks, **the context is where it starts getting a little shady**."

#### Theme 3: Two gaps for entrepreneurs (~02:38–02:39)

Asked whether the long, hard-to-verify work is an entrepreneurial opening, **Shafiq** named two:

1. **The agentic harness.** "The concept sounds so simple — a harness that holds everything together and sits on top of the agent — **but it is incredibly hard to do**, especially for long-running processes." It's something they're actively looking at.
2. **Cross-agent context exchange.** He stressed these are **industry problems, not Wells Fargo problems**. Protocols aren't the bottleneck: "A2A is a great one, and a lot of organizations are building on standard SDKs — that typically is not the issue." The issue is:

> **Optimizing which data to grab for what task. How would a ServiceNow agent collaborate with a Salesforce agent, collaborate with a homegrown agent, and share the right context and the right information?** Very difficult to do. That is a big, big opportunity.

#### Theme 4: Measuring reliability, and when an agent ships (~02:39–02:42)

**Chandhok** said it varies by use case. Citing a talk that morning about how hard evals are and how idiosyncratic each organization is about them, he sharpened the granularity:

> I would say **within organizations, each team is idiosyncratic about evals.** What to measure, how to measure, what "good" means — it needs to be defined process by process by process.

Circle is standing up frameworks for scalable evals. He also warned that **evals break for all kinds of reasons**: model drift, data issues, all manner of things that change how an agent performs. So where they have implemented, they **lock down the model, the harness, and every variable going in besides the input itself**.

They also use what he calls **shadowing**:

> The agent sits with the human. A compliance analyst gets an inbound, they're making a decision and looking at the case; we observe what the human does and what the agent does, then we evaluate that and run it in a reinforcement learning loop.

On KPIs he was candid that things are fuzzy. They're trying to work out **how much token spend equates to what kind of automation**, but they are deliberately **not optimizing for token savings right now** — letting people use the tokens and seeing how much productivity comes out. Productivity shows up in three shapes: **more output per human**, occasionally **revenue** (still small), or an obvious **cost saving / substituting labor that was doing X to do Y**. "It's all of the above. But there's no rule of thumb saying this is how you do KPIs or evals."

#### Theme 5: Weighting engineering effort, and the question enterprises get wrong (~02:42–02:46)

Asked how to weight model vs. harness vs. workflow integration vs. context and memory, **Shafiq** said this is where he spends much of his time. He contrasted the traditional product development lifecycle: an idea, iterated back and forth in a Word doc or PowerPoint, then engineering builds a Figma or prototype, then the development lifecycle with architectural patterns, vulnerability and risk assessment. "Very archaic, very human-driven, very sequential."

In the agentic world he sees two paths: the **technical choices** (memory, infrastructure, own cloud or public cloud) and, more decisively, the **business choices**. Here he flagged another startup signal: only a handful of companies are building frontier intelligence, but **a slew of companies will build the engine that makes it work inside enterprises**, because enterprises need security, governance, and compliance.

Then his sharpest critique:

> Generally the leaders would say, okay, we have this large process — can you use AI and make it simpler, faster, better, more automated? **And that is typically the wrong approach.** The approach would be: what is the art of the possible using AI, and can we **reimagine this whole experience**, and then find a way to go from your current process to that.

He calls this the gap in the enterprise, and paired it with an observation he and Chandhok had discussed in the green room: **ask developers or product managers individually and everyone claims roughly 30% more efficiency** — writing code faster than ever before. But in many cases **that doesn't translate into workflows**.

> The gap is **process engineering**: understanding the domain, the specific data, the use cases, and then working backwards into the right architecture — because **the architecture is starting to become the easier factor in all of this.**

#### Theme 6: Org design and the human-to-agent ratio (~02:46–02:50)

**Chandhok** said Circle is rolling out **the ability for employees to self-publish agents**, along with an **agent gateway**: you can see what all the agents are, find them in Slack, and talk to them.

But he refused the framing:

> I don't foresee a future in which the point person on a project is not a human. A human can go invoke any of the many agents inside this company, query our agent gateway — what agents are available, what finance agent do we have, what marketing agent do we have — and compose them into some kind of solution. **I don't think about it as an org design question, because I don't tell the people working for me how many Google Docs they can open.** They are creating an outcome for us.

His focus is therefore infrastructural: **being able to self-publish, having the data access to self-publish, having the right ACLs to self-publish**, and getting agent-to-agent communication figured out.

On whether organizations change: he thinks they'll be more productive (everyone's experience), and **may reorganize because the lines between function A and function B are blurrier**. The real questions are about team composition: do product managers do more product marketing, does product marketing do more brand, does BD do more product? "Even who shows up on sales calls — **maybe our agent shows up and takes notes.** There are all kinds of efficiencies like this being figured out. But in terms of org design, old-school McKinsey stuff, we're not thinking about it."

**Shafiq** answered the same question from the other end — the biggest non-technical barrier to adopting agents at scale:

> **There are not going to be any individual contributors.** Out of our bank of 200,000 employees, largely they're individual contributors. What does that mean? It means **the ICs now will be managers of agents.**

The friction is that ICs **aren't used to delegating** — they're used to owning work end to end and being fully responsible. Now you get a body of work, you use ChatGPT or Claude or any model, and **you still own the work but you're delegating it** — and that will be the dominant way of working going forward.

So one thing they're doing now is emphasizing that **everyone is going to be a manager**:

> Just like you give feedback to humans, you need mechanisms to give feedback to your agents, to grow your agents and get more out of them. That's very new, because **the playbooks really don't exist.** You're not used to a world of no ICs and all managers.

They're working with their HR team on how to roll that out.

#### Theme 7: Where's the moat once intelligence is democratized (~02:50–02:56)

**Chandhok** started by noting Circle is much smaller than Wells Fargo — at least two orders of magnitude smaller in engineering. Then two layers of answer.

**Layer one is speed**, via a jetpack metaphor:

> There's always a race on — you're in a race with somebody, and now suddenly you can wear a jetpack. If you can master the jetpack you take a lead over the competition. They'll catch up; they'll wear their jetpack and get there as well. So first, **I want to make sure I put my jetpack on and get my organization to put on the jetpack before everybody else does.**

**Layer two is the shape of the business.** He agrees a lot gets commoditized, and that **software-only businesses will be hard to defend** — "I think this is broad consensus." But Circle has harder things:

> We are **a company of networks**. USDC is our core product, and we think about it as a stablecoin network. We have a payments network on top of that, the **Circle Payments Network**. And we're building a new blockchain called **Arc**, which is also a network, because you need validators and participants aligning incentives to participate.

His claim: **network businesses are superior to software businesses, and software is an enabler of these network businesses** — the question becomes how to use software to build software-enabled networks. On top of that sits what he calls **the hard physics of the business**: real computational difficulty in Arc, and the complexity of issuing a stablecoin at all — **you are chartered by the OCC and you have to submit to the exams.** The strategy is to do the hard physics extremely well, move into adjacencies that are also hard physics, and use software as the accelerant on top.

**Shafiq** made the non-technical bottleneck explicit:

> There are going to be amazing changes in banking, and **many of those are not technological challenges.** 24/7 trading — why does trading end at 4:00 PM Eastern? The answer is largely **not technological.** It's not a big issue to enable that technologically. It's that regulators want the movement of money regulated, protecting consumers.

Instant global money is the same: "Yes, I can make the money available — but **if the other bank takes two days to close the book, who's paying for that delta, and what happens when the money doesn't reach?**" The regulatory side has to catch up, and new use cases will arrive as better regulation does.

He then echoed Chandhok with a clarification he clearly felt was needed:

> The software side of it is going to make us do the hardware side of the business really well. And when I say hardware, **I don't mean GPUs.** I know it's an agentic AI conference, but **we still have 4,000 branches.** We still believe there's value in human connection — someone coming in to talk to a bank advisor in Spanish because they only speak Spanish, and building a plan for their financial education.

Those won't go away; **how they're delivered and consumed will change dramatically.** His model-layer prediction: today is dominated by LLMs and the conversation is token cost; eventually it will be **small language models and fine-tuned models**, because that will become as easy as a click of a button — and the center of gravity moves to **vertical, specialized AI**, from which a lot of new use cases will come.

#### Closing: what will be automatable in five years that you can't imagine today (~02:56–02:59)

**Shafiq** named **underwriting**:

> Underwriting is the core for any bank — income verification, home loan verification — and it's a very archaic process. People bring in all sorts of documentation; you may send a utility bill that you photographed at a wrong angle with light hitting it, so someone has to send it back. **A very complex multimodal challenge.**

He expects it to become table stakes over the next couple of years; what holds it back today is compute and economics. He restated the model-layer trajectory (LLMs → small language models and fine-tuned models) and added "**and then quantum, once that compute is available.**"

**Chandhok** took a different turn:

> I'm AGI-pilled, so I believe we will be looking at AGI through our bedroom windows. And at that point, who am I to say what is not solvable?

But his real answer was the panel's best closing:

> It may be **a data center full of geniuses**, but humans are Byzantine. They are idiosyncratic, they are very hard to coordinate. So **it may be very lonely for those data centers full of geniuses** while the rest of us try to coordinate and figure this out. We have really good models, but **I am surprised by how much effort it takes just to convince people to do things even when those things are objectively good for them.** Does anybody have a parent you've tried to get to take their medicine? Or children, for that matter. It's objectively good for them. They will refuse.

> Human society is not ready to just take it from these data centers full of geniuses. That is my conclusion. I want those data centers around and I'm very glad they are here — but **we have a lot of problems to solve between now and this future that we're imagining.**

### Quotes

> "Tasks that are easy to verify are going to be ripe for agentic processes. ... Same thing in banking: the decision to give them credit was today; the verification is five years down the road." (~02:35, Faraz Shafiq)

> "We don't want to get hauled in by regulators just because our agent made a mistake. They're going to hold us responsible, not the agent." (~02:34, Nikhil Chandhok)

> "I would say within organizations, each team is idiosyncratic about evals." (~02:40, Nikhil Chandhok)

> "Can you use AI and make it simpler, faster, better, more automated? And that is typically the wrong approach." (~02:44, Faraz Shafiq)

> "There are not going to be any individual contributors. ... The ICs now will be managers of agents." (~02:49, Faraz Shafiq)

> "It may be a data center full of geniuses, but humans are Byzantine. ... It may be very lonely for those data centers full of geniuses while the rest of us try to coordinate." (~02:58, Nikhil Chandhok)

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Verifier's Law | 「容易驗證的任務適合 agentic 流程」的原則,Shafiq 用它排自動化順序 | The principle that easily verified tasks are ripe for agentic processes; Shafiq uses it to order automation | 講者未指名出處 / no source cited by the speaker |
| A2A (Agent2Agent) | 講者稱為「很棒的協定」;他認為協定不是瓶頸 | Called "a great one" by Shafiq; protocols aren't the bottleneck in his view | |
| Circle Payments Network | 建在 USDC 穩定幣網路之上的支付網路 | Payments network layered on the USDC stablecoin network | |
| Arc | Circle 正在建的區塊鏈,需 validator 與參與者對齊誘因 | The blockchain Circle is building; requires validators and aligned participants | Chandhok 稱其含「硬運算」問題 |
| Agent gateway (Circle) | 讓員工自行發布 agent、在 Slack 中查找與呼叫 | Lets employees self-publish agents and find/invoke them in Slack | 導入中 / being rolled out |
| Shadowing | agent 與人同時處理同一筆案件,比對後跑 RL 迴圈 | Agent and human work the same case; the comparison feeds an RL loop | Circle 的 eval 做法 |
| 房貸流程(~1,100 步) | Shafiq 全場的主要例子 | Shafiq's running example of a ~1,100-step process | 見 `faraz-shafiq--reimagining-banking-in-the-ai-era.md` |
| OCC | 美國貨幣監理署;發行穩定幣須受其特許與檢查 | Office of the Comptroller of the Currency; stablecoin issuance requires its charter and exams | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Nquille / Nikil / Nichol / Nikl | Nikhil (Chandhok) |
| far / Faras | Faraz (Shafiq) |
| verifiers law | Verifier's Law |
| sedukco / sudukco | Sudoku |
| socks compliance | SOX compliance |
| Mckenzie | McKinsey |
| the OC | the OCC |
| Service Now | ServiceNow |
| generic agents(主持人提問) | agentic agents |
| AGI build | AGI-pilled |

## 待確認 / To Verify

- **Verifier's Law** 講者未指明出處;若要引用需回查該詞的原始提出者與定義。/ Shafiq cited "Verifier's Law" without attribution; trace the original formulation before citing.
- Chandhok 引用「早上一場關於 eval 的演講」,未指名講者或場次。/ Chandhok referenced a morning talk on evals without naming the speaker or session.
- 「房貸約 1,100 步」「Wells Fargo 20 萬名員工」「4,000 家分行」「Mayfield 700+ 投資 / 125 IPO / 250 併購」皆為口述數字,未附出處。/ The ~1,100 steps, 200,000 employees, 4,000 branches, and Mayfield's 700+/125/250 figures are all as spoken, with no sources given.
- 「開發者與 PM 個別聲稱效率提升約 30%」為 Shafiq 的觀察,非引用研究。/ The "~30% more efficient" figure is Shafiq's observation, not a cited study.
- Chandhok 說 Wells Fargo 的工程組織「至少大兩個數量級」是現場口語估計。/ Chandhok's "two orders of magnitude" comparison was an offhand estimate.
