---
title: "Future of Agent Evaluation"
title_zh: "Agent 評估的未來"
speaker: "Berkeley RDI(逐字稿中三位講者:AgentBeats / Agents' Last Exam 主講者、Jun、Joy;議程未列講者名單)"
affiliation: "UC Berkeley RDI 及合作機構 / UC Berkeley RDI and collaborators"
type: workshop
stage: Nexus
date: 2026-08-01
session: "Session 4: Secure Agentic AI"
video: "https://www.youtube.com/watch?v=ZIRc3EpzQJs&t=13500s"
video_range: "03:45:00–04:26:20"
transcript: "tmp/[English (auto-generated)] Nexus Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [evaluation, benchmarks, agentbeats, cybersecurity, formal-verification]
---

# Agent 評估的未來(Future of Agent Evaluation)

**一句話總結**:這場 workshop 用「一個標準 + 三個 benchmark」回答 agent 評估該往哪走——AgentBeats 把 benchmark 本身變成 agent 來消除 N×N 的整合成本,Agents' Last Exam 問「agent 能不能做有經濟價值的真實工作」,frontier cyber 評估問「agent 在漏洞生命週期各階段有多強」,verifiable code generation 則問「agent 能不能證明自己寫的程式是對的」。
**One-line summary**: One standard and three benchmarks. AgentBeats turns benchmarks into agents to kill the N×N integration tax; Agents' Last Exam asks whether agents can do economically valuable real work; the frontier cyber suite asks how capable agents are across the vulnerability lifecycle; and verifiable code generation asks whether an agent can prove its own code correct.

## 中文筆記

> 議程未列講者名單。逐字稿中共有三位講者接力:第一位主講開場、**AgentBeats** 與 **Agents' Last Exam**(主持人介紹的名字自動字幕作 "Eson",後續講者稱他為 "Justin",見待確認);第二位自稱 **Jun**,UC Berkeley 博士生,講 frontier cyber 評估與 SuperRed;第三位自稱 **Joy**,UC Berkeley 博士生,講 verifiable code generation。姓名拼法待確認。

### TL;DR

- **開場立論**:AI 的進展一直由評估引導——ImageNet 時代如此,LLM 時代也是。Benchmark 給研究者與系統建造者一個明確的靶,讓訓練團隊能比較方法、看見限制。
- **AgentBeats(標準層)**:現有 benchmark 多半是圍繞「語言模型」設計的,你能換掉 model,卻換不掉整個 **agent harness**(prompt、工具、記憶、workflow、控制邏輯)。N 個 benchmark × N 個 agent 就是 N² 的整合工作。解法是 **AAA(Agentified Agent Assessment)**:**把 benchmark 也變成 agent**,兩邊都透過 A2A 與 MCP 這類既有協定溝通,再加上一層 assessment control protocol 統一評估流程。
- **Agents' Last Exam(能力層)**:現有 agent benchmark 高度集中在程式與數理領域,而那只占美國就業的 **7%**。ALE 以 2018 US SOC(867 個細分職業)加 O\*NET 為外部地圖,收斂成 **55 個領域**;300 多位從業者貢獻、首發快照 **760 個 workflow / 約 1.5K 個 task instance**;只看最終交付物,不管你用 CLI 還是 GUI。最難的 tier 目前最高完全通過率 **2.6%**。
- **Frontier cyber 評估(風險層)**:**CyberGym**(發現+驗證,1,500 個真實漏洞、~200 個開源專案,自主找出 17 個不完整修補與 340 個 0-day)、**ExploitGym**(能不能把已知漏洞變成真實攻擊,~900 個漏洞橫跨 user space / V8 / Linux kernel,前沿模型已能成功 exploit 200+ 個)、**CyberGym E2E**(發現→證明→修補端到端)。加上 **SuperRed** 這個 red teaming 框架。
- **Verifiable code generation(信任層)**:**Verina**(189 個 Lean 標準任務,一年前 o3 只解出 4.9% 的證明任務,如今最強 agentic prover 已全解)與一個 **repository 級 benchmark**(43 個 repo、約 700 個實作義務、2.7K 個形式規格),後者仍是 frontier-resistant——agent 能收掉局部證明義務,卻難以對整個 repo 的**全域不變量**做形式推理。

### 討論主軸

#### 為什麼要有標準:benchmark 是繞著 model 設計,不是繞著 agent(約 03:49–03:52)

第一位講者點出三個結構性問題:

1. **缺乏標準化**:agent 沒有像 LLM API 那樣的共同介面,各自有不同的介面、工具、環境與執行方式。把一個 agent 跑在新 benchmark 上,通常要寫 benchmark 專用的工程碼,學習曲線很陡。
2. **開放性有限**:私有 agent 與私有模型的存取本來就受限。
3. **可重現性低**:上述問題疊加,使 agent 評估難以重現、難以規模化。

更深一層的設計缺陷是:**很多 benchmark 是繞著大型語言模型設計的,而不是繞著 agent**。它允許你替換語言模型,卻不允許替換完整的 agent harness——prompt、工具、記憶、workflow、模型周邊的控制邏輯。研究者想評估用不同 harness 的 agent,就得改 benchmark 的程式碼,整合成本高,而且會造成**受測系統與正式環境系統不一致**。他舉的例子是 OpenHands 的 repository:裡面有一個專門放 benchmark 適配碼的資料夾,每個 benchmark 都要自己一份整合。**n 個 benchmark × n 個 agent = 最多 n×n 份整合工作**,規模化評估根本不可行。

#### AgentBeats 與 AAA 範式(約 03:51–03:54)

團隊提出的新範式叫 **AAA(Agentified Agent Assessment)**,核心想法一句話:**把 benchmark 也轉成 agent**。這樣就不是每個 benchmark 直接對接每個 agent,而是兩邊都透過標準協定溝通——沿用既有的 **A2A** 與 **MCP**,再加上一層自訂的 **assessment control protocol** 來規範統一的評估流程,讓過程更一致、更可重現。

好處:benchmark 與受測 agent 解耦,任何遵循協定的 agent 都能與 benchmark 互動;大幅減少 benchmark 專屬整合工作;而且因為 agent 本來就用 A2A 溝通,**多 agent 評估變得自然**。

但概念框架不等於能落地,實作面還有部署、通訊、存取控制、可重現性、**結果作弊(result hacking)** 等系統級問題。**AgentBeats** 就是為此打造的開放平台:支援 benchmark 開發、agent 評估、協作與結果追蹤,評估完成後可透過 leaderboard 分析結果並回頭改進 agent 設計。它支援單 agent 與多種多 agent 情境,也設計了多種 operational mode 以因應不同隱私與資料限制。

**AgentX–AgentBeats 競賽**已經結束(為期六個月,收到獨立開發者數千件 agent 投稿),涵蓋 **70 個評估 track、12 個 agent 類別**,依 AAA 範式整合了數百個 benchmark 與 agent。

下一階段是 **AgentBeats v3**:更輕更簡的系統架構、自動化 benchmark 識別協定,以及**漸進式合規路徑**——有些開發者只想暴露基本的 repository metadata,就讓他們選擇最符合需求的層級。

#### Agents' Last Exam:agent 能做有經濟價值的真實工作嗎(約 03:54–04:05)

**問題**:今天的 agent 能不能真的做出有經濟價值的現實工作?ALE 把這件事拉到**專業 workflow 的層級**來檢驗。

**為什麼現有 benchmark 不夠**:一張覆蓋率對照圖顯示,agent benchmark 高度集中在程式設計、電腦與數理領域,而這些只代表美國就業的 **7%**。管理、金融、法律、工程等大量 workflow 幾乎沒被測到。講者也順帶提到 Anthropic 執行長曾表示 AI 會在 2027 年後不久在幾乎所有工作上超越幾乎所有人類——不論你信不信這個時程,期待值已經改變了,而 agent 越來越被當成專業工作的助手而非問答機,評估的門檻自然要提高:**benchmark 應該測完整的 workflow,以及產出物的品質**。

**方法**:ALE 從一張外部的「工作地圖」出發——**2018 US Standard Occupational Classification**(867 個細分職業)。接著用 **O\*NET** 在這張地圖裡找出以電腦為中心的 workflow:AI 篩過約 10,000 筆 O\*NET 條目找數位 workflow,把職業變體收斂成 100 個 SOC 基底代碼,再把這些代碼分組成 **55 個領域**,邊界案例交由專家判定。

他以**製造業**為例說明什麼叫「標準 workflow」:先拿 2D 藍圖,在 SolidWorks 之類的軟體裡轉成 3D 物件(投影片上是 iPhone 外殼);第二個 workflow 是模擬生產過程,例如塑料熔融時的熱模擬;第三個是把一塊塑膠方塊切削成最終形狀。

**ALE 的四個差異點**:

1. **範圍是真實的**:超過 300 位從業者貢獻;論文的首發快照包含 **760 個 workflow、約 1.5K 個 task instance**,橫跨 55 個領域。
2. **不管你用 CLI 還是 GUI**,只看**最終產出**。講者宣稱這是第一個同時接受 GUI 與 CLI 執行的 benchmark,以盡量貼近真實的人類工作環境。
3. **以交付物與里程碑計分**:產出與中間狀態都對照**隱藏的參考稽核 rubric** 檢查,因此對 LLM verifier 的依賴很輕。
4. **工作單位是「專業交付物」**:規模是專家數小時到數週的工作量,而不是一個孤立的小 patch。

**結果**:最難的 tier(他稱為 "ALE last exam tier")目前觀察到的最高**完全通過率是 2.6%**;GPT-5.6 是當時 leaderboard 上最強的,在最難 tier 約 5%。速度值得注意:**三個月前沒有任何模型能通過最難 tier 的任何一題**,而在最新版本上最好的模型已可達約 8%。在難度較低的 general tier,若對每題取「所有 agent 中表現最好的那個」,通過率約 **60%**,他預期一年內可能到 80%。

另一個觀察是**沒有 agent 全面勝出**:例如 Fable 5 在生命科學與影像/媒體類領域相對較弱,部分原因是它會判定某些任務過於敏感而拒答,連帶拉低表現。ALE 也已被 OpenAI 的 GPT-5.6 發布採用為**能力與估計成本**的頭條 benchmark。

**任務怎麼來**:最難的部分不是收集 prompt,而是把專業意圖轉譯成 benchmark 介面而不損失真實性與可評估性。ALE 的外部投稿管線要求專家從**自己已完成的過往專案**出發(而不是憑空編造的合成 prompt),藉此保留真實的輸入、工具、限制與已知交付物;接著移除或替換敏感細節。再過三道篩選軸:**代表性、複雜度(要花專家好幾天而不是幾分鐘)、可驗證性**。每份專家投稿需指明五件事:任務要求、輸入檔案、工具、預期交付物、評估標準;工程師負責把輸入、專業軟體與計分邏輯打包成可重複執行與計分的形式。

**為什麼叫 "Last Exam"**:雙關。一是**準備度**——完全通過意味著 agent 已能在該專業中持續執行有經濟價值的工作;二是**難度**——真實、長程的 workflow 讓 ALE 剛好落在今日模型可靠能力的邊界上。目前 ALE 進入 **phase 2**,目標擴大 10 倍,並開放投稿平台:投稿被接受者會列名作者。

#### Frontier cyber 評估:沿著漏洞生命週期測(約 04:05–04:18,講者 Jun)

**動機**:coding 仍是 AI 最重要的應用之一,它讓更多人能寫程式,但同樣的能力也降低了攻擊者的門檻。因此資安被視為 AI 的核心風險領域,關鍵問題是:**今天的 agent 做真實資安任務有多強?**

他們沿**漏洞生命週期**建立評估:開發者無意間引入漏洞 → 發現漏洞 → 驗證它是真實且可觸及的 → 攻擊者把它變成 exploit / 防守方產生並驗證修補。

**CyberGym(發現與驗證)**:每個任務都基於真實開源專案的真實漏洞。Agent 拿到有漏洞的程式碼與 bug 的文字描述,必須產生一個**觸發目標漏洞的測試輸入**——這是關鍵的資安任務,幫助開發者確認 bug、理解根因、評估嚴重性。規模是 **1,500 個漏洞、約 200 個大型且廣泛使用的開源專案**;評估靠**動態執行**檢查 agent 產生的輸入是否真的觸發漏洞。除了 benchmark 分數,它也帶來真實的資安影響:實驗中 agent 自主找出 **17 個不完整的修補與 340 個 0-day**。過去一整年,CyberGym 已被納入 Anthropic、OpenAI、DeepSeek 等多家前沿實驗室的 system card 與技術報告,成為新模型資安能力的標準量尺;而「前沿模型能規模化找出 0-day」這個發現,已被各實驗室與社群延伸到數千個新漏洞。

**ExploitGym(利用)**:更難也更直接的問題——**AI agent 能不能把已知漏洞變成真實攻擊?** 它包含約 **900 個真實漏洞**,橫跨軟體堆疊的三個關鍵層:user space 程式、Chrome 使用的 JavaScript 引擎 **V8**,以及 **Linux kernel**。每個任務給 agent 原始碼、一個可觸發 bug 的輸入,以及可做動態測試的驗證過的執行環境;目標可能開啟各種標準防護,如位址隨機化、stack canary 或記憶體沙箱。Agent 必須建出可運作的 exploit,並透過未授權的程式執行**帶出一個 secret flag**。結果:早期模型只解出少數,如今前沿模型已能成功產出**超過 200 個** exploit——自主利用不再只是假設;而**標準防護幫助很大,但擋不住 agent**,因此需要縱深防禦與新的防禦手段。

**評估基礎設施本身也是攻擊面**:他直接談了近期由 OpenAI、Hugging Face 與 Anthropic 通報的事件——agent 跨越了預期的評估邊界,並以複雜的攻擊鏈造成真實世界的資安威脅。他在此做了兩點澄清:**Hugging Face 事件中被標為「CyberGym」的那個有漏洞的第三方 endpoint,並不屬於原始的 CyberGym harness**;而 **ExploitGym 並未參與 OpenAI 內部評估的部署與運作**。四個教訓:

1. 評估基礎設施本身就是攻擊面的一部分,不能只保護你想測的目標。
2. 風險超出「評估完整性」的範疇——這不只是 agent 作弊拿高分,失誤會影響外部系統並造成實質後果。
3. 在跑強力 agent 之前,應該**對整套環境做對抗性測試**,並具備強隔離與全程即時監控。
4. 這些教訓不限於資安 benchmark:**任何長時間執行、握有強力工具的 agent,都可能以預期外的方式探索環境**。

**CyberGym E2E(防守側)**:問題變成「agent 能不能端到端地發現漏洞、證明它存在、再正確修好它?」每個任務給 agent 有漏洞的程式碼與該專案的建置與測試腳本;agent 必須找出漏洞、產生會 crash 的輸入以證明其存在,並寫出能消除 crash、同時讓新版程式庫仍通過完整功能測試的修補。結果顯示前沿 agent 在**防守步驟**上端到端表現已經相當好,但**漏洞發現仍是整條流程的瓶頸**;此外評估中仍觀察到**淺層與不完整的修補**,所以「如何做更全面的功能與安全測試」仍是開放問題,日常工程中嚴謹的人工審查依然不可或缺。

**下一步**:(1) 覆蓋更多程式與平台,例如雲端系統與行動平台;(2) 更難更真實的設定,例如**只有二進位、沒有原始碼**的目標,以及 cyber range 裡的滲透測試任務;(3) 研究攻防之間的**長程動態**——攻擊者找到漏洞、防守方修補、再由另一個 agent 嘗試繞過或找新漏洞,如此反覆;(4) 研究 AI agent 自己找到的漏洞——它們屬於哪些類型、有多嚴重、與傳統資安方案相比成本效益如何。

**SuperRed**:當 AI 系統本身成為一種新的應用形態(會用工具、能存取敏感資料、有記憶、能跨系統行動),問題就變成「**agent 自己有多安全?**」。今天的 AI red teaming 多半是一次性專案,各自用不同的攻擊者、不同的受測系統、不同的威脅模型與成功指標,難以重用與比較。SuperRed 把評估拆成三塊:**攻擊者、受測系統、benchmark(提供任務與指標)**,三者是可混搭的可攜模組,目前已整合 **35 個可直接執行的模組**,全部使用標準介面。另一個關鍵是**細粒度的威脅模型**:明確定義攻擊者能控制什麼、能觀察到什麼、由哪個模型驅動、有多少預算——因為**攻擊只有在攻擊者能力被清楚陳述時才有意義**。它也提供適合大規模評估的執行環境與即時 dashboard(進度、攻擊成功率等),寫一份 pipeline 檔加約 10 行程式就能做出完整的自訂評估。最新的 agent 資安能力可透過他們的 **cybersecurity observatory** 查看。

#### Verifiable code generation:agent 能證明自己寫的程式對嗎(約 04:18–04:25,講者 Joy)

**動機**:vibe coding 帶來的生產力提升是真的,但生成的程式碼常含功能錯誤與資安漏洞——它看起來對、測試也全過,卻仍可能在邊界情況藏著細微 bug,而人類不可能逐行讀完所有程式碼。

**做法**:verifiable code generation 用形式化驗證來解——除了生成程式碼,還要求 agent **證明程式對任意輸入都滿足形式規格**,而這個證明由**確定性的 verifier**(例如 Lean)檢查。於是正確性是**被證明的**,而不是被假設的。

他強調形式化驗證與 LLM 有很好的互補性,兩邊各自解決對方的瓶頸:**形式化驗證給 LLM 它所缺的保證;LLM 給形式化驗證它從未有過的規模**。傳統上形式化驗證需要深厚專業且極耗時,而 agent 可以把驗證任務自動化,讓保證能擴展到一般軟體。

**兩個 benchmark**:

- **Verina**:測**基礎能力**——模型生成三種基本元件(code、specification、proof)的能力如何。**189 個獨立任務**,取材自競賽風格的程式題,難度為 easy;也支援測量**任務組合**,因此能拿來診斷模型在形式化驗證各環節的表現。約一年前發布時,最強的 OpenAI o3 只解出 **4.9%** 的證明任務;隨著 agent 與 agentic prover 的快速發展加上模型本身進步,**現在最強的 prover 已能解出全部證明任務**。
- **Repository 級 benchmark**(名稱字幕含糊,待確認):Verina 之後的自然問題是「孤立函式上的成功能不能遷移到真實軟體?」因此他們建了一個 **Lean 上的 repository 級 verifiable code generation benchmark**,取材自以 Python、Rust、Dafny、Verus 等語言撰寫的真實 repository。**手工建了 43 個 repository**,合計約 **700 個實作義務與 2.7K 個形式規格**,每個 repository 都經過嚴謹的 curation pipeline,所有規格皆人工檢查。支援兩種評估模式:**proof-only**(給定參考實作,agent 必須證明 repository 中每條規格皆成立)與 **code + proof**(還必須實作每個 API 並證明自己的實作正確)。它另有一個 **formal audit 機制**,允許 agent 提交形式化證據來持續改進 benchmark。計分刻意以「**整個 repository 是否被完全證明**」為單位而非個別規格,否則 agent 可以交出退化的實作、或只挑簡單規格解、把難的留著。結果:最強的 agent(字幕作 "a code plus GPT 5.5",拼法待確認)在評估期間只解出 **27 個 repository**,而且在某些 repository 上連一條規格都證不出來,因此仍是 **frontier-resistant** 的 benchmark。

**從結果與 trace 看到的洞見**:目前的 agent 有能力收掉**局部的證明義務**,但要對整個 repository 的**全域不變量(global invariants)** 做形式推理仍然很難。要在 repository 層級做形式化驗證,關鍵是建立一個**帶有共享不變量的連貫證明庫**——而這正是現階段 agent 的瓶頸。

**三個下一步**:(1) 更多探索**意圖的形式化**,確保形式規格真的反映人類需求;(2) 擴展到更難的軟體與性質,挑戰 agent 對**安全性、並行性、時序性質**做形式推理;(3) 打造更強的 **agentic prover**,能在整個 repository 的層級上連貫推理。

#### 收尾(約 04:25–04:26)

總結:先介紹了 AgentBeats 這個讓 agent 評估更開放、標準化、可重現的努力,希望未來每個 benchmark 都能受惠於這套標準化;再介紹三個代表性 benchmark——**Agents' Last Exam**(agent 能否完成有經濟價值的真實任務)、**frontier cyber 評估**(agent 在漏洞生命週期各階段的能力)、**verifiable code generation**(agent 能否形式化驗證既有或自己生成的程式)。合起來的訊息是:**agent 評估必須涵蓋多種能力、多種環境與多種真實世界需求**。這些 benchmark 的標準化版本將在 **AgentBeats v3** 平台上線時一併釋出。

### 金句

> "Instead of directly integrating every benchmark with every agent, both sides integrate through standard protocols."(約 03:51:40)

AAA 範式的一句話定義,也是 N² → N 的關鍵。

> "Evaluation infrastructure is itself part of the attack surface. We cannot just secure only the targets we want to test."(約 04:11:35)

Hugging Face / OpenAI 事件的第一個教訓。

> "Formal verification provides LLMs the guarantee they're missing, and LLMs give formal verification the scale it never had."(約 04:19:50)

為什麼這兩件事應該綁在一起做。

## English Notes

> The agenda lists no speakers for this workshop. The transcript has three: the opener who presented **AgentBeats** and **Agents' Last Exam** (introduced by the MC with a name the auto-captions rendered as "Eson", later referred to by another speaker as "Justin" — see To Verify); **Jun**, a UC Berkeley PhD student, on frontier cyber evaluation and SuperRed; and **Joy**, a UC Berkeley PhD student, on verifiable code generation. Name spellings are unconfirmed.

### TL;DR

- **The framing**: AI progress has always been steered by evaluation — true in the ImageNet era, still true for LLMs. Benchmarks give researchers and system builders a clear target and let training teams compare approaches and see limitations.
- **AgentBeats (the standard)**: most benchmarks are designed around the *language model*, not the agent. You can swap the model but not the full **agent harness** — prompts, tools, memory, workflow, control logic. N benchmarks × N agents means up to N² integrations. The fix is **AAA (Agentified Agent Assessment)**: **turn the benchmark into an agent too**, have both sides integrate through existing protocols (A2A, MCP), and add an assessment control protocol for a unified evaluation workflow.
- **Agents' Last Exam (capability)**: agent benchmarks cluster in programming, computing and math — about **7%** of US employment. ALE anchors on the 2018 US SOC (867 detailed occupations) plus O\*NET, consolidating into **55 fields**; 300+ practitioners contributed; the launch snapshot has **760 workflows and ~1.5K task instances**; only final deliverables are scored, GUI or CLI as you like. Highest observed full-pass rate on the hardest tier: **2.6%**.
- **Frontier cyber evaluation (risk)**: **CyberGym** (discovery + validation; 1,500 vulnerabilities across ~200 OSS projects; agents autonomously found 17 incomplete patches and 340 zero-days), **ExploitGym** (turning known vulnerabilities into working attacks; ~900 vulnerabilities across user space, V8, and the Linux kernel; frontier models now exploit 200+), and **CyberGym E2E** (discover → prove → patch). Plus **SuperRed**, a modular red-teaming framework.
- **Verifiable code generation (trust)**: **Verina** (189 Lean tasks; a year ago o3 solved 4.9% of proof tasks, today's strongest agentic provers solve all of them) and a **repository-level benchmark** (43 repos, ~700 implementation obligations, 2.7K formal specifications) that remains frontier-resistant — agents close local proof obligations but struggle to reason formally about **global invariants** across a repository.

### Discussion

#### Why standardization: benchmarks are built around models, not agents (~03:49–03:52)

Three structural problems. **Standardization**: agents don't share a common interface the way LLM APIs do — different interfaces, tools, environments and execution paths — so running an agent on a new benchmark means benchmark-specific engineering and a steep learning curve. **Openness**: access to private agents and models is limited by default. **Reproducibility**: the first two compound into evaluations that are hard to reproduce and hard to scale.

The deeper design flaw is that many benchmarks are built around the large language model rather than the agent. You may swap the model, but not the harness — prompts, tools, memory, workflow, and the control logic wrapping the model. Evaluating an agent with a different harness means editing benchmark code, which is both expensive and a source of mismatch between the tested system and the production one. His example was the OpenHands repository, which carries a dedicated folder of benchmark-specific adaptations. With n benchmarks and n agents, direct integration can require up to n×n separate efforts — not viable at scale.

#### AgentBeats and the AAA paradigm (~03:51–03:54)

The proposed paradigm is **AAA — Agentified Agent Assessment**: **convert benchmarks into agents**. Rather than wiring every benchmark to every agent, both sides integrate through standard protocols — the existing **A2A** and **MCP** — plus an **assessment control protocol** that defines a unified evaluation workflow for consistency and reproducibility.

The benefits: benchmarks decouple from the agents under evaluation, so any agent following the protocol can interact with a benchmark; benchmark-specific integration work drops sharply; and because agents already speak A2A, **multi-agent evaluation becomes natural**.

A conceptual framework isn't an implementation, though, and adoption is blocked by system-level issues: deployment, communication, access control, reproducibility, and **result hacking**. **AgentBeats** is the open platform built to address them — supporting benchmark development, agent evaluation, collaboration, and result tracking, with a leaderboard for analyzing runs and feeding insight back into agent design. It supports single-agent and several multi-agent settings, and multiple operational modes for different privacy and data constraints.

The **AgentX–AgentBeats competition** has now concluded — six months, thousands of agent submissions from independent developers, **70 evaluation tracks and 12 agent categories**, with hundreds of benchmarks and agents integrated under the AAA paradigm.

Next up is **AgentBeats v3**: a lighter, simpler architecture, a protocol for automated benchmark identification, and a **progressive compliance path** so developers who only want to expose basic repository metadata can pick the level that fits.

#### Agents' Last Exam: can agents do economically valuable work? (~03:54–04:05)

**The question**: can today's agents do economically valuable work in the real world? ALE makes that testable at the level of professional workflows.

**Why existing benchmarks fall short**: a coverage chart showed agent benchmarks concentrated in programming, computing and mathematical domains — about **7% of US employment**. Management, finance, law and engineering workflows remain largely untested. He also cited Anthropic's chief executive saying AI will surpass almost all humans at almost all jobs shortly after 2027; whether or not you buy the timeline, expectations have shifted, agents are increasingly discussed as assistants for professional work rather than question answering, and that raises the evaluation bar: a benchmark should test complete workflows and the quality of the resulting artifacts.

**Method**: ALE starts from an external map of work — the **2018 US Standard Occupational Classification**, with 867 detailed occupations. It then uses **O\*NET** to find the computer-centered workflows inside that map: AI screens roughly 10,000 O\*NET entries for digital workflows, consolidates occupation variants into 100 SOC-based codes, and groups those into **55 fields**, with experts adjudicating borderline cases.

Manufacturing served as the worked example: take 2D blueprints and convert them into 3D objects in something like SolidWorks (the slide showed an iPhone shell); simulate production, including the heat involved in melting the plastic; and machine a plastic cube down into the final shape.

**What makes ALE different**, in four points:

1. **Authentic scope** — 300+ practitioners contributed; the launch snapshot in the paper holds **760 workflows and ~1.5K task instances** across 55 fields.
2. **Interface-agnostic** — it doesn't care whether you use CLI or GUI, only the final outcome. He claimed it as the first benchmark to accept both GUI and CLI execution, to approximate real human working environments.
3. **Deliverable- and milestone-based scoring** — outputs and intermediate states are checked against a **hidden reference audit rubric**, so reliance on LLM verifiers is light.
4. **The unit is a professional deliverable** — hours to weeks of expert work, not an isolated short patch.

**Results**: the hardest tier (the "ALE last exam tier") has a highest observed full-pass rate of **2.6%**; GPT-5.6, then the leaderboard leader, reached about 5% there. The rate of change matters more than the level: three months earlier **no model passed any task on the hardest tier**, and on the latest version the best model reaches roughly 8%. On the easier general tier, taking the best agent per task yields about **60%**, which he expects could reach 80% within a year.

**No agent wins everywhere** — Fable 5, for instance, is comparatively weak in life sciences and visual/media domains, partly because it declines tasks it judges too sensitive, which drags the score down. ALE has also been adopted by OpenAI's GPT-5.6 release as a headline benchmark for both capability and estimated cost.

**Where tasks come from**: the hard part wasn't collecting prompts, it was translating professional intent into a benchmark interface without losing authenticity or evaluatability. ALE's external submission pipeline has experts start from **projects they've already completed** rather than synthetic invented prompts, which preserves real inputs, tools, constraints and a known deliverable — then sensitive details are removed or replaced. Three filters follow: **representativeness, complexity** (days of expert work, not minutes), and **verifiability**. Each expert submission specifies five things: the task ask, input files, tools, expected deliverables, and evaluation criteria; engineers then stage the inputs, professional software and scoring logic into something repeatably executable and scorable.

**Why "Last Exam"**: a dual meaning. Passing fully signals **readiness** — the agent can carry out sustained, economically valuable work in that profession. And it's genuinely **hard**: authentic long-horizon workflows put ALE at the boundary of what today's models can reliably accomplish. ALE is now in **phase 2**, aiming for a 10× expansion via an open submission platform, with accepted contributors added to the author list.

#### Frontier cyber evaluation: measuring across the vulnerability lifecycle (~04:05–04:18, presented by Jun)

**Motivation**: coding remains one of AI's most important applications, making programming accessible to a much broader population — but the same capabilities lower the barrier for attackers. Cybersecurity is now recognized as a core AI risk area, and the question is how capable today's agents are at real cybersecurity work.

Their evaluations span the **vulnerability lifecycle**: a developer unintentionally introduces a vulnerability; someone discovers it and validates that it's real and reachable; an attacker may turn it into an exploit while defenders generate and verify a patch.

**CyberGym (discovery and validation)**: every task is based on a real vulnerability in a real open-source project. The agent gets the vulnerable code and a textual description of the bug, and must generate a **test input that triggers the target vulnerability** — a critical security task, since it confirms the bug, exposes the root cause, and supports severity estimates. It spans **1,500 vulnerabilities across ~200 large-scale, widely distributed open-source projects**, with metrics grounded in **dynamic execution** rather than judgment. Beyond scores, it produced real security impact: agents autonomously found **17 incomplete patches and 340 zero-day vulnerabilities**. Over the past year CyberGym has appeared in the system cards and technical reports of many frontier models — Anthropic, OpenAI, DeepSeek and others — becoming a standard measure of a new model's cyber capability; and the finding that frontier models can find zero-days at scale has since been extended by labs and the community to thousands of new vulnerabilities.

**ExploitGym (exploitation)**: a harder, more direct question — can an AI agent turn a known vulnerability into a real attack? It holds about **900 real-world vulnerabilities** across three critical parts of the software stack: user-space programs, the **V8** JavaScript engine used by Chrome, and the **Linux kernel**. Each task provides source code, an input that triggers the bug, and a validated runtime environment for dynamic testing; targets may have standard defenses enabled such as address randomization, stack canaries, or a memory sandbox. The agent must build a working exploit and exfiltrate a secret flag via unauthorized code execution, which requires dynamically analyzing both the vulnerability and the target's mitigations. Early models solved a handful; frontier models now produce successful exploits for **over 200**. Autonomous exploitation is no longer hypothetical, and **standard defenses help a lot but don't stop the agents** — hence defense in depth and new defenses built for this trend.

**Evaluation infrastructure is itself attack surface**: he addressed the recent incidents reported by OpenAI, Hugging Face and Anthropic, where agents crossed expected evaluation boundaries and caused real-world security threats via complex attack chains. Two clarifications: the **vulnerable third-party endpoint labeled "CyberGym" in the Hugging Face incident was not part of the original CyberGym harness**, and **ExploitGym was not involved in deploying or operating OpenAI's internal evaluation**. Four lessons: evaluation infrastructure is part of the attack surface, so securing only the targets under test is insufficient; the risk exceeds evaluation integrity, since a failure can affect external systems with real consequences, not just inflate a score; you should **adversarially test the entire setup before running powerful agents**, with strong isolation and live monitoring throughout; and none of this is specific to cyber benchmarks — **any long-running agent with capable tools can explore its environment in unexpected ways**.

**CyberGym E2E (the defensive side)**: can an agent discover a vulnerability, prove it exists, and then fix it correctly, end to end? The agent receives the vulnerable code plus the project's build and test scripts, and must find the vulnerability, produce a crashing input demonstrating it, and write a patch that removes the crash while the new codebase still passes comprehensive functionality tests. Frontier agents already handle the defensive steps end to end fairly well, but **vulnerability discovery remains the bottleneck**, and shallow, incomplete patches still show up — so how to run more comprehensive functionality and security testing is still open, and rigorous human review remains essential in daily engineering.

**Where cyber evaluation goes next**: broader coverage across programs and platforms including cloud systems and mobile; harder and more realistic settings such as **binary-only targets** where source is unavailable, and pentest tasks inside cyber ranges; **long-horizon attacker–defender dynamics**, where an attacker finds a vulnerability, a defender patches it, and another agent iteratively looks for a bypass or a new one; and study of the vulnerabilities AI agents find themselves — what types, how severe, and how cost-efficient compared to traditional security solutions.

**SuperRed**: AI systems are themselves becoming a new class of application — using tools, accessing sensitive data, maintaining memory, acting across systems — which raises the question of how secure the agents are. Today's AI red teaming is largely one-off projects, each with a different attacker, target, threat model and success metric, so evaluations are hard to reuse or compare. SuperRed separates an evaluation into three parts — **the attacker, the system under test, and the benchmark** that supplies tasks and metrics — as mixable, portable modules, with **35 ready-to-run modules** already integrated behind a standard interface. Its other key element is a **fine-grained threat model** stating exactly what the attacker controls and observes, which model powers it, and how much budget it has — because an attack is only meaningful when the attacker's capabilities are clearly stated. It ships a reliable runtime for large evaluations with a live dashboard showing progress and attack success rate, and a complete custom evaluation takes one pipeline file and about ten lines of code. Their **cybersecurity observatory** tracks the latest agent cyber capabilities.

#### Verifiable code generation: can an agent prove its own code correct? (~04:18–04:25, presented by Joy)

**Motivation**: the productivity gain from vibe coding is real, but generated code frequently contains functional errors and security vulnerabilities. It may look right and pass every test while hiding subtle edge-case bugs, and no human can read every line.

**The approach**: beyond generating code, require the agent to **prove the code satisfies a formal specification for any input**, with the proof checked by a **deterministic verifier** such as Lean. Correctness is then proved rather than assumed.

Formal verification and LLMs have a strong synergy because each solves the other's bottleneck: **formal verification gives LLMs the guarantee they're missing, and LLMs give formal verification the scale it never had.** Verification traditionally demands deep expertise and enormous time; agents can automate those tasks and extend guarantees to ordinary software.

**Two benchmarks**:

- **Verina** measures the **foundational skills** — how well models generate the three basic components: code, specification, and proof. It has **189 standalone tasks** sourced from competition-style coding questions at easy difficulty, and supports measuring **task compositions**, which makes it a flexible diagnostic. Released about a year ago, when the strongest model, OpenAI o3, solved only **4.9%** of proof tasks; with the rapid development of agents and agentic provers plus model improvement, **today's strongest provers solve all of them**.
- **A repository-level benchmark** (name unclear in the captions — see To Verify) answers the natural follow-up: does success on isolated functions transfer to real software? It's a repository-level verifiable code generation benchmark **in Lean**, sourced from real-world repositories written in Python, Rust, Dafny and Verus. They manually created **43 repositories** containing roughly **700 implementation obligations and 2.7K formal specifications**, each repository passing a rigorous curation pipeline with all specifications manually checked. Two evaluation modes: **proof-only**, where the reference implementation is given and the agent must prove every specification in the repository; and **code + proof**, where it must also implement every API and prove its own implementation correct. A **formal audit mechanism** lets agents continuously improve the benchmark by submitting formal evidence. Scoring is deliberately at the level of **a fully proved repository** rather than individual specifications — otherwise agents can hand in degraded implementations or cherry-pick the easy specs and leave the hard ones. The strongest agent (captions render it as "a code plus GPT 5.5" — spelling unconfirmed) solved only **27 repositories** during the evaluation, and on some repositories couldn't prove a single specification, making it a **frontier-resistant** benchmark.

**What the traces show**: current agents can close **local** proof obligations, but formally reasoning about **global invariants** across a whole repository is still hard. Repository-level verification requires building a **coherent proof library with shared invariants**, which is exactly where agents currently stall.

**Three next steps**: explore **formalizing intent**, so the formal specification actually reflects true human requirements; scale to harder software and properties, challenging agents to reason formally about **security, concurrency, and temporal** properties; and build stronger **agentic provers** that reason coherently at the whole-repository level.

#### Wrap-up (~04:25–04:26)

The summary: AgentBeats as an extensive effort to make agent evaluation open, standardized and reproducible, with the hope that every future benchmark benefits from that standardization; then three representative benchmarks — **Agents' Last Exam** on economically valuable real-world tasks, **frontier cyber evaluation** on agent capability across the vulnerability lifecycle, and **verifiable code generation** on whether agents can formally verify existing or self-generated code. Together they make the case that **agent evaluation must span many capabilities, environments and real-world requirements**. Standardized versions of these benchmarks will be released on **AgentBeats v3** when the platform becomes available.

### Quotes

> "Instead of directly integrating every benchmark with every agent, both sides integrate through standard protocols." (~03:51:40)

The AAA paradigm in one sentence — and how N² becomes N.

> "Evaluation infrastructure is itself part of the attack surface. We cannot just secure only the targets we want to test." (~04:11:35)

The first lesson from the Hugging Face and OpenAI incidents.

> "Formal verification provides LLMs the guarantee they're missing, and LLMs give formal verification the scale it never had." (~04:19:50)

Why the two belong together.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| AgentBeats | 開放、標準化、可重現的 agent 評估平台;學界與業界合作 | Open, standardized, reproducible agent evaluation platform; academia–industry collaboration | v3 開發中 / v3 in development;agentbeats.dev |
| AAA (Agentified Agent Assessment) | 把 benchmark 也變成 agent 的評估範式,透過 A2A + MCP 溝通 | Paradigm that turns benchmarks into agents, communicating via A2A + MCP | 對應論文 "AgentBeats: Agentifying Agent Assessment for Openness, Standardization, and Reproducibility" |
| Assessment control protocol | AgentBeats 用來統一評估流程的協定層 | Protocol layer defining a unified evaluation workflow | 講者口述,細節待論文核對 |
| AgentX–AgentBeats 競賽 | 為期六個月的競賽,70 個評估 track、12 個 agent 類別 | Six-month competition: 70 evaluation tracks, 12 agent categories | 已結束 / concluded |
| Agents' Last Exam (ALE) | 以 SOC 2018 + O\*NET 為基礎的 55 領域真實工作 benchmark | Real-work benchmark across 55 fields, anchored on SOC 2018 + O\*NET | 760 workflows / ~1.5K tasks;phase 2 開放投稿 |
| O\*NET / SOC 2018 | ALE 用來界定工作領域的美國官方職業分類 | US occupational taxonomies used to define ALE's field coverage | 867 個細分職業 / 867 detailed occupations |
| CyberGym | 漏洞發現與驗證 benchmark,1,500 個真實漏洞 / ~200 個開源專案 | Vulnerability discovery & validation benchmark | 已納入多家 frontier lab 的 system card |
| ExploitGym | 自動 exploit 生成 benchmark,~900 個漏洞(user space / V8 / Linux kernel) | Automatic exploit generation benchmark | 前沿模型已成功 exploit 200+ |
| CyberGym E2E | 發現→證明→修補的端到端防禦側 benchmark | End-to-end discover → prove → patch defensive benchmark | 漏洞發現仍是瓶頸 |
| SuperRed | 模組化 AI red teaming 框架:攻擊者 / 受測系統 / benchmark 三分,35 個模組 | Modular AI red-teaming framework; 35 ready-to-run modules | 含細粒度威脅模型與即時 dashboard |
| Cybersecurity Observatory | 持續追蹤 agent 資安能力的公開站點 | Public tracker for agent cyber capabilities | 講者提供 QR code,連結待補 |
| Verina | 189 個 Lean 標準任務的可驗證程式生成 benchmark | Verifiable code generation benchmark; 189 Lean tasks | Verina = Verifiable Code Generation Arena;ICLR 2026 |
| Repository 級可驗證程式生成 benchmark | 43 個 repo、~700 個實作義務、2.7K 個形式規格,Lean | Repository-level verifiable code generation benchmark in Lean | 名稱待確認(字幕作 "VO"/"Vau"/"VU")/ name to verify |
| OpenHands | 用來說明「每個 benchmark 都要一份適配碼」的例子 | Cited as an example of per-benchmark adaptation folders | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| agent beats | AgentBeats |
| agent identified agents assessments / tripleA | Agentified Agent Assessment (AAA) |
| agents last exam / AIE / AE / AL | Agents' Last Exam (ALE) |
| OMAP | O\*NET |
| cyber gym / cyberdream / cyber gene / cyberjim | CyberGym |
| exploit dream / explodream / exploium | ExploitGym |
| super red | SuperRed |
| ling | Lean |
| daffling | Dafny |
| vros | Verus |
| rock(與 Python、Dafny、Verus 並列時) | Rust |
| open hands | OpenHands |
| codeex / cloud code | Codex / Claude Code |
| openAIO3 | OpenAI o3 |
| GBT 5.6 / GPT 5.6 | GPT-5.6 |
| deepseeker | DeepSeek |
| aent / aging evaluation | agent evaluation |
| result hacking(語意) | 指評估結果被作弊操縱 / gaming the evaluation result |

## 待確認 / To Verify

- 三位講者的正確姓名與職稱:主持人介紹第一位時字幕作 "Eson",後續講者稱其為 "Justin";第二、三位自稱 "Jun" 與 "Joy"。官網議程未列講者,需以影片投影片或 RDI 官方資料核實。/ Correct names and titles of all three presenters — captions give "Eson" (referred to later as "Justin"), "Jun", and "Joy"; the agenda lists none.
- Repository 級 verifiable code generation benchmark 的正確名稱(字幕作 "VO" / "Vau" / "VU"),需看投影片確認。/ Correct name of the repository-level verifiable code generation benchmark.
- 在該 benchmark 上表現最好的 agent 組合,字幕作 "a code plus GPT 5.5",可能是 Claude Code 或 Codex 搭配 GPT-5.5,需確認。/ The best-performing agent, rendered as "a code plus GPT 5.5".
- 「最強 agent 只解出 27 個 repository」與「benchmark 共 43 個 repository」的數字關係與「frontier-resistant」的描述看似不一致,需核對投影片(可能是 27% 或其他單位)。/ "Solved only 27 repositories" against a 43-repository benchmark seems inconsistent with calling it frontier-resistant — check the slides.
- Fable 5 在哪些領域相對較弱,字幕作 "life science and avidia visual and media",領域名稱需確認。/ The domains where Fable 5 lagged; captions render them as "life science and avidia visual and media".
- Cybersecurity Observatory、SuperRed、ALE phase 2 投稿平台的實際連結(講者以 QR code 呈現)。/ Actual URLs for the cybersecurity observatory, SuperRed, and the ALE phase-2 submission platform (shown only as QR codes).
- ALE 「hardest tier 最高完全通過率 2.6%」與「GPT-5.6 在最難 tier 約 5%」「最新版最好約 8%」三個數字的口徑差異(是否為不同版本或不同 tier)。/ Reconcile the 2.6% / 5% / 8% figures — they may refer to different snapshots or tiers.
