---
title: "LabOS: The AI-XR Co-Scientist That Sees and Works With Humans"
title_zh: "LabOS:看得見人、也與人協作的 AI-XR 共同科學家"
speaker: "Mengdi Wang"
affiliation: "Professor, Princeton"
type: talk
stage: Nexus
date: 2026-08-01
session: "Session 1: AI for Science"
video: "https://www.youtube.com/watch?v=LB7IkZhEYic&t=3791s"
video_range: "01:03:11–01:11:25"
transcript: "tmp/[English (auto-generated)] Nexus Stage - August 1st - Morning Session [DownSub.com].srt"
status: draft
tags: [ai-for-science, verification, reproducibility, robotics, xr]
---

# LabOS:看得見人、也與人協作的 AI-XR 共同科學家(LabOS: The AI-XR Co-Scientist That Sees and Works With Humans)

**一句話總結**:AI 擴張的真正瓶頸不是假設,是驗證——實體實驗沒有 checkpoint、沒有 log、無法回溯,所以 Mengdi Wang 的解法是讓 AI 戴上智慧眼鏡進實驗室,把每一個實體動作變成可觀測、可除錯的環境。
**One-line summary**: The real bottleneck on scaling AI isn't hypotheses, it's verification — physical experiments have no checkpoints, no logs, and no way to backtrack — so Wang's answer is to put AI behind smart glasses in the lab and turn every physical action into an observable, debuggable environment.

## 中文筆記

> 註:本場因時間超時被主持人中斷,最後一頁投影片是倉促帶過的。

### TL;DR

- **瓶頸在驗證,不在假設**。這也是為什麼這麼多 AI 公司在拼命建 trace data 與 RL environment——AI 要更快擴張,得先有辦法擴張「環境」與「驗證」。但這件事在科學裡難得要命。
- **可重現性危機的數字很難看**:Nature 的調查顯示 **70% 的生醫論文無法被他人重現,50% 連原作者自己都重現不出來**,而且橫跨化學、生物、物理、地球環境各領域。原因很簡單:實體實驗**沒有 checkpoint**(訓練模型有,agent workflow 也有,在無塵室裡沒有)、**沒有 log 可以 debug**、也沒辦法回頭改 harness。
- **AI 讓科學變慢而不是變快**:她引用同事的部落格——最近一次 NeurIPS 有 4 萬份投稿,論文與 agent 都爆量,但**驗證沒有同步加速**,結果是訊噪比更差,在滿坑滿谷 AI 生成內容裡更難撈到有用資訊。
- **LabOS 的賭注**:把多模態推理 AI 藏在智慧眼鏡後面,讓實驗室裡的**每個動作、每次狀態改變都被 AI 觀測到**,即時抓錯、把實體流程數位化、故障排除、給提示。搭配機器人做的端到端奈米製造迷你實驗室,把物理博士生原本要三個月的工作壓到一週,並開放成 API 讓任何人送 job 進去重現實驗。

### 重點整理

#### 驗證,而不是假設,才是 AI 擴張的瓶頸(約 01:03–01:07)

前幾位講者已經談了 AI agent 在數位空間的大量進展。她把科學研究拆成幾個階段:**hypothesize**(讓模型思考、推理、往深處挖)、**computation**(用代理模型模擬、找出最佳候選)、以及最後的 **validation / verification**。

她的主張很直接:**驗證已經成為擴張任何 AI 模型的主要瓶頸**。這正是為什麼現在這麼多 AI 公司與新創在積極打造新的 trace data 與新的 RL environment。**如果有辦法擴張環境與驗證,AI 就能跑得快得多**——但在科學裡,這件事難得要命。

她現場丟了一個問題:隨便挑一篇 Nature 上的化學或生物論文,可重現的比例是多少?台下猜 5%、30%。答案來自 Nature 自己做的調查:**70% 的生醫論文無法被其他人重現,50% 甚至連原作者自己都重現不出來**,而且這在化學、生物、物理、地球環境等領域都成立。

原因不在人不努力,而在**驗證本身的結構**。當有人在實驗檯或無塵室裡跑一個實驗:

- **沒有 checkpoint**。訓練模型有 checkpoint,agent workflow 可以回溯,實體實驗兩者都沒有。
- **沒有 log**,無從 debug,也無從改進 harness。

她的同事幾個月前寫了一篇部落格,結論是:**有了 AI,科學沒有變快,反而變慢了**。理由是最近一次 NeurIPS 收到 4 萬份投稿——論文太多了;而真正提供新知識與新資訊的是驗證,驗證卻沒有被加速。於是**論文更多、agent 更多,訊噪比反而更糟**,在大量 AI 生成內容裡撈出有用資訊變得更難。

回到驗證問題:我們可以有各種很炫的模型,告訴我們幾百萬個新穎假設,**但瓶頸永遠會在實驗室裡**。而做實驗的科學家同事把整個職涯、好幾年時間投在實體實驗室裡,即使拚盡全力,這整條 workflow 仍然非常容易出錯。

所以真正的大哉問是:**我們要怎麼把每一間科學實驗室都變成一個可驗證的環境(verifiable environment)?**

一邊是 AI 跑得飛快——每家前沿實驗室與新創都有 AI co-scientist;另一邊是科學家在實驗檯與無塵室裡,要花好幾個月甚至好幾年才能驗證一個假設。中間缺了關鍵的一塊。

#### LabOS:把實體實驗室變成可觀測環境(約 01:07–01:11)

**LabOS 是一個 AI-XR agent**:一個藏在智慧眼鏡後面的多模態推理 AI。她放的第一個例子是一位從印度來訪的大學部實習生,在 LabOS 協助下**幾乎第一天就能執行進階的基因體工程實驗**。

系統提供的東西是:讓科學實驗室裡**每一個動作、每一次狀態改變都變成 AI 可觀測的**,同時建立多層串流系統,讓 AI 能**即時協助人類研究者**——抓錯、把實體流程數位化、故障排除、在事情不對勁時給出指引與提示。

第二個例子(她強調「這不是動畫」)是與 **Princeton Quantum Institute** 同事合作的**端到端迷你機器人實驗室**,用來自動化**單原子層 graphene 元件的奈米製造**。多模態 agent 在電腦裡跑 auto research,而實際的量測、製造、tape-out 與所有顯微影像都由機器人完成。成果是:**原本物理博士生要花三個月的工作,現在一週完成**。她的同事正把這套系統開放成 **API**,任何人都可以送 job 進去重現實驗、測試新假設——目標是規模化。

(被主持人以時間為由中斷後的最後一頁)他們正在 pilot 的 LabOS 是一套讓**人類研究者與機器人並肩工作**的系統:每一條實體 workflow 都會被數位化,每一條 trace 都被收集並交由 AI 推理;而且這套系統設計成能**跨科學領域通用**——從生物實驗室、化學實驗室,到無塵室與奈米設施。

### 金句

> "70% of biomedical research papers are not reproducible by others, and 50% are not even reproducible by the same authors."(約 01:05:21)

這不是態度問題,是驗證沒有基礎建設的必然結果。

> "With AI, science is not faster. Science is actually getting slower."(約 01:06:28)

假設端加速、驗證端沒動,結果是訊噪比崩壞。

> "How do we turn every scientific lab into a verifiable environment?"(約 01:07)

整場演講的問題陳述。

## English Notes

> Note: the talk was cut short by the host for time; the final slide was rushed.

### TL;DR

- **The bottleneck is verification, not hypothesis generation.** That's why so many AI companies are racing to build trace data and RL environments — AI scales much faster if you can scale environments and verification. In science, that is brutally hard.
- **The reproducibility numbers are ugly**: a Nature survey found **70% of biomedical papers aren't reproducible by others and 50% aren't reproducible by their own authors**, and it holds across chemistry, biology, physics, and earth/environmental science. The reason is structural: physical experiments have **no checkpoints** (model training has them, agent workflows have them, a clean room doesn't), **no logs to debug**, and no way to go back and improve the harness.
- **AI is making science slower, not faster**: she cites a colleague's blog — 40,000 submissions at the most recent NeurIPS, an explosion of papers and agents, but **verification hasn't sped up**, so the signal-to-noise ratio degrades and useful information gets harder to find amid AI-generated content.
- **LabOS's bet**: put a multimodal reasoning AI behind smart glasses so that **every action and state change in a lab becomes observable to AI** — catching errors in real time, digitalizing physical workflows, troubleshooting, offering hints. Paired with an end-to-end robotic nanofabrication lab that compressed three months of PhD-student work into one week and is being released as an API.

### Key Points

#### Verification, not hypothesis, is what limits AI (~01:03–01:07)

Earlier speakers covered the advances in AI agents in the digital space. Wang breaks scientific research into stages: **hypothesize** (getting models to think, reason, dig deep), **computation** (simulation and surrogate models to find the best candidates), and finally **validation / verification**.

Her claim is blunt: **verification has become the major bottleneck for scaling any AI model.** That's precisely why so many AI companies and startups are actively building new trace data and new RL environments. **AI would scale much faster if there were a way to scale environments and verification** — and in science this is extraordinarily hard.

She put a question to the room: pick a random chemistry or biology paper in *Nature* — what fraction is reproducible? The audience guessed 5%, then 30%. The answer, from a survey run by researchers and *Nature*: **70% of biomedical research papers are not reproducible by others, and 50% are not even reproducible by the same authors** — and this holds across chemistry, biology, physics, and earth and environmental science.

The cause isn't effort, it's the **structure of verification**. When someone runs an experiment at a bench or in a clean room:

- There are **no checkpoints**. Model training has them; agent workflows can backtrack; physical experimentation has neither.
- There are **no logs** to inspect, nothing to debug, no way to improve the harness.

A colleague wrote a blog a few months earlier concluding that **with AI, science is not faster — science is getting slower**. The most recent NeurIPS cycle drew 40,000 submissions. There are simply too many papers, while verification — which is what actually supplies new knowledge and new information — hasn't sped up. **More papers and more agents therefore mean a worse signal-to-noise ratio**, and it becomes harder to extract anything useful from the volume of AI-generated content.

Back to verification: we can have all the fancy models telling us millions of novel hypotheses, but **the bottleneck will be in the lab**. Her experimental colleagues devote their careers and years of work to physical laboratories, and even at their best the workflow remains highly error-prone.

Hence the question that frames the talk: **how do we turn every scientific lab into a verifiable environment?**

On one side AI is advancing fast, with AI co-scientists from every major frontier lab and startup. On the other, scientists at the bench and in clean rooms spend months to years validating a single hypothesis. Something critical is missing in between.

#### LabOS: making the physical lab observable (~01:07–01:11)

**LabOS is an AI-XR agent**: a multimodal reasoning AI hiding behind smart glasses. Her first example was an undergraduate intern visiting from India who, with LabOS's help, could **perform an advanced genome engineering experiment essentially on day one**.

What the system provides: **every single action and every state change in a scientific lab becomes observable by AI**, alongside multi-tier streaming so that AI can **assist human researchers in real time** — catching errors, digitalizing physical workflows, troubleshooting, and offering guidance and hints when something doesn't work.

Her second example — and she stressed it was not an animation — is an **end-to-end mini robotic lab** built with colleagues at the **Princeton Quantum Institute**, automating the **nanofabrication of one-atom-thin graphene devices**. A multimodal agent runs auto-research inside the computer while the robot does the measurements, fabrication, tape-outs, and microscopic imaging. The result: work that **used to take physics PhD students three months now takes one week**. Her colleague is releasing the system as an **API**, so anyone can submit a job to reproduce an experiment or test a new hypothesis — the goal being to enable this at scale.

(Her final slide, after the host cut in for time.) They are piloting LabOS as a system where **human researchers work side by side with robots**: every physical workflow gets digitalized, every trace collected and reasoned over by the AI. It's designed to **generalize across scientific domains** — biology labs, chemistry labs, clean rooms, and nanofabrication facilities.

### Quotes

> "70% of biomedical research papers are not reproducible by others, and 50% are not even reproducible by the same authors." (~01:05:21)

Not an attitude problem — the predictable outcome of having no infrastructure for verification.

> "With AI, science is not faster. Science is actually getting slower." (~01:06:28)

Accelerate hypothesis generation without accelerating verification and the signal-to-noise ratio collapses.

> "How do we turn every scientific lab into a verifiable environment?" (~01:07)

The problem statement for the whole talk.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| LabOS | AI-XR co-scientist:智慧眼鏡背後的多模態推理 AI,即時觀測並輔助實體實驗 | AI-XR co-scientist: multimodal reasoning AI behind smart glasses that observes and assists physical experiments in real time | 對應論文 arXiv:2510.14861 / bioRxiv 2025.10.16.679418;Stanford–Princeton 合作(Le Cong × Mengdi Wang)/ Stanford–Princeton collaboration |
| 迷你機器人奈米製造實驗室 / mini robotic nanofab lab | 自動化單原子層 graphene 元件製造:量測、製造、tape-out、顯微影像全由機器人執行 | Automates one-atom-thin graphene device fabrication end to end — measurement, fabrication, tape-out, microscopy | 與 Princeton Quantum Institute 同事合作;三個月 → 一週;將開放為 API / with Princeton Quantum Institute colleagues; 3 months → 1 week; being released as an API |
| Nature 可重現性調查 / Nature reproducibility survey | 70% 生醫論文他人無法重現、50% 原作者也無法重現 | 70% of biomedical papers not reproducible by others; 50% not reproducible by their own authors | 演講中僅稱「a survey run by researchers and Nature」/ described only as "a survey run by researchers and Nature" |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Mangdi Wang | Mengdi Wang |
| lab OS | LabOS |
| Europe submission | NeurIPS submissions |
| clean rooms(字幕正確) | clean rooms |
| nanop fabrication | nanofabrication |
| graphing devices | graphene devices |
| purity students | PhD students |
| AI co-cientists | AI co-scientists |

## 待確認 / To Verify

- **實習生姓名**:字幕作 "Simmeran",拼寫未確認。/ The intern's name, transcribed as "Simmeran", is unverified.
- **同事的部落格**(主張「有了 AI 科學反而變慢」)作者與連結未提及。/ The colleague's blog arguing science is getting slower with AI was neither named nor linked.
- **NeurIPS 4 萬份投稿**的年度未指明(字幕作 "the most recent Europe submission")。/ The year of the 40,000-submission NeurIPS cycle wasn't specified.
- **Nature 可重現性調查**的年份與正式出處未提供(公開常引的是 2016 年 Nature 的 1,576 人調查)。/ The year and citation for the Nature reproducibility survey weren't given (the commonly cited one is Nature's 2016 survey of 1,576 researchers).
- 開放為 API 的那位 Princeton 同事姓名與服務名稱未提及。/ The Princeton colleague releasing the API, and the service's name, weren't mentioned.
