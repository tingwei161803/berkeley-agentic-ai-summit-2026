---
title: "Computer-Use Models Will Agentify the Web, Not APIs"
title_zh: "會把 web agent 化的是 computer-use 模型,不是 API"
speaker: "Dhruv Batra"
affiliation: "Chief Scientist / Co-founder, Yutori"
type: talk
stage: Nexus
date: 2026-08-01
session: "Session 2: Coding & Web Agents"
video: "https://www.youtube.com/watch?v=ZIRc3EpzQJs&t=1695s"
video_range: "00:28:15–00:40:41"
transcript: "tmp/[English (auto-generated)] Nexus Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [computer-use, web-agents, vision, long-tail, benchmarks]
---

# 會把 web agent 化的是 computer-use 模型,不是 API(Computer-Use Models Will Agentify the Web, Not APIs)

**一句話總結**:「agent 會成為 web 上主要的行動者、web 會被 agent 化」這兩步是對的,但「靠 API 來達成」這一步是錯的——因為 web 的長尾是為人眼建造的,只有看像素、按按鈕的 computer-use 模型才進得去。
**One-line summary**: The popular narrative gets two steps right — agents will drive most action on the web, and the web will be agentified — but the third step is wrong: it won't happen through APIs, because the long tail of the web was built for human eyeballs, and only vision-based computer-use models can reach it.

## 中文筆記

### TL;DR

- **他要駁的是三段論的第三步**:(1) agent 會取代人成為 web 上的主要行動者 ✓;(2) web 會被「agent 化」✓;(3) 靠 MCP / web MCP / 支付協定等十幾種標準的 API ✗。
- **長尾網站不會有 API**:餐廳菜單的現實是純文字(easy)、PDF(medium)、到一疊沒 OCR 的像素化掃描圖(hard)。光是歐洲某一國就有約 20 萬名自建網站的小店主——「我們在等的援軍不會來」。
- **「叫 coding agent 讀 HTML」也不成立**:電商庫存狀態根本不在 HTML 裡,而在載入時取回的 JSON,再由另一段程式決定選項要不要變灰。**瀏覽器本質上是 renderer**,像素才是 source of truth。
- **Navigator**:Yutori 的 pixels-to-actions 模型,輸入螢幕截圖、輸出人類式動作;但不受限於人類方式——它有 execute JavaScript 動作,可一次填完整張表單。
- **computer use 沒有停滯**:Ohio State 學術團隊維護的 benchmark 已被推到約 97%、基本飽和,需要出新的;專用小模型在成本與速度上也已勝過前沿模型。

### 重點整理

#### 論證的靶子:三段論的第三步(約 00:29–00:30)

網路上流行的說法分三步:

1. AI agent 而非人類,將成為 web 上主要的行動驅動者——幫我們訂會議、訂位、買東西、取得資訊。
2. 問「怎麼做到」,答案是:web 會被 agent 化,會被改造成 agent 友善的樣子。
3. 再問「怎麼改造」,答案是:透過 API——我的 agent、你的 agent、企業的 agent 都經由十幾種標準來呼叫,MCP、web MCP、支付協定等等。

他的主張很明確:**前兩步是對的,第三步是錯的**。真正會把 web(尤其是**長尾**)agent 化的,是像人一樣看螢幕、按按鈕操作瀏覽器的 computer-use agent。

#### 為什麼訂機票的 demo 很荒謬(約 00:30–00:31)

這個領域最常見的 demo:使用者在 iPhone 上說「幫我找這班機」,背後一個 browser-use agent 打開 flights.google.com,像人一樣點按鈕。他說這**荒謬得好笑**——那明明就是個資料庫,有現成的聚合器 API 服務,送結構化查詢、拿結構化結果就好,何必去點按鈕?

換個問題才看得出差別:「我要辦一場晚間聚會,這家餐廳的菜單上有無麩質的選項嗎?」人們想像的是未來有 `myrestaurant.com/menu` 這種端點,可以直接 curl、用自然語言查詢或篩選出 gluten-free 品項。

#### 長尾的真實樣貌(約 00:32–00:33)

他實際展示三種難度的餐廳網站:

- **Easy**:菜單是可讀的文字。
- **Medium**:菜單是 PDF。
- **Hard**:菜單是一疊各自獨立掃描的頁面圖片,拼在一起、像素化、**連 OCR 都沒做**。

而網站背後是真實的人——光是歐洲某一個國家,就有約 **20 萬名**自己維護網站的小店主。「你想像的是,明天或未來五年內他們會全部革新,為你的 agent 開好閘道。」他的判斷是:**不會發生**。web 極度長尾,單一小網站價值有限,但整條尾巴累積起來價值巨大;而基礎設施改變得很慢。

#### 為什麼「讓 agent 讀 HTML」也不行:osmium cube 的例子(約 00:33–00:35)

常見的反駁是:「那我們有 coding agent,直接讀 HTML 就好。」他用一個電商頁面反駁:問「這個 24mm 鋨立方體是否有貨?」

- 人眼看下拉選單,可以看到四個選項中有三個是 sold out、一個可買。
- 但 agent 去讀 HTML,選單只有品項描述,**完全沒有數量資訊**。
- 真相是:頁面載入時另有一個查詢回傳 JSON 字典,裡面才是當下的庫存與數量;點開下拉時,另一段程式碼決定該選項要顯示成灰色還是彩色。

結論用遊戲工程的類比講得最清楚:**瀏覽器本質上是一個 rendering engine**——底下有 assets、有 code,最終產出的是像素。**web 是為人眼建造的,像素才是 source of truth,所以機器必須用視覺來操作。** Yutori 為此寫了一篇 blog:《The Bitter Lesson for Web Agents》——如果你不看像素,你就會卡在無止盡的 feature engineering 上,永遠搆不到長尾。

> 現場插曲:一個彈窗蓋掉了他半張投影片,他一邊等工作人員處理一邊說:「API 不會來,但我的 computer-use agent 會來,而且它會做得比這更好。」

#### Navigator:pixels-to-actions(約 00:37–00:38)

Yutori 訓練的模型叫 **Navigator**:輸入是瀏覽器截圖,輸出是人類式動作(click、type、scroll)。

- 應用範例:「我有一組促銷碼,它到底能不能用?」——這種事**永遠不會有 API**,商店後台不可能開這個介面。Navigator 會開瀏覽器、走一遍模擬結帳流程、套用促銷碼、比對價格是否下降,然後回傳結構化物件:是的,可用,價格降了 22%。**這才是 web 的 API。**
- **要用視覺,但不必被人類的方式綁住**:模型有一個 `execute JavaScript` 動作,可以直接讀寫 JavaScript。在表單填寫任務上,它會自己寫程式一次填完多個欄位,而不是一格一格點。

#### 反駁「computer use 卡住了」與「太慢太貴」(約 00:38–00:40)

網路上有一種說法:coding agent 一直在進步,computer use 卻停滯了。他說事實不是這樣——**benchmark 一個接一個倒下**。他舉了一個由 Ohio State 學術團隊維護的 benchmark:過去兩年基本已被推到飽和,大約一個月前準確率已達 **97%**,得再造新的了。

至於慢與貴:如果你用**前沿通用模型**,確實如此。他對比 Opus 4.7 與 GPT-5.5——GPT-5.5 每個動作大約要 10 秒,某個資料集上跑完整個任務要花到 230 美元。而 Yutori 訓練的專用模型小得多,準確度相當、速度更快、也便宜得多。

**結語**:我們有 30 年的 web 是為人類消費而建造的,這正在改變,但「怎麼改」很重要。那個「任意網站都能拉、任意任務都能用自然語言描述」的 web API,將會由**背景中一大群操作瀏覽器的 agent**構成。

### 金句

> "The cavalry that we're waiting for is not coming."(約 00:33)

指望長尾網站都長出 agent 友善的 API,是在等一支不會抵達的援軍。

> "A browser really is a renderer. … The web was built for human eyeballs. That is the source of truth. And so machines will need to operate with vision."(約 00:35)

整場演講的核心一句。

> "APIs are not arriving, but my computer-use agent is arriving. It'll do a better job than this."(約 00:36)

投影片被彈窗蓋住時的即興回應,也剛好是他論點的現場演示。

## English Notes

### TL;DR

- **The target is step three of a syllogism**: (1) agents, not humans, will drive most action on the web ✓; (2) the web will be "agentified" ✓; (3) via APIs across a dozen-plus standards — MCP, web MCP, payment protocols ✗.
- **The long tail will never have APIs**: real restaurant menus are plain text (easy), PDFs (medium), or a gallery of pixelated, un-OCR'd page scans (hard). Roughly 200,000 small business owners in a single European country maintain their own sites. "The cavalry we're waiting for is not coming."
- **"Just have a coding agent read the HTML" also fails**: e-commerce stock state isn't in the HTML at all — it arrives as a JSON blob at page load, and separate code decides whether an option renders greyed out. **A browser is a renderer**; pixels are the source of truth.
- **Navigator**: Yutori's pixels-to-actions model takes a screenshot and emits human-like actions — but isn't limited to human methods, since it has an execute-JavaScript action that can fill an entire form at once.
- **Computer use is not stuck**: an academic benchmark from Ohio State is essentially saturated at ~97%, and specialized small models already beat frontier models on cost and speed.

### Key Points

#### The argument being attacked (~00:29–00:30)

The popular online narrative goes in three steps: (1) AI agents rather than humans will be the primary drivers of action on the web — booking meetings and appointments, buying things, retrieving information. (2) Asked how, people say the web will be agentified, made agent-friendly. (3) Asked how *that* happens, the answer is APIs — your agents, my agents, and enterprise agents calling through fourteen different standards: MCP, web MCP, payment protocols, and so on.

His claim: **the first two steps are right, the third is wrong.** What will actually agentify the web — specifically its **long tail** — are computer-use agents that operate browsers like a human, by looking at the screen and pressing buttons.

#### Why the flight-booking demo is absurd (~00:30–00:31)

The canonical demo in this literature: a user asks their iPhone to find a flight, and behind the scenes a browser-use agent opens flights.google.com and clicks buttons like a human. He calls it **ludicrously funny** — that's a database with aggregator API services already available. Send a structured query, get a structured result. Why would you click buttons?

The generalized question exposes the difference: "I'm planning an evening gathering with friends — are there any gluten-free items on this restaurant's menu?" People imagine a future `myrestaurant.com/menu` endpoint you can curl and filter with a natural-language query.

#### What the long tail actually looks like (~00:32–00:33)

He showed three difficulty tiers of real restaurant websites: **easy** — readable text; **medium** — menus as PDFs; **hard** — a gallery of individually scanned menu pages stitched together, pixelated, **not even OCR'd**.

Behind those sites are real people: roughly **200,000** small business owners maintaining their own websites in a single European country. "What you are imagining is that tomorrow, or in the next five years, they will all be revolutionized so that there are gateways for your agents to pull." His verdict: it isn't coming. The web is extremely long-tailed — individual sites may be of limited value, but the tail cumulatively carries enormous value, and infrastructure changes slowly.

#### Why reading the HTML doesn't work either: the osmium cube (~00:33–00:35)

The standard rebuttal is: fine, we have coding agents, just read the HTML. He counters with an e-commerce page and a trivial question — is this 24mm osmium cube in stock?

Scroll down to the quantity dropdown and human eyes can see three of the options are sold out and one is available. Send an agent to read the HTML and the selector carries descriptors for the items but **nothing about quantity**. Behind the scenes, a query on page load returns a JSON object listing what the store actually has, and a different piece of code decides at render time whether each dropdown option shows greyed out or in color.

The framing that makes it click comes from game engineering: **a browser really is a renderer** — assets underneath, code on top, pixels out the other end. **The web was built for human eyeballs; that is the source of truth; so machines will need to operate with vision.** Yutori wrote this up as a blog post, "The Bitter Lesson for Web Agents": if you don't look at the pixels, you get stuck feature-engineering your way toward a long tail you'll never reach.

> Live mishap: a popup covered half his slides. While waiting for it to be cleared, he ad-libbed: "APIs are not arriving, but my computer-use agent is arriving. It'll do a better job than this."

#### Navigator: pixels to actions (~00:37–00:38)

Yutori's model is called **Navigator**: input a screenshot of the browser, output a human-like action — clicking, typing, scrolling.

- Example task: "I have a promo code — does it work?" There is **no API for that**, and the store back office will never expose one. Navigator opens the browser, walks a mock checkout flow, applies the code, checks whether the price dropped, and returns a structured object: yes, it works, and the price went down 22%. **That is your API of the web.**
- **Vision-based, but not human-limited**: the model has an `execute JavaScript` action. On a form-filling task, it writes custom code and populates many fields simultaneously instead of clicking field by field.

#### Rebutting "computer use is stuck" and "it's slow and expensive" (~00:38–00:40)

There's a narrative that coding agents keep progressing while computer use has stalled. That's not what reality shows: **benchmarks keep falling**. He cited a benchmark run by an academic group at Ohio State, essentially saturated over the last couple of years — as of about a month before the talk, accuracies sit at **97%**, so new benchmarks will have to be created.

On speed and cost: yes, if you use a **frontier general model**. Comparing against Opus 4.7 and GPT-5.5, every action takes around 10 seconds with GPT-5.5, and a full task can run to $230 on some dataset. Yutori's specialized model is significantly smaller, just as accurate, faster, and much cheaper.

**Closing**: we've had 30 years of web built for human consumption, and that is changing — but the *how* matters. The universal web API, where you can pull any website and describe any task in natural language, will be delivered by a sea of agents driving browsers in the background.

### Quotes

> "The cavalry that we're waiting for is not coming." (~00:33)

Waiting for long-tail websites to sprout agent-friendly APIs is waiting for reinforcements that will never arrive.

> "A browser really is a renderer. … The web was built for human eyeballs. That is the source of truth. And so machines will need to operate with vision." (~00:35)

The thesis of the talk in one breath.

> "APIs are not arriving, but my computer-use agent is arriving. It'll do a better job than this." (~00:36)

Improvised when a popup blocked his slides — and an accidental live demo of his own argument.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Navigator | Yutori 的 pixels-to-actions computer-use 模型 | Yutori's pixels-to-actions computer-use model | 輸入截圖、輸出 click/type/scroll,另有 execute JavaScript 動作 |
| The Bitter Lesson for Web Agents | Yutori 的 blog 文章,主張視覺優於 DOM | Yutori blog post arguing vision generalizes better than DOM | 演講中明確提名 |
| MCP / web MCP / 支付協定 | 他要反駁的「API 派」代表標準 | The API-camp standards he argues against | 他形容為 "14 different standards" |
| Ohio State 的 web agent benchmark | 已近飽和(約 97%)的學術 benchmark | Near-saturated academic web-agent benchmark (~97%) | 講者未點名,推測為 OSU NLP 團隊的 Online-Mind2Web(待確認) |
| Opus 4.7 / GPT-5.5 | 用來對比延遲與成本的前沿模型 | Frontier models used as latency/cost baselines | 每動作約 10 秒、某資料集整任務至 $230 |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Duvatra / Duru Batra / Duv / Drew | Dhruv Batra |
| URI / Ytori / UTI / "we at UTI" | Yutori |
| GPD 5.5 | GPT-5.5 |
| identify the web | agentify the web |
| myfrest restaurant.commen | myrestaurant.com/menu(示意端點 / illustrative endpoint) |
| securing information | sourcing/retrieving information(語意推定 / inferred) |

## 待確認 / To Verify

- Ohio State 那個「已飽和至 97%」的 benchmark 名稱:講者未點名。OSU NLP 團隊的 **Online-Mind2Web**(300 個任務、136 個真實網站)最為吻合,但需看投影片確認。/ Name of the Ohio State benchmark saturated at 97% — the speaker didn't say it. OSU NLP's **Online-Mind2Web** is the closest match; confirm from slides.
- 「某資料集上每個任務 $230」的資料集名稱未提供。/ The dataset behind the "$230 per task" figure was not named.
- Opus 4.7 與 GPT-5.5 的版本號僅由字幕聽出,需投影片確認。/ Model versions "Opus 4.7" and "GPT-5.5" heard from captions only.
- 「歐洲某一國約 20 萬名自建網站小店主」的資料來源未提供。/ No source given for the ~200,000 self-maintained small-business websites figure.
- 促銷碼案例中的「價格降 22%」是舉例還是實測結果,講者說得含糊(原文 "or whatever")。/ Unclear whether the "22% price drop" was a real result or an illustrative number.
