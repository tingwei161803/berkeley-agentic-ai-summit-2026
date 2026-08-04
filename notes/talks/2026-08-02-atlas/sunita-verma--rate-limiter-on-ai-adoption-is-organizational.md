---
title: "Rate Limiter on AI Adoption Is Organizational"
title_zh: "AI 採用的速率限制器來自組織,不是技術"
speaker: "Sunita Verma"
affiliation: "Chief Technology Officer, Ironclad"
type: keynote
stage: Atlas
date: 2026-08-02
session: "Session 1: Enterprise AI"
video: "https://www.youtube.com/watch?v=LGW_6P1CMC8&t=24s"
video_range: "00:00:24–00:18:06"
transcript: "tmp/[English (auto-generated)] Atlas Stage - August 2nd - Morning Session [DownSub.com].srt"
status: draft
tags: [enterprise-ai, adoption, evals, organizational-change, developer-productivity]
---

# AI 採用的速率限制器來自組織,不是技術(Rate Limiter on AI Adoption Is Organizational)

**一句話總結**:企業導入 AI 卡住,不是因為技術不夠好,而是因為技能落差、流程與文化沒跟著改;Ironclad 的解法是「全員同時賦能 + 把教育當基礎設施 + 把流程從瀑布式改成前期共同定規格」,九個月內把工程速度換了一個檔次。
**One-line summary**: Enterprise AI stalls on people and process, not on model capability — Ironclad's answer was to upskill every function simultaneously, treat education as infrastructure, and move spec-writing to the front of the process so agents get well-specified work.

## 中文筆記

### TL;DR

- **主張**:企業 AI 採用卡關的原因不是「技術不行」,而是流程、文化與技能落差。所有前沿研究最終要靠這幾千家公司裡的人把價值兌現,否則就白做了。
- **診斷起點**:同一個 feature,兩位工程師的估時差距大到讓她停下來調查。差異不在年資或熟悉度,而在於一位是 **AI-pilled**(懂得怎麼駕馭、引導這項技術),另一位把 AI 當 chatbot 用卻自認已經掌握。
- **為什麼人會誤判自己**:手機、雲端這些前代技術出錯時,技術本身會「頂回來」,你被迫學會;AI 的介面是自然語言,光是能對話就讓人以為自己會了,忽略了輸出與結果都需要驗證。這是一套完全不同的心智模型。
- **只賦能工程師是短視**:多數大企業說「我們先讓工程師用起來」,結果是解開一個環節、卻在其他環節製造瓶頸。Ironclad 從第一天就讓 engineering / product / design **同時**上車。
- **撞到 Amdahl's Law**:技能補起來之後,產品開發速度仍沒起飛——因為流程沒改。仍是瀑布式(product 研究 → 交棒 UX → 交棒工程),工程端做完就在等產品回答。你只優化一段,沒碰的那段就變成新瓶頸。
- **三個修正**:教育即基礎設施(共同語彙、共用工具、context / RAG / memory 的統一系統)、流程前移(相關角色早期一起把問題吵清楚並把解法 memorialize 成 markdown 或 Notion 頁,再交給 agent 執行)、工具與護欄(code review agent + 一整套 skills 把關產出品質)。
- **成果可複製**:一家 Fortune 100 客戶主動要求跑同一套計畫,結果非常相似——他們的工作也同樣加速了。

### 重點整理

#### 主張:卡住的不是技術(約 00:01)

演講一開始就把結論放上桌:企業裡 AI 的採用停滯,**不是因為技術不 work 或還沒到位**,而是流程、文化這類「其他原因」。她接著自問一個更根本的問題:為什麼在座的人該在意企業有沒有把技術部署下去?她的答案是——峰會上這兩天講的所有好東西,最終都必須轉化成價值,否則就是白費;而技術的最終使用者,是散落在我們周圍那幾千幾萬家公司裡的人。

#### 起點:兩位工程師,兩個天差地遠的估時(約 00:02)

她加入 Ironclad 大約一兩個月後(演講當下往回推九個月),在一場 feature 討論裡刻意做了個實驗:分別問兩位工程師「做這個要多久」。回來的數字差距大到讓她停下來追究。

深入查下去,差異**不是**資深程度,也**不是**對 codebase 的熟悉度:一位是 AI-pilled,理解怎麼跟這項技術協作、怎麼引導它;另一位主要把 AI 當 chatbot 用,而且覺得自己已經掌握了。

她意識到當下有個選擇:以技術演進的速度,這道落差只會被複利放大,她可以接受一個「雙速工程組織」,也可以現在就動手處理。

#### 為什麼人們會誤以為自己已經掌握 AI(約 00:03)

她的推論是介面造成的錯覺。行動、雲端這些前一代技術,出錯時錯誤是**顯性**的——技術會把你頂回來,你必須先搞懂哪裡錯了才能往前。AI 不一樣:介面是自然語言,光是能跟它對話,就讓人覺得自己知道在做什麼,卻沒意識到**輸出要驗證、結果也要驗證**。

她也提醒台下:在場的人多半會說「這我早就知道」,但外面有一大批勞動力並不在同一個心智模型上。要讓技術被那群人採用,就得針對這件事做點什麼。

#### 只賦能工程師是短視:全員同時上車(約 00:05)

她跟很多 Fortune 500 甚至更大的公司聊過,絕大多數的做法是「我們會先賦能工程師」。她認為這是短視的:**你解開一個職能,卻在組織的其他部分製造瓶頸**。

Ironclad 從一開始就刻意反著做:所有人同時賦能。即使有些人已經很 AI-native、覺得不需要,他們仍然堅持 engineering、product、design 要一起被賦能。她給團隊設的目標是:讓公司變成一個「**用 AI 做東西、以及做 AI 這件事,都不是少數人的特製品**」的地方。

三個原則:

1. 不會有一群「光環組」在旁邊做 AI、然後拖著其他人走。
2. 難的部分——結果驗證、eval、eval harness——透過**工具**交付,讓所有人同時受益。
3. 不是只有頂尖的人能用 AI:**每個人都必須用、也都會用**。

#### 執行:20 天養成計畫與 12 月 hackathon(約 00:06)

她利用了一個現成的節點:2025 年 12 月的公司 hackathon(當時她到職才三個月)。她要團隊帶著 AI 能力進場,讓 hackathon 產出的是 AI 相關的成果。

於是她設計了一個 20 天的計畫,在 hackathon 前跑完:

- **第一天**:她自己開課(因為她本來就是做技術出身),全公司任何人都可以來聽。內容是 LLM 基本功——LLM 底層怎麼運作、怎麼思考 context、in-context learning、prompt optimization、tuning、evaluations。
- **第 2–20 天**:每天一位工程師上台講自己用這項技術做了什麼、怎麼做的、踩到什麼問題、學到什麼。
- 中間靠 Slack 頻道、日常互動和工程師自發的臨時聚會維持動能。

hackathon 當天參與度極高,團隊做出了她原本不覺得做得出來的東西,正面地嚇到她。**就「流暢度」而言,公司當時已經到位了。**

#### 撞牆:Amdahl's Law(約 00:09)

時間來到 2026 年 1 月。她原本預期產品裡的功能開發會跟著起飛,實驗端確實起來了,但**產品端沒有**。

她的診斷是 **Amdahl's Law**:你優化了流程的一段,那些你沒動到的環節就會變成新的瓶頸。具體來說,各職能都在用 AI、也在做 AI,但**流程一點都沒改**——仍然是瀑布式:product 做研究 → 交棒給 UX → 再交到工程手上;工程端很快做完,然後大部分時間都在等產品團隊回答問題。

#### 三個修正(約 00:10)

**一、教育即基礎設施。** 不只是上課,而是建立共同語彙(shared lexicon)、共用工具、共用 harness,以及全公司統一的 context management、RAG、memory 系統——把組織記憶收斂進單一系統。

**二、流程前移。** 現在要做一個東西時,相關的人會在**很早期**就聚在一起:討論問題、辯論問題、提出解法、反覆迭代,最後把解法 **memorialize 成一份 markdown 或 Notion 頁**,再把這份被打磨過的規格交給 AI agent 去執行。

她在這裡呼應了前一天 Ion Stoica 教授的演講:AI 的產出之所以不如預期,很大一部分來自**需求的 under-specification**。讓所有人在流程最前端把需求攤開講清楚,正是在處理這件事。她強調 Ironclad 並不完美,但把問題的**約束、邊界與解空間**先講清楚再交給 agent,確實看到很好的結果。

**三、工具與護欄。** 除了 code review agent,他們還建了一整套 skills,確保 agent 產出的品質(特別是寫程式這塊)符合公司標準,**讓沒有人需要去猜自己的 agent 有沒有做對事**。

#### 今天的樣子:agent framework、自動 eval、自建 code-gen harness(約 00:12)

- **Agent framework**:讓任何人都能很快建出一個 agent。底層用 OpenAI 的 Agents SDK 與 Vercel 的 AI SDK,接上各家前沿模型;他們也開始 tune 自己的模型,掛在這些 agent 後面。周邊建了持續 context 最佳化、memory 管理、持續 evals、prompting 等基礎設施。
- **自動化 evals**:系統大部分區域都有。用 LLM judge 評估 agent 產出,再交給一個 evaluation agent 對照 rubric 比較,直到它判定 eval 已經足夠接近 rubric 為止;整個過程持續執行、**不需要工程師介入**。東西一旦被建好、review 完、check in,就自動走這條評估流程。
- **自建 code generation harness**:他們評估過市面上的方案(Codex harness、Claude 的 harness 等),結論是沒有一個貼近他們想要的樣子。於是把其中一些(含開源方案)當作 benchmark 與底材,在上面搭建自己的 harness,並使用 **Temporal**。
  - 使用方式:任何人(**包含現在也在寫程式的 PM**)都能對 harness 下任務——要一個 UI、要一段後端服務、要任何一塊程式碼都可以。
  - Harness 會**開一台 VM**,在裡面把環境架到接近 production 的狀態,產生程式碼、在裡面測試,最後產出一個 **review-ready 的 PR**,再交給人類或 review agent 審查。
  - 目前處於 dogfood 階段,結果非常好。

#### 成果與外推(約 00:15)

- **產品端**:Ironclad 是商用法務(legal tech)產品,幾乎所有矽谷公司都是客戶,**包含各家前沿實驗室**。產品裡已經有許多 agent 在跑真實運行中的合約,背後承載的是數十億美元等級的價值。
- **工程統計**:執行速度和一年前完全不是同一回事(她特別說明圖表尾端的下墜是資料未收齊,不是退步)。
- **可複製性**:一家 Fortune 100 客戶主動找上門,希望跑同一套計畫。這個計畫原本不是設計來給外部用的,但他們還是幫客戶跑了,**結果非常相似**,客戶端也看到工作加速。
- **收尾**:她呼應前一天 Andrew Ng 的 fireside chat——Ng 擔心做 AI 的人對「教育」投資不足,而這會成為採用的一大障礙。她說自己這場就是在替這個論點補上一個來自實務的資料點。

### 金句

> "The adoption of AI in enterprises is not stalling because the technology is not working or is not there. It's stalling because of other reasons. And one of the other reasons tends to be processes, culture and so on."(約 00:01:30)

整場演講的論點就壓在這一句上:瓶頸在組織,不在模型。

> "We want to make sure we are a company where building with AI and building AI is not a bespoke act for certain people."(約 00:05:38)

「AI 不該是少數人的特製品」——這是她拒絕雙速組織的理由。

> "It's actually Amdahl's law … you update one part of the process, but now the parts of the process that you didn't touch actually become the bottleneck."(約 00:09:11)

補完技能只是第一段;不改流程,瓶頸只是換了個位置。

> "Education is an important component of getting AI deployed in enterprises."(約 00:17)

呼應 Andrew Ng 的擔憂,也是她整場的收束。

## English Notes

### TL;DR

- **The claim**: enterprise AI adoption isn't stalling because the technology doesn't work — it stalls on process, culture, and a skills gap. All the frontier research showcased at the summit only pays off if people inside thousands of ordinary companies can turn it into value.
- **The diagnosis started with an experiment**: two engineers gave wildly different estimates for the same feature. The gap tracked neither seniority nor codebase familiarity — one engineer was AI-pilled and knew how to steer the technology; the other used AI mostly as a chatbot while believing they had already mastered it.
- **Why people misjudge themselves**: with mobile or cloud, errors were obvious and the technology pushed back, forcing you to learn. AI's natural-language interface makes conversation feel like competence, and hides the fact that both outputs and outcomes need validation. It requires a genuinely different mental model.
- **Enabling only engineers is myopic**: most large companies start there, which unblocks one function while creating bottlenecks everywhere else. Ironclad deliberately enabled engineering, product, and design at the same time.
- **Then they hit Amdahl's Law**: fluency arrived, but product velocity didn't follow, because the process hadn't changed. They were still running waterfall — product research, hand-off to UX, hand-off to engineering — and engineers finished fast, then waited on answers.
- **Three fixes**: education as infrastructure (shared lexicon, shared tooling and harnesses, one system for context management, RAG, and memory); moving specification to the front (the right people convene early, argue the problem out, and memorialize the solution as markdown or a Notion page before handing it to an agent); and tooling and guardrails (code-review agents plus a library of skills that enforce output quality).
- **It generalizes**: a Fortune 100 customer asked Ironclad to run the same program for them; the outcomes were very similar, and the customer saw the same acceleration.

### Key Points

#### The claim: the bottleneck isn't the technology (~00:01)

She put the conclusion on the table immediately: AI adoption in enterprises is not stalling because the technology is missing or broken — it stalls for other reasons, chiefly process and culture. The follow-up question is why anyone in the room should care, and her answer is that all the excellent work presented at the summit has to deliver value or it was for nothing. The eventual users of this technology are the people inside the thousands of companies around us.

#### The starting point: two engineers, two very different estimates (~00:02)

About a month or two after joining Ironclad — nine months before the talk — she ran a deliberate experiment during a feature discussion, asking two engineers separately what it would take to build the same thing. The estimates diverged enough to give her pause.

Digging in, the difference was not seniority and not familiarity with the codebase. One engineer was AI-pilled — they understood how to work with the technology and steer it. The other was using AI mainly as a chatbot while feeling they had already mastered it.

That left her with a choice. Given how fast the technology was moving, the gap would compound: she could accept a two-speed engineering organization, or do something about it.

#### Why people believe they've mastered it (~00:03)

Her explanation is that the interface creates the illusion. With previous technology waves — mobile, cloud — errors were obvious. The technology pushed back, and you had to learn what was going wrong before you could make progress. With AI, the interface is natural language, so simply talking to it makes you feel you know what you're doing, without realizing that the outputs need to be validated and the outcomes need to be validated. It is a very different mental model.

She also noted that many people in the audience would say they already knew this — but a huge workforce out there does not share that mindset, and getting the technology adopted by that group requires doing something deliberate.

#### Enabling everyone at once (~00:05)

Talking to other companies — Fortune 500 and larger — she found that most say some version of "we'll enable our engineers." She considers this myopic: you enable one function and manufacture bottlenecks elsewhere in the organization.

Ironclad did the opposite from the start: everyone gets enabled simultaneously. Some people were already AI-native and felt they didn't need it; the company was nevertheless clear that engineering, product, and design would be enabled together. The goal she set: be a company where building with AI, and building AI, is not a bespoke act reserved for certain people.

Three principles:

1. There will be no halo group doing AI off to one side and dragging everyone else along.
2. The hard parts — outcome validation, evals, eval harnesses — get delivered through tooling, so everyone benefits at once.
3. It isn't that only top people get to use AI: everybody has to, and everybody will.

#### Execution: a 20-day program before the December hackathon (~00:06)

She used an event already on the calendar — the company hackathon in December 2025, when she was three months into the job. She wanted the team to arrive AI-ready and the hackathon to produce AI-built outcomes, so she designed a 20-day program to run beforehand.

Day one, she taught the classes herself, open to anyone in the company: LLM fundamentals, how LLMs work under the hood, how to think about context, in-context learning, prompt optimization, tuning, and evaluations. For the remaining days, one engineer per day presented what they had built with the technology, how they built it, what problems they ran into, and what they learned. Momentum was sustained through Slack channels and impromptu get-togethers the engineers organized themselves.

Participation at the hackathon was very high, and the team built capabilities she hadn't thought they could — a positive surprise. On fluency, the company had arrived.

#### Hitting Amdahl's Law (~00:09)

By January 2026, feature development still hadn't accelerated the way she expected. Experimentation had taken off; shipping into the product hadn't.

The diagnosis was Amdahl's Law: you update one part of the process, and the parts you didn't touch become the bottleneck. Every function was building AI and building with AI, but the process itself had not shifted at all. They were still running a waterfall — product does research, hands off to UX, hands off to engineering — and engineers would finish quickly, then spend most of their time waiting on answers from product.

#### The three fixes (~00:10)

**Education as infrastructure.** Beyond classes: a shared lexicon, shared tooling, shared harnesses, and common systems for context management, RAG, and memory — pulling organizational memory into a single system.

**Move specification to the front.** Now, when building something, the relevant people convene early: they discuss the problem, debate it, propose a solution, iterate on it, and memorialize the result as a markdown doc or a Notion page. Only then is that fleshed-out work handed to an agent to execute.

She tied this to Ion Stoica's talk the previous day: a major reason AI outcomes disappoint is under-specification of requirements. Getting everyone together at the front of the process is how you flesh those requirements out first. She was careful not to claim perfection, but clearly specifying the constraints, the boundaries, and the solution space before handing work to an agent has produced good outcomes.

**Tooling and guardrails.** Beyond code-review agents, they built a library of skills that ensure agent output — especially code — meets company standards, so nobody has to wonder whether their agent is doing the right thing.

#### Where they are now (~00:12)

- **Agent framework**: lets anyone create an agent quickly. Built on OpenAI's Agents SDK and Vercel's AI SDK, connected to the frontier models; they have also started tuning their own models, which are hooked up behind these agents. Around it sits infrastructure for continuous context optimization, memory management, continuous evals, and prompting.
- **Automated evals** across large parts of the system: LLM judges evaluate agent output, then an evaluation agent compares it against a rubric and keeps iterating until the eval comes close enough to the rubric. It runs continuously without pulling engineers in — once something is built, reviewed, and checked in, it flows into this evaluation process automatically.
- **Their own code-generation harness**: they evaluated what was available — the Codex harness, Claude's harness — and none matched what they wanted, so they used those (and open-source ones) as benchmarks and substrate and built their own on top, running on Temporal. Anyone, including product managers who now code, can hand the harness a job: a UI, a backend service, any piece of code. The harness spins up a VM, sets up an environment close to production inside it, generates the code there, tests it there, and produces a review-ready PR for a human or a review agent. It is in dogfood and producing very good results.

#### Results and generalization (~00:15)

Ironclad is a commercial legal-tech product; nearly every Silicon Valley company is a customer, including the frontier labs. Agents live in the product today, acting on live contracts carrying billions of dollars of value. Engineering statistics show a very different execution velocity than a year ago (she flagged that the drop at the end of the curve is incomplete data, not regression).

None of this is proprietary to Ironclad. A Fortune 100 customer asked to run the same program; although it hadn't been designed for external use, they ran it, and the outcomes were very similar — that customer is also seeing acceleration.

She closed by connecting to Andrew Ng's fireside chat the day before: Ng worries that people building AI under-invest in education, and that this becomes a barrier to adoption. Her talk, she said, is a data point from experience in support of that claim.

### Quotes

> "The adoption of AI in enterprises is not stalling because the technology is not working or is not there. It's stalling because of other reasons. And one of the other reasons tends to be processes, culture and so on." (~00:01:30)

The whole talk rests on this: the bottleneck is organizational, not architectural.

> "We want to make sure we are a company where building with AI and building AI is not a bespoke act for certain people." (~00:05:38)

Her stated reason for refusing a two-speed organization.

> "It's actually Amdahl's law … you update one part of the process, but now the parts of the process that you didn't touch actually become the bottleneck." (~00:09:11)

Closing the skills gap was only the first segment; without process change, the bottleneck just moves.

> "Education is an important component of getting AI deployed in enterprises." (~00:17)

Her closing line, and an echo of Andrew Ng's concern from the previous day.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Ironclad | 商用法務 / 合約管理平台,幾乎所有矽谷公司(含前沿實驗室)都是客戶 | Commercial legal-tech / contract platform; nearly all Silicon Valley companies including frontier labs are customers | 講者任 CTO / speaker is CTO |
| OpenAI Agents SDK | Ironclad 內部 agent framework 的基礎之一 | One of the foundations of Ironclad's internal agent framework | 逐字稿作 "agent SDK from OpenAI" |
| Vercel AI SDK | Ironclad agent framework 的另一個基礎 | The other foundation of their agent framework | 逐字稿誤植為 "Versell" |
| Temporal | 自建 code generation harness 的工作流引擎 | Workflow engine behind their in-house code-generation harness | 講者提到 Temporal 前一天也在會場 |
| Ironclad 內部 agent framework | 讓全公司任何人快速建 agent,含 context 最佳化、memory、持續 evals | Internal framework letting anyone build agents; context optimization, memory, continuous evals | 未公開命名 / unnamed publicly |
| Ironclad code generation harness | 開 VM、架近似 production 環境、生成並測試程式碼、產出 review-ready PR | Spins up a VM, builds a near-production environment, generates and tests code, emits a review-ready PR | dogfood 階段 / in dogfood |
| Ion Stoica 前一天的演講 | 談 AI 產出不如預期源於需求 under-specification | Prior-day talk on under-specification of requirements as a cause of poor AI outcomes | 逐字稿誤植為 "Ian Stoya" |
| Andrew Ng fireside chat | 擔憂教育投資不足會成為 AI 採用的障礙 | Warned that under-investment in education will become an adoption barrier | 逐字稿誤植為 "Andrew Ing" |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Sunita WHMA / Senita | Sunita Verma |
| Andel's law | Amdahl's Law |
| Ian Stoya | Ion Stoica |
| Andrew Ing | Andrew Ng |
| Versell | Vercel |
| AI pled / AID / AI'd | AI-pilled |
| evas | evals |
| hardness / Codex hardness / Claude's hardness | harness / Codex harness / Claude's harness |
| eval harnesses(語音正確,但字幕多處拼作 "harnesses"/"hardness" 混用) | eval harnesses |

## 待確認 / To Verify

- Ironclad 內部 agent framework 與 code generation harness 均未公開命名,無法查證產品名。/ Ironclad's internal agent framework and code-generation harness were not named publicly.
- 「以某些開源方案作為 substrate」具體指哪些開源 harness,講者未點名。/ Which open-source harnesses they used as substrate was not specified.
- 工程統計圖表(執行速度曲線)的具體數字未在演講中念出,只有定性描述。/ The engineering-velocity chart's figures were shown on slides but never stated aloud.
- 那家跑同一套計畫的 Fortune 100 客戶未具名。/ The Fortune 100 customer that ran the same program was not named.
