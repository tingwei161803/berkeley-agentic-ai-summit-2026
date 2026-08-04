---
title: "End-to-End Security Research with a Language Model"
title_zh: "用語言模型做端到端的資安研究"
speaker: "Milad Nasr"
affiliation: "Research Scientist, Anthropic"
type: talk
stage: Nexus
date: 2026-08-01
session: "Session 4: Secure Agentic AI"
video: "https://www.youtube.com/watch?v=ZIRc3EpzQJs&t=10861s"
video_range: "03:01:01–03:13:58"
transcript: "tmp/[English (auto-generated)] Nexus Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [security, cryptanalysis, research-automation, anthropic, evaluation]
---

# 用語言模型做端到端的資安研究(End-to-End Security Research with a Language Model)

**一句話總結**:兩年前一群前沿實驗室研究者預測「AI 做端到端研究要十年以上」,而講者用一篇本週剛發表的 7-round AES 密碼分析論文說明——這個預測錯得最離譜的不是編碼能力,而是研究能力;而且新的瓶頸已經從「想不想得到點子」變成「驗證得完不完」。
**One-line summary**: Two years ago a room of frontier-lab researchers predicted end-to-end AI research was more than a decade away; Nasr used a 7-round AES cryptanalysis paper published that same week to argue the prediction was most wrong about *research*, not coding — and that the bottleneck has moved from generating ideas to verifying results.

## 中文筆記

### TL;DR

- **預測與現實**:兩年前一群前沿實驗室研究者估計「agent 做超過 90% 編碼」最快 2–5 年、平均 5 年以上;「agent 做超過 90% 的一般性研究」則要 10 年以上。編碼的預測有點錯,**研究的預測錯得非常離譜**。
- **證據是一篇本週發表的密碼分析論文**:模型在 **7-round(簡化版)AES** 上找到新攻擊,把最佳複雜度從 2013 年的 **2^99** 降到 **約 2^89**,實測快 200–800 倍。**他強調:AES 本身沒有被破解**——真被破就是網際網路被破;這是學術性的簡化版本結果。同樣手法也用在 **HAWK**(後量子演算法)與 **LEA** 上。
- **典範轉移的方向與新瓶頸**:人類的做法是想幾週、找人討論、再實作;模型的做法是**產生大量點子並把每一個都實作出來試**。「ideas are cheap, execution is everything」可能要反過來了。實際數字:從一句「go beat AES」出發,模型產出**超過 3,000 個點子**,其中 2,000 多個真的適用、約 200 個具新穎性,**最後只有 4 個進了論文**。而現在**團隊大部分時間花在驗證結果上**。

### 重點整理

#### 兩年前的那兩個問題(約 03:01–03:04)

大約兩年前,他在一場類似的活動上和一群來自頂尖前沿實驗室的研究者做了一件研究者常做的事:預測未來。當時有兩個問題:

1. **還要多久,LLM 與 agent 能做掉我們超過 90% 的編碼工作?**——最樂觀的估計是 2 到 5 年,平均值超過 5 年。
2. **還要多久,agent 能做掉我們超過 90% 的一般性研究?**——超過 10 年。

他的評語是:編碼那題「我們錯了,但也許沒錯太多」;**研究那題,我們可能錯得非常、非常離譜**。

他也先把定義釘死。他說的「用 LLM 做研究」**不是把 LLM 當工具**——許多會議、包括作風非常保守的資安會議,如今都在某種程度上允許使用 LLM。他要問的是**完整的端到端研究**:從有想法、形成假說、設計方法論、到測試與再往下走。他很清楚很多人不同意、很多人覺得這不可能——**兩年前他自己就是其中之一**。

#### 那篇論文:7-round AES(約 03:05–03:10)

「這週我們剛發表了這份工作,顯示 Claude 能做密碼分析」——意思是在密碼演算法中找出弱點。其中一項結果是對對稱式加密演算法 **AES** 的新攻擊。論文作者只有兩位:他自己與 **Nicholas Carlini**。他刻意把兩人的學術履歷攤開:Carlini 的背景是系統安全、近期轉 ML security;他自己是網路安全、現在做 ML security。**「我們兩個人,加上一份網際網路的拷貝,再加上一堆 coding agent,照理說不該做得出對密碼系統的攻擊。」** 兩人都喜歡密碼學,也試過破解更簡單的東西,而且都很不擅長。

AES 的背景:2001 年由 **NIST** 標準化,是一個**迭代式演算法,共 10 輪**。它吃一個輸入與一把金鑰,主要由四個部分構成——**substitution**(S-box 把輸入映射到另一組輸出)、把 bit **重新排列**(permutation),以及**加上金鑰的某個函數**;然後把這一整套重複約 10 次。

接著是他重複兩次的免責聲明:**他們沒有破解 AES。真的破了 AES,就是把網際網路破了。** 這是一份學術工作,對象是**輪數縮減後的 AES**——只做 **7 輪**而非完整 10 輪,這是學界的標準研究對象,因為比較容易、也比較可能取得進展。

複雜度的量級對照:

- **暴力破解** 7-round AES:約 **2^128** 次運算——耗時比太陽變成新星還久。
- **2013 年提出的既有最佳演算法**:約 **2^99**——大概要 20 萬到 200 萬年。
- 而且這不是沒人努力:這個問題被相當充分地研究過。
- **他們的新結果**:約 **2^89**(取決於怎麼計算),實測**快約 200 到 800 倍**。他自嘲:「所以大概一千年就跑得完了,我不知道這有多重要。」

攻擊原理他用兩分鐘帶過:密碼演算法的攻擊通常是**在不真正破解演算法本身的前提下,找出輸入與輸出之間的關係**。AES 的 S-box 用了一個特定的公式——**先在某個有限域中取反元素,再做縮放與平移**。他的類比是:把一個物體縮放再平移,**形狀之間的比例關係不變**,只是移動了、放大了。**模型理解到 S-box 具有這個性質,並用它推導出攻擊演算法。** 方法非常複雜,他請有興趣的人去讀論文。

而且不只 AES:他們也對其他密碼系統做出攻擊,包括 **HAWK**(後量子演算法之一)與 **LEA**(在其他國家被使用)。他再次強調:**這些攻擊沒有改變網際網路上的任何東西,是學術成果。**

#### 模型是怎麼做研究的:3,000 個點子換 4 個結果(約 03:10–03:12)

他對比了兩種工作方式:

- **如果是他自己做**:找個地方坐下來想幾週,生出幾個點子,去找幾個人討論,可能收斂出幾個,然後才去實作。
- **模型的做法完全不同**:一次生出**大量**點子,而且**不去找人討論,而是把每一個都實作出來,看哪一個真的行得通**。

他由此提出一句反轉:**「我們以前說 ideas are cheap, execution is everything;現在也許是 ideas 更重要,而 execution 模型可以做得非常非常快。」**

但 AES 有個特殊困難:**執行本身就跑不動**——複雜度大於我們能負擔的量級,不可能真的去把一個 2^89 的演算法跑完。所以他們建了一個 **harness**:接收一個研究想法 → 去找幾個其他 agent 討論這個想法好不好 → 實作 → 對想法迭代。他的補充很誠實:**「現在你需要一個 harness;也許未來不用,但至少現在要。」**

搜尋規模的數字非常具體。從一句「**go beat AES**」開始,展開成一層又一層的想法樹:

- 模型產出**超過 3,000 個點子**;
- 其中**超過 2,000 個**確實適用於這個問題;
- 約 **200 個**是具新穎性的想法;
- **最後只有 4 個進到論文裡**。

代價是大量算力。

#### 「你們只是不擅長密碼學吧?」——以及新的瓶頸(約 03:12–03:13)

他主動提出最常見的質疑:**也許只是我們兩個不擅長密碼學,所以才會覺得這很厲害。** 他承認這有可能——他沒有密碼學背景,能讓他驚豔的東西未必能讓別人驚豔。但他們**把結果拿給真正的密碼學家看,對方確實感興趣**。

第二層質疑是:也許**人類整體**就是不擅長密碼學。對此他的回應是:他們看的不只是密碼學,還包括其他資安研究——用他自己較熟悉的網路安全背景往外延伸到隱私等領域——**每一個方向都有令人期待的結果**。而現在,**他們大部分的時間花在驗證這些結果上**。

收尾的那句話回到研究本質:我們過去說一個研究需要**同時**具備新穎性與品質;而其中一個信念是,**LLM 也許各自擅長其中一項,但無法同時做到兩者**。他的結語是:也許這件事正在開始鬆動。

### 金句

> "Two of us plus a copy of the internet plus a bunch of coding agents shouldn't essentially be able to come up with an attack on cryptographic systems."(約 03:06)

他刻意先貶低自己的資格,好讓成果的來源無可推諉。

> "We didn't break AES. If someone breaks AES, it breaks the internet."(約 03:07)

全場最重要的免責聲明,他講了兩次。

> "Maybe we had this saying before that ideas were cheap and the execution is everything. Now maybe ideas is more important, and execution the model can do very, very fast."(約 03:10)

研究工作的稀缺資源正在換位。

> "We are spending most of our time verifying the results."(約 03:13)

新的瓶頸不是產出,是驗證。

## English Notes

### TL;DR

- **Prediction vs. reality.** Two years ago a room of frontier-lab researchers estimated 2–5 years at best (5+ on average) until agents do more than 90% of our coding, and more than 10 years until agents do more than 90% of our general research. They were somewhat wrong on coding and **very wrong on research**.
- **The evidence is a cryptanalysis paper published that week.** The model found a new attack on **7-round (reduced) AES**, cutting the best known complexity from the 2013 result of **2^99** to roughly **2^89** — empirically 200–800× faster. **He was emphatic that AES itself is not broken**; breaking AES would break the internet. Same approach also produced attacks on **HAWK** (a post-quantum algorithm) and **LEA**.
- **The shape of the shift, and the new bottleneck.** A human sits and thinks for weeks, talks to people, then implements; the model **generates many ideas and implements all of them to see which works**. "Ideas are cheap, execution is everything" may be inverting. Concretely: from the prompt "go beat AES," the model produced **3,000+ ideas**, 2,000+ of them actually applicable, ~200 genuinely novel, and **exactly four made it into the paper**. Most of the team's time now goes to **verifying** results.

### Key Points

#### The two questions from two years ago (~03:01–03:04)

At an event much like this one two years ago, Nasr and a group of researchers from top frontier labs did what researchers do and tried to predict the future. Two questions:

1. **How long until LLMs and agents do more than 90% of our coding?** Best case 2–5 years; more than 5 years on average.
2. **How long until agents do more than 90% of our general research?** More than 10 years.

His verdict: on coding they were wrong, though maybe not by that much. On research they were possibly **very, very wrong**.

He pinned the definition down first. By "LLM research" he does **not** mean using an LLM as a tool — many conferences, including security venues that are extremely conservative, now allow that to some degree. He means **full end-to-end research**: having the idea, forming a hypothesis, developing a methodology, testing it, and going beyond. He acknowledged plenty of disagreement in the room, and that many people think it's impossible — **he was one of them two years ago**.

#### The paper: 7-round AES (~03:05–03:10)

"This week we published this work showing Claude can do cryptographic analysis" — meaning finding flaws in cryptographic algorithms. One result is a new attack on the symmetric algorithm **AES**. The paper has two authors: himself and **Nicholas Carlini**. He deliberately put their CVs on screen: Carlini comes from systems security and more recently machine-learning security; Nasr from network security, now machine-learning security. **"Two of us plus a copy of the internet plus a bunch of coding agents shouldn't essentially be able to come up with an attack on cryptographic systems."** They both like cryptography and have tried to break simpler things before — and are, in his words, very weak at it.

AES background: standardized by **NIST in 2001**, an **iterative algorithm with 10 rounds**. It takes an input and a key and has four main parts — **substitution** (the S-box maps an input to another set of outputs), a **permutation** that moves bits around, and adding a **function of the key** — repeated roughly ten times.

Then the disclaimer he gave twice: **they did not break AES. If someone breaks AES, it breaks the internet.** This is academic work on **reduced-round AES** — seven rounds instead of the full ten, which is what academics study because it is more tractable and improvement is plausible.

The complexity ladder:

- **Brute force** on 7-round AES: about **2^128** operations — longer than the time until our sun goes nova.
- **The best existing algorithm, from 2013**: about **2^99** — call it 200,000 to 2,000,000 years.
- And not for lack of trying: this is a fairly well-studied problem.
- **Their result**: about **2^89**, depending on how you count, and empirically **200 to 800 times faster**. His own gloss: "so maybe in around a thousand years — I don't know how much that matters."

The mechanism, compressed into two minutes: attacks on crypto algorithms typically look for a **relationship between input and output without breaking the algorithm itself**. The AES S-box uses a specific formula — it **inverts the input in a finite field, then scales and shifts it**. His analogy: if you take an object and scale and shift it, the **ratios within the shape stay the same**, just moved and zoomed. **The model recognized that the S-box has this property and used it to construct the algorithm.** The method is very complicated; he pointed interested people to the paper.

And it wasn't only AES — they also produced attacks on other cryptosystems, including **HAWK** (one of the post-quantum algorithms) and **LEA** (used in other countries). Again: **none of these attacks has changed anything about the internet. These are academic achievements.**

#### How the model does research: 3,000 ideas for four results (~03:10–03:12)

He contrasted two working styles:

- **If he did it himself**: sit somewhere and think for a few weeks, come up with a few ideas, go talk to a few people, converge on a few, then implement them.
- **The model does it differently**: generate a *lot* of ideas, and instead of going to talk to people, **implement all of them to see which one actually works**.

Hence the inversion: **"We used to say ideas were cheap and execution is everything. Now maybe ideas are more important, and execution the model can do very, very fast."**

AES has a complication: **execution itself is infeasible** — you cannot simply run a 2^89 algorithm. So they built a **harness** that takes a research idea, consults a few other agents on whether the idea is good, then implements it and iterates on it. His honest caveat: you need a harness right now; maybe not in the future, but at least today you do.

The search numbers were specific. Starting from a single instruction — **"go beat AES"** — the tree of ideas unfolded into:

- **more than 3,000 ideas** generated;
- **more than 2,000** actually applicable to the problem;
- around **200** that were genuinely novel;
- and **only four that made it into the paper**.

The cost was a lot of compute.

#### "Maybe you're just bad at crypto" — and the new bottleneck (~03:12–03:13)

He raised the obvious objection himself: maybe they simply are bad at cryptography, which is why they find this impressive. He conceded it might be true — he has no cryptography background, so what impresses him may not impress anyone else. But they showed the results to **actual cryptographers, who were interested in them**.

The second-order objection: maybe **humans in general** are bad at crypto. His answer is that they have looked well beyond crypto at other security research — extending from his own network-security background into privacy and elsewhere — with **promising results in all of them**. And notably, **most of their time now goes into verifying the results**.

His closing point returned to the nature of research: we used to say you need a novel idea *and* a good idea at the same time, and one prevailing belief was that **LLMs might be good at each but not at both simultaneously**. Maybe, he suggested, that is starting to move.

### Quotes

> "Two of us plus a copy of the internet plus a bunch of coding agents shouldn't essentially be able to come up with an attack on cryptographic systems." (~03:06)

He undercuts his own credentials first, so the source of the result is unambiguous.

> "We didn't break AES. If someone breaks AES, it breaks the internet." (~03:07)

The disclaimer he made twice, and the most important sentence in the talk.

> "Maybe we had this saying before that ideas were cheap and the execution is everything. Now maybe ideas is more important, and execution the model can do very, very fast." (~03:10)

The scarce resource in research is changing places.

> "We are spending most of our time verifying the results." (~03:13)

The new bottleneck is not production, it is verification.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| 7-round AES 密碼分析論文 / 7-round AES cryptanalysis paper | 演講當週發表:利用 AES S-box 的代數結構,把 7 輪 AES 攻擊複雜度從 2^99 降到約 2^89 | Published that week: exploits the algebraic structure of the AES S-box to cut 7-round AES attack complexity from 2^99 to roughly 2^89 | 論文標題為 "Cryptanalysis of 7-Round AES via the Algebraic Structure of its S-box"(Milad Nasr, Nicholas Carlini);<https://www-cdn.anthropic.com/c88771e1bf5ee8885349eed05e5484c0e5f7e02b/aes_mobius_bridge.pdf> |
| HAWK | 後量子密碼演算法之一,同一套方法也產出攻擊 | A post-quantum algorithm; the same approach produced an attack on it | 講者僅口頭提及,未展開 / mentioned only in passing |
| LEA | 在其他國家使用的區塊加密演算法,同樣被攻擊 | A block cipher used in other countries; also attacked | 同上 / same |
| Research harness | 接收研究想法 → 找其他 agent 評估 → 實作 → 迭代;AES 因執行成本過高而必要 | Takes a research idea, consults other agents on its merit, implements, iterates — necessary because AES execution is infeasible to brute-force | 講者認為是現階段必需品,未來未必 / he considers it necessary today, maybe not later |
| Nicholas Carlini | 論文共同作者,背景為系統安全與 ML security | Co-author; background in systems security and ML security | Anthropic |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Milad Naser | Milad Nasr |
| anthropic | Anthropic |
| cloud | Claude |
| Nicholas Kini / Nicholas Carlini | Nicholas Carlini |
| as / abs / areas | AES |
| hawk | HAWK |
| lea | LEA |
| splice | S-box |
| our son is going to Nova | our sun is going to nova |
| two to 128 / two to the 89 | 2^128 / 2^89 |
| SEC(在 "background in SEC" 中)| security |

## 待確認 / To Verify

- 逐字稿的 2^89 與「200 到 800 倍」與論文公開報導的區間(2^89.3–2^91.4、200–1000 倍)略有出入,以論文數字為準。/ The transcript's 2^89 and "200–800×" differ slightly from the published range (2^89.3–2^91.4, 200–1000×); defer to the paper.
- 演講未指名這項研究使用的模型版本(公開報導指向 Claude Mythos Preview),影片投影片可再確認。/ The talk did not name the model version used (public reporting points to Claude Mythos Preview); check the slides.
- 「3,000+ 個想法 / 2,000+ 適用 / ~200 新穎 / 4 篇入論文」的統計是否出現在論文附錄。/ Whether the 3,000+ / 2,000+ / ~200 / 4 idea-funnel statistics appear in the paper appendix.
- 兩年前那場「前沿實驗室研究者預測活動」的名稱與時間未說明。/ The name and date of the frontier-lab prediction gathering two years earlier.
