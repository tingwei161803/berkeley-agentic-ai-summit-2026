---
title: "Robot Foundation Models"
title_zh: "機器人基礎模型"
speaker: "Sergey Levine"
affiliation: "Co-Founder, Physical Intelligence; Professor, UC Berkeley"
type: talk
stage: Plenary
date: 2026-08-01
session: "Session 4: Robotics & World Models"
video: "https://www.youtube.com/watch?v=Tcn5Yb2K0h4&t=7884s"
video_range: "02:11:24–02:21:16"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [robotics, foundation-models, test-time-compute, multimodal-reasoning, reinforcement-learning]
---

# 機器人基礎模型(Robot Foundation Models)

**一句話總結**:機器人做不到「我今晚有客人要來」這種指令,不是因為動作不夠好,而是因為缺少把陌生工作拆解成熟悉步驟的「思考」——而這個思考不一定要用語言,用影像當中介思考往往更貼合物理世界。
**One-line summary**: Robots fail at prompts like "I've got guests coming tonight" not because their motor skills are lacking, but because they lack the test-time reasoning to decompose an unfamiliar job into familiar steps — and that reasoning does not have to happen in language; thinking in images is often the right modality for the physical world.

## 中文筆記

### TL;DR

- **真正的落差在「prompt 的層級」**:研究界的 benchmark 任務是「把玉米放進鍋子」這種 atomic task,但人真正想下的指令是「我今晚有客人要來」——那是一整份工作,需要 grounding、規劃與跨情境泛化。
- **Test-time compute 對機器人有第二個好處**:除了「想久一點解更難的題」,它還能把陌生問題拆成訓練分佈內的熟悉片段(「我沒抓過這個東西,但我在 web-scale 預訓練時定位過影像中的物體」);再用 RL 優化這些 thought,讓拆解出來的子指令是機器人真的做得到的。
- **思考不必用語言**:煮菜照食譜適合語言,攀岩則否。Physical Intelligence 的 **π0.7** 在決策流程中內建輕量 world model,同時用語言與影像思考再落地成動作——沒訓練過的氣炸鍋也能靠「口頭教學」學會操作。

### 重點整理

#### 問題:從 atomic task 到 whole job(約 02:12)

開場是個玩笑:他前一晚下班回家很累,請最愛的 LLM 幫忙打掃、摺衣服、做晚餐——結果 LLM 只回了一堆「你應該自己動手做」的建議。他想要的是坐在機器人裡、真的能動手的 embodied foundation model。

Robot foundation model 是個年輕但成長極快的領域。Physical Intelligence 做了兩年多,已有像是機器人連續 13 小時用義式咖啡機沖咖啡、在工廠組裝紙箱這樣的成果;學界與其他公司也有很多好結果。但他刻意不做成果展示,而是聚焦一個技術問題:**既然結果這麼好,為什麼我們身邊還沒有能聽任意 prompt 做事的機器人?**

答案在 prompt 的層級。研究用的任務長這樣:「put the corn in the pot」(來自 bridge dataset),機器人做到了,但那不是我們要的。我們要的是「我今晚有客人要來」——這句話指定的是**一整份工作而非一個原子任務**,而且它高度依賴脈絡:機器人要知道你是誰、你家長什麼樣,才知道這句話該怎麼解讀。中間有大量 grounding 與問題拆解。

#### Test-time compute 與用 RL 優化 thought(約 02:14–02:17)

Test-time compute 在 LLM 世界的作用大家都熟:多生成 token、想更久,解更難的題。但它還有個比較不明顯的好處:**把不熟悉的問題拆成熟悉的片段**。機器人可以說:「你要我拿起這個東西,我沒做過;但我在 web-scale 預訓練裡定位過影像中的物體,那就先定位再說。」

範例是一個刻意設計來隔離這個問題的研究級任務:「讓藍色積木成為盤子上唯一的東西」。盤子上現在放著壽司(玩具壽司)。正確的反應不只要有效,還要語意上合理——不能把壽司丟到桌上,那不衛生;壽司該進一個語意適當的容器。模型的 reasoning trace 不只處理了這件事,還判斷出壽司對它來說可能是陌生物體,於是決定**輸出空間座標**而不是直接依賴 action head,藉此吸收視覺上的 distribution shift。執行時 thinking trace 每幾秒依現場狀況更新一次。

Thinking model 最強的時候是 thought 被 RL 優化過的時候。這裡 RL 扮演雙重角色:**它會改寫任務描述,把它變成更接近機器人訓練分佈的樣子**。做法是提出多組不同的文字指令來拆解高階 prompt,選機器人最可能成功的那一組。

例子:命令機器人「把鎚子放到盤子上」——高度 out-of-distribution。用現成的 vision-language model(這裡是 Gemini),它不知道機器人會什麼、不會什麼,就直接說「好啊,把鎚子放到盤子上」,機器人不知道鎚子是什麼、怎麼放,結果失敗。經過 RL 之後,模型會**把任務「餵到嘴邊」**:「往左移一點,對準鎚子」——到這一步再說「放到盤子上」,就只剩一種做法,做對的機率大增。RL 在這裡填補的是 distribution gap。

#### 多模態思考與 π0.7(約 02:17–02:20)

照食譜煮菜適合用語言逐步思考;但攀岩時你不會想「我要把手臂往左移 37 公分」,你是用空間、用「等一下看起來會是什麼樣子」在思考。所以機器人基礎模型也可以**用別的模態思考**。早期一個研究工作是:把指令拆解成中介**影像**而非文字——想像「往目標推進一步之後畫面會長怎樣」,那張圖就是 thought,以它為條件再產生動作就容易多了。這招之所以有效,是因為影像生成可以在網路規模資料上預訓練,學會語言與影像的對應,機器人才有辦法「想像」子步驟。

最後是 Physical Intelligence 近期的大規模工作:**π0.7**,一個大型 vision-language-action 模型,在決策流程中**內建輕量 world model**,先用語言與影像推理任務,再把這一切落地成動作。

Demo:Lucy 教機器人使用氣炸鍋——**刻意沒有拿氣炸鍋訓練過**,是完全沒見過的家電。直接叫它「氣炸這顆地瓜」,它會成功,但很慢、摸索很久。若給一點額外監督就會可靠得多,而關鍵是:**這個監督不是動作**。Lucy 用講話的方式一步步口頭教學,產生的是「影像 + 語言」的新資料,動作全部是機器人自己做的、不是 ground truth。這批資料只用來 fine-tune 思考流程——本質上是在**教機器人怎麼想**。教完之後,螢幕上會同時看到模型自己生成的語言 thought 與影像 thought,任務就做得相當流暢了。

#### Takeaways(約 02:20)

- 思考 / 推理模型能讓機器人泛化得更好、聽懂更複雜的 prompt。長期來看這很重要,因為我們最終會想下這種指令:「你是管家機器人,晚上六點打掃、準備晚餐、星期六洗衣服。」——那就是**一句 prompt**,而機器人可能要花好幾週才能完整執行完。
- **思考不必是文字**。物理世界很複雜,該用哪個模態就用哪個。
- 甚至可以**同時用多個模態**,在對的抽象層級上思考:照食譜煮菜用語言,搞懂新家電則需要想像手該放哪裡去按按鈕、開容器。
- 這同時給了兩件事:解更難問題的方法,以及**把其他模態中的知識更有效地轉移進來**的方法。

### 金句

> "Why is it that with all these really nice results, we aren't seeing robots that can follow arbitrary prompts all around us today?"(約 02:12:30)

整場演講的問題意識——不是問「還能做出什麼 demo」,而是問「為什麼 demo 沒有變成日常」。

> "Break down an unfamiliar problem into more familiar steps."(約 02:15)

Test-time compute 對機器人真正的價值:不只是想更久,而是把 out-of-distribution 拉回 in-distribution。

> "The thinking doesn't have to be in text. The physical world is complex and you should use the right modality for the job."(約 02:20:30)

對「一切都用語言 chain-of-thought」的直接反駁。

## English Notes

### TL;DR

- **The real gap is the level of the prompt.** Research benchmarks ask for atomic tasks ("put the corn in the pot"); what people actually want to say is "I've got guests coming tonight" — an entire job that requires grounding, planning, and generalization to new context.
- **Test-time compute buys robots a second, less obvious benefit.** Beyond solving harder problems by thinking longer, it decomposes unfamiliar problems into pieces that sit inside the training distribution ("I've never grasped this, but web-scale pretraining taught me to localize objects in images"). RL on top curates the decomposition so the sub-instructions are ones the robot can actually execute.
- **Thinking need not be in language.** Recipes suit language; rock climbing does not. Physical Intelligence's **π0.7** folds a lightweight world model into its decision loop, reasoning in both language and images before grounding down to actions — enough to operate an air fryer it was deliberately never trained on, taught purely by spoken coaching.

### Key Points

#### From atomic tasks to whole jobs (~02:12)

He opened with a joke: tired after work, he asked his favorite LLM to clean the house, fold the laundry, and make dinner. It obliged with a list of things he should go do himself. What he wants instead is an embodied foundation model sitting in a robot that can actually do it.

Robot foundation models are a young but fast-growing field. Physical Intelligence has been at it for over two years — a robot pulling espresso for 13 hours straight, assembling boxes in a factory — and strong results are coming out of academia and other companies too. Rather than parade results, he zoomed in on one question: **given how good the results are, why aren't there robots around us following arbitrary prompts?**

The answer is the level of the prompt. Research tasks look like "put the corn in the pot" (from the bridge dataset). Nice, but not what we want. We want "I've got guests coming this evening" — a prompt that **specifies an entire job, not an atomic task** — and one whose meaning depends on what the robot knows about you and your home. A great deal of grounding and problem-solving sits between that sentence and a motor command.

#### Test-time compute, and using RL to optimize the thoughts (~02:14–02:17)

Test-time compute in the LLM world is familiar: generate more tokens, think harder, solve harder problems. The less obvious benefit is that it **breaks an unfamiliar problem into familiar pieces**. The robot can reason: "You want me to pick up this object; I've never done that. But in web-scale pretraining I have localized objects in images — let me use that as a stepping stone."

His illustrative task is deliberately artificial: *make the blue block the only thing on the plate*, with a piece of (toy) sushi currently sitting on it. The correct response has to be semantically sensible, not just effective — you don't put sushi on the table, that's unsanitary, so it should go into an appropriate container. The reasoning trace handles that, and further recognizes that the sushi may be visually unfamiliar, so it chooses to **emit a spatial coordinate** rather than lean on the action output to absorb the visual distribution shift. At run time the thinking trace refreshes every few seconds based on what's happening.

Thinking models are most powerful when the thoughts themselves are optimized with RL. Here RL plays a dual role: **it curates the task specification into something closer to the robot's training distribution.** You propose several textual decompositions of a high-level prompt and keep the one the robot is most likely to succeed at.

The example: "put the hammer on the plate" — thoroughly out of distribution. An off-the-shelf VLM (Gemini, in this case) doesn't know what the robot can and can't do, so it simply says "go ahead, put the hammer on the plate," and the robot — which doesn't know what a hammer is or how it goes on a plate — fails. After RL, the model spoon-feeds it: "move a little to the left so you're right over the hammer," and only then "put it on the plate," at which point there is essentially one way to do it. RL bridges the distribution gap.

#### Multimodal thinking and π0.7 (~02:17–02:20)

Following a recipe suits step-by-step language. Rock climbing does not — you don't think "move my arm 37 centimeters left," you think spatially, in terms of what things will look like. So robot foundation models can **think in other modalities**. In earlier work, instructions were decomposed not into text but into an intermediate **image**: imagine what the scene would look like after progress toward the goal, treat that as the thought, and condition the action on it. This works because image generation can be pretrained at internet scale on language-image associations, giving the robot a way to imagine substeps.

That brings him to recent large-scale work at Physical Intelligence: **π0.7**, a large vision-language-action model that **incorporates a lightweight world model into its decision-making**, reasoning about the task in language and in images and then grounding all of it into actions.

The demo: Lucy teaches the robot to use an air fryer — an appliance they **deliberately kept out of training**, so it must generalize zero-shot. Told to air-fry the sweet potato, it succeeds, but slowly and with a lot of fumbling. A little extra supervision makes it far more reliable, and crucially **the supervision is not in actions**: Lucy talks the robot through the task step by step, producing additional image-plus-language data. The actions in that data are the robot's own, not ground truth. The data is used only to fine-tune the thinking process — **teaching the robot how to think**. Afterward you can watch the model's own generated language thoughts alongside the intermediate image thoughts, and the task runs fluently.

#### Takeaways (~02:20)

- Reasoning models let robots generalize better and follow more complex prompts. That matters long-term, because the prompts we ultimately want are like "you're a robot butler: clean the house at 6pm, get dinner ready, do my laundry on Saturdays" — **one prompt**, possibly weeks of robot operation.
- **Thinking doesn't have to be in text.** The physical world is complex; use the right modality for the job.
- You can even use **multiple modalities simultaneously**, at the right level of abstraction: language for following a recipe, imagined imagery for figuring out where your hand should go to push a button on a new appliance.
- Together this provides both a way to solve harder problems and a way to **transfer knowledge more effectively from sources represented in other modalities**.

### Quotes

> "Why is it that with all these really nice results, we aren't seeing robots that can follow arbitrary prompts all around us today?" (~02:12:30)

The framing question of the talk — not "what demo is next," but "why hasn't the demo become ordinary life."

> "Break down an unfamiliar problem into more familiar steps." (~02:15)

What test-time compute is really worth to a robot: pulling out-of-distribution problems back into distribution.

> "The thinking doesn't have to be in text. The physical world is complex and you should use the right modality for the job." (~02:20:30)

A direct rebuttal to language-only chain-of-thought for embodied systems.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Physical Intelligence | 講者共同創辦的公司,做通用機器人基礎模型,已投入兩年多 | The company he co-founded, building general-purpose robot foundation models; over two years in | 例:機器人連續 13 小時操作義式咖啡機、工廠組裝紙箱 / e.g. 13 hours straight on an espresso machine, box assembly in a factory |
| π0.7 (pi 0.7) | 大型 VLA 模型,決策流程內建輕量 world model,同時用語言與影像思考 | Large VLA model with a lightweight world model in the decision loop; reasons in language and images | 演講中的主要新成果 / the talk's headline result;氣炸鍋 demo 出自此模型 |
| bridge dataset | 「put the corn in the pot」示範任務的來源資料集 | Source dataset for the "put the corn in the pot" demo task | 研究級平台,用來對比「原子任務 vs 整份工作」/ research-grade, used to contrast atomic tasks with whole jobs |
| Gemini | 現成 VLM,用來對照「未經 RL 優化的 thought」失敗案例 | Off-the-shelf VLM used as the un-optimized-thought baseline in the hammer example | |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Sergey Lavine / Lavine | Sergey Levine |
| PIO7 / pi 07 | π0.7 (pi 0.7) |
| physical intelligence(小寫) | Physical Intelligence(公司名 / company name) |
| bmanual | bimanual |
| multimmodal / multimodal | multimodal |
| webcale | web-scale |

## 待確認 / To Verify

- Demo 中示範口頭教學的 "Lucy" 為 Physical Intelligence 團隊成員,全名與職稱未在演講中提及。/ "Lucy," who coaches the robot in the air-fryer demo, is a Physical Intelligence team member; full name and title were not stated.
- 早期「以中介影像作為 thought」的指令跟隨工作,演講中未點名論文標題。/ The earlier instruction-following work that decomposes instructions into intermediate images was not named by paper title.
