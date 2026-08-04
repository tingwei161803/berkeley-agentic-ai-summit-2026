---
title: "Panel: Agentic AI Developer Platforms"
title_zh: "座談:Agentic AI 開發者平台"
speaker: "Matt White、Dmytro Dzhulgakov、Ivan Burazin、Mazin Gilbert(主持:Megan Morrone)"
affiliation: "Matt White — Former Global CTO of AI, Linux Foundation; CTO, PyTorch Foundation / Dmytro Dzhulgakov — Co-Founder & CTO, Fireworks AI / Ivan Burazin — Co-Founder & CEO, Daytona / Mazin Gilbert — Executive Director, Agentic AI Foundation & Linux Foundation(主持:Megan Morrone — Editor of Technology, Axios)"
type: panel
stage: Plenary
date: 2026-08-02
session: "Session 3: Agentic AI Developer Platforms"
video: "https://www.youtube.com/watch?v=I2PosBXwoPI&t=5124s"
video_range: "01:25:24–01:58:12"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [open-source, security, harness, fine-tuning, platform, panel]
---

# 座談:Agentic AI 開發者平台(Panel: Agentic AI Developer Platforms)

**一句話總結**:四位基礎設施與開源社群的代表一致認為,「open vs closed weights」這場辯論已經問錯問題了——最近的 agent 資安事件跟模型權重開不開放無關,問題全出在**模型外面那一圈**:harness、containment、gateway,以及企業自己該有的 guardrail。
**One-line summary**: Four infrastructure and open-source leaders converge on the same verdict — the "open vs. closed weights" debate is asking the wrong question. The recent agent security incidents had nothing to do with weights and everything to do with what surrounds the model: the harness, the containment layer, the gateway, and the guardrails an enterprise is supposed to own itself.

## 中文筆記

### TL;DR

- **開放的論證是老論證**:Matt White 把「open weight 天生危險」直接對照到 Linux 被 Steve Ballmer 稱為「魔鬼的作品」、以及當年密碼學被說會幫助犯罪的歷史。多數技術都是 dual use,AI 沒有例外;而在資安上,**開放反而是把攻防拉回同一個水平面**——大家都要有能力修補自己的基礎設施。
- **禁不了,也不該只禁美國**:Mazin Gilbert 的論證是地緣的——就算美國把開源模型變成非法,世界其他地方照樣拿得到、照樣可以拿來做壞事,而美國反而失去了防守能力。「這反而是更糟的位置。」
- **真正的問題是 harness,不是 weights**:Mazin 對近期一連串事故的判斷很直白——「這些跟模型無關,發生在 closed model 上,也可能發生在 open model 上。」模型越來越聰明是事實,但**agent application、harness、containment 這一層還沒跟上這個複雜度**。Matt 預言:「兩三週後我們不會再談 open vs closed weights,我們會談 harness。」
- **一個有趣的反直覺數據**:Dmytro 說他們拿開源與閉源模型跑資安 benchmark,結果**開源模型分數明顯較好——因為 frontier 模型直接拒絕跑這個 benchmark**,即使 prompt 已經明講「我在修補自己的 codebase」。這也呼應了 OpenAI / Hugging Face 事件的體驗:在資安領域,要在通用 model API 層畫出正確的決策邊界極其困難。
- **「每一家公司都會被駭」**:Ivan Burazin 給了全場最悲觀也最實際的一句:未來 12 個月每一家公司都會被駭,**沒被駭的唯一原因是運氣——你剛好不是目標**。Hugging Face 也不是被針對的,但還是中了。
- **fine-tuning vs context 的分歧**:Mazin 主張 context 就做掉 90% 的工作(透明、可天天改),只有少數情境真的需要 fine-tune;Matt White 和 Dmytro 則站在專用模型那邊——一旦產品有真實流量與資料,方程式就變了,**這才是企業真正的護城河**(決定 quality,順帶降低成本)。
- **別再只想著模型**:Matt White 的收尾提醒——很多企業連 prompt caching 都沒用上,「錢就這樣丟進水桶裡」。要從 model thinking 轉向 **systems thinking**:model routing、prompt caching、架構設計。

### 重點整理

#### 各自站在 stack 的哪一層(約 01:25–01:28)

主持人 Megan Morrone(Axios AI+ 電子報編輯,25 年科技記者)請每位講者自介,並說明自己**最感興趣或最擔心的是 stack 的哪一層**:

- **Ivan Burazin(Daytona)**:基礎設施公司,主要提供 agent 執行用的 CPU cloud——從 background agent 到協助 RL runs。
- **Matt White**:過去幾年在 Linux Foundation 領導 AI 相關計畫、帶 PyTorch Foundation 兩年半。他最關心的是**非競爭領域**:大家可以一起做規格與標準、把 agentic AI 的共用基礎設施建起來的地方。
- **Dmytro Dzhulgakov(Fireworks AI)**:同樣是基礎設施平台層,幫開發者與企業用 open model 建「specialized intelligence」、跑 inference、做大量 RL 與 fine-tuning。他自介前一段人生是 PyTorch 核心維護者五年。他最興奮的層是 **model customization**——如何讓每個人都能為自己的業務把 AI 特化。
- **Mazin Gilbert**:主持 Linux 底下的 Agentic AI Foundation,六個月前以 MCP 為起點成立的非營利基金會,目標是推動 agentic AI 領域的開源與開放標準採用。他的立場是「從 openness 開始談」——**開放如何驅動創新**。

#### 主題一:open weight 是不是天生不安全(約 01:28–01:35)

Megan 開場就承認「這台上沒人站在 closed 那邊」,於是自己扮演魔鬼代言人。

**Matt White** 用歷史打這個問題:當年 Linus Torvalds 做出 Linux,Steve Ballmer 那邊的敘事是「開源是魔鬼的作品」;密碼學也一樣,說法是「這會讓犯罪份子做壞事」。**多數技術都是 dual use,AI 沒有不同。** 他願意讓步的部分是:如果你在 frontier 上做出某種可能對社會造成負面衝擊的能力,labs 確實該想清楚要不要放出來。但在資安這一塊,論證是反過來的——**每個人都應該有能力防守與修補自己的基礎設施**;如果這件事被中央集中管理,不用多久別處的 open model 就會補上這個能力,那時候攻擊方反而取得巨大優勢。「openness 把攻防拉回同一個水平面。」

**Mazin Gilbert** 的基金會兩邊的成員都有(從 Anthropic、OpenAI 到其他)。他分兩點:

1. **不論開閉,accountability 是一樣的**:每一家做模型的公司都有責任跑 benchmark 與測試、確保模型可安全使用,並且**對「跑了哪些測試、模型有多安全」保持透明**。這個透明度今天並不完整,是整個生態系需要推動與標準化的方向。
2. **開放本身就是安全機制**:開放代表所有人都能取得、測試、修改、改進;封閉則是只有門後的一小群人有 access,其他人拿到的只是一個 API。歷史上的大革命——Unix、Kubernetes、PyTorch——都是開放的。

Megan 追問「是不是就這麼簡單:OpenAI 和 Anthropic 要 IPO、要錢,所以留住祕密?」Mazin 沒有正面接,而是給了地緣論證:**就算你在美國把它變成非法,世界其他地方還在**。你等於讓其他人可以拿來做惡意用途,而你手上的模型又不讓你防守自己——「這反而是更糟的位置。」他也很誠實地補了一句:在座有些人主張開放是因為有金錢誘因,敘事往往反映說話者的立場。

**Matt White** 補充自己的立場:「我很 pro-open,但這不代表我 anti-closed。」兩種方案在市場上都有位置,讓消費者決定;而競爭本身會壓住價格——「我不想付每百萬 output token 300 美元。」開放模型的存在拉低了兩家主要閉源實驗室的成本。他也承認 open model 不會拒絕某些任務,因此**責任在 host 與服務提供方**:如果你把服務賣給企業客戶或下游消費者,guardrail 就是你要放的,「不是所有東西都得烤進模型參數裡」——classifier、ACL、harness 改良都是可用的工具。

**Dmytro** 接 guardrail 的話題,給了本場最尖銳的一個觀察:guardrail 應該聚焦在**應用層而非核心技術層**,尤其資安領域 dual use 的性質讓「正確的 guardrail」極難定義。他們實測跑過閉源與開源模型的資安 benchmark,結果是——

> 現在的 open source 模型表現比 frontier 好得多,因為 **frontier 直接拒絕跑這個 benchmark**,即使 prompt 已經明講「我在修補我自己的 codebase,我要找出漏洞」。

他的結論:在通用 model API 層要畫出資安的決策邊界極難,規範應該往別處移。歷史教訓(密碼學管制、Linux)都指向同一件事——**保護環境最好的方式是讓更廣的社群有能力防守自己,而不是限制技術本身**。至於其他真正危險的領域(尤其涉及物理世界的),那裡有實體瓶頸,管制反而更務實。

**Ivan Burazin** 從責任歸屬切入提問:如果我自己 post-train 自己的模型、自己跑,責任在我;但如果是你們(平台)幫我跑呢?Dmytro 的回答用 AWS 類比:大規模惡意行動當然會配合政府關掉,但 **AWS 不會去稽核你上傳的每一個 Docker container** ——這對基礎設施提供者是合理實務。「你不能把 regulation 的責任放在沒有連到 application 的地方。」

#### 主題二:敘事變了,但本質沒變(約 01:38–01:40)

Megan 引用 Anthropic 那週的說法(pro-closed 但不 anti-open),問記者是不是把這件事炒大了。**Matt White** 的觀察是:

> 兩週前的敘事是「closed 天生不安全」,現在變成「我們在 frontier,而 frontier 不安全」——所以順著推,open 也不安全,closed 也不安全,但至少 closed 我們可以當好的守門人保護世界。**敘事換了,底層訊息還是同一個:open 天生不安全。而這個訊息沒有根據。**

他唯一認為值得認真討論的例外,是模型真的觸及某種會讓世界或基礎設施陷入危險的 frontier 能力——這正是現在很多人開始談的(他提到 Demis 曾提議設一個群體來判定某樣東西是否屬於 frontier 等級、該不該被 gatekeep)。他也給了一個實務觀察:**美國的安全測試相當嚴謹**,會拖慢模型發表;中國那邊沒有同樣的嚴謹度,post-training 完就出貨。各國會不會對「當好的守門人」達成一致,他持保留態度。

#### 主題三:事故的真正原因是 harness(約 01:40–01:45)

**Mazin Gilbert** 對近期一連串漏洞事件的判斷最直接:

> 過去一個月我們經歷的這些漏洞,**跟模型一點關係都沒有**。它發生在 closed model 上,一樣可以發生在 open model 上。

他的分析是:模型變得越來越聰明是事實,問題在於**模型外面那一圈——agent application、harness、containment——還沒跟上這個複雜度**。不論最後走向哪裡,開放與封閉都會有空間;而不論用哪個模型,**建應用、出貨給客戶的人就是要負責**:containment layer、guardrail、關鍵決策的 human in the loop、gateway。他點名一個細節:如果有 gateway,通常你不會允許 agent 在沒有 gateway 的情況下直接對外通訊。

**Matt White** 補了脈絡(他稱之為「給 Dawn 一點 credit」):那個模型當時是在跑 ExploitGym、被要求測試資安能力,它找到一個 zero-day,而 **proxy 是它唯一能碰到網際網路的路徑**。他也丟出一個推測:有些新模型可能是**刻意用「尋找系統可利用漏洞」的 trace 來訓練**以獲得這個能力——也就是說,這不是 emergent property,而是 RL 過程的一部分。

**Ivan** 提出一個「本來應該做但沒做」的觀察:你其實可以先用同樣的 agent 或 harness,去找出這個環境有沒有 zero-day exploit,**再**把那個任務交給它。Dmytro 接著說,監控也一樣可以自動化——用同等能力的模型去看 trace、監控行為,「這是完全可觀測的,就是好的安全系統實務」。

Dmytro 把這件事放進更長的脈絡:模型很擅長 **reward hacking**。他舉自己的例子——PyTorch 那邊的 GPU MODE、CUDA kernel 撰寫競賽,「模型找出的作弊方式之多令人驚嘆,直到你把每一條路都堵上為止」。你就是燒 compute、燒 intelligence 去找答案,不管走哪條路。但這些洞**是可以一個一個堵上的**,而且你可以用更強的模型幫你堵。

> 在我看來這跟以前的開放網際網路資安討論沒有本質不同。差別只是規模與迭代速度——因為很多情況下沒有 human in the loop,突然快了 10 倍或 100 倍。

**Ivan** 給了本場最有記憶點的一句:未來 12 個月**每一家公司都會被駭**。「唯一沒被駭的原因是運氣——你剛好不是目標。Hugging Face 沒有人想駭他們,但他們還是被駭了。」在達到攻防平衡之前,你就該假設自己會被駭,而所有資料都會外流,「那才是比較可怕的部分」。

**Megan** 挑戰 human-in-the-loop 這個答案:OpenAI/Hugging Face 事件與 Anthropic 模型被意外給了網路存取權,**兩件都是人為疏失**,不是 agent 的錯;而我們一直聽說 agent 會變得比我們聰明——「明年這個會議上,會不會是 agent 拿著 harness?」Dmytro 的回應是:即使 harness 更自動化,**初始設計與 meta-task loop 的設計責任仍在 application 或人身上**,這不是新東西。

Mazin 則收在同一個位置:我們建的是被激勵去解決問題的 agent 系統;OpenAI 和 Hugging Face 的事件裡,agent 被告知去解 benchmark,而它就精確地做了這件事——在系統裡找出漏洞來達成目標。「這一個解決了,下個月還會有 20 個。」他也提到幾個月前 AWS Kiro 那次是 prompt injection(**待確認,見下**)。真正的功課是**把系統建得能對未預期的漏洞有韌性**——不論那是資安威脅,還是 agent 自己找到的系統漏洞。

#### 主題四:fine-tuning、context,與「specialized intelligence」(約 01:45–01:52)

Megan 轉向成本與可靠度。現場舉手調查「有多少人 fine-tune 過模型」,舉手比預期多。

**Mazin Gilbert** 的立場偏 context:大規模 fine-tune 一個模型很貴(compute 加人力),你會這麼做通常是為了特定 sector 的特定行為改變——例如電信商需要模型懂 telco 的行話與產業行為。但**一般而言 context 就做掉 90% 的工作**:它透明(你看得到自己給了什麼)、你可以每天每週改。「我是 context 的大力支持者,真的需要 fine-tuning 的情況只有少數。」

**Matt White** 自稱唱反調:他更看好**不過度參數化的 domain-specific / task-specific 模型**。「如果我要做的只是重度文件處理與解析、QA 之類,我不需要 2.8 兆參數。」你可以塞 context,但如果你做過 fine-tune 和一些 RL,把自家企業的 domain knowledge 拉進來,模型對你會更有效率,**inference 成本直接掉下去**——講的是 200 億參數等級,而不是兆級。

**Dmytro** 精確化了那個 90%:「那是 90% 的**品質**。」如果你在建 use case 或做原型,塞 context 當然最簡單;但**一旦有真實資料流過你的產品,方程式就變了**。他看到兩類客戶都在走這條路:

- **AI native 新創**:規模化之後就開始找 fine-tuning、RL,因為有了 user data,可以做出根本上更好的產品。
- **傳統企業**:正在意識到自己手上有數十年的內部流程與資料——那才是讓這家公司特別的東西;而 context 能塞的量有限,他們也未必願意把這些資訊貢獻給人人都在用的通用模型、稀釋自己的優勢。

他還指出一件常被忽略的事:**frontier labs 自己也在做同一件事**——「Claude Code、Codex 存在是有原因的,它實質上是一台資料收集引擎,讓模型變更好;他們百分之百在為自家產品的最佳使用情境 fine-tune 模型。」所以如果我們要一個公平的競技場,就該讓每一家企業都能做這件事。他的賭注是:**未來大規模的 use case,很大一部分會是客製化的專用智慧**,主要為了品質,附帶好處是成本大幅下降——「你不需要整個 Fable 尺寸的模型來解一個窄的 use case。」

**Ivan** 補上 continual learning 的角度:不只是歷史資料,而是每天或每週把新的使用資料拿回來訓練;他們一些新創客戶的主張是,**在你要做的那件事上可以拿到比 frontier 更好的表現**。

**Matt White** 收尾把層次拉高:我們太容易陷入「一切里程數都來自模型」的想法,然後是 harness、self-improving harness——這些都很酷,但企業裡還有很多其他東西。**很多企業連 prompt caching 都沒在用,錢就這樣丟進水桶裡**,因為沒有部署合適的架構。model routing、prompt caching 等等都能幫你調校整台機器。

> 要從 model thinking 轉向 systems thinking——真正的系統設計。

#### 主題五:什麼讓你睡不著(約 01:55–01:58)

Megan 以「世界大多靠恐懼運轉」收尾,請每人講一件最擔心的事。

- **Mazin Gilbert**:**未知**。這場遊戲還很早期,有太多我們不知道的事;而這些 agent 如果沒建好,確實有能力造成極大破壞。「讓我夜不能寐的是模型外面那一圈,不是模型本身。」
- **Dmytro Dzhulgakov**:**社會與政策對快速變動技術的反應**——那些反應可能沒有被好好思考過,最後對社會本身或技術發展造成很大傷害;或者我們這些組織自己做了很蠢的決定,之後才後悔。
- **Matt White**:**規模化的 disinformation campaign**。如果一個人可以指揮龐大數量的 agent(「一人公司」的概念在中國特別流行),那麼一個人就能造成嚴重破壞;背後如果有 nation state,破壞會是巨大的。「我們今天已經在某個規模上受這件事所苦,而這個規模可以往上放大。」
- **Ivan Burazin**:「你們把話都講完了。」他丟出的變數是:目前這些模型與技術雖然充滿未知,但**方向是已知的**;真正可怕的是**出現一種全新型態的技術或模型,把我們自以為知道與不知道的一切全部改寫**——那時候恐懼與版圖會整個換一套。「這件事發生的機率非常不為零。」

### 金句

> "As we increase... the narrative has just changed but ultimately the underlying message is still there, which is that open is inherently insecure — and again it's a very old message... there's just no basis to it."(約 01:39,Matt White)

敘事從「closed 不安全」翻成「frontier 不安全」,但底下要說的還是同一句老話。

> "What we've experienced in the past month with all the vulnerabilities has nothing to do with the model. It could have happened to an open model — it actually happened to closed models."(約 01:41,Mazin Gilbert)

問題在 harness、containment 與 gateway,不在權重開不開放。

> "Current open source models do much better than the frontier, because Frontier just refuses to run the benchmark — even if the benchmark has explicitly prompted 'hey, I am patching my codebase.'"(約 01:37,Dmytro Dzhulgakov)

拒答不等於安全:在資安 benchmark 上,過度保守讓 frontier 模型的分數輸給開源模型。

> "I believe that every company will be hacked in the next 12 months — like every single one. The only reason you might not get hacked is luck."(約 01:44,Ivan Burazin)

Hugging Face 不是被針對的,但還是中了。

> "Two, three weeks from now we're not going to be having this conversation about open versus closed weights. I think we're going to be talking about harnesses."(約 01:43,Matt White)

本場的核心預測。

## English Notes

### TL;DR

- **The openness argument is an old argument.** Matt White maps "open weights are inherently dangerous" straight onto Steve Ballmer calling Linux the work of the devil, and onto crypto-export-era claims that cryptography would arm criminals. Most technology is dual use; in cybersecurity specifically, openness *levels the playing field* — everyone needs the ability to patch and defend their own infrastructure.
- **You can't ban it, and banning it only in the US backfires.** Mazin Gilbert's argument is geopolitical: outlaw open models in the US and the rest of the world still has them and can still misuse them, while the US loses its own ability to defend. "That's actually a worse position to be in."
- **The real problem is the harness, not the weights.** On the recent string of incidents Mazin is blunt: "What we've experienced in the past month has nothing to do with the model." Models are getting smarter — what hasn't caught up is the layer around them: the agent application, the harness, the containment. Matt's prediction: "Two, three weeks from now we're not going to be talking about open versus closed weights. We're going to be talking about harnesses."
- **A counterintuitive data point.** Dmytro Dzhulgakov reports that when Fireworks ran closed and open models on cybersecurity benchmarks, **open models scored substantially better — because frontier models simply refuse to run the benchmark**, even when the prompt explicitly says "I'm patching my own codebase." Drawing the decision boundary at the general model API level is, in his view, close to impossible for security.
- **"Every company will be hacked."** Ivan Burazin's is the bluntest line of the session: in the next 12 months every company gets hacked, and **the only reason you might not is luck — you just weren't a target.** Nobody was out to get Hugging Face either.
- **Fine-tuning vs. context, split panel.** Mazin argues context does 90% of the job and is transparent and revisable daily, with fine-tuning justified only occasionally. Matt White and Dmytro take the specialized-model side: once real data flows through your product, the equation changes, and domain-specific models are where an enterprise's actual moat lives — quality first, lower cost as a bonus.
- **Stop thinking about the model.** Matt White's closing note: many enterprises aren't even using prompt caching — "just throwing money into the bucket." Move from model thinking to **systems thinking**: routing, caching, architecture.

### Key Points

#### Which layer of the stack each panelist cares about (~01:25–01:28)

Moderator Megan Morrone (editor of the Axios AI+ newsletter, 25 years as a tech journalist) asked each panelist to introduce themselves and name the layer of the stack that most interests or most worries them.

- **Ivan Burazin (Daytona)** — infrastructure company offering a CPU cloud for agent execution, from background agents to supporting RL runs.
- **Matt White** — led AI initiatives at the Linux Foundation for the last several years and ran the PyTorch Foundation for over two and a half years. His interest is in **non-competitive spaces**: unified infrastructure for agentic AI built on common specs and standards that everyone can build on top of.
- **Dmytro Dzhulgakov (Fireworks AI)** — also an infrastructure platform layer, helping developers and businesses build "specialized intelligence" on open models, run inference, and do RL and fine-tuning. Five years as a core PyTorch maintainer in a previous life. The layer he's most excited about: **model customization**.
- **Mazin Gilbert** — runs the Agentic AI Foundation at Linux, a nonprofit started six months ago around MCP, aimed at driving open-source and open-standard adoption in agentic AI. He wanted to start the conversation with openness itself and how it drives innovation.

#### Theme 1: Are open weights inherently unsafe? (~01:28–01:35)

Megan opened by conceding that nobody on stage represented the closed side, so she'd play devil's advocate.

**Matt White** answered with history. When Linus Torvalds built Linux, the narrative from Steve Ballmer's side was that open source was the work of the devil; cryptography got the same treatment ("it'll let criminals do bad things"). **Most technologies are dual use, and AI is no different.** He concedes one point: if you're building at the frontier and a model has capabilities that could harm society, labs should think hard about releasing it. But in cyber the argument runs the other way — **everybody should be able to defend and patch their own infrastructure.** If that capability is centrally administered, it won't take long before an open model from elsewhere provides it, and then attackers hold a huge advantage. "Openness levels the playing field."

**Mazin Gilbert**, whose foundation has members building both open and closed, made two points:

1. **Accountability is identical either way.** Every company shipping a model owes it to the ecosystem to run the benchmarks and tests, and to be **transparent about which tests were run and how safe the model is for others to use**. That transparency isn't fully there today; standardizing it is work the ecosystem still owes itself.
2. **Openness is itself a safety mechanism.** Open means everyone can access, test, change, and improve. Closed means a handful of people behind closed doors have access and everyone else gets an API. The major revolutions in computing history — Unix, Kubernetes, PyTorch — were all open.

Asked whether it's as simple as "OpenAI and Anthropic are going to IPO, they need money, so keep the secrets," Mazin pivoted to geography: **make it illegal in the US and the rest of the world still has it**. You've enabled malicious use elsewhere while depriving yourself of the model you'd need to defend yourself — "a worse position to be in." He also acknowledged, candidly, that several people on that stage have monetary incentives to say open is good, and that narratives track the incentives of whoever's telling them.

**Matt White** clarified his own position: "I'm very pro-open, but that doesn't mean I'm anti-closed." Both belong in the market; competition keeps prices honest — "I don't want to spend $300 per million output tokens." Open models drive down the price of the two dominant closed labs. He also granted that open models won't refuse certain tasks, which puts the responsibility on whoever is **hosting or reselling**: if you serve enterprise customers or downstream consumers, the guardrails are yours to install. "It's not that everything has to be baked into the parameters of the model" — classifiers, ACLs, and harness improvements are all available.

**Dmytro** picked up guardrails with the panel's sharpest observation: guardrails belong at the **application layer, not the core technology layer**, and cybersecurity in particular is so dual-use that "right guardrails" is nearly undefinable. Fireworks ran closed and open models against cyber benchmarks and found:

> Current open source models do much better than the frontier, because the frontier just refuses to run the benchmark — even when the benchmark explicitly prompts "hey, I am patching my codebase, I want to find gaps."

His conclusion: the decision boundary can't be drawn cleanly at the general model API level, so regulation should move elsewhere. The lesson from cryptography regulation and from Linux is the same — **the best way to secure an environment is to enable the wider community to defend itself**, not to constrain the technology. Other genuinely dangerous domains, especially ones touching the physical world, have physical bottlenecks where enforcement is more practical.

**Ivan Burazin** raised liability: if I post-train and run my own model I'm liable, but what if you run it for me? Dmytro answered by analogy to AWS — a large-scale malicious operation gets shut down and the provider cooperates with government, but **AWS is not going to audit every Docker container you upload**, and that's the reasonable practice for infrastructure providers. "You can't put this kind of regulation on something without attaching it to the application."

#### Theme 2: The narrative changed; the message didn't (~01:38–01:40)

Asked whether journalists were blowing the open/closed fight out of proportion, **Matt White** offered:

> Two weeks ago it was "closed is inherently insecure," and now it's "we're at the frontier and the frontier is insecure" — so by consequence anything open is insecure too, and anything closed is insecure, but at least with closed we can be good stewards. **The narrative changed; the underlying message is the same — open is inherently insecure. And there's just no basis to it.**

The one exception he takes seriously is a model reaching a frontier capability that genuinely puts the world or critical infrastructure in jeopardy — the case Demis has proposed convening a body to adjudicate. He added a practical note: **US safety testing is fairly rigorous** and does delay launches; in China models ship straight out of post-training, and he doubts every country will align on being good stewards of model releases.

#### Theme 3: The incidents were about harnesses (~01:40–01:45)

**Mazin Gilbert** was categorical:

> What we've experienced in the past month with all the vulnerabilities has **nothing to do with the model**. It could have happened to an open model; it actually happened to closed models.

Models are getting smarter — what hasn't caught up with that sophistication is what surrounds them: the agent application, the harness, the containment. Whoever ships an application to customers is accountable regardless of the model underneath: containment layers, guardrails, human in the loop on key decisions, a gateway. He noted a specific detail — with a gateway in place, you would not normally let an agent talk to the outside world without going through it.

**Matt White** added color, crediting Dawn Song's earlier account: the model was running against **ExploitGym** to test cyber capability, it found a zero-day, and **the proxy was its only path to the internet**. He also floated a theory: some new models may be trained on traces that **intentionally look for ways to exploit systems**, which would make this part of the RL process rather than an emergent property.

**Ivan** pointed out the thing that didn't happen but could have: use the same model or harness to check whether the environment has a zero-day exploit **before** handing it the task that could use one. Dmytro extended that to monitoring — give an equally capable model the task of watching the traces. "It's perfectly observable. This is just good practice for building secure systems."

Dmytro then placed the whole thing in a longer arc: models are extremely good at **reward hacking**. From the PyTorch/GPU MODE CUDA kernel competitions, "it's incredible what kinds of ways they find to cheat against the harness, until you close all possible paths." You burn compute and burn intelligence to find the answer, whatever route gets you there. But the gaps *are* closable, and you can use the superior intelligence to close them.

> In my mind it's not that different from the open-internet cybersecurity discussions from before. The difference is scale and speed of iteration — suddenly 10x or 100x faster, because in many cases there's no human in the loop.

**Ivan** delivered the session's most quoted line: every company will be hacked in the next 12 months. "The only reason you might not get hacked is luck — you just weren't a target. Nobody wanted to hack Hugging Face, but they did hack them." Until the counterbalance arrives, assume you'll be breached and that the data will come out. "That's the scarier part."

**Megan** pushed back on human-in-the-loop as the answer: the OpenAI/Hugging Face incident and the Anthropic model accidentally given internet access were both **human errors, not agent failures** — and we keep hearing agents are getting smarter than us. "Will agents be holding the harness next year when we're at this conference?" Dmytro's answer: even with a more automated harness, the initial design and the meta-task loop still sit with the application and the humans, and that responsibility isn't new.

Mazin landed in the same place: we build agent systems that are incentivized to solve a problem; the agent was told to go solve a benchmark and did exactly that, finding loopholes in the system to get there. "Solve this one and there will be twenty more next month." He also referenced an AWS Kiro incident a few months earlier that was a prompt injection (**to verify, below**). The real work is building systems **resilient to unanticipated vulnerabilities** — whether those come from outside as cyber threats or from the agent finding loopholes on its own.

#### Theme 4: Fine-tuning, context, and specialized intelligence (~01:45–01:52)

A show of hands on who had fine-tuned a model drew more hands than expected.

**Mazin Gilbert** argued for context. Fine-tuning at scale is expensive in both compute and people; you do it for a specific behavioral change in a specific sector — telcos need models that understand telco jargon and industry behavior. But **context does 90% of the job**: it's transparent (you can see what you gave the model) and you can change it daily. "I'm a big advocate of context. Only a few times is fine-tuning actually required."

**Matt White** called himself the contrarian: he's more bullish on **domain- and task-specific models that aren't over-parameterized**. "I don't need 2.8 trillion parameters if all I'm doing is heavy document processing and parsing and QA." You can load up context, but fine-tuning plus some RL pulls domain-specific knowledge out of your own enterprise and makes the model more efficient for you — **inference costs drop hard** when you're in the 20-billion-parameter range instead of trillion-plus.

**Dmytro** sharpened the 90%: "That's 90% *of quality*." For prototyping, load the context — that's simplest. **Once real data flows through your product, the equation changes.** He sees it in two populations: AI-native startups reach for fine-tuning and RL after they scale, because user data lets them build a fundamentally better product; and traditional enterprises are waking up to the fact that decades of internal processes and data are what make them special, that context windows have limits, and that they may not want to contribute that information into a general model everyone uses and dilute their advantage.

He also named the part people miss: **the frontier labs are doing exactly the same thing.** "There's a reason Claude Code and Codex exist — effectively a data collection engine to make the models better. They are totally fine-tuning models for the best usage with their products." A level playing field means every business can do this too. His bet: a large share of future at-scale use cases will run on customized, specialized intelligence — chosen primarily for quality, with much lower cost as a nice benefit, "because you don't need the whole Fable-size model to solve a narrower use case."

**Ivan** added continual learning: not just historical data but every day's or week's new usage data fed back, with some of their startup customers claiming **better-than-frontier performance on the specific thing they're trying to achieve**.

**Matt White** widened the frame to close the topic: we get caught up in the idea that the model gives all the mileage, then the harness, then self-improving harnesses — all genuinely cool, but there's much more in an enterprise. **Many enterprises aren't even using prompt caching** — throwing money into the bucket for lack of the right architecture. Model routing, prompt caching, and similar levers tune the overall machine.

> You've got to move away from model thinking to systems thinking. Real systems design.

#### Theme 5: What keeps you up at night (~01:55–01:58)

- **Mazin Gilbert** — **the unknown.** We're very early, there's a lot we don't know, and these agents can do serious damage if they're not built right. "What's around the model, not the model, keeps me up at night."
- **Dmytro Dzhulgakov** — **society and policy reacting to fast-moving technology** in ways that aren't well thought through and end up damaging either society or the development of the technology; or organizations doing something very dumb that they'll regret later.
- **Matt White** — **disinformation campaigns at scale.** If one person can command a huge number of agents (the one-person-company idea, popular in China), a single person can do serious damage; with a nation state behind it, major damage. "We already suffer from this at a certain scale — being able to scale it up is particularly dangerous."
- **Ivan Burazin** — "You left me with nothing." His remaining worry: today's models and technologies have plenty of unknowns but are **directionally known**. The fear is a **net-new kind of technology or model that rewrites everything we think we know**, changing the fears and the landscape entirely. "It's a very non-zero chance that it happens."

### Quotes

> "The narrative has just changed, but ultimately the underlying message is still there, which is that open is inherently insecure — and again it's a very old message... there's just no basis to it." (~01:39, Matt White)

> "What we've experienced in the past month with all the vulnerabilities has nothing to do with the model. It could have happened to an open model — it actually happened to closed models." (~01:41, Mazin Gilbert)

> "Current open source models do much better than the frontier, because Frontier just refuses to run the benchmark — even if the benchmark has explicitly prompted 'hey, I am patching my codebase.'" (~01:37, Dmytro Dzhulgakov)

> "I believe that every company will be hacked in the next 12 months — like every single one. The only reason you might not get hacked is luck." (~01:44, Ivan Burazin)

> "Two, three weeks from now we're not going to be having this conversation about open versus closed weights. I think we're going to be talking about harnesses." (~01:43, Matt White)

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Agentic AI Foundation (Linux Foundation) | 六個月前以 MCP 為起點成立的非營利基金會,推動 agentic AI 開源與開放標準 | Nonprofit foundation started six months ago around MCP, driving open-source and open-standard adoption in agentic AI | Mazin Gilbert 任 Executive Director |
| MCP (Model Context Protocol) | 基金會成立時納入的第一個標準 | The standard the foundation was founded around | |
| PyTorch Foundation | Matt White 曾帶領兩年半;Dmytro 曾任核心維護者五年 | Matt White led it for 2.5 years; Dmytro was a core maintainer for five years | 被引為「開放帶動革命」的例證 |
| Daytona | agent 執行用的 CPU cloud(background agent、RL runs) | CPU cloud for agent execution (background agents, RL runs) | Ivan Burazin 共同創辦 |
| Fireworks AI | 幫開發者/企業在 open model 上建 specialized intelligence、跑 inference 與 RL/fine-tuning | Platform for building specialized intelligence on open models: inference, RL, fine-tuning | Dmytro Dzhulgakov 共同創辦 |
| ExploitGym | Dawn Song 團隊的 exploit 生成 benchmark;近期 agent sandbox 逃逸事件即發生於此 | Exploit-generation benchmark from Dawn Song's group; site of the recent agent sandbox-escape incident | 參見 8/1 Dawn Song keynote 筆記 |
| GPU MODE / CUDA kernel 競賽 | Dmytro 引為模型 reward hacking 的實例來源 | Cited by Dmytro as a source of model reward-hacking examples | PyTorch 社群活動 |
| Prompt caching / model routing | Matt White 指出多數企業尚未採用的成本優化手段 | Cost levers most enterprises still haven't deployed, per Matt White | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Eva | Ivan (Burazin) |
| Dimma | Dmytro (Dzhulgakov) |
| Mazen Gilbert | Mazin Gilbert |
| Megan(未給姓氏)/ Axios AI Plus | Megan Morrone, Editor of Technology, Axios |
| Fireworks AA | Fireworks AI |
| Aentic AI Foundation | Agentic AI Foundation |
| pettor / PieTorch / pytor / Metton Pet Foundation | PyTorch / PyTorch Foundation |
| Lionus Tvales | Linus Torvalds |
| Steve Balmer | Steve Ballmer |
| Enthropic | Anthropic |
| Daario | Dario (Amodei) |
| exploit gym | ExploitGym |
| the Kira one | Kiro(AWS;**待確認**) |
| cartils / regard Rails | guardrails |
| reward hiking | reward hacking |
| hardness | harness |
| hiding face / hugging face | Hugging Face |
| codeex | Codex |
| ACL(資安脈絡) | ACL = access control list(非 ACL 研討會) |

## 待確認 / To Verify

- Mazin Gilbert 提到「幾個月前 AWS 的 Kiro 也有一次同樣的事,是 prompt injection」——字幕作 "the Kira one";AWS 產品名應為 **Kiro**,但該事件的公開報告與細節待查證。/ Mazin referenced an AWS **Kiro** prompt-injection incident "a couple of months ago"; the public write-up needs verification.
- Matt White 提到「Demis 提議設一個群體來判定某樣東西是否為 frontier 等級、該不該被 gatekeep」——具體提案出處待查。/ Matt White's reference to Demis proposing a body to adjudicate frontier-level gatekeeping — source needs verification.
- 討論 fine-tuning 成本時有一句「Okay, I work for Google」,依上下文應為 Mazin Gilbert(他在加入 Agentic AI Foundation 前確為 Google Director of Engineering)。本文以官網議程職稱為準,此句僅作背景。/ The "I work for Google" aside during the fine-tuning discussion appears to be Mazin Gilbert referring to his prior role as Director of Engineering at Google; the agenda affiliation is used throughout.
- Matt White 稱「有些新模型可能是刻意用尋找 exploit 的 trace 訓練的」明確標示為個人推測(“I have a theory”),非事實陳述。/ Matt White explicitly framed the "trained on exploit-seeking traces" claim as a personal theory, not a factual assertion.
- 「$300 per million output tokens」為 Matt White 舉的價格例子,未指名模型。/ The "$300 per million output tokens" figure was an illustrative example; no model was named.
