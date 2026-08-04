---
title: "Panel: Agentic AI in Capital Markets"
title_zh: "座談:資本市場中的 Agentic AI"
speaker: "Jeff Wecker、Jen Allum、Ali Nazari、Li Deng(主持:Bradley Olson)"
affiliation: "Jeff Wecker — CTO, Two Sigma / Jen Allum — SVP, Co-Head of GenAI, The D. E. Shaw Group / Ali Nazari — Head of Deep Learning Research, Susquehanna International Group / Li Deng — Chief AI Officer, Vatic Investments; Former Chief AI Officer, Citadel(主持:Bradley Olson — Technology Editor, WSJ)"
type: panel
stage: Plenary
date: 2026-08-01
session: "Session 5: Agentic AI in Capital Markets"
video: "https://www.youtube.com/watch?v=Tcn5Yb2K0h4&t=13853s"
video_range: "03:50:53–04:21:47"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [finance, quant-trading, evaluation, talent, panel]
---

# 座談:資本市場中的 Agentic AI(Panel: Agentic AI in Capital Markets)

**一句話總結**:量化投資機構全面擁抱 agentic AI,但因為「犯錯成本極高、訊號極度雜訊」,他們的重點不是把模型做大,而是把**評估內建進研究迴圈**、把**信任當成需要反覆重建的東西**,並重新定義人才標準與 compute 的投資報酬。
**One-line summary**: Quant firms have adopted agentic AI wholesale, but because mistakes are expensive and signals are brutally noisy, their focus is not scaling models — it is building evaluation into the research loop, treating trust as something that must be continually re-earned, and rethinking both the talent bar and the ROI on compute.

## 中文筆記

### TL;DR

- **金融與軟體業最大的差別是「犯錯成本」**:軟體公司出錯有 unit test 兜著,金融出錯直接虧錢、甚至波及社會。因此量化圈雖然歷來是新技術的早期採用者,面對 agentic 系統卻必須格外謹慎。
- **信任不只要「取得」,還要「重新取得」**:模型會換、資料會變、市場會 shift——六個月前你信得過的東西,現在未必還信得過(Ali Nazari)。
- **瓶頸不會消失,只會位移**:frontier model 一次給你 30 個看起來都很棒的研究點子,難題就從「想不出點子」變成「判斷哪個點子值得你花時間」。
- **Scaling law 在金融可能不適用**:Li Deng 說他們花了好幾年嘗試 scaling,從未看到 emergent capability;金融真正的關鍵是**整個系統的設計**,特別是輸出端的評估與回饋迴圈,因為市場會對你的下單產生反應、環境本身會被你改變。
- **Compute 需求的下一波爆炸**:Two Sigma 有 1,800 名員工,但若每個人背後跑著總計 25 萬個 agent、各自產生 compute 需求,ROI 就必須被認真計算——「找 alpha 本來就要挖很多口乾井,但你得問自己失敗得夠不夠快」。
- **人才標準已經翻轉**:Two Sigma 取消了 coding test(「不然是在測 LLM 不是測人」);Vatic 從「沒 PhD 的履歷看都不看」變成一半以上的人沒有 PhD,實習生用大四生,agentic 工作做得比正職還快。

### 重點整理

#### 開場:各自的 wow moment 與失望時刻(約 03:51–03:58)

主持人 Bradley Olson 請每位講者自我介紹時,順便講一個最近的「wow moment」或「AI 表現不如預期」的時刻。

- **Jeff Wecker**(Two Sigma 工程負責人;此前為 Goldman Sachs 合夥人暨首任 Chief Data Officer,更早在 Bridgewater Associates 重建其投資引擎):幾年前拿 LLM 問育兒建議,「糟糕透頂」;最近再試一次結果相當驚艷。「我不知道是 LLM 變好了,還是我變差了。」
- **Jen Allum**(D. E. Shaw AI 團隊共同負責人):最近讓她驚喜的用法不是什麼革命性的東西,而是**把 AI 當 executive coach**。D. E. Shaw 以「精準溝通」著稱,這正是她想精進的領域;只要給對 context,AI 能給出即時、可執行、質化與量化兼具的回饋。
- **Ali Nazari**(Susquehanna 深度學習研究負責人;此前創辦過一家深度學習對沖基金,更早是資訊理論學者)講的是**失望**:一個月前他把一個研究問題丟給 frontier model,對方回了大約 30 個看起來都很有道理的解法,每一個若他自己想都要花上數月甚至數季。然後他意識到——最難的部分並沒有消失,只是**位移**了:他現在花的時間不是「生成想法」,而是「判斷這 30 個裡哪一個值得他的時間」。
- **Li Deng**(在 Microsoft 約 18 年,後加入 Citadel,現於 Vatic Investments)給了三個 wow moment:
  1. **2010 年**,受 Geoffrey Hinton 啟發首次認真看神經網路,頭兩三個實驗就把錯誤率砍掉三分之一到二分之一,他當場決定丟掉所有其他工具(在那之前他把所有機器學習工具都改寫成 Bayesian network),2010 年就已經在做 13–14 層的深度網路——當時 Microsoft 大多數人都不相信。
  2. **ChatGPT 出現時**,他第一反應是「一定有哪裡出錯了」——這正是當年別人對他語音辨識成果的反應(「你八成把訓練和測試資料混了」)。但 ChatGPT 是真的產品、真的在被使用,不可能造假。他得請一位曾經向他匯報、當時在 Google 帶推理團隊的舊部屬向他解釋:有一類 decoding 技術跟傳統機器學習完全不同。
  3. **Agentic AI**:不只是 pattern matching,而是真的能推理、能把東西組合起來、能做知識管理。

#### 金融業的採用曲線:差別在「犯錯成本」(約 03:58–04:03)

**Jeff Wecker** 先描述 Two Sigma 的形狀:「我們基本上是一家做投資的科技公司」——1,800 名員工中將近 1,000 人在工程、另外四五百人在建模,其餘才是所有其他職能。工程師拿到新工具的反應很直接:Claude 2025 年 2 月問世,他們幾週內就開始用、一個月到六週內就全面推開。真正讓他興奮的是**讓全公司每個人都把自己視為 AI first**——而且從各種指標(code branch 數、產出的文件、發表的東西)看得很清楚:**越早、越快採用的人,生產力提升幅度明顯越大**。現在連沒有技術背景的人都開始用 auto mode 的 Claude 或公司內部的 workbench,「創新速度是近年來最高的」。

**Ali Nazari** 補上關鍵的差異點:採用是真的,SIG 的工程師與研究員全都在用 AI 工具,但**金融和軟體公司最大的不同是犯錯成本**。軟體公司裡 AI 出錯,有 unit test 接住,修一修就過去了;金融業出錯要付出金錢代價,某些情況下甚至會波及整個社會。量化金融歷來是統計學習、機器學習的早期採用者,但面對 agentic 系統必須更小心。他提出的框架是:

> 有些事我一定用 AI,有些事我還是希望有人在迴圈裡。而且**信任不只要取得,還要一再重新取得**——模型會換、資料會變、市場會 shift,六個月前你信得過的東西,現在未必還信得過。

**Jen Allum** 回答「如何鼓勵團隊實驗、又如何決定什麼值得規模化」:她認為外界低估了一件事——**這類公司本質上就是創新事業**,持續創新是生存必需,所以實驗的 DNA 和歷史本來就在。D. E. Shaw 作為最早的量化基金之一,又是多策略的聯邦式組織,可以在全公司同時放很多實驗、由下而上地找到價值所在。她的原則是:看的是**學習速率與發現速率**,政策上採「maximalist」——自建、外購、以及兩者之間的一切都做,先讓大量實驗跑,**看什麼燒起來**,再回頭想要為誰、以什麼方式規模化。

#### 雜訊、評估,與 agentic 的自我改進迴圈(約 04:04–04:07)

**Li Deng** 把量化與科技業的工作流做了對照:量化這邊是抽取特徵(即 alpha)→ 用模型做預測 → 實驗與評估(叫 back-testing,對應科技業的 validation)→ 上線(paper trading / online trading,對應 testing)。**關鍵差異在於訊號極度雜訊——輸入訊號雜訊,輸出訊號更雜訊。**

他當年從 Microsoft 轉戰華爾街,部分原因就是想搞清楚這件事:他原以為這會是個無監督問題(訊號雜到不如放棄),結果發現是混合的——純無監督哪裡都去不了,是有一點監督訊號,只是雜訊極大。第一次看金融資料(把報酬 residualize 之後)他以為自己拿到了錯的資料,「看起來幾乎全是隨機噪音或隨機漫步」,但訊號確實在裡面,只是要從中萃取極微小的一點。

他點名當天稍早 Google DeepMind 的 **Oriol Vinyals** 講的遞迴式自我改進 pipeline:「那些 pipeline 我們全都走過了」,但他們把**遠多得多的力氣放在評估端**——因為當評估的輸出本身極度雜訊時,你連「該預測什麼訊號」都不知道,更不知道要怎麼提供正確的回饋去改進特徵。

關於 scaling,他講得很直白:過去幾年的工作**重點不在把模型做大、期待像大語言模型那樣冒出 emergent capability**。「我們試了不少,但不知道還要走多遠;因為輸入輸出本質上就雜訊,我們其實已經放棄那條路了。」真正的焦點是:如何讓整個系統形成正確的自我迴圈——而 **agentic 方法正是把 alpha 工程師的人力投入降到最低的關鍵**。

#### Compute 成本:下一波爆炸就在眼前(約 04:07–04:09)

**Jeff Wecker** 從公司的建模史講起:26 年前創立時多是低維度統計模型,接著是中低階機器學習模型,再到 ensembles,然後開始自己訓練 transformer。直到 GPT-3.5 出現,才終於能用公開可得的模型——因為 frontier 公司在訓練上給了大家如此巨大的起跑優勢,大幅降低了成本。

而現在 agent 中心的工作流帶來的是另一件事:

> 我們今天有 1,800 名員工。但如果這 1,800 人背後有 **25 萬個 agent** 在跑作業、每一個都產生自己的 compute 需求,我們就真的必須認真想這件事的投資報酬。

他坦承「找 alpha 本來就要挖很多口乾井,這毫無疑問」,但關鍵是要檢視 alpha 投資的成熟度模型,並問自己:**你失敗得夠快嗎?**——夠快才能擋住 compute 那邊龐大的投資需求。

#### AI 時代的人才與招聘(約 04:09–04:14)

**Jen Allum**:D. E. Shaw 一向以尋找特定類型的人著稱——好奇心、終身學習者、批判性思考者、系統性思考者;這些特質**現在更重要**。而因為公司裡數十年的長職涯很常見,她真正在找的是**適應力**:這個人未來會在同一家公司裡經歷好幾段不同的職涯。所以她在建團隊時,是把這些特質的權重拉高到與職能專業並列,並且往前多想一步——這個人的下一個角色、再下一個角色會是什麼。

**Ali Nazari**:有些標準不變(聰明、好奇、會問對問題、能獨立工作),而且比以前更重要。**變的是面試流程**——過去的考法是為「實作是最難的部分」那個時代設計的。現在 AI 包辦了大量實作,他們要驗證的變成:這個人能不能適應、能不能正確使用工具、以及**能不能察覺 AI 系統「非常有自信地說錯話」**。他丟出一個開放問題:

> 判斷力向來是這樣長出來的:你試、你犯錯、你從錯誤中學。但如果現在大部分實驗都是 AI 在做,**下一代的判斷力要從哪裡長出來?**

**Li Deng** 給了非常具體的數字變化:兩年前團隊成員大多是 Ivy League 的數學、物理、部分資工博士;以前收到沒有博士學位的履歷,「看都不看,直接說抱歉我們不收非博士」。**現在超過一半的人沒有博士學位**,實習生他們偏好收大四生——這些人做 agentic 的工作往往比正職還快。「整個人才輪廓在短短兩年內變了很多。」

**Jeff Wecker** 補了一句給現場聽眾:「我先澄清一下,**我們有在招人**。」但要的東西很不一樣:

> 我們當然已經取消 coding test 了——不然我們是在測 LLM,不是在測人。

他認為科學家 / 電腦科學家 / 工程師這類角色反而會更重要,關鍵能力是:把問題清楚地拆解成元件、能不能 prompt 出真正想要的結果、以及**能不能設計出會運用判斷力的 agent**,去加速特徵生成、模型生成、下單策略或投組建構模型的產出。他要的是有認知深度、願意好奇地把公司業務學進去,再把各自科學背景的技能拿來重構未來可能性的人。

#### 如果從零開始設計一家量化公司(約 04:14–04:17)

**Ali Nazari** 的答案結構清楚:量化交易分兩塊——研究(創造知識)與交易(使用知識),而他會把重心越來越放在研究側,並做三件事:

1. **讓每一次實驗——失敗的和成功的——都變成組織的知識**。特別是失敗:太多人把失敗放在自己腦袋裡,人一走知識就跟著走。
2. **把評估變成研究迴圈的一部分**,而不是最後才補上的東西。
3. **人類研究員與 AI 研究員走同一套研究流程、用同一套標準評估**,不管產出是 AI 生成還是人生成,從兩邊學到的知識都回流到組織的知識庫。

> 我看研究不是一堆任務的集合,而是一個持續學習的過程。我認為這是最大的區別。

**Jen Allum** 從合作方的角度補充:D. E. Shaw 自建不少,但也**廣泛地與外部公司合作**,並希望自己是個好的合作夥伴——尤其在受監管的領域裡交付產品,enterprise readiness、資安、以及對自家 IP 的保護都是硬需求。她認為(呼應 Ali 說的組織既有 know-how)市場上還有很大空間,值得更銳利地想清楚:**新產品對這類公司的價值主張到底是什麼、要怎麼才是「加值」而不是重複造輪子**。

#### Wildcard:一個大家普遍相信、但其實錯了的 AI 信念(約 04:17–04:21)

**Jeff Wecker**:錯的是「**你會需要更少的人**」這個想法。的確有些角色與工作未來不會存在,但在一個「系統性決策支援」會成為未來的世界裡,說你不需要技術人、科學家、數學家,這會被證明是錯的。他預期的結果反而是**大量新角色被創造出來**去承接勞動力的變化。

> 「未來人們不會有機會」這個被鼓吹的想法根本說不通。人類歷史上任何一項重大發明都不曾如此。世界會變、市場會長大,而能夠產生影響力的人只會越來越多。

**Li Deng**:他挑的是 **scaling**。當天稍早機器人與基礎模型的講者都在談第一波、第二波、甚至第三波 scaling;他認為在機器人領域也許成立,但**在金融領域他不相信**——他們花了好幾年嘗試 scaling,從來沒有到達 emergent capability 出現的那個點。他認為金融真正最重要的是**用系統性的方式看待整個系統**,尤其是機器學習各元件之間的整合、特別是輸出端的評估與回饋,因為**金融市場的回饋和科技業是完全不同性質的問題**,而這一塊的設計在 agentic 時代的權重只會更重。

他用一段親身經歷收尾:七年前他從 Microsoft 轉到 Citadel 時,他那位億萬富翁老闆親自告訴他——我們雇用你,**不是**期待你把語音辨識那套系統建構的專業搬過來。因為在科技業,你建一套翻譯系統、辨識系統,它今天能用、大概還能用一陣子,你每隔幾年才需要適應一次(比如換了總統、語言用法改變,語言模型才要跟著改;或者要等到編碼標準變了,原本訓練的系統才會壞掉)。

> 但你把那種思路帶進金融市場就會失敗。因為在金融市場裡,**你每下一次單,別人的反應就不一樣,你自己就改變了環境**——這種程度遠遠超過科技業。

結論:科技業那套關於 scaling 的傳統思維,以及今天在這裡聽到的很多東西,大部分可能都不適用於他們。

### 金句

> "The hardest part didn't disappear. It just moved."(約 03:54)

Ali Nazari 談 frontier model 一口氣給他 30 個研究點子之後的體悟:瓶頸從「產生想法」搬到了「判斷哪個想法值得你的時間」。

> "Trust is something that needs to be gained … and trust needs to be regained. Model change, data change, market change, market shift … something that you were trusting six months ago might not be trustable right now."(約 04:02)

金融業對 agentic 系統的核心態度:信任不是一次性的認證,是持續衰減、需要反覆重建的東西。

> "We have 1,800 employees today, but if behind those 1,800 employees there are a quarter of a million agents doing operations, all making their own compute demand, we really have to think about the implications, return on investment of that."(約 04:08)

Jeff Wecker 對 agentic 工作流帶來的 compute 需求爆炸提出的預警。

> "We've eliminated coding tests, of course — because we'd be testing LLMs and not people."(約 04:13)

一句話講完 AI 對技術招聘流程的衝擊。

> "I look at research as not a collection of tasks, [but] a process of continuous learning."(約 04:16)

Ali Nazari 對「從零設計一家量化公司」的核心答案。

> "In financial markets, every time you put an order into the market, people react differently — it changes the environment, much more so than the high-tech world."(約 04:21)

Li Deng 說明為什麼科技業的 scaling 思維難以移植到金融:你的行動本身就在改變你要預測的那個環境。

## English Notes

### TL;DR

- **The defining difference from software is the cost of a mistake.** In a software firm a bad AI output gets caught by a unit test; in finance it costs money and can spill over into society. Quant firms have historically been early adopters, but agentic systems demand more caution.
- **Trust has to be re-earned, not just earned.** Models change, data changes, markets shift — what you trusted six months ago may not be trustworthy today (Ali Nazari).
- **Bottlenecks don't disappear, they move.** When a frontier model hands you 30 plausible research directions at once, the hard problem shifts from generating ideas to deciding which one deserves your time.
- **Scaling laws may simply not transfer to finance.** Li Deng's team spent years trying to scale and never saw emergent capability; what matters instead is systemic design — especially evaluation and feedback on the output side, because the market reacts to your orders and you change the environment you are trying to predict.
- **The next compute explosion is a balance-sheet problem.** Two Sigma has 1,800 employees, but a quarter of a million agents behind them each generating compute demand forces a real ROI conversation: "you dig a lot of dry wells" seeking alpha — the question is whether you're failing fast enough.
- **The talent bar has already flipped.** Two Sigma dropped coding tests ("we'd be testing LLMs and not people"); Vatic went from discarding any CV without a PhD to having more than half its people without one, and prefers senior undergraduates as interns because they do agentic work faster than full-timers.

### Key Points

#### Opening: wow moments and disappointments (~03:51–03:58)

Moderator Bradley Olson asked each panelist to pair their introduction with a recent "wow moment" — or a moment when AI fell short.

- **Jeff Wecker** (runs engineering at Two Sigma; previously partner and first Chief Data Officer at Goldman Sachs; before that rebuilt Bridgewater's investment engine) tried an LLM for parenting advice a few years ago and found it "absolutely terrible"; a recent retry was genuinely impressive. "I don't know if the LLMs have gotten better or I got a lot worse."
- **Jen Allum** (co-head of one of D. E. Shaw's AI teams) picked something unglamorous: **AI as an executive coach**. D. E. Shaw is known for precise communication, an area she wants to improve, and she finds the feedback timely, actionable, and both qualitative and quantitative — provided you give it the right context.
- **Ali Nazari** (heads deep learning research at Susquehanna; previously founded a deep-learning hedge fund; before that an information theorist) chose a **disappointment**. A month ago he handed a frontier model a research problem and got back roughly 30 plausible solutions, each of which would have taken him months or quarters to reach alone. Then it hit him: the hardest part hadn't gone away — it had **moved**. His time now goes into deciding which of those 30 ideas is worth pursuing rather than into having ideas at all.
- **Li Deng** (~18 years at Microsoft, then Citadel, now Vatic Investments) offered three:
  1. **2010**: inspired by Geoffrey Hinton, he looked seriously at neural networks for the first time; the first two or three experiments cut error rates by a third to a half. He immediately abandoned every other tool (he had spent his first decade at Microsoft converting all his ML tooling to Bayesian networks) and was training 13–14 layer networks as early as 2010 — while most people at Microsoft refused to believe the results.
  2. **ChatGPT**: his first reaction was that something must have gone wrong — exactly the reaction others had had to his speech recognition results ("you probably mixed training and test data"). But ChatGPT was a shipping product being genuinely used, so it couldn't be an artifact. He had to ask a former direct report, by then leading a reasoning team at Google, to explain that a class of decoding techniques worked unlike anything in traditional ML.
  3. **Agentic AI**: not just pattern matching, but genuine reasoning, composition, and knowledge management.

#### The adoption curve in finance turns on the cost of mistakes (~03:58–04:03)

**Jeff Wecker** framed Two Sigma as "a technology firm that invests": of 1,800 employees, just under 1,000 are in engineering and another 400–500 in modeling. Engineers absorb new tools fast — Claude became available in February 2025, they were using it within weeks and had it broadly available within a month to six weeks. What excites him is getting **everyone** at the firm to think of themselves as AI-first, and the metrics are unambiguous: earlier and faster adopters are measurably more productive across code branches, written work, and published output. People with no technical background are now running Claude in auto mode or the firm's in-house workbenches in auto mode, and "the rate of innovation now is as high as it's been in recent memory."

**Ali Nazari** added the constraint that makes finance different. Adoption is real — every engineer and researcher at SIG uses AI tools — but **the cost of mistakes is the dividing line**. In a software company a bad AI output gets caught by unit tests, fixed, and forgotten. In finance it costs money, and in some cases carries risk well beyond the firm. Quant finance has been an early adopter of statistical learning and ML, but agentic systems require care. His framing:

> Some things I use AI for constantly; for others I want a human in the loop. And trust isn't just something you gain — **it has to be regained**, because models change, data changes, and markets shift. What you trusted six months ago may not be trustworthy now.

**Jen Allum**, asked how she encourages experimentation before committing to scale, argued that firms like hers are **underappreciated as innovation businesses**: the relentless need to innovate means the DNA and the institutional history of experimentation are already there. As one of the original quant funds and a federated business with multiple strategies, D. E. Shaw can run experiments across the organization and let value surface bottom-up. Her operating principle is to optimize for **rate of learning and rate of discovery**: be maximalist in policy, build and buy and everything in between, let lots of experiments run, **see what catches fire** — and only then decide where to scale it, for whom, and how.

#### Noise, evaluation, and the agentic self-improvement loop (~04:04–04:07)

**Li Deng** mapped the quant workflow onto the tech one: extract features (what quants call alpha) → model the forecast → experiment and evaluate (back-testing, the analogue of validation) → go live (paper or online trading, the analogue of testing). **The difference is noise: the input signal is noisy and the output signal is noisier still.**

Part of why he left Microsoft for Wall Street was to understand this. He expected the problem to be essentially unsupervised — the signal being so noisy you might as well ignore it — but found it to be a mix: pure unsupervised learning gets you nowhere, there is a little supervision, and it is extremely noisy. The first time he looked at financial data, after residualizing returns, he assumed he'd been given the wrong file: it looked like pure random noise or a random walk. The signal is there, but you're extracting a very small amount of it.

He referenced **Oriol Vinyals**' earlier talk on recursive self-improvement pipelines: "we went through them all," but his team weights **evaluation** far more heavily — because when the evaluation output is itself extremely noisy, you don't even know what the right signal to predict is, let alone how to give feedback that improves your features.

On scaling he was blunt: the work of the past few years has **not** been about making the model bigger and waiting for LLM-style emergent capability. "We tried quite a bit, but we don't know how far we'd have to go — because of the nature of the noisy input and output, we actually gave up on that part." The real focus is making the whole system close a proper self-loop, and **agentic methods are the key lever for minimizing the human effort alpha engineers have to pour in**.

#### Compute cost: the explosion is imminent (~04:07–04:09)

**Jeff Wecker** traced the modeling history: at the firm's founding 26 years ago it was mostly low-dimensionality statistical models, then low-to-mid ML, then ensembles, then training their own transformers. GPT-3.5 was the inflection where publicly available models finally became usable, because the frontier labs handed everyone such a head start on training that it collapsed the cost.

Agent-centric workflows change the shape of the problem again:

> We have 1,800 employees today. But if behind those 1,800 employees there are **a quarter of a million agents** doing operations, all making their own compute demand, we really have to think about the return on investment of that.

He conceded that "when you're seeking alpha, you dig a lot of dry wells — there's no doubt about it," but insisted on examining the maturity model of alpha investments and asking whether you are **failing fast enough** to hold back the compute spend.

#### Talent and hiring in the AI era (~04:09–04:14)

**Jen Allum**: D. E. Shaw has always hired for curiosity, lifelong learning, critical thinking, and systems thinking, and those qualities matter more now, not less. Because decades-long careers at the firm are common, what she's really screening for is **adaptability** — the expectation that someone will have multiple careers inside one organization. Building a team now means weighting those qualities alongside functional expertise and thinking a step ahead to the next role, and the one after that.

**Ali Nazari**: the constants hold (smart, curious, asks the right questions, works independently) and matter more than before. What changed is the **interview process**, which was designed for an era when implementation was the hardest part. With AI doing much of the implementation, they now test whether a candidate adapts, uses the tools properly, and — critically — can **detect when an AI system is confidently wrong**. His open question for the industry:

> Judgment traditionally develops by trying something, making a mistake, and learning from it. If AI does most of the experimentation for us, **how does the next generation develop judgment?**

**Li Deng** gave the sharpest numbers. Two years ago the team was mostly Ivy League PhDs in math, physics, and some CS; a CV without a doctorate was rejected unread. **Today more than half the team doesn't hold a PhD**, and for internships they actively want senior undergraduates — who often do agentic work faster than full-timers. "The whole talent profile has changed quite a bit in just two years."

**Jeff Wecker** wanted one thing on the record for the audience: "**we are hiring**." But the job is different:

> We've eliminated coding tests, of course — because we'd be testing LLMs and not people.

He argued the scientist / computer scientist / engineer archetype becomes *more* important going forward, with the load-bearing skills being: decomposing a problem cleanly into components, prompting to get the outcomes you actually want, and **designing agents capable of exercising judgment** to accelerate the generation of features, models, order-placement logic, or portfolio construction models. He's looking for people with the cognitive depth to be inquisitive, learn the business, and then bring their scientific training to bear on deconstructing what's newly possible.

#### Designing a quant firm from scratch (~04:14–04:17)

**Ali Nazari** split quant trading into research (creating knowledge) and trading (using it), said he'd weight research far more heavily, and named three concrete changes:

1. **Every experiment — failures included — becomes organizational knowledge.** Failures especially: people keep them in their heads, and the knowledge walks out the door when they leave.
2. **Evaluation becomes part of the research loop**, not something bolted on at the end.
3. **Human and AI researchers go through the same research process and are evaluated identically**, regardless of whether the output was AI- or human-generated, with knowledge from both flowing into the organization.

> I look at research not as a collection of tasks, but as a process of continuous learning. I think that's the big distinction.

**Jen Allum** took the partnership angle: D. E. Shaw builds a fair amount in-house but also **partners widely**, and tries to be a good partner. Delivering a product into a regulated space raises hard requirements around enterprise readiness, security, and IP protection. Echoing Ali's point about the know-how these firms already possess, she sees room for **much sharper thinking from product builders about what the actual value proposition is** — what a new product would be, and how it would be genuinely additive to a firm like theirs.

#### Wildcard: a widely held belief about AI that's wrong (~04:17–04:21)

**Jeff Wecker**: the wrong belief is that **you'll need fewer people**. Some roles and jobs won't exist, granted. But the idea that you won't need technologists, scientists, and mathematicians in a world where systemic decision support is the future will turn out false — and the likely consequence is a whole host of **new roles** created to absorb the shift in the workforce.

> The idea that there won't be opportunities for people in the future just doesn't make a lot of sense. It hasn't been true with any other major invention over human history. The world's changed, the markets grow, and the opportunity for more people to make an impact continues to grow.

**Li Deng** picked **scaling**. Earlier speakers in robotics and foundation models had talked about a first, second, and possibly third wave of scaling; he thinks that may hold for robotics but **does not believe it holds in finance**. His team spent years trying to scale and never reached the point where emergent capability appeared. What matters in finance is the **systematic view of the whole system** — especially the integration between ML components on the output side, evaluation and feedback — because feedback in financial markets is a categorically different problem from tech, and that design carries far more weight in the agentic era.

He closed with a story. When he moved from Microsoft to Citadel seven years ago, his boss — a billionaire — told him personally that they were hiring him but **not** for the systems-building expertise that had made his name in speech recognition. In tech, a translation or recognition system you build works today and keeps working for a while; you adapt every few years (a new president shifts how language is used, so the language model has to change; coding standards eventually shift and break a trained system).

> But in financial markets, every time you put an order into the market, people react differently — you change the environment, far more than in the high-tech world.

The conclusion: the traditional high-tech way of thinking about scaling, and much of what the audience had heard that day, may mostly not apply to them.

### Quotes

> "The hardest part didn't disappear. It just moved." (~03:54)

Ali Nazari, after a frontier model returned 30 plausible research directions at once: the bottleneck relocated from having ideas to triaging them.

> "Trust is something that needs to be gained … and trust needs to be regained. Model change, data change, market change, market shift … something that you were trusting six months ago might not be trustable right now." (~04:02)

The core stance of finance toward agentic systems: trust is not a certification, it decays.

> "We have 1,800 employees today, but if behind those 1,800 employees there are a quarter of a million agents doing operations, all making their own compute demand, we really have to think about the implications, return on investment of that." (~04:08)

Jeff Wecker's warning about what agentic workflows do to a compute budget.

> "We've eliminated coding tests, of course — because we'd be testing LLMs and not people." (~04:13)

The whole disruption of technical hiring in one line.

> "I look at research as not a collection of tasks, [but] a process of continuous learning." (~04:16)

Ali Nazari's answer to designing a quant firm from scratch.

> "In financial markets, every time you put an order into the market, people react differently — it changes the environment, much more so than the high-tech world." (~04:21)

Li Deng on why tech's scaling intuitions don't port: your own actions alter the environment you're predicting.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Two Sigma | 「做投資的科技公司」;1,800 員工中近 1,000 為工程、400–500 為建模 | "A technology firm that invests"; ~1,000 of 1,800 employees in engineering, 400–500 in modeling | Jeff Wecker 任職單位 / Wecker's firm |
| The D. E. Shaw Group | 最早的量化基金之一;多策略聯邦式組織,便於全公司平行實驗 | One of the original quant funds; federated multi-strategy structure enables org-wide parallel experiments | Jen Allum 任職單位 / Allum's firm |
| Susquehanna International Group (SIG) | 工程師與研究員全面採用 AI 工具,但對 agentic 系統採謹慎立場 | Firm-wide AI tool adoption among engineers and researchers, with a cautious stance on agentic systems | Ali Nazari 任職單位 / Nazari's firm |
| Vatic Investments | Li Deng 現職;團隊博士比例兩年內從近乎全部降到不足一半 | Li Deng's current firm; the share of PhDs on the team fell from near-total to under half in two years | 他此前為 Citadel Chief AI Officer / previously Chief AI Officer at Citadel |
| Claude(含 auto mode) | 2025 年 2 月問世後 Two Sigma 數週內採用;非技術背景員工也開始使用 auto mode | Adopted at Two Sigma within weeks of its February 2025 availability; now used in auto mode even by non-technical staff | 與內部 workbench 並用 / used alongside in-house workbenches |
| GPT-3.5 | Two Sigma 從「自訓 transformer」轉向「使用公開模型」的成本轉折點 | The cost inflection that let Two Sigma shift from training its own transformers to using publicly available models | Jeff Wecker 的建模史敘事 / from Wecker's modeling-history arc |
| Oriol Vinyals 的遞迴自我改進 pipeline | 當天稍早 Google DeepMind 的演講;Li Deng 表示「那些 pipeline 我們全都走過」 | Google DeepMind talk earlier the same day; Li Deng: "we went through them all" | 同場直播稍早的演講 / earlier talk in the same livestream |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Brad Olsen | Bradley Olson |
| Jeff Wcker | Jeff Wecker |
| Jen Alam | Jen Allum |
| Alina Zaryi | Ali Nazari |
| Lee Dang / Leah | Li Deng |
| Deeshaw / Dehore / Dshore / Dshaw / Dehaw | The D. E. Shaw Group |
| Saskuana | Susquehanna |
| SAS(「in quantitive finance SAS particularly」) | SIG(Susquehanna International Group) |
| VIT investment | Vatic Investments |
| Jeffrey Hinton | Geoffrey Hinton |
| basian network | Bayesian network |
| JP / JPT / CHG GBT | ChatGPT |
| GPT35 | GPT-3.5 |
| oral vine / v | Oriol Vinyals |
| high-tech wall / quant wall / high-tech war | high-tech world / quant world |
| aentic | agentic |
| the Atlantic area | the agentic era |
| evolation | evaluation |
| quantitive | quantitative |
| twothird | two-thirds |

## 待確認 / To Verify

- Bradley Olson 在自我介紹時說自己是「deputy bureau chief at the Wall Street Journal for technology」,官網議程列的是「Technology Editor, WSJ」。本文依議程為準,但兩者是否為同一職務的不同稱法待確認。/ Olson introduced himself as WSJ's "deputy bureau chief for technology"; the official agenda lists "Technology Editor, WSJ". Agenda used here; whether these are the same role under different labels needs checking.
- 字幕「we started using it within a few weeks and **WebGA** within a month uh six weeks」——推測為「we GA'd it within a month」(GA = general availability,即全公司開放),但無法確定,故正文寫為「一個月到六週內全面推開」。/ The "WebGA" fragment most likely means "we GA'd it" (general availability) within a month; unconfirmed.
- Li Deng 說「nowadays I think **two-thirds of them are no longer with the firm**」——語意可能是「當年那批純博士背景的成員三分之二已離職」,也可能是自動字幕誤植。此數字未寫入正文結論。/ Li Deng's "two-thirds of them are no longer with the firm" is ambiguous in the auto-captions and is not used as a load-bearing figure above.
- Jeff Wecker 說 Two Sigma「founded 26 years ago」;公開資料一般記為 2001 年創立(約 25 年)。依講者原話記錄。/ Wecker said the firm was "founded 26 years ago"; public sources generally date Two Sigma to 2001. Recorded as spoken.
- Li Deng 提到「I was reminiscent with uh **Jennifer** earlier today」——所指何人不明。/ The "Jennifer" Li Deng says he reminisced with earlier that day is unidentified.
- Li Deng 提到那位「當時在 Google 帶推理團隊」的前部屬,未具名。/ The former direct report "leading the reasoning team at Google" is not named.
