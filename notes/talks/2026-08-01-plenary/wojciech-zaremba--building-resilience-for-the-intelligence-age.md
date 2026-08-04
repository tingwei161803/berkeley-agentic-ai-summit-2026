---
title: "Building Resilience for the Intelligence Age"
title_zh: "為智慧時代建立韌性"
speaker: "Wojciech Zaremba"
affiliation: "Co-Founder, OpenAI; Head of AI Resilience, OpenAI Foundation"
type: talk
stage: Plenary
date: 2026-08-01
session: "Session 3: Agentic AI Foundational Capabilities"
video: "https://www.youtube.com/watch?v=Tcn5Yb2K0h4&t=3585s"
video_range: "00:59:45–01:10:08"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [ai-resilience, safety, policy, ecosystem, biosecurity]
---

# 為智慧時代建立韌性(Building Resilience for the Intelligence Age)

**一句話總結**:火的安全不是靠禁止用火達成的,而是靠偵測、消防隊、水管網、建材、檢查、保險層層疊起來的生態系;AI 也不會有 silver bullet,把個別模型對齊只是其中一層,真正要做的是去打造那些還不存在的機構與組織。
**One-line summary**: Fire didn't become safe because we banned it — it became safe through a layered ecosystem of detection, brigades, hydrants, materials, inspections and insurance; AI has no silver bullet either, aligning individual models is only one layer, and the real work is building the institutions that don't exist yet.

## 中文筆記

### TL;DR

- **AI resilience 是什麼**:OpenAI 重組後,非營利的 OpenAI Foundation 持有約四分之一的 OpenAI 股權,其中一個部門就是 AI resilience。它和 AI safety 相近但不同——safety 多半問「模型本身安不安全」,resilience 問「世界要長成什麼樣子,AI 才會走向好的結果」。
- **限制(restriction)這條路歷史上不太成功**:curfew 這個字源自法文、原意就是「熄火」,中世紀警察會半夜敲門要你把火熄掉——但倫敦大火還是在宵禁之下發生了。AI 這邊也類似:少數限制(如平台一致禁止 NCII)有效,但被大力倡議的開源限制其實並沒有落地。
- **火之所以變安全,是因為多層生態系**:早期偵測、受訓的消防隊與消防車、專門設計的水帶、遍布城市且有足夠壓力與水量的消防栓、把木造換成金屬與混凝土、檢查、保險、逃生動線⋯⋯沒有任何一項是 silver bullet。成效驚人:今天城市密度比中世紀高一個數量級,起火源多得多(電、瓦斯、工業、甚至資料中心),但沒有人在擔心火災。
- **對 AI 的三個具體對照**:生物領域要「硬化環境本身」(例如空氣消毒,讓病原體無法傳播);資安要走到**軟體形式化驗證**,才擋得住超級智慧的入侵;安全事故要有**像航空業那樣的公開事故資料庫**,並給通報者 safe harbor。
- **這是一份招募**:有些要靠公司、有些要靠非營利組織來完成。他呼籲有能力、能「扭曲現實」的人自問「這個世界還缺什麼,AI 才會走好」,然後去把那些新機構建出來——OpenAI Foundation 有大量資源支持這類努力。

### 重點整理

#### 定位:AI resilience 與 OpenAI Foundation(約 00:59–01:01)

開場投影片一路出錯,他順手自嘲:「這就是 AGI 還沒到的證據。」

正題:OpenAI 幾個月前完成重組,現在有一個非營利組織持有**約四分之一的 OpenAI 股權**——這是極為龐大的資源。OpenAI Foundation 底下的其中一個部門就是 **AI resilience**,而這場演講要解釋 AI resilience 是什麼:**它和 AI safety 相似,但不一樣**。他選擇用「火的韌性」這個類比來講,並先聲明火和 AI 在很多面向上非常不同,所以這些類比絕非完美。

#### 火與 AI 的兩個相似點(約 01:01–01:03)

**相似點一:兩者都是通用技術(general purpose technology)**,適用面極廣。火被用來加熱食物、提供溫暖、冶煉金屬、驅動引擎,基本上是文明的根基。AI 正在發生類似的事:它已經是知識與智慧生產的一部分、是科學流程的一部分;而**如果你認真看待機器人的走向,它將直接成為未來經濟引擎的基礎組件**。

**相似點二:兩者都帶著風險**。火的部分:歷史上有過幾場重大火災,倫敦被燒過四次,波士頓、芝加哥也有,大火期間倫敦約 80% 被吞噬。差別在於**今天我們已經相當清楚火的風險是什麼,AI 則不然**——問人們 AI 的風險是什麼,大家指的方向都不一樣,打開報紙就能看到各種恐懼。他的判斷是:**這些風險高度不確定**;最後可能有些會變成只是文書作業層級的小事,有些會比大家預期的嚴重 10 倍,而**有些真正的風險甚至根本不在現在這張清單上**。

#### 轉折:靠「限制」求安全,歷史上沒成功(約 01:03–01:04)

有趣的地方在這裡。人類最早對火的安全手段其實是**限制**:curfew(宵禁)一詞源自法文,原意就是「熄火」。中世紀很常見的情況是,你家晚上還有火在燒,警察會來敲門要求你熄掉。這顯然是**降低這項技術的能力**——而至少在這個案例上,它並沒有奏效:**倫敦大火還是在宵禁制度下發生了。**

AI 這邊比較複雜。有些限制看起來運作得相當好,例如**絕大多數平台都遵循禁止非合意親密影像(NCII)的限制**;但也有人倡議對開源模型設限,那些其實並沒有真的被實施。他的結論是:**在 AI 這邊,限制這條路也沒走出好結果。**

#### 火真正變安全的方式:沒有 silver bullet,只有多層生態系(約 01:04–01:07)

那火到底是怎麼變安全的?**結論是根本沒有單一解方**,最後靠的是一整套多層次的生態系:

- 火災**早期偵測系統**
- 受過專門訓練的**消防隊**、專用**消防車**、特別設計的**水帶**
- 城市層級的**供水網與消防栓**——而且要有足夠的壓力與水量才能真的滅火
- **建材的更替**:從木造換成金屬與混凝土
- **檢查制度、保險**
- **指定的逃生出口**與動線

一旦這些都到位,火就不再是我們特別擔心的事——**我們能夠完全享受它的好處**。這套做法有效嗎?**效果好得驚人**:今天的城市密度比中世紀高一個數量級,起火來源也多得多(電力、瓦斯、工業,甚至資料中心),但火災已經不是一般人會擔心的事情。

#### 對照回 AI:三個「硬化環境」的例子(約 01:07–01:09)

他觀察到 **AI 圈的人普遍在找那個 silver bullet,認為會有某一個解方讓 AI 走向好結果——他認為這個思考方式是錯的**。而且**只把個別模型對齊也不夠**,那是解方的一部分,但生態系裡需要的解方不只一個。三個具體例子:

- **生物安全**:模型在生物領域已經相當強,很多人擔心模型讓製造大流行變得容易。如果這是風險,**而且我們同時假設先進的開源模型會擴散開來,那麼只在前沿實驗室裡對這些能力加 guardrail 就不會夠**——該做,但不夠。我們可能需要**硬化環境本身**:例如有人在思考**空氣消毒**,因為空氣一旦被消毒,病原體就無法散播。
- **資安**:也許我們需要走到**軟體被形式化驗證**的程度,那才能防止它被超級智慧入侵。
- **安全事故**:也許我們需要**公開的事故資料庫**,像航空業那樣公開通報事故,而**通報者可以因為通報而獲得 safe harbor(免責保護)**。

#### 收尾:這是一份招募(約 01:09–01:10)

這些東西怎麼生出來?**有些可以透過成立公司來達成,有些則要靠成立非營利組織。** 但更根本的是:我們現在需要一批有能力的人——那種「能扭曲現實」的人、那種標竿型人物——**自問「這個世界還需要被建造出什麼,AI 才會走向好的結果」,然後真的去建立那些新的機構與組織**。而 OpenAI Foundation 這邊有大量資源可以支持這類努力。

最後一句話直接把責任交回台下:**AI resilience 會不會成功,取決於在座的各位。**

### 金句

> "That's an evidence that AGI is not yet here."(約 01:00)

投影片翻不動時的自嘲。

> "The great fire of London happened despite of curfews."(約 01:04)

限制技術能力並不等於安全——這是整場演講的支點。

> "It turns out that there wasn't a silver bullet. … It ends up being a multi-layer ecosystem approach."(約 01:05)

火的教訓,也是他對 AI 的主張。

> "It might not be sufficient to guardrail these capabilities within the frontier labs. … We might need to harden the environment itself."(約 01:08)

從「管好模型」轉向「改造世界」——這正是 resilience 有別於 safety 的地方。

> "Whether or not AI resilience will succeed depends on people in this room."(約 01:10)

## English Notes

### TL;DR

- **What AI resilience is**: after OpenAI's restructuring, a nonprofit now owns roughly a quarter of OpenAI's equity, and one of the OpenAI Foundation's divisions is AI resilience. It is adjacent to AI safety but distinct — safety mostly asks whether the model is safe; resilience asks what the world must look like for AI to play out well.
- **Restriction has a poor historical record.** "Curfew" comes from the French for *extinguish the fire*; in medieval times police would knock at your door at night to make you put it out. The Great Fire of London happened anyway. AI is similar: a few restrictions work (platforms broadly honor non-consensual intimate imagery bans), while the loudly advocated open-source restrictions were never really implemented.
- **Fire became safe through a layered ecosystem**: early detection, trained brigades and fire trucks, purpose-designed hoses, city-wide water supply with hydrants at sufficient pressure and volume, materials shifting from wood to metal and concrete, inspections, insurance, designated exits. No single item was the answer. The result is remarkable — cities an order of magnitude denser than medieval ones, far more ignition sources (electricity, gas, industry, even data centers), and nobody worries about fire.
- **Three concrete AI analogues**: for bio, harden the environment itself (e.g. sanitizing air so pathogens can't spread); for cyber, get software **formally verified** so superintelligence can't hack it; for safety incidents, build a **public incident database like aviation's**, with safe harbor for those who report.
- **This is a recruiting pitch.** Some of it gets built by companies, some by nonprofits. He wants capable, reality-warping people to ask what the world still needs for AI to go well, and then go build those institutions — the OpenAI Foundation has substantial resources to back such efforts.

### Key Points

#### Framing: AI resilience and the OpenAI Foundation (~00:59–01:01)

After several slides refused to advance, he deadpanned: "That's evidence that AGI is not yet here."

The substance: OpenAI restructured a number of months ago, and there is now a nonprofit that owns **around one quarter of OpenAI's equity** — a massive pool of resources. One of the OpenAI Foundation's divisions is **AI resilience**, and the talk exists to explain what that means: **similar to AI safety, and yet different.** He explains it through an analogy to fire resilience, flagging up front that fire and AI differ in many, many ways, so the analogies are by no means perfect.

#### Two similarities between fire and AI (~01:01–01:03)

**First, both are general purpose technologies** with enormously broad applicability. Fire heats food, provides warmth, smelts metal, powers engines — it is fundamental to civilization. Something similar is happening with AI: it is already part of how knowledge and wisdom get developed, part of the scientific process, and **if you take seriously where robotics is going, it will simply be a fundamental part of the economic engine of the future.**

**Second, both come with risks.** For fire: a number of major historical fires, London burned four times, Boston and Chicago too, roughly 80% of London consumed during the large fires. The difference is that **we understand fire's risks pretty well today, and we don't understand AI's** — ask people about AI risk and they point in different directions; open a newspaper and you'll find every fear on offer. His view: **these risks are highly uncertain.** Some may turn out to be paperwork-level nuisances, some may turn out 10x worse than expected, and **some real risks may not even be on the current list.**

#### The twist: safety through restriction didn't work (~01:03–01:04)

Here is the interesting turn. The earliest approach to fire safety was **restriction**. Curfew comes from the French and means *extinguish the fire*; in medieval times, if you had a fire going at home at night, police would come knock and tell you to put it out. That is plainly **a reduction in the capability of the technology** — and at least in this case, it didn't work out: **the Great Fire of London happened despite curfews.**

For AI it is more complicated. Some restrictions do seem to work well — **most platforms follow non-consensual intimate imagery restrictions.** Others, like the open-source restrictions various people advocated for, were never really implemented. His conclusion: **in AI's case too, restriction hasn't worked out well.**

#### How fire actually became safe: no silver bullet, a layered ecosystem (~01:04–01:07)

So what did it take? **There was no silver bullet.** It ended up being a multi-layer ecosystem:

- **Early detection** systems for fires
- Trained **firefighter brigades**, purpose-built **fire trucks**, specially designed **hoses**
- A city-wide **water supply with hydrants**, at sufficient pressure and in sufficient quantity to actually extinguish a fire
- **Materials** redesigned: wood replaced by metal and concrete
- **Inspections and insurance**
- **Designated exits** and egress routes

Once all of that was in place, fire stopped being something we worry about — **we became able to fully harness its benefits.** Did it work? **Remarkably well.** Cities today are an order of magnitude denser than medieval ones, with far more sources of fire — electricity, gas, industry, even data centers — and fire is not something people worry about.

#### The AI analogue: three ways to harden the environment (~01:07–01:09)

His observation is that **people in the AI space keep looking for the silver bullet, the one solution that makes AI play out well — and he thinks that is the wrong way to think about it.** It is also **not enough to make individual models aligned**; that is part of the solution, but the ecosystem needs several. Three examples:

- **Biosecurity**: models are becoming quite capable in the biological domain, and many foresee risk from models making pandemics easy to manufacture. If that is the risk — **and if we also assume advanced open-source models will diffuse — then guardrailing those capabilities inside frontier labs won't be sufficient.** It should be done, but it won't be enough. **We may need to harden the environment itself**: people are thinking about ideas like **sanitizing air**, because if air is sanitized, pathogens can't spread.
- **Cybersecurity**: perhaps we need to reach the point where **software is formally verified**, which would prevent it from being hacked by superintelligence.
- **Safety incidents**: perhaps we need a **public incident database, as aviation has** — incidents publicly reported, with those who report gaining **safe harbor** by reporting.

#### Closing: a recruiting pitch (~01:09–01:10)

How does any of this get created? **Some through founding companies, some through founding nonprofits.** But fundamentally, what's needed is for a number of capable people — reality-warping people, the kind who set the reference points — **to ask themselves what needs to be built in the world for AI to play out well, and then go after building those new institutions and organizations.** The OpenAI Foundation, he notes, has tons of resources to support endeavors like that.

His last line hands the responsibility back to the audience: **whether or not AI resilience succeeds depends on the people in this room.**

### Quotes

> "That's an evidence that AGI is not yet here." (~01:00)

On the slides refusing to advance.

> "The great fire of London happened despite of curfews." (~01:04)

Capping a technology's capability is not the same as making it safe — the pivot the whole talk rests on.

> "It turns out that there wasn't a silver bullet. … It ends up being a multi-layer ecosystem approach." (~01:05)

The lesson from fire, and his thesis for AI.

> "It might not be sufficient to guardrail these capabilities within the frontier labs. … We might need to harden the environment itself." (~01:08)

Moving from *control the model* to *change the world* — precisely what separates resilience from safety.

> "Whether or not AI resilience will succeed depends on people in this room." (~01:10)

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| OpenAI Foundation | OpenAI 重組後的非營利母體,持有約 1/4 OpenAI 股權;AI resilience 為其部門之一 | The nonprofit resulting from OpenAI's restructuring, holding ~1/4 of OpenAI equity; AI resilience is one of its divisions | 講者為該部門負責人 / the speaker heads it |
| 空氣消毒 / Air sanitization | 生物風險的「硬化環境」代表做法:空氣消毒使病原體無法傳播 | Representative environment-hardening measure for bio risk: sanitized air prevents pathogen spread | 講者舉例,未指名特定計畫 / cited as an idea, no specific project named |
| 形式化驗證軟體 / Formally verified software | 資安層面的長期解:可證明的軟體,超級智慧也駭不進去 | The long-run cyber answer: provably correct software that superintelligence cannot hack | 與 Dawn Song 同場稍早的 security-by-construction 主張呼應 / echoes Dawn Song's security-by-construction argument earlier in the session |
| 航空業式公開事故資料庫 / Aviation-style public incident database | 事故公開通報 + 通報者取得 safe harbor | Public incident reporting with safe harbor for reporters | 講者提議的制度設計 / proposed institutional design |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Voych Zeremba / Voych | Wojciech Zaremba |
| non-conensual intimate images | non-consensual intimate images (NCII) |
| curfew ... uh like a 80% of London | 語序為自動字幕斷句造成 / sentence breaks are an artifact of auto-captioning |
| asmtote(panel 段) | asymptote |

## 待確認 / To Verify

- 「非營利持有約四分之一 OpenAI 股權」為講者口述的約略數字;公開報導的確切比例宜另行查證後補上。/ The "around one quarter" equity figure is the speaker's approximation; the exact publicly reported percentage should be confirmed and cited.
- curfew 的字源:講者說法文原意是「extinguish fire」,一般辭源解釋為 *couvre-feu*(「覆蓋火」)。此處照講者原話記錄。/ Etymology: he said the French means "extinguish fire"; standard etymology gives *couvre-feu*, "cover the fire". Recorded as spoken.
- 「倫敦被燒過四次」「大火吞噬約 80% 的倫敦」等歷史數字為講者口述,未附出處。/ The historical figures (London burned four times, ~80% consumed) were stated without a source.
- AI resilience 部門的具體資助領域與金額(演講中未提),可由 OpenAI Foundation 官方公告補充。/ The division's specific funding areas and amounts weren't given in the talk; can be supplemented from OpenAI Foundation announcements.
