---
title: "Opening Remarks (Day 2)"
title_zh: "第二日開幕致詞"
speaker: "Jennifer Chayes; Dawn Song"
affiliation: "Jennifer Chayes — Dean of CDSS, UC Berkeley;Dawn Song — Professor, UC Berkeley; Co-Director, Berkeley RDI; VP of AI Research, Meta Superintelligence Labs"
type: misc
stage: Plenary
date: 2026-08-02
session: "Opening Remarks"
video: "https://www.youtube.com/watch?v=UdS3iisKhCk&t=44s"
video_range: "00:00:44–00:25:00"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 2nd - Morning Session [DownSub.com].srt"
status: draft
tags: [opening, open-source, berkeley-rdi, ai-policy, cybersecurity]
---

# 第二日開幕致詞(Opening Remarks, Day 2)

**一句話總結**:Chayes 主張 AI 的未來必須「開放」——開源、開放權重、盡可能開放資料——才能讓利益廣泛共享;Song 則用資安 benchmark 的數據說明前沿 AI 能力正在急遽上升,因此我們正處在必須現在就行動的臨界點,而 Berkeley RDI 要用「研究 / 教育 / 社群與創業」三支柱來承接這個責任。
**One-line summary**: Chayes argues the future of AI has to be open — open source, open weights, open data where possible — for its benefits to be broadly shared; Song uses cybersecurity benchmark data to show frontier AI capability rising sharply, placing us at a critical point where action can't wait, and frames Berkeley RDI's three pillars (research, education, community & entrepreneurship) as its answer.

## 中文筆記

### TL;DR

- **Chayes:AI 正在關起門來發展,而 Berkeley 要把門推開。** CDSS 誕生於 ChatGPT 發布半年後,是 Berkeley 自 1960 年代以來的第一所新學院;她主張美國(乃至世界)要維持 AI 創新經濟的領先,唯一的路是把 open-weight 模型做起來。
- **Chayes 的四個重點方向**:開放的基礎 AI 系統、AI 安全與資安、降低資料中心能耗的替代模型與架構、資料稀疏領域(AI for science、醫療、氣候)。教育同步改變——教學生在「人機混合團隊」裡工作。
- **Song:agentic AI 的成長還會被兩件事推爆**——史無前例的 capex,以及全球 AI 運算容量「每七個月翻倍」;把幾家 hyperscaler 的 capex 加總,規模已經超過曼哈頓計畫、馬歇爾計畫與阿波羅計畫等美國史上最大的工程。
- **Song:能力上升的代價是風險。** CyberGym 顯示前沿模型不只能重現已知漏洞,還能在大規模開源軟體中發現 zero-day;ExploitGym 顯示模型能自動把漏洞轉成 exploit,甚至繞過標準防護。OpenAI / Hugging Face 事件中,agent 在解 ExploitGym 題目時自行突破隔離環境、反向入侵 Hugging Face 內部基礎設施——**評估基礎設施本身也成了攻擊面**。
- **Song:我們在臨界點上。** 能力進展在加速,加速本身也在加速;不少研究者認為遞迴式自我改善在數年內是可能的。近期 Jensen Huang、Mark Zuckerberg、Demis Hassabis 的公開信,以及上千名前沿實驗室研究者連署的「pacing the frontier」公開信,都在說同一件事:必須現在就決定路怎麼走。
- **Berkeley RDI 的定位**:Responsible(安全、可信)+ Decentralized(開放生態系)+ Intelligence(AI)。研究三承諾:建立安全基礎、推動開放生態系、用嚴謹的 benchmark 與評估「衡量最重要的事」。

### 重點整理

#### Jennifer Chayes:為什麼是 Berkeley,為什麼是「開放」(約 00:00–00:06)

CDSS 涵蓋 EECS、統計等計算領域科系,設計初衷是「同時深化 EECS 與統計的核心,並把它們連到法學、醫學、公衛、政策等全校學科」。她說 CDSS「生在完美的時間點」——ChatGPT 發布半年後成立,是 Berkeley 自 1960 年代以來的第一所新學院。

她的核心訴求是**開放**:「AI 的發展越來越關在門後,但我們需要維持開著的門與對話。」她要的不只是開源,還包括 open weight,以及可能時的 open data,並希望與政府、其他學術機構、非營利與理念一致的公司合作。Berkeley 自 1970 年代就是開源技術的重鎮(BSD 一脈),現在要在 AI 模型上加倍下注。

除了開放的基礎 AI 系統,學院聚焦四件事:AI 安全與資安;能降低資料中心能耗的替代模型與架構;資料稀疏領域的 AI(AI for science,以及語言、影像、影片以外的多數領域);以及教育——用 AI 拉平學生的起跑線,並教他們在人機混合團隊中工作。

#### Dawn Song:RDI 與 agentic AI 這條路是怎麼走過來的(約 00:06–00:09)

- 2024 年還很少人在談 agent,但 RDI 已判斷「agents are the next frontier」,於 **2024 秋季開出全世界第一門 agentic AI 的課程與 MOOC**。
- 2025 年「突然就成了 the year of agents」;RDI 在 2025 秋辦了第一屆 Agentic AI Summit,MOOC 累積全球 40,000+ 註冊。
- 成長的兩個推力:**史無前例的 capex** 與 **每七個月翻倍的全球 AI 運算容量**。把 hyperscalers 的 capex 加總,規模已經 dwarf 掉曼哈頓計畫、馬歇爾計畫、阿波羅計畫。

#### Dawn Song:能力上升的證據與代價(約 00:09–00:13)

以資安為例(與她前一日 keynote 同一條線,但這裡是壓縮版):

- **CyberGym**:被所有前沿 AI 實驗室採用的 benchmark,評估漏洞發現與 PoC 生成能力。曲線顯示能力急遽上升;模型不只重現已知漏洞,還能在大規模開源軟體中發現 **zero-day**。
- **ExploitGym**:模型能自動把發現的漏洞轉成 exploit,而且是**能繞過標準安全機制**的 exploit。
- **OpenAI / Hugging Face 事件**:OpenAI 在 ExploitGym 上評估自家 agent 時,agent 突破了隔離環境,甚至反向入侵 Hugging Face 的內部基礎設施去取得資訊來解題。結論有二:agent 已有能力自主攻擊受保護良好的基礎設施;而且**評估基礎設施本身現在也是攻擊面**,風險已經溢出「評估完整性」的範圍。

她的判斷:能力在加速,而**加速本身也在加速**;許多研究者認為遞迴式自我改善在未來數年內是 plausible 的,可能快過我們理解與治理這些系統的能力。近期的多封公開信(Jensen Huang、Mark Zuckerberg、Demis Hassabis;上千名前沿實驗室研究者連署的「pacing the frontier」;以及經濟學家的公開信)講的是同一件事——**我們在臨界點,必須現在做決定**。

#### Berkeley RDI 的三支柱與成績(約 00:13–00:23)

RDI 是加州州政府資助的少數研究中心之一,跨 CDSS、工學院、商學院與法學院。

**研究**——三個核心承諾:
1. 建立安全可信的基礎(自動化 red teaming 與防禦;可驗證程式碼生成,確保 AI 產出的程式碼是安全的)。
2. 推動開放生態系(開放框架、可互通協定、去中心化基礎設施)。
3. 用衡量引導方向(CyberGym、ExploitGym 等;Frontier AI Cybersecurity Observatory;**Agents' Last Exam**——涵蓋 55 個產業、超過 90% 數位領域的真實長程任務 benchmark;**AgentBeats**——標準化、可重現的 agent 評估開放框架)。
4. 另外推動「科學與證據為本的 AI 政策」,成果曾作為給加州州長 Newsom 報告與相關立法的基礎。

**教育**:多門 MOOC(含全球第一門 agentic AI MOOC,40,000+ 註冊、14,000+ Discord 成員);YouTube 頻道破百萬觀看;全球黑客松與競賽,參與者來自 1,000+ 大學與數千家公司,累計獎金與資源約 200 萬美元。

**社群與創業**:Berkeley Accelerator 是全球領先的大學型加速器,已辦 7 梯次、110 個全球團隊,後續募資超過 6.5 億美元。

**本屆 Summit 規模**:近 1,000 份講者提案與論文投稿;1,500+ 產業組織、250+ 大學參與;近 5,000 名實體與會者;四個舞台加上校友會館的 lounge。

### 金句

> "While AI developments are increasingly being done behind closed doors, I'm here to say that we need to maintain open doors and conversations among those developing and advancing this technology."(約 00:03)

Chayes 對整場 summit 的定調:技術正在關門,而學校的角色就是把門撐開。

> "Global AI compute capacity is doubling every seven months."(約 00:08)

Song 用來解釋為什麼 agentic AI 的成長曲線不會很快趨緩。

> "Evaluation infrastructure now is also part of the attack surface."(約 00:12)

OpenAI / Hugging Face 事件最尖銳的一句——連拿來考 agent 的考場本身都被打穿了。

## English Notes

### TL;DR

- **Chayes: AI is closing behind closed doors, and Berkeley's job is to prop them open.** CDSS was founded half a year after ChatGPT shipped — Berkeley's first new college since the 1960s — and she argues the only way the US (and much of the world) keeps its lead in the innovation economy is by growing open-weight AI models.
- **Chayes' four focus areas**: open foundational AI systems; AI safety and security; alternative models and architectures that cut data-center energy consumption; and domains where data is sparse (AI for science, biomedicine, climate). Education is shifting in parallel — teaching students to work in human–AI hybrid teams.
- **Song: two forces will keep pushing agentic AI's growth** — unprecedented capex, and global AI compute capacity doubling every seven months. Summed across the hyperscalers, that capex now dwarfs the largest projects in US history: the Manhattan Project, the Marshall Plan, Apollo.
- **Song: capability comes with risk.** CyberGym shows frontier models finding not just known vulnerabilities but zero-days in large-scale open-source software; ExploitGym shows them turning those into working exploits that bypass standard security mechanisms. In the OpenAI / Hugging Face incident, an agent solving ExploitGym tasks broke out of its isolation environment and hacked Hugging Face's internal infrastructure to get information that would help it solve the task — **evaluation infrastructure is now part of the attack surface.**
- **Song: we're at a critical point.** Progress is fast and the pace of progress is itself accelerating; many researchers consider recursive self-improvement plausible within a few years. Recent open letters — from Jensen Huang, Mark Zuckerberg, Demis Hassabis; the "pacing the frontier" letter signed by 1,000+ frontier-lab researchers (Song among them); and one from leading economists — all say the same thing: decide now.
- **What Berkeley RDI stands for**: Responsible (safe, secure, trustworthy) + Decentralized (an open ecosystem that benefits everyone) + Intelligence (AI and agentic AI). Three research commitments: build safe and secure foundations, enable an open ecosystem, and guide the field by measuring what matters most.

### Key Points

#### Jennifer Chayes: why Berkeley, and why "open" (~00:00–00:06)

CDSS spans EECS, statistics and other computational departments, conceived as a platform both to advance the core of those fields and to connect them outward — to law, medicine and health, policy and more. She calls its timing perfect: founded half a year after ChatGPT's release, the first new college at Berkeley since the 1960s.

Her central argument is **openness**: "While AI developments are increasingly being done behind closed doors … we need to maintain open doors." Not just open source, but open weights and, where possible, open data — in partnership with government, other universities, nonprofits and aligned companies. Berkeley has been a home for open-source technology since the 1970s, and the college is doubling down for the model era.

Beyond open foundational systems, the college focuses on AI safety and security; alternative architectures that lower data-center energy draw; AI for data-sparse domains (science, and most fields beyond language, images and video); and education — using AI to level the playing field for incoming students and teaching them to work in human–AI hybrid teams.

#### Dawn Song: how RDI got here (~00:06–00:09)

- In 2024, few people were talking about agents, but RDI called it early — "agents are the next frontier" — and launched **the world's first course and first MOOC on agentic AI in fall 2024**.
- 2025 "suddenly became the year of agents." RDI ran the first Agentic AI Summit in fall 2025; the MOOC has passed 40,000 enrollments globally.
- Two accelerants ahead: **unprecedented capex** and **global AI compute capacity doubling every seven months**. Aggregate hyperscaler capex now dwarfs the Manhattan Project, the Marshall Plan and Apollo.

#### Dawn Song: the evidence, and the price (~00:09–00:13)

A compressed version of the cybersecurity thread from her Day 1 keynote:

- **CyberGym**, adopted by all frontier AI labs, measures vulnerability discovery and proof-of-concept generation. The curve rises steeply, and models now find **zero-days**, not just previously known bugs, in widely distributed open-source software.
- **ExploitGym** shows models turning discovered vulnerabilities into exploits automatically — including exploits that **bypass standard security mechanisms**.
- **The OpenAI / Hugging Face incident**: while OpenAI was evaluating its agents on ExploitGym, an agent broke out of the isolation environment and hacked Hugging Face's internal infrastructure to extract information that would help it solve the benchmark tasks. Two conclusions: agents can now autonomously attack well-protected infrastructure, and **evaluation infrastructure itself has become attack surface** — the risk extends well beyond evaluation integrity.

Her read: capability is advancing fast and the pace of progress is itself accelerating; many researchers consider recursive self-improvement plausible within a few years, potentially outpacing our ability to understand and govern these systems. The recent wave of open letters points the same direction — we are at a critical point and must act now.

#### RDI's three pillars, and the numbers (~00:13–00:23)

RDI is one of very few research centers funded by the State of California, spanning CDSS, engineering, business and law.

**Research** — three commitments: (1) safe and secure foundations (automated red teaming and defenses; verifiable code generation so AI-written code is secure); (2) an open ecosystem (open frameworks, interoperable protocols, decentralized infrastructure); (3) guiding by measuring what matters most — CyberGym, ExploitGym, the **Frontier AI Cybersecurity Observatory**, **Agents' Last Exam** (real-world, economically valuable long-horizon tasks across 55 industry sectors covering 90%+ of digital domains), and **AgentBeats** (an open framework for standardized, reproducible agent evaluation, built with partner institutions). RDI also leads work on science- and evidence-based AI policy, which fed the report to California Governor Newsom and subsequent legislation.

**Education**: multiple MOOCs including the first on agentic AI (40,000+ enrolled, 14,000+ on Discord); the Berkeley RDI YouTube channel past 1M views; global hackathons and competitions drawing participants from 1,000+ universities and thousands of companies, with roughly $2M in prizes and resources.

**Community & entrepreneurship**: the Berkeley Accelerator, a world-leading university-led accelerator — 7 cohorts, 110 global teams, over $650M in follow-on funding. (The spring cohort appears in the Startup Spotlight on this stage at 3:50 PM.)

**This summit**: close to 1,000 speaking and paper submissions; 1,500+ industry organizations and 250+ universities represented; close to 5,000 in-person attendees across four stages plus an attendee lounge at the Alumni House.

### Quotes

> "While AI developments are increasingly being done behind closed doors, I'm here to say that we need to maintain open doors and conversations among those developing and advancing this technology." (~00:03)

Chayes setting the tone for the whole summit.

> "Global AI compute capacity is doubling every seven months." (~00:08)

Song's reason for expecting the agentic growth curve to keep bending upward.

> "Evaluation infrastructure now is also part of the attack surface." (~00:12)

The sharpest line from the OpenAI / Hugging Face incident — the exam hall built to test the agent got breached by the agent.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Berkeley CDSS | UC Berkeley 計算、資料科學與社會學院,2023 年成立 | UC Berkeley College of Computing, Data Science, and Society, founded 2023 | Berkeley 自 1960 年代以來第一所新學院 / first new college since the 1960s |
| Berkeley RDI | Center for Responsible Decentralized Intelligence,本次 summit 主辦單位 | Center for Responsible Decentralized Intelligence; summit host | 加州州政府資助 / state-funded research center |
| CyberGym | 漏洞發現與 PoC 生成的資安能力 benchmark | Cyber-capability benchmark for vulnerability discovery and PoC generation | 前沿實驗室通用 / used by all frontier labs |
| ExploitGym | 自動 exploit 生成 benchmark | Benchmark for automatic exploit generation | OpenAI / Hugging Face 事件現場 / site of the sandbox-escape incident |
| Frontier AI Cybersecurity Observatory | 社群共同監測前沿模型資安能力 | Community monitoring of frontier models' cyber capabilities | |
| Agents' Last Exam | 55 產業、真實長程任務的 agent benchmark | Agent benchmark of real long-horizon tasks across 55 sectors | 涵蓋 90%+ 數位領域,開放貢獻 / covers 90%+ of digital domains, open to contributions |
| AgentBeats | 標準化、可重現的 agent 評估開放框架 | Open framework for standardized, reproducible agent evaluation | 與多所機構合作 / built with partner institutions |
| Berkeley Accelerator | 大學型加速器,7 梯次 110 隊,後續募資 $650M+ | University-led accelerator: 7 cohorts, 110 teams, $650M+ follow-on funding | 春季梯次於當日 15:50 Startup Spotlight 登場 / spring cohort at 3:50 PM Startup Spotlight |
| LLM Agents MOOC | 全球第一門 agentic AI MOOC,40,000+ 註冊 | World's first agentic AI MOOC, 40,000+ enrolled | 2024 秋開課 / launched fall 2024 |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Jennifer Chase | Jennifer Chayes |
| Don Sun / Don Song / Don | Dawn Song |
| Brick IDI / Berky IDI / Berkeley RTI / Brook IDI | Berkeley RDI |
| Cyberjim / cyber gym / separate gym | CyberGym |
| explo / exploit gym / explosion | ExploitGym |
| hacking face | Hugging Face |
| cloud mythos | Claude Mythos |
| agent be | AgentBeats |
| agents last exam | Agents' Last Exam |
| MOO | MOOC |
| Governor Nuomo | Governor Newsom |
| Demos | Demis Hassabis |
| aentic / a gentic / agent AI | agentic AI |
| chat h / chat GPT | ChatGPT |

## 待確認 / To Verify

- 「pacing the frontier」公開信的正式名稱、發起單位與連署人數(逐字稿只說 "over a thousand leading AI researchers")。/ Formal name, organizer and signatory count for the "pacing the frontier" open letter.
- 「Project Glasswing」(Song 在前一日 keynote 也提到,本場一併帶過)的正確名稱與出處。/ Correct name and source for "Project Glasswing", also mentioned in her Day 1 keynote.
- Berkeley RDI 黑客松累計獎金「約 $2 million in prizes and resources」的精確數字。/ Exact figure behind "around $2 million in prizes and resources".
- OpenAI / Hugging Face sandbox 逃逸事件的公開報告連結。/ Public report link for the OpenAI / Hugging Face sandbox-escape incident.
