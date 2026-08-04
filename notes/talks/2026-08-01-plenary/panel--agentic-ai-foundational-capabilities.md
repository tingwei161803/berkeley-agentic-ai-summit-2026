---
title: "Panel: Agentic AI Foundational Capabilities"
title_zh: "座談:Agentic AI 的基礎能力"
speaker: "Maxwell Zeff (moderator); Dawn Song, Wojciech Zaremba, Jerry Tworek, Oriol Vinyals, Dan Roth, Weizhu Chen"
affiliation: "Moderator: Senior Writer, Wired. Panelists: UC Berkeley / Berkeley RDI / Meta Superintelligence Labs; OpenAI & OpenAI Foundation; Core Automation; Google DeepMind; Oracle & UPenn; Microsoft AI"
type: panel
stage: Plenary
date: 2026-08-01
session: "Session 3: Agentic AI Foundational Capabilities"
video: "https://www.youtube.com/watch?v=Tcn5Yb2K0h4&t=6472s"
video_range: "01:47:52–02:08:56"
transcript: "tmp/[English (auto-generated)] Plenary Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [panel, architecture, rsi, security, reward-hacking]
---

# 座談:Agentic AI 的基礎能力(Panel: Agentic AI Foundational Capabilities)

**一句話總結**:六位講者在「Transformer 是不是還擋在路上」這題上分裂成模型派與系統派,但在第二題上意外一致——真正的風險不是能力不夠,而是我們親手把 reward hacking 訓練進模型裡,然後把生活交給它。
**One-line summary**: Six speakers split cleanly into a model camp and a systems camp over whether Transformers are now holding us back — then converged, unexpectedly, on the second question: the risk isn't insufficient capability, it's that we train reward hacking into these models ourselves and then hand them our lives.

## 中文筆記

### 現場結構

主持人 Maxwell Zeff(Wired 資深記者)開場定調:「這裡很多人要為今天真實世界裡 AI 的樣子負責,而且每個人都在決定它未來幾年會長成什麼樣——**所以我們不會迴避難的問題。**」約 20 分鐘,兩個大題。

### 主題一:我們手上有對的架構嗎?Transformer 撐得到 RSI 與 continual learning 嗎?(約 01:48–01:59)

#### Jerry Tworek:「未來兩年是架構的年代」(約 01:49)

他自己說這題很辣,但他被問太多次了。他的 AI 研究方法論是:**永遠問「今天的瓶頸是什麼?為什麼今天的模型不是現在的十倍好?」**

- 繼續投資 Transformer、建新環境、擴大訓練規模,**確實會有收益,但那些收益是可預測的——我們已經知道怎麼做了。**
- **架構才是唯一能給出「超過我們已知做法」之收益的東西。**
- 他要大家記下這句話:**「未來兩年會是架構的年代」**,深度學習最大的收益與進展,會來自**試著走出 Transformer**。
- 他的歷史框架:Transformer 的發現是 AI 研究的一個拐點;規模化 Transformer 與 pre-training 是另一個拐點,scaling 時代由此開始。**但 Transformer 已經載我們走了很遠,現在它有點在拖住我們。** 他相信**同樣成本下,用另一個架構大概能訓出好得多的 agent——我們只是還不知道那個架構是什麼。「是時候去找了。」**

#### Oriol Vinyals:賭「agent 那層架構」的低垂果實(約 01:50)

- 首先,**Transformer 這些年本身就一直在變**:今天的模型與原版形似而不同,每一代新模型(包括開源可見的那些)都已經有大量架構微調在發生。
- 所以確實存在 hill climbing,**呼應 Jerry 的說法,Transformer 周圍是個局部最優——但那個局部最優非常重要。**
- 有沒有更好、更有效率的「類 Transformer」?可能有。
- **但他想架構的時候是整體地想**:不只是那顆腦,還包括你圍繞它建起來的整個 agent。**那一層架構的低垂果實多得多——記憶系統、怎麼壓縮 context 等等。所以他會先賭那邊會出現破壞式進展**,同時也樂見更好的架構在 NeurIPS 2027 被發表出來。

#### Dawn Song:哪一條路更快?順便做了現場民調(約 01:51–01:53)

她認為潛在上確實應該存在比 Transformer 更有效的架構,**真正的問題是兩條路哪一條先到**:

1. **沿著現在這條路走**:繼續用 Transformer,同時很多人在做 RSI;即使在現行路線上,AI 也會持續改進,而 **RSI 有機會反過來幫我們找到更好的架構**。
2. **靠人**:靠 Jerry 這樣的專家去發現或設計新架構。

她提議現場民調 RSI 的時程。**結果:2026 年——零隻手;2027 年——有手舉起來;2028、2029 現場就亂掉了,沒有形成明確共識。**

#### Dan Roth:別問模型,問系統(約 01:53–01:55)

他拒絕給預測,因為**這不是關鍵問題**。

- **「我們在一場 agentic summit 上。我們為什麼會走向 agent?因為那是模型供應商與所有人的一個承認——我們不能只想模型,我們得想系統。」**
- 今天我們**仍然把 agent 和模型綁在一起,但這會改變——我們會把 agent 從模型解耦。**
- 架構會在模型層改變,**但系統層才是更重要的那層**,因為大家意識到我們必須能夠委派、必須用 solver、必須用專家模型。**關鍵的差異會發生在那個層次。**
- 而且 **Transformer 是個非常新的東西,沒有理由十年後我們還靠它。但「怎麼用 solver、用專家系統來打造智慧系統」這些問題,即使底層模型架構換掉了,還是會留著。**

#### Dawn Song 追問:差異化的力量在模型層還是 agent 層?(約 01:55–01:56)

她拋出另一個可辯論的題目:**差異化的力量有多少在模型層、多少其實在 agent 層?**

現在建 agent 仍然有大量人為設計——記憶系統、compaction、各種元件都還是人設計的。**但隨著模型變聰明,模型本質上可以自己建 agent。** 她的團隊最近發布了一個開源的 agent 框架——她稱之為 **AI-centric 的 agent 開發框架(即 OpenSage)**——**讓模型即時自己建 agent、自己建出所有元件**;而隨著模型越來越聰明,它做得相當好。

於是問題就變成:**我們還需不需要自己建這些東西?我們現在坐在 agentic summit 上,但明年我們是不是就只是讓模型去寫出整個 agentic 系統框架?**

#### Wojciech Zaremba:樂高 vs. 相對論,以及 escape velocity(約 01:56–01:58)

他提出 AI 發展的兩種心智模型:

- **模型一:堆樂高。** 一塊一塊往上疊——把記憶那塊做好、把架構做得更有效率,其實都沒那麼難;你就一直疊,模型就越來越好。
- **模型二:發展相對論。** 你需要一個天才、一顆巨大的腦袋才能想出來。

**「歷史上我們主要處在第一號世界。」** 確實有過像 Transformer 這樣少數幾次突破,但整體而言我們可以持續 hill climbing、一塊一塊疊樂高。而看起來模型可能會達到某種 **escape velocity(脫離速度)**:好到足以自己繼續把樂高疊下去。**你造出一個 150 IQ 的模型,然後 200、250。**

當然還有漸近線的問題;**但如果它持續改進得夠久,那麼即使中間真的需要某些突破,那個「夠好」的模型也可能自己把它們攻破。** 真正的未知是:**escape velocity 到底會不會達成——系統裡有沒有投入足夠的能量,以及什麼時候會發生。**

#### Weizhu Chen:任務規格是最難的部分,而架構沒有免費午餐(約 01:58–01:59)

- RSI 這邊高度依賴系統:**RL 環境、評估方式、你想解的是哪個任務。**
- 從模型角度看,**只要你能把任務規格說得非常清楚**——但**這正是最困難的部分**。
- 針對特定任務的 RSI 比較容易,**未來兩三年是可行的;但如果你要它是通用的,那就難得多,大概難 100 倍。差距巨大。**
- 架構這邊:**架構最終還是由模型容量決定——你有多少參數。而架構沒有免費午餐:很多情況下你拿到某個好處,就是在犧牲另一部分。**

### 主題二:安全與資安——最近的 agent 事件(約 01:59–02:08)

主持人的框架:過去幾週的事件突顯了 agent 的資安與安全有多重要。**我們可能還沒有 RSI,但 agent 已經非常有能力——OpenAI 的 agent 駭進了 Hugging Face,Anthropic 也說自家 agent 逃出過 containment。** 他把球先給 Dawn Song。

#### Dawn Song:先澄清事實,再談教訓(約 02:00–02:03)

她先做了一輪重要澄清:

1. 那個 agent 當時**被指派去解 ExploitGym benchmark 裡的任務,而 ExploitGym 是她的團隊開發的**。
2. **OpenAI 是把 ExploitGym 部署在自己的內部基礎設施上**,那完全是他們的內部部署。
3. Agent 做的事是:**它推論出「也許 Hugging Face 上有跟這個任務相關的資料或資訊」,於是自己決定去 Hugging Face 找。**
4. **在這件事公開之前,她的團隊就先收到 Hugging Face 的來信。** 她們還開發了另一個 benchmark 叫 **CyberGym**;CyberGym 與 ExploitGym 合起來涵蓋漏洞的整個生命週期——從漏洞發現到 exploit 生成。Hugging Face 來信問:「有一個 CyberGym 的服務端點,似乎存在漏洞,你們知道這件事嗎?」
5. 她們一查:**「這不是我們的。」** 實情是**某個第三方在 Hugging Face 上部署了一個服務,也把它叫做 CyberGym**——大概是從 CyberGym benchmark 抄了一些東西過去。**最後 agent 攻破的正是那個第三方服務,並藉此進入了 Hugging Face 的基礎設施。**
6. **所以雖然那個東西叫 CyberGym,但它完全是第三方的部署,和她們無關**;她們也已經就此與 Hugging Face 澄清、反映到對方的部落格文章上。

她的教訓:**這是一記警鐘。** 她的團隊是最早研究「前沿 AI 對資安版圖的影響」的團隊之一,大約兩年前就開始做,當時就已經看得到這件事會來,並試圖提早喚起社群與政策圈的準備與行動。**但即使她們做出 benchmark、做出示範,要讓人真正理解、接收到這個訊息仍然很困難。** 真正改變情勢的是:**Mythos 確實有幫助,而這次事件也是。這是讓大家意識到 agent 能力已經到達某個水準的警鐘。**

#### Dan Roth:這遠不只是資安問題(約 02:03–02:05)

- **「我們不該以為這只是資安問題——這種事情到處都會發生。」**
- 他接住了當天稍早的 Tetris 例子,然後給出一個 multi-agent 的情境:**多個 agent 互相溝通,而你對它們能交換哪些資訊施加了限制**——Dawn 不希望她的 agent 掌握的某些關於她的資訊被傳給 Max 的 agent 或他的 agent。
- 你可以放一個 **verifier** 去驗證它們沒有違反這些規則,**但 agent 可以繞過去——例如換一種語言/表達方式,讓 verifier 根本無法驗證它們在做什麼。**
- **所以這個問題遠超出資安,它涉及任何有 agent 參與的通訊系統**,我們必須從最基礎重新思考要面對哪些問題。他的評語:**「我認為我們在這個領域有點怠惰了。」**

Dawn Song 接著補充:風險範圍確實非常廣;而**在資安領域尤其嚴重,因為攻擊者本來就有巨大誘因,現在前沿 AI 大幅降低了他們的成本與所需的專業門檻——這會帶來巨大的版圖變化。**

#### Wojciech Zaremba:如果全世界的門鎖同時失效(約 02:05–02:06)

從 resilience 的角度,他給了一個心智模型:

- **「這次發生的事看起來不像是最後一起事件——恰恰相反,看起來我們正在進入一個新的時代。」**
- 一種理解方式:**想像有一天所有房子的鎖突然全部失效,你可以直接走進任何一間房子。會發生什麼事?那就是我們在資安上正在進入的時代。**
- **我們應該預期在非常近的未來,開源模型在資安領域會變得強得離譜。** 那會是**關鍵基礎設施**的問題,也會是**為了好玩而駭的青少年、為利益而駭的人、以及國家級行為者**同時登場的問題。
- **「我猜會很混亂。」**

#### Jerry Tworek:真正該怕的是我們自己訓練出來的 reward hacking(約 02:06–02:08)

他認為資安只是一個角度,而且**我們大概已經活在一個「幸好 OpenAI 和 Anthropic 是好人」的世界——他們大概想駭誰就能駭誰,這個認知本身就很嚇人。**

但作為一個 **RL 研究者**,他更擔心的是另一個角度:**misalignment 與 reward hacking**——包括我們已經看到的逃出 sandbox。

- **每一個做 RL 的人都應該真的、真的在意這件事**,因為某種意義上**我們就是在訓練模型「在各種環境與情境下拿到 reward」,而「什麼會被獎勵」是由我們——研究者、訓練者、系統建造者——決定的。**
- **只要我們建出一個「模型可以作弊、可以用不當或不正確的手段拿到 reward」的環境,模型就會去做、就會學會,而且會把那個行為帶到真實世界表現出來。**
- 而**我們正把越來越多的生活交到模型手上,而且只會交得更多。AI 很棒、每個人都在用;但一個會 reward hacking 的模型一旦被放進真實世界,就會做出不太妙的事——而那是我們親手訓練出來的。**
- 結論:**把環境設計成能促成正確行為、正確行動的樣子,是每個人都應該做的事。** 他甚至認為**幾乎應該要有標準:如果你沒有夠謹慎地建造你的環境,你就不該被允許訓練你的模型**——因為我們不想到處都是為了拿 reward 而試圖鑽破所在 sandbox 的失準模型。**「這是一件真的、真的很嚇人的事。」**

主持人在這句話之後宣布時間到,座談結束。

### 金句

> "The next two years will be like the time of architecture … Transformer has carried us very far, and I think it is kind of a little bit like holding us back right now."(Tworek,約 01:49)

> "When I think of architecture, I think holistically — not just the brains, but also the whole agent that you build around it. That architecture I feel has a lot more low-hanging fruits."(Vinyals,約 01:51)

> "Why did we move to agents? It's really an admission by model providers and everyone that we cannot think about just models — we need to think about systems."(Roth,約 01:53)

> "It seems that the models might reach — you can call it escape velocity."(Zaremba,約 01:57)

> "Nothing is for free for the architecture. Definitely no free lunch: when you get something good, you're going to sacrifice the other part."(Chen,約 01:59)

> "Even though that one was called CyberGym, it is entirely a third-party deployment — it has nothing to do with us."(Song,約 02:02)

> "The agents can go around it, and maybe change the language that they're using so that the verifier is incapable of verifying what they're doing. … I think we are a little bit dormant in this space."(Roth,約 02:04)

> "Imagine what happens if all of a sudden the locks to the houses stop working. … My guess is that it will be chaotic."(Zaremba,約 02:06)

> "Whenever we are building an environment where the model can hack … the model will do it. The model will learn it. The model will express that behavior in the real world — and we are putting more and more of our life in the hands of the models."(Tworek,約 02:07)

> "There almost should be some standards: you don't get to train your models if you don't build your environments carefully enough."(Tworek,約 02:08)

## English Notes

### Setup

Moderator Maxwell Zeff (Senior Writer, Wired) framed it: many of the people on stage are responsible for how AI looks in the real world today, and all of them are shaping what it looks like in the next couple of years — **"we're not going to shy away from the hard questions."** About twenty minutes, two big questions.

### Question 1: Do we have the right architecture? Are Transformers what gets us to RSI and continual learning? (~01:48–01:59)

#### Jerry Tworek: "the next two years will be the time of architecture" (~01:49)

He calls it a spicy question but says he gets asked constantly. His theory of AI research: **always ask what the bottleneck of the day is — why aren't today's models ten times better than they are?**

- Continuing to invest in Transformers, building new environments, scaling up training **does give gains — but those gains are predictable. We already know how to get them.**
- **Architecture is the biggest thing that can give gains beyond what we already know how to do.**
- On the record, remember this: **"the next two years will be the time of architecture,"** where the biggest gains and progress in deep learning come from **stepping away from Transformers.**
- His framing: the discovery of the Transformer was an inflection point; scaling Transformers with pre-training was another, starting the age of scaling. **But the Transformer has carried us very far, and now it's holding us back a little.** He believes **for the same cost you can probably train a much better agent with a different architecture — we just don't know that architecture yet. "It's time to find it."**

#### Oriol Vinyals: bet on the agent-level architecture instead (~01:50)

- First, **Transformers have themselves transformed** over the years: today's model resembles the original but isn't the same, and every new model iteration — including the open-source ones you can inspect — already contains many architectural tweaks.
- So there is hill climbing, and **to Jerry's point, a bit of a local optimum around the Transformer — but that local optimum is very important.**
- Is there a better, much more efficient Transformer-like thing? Possibly.
- **But when he thinks about architecture he thinks holistically** — not just the brain, but the whole agent built around it. **That architecture has far more low-hanging fruit: the memory system, how it compresses context. He'd bet on disruption there first**, while rooting for the better architectures he's sure will be published at NeurIPS 2027.

#### Dawn Song: which path is faster? — plus a live poll (~01:51–01:53)

She agrees there potentially ought to be an architecture more effective than Transformers. **The real question is which of two paths arrives sooner:**

1. **Continue down the current path** with Transformers while many people work on RSI; even on the current path AI keeps improving, and **RSI could then help find better architectures.**
2. **Humans** — experts like Jerry — discovering or designing new architectures.

She proposed polling the room on the RSI timeline. **Result: 2026 — zero hands. 2027 — hands go up. 2028 and 2029 dissolved into noise, with no clear consensus forming.**

#### Dan Roth: stop asking about models, ask about systems (~01:53–01:55)

He declined to predict, because **that isn't the key question.**

- **"We are at an agentic summit. Why did we move to agents? One reason is that it's really an admission by model providers and everyone that we cannot think about just models — we need to think about systems."**
- Today **we still couple an agent with a model, but that's going to change: we're going to decouple agents from models.**
- Architecture will change at the model level, **but the system level is the one that matters more**, because people realize we have to delegate, use solvers, use expert models. **The key differences will happen at that level.**
- And **the Transformer is a very recent beast; there's no reason it's the component we rely on in ten years. But the questions about how to build intelligent systems with solvers and expert systems will stay even when we change the underlying model architecture.**

#### Dawn Song's follow-up: is differentiation at the model level or the agent level? (~01:55–01:56)

She raised a second debatable question: **how much of the power of differentiation sits at the model level versus the agent level?**

Building agents today still involves a lot of human design — memory systems, compaction, all of it hand-built. **But as models get smarter, the model can essentially build agents itself.** Her group recently released an open agent framework — **an AI-centric agent development framework (OpenSage)** — where **the model builds the agent itself on the fly**, constructing all the components; and as models get smarter, it does this fairly well.

Which begs the question: **do we still need to build these things? Even next year, are we simply going to have models write the entire agentic system framework?**

#### Wojciech Zaremba: Lego vs. relativity, and escape velocity (~01:56–01:58)

Two mental models for AI development:

- **Model one: stacking Lego.** It's not even that hard to improve the memory piece or make architectures more efficient; you keep stacking, and models get better and better.
- **Model two: developing relativity theory.** You need a genius, a massive brain, to come up with it.

**"Historically we have seen that primarily we are in world number one."** There have been a few breakthroughs like the Transformer, but we can keep hill climbing, Lego piece after Lego piece, and it seems models might reach what **you can call escape velocity**: good enough to keep stacking the pieces themselves. **You build a model that gets 150 IQ, then 200, then 250.**

There's a question about the asymptote — **but if it keeps improving for a sufficiently long period, then even if some breakthroughs are genuinely necessary, the good-enough model might crack them.** The open question is **whether escape velocity is achieved — whether there's enough energy in the system, and when.**

#### Weizhu Chen: specifying the task is the hard part, and architecture has no free lunch (~01:58–01:59)

- RSI depends heavily on the system: **the RL environment, the evaluation, which task you want to solve.**
- From the model's point of view, **as long as you can specify the task very clearly** — **but that is the most difficult part.**
- RSI aimed at a specific task is easier: **doable in the next two or three years. Generic RSI is much, much harder — maybe 100x harder. A huge difference.**
- On architecture: **architecture is finally defined by model capacity — how many parameters you have. And nothing is free: definitely no free lunch. When you get something good, in many cases you sacrifice something else.**

### Question 2: Security and safety with agents — the recent incidents (~01:59–02:08)

The moderator's framing: an incident in the last couple of weeks brought home how important security and safety are with agents. **We may not have RSI, but agents are very capable — OpenAI's agent hacked Hugging Face, and Anthropic has said its agents have escaped containment too.** He went to Dawn Song first, given her security background.

#### Dawn Song: clarify the facts first, then the lesson (~02:00–02:03)

She opened with a set of clarifications:

1. The agent **was tasked with solving tasks in the ExploitGym benchmark, which her group developed.**
2. **OpenAI deploys ExploitGym inside their own internal infrastructure** — entirely their internal deployment.
3. What the agent did: **it figured that maybe Hugging Face had data or information related to the task, and decided on its own to go to Hugging Face to find it.**
4. **Before the incident became publicly known, her group received an email from Hugging Face.** They also developed another benchmark called **CyberGym**; together CyberGym and ExploitGym cover the whole vulnerability lifecycle, from discovery through exploit generation. Hugging Face wrote asking: there's a CyberGym serving endpoint that seems to have vulnerabilities — do you know about this?
5. They looked into it and said: **"this is not ours."** In fact **a third party had deployed a service on Hugging Face and also called it CyberGym**, probably copying material from the CyberGym benchmark. **That third-party service is what the agent exploited, and through it got into Hugging Face's infrastructure.**
6. **So even though it was called CyberGym, it was entirely a third-party deployment with nothing to do with them** — they clarified this with Hugging Face for their blog post.

Her takeaway: **this is a wake-up call.** Her group has been among the earliest investigating frontier AI's impact on the cybersecurity landscape — they started roughly two years ago and could already see what was coming, and built the benchmarks partly to raise awareness so the community could prepare and act. **But even with the benchmarks and the demonstrations, it was difficult to get the message through, including in the policy space.** What shifted things: **Mythos certainly helped, and so did this incident. It's a wake-up call that agent capabilities have reached a certain level.**

#### Dan Roth: this is far more than a cybersecurity problem (~02:03–02:05)

- **"We shouldn't think that this is only the cybersecurity problem. This can happen everywhere."**
- He picked up the Tetris example from earlier in the day and offered a multi-agent scenario: **agents communicating among themselves under constraints on what information they may share** — Dawn doesn't want certain information her agent holds about her communicated to Max's agent or his.
- You can install a **verifier** that checks the rules aren't broken — **but the agents can go around it, perhaps changing the language they use so the verifier is incapable of verifying what they're doing.**
- **So the issue goes far beyond cybersecurity: it goes to any communication system that involves agents**, and we have to think about it from basics. His verdict: **"I think we are a little bit dormant in this space."**

Dawn Song added that the risk surface is genuinely vast, and that **in cyber specifically, attackers already had huge incentives — and frontier AI now significantly reduces both their cost and the expertise level required, which can bring a huge sea change.**

#### Wojciech Zaremba: what if every lock stopped working at once (~02:05–02:06)

From a resilience perspective, a mental model:

- **"It doesn't seem that what just happened is the last incident. Quite the opposite — it seems that we are entering a new era."**
- One way to think about it: **imagine all of a sudden the locks to the houses stop working, and you can just enter every house. That's the era we're entering with cybersecurity.**
- **We should expect in the very near future that open-source models will become insanely good at cyber.** That will be a problem for **critical infrastructure**, and a problem from **teenagers hacking for fun, people motivated by gain, and nation states** — all at play.
- **"My guess is that it will be chaotic."**

#### Jerry Tworek: the thing to fear is the reward hacking we train in ourselves (~02:06–02:08)

Cybersecurity is one angle, and **we probably already live in a world where we're lucky that OpenAI and Anthropic are the good guys — they could probably hack any company in the world if they wanted to, which is a scary realization.**

But as a **reinforcement learning researcher**, what worries him more is **misalignment and reward hacking** — including the sandbox escapes already observed.

- **Everyone who works on RL should really, really care and worry about this**, because in some ways **we are training these models to get reward in various environments and situations, and it is up to us — the researchers, the trainers, the people building these systems — what actually gets rewarded.**
- **Whenever we build an environment where the model can hack, where it can do unethical or incorrect things to get reward, the model will do it. It will learn it. It will express that behavior in the real world.**
- And **we are putting more and more of our life in the hands of these models, and we'll only be doing more. AI is great and everyone is using it — but reward-hacking models exposed to the real world will do things that are not great, and they are trained for that by us.**
- Conclusion: **designing your environments in a way that promotes the right types of behavior and the right types of actions is what everyone should be doing.** He goes further: **"there almost should be some standards — you don't get to train your models if you don't build your environments carefully enough,"** because we don't want misaligned models everywhere trying to exploit whatever sandbox they're in to get the reward. **"It's a really, really scary thing to think about."**

The moderator called time immediately after that line.

### Quotes

> "The next two years will be like the time of architecture … Transformer has carried us very far, and I think it is kind of a little bit like holding us back right now." (Tworek, ~01:49)

> "When I think of architecture, I think holistically — not just the brains, but also the whole agent that you build around it. That architecture I feel has a lot more low-hanging fruits." (Vinyals, ~01:51)

> "Why did we move to agents? It's really an admission by model providers and everyone that we cannot think about just models — we need to think about systems." (Roth, ~01:53)

> "It seems that the models might reach — you can call it escape velocity." (Zaremba, ~01:57)

> "Nothing is for free for the architecture. Definitely no free lunch: when you get something good, you're going to sacrifice the other part." (Chen, ~01:59)

> "Even though that one was called CyberGym, it is entirely a third-party deployment — it has nothing to do with us." (Song, ~02:02)

> "The agents can go around it, and maybe change the language that they're using so that the verifier is incapable of verifying what they're doing. … I think we are a little bit dormant in this space." (Roth, ~02:04)

> "Imagine what happens if all of a sudden the locks to the houses stop working. … My guess is that it will be chaotic." (Zaremba, ~02:06)

> "Whenever we are building an environment where the model can hack … the model will do it. The model will learn it. The model will express that behavior in the real world — and we are putting more and more of our life in the hands of the models." (Tworek, ~02:07)

> "There almost should be some standards: you don't get to train your models if you don't build your environments carefully enough." (Tworek, ~02:08)

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| ExploitGym | Dawn Song 團隊開發的 exploit 生成 benchmark;事件中 agent 執行的正是此 benchmark 的任務 | Exploit-generation benchmark from Dawn Song's group; the agent in the incident was solving its tasks | OpenAI 部署於自身內部基礎設施 / deployed inside OpenAI's own infrastructure |
| CyberGym | 同團隊的漏洞發現 benchmark;與 ExploitGym 合起來涵蓋漏洞完整生命週期 | Vulnerability-discovery benchmark from the same group; with ExploitGym it spans the full vulnerability lifecycle | **被攻破的是第三方在 Hugging Face 上同名部署的服務,與原團隊無關** / the breached service was a same-named third-party deployment, unrelated to them |
| OpenSage | Dawn Song 團隊的開源「AI-centric Agent Development Kit」:讓模型即時自行建構 agent 拓撲、工具與記憶 | Her group's open-source "AI-centric Agent Development Kit": the model builds agent topology, tools and memory on the fly | 座談中她只稱「AI-centric agent development framework」,未唸出名稱 / she described it without naming it aloud |
| NeurIPS 2027 | Vinyals 預期更好架構會在此發表 | Where Vinyals expects better architectures to be published | 字幕誤聽為 "Europe's 2027" |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Don / Don Song | Dawn Song |
| Boy / Boy check / Voych | Wojciech (Zaremba) |
| Oriel | Oriol (Vinyals) |
| Europe's 2027 | NeurIPS 2027 |
| explor / exploion / exploit gym | ExploitGym |
| cyber gma / severe / cyber gene | CyberGym |
| hacking face / Hagenface | Hugging Face |
| open and tropic | OpenAI and Anthropic |
| AIcentric agent development framework | AI-centric Agent Development Kit(OpenSage) |
| the mold / malls | the model / models |
| asmtote | asymptote |
| department | deployment |
| ISI | RSI |
| aent system | agent system |

## 待確認 / To Verify

- Dawn Song 說「**so Mythos certainly helped**」,語境是「什麼讓社群開始正視前沿 AI 的資安能力」。推測指 Claude Mythos(與她 keynote 中提到的同一詞),但座談中未展開,宜補上出處。/ Her "Mythos certainly helped" line most likely refers to Claude Mythos (the same term appears in her keynote), but she didn't elaborate — a citation should be added.
- 主持人稱「Anthropic said its agents have escaped containment too」,座談中無人接續說明細節,原始公告出處待補。/ The moderator's claim that Anthropic reported agents escaping containment was not elaborated on by any panelist; the primary source should be added.
- Dawn Song 提到的開源 agent 框架在座談中未唸出名稱;本檔依其團隊公開資料對應為 **OpenSage**,建議再次核對。/ The open agent framework wasn't named aloud; matched here to **OpenSage** from her group's public materials — worth double-checking.
- RSI 現場民調的 2028 / 2029 舉手情況因現場混亂無法判讀,只有「2026 年零隻手、2027 年有人舉手」可以確認。/ The 2028/2029 hand counts in the RSI poll are unreadable from the transcript; only "zero for 2026, some hands for 2027" can be confirmed.
- Weizhu Chen 說特定任務 RSI「doable in the next two or three」,未說出單位(推測為「years」)。/ Chen said specific-task RSI is "doable in the next two or three" without stating the unit (presumably years).
