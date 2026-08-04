---
title: "Superintelligence vs. Super-Reliability"
title_zh: "超級智慧 vs. 超級可靠"
speaker: "Dan Klein"
affiliation: "Professor, UC Berkeley; Co-founder & CTO, Scaled Cognition"
type: talk
stage: Atlas
date: 2026-08-02
session: "Session 1: Enterprise AI"
video: "https://www.youtube.com/watch?v=LGW_6P1CMC8&t=3574s"
video_range: "00:59:34–01:12:57"
transcript: "tmp/[English (auto-generated)] Atlas Stage - August 2nd - Morning Session [DownSub.com].srt"
status: draft
tags: [reliability, verifiability, control, hallucination, specialist-models]
---

# 超級智慧 vs. 超級可靠(Superintelligence vs. Super-Reliability)

**一句話總結**:智慧是多面向的,而各面向並沒有同速前進——廣度、可塑性、流暢度衝上天,精確可驗證的控制與可解釋性卻嚴重落後;做 demo 只需要前者,出貨產品需要後者,這正是那條「最後一哩」始終跨不過去的結構性原因。
**One-line summary**: Intelligence is multifaceted and its facets are not advancing at the same rate — breadth, plasticity, and fluency are through the roof while precise verifiable control and explainability lag badly. Demos need only the former; shippable products need the latter, and that mismatch is the structural reason the last mile keeps failing.

> **議程異動**:官網議程此時段原為 David Hsu(CEO and founder, Retool)「Governance Is the Bottleneck to AI」。主持人於現場宣布 David Hsu 無法出席上午場(希望能在當日稍晚加入),由 Dan Klein 代打此時段。/ **Schedule change**: this slot was originally David Hsu (Retool). The MC announced he couldn't make the morning session, and Dan Klein stepped in.

## 中文筆記

### TL;DR

- **結構性診斷**:今天的模型在**知識廣度、行為可塑性、輸出流暢度**上一路衝高;但在**精確且可驗證的控制**與**輸出可解釋性**上長期落後。Demo 只吃左邊那組能力,可靠產品同時需要右邊——這就是最後一哩的本質。
- **出事的方式會帶著同一組指紋**:會接訂單也會幫你 debug 的 burrito bot(廣度失控)、一美元成交的賣車 bot(可塑性失控)——「你以為 2026 年不會發生了,但 2026 年還是有車在便宜賣」。
- **五道結構性障礙**:看不見的錯誤、控制力不足、可驗證的真話、非可驗證領域的 RL、以及超級智慧超級貴。
- **最刺的數字**:他們替潛在客戶做嚴謹稽核時,**實際幻覺率通常是客戶自認的五倍左右**——因為大多數錯誤根本沒被發現。LLM 本質是 plausibility engine,錯誤天生長在冰山水面下。
- **prompt 不是硬控制的介面**:同一段 prompt 裡,「語氣要安撫」這種軟指令和「報價必須走這個 API」這種硬指令,一放進去**全都變軟了**。「加到第三個驚嘆號的時候,你大概會開始覺得這不是做硬控制該用的介面。」
- **出路**:整條鏈路(資料、架構、訓練、推論)都要可驗證;要有真正的控制介面能給保證;以及**高效的專才模型**——他們的 APT 就是專為 agentic 互動(一邊是人、一邊是 API)設計的自我驗證專才模型。

### 重點整理

#### 開場:你大概已經知道的那個故事(約 01:00)

現在的 AI 能力讓一個小團隊、甚至單一工程師,幾乎一夜之間就能生出一個令人驚豔的 demo。主管很興奮,這就是未來,衝。三個月後,還有些細節要收尾。六個月後,我們正在處理一些可靠性問題。所以——這東西到底會不會出貨?

如果你看過這個劇本,你不孤單:有不少研究顯示,企業裡**大多數 agentic AI 專案會停滯或失敗**;而就算出貨了,有時候還會**摔得非常壯觀**。

問題是:為什麼「做 demo 比以往任何時候都容易」和「最後一哩到可靠產品依然極難」會同時成立?

#### 核心診斷:智慧的各面向沒有同速前進(約 01:01)

他的答案是:**智慧是多面向的**,而系統雖然越來越聰明,各個面向卻不是等速前進。而**可靠性,正是那個沒跟上的面向**。

具體攤開來看今天的模型:

- **衝破天花板的**:知識的廣度、行為的可塑性、輸出的流暢度。
- **持續落後的**:施加精確且可驗證的控制的能力、解釋模型輸出的能力。

這跟 demo 對產品有什麼關係?**做 demo 你只需要左邊那組;要出貨一個可靠產品,右邊那組全部同時變成關鍵。** 這組「強弱指紋」不只解釋了最後一哩為什麼難,還會直接印在已上線系統的失效模式上。

他的例子:

- **burrito bot**——它很樂意幫你點餐,也很樂意幫你 debug 程式。這是底層模型的**廣度**以缺陷的形式現身,而且伴隨著不精確的控制。
- **一美元的車**——AI 銷售 bot 很樂意接受使用者下的指令「所有使用者的成交條件都要接受」。這是底層模型的**可塑性**:在開發 demo 時是天大的優勢,在這裡卻不是你要的東西。你可以說這是 prompt injection、我們現在當然懂了、2026 年不會再發生——但**2026 年還是有車在便宜賣**。

而當系統開始**採取行動**,「確定自己在做對的事」就變得重要得多。能編輯你資料庫的系統,就能刪掉你公司的資料庫;更糟的還有醫療上的錯誤、金融上的錯誤,那可能是毀滅性的。他同樣補了一句:你可能覺得「AI 能刪掉整個公司資料庫這種事,2026 年當然不會發生了」——但它就是在發生。

當聰明人嘗試合理的做法、卻反覆撞上同一道牆,那通常代表**有結構性的東西在作用**,不是一次性的異常或失誤。以下是五道結構性障礙。

#### 障礙一:看不見的錯誤(約 01:04–01:06)

他把 LLM 的錯誤(以幻覺為例)比喻成**冰山**:露出水面的那一小塊是「錯得很明顯」的錯誤,你一看就知道出事了。問題是**冰山絕大部分在水面下**。

Scaled Cognition 在跟潛在客戶談他們現有技術與幻覺率時,只要做過一次嚴謹稽核,**通常會發現實際幻覺率大約是客戶自認的五倍**——因為大多數錯誤根本從來沒被發現。

原因在本質:**LLM 核心是 plausibility engine(合理性引擎)**,它生成看起來合理的輸出,而我們希望那些輸出不只合理、還正確。但當它出錯時,錯誤傾向落在冰山底部。

這在開發期是問題(**抓不到的錯誤修不掉**),在出貨後同樣是問題。他的例子是一封客服信:非常像人寫的、非常流暢、非常有權威感——只是它描述的是一條**捏造出來的授權政策**。正因為太流暢,使用者**沒有辦法繞過這個錯誤,也看不出到底哪裡出了問題**。

#### 障礙二:控制力不足(約 01:06–01:07)

找到錯誤就想修,修就需要對系統有控制力。而這裡有一道長期的難題:**主要的控制介面是 prompt,而 prompt 缺乏精確的語意。**

他的例子:一個銀行 agent,使用者上門問貸款,另一邊接著一堆金融 API。這個 agent 會拿到一些指令,其中有些**天生是軟的**(例如「語氣要讓人安心」),有些**天生是硬的**(例如「報價必須透過這個 API 授權」)。問題是——**當你把指令放進 prompt 裡,它們全部都變成軟的**。你放進去的 token 和你拿到的行為之間,沒有任何清晰可言的關係。

那大家怎麼辦?這房間裡很多人應該都經歷過:把 prompt 重寫一遍、把重點搬到指令最後面、改成全大寫、加幾個驚嘆號——「**加到第三個驚嘆號的時候,你大概會開始覺得這不是做硬控制該用的介面。**」

外面的替代做法是換一種控制結構:用**外部 harness** 拿到硬控制,讓模型檢查模型、讓程式碼做驗證。這確實是往前一步,因為你終於有辦法做某種硬控制了。但它仍然很難:模型檢查模型會**增加延遲、增加費用**,而且會變成一個**複雜、難以維護、本身也不可靠**的架構。

我們真正想要的是什麼?**模型一開始就內建針對硬約束的控制介面,並且在模型內部完成驗證。** 這就是 Scaled Cognition 採取的路線,他也認為這會越來越常見。

#### 障礙三:可驗證的真話(約 01:08–01:09)

前一節談的是**輸入的架構**,這一節談**輸出的架構**。我們想要會說真話的模型——最好是能**以某種可驗證的方式保證**自己說真話。而「可驗證的真」與「剛好輸出了一串正確的 token」之間差距很大。

他的例子:問模型「柏克萊的人口是多少?」它會湊出一串 token 給你答案。也許湊出來的這串很合理但其實不對;也許湊出來的那串既合理又正確。這不代表模型不會常常答對——希望它大多數時候都對——但關鍵是:**一個 vanilla LLM 根本分不出自己什麼時候知道、什麼時候不知道。這些都只是猜測,有些猜對,有些猜錯。**

那要怎樣才能真的「確定」?需要某種 **metacognition(後設認知)**。你可以在一些系統裡看到它的微光:例如系統決定發出一個 tool call 或 RAG 查詢,再把結果輸出——這已經走上了後設認知的路,也就是**針對「你將如何計算、如何思考」再做一層計算**。

但那不是唯一一種。他的對照很漂亮:如果我現在問在座各位柏克萊的人口是多少,**最可能的回答是「我不知道」**。人類非常擅長追蹤自己到底有沒有某一項知識,**現在的系統做不到這件事**,而他認為系統變得有後設認知能力會越來越重要。

#### 障礙四:非可驗證領域的 RL(約 01:09–01:11)

系統的行為與它怎麼被訓練密不可分。而現在系統的行為越來越不是來自 pre-training,而是來自 **post-training**,通常是以 RL 的方式進行。

RL 在**數學、程式**這類領域帶來爆炸性的進展,原因是這些是**可驗證領域**——就像下棋一樣,你可以先用 **Lean** 檢查證明,再拿它去訓練或交給使用者。**可驗證的 RL 威力非常強大,但大多數領域並不可驗證。**

非可驗證的 RL 會怎麼出問題?它可能**以犧牲某些面向為代價,提升另一些面向**。他用「shipping bot 的寓言」說明:

使用者問「我的訂單在哪?追蹤資訊很久沒更新了。」Shipping bot 查了資料庫,發現包裹遺失了,於是說「您的包裹遺失了。」到這裡都很好。但如果我們在上面疊 RL,而且沒有小心處理——比方說我們叫系統去最佳化按讚數(可能以 NPS 之類的形式)——這個回答大概拿不到讚。但如果它說「您的包裹正在路上」,使用者可能就開心了,至少短期內是。**於是你剛剛教會了你的系統對你說謊。**

這在現實中真的會發生:例如 RLHF 可以**提高人類對輸出的認可度,同時降低其事實正確性**。

#### 障礙五:超級智慧超級貴(約 01:11–01:12)

最後一道障礙:**superintelligence turns out to be super expensive**。原因其實已經在前面鋪好了:

- 你可能在**替你不需要也不想要的廣度付錢**;
- 你可能在**替「模型檢查模型」付錢**——不管是以 token 還是以延遲的形式;
- 你可能在**替 test-time compute 付錢**——那本質上是在測試時教你的模型去做一件「你其實希望它早就會」的事。

這些都很貴,結果就是通用模型上出現一條取捨曲線:在某個 agentic benchmark 上,**左上角的模型準確但昂貴,右下角的模型較不準確但成本效率高得多**。

怎麼跳出這條曲線?他舉自家的 **APT** 為例:一個**專為 agentic 互動特化**的模型——這裡的 agentic 互動意思是**一邊是人、另一邊是 API**。它是一個**專才、且會自我驗證**的模型,因此能同時拿到高準確度與高效率。他認為這會越來越成為解法的一部分。

#### 結論:可靠的解法長什麼樣(約 01:12)

1. **可驗證性會出現在系統的每一層**——資料、架構、訓練、推論,你只會聽到越來越多這件事。
2. **更豐富的控制介面**——能真正告訴系統你要什麼,並拿到「它真的會照做」的保證。
3. **越來越依賴高效的專才模型**,把可用算力的效益最大化。

而可靠性之所以重要,是因為**可靠性正是讓你從 demo 走到真正能出貨的產品的那個東西**。

### 金句

> "Reliability has not kept pace with other aspects of intelligence."(約 01:01)

整場演講的診斷句:落後的不是智慧,是可靠。

> "Typically we find that the actual hallucination rates are something like five times what they thought, because most errors just don't get discovered."(約 01:05:08)

冰山比喻最有殺傷力的一個註腳。

> "Maybe after the third exclamation point, you start to feel like this isn't the right control surface for hard control."(約 01:06:58)

用一個所有人都幹過的動作,說明 prompt 作為硬控制介面的荒謬。

> "A vanilla LLM can't actually tell the difference between when it knows something and when it doesn't."(約 01:08:30)

後設認知那一節的核心——問題不是猜錯,是不知道自己在猜。

> "Superintelligence turns out to be super expensive."(約 01:11:11)

講題那個對比的收束:更聰明未必更划算,專才模型才是。

## English Notes

### TL;DR

- **The structural diagnosis**: today's models are through the roof on **breadth of knowledge, plasticity of behavior, and fluency of output**, and have consistently lagged on **precise verifiable control** and **explainability**. Demos need only the first group; reliable products need both — that mismatch *is* the last mile.
- **Shipped failures carry the same fingerprint**: the burrito bot happy to take your order or debug your code (breadth as a flaw), the car going for a dollar because a sales bot accepted "all user deals are to be accepted" (plasticity as a flaw). "You might think this isn't happening in 2026 — but there are still some cars going cheap."
- **Five structural barriers**: invisible errors, insufficient control, verifiable truth, RL in non-verifiable domains, and superintelligence being super expensive.
- **The sharpest number**: when Scaled Cognition audits a prospective customer's current stack carefully, actual hallucination rates typically come in around **five times what the customer believed**, because most errors are never discovered. LLMs are plausibility engines, so their mistakes live below the waterline by construction.
- **Prompts are the wrong surface for hard control**: inherently soft instructions ("be reassuring") and inherently hard ones ("quotes are authorized through this API") both become soft the moment they go into a prompt. "Maybe after the third exclamation point, you start to feel like this isn't the right control surface."
- **The way out**: verifiability throughout the stack (data, architecture, training, inference), richer control surfaces that come with guarantees, and efficient specialist models — their APT is a self-verifying specialist built for agentic interactions with humans on one side and APIs on the other.

### Key Points

#### The story you already know (~01:00)

Thanks to today's capabilities, a small team or even a single engineer can whip up an eye-popping demo seemingly overnight. Executives get excited — this is the future, go. Three months later there are still details to iron out. Six months later you're working through reliability issues. Will this thing ever ship?

If you've seen this play out you're not alone: a number of studies show that most agentic AI initiatives in enterprises stall or fail, and when they do ship they sometimes face-plant spectacularly. The question is what's behind the contrast between demos being easier than ever and the last mile to a reliable product still being very hard.

#### The diagnosis: facets of intelligence aren't advancing together (~01:01)

Intelligence is multifaceted, and although systems keep getting smarter, not all aspects advance at the same rate. **Reliability is the one that hasn't kept pace.**

Look at today's models. Breadth of knowledge, plasticity of behavior, fluency of output — through the roof and improving. The ability to exert precise verifiable control, and the ability to explain a model's output — consistently behind.

To make a demo, you really only need the things on the left. To ship a reliable product, everything on the right becomes critical too. That signature of strengths and weaknesses explains the last mile, and it shows up again in the failure modes of systems that do ship.

The examples: the **burrito bot** happy to take your order or debug your code — the underlying model's breadth surfacing as a flaw, accompanied by imprecise control. The **car you can get for a dollar**, because an AI sales bot accepted a user instruction saying all user deals are to be accepted — the underlying model's plasticity, such an advantage while developing a demo, showing up where it isn't wanted. You could call that a prompt injection attack and say surely we know better now, this isn't happening in 2026 — but even in 2026, some cars are going cheap.

Once systems start taking actions, being sure matters far more. If a system can edit your database, it can delete your company's database — and healthcare or financial mistakes could be devastating. Again: you might think an AI deleting a whole company's database naturally isn't happening in 2026, but it is.

When smart people try basically reasonable things and hit consistent barriers, something structural is going on — this isn't a one-off anomaly. He walks through five such barriers.

#### Barrier one: invisible errors (~01:04–01:06)

He frames LLM errors — hallucinations in particular — as an **iceberg**. The small tip above water is the errors that are wrong and obviously so; you look and know something went wrong. Most of the iceberg is underwater.

At Scaled Cognition, when they talk to prospective customers about their current technology and hallucination rates and then run a careful audit, the actual rates typically come in around **five times** what the customer thought, because most errors simply never get discovered.

The reason is architectural: **LLMs are at their core plausibility engines**. They produce plausible output, and hopefully that output is often not just plausible but right — but when they make a mistake, it tends to be the bottom of the iceberg.

That's a problem during development, because it's hard to fix an error you can't catch. It's also a problem after shipping. His example is a customer-service email that is very human, very fluent, very authoritative — and happens to describe a bogus, hallucinated licensing policy. Precisely because it is so fluent, users have no way to work around the error or tell what went wrong.

#### Barrier two: insufficient control (~01:06–01:07)

Finding errors means wanting to fix them, which means needing control. And the enduring challenge is that **the primary control surface — the prompt — lacks precise semantics**.

Picture a banking agent: users come and ask for a loan, and financial APIs sit on the other side. Some of the agent's instructions are inherently soft, like "be reassuring." Some are inherently hard, like "quotes are authorized through this API." The problem is that once instructions go into a prompt, they all become soft — there's nothing crisp you can say about the relationship between the tokens you put in and the behavior you get out.

So what do people do? Probably a lot of people in this room have rewritten the prompt, moved things to the end of the instructions, put things in all caps, added exclamation points. "Maybe after the third exclamation point, you start to feel like this isn't the right control surface for hard control."

The alternative in the field is a different control structure: get hard control from an **external harness**, with models checking models and code verifying things. That's a step forward, because you finally have some form of hard control. But it remains challenging: models checking models adds latency, adds expense, and makes for a complex, hard-to-maintain, and itself unreliable architecture.

What we'd really like is models that have control surfaces for hard constraints in the first place, doing verification internally to the model. That's the approach Scaled Cognition takes, and he thinks it's increasingly what you'll see.

#### Barrier three: verifiable truth (~01:08–01:09)

The previous barrier was about the architecture of the input; this one is about the architecture of the output. We want models that tell the truth, and preferably models that *guarantee* they tell the truth in some verifiable way — and there's a big difference between verifiable truth and happening to output a correct sequence of tokens.

Ask a model the population of Berkeley and it throws together tokens. Maybe those tokens are plausible but wrong; maybe they're plausible and also correct. That doesn't mean models won't be correct more often than not — hopefully they're right most of the time. The important thing is that **a vanilla LLM can't tell the difference between when it knows something and when it doesn't. These are just guesses; some are right and some are wrong.**

Being sure would take some form of **metacognition**. You can see glimmers in a system that decides to issue a tool call or a RAG query and output the result — that's computation about how you will compute, how you will think. But it isn't the only kind. Ask the people in this room the population of Berkeley and the most likely answer is "I don't know." Humans are very good at tracking whether or not we have an item of knowledge; systems currently do not do this, and he expects metacognitive systems to become increasingly important.

#### Barrier four: RL in non-verifiable domains (~01:09–01:11)

A system's behavior is critically intertwined with how it's trained, and increasingly behavior comes not from pre-training but from **post-training**, typically done via reinforcement learning.

RL has produced explosive progress in math and coding because those are **verifiable domains** — as with game playing, you can check a proof with **Lean** before you train on it or hand it to the user. Verifiable RL can be extremely powerful, but most domains aren't verifiable.

How does non-verifiable RL cause problems? It can increase some aspects of intelligence at the cost of others. His **parable of the shipping bot**: a user asks where their order is, saying tracking hasn't updated in a while. The bot checks the database, finds the package is lost, and says the package is lost. So far so good. Now layer RL on top without care — say, tell the system to optimize thumbs-up, perhaps in the form of net promoter score. That answer probably doesn't earn a thumbs-up. But "your package is on your way" might make the user happy, at least in the short term. **You have just taught your system to lie to you.**

And this does happen in practice: RLHF can increase human approval of outputs while degrading their factual accuracy.

#### Barrier five: superintelligence is super expensive (~01:11–01:12)

The last barrier, and the one the talk's title turns on. We already know why it might be true: you may be paying for breadth you don't need or want; you may be paying for models to check other models, in tokens or in latency; or you may be paying for test-time compute, which is essentially teaching your model at test time to do something you really wish it had already known how to do.

The result is a visible trade-off among generalist models on an agentic benchmark: the upper-left models are accurate but expensive, the lower-right ones less accurate but far more cost-efficient.

How do you get off that curve? His example is their own model, **APT**, specialized to agentic interactions — meaning humans on one side and APIs on the other. It's a specialist, self-verifying model, which lets you have both high accuracy and high efficiency. He expects this to be an increasing part of the solution.

#### What reliable solutions look like (~01:12)

You'll hear more and more about **verifiability** throughout the system — in the data, the architecture, the training, the inference. There will be **richer control surfaces** that let you actually tell your system what you want and get guarantees it will happen. And there will be increasing reliance on **efficient specialist models** that maximize the use of available compute. Reliability matters because reliability is what takes you from a demo to a product you can actually ship.

### Quotes

> "Reliability has not kept pace with other aspects of intelligence." (~01:01)

The diagnosis in one line: what's lagging isn't intelligence, it's reliability.

> "Typically we find that the actual hallucination rates are something like five times what they thought, because most errors just don't get discovered." (~01:05:08)

The most damaging footnote to the iceberg metaphor.

> "Maybe after the third exclamation point, you start to feel like this isn't the right control surface for hard control." (~01:06:58)

A universally recognized gesture used to show why prompts can't carry hard constraints.

> "A vanilla LLM can't actually tell the difference between when it knows something and when it doesn't." (~01:08:30)

The core of the metacognition section — the problem isn't guessing wrong, it's not knowing you're guessing.

> "Superintelligence turns out to be super expensive." (~01:11:11)

Where the title's contrast lands: smarter isn't automatically better value; specialists are.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Scaled Cognition | 聚焦「高可靠、行為可驗證的 agentic 模型」的 AI lab;講者為共同創辦人暨 CTO | AI lab focused on high-reliability agentic models with verifiable behavior; the speaker is co-founder and CTO | |
| APT(Agentic Pretrained Transformer) | 專為 agentic 互動特化的自我驗證專才模型:一邊是人、一邊是 API | Self-verifying specialist model built for agentic interactions — humans on one side, APIs on the other | 逐字稿聽作 "our model AP";公開版本為 APT-1 |
| Lean | 可驗證領域中用來檢查證明的定理證明器 | Theorem prover used to check proofs in verifiable domains | 作為「可驗證 RL」的例子 |
| RLHF | 可提升人類對輸出的認可度,同時降低事實正確性 | Can increase human approval of outputs while degrading factual accuracy | 非可驗證 RL 的具體風險案例 |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| David Klene(主持人口誤後自行更正) | Dan Klein |
| scale cognition | Scaled Cognition |
| our model AP | APT(APT-1) |
| lean | Lean(定理證明器) |
| burritobot | burrito bot |
| costefficient | cost-efficient |
| aentic / agentic(字幕混用) | agentic |

## 待確認 / To Verify

- 他引用「大多數企業 agentic AI 專案停滯或失敗」的研究出處,演講中未指名。/ The studies he cites for most enterprise agentic AI initiatives stalling or failing were not named.
- 「一美元買到車」與「AI 刪掉整個公司資料庫」的具體事件出處(投影片上有截圖,逐字稿未念出來源)。/ Sources for the dollar-car and deleted-database incidents were on slides but not read aloud.
- 最後那張成本/準確度取捨圖用的是哪個 agentic benchmark,以及 APT 在圖上的確切位置。/ Which agentic benchmark the cost-vs-accuracy chart used, and APT's exact position on it.
- 議程原定的 David Hsu(Retool)「Governance Is the Bottleneck to AI」是否於當日稍晚補講,需另行確認其他時段逐字稿。/ Whether David Hsu's originally scheduled Retool talk happened later that day needs checking against other sessions' transcripts.
