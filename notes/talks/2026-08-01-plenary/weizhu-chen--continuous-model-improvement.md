---
title: "Continuous Model Improvement"
title_zh: "持續性的模型改進"
speaker: "Weizhu Chen"
affiliation: "Technical Fellow & CVP, Microsoft AI"
type: talk
stage: Plenary
date: 2026-08-01
session: "Session 3: Agentic AI Foundational Capabilities"
video: "https://www.youtube.com/watch?v=Tcn5Yb2K0h4&t=5823s"
video_range: "01:37:03–01:47:34"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [scaling, data, synthetic-data, distillation, harness]
---

# 持續性的模型改進(Continuous Model Improvement)

**一句話總結**:推動模型持續變好的是 compute、data、architecture、distillation 與 RL 五個引擎,但真正的槓桿不在模型本身——**先把模型周圍的一切最佳化再說**,而持續改進的前提是持續、大規模的部署,因為只有真實互動資料才知道哪裡壞了。
**One-line summary**: Five engines drive continuous model improvement — compute, data, architecture, distillation and RL — but the real leverage isn't the model itself: **optimize everything around it first**, and note that continuous improvement presupposes continuous deployment at scale, because only real interaction data tells you what's broken.

## 中文筆記

### TL;DR

- **Compute 有三個維度**:pre-training(更大模型、更多資料、更多 exploration)、post-training(簡單問題已解完,算力現在花在難問題、長程問題,以及**把 multi-agent 放進訓練而不只是推論**)、test-time compute(產品服務端,讓一整個模型家族協作)。
- **「Data is the king, everything else is the queen」**。合成資料的重點**不是品質而是覆蓋率**——能造出過去沒有的互補資料;而我們每天產生的人類資料,將成為合成資料的**種子**。
- **架構的第二個維度最常被忽略:推論成本**。模型最後能不能普及,是由**跑得多快、多便宜**決定的,所以**推論要在設計之初就定義好**。他認為資料比架構更能決定品質,架構則該多顧成本與效率。
- **蒸餾是機器學習的通則**:從網路資料學是向人類蒸餾,從產品遙測資料學也是,請人標註更是。**下一個更好的模型會建立在既有模型之上,而不是從零開始。** 而且——**更強的老師不代表更好的老師**,弱模型有時反而是好老師。
- **Harness 的兩句話**:一,**在想著優化模型之前,先把模型周圍的一切優化**;二,你今天建的 harness 有很多會**被模型吸收**,harness 會越來越簡單——但我們同時也在定義越來越複雜的場景。
- **持續改進 = 持續大規模部署**。不要只看 benchmark,要看生產環境的可用性;互動資料才是把模型變好的燃料。
- **最後一條也是他刻意留在最後的**:**人的參與仍然不可或缺**——尤其要確保自我改進是對齊人類價值,而不是模型自己想做的事。

### 重點整理

#### 引擎一:Compute 的三個維度(約 01:37–01:39)

第一個驅動力顯然是 **compute**——它是第一個 scaling engine,沒有算力什麼都做不了。多數改進本質上就是算力推出來的:算力多、訓練久,模型自然變好。**但算力還有第二層效果:它解鎖了大量實驗,而很多創新其實來自實驗與快速迭代。**

今天算力有三個維度:

1. **Pre-training**:大模型、更多資料,而**今天還多了 exploration**——可能來自模型、也可能來自人。探索得越多,模型就越好。這大致就是大家說的 pre-training scaling law。
2. **Post-training**:**簡單的問題今天已經解得差不多了**,所以算力現在集中在:怎麼解更難的問題、怎麼解更長的問題(long horizon),以及**怎麼在訓練階段就處理 multi-agent 問題——不只是在推論階段**。這可以稱作 post-training scaling law。
3. **Test-time compute**:用於產品服務,重點是**怎麼讓一整個模型家族彼此協作**。

#### 引擎二:Data,以及「覆蓋率比品質更重要」(約 01:39–01:41)

「**我們總說 data is the king,其他一切都是 queen;data 也是氧氣。**」資料是讓一切發生的第二個引擎。他分成幾塊:

- **Pre-training 資料**:pre-training 的進展多半來自資料——**每一次你把資料清得更乾淨、把資料刷新(網路資料每天都在變好、覆蓋越來越廣),模型就進步一次。**
- **合成資料的重點是覆蓋率**:「合成資料不只是品質問題,**最重要的是覆蓋率**——它能創造出比以前更多的互補資料。」
- **人類資料是種子**:他認為資料是未來最重要的東西。**我們每天創造的所有資料,大概都會成為合成資料的種子**——也就是說,合成資料會成為主流,而我們現有的資料,價值在於**怎麼用它產生更好的合成資料**。
- **Post-training 的資料就是 RL 環境**:關鍵在於**讓訓練時的 RL 環境跑起來和使用者實際使用時一模一樣**,這樣模型才會對真實產品情境有用。因為 RL 需要 trial and error,所以你必須把推論時會出現的東西搬進訓練裡,模型才學得到。**這很類似在訓練中建一個模擬環境,好讓你能大量生成資料。**

#### 引擎三:架構——別忘了推論成本(約 01:41–01:42)

模型架構很複雜,論文和細節極多,但他把它總結成**三個優化維度**:

1. **更高品質的模型**;
2. **更低的推論成本**——「**很多人直接忽略了第二點**」;
3. **支撐更長的 context 且更有效率**。

目標很簡單:**how can you make it better and cheapest?**

他的立場很清楚:**資料比模型架構更能決定模型品質;架構真正該多花心思的地方是推論成本與推論效率。** 因為**一個模型最後能不能流行起來,是由你能跑多快、能跑多便宜決定的**——他認為這比什麼都重要。**所以推論必須在一開始就被定義進去。** 另外,順著 GPU 的演進方向,設計上應該**往「更多計算、更少 I/O」走**。

#### 引擎四:蒸餾——機器學習其實一直都是蒸餾(約 01:42–01:44)

他認為機器學習裡很多事情**本質上就是蒸餾**,差別只在你是**從人類蒸餾**還是**從模型蒸餾**:

- 從網路上的既有資料學習 → 你在向人類蒸餾;
- 從產品的遙測互動資料學習 → 你也在向人類蒸餾;
- 請人幫你標註資料 → 你同樣在蒸餾他們的知識。

所以蒸餾一直都很普遍。**在產業界,蒸餾比從頭訓練有效率得多——你不需要從零建起任何東西。他相信下一個更好的模型,會建立在既有模型之上,而不是從零開始。**

**蒸餾也是一個很通用的模式**:你可以**建立多個 teacher**(因為讓學生從單一特定 teacher 學比較容易,而且多個 teacher 可以平行跑),最後蒸餾進一個模型。

但他也強調**蒸餾有一堆全新的研究問題**,不是簡單題:光是類型就有**強模型 → 強模型、強模型 → 弱模型,甚至弱模型 → 強模型**(這也是可能的)。而其中最反直覺的一條:**更強大的 teacher 模型,不代表它是更好的老師——這一點和人類非常像;而有時候弱模型反而可以是很好的老師。** 蒸餾這件事上「什麼都有可能」。

#### 引擎五:RL 的長處與三個痛點(約 01:44–01:45)

RL 今天運作得相當好:**它非常 effective(他特別更正:是有效,不是有效率)**,不論是可驗證還是不可驗證的問題都能解;它**特別適合修產品行為**——只要定義一個 grader、餵一些資料,就比其他做法有效率得多;而且它**能直接在真實環境裡運作**。他甚至認為 **RL + 蒸餾 + 合成資料,或許就足以讓我們走到自我改進。**

但 RL 也有明顯挑戰:

- **很慢**,他認為需要不少突破才能大幅加速;
- **更新非常增量**——跑起來會發現每次更新的幅度都很小,有時候一次 LoRA 級的更新其實就夠了;
- **另一面還是資料**:**驅動 RL 的就是資料,而資料對 RL 訓練只會更重要。他相信下一階段可能有 99.9% 的資料來自合成資料。**

#### Harness:先優化模型周圍的一切(約 01:45–01:47)

因為當天已經談了很多 harness,他講得很快,但留下兩句核心主張:

**第一,要優化的是整個系統,而 harness 是系統裡非常大的一塊——不要一開始就想著優化模型。** 他特地對台下的 builder 說:**在你想著優化模型之前,先把模型周圍的一切都優化過一遍。**

**第二,你今天建的 harness,有很多會在某個時點被模型吸收進去**,於是 harness 會變得越來越簡單——但**與此同時我們也在定義越來越複雜的場景、建越來越複雜的 harness**。這個吞噬過程會持續下去,沒有什麼是我們能改變的。

**還有一點他認為非常重要**:不要只在意 benchmark,**也要在意生產環境的可用性**——真實的互動資料對打造更好的模型非常有價值,那不是 benchmark 給得了的。因此:**持續的模型改進,真正需要的是持續的、大規模的部署**。當大量的人在用你的模型,你才能理解哪裡出了問題,才能從互動資料裡拿到洞見,也才能看到別的模型在同樣場景下是怎麼做的,並從中學習。

#### 收尾:下一輪的四個判斷(約 01:46–01:47)

1. **Scaling 還在有效,而且我們不知道天花板在哪裡。**
2. **模型已經能夠優化 harness,接下來也將能優化並改動另一個模型**——因為在這件事上模型比人更強,他認為這一定會發生。
3. **要優化的是整個系統;而合成資料將成為主流**,尤其是在下一代模型的訓練上。
4. **最後一點同樣非常重要:人的參與仍然不可或缺。** 我們仍然需要人來引導模型該怎麼做,**尤其是要確保這種自我改進對齊人類的價值,而不是去做模型自己想做的事。**

### 金句

> "We always say data is the king, everything else is the queen. And also data is oxygen."(約 01:39)

> "Synthetic data is not just about the quality. The most important is the coverage."(約 01:39)

合成資料的價值在於補上真實資料沒有的分布,不只是把品質拉高。

> "How popular a model becomes is finally going to be decided by how fast you're able to run it and how cheap you're able to run it. So we need to define the inference at the beginning."(約 01:41)

> "A more powerful teacher model doesn't mean it's a better teacher. That's very similar as humans."(約 01:43)

> "Before we think about optimizing the model, try to optimize everything around the model."(約 01:45)

整場演講給 builder 的一句話。

> "Continuous model improvement really requires continuous deployment at scale."(約 01:46)

> "Human involvement is still very essential … especially to make sure this self-improvement aligns with human values, instead of doing something the model wants to do."(約 01:47)

刻意留在最後一張投影片的一條。

## English Notes

### TL;DR

- **Compute has three dimensions**: pre-training (bigger models, more data, and now more exploration), post-training (the easy problems are solved, so compute goes to harder problems, long-horizon problems, and **multi-agent handled in training rather than only at inference**), and test-time compute for product serving, where a family of models has to interact.
- **"Data is the king, everything else is the queen."** What matters about synthetic data **isn't quality but coverage** — creating complementary data that didn't exist before; and the human data we generate daily becomes the **seed** for it.
- **Architecture's second dimension is the one people skip: inference cost.** How popular a model becomes is ultimately decided by **how fast and how cheap it runs**, so **inference has to be defined at the very beginning.** He'd bet on data over architecture for quality, and have architecture focus on cost and efficiency.
- **Distillation is the general pattern of machine learning**: learning from web data distills from humans, so does learning from product telemetry, so does human labeling. **The next better model will be built from existing models, not from scratch.** And counter-intuitively — **a more powerful teacher is not necessarily a better teacher**, while a weak model can sometimes teach well.
- **Two things about the harness**: first, **optimize everything around the model before you try to optimize the model**; second, much of what you build into the harness today **will be absorbed into the model**, so harnesses simplify — even as we keep defining more complicated scenarios.
- **Continuous improvement means continuous deployment at scale.** Don't optimize only for benchmarks; production usability and real interaction data are what actually make the next model better.
- **The point he deliberately saved for last**: **human involvement is still essential** — above all to ensure self-improvement aligns with human values rather than with what the model wants to do.

### Key Points

#### Engine one: three dimensions of compute (~01:37–01:39)

The first driver is obviously **compute** — the first scaling engine; without it you can't do anything. Most improvement is essentially compute-driven: more compute, train longer, the model gets better automatically. **But compute has a second-order effect: it unblocks a lot of experiments, and much of the innovation actually comes out of experimentation and fast iteration.**

Three dimensions today:

1. **Pre-training** — large models, more data, and **today also more exploration**, whether coming from the model or from humans. The more you explore, the better the model. This is roughly what people call the pre-training scaling law.
2. **Post-training** — **a lot of the simple problems are already solved**, so compute now focuses on how to solve harder problems, how to solve longer (long-horizon) problems, and **how to handle multi-agent problems in training, not just at inference.** Call it the post-training scaling law.
3. **Test-time compute** — for product serving, centered on **making a whole family of models interact together.**

#### Engine two: data, and why coverage beats quality (~01:39–01:41)

"**We always say data is the king, everything else is the queen. And data is oxygen.**" Data is the second engine that makes everything happen. Several parts:

- **Pre-training data** — most pre-training progress comes from data. **Every time you clean the data better, or refresh it (web data gets better and broader in coverage every day), the model improves.**
- **Synthetic data is about coverage** — "synthetic data is not just about the quality; the most important thing is the coverage," creating far more complementary data than before.
- **Human data is the seed** — he thinks data is the most important thing going forward, and **all the data we create every day will be the seed for synthetic data.** Synthetic data becomes the mainstream; the value of the data we already have lies in **how it produces better synthetic data.**
- **Post-training data means RL environments** — the key is **making the training-time RL environment run exactly as the user actually uses the product**, so the model becomes useful in real product scenarios. RL needs trial and error, so whatever appears at inference must be present in training for the model to learn it. **Very similar to building a simulation in training so you can generate data at volume.**

#### Engine three: architecture — don't forget inference cost (~01:41–01:42)

Model architecture is complicated and the literature is vast, but he summarizes it into **three optimization dimensions**:

1. **Higher model quality**;
2. **Lower inference cost** — "**a lot of people just ignore the second one**";
3. **Supporting much longer context, more efficiently.**

The goal is simple: **how do you make it better and cheapest?**

His position is explicit: **data matters more for model quality than architecture does; architecture should pay more attention to inference cost and inference efficiency.** Because **how popular a model becomes is finally decided by how fast and how cheap you can run it** — which he considers more important than anything else. **So inference must be defined at the beginning.** And tracking GPU advancement, designs should move toward **more compute and less I/O.**

#### Engine four: distillation is what machine learning has always been (~01:42–01:44)

He argues much of machine learning **is just distillation**, and the only question is whether you distill **from humans** or **from a model**:

- Learning from existing web data → distilling from humans;
- Learning from product telemetry and interaction data → distilling from humans;
- Asking humans to label data → distilling their knowledge.

So distillation was always ubiquitous. **In industry it's far more efficient than training from scratch — you don't need to build anything from zero. He believes the next better model will be built from existing models rather than from scratch.**

**Distillation is also a very general pattern**: build **multiple teachers** — it's easier for a student to learn from one specific teacher, and teachers can run in parallel — then distill into a single model.

But he stresses that **distillation brings a lot of new research problems**, not simple ones. The type space alone includes **strong → strong, strong → weak, and even weak → strong** distillation. And the most counter-intuitive finding: **a more powerful teacher model doesn't mean it's a better teacher — very much like humans — and sometimes a weak model can be a very good teacher.** With distillation, everything is possible.

#### Engine five: what RL is good at, and three pain points (~01:44–01:45)

RL works well today: **it is very effective** — he corrects himself mid-sentence, effective rather than efficient — at solving problems, verifiable or non-verifiable alike. It's **particularly good at fixing product behavior**: define a grader, add some data, and it's far more efficient than the alternatives. And it **works directly against the real environment.** He goes as far as saying **RL plus distillation plus synthetic data may be enough to get us to self-improvement.**

The challenges:

- **It's very slow** — he thinks real breakthroughs are needed to make it much faster;
- **Updates are very incremental** — run an RL chain and you'll see each update is tiny; sometimes a LoRA-scale update is already good enough;
- **And on the other side it's data again** — **what drives RL is data, and data only becomes more important for RL training. He believes maybe 99.9% of the data will come from synthetic data in the next step.**

#### The harness: optimize around the model first (~01:45–01:47)

Since the day had already covered harnesses at length he moves fast, but two claims stand out.

**First: optimize the entire system. The harness is a very big part of that system — don't start by optimizing the model.** Speaking directly to the builders in the room: **before you think about optimizing the model, try to optimize everything around the model.**

**Second: a lot of what you build into the harness today will at some point be absorbed into the model**, so harnesses get simpler and simpler — **while at the same time we keep defining more complicated scenarios and building more complicated harnesses.** That absorption keeps going, and there's nothing we can change about it.

**One more point he flags as very important**: don't care only about benchmarks; **care about production usability.** Real interaction data is extremely valuable for building a better model in ways benchmarks are not. Hence: **continuous model improvement really requires continuous deployment at scale.** When a lot of people use your model, you can understand what's going wrong, extract insight from interaction data, and see what other models do in the same scenarios and learn from them.

#### Closing: four calls for the next round (~01:46–01:47)

1. **Scaling keeps working, and we don't know where the ceiling is.**
2. **Models can already optimize the harness, and will also be able to optimize and change another model** — because models are better than humans at this. He thinks it's going to happen.
3. **Optimize the whole system; synthetic data becomes the mainstream**, especially for the next round of model training.
4. **And equally important: human involvement is still essential.** We still need humans to guide the model — **above all to make sure this self-improvement aligns with human values, instead of doing something the model wants to do.**

### Quotes

> "We always say data is the king, everything else is the queen. And also data is oxygen." (~01:39)

> "Synthetic data is not just about the quality. The most important is the coverage." (~01:39)

The value of synthetic data is filling distribution gaps real data never covered, not just raising quality.

> "How popular a model becomes is finally going to be decided by how fast you're able to run it and how cheap you're able to run it. So we need to define the inference at the beginning." (~01:41)

> "A more powerful teacher model doesn't mean it's a better teacher. That's very similar as humans." (~01:43)

> "Before we think about optimizing the model, try to optimize everything around the model." (~01:45)

The one line for builders in the room.

> "Continuous model improvement really requires continuous deployment at scale." (~01:46)

> "Human involvement is still very essential … especially to make sure this self-improvement aligns with human values, instead of doing something the model wants to do." (~01:47)

Deliberately saved for the final slide.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| LoRA | 講者為原論文最後作者(由主持人介紹時提及);演講中提到「LoRA 級的增量更新有時已足夠」 | He is the last author (mentioned in the host's introduction); in the talk he notes a LoRA-scale incremental update is sometimes already enough | 主持人稱其為「efficient LLM customization 的產業標準技術」 |
| RL 環境 / RL environments | Post-training 的「資料」形式:讓訓練環境與使用者真實使用情境一致 | The data form for post-training: make the training environment match real user usage | 他視之為 post-training 的核心工程 |
| Grader | 修產品行為的做法:定義 grader + 補資料,比其他方法有效率 | The way to fix product behavior: define a grader, add data — more efficient than alternatives | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Wu Chen / Wazu | Weizhu Chen |
| Laura | LoRA |
| pre-chaining / pre-chaning | pre-training |
| power training | post-training |
| posting | post-training |
| the I environment / the I training / the I chain | the RL environment / RL training / the RL chain |
| distear / distiller / diste / thisation | distill / distillation |
| honeys | harness |
| observed into the model | absorbed into the model |
| the lower update | the LoRA update |
| infants | inference |
| tri error | trial and error |
| SE improvement / set improvement | self-improvement |
| IIL | LLM |

## 待確認 / To Verify

- 「so you are able to generate an Olympic datas」語意不明,推測為「generate unlimited data」或類似說法,需看投影片確認。/ "Generate an Olympic datas" is unintelligible — likely "generate unlimited data" or similar; check the slides.
- 「with this DF model … this is very popular as well」中的 "DF model" 指涉不明(可能是某個具體模型名稱)。/ The "DF model" reference is unclear — possibly a specific model name.
- 「99.9% 的資料來自合成資料」為講者對下一階段的預期,非既有數據。/ The "99.9% synthetic data" figure is his forward-looking expectation, not a measured statistic.
- 演講未點名任何具體 Microsoft 模型或產品;若要補上對應的模型家族名稱需另行查證。/ No specific Microsoft model or product was named; mapping his remarks to a model family would require separate verification.
