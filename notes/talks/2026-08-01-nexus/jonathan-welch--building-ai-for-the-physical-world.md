---
title: "Building AI for the Physical World: Lessons from Accelerating Discovery for Chemists Across the Globe"
title_zh: "為物理世界打造 AI:替全球化學家加速發現的實戰教訓"
speaker: "Jonathan Welch"
affiliation: "Head of AI, Albert Invent"
type: talk
stage: Nexus
date: 2026-08-01
session: "Session 1: AI for Science"
video: "https://www.youtube.com/watch?v=LB7IkZhEYic&t=4809s"
video_range: "01:20:09–01:26:03"
transcript: "tmp/[English (auto-generated)] Nexus Stage - August 1st - Morning Session [DownSub.com].srt"
status: draft
tags: [ai-for-science, industrial-chemistry, retrieval, enterprise-ai, trust]
---

# 為物理世界打造 AI:替全球化學家加速發現的實戰教訓(Building AI for the Physical World: Lessons from Accelerating Discovery for Chemists Across the Globe)

**一句話總結**:在工業化學裡,agentic co-scientist 最重要的功能不是準確率而是**信任**;而信任不是被複雜推理的大失敗打垮的,是被「檢索排到第 300 名以後」這種安靜的領域錯位一點一點磨掉的。
**One-line summary**: In industrial chemistry the most important feature of an agentic co-scientist isn't accuracy, it's trust — and trust doesn't die in a dramatic reasoning failure, it dies quietly when a retrieval model ranks the right passage 300th because it has no discrimination inside the domain.

## 中文筆記

### TL;DR

- **信任才是最重要的 feature**,不是抽象的準確率,也不是很厲害但孤立的成果。信任的定義是**與使用者的領域對齊**;一旦系統開始「自信地講錯」,使用者失去的不只是對答案的信任,還有對**建這套系統的你**的信任——兩者都很難贏回來。
- **配方化學是 agentic co-scientist 最難進的領域**:它是工業化學裡最大的一塊(2,000 億美元年 R&D 支出中超過一半流向配方產品),但決定成敗的知識**幾乎都是隱性的、未發表的、專有的**,極少浮上公開領域。
- **信任崩壞的方式很安靜**:一個真實的配方化學家專利查詢,兩段看起來都能回答的段落,**領先的 embedding 模型把正確那段排在第 300 名以後**,而且兩段的相似度分數差距**幾乎是零**——代表模型在配方化學裡**完全沒有領域內鑑別力**。對 agentic co-scientist 而言,這已經不是「檢索差」,而是變成一個它會很有信心地拿去推理的**錯誤信念**。
- **有效的解法只有一個**:任務專屬、以本體論(ontology)結構化的對比式訓練——教模型這個領域的形狀,而不是餵它更多化學文字。commercial API 在他們的 benchmark 上基本得零分,open-weight 模型好一些,但**continued pre-training 沒有用**。

### 重點整理

#### 配方化學:最大、也最難被 AI 進入的領域(約 01:20–01:22)

Albert 是一個 **AI 原生的作業系統**,設計成一個讓 **AI agent 與化學家一起工作的協作介面**,目的是加速發現、讓新材料更快上市;客戶是世界上最大的一批化學公司,它是他們的 R&D 平台。

在企業規模部署 AI 的第一個教訓是:**實驗檯前的化學家有多懷疑**。因為他們在發明真正被使用的東西,期待很高,而且**連簡單的錯誤都不太原諒**,更別說昂貴的複雜錯誤。

他定義的「工業化學」就是**你身邊這個房間的化學**:牆上的塗料與塗層、手機上的黏著劑、眼鏡上的鍍膜、你今天早上用過的個人保養品。這些全都是**配方產品(formulated products)**,而**配方科學是工業化學裡最大的領域**——每年 2,000 億美元的 R&D 支出裡,**超過一半**流向這類配方產品。

而正是這個領域,**對 agentic co-scientist 來說最難進入**:因為決定成敗的知識**今天大多以隱性(tacit)、未發表、專有的形式存在**,極少、甚至從不會浮上公開領域。

在這個領域裡,Albert 的 co-scientist 協助合作夥伴發明**超過十億人每天依賴的產品**。這是這些化學家做每一個決定時扛的重量,也正是為什麼他們學到:**信任高於一切,才是最重要的 feature**。不是抽象的準確率,不是「很厲害但常常孤立」的能力與結果,而是**與他們的領域對齊**。他承認這聽起來理所當然,但當你在沒有明確問題選擇準則的情況下猛蓋能力時,非常容易忘記。

因為當你的工作是維護一個觸及十億人的材料市場區隔,你的期待自然很高。而**一旦使用者發現系統開始「自信地講錯」,他失去的不只是對那個答案的信任,而是開始失去對你——那個開發 agentic 系統的人——的信任**。要贏回其中任何一個,都是很陡的坡。

#### 信任是怎麼安靜崩掉的:一個檢索的例子(約 01:22–01:26)

他強調:**信任並不是被某次複雜推理的戲劇性失敗打垮的,而是被某種簡單而安靜的東西磨掉的——通常就只是與領域的基本錯位。**

他的例子是一個**真實的配方化學家查詢**:要找一份專利給 agent 拿去推理。候選有兩段文字,兩段看起來都像能回答問題,但只有一段是對的。結果:

- **一個領先的 embedding 模型把正確答案排在第 300 名以後**,遠遠超出正式環境裡 reranking 系統會去檢查的範圍。
- 更令人意外的是,這兩段文字對該查詢的**相似度分數差距幾乎是零**。

這代表模型在**配方化學這個領域裡完全沒有領域內鑑別力(within-domain discrimination)**。而對一個 agentic co-scientist 來說,這已經不只是一次糟糕的檢索——**它會變成一個被系統很有信心地拿去往下推理的錯誤信念**。

解法是往表層底下挖,看看這兩段到底差在哪。表面上它們共享相似的**材料本體論(material ontology)**、相似的**功能**與**最終應用領域**。但如果改用**本體論訊號**去浮現「一個配方化學家真正會用來分辨這兩者的東西」,就能得到領域對齊,並由此建出**訓練領域內鑑別力的強訊號**。

為了知道工業化學裡這些「領域內鑑別」到底住在哪,他們開始**建 benchmark**。在同一份公開語料上比較所有模型,結果是:

- **商用 API 基本上得零分**——完全沒有領域內鑑別力。
- **open-weight 模型好一些**,但**即使做 continued pre-training 也沒真的解決問題**。
- 真正有效的是**任務專屬、以本體論結構化的對比式訓練(ontologically structured contrastive training)**——教模型這個領域**實際的形狀**,而不是給它看更多化學文字;也就是與**使用者實際的思考方式**對齊。這讓他們從一個在正式環境裡「近乎零分」的模型,變成在企業規模上真正有意義的東西。

他的推論:**在不確定性很高的推理與發現場景裡,系統的好壞上限就是它與實際問題空間的對齊程度**——所以可規模化的 AI 解法會愈來愈**領域原生(domain-native)**。當天好幾場演講其實都指向同一件事:進到更專門的領域,就要建真正理解那個領域的 AI。

**最後他點出第二種、更長線也更重要的信任**:不是對答案的信任,而是**你為真實使用者打造 agentic 系統時所建立的信任**。理由是——**科學的公開紀錄是有倖存者偏誤的**,我們容易漏掉水面下的東西,而那些知識**今天大量活在企業 R&D 內部**。所以持續問自己「我們為終端使用者建的 AI,做了什麼來建立信任?」,正是取得那批資料的方式。

### 金句

> "…building AI for scientific discovery has taught us that above all else, trust is actually the most important feature."(約 01:22:14)

不是準確率,不是能力——是信任。

> "…once you reach a system and you begin to see that it's beginning to reason in a confidently wrong way, you don't just lose trust in the answer. You begin to lose trust in you, the one who's actually developing the agentic system."(約 01:22:46)

「自信地講錯」的代價會外溢到建造者身上。

> "Trust doesn't break down through some dramatic failure of complex reasoning. It breaks down through something simple and quiet."(約 01:23)

崩壞從來不是爆炸,是慢性錯位。

## English Notes

### TL;DR

- **Trust is the most important feature** — not accuracy in the abstract, and not impressive but isolated capability. Trust means alignment with the user's domain. Once a system starts reasoning in a confidently wrong way, users don't just lose trust in the answer; they lose trust in **you**, the person building the system, and winning either back is a steep climb.
- **Formulation chemistry is the hardest domain for agentic co-scientists to enter**: it's the largest domain in industrial chemistry (more than half of a $200B annual R&D spend goes to formulated products), yet the knowledge that determines success is overwhelmingly **tacit, unpublished, and proprietary**, seldom if ever surfaced publicly.
- **Trust breaks quietly**: on a real formulation chemist's patent query with two plausible-looking passages, **a leading embedding model ranked the correct one beyond position 300**, and the similarity-score gap between the two was **essentially zero** — the model has **no within-domain discrimination** in formulation chemistry. For an agentic co-scientist that isn't just bad retrieval; it becomes **a false belief the system reasons from confidently**.
- **Only one thing worked**: task-specific, ontologically structured contrastive training — teaching the model the shape of the domain rather than feeding it more chemistry text. Commercial APIs score effectively zero on their benchmark; open-weight models do better, but **continued pre-training doesn't fix it**.

### Key Points

#### Formulation chemistry: the biggest domain and the hardest to enter (~01:20–01:22)

Albert is an **AI-native operating system** built as a **collaborative surface where AI agents and chemists work together** to accelerate discovery and bring new materials to market faster. It's the R&D platform for some of the largest chemical companies in the world.

The first lesson from deploying AI at enterprise scale: **how skeptical bench chemists actually are**. They're inventing things people rely on, they expect a great deal, and they **don't easily forgive even simple mistakes** — let alone costly complex ones.

Industrial chemistry, as he defines it, is **the chemistry of the room around you**: the paints and coatings on the walls, the adhesives in your phone, the coatings on your glasses, the personal care products you used this morning. All of these are **formulated products**, and **formulation science is the largest domain in industrial chemistry** — more than half of a **$200 billion annual R&D spend** goes toward them.

And this is precisely the domain that's **least accessible to agentic co-scientists**, because most of the knowledge determining success today lives in **tacit, unpublished, proprietary form** and is seldom if ever surfaced publicly.

Within it, Albert's co-scientists help partners invent products that **over a billion people depend on every day**. That's the weight these chemists carry into every decision, and it's exactly why building AI for scientific discovery taught them that **above all else, trust is the most important feature** — not accuracy in the abstract, not capability or amazing but often isolated results, but **alignment with their domain**. He conceded this sounds obvious, and noted how easy it is to lose track of when you're building capabilities without clear problem-selection criteria.

Because when your job is maintaining a materials market segment that reaches a billion people's hands, your expectations are high. And **once a user sees a system beginning to reason in a confidently wrong way, they don't just lose trust in the answer — they start losing trust in you, the one developing the agentic system**. Winning either back is a very steep climb.

#### How trust actually breaks: one retrieval example (~01:22–01:26)

His emphasis: **trust doesn't break through a dramatic failure of complex reasoning. It breaks through something simple and quiet — usually just basic misalignment with the domain.**

The example is a **real query from a formulation chemist** looking for a patent for the agent to reason with. Two candidate passages, both of which look like they could answer it; one is correct. What happened:

- **A leading embedding model ranked the correct answer beyond the 300th position** — well outside what typical reranking systems check in production.
- More surprising still, the **difference in similarity score between the two passages was essentially zero**.

Which means the model has **no within-domain discrimination for formulation chemistry**. And for an agentic co-scientist, this isn't just a bad retrieval — **it becomes a false belief the system then reasons from very confidently**.

The fix is to dig beneath the surface and ask what actually makes the passages different. On the surface they share similar **material ontologies**, similar **function**, and similar **final application domain**. But using an **ontological signal** to surface what a formulation chemist would actually use to tell them apart yields domain alignment — and from there, powerful training signals for within-domain discrimination.

To find out where these within-domain distinctions live in industrial chemistry, they **built benchmarks**. Comparing every model on the same public corpus:

- **Commercial APIs score effectively zero** — no within-domain discrimination at all.
- **Open-weight models do better**, but **continued pre-training on them doesn't really work either**.
- What does work is **task-specific, ontologically structured contrastive training** — teaching the model **the actual shape of the domain's chemistry** rather than showing it more chemistry text, i.e. aligning with **how the actual users think**. That took them from a near-zero model in production to something meaningful at enterprise scale.

His conclusion: **reasoning and discovery under high uncertainty are only as good as the alignment between the system and the actual problem space it's applied to** — which is why he expects scalable AI solutions to become far more **domain-native**. Several talks that day pointed the same way: as you move into more specialized domains, you have to build AI that genuinely understands them.

**He closed on a second, longer-term and more important kind of trust**: not trust in the answer, but the trust you build when constructing agentic systems for real users. The reason is that **the public record of science is survivorship-biased** — we systematically miss what's beneath the surface — and a great deal of that missing knowledge **lives inside enterprise R&D today**. Continually asking "what are we doing to build trust in the AI we're building for end users?" is how you get access to that data.

### Quotes

> "…building AI for scientific discovery has taught us that above all else, trust is actually the most important feature." (~01:22:14)

Not accuracy, not capability — trust.

> "…once you reach a system and you begin to see that it's beginning to reason in a confidently wrong way, you don't just lose trust in the answer. You begin to lose trust in you, the one who's actually developing the agentic system." (~01:22:46)

The cost of confidently wrong output spills onto the builder.

> "Trust doesn't break down through some dramatic failure of complex reasoning. It breaks down through something simple and quiet." (~01:23)

It's never an explosion — it's chronic misalignment.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Albert(Albert Invent) | AI 原生作業系統,作為 AI agent 與化學家協作的介面;大型化學公司的 R&D 平台 | AI-native OS built as a collaborative surface for AI agents and chemists; R&D platform for large chemical companies | 其 co-scientist 協助發明超過十億人每天使用的產品 / its co-scientists help invent products a billion-plus people use daily |
| 領域內鑑別 benchmark / within-domain discrimination benchmark | 用同一份公開語料衡量各模型在工業化學裡的鑑別力 | Measures models' discrimination inside industrial chemistry on a shared public corpus | 商用 API ≈ 0 分;open-weight 較佳但 continued pre-training 無效 / commercial APIs ≈ 0; open-weight better, continued pre-training ineffective |
| 本體論結構化對比式訓練 / ontologically structured contrastive training | 用本體論訊號建構對比樣本,教模型領域的實際形狀 | Uses ontological signals to build contrastive pairs that teach the model the domain's actual shape | 他們唯一有效的方法 / the only approach that worked |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Albert Invent(字幕正確) | Albert Invent |
| formulary chemistry | formulation chemistry |
| tacid | tacit |
| onlogically / ontological uh onlogically | ontologically |
| Open-based models | open-weight models |
| aentic / agentic(混用) | agentic |

## 待確認 / To Verify

- **$200B 年 R&D 支出**的統計出處未提供(他只說「a $200 billion annual R&D spend」)。/ No source given for the $200B annual R&D spend figure.
- 被測的「leading embedding model」是哪一個未指名。/ The "leading embedding model" that ranked the answer beyond 300th wasn't named.
- 他們建的 benchmark 是否公開、有無名稱未說明。/ Whether their within-domain discrimination benchmark is public, and what it's called, wasn't stated.
- 「over a billion people depend upon every day」指的具體產品類別未細說。/ The specific product categories behind the "over a billion people" claim weren't detailed.
