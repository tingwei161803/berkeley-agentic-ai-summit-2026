---
title: "Scaling RL for Coding Agents - Lessons from Training SWE-1.7"
title_zh: "為 coding agent 擴展 RL:訓練 SWE-1.7 的經驗"
speaker: "Silas Alberti"
affiliation: "SVP of Research, Cognition"
type: talk
stage: Nexus
date: 2026-08-01
session: "Session 2: Coding & Web Agents"
video: "https://www.youtube.com/watch?v=ZIRc3EpzQJs&t=817s"
video_range: "00:13:37–00:28:10"
transcript: "tmp/[English (auto-generated)] Nexus Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [reinforcement-learning, coding-agents, training-stability, async-rl, entropy-collapse]
---

# 為 coding agent 擴展 RL:訓練 SWE-1.7 的經驗(Scaling RL for Coding Agents - Lessons from Training SWE-1.7)

**一句話總結**:Cognition 用四次規模逐步放大的 RL 訓練跑(Kevin-32B → SWE-grep → SWE-1.6 → SWE-1.7)證明,coding agent 的進步不需要花俏的新點子,而是把 multi-turn RL、parallel tool calls、asynchronous RL、對抗 entropy collapse 這些「簡單的事」在規模上確實執行到位。
**One-line summary**: Across four increasingly ambitious training runs — Kevin-32B, SWE-grep, SWE-1.6, SWE-1.7 — Cognition found that progress on coding agents comes not from clever new ideas but from executing simple things at scale: multi-turn RL, parallel tool calls, asynchronous RL, and beating entropy collapse.

## 中文筆記

### TL;DR

- **四次訓練跑的主軸是「用當下的算力與人力,挑一個剛好夠有野心的問題」**:從 32 張 H200 + 幾位實習生的 Kevin-32B,一路做到跨三大洲的 SWE-1.7。
- **Multi-turn agentic RL 很早就贏過 single-turn**:Kevin-32B 在 KernelBench 上用 GRPO 做多輪訓練,曲線明顯高於單輪版本。
- **訓練穩定性是可觀測的**:他們發現模型 chain-of-thought 開頭「okay」的消失率(戲稱 not-okay ratio)是訓練發散的早期指標——模型愈接近崩潰,內心話愈焦躁。
- **Parallel tool calling 是延遲的關鍵**:SWE-grep 訓練後一回合可同時發出約 8 個 tool call,end-to-end 延遲大幅下降,且 reward 與並行度在訓練中同步上升。
- **Async RL 不只是吞吐量優化,而是地理上的解放**:把 trainer 與 rollout 分離後,SWE-1.7 得以在四個國家、三大洲的零散算力上訓練——因為 RL 只需傳輸稀疏的 weight update 與 token batch。
- **Entropy collapse 是 RL 的天花板**:調好 recipe 讓 entropy 幾乎不下滑,就能繼續往上推效能——這是對「RL 已經到頂、該回頭做 pre-training」說法的直接反駁。

### 重點整理

#### 起點:Kevin-32B,32 張 GPU 能做什麼(約 00:14–00:17)

團隊剛起步時只有幾位實習生和 32 張 H200,問題是「這樣的算力能做什麼真正有趣的事」。答案是挑一個**夠窄、夠可驗證**的題目:當時剛發表的 KernelBench——給一個 PyTorch 函式,要模型寫出能加速它的 CUDA kernel。

他們實作 GRPO 並讓它跑起來,而真正想探索的是「multi-turn agentic training 長什麼樣」——這在一年多前還相當新穎。結果很漂亮:multi-turn 訓練曲線明顯高於 single-turn,而且用一個 32B 級的開源 base model 就在該 benchmark 上贏過當時的 o3。

**「not-okay ratio」的軼事**:這個 base model 有個怪癖——thinking 一律以 "okay" 開頭。訓練愈往後,它的內心獨白愈焦躁:從 "okay amigos, I need to optimize this 3D tensor matrix multiplication" 演變成 "okay holy crap I need to get this code optimized"。他們把「開頭不是 okay 的比例」拿來當不穩定指標,發現它能提早預告整個 training run 的發散。

#### SWE-grep:把 context retrieval 變成可驗證的 RL 問題(約 00:17–00:19)

下一步要做「產品裡真的用得上的 agent」。coding agent 最吃重的子問題之一是**找到對的檔案**:給一個關於 codebase 的問題(例:VS Code 是怎麼高效實作 file watching 的?),輸出相關檔案清單。

好處是 reward 乾淨可驗證——直接對 ground-truth 檔案清單算 F1。他們據此訓了 agent,並自建 code search eval,在當時(Sonnet 4.5 時代)拿到該 eval 的 state of the art,最後 ship 進 Windsurf。

科學上最有意思的收穫是 **parallel tool calling**。當時多數 base model 都是一次一個 tool call 循序執行,Anthropic 的 Sonnet 剛開始一次發 1–3 個。他們的目標是壓低 end-to-end 延遲,所以直接優化並行度——SWE-grep 有時一回合能同時發出 8 個 tool call。訓練曲線上可以看到 reward 與「每回合並行 tool call 數」同步上升。搭配 Cerebras 晶片,mini 版本跑到約每秒 3,000 tokens。

#### SWE-1.6:穩定性與 asynchronous RL(約 00:19–00:23)

到這階段開始做真正端到端的前沿 coding model,並用 SWE-Bench Pro 這類真實 coding eval 衡量。SWE-1.6 當時在該 benchmark 上追平 Opus 4.5。

- **同樣的原則仍然適用**,只是資料要更多更難:內部的可驗證軟體工程任務 eval 在一次 RL 跑中從 **52% 推到 68%**。
- **模型會自己學會想更久**:平均 thinking token 從約 4,000 起步,整個訓練跑下來大約翻倍。
- **穩定性是被逼出來的工程**:典型失敗是跑到約 200 步就崩潰;診斷根因、修正後重跑,曲線幾乎沿著原路徑重走,但這次能撐過原本的崩潰點。每一次演算法改良就把 training horizon 從 200 步推到 300 步、再往後推。
- **Asynchronous RL**:把 trainer 與 rollout 分離——rollout 把一批批 group 丟進 data buffer,trainer 在 buffer 夠滿時取用,做完一步訓練再把 weight update 送回 rollout。代價是 **staleness**:inference policy 落後 training policy 幾步。

#### SWE-1.7:entropy collapse 與跨三大洲的訓練(約 00:23–00:27)

**Staleness 與穩定性其實是同一件事**:演算法穩定性愈好,能容忍的 staleness 就愈高;能容忍愈高的 staleness,就愈能把 inference engine 吃滿。換句話說,**更好的演算法直接換來更高的算力利用率**——這正是 SWE-1.7 的前提。

SWE-1.7 的定位用「成本 vs 效能」的二維圖呈現:以它的尺寸級別來說表現相當突出,能和大得多的模型競爭而便宜許多。base model 是 Kimi K2.7,同尺寸級的對照組包括同樣基於 Kimi 的 Composer 2.5 與 GLM 5.2。

- **Entropy collapse 是主要瓶頸**。當時外界不少「RL 已經到頂、勝負回到 pre-training」的說法,但他們想再推一把。RL 的養分來自 group 內的多樣性與新行為的發現,而這都可由 entropy 衡量;典型訓練跑中 entropy 一路下滑,崩塌時就撞到天花板。調整 recipe 後,他們讓 entropy 的下滑幾乎難以察覺(仍會降,但斜率平緩得多),效能因此得以繼續往上推。細節見他們的技術報告。
- **跨四國三大洲的訓練**。現在要找大塊連續的訓練叢集非常難,尤其在合理的時程內(可能得提前一年下訂)。反而容易找到的是這裡一小片、那裡一小片的零散算力。最後這次訓練跑橫跨**澳洲、馬來西亞、加拿大、美國**。
- **這只有 async RL 能做到**:訓練叢集在美國,rollout 叢集散布全球;inference 叢集把 training batch 送到訓練叢集,訓練叢集把 weight update 送回去。之所以能跨全球運作,是因為要傳的東西本來就稀疏——RL 的 weight update 稀疏,training batch 也只是 token。

### 金句

> "A lot of progress in research is just executing the simple things at scale."(約 00:27)

收尾時的團隊哲學:他們並不相信進步來自複雜花俏的點子。

> "The not-okay ratio … was an early indicator of an eventual divergence of the training run."(約 00:17)

模型崩潰前,連內心獨白的語氣都先變了。

## English Notes

### TL;DR

- **Each run was sized to the compute and team of the moment**: from Kevin-32B (a few interns and 32 H200s) to SWE-1.7 spanning three continents — the skill is picking a problem that is exactly ambitious enough.
- **Multi-turn agentic RL beat single-turn early on**: Kevin-32B used GRPO with multi-turn training on KernelBench and clearly outperformed the single-turn variant.
- **Training instability is observable before it happens**: they tracked a "not-okay ratio" — how often the model's chain of thought stopped starting with "okay" — as an early divergence indicator, and the model's inner monologue visibly got more frantic as collapse approached.
- **Parallel tool calling is the latency lever**: after RL, SWE-grep issued roughly eight tool calls per turn, and reward and parallelism climbed together through training.
- **Async RL is a geographic unlock, not just a throughput trick**: separating trainer from rollouts let SWE-1.7 train on scattered compute across four countries and three continents, because only sparse weight updates and token batches cross the wire.
- **Entropy collapse is the RL ceiling**: tuning the recipe so entropy barely declines is what let them keep pushing performance — a direct rebuttal of the "RL has plateaued, it's all pre-training now" narrative.

### Key Points

#### Kevin-32B: what can you do with 32 GPUs? (~00:14–00:17)

The team started as a few interns with 32 H200s, asking what could be genuinely interesting at that scale. The answer was to pick something **narrow and cleanly verifiable**: KernelBench had just come out — given a PyTorch function, write a CUDA kernel that speeds it up.

They implemented GRPO and got it working, but the real question was what **multi-turn agentic training** looks like, which was still novel a year earlier. It worked: the multi-turn curve sat clearly above the single-turn one, and a 32B-class open base model beat o3 on that benchmark.

**The "not-okay ratio" anecdote**: this base model had a quirk of always opening its chain of thought with "okay." As training progressed the monologue got increasingly unhinged — from "okay amigos, I need to optimize this 3D tensor matrix multiplication" to "okay holy crap I need to get this code optimized." Measuring how often the thought *didn't* start with "okay" turned out to be an early warning of an eventual diverging run.

#### SWE-grep: turning context retrieval into a verifiable RL problem (~00:17–00:19)

Next they wanted an agent good enough to ship. A core sub-problem in coding agents is **finding the right files**: given a question about a codebase (e.g., how does VS Code efficiently implement file watching?), return the list of relevant files.

The reward is clean and verifiable — F1 against the ground-truth file list. They trained an agent on it, built their own code search eval, hit state of the art on that eval in the Sonnet 4.5 era, and shipped it into Windsurf.

The scientifically interesting result was **parallel tool calling**. Most base models at the time called tools sequentially, one at a time; Anthropic's Sonnet had just started issuing one to three at once. Because the goal was end-to-end task latency, they optimized for doing as much as possible in parallel — SWE-grep would sometimes fire eight tool calls per turn. Over the run, both reward and parallel-tool-calls-per-turn rose together. Served on Cerebras hardware, the mini variant ran at roughly 3,000 tokens per second.

#### SWE-1.6: stability and asynchronous RL (~00:19–00:23)

Now they moved to real frontier coding models for end-to-end tasks, measured on realistic evals like SWE-Bench Pro, where SWE-1.6 matched Opus 4.5 at the time.

- **The same fundamentals applied**, just with more and harder data: an internal eval of verifiable software-engineering tasks went from **52% to 68%** over a single RL run.
- **The model learned to think longer on its own**: average thinking tokens started near 4,000 and roughly doubled over the run.
- **Stability was hard-won engineering**: a typical run would collapse around step 200; they'd diagnose the root cause, fix it, and restart — the curve would retrace almost exactly the same trajectory but survive past the old collapse point. Each algorithmic improvement pushed the training horizon from 200 to 300 steps and further.
- **Asynchronous RL**: separate trainer from rollouts. Rollouts push batches of groups into a data buffer; the trainer drains the buffer as it fills, then sends a weight update back. The cost is **staleness** — how many steps the inference policy lags the training policy.

#### SWE-1.7: entropy collapse and training across three continents (~00:23–00:27)

**Staleness and stability turn out to be the same problem**: the more stable your algorithm, the more staleness you can tolerate; the more staleness you tolerate, the more fully you can saturate your inference engines. A better algorithm buys you full compute utilization — which is what made SWE-1.7 possible.

SWE-1.7 was presented on a 2D cost-versus-performance chart rather than a 1D bar chart. For its size class it lands impressively high, competing with much larger models at far lower cost. The base model was Kimi K2.7; the size-class comparisons were Composer 2.5 (also Kimi-based) and GLM 5.2.

- **Entropy collapse was the binding constraint.** There was a lot of chatter that RL had plateaued and everything was back to pre-training, but they wanted to push further. The juice in RL comes from diversity within a group and discovery of new behaviors — both measurable as entropy. Entropy normally declines through a run until it collapses and you hit your ceiling. After recipe tuning, the decline became almost imperceptible (still declining, but on a much flatter slope), which let performance keep climbing. Details are in their technical report.
- **Training across four countries and three continents.** Large contiguous training clusters are genuinely hard to get these days, especially on realistic timelines — you might have to order a year in advance. What's much easier is finding smaller slices of compute here and there. The resulting run spanned **Australia, Malaysia, Canada, and the US**.
- **Only async RL makes this possible**: the training cluster sat in the US with rollout clusters scattered globally; inference clusters send training batches up, the trainer sends weight updates back. It works across the globe because what crosses the wire is sparse — RL weight updates are sparse and training batches are just tokens.

### Quotes

> "A lot of progress in research is just executing the simple things at scale." (~00:27)

The closing philosophy: they don't believe progress requires complex or fancy ideas.

> "The not-okay ratio … was an early indicator of an eventual divergence of the training run." (~00:17)

Before a run collapses, even the tone of the model's inner monologue shifts.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Devin | Cognition 的 AI 軟體工程師產品 | Cognition's AI software engineer | 講者稱為 "the world's first AI software engineer" |
| Windsurf | Cognition 約一年前收購的 coding 產品 | Coding product Cognition acquired about a year ago | SWE-grep 即 ship 進此產品 |
| Kevin-32B | 用 multi-turn RL(GRPO)訓練寫 CUDA kernel 的開源模型 | Open model trained with multi-turn RL (GRPO) to write CUDA kernels | 名稱來自 K(ernel D)evin;官方 blog 說 base 為 QwQ-32B |
| KernelBench | PyTorch → CUDA kernel 的加速 benchmark | Benchmark for replacing PyTorch ops with optimized CUDA kernels | Kevin-32B 的訓練與評估環境 |
| SWE-grep / SWE-grep-mini | 高度並行的 code search 子 agent,RL 訓練 | Highly parallel code-search sub-agent trained with RL | 部署於 Cerebras;演講稱 mini 約 3,000 tok/s |
| SWE-1.5 / SWE-1.6 / SWE-1.7 | Cognition 的前沿 coding 模型系列 | Cognition's frontier coding model series | SWE-1.7 官方 blog 載明 base 為 Kimi K2.7 Code |
| SWE-Bench Pro | 真實 coding 任務 benchmark | Benchmark of realistic coding tasks | SWE-1.6 於此追平 Opus 4.5 |
| Cerebras | 提供高速推論的晶片供應商 | Inference hardware provider | 字幕誤植為 "Sirius" |
| Kimi K2.7 / Composer 2.5 / GLM 5.2 | SWE-1.7 的 base model 與同尺寸級對照組 | SWE-1.7's base model and same-size-class comparisons | Composer 2.5 亦基於 Kimi |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Selius Alberti / Silus / SAS | Silas Alberti |
| Devon | Devin |
| Kevin 32B | Kevin-32B |
| Quen 32B | Qwen 系列 32B(官方 blog 為 QwQ-32B)/ Qwen-family 32B (blog says QwQ-32B) |
| gpo | GRPO |
| Swiger app / sweet grab / we grab / sweep grab | SWE-grep |
| Sirius chips | Cerebras |
| sonet 4.5 / opus 4.5 | Sonnet 4.5 / Opus 4.5 |
| Sweben Pro | SWE-Bench Pro |
| Kimmy K2.7 | Kimi K2.7 |
| 3 1.5 / SU 1.7 | SWE-1.5 / SWE-1.7 |
| stailness / stallness | staleness |
| soft rate | solve rate |
| internet latency | end-to-end latency |
| infrance / Inference | inference |
| comput utilization | compute utilization |

## 待確認 / To Verify

- Kevin-32B 的 base model:演講聽起來是 "Qwen 32B",但 Cognition 官方 blog 寫的是 **QwQ-32B**;需看投影片確認。/ Kevin-32B's base model: the talk sounds like "Qwen 32B" but Cognition's blog says **QwQ-32B**; check the slides.
- SWE-grep-mini 的吞吐量:演講說約 3,000 tokens/s,Cognition blog 寫 2,800+ tokens/s。/ SWE-grep-mini throughput: talk says ~3,000 tok/s, blog says 2,800+.
- "Composer 2.5" 與 "GLM 5.2" 的正式版本名稱與發布方,僅由字幕聽出,待投影片確認。/ Exact product names/vendors for "Composer 2.5" and "GLM 5.2" — heard from captions only.
- 52% → 68% 為 Cognition 內部可驗證 SWE 任務 eval,非公開 benchmark,無法外部查證。/ The 52% → 68% figure is on Cognition's internal eval, not a public benchmark.
- 演講提到的 SWE-1.7 technical report 連結待補。/ Add a link to the SWE-1.7 technical report referenced in the talk.
