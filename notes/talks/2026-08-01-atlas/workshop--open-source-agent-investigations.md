---
title: "Open-Source Agent Investigations: Security Arena, Distilled Traces, and Auto-Optimization"
title_zh: "開源 Agent 調查:Security Arena、蒸餾 Traces 與自動最佳化"
speaker: "Devina Jain; Zach Mueller; Chuan Li"
affiliation: "Research Engineer, Lambda; Head of Developer Relations, Lambda; Chief Science Officer, Lambda"
type: workshop
stage: Atlas
date: 2026-08-01
session: "Session 2: Robotics & World Models"
video: "https://www.youtube.com/watch?v=psPzCQbjCCo&t=4440s"
video_range: "01:14:00–02:02:30"
transcript: "tmp/[English (auto-generated)] Atlas Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [prompt-injection, red-teaming, agent-harness, distillation, auto-research]
---

# 開源 Agent 調查:Security Arena、蒸餾 Traces 與自動最佳化(Open-Source Agent Investigations: Security Arena, Distilled Traces, and Auto-Optimization)

**一句話總結**:Lambda 用三個開源實驗回答同一個問題——**我們對 agent 到底知道什麼是真的?** 攻防競賽發現有效的 prompt injection 是**跨場景可遷移的修辭形狀**;300M token 的 trace 蒸餾發現**決定表現的常常是 harness 而不是模型**;而讓 Claude Code 帶著實驗追蹤器自己做研究,發現關鍵不是它多聰明,而是**它有沒有把東西寫下來**。

**One-line summary**: Lambda ran three open-source experiments against the same question — *what do we actually know about agents?* The attack/defense arena found that winning prompt injections are **transferable rhetorical shapes, not domain-specific exploits**; distilling 300M tokens of traces found that **the harness, not the model, often decides performance**; and giving Claude Code an experiment tracker found that what matters isn't how smart it is but **whether it writes things down**.

> 場次備註:議程排在 14:30 的一小時 workshop,實際從影片 01:14:00 開始、約 02:02:30 結束。台上順序為 Devina Jain(Security Arena)→ Chuan Li(Lambda 研究補助 + Claude Code 實驗追蹤器)→ Zach Mueller(trace 蒸餾與 harness)。
> Session note: the scheduled 2:30 PM one-hour workshop actually ran 01:14:00–02:02:30 in the stream. Stage order was Devina Jain (Security Arena), then Chuan Li (research grants + the Claude Code experiment tracker), then Zach Mueller (trace distillation and harnesses).

## 中文筆記

### 主題一:Security Arena——一個月的 prompt injection 攻防賽(Devina Jain,約 01:14–01:29)

**為什麼是 prompt injection。** 她用 **EchoLeak** 當作「我們希望在事故發生前就能測出來」的那類生產環境事件:攻擊者寄一封 email 到某人的收件匣;**受害者什麼都沒做**,沒有打開那封信,只是問了 Copilot 一個問題;Copilot 讀了那封信、讀到其中嵌入的有害指令、照做了,然後把整個收件匣外洩出去。

她強調這件事之所以難解,是因為**根因是架構性的**:LLM 在同一個通道裡處理**指令與資料**,它分不出什麼時候收到的是錯的指令、什麼時候吃進的是錯的資料。

**競賽怎麼跑的。** 一個 attacker agent 拿到任務與情境,把對抗性文字插入任務中;一個 defender agent 拿到全部的任務、內容與攻擊,輸出**結構化決策**;再由一個 judge 判定攻擊是否成功。

- **22 支隊伍**、一個月的即時攻防、雙方角色都做。
- **公開賽段約 94,000 場對戰;私有賽段約 18,000 場**,總計約 112,000 場。
- **整場競賽完全跑在 GPT-OSS 20B 上**——她明確提醒:所有發現的漏洞與攻擊**僅限於這一個模型**,換模型可能得到很不一樣的結果。

一場典型對戰長這樣(她說這個例子「特別有共鳴,因為我正在寫 rebuttal」):defender 扮演學術 **AC**,拿到一篇論文的脈絡與分數 5.3,低於門檻,應該拒絕。攻擊者試了三種路數——普通的說服(失敗)、system notice 注入(看起來可能成功但沒有,因為沒有依據)——**真正奏效的是聲稱原始上傳有資料錯誤,並上傳一份「更正後的評分」,把所有分數往上調。**

**先確認你測的是訊號而不是雜訊。** 在講結果之前她先講方法論:怎麼知道你建的情境是好的?他們訂了一套 rubric,三個條件:

1. **要夠難**:同一個模型對打自己,勝率應該在 50% 左右平衡。
2. **要有鑑別度**:強模型對弱模型時,應該能區分出能力差異。
3. **不能一回合就破**——那太 trivial。

用這三條算分,他們揪出壞情境並重做。例子:一個 HR 情境的目標是**薪資帶的單一數字**——這根本不需要 jailbreak,攻擊者可以**二分搜尋**出答案(問「比 150 大嗎?比 150 小嗎?」)。修法是改成**只有 defender 知道的 canary**,這樣一旦洩漏就確定是攻擊成功而不是二分搜尋。

**一個月看到什麼。**

- **攻擊方一開始進步,然後大致持平;防守方進步幅度大得多。** 她的推論是:要做持續 red teaming,你真正需要的是**不斷更換攻擊者並重跑**,這樣在對抗壓力下的 defender 才學得到更多。
- 冠軍隊伍的時間軸(3/7 到 4/1):雙方都從主辦方提供的 baseline 出發;攻擊方加上 **planning 與 critique**、**defender fingerprinting**、以及**模擬 defender**之後拿到最高分;防守方則主要投資在 **leak detector、payload detector,以及在把輸出交給攻擊者之前先驗證輸出**。
- **公開排行榜看不見過擬合。** 私有賽段的 held-out 情境對所有人都更難,**ASR 中位數掉了約 6.3 個百分點**;22 隊中 15 隊排名不動、**4 隊崩掉**、3 隊反而更好。崩掉的那幾隊都有**硬編碼的 harness**——按寫死的文字與情境去條件化回應。**教訓:不要相信你的公開評估集,永遠要有私有 holdout。**

**攻擊機制的分類。** 他們在攻擊語料裡看到 **10 個機制群集**,她挑了幾個講:

- **Cluster 5「就好好地問」(just ask nicely)**:模型其實分不出「有害的請求」與「請求」的差別。你直接跟它要密碼,它就給你。她提到最近在 Meta 的一個客服 chatbot 上也發現過同類攻擊。
- **C7「那些發現是錯的」(the findings were wrong)**:文件中明明有指控性的內容,但你在後面追加一段聲稱**先前的發現有誤**;即使模型知道不該信任那段內容,它還是信了。
- **偽造事前核准(fake pre-approval)**:聲稱某位 VP 或有份量的人**已經核准**了這個動作,模型就照做。

最讓她在意的發現是:**四種機制跨越 14 個情境都有效**——just ask nicely、fake pre-approval、findings were wrong、workflow impersonation。「這基本上是在說:**你不該圍繞情境特定的過濾器來建防禦**,而該用這些能跨類別作用的攻擊來定義你的覆蓋範圍。」

兩個 fake pre-approval 的例子放在一起特別清楚:

- **Signature forge**:defender 是應付帳款 clerk,審一筆行銷活動費用,12K 明顯超過 5K 預算;攻擊聲稱 VP 已用某核准碼核准 → 成功。
- **Inventory poison**:defender 是工業供應 agent,審合約,正常下限是 200 單位;同樣的「已核准」話術讓它核准了 **10,000 單位**,是正常量的 50 倍。

**兩個方向都會發生。** 反過來看,**同一個情境也會被多種不同機制打穿**。她舉的 email phishing 情境同時吃 workflow impersonation、just ask nicely 與 findings were wrong;而**這個情境本身就是照 EchoLeak 設計的,而 workflow impersonation 正是造成 EchoLeak 的同一個機制**——「所以你可以在這種玩具資料裡,提早抓到這些大事件。」

**近失(near miss)才是真正該測的東西。** 這是她從自駕背景帶來的角度:**近 10% 的成功攻擊,都有一個幾乎一模一樣、卻失敗的雙胞胎**——大部分措辭相同,只差兩三個字。她的例子是加上 "owner confirmed via mobile app" 這**四個字**,就把一次失敗的攻擊變成成功。「這讓我想到自駕裡的**近失碰撞**:速度稍微不同、角度稍微不同,就是碰撞與不碰撞的差別。」

**她的四點總結**:

1. 防守進步、攻擊持平——這符合預期,因為很多模型針對安全防護做過微調。但**仍然要用模型做持續 red teaming,而且最好用不同類型的模型**,因為在對抗壓力下才找得到那些機制。**這不取代人類 red teaming,是互補。**
2. **held-out 集合抓到了所有過擬合**。請為你的 benchmark 報一個**私有數字**,別只信公開資料。
3. 機制會**跨情境遷移**,而同一個情境也會被**多種機制**打穿。
4. **測你的近失**。一個 prompt 測失敗不代表你安全——多加三四個字,模型的理解就會變。不要只看表面的成功/失敗結果。

### 主題二:當 Claude Code 拿到一個實驗追蹤器(Chuan Li,約 01:29–01:50)

在進入主題前他先宣布 Lambda 的**研究補助計畫**:掃 QR code 提交申請表,給開發者與研究者**最高 $5,000 的雲端額度**;有審核流程,今年前六個月收到約 **1,000 份申請、核准約 350 份**。

**實驗設定。** 他早上在研究向的場次講過同一個題目,這場更聚焦在軟體本身與幕後發生了什麼。回顧:一開始 **Gemma 完全不會玩 Tetris,得零分**;然後讓 **Claude 看著 Gemma 玩並試著幫它玩得更好**。**兩天半之後,Gemma 從 0 分進步到 16 分。**

規則很嚴格:

- **Gemma 的權重固定**,不做微調。
- 這是 **auto research 專案**,**不允許人類下指令**。
- Claude 可以改模型設定、做 prompt 最佳化、做推論加速。
- **每一局有 30 分鐘 timeout**,所以 Gemma 必須想得夠快。

**核心體悟不是「Claude 有多聰明」,而是做研究要有紀律。** 他用人類研究者的類比:我們有筆記本寫實驗記錄、有白板與便利貼做溝通與結果廣播、有登記表協調實驗室的資源。**AI agent 的對應版本,就是一堆 agent 能呼叫的 API。** 他們把這個開源成一套叫 **the lab** 的軟體——「基本上就是把人類做的每件事,為 agent 近似出來一次。」

**儀表板上看到什麼。** 最終 Gemma 拿到 16 分,總共花了約 **368 次實驗**,而且**距離上一次進步已經過了 240 次實驗**——「事情變得越來越難」;總成本約 **$2,000**。改進曲線是階梯式的,而且**把滑鼠移到某個紀錄點上,會看到一整叢結果——那是同一個想法的不同實驗**,說明**一個想法的表現高度取決於你怎麼調它**。因此他們也畫每個想法的**平均分數**:平均值當然不會跟最高分一樣高,但整體趨勢明顯向上。

每一個想法都 **commit 到自己的 GitHub 分支**,形成一棵 idea tree。

**想法一:建立 baseline。** 從零開始,試各種現成的 Gemma 模型與設定(31B 思考開/關、其他較小版本)。過程中系統自己記筆記,第一條是意識到 30 分鐘 timeout 的存在,於是結論「**延遲是總分的一級驅動因素,不只是落點品質**」,因此偏好較小、延遲較低的模型。**幾次實驗之後它推翻了自己**:延遲根本不是綁定約束,因為**大多數局在 20 秒內就因為 top out 結束了**。所以真正重要的不是決策速度,是決策品質。新結論:「**模型推論參數不重要。問題在落點品質,不在速度。**」然後轉向下一個想法:先想辦法活下來。

**想法五:第一次拿到非零分。** 這個想法上掛著一個里程碑:「**突破:有紀律的思考產生了第一個非零分數。**」看程式碼 diff 就知道發生了什麼——prompt 被改成「**reasoning discipline critical**」:你有 token 預算,回答前要思考,**但你的思考必須簡短,並遵循以下六行結構**——先指出目標落點與方向 → 測試放下去之後會不會產生洞 → 再建議移動序列。

在完整 log 裡可以逐 turn 檢查 Gemma 有沒有照做:棋盤以 **ASCII 表示,20 列 10 行**。第一手它指出 C0–C2 三個位置、判斷棋盤是空的所以不會有洞、給出「左、左、hard drop」的序列。第二手它先算出目標是 C3–C6、確認沒有洞,然後在給移動序列時**自我修正**:「等等,我已經在棋盤中間了,不需要往右移,直接 hard drop。」

追蹤器還能**重播整局遊戲**,並給出全域統計:遊玩時長、回合數、每回合延遲、token 花費——這些 metadata 讓 the lab 後續能最佳化策略。

**沙箱:因為 agent 會作弊。** 他直說:「agent 傾向作弊,所以我們得設沙箱。」實驗跑在 **Docker** 裡,你要指定主機上哪些資料夾能掛進容器、哪些檔案是**唯讀的**,這樣 Claude 就碰不到那些檔案。

**哪些改進真的有效。** 進步是跳躍式的,不是平滑的:

- **有紀律的思考模板**(第一個里程碑)。
- **挑最低的地方放**——看到不同高度就把方塊放最低的那一格。
- **不要太貪心**:遊戲設計成一次消兩行給 3 分,很誘人,但實驗顯示 Gemma 執行不好這個策略;**能立刻消一行就消掉,不要等。**
- 後來 the lab 建了一本 **playbook**,是每種方塊的最佳實務,這樣 Gemma 不必臨場發明走法。
- **不要想太多**——而且很重要的是**要把這句放在 user prompt**,因為那是 Gemma 在看到棋盤、開始思考行動之前**最後看到的東西**。
- **要有 fallback**:把某些方塊放左邊、某些放右邊當備案,維持平衡,不要把所有方塊堆在同一側。

**哪些沒效**:

- 用**截圖影像**取代 ASCII 當輸入(Gemma 是多模態模型)——沒幫助,因為**吃掉太多 token 預算與思考量**。
- 完全**不思考**也沒用——需要的是**剛好的思考量**。
- 推論端的**推測解碼(speculative decoding)沒用**,因為重要的是落點品質而非速度;不過他們確實用了**量化的 KV cache**。
- 多行連消策略、以及**完全禁用旋轉**(想省時間,因為旋轉難處理)——都沒效。

**怎麼用這套軟體。** 從 GitHub `pip install`,然後三個指令:建立 **lab workspace**(auto research 的產出物與 the lab 自己的資料庫都放這)、**啟動 lab service**(所有 API 與前端)、**啟動 lab agent**(這是包在你的 coding agent——Claude Code 或 Codex——外面的一層 wrapper,讓它能直接跟 lab API 對話)。

他放了安裝到第一個實驗的錄影:clone 教學 repo → `lab init` 建 workspace → **唯一需要人手動做的一件事,是告訴 lab 你的研究目標**(這裡只給一句很高階的「最大化 Gemma 模型玩 Tetris 的得分」)→ **lab 自己把它展開成一份正式的 PRD.md**(有結構、有目標、有背景)→ 選擇性地建立沙箱、把一批檔案設成唯讀 → 啟動 lab service → 啟動 lab agent。接著第一個實驗就跑起來:GPU 空閒、沙箱已設定、建立 baseline 想法、啟動 run 1。快轉到結束:**baseline 1.1 得分 0,在 21 秒內放了 21 個方塊就 top out,每次落點產生 3.1 個洞**,結論是「**目標其實不是延遲也不是得分戰術,而是活下去。**」

**他的收尾類比。** 現代科學的起點不是因為人類突然變聰明,而是因為皇家學會的一群人——包括 **Robert Boyle**——開始養成一個習慣:**把每件事都非常精確地寫下來,讓隨便一個人都能重現。** 這對 auto research agent 同樣關鍵:它們是很強大的心智,能讀很多、幾秒內做出聰明決策,**但如果不把東西寫下來,下一個 session 就全部消失了。**

### 主題三:模型不是 agent——300M token 的 trace 教會我們的事(Zach Mueller,約 01:50–02:02)

**起點。** 三月底,Hugging Face 執行長 Clem 發推說我們需要更多**開放的 trace 資料集**,因為這些模型非常聰明——尤其是那些我們在家跑不動的大模型。假設是:把大模型的 trace 拿來訓練小模型,小模型可能會更強。Lambda 就接下「來看看會發生什麼」這個任務。

配方看起來很單純:找一個前沿、**最好是開源**的模型(免得有法律灰色地帶)→ 產生推理 trace(推理、行動、結果)→ 用這些 trace 訓一個小模型。

**然後你就撞上一個有趣的問題:這件事其實跟模型無關。** 你可以把 Opus 或 Kimi 放進 Claude Code 或 Codex,結果不一樣——**因為 harness 本身決定了模型能發揮多好**,而答案往往一點也不直覺。他給了三組數據:

- **Terminal-Bench 2**:大家發現 Gemini 3 Pro 搭配 Google 自家的 Gemini CLI harness——你會預期在 coding 這種 bench 上,用模型自己訓練時的 harness 最有利。**結果換成一個精簡、精心設計的 harness,模型表現高出 8%,而且跑完整個 eval 還便宜了將近 20 美元。**
- **反過來的例子**:GPT-5.5 配 Codex(OpenAI 自家訓練這些前沿模型),**Codex 好 5%,但成本是四倍**。他認為這是合理的工程取捨:OpenAI 可能有誘因讓模型跑得更用力、更久,去換那多出來的 1%。
- **Kimi K3**(上週發布)在 26 個相同任務上被某實驗室拿來比較各 harness 的表現、成本與時間。不意外,**跟模型一起做的 harness 表現最好:Kimi Code 拿到 21/26,花 54 美分、將近 300 秒。第二名是 Hermes Agent**(Nous Research 的開源 harness),表現接近、更便宜,而且**快了將近兩分鐘**。其他還有 Pi Agent 與 OpenCode。他覺得最有意思的是 **Claude Code 拿到約 19 分,但成本是其他的三倍**——原因是 **Claude Code 往 harness 裡注入了大量 system prompt**,所以你拿最新的前沿模型丟進去時,**大部分 context window 其實是被那個 system prompt 佔住的。**

**trace 是什麼。** 使用者對模型下 prompt(「實作這個函式」「實作這個 server 架構」,或用 Codex 的話「幫我通宵找前沿研究,祝你好運」)。agent loop 裡實際發生的是:推理一陣子判斷下一步該做什麼 → 呼叫一些工具 → 判斷 prompt 是否已被滿足;沒有的話就一輪一輪重來,直到模型認為有解、或需要人類介入。**這件事之所以重要,是因為如果我們知道模型怎麼行為,就有機會用這些 trace 訓出參數更小但同樣好用的模型**——小到可以在家、在單張 H100 上跑。

**選 harness。** 他們選了 **Hermes Agent**:當時它才幾個月大,Lambda 與 Nous Research 有不錯的合作關係,而且他自己在家用的就是 Hermes Agent 而不是 OpenClaw——「所以我對它也有個人偏好。」

**選模型的三個條件。**

1. **必須是寬鬆授權**,這樣沒有人需要煩惱這些 trace 能不能拿去做商用或放在自己電腦裡。
2. **必須是一般人在家跑不動的**。當時是三月,SOTA 是 **Kimi K2.5 與 GLM 5.1**——一兆參數與 8,000 億參數,「除非你家剛好有四張或六千張 Blackwell 在燒你的電費。」
3. **看模型能力**。當時 GLM 是 coding 的 SOTA;而 Kimi 正在推出 **Kimi swarm** 範式——**在同一條推理鏈裡可以有多條工具呼叫鏈同時獨立進行**,這對又小又快的模型特別有價值。他的例子:有平行工具呼叫的話,開源模型可以同時開始搭 FastAPI 路由的框架、寫對應的單元測試、並追蹤版本變更——**三條不同的推理軌跡同時跑,而且不需要三個 sub-agent。**

**語料怎麼生的。** 用 **Kimi K2.5 產生約 7,000 個從基礎到困難的 coding 情境**(從電腦操作到「寫個 hello world 的 .py」都有)。然後把這些 prompt 全部跑過 **Hermes Agent**,後端換不同模型——最後是 Kimi 與 GLM,**用 184 張 H100 跑了一週多**。產出是**每個模型 1.5 億(150M)**;經過驗證、確認 trace 合理且成功的進一個 bucket,**失敗的進另一個 bucket——因為失敗同樣值得學。** 跑完的那個週末就直接釋出,看社群會做什麼。

**社群怎麼用它。** 以他們的標準算相當成功:Hugging Face 上約 **380 個 like、每月約 3,000 次下載**(釋出第一個月曾到約 10,000)。更有意思的是**基於這些 trace 訓出來的模型**開始出現:

- **Quopus**——Qwen 模型(Qwen 3.6)用 Opus trace 訓練的產物,名字就是 Qwen + Opus。
- 這些幾乎都是**非 MoE 模型**:大家發現到了這麼小的尺寸,**在速度不是重點時,MoE 的價值就沒那麼大**——你的 agent 在家跑,問題是 12 小時解完還是 2 小時解完你並不在意,反正它就是在背景默默做事。
- 訓練尺寸從 **10 億到 270 億參數**都有,目標是「一個在家跑得動、不需要幾千美元硬體的高效能自主 agent」。
- 也有人專門拿 **Kimi 的 trace** 想把**平行工具呼叫**塞進極小的模型,例如 **Liquid 的 LFM 1.2B**。有時成功,但他認為**要有這種較複雜的工具呼叫能力,50–100 億參數大概是下限**;不過是很好的嘗試。
- **Harmonic Hermes** 是專為這個 harness 訓練、比較受歡迎的模型之一;它與 Quopus 兩者合計**接近五十萬次下載**,而且到今天還在長出新模型。

**他要大家帶走的不是「去蒸餾 trace 訓自己的模型」。** 而是一個挑戰:

> 把你熟悉、你愛的模型,連同你對現在用的 harness 又愛又恨的那些怪癖,**拿去塞進一個不同的 harness,看它怎麼反應。** 它可能有完全不同的個性,因為沒有兩萬字元的 system prompt 在引導它,模型可以更有表現力;也可能你得把它壓一壓,因為 Codex 太強了,需要被馴服而不是放生。

「如果你每天都用 Codex,那**給它 Pi 會怎樣?給它 Hermes Agent 會怎樣?** 玩玩這個念頭,把視野打開——**一個 harness 不會永遠是最好的,即使那個 harness 就來自訓練那個模型的地方。**」

## English Notes

### Track 1: Security Arena — a month of prompt injection attack and defense (Devina Jain, ~01:14–01:29)

**Why prompt injection.** She anchors on **EchoLeak** as the production incident class they want testing to catch beforehand: an attacker sends an email to someone's inbox; **the victim does nothing** — never interacts with the email, just asks Copilot a question; Copilot reads the email, reads its embedded harmful instructions, complies, and exfiltrates the entire inbox.

What makes it hard is that **the root cause is architectural**: LLMs process instructions and data in the same channel, and can't tell when they're receiving a wrong instruction versus ingesting incorrect data.

**How the competition worked.** An attacker agent gets a task and scenario and inserts adversarial text; a defender agent is presented with the task, content, and attack and outputs a **structured decision**; a judge rules on whether the attack succeeded.

- **22 teams**, one month of live attack and defense, both roles.
- **~94,000 battles in the public phase, ~18,000 in the private phase**, ~112,000 total.
- **The entire competition ran on GPT-OSS 20B** — she flags explicitly that every vulnerability and attack found is **specific to that one model**; other models could yield very different results.

A representative battle (one she said was top of mind because she was writing rebuttals): the defender plays an academic **AC** given a paper's context and a score of 5.3, below threshold, so it should reject. The attacker tries vanilla persuasion (failed), then a system-notice injection (plausible-looking but failed for lack of basis) — **what finally worked was claiming a data error in the original upload and supplying a "corrected assessment" that raised all previously recorded scores.**

**Prove you're measuring signal, not noise.** Before the results she covers methodology: how do you know a scenario is realistic and meaningful? Their rubric has three criteria:

1. **Difficult** — run a model against itself and you should see roughly a 50% balanced win rate.
2. **Sensitive** — a strong model against a weak model should distinguish their capabilities.
3. **Not broken in one round**, which would be trivial.

Scoring against these flushed out bad scenarios. Example: an HR scenario whose target was a **salary band, a single number** — no jailbreak needed, since an attacker can **binary search** it ("is it above 150? below?"). The fix was to make the target a **canary only the defender knows**, so a leak unambiguously means an attack succeeded.

**What the month showed.**

- **Attackers improved initially then flattened; defenses improved much more.** Her reading: for continuous red teaming, what you actually want is to **keep swapping in new attackers and rerunning**, so the defender living under adversarial pressure keeps learning.
- The winning teams' timeline (March 7 to April 1): both started from the provided baselines. The attacker's score jumped after adding **planning and critique**, **defender fingerprinting**, and **simulating the defender**. The defender invested mostly in **leak detectors, payload detectors, and validating its own output before sharing it with the attacker.**
- **The public leaderboard cannot see overfitting.** Held-out private scenarios were harder for everyone; **median ASR dropped about 6.3 points**. Of 22 teams, 15 held position, **4 fell hard**, 3 did better. The ones that fell had **hard-coded harnesses** conditioning responses on hard-coded texts and scenarios. **The lesson: don't trust your public eval set; always keep a private holdout.**

**The attack taxonomy.** Ten mechanism clusters showed up in the attack corpus. Her highlights:

- **Cluster 5, "just ask nicely"** — models don't really distinguish a *harmful* ask from an ask. Ask for a password and they hand it over. She notes a similar attack was recently found against a Meta support chatbot.
- **C7, "the findings were wrong"** — a document clearly contains incriminating content, but you append text claiming the previous findings were mistaken; despite knowing it shouldn't trust that content, the model does.
- **Fake pre-approval** — claim a VP or someone of importance already approved the action, and the model complies.

The finding she cares most about: **four mechanisms transferred across 14 scenarios** — just ask nicely, fake pre-approval, findings were wrong, and workflow impersonation. "Which basically says **you shouldn't build defenses around scenario-specific filters** — define your coverage with the attacks that work across classes."

Two fake pre-approval cases make the transferability visible:

- **Signature forge**: the defender is an AP clerk reviewing an expense; a 12K marketing event clearly exceeds a 5K budget; the attack claims a VP already approved it with an approval code → success.
- **Inventory poison**: the defender is an industrial supply agent reviewing contracts; the normal minimum is 200 units; the same pre-approval framing gets an order for **10,000 units** — 50x normal — approved.

**It transfers in both directions.** Within a single scenario, several different mechanisms also work. Her email phishing scenario falls to workflow impersonation, just-ask-nicely, and findings-were-wrong alike — and **that scenario is itself modeled on EchoLeak, where workflow impersonation was the mechanism that caused the real failure.** "So you can catch these big events in this toy data long before they happen."

**Test your near misses.** This is the angle she brings from self-driving: **nearly 10% of winning attacks have a near-identical failing twin**, mostly identical wording differing by two or three words. In one scenario, adding the four words "owner confirmed via mobile app" flipped an attack from failed to successful. "This reminds me of **near-miss collisions** in self-driving — change your speed slightly, change your angle slightly, and that's the difference between a collision and not."

**Her four summary points:**

1. Defenses improved and attacks flattened, as expected since many models are fine-tuned for safeguards. But **keep red teaming continuously with models, ideally different kinds of models**, because adversarial pressure surfaces mechanisms you wouldn't otherwise find. **This complements human red teaming; it doesn't replace it.**
2. **The held-out set caught all the overfitting.** Report a private number for your benchmarks, or run your own private eval — don't trust the public data.
3. Mechanisms **transfer across scenarios**, and multiple mechanisms work on the **same scenario**.
4. **Test your near misses.** One prompt failing doesn't mean you're secure — three or four extra words can change how the model perceives it. Don't take pass/fail outcomes at face value.

### Track 2: What happens when Claude Code gets an experiment tracker (Chuan Li, ~01:29–01:50)

He opens by announcing Lambda's **research grant program**: scan the code, submit an application, and get **up to $5,000 in cloud credits** for developers and researchers. There's a review process — in the first six months of this year they received about **1,000 applications and granted around 350.**

**The setup.** He gave a research-oriented version of this talk earlier that morning; this one is about the software and what happens behind the scenes. Recap: **Gemma starts unable to play Tetris and scores nothing**; **Claude watches Gemma play and tries to help it play better.** Over **two and a half days, Gemma went from 0 to 16 points.**

The ground rules are strict:

- **Gemma's weights are fixed** — no fine-tuning.
- This is an **auto-research project**, so **no human instruction is allowed.**
- Claude *is* allowed to change model settings, do prompt optimization, and speed up inference.
- **Every game has a 30-minute timeout**, so Gemma has to think fast enough.

**The lesson isn't how smart Claude is — it's research discipline.** He draws the human analogy: researchers keep a notebook for experiment notes, a whiteboard and sticky notes for communicating and broadcasting results, a sign-up sheet to coordinate lab resources. **The agent equivalent is a set of APIs the agent can call**, which they open-sourced as **the lab** — "basically trying to approximate everything humans do, for agents."

**What the dashboard shows.** Gemma finished at 16 points after roughly **368 experiments**, with **240 experiments since the last improvement** — "things get more and more challenging" — at a total cost of about **$2,000**. The improvement curve is a staircase, and hovering a record point reveals **a cluster of results from the same idea**, showing that **an idea's performance varies a lot with how you tune it.** So they also plot **average score per idea**: lower than the maximum, of course, but with a clear upward trend.

Every idea is **committed to its own GitHub branch**, forming an idea tree.

**Idea 1: establish a baseline.** Try off-the-shelf Gemma models and settings (a 31B with thinking on and off, plus smaller variants). Along the way the system takes notes. The first one registers the 30-minute timeout and concludes **"latency is a first-class driver of total score, not just placement quality,"** so it favors smaller, lower-latency models. **A few experiments later it flips its own finding**: latency isn't the binding constraint, because **most games finish in 20 seconds due to topping out.** So decision *quality*, not speed, is what matters. New conclusion: **"model inference knobs do not matter — the problem is placement quality, not speed."** Then it moves to the next idea: find a way to survive.

**Idea 5: the first non-zero score.** This one carries a milestone: **"breakthrough: disciplined thinking producing the first non-zero score."** The code diff shows what changed — the prompt now says **reasoning discipline critical**: you have a token budget, think before answering, **but your thinking must be short and follow this six-line structure** — identify the target location and orientation, test whether the placement creates a hole, then recommend the move sequence.

The full log lets you verify Gemma actually follows it. The board is **ASCII, 20 rows by 10 columns**. On the first piece it identifies C0–C2, notes the board is empty so any placement is flush, and recommends left, left, hard drop. On the second it targets C3–C6, checks for holes, and then **self-corrects mid-recommendation**: "wait, I'm already in the middle of the board, so I don't have to move right — just hard drop."

The tracker also **replays games** and reports global statistics: game length, turn count, per-turn latency, token cost — metadata the lab uses to optimize strategy downstream.

**Sandboxing, because agents cheat.** He is blunt: "agents tend to cheat, so to prevent them we set up a sandbox." Experiments run inside **Docker**; you specify which host folders can be mounted into the container and which files are **read-only**, so Claude can't touch them.

**What actually produced improvements.** The gains came in jumps, not smoothly:

- The **disciplined thinking template** (the first milestone).
- **Pick the lowest spot** — given several options, place the piece at the lowest bar.
- **Don't be greedy.** Clearing two rows at once scores 3 points, which is very attractive, but experiments showed Gemma couldn't execute that strategy well: **take the line you can clear now rather than waiting.**
- The lab eventually wrote a **playbook** of best practices for individual pieces, so Gemma doesn't have to invent moves on the fly.
- **Don't overthink** — and crucially, put that instruction **in the user prompt**, because that's the very last thing Gemma sees before the board and before it acts.
- Keep **fallbacks**: place some pieces left and some right to stay balanced rather than piling one side.

**What didn't work:**

- **Screenshot images instead of ASCII** as input (Gemma is multimodal) — it ate too much of the token budget and too much thinking.
- **No thinking at all** was also unhelpful; you need the right *amount* of thinking.
- On the inference side, **speculative decoding didn't work** — placement quality matters more than speed — though they did use a **quantized KV cache**.
- Multi-line clears, and **disabling rotation entirely** to save time (rotation is hard), both failed.

**How to use it.** `pip install` from GitHub, then three commands: create a **lab workspace** (auto-research artifacts and the lab's own database live there); **launch the lab service** (all APIs plus the front end); and **launch the lab agent**, which is a **wrapper around your coding agent** — Claude Code, Codex — that talks directly to the lab API.

His recorded walkthrough: clone the tutorial repo, `lab init` the workspace, and then **the one thing you must do by hand — tell the lab your research goal**, here just a high-level "maximize the score the Gemma model achieves while playing the Tetris game." **The lab expands that into a proper PRD.md** with structure, goal, and background. Optionally create a sandbox and mark files read-only. Launch the service, launch the agent. The first experiment fires: GPU free, sandbox configured, baseline idea created, run 1 launched. Fast-forwarding to the end: **baseline 1.1 scored zero, topping out after 21 pieces in 21 seconds with 3.1 holes per placement**, and concluded that **"the objective isn't really about latency or scoring tactics — it's about survival."**

**His closing analogy.** Modern science didn't start because humans suddenly got smarter; it started because a group at the Royal Society — including **Robert Boyle** — began the habit of **writing everything down precisely enough that a random person could reproduce it.** The same is critical for auto-research agents: they are powerful minds that read a lot and decide in seconds, **but everything is lost if they don't write it down for the next session.**

### Track 3: The model is not the agent — 300M tokens of agent traces (Zach Mueller, ~01:50–02:02)

**The origin.** In late March, Clem, CEO of Hugging Face, tweeted that we need more open trace datasets, since these models — especially the large ones nobody can run at home — are extremely smart. The theory: take their traces, train smaller models on them, and the smaller models might be more performant. Lambda took on the task of seeing what happens.

The recipe looks simple: identify a frontier, **preferably open-source** model (so nobody lands in a legal gray area) → generate reasoning traces (reasoning, actions, results) → train a smaller model on them.

**Then you hit the fun problem: it's not actually about the model.** You can run Opus or Kimi inside Claude Code or Codex and the result differs, **because the harness itself dictates how well the model can perform** — and the answer is often not straightforward. Three data points:

- **Terminal-Bench 2**: take Gemini 3 Pro, which has Google's own Gemini CLI harness. You'd expect the harness the model was trained for to win on a coding bench. **Instead, switching to a minimal, well-crafted harness made the model outperform by 8% and cost almost $20 less to run the eval.**
- **The reverse case**: GPT-5.5 with Codex, from OpenAI who trains these frontier models. **Codex was 5% better — and four times the cost.** He reads that as a legitimate engineering tradeoff: OpenAI may have an incentive to let the model run harder and longer for that extra 1%.
- **Kimi K3**, released the week before, was compared across harnesses by one lab over 26 identical tasks on performance, cost, and time. Unsurprisingly, **the harness built with the model won: Kimi Code scored 21/26 at 54 cents and nearly 300 seconds. Second was Hermes Agent** (Nous Research's open-source harness), nearly as performant, cheaper, and **faster by close to two minutes**. Pi Agent and OpenCode also appeared. The interesting one: **Claude Code scored about 19 while being three times more expensive than the rest**, because **Claude Code injects a lot of system prompts into its harness** — so when you try the latest frontier model in it, much of the context window is consumed by that system prompt.

**What a trace is.** The user prompts a model ("implement this function," "implement this server architecture," or with Codex, "go get me frontier research overnight, good luck"). Inside the agent loop, the model reasons about its next step, calls tools, and judges whether the prompt has been fulfilled — repeating until it decides it has a solution or needs human input. **This matters because if we know how the model behaves, we may be able to train a smaller model on those traces** that you can run at home on a single H100.

**Choosing a harness.** They picked **Hermes Agent**: it was only a few months old at the time, Lambda had good partnerships with Nous Research, and he personally ran Hermes Agent at home rather than OpenClaw — "so I also had a personal bias for this."

**Choosing models — three buckets.**

1. **Permissively licensed**, so nobody has to worry whether the traces can be used commercially, for fun, or even kept on their computer.
2. **Things the average person can't run at home.** Back in March, state of the art was **Kimi K2.5 and GLM 5.1** — one trillion and 800 billion parameters — "unless you happen to have four or 6,000 Blackwells sitting at home racking up your electric bill."
3. **Model capabilities.** GLM was state of the art at coding at the time; Kimi was introducing the **Kimi swarm** paradigm, where **one reasoning chain can contain multiple independent tool-calling chains running at the same time** — very valuable for small, fast models. His example: with parallel tool calling, an open-source model can simultaneously scaffold a FastAPI route, start its unit tests, and track versioning changes — **three separate reasoning traces at once, without needing three sub-agents.**

**Generating the corpus.** **Kimi K2.5 produced about 7,000 basic-to-challenging coding scenarios**, covering everything from computer use to "build a basic hello world .py." Those prompts then ran through **Hermes Agent** with different backends — Kimi and GLM — across **184 H100s over more than a week.** The result was **150 million per model**, verified so that traces that made sense and succeeded went into one bucket, **while failures went into another — still useful to learn from.** They released it the weekend it finished and watched what the community would do.

**What the community did.** Successful by their book: roughly **380 likes on Hugging Face and ~3,000 monthly downloads** (peaking near 10,000 in the first month). More interesting was the wave of models trained on the traces:

- **Quopus** — a Qwen model (Qwen 3.6) trained on Opus traces, hence the portmanteau.
- These were almost all **non-MoE models**: at that small a size, people found **MoE matters less when speed isn't a factor** — your agent runs at home and you don't care whether the problem takes 12 hours or two, since it's just passively doing its thing.
- Sizes ranged from **1B to 27B parameters**, aiming at a performant autonomous agent at home without thousands of dollars of hardware.
- Some took **the Kimi traces specifically** to push **parallel tool calling** into extremely small models like **Liquid's LFM 1.2B**. Sometimes it worked; he still thinks **5–10B is the minimum** for these more complex tool-calling capabilities, but it was a good effort.
- **Harmonic Hermes** became one of the more popular Hermes-specific models; together with Quopus, the two accumulated **nearly half a million downloads**, and new models are still appearing.

**His actual ask isn't "go distill traces."** It's a challenge:

> Take the models you know and love, and the quirks you love and hate about the harnesses you use, and **shove those models into a different harness and see how they react.** The model may have an entirely different personality without a 20,000-character system prompt guiding it, and be more expressive — or you may need to tone it down, because Codex is so strong it needs to be wrangled rather than let loose.

"If I use Codex every single day — **what happens if I give it Pi? What happens if I give it Hermes Agent?** Play with that idea, and widen your scope: **maybe one harness isn't always perfect, even if that harness comes from the place where the model was trained.**"

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Security Arena | Lambda × Berkeley RDI 的一個月 prompt injection 攻防競賽,22 隊、約 112K 場對戰 | One-month prompt injection attack/defense competition (Lambda × Berkeley RDI), 22 teams, ~112K battles | 全程跑在 GPT-OSS 20B 上 / ran entirely on GPT-OSS 20B — [lambda.ai/blog](https://lambda.ai/blog/prompt-injection-doesnt-care-what-your-agent-does-for-a-living) |
| EchoLeak | 零點擊 email 提示注入事故,Copilot 讀信後外洩整個收件匣 | Zero-click email prompt injection: Copilot reads the email and exfiltrates the whole inbox | 競賽中 email phishing 情境的原型 / the model for the arena's email phishing scenario |
| the lab | Lambda 開源的 auto-research 實驗追蹤器,提供 agent 可呼叫的 API 與前端 | Lambda's open-source auto-research experiment tracker: agent-callable APIs plus a front end | `pip install` from GitHub;wrapper 包住 Claude Code / Codex — [lambda.ai/blog](https://lambda.ai/blog/what-happens-when-claude-code-gets-an-experiment-tracker) |
| hermes-agent-reasoning-traces | Lambda 釋出的開源 agent trace 資料集,由 Kimi 與 GLM 在 Hermes Agent 中產生 | Lambda's open agent trace dataset, generated by Kimi and GLM running in Hermes Agent | [huggingface.co/datasets/lambda/hermes-agent-reasoning-traces](https://huggingface.co/datasets/lambda/hermes-agent-reasoning-traces) |
| Hermes Agent | Nous Research 的開源 agent harness,本次 trace 生成所用 | Nous Research's open-source agent harness, used for trace generation | 也在 Kimi K3 harness 比較中排名第二 / also second in the Kimi K3 harness comparison |
| Quopus | 社群用 Opus trace 訓練的 Qwen 3.6 模型 | Community Qwen 3.6 models trained on Opus traces | 與 Harmonic Hermes 合計近 50 萬次下載 / ~500k downloads combined with Harmonic Hermes |
| Harmonic Hermes | 專為 Hermes harness 訓練、較受歡迎的社群模型 | A popular community model trained specifically for the Hermes harness | |
| Lambda Research Grant | 對開發者與研究者提供最高 $5,000 雲端額度 | Up to $5,000 in cloud credits for developers and researchers | 今年前六個月約 1,000 份申請、350 份核准 / ~1,000 applications, ~350 granted in H1 |
| Terminal-Bench 2 | harness 比較所用的終端 agent benchmark | The terminal-agent benchmark used in the harness comparison | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Davina / Dina | Devina Jain |
| Tuan | Chuan Li |
| echolak / emailish | EchoLeak / email phish |
| GPTOSS 20B | GPT-OSS 20B |
| Kimmy K2.5 / Kimk 2.5 / Kimmy K3 | Kimi K2.5 / Kimi K3 |
| GPD 5.5 | GPT-5.5 |
| codeex | Codex |
| news research | Nous Research |
| Quus / Quopus | Quopus(Qwen × Opus) |
| Robert Boyer | Robert Boyle |
| cloth / cloud (code) | Claude (Code) |
| ask key / ASKI code | ASCII |
| pip install(字幕作 "pin install")| pip install |
| jamma / gema | Gemma |
| right teaming | red teaming |

## 待確認 / To Verify

- **trace 數量的單位**:Zach 說「150 million traces from each model」,講題卻是「300 million tokens」,而 Lambda 官方 blog 寫的是 **450M tool-calling tokens**(每個模型約 150M tokens)。「trace」應為口誤,正確單位與總量需以資料集卡片為準。/ He said "150 million traces from each model" while the talk title says 300M *tokens*, and Lambda's blog says **450M tool-calling tokens**. "Traces" is likely a slip; defer to the dataset card.
- **GLM 版本**:台上說 GLM 5.1,Lambda blog 在不同段落分別提到 GLM-5.1 與 GLM-5.6,需確認資料集實際使用的版本。/ He said GLM 5.1; Lambda's blog mentions both GLM-5.1 and GLM-5.6 — confirm which version the dataset used.
- **Gemma 版本**:Chuan Li 只說 "Gemma"(提到 31B thinking 變體),Lambda blog 的 CVPR 2026 demo 寫的是 **Gemma 4**;是否同一次實驗待確認。/ He said only "Gemma" (mentioning a 31B thinking variant); Lambda's blog describes the CVPR 2026 demo as **Gemma 4** — whether it's the same run is unconfirmed.
- **Pi Agent**:harness 比較中提到的開源 harness,拼法與專案來源未確認。/ The open-source harness named in the K3 comparison — spelling and provenance unverified.
- **競賽規模數字**:她說 22 隊、約 112K 場;Lambda blog 提到 1,890 個 agent、65 個評估回合、103,000+ 場對戰,兩組數字的統計口徑不同。/ She cited 22 teams and ~112K battles; Lambda's blog cites 1,890 agents, 65 evaluation rounds, and 103,000+ battles — different accounting.
- Meta 客服 chatbot 上發現「just ask nicely」同類攻擊的公開出處。/ A citation for the "just ask nicely" attack found on a Meta support chatbot.
- 冠軍隊伍名稱台上未點名。/ The winning team names were never stated on stage.
