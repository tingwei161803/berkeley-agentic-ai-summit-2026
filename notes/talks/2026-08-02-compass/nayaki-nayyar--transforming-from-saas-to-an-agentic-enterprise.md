---
title: "Transforming from SaaS to an Agentic Enterprise"
title_zh: "從 SaaS 轉型為 Agentic Enterprise"
speaker: "Nayaki Nayyar"
affiliation: "CEO, Siteimprove"
type: talk
stage: Compass
date: 2026-08-02
session: "Session 3: Enterprise AI"
video: "https://www.youtube.com/watch?v=1UrriPJRSPU&t=4850s"
video_range: "01:20:50–01:27:05"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [enterprise, accessibility, mcp, content-intelligence, saas]
---

# 從 SaaS 轉型為 Agentic Enterprise(Transforming from SaaS to an Agentic Enterprise)

**一句話總結**:當內容量無限、且人人都能生成內容時,事後掃描與修補來不及了;Siteimprove 的轉型路線是把合規檢測「左移」到創作當下,用 MCP server 把自家 agent 直接接進 Lovable、VS Code 這類 AI 創作工具裡。
**One-line summary**: When content volume is effectively infinite and everyone is a creator, scanning and fixing after the fact no longer works; Siteimprove's answer is to shift compliance left into the moment of creation, wiring its agents directly into AI building tools like Lovable and VS Code through an MCP server.

## 中文筆記

### TL;DR

- **客戶的兩個核心痛點**:一是**內容合規**——歐洲的 EAA(European Accessibility Act)與北美的 ADA 都要求大型企業確保內容可及性;二是**內容能見度**——搜尋已經從傳統搜尋演化成 AI 驅動搜尋,內容能不能被 AI 找到成了新問題。
- **解法是 shift left**:不在事後掃描,而是在開發者、設計師、內容創作者**產生內容的當下**就偵測並自動修復問題。
- **落地方式是 MCP server**:把自家 agent 接進 Lovable、Copilot、VS Code 等 AI 工具,讓 agent 之間互相呼叫;原本要花數週到數月的整合,現在幾天甚至幾分鐘就能完成。

### 重點整理

#### 問題:無限內容 + 兩種合規壓力(約 01:21–01:23)

Siteimprove 已在業界超過 20 年,全球有 **5,500+ 客戶**,涵蓋 Global 2000 與 Fortune 500、金融機構、醫療、公部門等產業。講者說我們現在活在一個「AI 驅動、內容無限」的世界——網頁內容、行動內容、社群內容、文件,各種形態的內容都在暴增,而大型全球企業對此非常吃力。

客戶的第一個共同挑戰是**內容合規**,尤其是可及性(accessibility):歐洲有 **EAA(European Accessibility Act)**,北美有 **ADA(Americans with Disabilities Act)**,都要求大型企業確保內容合規。

第二個挑戰是**內容能見度**:搜尋已經從傳統搜尋演化成 AI 驅動的搜尋(她當場請聽眾舉手,幾乎全場都在用 AI 搜尋找資訊)。內容能不能出現在這些 AI 搜尋裡,成了新的競爭問題。

第三個挑戰她描述為:**在人人都是開發者、人人都能生成內容與設計的世界裡,怎麼確保這些內容是合規且有效的?**

#### 解法:shift left 與 agentic content intelligence platform(約 01:23–01:25)

回應是**「shift left」**——在創作的當下就解決問題,在開發者寫程式、設計師做設計、內容創作者產內容、應用被生成出來的那一刻就偵測問題並修復,而不是事後補救。

為此,他們去年推出了 **agentic content intelligence platform**,分四大支柱:

1. **Accessibility agents**:在創作當下偵測並自動修復可及性問題。
2. **Conversational analytics agents**:你可以直接問問題,它自動生成報表與 dashboard。
3. **Search agents**:確保內容在各種 AI 驅動搜尋中可被看見。
4. **Content strategy agents**:產生 content brief、content draft 與各種內容描述。

同時他們發布了 **MCP server**,把 agent-to-agent 的整合能力接進 Lovable、Copilot、VS Code 這類 AI 工具。她強調的效益是**整合速度**:原本進入市場需要數週甚至數月的整合,現在能在幾天、甚至幾分鐘內完成。

#### Demo:Lovable × Siteimprove agent 互相呼叫(約 01:25–01:27)

現場播放了一段預錄 demo,展示與 **Lovable** 的整合:

1. 先問 Lovable 有哪些 agent 可用——它立刻偵測到 Siteimprove agents、Lovable agents 與 browser agents。
2. 再問 Siteimprove agents 能做什麼——列出多個能力(偵測、AI rules、auto remediation 等;確切名稱見「待確認」)。
3. 抓取右側網站的 URL,跑一次快速可及性檢查,回報約 **5 個問題**。
4. 最後下一個提示,讓 **Siteimprove agents 與 Lovable agents 互相協作**:透過 MCP server 呼叫 agent、偵測問題、並自動修復。

她的結論:過去偵測與修復這些問題要花數週到數月,現在幾分鐘就能完成。目標是幫客戶讓那些「無限量的內容」同時**保持合規又有成效**——「這對我們不是二選一,是 and,而且全部跑在單一平台上」。

### 金句

> "Our response … is to shift left — is to address this problem at the time of creation."(約 01:23)

在「人人都是開發者」的世界裡,事後掃描的模式已經追不上內容產生的速度。

> "It's not an either-or solution for us. It's an and solution, and that's all running on one single platform."(約 01:27)

合規與成效不是取捨關係,而是要同時滿足的兩個條件。

## English Notes

### TL;DR

- **Two core customer pains**: **content compliance** — the European Accessibility Act (EAA) in Europe and the ADA in North America both require large enterprises to keep content accessible — and **content visibility**, now that search has moved from traditional engines to AI-driven search.
- **The answer is shifting left**: detect and remediate issues at the moment developers, designers, and content creators produce the content, rather than scanning after publication.
- **The delivery mechanism is an MCP server** that plugs their agents into Lovable, Copilot, VS Code, and similar AI building tools so agents can call each other — collapsing integrations that used to take weeks or months into days or minutes.

### Key Points

#### The problem: infinite content plus two kinds of compliance pressure (~01:21–01:23)

Siteimprove has been in the industry 20+ years with **5,500+ customers worldwide** across the Global 2000 and Fortune 500 — financial institutions, healthcare, public sector, and more. Her framing: we now live in an AI-driven world with infinite content — web, mobile, social, documents — and large global enterprises are struggling with all of it.

The first challenge every customer raises is **compliance**, specifically accessibility. The **European Accessibility Act (EAA)** in Europe and the **ADA (Americans with Disabilities Act)** in North America both require large enterprises to keep their content compliant.

The second is **content visibility**: search has evolved past traditional search into AI-driven search — she asked for a show of hands and, at an agentic AI conference, essentially everyone was using AI search. Whether your content surfaces there is now a competitive question.

The third: in a world where everyone is a developer and everyone can generate content and designs, how do you ensure that content stays compliant and performs?

#### The response: shift left and an agentic content intelligence platform (~01:23–01:25)

Their answer is to **shift left** — address the problem at the time of creation, detecting and remediating issues as developers write code, designers produce designs, and creators generate content, instead of cleaning up afterward.

Last year they released an **agentic content intelligence platform** across four pillars:

1. **Accessibility agents** — detect and auto-remediate accessibility issues at creation time.
2. **Conversational analytics agents** — ask a question, get generated reports and dashboards.
3. **Search agents** — make content visible across AI-driven search surfaces.
4. **Content strategy agents** — content briefs, drafts, and descriptions.

Alongside that they released an **MCP server** enabling agent-to-agent integration across AI tools — Lovable, Copilot, VS Code. The benefit she emphasized is integration speed: what used to take weeks or months to bring to market can now be done in days or even minutes.

#### Demo: Lovable and Siteimprove agents calling each other (~01:25–01:27)

A recorded demo of the **Lovable** integration:

1. Ask Lovable which agents it has access to — it immediately detects the Siteimprove agents, Lovable agents, and browser agents.
2. Ask what the Siteimprove agents can do — it lists capabilities including detection, AI rules, and auto-remediation (exact product names in "To Verify").
3. Grab the URL of the site shown on the right and run a quick accessibility check — roughly **five issues** come back.
4. Prompt the **Siteimprove agents and Lovable agents to work together**: calls go through the MCP server, issues are identified, and remediation happens automatically.

Her conclusion: detecting and remediating these issues used to take weeks to months and now takes minutes. The goal is helping customers keep their infinite volume of content both compliant *and* performing — "it's not an either-or for us, it's an and, and that's all running on one single platform."

### Quotes

> "Our response … is to shift left — is to address this problem at the time of creation." (~01:23)

In a world where everyone is a developer, post-hoc scanning can't keep up with content creation.

> "It's not an either-or solution for us. It's an and solution, and that's all running on one single platform." (~01:27)

Compliance and performance are both requirements, not a trade-off.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Siteimprove.ai Agentic Content Intelligence Platform | 四大支柱:accessibility / conversational analytics / search / content strategy agents | Four pillars: accessibility, conversational analytics, search, and content strategy agents | 去年發布 / released last year |
| Siteimprove.ai MCP Server | 讓自家 agent 接進 Lovable、Copilot、VS Code 等 AI 創作工具,支援 agent-to-agent 呼叫 | Connects their agents into Lovable, Copilot, VS Code and other AI-native tools for agent-to-agent calls | 官方新聞稿另提及 Anthropic Claude 與 Figma 連接器 / press materials also list Anthropic Claude and Figma connectors |
| EAA (European Accessibility Act) | 歐洲的可及性法規 | EU accessibility legislation driving enterprise compliance demand | |
| ADA (Americans with Disabilities Act) | 北美的可及性法規 | US accessibility legislation | 逐字稿誤作 "American Disability Act" |
| Lovable | Demo 中示範整合的 AI 應用生成工具 | The AI app-building tool used in the live-recorded demo | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Nyaki Naar / Nyaki Ner | Nayaki Nayyar |
| Sentiment Proof / side improve | Siteimprove |
| SAS | SaaS |
| American Disability Act | Americans with Disabilities Act (ADA) |
| agent-gagent | agent-to-agent |
| lovables of the world / co-pilots of the world / VS codes of the world | Lovable / Copilot / VS Code |

## 待確認 / To Verify

- Demo 中念到的三個 agent 能力名稱:「alpha detect agent」「AI rules agent」「auto remediation agents」——前兩者拼法無法確認(「alpha detect」可能是可及性領域慣用的 a11y 相關命名),需看影片畫面確認。/ The three capability names read out in the demo — "alpha detect agent", "AI rules agent", "auto remediation agents" — the first two can't be confirmed from audio; check the on-screen demo.
- 講者提到的「MCP server 讓整合從數週縮短到數分鐘」缺少具體案例佐證。/ No concrete case study was given behind the "weeks to minutes" integration claim.
- 5,500+ 客戶數與「20 plus years」為講者口述,未見於本場其他資料。/ The 5,500+ customer count and "20+ years" figure are as spoken; not otherwise sourced here.
