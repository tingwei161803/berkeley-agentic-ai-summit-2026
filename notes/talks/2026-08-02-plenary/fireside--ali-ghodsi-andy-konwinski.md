---
title: "Fireside Chat: Ali Ghodsi × Andy Konwinski"
title_zh: "爐邊對談:Ali Ghodsi × Andy Konwinski"
speaker: "Ali Ghodsi; Andy Konwinski"
affiliation: "Ali Ghodsi — Co-Founder & CEO, Databricks;Andy Konwinski — Co-Founder, Databricks; Perplexity; Laude Ventures"
type: fireside
stage: Plenary
date: 2026-08-02
session: "Fireside Chat"
video: "https://www.youtube.com/watch?v=UdS3iisKhCk&t=5791s"
video_range: "01:36:31–02:07:48"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 2nd - Morning Session [DownSub.com].srt"
status: draft
tags: [databricks, open-source, evaluation, benchmarks, open-science]
---

# 爐邊對談:Ali Ghodsi × Andy Konwinski(Fireside Chat)

**一句話總結**:兩位 Databricks 共同創辦人從 2009 年的 Berkeley 研究室聊到 2026 年的 benchmark 危機——結論是模型與 harness 遲早會被優化器自動爬坡,人類真正該花腦力的地方是**寫出好的 eval**;而 benchmark 應該像軟體一樣持續版本迭代而不是每次砍掉重練,開放科學則需要一種「實驗室的實驗室」新結構才有機會與封閉前沿實驗室共存。
**One-line summary**: Two Databricks co-founders trace a line from a 2009 Berkeley research group to the 2026 benchmark crisis — concluding that models and harnesses will increasingly be hill-climbed by optimizers, so the place humans should spend their brainpower is **writing good evals**; that benchmarks should be versioned like software instead of thrown away and rebuilt each round; and that open science needs a new "lab of labs" structure to stand a chance alongside the closed frontier labs.

## 中文筆記

### 對談雙方

| 講者 | 身分 | 這場對談裡的視角 |
|------|------|------------------|
| Ali Ghodsi | Co-Founder & CEO, Databricks;UC Berkeley 兼任教授 | 經營一家 13 年、11,000 人的公司,從內部實際部署 AI 的角度看事情 |
| Andy Konwinski | Co-Founder, Databricks;Perplexity;Laude Ventures | 從 Laude 這一側看 benchmark、eval 與開放科學的生態建設 |

主持人 Aaron Jacobson(NEA)介紹時提到,NEA 早在 2014 年 Series B 就投了 Databricks。兩人都出身 Berkeley 的 Mesos / Spark 研究線:Ali 是 Apache Spark 的創建者之一,研究資源管理、排程與資料快取(成果應用於 Apache Mesos 與 Apache Hadoop);Andy 在 Berkeley 拿到 CS 博士,參與 Apache Hadoop、共同創建 Apache Mesos 與 Apache Spark,現在在 Berkeley 共同開設「從研究到新創」的博士生 seminar。

### 主題一:2009 年的 Berkeley,以及那位睡著的市長(約 01:38–01:42)

- **Andy 的記憶**:2009 年 Ion Stoica 或 Scott Shenker 發了一封信給 Mesos 小組說「有位訪問學者要加入」。他和 Matei Zaharia、Ben Hindman 當時「非常沒安全感」,滿腦子想的是「這位大神是誰?第一作者還輪不輪得到我?」——然後 Ali 走進來,身材壯碩,Andy 心想「希望我們不用靠掰手腕決定第一作者」。後來 Ali 做出了 **DRF(Dominant Resource Fairness)** 那篇論文,並且從研究夥伴變成他的導師、實質上的共同指導教授。
- **Ali 的記憶**:2009–2012 年的 Berkeley「站在所有新演算法的最前線,因為**新的電腦就是資料中心**」。當時對 AI 與機器學習、對資料中心這些題目其實充滿懷疑。他說那是他最好、也最具形塑性的幾年。
- **他最喜歡的故事**:Databricks 剛創立時有個大辯論——公司要設在 Berkeley 還是 San Francisco?創辦人剛好一半一半。他們先去見了校長,校長說「你們該去跟市長談談」,於是把 Berkeley 市長請進他們那間「不怎麼樣」的辦公室(「因為 Berkeley 沒有好的辦公空間」)。市長帶了一大群人來,一群研究生對著一群政治人物**簡報進階排程演算法**,市長全程打瞌睡,最後醒過來握著手說了一句:

  > 「我希望有一天,每個家庭裡都有一塊 data brick。」

  兩人笑說這件事**至今還沒發生**——「不過也許 NVIDIA 最新的機櫃算是往那個方向走了一步」。

### 主題二:Berkeley 到底特別在哪裡?(約 01:42–01:44)

**Ali**:他來 Berkeley 之前做過多份博後,大致住過九個國家、走訪九所大學。他認為 Berkeley 這座城市和這所大學都特別,而特別之處是一種態度:**「你可以改變任何事、質疑任何事。」**

這對他一開始是文化衝擊:研究組在做的題目讓他覺得「這不算研究吧,我們不該做這個」,對方卻說「不,我們就是要做,這很酷,而且會有影響力」。他當時想「這說不通啊,這根本是在作弊吧」——但答案永遠是「我們什麼都能做,我們來這裡就是要改變世界」。

他也承認這種精神有時會走向極端,但那正是**光圈開得夠大**的代價:有超高影響力的研究,也有像「delay-tolerant networks」那種——因為「網際網路顯然是壞的,如果我們要做星際通訊,就得為星際通訊重新設計一套新的網際網路,畢竟我們終究要殖民整個宇宙」——當年網路組真的有這個研究題目。

**Andy 的補充故事**:早期他們是作業系統與分散式系統研究組,深受 BSD 啟發。後來成為 Mesos 的專案在命名時反覆掙扎,他提出的候選是 **BCD(Berkeley Cloud Distribution / Berkeley Cluster Distribution)**,直接致敬 BSD。Matei 和 Ben 都反對:「我們憑什麼狂妄到把自己命名成跟 BSD 只差一個編輯距離?」Andy 的回答是:「因為我們就是要做出更有影響力的那個作業系統啊。」他這一票沒贏。(順帶一提,當時官方命名體系是 **BDAS**,而且規定要唸成 "badass"。)

Ali 的結論:**那就是 Berkeley 精神——質疑既定規範。**

### 主題三:Databricks 為什麼一直做開源?MLflow 與 Omnigent(約 01:44–01:48)

**Ali 的策略觀**:開源標準與開源介面之所以重要,是因為它**創造社群,而社群會變得非常強大**。他講得很直白:

> 「如果沒有 Spark 生態系,Databricks 這家公司根本不會存在——因為那個生態系遠比我們任何人單獨能做出來的都要大。」

所以開源既對社群和世界好,**也是門好生意**,Databricks 已經證明過。

- **MLflow**:很多人不知道它至今**每個月仍有 4,000 萬次下載**。它誕生於機器學習時代(約十年前),當時大家迷戀「最好的模型」,但 ML 工程師很難迭代不同模型——他們需要某種類似 git 版本控制的方式來追蹤所有實驗。那就是 MLflow。
- **Omnigent**(今年夏天剛推出):問題意識是**現在的 harness 太多了**。Ali 給了一個很有意思的對照:

  **大型語言模型不黏著,harness 卻很黏著。** 因為 Databricks 同時服務專有模型與開源模型,他們手上有全部的資料,看到的現象是「**只要有新的專有模型或開源模型出來,人們在幾天之內就搬過去了**」。而在軟體業,任何其他東西都是黏的——你會一直用下去,即使流失也是緩慢衰減,不會瞬間全員倒戈。**LLM 是例外。** 但 harness 是建在 LLM 之上的,而它們**像舊軟體一樣把你鎖住**:你習慣了它的介面、記憶機制、快捷鍵。

  所以 Omnigent 的構想是一個 **meta harness——harness 的 harness**,讓你能自由切換:能接 Claude Code、能接 Codex、能接任何一個(OpenCode、Pi⋯),藉此取得多工復用與社群效應。

  成績:**推出後頭幾週就有 1,000 個 GitHub fork,數週內數百人貢獻。**

- **Ali 對開源的長線判斷**:開源在接下來幾年會因為 vibe coding / AI 而**大爆發**。過去要有一個 Linus Torvalds 花巨大心力寫出一整套作業系統去跟 Windows 競爭,而且總得有人付他薪水,所以最後他被公司雇用。**但今天寫軟體的成本正在下降**,所以會出現多得多的開源專案,並且成為標準。

### 主題四:規格 > 實作,以及「PR 裡放的是 prompt」(約 01:47–01:49)

**Andy 的預測**:他覺得我們會走到某種新版本的 GitHub——**pull request 裡裝的不是程式碼,而是 prompt**,而 reviewer 的工作是去跑那些 prompt。他認為 OpenClaw 之類的東西(可能還有 Spark)已經在往那個方向移動,committer 的工作變成判斷「這段程式碼有多少是人寫的、人在這個 PR 上花了多少小時」。

**Ali 的回應**:他確實認為方向是——**只要你能指定程式該做什麼,並且有測試地基與 harness,實作本身就不重要了**;AI 可以找出最快、最好的實作,而且可能重寫很多很多次。但這**要求你有一種極為滴水不漏的方式來指定程式碼**。

### 主題五:Databricks 自己做 eval:Office QA(約 01:49–01:52)

**Ali 說明他們最近公布的內部工作**:他們把公司內部的 coding issue 與任務大量爬下來,建了一個**超過一千題的大型資料集**。來源是——約 **4,000 名工程師**每天在寫程式,而**全公司約 11,000 人**會提出各種問題(例如資料科學問題、想知道業務狀況、在第一線工作時遇到的問題)。

**Andy 的解讀**:那基本上是一份**宣告式的規格**——你用這些問答把需求宣告出來了。人們問問題,你有 Databricks 的答案,現在你就有了一份「我們希望 agent 能回答這些」的規格,也就是**一份專屬於 Databricks 的評估 / benchmark**。

**Ali 為什麼要做**:一方面是**污染(contamination)問題**——每天都有東西發布,所以他們想要一個屬於自己的 ground truth,用來回答「我們該用哪個模型?能不能直接用 GLM 5.2?它會一樣好嗎?」

另一方面是他對前沿實驗室的觀察:

> 「前沿實驗室太執著於超級智慧、太執著於朝超級智慧前進,以至於**我們每天想做的很多事情根本不在他們的 eval 裡**。」

他舉的對照是 **HLE(Humanity's Last Exam)**——裡面是非常複雜的數學與物理題。但當 Databricks 去測「我們每天要做的很基本的任務」時,前沿模型表現並不好:**最難的那批大約只對 20%,平均難度的大約 40%。**

他的例句非常樸素:「這是 1940 年代美國的預算,請告訴我國防支出是多少。」模型得掃描 PDF、搞懂怎麼在四個維度上呈現資料。「結果那真的很難」——因為業界的焦點放在物理與數學這類**可以拿去做 RL 的東西**,而不是這些平凡的企業或商業任務。

於是他們做了一個叫 **Office QA** 的 eval(名字取自電影《Office Space》,就是那個 TPS report 的梗)。專注解這個問題之後,他們做出的 agent 能做 PDF parsing 之類的事,**正確率接近 80%**。

Ali 的結論:**eval 與 spec 在未來會極其重要。**

### 主題六:K Prize 與 Terminal-Bench 的起源(約 01:52–01:54)

**Andy 的線**:他們與 Stanford 教授 **Ludwig Schmidt** 合作——Schmidt 的團隊做過 CLIP 與 **DataComp** 系列。DataComp 的創新在於**把方向顛倒過來**:不是固定資料集去改模型,而是**固定模型與 agent、去改資料集**,並替此做一個排行榜,看改變資料集能把同一個 agent 的結果推到多高。

他和 Schmidt 在 NeurIPS 見面,而那正是他發布 **K Prize** 的那一屆 NeurIPS。K Prize 的規則:

- **100 萬美元**,他當場在台上發推承諾親自開支票。
- 給第一支在「**contamination-free 版本的 SWE-bench**」上達到 **90%** 的隊伍。
- 做法:設一個**投稿截止日**,參賽者必須在那之前交出 agent 程式碼;**截止後才去爬接下來四個月的新 GitHub issue**(來自 PyTorch、Spark 這類熱門 repo),再拿這些新題目去跑已經封存的 agent。這樣參賽者不可能在測試集上訓練。
- 結果:**成功率大約 10%**——Andy 說對一個全新 benchmark 來說這算相當好。

**Ali 的反應**(全場最好的一句對照):

> 「這不是很瘋狂嗎?所有東西都飽和在 90%,但你只要做一個新的,就變成 10%。」

### 主題七:benchmark 應該像軟體一樣做,而不是砍掉重練(約 01:54–01:57)

**Andy 的核心主張**(他說這是他們幾週前才發布的新工作):

現行做法是一個**非常沒效率的循環**——每做一個新 benchmark,基本上就把上一個丟掉、從零開始。他用自己的經驗當例證:

- 他們做了 Terminal-Bench 1,然後 2,然後 2.1。
- **從 2 到 2.1 的內容,主要就是修好五到十個被社群發現「其實無解」的任務。**
- 但大部分 benchmark 連這種小版本更新都不做。
- 結果產生了一種**影子文化**:「非常熟悉 Terminal-Bench 2 的人都知道,**83% 其實就等於 100%**」——因為剩下的是無解題。
- 「如果你是 benchmark 的作者,你不會想要這樣。**你要 100 分是拿得到的,只是非常難。**」

所以他的提案是:**benchmark 應該像寫軟體一樣**——你不會每次出新版 Spark 就把整個 codebase 丟掉,你是**在 codebase 上做修改、修 bug**。對應到 benchmark 就是:

1. **刪掉已飽和的舊任務**(現在大家都做對了,就不要再留在 benchmark 裡)。
2. **加入十個更難的新任務**。
3. **每兩三週就發一版**,持續更新——「就像軟體一樣,而且你在修 bug」。

Terminal-Bench 3 之後就會是 3.1、3.2、3.3,節奏很快、每次都是相對小的迭代更新。

**Ali 的加碼**:他喜歡這個做法的原因是 **Goodhart's law**——「任何你拿來評估的指標,一旦被用來評估就會被 game,從而失去它原本的目的。」這正是**所有東西都停在 90% 的原因**,而持續迭代的 benchmark 恰好能對抗這件事。

**Andy 再補一層**:這樣還能**溫和地引導方向**。例如 **reward hacking** 現在是前沿的主要議題之一——「一年前幾乎沒人在談 reward hacking,現在很多人在想圍繞它的新工具,agent 也越來越會識別它。」所以他們想要更多**對 reward hacking 有韌性的任務**,或**明確測試 agent 對 reward hacking 抵抗力的任務**;在新架構下,「兩週內想出三個新任務、切一個新版本」是做得到的。

### 主題八:人類該把腦力花在哪裡?(約 01:57–01:58)

**Andy** 把前面幾條線收攏成一個判斷,並明說他認同 Ali 稍早的說法:**只要你有好的 eval,agent 與 harness 的程式碼會越來越被自動優化。**

他描述的典範轉移是:

- **早期(LangChain / LangGraph 那類框架)**:人類花心力思考「怎麼把我的 agent 架構設計好」。
- **現在**:人類把全部腦力花在**設計評估**上——「你要怎麼精準捕捉你公司裡(或政府裡、或任何你想優化的對象裡)那些困難事情的分布?」然後**放出優化器去爬那個 eval**:程式碼優化器、prompt 優化器、模型權重優化器,或以上全部。

這兩個趨勢加起來,就是他和 Laude 的 Harbor 開源團隊現在投入最多心力的地方。

### 主題九:Open Frontier——開放科學還有機會嗎?(約 01:58–02:02)

**Ali 提問**:Open Frontier 是 Andy 他們投入大量資源在推的開放研究 / 開放科學倡議。面對那些薪資高得離譜、極度保密、不發表結果的封閉前沿實驗室,**開放這一側有機會嗎?**

**Andy 的回答**分成三段:

**(1) 現況診斷。** 他先謝謝 Ali 一個月前來那場會議演講——他們**集合了約一百位仍在做開放科學的頂尖 AI 研究者**,一起討論「我們所認識的科學的命運」。觀察到的核心事實是:許多頂尖人才正在離開學界,而且是兩件事同時發生——

- **薪資**:從 30–40 萬美元,跳到 1,000 萬到 1 億美元等級。
- **資源**:從一個獲得 1,000 萬到 5,000 萬美元經費的實驗室,跳到有數十億、數百億美元的實驗室。

他說即使以十年前創立 Databricks 的標準看,這都「絕對是瘋狂的」——現在有人拿到十億美元等級的薪酬包。這兩件事是他**真心憂慮科學前景**的原因。

**(2) 正面回答「能不能正面對決」:不能。** 非營利研究靠的是慈善捐贈與美國政府經費(包括他們此刻所在的這所大學),**永遠不可能募到跟 Anthropic 或 OpenAI 同一個量級的數千億**。

**(3) 但他們確實需要多募一到兩個數量級。** 而那需要一種**新的募資形態**,也需要一種**學界從來不需要有過的實驗室協作方式**——他稱之為「**lab of labs**」架構:

> 介於「學術實驗室現在的協作方式(基本上就是讀彼此的論文、在對方想法上疊加)」與「Meta / OpenAI / Anthropic 那種中央統一管理、全體聚焦單一 stack 與單一模型」之間——**一個較鬆散但仍然對齊的多實驗室協作體**。

他點名的拼圖:

| 方向 | 誰 | 單位 |
|------|-----|------|
| 評估 | **Harbor** | Laude |
| 預訓練 | **Marin**,Percy Liang 主持 | Stanford |
| Agentic 框架 | Graham Neubig | CMU |
| Prompt 優化與 contextualization | Matei Zaharia | Berkeley |
| 同上 | Omar Khattab | MIT |

再加上獨立研究者:他說**非營利現在正在爆發**——不是 Anthropic 那個量級,而是五人、十二人的小團隊,而且是**真正的非營利,不是 neolab、不是營利公司**。

他形容操作上的挑戰非常實際:「要想辦法把這群貓趕在一起,**第一步是先讓所有人的臉出現在同一張投影片上**,第二步才是真的把它運作起來——你們多久碰一次面?怎麼對 artifact 達成共識?怎麼把 Marin 產出的模型,或那些正在放出開放權重模型的實驗室(例如 Thinking Machines,或聲稱在做開放模型、最終會釋出的 Reflection)接起來?**怎麼在非營利的架構下讓整體大於部分之和?**」

**動能**:他們談這件事談了大約一年,而現在 **Satya Nadella 也發推談到需要這類東西**,加上 **Databricks 正在示範這種開放生態系確實有機會站得住**。Ali 回應說他對此非常興奮。

### 主題十:給 Berkeley 大學生的話——CS 還有希望嗎?(約 02:02–02:07)

**Andy 提問**:我們都在這裡教過、指導過大學生,也把一些人帶進 Databricks;你現在仍然雇用數百位工程師在做前沿基礎設施。**現在來 Berkeley 是不是沒希望了?** 他說自己做畢業致詞時,很多學生非常焦慮,家長事後跑來問「我們很困惑,到底該怎麼辦?」

**Ali 的回答(這場對談最長也最具說服力的一段)**:

他先描述那個他認為錯誤的氛圍——「尤其在前沿實驗室,有一種『只剩兩年工作可做,然後所有人都會失業、programming 會消失』的情緒,在 SF 越來越常遇到這種人。」

> 「我認為這是**完全錯的**。」

他的論點是**社會層面的變革本來就很慢**:

- **電力**:從 1880 到 1920,電動機取代蒸汽機,才真正在社會上收割到好處;而且**直到 1920 才在 GDP 上看到影響**。更關鍵的是——這不能推給「那是實體技術所以困難」,因為**電動機在 1840、1850 年代就已經存在了**。
- **PC 革命**:同樣花了很長時間。
- **他自己的公司**:Databricks 有 AI、正在盤點組織裡的每一件事,「你就會看到這有多難——你有太多在過去累積起來的任務;我們只存在 13 年,外面有些組織已經存在 50 年、100 年,**要改變你正在做的每一件事,要花非常非常久**」。

所以他判斷:**這場 agentic 革命至少會花十年,甚至更久。**

而且**好點子的產生本身也很慢**。他最喜歡的例子:**網際網路在 2000 年就已經存在了,但 Airbnb 的 Brian 要到 2009 年才想出那個點子**——比網路晚了十年甚至更久。而 Airbnb 不需要任何新的實體基礎設施:網路在了,人們手上有可以出租的房子,什麼都不缺。**只是想出好點子、讓它擴散滲透進社會,就是要花很長時間。**

> 「所以我認為,**最有意思的事情大多都還沒發生。**」

他點名兩個他常提的方向:

1. **醫療**:「會出現一家醫療公司,大概值好幾兆美元」——你能得到一位**看過數十億病患的醫生**,提供個人化的醫療照護。「如果能改善你和你所愛的人的健康,人們願意付出任何代價。」
2. **教育**:VC 過去總說教育賺不到錢,但他認為——「在美國,**選舉的輸贏就是靠教育**;人們非常在乎給孩子的教育。」而這項技術對教育是變革性的,所以會出現創新,可能來自大學、可能來自非營利,也會來自公司。

他的收束:

> 「這是有史以來最好的時代。我真希望我是現在才 20、25 歲出社會⋯⋯如果你是十年、二十年前出來,一切都比較平順。**這種大轉型的時刻,就是活著並參與其中最好的時候。**」

而對 CS 本身:「我認為 computer science 還有很長的路要走,而且**未來被寫出來的軟體會遠遠多於過去**。所以我超級樂觀。」

**Andy 的呼應**:他說自己「平行地樂觀」。他在 Laude 仍與 Berkeley、Stanford、MIT 等頂尖大學的實驗室合作、與博士生共事。他的觀察是:

**去找那些真的把東西 ship 出去的學生**——發布一個開源專案、把論文推文出去並得到大量回響的那種。跟他們談,你會發現**他們的動機是 impact**,和當年他們在 Patterson 的實驗室裡想著 BSD、想著怎麼改變世界時一模一樣。

他說他會直接問這些學生:**你為什麼要對那些兩百萬、五百萬、一千萬美元年薪的 offer 說不?** 那些位置能做前沿研究、能形塑 Claude 的運作方式,但**你不能對外談論它**。答案永遠是同一個——

> 「能去做你自己認定是那個關鍵願景的問題,並且承諾把它傳播給全世界,**最終的影響力比那張 1,000 萬或 5,000 萬美元的支票更大**;支票本身也代表著影響力,但它是一個**落後指標**。」

Ali 的最後回應:「說得好。是的,你在前沿實驗室能賺很多錢,**但你永遠不會有機會擁有那麼大的影響力**——因為就在這場轉型當中,假設正在改變、新想法可以綻放。**這就是該做那件事的時候。**」

### 金句

> "I hope that one day I will have a data brick in every home."(Berkeley 市長,Ali 轉述,約 01:42)

一位對排程演算法簡報全程打瞌睡的市長,醒來說出的一句話。「至今還沒發生。」

> "There's this kind of attitude that you can change anything, you can question anything."(Ali,約 01:42)

他認為 Berkeley 之所以是 Berkeley 的原因;初來乍到時對他是文化衝擊。

> "Anything else in software is sticky … With LLMs that is [not] the case."(Ali,約 01:46)

Databricks 同時服務專有與開源模型,資料顯示**新模型一出、人們幾天內就搬走**。但 harness 又把人黏住了——這正是 Omnigent 的問題意識。

> "Isn't it crazy that everything is 90% saturated, but when you do a new one it's like 10%?"(Ali,約 01:54)

K Prize 結果引出的一句,直指 benchmark 飽和的荒謬。

> "We should write benchmarks like software … you don't throw away the codebase every time you do a new version of Spark."(Andy,約 01:55)

整場最可操作的主張:刪掉飽和任務、加入更難的、每兩三週發一版。

> "People who knew Terminal-Bench 2 really well knew that 83% was actually 100%."(Andy,約 01:55)

無解任務造就的影子文化——benchmark 作者最不想要的東西。

> "Now instead you have your humans spending all their brain power coming up with the evaluation."(Andy,約 01:57)

從「人設計 agent 架構」到「人設計 eval、優化器去爬坡」的典範轉移。

> "The internet already existed by 2000, but it took Brian at Airbnb till 2009."(Ali,約 02:04)

用來說明**好點子本身就是瓶頸**——基礎設施到位不等於應用到位。

> "This is the best time to be alive and be part of it."(Ali,約 02:05)

他給焦慮的 Berkeley 學生與家長的答案。

> "You can make a lot of money at the frontier lab, but you'll never ever have the chance to have as much impact."(Ali,約 02:07)

對談結語;Andy 的版本是:那張支票也代表影響力,但它是**落後指標**。

## English Notes

### Who's talking

| Speaker | Role | Vantage point in this conversation |
|---------|------|------------------------------------|
| Ali Ghodsi | Co-Founder & CEO, Databricks; adjunct professor at UC Berkeley | Running a 13-year-old, 11,000-person company that is deploying AI on itself |
| Andy Konwinski | Co-Founder, Databricks; Perplexity; Laude Ventures | Building ecosystem infrastructure for benchmarks, evals and open science |

Moderator Aaron Jacobson (NEA) notes that NEA first backed Databricks at the Series B in 2014. Both came out of Berkeley's Mesos/Spark line: Ali was one of the creators of Apache Spark, with research in resource management, scheduling and data caching applied to Apache Mesos and Apache Hadoop; Andy did his CS PhD at Berkeley, contributed to Apache Hadoop and co-created Apache Mesos and Apache Spark, and now co-teaches a PhD seminar on research-to-startups at Berkeley.

### Theme 1: Berkeley in 2009, and the mayor who fell asleep (~01:38–01:42)

- **Andy's memory**: in 2009 an email went out — from Ion Stoica or Scott Shenker — to the Mesos group announcing a visitor joining the team. He, Matei Zaharia and Ben Hindman were "very insecure" and mostly wondering *who is this elite guy, and who's going to be first author now?* Then Ali walked in, jacked, and Andy thought: "I hope we don't have to arm wrestle for this first author." Ali went on to the **Dominant Resource Fairness (DRF)** paper and became a mentor and effectively one of Andy's co-advisors.
- **Ali's memory**: 2009–2012 Berkeley was "at the frontier of all these new algorithms for the new computer — and **the new computer was the data center**." There was a lot of skepticism at the time about AI, machine learning and data centers. He calls those his best and most formative years.
- **His favorite story**: early in Databricks' life there was a real debate — run the company out of Berkeley or San Francisco? The founders split down the middle. They met the chancellor, who told them to talk to the mayor, so they brought the mayor of Berkeley into their not-very-nice office ("because Berkeley doesn't have great office space"). He arrived with an entourage of politicians, and a group of researchers proceeded to **pitch them on advanced scheduling algorithms**. The mayor dozed through the whole talk, woke up at the end, shook a hand and said:

  > "I hope that one day I will have a data brick in every home."

  Both agree it still hasn't happened — "though maybe NVIDIA's most recent rack is where we go someday."

### Theme 2: What actually makes Berkeley special (~01:42–01:44)

**Ali**: before Berkeley he did several postdocs, living in roughly nine countries and visiting nine universities. Both the city and the university are special, and what makes UC Berkeley special is an attitude: **you can change anything, you can question anything.**

It was a culture shock. He'd look at what the group was working on and think "that's not research, we're not supposed to do that," and the answer would be "no, we're doing it, it's cool, it will have impact." He'd protest that it made no sense, that it felt like cheating somehow — and the answer was always "we can do anything, we're just here to change the world."

He admits it sometimes goes to extremes, but that's the cost of a **wide aperture**: alongside very high-impact work there was research on delay-tolerant networks, on the premise that "obviously the internet is broken if we want to do interplanetary communication, so we have to redesign a new internet for it, because eventually we're going to colonize all of the universe."

**Andy's companion story**: they were an operating-systems and distributed-systems group taking deep inspiration from BSD. When naming what became Mesos, his candidate was **BCD — Berkeley Cloud Distribution / Berkeley Cluster Distribution** — one edit distance from BSD. Matei and Ben both said no: "who are we to be so lofty as to name ourselves like only one edit distance from BSD?" Andy's answer: "well, we're going to build the more impactful operating system — that's who we are." He lost the vote. (The official nomenclature at the time was **BDAS**, which you were required to pronounce "badass.")

Ali's verdict: **that's the Berkeley spirit — question the norms.**

### Theme 3: Why Databricks keeps open-sourcing — MLflow and Omnigent (~01:44–01:48)

**Ali's strategic view**: open standards and open interfaces matter because they **create communities, and those communities become very powerful**. He puts it bluntly:

> "Databricks would not have existed as a company if it wasn't for the Spark ecosystem — because the Spark ecosystem was way bigger than anything any of us would have done."

So it's good for the community and the world, **and it's a good business idea** — Databricks has proven that out.

- **MLflow**: people don't realize it still does **40 million downloads a month**. It came from the ML era about ten years ago, when everyone was obsessed with having the best model but it was very hard for ML practitioners to iterate across models. They needed something like git version control to iterate and keep track of all the experiments. That was MLflow.
- **Omnigent** (launched this summer): the problem is that **there are simply too many harnesses**. Ali draws a sharp contrast:

  **LLMs are not sticky; harnesses are.** Because Databricks serves both proprietary and open-source models, they see all the data — and what they see is that **when a new proprietary or open-source model ships, people move to it within days**. "We've never seen anything like it. Anything else in software is sticky — you stick with it, there's a decay, people slowly churn and migrate, but it takes a while. You don't just instantaneously flip-flop. With LLMs that is the case." But harnesses get built on top of the models, and harnesses **lock you in like old software**: you get used to the interface, the memory, the keyboard shortcuts.

  So Omnigent is a **meta harness — a harness of harnesses** — that lets you switch freely: it works with Claude Code, with Codex, with any of them (OpenCode, Pi, you name it), giving you multiplexing plus the community.

  Traction: **1,000 GitHub forks in the first couple of weeks, and hundreds of contributors within weeks.**

- **Ali's long view on open source**: it's headed for a huge boon over the next several years thanks to vibe coding and AI. It used to take enormous effort for a Linus Torvalds to build a whole operating system and compete with Windows, and eventually someone has to pay his salary so he gets hired by a company. **But the cost of writing software is going down**, so expect many more open-source projects — and more of them becoming standards.

### Theme 4: Specs over implementations, and "PRs that contain prompts" (~01:47–01:49)

**Andy's prediction**: we're heading toward a version of GitHub where **pull requests contain prompts rather than code**, and reviewers decide by running those prompts. He thinks things like OpenClaw — and probably Spark — are already drifting that way, where a committer's job becomes judging how much of the code was written by a human and how many hours a human actually spent on the PR.

**Ali's response**: he agrees with the direction — **if you can specify what the program should do and you have the testing foundation and harnesses, the implementation doesn't matter**. The AI can find the fastest, best implementation, and may rewrite it many times over. But that **requires a really airtight way of specifying the code.**

### Theme 5: Databricks' own eval — Office QA (~01:49–01:52)

**Ali on the work they recently announced**: they scraped a large volume of their own internal coding issues and tasks into a **dataset of over a thousand items**. The source: roughly **4,000 engineers** writing code every day, and a company of about **11,000 people** submitting questions — data science questions, questions about how the business is doing, questions arising from working in the field.

**Andy's reading**: that's essentially a **declarative spec** — you've declaratively encoded requirements as questions and answers. People ask a question, you have the Databricks answer, and now you have a specification for something an agent could learn to do: "here's a bunch of questions we wish our agents could answer." A **bespoke evaluation / benchmark for Databricks.**

**Why Ali built it**: partly **contamination** — something new is released every day, so they wanted their own ground truth to answer "which model should we use, and can we just use GLM 5.2? Is it going to be as good or not?"

And partly an observation about the frontier labs:

> "The frontier labs are so obsessed with superintelligence and the march toward superintelligence that **many of the things we want to do every day are not part of their evals**."

His contrast is **HLE (Humanity's Last Exam)** — very complicated math and physics questions. But when Databricks tested the very basic tasks they do daily, frontier models weren't doing well: **around 20% correct on the hardest ones, maybe 40% on average ones.**

His example is deliberately mundane: "here is the 1940s budget of the United States — just get us what the defense spending was." The model has to scan the PDF and figure out how to present things across four dimensions. "It turns out that's really hard," because the focus has been on physics and math — **things you can RL** — rather than mundane enterprise or business tasks.

So they built an eval called **Office QA** (named after the movie *Office Space*, of TPS-report fame). Focusing on it, they built an agent that could do the PDF parsing and reached **close to 80% correctness**.

Ali's conclusion: **evals and specs are going to be extremely important going forward.**

### Theme 6: Where the K Prize and Terminal-Bench came from (~01:52–01:54)

**Andy's thread**: they teamed up with Stanford professor **Ludwig Schmidt**, whose group had done CLIP and the **DataComp** family of projects. DataComp's innovation was **inverting the usual setup**: instead of changing the model while holding the dataset fixed, you hold the model and agent fixed and change the dataset, with a leaderboard for how far a better dataset can push one fixed agent.

He met Schmidt at NeurIPS — the same NeurIPS where he launched the **K Prize**:

- **$1 million**, promised from the stage in a tweet, with Andy writing the check personally.
- To the first team to reach **90% on a contamination-free version of SWE-bench**.
- The mechanism: a **submission cutoff date** by which teams had to submit their agent code; **only afterward** did they scrape new GitHub issues from the four months following (from popular repos like PyTorch or Spark) and run the already-frozen agents against them. Training on the test set becomes impossible.
- The result: roughly a **10% success rate** — which Andy says is really good for a new benchmark.

**Ali's reaction**, the best contrast in the session:

> "Isn't it crazy that everything is 90% saturated, but when you do a new one it's like 10%?"

### Theme 7: Write benchmarks like software, don't start over (~01:54–01:57)

**Andy's central argument**, from work they announced a couple of weeks earlier:

Today's practice is a **very inefficient cycle** — every new benchmark mostly throws away the last one and starts from scratch. His own experience is the evidence:

- They shipped Terminal-Bench 1, then 2, then 2.1.
- **The whole of 2 → 2.1 was mostly fixing five to ten tasks the community had discovered were essentially unsolvable.**
- Most benchmarks don't even do those minor version releases.
- The result is a **shadow culture**: "people who knew Terminal-Bench 2 really well knew that **83% was actually 100%**," because the rest were unsolvable. "You don't want that if you're a benchmark maker. You want 100 to be achievable, but just be really hard."

His proposal: **write benchmarks like software.** You don't throw away the codebase every time you cut a new version of Spark; you change the codebase and fix bugs. Translated to benchmarks:

1. **Delete saturated tasks** — if everybody gets them right now, they don't belong in the benchmark.
2. **Add ten new, harder tasks.**
3. **Ship every two or three weeks**, continuously — "like software, and you're fixing bugs."

After Terminal-Bench 3 it'll be 3.1, 3.2, 3.3 — fast, relatively small iterative updates.

**Ali's addition**: what he likes about it is **Goodhart's law** — whatever metric you use to evaluate something ceases to serve its purpose because it gets gamed. That's exactly why everything sits at 90% everywhere, and a continuously updated benchmark is the natural defense.

**Andy, one layer further**: it also lets you **gently steer**. **Reward hacking** is now part of the major frontier — "very few people were talking about reward hacking a year ago; now a lot of people are thinking about new tooling around it, and agents are getting better at identifying it." So they want more tasks that are robust to reward hacking, or that explicitly test an agent's resilience to it — and under the new model, "we can come up with three new tasks and cut a new version of the benchmark in a week or two."

### Theme 8: Where humans should spend their brainpower (~01:57–01:58)

**Andy** pulls the threads together, explicitly endorsing Ali's earlier point: **as long as you have good evals, the agent and harness code will increasingly be optimized automatically.**

The paradigm shift he describes:

- **Early days (LangChain, LangGraph and similar frameworks)**: humans thinking hard about how to architect the agent.
- **Now**: humans spending all their brainpower on **designing the evaluation** — "how do you accurately capture the distribution of hard things inside your company, or your government, or whatever you're trying to optimize?" — and then **unleashing optimizers to hill-climb those evals**: code optimizers, prompt optimizers, model-weight optimizers, or all of the above.

Those two trends together are where he and Laude's **Harbor** open-source team are focused right now.

### Theme 9: Open Frontier — does open science stand a chance? (~01:58–02:02)

**Ali's question**: Open Frontier is an initiative Andy's team is spending a lot of money on, backing open research and open science. Against closed frontier labs with enormous salaries, deep secrecy and no published results — **does the open side have a chance?**

**Andy's answer, in three parts:**

**(1) The diagnosis.** He thanks Ali for speaking at the meeting a month earlier — they **assembled about a hundred of the top AI researchers still doing open science** to talk about the fate of science as we know it. The core observation is that top minds are leaving academia, and two things are happening at once:

- **Salaries**: from $300–400K to $10M–$100M.
- **Resources**: from a lab with $10–50M in funding to labs with billions and hundreds of billions.

He says this is insane even by the standards of founding Databricks ten years ago — people now have billion-dollar comp packages. Those two things are why he genuinely worries about the future of science.

**(2) Can they compete head-on? No.** Nonprofit research is funded by philanthropy and the US government — including the university they're sitting in — and **will never raise hundreds of billions at the level of an Anthropic or an OpenAI.**

**(3) But they do need one to two orders of magnitude more than they have now.** That requires a **new shape of fundraising**, and a way of teaming up that academic labs have never really needed — what he calls a **"lab of labs" architecture**:

> Somewhere between how academic labs collaborate today (mostly by reading each other's papers and building on the ideas) and how Meta, OpenAI and Anthropic operate (centrally run, laser-focused on one stack and one model) — **a looser but still aligned collaboration of many labs.**

The pieces he names:

| Direction | Who | Where |
|-----------|-----|-------|
| Evaluations | **Harbor** | Laude |
| Pre-training | **Marin**, led by Percy Liang | Stanford |
| Agentic frameworks | Graham Neubig | CMU |
| Prompt optimization and contextualization | Matei Zaharia | Berkeley |
| Same | Omar Khattab | MIT |

Plus independent researchers: nonprofits are **blowing up right now** — not at Anthropic scale, but five- or twelve-person teams, and **actual nonprofits, not neolabs, not for-profits.**

He's candid about the operational challenge: you have to herd those cats — "first of all get all their faces on one slide," and second actually operationalize it. How often do you meet? How do you agree on artifacts? How do you connect to the models Marin is producing, or to labs putting out open-weight models — Thinking Machines, or Reflection, which claims to be working on an open model and to be releasing one eventually? **How do you get the sum to be greater than the parts in a nonprofit?**

**Momentum**: they've been talking about this for about a year, and now **Satya Nadella has tweeted about the need for this sort of thing**, while **Databricks is showing the way for the possibility of this open ecosystem actually standing a chance.** Ali says he's very excited about it.

### Theme 10: What to tell Berkeley undergrads — is CS hopeless? (~02:02–02:07)

**Andy's question**: we've both taught and mentored undergrads here and brought some along to Databricks; you still pay hundreds of engineers to build frontier infrastructure. **Is it hopeless to come to Berkeley?** He gave the commencement speech here, students were deeply worried, and families came up afterward saying "we're confused — what should we do?"

**Ali's answer — the longest and most persuasive stretch of the conversation:**

He starts with the sentiment he thinks is wrong: "at the frontier labs in particular there's a sentiment that there's only two more years of work left and then everybody's going to be out of a job and programming is going to go away. You meet more and more people who feel that way, especially in SF."

> "I think this is completely wrong."

His argument is that societal change is intrinsically slow:

- **Electricity**: from 1880 to 1920 the electric engine replaced the steam engine before society could really reap the benefits, and it took until 1920 to see any impact on GDP. And you can't wave that away as "it was physical, so it was hard" — **the electric engine already existed in the 1840s and 1850s.**
- **The PC revolution**: same story, took a long time.
- **His own company**: Databricks has AI and is trying to identify everything it does across the organization — "you just see how hard it is. You have so many tasks that have built up. We've only existed for 13 years; some organizations have been around 50, 100 years. **It takes a very, very long time to change everything you're doing.**"

So: **the agentic revolution will take a decade at least, if not more.**

And **coming up with good ideas is itself slow**. His favorite example: **the internet already existed by 2000, but it took Brian at Airbnb until 2009** — ten years or more after the internet, with no physical infrastructure needed; people already had houses they could rent. **It just takes a long time to come up with good ideas and for them to percolate and disseminate through society.**

> "Most of the interesting things that are going to happen haven't happened yet."

Two directions he keeps returning to:

1. **Healthcare**: "there's going to be a healthcare company, and it's probably going to be worth trillions of dollars" — where you get **a doctor that has seen billions of patients** and can give you personalized care. "People would be willing to pay anything for that, if you could help the health of you and your loved ones."
2. **Education**: VCs have always said there's no money in education, but "if you look at the United States, **elections are won and lost based on education**, and people care about the education they give their kids." The technology is transformative here, so expect innovation from universities, nonprofits and companies alike.

His close:

> "This is the best time ever. I wish I was born so I would have come out now when I'm 20, 25 … If you came out 10 or 20 years ago, things are more smooth. **This big transformation is the best time to be alive and be part of it.**"

And on CS itself: computer science has far to go, and **we're going to see way more software written in the future than we've seen in the past.** "So I'm super, super optimistic."

**Andy's echo**: he's "very parallelly optimistic." At Laude he still works with PhDs in partnership with labs at Berkeley, Stanford, MIT and other top universities. His observation:

**Find the students who ship something** — launch an open-source project, tweet a paper and get a large response. Talk to those students and you find **they're motivated by impact**, exactly the way he and Ali were back in the Patterson labs thinking about BSD and how they could change the world.

He asks them directly: **why say no to those $2M, $5M or $10M-a-year comp packages?** Those roles let you do frontier research and shape how Claude works — **but you won't be able to talk about it.** The answer is always the same:

> "Getting to work on the problem you see as the visionary one, and a commitment to disseminating that to the whole world, is more impactful in the end — even than the proxy that this $10 million or $50 million check represents. That's also representing impact, but it's kind of a **lagging indicator**."

Ali's final word: "Yes, you can make a lot of money at the frontier lab, **but you'll never ever have the chance to have as much impact** — because during this transformation you can do things where assumptions are changing and new ideas can flourish. **This is the time to do that.**"

### Quotes

> "I hope that one day I will have a data brick in every home." (the mayor of Berkeley, as told by Ali, ~01:42)

Said by a mayor who had slept through the entire pitch on scheduling algorithms. "Still hasn't happened."

> "There's this kind of attitude that you can change anything, you can question anything." (Ali, ~01:42)

His explanation of what makes Berkeley Berkeley — and a culture shock when he first arrived.

> "Anything else in software is sticky … With LLMs that is [not] the case." (Ali, ~01:46)

Databricks serves both proprietary and open models and sees the data: **people move within days of a new release.** But harnesses lock you in — which is exactly the problem Omnigent targets.

> "Isn't it crazy that everything is 90% saturated, but when you do a new one it's like 10%?" (Ali, ~01:54)

Prompted by the K Prize result; the absurdity of benchmark saturation in one line.

> "We should write benchmarks like software … you don't throw away the codebase every time you do a new version of Spark." (Andy, ~01:55)

The most actionable claim of the session: delete saturated tasks, add harder ones, ship every two or three weeks.

> "People who knew Terminal-Bench 2 really well knew that 83% was actually 100%." (Andy, ~01:55)

The shadow culture unsolvable tasks create — the last thing a benchmark author wants.

> "Now instead you have your humans spending all their brain power coming up with the evaluation." (Andy, ~01:57)

The shift from humans architecting agents to humans writing evals while optimizers hill-climb them.

> "The internet already existed by 2000, but it took Brian at Airbnb till 2009." (Ali, ~02:04)

Why **ideas** are the bottleneck, not infrastructure.

> "This is the best time to be alive and be part of it." (Ali, ~02:05)

His answer to the anxious Berkeley students and their families.

> "You can make a lot of money at the frontier lab, but you'll never ever have the chance to have as much impact." (Ali, ~02:07)

The closing exchange; Andy's version is that the check also represents impact — but as a lagging indicator.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Omnigent | Databricks 開源的 meta harness(harness 的 harness),可組合、治理、共享 agent | Databricks' open-source meta-harness for composing, governing and sharing agents | 支援 Claude Code、Codex、Cursor、OpenCode、Pi 與自寫 agent;Apache 2.0;推出頭幾週 1,000 forks / works with Claude Code, Codex, Cursor, OpenCode, Pi and custom agents; Apache 2.0; ~1,000 forks in the first weeks |
| MLflow | Databricks 開源的 ML 實驗追蹤工具,類似 git 版本控制的實驗迭代方式 | Databricks' open-source ML experiment tracking — git-like version control for model iteration | 講者稱每月仍有 4,000 萬次下載 / he cites 40M downloads a month |
| Apache Spark / Mesos / Hadoop | 兩人共同的 Berkeley 研究根源;Databricks 因 Spark 生態系而存在 | Their shared Berkeley research lineage; Databricks exists because of the Spark ecosystem | Mesos 差點被命名為 BCD / Mesos was nearly named BCD |
| Office QA | Databricks 自建的內部 eval,聚焦「平凡但每天要做」的企業任務 | Databricks' in-house eval focused on mundane everyday enterprise tasks | 名稱源自電影《Office Space》的 TPS report 梗;他們的 agent 達到接近 80% / named after Office Space's TPS reports; their agent reached ~80% |
| Harbor | Laude Institute 的開源 agentic 評估框架 / test runner | Laude Institute's open-source framework for running agentic evaluations and RL rollouts | Terminal-Bench 2.0 建在其上 / Terminal-Bench 2.0 is built on it |
| Terminal-Bench | Stanford × Laude 主導的終端環境 agent benchmark,版本迭代到 2.1 | Stanford × Laude agent benchmark for containerized terminal environments; iterated through 2.1 | 後繼者 Frontier-Bench(原 Terminal-Bench 3.0)採「像軟體一樣持續發版」的做法 / successor Frontier-Bench (formerly Terminal-Bench 3.0) adopts the ship-like-software model |
| K Prize | Andy 個人出資 100 萬美元的獎金,授予首支在 contamination-free SWE-bench 達 90% 的隊伍 | Andy's personally funded $1M prize for the first team to hit 90% on a contamination-free SWE-bench | NeurIPS 台上發推承諾;首輪成功率約 10% / promised in a tweet from the NeurIPS stage; first round yielded ~10% |
| DataComp | Ludwig Schmidt 團隊的 benchmark:固定模型、改變資料集 | Ludwig Schmidt's benchmark family: hold the model fixed, change the dataset | 與 CLIP 同一團隊 / same group as CLIP |
| Open Frontier | Laude Institute 召集的開放科學倡議,2026/6/30 於舊金山集合約 100 位研究者 | Laude Institute's open-science initiative; ~100 researchers convened in San Francisco on 30 June 2026 | Ali 曾在該場演講 / Ali spoke at the meeting |
| Marin | Stanford 的開放預訓練專案,Percy Liang 主持 | Stanford's open pre-training project, led by Percy Liang | Andy 舉為「lab of labs」的一塊拼圖 / cited as a piece of the "lab of labs" |
| HLE (Humanity's Last Exam) | 高難度數理 benchmark,Ali 用作「前沿實驗室關注點」的對照 | Hard math/physics benchmark, used as his contrast for what frontier labs optimize | |
| Laude Institute | Andy 創立的非營利,以 1 億美元支持大學研究者把成果開源化 | Andy's nonprofit, self-funded with $100M to help university researchers ship open research | 議程列其身分為 Laude Ventures / the agenda lists him under Laude Ventures |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Ali Godsey / Ghazi | Ali Ghodsi |
| Andy Kowinsky | Andy Konwinski |
| Yan / Scott Shanker | Ion Stoica / Scott Shenker |
| Mate / Mate Zaharia | Matei Zaharia |
| Ben | Ben Hindman |
| Messos | Mesos |
| dominant research resource fairness | Dominant Resource Fairness (DRF) |
| Data Bricks / data bicks / databicks | Databricks |
| Omniant / Omnigent and | Omnigent |
| Nurips / Nurups | NeurIPS |
| Commons key prize | K Prize |
| Swebench | SWE-bench |
| terminal bench | Terminal-Bench |
| Ludick Schmidt / Ludig / Ludwig | Ludwig Schmidt |
| data comp | DataComp |
| Percy Lang | Percy Liang |
| Graham Nubic | Graham Neubig |
| Omar Katab | Omar Khattab |
| good heart's law | Goodhart's law |
| Sat Nadella | Satya Nadella |
| LD / at LA | Laude |
| open claw | OpenClaw |
| pi | Pi(harness 名稱 / harness name) |
| lang chain / lang graph | LangChain / LangGraph |
| BDAS | BDAS(Berkeley Data Analytics Stack,唸作 "badass") |
| office QA / office(the movie) | Office QA(名稱源自《Office Space》/ named after *Office Space*) |
| Reflections | Reflection |

## 待確認 / To Verify

- **「GLM 52」** 的正確型號(推測是 GLM-5.2,但逐字稿無法確認),不做臆測。/ The model heard as "GLM 52" — probably GLM-5.2, but not confirmed; deliberately not guessed.
- **Office QA** 是否為 Databricks 對外公布的正式 benchmark 名稱、以及是否有公開連結。/ Whether "Office QA" is the public name of the Databricks benchmark and whether a public link exists.
- **MLflow 下載量**:講者說「每月 4,000 萬次下載」,又說「一年數十億次」——兩者在算術上不一致(4,000 萬 × 12 ≈ 4.8 億),以口述原文記錄,實際數字待查。/ He says 40M downloads a month and also "billions a year"; those don't reconcile (40M × 12 ≈ 480M). Recorded as spoken; actual figure needs checking.
- **「我們幾週前才發布」的新 benchmark 專案**:依內容應指 Terminal-Bench 的後繼者 Frontier-Bench(原 Terminal-Bench 3.0),但講者未在對談中點名,故不寫死。/ The "announced a couple of weeks ago" project appears to be Frontier-Bench (formerly Terminal-Bench 3.0), but he never names it on stage, so it is not asserted.
- **Reflection / Thinking Machines 的開放權重模型計畫**:講者用的措辭是 "claims to be working on"、"eventually soon",屬轉述而非事實陳述。/ His wording is "claims to be working on … eventually soon" — reported speech, not a factual claim.
- **Andy 的機構歸屬**:逐字稿聽到的是 "LD"/"LA",對應 Laude;議程列為 Laude Ventures,而 Harbor 與 Open Frontier 是 Laude Institute(非營利)的專案,兩者的分工待確認。/ The transcript's "LD"/"LA" maps to Laude; the agenda lists Laude Ventures, while Harbor and Open Frontier are Laude Institute (nonprofit) efforts — the split between the two entities is unverified.
- **Databricks 內部資料集規模**:講者只說「超過一千題」,精確數字與公開發布狀態待確認。/ He only says "over a thousand"; the exact size and public release status are unverified.
- **K Prize 首輪約 10% 成功率**的官方結果頁面連結。/ Official results page for the K Prize's ~10% first-round success rate.
