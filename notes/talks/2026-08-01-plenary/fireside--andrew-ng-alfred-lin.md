---
title: "Fireside Chat: Andrew Ng × Alfred Lin"
title_zh: "爐邊對談:Andrew Ng × Alfred Lin"
speaker: "Andrew Ng × Alfred Lin"
affiliation: "Andrew Ng — Founder, DeepLearning.AI / Alfred Lin — General Partner, Sequoia Capital"
type: fireside
stage: Plenary
date: 2026-08-01
session: "Fireside Chat"
video: "https://www.youtube.com/watch?v=Tcn5Yb2K0h4&t=15707s"
video_range: "04:21:47–04:46:30"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [agi, open-weights, jobs, startups, agency]
---

# 爐邊對談:Andrew Ng × Alfred Lin(Fireside Chat: Andrew Ng × Alfred Lin)

**一句話總結**:AGI 的時程之爭其實是定義之爭(而定義曾被商業合約扭曲);open-weight 模型的輿論戰在社群媒體上贏了、在華府還沒贏;而所謂「AI 失業潮」是被監管俘獲的恐懼敘事撐起來的假命題——真正的挑戰是**升級技能**,以及找到那些不需要別人允許就會動手做事的「高 agency」的人。
**One-line summary**: The AGI timeline debate is really a definitions debate — and the definition was once distorted by a commercial contract; the open-weights fight has been won on social media but not in Washington; and the "AI job apocalypse" is a false premise propped up by regulatory-capture fear narratives — the real challenge is upskilling, and finding people with the agency to act without asking permission.

## 中文筆記

### TL;DR

- **AGI 的時程完全取決於定義**:照原始定義(AI 能做任何人類能做的智力工作),Ng 認為還要好幾十年;照「能做 50% 有經濟價值的工作」這種被下修的定義,他說我們三、五十年前就到了。而下修這個門檻曾經有**明確的財務誘因**——Microsoft 與 OpenAI 的合約。該條款已變更,結果是「AI 的炒作變少了,我覺得是好事」。
- **Open-weight 之戰贏了一半**:社群媒體上的風向已經贏了,但**華府和各州議會還沒贏**,所以不能鬆懈。Ng 更進一步主張 open model **比 closed model 更安全**,並用自己團隊上週的親身經歷佐證:做 OpenWorker 的資安審查時,閉源前沿模型拒答,他們得靠 open-weight 模型才完成自己的安全審查。
- **泡沫風險在模型層,不在推論需求**:Ng 對「推論需求沒有實務上的天花板」很有信心(資料中心蓋出來就會被用掉);他不確定的是模型層——「每一塊投入資本換到的智能」是個很難算的方程式。
- **下一個 coding agent 級別的機會沒有人知道**:水平層的資訊發現已被 ChatGPT / Gemini 佔住且難以撼動;垂直應用目前最有價值的是 AI coding。Alfred Lin 的忠告:**顯而易見的事大公司也會做**,要找的是像 WhatsApp(國際簡訊成本)、相機、GPS 那樣「這個新載體獨有、而且不顯而易見」的東西。
- **不會有 AI 失業潮**:受 AI 影響最深的工作其實是軟體工程,而軟體工程的就業市場非常健康、還缺人。模式是:AI 釋出 30–50% 的時間 → 剩下的互補工作變得更有價值 → 人往上長、承接更大的範圍(前後端工程師變全端,行銷協調員變 full-cycle marketer)。
- **企業開始在職缺描述裡明寫要「high agency」的人**——Ng 的冷笑話:他們在找「highly agentic」的人。篩選方法是行為面試:問這個人過去五年到底自己動手做了什麼。

### 重點整理

#### AGI 還有多遠?先問你怎麼定義(約 04:22–04:24)

Alfred Lin 開場就丟出硬球:你二月說 AGI 大約還有 50 年,現在進展這麼快,還這麼認為嗎?

Ng 的回答是把問題拆開:**取決於你怎麼定義,我們可能 30 年前就到了 AGI,也可能還要好幾十年才到。**

他採用的是原始定義——**AI 能做人類能做的任何智力工作**。這意味著:AI 要能花五年寫出一篇原創的博士論文(或更快),也要能像我們任何人練習幾小時後就學會的那樣,**開一台卡車穿過森林**。「AGI 在我看來也得做到這件事。」照這個標準,還要好幾十年。

接著他點出定義被稀釋的原因:曾經存在一個**明確的財務誘因去降低 AGI 的門檻**,讓它更容易被宣告達成——來自 Microsoft 與 OpenAI 之間的合約(該條款後來已變更,所以這個誘因消失了)。當時的定義版本是「AI 能做 50% 有經濟價值的工作」。Ng 的反諷是:

> 要是我們一百年前就採用那個定義,那隨著大部分工作從農業轉移到非農業,我大概會宣布我們**三十年前、五十年前**就抵達 AGI 了。

他的結論帶著一絲樂觀:因為那份協議變更,**現在關於 AI 的炒作變少了,他覺得這是好事**。

#### Open-weight 模型:社群媒體贏了,華府還沒(約 04:24–04:29)

Alfred Lin 提到 Jensen Huang 生平第一則 X 貼文就是在為 open model 辯護,問 Ng 怎麼看、安全疑慮是否成立。

Ng 先回顧這幾年的體感:兩三年前他對**針對 open-weight 模型的攻擊之猛烈**感到意外。但動機並不難懂——

> 如果有人花了幾十億美元訓練一個模型,而別人放出一個 open-weight 版本、稀釋掉這筆投資的價值,那當然很不方便。

他說得很直接:兩三年前他人就在房間裡,聽到幾家公司(「就是大家想得到的那幾家」)的高層對政府監管者說出**坦白講是誤導性的、關於 AI 安全的誇大說法**,目的是推動監管俘獲(regulatory capture)。他很慶幸後來因為開源社群大量飛去華府、與國會和白宮溝通,**現在華府對這類監管俘獲的操作已有廣泛認知**。他也特別稱讚 Jensen Huang 那份聲明「寫得非常好,還沒讀過的值得一讀」。

但他的判斷是這場仗只贏了一半:

> 目前 open-weight 模型的輿論風向,**在社群媒體上贏了,但在華府、在我們的州議會還沒贏**。所以我們還不能放鬆對 open-weight 模型的防守。

接著是他最強的一個主張——**open model 在他看來比 closed model 更安全**,並附上上週的親身案例:他和 Rohit Prasad 一起發布了開源 agent harness **OpenWorker**,他的團隊要對它做資安審查時,**Claude Fable 5 和 GPT-5.6 Sol 超過某個程度就拒絕回答**,最後是靠 open-weight 模型才把自家的安全審查做完。他也提到當時「OpenAI 攻進 Hugging Face」的事件,認為 Hugging Face 正是需要 open-weight 模型來防禦自己。

他也講得很清楚這不是站隊:

> 我希望 Anthropic 和 OpenAI 都成功,兩家公司我都喜歡。我可能是全世界唯一一個 Sam 和 Dario **都當過我下屬**的人。[笑聲]

> 我希望能找到一條路,讓這些公司裡我所有的朋友都過得很好,**同時**也有一個美好的 open-weight、open-source 生態系——因為那能確保 **AI 不會有守門人**。

**Alfred Lin** 接著把 open source 放進商業史的脈絡(並刻意把討論從 open weight 拉回 open source):創投的歷史本來就是在找更便宜的做法。網路時代大量產品建在開源之上——沒有開源軟體,很多東西會貴得多、慢得多,而且只有少數公司蓋得起那種基礎設施。**資料庫的多樣性、瀏覽器的多樣性,都是開源帶來的。** 對新創而言,開源同時是**通路**、是「便宜地證明自己有多聰明多能幹」的方式、也是**招募手段**。他的結論是 open weight、closed、open source 各有各的位置;而「開源比較不安全」這個指控在軟體開源時代就出現過——是的,你得自己去補漏洞,但它仍然是最快讓你跑起來的路。

#### 泡沫風險:模型層 vs. 推論需求(約 04:29–04:31)

Alfred Lin:你最近說模型層有泡沫風險,「我是幫投資圈的朋友問的」,我們該擔心嗎?

Ng 把自己的說法拆成兩半:

- **他更有信心的那一半是推論需求**:「我認為**推論需求沒有實務上的天花板**。」再多的資本投進資料中心——只要蓋出來,我們大概相當長一段時間內都會把能蓋出來的推論產能用光。這不代表沒人會虧錢(也許會蓋過頭),但這邊的風險看起來比較低。
- **他不確定的那一半是模型層**:「**每一塊投入資本換到多少智能**」是個很難的方程式——投入的資本成長非常快,智能或許也成長非常快,兩者交叉的結果會怎樣,他不知道。他「審慎樂觀地認為沒有泡沫,但希望自己能排除這個可能,卻做不到」。

支撐推論側樂觀的具體理由是 AI coding:目前**滲透率還很低**,但所有用過 coding agent 的人都感受到速度與效率的提升,所以他非常有信心 AI coding 未來的滲透率會遠高於現在,並帶動 token 需求大幅成長。

#### 下一個 coding agent 級別的機會在哪?(約 04:31–04:37)

Ng 坦承「我不知道,我也希望我知道」,但分享了一個框架:對照網際網路的興起,價值分成**水平的資訊搜尋層**(Google、Bing 之爭)和**大量垂直應用**(Uber vs. Lyft 之於共乘,Travelocity、Expedia 之於旅遊,零售等等)。他的判斷是:

- **水平的資訊發現層**已經被 ChatGPT 和 Gemini 佔住,而且相當難以撼動。
- **垂直應用**裡目前單一最有價值的桶子是 **AI coding**,coding agent 的表現「相當驚人」。他的團隊也大量把 coding agent 用在資料科學工作上;他自己也花時間在金融領域、與一些大型銀行合作,發現金融服務同樣有很多有用的 agent workflow。

**Alfred Lin** 的回答是投資人視角:「如果我知道,我就自己去開公司了。」但他認為**現在可能是有史以來最適合創業的時候**,同時給出兩個難處與一個判準:

Sequoia 常談「科技的加速變化」有兩個很難的地方——**我們今天在談的東西,三個月前根本沒在談;這意味著今天談的東西,未來也不會再談。** 但如果你在創業(這比他這種投資創業者的人更吃緊),你必須做出**能撐十年的東西**;而在今天這種需要大量算力、因此得募一大筆錢的環境下,「要理解什麼能撐十年,非常非常難」。

他的判準是:**別做顯而易見的事**。

> 顯而易見的東西當然會被做出來——在座的各位會做,但大公司也會做。

他用行動時代做類比:網路上的一切都搬到了手機上,把網站變成 mobile web 或 app 有點麻煩,但沒有那麼難。真正的機會是**這個載體獨有、而且不顯而易見**的東西:

- **這個裝置永遠開著** → 所有通訊類 app 都爆發(email 爆發、簡訊爆發)。
- 但光是「做一個訊息 app」不夠。**WhatsApp 之所以不同,是因為它解的是國際簡訊的成本問題**——在美國國內大家吃到飽,簡訊不痛不癢;但國際簡訊非常貴,WhatsApp 解掉了它,才長成一家大公司。
- 這個裝置比筆電多了兩樣東西:**相機**(於是人人都成了攝影記者)和 **GPS**(前一代裝置沒有),這兩樣各自開出了投資領域。

> 所以每當我聽到有公司把既有的內容和流程餵進 AI——那顯然會被做出來。但**「在 AI 裡什麼東西會被做成本質上不一樣的樣子」,我覺得我們還沒把那個邊界推開**,而我在找的就是那個。

Ng 接著補上一個關於**護城河**的觀察:很多人在問「軟體的新護城河是什麼」,他認為這是非常有效的問題。他的態度是:能做又有價值的東西就去做,**但如果你做的東西任何人用 coding agent 三個月就能複製,那傳統 SaaS 的經營方式(做一個軟體、長期賣類似的軟體)恐怕得改。** 因此值得分析:哪些 deep tech 是真的難以複製、而且會長期有價值的?

他同時觀察到一種**新的建構模式**,而前沿實驗室其實已經在這樣做了:

> 你做出來的東西三到六個月就過時,但你不斷做出新的東西、它們也不斷過時——**然而每一次快速過時的過程,都幫你累積了某種資產**。於是你長期累積下來的資產,慢慢長成一個比較有防禦力的護城河。

#### 不會有 AI 失業潮(約 04:37–04:42)

Alfred Lin 問他為何多次說「不會有 AI 失業潮(no AI job apocalypse)」。Ng 的回答分成診斷與機制兩層。

**診斷**:「AI 會讓 50% 的人失業、街頭會有暴動」這類說法是假的。這其實是企業**監管俘獲恐懼敘事**的一部分——「我的技術很危險。不,我的更危險。不,快點更用力地監管我。」他還引用《Wall Street Journal》幾天前的報導:一些原本以為 AI 會減少人力的大企業,**現在反過來開始加大招募**。

**最強的反證來自軟體工程本身**:受 AI 影響最深的工作正是軟體工程(因為 coding agent),然而軟體工程的就業市場**非常健康**,而且「我們根本找不到足夠的、有本事的 AI 工程師」。

**機制**:他預期 AI 進入金融、行銷、HR、行政等領域時會重演同一個模式——**極少發生職業崩潰,人反而更忙**:

- 一個後端工程師開始用 coding agent,釋出了大概 30–50% 的時間(他自己也不確定確切數字)。
- 但**剩下那些「與寫程式互補」的工作,價值反而更高了**。
- 於是工程師往上長、承接更大的範圍——「所以現在我不再雇前端或後端工程師了,幾乎所有人都是全端,因為我們現在都能做。」
- 其他職務已經看到早期跡象:原本只負責統籌行銷活動的 marketing coordinator,若 AI 釋出 30–40% 的時間,就能往上長成 **full-cycle marketer**——從頭到尾跑完行銷活動、做資料分析、驅動成長。

他的結論是:**「AI 能 100% 取代該職務 100% 的任務、因而導致整個職業類別崩潰」的工作,數量會非常少。**

但真正的挑戰隨之而來——**升級技能(upskilling)**:如果你 30% 的工作消失了,你要怎麼往上長、承接更廣的任務,同時學會使用 AI?這正是他仍然花大量時間在 Coursera、Udemy、DeepLearning.AI,以及**本週剛宣布的 LearnVector** 上的原因。

**Alfred Lin** 補上一個學術界的視角:我們此刻就坐在一所學術機構裡,而學術的基本命題是——**每個問題都有解,而每個解都會製造出更多問題。我們不會用完問題。** 他也用了農業的類比:兩百年前我們有 80% 的人得在農場上確保自己有飯吃,能把那件事自動化掉、讓我們去做別的事,其實是好事。他同意軟體工程師未來也許不再寫程式,但呼應前一場座談:**把大問題拆成越來越小的問題的能力**、以及**判斷該解哪個問題的能力**,仍然重要,而且不會消失。

Ng 最後把話題收到一個他認為被嚴重忽視的方向。他說在他們對軟體專業人士的調查裡,**很多人其實是困惑的**——不知道該往哪走、該學什麼,而且擔心學了三個月就過時的東西。所以他花很多時間去釐清:所謂「擅長 AI engineering」到底具體需要哪些技能,然後幫人們抵達那裡。

> 我知道矽谷有大量的心力投在加速 AI 的發展,我完全支持,讓我們繼續。但**它的互補面得到的關注嚴重不足**——所以我也想花更多時間在的,不只是加速 AI 的發展,而是**加速人的發展**。

#### 給現場的建議:找(和成為)高 agency 的人(約 04:42–04:46)

Alfred Lin 提到 Ng 二十年前正是在柏克萊念博士,問他會給在場的人什麼建議。

Ng 先接了一句題外話:「在你列的所有頭銜裡,你漏掉了一個我大概最引以為傲的——**父親**。那真的很珍貴。」(全場鼓掌)

然後他說:「這聽起來很老套,但**現在聽起來就是有史以來最適合建造的時候**。」他的團隊看到太多機會了;是的,因為 coding agent 他們能寫得更快,但**點子清單成長的速度,似乎比他們部署 coding agent 追趕的速度還要快**。

他真正想講的是一個招聘上的觀察。他的團隊長期以來除了找技術能力、AI 能力強的人以外,還特別找**高度 agency(high degree of agency)**的人:

> 意思是那種不等別人告訴他該做什麼的人——他會四處看看公司裡、環境裡、學校裡發生了什麼,然後有足夠的主動性直接決定「我要做這件事」。用安全負責的方式做、不要傷害到別人,但**真的有些事情你不需要請求許可**,就去做、去驗證它;就算失敗了,只要不傷害任何人,那也沒關係。

而他覺得最有意思的是:**越來越多職缺描述真的開始在找「高 agency」的人。**

> 而這件事有個很怪的說法是——我看到有公司在找**「highly agentic」的人**。[笑聲]

Alfred Lin 追問怎麼篩選這種特質。Ng 的答案是**行為面試**:去問這個人實際上做了什麼。

> 如果有人說「過去五年我做了我老闆叫我做的事」,那是一種人。但也有人會說「你知道嗎,我業餘時間做了這個、週末做了那個,這個失敗了、那個也失敗了,喔但那件事成功了,我又試了這個那個,不行,但這個可以」——

他最後把這件事拉回動機:其實這也非常好玩。他舉了自己昨晚的例子:**同時跑 Codex 和 Claude Code、餵同一個 prompt,睡一覺起來看哪個做得比較好**;而且來會場的車上他又開了一個。

> 我做這些事是因為好玩。有時候我做出來的東西剛好對別人也有用,那非常令人滿足;但很多時候我做的東西完全沒用、永遠不會見天日。可是那些**非常廉價的大量失敗**,本身也是很好玩的事——只要用不會危害到任何人的、負責任的方式去做。

### 金句

> "Depending on how you define AGI, we might have gotten to AGI either 30 years ago, or quite possibly not yet for many decades."(約 04:23)

一句話說明 AGI 的時程之爭,本質上是定義之爭。

> "There was a specific financial incentive to lower the bar for AGI, to make it easier to get there."(約 04:23:30)

指 Microsoft–OpenAI 合約中曾採用的「能做 50% 有經濟價值工作」定義;條款已變更。

> "The battle for the sentiment of open-weight models is won on social media, but it is not yet won in Washington DC and in our state houses. So we cannot yet relent on our defense of open-weight models."(約 04:26)

Ng 對 open-weight 現況的判斷:輿論贏了一半,不能鬆手。

> "I might be the only person in the world that both Sam and Dario has worked for."(約 04:26:55)

在強調「我希望 Anthropic 和 OpenAI 都成功」時的自嘲。

> "I don't want there to be gatekeepers to AI."(約 04:27)

他支持 open ecosystem 最根本的理由。

> "There will be no AI job apocalypse."(約 04:37)

全場最直接的一句斷言。

> "I would like to also spend more time on accelerating not just AI development, but on accelerating human development."(約 04:42)

他認為矽谷嚴重忽視的那個互補面。

> "I see companies looking for people that are highly agentic."(約 04:44:50)

在 Agentic AI Summit 現場最貼題的一個笑點——同時是他對人才的真實判準。

## English Notes

### TL;DR

- **AGI timelines are entirely a definitions fight.** On the original definition (AI that can do any intellectual task a human can), Ng still says many decades. On the watered-down "50% of economically useful work" version, he'd have declared AGI 30 or 50 years ago. And there was a **specific financial incentive** to lower that bar: the Microsoft–OpenAI contract. That clause has since changed, and the result is "less hype about AI, which I think is a good thing."
- **The open-weights fight is half-won.** Sentiment has been won on social media but **not in Washington or the state houses**. Ng goes further and argues open models are *safer* than closed ones, citing his own team's experience last week: doing a security review of OpenWorker, the closed frontier models refused past a point, and they needed open-weight models to finish reviewing their own software.
- **Bubble risk sits in the model layer, not inference demand.** Ng is confident there's no practical ceiling on inference demand — build the data centers and we'll consume the capacity. What he can't rule out is the model layer, where "intelligence per dollar invested" is a hard equation.
- **Nobody knows what the next coding-agent-scale category is.** The horizontal information layer is locked up by ChatGPT and Gemini; the most valuable vertical so far is AI coding. Alfred Lin's advice: **the obvious things get built by big companies too** — look for what's unique to the new medium and non-obvious, the way WhatsApp attacked international SMS cost, or the way the camera and GPS opened whole categories on mobile.
- **No AI job apocalypse.** The job most affected by AI is software engineering, and that market is healthy and short of talent. The pattern: AI frees 30–50% of someone's time → the complementary work becomes *more* valuable → people rise into broader scope (back-end and front-end developers become full-stack; a marketing coordinator becomes a full-cycle marketer).
- **Companies are now literally writing "high agency" into job descriptions** — or, as Ng put it to an Agentic AI Summit audience, they're looking for people who are "highly agentic." He screens for it with behavioral interviewing.

### Key Points

#### How far is AGI? Ask how you're defining it (~04:22–04:24)

Alfred Lin opened hard: in February you said AGI is about 50 years away — do you still believe that, given how fast things are moving?

Ng split the question apart: **depending on the definition, we might have reached AGI 30 years ago, or quite possibly not for many decades.**

The definition he uses is the original one — **AI that can do any intellectual task a human can**. That means AI that could spend five years writing an original PhD thesis (or do it faster), and also AI that could do what any of us could learn with a few hours of practice: **drive a truck through a forest**. "AGI seems to me like it would have to do that too." By that bar, many decades.

Then he named why the bar got diluted. There was a **specific financial incentive to lower the threshold for AGI** so it would be easier to declare — arising from the Microsoft–OpenAI contract (the clause has since changed, so the incentive is gone). The definition circulating then was "AI that could do 50% of all economically useful work." Ng's reductio:

> If only we had put that definition in place a hundred years ago, then as most work transitioned from agriculture to non-agricultural work, I would declare we got to AGI like 30 years ago, or 50 years ago.

His closing note was optimistic: because that agreement changed, **there's now less hype about AI, which he thinks is a good thing.**

#### Open weights: won on social media, not in Washington (~04:24–04:29)

Lin noted that Jensen Huang's first-ever X post was a defense of open models, and asked whether the security concerns hold up.

Ng started with the last few years: two or three years ago he was **surprised by the sheer intensity of the attack on open-weight models**. The motive isn't mysterious —

> If someone spent billions of dollars training a model, it's kind of inconvenient if someone else releases an open-weight version that degrades the value of that investment.

He was blunt about what he witnessed: he was in the room two or three years ago when executives from several companies — "the obvious ones" — told government regulators **frankly misleading, hyperbolic things about AI safety** in order to drive regulatory capture. He's glad that, thanks to the open-source community flying to DC and talking to Congress and the White House, **there is now broad awareness in Washington of those regulatory-capture moves**. He also praised Huang's statement as "really well written, worth reading if you have not yet."

But he scored the fight as only half-won:

> The battle for the sentiment of open-weight models is won on social media, but it is not yet won in Washington DC and in our state houses. So we cannot yet relent on our defense of open-weight models.

Then his strongest claim: **open models seem safer to him than closed models** — with a first-hand example from the previous week. He and Rohit Prasad had released **OpenWorker**, an open-source agent harness; when his team ran a security review of it, **Claude Fable 5 and GPT-5.6 Sol refused past a certain point**, and they had to use open-weight models to complete the security review of their own software. He tied this to the recent incident of OpenAI's models breaking into Hugging Face — noting Hugging Face needed open-weight models to defend itself.

He was equally clear this isn't tribal:

> I hope Anthropic and OpenAI succeed. I like both companies. I might be the only person in the world that both Sam and Dario has worked for. [laughter]

> At the same time, I hope we find a path to all of my friends in these companies doing well **and** having a wonderful, fantastic open-weight, open-source ecosystem — because that ensures there are no gatekeepers to AI.

**Alfred Lin** placed this in business history, deliberately pulling the frame back from open *weights* to open *source*: the history of venture capital is looking for things that are cheaper. A great deal of what was built on the internet was built on open source; without it, things would have cost far more, taken far longer, and only certain companies could have built that infrastructure. **The diversity of databases and of browsers exists because of open source.** For a startup, open source was simultaneously a **distribution channel**, a cheap way to demonstrate how capable you are and invite other developers to build with you, and a **recruiting tool**. His conclusion: open-weight, closed, and open-source models each have a place; and the "open isn't as safe" knock is the same charge levelled at open-source software — yes, you have to patch the holes if you use them, but it remains the fastest way to get up and running.

#### Bubble risk: the model layer versus inference demand (~04:29–04:31)

Lin: you said recently there's bubble risk in the model layer — asking for a friend in the investment community — should we be worried?

Ng separated the two halves of his own statement:

- **The half he's confident about is inference demand**: "there's no practical ceiling." However much capital goes into data centers, if we build them we'll consume all the inference capacity we can build for quite some time. That doesn't mean no one loses money — maybe we overbuild — but the risk there looks lower.
- **The half he's unsure about is the model layer**, where **intelligence per dollar invested** is a tough equation: capital going in is growing very quickly, intelligence is maybe also growing very quickly, and where that lands he doesn't know. He's "cautiously optimistic there isn't a bubble, but I wish I could rule it out."

His concrete grounding for the inference side is AI coding: **penetration is still very low**, yet everyone using coding agents sees real speed and efficiency gains — so he's very confident AI coding alone will reach vastly greater penetration and drive vastly greater token demand than today.

#### Where's the next coding-agent-scale opportunity? (~04:31–04:37)

Ng admitted "I don't know, I wish I knew," but offered a map. By analogy to the internet, value split between a **horizontal information search layer** (Google, Bing) and a **long tail of verticals** (Uber vs. Lyft in ride-sharing, Travelocity and Expedia in travel, retail, and so on). His read:

- The **horizontal information discovery layer** is held by ChatGPT and Gemini, and looks pretty hard to displace.
- Among **verticals**, the single most valuable bucket so far is **AI coding**, where coding agents have been "incredible." His own team uses coding agents heavily for data science work too; he also spends time in the financial sector working with large banks and finds plenty of useful agent workflows in financial services.

**Alfred Lin** answered as an investor: "if I knew, I would start a company." But he thinks **this may be the best time ever to start one** — and gave two difficulties and one test.

Sequoia talks about accelerating change having two hard properties: **what we're talking about today, we weren't talking about three months ago — which means whatever we're talking about today, we won't be talking about in the future.** If you're building a company (a bigger problem for founders than for someone like him who invests in them), you have to build something that lasts. And given the capital compute now demands, you'll raise a substantial amount and want it to last a decade — "it's very, very hard to understand what's going to last for a decade."

His test: **don't build the obvious thing.**

> The immediate thing that seems obvious — those things are going to get done by some of you in the audience, but it's also going to be done by large companies.

He used mobile as the analogy. Everything on the internet made it to mobile; turning a website into mobile web or a mobile app was a little complicated, but not that hard. The real openings were what was **unique to the device and non-obvious**:

- **The device is always on** → everything around communications blew up (email, texting).
- But a messaging app alone wasn't enough. **WhatsApp was different because it solved a cost problem: international SMS.** Domestically everyone had one data plan and SMS wasn't a big deal; internationally it was very expensive. Solving that built a big company.
- The device had two things a laptop didn't: **the camera** (everybody became a photojournalist) and **GPS** (not true of the previous generation) — each opening its own investable area.

> So when I hear about companies taking existing context and processes and feeding it into AI — that's obviously going to get done. But **what is uniquely going to be made differently in AI, I think we haven't pushed the boundaries of that**, and that's what I'm looking for.

Ng added a **moat** observation: many people ask what the new moats in software are, and he thinks it's a very valid question. His stance: if something can be built and it's valuable, build it — **but if whatever you build can be replicated by anyone with a coding agent in three months, the traditional way of running a SaaS business (build software, sell similar software for a long time) may have to change.** So the analysis worth doing is: which deep-tech things are genuinely hard to replicate and durably valuable?

He also flagged a **new pattern of building**, one the frontier labs are already running:

> You build stuff that goes obsolete in three to six months, but you keep having new stuff that keeps getting obsolete — and **everything that quickly goes obsolete helps you accumulate some asset before it goes obsolete**. So the asset you accumulate over time grows into, hopefully, a more defensible moat.

#### There will be no AI job apocalypse (~04:37–04:42)

Lin asked why he's repeated this line. Ng answered with a diagnosis and a mechanism.

**The diagnosis**: the claim that AI will put 50% of people out of work and there'll be rioting in the streets is false. It was part of the **regulatory-capture fear narrative** — "my technology is dangerous. No, mine is even more dangerous. No, regulate me harder." He cited a *Wall Street Journal* report from a few days earlier: some large businesses that expected AI to reduce headcount are **turning around and hiring more**.

**The strongest counter-evidence is software engineering itself**: it's the job most affected by AI, because of coding agents — and the software engineering job market is **very healthy**, with Ng adding "we just can't find enough skilled AI engineers."

**The mechanism**: as AI enters finance, marketing, HR, and administrative work, he expects the same pattern — **very rarely job collapse, and people ending up busier**:

- A back-end developer starts using a coding agent, which frees up maybe 30–50% of their time (he's not sure of the exact number).
- **The remaining work — the complement of the coding — becomes even more valuable.**
- So developers rise and take on broader scope: "these days I don't hire front-end or back-end developers. Almost all of my engineers are full-stack, because we can now all do that."
- Early signs elsewhere: a marketing coordinator who used to just run coordination, given back 30–40% of their time, can rise into a **full-cycle marketer** — running campaigns start to finish, doing the data analysis, driving growth.

His conclusion: **the number of jobs where AI can do 100% of the tasks 100% of the time, collapsing the whole category, will be very small.**

What follows is the real challenge — **upskilling**: if 30% of your job goes away, how do you rise up into a broader set of tasks *and* learn to use AI? That's why he still spends significant time on Coursera, Udemy, DeepLearning.AI, and **LearnVector, announced that week**.

**Alfred Lin** offered the academic frame: we're sitting in an academic institution, and the thesis of academia is that **every problem has a solution and every solution creates more problems — we're not going to run out of problems.** He reached for agriculture: 200 years ago 80% of us would be farming just to feed ourselves, and it's good we automated that so we could do other things. He agreed software engineers may not be the ones writing the code, but echoed the previous panel: **the ability to break large problems into smaller ones**, and **the ability to figure out which problems to solve**, aren't going away.

Ng closed the thread on what he thinks is badly under-served. In their surveys of software professionals, **people are confused** — unsure where to go, what to learn, and worried about learning something that goes obsolete in three months. So he spends a lot of time working out what being skilled at AI engineering actually requires, and helping people get there.

> I know here in Silicon Valley there's a ton of work on accelerating AI development. Fully support that, let's keep working on it. I think the complement of that has had insufficient attention — which is why I'd like to spend more time on accelerating not just AI development, but **accelerating human development**.

#### Advice to the room: find (and be) high-agency people (~04:42–04:46)

Lin noted Ng was a PhD student at Berkeley 20 years ago and asked what he'd advise the audience.

Ng first corrected the introduction: "Of all my credentials, you left one out that I'm probably most proud of, which is **father**. That's really precious." (Applause.)

Then: "This sounds cliché, but this sounds like the best time ever to build." His teams see so many opportunities — yes, they can code faster now because of coding agents, but **their list of ideas seems to grow even faster than they can deploy coding agents to keep up.**

His real point was about hiring. Beyond strong technical and AI skills, his team has long looked for people with a **high degree of agency**:

> Meaning people who don't wait to be told what to do — who look around, see what's going on in your company or your context or your university, and have the agency to just decide "I'm going to do this." Do it in a safe and responsible way, don't harm others — but really, **there are some things you don't need permission to do**. Just go do it and prove it out; and if it fails in a way that doesn't harm anyone, that's fine too.

What he finds genuinely interesting is that **more and more job descriptions are now asking for a high sense of agency**:

> And the weird way of saying this is — I see companies looking for people who are **highly agentic**. [laughter]

Asked how you screen for it, Ng's answer was **behavioral interviewing**: ask people what they've actually done.

> If someone says "for the last five years I did what my boss told me," that's one type of person. But then there are people who say "in my spare time I did this, on the weekend I did this, and this failed, and that failed — oh, but that thing worked, and I tried this and this, it didn't work, but that worked."

He grounded it in motivation: it's also just fun. His example from the night before — **running Codex and Claude Code in parallel on the same prompt, to see which had done better by morning**; and he'd kicked off another one in the car ride over.

> I do this stuff because it's fun. Sometimes I build something that ends up being useful to other people too, and that's very satisfying. A lot of the time I build stuff that's totally useless and will never see the light of day. But **many very inexpensive failures** is also a really fun thing to do — as long as someone does it in a responsible way that doesn't risk anyone.

### Quotes

> "Depending on how you define AGI, we might have gotten to AGI either 30 years ago, or quite possibly not yet for many decades." (~04:23)

The AGI timeline debate, restated as a definitions debate.

> "There was a specific financial incentive to lower the bar for AGI, to make it easier to get there." (~04:23:30)

On the "50% of economically useful work" definition that came out of the Microsoft–OpenAI contract; the clause has since changed.

> "The battle for the sentiment of open-weight models is won on social media, but it is not yet won in Washington DC and in our state houses. So we cannot yet relent on our defense of open-weight models." (~04:26)

Ng's scorecard on open weights.

> "I might be the only person in the world that both Sam and Dario has worked for." (~04:26:55)

Delivered while insisting he wants both Anthropic and OpenAI to succeed.

> "I don't want there to be gatekeepers to AI." (~04:27)

The root of his case for an open ecosystem.

> "There will be no AI job apocalypse." (~04:37)

The bluntest line of the session.

> "I would like to also spend more time on accelerating not just AI development, but on accelerating human development." (~04:42)

The complement he thinks Silicon Valley has badly neglected.

> "I see companies looking for people that are highly agentic." (~04:44:50)

The most on-theme joke possible at an Agentic AI Summit — and a genuine hiring criterion.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| OpenWorker | Andrew Ng 與 Rohit Prasad 發布的開源 agent harness / 桌面 AI coworker;其資安審查是本場「open model 更安全」論據的來源 | Open-source agent harness / desktop AI coworker released by Andrew Ng and Rohit Prasad; its security review is the source of his "open models are safer" argument | 2026-07-23 以 MIT 授權發布,本機優先、自帶 API key([GitHub](https://github.com/andrewyng/openworker)) |
| LearnVector | Ng 新創的 AI 原生學習公司,主打知識工作者的技能升級 | Ng's new AI-native learning company, aimed at upskilling knowledge workers | 2026-07-28 宣布,Coursera 策略投資 1 億美元、約三分之一股權;首批產品預計 2027 年初 |
| Jensen Huang 的 open-weight 公開信 | NVIDIA 執行長生平第一則 X 貼文,呼籲華府勿限制 open-weight 模型 | The NVIDIA CEO's first-ever X post, urging Washington not to restrict open-weight models | 2026-07-24,〈Open Weights and American AI Leadership〉,連署公司一日內從 25 家增至 50 家 |
| Claude Fable 5 / GPT-5.6 Sol | 資安審查中「超過某個程度就拒答」的兩個閉源前沿模型 | The two closed frontier models that "refused beyond a certain point" during the security review | 講者原話 / as stated by the speaker |
| Coursera / Udemy / DeepLearning.AI | Ng 持續投入的技能升級管道 | The upskilling channels Ng continues to invest time in | Ng 為 Coursera 共同創辦人 / Ng co-founded Coursera |
| Codex / Claude Code | Ng 前一晚以同一 prompt 並行跑的兩個 coding agent | The two coding agents Ng ran in parallel on the same prompt the night before | 他用來說明「高 agency」也源於好玩 / his illustration that high agency comes from fun |
| WhatsApp(國際簡訊)/ 相機 / GPS | Alfred Lin 用來說明「載體獨有且不顯而易見」的三個行動時代範例 | Lin's three mobile-era examples of what is unique to a new medium and non-obvious | 對應到 AI 時代該找什麼 / the template for what to look for in AI |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Alfred Lynn | Alfred Lin |
| Squire | Sequoia |
| Corsera | Coursera |
| open worker | OpenWorker |
| learn vector | LearnVector |
| fable 5 | Claude Fable 5 |
| 5.6 soul | GPT-5.6 Sol |
| open way models | open-weight models |
| expost | X post |
| regry capture / recapture | regulatory capture |
| OPI | OpenAI |
| track GP | ChatGPT |
| Uber and lift | Uber and Lyft |
| travel velocity | Travelocity |
| defenseful mode / new modes in software | defensible moat / new moats in software |
| job populace / (AI job) copyps | job apocalypse |
| clock code | Claude Code |
| codeex | Codex |
| "Almost all of my **agents** are full stack developers" | "Almost all of my **engineers** are full-stack developers"(前文為「我不再雇前端或後端工程師」)|
| Thanks, A. | Thanks, Alfred. |
| Loros Plaza(主持人閉幕致詞 / closing remarks)| Lower Sproul Plaza(UC Berkeley)|
| aentic | agentic |

## 待確認 / To Verify

- 字幕「we actually used **GM 5.2 too in Q3** in order to complete our own security review」——「GM 5.2」極可能是 **GLM 5.2**(OpenWorker 官方說明列出的 open-weight 選項包含 GLM 與 Kimi);「too in Q3」則可能是 **Qwen3**,但無法確定,故正文只寫「open-weight 模型」。/ "GM 5.2" is most likely **GLM 5.2** (OpenWorker's documented open-weight options include GLM and Kimi); "in Q3" may be **Qwen3**. Unconfirmed, so the note says only "open-weight models."
- Ng 提到「上週 OpenAI 攻進 Hugging Face、Hugging Face 需要 open-weight 模型來自我防禦」——此事件與 Dawn Song keynote 提到的 ExploitGym sandbox 逃逸事件應為同一件,公開報告出處待補。/ The "OpenAI hacking Hugging Face" incident Ng cites appears to be the same event Dawn Song described in her keynote (the ExploitGym sandbox escape); a public citation is still needed.
- Ng 引用的《Wall Street Journal》報導(「幾天前報導原本預期 AI 會減少人力的大企業轉為擴大招募」)確切篇目待查。/ The specific *Wall Street Journal* article Ng cites (large businesses that expected AI to cut labor now hiring more) has not been located.
- 主持人在介紹中稱 Ng「coined the term agentic(相對於 agentic AI)」——此說法出自主持人,未經查證。/ The MC's claim that Ng "coined the term agentic" is unverified.
- Ng 說 Microsoft–OpenAI 合約中的 AGI 條款「已經變更,所以那個誘因消失了」;變更的具體內容與時點未在對談中說明。/ Ng says the AGI clause in the Microsoft–OpenAI contract "has changed, so that's gone away"; the specifics and timing were not stated.
