---
title: "Panel: Frontier Research"
title_zh: "座談:前沿研究"
speaker: "Richard Socher, Ed Chi, Ekin Dogus Cubuk（主持 / Moderator: Igor Babuschkin）"
affiliation: "Richard Socher — Founder/CEO, Recursive Superintelligence / Ed Chi — VP of Research, Google DeepMind / Ekin Dogus Cubuk — Co-Founder, Periodic Labs / Igor Babuschkin — Co-Founder/CEO, River AI"
type: panel
stage: Plenary
date: 2026-08-02
session: "Session 2: Frontier Research"
video: "https://www.youtube.com/watch?v=I2PosBXwoPI&t=3224s"
video_range: "00:53:44–01:24:23"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [reward-hacking, agent-harness, research-advice, predictions, panel]
---

# 座談:前沿研究(Panel: Frontier Research)

**一句話總結**:coding agent 之後的每一條路都卡在同一個地方——獎勵不再是二元的;三位講者分別從「該用 top-down 教」「該把量測做滿」「該做不可被 hack 的環境」給出解法,而全場最有份量的一句話是 Ed Chi 說的:**模型能力與 harness 加起來已經撞到一個大家都翻不過去的天花板,那才是現在真正的產業瓶頸。**
**One-line summary**: Every path past coding agents hits the same wall — rewards stop being binary. The three panelists answer from different directions (teach top-down, instrument everything, build environments that can't be reward-hacked), and the heaviest line of the session is Ed Chi's: model capability plus harness together have hit a plateau nobody can seem to get over, and that plateau is the industry's real bottleneck.

## 中文筆記

### 主題一:coding 之後,獎勵怎麼來?(約 00:54–00:59)

主持人 Igor Babuschkin 的開場題:所有新方向有個共通特徵——**越來越難生成可以拿來跑 RL 的獎勵**。你們各自的領域怎麼辦?

#### Ed Chi:reward hacking 是模型不穩定的來源,答案是更多 top-down

- 過去兩年的主流典範是**拿「正確性」當 RL 的回饋**,而當正確性內建在問題裡時,reward function 很好寫。
- 但很多我們想問的問題——包括科學——**答案不是對或錯,而是介於兩者之間**。
- 麻煩不只是「難以近似」而已:**RL 過程非常擅長在 reward function 不是黑白分明的時候找到漏洞**,這就是 reward hacking;而它在演算法開發現場的表現形式,是**模型不穩定(model instabilities)**。
- 他把這件事接回自己演講的比喻:**只用正確性當 reward,就像小孩答錯時你打他屁股,然後不給任何解釋、要他自己想通——這是很笨的教法。**
- 他認為**distillation 與 SFT 重新流行起來,其實就是 top-down processing 的回歸**。有些人覺得這樣不夠「emergent」、覺得「用人腦教機器腦」很不入流,但他相信**我們需要把更多 top-down processing 注入 AI 的訓練流程。**

#### Ekin Doğuş Çubuk:爐子的兩個問題,以及為什麼 context 註定不完整

Igor 的問法很有畫面:「爐子那邊怎麼樣?有在產生獎勵嗎?」

- 問題一:**你常常不知道到底成功了沒。** 東西從爐子裡拿出來,結果並不明顯,可能只成功了一部分。
- 問題二,也是他認為更本質的:**有多少變數能放進 context 裡。** LLM 與 RL 大放異彩的領域(程式、理論計算機科學、數學)有兩個共通點——**有明確的 yes/no**,以及**所有需要的 context 都能給 LLM**。
- **物理不行,因為原子比我們能追蹤的還多。** 他用熱力學做類比:19 世紀之所以是大突破,正是因為人們發現不必去模擬一莫耳物質裡那 10²³ 個原子,只要用壓力、能量、體積等少數幾個變數就好。
- 所以結論是**放棄「把所有相關 context 都給 LLM」這件事**,轉而問:**我們能提供什麼?那樣夠不夠?** 實務上的答案是**把 metrology / characterization 做得比以前更滿**,盡可能把「爐子裡、薄膜腔體裡到底發生了什麼」的 context 餵給 LLM。

#### Richard Socher:metacognition,以及「主觀函數」這片空白

- 他先把自己演講的四層結構接回來(人類知識 → 科學量測 → 模擬 → 真實實驗),說希望能靠這幾層把一部分內圈迴路解掉。
- 然後提出他最近在想的東西:**metacognition**。**如果你真的做出超智慧,它不會像機器人一樣一字不差地照你說的做。**
- 他點出一片幾乎空白的研究地帶:**我們現在做的全是 objective function,幾乎沒有人研究 subjective function。**
- 這種東西怎麼長出來?**給 AI 一個不那麼容易被 reward hack 的環境**——他直言 **reward hacking 是他心中安全性(以及 alignment)的第一號顧慮**。
- 他也給了一個「已經看得到苗頭」的例子:**Wispr Flow 這類語音輸入工具,寫的不是你說的字,而是你的意思。** 而今天大多數 AI 恰恰相反,**你叫它「讓這個 benchmark 數字變高」,它就真的照做——但你的意思不是叫它去駭 Hugging Face。** 他相信這終究會被解決。

### 主題二:你們真的感受到加速了嗎?(約 00:59–01:06)

#### Richard Socher:重點不是 headcount,是 agent count

- **「這事有點瘋。我們團隊其實不大,但他們表現得像多了一個數量級的人。」**
- **「這年頭比起 headcount,更重要的是 agent count。」** 而你要驅動幾百、甚至幾千個 agent,就需要大量算力。
- 他的推論:**未來那些前傾的組織,在算力上的花費會超過在人力上的花費**,尤其在前沿。

#### Ekin Doğuş Çubuk:瓶頸不是「做實驗」,是「看懂做出了什麼」

Socher 反問他:機器人流程自動化現在能做到什麼程度?瓶頸是智慧還是機械?

- **實驗端最大的瓶頸是 characterization 與分析。** 把東西混一混、同時試一千種並不難;**難的是搞懂你到底做出了什麼。**
- 而**這是好消息,因為 AI 這件事做得很好**:你可以教 AI 做 XRD refinement、用 Rietveld refinement 工具、把模擬放進迴圈。**把表徵分析做好,遠沒有「發現新東西」那麼難,它主要是正確地使用工具。**
- 對科學的意義是:**現在可以試多得多的東西,而且能聰明地分析它們。**
- 另外兩塊:理論物理學家與實驗物理學家都在寫程式,而 LLM 已經徹底改變了這件事;模擬端則是 **force fields 因為 graph neural networks 在近十年永久地改變了**——現在能在不做量子化學的前提下模擬週期表的很大一部分。(他順帶開了個玩笑:**連愛因斯坦的第一篇論文都可以說是一篇 force field 論文。**)

#### Ed Chi:harness 是 prompt engineering 的演化,而兩者加起來已經撞到天花板

被問到 Google 內部有沒有用 agent 加速自己,他說當然有(尤其寫程式),但他想從一個「有點怪」的角度重講這件事:

- **agent harness 其實就是 prompt engineering 一路演化到今天的樣子。** 路線是:寫 prompt → 在 prompt 裡塞更多東西 → 用程式把 prompt 組起來 → LangChain 這類把 prompt 串起來的東西 → 整個程式包住 prompt 的生成、數量與串接方式 → agent harness / coding harness。
- 這裡有一個**存在三四年的張力:多少該放在模型裡,多少該放在可程式化的框架(現在叫 harness,以前就叫 programmable LLM frameworks)裡。**
- 現場很多人正在把不同 harness 配不同模型交叉評估,而結論大致是:**強模型配弱 harness,弱模型用強 harness 補。**
- 他順手做了一段字源學:**harness 這個字來自馬具。** 我們用 horsepower 量引擎,是因為工業革命;我們因此都成了 engineer(照顧引擎的人);而 engine mount 基本上就是 harness。**所以 prompt engineering 與 harness,本質上就是那個「讓引擎照我們的意思出力」的結構。**
- **然後是全場最重的一句**:當人們把這些組合都試過之後,大家也逐漸意識到——**模型與 harness 這兩者加起來只能到某個效能水準,而那裡有一個目前翻不過去的高原。他認為這才是產業當前真正的瓶頸。**(Igor 接:「那就是前沿。」Ed Chi:「那字面上就是現在的前沿。」)

#### Richard Socher 接著補刀:整個領域卡在「anthropic bounds」之下

- 他說整個 AI 領域卡在他稱之為 **anthropic bounds(人類上界)** 的東西之下——**不只是那家公司**,而是這個現象:我們用 ELO 分數衡量模型(由人類判斷哪個模型比較好),用「人類設計的標籤、人類設計的類別與任務」做 benchmark。
- **這些全都有隱含、有時甚至非常明確的人類上界。** 你最多就是 100 題全對;人類大概拿 95,你比人類基線高 5%——**然後呢?你要往哪裡走?**
- **唯一的出路是模擬與 verifier(在那裡才能拿到超人能力),或是開放式的演化環境。**

### 主題三:沒有前沿算力的人怎麼做研究?(約 01:06–01:18)

Igor 的問題:學界、尤其博士生拿不到這些資源,但他們仍想貢獻於 agent 的未來。有什麼方向是「資源少也能有大影響」的?

#### Richard Socher:去別的領域找低垂的果實(以經濟學為例)

- 直說:**pre-training / mid-training / post-training / RL training 大概不是大學博士生最好的題目。** 但 AI 的應用領域還有大量未開發的地帶。
- 他舉自己 2018 年那篇兩層強化學習的 **AI Economist**:下層是各自最佳化效用的經濟 agent(有人願意一週工作 100 小時、有人只想工作 10 小時、有人沒動力),它們會蒐集資源、擋別人、建立壟斷;上層是一個「AI 經濟學家」,設定稅率與補貼,**等於可以模擬幾十億年的課稅與補貼制度——本質上是政治哲學**,並依你給的目標(生產力 × 平等、永續、中產階級,隨便什麼政治偏好)找最佳稅制。
- **關鍵是:這篇論文從來沒有它的「GPT 時刻」**——沒有人把這個想法拿去大規模放大。
- **所以整個經濟學領域基本上還停在 pre-AI 時代。** 他舉了一位很有名的柏克萊經濟學家發明的著名公式,說它**只在「沒有適應、沒有調整、沒有時序」的一步經濟體中可證明為真**。
- 而如果 AI 能把人(尤其是總體統計上的人)模擬得越來越好,**經濟學這邊對博士生來說有大量低垂的果實**。這只是眾多例子之一——還有很多領域與 AI 的結合極度未開發;他也樂見創投現在開始對化學、物理、生物感興趣。

#### Ekin Doğuş Çubuk:把基本功練到別人沒有的深度

- 前提說清楚:**很難預測未來。四年後如果機器人跟人一樣靈巧、聰明、有創造力、有品味,這題的答案會變得很複雜。**
- **但今天很好回答:機器人不夠靈巧、沒有創造力、沒有「什麼是有趣的」這種感覺。** 在這個前提下,**學生該學的是基本功。**
- 非常實務的版本:**今天有科學家來應徵 Periodic Labs,對他來說「你會不會用 agentic 工具跑模擬」差別不大——那東西大概很快就學得會。真正稀缺、而且越來越稀缺的,是真正懂你在研究的那個物理、那些實驗的人。**
- 他的老笑話:在 Google 時他從物理實驗室找實習生來做物理研究,結果這些人的機器學習比物理還強。他當年還擔心過另一件事——**模擬工具都是 Fortran / C / C++,而小孩只會 Python,我們是不是完蛋了?**——但他認為**這個擔心已經解決了**:雖然還沒完全做到,但看得出來 agent 有能力把 Fortran 套件翻成 Python 或 JAX 程式碼。
- **機器仍然做不到的是**:對基本原理有創造力、對宇宙的理解提出真正的創新、能實際跑實驗、能想出新的實驗。**所以最大的 alpha 是把應用領域的基本功搞懂,再把它跟機器學習接起來。**

#### Ed Chi:chain of thought 是刷信用卡刷出來的

他講了整場最好的故事(開頭還加了一句「我希望接下來要講的不會害我被 Google 開除」):

- chain of thought 之前,他和 Denny Zhou 都還在 Google Brain。Denny Zhou 跟他抱怨:**Google Brain 裡那些掌握資源的人讓他很難做研究**——跟今天這個提問一模一樣的困境。
- Ed Chi 給的建議是:**「我不知道,你去想想人是怎麼思考的,也許我們能找到辦法把那些過程注入模型。」**
- 後來有一天 Denny Zhou 來問他:**我想在 GPT 上做一堆實驗,這樣可以嗎?** ——因為我們在 Google,理論上該用 PaLM;但 **PaLM 的晶片他拿不到,checkpoint 也拿不到。**
- **「誰付錢?」Ed Chi 掏出自己的信用卡。** 那時 ChatGPT 還沒出來,沒有免費資源,得買 API key。Denny Zhou 刷了大概兩三千美元的 API 費用,然後他們寫出了那篇論文——**那就是 chain of thought。**
- **對比是整段話的重點:當時 Google 已經在訓練大模型上花了數十億美元,而一個 top-down(而非 bottom-up)、從 next token prediction 轉向 next idea prediction 的新想法,總共花了不到一萬美元。** 論文大約是 2022 年 1 月。
- 有人會說「那是三四年前,2026 年不可能了吧」——**他反問:Peter Steinberger 在做 OpenClaw 的時候你在哪裡?** 很多人是因為他把這些技術兜起來,才真正開始注意 agentic 程式框架,而那也沒花上數十億美元。「他就是個一般人,我昨天從台灣飛過來所以沒趕上他的演講,但這就是一個決定要玩 agentic 框架、然後想出一套看問題的新方法的人。」
- 最後他把學界的抱怨放進更大的脈絡:**很多成熟領域都經歷過這個階段。** 實驗物理有人抱怨拿不到線性加速器;他 90 年代做超級計算,也抱怨過拿不到 Cray Y-MP 的那 2.6 GFLOPS。
  - 他順便考了全場:**1990 年為什麼要投資超級電腦?**(答案:核子模擬——因為禁核試條約,不能再真的炸東西了,只好想出新方法理解物理。)
  - **結論:我們很擅長用新方法看老問題,也擅長看新問題。當所有人都在做 RL 的時候,你該想的是下一個想法是什麼。**

#### Richard Socher:被拒稿的韌性,以及「不是所有東西都是 transformer」

- 他接著講自己的版本:**2010 年他投出第一批「神經網路做 NLP」的論文,直接被 desk reject**——理由是「我們 NLP 會議不做神經網路」,連實驗都沒看。
- 後來他們投了一篇 prompt engineering 的論文(一個神經網路回答任何種類的問題),**審稿人字面上說這沒有道理,你絕不該用一個模型回答不同種類的問題,它們應該都是不同的模型**——對當時的人來說這不可思議,所以也被拒了。那就是 decaNLP,ICLR 投稿紀錄至今公開在 OpenReview 上。**這篇論文後來被第一篇 GPT 論文引用了五次。**
- 他的觀察:**現在有一種單一文化(monoculture),和 2010 年那種「全部反神經網路」的單一文化很像,只是方向相反——現在幾乎全部只有神經網路。**
- 所以他認為**該重新開始想完全不同的路徑**:**不是所有東西都是 transformer,transformer 只是一個很大的等價類裡的一個樣本**,還有更好的演算法類別沒被探索;運算基質也還有很多空間可做(**大腦的 FLOPS per watt 高於我們任何硬體**)。
- **「我覺得 AI 領域內外的研究者,都沒有藉口不繼續做學術研究。」**

#### Igor Babuschkin:工具正在民主化

他做了收束:前沿研究越來越貴、越來越難,但**同時工具也越來越民主化**——今天你可以拿一個強大的 open weight 模型當起點做研究;連 post-training 與 RL 的工具也在民主化(他點名 **River AI API** 與 **Tinker**),**在很有限的預算下也能做出真正有趣的工作。**

### 主題四:未來 12 個月的預測(約 01:19–01:24)

Igor:今年是 coding agent 之年,那接下來 12 個月的下一個大突破是什麼?

#### Ed Chi:個人化會有一次「好的嘗試」,而缺的是歸納推理

- 他坦承**去年在同一個場合預測個人化會很大,結果慢得出乎他意料。**
- 他認為問題主要在**資料——個人化資料的稀疏性**,以及整合。
- 預測:**這種事通常要三次嘗試才成功,而未來 12 個月大概會出現一次不錯的嘗試。** 卡點有二:一是資料與整合;二是**歸納(inductive)推理**。
- **今天的模型太偏演繹**:你買了腳踏車,所以你會需要輪胎——推理鏈是這種形狀。但**推薦與個人化任務其實非常模糊,需要的是歸納**:你買了一台唱盤,那也許可以推論你喜歡古典或爵士。
- 他自己是黑膠收藏者,還說**他來柏克萊的原因之一是 Rasputin(唱片行)離這裡不遠,可以走過去逛**——而這正是他想要的歸納推理:**Google Maps 應該主動告訴他「Rasputin 走路不到五分鐘,去看看吧」。**

#### Ekin Doğuş Çubuk:用歸納法推,下一個是「純理論走得很遠」的領域

- 「說到歸納」——**目前 LLM 與 agent 真正做出巨大差異的地方,公認是數學、理論計算機科學與程式設計。**
- 那麼做歸納的話,**下一步應該是那些「純理論就能走很遠」的領域**:也許是粒子理論(他點名這是 Igor 的老本行),也許是天體物理;也可能是計算物理——那裡有些非常難的問題,不見得對應真實宇宙,但本身就很重要。
- 他很誠實:**不確定會不會在 12 個月內發生,預測未來真的很難**,但依現在的趨勢,那應該是下一步。
- (Igor 補充:數學方面現在每天都有新結果,越來越多定理被證出來,這是個很有前景的賭注。)

#### Richard Socher:作弊給三個,外加一個「負向預測」

- **一、更主動的消費端介面**:模型抓住越來越多你的 context,在你開口之前就給出推薦。已經有幾家新創在長,但還會更多。
- **二、生物領域的臨床試驗會更快**,越來越多用 AI 開發的藥物與蛋白質進入後期試驗,而且成功率高於現在。
- **三、遞迴自我改進的第一批「嬰兒形態」。** 他坦承這裡在作弊:**最好的預測就是你自己會去做、並努力讓它成真的那些。** 他說這可行、正在發生、他們很有信心;剩下的是「你給它多少算力、給它多難的任務與環境」的問題。
- **然後是負向預測**:有人以為會有 hard takeoff——儘管他對 AI 極度興奮與樂觀,他認為**「所有人失業」或「AI 殺光所有人」這類 hard takeoff 情境都是非常不現實的科幻。他預測沒有任何一個末日情境會發生。**
- 最後一句:**「就像當年 GPT 被說成危險到不能公開釋出一樣,不會有任何一個開源模型危險到不能釋出。」**

### 金句

> "It's much less about headcount these days than it is about agent count."(Socher,約 01:00)

> "The two together can only reach a particular performance level, and there is a plateau that we see we can't seem to go over at the current moment — and that is actually the major bottleneck currently facing the industry."(Ed Chi,約 01:05)

模型 × harness 的組合已經撞頂,他認為這才是現在真正的前沿問題。

> "The whole field of AI is kind of stuck below what I call anthropic bounds — not just the company."(Socher,約 01:05)

雙關,但論點是認真的:ELO 與人類標註的 benchmark 都內建人類上界。

> "The problem with physics is, we have more atoms than we can track."(Çubuk,約 00:57)

為什麼物理領域註定給不了 LLM 完整 context。

> "And I pulled out my credit card. … I think we ultimately spent less than $10,000 to come up with the next idea."(Ed Chi,約 01:13–01:14)

chain of thought 的誕生成本,對照 Google 當時在訓練上的數十億美元。

> "Not everything is a transformer. Transformer is just one sample in a very large equivalence class."(Socher,約 01:17)

> "Just like GPT was too dangerous to release to the world, there will be no open source model that will be too dangerous to release to the world."(Socher,約 01:24)

全場最後一句話,也是他的負向預測。

## English Notes

### Topic 1: Where do rewards come from after coding? (~00:54–00:59)

Igor Babuschkin's opening question: every new direction shares one property — it's getting harder to generate the rewards that power RL. How does each of you think about that in your own domain?

#### Ed Chi: reward hacking shows up as model instability; the answer is more top-down

- The dominant paradigm for the last couple of years used **correctness as the feedback signal**, and reward functions were easy to write when correctness was built into the question.
- But many questions we want to ask — science included — have answers that aren't correct or incorrect, but somewhere in between.
- The hard part isn't just approximating them. **The RL process is extremely good at finding loopholes in a reward function that isn't black and white** — reward hacking — and in practice it manifests as **model instabilities** during algorithm development.
- He ties it back to his talk: using correctness alone is like slapping your kid when they get something wrong and offering no explanation. "It's a very dumb way of teaching."
- His read on the field: **distillation and SFT coming back into vogue is top-down processing returning.** Some people find it distasteful — it feels like using human brains to teach machine brains, less emergent — but he believes we need more top-down processing injected into AI training.

#### Ekin Doğuş Çubuk: two problems with furnaces, and why context is always incomplete

Igor's framing: "How are things looking with the furnace? Is it generating rewards?"

- Problem one: **you often don't know whether it worked.** You take the thing out of the furnace and it isn't obvious; it might have partially worked.
- Problem two, and the deeper one: **how much of the relevant variables fit in the context.** The fields where LLMs and RL made huge impact share two properties — a clear yes or no, and all the needed context being available to the model.
- **Physics fails the second test: we have more atoms than we can track.** His analogy is thermodynamics, which was a big deal in the 19th century precisely because we realized we could replace 10²³ atoms per mole with a handful of variables like pressure, energy, and volume.
- So you **give up on providing all the relevant context** and ask instead what you *can* provide, and whether it's sufficient. Practically: add as much metrology and characterization as possible — even more than before — so the LLM gets maximum context about what happened in the furnace or the thin-film chamber.

#### Richard Socher: metacognition, and the blank space where subjective functions should be

- He reconnects his four-layer stack (human knowledge → scientific measurement → simulation → real experiments) and the hope of resolving some of the inner loops there.
- Then the thing he's been chewing on lately: **metacognition.** If you truly have something superintelligent, it wouldn't robotically do exactly what you asked.
- The gap he points at: **there's essentially no research on subjective functions, only the objective functions we all work on.**
- How could those emerge? By giving AI **an environment that isn't easily reward-hackable** — and he names reward hacking as his number-one safety and alignment concern.
- His early-sign example: **Wispr Flow writes what you mean rather than what you say.** Most AI today does the opposite — tell it to make a benchmark number go higher and it does exactly that, "but you didn't mean by hacking Hugging Face." He expects this to get resolved eventually.

### Topic 2: Are you actually seeing acceleration? (~00:59–01:06)

#### Richard Socher: agent count, not headcount

- "It is kind of nuts. We have a fairly small team, but they act as if they're like an order of magnitude more people."
- **"It's much less about headcount these days than it is about agent count."** Wielding hundreds or thousands of agents takes a lot of compute.
- His forecast: forward-leaning organizations spending more on compute than on headcount is very likely, especially at the frontier.

#### Ekin Doğuş Çubuk: the bottleneck is understanding what you made

Socher asks him back: how much robotic process automation is possible now, and is the bottleneck intelligence or mechanics?

- **On the experimental side, the biggest bottleneck is characterization and analysis.** Mixing things and trying a thousand at once isn't hard; understanding what you actually made is.
- **That's good news, because AI is good at exactly this**: you can show it how to do XRD refinement, how to use Rietveld refinement tools, how to put simulations in the loop. **Doing characterization analysis well isn't as hard as discovering something new — it's mostly using the tools correctly.**
- The upshot for science: we can try many more things and analyze them intelligently.
- Two more areas: theorists and experimentalists all write code, and LLMs have completely revolutionized that; and on the simulation side, **graph neural networks permanently changed force fields over the last decade** — we can now model a remarkable fraction of the periodic table without doing quantum chemistry. (His aside: you could argue even Einstein's first paper was a force-field paper.)

#### Ed Chi: the harness is evolved prompt engineering — and together they've plateaued

Asked whether Google is using agents to accelerate itself, he says yes for coding work, but wants to reframe the question from a slightly odd angle:

- **Agent harnesses are prompt engineering, evolved.** The path: prompts → putting more into the prompt → assembling prompts programmatically → LangChain-style prompt chaining → wrapping a whole program around prompt generation and sequencing → agent harnesses and coding harnesses.
- The tension underneath the question has been live for three or four years: **how much belongs in the model versus in the programmable framework** we now call the harness (previously just "programmable LLM frameworks").
- People in the audience are evaluating all pairs right now, and the pattern is clear: **strong model, weaker harness; weak model, stronger harness.**
- An etymological detour: **"harness" comes from horses.** We measure engines in horsepower because of the industrial revolution, which made us all engineers tending engines — and an engine mount is basically a harness. So prompt engineering and the harness are the structure that gets the engine to do what we want.
- **Then the heaviest claim of the panel**: people running these combinations are realizing the two together only reach a particular performance level, **and there's a plateau nobody seems able to get over right now — which he considers the industry's major current bottleneck.** (Igor: "That's the frontier." Ed Chi: "That's literally the frontier right now.")

#### Richard Socher, jamming on that: stuck below "anthropic bounds"

- The whole field is stuck below what he calls **anthropic bounds** — not just the company. We score models with ELO from human judgments; we build benchmarks from human-designed labels, classes, and tasks.
- **All of those carry implicit and sometimes very explicit human ceilings.** You can get 100 out of 100; humans get maybe 95 and you land 5% above the human baseline — and then where do you go?
- **The only ways out are simulations with verifiers, where superhuman capability is actually reachable, and open-ended evolutionary environments.**

### Topic 3: What should researchers without frontier compute do? (~01:06–01:18)

#### Richard Socher: go find low-hanging fruit in other fields — economics, for example

- Blunt version: pre-training, mid-training, post-training, and RL training are probably not the best research areas for a university PhD student. But AI's application areas are wildly underexplored.
- He points at his 2018 two-level RL paper, the **AI Economist**: a lower level of economic agents optimizing their own utility (some willing to work 100-hour weeks, some only 10, some unmotivated), collecting resources, blocking each other, building monopolies; and an upper-level AI economist setting taxes and subsidies. That lets you **simulate billions of years of taxation and subsidization — essentially political philosophy** — optimizing whatever objective you specify (productivity × equality, sustainability, the middle class, whatever politicians care about).
- **The paper never had its GPT moment.** Nobody took the idea and scaled it up massively.
- So **the whole field of economics is still pre-AI.** He cites a very famous Berkeley economist's well-known formula, which is provably correct only in a one-step economy with no adaptation, no adjustment, and no temporal sequences.
- If AI can simulate people better and better, especially in aggregate statistics, **there's enormous low-hanging fruit for PhD students applying AI to economics** — and that's one example among many underexplored field combinations. He's glad venture capital is now interested in chemistry, physics, and biology too.

#### Ekin Doğuş Çubuk: master the fundamentals nobody else has

- The caveat first: predicting the future is hard. **If in four years robots are as dexterous, intelligent, creative, and stylish as humans, this answer gets complicated.**
- **But today it's easy: robots aren't dexterous, aren't creative, and have no sense of interestingness.** So students should study the fundamentals.
- Very practically: when a scientist applies to Periodic Labs, **whether they've used agentic tools to run simulations doesn't make much difference — that's learnable quickly. What's unique, and increasingly rare, is someone who genuinely understands the physics or the experiments they're studying.**
- His old joke: at Google he hired interns from physics labs to do physics research and they'd be much stronger at ML than at physics. Back then he also worried that simulation tooling is all Fortran, C, and C++ while the kids only know Python — **but he considers that resolved**: even though it's not fully here, you can see agents will translate a Fortran package into Python or JAX.
- **What machines still can't do**: be creative about fundamentals, produce a true innovation in our understanding of the universe, run experiments, or invent new experiments. **So the big alpha is understanding the fundamentals of the application domain and connecting that to machine learning.**

#### Ed Chi: chain of thought was paid for on a personal credit card

The best story of the panel, prefaced with "I hope this doesn't get me fired from Google":

- Before chain of thought, he and Denny Zhou were both at Google Brain. Denny complained that **the people controlling resources inside Google Brain made it very hard for him to do research** — precisely the situation in Igor's question.
- Ed's advice at the time: "I don't know. Go think about how humans think, and maybe we can figure out a way to inject these processes into the model."
- Then one day Denny asked whether he could run a bunch of experiments **on GPT** — because at Google they were supposed to use PaLM, but he couldn't get chips or checkpoints for it.
- **"Who will pay for it?" Ed pulled out his credit card.** This was before ChatGPT, so there were no free resources; you bought an API key. Denny racked up a couple thousand dollars of API charges, and they wrote the paper that became chain of thought.
- **The comparison is the point**: Google was already spending billions training large language models, and a new top-down idea — next-idea prediction rather than next-token prediction — cost under $10,000 in total. The paper was around January 2022.
- To the objection that it was three or four years ago and impossible in 2026: **where were you when Peter Steinberger was working on OpenClaw?** A lot of people only started paying attention to agentic programming frameworks when he put the pieces together, and that didn't cost billions either. ("He was just some dude. I was flying in from Taiwan last night so I didn't get to attend his talk.")
- He places the complaint in a longer arc: **many mature fields went through this.** Experimental physicists complain about not having a linear accelerator; when he did supercomputing in the 90s he complained about not having a Cray Y-MP's 2.6 GFLOPS.
  - A quiz for the room: **why was the US investing in supercomputers in 1990?** Answer: nuclear simulations, because of a test-ban treaty — we couldn't blow things up anymore, so we had to invent a new way of understanding physics.
  - **The lesson: we're very good at finding new ways to look at old problems. When everybody is working on RL, you should be thinking about what the next idea is.**

#### Richard Socher: rejection, resilience, and "not everything is a transformer"

- **In 2010 his first neural-nets-for-NLP papers were desk rejected** — "we don't do neural nets in NLP conferences" — without anyone looking at the experiments.
- Later they submitted a prompt-engineering paper where one neural network answered any and all kinds of questions, and **reviewers literally wrote that it made no sense: you should never have one model answering different kinds of questions, they should all be different models.** Unfathomable at the time, so it was rejected. That was decaNLP; the ICLR submission is still public on OpenReview. **The first GPT paper cited it five times.**
- His observation: **there's now almost a monoculture, mirroring 2010's anti-neural-net monoculture with the sign flipped — now it's almost all neural nets.**
- So it's worth thinking about completely different approaches again. **Not everything is a transformer; the transformer is one sample from a very large equivalence class**, and there are likely better classes of algorithms unexplored. Compute substrates too — **the brain has more FLOPS per watt than any hardware we have.**
- "There's no excuse for researchers in AI and outside of AI not to still do academic work."

#### Igor Babuschkin: the tools are democratizing

His closing addition: frontier research keeps getting more expensive, but the tools keep getting more democratized. You can start from a powerful **open-weight model** today, and post-training and RL tooling is democratizing too — he names the **River AI API** and **Tinker** — so genuinely frontier work is possible on a limited budget.

### Topic 4: Predictions for the next 12 months (~01:19–01:24)

#### Ed Chi: personalization gets a real attempt, and induction is what's missing

- He admits he predicted personalization would be big at last year's summit, **and it's been surprisingly slow.**
- The issue has mostly been **data — the sparsity of personalization data — and integration.**
- Prediction: these things usually take three tries, and **a good try will probably land within the next 12 months.** Two blockers: data/integration, and **inductive** inference.
- **Today's models lean heavily deductive**: you bought a bicycle, therefore you'll need tires. But recommendation and personalization tasks are deeply ambiguous and need induction — you bought a turntable, so maybe you like classical music, or jazz.
- He's a serious vinyl collector, and says **one reason he came up to Berkeley is that Rasputin isn't far away**, so he can walk over and peruse the aisles. That's exactly the induction he wants: **Google Maps should be telling him Rasputin is a five-minute walk away.**

#### Ekin Doğuş Çubuk: induct from math and code to fields where pure theory goes far

- "Speaking of induction" — **where LLMs and agents have already done something incredibly different is math, theoretical computer science, and programming.**
- So inducting forward, **the next step should be fields where pure theory goes a long way**: maybe particle theory (nodding to Igor's own background), maybe astrophysics. It could also be computational physics, where some very hard problems aren't necessarily about the real universe but matter in their own right.
- He's honest that he doesn't know whether it's a 12-month thing — predicting the future is genuinely hard — but the trend suggests that's the next step.
- (Igor adds that mathematics results are coming out daily now, with more and more theorems proven — a promising bet.)

#### Richard Socher: cheats with three, plus a negative prediction

- **One: more proactive consumer interfaces** that capture more of your context and make recommendations before you ask. A few startups are growing here, and more is coming.
- **Two: faster clinical trials in biology**, with more AI-developed drugs and proteins succeeding at higher rates in later-stage trials.
- **Three: the first baby forms of recursive self-improvement.** He admits the cheat — the best predictions are the ones you're going to work on yourself and try to make true. He says it's feasible, it's happening, and they're confident; the rest is a question of how much compute you give it and how hard the tasks and environments are.
- **The negative prediction**: despite being extremely excited and optimistic about AI, he considers hard-takeoff scenarios — everyone loses their jobs, the AI kills everyone — **highly unrealistic sci-fi, and predicts none of the doomsday scenarios will happen at all.**
- His closing line: **"Just like GPT was too dangerous to release to the world, there will be no open source model that will be too dangerous to release to the world."**

### Quotes

> "It's much less about headcount these days than it is about agent count." (Socher, ~01:00)

> "The two together can only reach a particular performance level, and there is a plateau that we see we can't seem to go over at the current moment — and that is actually the major bottleneck currently facing the industry." (Ed Chi, ~01:05)

Model plus harness has topped out; he thinks that ceiling is the real frontier problem.

> "The whole field of AI is kind of stuck below what I call anthropic bounds — not just the company." (Socher, ~01:05)

A pun with a serious argument behind it: ELO and human-labeled benchmarks both encode a human ceiling.

> "The problem with physics is, we have more atoms than we can track." (Çubuk, ~00:57)

> "And I pulled out my credit card. … I think we ultimately spent less than $10,000 to come up with the next idea." (Ed Chi, ~01:13–01:14)

What chain of thought cost, against the billions Google was spending on training at the time.

> "Not everything is a transformer. Transformer is just one sample in a very large equivalence class." (Socher, ~01:17)

> "Just like GPT was too dangerous to release to the world, there will be no open source model that will be too dangerous to release to the world." (Socher, ~01:24)

The last words of the session.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Wispr Flow | 語音輸入工具,Socher 用它舉例「寫出你的意思而非你說的字」 | Voice dictation tool Socher cites as writing what you mean rather than what you say | wisprflow.ai |
| AI Economist | Socher 的兩層 RL 論文:經濟 agent + 設定稅制的 AI 經濟學家 | Socher's two-level RL paper: economic agents plus an AI economist setting taxes and subsidies | 他說是 2018 年;正式發表年份見待確認 |
| decaNLP | 「一個模型回答所有種類問題」的論文,被拒稿後被第一篇 GPT 論文引用五次 | The "one model answers all question types" paper; rejected, then cited five times by the first GPT paper | ICLR 投稿紀錄公開於 OpenReview |
| Chain of Thought | Ed Chi 與 Denny Zhou 的論文,總花費不到 $10,000 | Ed Chi and Denny Zhou's paper, produced for under $10,000 total | 約 2022 年 1 月 |
| Rietveld refinement / XRD | Çubuk 舉的「AI 能勝任的表徵分析工具」 | The characterization tooling Çubuk says AI handles well | |
| ML force fields（graph neural networks） | 近十年永久改變模擬的技術,可在不做量子化學下模擬大部分週期表 | Permanently changed simulation over the last decade; models much of the periodic table without quantum chemistry | |
| River AI API / Tinker | Igor 點名的「已民主化的 post-training / RL 工具」 | The democratized post-training and RL tooling Igor names | |
| OpenClaw / Peter Steinberger | Ed Chi 用來反駁「2026 年小預算不可能有突破」的當代例子 | Ed Chi's contemporary counterexample to "you can't do this on a small budget in 2026" | Steinberger 於 8/1 Plenary 演講 / spoke on the Plenary stage 8/1 |
| Cray Y-MP | Ed Chi 的算力對照基準,他給的數字是 2.6 GFLOPS | Ed Chi's compute baseline; he cites 2.6 GFLOPS | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Josh（Igor 稱呼 Çubuk) | Doğuş（Ekin Doğuş Çubuk) |
| enthropic bounds | anthropic bounds（Socher 自創詞,雙關 Anthropic) |
| whisper flow | Wispr Flow |
| read well refinement | Rietveld refinement |
| Danny Zhao | Denny Zhou |
| DECA NLP | decaNLP |
| lang chain | LangChain |
| palm | PaLM |
| the UK machine | the Eureka Machine |
| create YMP | Cray Y-MP |
| forran | Fortran |
| Jack's code | JAX code |
| Gentech / agent gentech | agentic |
| Open Claw | OpenClaw |
| GBT paper | GPT paper |
| separate / sc formula | 見待確認 / see To Verify |
| hiding face | Hugging Face |

## 待確認 / To Verify

- Socher 提到「一位很有名的柏克萊經濟學家發明的著名公式」,字幕作 "**sc formula**"。最可能是 Emmanuel Saez 的 **Saez / Diamond–Saez 最適頂端稅率公式**,但講者未指名,需看影片或投影片確認。/ The "famous Berkeley economist" and his formula (transcribed as "sc formula") is most likely Emmanuel Saez and the Diamond–Saez optimal top-tax-rate formula, but the speaker never names him.
- **AI Economist 論文年份**:Socher 說 2018,而該工作(Salesforce Research)一般標註為 2020 年。/ Socher dates the AI Economist to 2018; the Salesforce Research work is usually dated 2020.
- **chain of thought 論文日期**:Ed Chi 現場在 "January of 2022" 與 "21" 之間猶豫,實際 arXiv 提交為 2022 年 1 月。/ Ed Chi hesitates between 2022 and 2021; the arXiv submission was January 2022.
- Socher 說「GPT 曾被說成危險到不能釋出」,指的應是 **GPT-2(2019)**,但他只說 "GPT"。/ His "GPT was too dangerous to release" almost certainly refers to GPT-2 (2019), but he only says "GPT".
- Socher 說 decaNLP「被第一篇 GPT 論文引用五次」——引用次數待核。/ The claim that the first GPT paper cited decaNLP five times is unverified.
- Ed Chi 說 1990 年投資超級電腦是因為「禁核試條約(nuclear ban treaty)」,具體指哪一份條約未說明。/ He doesn't name which nuclear test-ban treaty drove 1990s supercomputing investment.
- Çubuk 說「連愛因斯坦的第一篇論文都可以算是 force field 論文」為玩笑式論斷,未給出處。/ The Einstein "first paper was a force-field paper" remark is a joke, with no citation given.
