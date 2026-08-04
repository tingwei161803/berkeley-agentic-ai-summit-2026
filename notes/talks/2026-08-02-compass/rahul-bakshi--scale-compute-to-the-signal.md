---
title: "Scale Compute to the Signal"
title_zh: "讓算力貼著訊號走"
speaker: "Rahul Bakshi"
affiliation: "Director, Applied Science (Edge AI), Amazon"
type: talk
stage: Compass
date: 2026-08-02
session: "Session 2: AI Systems"
video: "https://www.youtube.com/watch?v=1UrriPJRSPU&t=1385s"
video_range: "00:23:05–00:30:43"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [edge-ai, energy, silicon, function-calling, on-device]
---

# 讓算力貼著訊號走(Scale Compute to the Signal)

**一句話總結**:大家都在問「怎麼給 agent 更多算力」,但在邊緣裝置上算力有一道由**人體皮膚耐熱極限**畫出的硬天花板(約 1–1.5 W),所以真正該問的是「這個任務值不值得往上升級一層」——而現在缺的不是模型,是一個懂得按任務動態編排感測器、無線電與算力預算的 composable runtime。

**One-line summary**: Everyone asks how to give agents more compute, but at the edge there is a hard ceiling drawn by human skin's heat tolerance — roughly 1–1.5 W — so the real question is whether a task earns an escalation to the next tier; and what's missing isn't a model, it's a composable runtime that budgets sensors, radio, and compute per task.

## 中文筆記

### TL;DR

- **算力天花板是生理性的,不是工程性的**:穿戴式裝置只有大約 1–1.5 W 可用,因為人體皮膚超過 43°C 就會開始灼傷與不適。這道牆不會因為多蓋幾座 gigafactory 而移動,而**邊緣與雲之間的這種不對稱,正是下一代混合架構最肥沃的創新土壤**。
- **三層功耗階梯,原則只有一句:非必要不升級**。第一層在訊號源頭處理(wake word 偵測、event camera),耗能極小;第二層在裝置上跑演算法或 tool calling,功耗差幾個數量級;第三層才動用資料中心級算力,又差幾個數量級。而且往上升級不只貴在算力——**無線電的成本十年來幾乎沒跟著傳輸成本一起下降**。
- **三個 call to action**:(1) 業界缺的是 **composable runtime**,能判斷「這個任務不需要開相機和麥克風,只要開無線電做一次 API 呼叫」,並據此配置功耗預算;(2) benchmark 應該把 **joules per task** 納入指標,而不只是參數量與準確率;(3) 晶片開發者請把 **resting power** 再往下壓。

### 重點整理

#### 把問題反過來問:如果沒有更多算力可給呢?(約 00:23:05–00:26:20)

Rahul Bakshi 帶領 Amazon 的 applied science 團隊,負責自研晶片——最新一代的 **AZ3** 就是去年秋天發表的 Echo 裝置所搭載的矽晶片。他的日常因此都圍繞著 edge compute、edge device 與 edge-scale processing。

過去幾年的主流問題是「怎麼給 agent 更多算力」,這問題很重要,因為算力解鎖新能力。但他當場把問題翻面:**如果因為物理限制,根本沒有更多算力可以給呢?** 另一個主軸是:很多邊緣 agent **根本不需要 frontier 等級的智能**,在嚴格定義的功耗預算下,反而有很多有趣的最佳化空間可做。

擴張算力的一條路當然是蓋更多資料中心——Amazon、其他 hyperscaler、neocloud 都在蓋 gigafactory,這是一個槓桿。但另一端有一道**真實的功耗天花板**。他用穿戴式裝置當最極端的例子,因為那裡的限制最硬:智慧手錶、智慧眼鏡、戒指這類裝置,通常只有大約 **1 到 1.5 W** 可用。

而理由是生物性的:**人體皮膚無法承受超過 43°C 的熱,再上去就開始灼傷、極不舒服**(約 00:25:51)。這就是邊緣側的硬天花板。他認為,**邊緣與雲之間的這種不對稱,正是下一代混合架構的沃土**。

#### 三層功耗階梯與「非必要不升級」(約 00:26:20–00:29:00)

接受這道天花板之後,邊緣裝置上執行的東西大致落在三層功耗剖面:

1. **最省的一層:在訊號源頭處理訊號**。微型 wake word 偵測器、event camera 都屬於這層——在來源處偵測,燒最少的能量。
2. **中間層:拿這個訊號做什麼**。要跑演算法、或跑 tool calling 工作流,就進入下一級能耗;仍在裝置上,但算力與功耗**高出好幾個數量級**。
3. **最貴的一層:資料中心級算力**。當任務需要裝置上沒有的 context,或需要 world knowledge,才呼叫這一層,又**再高幾個數量級**。

結論一句話:**escalate only when the task calls for it**(約 00:27:20)。

接著他用兩個獨立的資料點導向同一個結論(約 00:27:35):

- 今年稍早,Berkeley 的 **function calling leaderboard**(BFCL)顯示,**一個小語言模型在 function calling 任務上已經追平 frontier 等級的表現**。這個 benchmark 追蹤的是 function calling 的基本功——產出的 JSON 有沒有正確的 function、API 與參數。重點不在於小模型全面追上,而在於:**對範圍夠小、定義夠明確的任務集合,我們已經有辦法把 frontier 等級的智能放到邊緣裝置上。**
- 另一個數字更違反直覺(約 00:28:37):過去十年,無線網路**傳輸一個位元的成本**已經下降好幾倍;但**無線電本身的成本並沒有等比例下降**。所以往上升級一層,在能耗與電池續航上都是昂貴的決定,非必要不該做。

#### 三個 call to action(約 00:29:00–00:30:40)

級聯式的分層架構本身早就成熟——Amazon、Apple、Meta 的助理十幾年來都是「偵測 wake word,必要時才逐級往上升」。**真正缺的是 composable runtime**(約 00:29:22),這是他給現場的第一個 call to action。

他舉的例子很具體:當你問助理「我的班機幾點?誤點了嗎?」——如果 runtime 有足夠的智能知道,**做這件事根本不需要開啟任何感知感測器(相機、麥克風),只需要開無線電做一次 API 呼叫**,那就可以據此編出一份功耗預算,並給 function calling 一個對應的動態排程。

第二個 call to action 給 benchmark 社群(約 00:30:16):Berkeley 已經有 function calling benchmark,**應該擴充成也涵蓋 joules per task,而不只是參數量與準確率**——能耗也是一個重要的前沿。

第三個給在場的晶片開發者(約 00:30:33):**請把 resting power 再往下壓**,這樣我們才能為邊緣做出更有效率的 agent。

### 金句

> "What if there wasn't more compute to give to our agents because of physics limitations?"(約 00:23:45)

整場演講的翻轉點:算力不是無限供給的參數。

> "Human skin cannot tolerate more than 43 degrees centigrade of heat without starting getting burned."(約 00:25:51)

穿戴式裝置的功耗天花板不是工程妥協,是生理常數。

> "The takeaway is escalate only when the task calls for it."(約 00:27:20)

一句話的邊緣 agent 設計準則。

> "What is missing is a composable runtime."(約 00:29:22)

模型已經夠好了,缺的是會編排感測器、無線電與算力預算的那一層。

## English Notes

### TL;DR

- **The compute ceiling at the edge is biological, not engineering.** Wearables have roughly 1–1.5 W to work with because human skin starts burning past 43°C. No number of gigafactories moves that wall — and **the resulting edge/cloud asymmetry is the fertile ground for next-generation hybrid architectures**.
- **Three power tiers, one rule: escalate only when the task calls for it.** Tier one processes signals where they originate (wake-word detectors, event cameras) at minimal energy; tier two runs algorithms or tool-calling workflows on-device at orders of magnitude more power; tier three invokes data-center-class compute at orders of magnitude beyond that. Escalation isn't just compute-expensive — **the cost of the radio has not fallen anywhere near as fast as the cost of transporting a bit**.
- **Three calls to action**: (1) the industry needs a **composable runtime** that can reason "this task needs no camera or microphone, just the radio and one API call" and budget power accordingly; (2) benchmarks should measure **joules per task**, not only parameter count and accuracy; (3) silicon developers should keep pushing **resting power** down.

### Key Points

#### Inverting the question: what if there is no more compute to give? (~00:23:05–00:26:20)

Rahul Bakshi leads an applied science team at Amazon responsible for custom silicon — the latest generation, **AZ3**, powers the Echo devices launched last fall. His days are consequently spent on edge compute, edge devices, and edge-scale processing.

The dominant question for the last few years has been how to give agents more compute, and it's a good question because compute unlocks capability. But he flipped it on stage: **what if, because of physics, there simply isn't more compute to give?** His second theme: a great many edge agents **don't need frontier-level intelligence at all**, and working inside a tightly defined power budget opens up genuinely interesting optimizations.

One lever for more compute is more data centers — Amazon, the other hyperscalers, and the neoclouds are all building gigafactories. But at the other end sits a **real power ceiling**. He used wearables as the extreme case because the constraints there are hardest: a smartwatch, smart glasses, or a ring typically has about **1 to 1.5 watts** to work with.

The reason is biological: **human skin cannot tolerate more than 43°C without starting to burn and becoming deeply uncomfortable** (~00:25:51). That is the hard edge-side ceiling — and, in his framing, **the asymmetry between edge and cloud is exactly where next-generation hybrid architectures will be invented**.

#### Three power tiers and the escalation rule (~00:26:20–00:29:00)

Accept the ceiling and what runs on edge-scale devices sorts into three power profiles:

1. **Most efficient: process the signal where it originates.** Tiny wake-word detectors and event cameras live here — detect at the source, burn minimal energy.
2. **Next: decide what to do with that signal.** Running algorithms or tool-calling workflows still happens on-device but costs orders of magnitude more compute and power.
3. **Most expensive: data-center-class compute**, invoked when the task needs context that isn't on the device or requires world knowledge — orders of magnitude beyond tier two again.

The rule that falls out: **escalate only when the task calls for it** (~00:27:20).

He then offered two independent data points that land on the same conclusion (~00:27:35):

- Earlier this year, Berkeley's **function calling leaderboard** (BFCL) showed **a small language model matching frontier-level performance on the function-calling task**. The benchmark tracks the primitives — does the generated JSON carry the right functions, the right APIs, the right parameters? The point is not that small models have caught up generally, but that **for small, well-defined task sets there is now a pathway to frontier-level intelligence at edge scale**.
- The second data point is the counterintuitive one (~00:28:37): over the last decade the cost of transporting a single bit across wireless networks has fallen many-fold, but **the cost of the radio has not fallen by anything like the same factor**. Escalating to the next tier is expensive in both energy and battery life, and should happen only when necessary.

#### Three calls to action (~00:29:00–00:30:40)

The cascaded tier architecture itself is well established — Amazon's, Apple's, and Meta's assistants have detected wake words and escalated only when necessary for more than a decade. **What's missing is a composable runtime** (~00:29:22), and that was his first ask of the room.

His example was concrete: you ask your assistant "hey, what time's my flight, is it late?" If the runtime were smart enough to know that **this activity requires no perception sensors at all — no camera, no microphone, just the radio and one API call** — then a power budget could be constructed for it and function calling could be given a corresponding dynamic schedule.

The second ask went to the benchmarking community (~00:30:16): Berkeley already has the function-calling benchmark, and there's an opportunity to extend it to include **joules per task**, not just parameter counts and accuracy. Energy is a frontier too.

The third went to the silicon developers in the audience (~00:30:33): **push the frontier on lowering resting power** so more efficient edge agents become buildable.

### Quotes

> "What if there wasn't more compute to give to our agents because of physics limitations?" (~00:23:45)

The talk's pivot: compute is not an unbounded input.

> "Human skin cannot tolerate more than 43 degrees centigrade of heat without starting getting burned." (~00:25:51)

The wearable power ceiling isn't an engineering compromise; it's a physiological constant.

> "The takeaway is escalate only when the task calls for it." (~00:27:20)

Edge agent design in one sentence.

> "What is missing is a composable runtime." (~00:29:22)

The models are good enough; the missing layer is the one that budgets sensors, radio, and compute.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| AZ3 (Amazon) | Amazon 自研的邊緣 AI 晶片,搭載於 2025 秋季發表的 Echo 裝置 | Amazon's custom edge AI silicon, shipping in the Echo devices launched in autumn 2025 | 已查證:AZ3 / AZ3 Pro,2025 年 9 月底發表 |
| Berkeley Function Calling Leaderboard (BFCL) | 追蹤模型 function calling 能力(function / API / 參數是否正確)的排行榜 | Leaderboard tracking function-calling ability — correct functions, APIs, and parameters in the generated JSON | 演講建議擴充加入 joules per task |
| Composable runtime | 講者提出的 call to action:能按任務動態決定該開哪些感測器與功耗預算的執行層 | His call to action: a runtime that decides per task which sensors to power and what energy budget to allocate | 尚無既有實作,屬倡議 / an ask, not an existing system |
| Event camera | 第一層功耗階梯的代表性感測器之一 | Example sensor at the lowest power tier | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Roel Bakshi / Rahu | Rahul Bakshi |
| a3 | AZ3 |
| variable technology / variable computer | wearable technology / wearable computer |
| jewels per task | joules per task |
| next year(在 "escalation to the next year is expensive" 中) | next tier |
| gigafactories | (原文如此,指大型 AI 資料中心) |

## 待確認 / To Verify

- BFCL 上追平 frontier 表現的具體小模型名稱與數據:講者只說 "a small language model",未點名。/ The specific small language model that matched frontier performance on BFCL — he only said "a small language model."
- 「無線電成本未同步下降」那張圖表的資料來源與時間區間。/ Source and time range for the chart on radio cost versus bit-transport cost.
- 演講中提到的 AZ3 具體算力/功耗規格未在逐字稿出現,需看投影片。/ AZ3's specific compute/power figures never appear in the transcript; check the slides.
