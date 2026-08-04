---
title: "Unlocking Scientific Abundance by Learning from Superhuman AI"
title_zh: "從超人 AI 身上學習,開啟科學的豐饒時代"
speaker: "Eric Ho"
affiliation: "Co-Founder/CEO, Goodfire"
type: talk
stage: Nexus
date: 2026-08-01
session: "Session 1: AI for Science"
video: "https://www.youtube.com/watch?v=LB7IkZhEYic&t=1965s"
video_range: "00:32:45–00:47:49"
transcript: "tmp/[English (auto-generated)] Nexus Stage - August 1st - Morning Session [DownSub.com].srt"
status: draft
tags: [interpretability, ai-for-science, mechanistic-interpretability, neural-geometry, biology]
---

# 從超人 AI 身上學習,開啟科學的豐饒時代(Unlocking Scientific Abundance by Learning from Superhuman AI)

**一句話總結**:超人科學模型已經知道一些人類還不知道的事;把它們的內部計算逆向工程出來,就能把那些知識搬回人類手上——這是把 AI 能力轉成科學發現最直接的一條路。
**One-line summary**: Superhuman scientific models already know things humans don't; reverse-engineering their internal computations is the most direct way to move that knowledge back into human hands.

## 中文筆記

> 註:這場演講的投影片直到約 00:38 才接上,前段是 Eric Ho 即興的公司介紹與現場 Q&A,內容本身相當實質,故一併記錄。

### TL;DR

- **可解釋性的目標不只是安全,是「intentional design」**:能理解、編輯、debug 模型,像對待寫出來的軟體一樣,而不是靠試誤訓練。
- **從模型身上學,而不只是檢查模型**:人類的表徵空間 H 與機器的表徵空間 M 有一塊交集——那裡是「AI 已經知道、而人類有能力理解」的知識。共同創辦人 Tom(Goodfire 首席科學家)在 DeepMind 時已用 AlphaZero 證明可行:逆向工程出來的棋理真的教會了人類特級大師下得更好。
- **模型不能被信任來解釋自己**:它吐出的 token 常常與它實際的計算不忠實(unfaithful),所以必須直接看內部。
- **兩個已落地的生物學案例**:逆向工程 Prima Mente 的表觀基因體模型 Pleiades,發現它主要靠一個當時文獻裡沒有的 **fragmentomic** 生物標記來偵測阿茲海默症(表徵成一個編碼片段長度的半甜甜圈流形);與 Mayo Clinic 合作用 DNA foundation model 的 embedding 預測 SNP 致病性,取得 state-of-the-art。

### 重點整理

#### 為什麼要看進模型內部(約 00:33–00:40)

Goodfire 是專做 AI 可解釋性的研究公司,整天在想「模型腦子裡到底在幹嘛」——直接看神經元、參數、計算過程。動機有兩層:一是我們理應理解這個史上最重大的技術,尤其它正被放進世界的每個角落;二是要走向他們說的 **intentional design**——一個我們能理解、能編輯、能 debug 這些系統的未來,**像對待寫出來的軟體,而不是像今天這樣靠試誤訓練**。

在等投影片的空檔他回答了兩個現場提問,反而把公司立場講得更清楚:

- **關於對齊與 steering**:他認為看不到深層理解,就很難想像我們真能對齊模型、得到我們要的系統。他們的技術之一叫 **reinforcement learning with feature rewards**——「feature」指的是被抽取出來、而且我們知道它在做什麼的模型內部計算(可以是任何東西,他半開玩笑舉例:不安全行為、「hacking Hugging Face」這種也可以是一個 feature)。抽出來之後就能拿它去 steer 與引導訓練:**挑我們要的更新,移除我們不要的更新**。
- **關於「你們是不是 AI 治理公司」**:不是。他們在做產品 **Silico**——可以理解成一個 AI neuroscientist,進去理解、設計、debug 模型;公司同時在做「發現新訓練方式」的科學,也在做把它交付出去的平台。

技術上的困難很直接:就算給你一個超人模型,你打開來只會看到一堆看不出所以然的數字與計算;模型現在動輒兆級參數,沒有人類能理解藏在權重裡的一兆個數字。更麻煩的是**你也不能問模型自己**——模型輸出的 token 常常對它真正的計算不忠實,兩者會打架。可解釋性要解的就是這個:把一團亂數與參數變成人類看得懂的解釋。

#### Move 37 與 M ∩ H:從超人 AI 身上學東西(約 00:41–00:44)

他用 AlphaGo 的 move 37 當問題設定:AlphaGo 對李世乭那盤,第 37 手所有人一開始都覺得是失誤,結果那步扭轉了整盤棋。問題是——**AlphaGo 的表徵裡到底發生了什麼,讓它下得出這一手?** 那不是隨機的,它對圍棋有某種比任何人類都豐富的理解。

於是他畫出設定:人類有表徵空間 H,機器有表徵空間 M,真正有意思的是 **M ∩ H**——那塊「AI 知道了新東西、而人類還有能力理解」的區域。

這聽起來像科幻,但他的共同創辦人 Tom(Goodfire 首席科學家)在 DeepMind 時已經用 **AlphaZero** 做出來了,而且是直接與 Demis 合作的幾篇論文:在特定局面下逆向工程 AlphaZero 的計算,產出的知識**真的教會了人類西洋棋特級大師下得更好**。他把這件事定為公司使命的一大部分:從模型裡萃取科學知識再教回給人類,「這樣我們才不會被丟在後頭」。

操作化的方式是訓練一個 **AI neuroscientist**,能跨十億到兆級參數的模型去逆向工程它們的計算,把對人類而言像亂碼的神經元翻譯成可理解的概念。語言模型與影像模型上的任意概念都能這樣抽(金門大橋、對使用者阿諛附和),但這天他要談的是更有意思的行為:生物學裡的新科學。

#### 神經幾何與兩個生物學案例(約 00:44–00:47)

要理解模型在做什麼,得先知道它的**結構**長什麼樣。他們最近釋出的研究提出 **neural geometry**:**AI 模型是用複雜的形狀在思考**——看那些流形,通常是扭轉的、彎曲的幾何,而不是單純的詞、方向或個別數字。他們在意這個結構,因為結構裡可能藏著人類自己走不到的自然界洞見。

**案例一:阿茲海默症偵測。** 合作對象是 **Prima Mente**,他們訓練了一個表觀基因體 foundation model 叫 **Pleiades**,用來從 cell-free DNA 偵測阿茲海默症,而且是該任務的 state-of-the-art——但他們**完全不知道模型是怎麼辦到的**。Goodfire 用 AI neuroscientist 逆向工程它的計算,發現模型主要仰賴一個 **fragmentomic 生物標記**;這在當時的文獻裡沒有,是個意外發現,幾個月前上了《紐約時報》,而且在獨立世代群(cohort)上驗證成立。至於模型怎麼表示這個訊號:一個編碼**片段長度**的**半甜甜圈狀流形**。他強調兩件事都得自己造:抽取流形計算的工具,以及看懂它在表示什麼。

**案例二:遺傳變異致病性。** 與 **Mayo Clinic** 合作,主攻 **SNP(單核苷酸多型性)**,想搞清楚哪些變異真的致病。做法是用 DNA foundation model(DNA transformer)的 embedding 去預測致病性,在這個任務上取得 state-of-the-art——同樣是先把模型內部映射出一個豐富結構,再從結構裡拿準確率。

他的收尾:這才剛開始——拿超人科學模型、理解它學到什麼、再驗證,可以看成一條**新洞見的假說生成迴圈**。產品 **Silico** 下週開放公開存取,任何人訓練的科學模型(生物、材料、物理)都可以套用這套技術。

### 金句

> "…the actual tokens that the model emits often are not actually faithful to their computation. There are clashes between those."(約 00:40:22)

不能問模型自己在想什麼——這是為什麼必須看內部。

> "AI models think in complex shapes."(約 00:44:12)

neural geometry 的一句話版本:不是詞、不是方向,是彎曲的流形。

## English Notes

> Note: the slides didn't come up until ~00:38. The first stretch is Ho improvising a company overview and taking questions from the floor — substantive enough to record here.

### TL;DR

- **Interpretability isn't only about safety — it's about "intentional design"**: a future where we understand, edit, and debug models the way we do written software, instead of training by trial and error.
- **Learn *from* models, not just *about* them**: humans have a representation space H, machines have M, and the interesting region is M ∩ H — knowledge the AI already has that humans are still capable of understanding. Co-founder Tom (Goodfire's chief scientist) proved this works at DeepMind with AlphaZero: reverse-engineered chess knowledge genuinely taught human grandmasters to play better.
- **A model can't be trusted to explain itself**: the tokens it emits are often unfaithful to its actual computation, so you have to look inside.
- **Two shipped biology results**: reverse-engineering Prima Mente's epigenetic foundation model **Pleiades** revealed it was mostly relying on a **fragmentomic** biomarker for Alzheimer's detection — not in the literature at the time — represented as a half-donut manifold encoding fragment length; and work with **Mayo Clinic** using DNA foundation-model embeddings hit state of the art on predicting which SNPs are pathogenic.

### Key Points

#### Why look inside the model (~00:33–00:40)

Goodfire is an AI interpretability research company; they spend their days on what's actually going on inside a model — neurons, parameters, computations. Two motivations: we ought to understand the most consequential technology of all time, particularly as it's deployed everywhere; and they want **intentional design** — a future where these systems can be understood, edited, and debugged **like written software rather than trained by trial and error**.

Two audience questions during the slide delay drew out the company's position more sharply than the deck did:

- **On alignment and steering**: he finds it hard to picture a future where we genuinely align models and get the systems we want without deep understanding. One of their techniques is **reinforcement learning with feature rewards**, where a "feature" is an internal computation that's been extracted and understood. A feature can be anything — he only half-joked that unsafe behavior, or "hacking Hugging Face," could be one. Once extracted, it can steer and guide training: **pick the updates you want, remove the ones you don't**.
- **On whether they're an AI governance company**: no. They're building a product called **Silico** — think of it as an AI neuroscientist that goes in, understands, designs, and debugs models. The company is simultaneously doing the science of a different way to train models and building the platform that delivers it.

The technical difficulty is blunt. Take a superhuman model as given, look inside, and all you see are random-looking numbers and computations no human can parse — and these are trillion-parameter models now. Worse, **you can't just ask the model**: the tokens it emits are frequently unfaithful to its computation, and the two clash. Interpretability is the problem of turning that jumbled mess into a human-understandable explanation.

#### Move 37 and M ∩ H: learning from superhuman AI (~00:41–00:44)

He sets up the problem with AlphaGo's move 37 against Lee Sedol — the move everyone initially read as a mistake, which turned the game. The question is **what was in AlphaGo's representations that produced it?** It wasn't random; there was some richer understanding of Go than any human had.

Hence the framing: humans have a representation space H, machines have M, and what matters is **M ∩ H** — where AI can teach us something new about the world *and* we retain the capacity to understand it.

This sounds like science fiction, but his co-founder Tom, Goodfire's chief scientist, already did it with **AlphaZero** in a couple of papers at DeepMind, collaborating directly with Demis: reverse-engineering AlphaZero's computation in narrow positions produced knowledge that **taught human chess grandmasters to play more effectively**. He frames this as a large part of the company's mission — extract scientific knowledge from models and teach it back to humans "so we don't get left in the dust."

Operationally that means training an **AI neuroscientist** capable of going into billion- and trillion-parameter models to reverse-engineer their computations, translating what looks like gibberish at the neuron level into human-interpretable concepts. You can do this with arbitrary concepts in language and image models — the Golden Gate Bridge, sycophancy — but the point of this talk is more interesting behavior: novel science in biology.

#### Neural geometry and two biology case studies (~00:44–00:47)

Understanding what a model does starts with understanding its **structure**. Their recent research introduces **neural geometry**: **AI models think in complex shapes**. Look at the manifold and you typically find twisting, curved geometry rather than words, directions, or individual numbers. The structure matters because it may encode insights about the natural world we wouldn't have reached ourselves.

**Case one: Alzheimer's detection.** Their partner **Prima Mente** trained an epigenetics foundation model called **Pleiades** to predict Alzheimer's, and it is state of the art at detection from cell-free DNA — but they had no idea how it worked. Goodfire's AI neuroscientist reverse-engineered the computation and found the model was mostly using a **fragmentomic biomarker** — a surprising result that wasn't in the literature at the time, covered in the *New York Times* a few months back, and one that generalized to an independent cohort. The representation itself was a **half-donut manifold encoding fragment length**. Both halves were work: building tools to extract manifold computations, and working out what the manifold represented.

**Case two: genetic variants.** With **Mayo Clinic**, focused on **SNPs** (single nucleotide polymorphisms) and the question of which variants are actually pathogenic. Using the embeddings of a DNA transformer foundation model, they reached state-of-the-art accuracy on disease-causing variant prediction — again by mapping the model into a rich structure first and reading accuracy out of it.

His close: this is the beginning of the quest — take superhuman scientific models, understand what they've learned, validate it, and treat the whole thing as a **hypothesis generation loop for novel discovery**. Their system **Silico** goes into public access the following week, applicable to any model you're training across biology, materials, and physics.

### Quotes

> "…the actual tokens that the model emits often are not actually faithful to their computation. There are clashes between those." (~00:40:22)

You can't ask the model what it's thinking — which is exactly why you have to look inside.

> "AI models think in complex shapes." (~00:44:12)

Neural geometry in one line: not words, not directions — curved manifolds.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Silico | Goodfire 的產品:AI neuroscientist,理解、設計、debug 任意模型 | Goodfire's product: an AI neuroscientist that understands, designs, and debugs models | 演講時說「下週開放公開存取」/ said to enter public access "next week" |
| Reinforcement learning with feature rewards | 用抽取出的內部 feature 當獎勵訊號來 steer 與引導訓練 | Steering and guiding training with extracted internal features as reward signals | 挑要的更新、移除不要的更新 / keep the updates you want, drop the ones you don't |
| Neural geometry | 主張模型以彎曲流形而非方向/詞彙進行運算的研究線 | Research line arguing models compute over curved manifolds, not directions or words | Goodfire 近期釋出 / recently released by Goodfire |
| Pleiades(Prima Mente) | 表觀基因體 foundation model,從 cell-free DNA 偵測阿茲海默症 | Epigenome foundation model detecting Alzheimer's from cell-free DNA | 逆向工程後發現主訊號是 fragmentomics;曾登《紐約時報》/ reverse-engineering revealed fragmentomics as the main signal; covered in the *New York Times* |
| Mayo Clinic 合作 / collaboration | 用 DNA foundation model embedding 預測 SNP 致病性,取得 SOTA | Predicting SNP pathogenicity from DNA foundation-model embeddings; state of the art | |
| AlphaZero 可解釋性工作 / interpretability work | Tom(現 Goodfire 首席科學家)在 DeepMind 與 Demis 合作,逆向工程棋理並教給人類特級大師 | Tom (now Goodfire's chief scientist) at DeepMind with Demis: reverse-engineered chess knowledge taught to human grandmasters | 演講中僅稱 "Tom" / referred to only as "Tom" in the talk |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| GoodFire / good fire | Goodfire |
| silico / silicico | Silico |
| Prima | Prima Mente |
| Pletes | Pleiades |
| fragmenttoic / fragmenttoic biioarker | fragmentomic / fragmentomic biomarker |
| Alph Go / Alpho / alpho | AlphaGo |
| Alpha Zero / Alph zero | AlphaZero |
| Lee Sadull / Lisa doll | Lee Sedol |
| GDM | Google DeepMind |
| SNIPS | SNPs(single nucleotide polymorphisms) |
| sick of fancy | sycophancy |
| self-free DNA | cell-free DNA |

## 待確認 / To Verify

- 演講中僅稱共同創辦人為 "Tom";Goodfire 首席科學家公開資料為 Tom McGrath(DeepMind 可解釋性團隊共同創辦人),但講者本人未唸出全名。/ The co-founder is referred to only as "Tom"; public sources name Goodfire's chief scientist as Tom McGrath (co-founder of DeepMind's interpretability team), but the full name wasn't said on stage.
- 「published in the New York Times a few months ago」的正確報導與日期未查證。/ The specific *New York Times* piece and its date were not located.
- Mayo Clinic 案例所用的 DNA foundation model 名稱未提及。/ The DNA foundation model used in the Mayo Clinic work was not named.
- AlphaGo vs. Lee Sedol 賽制他說「best of seven,我記得是」,實際為五局三勝(不影響論點)。/ He said "best of seven, I believe"; the match was actually best of five — noted for accuracy, doesn't affect the argument.
- neural geometry 研究的正式論文標題與連結未提供。/ No formal title or link given for the neural geometry research.
