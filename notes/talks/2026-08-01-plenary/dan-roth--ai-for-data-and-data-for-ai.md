---
title: "AI for Data and Data for AI"
title_zh: "用 AI 處理資料,用資料餵養 AI"
speaker: "Dan Roth"
affiliation: "Chief AI Scientist, Oracle; Professor, UPenn"
type: talk
stage: Plenary
date: 2026-08-01
session: "Session 3: Agentic AI Foundational Capabilities"
video: "https://www.youtube.com/watch?v=Tcn5Yb2K0h4&t=5024s"
video_range: "01:23:44–01:36:24"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [data, retrieval, nl2sql, enterprise, reliability]
---

# 用 AI 處理資料,用資料餵養 AI(AI for Data and Data for AI)

**一句話總結**:通用資料已經被模型吞完了,真正有價值的企業、醫療、政府資料會永遠留在模型外面且不斷變動——所以 agent 底下那層「語意資料層」才是勝負關鍵;而現在連問「歐洲男子網球選手獎金排名」這種小問題,前沿模型都會漏人、算錯、前後不一致。
**One-line summary**: General-purpose data has already been swallowed by the models; the data that matters — corporate, medical, government — will stay outside them and keep changing, which makes the semantic data layer beneath agents the real battleground. And today a frontier model can't even rank European male tennis players by prize money without dropping a player, duplicating a figure, and contradicting itself on retry.

## 中文筆記

### TL;DR

- **通用資料的時代結束了**:模型供應商已經吞掉了大部分通用資料,但企業、金融機構、政府單位、醫療中心、個人的資料**會留在模型之外,而且是動態的**。GenAI 的關鍵用例之一,將是**協調並支撐對外部資料的存取與使用**。
- **「AI for data」只是上半場,「data for AI」才是重點**:agent 需要存取的資料種類極多(設計文件、ticket、歷代軟體的往來討論、trajectory、操作紀錄、tool-use traces)。**資料的品質、結構與治理,決定了 AI 實際能做到什麼。**
- **檢索能用是個迷思**:「試著搜尋你自己的 email,然後告訴我它到底能不能用。」檢索只有在查詢與文件**詞面夠接近**時才有效,而這通常不會發生——所以需要跨知識來源的**語意資料層**。
- **絕對數字比排行榜誠實**:Oracle 團隊在 Spider 2 與 Archer 上都名列前茅,但**Archer 的絕對成績約 55%、Spider 2 只有 70 出頭**——離「能可靠存取與使用資料」還很遠。
- **網球範例把問題攤開**:前沿模型能自己規劃、跨結構化/非結構化/網路資料取材、調和衝突資訊、輸出漂亮表格——但**排序沒排好、漏掉 Carlos Alcaraz、兩名選手的獎金精確到美元完全相同**;提醒它補上 Alcaraz 之後,**Andrey Rublev 整個消失了**,金額也悄悄變動。
- **真正的結論不是「模型不行」,而是「失敗不可見」**:網球錯了無所謂,但同樣的查詢換成公司財務分析呢?**visibility of failure** 沒解決,這類系統就沒辦法可靠、一致地使用。

### 重點整理

#### 換檔:從模型談到資料(約 01:23–01:25)

他刻意換個主題:談資料——我們怎麼使用資料、怎麼存取資料。他真正興奮的是 **GenAI 對資料的承諾**:讓我們從那個混亂的世界——**各種型態、各種表示法的資料,人得先學會領域知識、學會資料怎麼被表示、把資料從一種格式轉成另一種、還要搞懂怎麼融合異質資料**——搬到一個乾淨得多的世界:**用我們自己的概念、自己的術語、自己的指標,直接在概念層次上操作資料。**

而讓這件事更令人興奮的是一個事實:**世界上大量的資料會一直待在語言模型之外**。語言模型已經吞掉了很多資料——這也是我們今天有強大 agent 的原因——但**通用資料已經沒有了**,大部分都已經被模型供應商吸收完畢。可是外面還有非常多資料:**企業的資料、金融機構的資料、政府單位、個人、醫療中心的資料;這些資料會留在模型外面,而且是動態的。**

所以問題變成:**我們怎麼處理這些外部資料?** 他認為 GenAI 的關鍵用例之一,就是**協調並支撐外部資料的存取與使用**。這對人類消費資料成立,**對 agent 使用資料更重要**——想想你的 coding agent:要開發 coding agent,它得存取大量資料,從設計文件、ticket,到關於前幾代軟體發生過什麼事的往來討論;它得存取知識來源並對其做點什麼。

#### 為什麼「靠檢索做決策」比想像中難(約 01:25–01:28)

**可靠地支撐那些依賴「取回資料再使用資料」的決策,是極度困難的——比我們以為的難得多。** 原因很多:

- **資訊檢索本身**。「有一個迷思是資訊檢索已經能用了——但你試著搜尋自己的 email,然後告訴我它到底能不能用。」
- 理解**資訊需求**、理解**被儲存的資料**、實際**使用資料**——在今天的世界裡全都極具挑戰性。

多數時候我們想的是 **AI for data**:AI 怎麼幫我們(人)使用資料。**「別問 AI 能為你做什麼」——我們真正在乎的是 data for AI**,因為要開發 agent,agent 得存取大量不同種類的資料。

所以 **AI 與企業資料的關係不是一維的**:AI 解鎖你既有資料的價值,但**你資料的品質、結構與治理,反過來決定了 AI 實際能做到什麼**。同時理解方程式的兩邊非常重要,**這就是「能用的 AI」和「不能用的 AI」之間的差別**。

**agent 底下那層資料層至關重要,也極難建造。** 想想 agentic 能力需要什麼資料:各式各樣的文件類型,加上 **trajectory data、operation data、tool-use traces**——你的 agent 要真的做到你要它做的事,這些都得有。

#### 難在哪:核心困難與底層要求(約 01:28–01:31)

**核心困難**:

- **檢索**:除非你表達資訊的方式和你在乎的文件**詞面上夠接近**,否則檢索不會work——而這通常不會發生。這就**必須發展跨知識來源的語意資料層(semantic data layer)**:一方面把資料的表示拉近到資訊被表達的方式,另一方面**讓你不必在意資料來自哪個來源**。
- **結構化**:NL to SQL、NL 到其他形式化表示。這個轉換非常困難,**部分原因是它同時也依賴檢索**。
- **多知識來源**:要讓 agent 用資料,就得讓它存取多個知識來源,而**每個來源都需要各自的專業知識**。
- **富文件(rich documents)**:論文、圖表、影片、影像越存越多,而**這些富資料內部的資訊,除非你做點什麼去暴露它,否則你的檢索根本看不到**;還有一些前處理,你的 agent 可能做、也可能不做。
- **規劃**:怎麼存取資料、用什麼順序存取、**怎麼用一個來源去過濾另一個來源**——這是非常有挑戰性的問題(下一節的網球例子就是為此)。
- **衝突資訊**:想想你的檔案系統或 email,裡面有多少互相矛盾的資料?而我們希望存取資料的 agent 能好好處理這件事。
- **推理**:很多情況下**超出通用模型的能力範圍**。

**在這些核心困難之下,還有一層**:治理、政策執行、可靠性、一致性、可稽核性——只要你想在企業、醫療中心這類場景使用大規模資料,這些非處理不可。加上**最佳化**:第一代我們不太在意成本,但現在得在意——**什麼時候離線處理資料、什麼時候在 runtime 處理、怎麼快取運算、怎麼利用 query log 與歷史紀錄**,全都是很難的問題。

#### NL2SQL:排行榜第一,但絕對分數才是重點(約 01:31)

他挑一個切面深入:**NL2SQL**。先來個「厚臉皮的置入」——Oracle 的一些團隊參加 **Spider 2** 與 **Archer** 等競賽,表現非常好,在排行榜上名列前茅。

**但比置入更重要的是絕對成績**:**Archer 大約 55%,Spider 2 只有 70 出頭**——這意味著**我們距離「能好好存取與使用資料」還非常遠**。

#### 網球範例:漂亮的表格,和藏在裡面的四個錯(約 01:31–01:35)

他自己是網球迷,所以拿網球當例子。幾週前他丟給一個頂尖模型一個問題:**「給我一份歐洲男子網球選手的清單,按網球收入排序。只算網球收入。」**

這問題其實非常複雜:模型得知道**誰是選手、他們來自哪個國家、那個國家算不算歐洲、2025 年他們打了哪些賽事、每一站賺了多少錢**。模型確實把思路攤開給他看——**去了哪些來源、查了哪些表格、讀了哪些文字段落**——最後給出一張漂亮的表。

**先別急著挑錯,想想這有多酷**:這正是那個承諾——**我只用自然語言表達資訊需求,模型就自己設計了計畫、存取多個結構化與非結構化來源與網路、用參數知識判斷國家歸屬、調和了外面大量互相矛盾的資訊、彙總並整理成一張表。** 漂亮。

**然後看細節**:

1. 有**兩筆排序錯了**。這是最讓他意外的錯誤,因為**模型應該去呼叫工具來正確排序**才對。
2. **有人不見了**——**模型把 Carlos Alcaraz 給忘了**。
3. 另外有**兩位選手的收入精確到美元完全相同**。他們賺的是數百萬美元等級,卻精確到個位數美元一模一樣——**不可能發生,顯然是錯的**。

**為什麼會這樣?** 因為模型必須**跨知識來源最佳化存取路徑**。它可以先產生選手清單、再判斷是不是歐洲國家、再查打了哪些賽事、每站賺多少;也可以**從賽事清單下手**,看每站誰打了、賺多少。**賽事數量遠少於選手,所以也許後者才是對的做法——但另一方面,賽事的資料比較雜訊多。** 所以做對這件事,**真的取決於你對資料與領域的理解**;在網球這個領域還算可能,**在大多數領域就是不可能**。所以雖然 agent 做這件事比我們快,**它們容易出錯、成本又高**。

**最關鍵的是接下來這一步**:他提醒模型忘了 Carlos Alcaraz,模型把 Alcaraz 加了進去——**但仔細看會發現其他東西也變了**:排在第七的 **Andrey Rublev 從新清單裡完全消失了**;金額也有些微變動;**某個原本超過六百萬的人,現在變成不到六百萬**。**前後不一致。**

**而他真正想指出的是**:這是網球,誰在乎呢?而且**他自己知道正確答案,所以他有能力檢查對錯**。**但如果同樣一個問題問的是你公司的財務分析,或任何其他敏感資訊呢?** 這時候 **visibility of failure(失敗的可見性)** 就變得極其重要。**不解決這件事,我們就沒辦法可靠、一致地使用這類系統。**

#### 收尾(約 01:35–01:36)

真實世界的資料是**多模態、時序性、多語言、異質的**,要把裡面的資訊解鎖出來還有非常多工作要做。而**同時理解方程式的兩邊**——**AI for human consumption over data**(用 AI 幫人使用資料)與 **data for agent consumption**(把資料備妥給 agent 使用)——**正是「能用的 AI」和「令人失望的 AI」之間的差別。**

### 金句

> "There is a myth that information retrieval works, but you know, try to search your email and tell me whether it does work."(約 01:26)

一句話戳破 RAG 時代最常見的前提假設。

> "Ask what AI can do for you — but really we care about data for AI."(約 01:26)

演講標題的雙關,也是他的立場:重點在後半句。

> "While AI unlocks value from the data you already have, the quality, the structure, the governance of your data really determines what AI can actually do."(約 01:27)

企業導入 AI 的實際天花板不在模型,而在資料層。

> "This is tennis — really, who cares. … But if this was the same question that you ask about your financial analysis of your company, the notion of visibility of failure is really important."(約 01:35)

整場演講的真正論點:問題不是模型會錯,而是你不知道它錯了。

> "AI for human consumption over data, and data for agent consumption, is really the difference between AI that works and AI that disappoints."(約 01:36)

## English Notes

### TL;DR

- **The era of general-purpose data is over.** Model providers have already swallowed most of it, but the data belonging to corporations, financial institutions, government agencies, medical centers and individuals **will stay outside the models, and it is dynamic.** One of GenAI's key use cases will be **orchestrating and supporting access to and use of external data.**
- **"AI for data" is only the first half; "data for AI" is the point.** Agents need an enormous range of data — design documents, tickets, correspondence about earlier generations of the software, trajectories, operational records, tool-use traces. **The quality, structure and governance of your data determine what AI can actually do.**
- **"Retrieval works" is a myth.** "Try to search your email and tell me whether it does work." Retrieval only fires when the query is **lexically close enough** to the target documents, which typically doesn't happen — hence the need for a **semantic data layer** across knowledge sources.
- **Absolute numbers are more honest than leaderboards.** Oracle's teams lead on Spider 2 and Archer, but **Archer sits around 55% and Spider 2 in the low 70s** — far from being able to access and use data properly.
- **The tennis example lays it bare.** A frontier model planned its own approach, pulled from structured, unstructured and web sources, reconciled conflicting information and produced a beautiful table — **with two rows mis-sorted, Carlos Alcaraz missing entirely, and two players' prize money identical to the dollar.** Prompted to add Alcaraz, it did — and **Andrey Rublev vanished** from the list while the numbers quietly shifted.
- **The real conclusion isn't "models are bad" — it's that failure is invisible.** Getting tennis wrong costs nothing; ask the same question about your company's financials and **visibility of failure** becomes the blocker to using these systems reliably and consistently.

### Key Points

#### Changing gear: from models to data (~01:23–01:25)

He deliberately shifts topic to data — how we use it, how we access it. What excites him is **GenAI's promise for data**: moving from the messy world — **many data types and representations, where people must learn the domain, learn how data is represented, transform between formats, and figure out how to fuse diverse data** — to something far cleaner: **working with data at a conceptual level, on our own terms, with our own metrics.**

What adds to the excitement is a structural fact: **a large amount of the world's data will remain outside language models.** Models have swallowed a lot of data — which is why we have powerful agents today — but **there is no more general-purpose data;** most of it has already been absorbed by model providers. Yet there is a lot of data out there: **corporations, financial institutions, government agencies, individuals, medical centers. This data will stay outside the models, and it will be dynamic.**

So the question becomes: how do we deal with this external data? He believes one of GenAI's key use cases will be **orchestrating and supporting access to and use of external data.** True for human consumption, but **just as important for agents.** Think about coding agents: to build them, they need access to a great deal of data — from design documents to tickets to correspondence about what happened in previous generations of the software — and they need to do something with those knowledge sources.

#### Why decisions that depend on retrieval are so hard (~01:25–01:28)

**Reliably supporting decisions that depend on retrieving and using data is extremely difficult — more difficult than we tend to think.** Several reasons:

- **Information retrieval itself.** "There is a myth that information retrieval works — but try to search your email and tell me whether it does."
- **Understanding information needs**, understanding **the stored data**, and actually **using the data** are all extremely challenging in today's world.

Most of the time we frame this as **AI for data** — how AI can help *us* use data. **"Ask what AI can do for you" — but what we really care about is data for AI**, because building agents means agents accessing lots of different kinds of data.

So **the relationship between AI and enterprise data is not one-dimensional.** AI unlocks value from the data you already have, but **the quality, structure and governance of your data determine what AI can actually do.** Understanding both sides of that equation is **the difference between AI that works and AI that may not.**

**The data layer underneath agents is crucially important and very difficult to build.** Consider what agentic capabilities need: the many distinct types of documentation that exist, plus **trajectory data, operational data, tool-use traces** — everything your agents need to actually do what you want.

#### Where the difficulty lives (~01:28–01:31)

**Core difficulties:**

- **Retrieval.** It doesn't work unless the way you present your information is **lexically close enough** to the documents you care about — which typically doesn't happen. This **necessitates a semantic data layer across knowledge sources**: bring the representation of the data closer to how information is expressed, and make it so **you don't have to care which data source it came from.**
- **Structure.** NL-to-SQL, NL-to-other-formal-representations. Very difficult, **partly because it also depends on retrieval.**
- **Multiple knowledge sources.** Agents need access to many of them, and **each requires its own expertise.**
- **Rich documents.** More and more rich documents get stored — papers, figures, video, images — and **the information inside them is not exposed to your retrieval unless you do something to expose it.** Plus preprocessing your agents may or may not perform.
- **Planning.** How to access data, in what order, **how to filter one source by another** — very challenging (the tennis example exists to show this).
- **Conflicting information.** Think about your file system or your email: how much of it contradicts itself? And we want data-accessing agents to handle that well.
- **Reasoning.** In many cases **beyond the capabilities of general-purpose models.**

**Underneath all of it** sit governance, policy enforcement, reliability, consistency and auditability — unavoidable if you want to use large-scale data in a corporation or a medical center. Plus **optimization**: the first generation didn't care much about cost, but now we do — **when to process data offline versus at runtime, how to cache computation, how to use query logs and history** — all genuinely hard problems.

#### NL2SQL: top of the leaderboard, and what the absolute score says (~01:31)

He takes one slice in depth: **NL2SQL**. First a self-described shameless plug — some of Oracle's teams have competed in benchmarks like **Spider 2** and **Archer** and done really well, leading the leaderboards.

**But beyond the plug, look at the absolute results**: **Archer is around 55%, Spider 2 just in the low 70s** — which means **we are really far from being able to address the problem of accessing and using data properly.**

#### The tennis example: a beautiful table with four things wrong (~01:31–01:35)

He follows tennis closely, so tennis is his running example. A few weeks ago he put a question to a top model: **"Give me a list of the European male tennis players sorted by their tennis income. Only tennis income."**

It's a genuinely complex question: the model must know **who the players are, which countries they come from, whether those are in Europe, which tournaments they played in 2025, and how much they made at each.** The model did show its work — **which sources it went to, which tables, which pieces of text** — and produced a nice table.

**Before analyzing it, appreciate how cool this is.** This is the promise: **express an information need in natural language, and the model devises a plan, accesses many sources — structured, unstructured, web — uses parametric knowledge to know where countries are, reconciles a great deal of conflicting information, aggregates it, and summarizes it into a table.** Beautiful.

**Then look at the details:**

1. **Two entries are not sorted correctly.** This was the most surprising mistake to him, **because the model should have called a tool to do the sorting properly.**
2. **Someone is missing** — **the model forgot Carlos Alcaraz.**
3. **Two players' income is identical to the dollar.** They made millions of dollars, and the figures match to the dollar. **That cannot happen. Clearly a mistake.**

**Why?** The model has to **optimize access across knowledge sources.** It can generate a list of players, filter to European countries, find which tournaments they played and how much they made; or it can start **from the list of tournaments** and look at who played and what they earned. **There are far fewer tournaments than players, so maybe that's the right way — but tournament data is noisier.** Doing it right **really depends on understanding the data and the domain** — possible in tennis, **and in most cases simply impossible.** So while agents do this faster than we can, **they're prone to errors and high cost.**

**And then the step that matters most.** He reminded the model it had forgotten Carlos Alcaraz; it added him — **but look carefully and a few other things changed too.** **Andrey Rublev, number seven, completely disappeared** from the new list. The money changed a little. **Someone who had made over six million now makes less than six million.** It is not consistent.

**His actual point:** this is tennis — who cares. And **he knows the results, so he can look at it and decide whether it's correct.** **But if this were the same question about your company's financial analysis, or any other sensitive information?** Then **the notion of visibility of failure becomes really important. Without addressing it, we cannot use these kinds of systems reliably and consistently.**

#### Closing (~01:35–01:36)

Real-world data is **multimodal, temporal, multilingual, heterogeneous**, and a great deal of work remains to unlock the information inside it. Understanding **both sides of the equation** — **AI for human consumption over data**, and **data for agent consumption** — is **really the difference between AI that works and AI that disappoints.**

### Quotes

> "There is a myth that information retrieval works, but you know, try to search your email and tell me whether it does work." (~01:26)

One line puncturing the RAG era's most common premise.

> "Ask what AI can do for you — but really we care about data for AI." (~01:26)

The talk title's pun, and his position: the second half is what matters.

> "While AI unlocks value from the data you already have, the quality, the structure, the governance of your data really determines what AI can actually do." (~01:27)

An enterprise's real AI ceiling is set by its data layer, not its model.

> "This is tennis — really, who cares. … But if this was the same question that you ask about your financial analysis of your company, the notion of visibility of failure is really important." (~01:35)

The talk's actual thesis: the problem isn't that models err, it's that you can't see when they do.

> "AI for human consumption over data, and data for agent consumption, is really the difference between AI that works and AI that disappoints." (~01:36)

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Spider 2 | 真實企業級 text-to-SQL benchmark;演講中絕對成績「70 出頭」 | Real-world enterprise text-to-SQL benchmark; absolute score cited as "low 70s" | Oracle 團隊於 Spider 2.0-Lite 排行榜居首 / Oracle leads the Spider 2.0-Lite leaderboard |
| Archer | 雙語 NL2SQL 評測挑戰;演講中絕對成績「約 55%」 | Bilingual NL2SQL evaluation challenge; absolute score cited as "~55%" | 與公開報導的英文執行準確率 54.96% 相符 / matches the publicly reported 54.96% English execution accuracy |
| 語意資料層 / Semantic data layer | 跨知識來源的表示層,讓查詢不必詞面對齊、也不必在意資料來源 | Cross-source representation layer removing both lexical-match dependence and source awareness | 他點名的核心必要建設 / the core piece he says must be built |
| 網球獎金排名範例 / Tennis prize-money example | 用一個頂尖模型的真實輸出展示規劃、衝突調和與四類錯誤 | A real frontier-model output demonstrating planning, conflict reconciliation, and four classes of error | 模型名稱未公開 / model not named |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| UPEN | UPenn (University of Pennsylvania) |
| Genai | GenAI |
| Alcarez / Carlos Alcarez | Carlos Alcaraz |
| Andre Rublev | Andrey Rublev |
| Archer H | Archer(疑為 "Archer, uh" 的誤聽 / likely a mis-hearing of "Archer, uh") |
| NL2 to SQL | NL2SQL |
| noted one-dimensional | not one-dimensional |
| multimodel | multimodal |
| department(panel 段) | deployment |

## 待確認 / To Verify

- 網球查詢所使用的「top model」未具名。/ The "top model" used for the tennis query was not named.
- 「17 different types of documentation」為口語約數還是指某個明確清單,無法從逐字稿判斷。/ Unclear whether "the 17 different types of documentation" refers to a specific enumeration or is rhetorical.
- Spider 2「低 70 幾」對應的是哪個子集(Spider 2.0-Lite / Snow / full),演講未說明。/ Which Spider 2 subset the "low 70s" refers to (Lite / Snow / full) was not specified.
- 字幕中的 "Archer H" 是否指 Archer 的某個 hard 子集,需看投影片確認。/ Whether "Archer H" denotes an Archer hard subset — check the slides.
