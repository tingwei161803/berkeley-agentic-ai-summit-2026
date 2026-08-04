---
title: "ScarfBench: Can Agents Migrate Enterprise Java?"
title_zh: "ScarfBench:Agent 能搬得動企業級 Java 嗎?"
speaker: "Rahul Krishna"
affiliation: "Senior Research Scientist, IBM Software Innovation Labs"
type: talk
stage: Compass
date: 2026-08-02
session: "Session 4: Agent Evaluation & Benchmarks"
video: "https://www.youtube.com/watch?v=1UrriPJRSPU&t=9268s"
video_range: "02:34:28–02:43:39"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 2nd - Afternoon Session [DownSub.com].srt"
status: draft
tags: [benchmarks, code-migration, enterprise-java, behavioral-testing, modernization]
---

# ScarfBench:Agent 能搬得動企業級 Java 嗎?(ScarfBench: Can Agents Migrate Enterprise Java?)

**一句話總結**:企業 Java 應用的行為大半藏在框架的 proxy、reflection 與 interceptor 裡,原始碼根本看不到,所以框架之間沒有一對一對應;結果是 coding agent 很擅長讓遷移後的程式**編譯過、部署起來**,但只有 **2–14%** 的遷移真正保住了原本的行為——**「編得過」是個會騙人的訊號**。
**One-line summary**: Enterprise Java behavior largely lives in framework proxies, reflection, and interceptors rather than in the source, so there is no one-to-one equivalence between frameworks. The result: coding agents are very good at producing migrations that **compile and deploy**, yet only **2–14%** actually preserve the source application's behavior — **compilation is a deceptive signal**.

## 中文筆記

### TL;DR

- **應用活得比框架久**:企業 Java 應用累積了數十年的 institutional knowledge——商業規則、資料語意、workflow、整合。遷移必須**換掉底層技術棧,同時保住應用行為**,而後者才是難的部分。
- **難在框架把行為藏起來了**:Java 框架用 proxy、reflection、interceptor 把 runtime 行為包在 API 後面,**程式碼本身根本沒有記錄這些**。所以 Spring 與 Jakarta 之間**不存在一對一對應**;遷移後看起來 build 得過、跑得動,卻可能藏著**只在部署時才浮現的 silent failure**。
- **ScarfBench = Self-Contained Application Refactoring Benchmark**,由 IBM 的領域專家**手工**把每個應用跨 Spring / Quarkus / Jakarta 轉寫,並為每個應用**手寫行為測試**——從 curl 煙霧測試到 Playwright 的瀏覽器點擊驗證。
- **最關鍵的結果**:agent 讓程式編譯與部署成功的能力很強,但**遷移後只有 2–14% 行為完全一致**。**compilation 是個 weak signal**,它給了「agent 很會遷移」的假象。
- **遷移方向是不對稱的**:Spring→Quarkus 與 Jakarta→Spring 是完全不同的難題;資料強烈顯示**有些框架特別難遷入,有些特別難遷出**。

### 重點整理

#### 為什麼企業 Java 遷移值得做,也值得測(約 02:36–02:37)

Rahul Krishna 是 IBM Research 的資深研究科學家。(這場開頭投影片出了問題,他中途改用自己的筆電接續,約 02:35–02:36 有一段空白。)

用 Java 寫的企業應用至今仍然關鍵。這些 legacy 應用當初寫在某個框架上,而**應用本身往往活得比框架還久**。現代化之所以重要,是因為新框架帶來**受支援的 runtime、更好的安全性、更好的部署形態**等等。

但真正的關鍵洞見在於:**部署中的應用裡沉澱了數十年的 institutional knowledge**——商業規則、資料語意、workflow、整合關係。因此:**遷移必須替換底層技術棧,同時保住應用的行為。**

#### 為什麼這件事很難:行為不在程式碼裡(約 02:37)

Legacy Java 應用所依賴的框架,**用 API 把 runtime 行為藏了起來**——各種 proxy、reflection、interceptor。**程式碼本身並沒有捕捉到這些行為,是框架自己在處理。**

後果是:**Spring 寫的應用與 Jakarta 寫的應用之間,並不存在一對一的等價關係。** 當你遷移這些應用,它看起來 build 得正確、跑得正確,**但可能存在只有在部署時才會顯現的 silent failure**。

#### 典型企業 Java 應用的結構(約 02:38–02:39)

大型應用通常分層,每層處理一個特定關注點:**presentation layer**(透過瀏覽器或手機呈現)一路往下到 **data access layer**(資料庫讀寫),再加上把它們串起來的 **cross-cutting concern**(組態、安全性等)。

難點在於:大量行為與商業邏輯**藏在框架與其 API 之後**,而每個框架都有自己的怪癖——dependency injection、annotation 等等,決定了商業邏輯以什麼形式被嵌入。**你去程式碼裡翻,可能一個都找不到。**

而且雖然這些層在「關注點」上是分開的,**部署後的應用是所有層同時互相交互**——這才是問題真正棘手的原因。

#### ScarfBench 的設計(約 02:39–02:40)

**ScarfBench = Self-Contained Application Refactoring Benchmark**,目標有兩個:

1. 檢驗 **agent 在跨框架遷移與現代化應用上到底有多有效**。
2. 在這個過程中透過**理解 agent 的 trajectory**,建立一份「field manual」——關於如何為一般性的現代化任務打造 agentic 解決方案。

benchmark 分兩組:

- **Focused applications**:針對**單一層**的自足應用。
- **Whole applications**:把各層組合成一個**完整的商業 use case**。

IBM 的做法是:讓大量**領域專家(SME)手工**把每個應用跨 **Spring、Quarkus、Jakarta** 轉寫。表格每一列是一個應用,而**一個遷移單位就是「某個應用從某框架到另一框架」**。

這樣設計同樣有兩個目的:

1. **每種遷移都有自己的怪癖,而且是不對稱的**——Spring→Quarkus 和 Jakarta→Spring 是非常不同的兩件事。
2. **看 agent 處理各個獨立層的能耐**——agent 可能很擅長轉換 presentation layer,卻在 integration 或 dependency injection 層上卡住。

Whole application 的部分,同一個應用同時收錄 **monolith** 與等價的 **microservice** 部署兩種形態,一樣由 SME 手工跨所有框架轉寫。

規模(講者現場口述):約 **38 個應用**,展開成 **114 個變體**,directed transformation 合計約 **228 個**。(論文公布的數字略有不同,見「待確認」。)

#### 真正的分野:手寫的行為測試(約 02:41–02:42)

他強調 benchmark 的關鍵差異在於 **handwritten test cases**。在遷移每個應用時,開發者為「這個應用部署後應該表現出的行為」撰寫測試。範圍涵蓋:

- **HTTP 檢查**:例如一個 curl 煙霧測試,確認目標框架下部署的應用開放了相同的 HTTP / HTTPS 埠——本質是 health check。
- **煙霧測試也涵蓋**:messaging 是否正常、資料庫的 update / commit / rollback 行為是否符合預期。
- **JSP 頁面層級**:確認部署後的應用瀏覽器點擊動作正確、資料正確傳遞。
- **Playwright 測試**:對於有瀏覽器端點的應用,確保**遷移後應用上的使用者操作與來源應用看起來完全一致**。

#### 結果:編譯得過,行為卻沒保住(約 02:42–02:43)

他們評估了大量 coding agent(更多結果、失敗模式的分類與 agent 建構建議都在論文裡)。現場的重點結論:

> **Agent 非常擅長把應用遷移到「能編譯、能部署」的狀態,但在「保住目標應用的行為」上並不好。**

具體數字:**遷移後只有 2–14% 的案例行為與來源應用完全一致。**

他點出的方法論教訓:**compilation 本身是一個 weak signal**——它給了我們「agent 很會遷移」的錯誤指示,但行為根本沒被保住。

此外,資料流向也強烈顯示:**有些框架特別難「遷入」,有些框架特別難「遷出」**。agent 從一個應用遷到另一個應用的過程中,存在內在的複雜度與不對稱性。

### 金句

> "The applications themselves often outlive the frameworks."(約 02:36)

企業現代化問題的一句話定義。

> "If we go hunting for it in the code, we may not find any of these."(約 02:38)

商業邏輯藏在框架的 annotation 與 dependency injection 裡——這正是純看程式碼的 agent 會失手的地方。

> "Compilation itself was a weak signal … that gave us a false indication that the agents are really good at migration, but the behavior was not preserved."(約 02:42)

整場最重要的方法論警告。

## English Notes

### TL;DR

- **Applications outlive frameworks.** Enterprise Java apps accumulate decades of institutional knowledge — business rules, data semantics, workflows, integrations. Migration has to **replace the underlying stack while preserving behavior**, and the second half is the hard part.
- **The difficulty is that the framework hides the behavior.** Java frameworks bury runtime behavior behind their APIs using proxies, reflection, and interceptors, and **the code itself doesn't capture any of it**. So there is **no one-to-one equivalence** between Spring and Jakarta; a migrated app can build and run fine while hiding **silent failures that only surface at deployment.**
- **ScarfBench = Self-Contained Application Refactoring Benchmark**, built by having IBM subject-matter experts **manually** port every application across Spring, Quarkus, and Jakarta, with **hand-written behavioral tests** for each — from curl smoke tests to Playwright browser-interaction checks.
- **The headline result**: agents are strong at producing migrations that compile and deploy, but **only 2–14% of migrations preserved behavior exactly**. **Compilation is a weak signal** that creates a false impression of competence.
- **Migration direction is asymmetric**: Spring→Quarkus is a very different problem from Jakarta→Spring, and the data strongly suggests **some frameworks are hard to migrate *to* and others hard to migrate *from*.**

### Key Points

#### Why enterprise Java migration is worth benchmarking (~02:36–02:37)

Krishna is a senior research scientist at IBM Research. (The talk opened with a slide failure; he switched to his own laptop mid-talk, leaving a gap around 02:35–02:36.)

Enterprise applications written in Java remain critical. These legacy applications were written against some framework, and **the applications themselves often outlive the frameworks.** Modernization matters because newer frameworks bring **supported runtimes, better security, and better deployment modalities**, among other things.

But the real insight is what's sitting inside a deployed application: **institutional knowledge embedded over several decades** — business rules, data semantics, workflows, integrations. So **migration must replace the underlying technology stack while preserving application behavior.**

#### Why it's hard: the behavior isn't in the code (~02:37)

The Java frameworks these legacy applications are written against **hide runtime behaviors behind their APIs** — proxies, reflection, interceptors. **The code doesn't capture any of this; the framework handles it.**

The consequence: **there is no one-to-one equivalence between an application written in Spring and one written in Jakarta.** When you migrate, it may look like the app builds and runs correctly, **but there may be silent failures that only show up at deployment time.**

#### The anatomy of a typical enterprise Java application (~02:38–02:39)

Large applications are organized in tiers, each addressing a specific concern: the **presentation layer** (serving a browser or phone app) down through the **data access layer** (database reads and writes), plus a **cross-cutting concern** tying everything together with configuration, security, and so on.

The difficulty is that much of the behavior and business logic is **hidden behind the framework and its APIs**, and each framework has its own idiosyncrasies — dependency injection, annotations — that dictate how business logic gets embedded. **Go hunting for it in the code and you may find none of it.**

And although the layers are separate in terms of concerns, **a deployed application has all of them interacting with one another, often at the same time** — which is what makes the problem genuinely challenging.

#### The design of ScarfBench (~02:39–02:40)

**ScarfBench** stands for **Self-Contained Application Refactoring Benchmark**, with a twofold objective:

1. Measure **how effective agents actually are at migrating and modernizing applications** from one framework to another.
2. Along the way, by **understanding agent trajectories**, build a "field manual" for constructing agentic solutions for general modernization.

Two groups:

- **Focused applications**: self-contained apps for a **single layer**.
- **Whole applications**: those layers assembled into a **cohesive business use case**.

IBM's method was to have a large number of **subject-matter experts manually convert** each application across **Spring, Quarkus, and Jakarta**. Each row is an application, and **a unit of migration is any app going from one framework to another.**

This design also serves two purposes:

1. **Every migration has its own idiosyncrasies, and they are asymmetric** — Spring→Quarkus is very different from Jakarta→Spring.
2. **It exposes how agents handle independent layers** — an agent may be excellent at converting the presentation layer while struggling with integration or dependency injection.

The whole-application group captures each app both as a **monolith** and as an equivalent **microservice** deployment, again manually converted by SMEs across all frameworks.

Scale, as spoken on stage: roughly **38 applications** individually, expanding to **114 variations**, with directed transformations totaling about **228**. (The published paper's figures differ slightly — see To Verify.)

#### The real differentiator: hand-written behavioral tests (~02:41–02:42)

The key distinction he emphasized is the **handwritten test cases**. As each application was migrated, developers wrote tests for the behaviors expected once it's deployed, spanning:

- **HTTP checks** — a curl smoke test confirming the app deployed in the target framework exposes the same HTTP and HTTPS ports; essentially a health check.
- **Smoke tests also cover** whether messaging works correctly and whether database updates, commits, and rollbacks behave as expected.
- **JSP-page-level checks** verifying browser click actions and correct data propagation in the deployed application.
- **Playwright tests** for apps with a browser endpoint, ensuring **user actions on the migrated application look identical to the source app.**

#### Results: it compiles, but the behavior is gone (~02:42–02:43)

They evaluated a large number of coding agents; more results, failure-mode taxonomies, and guidance on building better agents are in the paper. The stage highlight:

> **Agents are highly effective at migrating applications to the point where they compile and deploy — and not good at maintaining behavior in the target application.**

The number: after migration, **only 2–14% of migrations had exactly the same behavior as the source application.**

The methodological lesson he drew: **compilation itself was a weak signal**, giving a false indication that agents are good at migration when behavior was not in fact preserved.

The flows also strongly suggest that **some frameworks are really hard to migrate *to* and some are really hard to migrate *from*** — an inherent complexity and asymmetry in how agents move applications between frameworks.

### Quotes

> "The applications themselves often outlive the frameworks." (~02:36)

A one-line definition of the enterprise modernization problem.

> "If we go hunting for it in the code, we may not find any of these." (~02:38)

Business logic lives in the framework's annotations and dependency injection — exactly where a source-reading agent will miss it.

> "Compilation itself was a weak signal … that gave us a false indication that the agents are really good at migration, but the behavior was not preserved." (~02:42)

The most important methodological warning in the talk.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| ScarfBench | 企業 Java 跨框架遷移 benchmark,SME 手工轉寫 + 手寫行為測試 | Enterprise Java cross-framework migration benchmark; SME-authored ports plus hand-written behavioral tests | IBM Research 開源,含公開 leaderboard(scarfbench.info、GitHub scarfbench/benchmark)/ open-sourced by IBM Research with a public leaderboard |
| ScarfBench 論文 / paper | 含完整結果、失敗模式分類與 agent 建構建議 | Full results, failure-mode taxonomy, and guidance on building better agents | arXiv:2605.06754 "ScarfBench: A Benchmark for Cross-Framework Application Migration in Enterprise Java" |
| Spring / Quarkus / Jakarta EE | benchmark 涵蓋的三個 Java 框架 | The three Java frameworks the benchmark spans | |
| Playwright | 用於驗證瀏覽器端行為一致性的測試工具 | Used to verify browser-side behavioral equivalence | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| scarfbench | ScarfBench |
| jakata / jakarta | Jakarta (EE) |
| applica agents | coding agents |
| playright | Playwright |
| GSP pages | JSP pages |
| microser | microservice |
| behav / behavi | behavior |

## 待確認 / To Verify

- 規模數字有出入:講者口述約 38 應用 / 114 變體 / 228 directed transformations,而公開資料為 34 個 application family / 102 個框架變體 / 204 個 directed migration。以哪一組為準需核對論文與投影片。/ Scale figures conflict: he said ~38 apps, 114 variants, 228 directed transformations, while published materials give 34 application families, 102 framework variants, and 204 directed migrations. Needs checking against the paper and slides.
- 行為保真率:講者說「2–14%」,IBM 公開說明為「最強的 agent 也低於 10%」,兩者範圍與統計口徑需釐清。/ Behavioral fidelity: he said 2–14%; IBM's public materials say even the strongest agents are below 10%. The ranges and how they're computed need reconciling.
- 演講中未點名所評估的 coding agent 清單。/ The list of coding agents evaluated was not named on stage.
- ScarfBench 縮寫的正式展開方式(講者念作 Self-Contained Application Refactoring Benchmark)。/ The official expansion of the acronym as printed (he pronounced it Self-Contained Application Refactoring Benchmark).
