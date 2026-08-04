---
title: "Information Retrieval in the Age of Agentic AI"
title_zh: "Agentic AI 時代的資訊檢索"
speaker: "Tanya Roosta"
affiliation: "Director of AI, AMD; Berkeley alumna"
type: talk
stage: Compass
date: 2026-08-01
session: "Session 2: Frameworks & Dev Platforms"
video: "https://www.youtube.com/watch?v=AO0RXP-fVZQ&t=1798s"
video_range: "00:29:58–00:37:19"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [information-retrieval, rag, evaluation, deep-research, benchmarks]
---

# Agentic AI 時代的資訊檢索(Information Retrieval in the Age of Agentic AI)

**一句話總結**:檢索的工作單位已經從「查一次」變成「和世界持續對話」——但我們的評估方式還停在拿 BLEU / ROUGE 打最終答案的分數;要跟上,就得改成**評估整條 trace:每一跳的正確性、是否足以回答問題,以及 token 與延遲的成本**。
**One-line summary**: The unit of work in retrieval has moved from a lookup to an ongoing conversation with the world — yet we still grade the final answer with BLEU and ROUGE. Evaluation has to move to **the trace: the correctness of every hop, whether each hop was adequate, and the cost in tokens and latency**.

> 講者以視訊參與,連線調整後於 **00:32:25** 正式開始。/ She joined remotely; after an A/V delay the talk actually starts at **00:32:25**.

## 中文筆記

### TL;DR

- **典範轉移**:從傳統 IR / classic RAG 的直線流程(query → 取文件 → 排序 → rerank → 給使用者一份清單),轉向 agentic flow(planning → 判斷 query intent → 搜尋 → 蒐集 → 分析 → critique → 給出最終結果)。**工作單位從 lookup 變成「與世界的持續對話」**,而且動輒 20 turns 以上、變成 multi-hop。
- **令人不安的落差**:互動已經是多輪、有時間性、須有證據支撐的,**但評估還停在看最終答案、用 BLEU / ROUGE 打分**。這對 agentic IR 根本不管用。
- **該怎麼做**:改看 **trace**——逐跳評估正確性、每一跳是否足以回答使用者的問題,以及 token 數與 latency 這類成本指標。
- **領域走向**:reasoning-aware retrieval(用 agent 的推理 trace 而非只有 query keywords)、multi-turn / hop-aware benchmark(如 **MTRAG**)、graph RAG、self-RAG(抑制幻覺)、adaptive RAG(依複雜度與成本路由 query),以及把 **token 用量本身當成一個 IR 指標**。

### 重點整理

#### 從 classic RAG 到 agentic IR(約 00:32–00:34)

Roosta 用一組對照開場。**傳統資訊檢索 / classic RAG** 是一條直線:使用者送出 query → 搜尋引擎取回文件 → 產生排序清單 → rerank → 把清單呈現給使用者。

**Agentic flow** 則不同:agent 會做 planning、試著弄清楚這個 query 的 intent、執行搜尋、蒐集結果、分析、critique,最後才給出結論。她的總結是:**工作單位已經從「查詢」變成「與世界持續進行的一場對話」**。

這件事最明顯地體現在 deep research agent 上。她舉的例子是一個關於膽固醇藥物的問題:agent 先理解問題意圖,然後用各種工具去蒐集網站資料、價格資訊、藥物交互作用等等,再把答案**扎根在檢索到的證據上**,最後呈現給使用者——省下人類自己翻文件與部落格文章的好幾個小時。她提到現在這類 agentic IR **常常跑到 20 個 turn 左右,已經是 multi-hop 的東西**。

#### 落差:評估方法還停在單輪時代(約 00:34–00:35)

「但這裡有一個令人不安的落差。」我們要評估 agentic IR 時,**仍然傾向只看最終答案**,用 BLEU、ROUGE 這類分數判斷答案對不對。可是現在的資訊尋求是**互動的、多輪的、有時間面向的、而且必須是 evidence-driven**——單看最終答案根本測不準。

她的處方是**回到 trace**:逐跳去評估每一步的正確性、每一跳是否**足以**回答使用者的問題,以及成本面——用了多少 token、延遲多少。

#### 領域正在往哪走(約 00:36)

她列出幾條正在成形的方向:

- **Reasoning-aware retrieval**:檢索訊號不再只有 query 的關鍵字,而是納入 **agent 的推理 trace**。
- **Multi-turn / hop-aware benchmark**:如 **MTRAG** 這類專為多輪對話式 RAG 設計的評估集。
- **Graph RAG**:讓檢索看得到實體之間的關係。
- **Self-RAG**:用來削掉一部分幻覺。
- **Adaptive RAG**:依 query 的複雜度與所需投入來路由。
- **把 token 用量當指標**:實際計算並最佳化用掉多少 token,把它視為資訊檢索的一項評估指標。

**收尾**:我們尋求資訊的方式已經改變,agent 改變了我們取得資訊的方法;那麼**我們評估「這些 agent 有沒有做對事、有沒有達成它設定的目標」的方式,也必須跟著改變**。

## English Notes

### TL;DR

- **The shift**: from traditional IR / classic RAG as a straight line (query → fetch documents → ranked list → rerank → hand the user a list) to an agentic flow (plan → infer intent → search → gather → analyze → critique → present). **The unit of work moved from a lookup to an ongoing conversation with the world**, often running 20 turns and going multi-hop.
- **The uncomfortable gap**: information seeking is now interactive, multi-turn, temporal, and evidence-driven, **but we still grade the final answer with BLEU and ROUGE**. That doesn't work for agentic IR.
- **What to do instead**: evaluate the **trace** — the correctness of every hop, whether each hop was adequate to answer the user, and the cost in tokens and latency.
- **Where the field is heading**: reasoning-aware retrieval (using the agent's reasoning traces, not just query keywords), multi-turn/hop-aware benchmarks such as **MTRAG**, graph RAG, self-RAG for hallucinations, adaptive RAG routing by query complexity and effort, and **token consumption itself as a retrieval metric**.

### Key Points

#### From classic RAG to agentic IR (~00:32–00:34)

Roosta framed the change as two pictures. **Traditional IR and classic RAG** are a straight line: a query comes from the user, the search engine fetches documents, produces a ranked list, reranks it, and presents the list.

The **agentic flow** does something else: the agent plans, works out the intent behind the query, searches, gathers results, analyzes, critiques, and only then presents a final result. Her summary: **the unit of work has moved from a lookup to an ongoing conversation with the world.**

Deep research agents are where this is most visible. Her example was a question about cholesterol medication: the agent works out the intent, uses various tools to gather websites, pricing information, drug interactions, and so on, **grounds the answer in retrieved evidence**, and presents it — saving hours of reading documents and blog posts. These runs now routinely stretch to around **20 turns**, making the whole thing multi-hop.

#### The gap: evaluation is still single-turn (~00:34–00:35)

"Here's the uncomfortable gap." When we evaluate agentic IR, we still **look only at the final answer** and score it with BLEU and ROUGE. But information seeking is now interactive and multi-turn, it has a temporal aspect, and it has to be evidence-driven. Grading the final answer alone simply doesn't work.

Her prescription: look at **the trace**. Assess the correctness of each hop, whether each hop was **adequate** to answer the user's question, and the cost — number of tokens, latency, and so on.

#### Where the field is heading (~00:36)

- **Reasoning-aware retrieval** — retrieval signals drawn from the agent's reasoning traces, not just keywords from the query.
- **Multi-turn, hop-aware benchmarks** such as **MTRAG**.
- **Graph RAG**, so retrieval can see relationships between entities.
- **Self-RAG**, to cut through some of the hallucinations.
- **Adaptive RAG**, routing queries based on their complexity and the effort they warrant.
- **Token count as a metric** — actually measuring and optimizing token usage as an information-retrieval metric in its own right.

Her closing point: our information seeking has changed and agents have changed how we get information, so **the way we assess whether these agents are doing the right thing and achieving the goal they set out for has to change too**.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| MTRAG | 多輪對話式 RAG 評估 benchmark | Multi-turn conversational benchmark for evaluating RAG systems | 字幕作 "MTRA";IBM Research 提出(arXiv 2501.03468),110 段對話、平均 7.7 turns、四個領域 |
| Graph RAG | 帶入實體關係的檢索增強生成 | Retrieval-augmented generation over entity relationships | |
| Self-RAG | 讓模型自我檢核以抑制幻覺的 RAG 變體 | RAG variant with self-reflection to reduce hallucination | |
| Adaptive RAG | 依 query 複雜度與所需成本路由的 RAG | RAG that routes queries by complexity and effort | |
| BLEU / ROUGE | 傳統文字生成評分指標,她認為不足以評估 agentic IR | Classic text-generation metrics she argues are insufficient for agentic IR | 字幕作 "blue and rouge" |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Tanya Rusta | Tanya Roosta |
| rack / classic rack | RAG / classic RAG |
| blue and rouge | BLEU and ROUGE |
| MTRA | MTRAG |
| self rack / adaptive rack / graph rack | self-RAG / adaptive RAG / graph RAG |
| the unit of work has "used" from lookup | has *moved* from lookup |

## 待確認 / To Verify

- 「MTRA」推定為 IBM 的 **MTRAG** benchmark,需以投影片確認。/ "MTRA" is read here as IBM's **MTRAG** benchmark — confirm against the slides.
- 她說 agentic IR「動輒 20 turns」,未說明資料來源。/ The "potentially 20 turns" figure was given without a source.
- 她提出的逐跳評估是否對應某個具體框架或論文,演講中未點名。/ Whether her per-hop evaluation proposal maps to a specific published framework was not stated.
