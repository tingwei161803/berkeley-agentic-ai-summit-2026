---
title: "Redefining the Token Efficiency Frontier with Diffusion LLMs"
title_zh: "用 Diffusion LLM 重新定義 Token 效率的前沿"
speaker: "Aditya Grover"
affiliation: "Co-Founder/CTO, Inception Labs"
type: talk
stage: Atlas
date: 2026-08-01
session: "Session 1: Foundational Capabilities"
video: "https://www.youtube.com/watch?v=WeriQic-QW0&t=2475s"
video_range: "00:41:15–00:53:30"
transcript: "tmp/[English (auto-generated)] Atlas Stage - August 1st - Morning Session [DownSub.com].srt"
status: draft
tags: [diffusion-llm, inference-efficiency, parallel-decoding, inception-labs, agents]
---

# 用 Diffusion LLM 重新定義 Token 效率的前沿(Redefining the Token Efficiency Frontier with Diffusion LLMs)

**一句話總結**:AI 的每一次大躍進都來自「把某件事平行化」——先是 GPU 平行化矩陣乘法,再是 Transformer 平行化訓練,而下一步是用 diffusion 平行化**生成**本身;當智慧本身已不稀缺,真正的新貨幣是 intelligence per watt。
**One-line summary**: Every major leap in AI came from parallelizing something — GPUs parallelized matrix multiplication, Transformers parallelized training, and diffusion parallelizes *generation* itself; now that intelligence is abundant, the new currency is intelligence per watt.

## 中文筆記

### TL;DR

- **一條主線貫穿整個 AI 史:平行化。** 90 年代末硬體能平行跑矩陣乘法 → Transformer 讓訓練能平行(擺脫 RNN / LSTM「每一塊錢算力能學多少」的瓶頸)→ diffusion 在視覺取代 GAN → 現在把同樣的想法搬到文字,平行化**解碼**。
- **文字難做 diffusion,是因為 diffusion 是為連續模態發明的**:影像有很自然的加噪與去噪數學;文字是離散的,「什麼叫加噪、什麼叫原則性的去噪」本身就很難定義並規模化訓練。
- **Mercury 的商業意義是「速度買到什麼」**:在 Artificial Analysis 的圖上,Mercury 和同量級的速度優化模型(Claude Haiku、GPT-5 mini)品質相當,但快得多;而 **Mercury 2 能做 reasoning,卻仍比 GPT-4.1 這類非 reasoning 模型更快**——等於可以把 reasoning 模型部署在原本只能放非 reasoning 模型的位置。

### 重點整理

#### 主線:平行化是 AI 的第一性原理(約 00:42–00:44)

Grover 開場說,他要接續前面幾場演講的元素,定義他認為的「generative AI 的新基礎」:某種極快、極有效率、建立在 diffusion 之上的東西。而所有這些進展的核心,是一個信念:**平行化是計算機科學的基本概念,是 AI 的基本概念,也會是指向未來的基本信念。**

三個轉捩點:

1. **1990 年代末**:硬體終於能夠平行執行一個非常簡單卻基本的運算——矩陣乘法。這是今日 generative AI 世界的決定性時刻。
2. **Transformer**:架構層面的平行化,讓 AI 模型能平行訓練。這讓我們從 RNN / LSTM 那個「每花一塊錢算力能學到多少」被根本卡死的世界,進入能訓練巨型語言模型的新時代。
3. **演算法層面**:視覺領域的 diffusion 取代了當時主流的 GAN,成為高效率、高保真生成影像與影片的主流做法。

而最新的一波,是把同樣的想法帶進文字。

#### 為什麼文字很難,以及 Mercury 怎麼做(約 00:44–00:46)

- **根本困難**:diffusion 是為**連續模態**發明的。影像有非常自然的「加噪」概念,以及對應的、數學上有依據的原則性去噪理論。**文字是離散的**,這讓「什麼是好的加噪 / 去噪定義,而且能在規模上訓練」變得根本地困難。
- **Inception 的做法**:不像今天幾乎所有語言模型那樣一次生成一個 token(底下那條 autoregressive 路線),而是設計出一套**對文字去噪**的方式:從一段完全是亂碼的東西開始,送進神經網路(架構可以是任意的,他們用 Transformer),訓練它修掉輸入裡的雜訊。這樣模型能在文字中找到結構,並在**短得多的時間內**生成連貫內容——因為它是**平行預測所有被去噪的 token**。

#### Text diffusion 的時間線(約 00:46–00:48)

- **2019**:denoising diffusion 在影像上起飛,Midjourney 以及 Google、OpenAI 等實驗室做出大規模高品質影像生成的示範。
- **接下來數年**:整個研究社群的努力,最後在他其中一位共同創辦人的實驗室做出突破——**第一個在文字上達到 GPT-2 同等水準的 diffusion 模型**。
- **2024**:GPT-2 早就不是語言模型的成功標準了,於是他們決定成立 **Inception**,把這個想法真正做到規模。
- **幾個月後**:推出 **Mercury**,第一個商業規模的 diffusion language model,能做程式碼編輯與生成、數學解題、常識推理等任務,而且極快。這也吸引了學界與業界許多知名人物的注意。
- **再幾個月後**:Google、Nvidia、Alibaba 等實驗室紛紛跟進推出自己的 diffusion LLM 計畫。
- **2026 年稍早**:推出第二代 **Mercury 2**,這一代具備 **reasoning** 能力。而且 **diffusion 的 reasoning 看起來跟 autoregressive LLM 的 reasoning 非常不一樣**。

#### 用 Artificial Analysis 的圖說話(約 00:48–00:49)

X 軸是速度(tokens per second,越右越好),Y 軸是 Artificial Analysis 定義的品質指數(涵蓋一系列 agentic benchmark)。比較對象是各家實驗室**速度優化區間**的 SOTA 模型——Claude Haiku 系列、GPT-5 mini 這類。

結論:**Mercury 在同量級模型中拿到相當的品質,但快得多**,因為它是平行去噪 token,徹底脫離逐字生成的典範。

#### 三個落地案例:速度到底買到什麼(約 00:49–00:53)

- **語音 / 客服 agent**:你在意的不只是智慧,還有回應時間——尤其 **time to first token** 對客服語音應用極度關鍵。Mercury 定義了一條不同的前沿:在極短的 first-token 延遲下拿到很好的智慧。更關鍵的是,**Mercury 2 能做 reasoning,卻仍比目前多數語音公司在生產環境用的 GPT-4.1(非 reasoning 模型)更快**——「這就是速度買到的東西:你可以把 reasoning 模型部署在原本只放得下非 reasoning 模型的地方。」
- **硬體註腳**:他們所有部署都在 **Nvidia** 硬體上,速度優勢純粹來自 diffusion 與平行生成。因此像 **Cerebras、Groq** 這類新硬體的加速效果,理論上可以與 text diffusion **疊加**。
- **搜尋**:除了速度還在意成本;他展示準確率對速度、準確率對成本兩張圖,結論同樣是「能真正上生產的模型必須在三者間取得好的組合」,而 Mercury 在這個空間也取得很好的平衡。
- **Coding**:「我已經無法想像沒有 coding agent 的生活。」但主 agent 往往極度囉唆、吃掉大量 token,而那並不總是你需要的。要把 token 經濟壓到可持續,**Augment Code 這類公司把 Mercury 與 Opus 這種重量級模型搭配使用**,取得延遲與成本的良好平衡。

#### 結語:新的貨幣是 intelligence per watt(約 00:53)

「如果你看智慧的前沿,我們已經到了一個對很多應用來說智慧夠好的階段。現在真正重要的,是當我們替周遭所有人創造價值時,要開始思考一種新的貨幣:**intelligence per watt**。而 diffusion LLM 看起來是重新定義那條前沿的一個很好的賭注。」

### 金句

> "Parallelization is a fundamental concept for computer science, fundamental concept for AI, and a fundamental belief that will also guide towards the future."(約 00:42)

整場的主軸,也是他把 GPU、Transformer、diffusion 串成一條線的方式。

> "Mercury 2 can do reasoning and still be faster than a GPT [4.1] model. So that's what speed buys you — you can actually deploy reasoning models at the speed of, or even better than, non-reasoning models."(約 00:51)

這句話最精準地說明了「快」的商業價值:不是省時間,是解鎖原本放不進去的能力。

> "The new currency of intelligence per watt — and diffusion LLMs seem like a really good bet to redefining that frontier."(約 00:53)

收尾金句。

## English Notes

### TL;DR

- **One thread runs through all of AI: parallelization.** Late-90s hardware parallelized matrix multiplication; the Transformer parallelized training (escaping the RNN/LSTM ceiling on how much you could learn per dollar of compute); diffusion displaced GANs in vision; and the current wave brings that idea to text by parallelizing *decoding*.
- **Text is hard for diffusion because diffusion was invented for continuous modalities.** Images have a natural notion of adding noise and a sound mathematical theory of principled denoising. Text is discrete, which makes "what is a good noising and denoising process, trainable at scale" fundamentally difficult.
- **The commercial story is what speed buys you.** On Artificial Analysis's chart, Mercury matches the quality of comparable speed-optimized models (Claude Haiku, GPT-5 mini) while being much faster — and **Mercury 2 reasons and is still faster than non-reasoning models like GPT-4.1**, which means you can deploy a reasoning model where only a non-reasoning one used to fit.

### Key Points

#### The thread: parallelization as AI's first principle (~00:42–00:44)

Grover opened by saying he'd pick up elements from the preceding talks to define what he believes is the new foundation for generative AI: something extremely fast and efficient built on diffusion. At the heart of every advance he cites is one belief — parallelization is a fundamental concept for computer science, for AI, and for what comes next.

Three inflection points: in the late 1990s, hardware could finally execute a simple but basic operation, matrix multiplication, in parallel, which turned out to be the defining moment for today's generative AI. A few years later, the Transformer parallelized *training*, taking the field out of the RNN/LSTM world that was fundamentally bottlenecked by how much could be learned per dollar of compute and into an era of massive language models. And on the algorithm side, diffusion replaced GANs as the dominant way to generate images and video efficiently and at high fidelity.

#### Why text is hard, and how Mercury works (~00:44–00:46)

Diffusion was invented for continuous modalities: for images there's a natural notion of what it means to add noise and a good mathematical theory of principled denoising. Text is discrete, which makes it fundamentally hard to define noising and denoising processes that can be trained at scale.

Inception's approach: instead of generating tokens sequentially, one at a time — the autoregressive paradigm essentially every language model uses today — start from something completely gibberish, pass it through a neural network (any architecture; they use Transformers), and train that network to fix the noise in its input. That's how the model finds structure in text and produces something coherent in far less time, because it predicts all the denoised tokens **in parallel**.

#### A timeline of text diffusion (~00:46–00:48)

Denoising diffusion took off for images around 2019, when Midjourney and labs including Google and OpenAI demonstrated large-scale, high-quality image generation. It took years of work by the whole research community to reach a breakthrough in one of his co-founders' labs: a diffusion model for text that reached parity with GPT-2. By 2024, GPT-2 was no longer a meaningful bar for language, which is when they formed **Inception** to take the idea to scale.

A few months later they launched **Mercury**, the first commercial-scale diffusion language model — capable of code editing and generation, mathematical problem solving, and common sense at scale, and extremely fast. It caught the attention of notable people in both academia and industry, and within months labs from Google to Nvidia to Alibaba followed with their own diffusion LLM efforts. Earlier in 2026 came **Mercury 2**, which adds reasoning — and diffusion reasoning looks very different from how it works for autoregressive LLMs.

#### Reading the Artificial Analysis chart (~00:48–00:49)

X-axis: speed in tokens per second, higher is better. Y-axis: Artificial Analysis's quality index across a wide range of agentic benchmarks. The comparison set is the speed-optimized regime from the frontier labs — the Claude Haikus and GPT-5 minis of the world. Mercury lands at similar quality for models of similar size while being much, much faster, precisely because it denoises tokens in parallel rather than generating them sequentially.

#### Three case studies for what speed buys (~00:49–00:53)

- **Voice and support agents.** What matters isn't intelligence alone but intelligence plus response time — and **time to first token** is critical for customer-support voice applications. Mercury defines a different frontier: strong intelligence at very low time-to-first-token. The sharper point: **Mercury 2 reasons and is still faster than GPT-4.1**, the non-reasoning model in production at most voice companies. "That's what speed buys you — you can deploy reasoning models at the speed of, or better than, non-reasoning models."
- **A hardware footnote.** All their deployments run on **Nvidia** hardware; the speedup comes purely from diffusion and parallel token generation. So complementary advantages from newer hardware like **Cerebras** and **Groq** could stack on top of a diffusion model for text.
- **Search.** Here cost matters alongside speed. Two plots (accuracy vs. speed, accuracy vs. cost) make the same point: a production-deployable model needs a good combination of all three, and Mercury strikes a good balance in that space.
- **Coding.** "I can't imagine my life now without using coding agents." But the primary agent is often extremely verbose and token-hungry, and that isn't always what you need. To drive token economics toward something sustainable, companies like **Augment Code** use Mercury alongside heavyweight models like Opus, getting a good balance of latency and cost.

#### Closing: intelligence per watt (~00:53)

"If you think about the frontier of intelligence, we've reached a point where we have extremely good intelligence for a lot of applications. But now what's really important, as we build value for everyone around us, is to think about the new currency of intelligence per watt — and diffusion LLMs seem like a really good bet to redefining that frontier."

### Quotes

> "Parallelization is a fundamental concept for computer science, fundamental concept for AI, and a fundamental belief that will also guide towards the future." (~00:42)

The spine of the talk, and how he connects GPUs, Transformers, and diffusion into one line.

> "Mercury 2 can do reasoning and still be faster than a GPT [4.1] model. So that's what speed buys you — you can actually deploy reasoning models at the speed of, or even better than, non-reasoning models." (~00:51)

The clearest statement of why speed is a business argument, not a convenience one: it unlocks capability that previously didn't fit.

> "The new currency of intelligence per watt — and diffusion LLMs seem like a really good bet to redefining that frontier." (~00:53)

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Mercury | 第一個商業規模的 diffusion language model | The first commercial-scale diffusion language model | Inception Labs;arXiv 2506.17298 |
| Mercury 2 | 第二代,加入 reasoning 能力;仍比非 reasoning 模型快 | Second generation, adds reasoning while staying faster than non-reasoning models | 2026 年稍早推出 / launched earlier in 2026 |
| Artificial Analysis | 提供速度 vs. 品質指數比較圖的第三方評測機構 | Third-party benchmark source for the speed-vs-quality chart | 品質指數涵蓋多項 agentic benchmark |
| Augment Code | 把 Mercury 與 Opus 等重量級模型搭配使用的 coding agent 公司 | Coding-agent company pairing Mercury with heavyweight models like Opus | 用於降低延遲與成本 |
| Cerebras / Groq | 講者提到可與 text diffusion 疊加的加速硬體 | Accelerator hardware he suggests could stack with text diffusion | Inception 自身部署全在 Nvidia 硬體上 |
| GPT-4.1 / GPT-5 mini / Claude Haiku | 速度優化區間的對照模型 | Comparison models in the speed-optimized regime | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Adit Grover / Adita | Aditya Grover |
| the fusion LLMs / diffusion LMS | diffusion LLMs |
| auto reggressive | autoregressive |
| den noiseise / dnoising / D noiseis | denoise / denoising |
| GPD 2 / GPD 5 minis / GPD 4.1 | GPT-2 / GPT-5 mini / GPT-4.1 |
| claude haikus | Claude Haiku |
| Grock | Groq |
| quality index by artificial analysis | Artificial Analysis quality index |
| augment code | Augment Code |
| zero(句尾)| (自動字幕雜訊,非內容)/ caption noise, not content |

## 待確認 / To Verify

- 「2019 年 denoising diffusion 起飛,像 Midjourney 這樣的公司…」——Midjourney 成立於 2021,講者的時間點與公司舉例可能是口誤或簡化,需對照投影片。/ He dated denoising diffusion's takeoff to 2019 and cited Midjourney, which was founded in 2021 — likely a simplification; check the slide.
- 「其中一位共同創辦人的實驗室做出與 GPT-2 同等水準的文字 diffusion 模型」——他未點名是哪位共同創辦人與哪篇論文(Inception 共同創辦人為 Stefano Ermon、Aditya Grover、Volodymyr Kuleshov)。/ He didn't name which co-founder's lab or which paper achieved GPT-2 parity.
- Artificial Analysis 圖表的擷取日期與模型版本未標示。/ The snapshot date and model versions behind the Artificial Analysis chart weren't stated.
- Augment Code 案例中「Opus」的具體版本未說明。/ The specific Opus version in the Augment Code case study wasn't stated.
