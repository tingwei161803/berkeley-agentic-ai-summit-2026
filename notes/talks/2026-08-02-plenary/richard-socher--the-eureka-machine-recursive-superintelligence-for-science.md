---
title: "The Eureka Machine: Recursive Superintelligence for Science"
title_zh: "Eureka Machine:為科學而生的遞迴超智慧"
speaker: "Richard Socher"
affiliation: "Founder/CEO, Recursive Superintelligence"
type: talk
stage: Plenary
date: 2026-08-02
session: "Session 2: Frontier Research"
video: "https://www.youtube.com/watch?v=I2PosBXwoPI&t=502s"
video_range: "00:08:22–00:21:39"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [recursive-self-improvement, ai-for-science, auto-research, benchmarks, superintelligence]
---

# Eureka Machine:為科學而生的遞迴超智慧(The Eureka Machine: Recursive Superintelligence for Science)

**一句話總結**:把「自動化所有未來發明」當成終極發明,而通往那裡的路徑是先讓 AI 自動化 AI 研究本身——他們的 RSI 系統已經在三個公開 benchmark 上超越了社群多年的累積成果。
**One-line summary**: If the ultimate invention is the one that automates all future inventions, the road there runs through AI automating AI research first — and their recursive-self-improvement system has already beaten years of community effort on three public benchmarks.

## 中文筆記

### TL;DR

- **「Eureka Machine」是他個人版本的「登陸火星」**:一台自動化人類所有未來發明的機器。要造出它,路上必得先做出 **recursive self-improving superintelligence(RSI)**。
- **Eureka Machine 有四根支柱**:LLM 承載的現有人類知識 → 科學量測資料 → 模擬 → 實體實驗室自動化;四根支柱之上跑一個「相當於 5,000 個 PhD」的 agent swarm。
- **從「AI 的科學」開刀**:自動化科學,最該先自動化的就是 AI 研究本身。今年才變得可能,因為 **AI 就是程式碼,而 AI 已經會寫程式**,而且能撐的時間跨度越來越長。
- **不是紙上談兵**:他們的 RSI 系統在 nanochat、nanoGPT speedrun、NVIDIA 的 **SOL-ExecBench** 三個 benchmark 上,都超越了成千上萬人(與他們的 agent)多年累積的成果——而且產出的是**真發明**(例如把 hash table 塞進 transformer、新的 momentum 形式),不是調超參數。
- **我們離智慧的上限「天文級地遠」**:AI = 預測(數學上等價於壓縮)× 行動 × 目標;光以最單純的視覺智慧為例,上限是數以兆計的感測器、從量子不確定性到重力波的全頻譜——所以「AI 走不了多遠」的說法完全站不住腳。

### 重點整理

#### 為什麼是現在:技術是唯一的永續成長來源(約 00:09–00:13)

他從 **open-ended evolution(開放式演化)** 講起,說這是 AI 社群至今仍相對低估的一個過程:生物演化花了十億年以上才「發明出眼睛」,技術演化把時間壓縮到數千年,而 AI 現在把週期壓到以週計。

他引 Marc Andreessen 的說法主張**技術是唯一永續的成長來源**,並更進一步:**沒有任何「物質性」問題是更多技術解不掉的**(心理與政治問題另當別論)。所以在他看來,不加速反而才是更大的危險——那等於讓更少的人得以繁盛。

金句式的自我定位:**我們這代人太晚出生,趕不上探索地球;太早出生,趕不上探索星辰;但正好趕上打造超智慧。** 而且這次的跳躍會比過去快得多:1903 年還沒有人類實現持續動力飛行,60 年後人類登月;而現在的加速技術主要在軟體裡,只會更快。

推論鏈很簡單:**更多科學 → 更多技術 → 更多成長 → 更多人類繁盛**。所以第一號目標就是加速科學發現。他花了很久思考這件事,寫成一本九月出版的書《The Eureka Machine》。

#### Eureka Machine 的四根支柱與 agent swarm(約 00:13–00:16)

1. **現有的人類知識**——今天主要由 LLM 承載。他直接回應了版權爭議:當這些模型開源之後,它們就像網際網路一樣,越來越成為全人類的資源。
2. **科學量測資料**——人類感官很有限,感知智慧的上限遠高於此,而打開上限的方式就是科學儀器的量測。
3. **模擬**——「**任何你能模擬、能驗證的東西,AI 終究會解掉**」。他說自己從來不特別驚訝 AI 能打贏西洋棋和圍棋,因為那能模擬、能驗證,於是能生出無限訓練資料。
4. **實體實驗室自動化**——還是有些東西模擬不了,那就得做機器人流程自動化、真的把實驗室自動化起來。

四根支柱之上是 **agent swarm**;理想上在你叫它去做實體實驗之前,它就已經具備「約 5,000 個不同 PhD」的等價能力。

而 Recursive 的做法是:**要自動化科學,沒有比「AI 這門科學」更該先下手的對象**。做法上是讓 AI 對自己的缺陷建立某種自我覺察——涵蓋從 pre-training 到 harness 的整條鏈路。他強調這在今年才變得獨特可行:**AI 就是程式碼,而 AI 已經會寫程式**,加上能處理的時間跨度越拉越長,才真的能讓 AI 對自己動工。

#### Auto research 的實測:三個 benchmark 上超越多年累積(約 00:16–00:19)

他先把概念切乾淨:**讓一個 AI 去改進「另一個」系統,那叫 auto research,不是真正的 recursive self-improvement**——但它是很有用的里程碑與踏腳石。

科學(以及 AI 研究)的流程可拆成三步:**ideation → implementation → validation**。實作端現在越來越強,驗證仍然很花時間,真正的問題是「你能想出多少真正新穎的點子」。

他們把 RSI 系統丟到三個已經被成千上萬人(常常還帶著自己的 agent 與好奇心)反覆刷過的 benchmark 上:

| Benchmark | 內容 | 結果 |
|---|---|---|
| **nanochat** | 很受歡迎的 auto research benchmark | 不到兩天就把 bits-per-byte 明顯壓下來 |
| **nanoGPT speedrun** | 追求越來越快的訓練演算法 | 超越既有紀錄 |
| **SOL-ExecBench** | NVIDIA 的 benchmark,評估 CUDA kernel(GPU 與 AI 程式碼之間的介面) | 有顯著跳躍 |

他特別強調**這不是調參**:系統做出了真正有用的發明,例如**把 hash table 併進 transformer**、**想出新的 momentum 形式**。而且這件事有直接經濟意義——kernel 效率決定 foundation model 的 **intelligence per dollar**;在動輒數十億美元的資料中心上多榨出 5–10% 效率,對公司來說是很可觀的結果。

#### 智慧的上限:我們還在起跑線(約 00:19–00:21)

他說自己試著給 AI 一個完整定義但找不到好的,最後歸結為三個主成分:**prediction(數學上等價於 compression)× actions × goals**,並由此展開他所謂的「十種智慧空間」。

以最單純的**視覺智慧**為例來標定我們的位置:電腦視覺至今大致停在人眼的電磁頻譜範圍,但人眼其實不怎麼樣(螳螂蝦的眼睛更厲害)。真正的上限是——不必是雙眼視覺,可以是數百萬、數兆個感測器;考慮這些感測器彼此還能與一個中央智慧通訊的光錐半徑;向下看到量子層級的不確定性,向上看到重力波,再把這一切融合、疊上更多層次的物件抽象。

結論:**在許多智慧空間裡,我們距離上限「天文級地遠」**——所以這仍然是極令人興奮、極值得投入的研究領域。

### 金句

> "Our generation was too late to explore the earth, too early to explore the stars, but we're right on time to build superintelligence."(約 00:12)

太晚探索地球,太早探索星辰,正好趕上造超智慧。

> "Everything you can simulate, anything you can essentially verify, AI will obviously solve."(約 00:14)

這句話同時解釋了為什麼棋類早就被攻破,以及為什麼「可模擬 / 可驗證」是他四根支柱裡的關鍵一根。

> "It's not just like tuning hyperparameters — it makes some truly useful inventions, like incorporating hash tables into transformers."(約 00:18)

auto research 已經不只是搜參數空間。

> "We're literally astronomically far away from the upper bounds across many of the different spaces of intelligence."(約 00:21)

對「AI 快到頂了」的直接反駁。

## English Notes

### TL;DR

- **The "Eureka Machine" is his personal version of going to Mars**: the ultimate invention — a machine that automates all of humanity's future inventions. Getting there requires building recursive self-improving superintelligence (RSI) along the way.
- **Four pillars**: existing human knowledge (now carried by LLMs) → scientific measurement data → simulation → automated physical labs. On top of them runs an agent swarm with the equivalent of ~5,000 PhDs.
- **Start with the science of AI itself.** This became uniquely possible this year because AI *is* code and AI can now write code — over increasingly long time horizons.
- **Receipts, not slideware**: their RSI system beat years of accumulated community work on nanochat, the nanoGPT speedrun, and NVIDIA's **SOL-ExecBench** — and produced genuine inventions (hash tables inside transformers, new forms of momentum), not hyperparameter sweeps.
- **We are astronomically far from the upper bounds of intelligence.** AI decomposes into prediction (mathematically equivalent to compression) × actions × goals; even the simplest case, visual intelligence, has an upper bound of trillions of sensors spanning quantum uncertainty to gravitational waves.

### Key Points

#### Why now: technology as the only perpetual source of growth (~00:09–00:13)

He opens on **open-ended evolution**, a process he thinks the broader AI community still underexplores. Biological evolution took over a billion years to invent the eye; technological evolution compressed the cycle to millennia; AI now runs it in weeks.

Citing Marc Andreessen, he argues technology is the only perpetual source of growth — and goes further: **there are no material problems that cannot be solved with more technology** (psychological and political problems being a different beast). On that view, *not* accelerating is the bigger danger, because it means fewer people get to flourish.

His framing line: our generation was too late to explore the earth, too early to explore the stars, but right on time to build superintelligence. And this jump will be faster than previous ones — in 1903 no human had achieved sustained powered flight, and 60 years later we landed on the moon; today the accelerating technology lives in software, so it compounds faster still.

The chain is simple: more science → more technology → more growth → more human flourishing. Hence goal number one is accelerating scientific discovery — the subject of his book, *The Eureka Machine*, out in September.

#### The four pillars and the agent swarm (~00:13–00:16)

1. **Existing public knowledge**, now largely encoded in LLMs. He addresses the copyright discomfort head-on: once these models are open source, they become a resource for humanity in the way the internet did.
2. **Scientific measurement data**, because human senses are severely limited and the ceiling on perceptual intelligence is unlocked by instruments, not eyes.
3. **Simulation** — "everything you can simulate, anything you can essentially verify, AI will obviously solve." He was never surprised that chess and Go fell: simulate, verify, generate unlimited training data.
4. **Robotic process automation of physical labs**, for everything that can't yet be simulated.

Above the pillars sits an **agent swarm** that ideally carries the equivalent of ~5,000 distinct PhDs before you ever ask it to run a physical experiment.

Recursive's angle: if you're automating science, the best science to start with is the science of AI itself. That means letting the system build a form of self-awareness about its own shortcomings across the whole pipeline, from pre-training through harnesses.

#### Auto research, measured: three benchmarks (~00:16–00:19)

He draws a clean line first: **asking one AI to improve some other system is auto research, not true recursive self-improvement** — but it's a useful milestone on the way.

Science, and AI research, is three steps: ideation, implementation, validation. Implementation keeps improving, validation still costs time, and the live question is how many genuinely novel ideas the system can generate.

They pointed their RSI system at three benchmarks thousands of people had already worked on, often with their own agents:

| Benchmark | What it measures | Result |
|---|---|---|
| **nanochat** | Popular auto-research benchmark | Bits-per-byte reduced significantly in under two days |
| **nanoGPT speedrun** | Ever-faster training algorithms | Beat prior records |
| **SOL-ExecBench** | NVIDIA benchmark for CUDA kernels — the interface between GPUs and AI code | Significant jump |

The point he stresses: this is not hyperparameter tuning. The system produced real inventions — incorporating hash tables into transformers, novel forms of momentum. And it matters commercially: kernel efficiency drives **intelligence per dollar**, and squeezing 5–10% more out of a multi-billion-dollar data center is a very significant end result.

#### The ceiling: we've barely started (~00:19–00:21)

He tried to define AI properly, found no good definition, and settled on three principal components: **prediction (mathematically equivalent to compression) × actions × goals**, from which he derives ten "spaces of intelligence."

Take the simplest one, visual intelligence. Computer vision still mostly lives inside the electromagnetic band of the human eye — and human eyes aren't that good (mantis shrimp have better ones). The actual upper bound isn't binocular vision at all: millions or trillions of sensors, spread as far apart as the light cone still permits them to talk to one central intelligence, seeing down to quantum uncertainty and up to gravitational waves, then fusing all of it across many more layers of object abstraction.

So when people say AI won't go much further: we are literally astronomically far from the upper bounds in many spaces of intelligence — which is exactly what makes the area worth researching.

### Quotes

> "Our generation was too late to explore the earth, too early to explore the stars, but we're right on time to build superintelligence." (~00:12)

> "Everything you can simulate, anything you can essentially verify, AI will obviously solve." (~00:14)

Why board games fell early, and why "simulatable / verifiable" is the load-bearing pillar.

> "It's not just like tuning hyperparameters — it makes some truly useful inventions, like incorporating hash tables into transformers." (~00:18)

> "We're literally astronomically far away from the upper bounds across many of the different spaces of intelligence." (~00:21)

A direct rebuttal to the "AI is plateauing" story.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Recursive (Recursive Superintelligence) | 他的新公司,目標是自動化科學,並從 AI 自身的科學開始 | His new company: automate science, starting with the science of AI itself | 主持人介紹時提到募資 $650M / moderator cited a $650M raise |
| The Eureka Machine（書 / book） | 九月出版,論述 AI 如何解鎖科學發現的新時代 | Book out in September on AI unlocking a new era of scientific discovery | 全名 *The Eureka Machine: Why AI Is the Key to Unlocking a New Era of Scientific Discoveries* |
| nanochat | 受歡迎的 auto research benchmark,他們兩天內顯著壓低 bits-per-byte | Popular auto-research benchmark; bits-per-byte cut significantly in under two days | |
| nanoGPT speedrun | 追求更快訓練演算法的 speedrun benchmark | Speedrun benchmark for faster training algorithms | |
| SOL-ExecBench | NVIDIA 的 CUDA kernel benchmark,以硬體 Speed-of-Light 上限為標尺 | NVIDIA's CUDA-kernel benchmark, scored against hardware speed-of-light bounds | github.com/NVIDIA/SOL-ExecBench |
| MetaMind / You.com | 他先前創辦的兩家公司(主持人介紹) | His two earlier companies (from the moderator's intro) | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Richard so / Soccer | Richard Socher |
| recursive super intelligence（公司名） | Recursive / Recursive Superintelligence |
| Metammind | MetaMind |
| Mark Andre | Marc Andreessen |
| neonets / recursive neonets | recursive neural nets |
| soul execbench | SOL-ExecBench |
| NanoGPD speedrun | nanoGPT speedrun |
| nano chat | nanochat |
| "AI is code and AI can't code" | "AI is code and AI *can* code" |
| ideulate | ideate |
| LMS / LM | LLMs / LLM |
| scurves | S-curves |

## 待確認 / To Verify

- Recursive 的 **$650M** 募資數字出自主持人 Igor Babuschkin 的介紹,講者本人未提;正式數字待查。/ The $650M raise came from the moderator's intro, not the speaker; confirm the official figure.
- **nanoGPT speedrun** 是否即社群常稱的 `modded-nanogpt` speedrun,講者未指明版本。/ Whether this is the community's `modded-nanogpt` speedrun — the speaker didn't specify.
- 三個 benchmark 的**具體改善幅度**講者未給數字(只說 "significantly" / "significant jump"),需看投影片。/ No numbers given for the improvements; check the slides.
- 「十種智慧空間(10 different spaces of intelligence)」的完整清單只在投影片上,逐字稿未列。/ The full list of the ten spaces of intelligence is only on the slide.
- 「把 hash table 併進 transformer」的具體做法與是否有公開發表,待查。/ What "incorporating hash tables into transformers" concretely means, and whether it's published.
