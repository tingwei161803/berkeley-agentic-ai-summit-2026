---
title: "Semantic Alignment Models for Math and Software Engineering"
title_zh: "數學與軟體工程中的語意對齊模型"
speaker: "Vijay Ganesh"
affiliation: "Professor, Georgia Institute of Technology"
type: talk
stage: Atlas
date: 2026-08-02
session: "Session 3: AI for Math"
video: "https://www.youtube.com/watch?v=-7AJJLwYW1Q&t=4669s"
video_range: "01:17:49–01:24:17"
transcript: "tmp/[English (auto-generated)] Atlas Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [autoformalization, lean, formal-methods, neuro-symbolic, code-translation]
---

# 數學與軟體工程中的語意對齊模型(Semantic Alignment Models for Math and Software Engineering)

**一句話總結**:在 autoformalization 這種「跨模態但語意必須相等」的任務上,與其把模型做大,不如把 **semantic alignment** 這個性質直接訓進 embedding 空間——語意相同的物件靠近、不同的遠離——他們用這招做出比前沿模型小 1000 倍卻在所有測試 benchmark 上更強的模型。
**One-line summary**: For autoformalization — a cross-modal task where semantic content must be preserved exactly — the win isn't scale but training the property of **semantic alignment** directly into the embedding space: objects with the same semantic content sit close together, different ones far apart. That recipe produced a model 1000× smaller than frontier models that beat them on every benchmark tested.

## 中文筆記

### TL;DR

- **問題:autoformalization**——把自然語言數學(英文、法文…)翻譯成形式語言數學(Lean 或其他定理證明語言)。動機是人寫的證明常常**不完整**(缺步驟,而數學家自己可能沒察覺),更糟的是有時**根本是錯的**;翻成形式語言後就能用 Lean 定理證明器實際檢查定理是否真的被證明了。
- **目標設定很銳利**:做一個比前沿模型**至少小 1000 倍**的模型,而且在 autoformalization 這**單一任務**上要贏過最大的前沿模型。
- **關鍵性質:semantic alignment**——同一個物件用不同模態表示、語意內容相同時,要在模型的 embedding 空間中**靠近**;語意內容不同就要**遠離**。訓練配方叫 **semantic contrastive learning**;帶來的直接好處是**檢索(retrieval)階段效率大幅提升**。
- **不只數學**:同樣的性質適用於程式語言間的翻譯、規格 → 電路、以及連結不同數學領域的定義以發現新關係——而且可以用小模型做到。
- **正在做的延伸**:COBOL → Python 的遺留程式碼翻譯。因為**輸入程式本身就是規格**,不需要另外寫 spec;他們用 **LLM 驅動的符號執行(symbolic execution)** 從輸入程式生成測試集,再用它驗證輸出程式與輸入是否語意等價。

### 重點整理

#### 什麼是 autoformalization,以及為什麼需要它(約 01:18–01:19)

他自我介紹:Georgia Tech 計算機科學教授,研究領域涵蓋**形式化方法**與**數學、物理、程式的 neuro-symbolic AI**。他明確說明自己的題目和前兩位講者不同。

**Autoformalization = 把自然語言數學翻譯成形式語言數學。** 自然語言數學指用英文、法文等語言寫的數學;形式語言指 **Lean** 或其他定理證明語言。

為什麼要翻?因為自然語言數學有兩個問題:

1. **人寫的證明常常不完整**——缺了步驟,而且**寫的數學家自己可能不知道**。
2. 更糟的是,**有時候證明根本是錯的**。

翻成形式語言之後,就可以把 **Lean 定理證明器**開下去,實際檢查那個定理到底有沒有被證明。

#### 什麼叫「等價」(約 01:19–01:20)

他們要造的是一個盒子:輸入自然語言數學,輸出**等價**的形式語言數學。這裡的等價指的是 **semantic equivalence(語意等價)**:輸入的畢氏定理的語意內容,必須和輸出的 Lean 程式的語意內容相同——它必須在講直角三角形,而且那個關係必須一樣。

**任務設定**:做出這樣一個盒子,而且要比前沿模型**至少小 1000 倍,甚至更小**;問題是——**要怎麼訓練這樣一個模型,讓它在 autoformalization 這一個任務上贏過外面最大的前沿模型?**

#### Semantic alignment 與 semantic contrastive learning(約 01:20–01:22)

他提出的性質叫 **semantic alignment**。這個概念本身不新,很多場景都有人談過,但**在數學裡它有特定意義**:

> 兩個物件以**不同模態**表示,若它們的**語意內容相同**,就要在模型的 embedding 空間中**彼此靠近**;若語意內容不同,就要**彼此遠離**。

把這個性質灌進模型之後,模型在 autoformalization 上就有效得多——他特別點名**在檢索(retrieval)的時候效率高出很多**。

這個性質的價值不限於「自然語言數學 → 形式語言數學」,還包括:
- 程式語言之間的**程式碼翻譯**
- **規格 → 電路**
- **連結不同數學領域的定義**,看出跨領域定義之間的關係,從而發現新數學

而且——這是他反覆強調的重點——**用非常小的模型就能做到,不必有前沿模型的存取權**。

訓練配方叫 **semantic contrastive learning**:把上述性質灌進模型(語意相同 → embedding 靠近)。結果是在**他們測試的所有 benchmark 上都比前沿模型強得多**。

#### 延伸到程式碼翻譯(約 01:22–01:23)

他們正把這個想法帶到程式碼翻譯:建一個工具,把 **COBOL 這類遺留語言的程式翻成 Python**,並在輸入程式上部署驗證工具與自動化測試工具。

這裡有個很漂亮的設計論點:**在這個情境下不需要規格,因為輸入程式本身就是規格**。他們用 **LLM 驅動的符號執行**從輸入程式生成一組測試集,有了測試集之後就能拿去跑輸出程式,檢查輸入輸出兩個程式是否**語意等價**。他也直言這件事有很強的商業誘因。

#### 結論(約 01:23–01:24)

他的總結:在任何**你能取得形式化物件**的場景中——做形式物件之間的翻譯、或把非形式物件翻成另一個模態的形式物件——**把 semantic alignment 這個性質灌進模型,是打造一個能 scale 的系統的好方法**;而且模型規模可以小很多,卻仍能擴展到非常大的程式碼庫。

### 金句

> "Often human-written proofs are incomplete, meaning they are missing steps, and the human mathematicians may not be aware of that. Worse, sometimes the proofs are incorrect."(約 01:19)

autoformalization 的真正動機不是形式主義潔癖,而是人類證明本來就會出錯。

> "If two objects which are represented in different modalities have the same semantic content, then we want them to be close by in the embedding space of the model."(約 01:21)

一句話定義 semantic alignment。

> "In this setting, we don't need specifications because the input program is the specification."(約 01:23)

程式碼翻譯之所以比一般形式化容易的關鍵洞見。

## English Notes

### TL;DR

- **The problem: autoformalization** — translating natural language math (English, French, …) into formal language math (Lean or another theorem-proving language). The motivation is that human-written proofs are often incomplete, with missing steps the mathematicians may not be aware of, and sometimes outright incorrect. Once formalized, you can run the Lean theorem prover and check whether the theorem was actually proven.
- **A sharp target**: build a box at least **1000× smaller** than frontier models that nevertheless **outperforms the largest frontier models** on this one task.
- **The key property is semantic alignment**: two objects represented in different modalities with the same semantic content should be close in the model's embedding space; different semantic content should be far apart. The training recipe is **semantic contrastive learning**, and the concrete payoff is far more effective retrieval.
- **It generalizes**: code translation between languages, specification → circuit, and connecting definitions across areas of math to surface relationships and discover new math — all with small models, no frontier access required.
- **Current extension**: COBOL → Python legacy code translation. No specification is needed because **the input program is the specification**; they use **LLM-driven symbolic execution** to generate a test suite from the input, then run it against the output to check semantic equivalence.

### Key Points

#### What autoformalization is and why it matters (~01:18–01:19)

He introduces himself as a professor of computer science at Georgia Tech working broadly in formal methods and neuro-symbolic AI for mathematics, physics, and code, and notes his problem differs from those of the previous two speakers.

Autoformalization means translating natural language math — math written in English, French, and so on — into formal language math, meaning Lean or another theorem-proving language.

Why bother? Because human-written proofs are often incomplete, missing steps that the human mathematicians may not be aware of; and worse, sometimes the proofs are incorrect. Translating into formal language lets you deploy the Lean theorem prover and check whether the theorem was indeed proven.

#### What "equivalent" means (~01:19–01:20)

The goal is a box that takes natural language math in and produces equivalent formal language math out, where equivalence means **semantic equivalence**: the semantic content of, say, the Pythagorean theorem going in must be the same as the semantic content of the Lean coming out — it has to talk about right-angle triangles, and the relationship must be the same.

The task they set themselves: build that box at least 1000× smaller than frontier models, maybe smaller still, and train it so it **outperforms the largest frontier models on this one task of autoformalization**.

#### Semantic alignment and semantic contrastive learning (~01:20–01:22)

The property he proposes is **semantic alignment**. The concept isn't new in general — people have discussed it in many settings — but in mathematics it takes a particular meaning: if two objects represented in different modalities have the same semantic content, they should be **close by in the model's embedding space**; if their semantic content differs, they should be **far apart**.

Imbuing the model with this property makes it much more effective at autoformalization, and specifically far more effective at retrieval time.

The value isn't confined to natural-to-formal math translation. It also covers code translation from one language to another, going from a specification to a circuit, and connecting definitions from different areas of math — seeing relationships between definitions across areas and thereby discovering new math — all doable with very small-scale models, without frontier model access.

They trained their models using a recipe they call **semantic contrastive learning**, imbuing the model with the property. The result was a far more powerful model than frontier models on all the benchmarks they tested.

#### Extending to code translation (~01:22–01:23)

They're now taking the idea into code translation: a tool that takes programs in legacy languages like COBOL and translates them into Python, deploying verification tools and automated testing tools on the input program.

The neat design argument: in this setting you don't need a specification, because **the input program is the specification**. They use LLM-driven symbolic execution to generate a test suite from the input program, then run that suite against the output to check whether the input and output programs are semantically equivalent. He notes the strong business case for code translation.

#### Takeaway (~01:23–01:24)

In settings where you have access to formal objects — translating between formal objects, or from an informal object into a formal object in another modality — imbuing the model with the property of semantic alignment is a good way to build a system that scales: much smaller in size, yet still able to scale to very large codebases.

### Quotes

> "Often human-written proofs are incomplete, meaning they are missing steps, and the human mathematicians may not be aware of that. Worse, sometimes the proofs are incorrect." (~01:19)

The real motivation for autoformalization isn't formalist purity — it's that human proofs contain errors.

> "If two objects which are represented in different modalities have the same semantic content, then we want them to be close by in the embedding space of the model." (~01:21)

Semantic alignment in one sentence.

> "In this setting, we don't need specifications because the input program is the specification." (~01:23)

Why code translation is an easier formalization target than math.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Autoformalization | 自然語言數學 → 形式語言數學的翻譯任務 | Translating natural language math into formal language math | 本場的核心問題 / the talk's central problem |
| Lean | 定理證明語言與證明器,用於驗證翻譯結果 | Theorem-proving language and prover used to check the translation | 也提及「其他定理證明語言」/ he also allows for other theorem-proving languages |
| Semantic alignment | 語意相同的跨模態物件在 embedding 空間靠近的性質 | The property that cross-modal objects with identical semantics sit close in embedding space | 概念本身不新,但在數學中有特定意義 / not a new concept generally, but specific here |
| Semantic contrastive learning | 把 semantic alignment 灌進模型的訓練配方 | The training recipe that imbues the model with semantic alignment | 產出模型比前沿模型小 1000 倍以上 / yields a model 1000×+ smaller than frontier models |
| COBOL → Python 翻譯工具 | 遺留程式碼翻譯,搭配驗證與自動測試 | Legacy code translation with verification and automated testing | 用 LLM 驅動符號執行生成測試集 / test suite generated by LLM-driven symbolic execution |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| VJ | Vijay Ganesh |
| the the model with the property | imbuing the model with the property(字幕重複)/ transcript stutter |
| odd formalization | autoformalization |

## 待確認 / To Verify

- 模型/系統的正式名稱:整場都以「our model」稱呼,未給名稱。/ The model or system has no name in the talk — it's only "our model".
- 「在所有測試 benchmark 上都贏過前沿模型」的 benchmark 名稱與數字皆未提及。/ Neither the benchmark names nor the numbers behind "outperforms frontier models on all benchmarks tested" were given.
- 「至少小 1000 倍」的比較基準(參數量?推論成本?)未說明。/ What the 1000× smaller comparison is measured in — parameters, inference cost, or something else.
- 論文出處未提及,需另行查找 Georgia Tech / Vijay Ganesh 團隊的相關發表。/ No paper was cited; the corresponding publication needs to be located separately.
- COBOL → Python 工具是否已公開或商業化,講者僅說「有很強的商業誘因」。/ Whether the COBOL → Python tool is public or commercial; he only said there's a strong business case.
