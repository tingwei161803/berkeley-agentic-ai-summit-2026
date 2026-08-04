---
title: "Safety and Security of Agentic AI"
title_zh: "Agentic AI 的安全與資安"
speaker: "John A McDermid"
affiliation: "Director, Centre for Assuring Autonomy, Institute for Safe Autonomy, University of York"
type: talk
stage: Nexus
date: 2026-08-01
session: "Session 4: Secure Agentic AI"
video: "https://www.youtube.com/watch?v=ZIRc3EpzQJs&t=12350s"
video_range: "03:25:50–03:37:55"
transcript: "tmp/[English (auto-generated)] Nexus Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [safety, security, cyber-physical-systems, causal-models, maritime]
---

# Agentic AI 的安全與資安(Safety and Security of Agentic AI)

**一句話總結**:在 cyber-physical 系統裡,safety 與 security 傳統上被分開評估,但 agentic AI 讓攻擊面同時擴張到訓練管線與**物理環境**;用 structural causal world model 把兩者接起來後會發現——單獨都安全的兩個攻擊,只要**改變發生順序**就能組合成致命結果。
**One-line summary**: Safety and security have traditionally been assessed in isolation, but agentic AI in cyber-physical systems expands the attack surface into training pipelines *and* the physical world; modeling both in a structural causal world model reveals that two attacks that are individually survivable become lethal when their time ordering changes.

## 中文筆記

### TL;DR

- **Safety ≠ Security,但不能再分開做**:講者做了 40 年軟體密集系統的 safety(定義是「對人、環境的物理傷害」),他的訊息很直接——資安圈與安全圈必須坐下來談,否則會部署出在物理世界造成災難的系統。
- **AI 把攻擊面往兩個方向撐開**:一邊是訓練管線、prompt、context 等傳統 IT 面向;另一邊是**物理環境本身**——貼紙貼在停止標誌上就能讓感知模型讀成「速限 45 mph」(實驗室 93%、真實世界 83%)。
- **SCWM(structural causal world model)**:四層結構——ontology(世界中重要的事物,如浪高)→ 不確定性建模 → 不確定性邊界 → 底層可用形式化方法驗證演算法行為。攻擊被建模成**對因果圖的 intervention**,再沿圖傳播到 safety metric。
- **複合攻擊案例(無人水面載具)**:對遠端操控中心做 DoS(數位)+ 用 UAV 在攝影機前擋一張圖(物理)。**兩者單獨發生都安全**,合起來就是一艘自主航行、卻看不見前方油輪的船。
- **最反直覺的發現**:safety 與 security 都不太處理**事件的時間順序**,但時序本身就能繞過防禦——你可能把單一 agent 做安全了,改變事件順序卻能瓦解整個 agentic ecosystem 的安全性。

### 重點整理

#### 背景:York 的 Centre for Assuring Autonomy(約 03:26–03:27)

講者做軟體密集系統的 safety 大約 40 年,這裡的 safety 指的是**對人與環境的物理傷害**;過去九到十年主持自主系統保證(assurance of autonomous systems)的研究計畫,近年逐步涵蓋 AI 乃至 agentic AI——儘管 agentic AI 目前在安全關鍵系統中部署還不多。

中心規模已接近 100 人(faculty、研究員與博士生),領域橫跨海事、自動駕駛與 AI 在醫療照護的應用。這場演講以**海事**為例,因為它最能呈現問題的本質。(插曲:投影片的逐步動畫沒有正常運作,他大半場是「繞著投影片講」。)

#### 為什麼要把 safety 與 security 一起做(約 03:28–03:29)

傳統上 safety 與 security 是**各自獨立評估**的。但在 cyber-physical 系統裡,網路攻擊會**級聯**穿過技術系統、穿過感知系統,最後造成不安全的結果——safety 圈稱之為 hazard(威脅到人員或設備物理安全的狀態)。

導入 AI 之後,safety 與 security 的問題**同時**被改寫:攻擊面大幅擴張,除了作業系統之外還多了訓練管線;而如果系統有物理實體,**物理環境本身也是威脅面的一部分**。

他借用了別人的一個經典例子(明確聲明不是他們的研究):有人訓練一個 AI 演算法去找感知系統的弱點,然後印出貼紙貼在停止標誌上,讓感知邏輯判定那是「速限 45 mph」的標誌——實驗室準確率 93%,真實世界 83%。

#### SCWM:把 security 綁進因果世界模型(約 03:29–03:30、03:33–03:35)

Safety 的基礎是**因果模型**。他的團隊因此建構世界模型來表示這些因果結構,稱為 **structural causal world models(SCWM)**。他特別區分:AI 圈很關注「自動學出世界模型」,而 SCWM 是**我們自己明確描述**的,並且把 security 綁進這個結構裡。

SCWM 有四層:

1. **Ontology**:描述在這個工作場景中重要的世界事物。例如「浪高」——因為波浪施加在船體上的力會改變其操縱性。
2. **不確定性建模**:同一件事在特定情境下無法精確計算,例如你算不出浪與船體交互作用的確切波形,因此海況如何影響船的運動存在不確定性。
3. **不確定性邊界**:上述不確定性被映射成一組 bound。
4. **底層驗證**:喜歡形式化方法的人可以在這層驗證演算法行為——「我可以設定不確定性的邊界,並在這些已知邊界內安全運作」。

安全事件如何進入這個模型:**把攻擊視為對因果依賴圖的 intervention**。實際上你會建出所有相關因素的因果依賴圖(他在投影片上只 highlight 四個節點),security 事件擾動這些關係,再沿著圖傳播到最終的 safety metric 偏差。

本例關心的 metric 是 **closest point of approach(最近會遇距離)** 與 **time to closest approach(抵達最近會遇點的時間)**。距離越小越危險;時間則取決於船有多大、多靈活——船越笨重,你就得越早預測到最近會遇點,才有足夠時間操舵。

#### 案例:無人水面載具的複合攻擊(約 03:30–03:33)

情境(他強調是與真實系統高度相似的代表性模擬,不是真實系統本身):一艘 unmanned surface vessel,依 IMO(International Maritime Organization)定義屬於 **degree three 自主等級**——大致上遠端操控,但必要時可在無遠端介入下自主運作。

他們建了模擬:感知用 **YOLO** 物件偵測器,加上一個他們稱為 **dropout protection module(DPM)** 的模組——當船失去與遠端操控中心的通訊(例如遭到 jamming)時,就回退到完全自主功能。另外還有 **AIS**(向其他船舶廣播自身位置的系統),它是可以被 spoof 的。

**複合攻擊**由兩部分組成:

1. **數位攻擊**:對遠端操控中心發動 DoS,使其無法再控制該船。直接效果是船上的 DPM 接手,自主續行原本協議好的航路。
2. **物理攻擊**:放飛一架 UAV,在船載攝影機前擺一張影像,使系統要嘛完全偵測不到來船,要嘛把它誤判成需要**不同**閃避動作的其他東西。

關鍵在於:

- 只發生 (1) → 安全。船回退到 DPM,繼續安全航行。
- 只發生 (2) → 安全。遠端操作員有資料回傳,會發現異常並採取適當行動。
- **(1)+(2) 同時發生 → 不安全狀態**。船在自主航行,卻不知道前方有油輪、不會採取閃避動作,於是進入碰撞航線。

他用一張圖展示兩個初始攻擊如何沿系統傳播:攻擊會降低對他船位置的估計品質,在影像攻擊的情況下甚至直接改變船的「信念」(前方到底有什麼),最後表現為 closest point of approach 與 time to closest approach 這兩個 safety metric 的劣化。

#### 結論:新的分析方法,以及被忽略的時序(約 03:36–03:37)

總結三點:

1. **AI 在 cyber-physical 系統中帶來新挑戰**:攻擊面大幅擴張,包含訓練資料、prompt、context(若用 LLM)等。
2. **物理攻擊面同樣真實**:spoofing 影像是最明顯的一種,但同樣的手法可以在其他電磁頻域進行。
3. **時序是盲點**:safety 領域(以及某種程度上 security 領域)通常不太處理**事件的時間順序**;而他們做這個分析正是要顯示,**時序可以繞過防禦**——「我可能已經讓某個 agent 安全了,但只要改變事件的時間順序,我就能瓦解整個 agentic 生態系的 safety 與 security。」

因此需要新的、**整合 safety 與 security** 的分析方法。SCWM 是其中一種可能途徑,他們目前正把世界模型延伸到涵蓋**agent 與人類之間的共享理解**(在有對話式介面的場合)。

他給資安聽眾的臨別訊息:如果你做 security,請來找我們做 safety 的人聊——這兩件事的交界處有新的挑戰,不一起看,我們就會部署出進入物理世界後產生極不樂見後果的系統。

### 金句

> "I may have might have made one agent secure but actually by changing the time ordering of events I can actually undermine the safety and security of the agentic ecosystem."(約 03:36:58)

單點安全不等於系統安全,而時序是最容易被漏掉的那一維。

> "If you work on security, please come and talk to we guys who do safety — there's new challenges that arise at the interaction of those two issues."(約 03:37:20)

整場演講的核心呼籲。

## English Notes

### TL;DR

- **Safety and security are different disciplines that can no longer be practiced apart.** After 40 years on the safety of software-intensive systems — safety meaning physical harm to people and the environment — his message to a security audience was blunt: come talk to us, or we will field systems with very undesirable physical consequences.
- **AI stretches the attack surface in two directions**: the familiar IT side (training pipelines, prompts, context) and the **physical environment itself** — stickers on a stop sign made a perception system read "45 mph speed limit" with 93% accuracy in the lab and 83% in the real world.
- **Structural causal world models (SCWM)** have four layers: an ontology of what matters in the world (e.g. wave height), an uncertainty model, uncertainty bounds, and a bottom layer where algorithm behavior can be formally verified within those bounds. Attacks are modeled as **interventions on the causal graph** and propagated to a safety metric.
- **Compound attack on an unmanned surface vessel**: DoS the remote operating center (digital) *and* fly a UAV holding an image in front of the cameras (physical). **Either one alone is safe.** Together you get a vessel navigating autonomously while blind to an approaching tanker.
- **The counterintuitive finding**: neither safety nor security engineering pays much attention to the **time ordering of events**, yet ordering alone can defeat defenses — you can secure an individual agent and still undermine the whole agentic ecosystem by resequencing.

### Key Points

#### Background: the Centre for Assuring Autonomy at York (~03:26–03:27)

Roughly 40 years on the safety of software-intensive systems, where safety means physical harm to people and the environment; the last nine or ten running a programme on the assurance of autonomous systems, progressively extending to AI and now agentic AI — even though agentic AI isn't deployed much in safety-critical systems yet.

The centre is approaching 100 people across faculty, researchers and PhD students, working in maritime, autonomous driving, and AI in healthcare. This talk used maritime as the illustrative domain because it exposes the nature of the problem well. (A running aside: the slide build-up didn't work, so he talked around the deck.)

#### Why safety and security have to be analyzed together (~03:28–03:29)

Traditionally these are assessed independently, in isolation. But in cyber-physical systems, cyber attacks **cascade** through the technical system and through perception systems into unsafe effects — hazards, in safety terminology: states that threaten the physical safety of equipment or personnel.

Introducing AI changes both sides substantially. The attack surface grows to include training pipelines as well as the operating system; and once the system is physical, the physical environment is part of the threat surface too.

The illustration he borrowed (explicitly not his group's work): researchers trained an AI algorithm to find weaknesses in a perception system, then printed stickers to put on a stop sign so the perception logic classified it as a 45 mph speed limit — 93% accuracy in the lab, 83% in the real world.

#### SCWM: binding security into a causal world model (~03:29–03:30, 03:33–03:35)

Safety rests on models of cause and effect, so his group builds world models that represent those causal structures — **structural causal world models (SCWM)**. He drew a deliberate contrast with the AI community's interest in *automatically learned* world models: these are described explicitly, and security is bound into the structure.

Four layers:

1. **Ontology** — the things in the world that matter for this operation. Wave height, for instance, because the force of waves on a vessel alters its maneuverability.
2. **Uncertainty** — you can't compute exactly how wave patterns interact with the hull, so sea state's effect on vessel motion carries uncertainty.
3. **Bounds on uncertainty** — that uncertainty is mapped into bounds.
4. **Verification** — for those who like formal methods, you can verify algorithm behavior at this level: set bounds on the uncertainty and show safe operation within the known bounds.

Security enters as **interventions on the causal dependency graph**. In practice you build the graph over everything that matters in the situation (his slide highlighted four nodes); security events perturb those relationships, and the effect propagates from attack to an ultimate deviation in a safety metric.

Here the metrics are **closest point of approach** and **time to closest approach**. The smaller the distance, the more likely a collision; and time matters especially for large, less maneuverable vessels, which need the prediction much further out to have room to act.

#### Case study: a compound attack on an unmanned surface vessel (~03:30–03:33)

The setup — representative of, though not identical to, a real system they've worked on: an unmanned surface vessel at what the IMO (International Maritime Organization) calls **degree three autonomy**, largely remotely operated but able to run autonomously without remote interaction if needed.

Their simulation uses a **YOLO** object detector plus a **dropout protection module (DPM)** that falls back to fully autonomous operation if the vessel loses communication with the remote operating center — which can happen for many reasons, jamming among them. **AIS**, which broadcasts your position to other vessels, is spoofable, and there are plenty of other concerns besides.

The compound attack:

1. **Classical digital attack** — a denial of service against the remote operating center, so it can no longer control the vessel. Immediate effect: the DPM kicks in and the vessel continues autonomously along the agreed path.
2. **Physical attack** — fly a UAV and hold an image in front of the cameras, so the approaching tanker is either not detected at all or classified as something completely different requiring a different evasive maneuver.

The point is the composition:

- Attack 1 alone: safe. Fall back to the DPM; the vessel operates safely.
- Attack 2 alone: safe. Remote operators get a data feed, notice, and take appropriate action.
- **Both together: an unsafe state.** The vessel maneuvers autonomously without knowing a tanker is in front of it, takes no evading action, and ends up on a collision course.

His propagation graph traced how the two initial attacks move through the system: degrading the position estimate of the other vessel, and in the image-attack case changing the vessel's beliefs about what is actually ahead — surfacing as degradation in closest point of approach and time to closest approach.

#### Conclusions, and the blind spot nobody models (~03:36–03:37)

Three summary points:

1. **AI in cyber-physical systems introduces new challenges** — a much expanded attack surface including training data, prompts, and context where LLMs are involved.
2. **The physical attack surface is real** — spoofing images is the obvious case, but the same can be done in other electromagnetic domains.
3. **Time ordering is the blind spot.** Safety engineering, and to an extent security engineering, tends not to worry about the temporal order of events. Part of why they ran this analysis was to show that ordering can overcome defenses: one agent may be secure, yet resequencing events undermines the safety and security of the agentic ecosystem.

The conclusion is that new analysis approaches integrating safety and security are needed. SCWM is one possible route, currently being extended so the world model also captures shared understanding between agents and humans where dialogue interfaces exist.

His closing appeal to a security audience: if you work on security, come and talk to the safety people — new challenges arise at the interaction of the two, and if we don't look at them together we will deploy systems with very undesirable effects once they reach the physical domain.

### Quotes

> "I may have might have made one agent secure but actually by changing the time ordering of events I can actually undermine the safety and security of the agentic ecosystem." (~03:36:58)

Per-component security doesn't compose, and ordering is the dimension most often left out of the model.

> "If you work on security, please come and talk to we guys who do safety — there's new challenges that arise at the interaction of those two issues." (~03:37:20)

The talk's central appeal.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Centre for Assuring Autonomy (CfAA), University of York | 自主系統保證研究中心,近 100 人,涵蓋海事、自駕、醫療 | Assurance research centre for autonomous systems, ~100 people, maritime / automotive / healthcare | 講者為 Director |
| Structural Causal World Models (SCWM) | 四層因果世界模型,將 security 攻擊建模為對因果圖的 intervention | Four-layer causal world model; security attacks modeled as interventions on the causal graph | 對應論文 "Structural Causal World Models for Safety Assurance of AI-based Autonomy"(2026)/ see the 2026 paper of the same name |
| Dropout Protection Module (DPM) | 模擬船失去與遠端操控中心通訊時,回退到完全自主運作的模組 | Module that falls back to fully autonomous operation when comms to the remote operating center drop | 他們模擬系統中的元件 / component of their simulation |
| YOLO | 模擬中使用的物件偵測器 | Object detector used in the simulation | |
| AIS (Automatic Identification System) | 船舶向他船廣播位置的系統,可被 spoof | Vessel position broadcast system; spoofable | |
| IMO degree three autonomy | 講者定義為「大致遠端操控,必要時可無遠端介入自主運作」 | Speaker's gloss: largely remotely operated, able to operate autonomously without remote interaction if necessary | IMO MASS 官方分級用語需另行核對(見待確認)/ cross-check against official IMO MASS wording (see To Verify) |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| John McDermad / McDermott | John A McDermid |
| center of assuring autonomy | Centre for Assuring Autonomy |
| SCWM(字幕作 "structure causal world models") | structural causal world models |
| Gentic AI / aentic | agentic AI |
| mclassified | misclassified |
| Swifting images | spoofing images |
| submarine security thread models(主持人語) | maritime security threat models |

## 待確認 / To Verify

- 停止標誌貼紙攻擊的 93%(lab)/ 83%(real world)數字與原始論文出處未指名,建議核對。/ The 93% lab / 83% real-world figures for the stop-sign sticker attack were given without a citation.
- IMO 對 MASS(Maritime Autonomous Surface Ships)degree three 的官方定義用語,與講者口述的描述是否一致,需比對 IMO 文件。/ Whether the speaker's gloss of "degree three autonomy" matches IMO's official MASS degree definitions.
- 他提到正在延伸 SCWM 以納入「agent 與人類的共享理解」,此延伸工作是否已有公開論文。/ Whether the SCWM extension covering shared human–agent understanding has been published.
