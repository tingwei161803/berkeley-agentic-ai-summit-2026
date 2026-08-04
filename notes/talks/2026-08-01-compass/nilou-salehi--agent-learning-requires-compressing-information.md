---
title: "Agent Learning Requires Compressing Information into an Executable Reasoning Structure"
title_zh: "Agent 的學習,是把資訊壓縮成一個可執行的推理結構"
speaker: "Nilou Salehi"
affiliation: "Associate Professor, UC Berkeley"
type: talk
stage: Compass
date: 2026-08-01
session: "Session 2: Frameworks & Dev Platforms"
video: "https://www.youtube.com/watch?v=AO0RXP-fVZQ&t=2635s"
video_range: "00:43:55–00:49:32"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [reasoning-graphs, enterprise-agents, long-horizon, memory, architecture]
---

# Agent 的學習,是把資訊壓縮成一個可執行的推理結構(Agent Learning Requires Compressing Information into an Executable Reasoning Structure)

**一句話總結**:模型在做的、harness 在做的,本質是同一件事——**把大量資訊壓縮成可執行的形式**;而對那些必須高度一致、可解釋、長期跑的企業流程,最適合的可執行形式是一張由 agent 自己搭建的 **reasoning graph**。
**One-line summary**: A model and a harness are doing the same thing — **compressing large amounts of information into something executable**. For enterprise processes that must run repeatedly with high consistency and explainability, the right executable form is a **reasoning graph that an agent builds for itself**.

## 中文筆記

### TL;DR

- **統一視角**:我們這些年在解的問題其實只有一個——**壓縮資訊**。模型在做的是這件事,harness 在做的也是這件事:把大量資訊壓成一個**可執行**的格式(transformer 是可執行的,它預測下一個 token)。
- **接下來的關鍵題**:會出現愈來愈多做這件事的架構,所以第一個要解的問題是——**流程有哪些類型,每一類的最佳架構 / harness 是什麼**。
- **Reasoning graph**:一張由 agent 組成的圖。最底層負責連接原始資料所在的各種系統並理解資料,中間層負責推理,最上層負責在對的時間採取對的行動;**從底到頂的任一條路徑就是一條可能的推理路徑**。適用於「需要反覆執行且要求極高一致性」的流程。
- **由 agent 來建圖**:這張圖不該由人手寫,而是由一個 **architect agent** 建出來,形成「agent 與 harness 之間的 handshake」——而且**每建一次就變得更會建**(compounding intelligence 進到模型權重裡)。
- **戰績(invoice matching)**:baseline agent harness 即使用 Fable 也只做對約 40%;他們的 reasoning graph 做到 **99.9% 準確率**,**96% 的案例還能正確解釋決策理由**;某 Fortune 500 客戶單張發票處理成本從 **5 美元 → 1.5 美元 → 本週的 10 美分**。

### 重點整理

#### 一切都是壓縮(約 00:44)

Salehi 的開場命題很簡潔:**我們多年來在解的那個問題,就是壓縮資訊**。因為說到底,模型做的就是這件事,harness 做的也是這件事——我們只是不斷找出新方法,把大量資訊壓縮成**一個可執行的格式**。transformer 模型就是可執行的,它執行的方式是預測下一個 token。

接下來幾年會出現愈來愈多、以更複雜方式做這件事的架構。所以**首先要解的問題是:流程有哪些種類,而每一種流程的最佳架構或 harness 是什麼?**

#### Reasoning graph:一張由 agent 構成的圖(約 00:44–00:46)

她分享團隊做得很成功的一種:**reasoning graph**——圖上的每一個圓圈都是一個 agent。他們發現對於**需要反覆執行、且要求極高一致性**的流程,這是非常好的架構。

分層結構是:

- **最底層**:一層 agent 只做一件事——連接到原始資料所在的各個系統,並理解那些原始資料。
- **中間層**:負責推理的 agent。
- **最上層**:在對的時間採取對的行動的 agent。

**任何一條從底層走到頂層的路徑,就是一條可能的推理路徑。**她也指出當天其他場次出現過同一個想法的不同變體——這些路徑可以平行跑,也可以用各種方式最佳化。

那麼,這張圖怎麼生出來?**必須由 agent 來做。**她預期未來會愈來愈常看到「**agent 與 harness 之間的 handshake**」:那個 agent 被訓練成非常懂得怎麼和特定 harness 協作;而不同架構會擅長不同類型的流程。

他們投入最多的是一個 **architect agent**,負責處理那些必須高度一致且可解釋的流程——財務流程、供應鏈,或任何公司需要一遍又一遍跑下去的東西:**非確定性、仍需要智能,但必須高度一致並且說得出理由**。

成果:一致性非常高——**在某些例子或 benchmark 上,連 Fable 都只能做到約 40–70% 準確率,他們可以穩定超過 95%**;速度也很快。而且**整個 harness 的生成過程沒有寫任何 custom code**,全部是 architect agent 與這個 harness 協作的產物,所以**新的 use case 幾週就能上線**。

她認為這個架構最重要的部分是 **compounding intelligence,而且它累積在模型的權重裡**:architect 每接一個新 use case、為它建一張 reasoning graph 並學會怎麼建,它就更會建。

#### 案例:invoice matching(約 00:47–00:49)

她挑了一個具體流程說明:**發票比對**。

超大型企業每個月要處理數百萬張發票,而決策看似很簡單——**付,或不付**。難點在兩邊都不能鬆:他們會收到一定比例的詐欺發票,所以不能全付;但也不能拖太久,因為沒有按時付款會影響整條供應鏈。

流程本身是:收到發票 → 比對到採購單(PO)→ 正規化 → 處理大量例外。例外多到令人頭痛:單位不同、幣別不同、某些地區有稅。她說有一個例子她印象特別深刻也覺得特別好笑——**如果貨品是液體,發票金額比採購單少最多 5% 是可以接受的,但只限夏季,因為會蒸發掉一些,你也拿它沒辦法**。

所以 agent **必須持續學習**:這不是一次性的 one-shot learning,也不是在單一 session 裡發生的事,而是一個**橫跨數週數月的長程流程**;每遇到一個例外,就得從中學到東西。

數字:

- 一個 baseline agent harness,**即使用 Fable,也只做對約 40%**。
- 他們的 **architect agent 為這個流程建出的 reasoning graph**——包含大量 agent、它們的接線、各自的 instruction、每個 agent 該用哪個模型、每個 agent 自己的長期記憶——**這些工程決策全部由 agent 做**。
- 結果在真實資料上達到 **99.9% 準確率**,**第一版圖一週內就上線**,而且 **96% 的案例不只給出正確決策,還能正確解釋這個決策為什麼成立**。
- 成本:某 Fortune 500 客戶單張發票的處理成本從 **5 美元降到 1.5 美元**,而**就在本週再降到 10 美分**。

**結語**:能把學到的東西壓縮成一個**可重複使用的結構**,就能做到這種級別的進展。

### 金句

> "The whole problem that we're all solving and have been solving for years now is compressing information."(約 00:44)

整場演講的第一句,也是它的全部論點。

> "If it's liquid, it's okay if the amount on the invoice is up to 5% less than what was on the purchase order — but only during summers, because some of it evaporates and there's nothing you can do."(約 00:47)

一個很好笑但很真實的例子,說明為什麼企業流程沒辦法一次學完:規則本身就是這樣長出來的。

## English Notes

### TL;DR

- **One framing**: the problem we've all been solving for years is **compressing information**. That's what a model does, and it's what a harness does — finding ways to take a great deal of information and compress it into an **executable** format (a transformer is executable; it predicts the next token).
- **The next question**: more architectures will do this in more complicated ways, so the first thing to figure out is **what the types of processes are, and what the optimal architecture or harness is for each**.
- **Reasoning graphs**: a graph of agents. A bottom layer connects to the systems where raw data lives and does nothing but understand that data; a middle layer reasons; a top layer takes the right action at the right time. **Any path from bottom to top is one possible reasoning path.** It fits processes that must run repeatedly with very high consistency.
- **An agent builds the graph**: not a human. An **architect agent** produces it, forming a "handshake between an agent and a harness" — and it **gets better at building them every time**, with the compounding intelligence living in the model's weights.
- **Invoice matching results**: a baseline agent harness, even using Fable, gets ~40% right. Their reasoning graph reached **99.9% accuracy**, correctly **explained** the decision in 96% of cases, and took one Fortune 500 client from **$5 per invoice to $1.50, and this week to 10 cents**.

### Key Points

#### It's all compression (~00:44)

Salehi opened with a single claim: **the problem we've all been solving for years is compressing information**. At the end of the day that's what a model does and what a harness does — we keep finding different ways to take lots and lots of information and compress it into a format that is executable. A transformer model is executable, and the way it executes is by predicting the next token.

Over the next few years there will be more and more architectures doing this in more complicated ways. So the first problem to solve is: **what are the various types of processes, and what is the optimal architecture or harness for each?**

#### Reasoning graphs: a graph of agents (~00:44–00:46)

The one her team has had a lot of success with is the **reasoning graph** — every circle in the graph is an agent. They've found this is a very good architecture for processes that need to be run repeatedly and with very high consistency.

The layering:

- **Bottom**: agents that connect to all the different systems where the raw data lives, whose only job is to understand that raw data.
- **Middle**: agents that do the reasoning.
- **Top**: agents that take the right action at the right time.

**Any path from bottom to top is one possible reasoning path.** She noted that variations on the same idea had shown up in other talks that day — the paths can be run in parallel and optimized in various ways.

So how do you create one? **It has to be done by an agent.** What we'll see more and more, she argued, are **handshakes between an agent and a harness**, where the agent is trained to know that harness very well — and different architectures will suit different kinds of processes.

The one her team has invested most in is an **architect agent** aimed at processes that must run consistently and accurately: financial processes, supply chain, anything a company needs to keep running over and over. **Non-deterministic, still requiring intelligence, but demanding high consistency and explainability.**

The payoff is consistency: they routinely clear **95% accuracy on examples and benchmarks where even Fable only reaches about 40–70%**, and it's fast. **No custom code is written anywhere in generating the harness** — it's all the architect agent working with the harness — so new use cases launch in a matter of weeks.

The most important property, she said, is **compounding intelligence held in the model's weights**: each time the architect takes a new use case, builds a reasoning graph for it, and learns how, it gets better at doing that.

#### Case study: invoice matching (~00:47–00:49)

Very large companies receive enormous volumes of invoices and face a deceptively simple decision: **pay it or don't**. They can't pay everything, because a certain amount of it is fraud; they also can't sit on invoices too long, because late payment ripples through the supply chain. At scale that's millions of invoices a month.

The process: receive the invoice, match it to a PO, normalize it, and handle a long tail of exceptions — different units, different currencies, tax in certain jurisdictions. Her favorite: **if the goods are liquid, the invoice may come in up to 5% under the purchase order — but only during summer, because some of it evaporates and there's nothing anyone can do about it.**

Which is exactly why the agent has to **keep learning**. It isn't one-shot, and it doesn't happen inside a single session: it's a long-horizon process spanning weeks and months, and every exception is something to learn from.

The numbers:

- A baseline agent harness, **even using Fable, gets about 40% of it right**.
- Their **architect agent built the reasoning graph** for this process — the agents, their wiring, their instructions, which model each agent should use, and a long-term memory per agent. **All of those engineering decisions were made by the agent.**
- The graph hit **99.9% accuracy** on real data, the first version was up and running **within a week**, and in **96% of cases it not only made the right decision but correctly explained why**.
- Cost at one Fortune 500 client fell from **$5 per invoice to $1.50**, and **this week to 10 cents**.

Her closing line: those are the kinds of advances available once you can take that learning and compress it into a reusable structure.

### Quotes

> "The whole problem that we're all solving and have been solving for years now is compressing information." (~00:44)

The first sentence of the talk, and its entire argument.

> "If it's liquid, it's okay if the amount on the invoice is up to 5% less than what was on the purchase order — but only during summers, because some of it evaporates and there's nothing you can do." (~00:47)

A funny but very real illustration of why enterprise processes can't be learned in one pass.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Across AI | 講者自述其共同創辦的公司,主打企業級 reasoning graph 架構 | The company she co-founded, built around enterprise reasoning-graph architecture | 字幕作 "Across AI";公開資料顯示為 UC Berkeley I School 與 USC 教授共同創辦 |
| Reasoning graph | 分層的 agent 圖:資料理解層 → 推理層 → 行動層;任一底到頂路徑為一條推理路徑 | Layered graph of agents — data understanding, reasoning, action — where any bottom-to-top path is a reasoning path | 由 architect agent 自動生成 / generated by the architect agent |
| Architect agent | 為特定流程自動建構 reasoning graph(含接線、instruction、選模型、長期記憶)的 agent | Agent that builds the reasoning graph for a process: wiring, instructions, model choice per agent, long-term memory | 每建一次就更會建 / improves with each use case |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| professor Neu / My name is Nio | Nilou Salehi |
| Across AI(字幕正確)| — |
| transforming model | transformer model |
| oneshot | one-shot |

## 待確認 / To Verify

- **職稱衝突**:她在台上自述為 Across AI 的 **co-founder and CEO**;而 2024–2025 年的公開資料顯示 Across AI 由 UC Berkeley 的 Niloufar Salehi(co-founder / CPO)、USC 的 Afshin Nikzad(CTO)與 Steven Mih(CEO)共同創辦。角色可能已變動,需查證。frontmatter 依官網議程列 UC Berkeley 職稱。/ **Title conflict**: on stage she introduced herself as **co-founder and CEO** of Across AI, while public 2024–2025 material lists her as co-founder/CPO with Steven Mih as CEO. Roles may have changed; the frontmatter follows the official agenda.
- 議程姓名為 "Nilou Salehi",公開學術資料多作 **Niloufar Salehi**。/ The agenda uses "Nilou Salehi"; academic sources generally use **Niloufar Salehi**.
- 「even Fable can only hit about 40 to 70%」所指的 benchmark 未在台上點名。/ The benchmark behind the "even Fable only hits 40–70%" claim was not named.
- 99.9% 準確率與 96% 可解釋率的評估設定(資料量、切分方式)未說明。/ The evaluation setup behind the 99.9% accuracy and 96% explanation figures was not described.
