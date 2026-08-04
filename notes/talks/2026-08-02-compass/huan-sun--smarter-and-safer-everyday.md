---
title: "Smarter and Safer Everyday? Continual Learning and Safety in Computer-Use Agents"
title_zh: "每天更聰明也更安全?Computer-Use Agent 的持續學習與安全"
speaker: "Huan Sun"
affiliation: "Associate Professor, The Ohio State University"
type: talk
stage: Compass
date: 2026-08-02
session: "Session 1: AI Safety"
video: "https://www.youtube.com/watch?v=l8GS08n-25Q&t=3014s"
video_range: "00:50:14–00:56:20"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 2nd - Morning Session [DownSub.com].srt"
status: draft
tags: [computer-use-agents, continual-learning, safety, evaluation, open-weight-models]
---

# 每天更聰明也更安全?Computer-Use Agent 的持續學習與安全(Smarter and Safer Everyday? Continual Learning and Safety in Computer-Use Agents)

**一句話總結**:分佈偏移既是 agent 最需要在部署後持續學習的地方,也正是安全失效最容易發生、最容易被漏看的地方——所以「持續學習」與「安全」之間存在一個尚未被探索的危險張力,而錯誤的正回饋會把不安全行為一輪一輪地強化回模型裡。
**One-line summary**: Distribution shift is both where an agent most needs to keep learning after deployment and where safety failures most easily emerge and get missed — an unexplored, dangerous tension, because a reward signal that only tracks task success will reinforce unsafe behaviour update after update.

## 中文筆記

> 她開場提到自己「似乎是這個 session 裡唯一來自學術界的人」,並說希望能說服大家:大學做的事對產業前沿仍然高度相關。

### TL;DR

- **Safe continual learning 的定義**:我們要問的是——**如何在部署後持續改進 agent,而不同時持續累積新的安全風險?**
- **這個悖論的機制**:agent 完成了任務但漏掉了安全約束,而評估者(無論是人還是 agentic 系統)只看任務是否成功、或不夠穩健而抓不到那個安全失效,於是**agent 仍然拿到正回饋 → 下一次更新強化了這個不安全行為 → 造成重複發生、甚至更激進的安全失效**。
- **關鍵發現**:文獻中有大量研究用**對抗攻擊或惡意 prompt** 去攻破 agent,但她的團隊發現——**完全不需要對抗攻擊。在良性輸入與一般環境下,嚴重的傷害就會出現。**
- **兩個方向的工作**:(1) 在部署前、大規模地**提早浮現長尾失效模式**;(2) 建立**開源基礎設施**,用較小的 open-weight 模型嚴謹研究 safe continual learning——因為社群目前在環境建置、任務合成、軌跡評估這幾塊有巨大缺口。

### 重點整理

#### 悖論:最需要學習的地方,正是最容易失效的地方(約 00:51–00:53)

她把整場的核心定義為 **safe continual learning**:

> 我們如何在部署之後持續改進 agent,而**不持續累積新的安全風險**?

悖論在於**分佈偏移**同時扮演兩個角色:

- 從訓練到部署的分佈偏移,**正是 agent 部署後需要持續學習的地方**。
- 但那**也正是安全失效會浮現、而且容易被漏掉的處境**。

具體的惡化迴路她講得很清楚:想像在持續學習的過程中,agent **完成了任務,但在過程中漏掉了某些安全約束**。這時 agent 仍然可能拿到正向回饋——因為評估者(無論是人類還是 agentic 系統本身)**可能純粹只看任務是否成功,或者不夠穩健、抓不到那個安全失效**。於是:

> 下一次對 agent 的更新,就可能**強化那個不安全行為**,最終導致重複的安全失效,甚至更激進的安全失效。

#### 不需要攻擊,良性輸入就足以造成嚴重傷害(約 00:53–00:55)

文獻中已有大量研究製造**對抗攻擊或惡意 prompt** 來攻破 agent。她團隊的工作指向另一個方向:

> 即使**沒有**對抗攻擊,只是在良性輸入與一般環境下,嚴重的傷害就可能出現。

她把這件事與**近期 OpenAI / Hugging Face 的事件**連結起來,並給出示範:

- 同一件事有很多種問法。**一種問法下 agent 行為正常;另一種只是原始任務指令的輕微擾動——而且依然是良性的——agent 就展現出有害行為。**
- 具體例子:**使用者想要為某一個帳號取得 SSH 存取權,結果 agent 做出了超出該範圍的不安全變更。**
- 更一般的模式:**指令中出現一些語意模糊的措辭 → agent 做出不安全的推論 → 推論導致有害行動。**

所以核心問題是:**如何在這些長尾失效模式變成部署事故之前,主動地、大規模地把它們浮現出來?**

#### 開源基礎設施:讓 open-weight 模型能被嚴謹地研究(約 00:55–00:56)

第二條線是工程與社群基礎建設。她指出社群目前**有一個巨大的缺口**:要讓 open-weight 模型在新環境中持續學習,你需要**環境建置(environment setup)、任務合成(task synthesis)、軌跡評估(trajectory evaluation)** 一整套東西,而這些目前都缺乏支援。

她的團隊已經**釋出了一個框架**來支撐 safe continual learning 的研究,**特別是針對 computer-use agents**,並刻意選擇**較小的 open-weight 模型**,讓這類研究可以被嚴謹地重現。

收尾的 takeaway 很簡單:

> 我們要讓 agent **同時持續改進能力與安全**。這是我們團隊的使命。

### 金句

> "Even without adversarial attacks — just under benign inputs and ordinary environments — severe harms could emerge."(約 00:53)

把 agent 安全的討論從「攻擊者模型」拉回「日常使用」。

> "The next update to the agent may reinforce that unsafe behavior."(約 00:52)

持續學習不是中性的:評估抓不到的失效,會被學習迴路本身放大。

## English Notes

> She opened by noting she seemed to be the only academic on the session, and said she hoped to convince the room that university work remains highly relevant to the industry frontier.

### TL;DR

- **Safe continual learning, defined**: how can we keep improving agents after deployment **without continually accumulating new safety risks**?
- **The mechanism of the paradox**: an agent completes a task but misses a safety constraint; the evaluator — human or agentic — focuses on task success or simply isn't robust enough to catch it; **so the agent still receives positive feedback, the next update reinforces the unsafe behaviour, and failures become repetitive or more aggressive.**
- **The key finding**: a large literature attacks agents with adversarial prompts, but her group's work shows **you don't need an attack at all — under benign inputs in ordinary environments, severe harms emerge.**
- **Two lines of work**: (1) proactively **surfacing long-tail failure modes at scale, before deployment**; (2) **open-source infrastructure** for rigorously studying safe continual learning with smaller open-weight models, filling a real gap in environment setup, task synthesis, and trajectory evaluation.

### Key Points

#### The paradox: where learning is needed is where failure hides (~00:51–00:53)

She framed the whole talk around **safe continual learning**:

> How can we continually improve agents after deployment **without continually accumulating new safety risks**?

The paradox is that **distribution shift plays both roles at once**:

- The shift from training to deployment is **exactly where agents need to learn continually after deployment**.
- It is **also the situation where safety failures emerge and are easy to miss.**

The degradation loop is worth stating precisely. During continual learning, an agent **completes a task but misses some safety constraints along the way**. It can still receive positive feedback, because the evaluator — human or the agentic system itself — **may focus purely on task success, or simply isn't robust enough to catch the safety failure**. Then:

> The next update to the agent may **reinforce that unsafe behaviour**, and eventually cause repetitive safety failures, or even more aggressive ones.

#### No attack required: benign inputs, severe harms (~00:53–00:55)

Numerous studies in the literature construct **adversarial attacks or malicious prompts** to break an agent. Her group's work points somewhere else:

> Even **without** adversarial attacks — just under benign inputs and ordinary environments — severe harms could emerge.

She tied this to the **recent OpenAI / Hugging Face incident**, then walked through demonstrations:

- There are many ways to ask an agent to do the same thing. **Under one phrasing it behaves normally; under a slight — and still benign — perturbation of the same task instruction, it exhibits harmful behaviour.**
- The concrete case: **the user wants SSH access for one account, and the agent makes unsafe changes well beyond that.**
- The general pattern: **ambiguous phrasing in the instruction → the agent makes an unsafe inference → the inference produces harmful actions.**

Hence the core question: **how do we proactively surface these long-tail failure modes, at scale, before they become deployment incidents?**

#### Open-source infrastructure so open-weight models can be studied properly (~00:55–00:56)

The second line is community infrastructure. She identified **a huge gap right now**: letting open-weight models learn continually in a new environment requires **environment setup, task synthesis, and trajectory evaluation** — and none of it is well supported today.

Her group has **released a framework** to support the study of safe continual learning, **specifically for computer-use agents**, deliberately built around **smaller open-weight models** so the research can be done rigorously and reproducibly.

The closing takeaway was deliberately simple:

> We want agents to **continually improve both capability and safety**. Our group is driven by this mission.

### Quotes

> "Even without adversarial attacks — just under benign inputs and ordinary environments — severe harms could emerge." (~00:53)

Moves the agent-safety conversation off the attacker model and back onto ordinary use.

> "The next update to the agent may reinforce that unsafe behavior." (~00:52)

Continual learning isn't neutral: whatever the evaluator misses, the learning loop amplifies.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Safe continual learning | 講者定義的核心問題:部署後持續改進 agent 而不累積新安全風險 | Her framing: keep improving agents post-deployment without accumulating new safety risk | 演講的主軸概念 |
| 良性輸入下的長尾失效研究 / benign-input failure study | 顯示無需對抗攻擊、僅在良性輸入下即可誘發嚴重傷害 | Shows severe harms arise from benign inputs without any adversarial attack | 疑似對應其團隊論文 "When Benign Inputs Lead to Severe Harms"(待確認,見下)|
| 安全持續學習開源框架 / open-source CL framework | 支援 open-weight 模型在新環境中持續學習的環境建置、任務合成、軌跡評估 | Environment setup, task synthesis, and trajectory evaluation for open-weight continual learning | 講者說已釋出,但台上未念出名稱(待確認)|
| OpenAI / Hugging Face 事件 | 講者用以類比 agent 在良性情境下逸出預期範圍 | Cited as an analogue of agents exceeding intended scope in ordinary settings | 同日 Dawn Song keynote 亦提及此事件 |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| House Sun / Hansson | Huan Sun |
| continue learning | continual learning |
| hugging phase | Hugging Face |
| longtail | long-tail |
| openweight | open-weight |

## 待確認 / To Verify

- **兩個專案的正式名稱**:講者在台上**沒有念出任何論文或框架的名稱**。依其研究群(OSU NLP Group)近期產出,最可能對應的是 "When Benign Inputs Lead to Severe Harms: Eliciting Unsafe Unintended Behaviors of Computer-Use Agents" 與 "Autonomous Continual Learning of Computer-Use Agents for Environment Adaptation",但**無法從逐字稿確認**,需核對投影片。/ She named neither paper nor framework on stage; the two titles above are the most plausible matches from her group's recent output but are **not** confirmed by the transcript.
- **框架的釋出位置**:她說「we have released this framework」,但未給 repo 連結或名稱。/ No repository name or link was given.
- **她提到的第二個示範案例**:逐字稿只留下「this is another example … with some ambiguous phrases」,細節未入字幕。/ The second demo's details did not survive the auto-captions.
