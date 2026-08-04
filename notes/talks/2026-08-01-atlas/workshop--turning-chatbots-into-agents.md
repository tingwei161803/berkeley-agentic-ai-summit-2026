---
title: "Turning Chatbots into Agents: What Modern RL Looks Like"
title_zh: "把聊天機器人變成 Agent:現代 RL 長什麼樣子"
speaker: "Lovre Pesut; Muhammad Hashmi"
affiliation: "AI Engineer, Daytona; DevRel, Daytona"
type: workshop
stage: Atlas
date: 2026-08-01
session: "Session 1: Foundational Capabilities"
video: "https://www.youtube.com/watch?v=WeriQic-QW0&t=4113s"
video_range: "01:08:33–01:52:45"
transcript: "tmp/[English (auto-generated)] Atlas Stage - August 1st - Morning Session [DownSub.com].srt"
status: draft
tags: [reinforcement-learning, sandboxes, rl-environments, reward-hacking, daytona]
---

# 把聊天機器人變成 Agent:現代 RL 長什麼樣子(Turning Chatbots into Agents: What Modern RL Looks Like)

**一句話總結**:同樣的 harness、同樣的工具,GPT-2 會直接崩潰而 Kimi K3 能自己修 bug——中間的差別叫 reinforcement learning;而現代 RL 的真正瓶頸不在演算法,在於「誰來提供幾千萬個一次性沙箱」與「環境本身已經變成新的資料」。
**One-line summary**: Same harness, same tools — GPT-2 falls apart where Kimi K3 fixes your bug, and the difference is reinforcement learning; but modern RL's real bottleneck isn't the algorithm, it's who supplies the tens of millions of disposable sandboxes, and the fact that *environments* have become the new training data.

> 場次備註:議程排在 10:50,但因現場技術問題延後,實際從影片 01:08:33 才開始(前面 00:53:34–01:08:33 是排除技術狀況的空檔)。實際講述順序為 Muhammad Hashmi(前半:歷史)→ Lovre Pesut(後半:現代做法與案例),與議程列名順序相反。
> Session note: scheduled for 10:50 but delayed by technical problems; the workshop actually starts at 01:08:33 in the stream. Order on stage was Muhammad Hashmi (history) then Lovre Pesut (modern practice) — the reverse of the agenda listing.

## 中文筆記

### 開場:Daytona 是誰,為什麼在這裡(約 01:08)

Muhammad Hashmi 開場說明:Daytona 做的是**跑 agent 與其 workload 的基礎建設**——透過 API 建立電腦,自選作業系統、CPU 數量、RAM、磁碟。兩個主要使用情境:**在背景/雲端跑 agent**,以及 **reinforcement learning**。理由很直接:訓練 agent 時模型是靠「實際做事」來學,而 coding agent 或 computer-use agent 需要一個計算環境來做這些事。

而這場 workshop 要回答的問題是:**我們到底怎麼從幾年前那個「有時候有用的問答助理」走到今天會自己動手的 agent?**

### 主題一:同樣的 harness,差在哪裡(Muhammad,約 01:10)

他先放了一段 **Kimi K3** 的終端 agent:給它一個 prompt 去修 bug 或實作功能,它開始跑一堆指令、寫檔案。然後放下一張——**同樣的 harness、同樣的工具,但模型換成七年前的 GPT-2**。送同樣的 prompt,它直接崩潰,完全不知道該做什麼。

「理解這兩張投影片的差別,大概就是這場的主軸。簡短的答案是 reinforcement learning。」

他補充了一個重要的觀察角度:RL 本身不是新東西,已經存在數十年了,**真正改變的是背後的模型,以及什麼東西被獎勵。**

### 主題二:從 next-token 到 agent 的一條線(Muhammad,約 01:12–01:29)

他用一條時間線把整個演進串起來,重點在「每一步到底獎勵了什麼」:

- **Pre-training**:模型從機率分布抽下一個 token;拿 ground truth 算 loss(負對數機率),再把梯度更新回權重。他用逐 token 的機率變化投影片示範某個 token 從 61% 被推上去的過程。
- **In-context learning 是掉出來的**:你給模型三個 Python 函式的模式,它就能相當準確地預測第四個——「沒有人把這個模式建進權重裡,它就是從 next-word prediction 掉出來的**湧現性質**」。模型放大之後,這種模式跟隨能力顯著變好。
- **「一步步想」**:幾年前那篇 thinking step by step 的論文,以及大家記憶中「明確叫 GPT 想仔細一點,它就更常答對」的體驗。
- **從補句子到當助理**:早期模型只是把你的輸入補完;要變成助理,得先讓它**學會「當助理」這個模式**——給它大量問答樣本,它就學到「面對問題要當個有幫助的助理」。這是另一次重大轉折。
- **模仿的極限**:如果你拿一本數學課本的資料集,只獎勵那些能通往正解的 token,那其實是**在規定模型該怎麼走到答案**。問題是我們本來就不知道最好的路徑是什麼。
- **所以 RL 的動機是**:只獎勵最終答案,然後期待推理能力**自己長出來**——而這件事後來確實成立。
- **RLHF**:先出現的是人類偏好——你選哪個回答比較好,再用它訓練 reward model,讓底層 LLM 對齊人類偏好。
- **RLVR(可驗證獎勵)**:既然知道推理有用,為什麼還要教它模仿寫好的解法?只獎勵最終答案就好。**DeepSeek-R1** 就是這個路線的示範:不檢查每個 token 是否符合資料集,只檢查最終答案。
- **credit assignment 的問題**:推理鏈很長時,怎麼知道哪些 token 該領這份獎勵?模型可能前幾千個 token 走得很合理,後面才走岔。當時的答案是 **critic model**——猜測某個 token 是否「比預期更好」,因為本來就很可能被輸出的 token 不該領太高的獎勵。但這要**同時訓練另一個模型**。
- **GRPO(group relative policy optimization)**:不用另訓一個模型,改成一次抽一**組** rollout,用「同一題的多次嘗試」當作 credit 的代理。他的例子:同一題四次嘗試,三次過、一次失敗——那次失敗相當「意外」,所以那些 token 應該被**懲罰得比其他 token 被獎勵得更重**。如果不處理這個相對關係、什麼都平均獎勵,模型就會收斂到單一做事方式。
- **Tool calling**:模型要寫程式,理想上它應該能**測試**那段程式,至少在你貼進編輯器之前先知道它會壞。做法是讓模型輸出特殊 token 包住的內容,由一個 parser 認出來、拿去環境裡執行。訓練上就是先獎勵它照格式輸出,再獎勵它更常在解題時使用工具。
- **一次 tool call 還不是 agent**:agent 是不斷「行動 → 觀察」直到任務完成或它認為完成。演化路徑是 GitHub Copilot → 住在編輯器裡的 agent → 今天的終端 agent。
- **關鍵結論**:**RL 裡的「環境」變成了一台電腦。** Coding agent 必須呼叫檔案編輯工具、程式執行工具,而這些都得在某個計算環境裡執行。所以訓練 agent 現在得處理大量雲端基礎建設——這正是大家用 Daytona 做 RL 的原因。

### 主題三:一次真實的 RL 訓練跑起來長什麼樣(Lovre,約 01:30–01:39)

Lovre Pesut 接手,先做一個誠實的框定:**我們不知道 OpenAI 那些解開數學未解問題的模型是怎麼訓的**,但我們對**中國的開源模型**知道很多——**Kimi K2 / K3**、**GLM**,以及 Cursor 的 **Composer 2**(他說 Composer 2 也是基於 Kimi)。這場後半就建立在這些公開技術報告上。

他先給出現代 RL 的標準形狀:**每個 agent 拿到一個隔離的沙箱,在裡面做任務,再用某種可驗證的標準打分。** 這也是 coding 成為這些模型最大應用的副作用。

**案例:Qwen3 8B 的一次訓練跑**

- 配置:trainer 用 **SkyRL**,環境與 rollout 用 **Harbor**,沙箱是 Daytona sandboxes(但他強調任何沙箱都可以)。
- 這裡帶出一個值得記住的區分:**現代 RL 基本上分兩塊——產生 rollout 的那一半,和更新權重的 trainer;現在通常是不同函式庫各管一塊,再加上某種沙箱底層。**
- 規模:8 張 H100、4 小時、1440 次 rollout;起始 reward 約 0.3(因為是二元獎勵,等同 30% 正確率)。
- 他放了一段 **60 倍速**的訓練過程視覺化:GPU 使用率會抖(沙箱啟動與 episode 收尾時有 downtime,極度優化的設定可以更平順);每個 step 是 8 個任務 × 每題 4 次 rollout = 每 step 建立又銷毀 **32 個沙箱**;reward 緩慢爬升。
- **時間都花在哪**:RL 訓練通常**大部分時間花在 rollout**(模型行動、生成回合),其次是 backward pass(也不是可忽略的一塊),再來是 **weight syncing**——trainer 更新完權重後要把新 policy 送給 rollout 產生端。這個案例是完全同步的 RL:跑一步 → 更新權重 → 下一步用全新權重跑。

**最有意思的部分:模型到底學到了什麼**

「RL 在某些方面比 pre-training 更**可解釋**,因為資料量小得多,你可以直接把 trajectory 拿來看模型發現了什麼有效。」

這一跑把成功率從約 30% 拉到約 60%,但模型學到的**不是什麼演算法新洞見**,而是**把格式寫對**:

- 不再在雙引號裡面又用雙引號(寫檔案到 Python / 文字檔時)。
- 不再輸出**字面上的 `\n` 字元**而不是真正的換行——這在一開始大約**四分之一**的 rollout 裡絆倒了它。

「這正好連到那個老爭論:RL 到底是教會模型新東西,還是只是強化 pre-training 裡已經有的東西?至少在這個例子裡,我們可以說模型主要學會的是處理格式、處理 harness,而不是學會什麼新的演算法。」

(技術細節:每次 rollout 只在 **agent 的 token** 上訓練,tool 結果等不算。)

### 主題四:大規模訓練跑到底做了什麼(Lovre,約 01:39–01:48)

**Kimi K3 的技術報告細節**

- **51 M 沙箱**:他們明確說明訓練用掉 5,100 萬個沙箱。
- **microVM 與 pause**:他們用 microVM,而且**大量使用 pause 功能**——因為 Kimi 在回合之間傾向想很久,把沙箱暫停就能在思考期間不佔用計算資源。
- **Dynamic harness(他認為最有趣的一點)**:怎麼讓模型準備好面對**任何**可能被丟給它的 harness?他們做了一個**可設定的動態 harness**——用 config 開關各種 harness 面向:system prompt、sub-agents、memories、skills 等等,把它當成一條**資料增強的軸**。這樣模型不只準備好面對現有的所有 harness,連未來的 harness 大概也涵蓋得到,因為它是在 harness 特性的大量排列組合上訓練的。
- **對照 Composer 2**:Cursor 的做法正好相反——**專門為 Cursor 自家 harness 訓練**。「Kimi 走的是 harness 多樣性、追求對任何東西都穩健;Composer 2 走的是把模型為 Cursor 準備到極致。」這是兩種很不一樣的 agentic 訓練哲學。
- **不同 reasoning 等級**:給定 reasoning 等級就給一個 token 預算(也視題目而定);超出預算就直接給 **−1** 獎勵,不管當時是否正確。
- **九次 RL 跑 + on-policy distillation**:最終模型其實由**九次獨立的 RL 訓練**組成——reasoning 等級 low / high / max 各一個,加上 general(一般對話)、agentic、coding 等專家模型——最後**全部蒸餾進最終模型**。
- **on-policy distillation 怎麼運作**:拿專家模型(例如 coding 專家),用**通才模型**產生 rollout,再用專家模型去**評分那些 token**。這樣就能把每個專家的一部分智慧灌進最終模型。條件是你要能取得模型每個 token 的完整 log probs;做得到的話,teacher → student 的蒸餾非常有效。

**環境已經變成新的資料**

Kimi K3 與 GLM 都揭露了他們**用自家 agent 合成環境**的做法,而且變化很多。Kimi K3 甚至建了一張**涵蓋整個網際網路的巨大有向圖**,試圖用合成環境覆蓋每一個領域。

「環境可以說是新的一種資料形式。以前你想盡辦法把資料集做大;現在網路上的 pre-training 資料還算不少,但**環境沒那麼多**,而環境才是現在資料棧裡真正有價值的部分。於是你會想派你的模型去建更多、更好的環境。」

**Reward hacking:從比喻變成字面**

- 經典圖示:**OpenAI 2016 年**那個賽船遊戲——模型不去比賽,而是學會在原地繞圈撿分數包。
- 在 LLM 上是同樣的事,但**精緻得多**,因為你的 policy 本身就是個聰明的 agent。
- 「而現在我們知道,reward hacking **已經字面意義上變成 hacking 了**,至少在某些案例裡。」
- Kimi 和 GLM 都花了很多篇幅談他們的具體對策:針對不同環境做不同介入來預防或減輕 reward hacking。例如**寫 kernel** 就是一個特別容易被 hack 的環境,得花很多力氣確保你的 reward 是真的,而不只是 verifier 的一個怪癖。

### 主題五:同步 vs. 非同步 RL(Lovre,約 01:48–01:52)

- **時間都耗在 rollout**:模型要想很久,還可能執行耗時的動作。
- **完全同步 RL 的痛點**:你被**最長的那條 rollout** 卡住——所有 episode 跑完才能進 backward pass 與 weight sync。
- **非同步 RL**:盡量產生 rollout,不等特定幾條跑完,只等到「夠多條完成」就立刻更新 policy 與權重。現在為了最大化吞吐量非常流行。
- **代價**:你會拿到由**過期 policy** 產生的 rollout,這既打破 RL 演算法的一些理論假設,也讓整件事更不穩定——「而 RL 本來就已經是出了名的不穩定。」
- **Kimi K3 的折衷**:介於同步與非同步之間——收集到一定量的 rollout 後,把剩下的 rollout **暫停**留到下一次 weight sync。「是非同步 RL 的一個比較不極端的版本。」完全非同步的話 policy 一直往前走,staleness 會以一些不平凡的方式傷到訓練過程。

### 收尾(約 01:52)

「現代 reinforcement learning 的 API 現在相當標準化了:你有 trainer、有 rollout generator,還有某個地方在跑你的沙箱。」他補充,Daytona 這邊看到的正是對沙箱本身的大量需求。最後提到有一個 repo 可以找到產生這些圖表的程式碼(未在字幕中報出名稱)。

### 金句

> "Same model, same harness, same tools — but it's GPT-2. So when you send the same prompt, it just breaks. It doesn't know what to do."(約 01:11)

整場的出發點:差別不在鷹架,在模型被獎勵過什麼。

> "It didn't learn some new insights about algorithms — it just learned to format what it wrote better."(約 01:38)

RL 到底教了模型什麼?至少在這個小規模跑裡,答案是「學會跟 harness 相處」。

> "Reward hacking has literally become hacking nowadays — at least in some cases."(約 01:47)

> "Environments are a new form of data. Previously you would try to increase your dataset as much as you could; nowadays there's a decent amount of pre-training data on the internet, but there's not that many environments — and the environments are currently the actually valuable part of the data stack."(約 01:46)

這場最有觀點的一句話。

## English Notes

### Setup: who Daytona is and why they're here (~01:08)

Muhammad Hashmi opened by explaining that Daytona builds infrastructure for running agents and their workloads: computers you create through an API, choosing OS, CPU count, RAM, and disk. Two primary use cases — running agents in the background or on the cloud, and reinforcement learning. The RL case is direct: when you train an agent, the model learns by *doing* the task, and coding or computer-use agents need a compute environment to do it in.

The workshop's question: how exactly did we get from chatbots to today's agents?

### Theme 1: same harness, different model (Muhammad, ~01:10)

He showed a **Kimi K3** terminal agent taking a prompt to fix a bug or implement a feature and running commands, writing files. Then the next slide: **same harness, same tools, but GPT-2** — a model from seven years ago. Send the same prompt and it simply breaks. "The short answer to the difference between these two slides is reinforcement learning."

His framing note is worth keeping: RL isn't new, it's been around for decades. What changed is the model underneath it and **what gets rewarded**.

### Theme 2: the line from next-token prediction to agents (Muhammad, ~01:12–01:29)

He walked a timeline, always asking what was being rewarded at each step.

**Pre-training** samples the next token from a probability distribution; loss is the negative log probability against ground truth, and the gradient updates the weights. He walked through a per-token slide showing one token's probability being pushed up from 61%.

**In-context learning fell out of that for free.** Show the model three Python functions in a pattern and it predicts the fourth fairly accurately — nobody built that into the weights, it emerged from next-word prediction, and scaling the model made pattern-following much better. Then came the "think step by step" era, where explicitly telling GPT to reason carefully made it right more often.

**From completion to assistant**: early models just completed whatever you gave them. To behave like an assistant, the model first had to *learn the pattern of being an assistant* — show it many question-answer samples and it learns that a question calls for a helpful response. Another major shift.

**The ceiling of imitation**: if you take a math textbook dataset and reward only the tokens leading to the final answer, you're prescribing *how* the model should get there — and we don't actually know the best route. That's the motivation for RL: reward only the final answer and let reasoning emerge. Which, as it turned out, worked.

The sequence from there: **RLHF** (human preference between two responses trains a reward model that aligns the LLM), then **RL with verifiable rewards**, demonstrated by **DeepSeek-R1** — don't check whether every token up to the answer matches your dataset, just check the final answer.

**Credit assignment** is the problem that creates: with a long reasoning chain, which tokens earned the reward? The model may have been on a reasonable path for thousands of tokens before taking a bad turn. The answer at the time was a **critic model** guessing whether a predicted token was better than expected — a token that was already very likely doesn't deserve as much reward as an unlikely one. But that means training a second model in tandem.

**GRPO** (group relative policy optimization) removed that. Instead of one sample graded token by token, you sample a *group* of rollouts and use multiple attempts at the same task as a proxy for credit. His example: four rollouts on one task, three pass and one fails — the failure was unexpected, so those tokens should be **penalized harder than the others are rewarded**, because success was already likely. Without handling this relative reward, the model converges toward one single way of doing things.

**Tool calling**: for a model to write code, ideally it can test that code — at least knowing it failed before you paste it into your editor. The model outputs special tokens that a parser recognizes and executes in an environment; training-wise, you reward the output format first and then reward using the tool more often when solving problems.

**But one tool call isn't an agent.** An agent keeps acting and observing until the task is done, or until it thinks it is. The evolution ran GitHub Copilot → agents living in your editor → today's terminal agents. And the conclusion that matters: **the RL "environment" became a computer.** Coding agents call file-editing and code-execution tools that have to run somewhere, so training an agent now means dealing with a lot of cloud infrastructure — which is exactly why people use Daytona for RL.

### Theme 3: what an actual RL run looks like (Lovre, ~01:30–01:39)

Lovre Pesut took over with an honest framing: we don't really know how OpenAI's models that solved open mathematical problems were trained, but we know a lot about the **Chinese open models** — **Kimi K2/K3**, **GLM** — and about Cursor's **Composer 2**, which he says is also based on Kimi. The rest of the session builds on those public tech reports.

The standard shape of modern RL: every agent gets an isolated computer, does a task in it, and is graded on some verifiable criterion. That's partly a side effect of coding being the biggest application of these models right now.

**Case study: a Qwen3 8B run.** Trainer: **SkyRL**. Environments and rollouts: **Harbor**. Sandboxes: Daytona (though he stressed any sandbox works). This surfaces a distinction worth holding onto: **modern RL splits into the part that generates rollouts and the trainer that updates weights**, usually different libraries, plus a sandbox substrate underneath.

The run: 8 H100s, four hours, 1440 rollouts, starting at roughly 0.3 reward — which equals 30% accuracy because the reward is binary. He played a **60x speed-up** of the run: GPU utilization is jumpy (sandbox startup and episode wind-down create downtime; hyper-optimized setups smooth this out), each step is 8 tasks × 4 rollouts = **32 sandboxes created and torn down per step**, and reward climbs slowly. On where time goes: mostly **rollouts** — the model acting and generating turns — then the backward pass, which is non-trivial, then **weight syncing**, getting the new policy from the trainer to the rollout generators. This particular run was fully synchronous: one step, update weights, next step with completely new weights.

**The most interesting part: what did the model actually learn?** "RL can be more interpretable than pre-training, because the volume of data is smaller and you can just look at the trajectories and see what the model found that worked."

The run went from ~30% to ~60% success. But the model learned **no new algorithmic insight** — it learned to format what it wrote. It stopped nesting double quotes inside double quotes when writing to Python and text files, and it stopped emitting a literal `\n` character instead of an actual newline, a bug that tripped up roughly **a quarter of rollouts** at the start.

"That connects to the whole debate about whether RL actually teaches the model new things or just reinforces things taught during pre-training. At least in this example, the model mostly learned to deal with the format of things, to deal with the harness, rather than learning new algorithmic things." (Technical footnote: in each rollout you train only on the **agent's** tokens, not tool results.)

### Theme 4: what the big runs actually did (Lovre, ~01:39–01:48)

**From the Kimi K3 tech report:**

- **51 million sandboxes** used during training — they state the number explicitly.
- **microVMs and the pause feature**, used heavily: Kimi tends to think a lot between turns, and pausing the sandbox during that thinking frees the compute.
- **Dynamic harness** — the detail he found most interesting. How do you prepare a model for *any* harness it might be dropped into? They built a configurable harness that toggles features on and off — system prompts, sub-agents, memories, skills — and used that as an axis of **data augmentation**. The model ends up trained on many permutations of harness features, so it's ready not just for every current harness but plausibly for future ones too.
- **The contrast with Composer 2**: Cursor took the opposite approach and trained specifically on Cursor's harness. "Kimi's approach is harness diversity and robustness to anything you could throw at it; Composer 2's was let's get this model really ready for Cursor." Two quite different philosophies for preparing a model for agentic work.
- **Reasoning levels**: each level gets a token budget (also problem-dependent), and going over the budget earns **−1 reward regardless of whether the answer was right**.
- **Nine RL runs plus on-policy distillation**: the final model is composed of nine separate RL runs — one per reasoning level (low, high, max), plus general-conversation, agentic, and coding models — all then distilled onto the final model. So they verifiably did distillation, though we don't know whether other models were also in the mix.
- **How on-policy distillation works here**: take an expert model (say the coding expert), generate rollouts with the *generalist* model, and score the generalist's tokens with the expert. That imparts part of each expert's wisdom into the final model. You need access to full log probs per token, but given that it's a powerful teacher-to-student technique — and it composes nicely with RL in general.

**Environments are the new data.** Kimi K3 and GLM both share details about generating synthetic environments with their own agents, with a lot of variety; Kimi K3 built a large directed graph of the internet, trying to cover every area with some synthetic environment. His framing: "Environments are a new form of data. Previously you'd try to increase your dataset as much as you could; nowadays there's a decent amount of pre-training data on the internet, but there aren't that many environments — and environments are currently the actually valuable part of the data stack. So you want to employ your models in building better and better environments."

**Reward hacking.** The canonical illustration is OpenAI's 2016 boat-racing example, where the model ignored the race and learned to spin in a circle collecting score packets. With LLMs it's the same thing but far more sophisticated, because your policy is an actually intelligent agent. "And now, as we know, reward hacking has literally become hacking nowadays — at least in some cases." Kimi and GLM both discuss specific countermeasures at length, with different interventions per environment; writing kernels, for instance, is an environment with many ways to hack, so it takes real effort to ensure your reward is a real one and not a quirk of your verifier.

### Theme 5: synchronous vs. asynchronous RL (Lovre, ~01:48–01:52)

Most of the time in an RL step goes into rollouts — models think for a long time and may execute slow actions. In **fully synchronous** RL you're constrained by your longest rollout: everything waits for all episodes to finish before the backward pass and weight sync.

**Asynchronous RL** generates as many rollouts as it can, waits only for a certain number to finish, and immediately updates the policy and weights. It's popular now for maximizing throughput. The cost: rollouts generated by a **stale policy**, which breaks some of the theoretical assumptions of RL algorithms and makes the whole thing less stable — "and reinforcement learning is already notoriously unstable."

**Kimi K3 landed in between**: they collect a certain number of rollouts, then *pause* the remaining ones and carry them to the next weight sync — a less extreme version of asynchronous RL. Fully async lets the policy move on and accumulates staleness that can hurt training in non-trivial ways.

### Closing (~01:52)

"The API of modern reinforcement learning is pretty standardized now: you have your trainer, your rollout generator, and somewhere your sandboxes run." Daytona's own view of the market is a lot of demand for sandboxes specifically. He pointed to a repo containing the code that generated the presentation's charts (name not audible in the captions).

### Quotes

> "Same model, same harness, same tools — but it's GPT-2. So when you send the same prompt, it just breaks. It doesn't know what to do." (~01:11)

The premise of the workshop: the difference isn't the scaffolding, it's what the model was rewarded for.

> "It didn't learn some new insights about algorithms — it just learned to format what it wrote better." (~01:38)

What RL actually taught the model in their run: how to get along with the harness.

> "Reward hacking has literally become hacking nowadays — at least in some cases." (~01:47)

> "Environments are a new form of data. … The environments are currently the actually valuable part of the data stack." (~01:46)

The most opinionated claim of the session.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Daytona | 透過 API 建立沙箱電腦的 agent 基礎建設;主打背景 agent 與 RL | Agent infrastructure: sandboxed computers via API, for background agents and RL | 本場主辦方 / the presenting sponsor |
| Kimi K3 | Moonshot AI 的開源前沿模型;技術報告是本場後半的主要素材 | Moonshot AI's open frontier model; its tech report is the backbone of the second half | 51.2M 沙箱、Firecracker microVM、九次 RL 跑後蒸餾 |
| GLM | 另一個公開較多訓練細節的中國開源模型系列 | Another Chinese open model family that publishes training details | 合成環境與 reward hacking 對策 |
| Composer 2 | Cursor 的模型,專門針對 Cursor 自家 harness 訓練 | Cursor's model, trained specifically on Cursor's own harness | 講者說它也基於 Kimi |
| SkyRL | 案例中使用的 RL trainer 函式庫 | The RL trainer library used in the case study | NovaSky-AI(UC Berkeley Sky Computing Lab);官方與 Harbor 整合 |
| Harbor | 案例中負責環境與 rollout 的函式庫 | The environments/rollout library in the case study | 與 SkyRL 有官方整合 |
| Qwen3 8B | 案例訓練跑的基礎模型 | Base model of the demo training run | 8×H100 / 4 小時 / 1440 rollouts / 0.3→0.6 reward |
| DeepSeek-R1 | RLVR「只獎勵最終答案」路線的代表 | The reference point for verifiable-reward RL | |
| GRPO | 用一組 rollout 取代 critic model 的 credit assignment 方法 | Group-relative credit assignment replacing the critic model | |
| OpenAI 2016 boat-race reward hacking | 賽船遊戲繞圈撿分的經典 reward hacking 圖示 | The canonical reward-hacking illustration | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Lou | Lovre (Pesut) |
| Kimmy K3 / Kimik3 / Kimikry / Kim Kitri / Gimme K3 / Kimy | Kimi K3 |
| Kimmy K2 | Kimi K2 |
| quen 38 billion | Qwen3 8B |
| sky RL | SkyRL |
| harbor | Harbor |
| deepse R1 | DeepSeek-R1 |
| GM / GLM | GLM |
| composer to / composer too | Composer 2 |
| reinforcement learning with verifiable words | RL with verifiable rewards (RLVR) |
| reposting | RL post-training(語境推斷)|
| Lower Sprawl Plaza | Lower Sproul Plaza |
| irregardless | regardless |
| dual results | tool results |

## 待確認 / To Verify

- 講者在結尾提到「有一個 repo 可以看到產生這些圖表的程式碼」,但字幕沒有錄到名稱與網址。/ He pointed to a repo with the code behind the charts; the name and URL aren't in the captions.
- 「Composer 2 也是基於 Kimi」是講者口述的說法,未給出處。/ "Composer 2 is also based on Kimi" is his claim on stage, uncited.
- Kimi K3 dynamic harness 那句「so it works at [Kimi CLI] but also works at Claude Code, Codex etc.」中的 harness 名稱由字幕還原("Kimmy Schmi code" / "cloud codecs"),需對照技術報告確認實際列舉了哪些 harness。/ The harness names in the dynamic-harness passage are reconstructed from garbled captions; check the tech report for the actual list.
- 「九次 RL 跑」的組成(low / high / max + general / agentic / coding)是講者口述的拆法,是否恰好九個需對照技術報告。/ Whether the nine RL runs decompose exactly as he described needs checking against the report.
- Harbor 的維護者與定位(搜尋顯示與 SkyRL 有官方整合,並有 fleet-ai/harbor-train 這個 repo),但講者未說明歸屬。/ Harbor's maintainer wasn't stated on stage.
- 案例訓練跑的任務集合只描述為「terminal 裡的一些標準 Python 任務」,未給 benchmark 名稱。/ The task set was described only as "standard Python things in a terminal"; no benchmark named.
