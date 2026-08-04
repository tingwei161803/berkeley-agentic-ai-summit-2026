---
title: "The Future of Personalized Universal Agents"
title_zh: "個人化通用 Agent 的未來"
speaker: "Ed Chi"
affiliation: "VP of Research, Google DeepMind"
type: talk
stage: Plenary
date: 2026-08-02
session: "Session 2: Frontier Research"
video: "https://www.youtube.com/watch?v=I2PosBXwoPI&t=1299s"
video_range: "00:21:39–00:33:17"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [chain-of-thought, personalization, information-retrieval, reasoning, research-taste]
---

# 個人化通用 Agent 的未來(The Future of Personalized Universal Agents)

**一句話總結**:他用「每十年只有三個真正重要的想法」這個框架回顧三十年——索引、向量空間、深度學習;sequential transduction、chain of thought、post-training——並主張下一個十年的主軸是**從排序走向個人化推理**,而訓練方式必須從 bottom-up 的 RL 轉向 top-down 的「像教小孩一樣教機器」。
**One-line summary**: Framing three decades as "only three ideas per era that really mattered" — indexing, vector space models, deep learning; then sequential transduction, chain of thought, post-training — he argues the next decade moves from ranking to personalized reasoning, and that training must shift from bottom-up RL toward top-down teaching, the way we teach children.

## 中文筆記

### TL;DR

- **開場自白**:他自認是個「學得很慢的人」,也有 impostor syndrome;發表了 200 多篇論文,真正引以為傲的大概只有 10 篇。他要講的是**回頭看,每個時代真正重要的只有三個想法**。
- **第一個二十年(資訊檢索)**:索引(圖書館是人類第一個偉大發明)、向量空間模型、深度神經網路。**搜尋與推薦的本質是排序**;next token prediction 說穿了也是排序。
- **他親口承認的重大失誤**:1992 年他的博士指導教授 John Riedl 提議把向量空間模型從 document–term 矩陣搬到 user–item 矩陣——也就是推薦系統的誕生——**而他告訴老師這是個笨點子**。
- **2015–2025 三個想法**:sequential transduction(Transformer 論文摘要第一句的那個詞)、以 chain of thought 完成的 **next idea prediction**、post-training。他說**我們當初該把它們叫做 large reasoning models 而不是 large language models**。
- **他對現在的批評**:業界的 bottom-up processing(尤其是 RL)太多了。**教小孩答錯時不能只是打他,要給解釋**——chain of thought 正是這個想法,而蒸餾之所以可行也全靠這些 reasoning traces。
- **下一個十年**:從排序與推薦,走向真正能推理你的品味的個人助理。他自己在 Google 現在的主軸只有 reasoning 與 planning。

### 重點整理

#### 框架:每個時代只有三個想法(約 00:22–00:26)

他以「我學得很慢」開場,說身為科學家真正在乎的從來不是寫下一篇論文,而是下一個大想法是什麼——而他花了很久才看清哪些想法真的重要。

**第一個二十年,三個來自資訊檢索的想法:**

1. **索引(indexing)**——他認為人類第一個偉大發明是圖書館,而圖書館建立在索引之上。90 年代這件事變成用 MapReduce 蓋大型搜尋引擎。
2. **向量空間模型**——word2vec 幾年前拿下十年 test-of-time 獎,核心正是用神經網路在向量空間裡計算詞與詞的關係,讓機器真正理解語義。
3. **深度神經網路**(2010–2015)。

中間插進他的自白:**1992 年,他的博士指導教授 John Riedl 問「如果我們把向量空間模型套到 user–item 矩陣、而不是 document–term 矩陣呢?」——這就是推薦系統的誕生,而他當場說那是個笨點子。**

他把這三個想法收束成一句話:**有了超級電腦之後,我們把一件事做得好太多了,那就是排序。** 搜尋、推薦、整個網際網路生態,底層都是排序與 ranking;而**next token prediction 本質上也只是排序**——排出你下一個最可能說出口的字。

他也拿算力當對照:1992 年他當研究生時用的是超級電腦,而他口袋裡的手機現在有 1,690 GFLOPS,「幾乎是一千倍的算力……我們每個人口袋裡都揣著一千台超級電腦」。

#### 2015–2025:transduction、chain of thought、post-training(約 00:26–00:31)

他放出 Transformer 論文那張人人都看過的圖,問全場:**你們真的讀過那篇論文嗎?** 然後唸出摘要第一句——"The dominant sequence transduction models are based upon complex recurrent neural networks that include an encoder and decoder"——並坦承自己第一次讀完全不懂,現場也有至少一半的人舉手說到現在還不懂。

他花了一段解釋 **transduction**:那是「把一種能量波轉換成另一種能量波」。**你此刻就正在經歷 transduction**——他身上的麥克風把聲波轉成電波,場邊的喇叭把電波轉回聲波,而你的耳朵本身就是一個 transducer,鼓膜震動接上神經元把資訊送進大腦。所以 2014 年前後真正的大想法是:**把 sequential transduction 和神經網路結合起來**,而這不是憑空發生的,它建立在「我們的大腦怎麼運作」的認知理解之上。這個新的通用計算模型因此能吃多模態資料、能同時理解各種語言。

**第二個想法來自一個很基本的問題**:他和 Denny Zhou 在 Google Brain 問「我們能不能用教小孩的方式教機器?」——當時我們把一件事做錯了:**小孩答錯的時候,希望你不是直接打他;但我們當時就是這樣訓練機器的。** 於是他們想:也許該給機器一個「為什麼你錯了」的解釋。這就是 **chain of thought**,也就是 **top-down processing**。

他對現況的批評直接接在後面:**現在業界(尤其是 RL)的 bottom-up processing 太多了**,我們應該更像教小孩那樣給解釋。他還補了一個常被忽略的推論:**我們之所以能把一個模型蒸餾進另一個模型,靠的就是 chain of thought 產生的 reasoning traces。** 從 next token prediction 走到 **next idea prediction**,就是整個 reasoning 領域的起點。

**回頭看,我們當初該叫它們 large reasoning models,而不是 large language models**——因為我們真正在乎的是推理能力。

第三個想法是 **post-training**(他把細節留給同場其他講者)。

#### 2025–2035:從排序走向個人化推理(約 00:31–00:33)

他先把算力那條線接回來:一顆最新世代的 TPU 晶片,算力已經是他開場展示的那台 Cray Y-MP 的天文數字倍(具體倍率與世代見「待確認」)——「這個放口袋裡是真的會燒穿的」。

然後放了一段 demo 影片:使用者拿著朋友送的一疊書,問助理「你會怎麼形容她的閱讀品味?」助理答出「歷史、傳記,可能還帶點政治或社會評論」;再問「哪一本她會最喜歡?」助理挑了 *Half of a Yellow Sun*,理由是它在歷史脈絡裡探討複雜的社會與政治議題,呼應她對「能看見重要時代切面」的敘事的興趣。

他的評語就是那句:**這已經不只是排序與 ranking 了,對吧?個人助理正在往這個方向走。**

最後他指著去年在同一個舞台放過的那張投影片說:**當時就已經有這些想法了,現在人人都在談 agent。下一個十年的想法其實已經在發生**——Richard 剛剛談的自我改進、其他講者談的多模態、工具使用、多步複雜推理。而他自己現在在 Google 的主要工作就只聚焦在 **reasoning 與 planning**,因為未來在那裡。

### 金句

> "In 1992, my PhD adviser John Riedl came to me and said, 'What if we use those vector space models and applied them to user–item matrices instead of document–term matrices?' … and I told him it was a dumb idea."(約 00:24)

推薦系統誕生的那一刻,他投了反對票。

> "What is sequential transduction? What the f does that even mean?"(約 00:27)

他問全場有沒有真的讀過 Transformer 論文,一半的人到現在還不懂那句摘要。

> "When you teach your kids, I hope every time they get it wrong, you don't just hit them. But that was the way that we were teaching our machines."(約 00:29)

chain of thought 的出發點。

> "In retrospect I wish we had not called it large language models; rather we should have been calling them large reasoning models."(約 00:30)

> "Now that is not just sorting and ranking anymore, is it? That is where personal assistance is going."(約 00:32)

三十年的排序史,在這支 demo 影片這裡轉彎。

## English Notes

### TL;DR

- **He opens by calling himself a slow learner** with impostor syndrome: 200+ papers published, maybe 10 he's proud of. The talk is a retrospective on the handful of ideas per era that actually mattered.
- **First two decades (information retrieval)**: indexing (the library as humanity's first great invention), vector space models, deep neural networks. Search and recommendation are fundamentally **sorting** — and so is next-token prediction.
- **His confession**: in 1992 his PhD advisor John Riedl proposed applying vector space models to user–item matrices instead of document–term matrices — the birth of recommender systems — and Ed told him it was a dumb idea.
- **2015–2025, three ideas**: sequential transduction (the phrase opening the Transformer abstract), **next-idea prediction** via chain of thought, and post-training. In hindsight, he says, we should have called them large *reasoning* models.
- **His critique of the field**: too much bottom-up processing, especially RL. You don't just hit a kid when they get it wrong — you explain. Chain of thought *is* that explanation, and distillation only works because of the reasoning traces it produces.
- **Next decade**: from ranking to assistants that actually reason about your taste. His own work at Google is now narrowed to reasoning and planning.

### Key Points

#### The frame: three ideas per era (~00:22–00:26)

As a scientist, he says, what he cared about was never the next paper but the next big idea — and it took him a long time to see which ideas mattered.

**Three ideas from information retrieval, spanning his first two decades:**

1. **Indexing.** The library is, in his opinion, humankind's first great invention, and it is built on indexing. In the 90s that became MapReduce and web-scale search engines.
2. **Vector space models.** word2vec took the ten-year test-of-time award a few years ago; its core idea was using neural networks to compute relationships between words so machines could grasp semantics.
3. **Deep neural networks** (2010–2015).

Wedged in between is the confession about John Riedl and user–item matrices.

The unifying claim: once supercomputers arrived, the one thing we got dramatically better at was **sorting**. Search, recommendation, the whole internet ecosystem run on sorting and ranking — and next-token prediction is sorting too, ranking the most likely next word.

He anchors the compute arc with a comparison: the supercomputer he used as a 1992 grad student versus the 1,690 GFLOPS phone in his pocket — nearly a thousand times more compute. "We're all walking around with like a thousand supercomputers in our pocket."

#### 2015–2025: transduction, chain of thought, post-training (~00:26–00:31)

He puts up the Transformer architecture figure everyone has seen and asks: **have you actually read the paper?** Then reads the first sentence of the abstract aloud, admits he had no idea what it meant the first time, and gets at least half the room to raise their hands admitting the same.

His unpacking of **transduction**: the conversion of one energy wave into another. You are experiencing it right now — his microphone turns sound into electrical waves, the hall's speakers turn them back into sound, and your ear is itself a transducer whose membrane vibrates into neurons that carry information into your brain. So the big idea around 2014 was marrying sequential transduction with neural networks — and crucially, it wasn't invented in the ether, it rested on a cognitive understanding of how our brains communicate. The resulting universal computational model can absorb multimodal data and handle many languages at once.

**The second idea came from a plain question** he and Denny Zhou asked at Google Brain: can we teach machines the way we teach our children? One thing was clearly wrong. When your kid gets something wrong, you (hopefully) don't just hit them — but that's exactly how we were training machines. Give them an explanation instead. That became **chain of thought**, i.e. **top-down processing**.

His critique follows immediately: the industry does far too much bottom-up processing, particularly with RL. And a consequence people underrate — **distillation works because of the chain-of-thought reasoning traces**. Moving from next-token prediction to **next-idea prediction** is what started the whole reasoning field.

Hence: in retrospect we should have said large *reasoning* models, because reasoning is what we actually care about.

Third idea: **post-training**, which he leaves to the other speakers on the stage.

#### 2025–2035: from ranking to personalized reasoning (~00:31–00:33)

Picking the compute thread back up: a single latest-generation TPU chip now dwarfs the Cray Y-MP from the start of his talk by an astronomical factor (exact multiplier and chip generation flagged under To Verify) — "that's definitely going to burn a hole in your pocket."

Then a short demo video. A user holds up a stack of books a friend has been reading and asks how to describe her taste; the assistant answers "a mix of history, biography, and perhaps a touch of political or social commentary." Asked which one she'd like most, it picks *Half of a Yellow Sun* for its exploration of complex social and political issues in a historical setting, aligning with her interest in narratives about significant periods.

His line: that is not just sorting and ranking anymore — that's where personal assistants are going.

He closes on the slide he showed on this same stage a year ago: the ideas were already there, and now everybody is talking about agents. The next decade's ideas are already happening — self-improvement (as Richard just covered), multimodality, tool use, multi-step complex reasoning. His own work at Google is now focused purely on **reasoning and planning**, because that's where the future is.

### Quotes

> "In 1992, my PhD adviser John Riedl came to me and said, 'What if we use those vector space models and applied them to user–item matrices instead of document–term matrices?' … and I told him it was a dumb idea." (~00:24)

He voted against recommender systems at the moment of their birth.

> "What is sequential transduction? What the f does that even mean?" (~00:27)

> "When you teach your kids, I hope every time they get it wrong, you don't just hit them. But that was the way that we were teaching our machines." (~00:29)

The origin of chain of thought, in one image.

> "In retrospect I wish we had not called it large language models; rather we should have been calling them large reasoning models." (~00:30)

> "Now that is not just sorting and ranking anymore, is it? That is where personal assistance is going." (~00:32)

Thirty years of sorting, turning a corner on one demo video.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| word2vec | 向量空間模型的代表作,幾年前獲十年 test-of-time 獎 | Vector space model landmark; won a ten-year test-of-time award | |
| Chain of Thought prompting | 他與 Denny Zhou 等人的工作,把 next token prediction 推向 next idea prediction | His work with Denny Zhou and others; moved the field from next-token to next-idea prediction | 起源故事見同場 panel(約 01:12–01:14)/ origin story told in the panel (~01:12–01:14) |
| "Attention Is All You Need" | 他現場逐句拆解摘要第一句的 "sequence transduction" | He reads and unpacks "sequence transduction" from the abstract's first sentence | |
| Cray Y-MP | 他 1992 年當研究生時用的超級電腦,全場算力對照的基準 | The supercomputer he used as a 1992 grad student; the baseline for his compute comparisons | panel 中他給的數字是 2.6 GFLOPS / he cites 2.6 GFLOPS in the panel |
| *Half of a Yellow Sun* | demo 影片中助理推薦的書 | The book the assistant recommends in the demo video | Chimamanda Ngozi Adichie 著 |
| LaMDA / Bard / Gemini / Project Astra | 主持人介紹中提到的他在 Google 參與的產品線 | Product lines he worked on at Google, per the moderator's intro | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Etchie / ad | Ed Chi |
| John Rele | John Riedl |
| Danny Zhao | Denny Zhou |
| wordtovec / word tovec | word2vec |
| Lambda（模型) | LaMDA |
| Xerox Spark | Xerox PARC |
| sik chi academy | SIGCHI Academy |
| C create Cray YMP / create YMP | Cray Y-MP |
| train of thought | chain of thought |
| 20110 to 2015 | 2010 to 2015 |
| imposttor syndrome | impostor syndrome |
| document turn matrices | document–term matrices |
| mindbrain（耳朵裡的) | membrane |

## 待確認 / To Verify

- 字幕作 "a single **V8** TPU chip now is **4.7 times** more computation than the Cray Y-MP"。兩處都可疑:Google 第八代 TPU(8t / 8i)在 2026 Cloud Next 只是預覽、目標 2027 量產,現役旗艦是第七代 Ironwood;而「4.7 倍」與他自己給的 Cray Y-MP 2.6 GFLOPS 對照明顯不合(數量級應為百萬倍)。需看投影片確認世代與倍率。/ The caption says "a single V8 TPU chip now is 4.7 times more computation than the Cray Y-MP." Both parts look wrong: Google's 8th-gen TPUs (8t/8i) were only previewed at Cloud Next 2026 for a 2027 launch, and 4.7× is inconsistent with his own 2.6 GFLOPS figure for the Cray Y-MP (the real ratio is on the order of millions). Check the slide.
- demo 影片是哪一個產品(Project Astra?Gemini app?)講者未指名。/ The demo video is not named on stage — Project Astra? the Gemini app?
- 他說 word2vec 拿的是「十年 test of time 獎」,未指明是哪個會議(NeurIPS)。/ He doesn't name the venue for the word2vec test-of-time award.
- 他提到台下的 "Vincent"(2015–2025 那三個想法的見證人),身分未明。/ The "Vincent" he acknowledges in the audience is unidentified.
- 他說 1992 年 John Riedl 提出 user–item 矩陣的想法;推薦系統文獻通常把 GroupLens 定在 1994 年,年份待對。/ He dates the user–item matrix conversation to 1992; the recommender-systems literature usually dates GroupLens to 1994.
