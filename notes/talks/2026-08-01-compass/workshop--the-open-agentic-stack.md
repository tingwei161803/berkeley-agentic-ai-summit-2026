---
title: "The Open Agentic Stack: Building the Future of AI Systems with Open Source, Open Standards and Composability"
title_zh: "開放的 Agentic Stack:用開源、開放標準與可組合性打造 AI 系統的未來"
speaker: "Matt White, Ben Burtenshaw, Daniel Han Chen, Shang Yang, Romil Bhardwaj"
affiliation: "Matt White (Former Global CTO of AI, Linux Foundation; CTO, PyTorch Foundation); Ben Burtenshaw (Community Engineer, Hugging Face); Daniel-Han Chen (Co-Founder, Unsloth); Shang Yang (RadixArk); Romil Bhardwaj (Co-Founder and CPO, SkyPilot)"
type: workshop
stage: Compass
date: 2026-08-01
session: "Session 3: Foundational Capabilities"
video: "https://www.youtube.com/watch?v=AO0RXP-fVZQ&t=10626s"
video_range: "02:57:06–03:56:20"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [open-source, rl-environments, quantization, rl-infrastructure, compute, workshop]
---

# 開放的 Agentic Stack(The Open Agentic Stack: Building the Future of AI Systems with Open Source, Open Standards and Composability)

**一句話總結**:**agent 不是一個模型,而是一整個 stack**——模型、harness、工具、環境、guardrail、RL 系統、評估基礎設施、算力,任何一層被垂直封閉,整個生態系就變得不可攜、缺乏競爭且更脆弱;這場 workshop 用四場子講題,分別攤開環境(OpenEnv)、模型(Unsloth)、RL(Miles)與算力(SkyPilot)這四層該怎麼保持開放。
**One-line summary**: **An agent is not a model, it's a stack** — model, harness, tools, environment, guardrails, the RL systems that improve it, the evaluation infrastructure that measures it, and the compute it all runs on. Close and vertically control any one layer and the whole ecosystem becomes less portable, less competitive, and more fragile. Four talks work through four of those layers: environments (OpenEnv), models (Unsloth), reinforcement learning (Miles), and compute (SkyPilot).

> 主持人於 **02:57:06** 介紹本場;因議程落後約 25 分鐘,Matt White 於 **02:58:30** 提前開講。
> The MC introduced the workshop at **02:57:06**; running about 25 minutes behind, Matt White started early at **02:58:30**.

## 中文筆記

### 開場:Matt White — 為什麼 agent 時代的開放性更重要(約 02:58:30–03:04:45)

他先自我介紹:Linux Foundation 前 AI 全球 CTO,曾任 **PyTorch Foundation** 執行董事與 CTO,現為哥倫比亞大學訪問學者。這一段沒有投影片,他明說「就是我在碎念」,但這是整場的立論基礎。

**論點一:能力躍升的同時,開放性正承受真實壓力。** 模型現在能跨長脈絡推理、寫並執行程式碼、使用工具與操作軟體、協調日益複雜的工作流,能解複雜數學證明、生成龐大程式庫、驅動會在**生產網路上採取行動、產生真實世界影響**的系統。而恰恰在這個時刻,「**限制甚至禁止 open-weight 模型的取用**」已不再是假設性議題——它正在華府與各地被積極辯論;同時也有透過**晶片、算力、蒸餾、安全測試與模型釋出流程**來控制前沿的提案。

他明確承認:**這些安全、資安與國安顧慮是真實且正當的,值得技術上嚴謹的回應。** 但另一邊的風險也必須說清楚:**粗糙的限制會把能力、基礎設施與決策權集中到極少數機構手上**,把 AI 從一個可廣泛取得的通用技術,變成「社會其餘部分只被允許向少數幾間實驗室**租用**」的東西。「That cannot be the foundation on which we build the future.」

**論點二:開放是競爭與安全的來源。** 開放帶來競爭,讓研究者能檢視系統、開發者能改造、學生能學習、企業能維持對自身資料與 stack 的主權、國家能建立不永久依賴單一供應商的 AI 能力。開放同時是**安全的必要成分**:可重現的評估、透明的介面、獨立的審查、共享的安全工具,以及發現並修正問題的能力。

但他也劃清界線:**開放不等於無治理**,不等於粗心、不安全或放任。開放意味著系統**可被檢視、評估、改造與改進**;介面可互通、實作可被挑戰,而且**沒有任何單一組織控制所有層級或決定誰能參與**。

**論點三:agent 讓這件事更關鍵,因為 agent 是一個 stack。** 一個 agent 包含模型、harness、它能呼叫的工具、它行動的環境、guardrail、讓它變好的 RL 系統、量測它的評估基礎設施,以及支撐一切的算力;它可能依賴 API、憑證、sandbox、記憶、推論系統、編排框架與多種專用硬體,並在完成**單一任務**的過程中跨越組織、雲端與地理邊界。**任一層被封閉並垂直控制,整個生態系就變得不可攜、缺乏競爭、更脆弱。**

所以:**光有開放模型不夠**。還需要開放的**環境**(agentic 任務才能被重現與分享)、開放的 **RL 框架**(更多人才能改進模型與 agent)、開放的**算力層**(工作負載不被單一雲或算力供應商綁架),以及開放的**標準**(讓所有元件無需向中央平台請求許可就能協同)。

**Open agentic stack 不是一個專案、一個框架或一個模型,而是一個由開源軟體、開放標準與可組合元件構成的共享架構。** 這場 workshop 就沿著四個基礎層走:**環境、模型、強化學習、算力**。四場講題各自處理不同的技術挑戰,但共享同一個原則:**AI 的未來應該是模組化而非單體、可互通而非受困、開放參與而非許可制。** 他強調這不只是哲學偏好,而是健康 AI 生態系在**架構、經濟與戰略上的要求**。

### 子講題一:Ben Burtenshaw(Hugging Face)— Open Source Agentic RL Environment(約 03:05:45–03:18:20)

**主張**:**RL 環境是民主化 AI 最好的方式**——因為環境「就只是應用程式」,是我們每天都在寫的那種東西,所以人人都能參與。

**什麼是 RL 環境。** 最簡單的說法:一個 actor / agent 在其中行動的世界。經典例子是西洋棋——棋盤是世界、棋子是狀態、規則是可採取的行動、分數是 reward,而 RL 就是拿這個 reward 去更新 agent。放大到現實:**軟體工程**可以定義成任務在 GitHub issue、工作在 pull request、分數是測試套件與 CI 的結果——這就是 **SWE-smith** 這類論文建構軟體工程環境的方式。把 PR 裡的程式碼拿掉、讓 agent 自己生成、再用測試套件給 reward,你就有了一個能訓練軟體工程 agent 的環境。同樣的原型可以搬到 email triage、專案管理等任務——只要在該環境中定義出**任務、reward 與狀態**,再把它做成應用程式。

**生態系:「capability cycle」。** 他把老派機器學習的 MATTER cycle(model, annotate, train, test, evaluate, revise)更新成能力循環:**discover → benchmark → represent → train**。

1. 用 harness 或 prompt **誘出(elicit)** 一個能力,看到模型「做得到,只是不太可靠」。
2. 用另一套 evaluation harness **量測**這個能力的頻率與可靠度,社群可以在上面迭代。
3. 把它**表徵**成資料集,最終成為環境——**這一步需要領域專業**。像 **Mercor** 這類公司會去接觸並雇用各領域專家,圍繞某個能力打造 RL 環境,部分基於 benchmark,但理想上兩者之間**不能有洩漏**。
4. 交給 trainer 訓練——又是另一段軟體 stack、另一個社群。

結論:**環境正是把能力從領域專家搬進模型的載體**;能力進了權重之後,大家就往下一個能力前進。既然這麼多社群都在環境上交會,**這一層就非開放不可**——「想像一下如果資料集是封閉格式,那會有多可怕」。

**現況的問題:環境極度分散。** 你只能去論文與 GitHub 找。最近的 **Kimi K3** 論文附帶了**數千個**環境,**MiniMax** 論文他記得有**一萬個**,連第一篇 **DeepSeek** 論文也有約**一千個**。而這些實作方式各異、分享方式各異,很多是**被販售的**,不像 open-weight 模型那樣唾手可得。他形容這很像 2017 年當 MLE 的日子:在 GitHub 找到實作、再去 Google Drive 找權重,什麼都沒有像今天的 model checkpoint 那樣可暴露、可互通。

**訓練時問題會複合。** 訓練流程是一個框架(如 **TRL** 或 **Unsloth**)根據模型的行為更新模型,而中間需要一個 **agent harness** 去執行任務、與環境互動、使用環境裡的工具,然後才更新模型。**每一條邊都是一個需要被介面化的層**——harness 不能寫死它預期的環境定義,而且還得同時支援多種 harness(他點名 Codex、Claude Code 等)。

**OpenEnv 的解法。**

- **環境 hub**:Hugging Face 上目前有約 **4,000 個**環境,以標準格式提供,可接進大多數主流訓練框架。其他 hub 還有 **Prime Intellect**,更多正在出現;他們正與其他組織**共享規格**,讓別人建 hub 時也能用同一套 spec 下載與分享環境。
- **CLI 體驗像 Docker**:`openenv init` 給你一個 hello-world 環境的骨架(只回傳一個泛用分數),接著你只要寫自己的業務邏輯——或請 coding agent 幫你生成。也可以從 **verifiers** 之類的函式庫匯入環境,然後在 hub 上 **push / pull / fork**。
- **下一步是 discover 與 validate**:目前找到適合自己用例的環境很困難,能在 hub 上搜尋之後就能撈到一堆社群環境;但這帶來新問題——**哪個環境比較好?哪個真的對我的用例有幫助?** 於是有了新的 `validate` 指令:確認 spec 有效,並且**訓一個小模型看它是否在給定 benchmark 上帶來提升**。這兩個指令合起來,就構成 post-training 中整合環境的**自主迴路**。

**怎麼用一個 RL 環境?** 三條路,由易到難:

1. **Evaluation**(他建議大多數人從這裡開始):把典型工作負載表徵成環境,拿模型(權重或純 API)跑一組任務加 reward function,得到一個總分。
2. **Reinforcement learning**(核心用法):拿一個 policy 在環境中 rollout 得到一組動作,對每次 rollout 算 reward,用 **GRPO** 之類的演算法取整組平均後更新權重,反覆迭代。
3. **Distillation**:這時**不能從字串/token 蒸餾,需要 log probabilities**。取一個 student 與一個 teacher,讓 student 在環境中執行任務、取其 log probs;再讓 teacher 在**同一批 token 上** rollout、取其 log probs;用兩者的差(**reverse KL**)更新 student。變體包括 **self-distillation**(拿 student 最好的一次跟平均比),或給 student **特權資訊 / 提示**——例如在 PR 情境裡,一開始就把真正的解法給 agent,再用它「差的一次」與「好的一次」之差來更新權重。

**他認為這件事會怎麼成功:leaderboard。** 環境目前活在一個「影子領域」——在圍繞模型發布的社群討論裡幾乎不被提及。他相信只要大家開始自己建環境、試環境,再把它們放上 leaderboard、找出哪些真的對模型成功有貢獻,就會有更多人參與。

### 子講題二:Daniel Han Chen(Unsloth)— Making Open Models Not Suck(約 03:19:38–03:35:35)

**Unsloth 是誰。** Hugging Face 上最大的組織之一,約 **4 億次**累計下載(他說這數字已過時),是全世界第三大的模型散布者,大模型小模型都發。但他們**不只散布模型,還修 bug**:與全球各大實驗室與硬體供應商合作,在模型送到你手上**之前**先修好問題。他點名 OpenAI 的 gpt-oss、Llama、Gemma、Mistral 都曾有問題。「如果你在筆電上跑開源模型,它八成被我們以某種方式修過。」

**量化的現況。** **Kimi K3** 幾天前(週一)發布,是任何人都能下載的最強 open-weight 模型,原始大小 **1.5 TB**;他們把它量化到 **1 bit**,降到約 **600 GB**。難點在於 **Kimi K3 原生就是 4-bit**,從 4-bit 再壓到 1-bit 省下的空間有限;但他們的結果是**保留 76–78% 的準確率,體積減少 82%**——「把模型縮小 82%,不會讓它笨 82%,只會笨 16% 左右」。另外 **DeepSeek V4 Flash** 前一天(0731)在一個奇怪的時區突然發布,他們也量化了,現在只需 **90 GB** 的 VRAM 或 RAM 就能跑;他評價它是**同尺寸中最好的模型**——Kimi K3 更強但體積巨大,V4 Flash 則真的能塞進你的本機。

**METR 曲線與「推理發明前的平行線」。** 他展示 METR 的任務時長圖:模型現在能完成人類要花 **16 小時**的任務(50% 成功率;80% 成功率下約 6 小時)。他自己把 **Mythos / Fable** 標成紅線,也標了 **GPT-5.6 Sol**——這是**移除作弊案例後**的數字;若把作弊案例算進去,GPT-5.6 Sol 是 **270 小時**,但那不是好例子,移除後約 16 小時。

他的核心觀察是曲線上那段**水平區**:**2023 到 2024 年左右其實有一段近似停滯**(GPT-4 到 GPT-4o 進步不大),原因是**強化學習與推理當時還沒被發明**。如果分開擬合「推理發明前」與「推理發明後」兩段趨勢:
- **灰線(推理前)**:能力**每 7 個月翻倍**;若 OpenAI 沒推出 o1-preview、沒告訴大家可以做推理,**模型現在早就平原化了**。
- **綠線(加入 RL 與推理後)**:翻倍時間縮短到 **3.5 個月**——「Opus 5 幾天前發布,再等 3.5 個月就會有比它更好的」。

但他強調前提是**趨勢會延續**:根本問題是綠線會不會一直往上,還是我們會退回灰線、AI 放慢然後得再發明新東西。「這是我們有生之年會看到答案的問題——**你只要等 3.5 到 7 個月就知道了**。」

**開源模型追上封閉模型了嗎?** 他先引 **Artificial Analysis** 的開源 vs 閉源曲線:開放模型已經非常接近閉源。但他說自己**最愛的單一 benchmark 是 WeirdML**(Google 搜 "weird ML"),理由是**很難被 game**。依 WeirdML:**Fable 5 表現很好但極度昂貴**;就成本與準確率的平衡而言他推薦 **Opus 5 High**;開放模型裡 **Kimi K3 非常強大**,也在榜上。

他接著把「閉源分數減開放分數」畫成一條**差距曲線**:約一年半前有一段他稱為 **open source drought(開源乾旱)** 的落差,對應 o1-preview 之後開放模型跟不上的時期;而 **DeepSeek R1 公開了 GRPO 怎麼做**之後,開放模型重回趨勢線。他的估計:**若 DeepSeek 沒有公開 GRPO,開放模型會落後閉源 16 個月;現在只落後約 2 個月。** 有一篇 blog post 外推到 **2026 年 12 月**會出現與閉源同級的開放模型——但這都是趨勢外推,「誰知道呢,等幾個月就知道了」。

**token 價格暴跌是合理的嗎?** 他注意到 OpenAI 幾天前把 **GPT Luna 降價 80%**,聽起來驚人,但他認為**其實不奇怪**,並在演講前實際算了一遍:

- 依 **SemiAnalysis** 的 InferenceX 對 vLLM / SGLang 等推論引擎在 NVIDIA 與 AMD GPU 上的 benchmark:**DeepSeek V4 Pro** 在單張 **GB300** 上約 **13k tokens/s** 吞吐 → **一小時 4,700 萬 token**。
- GB300 的價格約 **每 GPU 每小時 5 美元**。
- 兩者相除:**DeepSeek V4 Pro 的地板價約 11 美分 / 百萬 token**。而 DeepSeek 實際收 **44 美分 / 百萬輸入 token、87 美分 / 百萬輸出 token**——**所以並不是在燒錢**。
- 同理,假設 GPT-5.6 Luna 與 DeepSeek V4 同尺寸(他明說「很可能不是」),OpenAI 降到那個價位**仍有約 1 美元 / 百萬輸出 token 的空間**。
- 對照組:**Kimi K3** 是新架構、尚未充分最佳化,依 SemiAnalysis 約 **5k tokens/s per GPU**(比 DeepSeek 慢約 2.6 倍),地板價約 **30 美分 / 百萬 token**;而它實際收 **15 美元 / 百萬輸出 token**——也就是 Moonshot 與其他推論供應商在你的 API 費用上賺了約 **14.17 美元**。「他們如果想降,可以一路降到 30 美分。」結論:**這些模型的價格仍然偏高,DeepSeek 是唯一接近地板價收費的。**

**另一條路:在本機跑。** 他也喜歡看 **Arena** 的 Pareto efficiency 圖(他說自己不太看 Arena 分數,但這張圖有用):很多開源模型都在 Pareto 前緣上。以 **web development**(HTML/前端)為例,**Opus 5 Max 目前最好,Kimi K3 緊追在後**;**GLM 5.2** 等模型也在圖上。而如果你不想付 API 費用,可以在本機跑——成本降到只剩電費與一些前期投入。

這正是 Unsloth 在做的事:用 **dynamic quantization** 把模型壓到極小的 bit 數。**GLM 5.2 的 1-bit 版**是個好例子——一次 prompt(沒有讓它改 bug、修 bug)就表現得非常好,對比的還是全精度的閉源模型。他們也發布 **perplexity** 與 **KL divergence** 的 benchmark 佐證 1-bit 可用。他們的目標是繼續往下壓:Kimi 現在 600 GB「大概還塞不進你的電腦」,他們想做到**甚至低於 1 bit**,例如把 Kimi 壓到 250 GB。

**最後一個重點:ARC-AGI 的 harness 設定。** 幾天前 OpenAI 指出 **ARC-AGI benchmark 對 GPT 其實不太公平**,原因是評測用了 **175k token 的 rolling truncation**,而且**沒有啟用 compaction、沒有啟用 preserve thinking**。他的結論很直接:**只要打開這兩個 flag,OpenAI 模型的準確率就能一路提升到 40%——你什麼都不用做。**(他在此因時間不足跳過剩下的投影片。)

### 子講題三:Shang Yang(RadixArk)— Miles: An Intro to Enterprise Facing RL with Miles(約 03:36:48–03:45:35)

講者自我介紹:RadixArk 的 research resident,同時是 MIT 博士生,代表團隊介紹 **Miles**。

**Miles 是什麼**:RadixArk 開發的**開源 RL 引擎**,面向前沿模型的生產級強化學習,主打**快速與穩定**。定位是「**穩定、高效、可重現的大規模 RL 系統**」——讓你用最小的力氣,就能在現代語言模型上、搭配各種環境與 reward 設計跑起 RL 訓練。

**三層架構:**

1. **Rollout 層**:以 **SGLang** 作為 rollout 引擎,專為高吞吐生成最佳化,且與當今的 agentic 系統、agentic 環境與 agentic infra 高度相容。
2. **編排層(中間)**:把 rollout 引擎與後端訓練系統組織成一個整體,讓系統高效運轉。
3. **訓練層**:支援 **Megatron** 與 **FSDP** 等不同訓練引擎,也可在自己的算力上自訂訓練引擎。

**資料流**:rollout 引擎與外部環境或 agent 框架互動產生 trajectory(SGLang 提供生成層,環境本身可依客戶需求高度客製)→ 中間層把 trajectory 轉成 reward 與 loss 等訓練訊號 → Megatron / FSDP 做 forward/backward、算 loss、更新權重 → 權重同步回推論引擎,整條 pipeline 循環運轉。

**為什麼用 SGLang 當 rollout 後端:**
- 與 RL 工作負載**共同演化**,包含 partial rollout 支援與專用的 rollout 控制,容易針對特定工作負載定制。
- **router 設計效能高**:精心設計的快取與負載平衡以支撐高吞吐生成。
- **原生支援與訓練引擎的非同步生成**——這是當代 RL 演算法的關鍵特性。
- 迭代快,且有許多最佳化,例如與 Miles 搭配的 **speculative decoding**,可在 RL 的 rollout 階段使用。

**Miles 如何改變 RL 開發流程:**
- **可客製**:用可插拔的 function pass 支援不同工作負載,自定 RL 工作負載、reward function 與更新方法都很容易。
- **模組化且非侵入式**:更換訓練後端(FSDP / Megatron)很容易,未來會支援更多後端。

**系統設計細節:**
- **Multi-agentic rollout**;特別支援 **token-in-token-out(TITO)**——同一段 multi-turn 生成不需要反覆 tokenize / detokenize,省下大量成本、也讓推論更穩定。
- **R3(routing replay)**:訓練 MoE 模型時,同一個請求在不同次執行可能被路由到**不同的 expert**;R3 確保這件事**完全可重現**。
- **低精度**:端到端 **MXFP8** 支援,以及 rollout 階段的 **per-token NVFP4 量化**,可大幅降低延遲、提升吞吐——都已在他們最新的 blog 以真實訓練工作負載驗證。
- **LoRA 支援**,供資源受限情境下用較少 GPU 訓練大模型。

**支援矩陣與實績:**
- **Day-zero 支援**最新模型:**Kimi K3**、Thinking Machines Lab 的 Ling(逐字稿作 "inkling",待確認)、**DeepSeek V4**、**Nemotron Ultra** 等。
- 廣泛的精度與硬體支援;fine-tuning recipe 不只 SFT / RL,也支援 **on-policy distillation**。
- 已在 **超過 10,000 張 GPU** 的 RL 訓練工作負載上驗證。以 **Kimi K2.6** 為例,生成吞吐加速到 **每 GPU 每分鐘 12.5k output tokens**。
- 穩定性最佳化:R3、TITO,以及**精度對齊訓練**(降低 training–inference mismatch);另有**容錯恢復**,並支援 **Ray on Kubernetes、Slurm、bare metal** 等叢集後端。

**近期成果:**
- **Kimi K3(近 3 兆參數)day-zero 支援**,並用 Miles 在數學題目上做 fine-tuning,準確率從 40% 左右提升到 **76%**。
- **Ling(Thinking Machines Lab,兆級參數)**:做了全參數 fine-tuning 與 LoRA fine-tuning,並最佳化 **LoRA adapter 同步**(把 LoRA rank merge 進 SGLang 推論引擎),把時間從**近 50 秒降到不到 3 秒**。
- 一篇**混合精度訓練**的近期 blog:驗證用 MXFP8 或 NVFP4 等不同精度選擇,能在**維持模型準確率與訓練穩定性**的同時,大幅加速 rollout 與推論。

### 子講題四:Romil Bhardwaj(SkyPilot)— AI Needs an Open Compute Layer(約 03:46:13–03:55:58)

**論點**:AI 需要一個**開放的算力層**——具體來說,是一個**坐在工作負載與實際 GPU 之間**的東西。

**為什麼建 AI infra 這麼難?他用 OpenAI 當例子**:2016 年與 Azure 簽下 GPU 獨家供應協議;2024 年又與 Oracle 簽了 **100 億美元**的合約換更多算力;僅僅一年後又與 CoreWeave 簽了 **110 億美元**。而即使如此仍不夠——Sam Altman 還在推特上喊「我們需要更多 GPU,你要是能弄到就打給我們」。他的推論很直接:**如果地球上資金最雄厚的公司都拿不到足夠的 GPU、也拿不到單一叢集裡的量,那你大概也拿不到。GPU 短缺是非常真實的。**

**典型 AI 組織的算力現況**:AI 團隊手上有一些 **NeoCloud 保留量**(hyperscaler 沒容量時簽的 2–3 年合約);又加了一些 hyperscaler 的 **on-demand** 實例補容量;因法規或想把資料留在自家而又有一些 **on-prem** 叢集;客戶在歐洲所以還得在歐洲再開一個叢集;最後為了跑環境與 sandbox,還需要一大票 CPU,於是又多維護一個 CPU 叢集。**每一個決策在當下都合理,但結果是你現在得管理一大堆叢集。**

**RL 讓情況更糟——它把問題變成排程問題。** 一次 RL 訓練整體是**一個 job**,但由許多子元件構成,且資源需求截然不同:**trainer** 需要大量 VRAM、需要很猛的 GPU;**rollout server**(產生 trajectory 的那個)不需要那麼多 VRAM,但需要**很多張**才能大量生成;而若做程式碼生成,**sandbox** 需要大量並行 CPU 來執行所有 trajectory,而且要求**很快的啟動速度**。

**為什麼不直接用現成方案?**
- **Slurm**:二十年前來自 HPC 世界,他認為是最好的進階排程與 quota / 優先權管理系統之一。但**不支援容器形式的隔離**(pyroot 之類可以硬接上去,但本來就不是為此設計),而且從來不是為 serving 而生——它是 batch job 導向。
- **Kubernetes**:約十年前出現,微服務起家,很有彈性、為雲而生。但**學習曲線極陡**(「把 Kubernetes 交給一個研究員,他大概只能去問 agent 怎麼用」),而且缺少 AI 需要的原語,尤其是 **gang scheduling**——同樣得靠 Volcano 之類的排程器硬接。

更關鍵的是:**兩者都是單一叢集管理器**,都不解決「我有 10 個叢集在跑,要怎麼管」的問題。**所以真正缺的不是更好的排程器,而是管理這些排程器與平台的東西。**

**目標不是取代 Kubernetes 或 Slurm**——它們在各自的領域很好——而是**橋接**:一邊是訓練、serving、sandbox 這些工作負載,一邊是散落在 Kubernetes、Slurm 等處的破碎算力。理想的**開放統一算力層**要能最佳化可得性、決定 job 跑在哪裡最好、處理執行,而且**讓工作負載不必知道底下是什麼**。

**SkyPilot 就是在做這件事**:完全開源、讓你在任何有算力的地方使用 AI 算力,核心理念是 **bring your own framework**——Ray、PyTorch、OpenEnv、Unsloth,你自己的框架都行;你只要提交「我需要 8 張 B300 跑這個」,SkyPilot 就負責編排:掃過你的 Slurm 叢集、Kubernetes 叢集甚至雲端 VM,安排資源、跑 job、把 log 與結果交回來。專案起源於幾棟樓外的 **Soda Hall**,根植於 **Sky Computing Lab** 的研究,社群活躍,也被目前最大的一些公司使用。

**實際長什麼樣:**
- 最簡單的取得資源方式就是 `sky launch`,指定要跑在哪個 infra、需要什麼 GPU。**從 Kubernetes 換到 AWS 只是改一個 flag**;換 GPU 型號也是改一個 flag(你的應用不需要知道底下跑什麼)。
- 更複雜的情境用 **job groups** 這個宣告式抽象:例如「我有一個 rollout server 需要這些資源、跑這些指令;我要開一千個 sandbox 跑東西;rollout server 跑 H100,trainer 跑 B200」,交給 SkyPilot 編排整個工作負載。過程中還附帶 **service discovery** 與**生命週期管理**——**其中一個 job 掛掉不代表整輪要失敗,它會自動重啟那個 job**。

**Serving 同樣受益**:你獲得**跨所有叢集的容量**——不必在單一叢集起一個 KServe 實例,而是讓 SkyPilot 跨叢集跑推論;發生故障時可**無縫把 replica 搬到還有容量的區域**。而把所有工作負載都走同一層之後,還能做一件有意思的事:**在同一批算力上同時跑推論與訓練**——推論請求暴增時,SkyPilot 可以**動態把資源從訓練挪給推論**(先 preempt 訓練 job,由你的 checkpointing 邏輯保住進度);等尖峰過去再自動縮回推論、繼續訓練。

**最後他強調 bring-your-own**:你不是把信用卡交給 SkyPilot 去買算力,而是**自帶算力、自帶資料,一切跑在你自己的環境裡**。結語呼應開場:我們不需要重新發明或取代 Kubernetes 與 Slurm,**需要的是一個統一層,橋接工作負載與你手上那一堆叢集**。

## English Notes

### Opening: Matt White — why openness matters more in the agent era (~02:58:30–03:04:45)

Former Global CTO of AI at the Linux Foundation, previously executive director and CTO of the **PyTorch Foundation**, now a visiting scholar at Columbia. No slides — "it's just me rambling" — but this is the frame for everything after.

**One: capability is surging exactly as openness comes under real pressure.** Models reason across long contexts, write and execute code, use tools and operate software, coordinate increasingly complex workflows, solve complex mathematical proofs, generate extensive codebases, and power systems **that take actions in production networks with real-world impact**. And at precisely this moment, restricting or even banning access to open-weight models **is no longer hypothetical** — it's being actively debated in Washington and elsewhere, alongside proposals to control the frontier through chips, compute, distillation, safety testing, and model release processes.

He concedes the point directly: **the safety, security, and national security concerns behind those discussions are real and legitimate, and deserve serious technically informed responses.** But the risk on the other side must be stated with equal clarity: **blunt restrictions concentrate capability, infrastructure, and decision-making into very few institutions**, turning AI from a broadly accessible general-purpose technology into something the rest of society is only permitted to *rent* from a few labs. "That cannot be the foundation on which we build the future."

**Two: openness is both how you get competition and part of how you get safety.** It's how researchers inspect systems, developers adapt them, students learn, enterprises keep sovereignty over their data and stack, and countries build AI capability without permanent dependence on a single vendor. It enables reproducible evaluation, transparent interfaces, independent scrutiny, shared security tooling, and the ability to find and fix problems. But **openness does not mean ungoverned** — not careless, unsafe, or a free-for-all. It means systems can be inspected, evaluated, adapted, and improved; interfaces are interoperable, implementations contestable, and **no single organization controls every layer or decides who may participate.**

**Three: agents raise the stakes because an agent is a stack.** Model, harness, invocable tools, environment, guardrails, the RL systems through which it improves, the evaluation infrastructure that measures it, and the compute underneath. It may depend on APIs, credentials, sandboxes, memory, inference systems, orchestration frameworks, and multiple forms of specialized hardware — crossing organizational, cloud, and geographic boundaries **while completing a single task**. Close and vertically control any one layer and the ecosystem becomes less portable, less competitive, and more fragile.

So **open models alone are not enough**. We also need open **environments** so agentic tasks can be reproduced and shared, open **RL frameworks** so more people can improve models and agents, open **compute layers** so workloads aren't captive to one cloud or vendor, and open **standards** so the components interoperate without permission from a central platform.

**The open agentic stack is not one project, framework, or model — it's a shared architecture built from open source software, open standards, and composable components.** The workshop walks four foundational layers: environments, models, reinforcement learning, compute. Different technical challenges, one shared principle: **the future of AI should be modular rather than monolithic, interoperable rather than captive, and open to participation rather than controlled by permission** — an architectural, economic, and strategic requirement, not just a philosophical preference.

### Talk 1: Ben Burtenshaw (Hugging Face) — Open Source Agentic RL Environments (~03:05:45–03:18:20)

**Thesis**: **RL environments are the best way to democratize AI**, mainly because they're easy to build — they're just applications, the kind of thing we write daily — so everyone can get involved.

**What an RL environment is.** The simplest framing: a world an agent acts within. Chess is the canonical case — the board is the world, the pieces are state, the rules are the actions, the score is the reward. Scale that up to **software engineering**: the task is a GitHub issue, the work is the pull request, the score is the test suite and CI. That's how papers like **SWE-smith** built software engineering environments. Strip the code out of the PR, have an agent generate it, use the test suite for reward, and you have an environment to train a software engineering agent. Carry that archetype to email triage, project management, and so on — find the task, the reward, and the state, and build them into applications.

**The ecosystem: a capability cycle.** He updates the old MATTER cycle (model, annotate, train, test, evaluate, revise) into **discover → benchmark → represent → train**. You *elicit* a capability with a harness or prompt and see the model can do a thing, maybe unreliably. You *evaluate* it with a separate evaluation harness that measures how reliable it is, and iterate on that as a community. You *represent* it, first as a dataset and eventually as an environment — **this is where domain expertise enters**; companies like **Mercor** go hire domain experts and build RL environments around a capability, partially based on the benchmark but ideally with no leakage between the two. Then the trainers come in — another software stack, another community.

The upshot: **environments are the means by which capabilities move from domain experts into models.** Once a capability is in the weights, everyone moves to the next one. Because so many communities meet at the environment, **that layer has to be open** — "imagine if datasets were in a closed format; it would be a particularly horrible situation."

**The current problem is fragmentation.** Environments live in papers and on GitHub. The recent **Kimi K3** paper came with thousands of environments; the **MiniMax** paper had around ten thousand; even the first **DeepSeek** paper had roughly a thousand. All implemented differently, shared differently, and many of them **sold** rather than readily available the way open-weight models are. It reminds him of being an MLE in 2017: find the implementation on GitHub, then chase the weights down on Google Drive — nothing exposed and interoperable the way model checkpoints are today.

**The problem compounds at training time.** A training process is a framework (**TRL**, **Unsloth**) updating a model based on its actions, but in between you need an **agent harness** to perform the task, interact with the environment, and use its tools. **Every edge there is a layer that needs an interface** — a harness can't hardcode an expected environment definition, and you need to work with multiple harnesses (he names Codex, Claude Code, and others).

**What OpenEnv does about it.**

- **Environment hubs**: about **4,000 environments** on Hugging Face today, in a standard format you can plug into most major training frameworks. Others exist (**Prime Intellect**) with more coming; they're sharing their spec with other orgs so anyone building a hub can use the same format for downloading and sharing.
- **A Docker-like CLI**: `openenv init` scaffolds a hello-world environment that just returns a generic score; from there you write the business logic yourself, or generate it with a coding agent. You can import environments from libraries like **verifiers**, and push, pull, and fork on the hub.
- **Coming next: discover and validate.** Finding an environment for your use case is hard today; hub search would give you a range of community environments — which creates the next problem: *which one is better? which will actually help my use case?* Hence a new `validate` command that checks the spec is valid and **trains a small model to see whether it lifts performance on a given benchmark**. Together those two commands give an autonomous loop for integrating environments into post-training.

**Three ways to use an environment**, easiest first:

1. **Evaluation** — what he suggests most people start with. Represent a typical workload as an environment, run a model (weights or just an API) over a set of tasks with a reward function, get an aggregate score.
2. **Reinforcement learning** — the core use. Roll a policy out over the environment, compute rewards per rollout, use something like **GRPO** to take the group mean and update weights, iterate.
3. **Distillation** — here you **can't distill from strings or tokens; you need log probabilities.** Roll out the student in the environment, take its log probs; have the teacher roll out over the same tokens, take its log probs; update the student on the difference (**reverse KL**). Variants: **self-distillation** (best student example versus the average), or giving the student **privileged information or a hint** — in the PR setup, hand the agent the actual solution up front and update weights on the difference between its bad run and its good run.

**How he expects this to work: leaderboards.** Environments currently live in "a bit of a shadow realm," rarely discussed in the community around model releases. If people build and try their own environments, put them on leaderboards, and figure out which ones actually contribute to model success, more people will get involved.

### Talk 2: Daniel Han Chen (Unsloth) — Making Open Models Not Suck (~03:19:38–03:35:35)

**Who Unsloth is.** One of the largest organizations on Hugging Face, roughly **400 million cumulative downloads** (a number he says is already outdated), the third largest model distributor in the world, shipping both the largest and smallest models. But they don't just distribute — **they fix bugs in open source models**, collaborating with the major labs and hardware providers to fix issues *before* the model reaches you (he cites OpenAI's gpt-oss, Llama, Gemma, Mistral). "If you're using open source models on your laptop, they were most likely fixed by us in some way."

**Quantization right now.** **Kimi K3** shipped Monday — the best open-weight model anyone can download, **1.5 TB** as released. They quantized it to **1 bit**, bringing it to about **600 GB**. The hard part: **Kimi K3 is natively 4-bit**, so 4-bit → 1-bit doesn't save as much. Their result: **76–78% of accuracy retained for an 82% size reduction** — shrinking a model by 82% doesn't make it 82% dumber, only about 16%. Separately, **DeepSeek V4 Flash** dropped the previous day (0731) at an odd hour in an odd time zone; they quantized it too, and it now needs **90 GB** of VRAM or RAM. His verdict: **the best model for its size** — Kimi K3 is much better but enormous, while V4 Flash actually fits on your machine.

**The METR curve and the pre-reasoning plateau.** Models now complete tasks that take humans **16 hours** (at 50% probability; about 6 hours at 80%). He plotted **Mythos / Fable** as a red line and **GPT-5.6 Sol** — the latter **with cheating examples removed**. Including cheating cases, GPT-5.6 Sol reaches **270 hours**, which he says isn't a good example; removing them puts it around 16.

His central observation is the flat stretch in the curve: **roughly 2023–2024 was an approximate plateau** (GPT-4 to GPT-4o showed little progress), because **reinforcement learning and reasoning hadn't been invented yet**. Fit two separate trends:
- **Gray line (pre-reasoning)**: capability **doubling every 7 months**. Had OpenAI never shipped o1-preview and told everyone reasoning was possible, models **would have plateaued by now**.
- **Green line (with RL and reasoning)**: doubling time shrinks to **3.5 months**. "Opus 5 came out a few days ago — wait 3.5 months and you'll get something better."

The caveat he stresses is that this holds only **if the trend continues**. Will the green line keep climbing, or do we fall back to the gray one and have to invent something new again? "That's a question we'll see answered in our lifetimes — **all you need to do is wait 3.5 to 7 months.**"

**Have open models caught up?** He cites **Artificial Analysis**' open-versus-closed curves: open models are now very close. But his favorite single benchmark is **WeirdML** (search "weird ML"), because it's genuinely hard to game. By WeirdML: **Fable 5 is very good and ginormously expensive**; for cost/accuracy balance he'd recommend **Opus 5 High**; among open models **Kimi K3 is extremely powerful** and on the leaderboard.

He then plots closed minus open as a **gap curve**. About a year and a half ago there's a stretch he calls the **open source drought** — the period after o1-preview when open models fell behind. Once **DeepSeek published how to do GRPO with R1**, open models snapped back to trend. His estimate: **without DeepSeek publishing GRPO, open models would be 16 months behind closed; now it's about 2 months.** A blog post extrapolates that by **December 2026** there'll be an open model as good as a closed one — all trend extrapolation, so "who knows; wait a few months and we shall see."

**Are collapsing token prices reasonable?** OpenAI cut **GPT Luna** prices by **80%** a few days ago. Shocking-sounding, but he thinks not — and he ran the numbers before the talk:

- Per **SemiAnalysis**' InferenceX benchmarks of vLLM / SGLang and other inference engines on NVIDIA and AMD GPUs: **DeepSeek V4 Pro** does about **13k tokens/s** on a single **GB300** → **47 million tokens per hour** at saturation.
- A GB300 costs roughly **$5 per GPU-hour**.
- Divide: **DeepSeek V4 Pro's floor price is about 11 cents per million tokens.** DeepSeek charges **44 cents per million input** and **87 cents per million output** — **so nobody is shedding money running these models.**
- By the same logic, assuming GPT-5.6 Luna is the same size as DeepSeek V4 (he's explicit it's most likely not), OpenAI still clears roughly **$1 per million output** at the new price.
- The contrast: **Kimi K3** is a new, not-yet-optimized architecture at about **5k tokens/s per GPU** (~2.6× slower than DeepSeek), giving a floor of about **30 cents per million tokens** — while it charges **$15 per million output**. That means Moonshot and other inference providers are taking about **$14.17** of your API bill. "If they wanted to reduce price, they could go all the way to 30 cents." Conclusion: **prices are still somewhat inflated, and DeepSeek is the only one charging near floor.**

**The other option: run locally.** He likes **Arena**'s Pareto efficiency plot (less so the Arena score itself): many open source models sit on the Pareto frontier. For **web development** (HTML/front-end), **Opus 5 Max is currently best with Kimi K3 just behind**; **GLM 5.2** and others are on the plot too. If you don't want to pay API costs, run locally and the cost drops to electricity plus some front-loaded setup.

Which is Unsloth's business: **dynamic quantization** down to very small bit widths. **GLM 5.2 at 1 bit** is his showcase — a one-shot prompt, no bug-fixing iterations, holding up well against full-precision closed models. They publish **perplexity** and **KL divergence** benchmarks to show 1-bit works. The goal is to push further: Kimi at 600 GB still probably doesn't fit on your computer, so they're aiming **below 1 bit** — Kimi at 250 GB, for example.

**Last point: the ARC-AGI harness settings.** A few days ago OpenAI noted the **ARC-AGI benchmark is somewhat unfair to GPT**, because the eval used a **rolling truncation of 175k tokens** with **compaction disabled** and **preserve thinking disabled**. His blunt takeaway: **just enable those two flags and OpenAI's models climb to 40% accuracy. You don't need to do anything else.** (He then ran out of time and skipped the remaining slides.)

### Talk 3: Shang Yang (RadixArk) — Miles: An Intro to Enterprise Facing RL with Miles (~03:36:48–03:45:35)

The speaker is a research resident at RadixArk and a PhD student at MIT, presenting **Miles** on behalf of the team.

**What Miles is**: an **open source RL engine** for frontier models, production-facing, built for speed and stability — "a stable, efficient, and reproducible reinforcement learning system at scale," minimizing the effort to run an RL job on modern language models across different environments and reward designs.

**Three layers:**

1. **Rollout** — **SGLang** as the rollout engine, specialized for high-throughput generation and highly compatible with today's agentic systems, environments, and infra.
2. **Orchestration** (middle) — organizes the rollout engine and the backend training systems as a whole so the system runs efficiently.
3. **Training** — supports **Megatron** and **FSDP**, and you can customize your own training engine on your own compute.

**Data flow**: the rollout engine generates trajectories by interacting with an external environment or agent framework (SGLang provides the generation layer; the environment itself can be heavily customized per customer requirements) → the middle layer turns trajectories into rewards and loss functions, i.e. training signals → Megatron or FSDP runs forward/backward, computes loss, updates weights → weights sync back to the inference engines, and the loop closes.

**Why SGLang as the rollout backend:**
- **Co-evolved with RL workloads**, including partial rollout support and dedicated rollout control, so specifying your workload is easy.
- **High-performance router design** — well-designed caching and load balancing for high-throughput generation.
- **Native asynchronous generation with the training engine** — an important feature for modern RL algorithms.
- Fast-moving, with optimizations such as **speculative decoding** with Miles, usable during the RL rollout stage.

**How Miles changes the RL development workflow:**
- **Customizable** — different workloads via pluggable function passes; defining your own RL workload, reward function, and update method is easy.
- **Modular and non-invasive** — switching training backends (FSDP, Megatron) is easy, with more backends coming.

**System design details:**
- **Multi-agentic rollout**, with **token-in-token-out (TITO)** support so the same multi-turn generation isn't tokenized and detokenized repeatedly — saving cost and making inference more stable.
- **R3 (routing replay)**: when training MoE models with RL, the same request can be routed to different experts across runs. R3 makes this **fully reproducible**.
- **Low precision**: end-to-end **MXFP8** support plus **per-token NVFP4 quantization** for the rollout stage, greatly reducing inference latency and increasing throughput — all verified in their latest blog against real training workloads.
- **LoRA support** for resource-constrained settings, training large models on fewer GPUs.

**Support matrix and track record:**
- **Day-zero support** for the newest models: **Kimi K3**, Thinking Machines Lab's Ling (captions render "inkling" — to verify), **DeepSeek V4**, **Nemotron Ultra**, and others.
- Wide precision and hardware coverage; fine-tuning recipes beyond SFT and RL, including **on-policy distillation**.
- Verified on RL training workloads across **more than 10,000 GPUs**. For **Kimi K2.6**, generation throughput was sped up to **12.5k output tokens per minute per GPU**.
- Stability work: R3, TITO, and **precision-aligned training** to reduce training–inference mismatch; plus **fault-tolerant recovery** and cluster backends including **Ray on Kubernetes, Slurm, and bare metal**.

**Recent releases:**
- **Day-zero support for Kimi K3** (nearly 3 trillion parameters), with fine-tuning on math problems lifting accuracy from around 40% to **76%**.
- **Ling (Thinking Machines Lab, trillion-parameter class)**: both full-parameter and LoRA fine-tuning, with **LoRA adapter synchronization** optimized (merging the LoRA rank into the SGLang inference engine) from nearly **50 seconds to under 3 seconds**.
- A recent **mixed-precision training** blog verifying that MXFP8 or NVFP4 maintain model accuracy and training stability while substantially accelerating rollout and inference.

### Talk 4: Romil Bhardwaj (SkyPilot) — AI Needs an Open Compute Layer (~03:46:13–03:55:58)

**The case**: AI needs an **open compute layer** — specifically, something that sits between your workloads and the actual GPUs they run on.

**Why AI infra is hard, told through OpenAI**: an exclusive Azure GPU agreement in 2016; a **$10 billion** Oracle deal in 2024 for more compute; another **$11 billion** with CoreWeave just a year later. And it still isn't enough — Sam Altman is on record asking for more GPUs and telling people to call if they can secure any. His conclusion: **if the most capitalized company on the planet can't secure enough GPUs, or get them in a single cluster, you probably can't either. The GPU crunch is very real.**

**What a typical AI organization actually has**: some **NeoCloud reservation** (a two- or three-year deal signed when the hyperscalers had no capacity); some hyperscaler **on-demand** instances to supplement it; some **on-prem** clusters for regulatory reasons or to keep data in-house; another cluster in Europe because there are customers in Europe; and a large **CPU cluster** for running environments and sandboxes. **Each was a sensible decision at the time; the result is a large collection of clusters you're now responsible for managing.**

**RL makes it worse — it turns this into a scheduling problem.** An RL run is one job composed of subcomponents with very different resource profiles: the **trainer** needs lots of VRAM and beefy GPUs; the **rollout server** generating trajectories needs less VRAM but a *lot* of instances; and for something like code generation, the **sandboxes** need a ton of parallel CPUs with very fast startup.

**Why not use existing solutions?**
- **Slurm**: two decades old, from HPC, and in his view among the best advanced scheduling and quota/priority systems out there. But it **doesn't support container isolation** (you can bolt on pyroot and similar layers, but it wasn't designed for it), and it was never built for serving — it's for batch jobs.
- **Kubernetes**: about ten years old, popular for microservices, very elastic and cloud-native. But a **super steep learning curve** ("hand Kubernetes to a researcher and they'll just go ask their agent to make it work") and it lacks AI-specific primitives, notably **gang scheduling**, again bolted on via schedulers like Volcano.

More importantly, **both are single-cluster managers**. Neither solves "I have 10 different clusters running — how do I manage them?" **What's missing isn't a better scheduler; it's something to manage all the schedulers and platforms you already have.**

**The goal isn't to replace Kubernetes or Slurm** — they're good at what they do — but to **bridge the gap** between workloads (training, serving, sandboxes) and compute fragmented across Kubernetes, Slurm, and clouds. An open unified compute layer should optimize availability, figure out the best place to run a job, handle execution, and do it **without the workload needing to know what's under the hood.**

**That's SkyPilot**: fully open source, use AI compute wherever you have it, **bring your own framework** — Ray, PyTorch, OpenEnv, Unsloth, your own. You submit "I need eight B300s to run this" and SkyPilot orchestrates: it looks at your Slurm clusters, Kubernetes clusters, and cloud VMs, provisions, runs the job, and returns logs and results. The project started a few buildings away in **Soda Hall**, rooted in **Sky Computing Lab** research, with an active community and adoption at some of the largest companies.

**What it looks like in practice:**
- The simplest path is `sky launch`: state the infra and the GPUs you need. **Switching from Kubernetes to AWS is one flag**, and so is switching GPU type — your application doesn't need to know what's running underneath.
- For complex work there's a declarative abstraction called **job groups**: "a rollout server with these resources running these commands; spin up a thousand sandboxes; put the rollout server on H100s and the trainer on B200s" — then SkyPilot orchestrates the whole workload, with **service discovery** and **lifecycle management** included. **One job failing doesn't fail the run** — SkyPilot restarts just that job.

**Serving benefits too**: you gain **capacity across all your clusters** instead of launching one KServe instance per cluster, and when a failure hits, SkyPilot **seamlessly moves replicas to a region where you still have capacity**. Routing all workloads through one layer also enables something interesting: **running inference and training on the same compute**. When inference requests spike, SkyPilot **dynamically reallocates from training to inference** — preempting training jobs while your checkpointing logic preserves progress — then scales inference back down after the spike and resumes training.

**Bring-your-own, emphatically**: you don't hand SkyPilot a credit card to buy compute. You bring your own compute from your own provider and your own data; everything runs on your own premises. Closing echo of the opening: we don't need to replace Kubernetes or Slurm — **we need a unified layer bridging workloads and all those clusters.**

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| OpenEnv | agentic 執行環境的開放規格與 hub;CLI 體驗類似 Docker(`openenv init`),支援 push/pull/fork | Open spec and hub for agentic execution environments; Docker-like CLI (`openenv init`) with push/pull/fork | Meta + Hugging Face 合作;HF 上約 4,000 個環境 / Meta–Hugging Face partnership; ~4,000 environments on HF |
| Prime Intellect | 另一個環境 hub | Another environment hub | OpenEnv 正與其共享 spec / spec sharing under way |
| verifiers | 可從中匯入環境的函式庫 | Library you can import environments from | |
| SWE-smith | 以 GitHub issue / PR / 測試套件建構軟體工程環境的代表性論文 | Representative work building SWE environments from issues, PRs, and test suites | 字幕聽成 "Swissmith" |
| Mercor | 雇用領域專家、圍繞能力打造 RL 環境的公司 | Company hiring domain experts to build RL environments around capabilities | 字幕聽成 "Merkore" |
| TRL | Hugging Face 的訓練框架 | Hugging Face training framework | |
| Unsloth | 開源模型的散布與 bug 修復,dynamic quantization | Open model distribution, bug fixes, and dynamic quantization | HF 上約 4 億次下載 / ~400M downloads |
| WeirdML | Daniel 最愛的 benchmark,理由是難以 game | His favorite benchmark, because it's hard to game | Google "weird ML" |
| METR 任務時長圖 / METR time-horizon plot | 模型能完成的人類任務時長隨時間的變化 | Length of human task a model can complete, over time | 講者說圖本身已過時 / he notes the plot is outdated |
| Artificial Analysis | 開源 vs 閉源模型能力曲線 | Open vs closed model capability curves | |
| SemiAnalysis InferenceX | 推論引擎在 NVIDIA / AMD GPU 上的吞吐 benchmark,他用來算 token 地板價 | Inference engine throughput benchmarks used for his floor-price calculation | |
| Miles | RadixArk 的開源 RL 訓練框架,SGLang rollout + Megatron/FSDP 訓練 | RadixArk's open-source RL training framework; SGLang rollout plus Megatron/FSDP training | github.com/radixark/miles;PyTorch Foundation blog 有介紹 |
| SGLang | Miles 的 rollout 引擎;高吞吐生成、非同步、partial rollout | Miles' rollout engine: high-throughput generation, async, partial rollout | |
| SkyPilot | 開源統一算力層,跨 Kubernetes / Slurm / 雲端 VM 編排 AI 工作負載 | Open source unified compute layer orchestrating AI workloads across Kubernetes, Slurm, and cloud VMs | 起源於 UC Berkeley Sky Computing Lab |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| open aentic stack / compostability | open agentic stack / composability |
| Linux edition | Linux Foundation |
| Ben Burtonshaw | Ben Burtenshaw |
| openend / OpenM / open m / openm in it | OpenEnv / `openenv init` |
| Swissmith | SWE-smith |
| Merkore | Mercor |
| Kimmy K3 / Kim K3 / Kim key3 / KI | Kimi K3 |
| Miniaax / Miniax | MiniMax |
| deep seat / deep suite / Deep See | DeepSeek / DeepSWE(視語境)|
| Daniel Honchen | Daniel Han Chen |
| Unsolve | Unsloth |
| GWSS | gpt-oss |
| Jamma / MRO | Gemma / Mistral |
| GBD / GBD 5.6 soul / GBD Luna | GPT / GPT-5.6 Sol / GPT Luna |
| meter plot | METR plot |
| gpo | GRPO |
| Ko divergence | KL divergence |
| Shangyang from Radics Arc / Radx | Shang Yang from RadixArk |
| mouse / MOS | Miles |
| Nvidia action / maxron | Megatron |
| FSTP | FSDP |
| MVIP4 / MXP8 | NVFP4 / MXFP8 |
| the Chinese(多處)| inference(自動字幕把 "inference" 聽成 "Chinese")|
| three fore models / R3 | R3 (routing replay) |
| tito | TITO (token-in-token-out) |
| natron ultra | Nemotron Ultra |
| sinking machines lab | Thinking Machines Lab |
| kubernetics | Kubernetes |
| Raml Bardage / Romeo Barage / Romel | Romil Bhardwaj |
| Sky Palot / Skypet / Sky Pallet / SkyPower | SkyPilot |
| slur / slowmo / slum | Slurm |
| core(「with core to get even more GPUs」)| CoreWeave |
| Sam Olen | Sam Altman |
| pyroot | pyxis / enroot(容器化 Slurm 外掛,待確認)|
| soda hall | Soda Hall (UC Berkeley) |
| case serve | KServe |
| old charts | cold starts |

## 待確認 / To Verify

- **Thinking Machines Lab 的兆級參數模型名稱**:逐字稿作 "the inkling from sinking machines lab",Miles 對其提供 day-zero 支援並做 full/LoRA fine-tuning。名稱拼法待確認。/ Name of the trillion-parameter Thinking Machines Lab model rendered as "inkling".
- **Miles fine-tune Kimi K3 用的數學題目集**:逐字稿作 "the amass problem",準確率 40% → 76%,實際 benchmark 名稱待確認。/ The math benchmark used, rendered as "the amass problem".
- **Slurm 的容器化外掛**:逐字稿作 "pyroot",語境為「可以硬接上去的容器層」,正確名稱待確認(可能為 pyxis / enroot)。/ The Slurm container plugin rendered as "pyroot".
- **Daniel 提到的「2026 年 12 月開放模型追平閉源」blog post** 的出處。/ Source for the blog post extrapolating open–closed parity by December 2026.
- **GPT-5.6 Sol 在 METR 上「含作弊 270 小時 / 去除作弊約 16 小時」**的原始資料來源。/ Source for the METR figures with and without cheating cases.
- **OpenAI 關於 ARC-AGI harness 設定(175k rolling truncation、compaction、preserve thinking)的公告出處**。/ Citation for OpenAI's ARC-AGI harness note.
- **Ben 提到的環境數量**(Kimi K3 數千、MiniMax 一萬、DeepSeek 約一千)為現場口述,原論文數字待核對。/ Environment counts quoted from memory on stage; verify against the papers.
- OpenAI 與 CoreWeave 的 **110 億美元**合約、與 Oracle 的 **100 億美元**合約金額為講者口述,待核對。/ The $11B CoreWeave and $10B Oracle figures were quoted on stage.
