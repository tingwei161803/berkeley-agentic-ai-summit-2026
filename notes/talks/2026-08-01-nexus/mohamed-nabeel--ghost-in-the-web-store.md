---
title: "Ghost in the Web Store: Preempting LLM-Hallucinated Browser Extension Supply Chain Attacks"
title_zh: "Web Store 裡的幽靈:先攻擊者一步堵住 LLM 幻覺型瀏覽器擴充套件供應鏈攻擊"
speaker: "Mohamed Nabeel"
affiliation: "Senior Principal Researcher, Palo Alto Networks"
type: talk
stage: Nexus
date: 2026-08-01
session: "Session 4: Secure Agentic AI"
video: "https://www.youtube.com/watch?v=ZIRc3EpzQJs&t=13090s"
video_range: "03:38:10–03:45:00"
transcript: "tmp/[English (auto-generated)] Nexus Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [security, hallucination, supply-chain, browser-extensions, web-security]
---

# Web Store 裡的幽靈(Ghost in the Web Store)

**一句話總結**:LLM 會「有自信地」推薦根本不存在、已下架或無人認領的瀏覽器擴充套件,攻擊者只要把這些幻覺名稱註冊回來,就能不必入侵任何系統、直接讓 AI 幫他們開門——他們的做法是**先去找這些幽靈**,在攻擊者把它們復活之前。
**One-line summary**: LLMs confidently recommend browser extensions that never existed, were deleted, or sit unclaimed — and an attacker who registers those hallucinated identifiers gets in without breaking anything. The research hunts those ghosts before attackers bring them back to life.

## 中文筆記

### TL;DR

- **威脅模型的重點是「誰在瀏覽網路」變了**:過去二十年的 web 防護是為「人類瀏覽網路」設計的;現在要問的是**如何建一個保護 agent 的 web**,保護了 agent 就等於保護了人。
- **幻覺在供應鏈上不是假設性問題**:已有研究顯示 PyPI / npm 套件名稱會被幻覺;講者團隊近期也做了**幻覺網域名稱**的研究。而瀏覽器擴充套件更危險——權限過大、看得到你的 session token 與 cookie,一旦被攻陷,攻擊者就有你作業系統的第一排座位。
- **三個「幻覺高發區」(hallucination-prone zones)**:(1) **時效性**——現在每個月新增約 2 萬個擴充套件,過去是一整年才這麼多,而 LLM 不擅長偵測新近變化;(2) **已刪除的東西**——同時期也有數千個擴充套件被下架,但 LLM 是 **snapshot learner**,以為它們還在;(3) **無品牌的擴充套件**——沒有品牌訊號的擴充套件特別容易被編造。
- **實測結果**:LLM 推薦的一批擴充套件是**真實存在但已被下架**的,其中不少已被標記為惡意軟體;另一批則是**無人認領**的識別碼,LLM 依然自信地叫你安裝。他們持續監控高幻覺率的擴充套件,研究之後觀察到**約十來個**被註冊並用於惡意活動。
- **可帶走的一句話**:幻覺是 LLM 的固有性質,不會消失;不要盲信瀏覽器或 chatbot 給的推薦,一定要查證。

### 重點整理

#### 開場:從「保護人瀏覽網路」到「建一個保護 agent 的 web」(約 03:38–03:39)

講者在 Palo Alto Networks 做 web security。他的切入點很簡潔:過去這些年,web 防護是為「人類在瀏覽網路」建立的;隨著 LLM 與 agent 大量普及,現在瀏覽網路的不再是人。所以團隊近期在想的是——**怎麼建一個會保護 agent 的 web**,而保護 agent 反過來就是保護人。

本場聚焦其中一塊:**幻覺**,而且是**瀏覽器擴充套件上的幻覺**。理由是「瀏覽器就是新的作業系統」,理解這個攻擊面很重要。

他也點出研究缺口:現有關於幻覺的研究、甚至 benchmark,主要衡量的是**摘要任務**上的幻覺,而不是供應鏈安全或相關產出物上的幻覺。

#### 一個關於火星日落的插曲(約 03:40–03:41)

他女兒問他:如果站在火星上看天空,日落是什麼顏色?他不想讓她失望,就去問了自己最愛的 chatbot,得到一段關於紅色日落、寫得非常漂亮的描述。他轉述給女兒,她很開心——但**答案是錯的,火星的日落是藍色的**。

原因是 LLM 把地球的經驗一般化到火星,又抓住「火星天空是紅的」這個事實推導出紅色日落;真正的物理是紅光波長較長、難以穿過大氣粒子,而藍光波長較短——連火星車拍回來的照片都是藍色日落。從此他學會凡事再確認一次。

#### 為什麼是瀏覽器擴充套件(約 03:42–03:43)

安全領域的幻覺不是假設性問題:已有研究顯示 **PyPI 與 npm 的套件名稱**會被幻覺,講者團隊近期也做了**幻覺網域名稱**的研究。而擴充套件之所以特別危險:

- **權限過大**;
- **看得到你的 session token 與 cookie**;
- 一旦有任何一個被攻陷,攻擊者就等於拿到通往你作業系統的第一排座位。

而攻擊手法「簡單得令人不安」:攻擊者不需要突破你的系統,只需要**騙過 AI**,讓 AI 幫他從正門走進來。

#### 三個幻覺高發區與實測結果(約 03:43–03:44)

問題根源在 LLM 的運作方式本身。他歸納出三個 **hallucination-prone zones**:

1. **時效性(recency)**:因為 AI 的緣故,擴充套件正在暴增——現在**每個月約 2 萬個**新擴充套件,而過去是一整年才產生這個數量。LLM 不擅長偵測新近變化,於是傾向「幻覺+盡量幫忙」。
2. **刪除(deletion)**:同一時間也有**數千個**擴充套件被刪除。LLM 是 **snapshot learner**,對「已被刪除」沒有概念,會以為它們還在。
3. **無品牌(no brand)**:並非所有擴充套件都有品牌訊號,這也會誘發幻覺。

實測發現分成兩類:

- 一類是 LLM 幻覺出來的擴充套件其實**真實存在過但已被刪除**,而且其中許多在瀏覽器商店裡**被標記為惡意軟體**。
- 另一類是**無人認領**的識別碼,LLM 仍自信地告訴你可以安裝——攻擊者可以直接利用。

最後一張投影片是他們**持續監控**的高幻覺率擴充套件清單:他們持續重新評分、追蹤;在研究之後,他們看到**約十來個**這類擴充套件被註冊並用於惡意活動。

#### 結論(約 03:44)

不要盲信瀏覽器(或 chatbot)給你的推薦,永遠再確認一次——因為**幻覺是 LLM 的固有性質,不會消失**。

### 金句

> "Attackers don't need to break into your system. They just need to trick the AI to get through your front door."(約 03:42:47)

整場最精煉的威脅模型:供應鏈攻擊的入口從「漏洞」變成「幻覺」。

> "LLMs are snapshot learners. They don't have an understanding of deleted extensions. They think they are already still existing."(約 03:43:30)

「已刪除」這個概念在訓練快照裡不存在——這正是幽靈的來源。

## English Notes

### TL;DR

- **The threat model changed because the browsing population changed.** Two decades of web defenses were built for humans browsing the web. The question now is how to build a web that protects *agents* — which in turn protects the humans behind them.
- **Supply-chain hallucination is not hypothetical**: prior work shows LLMs hallucinate PyPI and npm package names, and his team recently published research on hallucinated domain names. Extensions are worse: excessive permissions, visibility into session tokens and cookies, and a front-row seat to your operating system if compromised.
- **Three hallucination-prone zones**: (1) **recency** — roughly 20,000 new extensions per month now, versus that many per *year* previously, and LLMs are poor at recency; (2) **deletion** — thousands are removed in the same period, but LLMs are **snapshot learners** with no concept of deletion; (3) **brand-less extensions**, which lack the signal that anchors a model.
- **Findings**: one set of hallucinated extensions turned out to be real but deleted, many of them flagged as malware; another set were unclaimed identifiers the LLM still confidently told users to install. Monitoring the highest-hallucination extensions, they saw **about a dozen** subsequently registered and used for malicious activity.
- **Takeaway**: hallucination is inherent to LLMs and will not go away — never blindly trust a browser or chatbot recommendation.

### Key Points

#### From protecting human browsing to building a web that protects agents (~03:38–03:39)

He works in web security at Palo Alto Networks, and framed the shift plainly: the protections built over the years assumed humans were the ones browsing. With LLMs and agents proliferating, that's no longer true — so the team has been thinking about how to build a web that protects agents, which by extension protects humans.

This talk narrowed to hallucinations, specifically hallucinations about **browser extensions**, on the premise that the browser is the new operating system, which makes it an attack surface worth understanding precisely. He also noted a gap in the literature: existing hallucination research and benchmarks mostly measure hallucination in **summarization**, not in supply-chain security artifacts.

#### An aside about sunsets on Mars (~03:40–03:41)

His young daughter asked what color the sunset would be if she stood on Mars. Not wanting to disappoint her, he asked his favorite chatbot, which described a red sunset beautifully. She was delighted with the answer — which was wrong. Martian sunsets are **blue**.

The model generalized from Earth and leaned on the fact that the Martian sky is red. The actual physics runs the other way: red has the longer wavelength and scatters out, blue the shorter one — and the rover photos show blue sunsets. Ever since, he double-checks answers.

#### Why browser extensions (~03:42–03:43)

Hallucination in security is already documented — hallucinated PyPI and npm package names, and his own team's recent research on hallucinated domain names. Extensions raise the stakes because they hold excessive permissions, see your session tokens and cookies, and hand a compromise attacker a front-row seat to your operating system.

The attack itself is, in his word, deceptively simple: attackers don't need to break into your system, they just need to trick the AI into walking them through the front door.

#### Three hallucination-prone zones, and what they found (~03:43–03:44)

The problem arises from how LLMs work. He named three zones where they perform badly:

1. **Recency.** AI has driven an extension boom — roughly 20,000 new extensions *per month*, where previously that many appeared over a whole year. LLMs are bad at recency detection, so they hallucinate while trying to be helpful.
2. **Deletion.** Thousands of extensions are deleted over the same period, but LLMs are snapshot learners with no representation of deletion — they think the deleted ones still exist.
3. **No brand.** Not every extension has a brand, and the absence of that signal invites hallucination.

Two categories of finding:

- Extensions the LLM hallucinated that were **real but deleted**, many of them marked as malware in the store.
- **Unclaimed** extensions the LLM nonetheless confidently told users to install — directly exploitable by attackers.

His closing slide showed the set they keep monitoring and rescoring. After the study, about a dozen of these highly-hallucinated extensions were registered and used for malicious activity.

#### Conclusion (~03:44)

Don't blindly trust recommendations from your browser or chatbot. Always fact-check, because hallucination is inherent to LLMs and won't go away.

### Quotes

> "Attackers don't need to break into your system. They just need to trick the AI to get through your front door." (~03:42:47)

The whole threat model in one line: the supply-chain entry point moved from vulnerabilities to hallucinations.

> "LLMs are snapshot learners. They don't have an understanding of deleted extensions. They think they are already still existing." (~03:43:30)

"Deleted" is a concept that doesn't exist inside a training snapshot — which is exactly where the ghosts come from.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| 幻覺網域名稱研究 / Hallucinated domain research | 講者團隊近期關於 LLM 幻覺網域被攻擊者註冊的研究 | His team's recent research on attackers registering LLM-hallucinated domains | 對應 Unit 42 2026 年 "Phantom Squatting: AI-Hallucinated Domains as a Software Supply Chain Vector" |
| PyPI / npm 幻覺套件研究 | 既有研究顯示 LLM 會幻覺出不存在的套件名稱 | Prior work showing LLMs hallucinate nonexistent package names | 講者引用為先例,未指名論文 / cited as precedent, paper not named |
| 高幻覺擴充套件監控清單 / Hallucinated extension watchlist | 團隊持續重新評分與監控的擴充套件集合 | Set of extensions the team continuously rescores and monitors | 研究後約十來個被註冊並用於惡意活動 / ~a dozen later registered for malicious use |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Muhammad Nabil | Mohamed Nabeel |
| PA Alter Network / PaloAlto Network | Palo Alto Networks |
| junk professor | adjunct professor |
| pi and npm packages | PyPI and npm packages |
| mass / Martian(指行星時) | Mars |
| rob ran on mass | rover on Mars |
| eicric | (聽不清,推測為 electric/lyric 類形容詞;語意為「文采斐然的描述」) |
| browse extensions | browser extensions |

## 待確認 / To Verify

- 主持人介紹時提到他同時是「adjunct professor at National University in San Diego」;官網議程只列 Palo Alto Networks 職稱,兼職教職資訊建議另行核實後再寫入。/ The MC also introduced him as an adjunct professor at National University (San Diego); the official agenda lists only the Palo Alto Networks title.
- 「每月約 20,000 個新擴充套件」與「數千個被刪除」的資料來源與統計區間未說明。/ The ~20,000 new extensions per month and "thousands deleted" figures were given without a source or time window.
- 研究後被註冊並用於惡意活動的擴充套件「約一打」的確切數字與案例。/ The exact count and cases behind "about a dozen" extensions registered for malicious use.
- 議程標題為 "Ghost in the Web Store";對應論文或 Unit 42 報告是否已公開發表、連結為何。/ Whether the "Ghost in the Web Store" work has a published paper or Unit 42 write-up, and its link.
