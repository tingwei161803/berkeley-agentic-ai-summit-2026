---
title: "Photonics Is the Future of Computing"
title_zh: "光子學是運算的未來"
speaker: "Nick Harris"
affiliation: "Founder/CEO, Lightmatter"
type: talk
stage: Compass
date: 2026-08-01
session: "Session 1: AI Systems"
video: "https://www.youtube.com/watch?v=IBpR4uYftLY&t=1466s"
video_range: "00:24:26–00:32:55"
transcript: "tmp/[English (auto-generated)] Compass Stage - August 1st - Morning Session [DownSub.com].srt"
status: draft
tags: [photonics, interconnect, datacenter, hardware, scaling]
---

# 光子學是運算的未來(Photonics Is the Future of Computing)

**一句話總結**:AI 的成長曲線正在撞上美國電網的成長曲線,而真正的瓶頸不是算力而是 **interconnect**;Lightmatter 用光把上千顆 GPU 連成「一顆大腦」,以逼近零延遲、無限頻寬的極限來換取 3 倍訓練速度與 11 倍 decode 互動性。
**One-line summary**: AI's growth curve is outrunning the US power grid, and the real bottleneck is interconnect rather than compute; Lightmatter uses light to fuse thousands of GPUs into a single brain, approximating zero latency and infinite bandwidth to deliver 3× faster training and 11× decode interactivity.

## 中文筆記

### TL;DR

- **為什麼要蓋這些資料中心**:AI 模型能連續工作並有 50% 機率完成任務的時間長度呈指數成長,現在已到**約 24 小時**;而電力供給是瓶頸——美國電網年成長率只有個位數百分比,frontier AI 的用電曲線會直接撞穿它。一個 gigawatt 級資料中心約等於紐約市(~7 GW)的量級零頭,而 1,000 個機櫃就是 1 GW。
- **瓶頸是 interconnect,不是算力**:讓 GPU/XPU 彼此溝通才是今天推進 agentic AI workload 的主要障礙。若延遲趨近零、頻寬趨近無限,幾公尺外的 GPU 與同一顆晶片就沒有區別——這就是 **strong scaling**,讓上千顆晶片「像單一顆晶片一樣」運作。
- **實測效益與硬體規格**:同樣數量 GPU、同樣 workload,**訓練時間縮短 3 倍**;推論的 **pre-fill 快 3 倍**、**decode 的每使用者 tokens/sec 提升 11 倍**。旗艦晶片 **M1000** 為 114 Tb/s(業界水準約 10 Tb/s),單條光纖 1.6 Tb/s(業界約 0.2 Tb/s);單一 M1000 機櫃就是數 petabit/s 的 I/O。

### 重點整理

#### AI build-out 與電力天花板(約 00:24:50–00:27:30)

世界正在進行一場大規模 AI 基礎建設擴張:德州、英屬哥倫比亞的資料中心用電量已達「地球最大城市」等級——紐約市大約 7 GW,而這在德州 Abilene 那樣的地方會變成「相當平均」的資料中心規模。

為什麼值得?因為模型能獨立工作的時間長度(給定複雜任務、有 50% 機率完成的執行時長)持續指數成長,**現在已達約 24 小時**,而且資料裡看不到飽和跡象。Harris 的說法是:我們正在壓縮「完成困難而有價值的工作」所需的時間。

但供給端跟不上:美國電網每年新增的能源只有個位數百分比成長,frontier AI 的用電曲線會**直接衝破**電網能提供的量。核能是選項之一(每 GW 資料中心配 10 座 100 MW 反應爐),但他要大家先感受一下數量級——一戶人家幾 kW、**一個機櫃開始逼近 1 MW、1,000 個機櫃就是 1 GW**,而這個會議廳大概只放得下幾百個機櫃。

#### 為什麼是 interconnect:strong scaling 與「單一大腦」(約 00:28:00–00:31:00)

Harris 直接跳到結論:**interconnect 才是今天的主要瓶頸**。Lightmatter 用光連接 GPU 與晶片,單一波導/光纖傳輸 1.6 Tb/s——「一條光纖等於 1,600 戶人家的頻寬」。成果:

| 指標 | 提升 |
|------|------|
| Time to train(同樣 GPU 數、同樣 workload) | 3× |
| Inference pre-fill | 3× |
| Inference decode(每使用者 tokens/sec 互動性) | 11× |

背後的目標是打造**行為上等同單一顆晶片的巨型系統**,也就是計算機科學意義上的 **strong scaling**。理想狀況:兩顆晶片跑同一個 workload 該得到兩倍效能,一千顆該得到一千倍;但多數 workload 不是 embarrassingly parallel,需要同步、需要共享運算的一部分。極限解法是**零延遲 + 無限頻寬**——那樣的話,幾公尺外的 GPU 與本地晶片就沒有差別。Lightmatter 在做的就是逼近這個「完美 interconnect」。他預期**未來兩年會看到第一批上千顆 GPU/XPU 表現得像單一顆巨型 GPU 的系統**。

#### 硬體與可靠性(約 00:31:00–00:32:50)

- **M1000**:號稱世界最快的光通訊元件,**114 Tb/s**;上下緣接光纖,每條 1.6 Tb/s。對比:業界最先進約 10 Tb/s、單纖約 0.2 Tb/s——「到處都是 10 倍」。連接北美與歐洲的海底電纜約 200 Tb/s,不到兩顆這種晶片。
- **機櫃**:單一 M1000 機櫃就是數 petabit/s 的 I/O——「全世界的網際網路流量,等於左邊那一個 Lightmatter 機櫃」。
- **可靠性**:規模化 AI 平台的一大挑戰是可靠性。10 萬顆 GPU 的資料中心會有約 1,000 萬條連線,這些連線**不能出錯**,否則凍結訓練、拖垮推論。因此 Lightmatter 自建整座驗證用資料中心,同時運轉數百到數千套平台,證明它們就是不會掛。

### 金句

> "I don't know anybody who can work for 24 hours non-stop and have a 50% chance at solving a hard technical problem. Certainly I can't do it."(約 00:26:00)

用來說明模型自主工作時長曲線的意義——這條曲線就是整個 build-out 的動機。

> "It enables you to build gigantic computer systems that behave as a single brain."(約 00:29:33)

Lightmatter 對「光子學能給你什麼」的一句話回答。

> "The entire world's traffic, internet traffic, is a single rack from Lightmatter M1000 there on the left."(約 00:31:54)

一個讓人記住的數量級對照。

## English Notes

### TL;DR

- **Why the build-out is happening**: the run time over which a model has a 50% chance of completing a hard task keeps growing exponentially and now sits at roughly **24 hours**, with no saturation visible in the data. The constraint is power — the US grid adds only a few percent of capacity per year, while the frontier-AI power curve smashes straight through it. A gigawatt is 1,000 racks; New York City is about 7 GW; that scale is becoming an *average* Texas data center.
- **Interconnect, not compute, is the bottleneck**: how GPUs and XPUs talk to each other is the principal challenge in scaling agentic AI workloads. At the limit of zero latency and infinite bandwidth, a GPU meters away is indistinguishable from a local one — that's **strong scaling**, thousands of chips acting as one.
- **Measured payoff and hardware**: same GPUs, same workload, **3× faster time to train**; **3× pre-fill** and **11× decode interactivity** (tokens/sec/user) for inference. The **M1000** moves 114 Tb/s (state of the art ≈ 10 Tb/s) over 1.6 Tb/s fibers (state of the art ≈ 0.2 Tb/s), and a single M1000 rack carries several petabits/sec of I/O.

### Key Points

#### The build-out and the power ceiling (~00:24:50–00:27:30)

The world is undergoing a massive AI build-out: data centers in Texas and British Columbia now draw as much power as the largest cities on Earth. New York City is around 7 GW — soon a fairly average data center in a place like Abilene, Texas.

The justification is capability growth. Model run time — how long a model can work on a complex task with a 50% chance of finishing — has been growing exponentially and now sits near 24 hours. Harris sees no saturation in the data, and frames the whole build-out as compressing the time it takes to do very hard, very valuable work.

Supply can't keep up. US grid capacity grows a few percent per year; frontier AI power consumption blows past it. Nuclear is one answer (roughly ten 100 MW reactors per gigawatt data center), but he first wants the audience to feel the scale: a house is a few kilowatts, **a rack is approaching a megawatt, a thousand racks is a gigawatt** — and the conference hall they were sitting in would hold a few hundred racks.

#### Why interconnect: strong scaling and the "single brain" (~00:28:00–00:31:00)

Given ten minutes, Harris jumps to the conclusion: **interconnect is the principal challenge**. Lightmatter connects GPUs and chips with light, at 1.6 Tb/s per waveguide/fiber — "1,600 homes' worth of bandwidth in a single optical fiber." The results: 3× faster time to train on the same GPUs running the same workload, 3× on inference pre-fill, and 11× interactivity (tokens per second per user) on decode.

The underlying goal is systems that **behave as a single brain** — strong scaling in the computer-science sense. Ideally two chips on one workload give you two units of performance and a thousand chips give you a thousand; in practice most workloads aren't embarrassingly parallel and need synchronization and shared state. At the limit you want zero latency and infinite bandwidth, at which point GPUs many meters apart are indistinguishable from local ones. Lightmatter is approximating that perfect interconnect, and Harris expects the **first systems where a thousand GPUs or XPUs act as one giant XPU within the next two years**.

#### The hardware, and reliability (~00:31:00–00:32:50)

- **M1000**: billed as the fastest optical communication device in the world at 114 Tb/s, with optical fibers along the top and bottom edges moving 1.6 Tb/s each. State of the art is around 10 Tb/s per device and 0.2 Tb/s per fiber — "there's 10x's all over the place." The transatlantic cables connecting North America to Europe run about 200 Tb/s, less than two of these chips.
- **Racks**: a single M1000 rack carries several petabits per second of I/O — the entire world's internet traffic in one rack.
- **Reliability**: a major scaling challenge. A data center with 100,000 GPUs has on the order of 10 million links, and those links had better not produce errors — errors freeze training runs and crash inference. Lightmatter therefore builds entire validation data centers, operating hundreds to thousands of these platforms to prove they simply won't crash.

### Quotes

> "I don't know anybody who can work for 24 hours non-stop and have a 50% chance at solving a hard technical problem. Certainly I can't do it." (~00:26:00)

His framing of the time-horizon curve — the curve that motivates the entire build-out.

> "It enables you to build gigantic computer systems that behave as a single brain." (~00:29:33)

Lightmatter's one-sentence answer to "what does photonics buy you?"

> "The entire world's traffic, internet traffic, is a single rack from Lightmatter M1000 there on the left." (~00:31:54)

A comparison built to be remembered.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Lightmatter Passage M1000 | 3D 光子 superchip,114 Tb/s 光學頻寬,256 條光纖 | 3D photonic superchip; 114 Tbps optical bandwidth, 256 fiber attachments | 2025-03 發表,官方規格與演講數字一致 / announced Mar 2025; specs match the talk |
| Strong scaling | 讓多晶片系統的效能隨晶片數線性成長的目標 | Goal of near-linear performance scaling across many chips | 演講中用來說明「單一大腦」的技術目標 / the technical framing of the "single brain" |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Agentyc AI | Agentic AI |
| Light matter | Lightmatter |
| 1.6 ter- / 114,000 houses | 1.6 Tbps / 114,000 homes' worth of bandwidth(口語斷句)|
| Abilene(字幕作 "Abilene" 但唸法模糊)| Abilene, Texas |
| "10 100 MW nuclear reactors per gigawatt data center" | ten 100 MW reactors per gigawatt data center |

## 待確認 / To Verify

- 「50% 成功率的任務時長曲線」未在演講中點名出處(業界常引用 METR 的 time-horizon 研究),需看投影片確認來源。/ The source of the 50%-success-rate time-horizon curve was never named on stage (commonly attributed to METR's time-horizon work); check the slides.
- 3× time-to-train、3× pre-fill、11× decode 的量測條件(模型、GPU 數、對照基準)未說明。/ The measurement conditions behind 3× train / 3× pre-fill / 11× decode (model, GPU count, baseline) were not stated.
- 「德州與英屬哥倫比亞的資料中心」未指名具體站點。/ The Texas and British Columbia data centers were not named specifically.
