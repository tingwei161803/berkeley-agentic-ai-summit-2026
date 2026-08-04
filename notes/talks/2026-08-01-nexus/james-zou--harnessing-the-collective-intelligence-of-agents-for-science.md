---
title: "Harnessing the Collective Intelligence of Agents for Science"
title_zh: "駕馭科學研究中的智能體集體智慧"
speaker: "James Zou"
affiliation: "Professor, Stanford"
type: talk
stage: Nexus
date: 2026-08-01
session: "Session 1: AI for Science"
video: "https://www.youtube.com/watch?v=LB7IkZhEYic&t=1290s"
video_range: "00:21:30–00:32:45"
transcript: "tmp/[English (auto-generated)] Nexus Stage - August 1st - Morning Session [DownSub.com].srt"
status: draft
tags: [ai-for-science, multi-agent, drug-discovery, agent-infrastructure, reproducibility]
---

# 駕馭科學研究中的智能體集體智慧(Harnessing the Collective Intelligence of Agents for Science)

**一句話總結**:新的 scaling 軸不是把單一模型做大,而是把互相協作的科學家 agent 從十個推到數千、數百萬個——並為此重建整套「給 agent 用而不是給人用」的科學資料基礎建設。
**One-line summary**: The new scaling axis isn't bigger individual models but more collaborating scientist agents — from ten to thousands to millions — which in turn requires rebuilding scientific data infrastructure for agents instead of humans.

## 中文筆記

### TL;DR

- **把 agent 數量當作 scaling 軸**:Virtual Lab(5–10 個 agent)→ Virtual Biotech(數萬個 agent)→ 目標數百萬個;每上一個量級,湧現的能力都不同。
- **兩個已被真實世界驗證的結果**:Virtual Lab 設計的 nanobody 經實驗合成測試,對近期 SARS-CoV 變異株的結合力優於此前最好的人類設計抗體;Virtual Biotech 針對肺癌標的 CD276 提出的 ADC 設計,數個月後被 Merck 獨立做出同樣設計、進臨床並獲 FDA breakthrough designation。
- **瓶頸在基礎建設**:現有科學資料庫與 API 是為人類(或前 AI 時代演算法)設計的,對 agent 太脆弱、太受限;他們把資料庫轉成 **agent-native 虛擬檔案系統(PaperClip)**,準確率更高,而且比走傳統 MCP / API 快一個數量級也便宜一個數量級。
- **Paper agents**:把靜態論文轉成會做事的「虛擬作者」。副作用之一是自動化的可重現性檢查——很多情況下 paper agent 直接抓出原論文的關鍵錯誤與限制;更有趣的是 paper agent 之間會自己談出合作。

### 重點整理

#### 從 Virtual Lab 到 Virtual Biotech(約 00:22–00:27)

他領導 Stanford 的 AI for Science Lab,最近最興奮的方向是**把協作的 AI 科學家 agent 數量當成新的 scaling 維度**:不是把單一模型放大,而是從幾十個 agent 推到數百、數千、數百萬,看會湧現什麼新能力。

**Virtual Lab** 是第一步:5–10 個 agent 模擬他在 Stanford 的實體實驗室。有一個 AI professor agent 主持,底下是不同專長的 AI student agent(數學、資料科學、蛋白質設計);它們開自己的 group meeting,有預算可以真的跑實驗,還有一個複製版的「Stanford agent school」讓 agent 在各自領域裡變成更好的研究者。

第一個指派的專案是**設計能結合近期 SARS-CoV 變異株的 binder**。demo 裡可以看到 group meeting 的過程:professor agent 說明目標,免疫學 agent 建議做 nanobody,ML agent 提出最佳化構想。經過一連串 group meeting 與一對一討論後,agent 設計出一套與既有文獻不同的 nanobody 最佳化計算框架,跑完再回報幾個新設計。實驗合作者合成並實測,證實是相當有效的 binder,**對部分近期變異株甚至優於此前最好的人類設計抗體**。

**Virtual Biotech** 是下一級:用數萬個 AI 科學家 agent 模擬一整間藥廠。頂層是 CSO agent,有自己的 chief of staff、辦公室與法務;底下是對應人類藥廠的各個部門——找標的、依標的設計分子、設計臨床試驗與安全性評估。每個部門再由專精不同的 agent 組成(有的擅長遺傳學資料,有的擅長單細胞分析)。

指派的專案是為肺癌標的 **CD276**(一種抑制免疫反應的跨膜蛋白,藥廠高度關注)設計新療法。數千個 agent 做了大量遺傳學、基因體、病患資料分析後,提出一個**針對 CD276 的 ADC(antibody–drug conjugate)**設計:抗體連上化療 payload,命中標的後釋放。這在當時對 CD276 算是相對新的設計。幾個月後,**Merck 獨立做出同一個 CD276 ADC**,在人體試驗中證實有效並取得 FDA breakthrough designation——等於人類研究反過來驗證了 Virtual Biotech 的設計。

#### 讓 agent 用得動的基礎建設:PaperClip(約 00:27–00:29)

要讓數千個 agent 在科學上真的有效率,他們發現必須**新增一層專為 agent 而生的基礎建設與環境**。現有的科學資料庫(包含各種蛋白質資料庫)大多是設計給人類、或給前 AI 時代的演算法消費的,對 agent 來說 API 太脆弱、太受限。

他們的做法是把這些既有資料庫——數百萬個蛋白質、分子、基因表現資料——**轉換成 agent-native 的虛擬檔案系統**,讓 agent 更容易跨資料源合成與彙整資訊。這套東西叫 **PaperClip**,涵蓋範圍已擴到「全部科學知識」:arXiv 及其他地方的全文論文,加上各種資料庫。比較結果是:用這種虛擬檔案系統表示所有科學資料集與知識,**準確率明顯優於**同樣模型走傳統 MCP / API 存取資料庫的做法,而且**快一個數量級、便宜一個數量級**。他強調這是免費的,一行程式碼就能把全部知識掛給你的 agent。

#### Paper agents:把論文變成會協作的虛擬作者(約 00:29–00:32)

過去幾百年,人類把知識封裝成**靜態論文**這種很被動的產物;讀者或潛在合作者光讀死的文字,往往很難把知識搬到自己的問題上。他們的想法是把這些靜態產物**轉成動態、可互動的「虛擬作者」,也就是 paper agent**——你可以直接問它「幫我把這篇論文的方法套到我的資料集上」,它會自動執行、產生可重現的 workflow,再把結果與發現交回來。

底層是一條 paper-to-agent 的自動化流程:一群 worker agent 讀原論文與相關程式碼、資料,建立虛擬環境,嘗試**復現原本的研究流程**;過程中產出一個 paper MCP,再包成 paper agent。

副產品是**自動化的可重現性檢查**:demo 裡的 paper agent 能生成與原刊物一致的中間圖表與結果(該篇是可重現的);但他強調**在很多其他案例中,paper agent 直接找出了原論文的關鍵錯誤與限制**。

最有意思的應用是 agent 之間的新型合作。他們正在把人類發表過的每一篇論文都轉成 agent,規模是數百萬個,而這些 agent 開始互相對話。一個真實例子:Google DeepMind 幾個月前發表的 **AlphaGenome** 被轉成一個「知道怎麼用這個工具」的 agent;另一組人發表的、連結 GWAS 上 ADHD 風險突變的遺傳資料集被轉成另一個「知道怎麼用這份資料」的 agent。**這兩個 agent 自己聊了起來,判斷彼此可以合作,然後自動發現了一個此前未知、會提高 ADHD 風險的突變。**

### 金句

> "So instead of scaling individual models but scale the number of agents, you know, from tens of agents to hundreds to thousands and even millions of agents that collaborate and see what are the new kinds of capabilities that emerges."(約 00:22:03)

整場演講的主張濃縮在這一句:scaling 的對象換了。

> "…why don't we turn all of those static artifacts of knowledge from papers into dynamic and interactive virtual authors that we call paper agents."(約 00:29:53)

論文不再是要被讀的東西,而是可以被指派工作的對象。

## English Notes

### TL;DR

- **Scale the number of agents, not the size of the model**: Virtual Lab (5–10 agents) → Virtual Biotech (tens of thousands) → millions. Each order of magnitude surfaces different emergent capabilities.
- **Two results validated outside the simulation**: Virtual Lab's nanobody designs were synthesized and tested, binding recent SARS-CoV variants better than the best prior human-designed antibodies; and Virtual Biotech's ADC design for the lung-cancer target CD276 was independently arrived at by Merck months later, tested in humans, and granted FDA breakthrough designation.
- **The bottleneck is infrastructure**: existing scientific databases and APIs were built for humans or pre-AI algorithms and are too brittle for agents. Converting them into an **agent-native virtual file system (PaperClip)** gives better accuracy while being an order of magnitude faster and cheaper than the same models hitting those databases through conventional MCPs or APIs.
- **Paper agents** turn static papers into virtual authors that do work. One side effect is automated reproducibility checking — in many cases the paper agent surfaced key mistakes and limitations in the original publication. The more interesting effect is paper agents negotiating collaborations with each other.

### Key Points

#### From Virtual Lab to Virtual Biotech (~00:22–00:27)

Zou leads Stanford's AI for Science Lab, and the direction he's most excited about is treating **the number of collaborating AI scientist agents as a new scaling axis** — going from tens of agents to hundreds, thousands, even millions, and seeing what capabilities emerge.

**Virtual Lab** was the first step: five to ten agents emulating his physical lab. An AI professor agent runs it; AI student agents bring different expertise (mathematics, data science, protein design). They hold their own group meetings, get a budget to run real experiments, and attend a replica "Stanford agent school" to become better researchers in their domains.

Their first assignment was designing **binders for recent SARS-CoV variants**. The demo walks through a group meeting: the professor agent lays out the goal, the immunologist agent recommends nanobodies, the machine-learning agent proposes an optimization approach. After a series of group meetings and one-on-one discussions, the agents produced a nanobody-optimization framework that differed from anything previously published, ran it, and came back with candidate designs. Experimental collaborators synthesized and tested them: effective binders, and for some recent variants **better than the best previously published human-designed antibodies**.

**Virtual Biotech** scales this to an entire pharma company with tens of thousands of scientist agents. A CSO agent sits at the top with its own chief of staff, office, and lawyers; below it are divisions mirroring a human pharma org — target identification, molecule design against those targets, clinical trial design and safety. Each division is staffed by specialized agents (one good at genetics data, another at single-cell analysis).

The assignment: design a new therapeutic for **CD276** in lung cancer, a transmembrane protein that suppresses immune response and a target many pharma companies care about. After heavy analysis across genetics, genomics, and patient data, the agents proposed an **antibody–drug conjugate (ADC)** — an antibody designed for CD276 linked to a chemotherapy warhead released on target. That was a relatively novel design for CD276 at the time. Several months later **Merck independently designed the same CD276 ADC**, tested it in human populations, showed efficacy, and received FDA breakthrough designation — a rare case of human studies independently corroborating an agent-generated design.

#### Infrastructure agents can actually use: PaperClip (~00:27–00:29)

Making thousands of agents effective at science required **a new layer of infrastructure and environments built for them**. Existing scientific databases — including the ones holding millions of proteins — were designed to be consumed by humans or by pre-AI algorithms, so their APIs are too brittle and too limited for agents to use efficiently.

Their answer was to convert those databases (millions of proteins, molecules, gene expression records) into **agent-native virtual file systems**, making it far easier for agents to synthesize and aggregate across sources. The system is called **PaperClip**, and its scope has grown to essentially all of scientific knowledge: full-text papers from arXiv and elsewhere, plus the databases. The comparison he showed: representing scientific data and knowledge this way yields **higher accuracy** than giving the same language models access through traditional MCPs or APIs, while being **an order of magnitude faster and cheaper**. It's free, and one line of code hands the whole corpus to your agents.

#### Paper agents: papers that collaborate (~00:29–00:32)

For hundreds of years humans have encoded knowledge in **static papers** — passive artifacts. Readers and would-be collaborators often can't tell, from the words alone, how to adapt the knowledge to their own problem. So: turn those static artifacts into **dynamic, interactive virtual authors — paper agents**. Ask one to apply the paper's method to your dataset and it does so automatically, generating reproducible workflows and returning results.

Under the hood is an automated paper-to-agent pipeline: worker agents read the original paper plus any associated code and data, build a virtual environment, and try to replicate the original research — producing a paper MCP that becomes a paper agent.

One application is **reproducibility checking**. In the demo the paper agent regenerated intermediate figures and results matching the original publication, so that paper reproduced. But he was explicit that **in many other cases the paper agent identified key mistakes and limitations in the original publication**.

The most interesting application is a new form of agent-to-agent collaboration. They're in the process of converting every paper ever published — millions of paper agents — and those agents have started talking to each other. A real example: Google DeepMind's **AlphaGenome** paper became an agent that knows how to use that tool; a separate group's genetic dataset of mutations linked to GWAS risk for ADHD became an agent that knows how to use that data. **The two agents started talking, decided they could collaborate, and automatically discovered a previously unknown mutation that increases ADHD risk.**

### Quotes

> "So instead of scaling individual models but scale the number of agents, you know, from tens of agents to hundreds to thousands and even millions of agents that collaborate and see what are the new kinds of capabilities that emerges." (~00:22:03)

The whole talk in one sentence: the object of scaling has changed.

> "…why don't we turn all of those static artifacts of knowledge from papers into dynamic and interactive virtual authors that we call paper agents." (~00:29:53)

A paper stops being something you read and becomes something you assign work to.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Virtual Lab | 5–10 個 agent 模擬實體實驗室(AI professor + AI students + group meetings + 預算) | 5–10 agents emulating a physical lab: AI professor, AI students, group meetings, a budget | nanobody 成果已發表於 Nature(2025-07-29)/ nanobody result published in *Nature*, 29 Jul 2025 |
| Virtual Biotech | 數萬個 agent 模擬整間藥廠(CSO agent + 各部門) | Tens of thousands of agents emulating a full pharma org (CSO agent plus divisions) | CD276 ADC 設計後被 Merck 獨立驗證 / CD276 ADC independently corroborated by Merck |
| PaperClip | 把科學資料庫與全文論文轉成 agent-native 虛擬檔案系統 | Agent-native virtual file system over scientific databases and full-text papers | 免費、一行程式碼接入;比 MCP/API 路線快且便宜一個數量級 / free, one line of code; ~10× faster and cheaper than MCP/API access |
| Paper agents / Paper2Agent | 自動把論文(含程式碼與資料)轉成可執行的 paper MCP → paper agent | Automated pipeline converting a paper plus its code and data into a paper MCP, then an agent | 對應論文 Paper2Agent(arXiv:2509.06917)/ corresponding paper: Paper2Agent (arXiv:2509.06917) |
| AlphaGenome | Google DeepMind 的基因體模型,被轉成 paper agent 參與自動合作 | Google DeepMind genomics model, turned into a paper agent that autonomously collaborated | 與 ADHD GWAS 資料集 agent 合作發現新突變 / paired with an ADHD GWAS dataset agent to find a novel mutation |
| CD276 | 肺癌標的,抑制免疫反應的跨膜蛋白 | Lung-cancer target; transmembrane protein that suppresses immune response | 又名 B7-H3(未於演講中提及)/ also known as B7-H3 (not mentioned in the talk) |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| James Zoo | James Zou |
| nanobbody / imunologist | nanobody / immunologist |
| virtual baltech / btech | Virtual Biotech |
| Mercy / Merc | Merck |
| paper clip | PaperClip |
| alpha genome | AlphaGenome |
| GW was | GWAS |
| antibbody drug conjugate | antibody–drug conjugate (ADC) |
| cso agent / chief scent officer | CSO agent / Chief Scientific Officer |

## 待確認 / To Verify

- **PaperClip** 的正式名稱與歸屬:市面上另有一個同名的通用 agent 編排平台(paperclip.ing),與 Zou 描述的「科學虛擬檔案系統」是否為同一專案,無法從公開資料確認。/ The name **PaperClip** is ambiguous — a general-purpose agent-orchestration platform of the same name exists (paperclip.ing); whether it is the same project as the scientific virtual file system Zou described could not be confirmed.
- 字幕中與 PaperClip 對照的基線寫作 "clot science" / "latest clot models",推測是 Claude 相關產品,但拼寫與確切對象待確認。/ The baseline compared against PaperClip, transcribed as "clot science" / "latest clot models", is presumably a Claude-related product but the exact name is unconfirmed.
- Virtual Biotech 的 agent 數量,演講中同時出現「tens of thousands」與「many thousands」,實際規模待確認。/ Virtual Biotech's agent count — the talk says both "tens of thousands" and "many thousands".
- Merck 的 CD276 ADC 取得 FDA breakthrough designation 的時間與藥物代號未提及。/ The date and code name of Merck's CD276 ADC breakthrough designation were not given.
- 「Stanford agent school」是內部代稱還是正式系統名稱,未確認。/ Whether "Stanford agent school" is an informal nickname or a named system is unconfirmed.
