---
title: "Combining Experiments, Large Language Models, and Theory to Discover Quantum Materials"
title_zh: "結合實驗、大型語言模型與理論來發現量子材料"
speaker: "Ekin Dogus Cubuk"
affiliation: "Co-Founder, Periodic Labs"
type: talk
stage: Plenary
date: 2026-08-02
session: "Session 2: Frontier Research"
video: "https://www.youtube.com/watch?v=I2PosBXwoPI&t=1997s"
video_range: "00:33:17–00:42:43"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [ai-for-science, materials-discovery, superconductivity, autonomous-labs, scientific-method]
---

# 結合實驗、大型語言模型與理論來發現量子材料(Combining Experiments, Large Language Models, and Theory to Discover Quantum Materials)

**一句話總結**:再強的 AI 也沒辦法「純靠想」想出下一個科學突破,因為宇宙太複雜了——超導的整部歷史都在說同一件事;所以正確的問題不是「AGI 能不能 zero-shot 突破」,而是「怎麼把 agent 塞進那套已經用了幾百年的科學方法裡」。
**One-line summary**: No amount of intelligence can think its way to the next scientific breakthrough — the universe is too complex, and the entire history of superconductivity says so. The right question isn't whether AGI can zero-shot a discovery, but where agents belong inside the scientific method we've used for centuries.

## 中文筆記

### TL;DR

- **他要回答的問題**:今天或未來的 AI 能不能直接 **zero-shot** 出下一個重大科學突破?之所以必須是 zero-shot,是因為**突破就定義而言不可能在訓練資料裡**。
- **他的答案是「不能」**,而反面就是他所謂的 **thinkism**:把你(或 AGI、或一群 agent)關在一間堆滿教科書、論文、專利的房間裡拼命想。宇宙太複雜,任何智慧都想不出來。
- **超導史就是證據**:1911 年的超導、MgB2、1986 年的銅氧化物高溫超導——**三次都不是從理論推導出來的**,而是新能力、大量試誤,或根本找錯目標時撞上的。
- **所以 agent 不是沒用,而是要放對位置**:把 AI 插進「觀察 → 假說 → 實驗 → 結果 → 理解失敗 → 再試」這個既有迴圈的各個環節——模擬(force fields)、characterization、文獻搜尋、實驗設計(DOE)。
- **給科學學生的建議正好相反於「AI 要取代科學家」的敘事**:去把**基本功**練到最扎實,並投入實驗方法與量測工具的創新——你造出新的量測方法,AI 才有更多資料可看,thinkism 那部分技能才發揮得出來。

### 重點整理

#### 問題設定:AGI 能 zero-shot 一個突破嗎?(約 00:34–00:35)

他開場先把問題釘死:**breakthrough 依定義不可能在訓練集裡**,所以它必須在「沒有先例示範」的情況下做出來——也就是 zero-shot。

換個問法就是:**thinkism 能不能推進物理學?** 所謂 thinkism,是「你把自己鎖在一個房間裡,手上有這個領域所有的教科書、所有做過的實驗、論文、專利,然後你非常非常努力地想」——不管想的人是人類、是 AGI、還是一整群 agent。

他的答案很直接:**不能。因為宇宙對任何智慧來說都太複雜了,沒有誰能靠想的方式想進一個科學進展裡。** 那替代方案是什麼?就是人類做了幾百年的事——**跟宇宙迭代**:提出假說 → 試 → 第一次通常不成 → 從失敗學到東西 → 再試。

#### 超導史:三次突破,沒有一次來自「想得夠努力」(約 00:35–00:39)

**1911,超導的發現。** 不是某個天才想通了「把汞降到夠低的溫度,電子會透過聲子感受到吸引力」。實際發生的是:**Kamerlingh Onnes 的實驗室先造出一個新能力**——把溫度降到史上任何紀錄之下(大約 4 K,最低做到 1.8 K)——而汞剛好在 4 K 就會超導。而且這還是主線任務(液化氦)的**副產品**。幾年後他拿了諾貝爾獎,但**很重要的一點:諾貝爾獎不是頒給超導的發現,是頒給他能液化氦。**

**1957/58,BCS 理論。** John Bardeen 與合作者搞懂了傳統超導的理論。照理說,人類既然懂了機制,就該用它推導出一堆新超導體——**但歷史不是這樣走的**。從 1958 到 2000 年左右,傳統超導最大的進展(用深度學習的語言說就是當時的 SOTA)是 **MgB2**;而它的發現方式是**試了幾萬種材料,剛好那一種是很好的 BCS 超導體**,不是有人拿著理論想出來的。

**1986,銅氧化物(cuprates)。** Karl Alexander Müller 與合作者找到第一個高溫、非傳統超導體。但**你去看他的諾貝爾獎演說就會發現,他當時其實是在找傳統超導體**——因為他根本還不知道「非傳統超導體」會長什麼樣子。

他把範圍講清楚:這個結論適用於**材料科學、化學、固態物理這類複雜系統**,**不包含數學與理論計算機科學**(他認為那是另一個 regime)。在複雜系統這一邊,**大多數東西是靠意外或大量試誤找到的**。

#### 那 agent 要放在哪裡?(約 00:39–00:41)

他的結論不是悲觀:**我們沒事,只要想清楚怎麼把 agent 用進那套已經用了幾百年的科學方法裡就好。**

科學方法的骨架是:觀察 → 假說 → 用實驗檢驗 → 看結果 → 第一次通常不太行 → 理解為什麼失敗 → 再試一次。而 AI 可以插進不只一個位置:

- **模擬**(迴圈正中央)——**已經被機器學習徹底改寫了**。今天大家用 force fields 來近似基態的量子力學;他說得很重:**就算再來一次 AI winter,他也無法想像 force fields 還會回到不用機器學習的時代。** AlphaFold 是另一個例子。但他也提醒:**force fields、AlphaFold 都是工具**,它們不會直接給你下一個新藥或下一個超導體。
- **Characterization(表徵分析)**——幫你看懂實驗資料到底發生了什麼。很技術,但 AI 能大幅自動化與放大規模。他順帶提到 **Berkeley 這邊已經有前沿工作**,用機械手臂在實驗室裡大量嘗試粉末合成。
- **文獻搜尋**——把所有論文讀過,找出還有哪些想法值得試。
- **DOE(design of experiment,實驗設計)**——根據目前為止的所有實驗,決定下一個實驗做什麼。

他補了一句誠實話:實際上沒有投影片畫得那麼乾淨,**真實情況是一張所有環節互相糾纏的 spaghetti plot**;但只要**刻意而謹慎地**把 AI 放進去,整套科學方法確實會加速。

#### 給科學學生的話(約 00:41–00:42)

**看到 LLM 的進展不該覺得沮喪,應該覺得相反——現在是做科學最令人興奮的時候。**

他的具體建議是:**把基本功練透。** 物理的就去讀超導理論、固態化學;生物的就去搞懂生物學裡真正重要的東西。並且特別重視**實驗**——因為回頭看,**很多重大進展都發生在有人做出新的實驗方法、新技術、新量測工具的時候**,而這些都是你能貢獻的。

而且這是正向循環:**你創造出新的實驗方法與工具,AI 就會看到更多資料**,它那套 thinkism 的技能就能用更大的規模、更快地把資料變成理解,然後你的下一個實驗就更有機會成功、也更聰明。

### 金句

> "The universe is too complex for any intelligence, whether it's humans or machines, to think their way into the scientific advance."(約 00:35)

全場的核心論點。

> "Nobel Prize was not given to superconductor discovery — it was given to the fact that he could liquefy helium."(約 00:37)

Kamerlingh Onnes 的獎座在「新能力」上,不在「新發現」上;這正是他想說的因果方向。

> "He was actually trying to find a conventional superconductor, because he didn't even know what an unconventional superconductor would be."(約 00:38)

高溫超導的發現者,是在找別的東西的時候撞上它的。

> "This universe is too complex for thinkism alone to innovate."(約 00:41)

最後一張投影片。

## English Notes

### TL;DR

- **The question**: can today's (or tomorrow's) AI **zero-shot** the next big scientific breakthrough? It has to be zero-shot, because a breakthrough by definition cannot be in the training set.
- **His answer is no** — and the position he's arguing against is what he calls **thinkism**: locking yourself (or an AGI, or a swarm of agents) in a room with every textbook, paper and patent in the field and thinking very hard.
- **The history of superconductivity is the evidence.** The 1911 discovery, MgB2, and the 1986 cuprates were each found by building a new capability, by brute-force trial and error, or by looking for something else entirely — never by deriving from theory.
- **So agents aren't useless — they belong in specific slots** of the loop scientists have used for centuries: simulation (ML force fields), characterization, literature search, and design of experiments.
- **His advice to science students inverts the doom narrative**: go deep on fundamentals and on experimental methods and measurement tools. New instruments create new data, and only then does AI's thinkism skill have something to work with.

### Key Points

#### Framing: can AGI zero-shot a breakthrough? (~00:34–00:35)

He pins the question down immediately: a breakthrough can't be in the training set, so it has to be produced without a previous demonstration — zero-shot by construction.

Restated: **can thinkism ever be enough for advancing physics?** Thinkism being the idea that you lock yourself in a room with all the textbooks, all the previous experiments, papers and patents in the field, and think really hard — whether you're a human, an AGI, or a bunch of agents.

His answer: no, because the universe is too complex for any intelligence to think its way into a scientific advance. The alternative is what we've done for centuries — **iterate with the universe**: hypothesis, attempt, failure, learn from the failure, try again.

#### Three superconductivity breakthroughs, none from thinking harder (~00:35–00:39)

**1911, the discovery itself.** Nobody reasoned their way to "cool mercury far enough and electrons will feel an attractive force through phonons." What happened is that **Kamerlingh Onnes's lab built a new capability** — cooling below any temperature previously recorded, around 4 K, eventually reaching 1.8 K — and mercury happens to superconduct at 4 K. It was a side project of the main effort, which was liquefying helium. Onnes won a Nobel a few years later, and Cubuk underlines the detail that matters: **the Nobel was not for superconductivity, it was for liquefying helium.**

**1957/58, BCS theory.** Bardeen and collaborators explained conventional superconductivity. In principle, humans could then use that understanding to find many more superconductors — but that isn't what happened. From 1958 to roughly 2000, the biggest advance in conventional superconductivity (the SOTA, in deep-learning language) was **MgB2**, and it was found by trying tens of thousands of materials until one turned out to be an excellent BCS superconductor.

**1986, the cuprates.** Karl Alexander Müller and a collaborator found the first high-temperature, unconventional superconductor. But read his Nobel lecture and you discover **he was actually looking for a conventional superconductor**, because he had no concept of what an unconventional one would even be.

He scopes the claim carefully: this holds for complex systems — materials science, chemistry, solid-state physics — and explicitly **not** for math and theoretical computer science, which he considers a different regime. On the complex-systems side, most things were found by accident or by intelligent trial and error.

#### Where the agents go (~00:39–00:41)

His conclusion isn't pessimistic: we're fine, we just have to work out how to use agents inside the scientific method we already have.

The loop is: observations → hypothesis → experiment → result → (it probably didn't work) → understand why it failed → try again. AI slots into several places at once:

- **Simulation**, in the middle of the loop, has already been completely rewritten by machine learning. Force fields approximate the ground-state quantum mechanics, and he puts it strongly: **even if another AI winter arrived, he can't imagine ever going back to force fields without machine learning.** AlphaFold is the other example. But he flags the limit — force fields and AlphaFold are *tools*; they don't hand you the next drug or the next superconductor.
- **Characterization**: making sense of what the experiment actually produced. Technical, but exactly the kind of thing AI can automate and scale. He notes that Berkeley has produced frontier work here, using robotic arms to try many powder syntheses in the lab.
- **Literature search**: reading everything and surfacing which ideas are worth trying next.
- **Design of experiments**: given everything measured so far, choosing the next experiment.

The honest caveat: it's never as clean as the slide. Reality is a spaghetti plot where everything interacts with everything else — but you can still see the whole method accelerate if AI is inserted deliberately and carefully.

#### Advice to science students (~00:41–00:42)

Don't look at LLM progress and get discouraged; conclude the opposite. It's an exciting time to do science.

His concrete advice: **go all-in on the fundamentals.** If you're a physicist, study the theory of superconductivity and solid-state chemistry; if you're a biologist, learn what actually matters in biology. And take experimentation seriously, because a lot of historical progress came from someone inventing a new experimental method, technique, or measurement tool — all of which you can still contribute to.

The loop closes on itself: as you create new experimental methods and tools, AI sees more data, applies its thinkism skill to make sense of it faster and at larger scale, and your next experiment gets both more successful and more intelligent.

### Quotes

> "The universe is too complex for any intelligence, whether it's humans or machines, to think their way into the scientific advance." (~00:35)

The thesis of the talk.

> "Nobel Prize was not given to superconductor discovery — it was given to the fact that he could liquefy helium." (~00:37)

The prize went to the new capability, not the discovery it enabled — which is exactly the causal direction he's arguing for.

> "He was actually trying to find a conventional superconductor, because he didn't even know what an unconventional superconductor would be." (~00:38)

> "This universe is too complex for thinkism alone to innovate." (~00:41)

His closing slide.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Periodic Labs | 他與 Liam Fedus 共同創辦,結合模擬、實驗與 LLM 加速實體 R&D,以高溫超導為 north star | Co-founded with Liam Fedus; combines simulation, experiments and LLMs to accelerate physical R&D, with high-Tc superconductivity as a north star | 官網議程職稱為 Co-Founder;他自稱 co-CEO and co-founder |
| GNoME | 他在 Google Brain / DeepMind 帶的材料發現工作,發現超過 200 萬種新晶體 | The materials-discovery work he led at Google Brain / DeepMind; over 2 million new crystals | 主持人介紹時提到 / from the moderator's intro |
| AlphaFold | 他舉的「機器學習改寫科學工具」的第二個例子 | His second example of ML rewriting a scientific tool | 他強調它是工具,不是發現本身 / a tool, not the discovery |
| ML force fields | 近似基態量子力學的模擬工具,已被機器學習永久改寫 | Simulation tools approximating ground-state quantum mechanics, permanently changed by ML | panel 中補充:近十年因 graph neural networks 而改變(約 01:02) |
| MgB2（magnesium diboride） | 1958–2000 間傳統超導最大的進展,靠試遍數萬種材料找到 | The biggest conventional-superconductivity advance between 1958 and 2000, found by screening tens of thousands of materials | |
| Cuprates | 1986 年第一個高溫(非傳統)超導體 | The first high-temperature (unconventional) superconductors, 1986 | Karl Alexander Müller 等人 |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Do Chubuk / Dos / Do / D / Josh | Ekin Doğuş Çubuk（Doğuş) |
| Gnome | GNoME |
| Liam Fetis | Liam Fedus |
| Camelang Anes / Anest's lab / an | (Heike) Kamerlingh Onnes |
| John Bardin | John Bardeen |
| BCA superconductivity | BCS superconductivity |
| magnesium dyoride, MGB2 | magnesium diboride, MgB2 |
| coupe rates | cuprates |
| Alex Mueller | (Karl) Alexander Müller |
| phonance | phonons |
| the soda（in deep learning language) | the SOTA |
| DOE design of experiment | design of experiments (DoE) |
| supercondiv conductivity / superc conductivity | superconductivity |

## 待確認 / To Verify

- 他說 BCS 理論是「around 1958」,學界通用年份是 **1957**(Bardeen–Cooper–Schrieffer)。/ He dates BCS to "around 1958"; the standard date is 1957.
- **MgB2 的超導性發現年份**他未明說(只說 1958–2000 這段區間),實際是 2001 年由日本團隊報告——與他的敘述略有出入,值得對照投影片。/ He doesn't date the MgB2 discovery; it was reported in 2001, slightly outside the 1958–2000 window he draws. Worth checking the slide.
- 他提到「Berkeley 這邊用機械手臂做粉末合成」的前沿工作但未指名,推測是 LBNL 的 A-Lab,待確認。/ The Berkeley robotic-arm powder-synthesis work is unnamed on stage — likely LBNL's A-Lab, but unconfirmed.
- GNoME「超過 200 萬種新晶體」的數字出自主持人介紹,非講者本人。/ The "over 2 million crystals" figure comes from the moderator, not the speaker.
- Kamerlingh Onnes 實驗室的降溫數字(約 4 K、最低 1.8 K)以逐字稿為準,未與文獻核對。/ The cooling figures (~4 K, down to 1.8 K) are as spoken, not cross-checked against sources.
