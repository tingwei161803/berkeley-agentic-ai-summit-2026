---
title: "Trustworthy Agentic AI in Regulated Domains: Robustness, Privacy, and Accountability as Co-Design Imperatives"
title_zh: "受監管領域的可信 Agentic AI:把穩健性、隱私與問責視為共同設計的必要條件"
speaker: "Lovedeep Gondara"
affiliation: "Head of AI R&D, Vanguard; Adjunct Professor, University of British Columbia"
type: talk
stage: Compass
date: 2026-08-02
session: "Session 1: AI Safety"
video: "https://www.youtube.com/watch?v=l8GS08n-25Q&t=1518s"
video_range: "00:25:18–00:34:46"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 2nd - Morning Session [DownSub.com].srt"
status: draft
tags: [trustworthy-ai, regulated-industries, privacy, accountability, autonomy-levels]
---

# 受監管領域的可信 Agentic AI:把穩健性、隱私與問責視為共同設計的必要條件(Trustworthy Agentic AI in Regulated Domains: Robustness, Privacy, and Accountability as Co-Design Imperatives)

**一句話總結**:可信度在 agentic 系統裡是**系統屬性、不是模型屬性**——因為穩健性、隱私、問責這三個我們都想要的性質彼此會直接衝突,所以真正該研究的不是怎麼把一切推到全自主,而是怎麼把 L2/L3 做得好用、安全且可證明合規。
**One-line summary**: In agentic systems trustworthiness is a **systems property, not a model property** — robustness, privacy, and accountability actively contradict one another — so the interesting research question isn't how to push everything to full autonomy, but how to make level 2 and level 3 useful, safe, and provably compliant.

## 中文筆記

### TL;DR

- **核心命題**:「一個模型幻覺出一個建議,是個困擾;一個 agent 照著它行動,是個責任(liability)。」從古典 ML 到 LLM,我們都還有中斷、偵測、修正的餘裕;到了自主 agent,那個餘裕沒了——後果從行事曆填錯一路到生產資料庫被刪。
- **Agent 特有的失效模式**(他列了六個,現場講了五個):compounding error(每步 95% 準確,10 步後掉到 60% 以下)、**indirect** prompt injection(工具呼叫的回傳結果本身帶惡意指令,而那是 agent 的輸入)、goal drift(拆解子任務後為子目標最佳化而偏離最終目標)、inter-agent manipulation 與 agent collusion、unauthorized tool invocation(為了彈性而設計的寬鬆 schema 讓稽核變難)。
- **三個想要的性質彼此衝突**:privacy vs auditability(要稽核就要詳細 log,詳細 log 就會曝露你想保護的資訊)、autonomy vs accountability(要問責就要有人介入點,有人介入就削減自主)、robustness vs autonomy(要穩健就得能中止漂移中的 agent,中止就是削減自主)。
- **結論**:不要問怎麼把所有東西推到 L4,要問**怎麼讓 L2/L3 對我們更有用**;金融、醫療這類受監管領域會暴露出其他領域看不到的失效模式,而可信度必須被當成系統屬性來設計。

### 重點整理

#### 三個世代的失敗:從「困擾」到「責任」(約 00:26–00:27)

他要全場記住的一句話,也是全場的核心論點:

> A model that hallucinates a recommendation is a nuisance. An agent that acts on it is a liability.

順著這條線看三個世代:

| 世代 | 輸出 | 會出什麼錯 | 有沒有補救餘裕 |
|------|------|-----------|---------------|
| 古典 ML | 機率 / 排序 / 標籤 | 標籤錯、機率誤差、排序錯 | **有**,可以中斷模型流程並介入 |
| LLM | 非結構化文字 | 幻覺、錯誤資訊 | **有**,可以偵測並修正 |
| 自主 Agent | 行動 | 「天花板就是極限」 | **沒有** |

最後一格他給的例子從輕到重排開:**行事曆多一筆錯誤條目 → 收件匣被清空 → 生產資料庫被刪除。**

#### Agent 特有的五種失效模式(約 00:27–00:30)

1. **Compounding error**:長程 agent 要走很多步才到目標。假設**每一步準確率 95%**,在若干前提下,**走完 10 步的準確率會掉到 60% 以下**。
2. **Indirect prompt injection**:他特別區分了這跟 LLM 的 prompt injection 不同——agent 在自主環境裡跑,**工具呼叫的結果本身可以夾帶惡意指令,而這些輸出正是 agent 的下一輪輸入**;同理,agent 檢索回來的任何內容也可能夾帶指令。
3. **Goal drift**:長程 agent 通常會把最終目標拆解成子任務;一旦它開始為那些子任務最佳化,就可能偏離最終目標。
4. **Inter-agent manipulation / agent collusion**:作為研究題目,多 agent 系統的這種動力學非常有趣;但**放到 production 就必須嚴肅看待**——依照 orchestration 的方式,一個惡意 agent 有可能說服其他 agent 替它辦事。
5. **Unauthorized tool invocation**:設計自主系統時,無論是 tool calling 還是 agent 間通訊,我們傾向把 schema 設計得有彈性;**而彈性的 schema 讓稽核更難做,也留下我們不想要的惡意行為空間**。

#### 三個想要的性質,以及它們彼此的衝突(約 00:30–00:32)

高階來看,一個可信的 agentic 系統要三件事:

- **Robustness**:agent 能撐過長程任務,壓住前面說的累積誤差。
- **Privacy**:agent 在環境裡經常碰到敏感私密資料,那些資料的隱私必須被保住。
- **Accountability**:必須能**稽核 agent 的行動**——「如果我們無法稽核導致某個結果的那條行動鏈,我們就已經失敗了。」

而這正是多 agent 系統與單一模型最不一樣的地方:**這些性質單獨看沒問題,放在一起就互相干涉。**

- **Privacy ↔ Auditability**:要稽核就得留詳細 log;但詳細的 log 本身就會曝露你原本想保護的那些資訊。
- **Autonomy ↔ Accountability**:自主的定義就是 agent 自己去做、我們不打斷;但那要怎麼指派責任?要有問責就需要 human in the loop、需要人可以介入的步驟——而那就削減了自主。
- **Robustness ↔ Autonomy**:要建穩健的系統,就得能中止一個正在漂移、或沒有照我們要的方式行動的 agent;中止本身就是在削減自主,但為了穩健你非做不可。

#### 自駕車式的自主分級,以及真正該問的問題(約 00:32–00:33)

他提到這張投影片跟 **Vincent 前一天講的那張很像**,而且跟很多人聊下來,大家對 agent 自主的想像確實都很接近自駕車的分級——這很自然,因為談自主時我們想的就是同一套 autonomy level。

- **Level 0**:AI 只給建議,由人決定要不要採納、要不要照做。
- **Level 4**(另一端):完全自主,我們只觀察輸出,其他什麼都不做。

而他的立場很清楚:

> 對我來說,更有趣的研究問題不是怎麼把一切變得更自主、怎麼把所有東西推向 L4,而是**怎麼讓 level 2 和 level 3 為我們工作得更好**——怎麼確保 L2/L3 系統是有用的、安全的、而且**可證明合規的(provably compliant)**,這樣我們才能把盡可能多的工作從自己手上卸下來,同時確保部署出去的東西是可信的。

#### 兩個帶走的結論(約 00:34)

1. **金融、醫療這類受監管領域會暴露出該領域獨有、且 agentic 系統獨有的失效模式。**
2. **Agentic AI 的可信度必須被當成「系統屬性」而不是「模型屬性」來思考**——因為這些性質經常彼此互動、彼此矛盾,設計系統時必須把這整組張力一起放進來考慮。

### 金句

> "A model that hallucinates a recommendation is a nuisance. An agent that acts on it is a liability."(約 00:26)

他要全場記住的一句,也是把 LLM 風險與 agent 風險分開的分界線。

> "If we cannot audit the chain of actions that led to a certain outcome, we have failed."(約 00:30)

受監管領域對 accountability 的底線標準。

> "The more interesting research question is how we make level two and level three work for us better."(約 00:33)

對「自主等級競賽」的一次降溫:價值在中間層,不在終點。

## English Notes

### TL;DR

- **The thesis**: "A model that hallucinates a recommendation is a nuisance. An agent that acts on it is a liability." Classical ML and LLMs both leave room to interrupt, detect, and correct. Autonomous agents remove that room — and the blast radius runs from a wrong calendar entry to a wiped inbox to a deleted production database.
- **Agent-specific failure modes** (six on the slide, five covered live): compounding error (95% per-step accuracy drops below 60% over 10 steps); **indirect** prompt injection, where tool-call results carry malicious instructions and those results are the agent's next input; goal drift, where optimizing decomposed subtasks pulls the agent away from the final goal; inter-agent manipulation and collusion; and unauthorized tool invocation, where the flexible schemas we design for capability make auditing harder.
- **The three properties we want actively conflict**: privacy vs auditability (the detailed logs auditing requires expose exactly what privacy protects); autonomy vs accountability (accountability requires human intervention points, which cut autonomy); robustness vs autonomy (robustness requires the ability to halt a drifting agent, which also cuts autonomy).
- **Conclusion**: stop asking how to push everything to L4; ask **how to make L2 and L3 work better for us**. Regulated domains surface failure modes other domains never see, and trustworthiness has to be designed as a systems property.

### Key Points

#### Three generations of failure: from nuisance to liability (~00:26–00:27)

The line he asked the room to remember is also the talk's spine:

> A model that hallucinates a recommendation is a nuisance. An agent that acts on it is a liability.

Tracing it across three generations:

| Generation | Output | What goes wrong | Room to recover? |
|-----------|--------|-----------------|------------------|
| Classical ML | probability / rank / label | wrong label, probability error, wrong ranking | **Yes** — you can interrupt the model flow and intervene |
| LLM | unstructured text | hallucination, wrong information | **Yes** — you can detect and correct |
| Autonomous agent | actions | "the sky is the limit" | **No** |

His escalation for that last row: **a wrong calendar entry → a wiped inbox → a deleted production database.**

#### Five agent-specific failure modes (~00:27–00:30)

1. **Compounding error.** A long-horizon agent takes many steps. At **95% per-step accuracy**, under some assumptions, **accuracy after 10 steps falls below 60%**.
2. **Indirect prompt injection.** He was careful to separate this from LLM prompt injection: an agent running autonomously receives **tool-call results that can themselves embed malicious instructions, and those outputs become the agent's inputs**. The same applies to any content the agent retrieves.
3. **Goal drift.** Long-horizon agents decompose a final goal into subtasks; once they start optimizing for the subtasks, they can end up misaligned with the goal that generated them.
4. **Inter-agent manipulation and agent collusion.** As a research area, the dynamics of multi-agent systems are genuinely interesting — but **in production this has to be taken seriously**, because depending on the orchestration, a malicious agent may convince other agents to do its bidding.
5. **Unauthorized tool invocation.** When designing autonomous systems we make schemas flexible, whether for tool calling or inter-agent communication. **Flexible schemas make auditing harder** and open room for behaviour nobody wants.

#### The three properties, and how they fight (~00:30–00:32)

A trustworthy agentic system needs three things at a high level:

- **Robustness** — the agent survives long-horizon tasks, containing the compounding error above.
- **Privacy** — agents in a live environment routinely touch sensitive private data, and that data's privacy has to hold.
- **Accountability** — you must be able to **audit the agent's actions**: "if we cannot audit the chain of actions that led to a certain outcome, we have failed."

This is what makes multi-agent systems different from standalone models: **properties that are fine in isolation interfere once composed.**

- **Privacy ↔ auditability.** Auditing a multi-agent system requires detailed logs; detailed logs expose the very information you are trying to protect.
- **Autonomy ↔ accountability.** Autonomy by definition means agents proceed without interruption — so who is accountable? Assigning accountability requires a human in the loop and points at which humans can intervene, and that reduces autonomy.
- **Robustness ↔ autonomy.** Building robust systems means being able to halt an agent that is drifting or not doing what you wanted. Halting reduces autonomy — but robustness requires it.

#### Autonomy levels, and the question actually worth asking (~00:32–00:33)

He noted the slide closely resembled **one Vincent had shown the previous day**, and that from conversations across the summit, everyone is converging on the self-driving-car framing for agent autonomy — naturally enough, since autonomy is the same concept.

- **Level 0**: AI only advises; humans decide whether to take or act on the advice.
- **Level 4** at the far end: fully autonomous, humans only observe the output.

His position:

> The more interesting research question isn't how we make everything more autonomous or move everything toward L4. It's **how we make level two and level three work for us better** — how we make sure L2 and L3 systems are useful, safe, and **provably compliant**, so we can take as much work off our plate as possible while still making sure what's deployed is trustworthy.

#### Two takeaways (~00:34)

1. **Regulated domains such as finance and healthcare expose failure modes that are unique both to those domains and to agentic systems.**
2. **Trustworthiness in agentic AI has to be treated as a systems property, not a standalone model property** — because these properties keep interacting and contradicting each other, and the design has to hold the whole tension set at once.

### Quotes

> "A model that hallucinates a recommendation is a nuisance. An agent that acts on it is a liability." (~00:26)

The line he asked the room to remember, and the boundary between LLM risk and agent risk.

> "If we cannot audit the chain of actions that led to a certain outcome, we have failed." (~00:30)

The accountability floor for regulated deployment.

> "The more interesting research question is how we make level two and level three work for us better." (~00:33)

A deliberate cooling of the autonomy-level race: the value is in the middle tiers, not the endpoint.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| 自主分級 L0–L4 / Autonomy levels L0–L4 | 借用自駕車分級來描述 agent 自主程度 | Self-driving-car style levels applied to agent autonomy | 講者提到與 Vincent 前一天的投影片高度相似 |
| Compounding error | 每步 95% 準確 × 10 步 → 低於 60% | 95% per-step accuracy over 10 steps drops below 60% | 講者現場的算術示例 |
| Indirect prompt injection | 工具回傳結果夾帶惡意指令,再成為 agent 輸入 | Malicious instructions embedded in tool-call results that become agent inputs | 與 LLM 層的 prompt injection 明確區分 |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Love Depot / Love Deep | Lovedeep (Gondara) |
| codeesign | co-design |
| aentic / aging AI | agentic AI |
| multi- aent | multi-agent |
| syphency | sycophancy |

## 待確認 / To Verify

- **第六個失效模式**:他說投影片上有六個,但「為了時間只講其中幾個」,實際只講了五個(compounding error、indirect prompt injection、goal drift、inter-agent manipulation & collusion、unauthorized tool invocation);第六個需看投影片。/ He said six failure modes were on the slide but covered only five; the sixth needs the slides.
- **"Vincent"**:指前一天演講的 Vincent(依議程最可能是 Vincent Vanhoucke),但講者只稱名不稱姓,無法從逐字稿確認。/ He referred only to "Vincent" from the previous day; most likely Vincent Vanhoucke, but not confirmable from the transcript.
- **compounding error 的假設條件**:他說「in that case of course I'm assuming a few things here」但未列出假設。/ He flagged that the 95%→60% arithmetic rests on assumptions he did not enumerate.
