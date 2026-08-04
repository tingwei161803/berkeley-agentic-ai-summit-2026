---
title: "Building Agentic Apps End-to-End with Replit Agent"
title_zh: "用 Replit Agent 端到端打造 Agentic 應用"
speaker: "Brandon Middleton"
affiliation: "Head of Education, Replit"
type: workshop
stage: Atlas
date: 2026-08-01
session: "Session 2: Robotics & World Models"
video: "https://www.youtube.com/watch?v=psPzCQbjCCo&t=8075s"
video_range: "02:14:35–03:13:54"
transcript: "tmp/[English (auto-generated)] Atlas Stage - August 1st - Afternoon Session [DownSub.com].srt"
status: draft
tags: [education, ai-literacy, vibe-coding, replit, assessment]
---

# 用 Replit Agent 端到端打造 Agentic 應用(Building Agentic Apps End-to-End with Replit Agent)

**一句話總結**:這場名為「用 Replit Agent 蓋 app」的 workshop,實際上有四分之三在談教育——當資訊與智慧都變得充沛,大學那套「用時數換學習、用學歷換能力、用排序換教育」的設計就失效了;而 vibe coding 的意義不是省下寫程式的時間,是讓一個 15 歲高中生、一個沒有 CS 背景的音樂人、甚至 Shaquille O'Neal,都能把自己的想法直接做成能用的東西。

**One-line summary**: A workshop billed as "build apps with Replit Agent" spends three quarters of its time on education — because once information *and* intelligence are abundant, a university built on trading time served for learning, credentials for capability, and sorting for teaching stops working; and the point of vibe coding isn't saving keystrokes, it's letting a 15-year-old, a musician with no CS background, or Shaquille O'Neal turn an idea into something that runs.

> 場次備註:議程排在 15:30 的一小時 workshop,實際從影片 02:14:35 開始、03:13:54 結束。開場約 5 分鐘為 trivia 送贈品與投影機/螢幕的技術狀況(02:16–02:20),講者自嘲「可以給我一個掌聲鼓勵這個連投影都搞不定的技術人嗎」。
> Session note: the scheduled 3:30 PM one-hour workshop actually ran 02:14:35–03:13:54. The first ~5 minutes are trivia giveaways and projector trouble (02:16–02:20) — "can I have a round of applause for being the tech guy that cannot even..."

## 中文筆記

### 講者自介與這場的定位(約 02:20–02:22)

Brandon Middleton 是 Replit 的 Head of Education。他先講了兩件跟履歷無關的事:11 年前他以「第一個用嘻哈 rap 完成畢業致詞的人」進了金氏世界紀錄(Haas 的 evening & weekend MBA,2015 年畢業);以及他在 Amazon(AWS,待了六年)、Microsoft 等地方任職期間,都一直在本業之外教書——到了 Replit 才第一次能**全職**做這件事。他現在的守備範圍是大學、K–12 與非營利組織,主題是「怎麼把 AI 素養變成實際可操作的東西」。

他把這場定調成**同時是演講也是示範**:一邊談教育,一邊用 Replit 把應用蓋出來。開場他請全場舉手:研究/自認是技術人的一大片,而**自認非技術、但有在 vibe coding 的也不少**——他說這場會同時照顧兩邊。

第一個 demo 就是他**當天早上用 Replit Agent 做的一個 app**:全場打開一個網址、上傳照片與留言,照片就即時出現在大螢幕的「scroll wall」上。他用這個現場運作的東西當作 agentic AI 的最小示範,後面也用同一個 app 來講資料庫、部署與 API。

### 主題一:大學的設計前提已經不成立了(約 02:24–02:30)

他在 Stanford d.school 每年春季開一門叫 **Redesigning Finance** 的課,學生會拿學費與體驗的落差開他玩笑。他認為玩笑之所以好笑是因為有真的成分:「**我相信美國夢、我照著所有人告訴我的去做,它就會給我一份工作**」這個信念正在消退。

他的核心論證是:**現行教育系統其實設計得很好——只是它是為幾百年前的世界設計的。**

- 當年**資訊是稀缺的**:你必須來到大學,才能從教授那裡取得資訊;知識鎖在圖書館、實驗室與講堂裡。
- 當年「**記得答案**」就是學習的證據。今天不是了——你可以有一堆書本知識而沒有街頭智慧,可以觀察到一堆東西但那些全是錯誤資訊或假訊息。
- 今天**資訊到處都是,答案是充沛的,而且智慧本身也正在變得普遍而充沛**:模型成本在掉、模型智慧在快速變好。

於是他丟出那個讓機構不舒服的問題:**如果我們今天——2026 年夏天——拿一張白紙重新設計大學,我們會怎麼做?**

- 還會把一切繞著講堂與圖書館組織嗎?
- 還會是 16 週一學期嗎,還是應該更短?
- 還要點名嗎?出席在未來的教育裡還重要嗎?
- 期末考的閉卷回憶與死背,是要留著還是丟掉?

他的判斷是三個「搞混」:**我們把「在校時間」跟「學習」搞混了,把「文憑」跟「學生真正的能力」搞混了,有時候還把「花四五年把學生排序」跟「教育學生」搞混了。** 結果大學變成一套**極度昂貴的排序系統**——用招生排序、用成績與科系排序、有時候直接用學校本身排序——而四五年後的產出,我們稱之為 merit,並且真的據此決定錄不錄用一個人。

### 主題二:AI 素養巡迴與現場的訊號(約 02:26–02:33)

Replit 做了一個他稱為 **AI literacy tour** 的計畫,已經走過**芝加哥、紐約、洛杉磯、亞特蘭大與灣區**,由下而上地問:**現在當一個學生是什麼感覺?當一個老師、拿著上級交下來的 AI 命令、要把 AI 素養翻譯成對自己與學生有意義的東西,又是什麼感覺?** 訪談對象從幼稚園老師一路到 R1 大學的研究者與教授。

他放的一張照片是東帕羅奧圖(East Palo Alto)的社區工作坊:同一個房間裡從 **7 歲到 77 歲**,一起討論當地的資源分配問題。他用便利貼和手機把 7、8 歲小孩說的話和 75、76 歲長者說的話一起收下來,再用 Replit 上傳到一個應用裡、**把 AI 當夥伴一起思考**——重點是讓那些不自認是工程師或資訊科學家的社區成員,親眼看到這件事有多容易。

同時,職場端傳來的訊號相當嚴峻:

- 2026 年初,**年輕的應屆大學畢業生失業率約 5.7%**。
- 更刺眼的是**約 41.5% 屬於低度就業(underemployed)**——「我可能從一間很不錯的學校畢業,但我做的工作遠低於我的智識能力,甚至低於我的興趣。」
- 世界經濟論壇的報告指出,**接近 40% 的勞工現有技能預期會在 2026 到 2030 年之間改變**;他換算成:如果用 100 個人代表全球 80 億人,**其中 59 人得在未來四年內轉換、再訓練、重新轉向。**

他強調這**不代表大學本身沒有價值**,而是「**教育、學生能力、與機會這三者之間的連結,目前處於高度張力狀態**,而我們必須把它解掉。」

他自己的路徑就是論證:UIUC 電機系畢業 → 到灣區進 Cisco 當網路軟體工程師 → Haas MBA(2015)→ 之後放下了不少程式與產品管理的技能 → 離開 AWS 加入 Replit 後,又把設計、工程、產品管理這個三角裡的技能撿回來。所以他的結論是:**learn、unlearn、relearn 才是核心技能。**

### 主題三:AI 不是下一個 edtech 小工具(約 02:33–02:40)

他刻意把 AI 跟計算機、跟 2003 年的 Google 搜尋區隔開來:AI 當然可以自動化批改、論文摘要、生成教案,**但他認為 AI 給的是一個「百年一遇、把教育重新繞著人的潛能重建」的機會。**

他相信每個人都有一種天生的熱情、渴望與能力,能對這 80 多億人交付某種東西;而 vibe coding 與 agentic AI 可以幫人達到自己的巔峰狀態。**「人類史上第一次,想像每個人都有 agentic 助理與個人家教,是真的可能在幾年內實現的事。」**

他特別指出這件事的**分配面**:在帕羅奧圖,他的鄰居會把小孩送去週六學校、下午三點放學但六點才到家,因為排滿了 STEM 家教。「**懂得navigate這套系統的家長,他們的小孩其實過得很輕鬆。**」他真正在意的是另一邊——那些**在滿座的講堂裡沒有自信舉手**的學生。24 小時全天候的個人家教意味著:

- 凌晨兩點那個太害羞、不敢在課堂上舉手的學生,可以問到問題;
- 需要**用另一種方式解釋**的學生有選擇(視覺型 vs 聽覺型;口試表現好 vs 限時筆試);
- 需要各種學習調整(accommodations)的學生能拿到,而且**不必承受尷尬、疲憊或來自老師與同學的評價**——尤其當老師本來就處在一對多的場合裡。
- **多語言支援**:他自嘲住灣區 21 年、只會英文,「會兩種以上語言的請舉手——所以基本上我輸給你們全部人。」但他認為 agentic AI 在這裡幫得上忙:你可以用英文、法文、西班牙文或任何母語對 Replit 說話,再把成果翻譯給互動另一端說不同語言的人。

**但他明確反對「取代老師」的框架**:這是**擴大一個老師能觸及的範圍**——面對 15 人、50 人、100 人的班級。當老師從 broadcaster 變成**設計者、教練、導師、評論者與社群建立者**,學生反而有更多空間長出領導力與主導權。「**AI 絕對可以傳遞資訊,但老師要做的、也是真正重要的,是那種很個人的關心與在意**——那個常常無形的東西,那個老師對學生的信任,會讓學生願意多熬兩小時把東西做完,或對自己交出去的作品產生驕傲。」

他用一個非典型的學生案例補充「教育」的邊界:一位簽在唱片公司十年、發過三張專輯、拿過葛萊美的音樂人,五年前解約後來到 Replit 辦公室——他問的不是 agentic AI 的技術問題,而是**他想自己開一家唱片公司**,解決當年困擾他的那些事,例如**串流版稅的收入認列**(在 Spotify、YouTube Music 上串流一次只拿到幾分之一美分),以及他去稽核自己該拿多少錢時被踢皮球、被掃到地毯下的種種錯誤。他沒有 CS 背景,就用 vibe coding 來重新想像音樂產業的這一塊。「即使他不屬於任何一所大學,這在我的守備範圍裡**仍然算教育**——音樂教育、商業教育、科技教育。」

### 主題四:那評量要怎麼改?(約 02:48–02:52)

他的立場很直接:**「考試差不多已經死了。」**

在他自己的 Redesigning Finance 課上,他要求學生**錄 5 到 7 分鐘的 YouTube 影片**,講自己如何跟一個金融主題搏鬥。去年的題目之一是:如果你要重新設計再保險與保險業、改善**理賠人**的體驗,面對下一場洛杉磯野火或下一次佛州洪水,你會在**理賠人層級、保險公司層級、再保險公司層級**分別怎麼設計?學生得**真的做出東西**,然後**同步口頭辯護**自己做的東西。「所以除非他們已經精通 deepfake,不然他們是真的把功夫花在想清楚、做出原型,再把影片放在旁邊一起交。」

**他也重新設計了打分方式**:全部是小組作業,但會依學生**年級**(大一到碩士)與**背景**(工程本科 vs 剛接觸技術的新手)做**適性化**評分,評分維度包含**設計的完成度**,以及**協作程度——而且是由組員互評決定,不是由老師與助教判斷。**

他認為該問的問題整個換掉了。不該再問「**這個學生有沒有用 AI?**」,而該問:

- 這個學生**真的思考過**嗎?
- 他**驗證**過自己交出去的東西嗎?
- 他**標註來源**、說明東西從哪來了嗎?
- 他**改進**過那個成果嗎?
- 他能**解釋**自己為什麼做這些決定與取捨嗎?
- 他能**為結論辯護**嗎?
- 他能告訴我們**機器在哪裡出錯了**嗎?——這一項是在用他自己的判斷力與領域專業去評斷機器說的話。

具體做法:**每個重要的個人或小組專案之後都安排一次口頭辯護**;學生交的不只是一個最終答案,而是**一份被追蹤下來的推理紀錄**。他在 Replit 裡蓋了一套系統讓學生回顧課堂、交作業並追蹤這個歷程——「**兩堂課之間你可能學到很多,兩次考試之間你可能學到很多,而傳統系統根本捕捉不到那些時刻。**」

他還舉了兩個「作品比領域專業重要」的例子:

- 舊金山一場生醫黑客松,學生用 Replit 做**生物標記發現**與藥物探索相關的東西。他坦承自己分子細胞生物學與化學都不強,但身為評審,他的回饋聚焦在**他們對解法想得多深、訪談了多少人、流程如何**,而不是領域知識。「我們就算不深入某個領域,也能用自己的生命經驗與觀點,讓學生做的東西變得更好一點。」
- 芝加哥 Holy Trinity High School 的 **Jack,15 歲**,通勤 25–30 英里上學。校長去年春天讓學生用 Replit,Jack 把學校重視的**價值與行為準則**做成一套系統交給老師:老師直接用**手機**標記符合校方價值的模範行為,學生累積 **XP**,並在**學生早上下校車走進大廳時的數位看板上顯示排行榜**,XP 還能在校內兌換特別的東西。「一個 vibe coding 平台被用來**改變一所學校的文化與環境**。」
  而當他問 Jack 怎麼看待學 AI 這件事,Jack 拆成三層:**learning with AI**(把它當家教、協作者、評論者、翻譯)、**learning about AI**(資安、治理、模型與演算法怎麼運作——來自全校唯一一位做過深度專業進修的老師,再由他帶給高二到高三學生)、以及 **learning beyond AI**(為了把應用透過藍牙串到數位看板而學的東西,以及學校周邊社區的影響與議題)。他覺得這三層很值得當起手式,而且可以延伸到醫學、司法、資源分配等遠超出教室的領域。

他也誠實地說,這個話題很快會變成**哲學與意識形態的討論**:社會裡長期存在的經濟不平等、貧窮、戰爭等問題,**不是技術能治好的**,金錢有時是因素但也解不完。他希望能跟社群與學生談這些,而不只是給 AI 素養的技術基礎。

### 主題五:Replit 平台導覽(約 02:42–02:48、03:04–03:12)

他請一位觀眾用一句話解釋 Replit 給沒用過的人,得到的答案是:**「從想法到做出 AI 應用,而不需要懂底下的技術。」** 他很滿意這個定義。

介面上他實際點過的東西:

- **prompt box**:跟 ChatGPT 或 Claude 的互動方式類似;旁邊有 **import**,可以把在別處已經做的東西匯進來。
- **511 個整合/連接器**(個人與企業版):Dropbox、Discord、Slack、Google Drive、Databricks、Google Sheets 等。「先把這些接起來再開始蓋,比較好玩」——你可以直接說「去拿我的 Google Drive、Dropbox、Databricks 跟 Google Sheets,我要做一個做 XYZ 的應用」。
- **產出類型**:網站、行動 app、設計、遊戲、簡報。**這場的投影片本身就是他用 Replit 做的。** 知道要做什麼就點對應的按鈕,可以把模型往那個方向導。
- **Learn 與文件**(左下角):他們花了不少功夫做影片內容,把人從 0 帶到 100,再從 100 往上一點。
- **模式**:**Lite**(基本問題,例如「把投影片背景從黑色改成橘色」「把這頁文字改掉」)、**Economy**(預設的中間檔推理與智慧)、**Power**(要做非常有企圖心的事情時)。**每個模式都還能點進去選封閉或開源模型**——「為你要做的事挑對模型,是這個體驗的一部分。」

最後 10 分鐘他做了一輪 **vibe coding 101**,大致是端到端蓋 app 的順序:

1. **多人協作**:workspace 上方有 invite 按鈕,可以邀請其他開發者**對同一份程式碼一起下 prompt**——「就像四五六個人一起編一份 Google Doc,只是你們在一起蓋軟體。」
2. **第一個 prompt**:他都讓新手從**個人作品集頁**開始——「做個東西幫我表達我的職涯成果」,丟一張自己的照片進去,讓它做。
3. **Publish**:把 hosting、資料庫、資安掃描這些「從 localhost 到可部署」需要的基礎設施全部抽象掉,讓任何人點網址都能用。
4. **加資料庫**:「你們剛才能上傳照片,是因為它不只是一個前端頁面。」他當場打開 **Tools → Database**,展示 Replit 同時有**開發資料庫**(publish 前測試用)與 **production 資料庫**;現場的開發庫有 22 列、production 有 32–33 列,「這就是本地做跟 publish 到全世界的差別。」
5. **加 API**:天氣、股票時間序列、Shopify,或任何你喜歡的服務,讓 app 每次載入時把資料拉進介面。
6. **加認證**:他說**整場最短、卻能做到最酷的事的一句話是「add Replit Auth to my app」**——五六個字就會生出一個登入入口,支援 Google、Apple 等常見登入方式,使用者從此可以記錄自己的 session、照片與文字。

他在最後留了 **vibe coding 的限制**,講得相當坦白:

- **你還是得懂一點產品怎麼做**,不然做不出來。
- **你會遇到看不懂的錯誤**:做法是**截圖直接拖進介面**,說「我不知道這是什麼、怎麼修」——「**幫你蓋東西的那個 Replit Agent,就是你可以問問題、把自己解卡的同一個 agent**,你不必等到有人類能來幫你。」
- **複雜度與技術債**:他認為這張清單上**最有用的技能是 debugging**;如果你不是技術背景,學會它就是大量的 trial and error,是你會跟 agent 一起花掉、去補上傳統工程師在課堂裡學到的那些東西的時間。
- **護欄**:publish 前有資安掃描,另外還有介面層面的驗證與「什麼合適、什麼不合適」的判斷。「平台端我們盡可能保護使用者與建置者,**但也有一些常識與責任是在你這邊的。**」

### 主題六:五個承諾與「證明你做過什麼」(約 03:00–03:04、03:09–03:10)

他留給全場五個**承諾**,對象是老師、研究者,也希望學生能接住:

1. **保障每一個學生都有 AI 存取權**——從資源充裕的大學,一路往下到他認為適合的國中與高中。
2. **重新設計評量,繞著批判性思考轉**,而不是「這是對的答案、那是錯的答案」。「今天我們過的生活裡有大量灰色地帶」,他認為**光譜**值得考慮。
3. **把教學創新看得跟研究一樣重**。他認為學術界在「獎勵好教學」與「獎勵研究」之間對比鮮明,希望高等教育更願意照亮那些能把 25、50、100 人一次帶進 AI 素養的老師——「這對我們是很大的機會。」
4. **用終身學習取代一次性的學位**。他提到幾年前在 Stanford 當兼任教師時討論過的 **on-ramp / off-ramp** 概念:一旦你進了這個機構,你就**終身是這裡的人**——25 歲離開、30 歲回來,或 45 歲離開、47 歲回來都行。他承認**經濟模型與具體實作方式仍是開放問題**,但「人需要社群」這件事早已被理解。
5. **衡量能力與流動性,而不是排名**。他認為讓學生在畢業求職時擁有一套 **proof of work** 是很大的機會。「我半開玩笑地想過,幫**履歷、成績單、也許還有 GPA** 辦一場告別式。」因為他認為未來會走到:**你指給我看的是你的作品集**,是你獨力與協作累積下來的所有專案證據;而當我隔著桌子面試你,決定我要不要把你找進團隊的,會是**你能不能把故事講出來、能不能讓我看見你當時面前有哪些分岔、你選了哪一條、以及為什麼。**

呼應第 5 點,他講了一個 Penn State 的故事:四位剛畢業的學生一起來 Replit 辦公室,說他們還在繼續做大學時開的事業。他問「所以你們每個人都一邊創業一邊上課?」對方說「算是吧」——他們每學期修四門課,**每門課只派一個人去上,學完回來教其他三個人**;省下來的時間就拿去創業。四年做了四家公司,他追問「有賺到錢嗎?五位數?幾千塊?」對方說:「不,我們**每個人**在這四年裡各做出大約**一百萬美元的 ARR**。」

於是他開始想:**與其談 GPA、成績單、履歷,「在四年內學會東西、把它變現、參與經濟,最後零負債地走上畢業台」會不會才是教育團隊該設的目標?** 他當場問全場覺得這是不是合理的目標,並補了一句:「我大概會**雇用**那幾個人。」

他也放了一張自己**三個小孩**(14 歲、10 歲、7 歲)的照片,說他把他們叫做三家新創,每個發薪週期結束就把錢包掏空讓他們開心。他之所以有動力,是因為**四年後最大的那家「新創」就要上大學**,而 2030 年的學習、教育、認證、大學、甚至工作會長什麼樣子,沒人知道。「如果你覺得你知道 2030 年會發生什麼,**請立刻在演講後來找我。**」他認為**實驗窗口大概只有一年到一年半、最多兩年**,要在這段時間把所有想法都試一遍,看哪些有效、哪些沒有。

Replit 的 **Faculty Fellows** 計畫就是在做這件事:一個現在約 **75 位老師**的 cohort,每月一場 webinar;願意實驗的老師用 Replit 蓋出體驗與工具,拿去給學生用或用在研究裡,然後回來向 cohort 報告**什麼有效、什麼沒效**,「這樣下一個還沒敢把腳伸進水裡的人,可以站在別人的共享經驗上,更有信心地試。」

### 一個非典型的教學案例:教 Shaquille O'Neal vibe code(約 02:56–03:00)

去年 12 月,他和 Replit 創辦人 Amjad 在亞特蘭大的一個拍攝現場,教 **Shaquille O'Neal** vibe coding。第一個問題非常實體:**Shaq 的手太大,打不了字。** 解法是請他開好幾個瀏覽器分頁、按 F5、然後**直接用講的**。

**90 分鐘內**他們做出了三個東西:

- **Shaq GPT**:回答所有運動問題,而且**把「Charles Barkley sucks」硬編碼進任何跟 Charles Barkley 有關的問題**(TNT 的搭檔)。
- **Shaq Daddy**:「Brandon,我想解決美國的孤獨流行病。有很多單身男性需要知道怎麼跟女性說話,我們得讓這些男人結婚。」——一個給全美男性的搭訕台詞生成器。
- 一個**廣告與投資追蹤器**:Shaq 的品牌鋪天蓋地(他說 Snoop Dogg 大概跟他不相上下),所以做一個能看**今年至今、或歷來**的東西,理解自己的時間與品牌的投資報酬率。

他真正想講的重點不是這幾個 app,而是:**看到一個那樣的人願意展現脆弱、坦然承認自己不懂、然後真的去試**,是很有力量的。這也是他對 Replit 教育團隊的願景——找到那些**有意願與謙遜去嘗試新事物**的人,等他們做出成果之後,把它帶回自己的觀眾、自己的母校(Shaq 是 LSU)。「如果你有想法,關於怎麼在一個**其他人仰望、或小孩覺得很酷的平台或人物**身上把這件事規模化,這其實是我教育團隊策略的一部分。」開學季會看到他們跟 Shaq 與其他人做更多這類事。

### 金句

> "We've confused time served in college institutions with learning. We've confused the credentials with a student's capability to actually perform. And sometimes we've confused sorting students throughout four or five years with actually educating them."(約 02:29)

整場對高等教育的核心指控,三句話講完。

> "College has become this extraordinarily expensive sorting system."(約 02:29)

上一句的結論。

> "The question should no longer be, did the student use AI? … Did the student actually think? Did the student verify the work? … Can the student tell us where the machine got it wrong?"(約 02:51)

評量該問的問題整組換掉——最後一問尤其關鍵:能指出機器錯在哪,才是判斷力的證據。

> "The same tool that you're using to build out your application is the same Replit agent that you can ask questions to in order to get unblocked."(約 03:12)

對非技術使用者而言,「蓋東西的 agent 也是幫你解卡的 agent」是最實際的一條。

> "Each of us made like a million dollars each over four years in ARR for the businesses that we started."(約 03:10)

Penn State 那四位學生的原話,也是他「用作品集取代成績單」主張最有力的註腳。

## English Notes

### Framing: who's speaking and what this session actually is (~02:20–02:22)

Brandon Middleton is Replit's Head of Education. Two facts he leads with that aren't on a résumé: eleven years ago he entered the Guinness Book of World Records as **the first person to rap a commencement speech** (Haas evening and weekend MBA, class of 2015), and across jobs at Amazon (six years at AWS) and Microsoft he always taught on the side — Replit is the first place he gets to do it full time. His remit now runs from universities and colleges to K–12 and nonprofits, all aimed at making AI literacy practical and tactical.

He frames the session as **both a talk and a demonstration**: talk about education while building an app with Replit. A show of hands revealed a room heavy on technologists but with a substantial contingent of **self-described non-technical people who vibe code**, and he promised to serve both.

The first demo is **an app he built that morning with Replit Agent**: the room opens a URL, uploads photos and messages, and a "scroll wall" fills the big screen live. That same app becomes the running example later for databases, deployment, and APIs.

### Thread 1: the premises college was designed on no longer hold (~02:24–02:30)

He teaches **Redesigning Finance** at the Stanford d.school every spring quarter, where students joke to him about the state of higher education — the tuition price against the classroom experience, and whether being in class is differentiated from going to YouTube. He thinks the jokes land because they're partly true: the belief that "I believe in the American dream, I did everything people told me to do, and it gets me a job" is starting to wane.

His central argument: **the education system as it exists was actually designed pretty well — for a world that no longer exists.**

- Information used to be **scarce**. You came to a university to receive it from a professor; knowledge was locked in libraries, laboratories, and lecture halls.
- **Remembering the answer** used to be the evidence of learning. Not anymore — you can have a lot of book knowledge and no street smarts, or a lot of observations that turn out to be misinformation or disinformation.
- Today information is everywhere, answers are abundant, and **intelligence itself is becoming pervasive and abundant** as model costs drop and model quality climbs.

Which produces the uncomfortable question for the institution: **if we were designing college for today — summer of 2026 — from a blank sheet of paper, how would we do it?** Would we still organize everything around lectures and libraries? Still run 16-week semesters, or make them shorter? Still count attendance? Keep closed-book recall and rote memorization on final exams, or throw them away?

His diagnosis is three confusions: **we've confused time served with learning, credentials with capability to perform, and — sometimes — sorting students over four or five years with educating them.** The result is an extraordinarily expensive sorting system: sorted by admissions, by grades and departments, sometimes by the institution attended — and the output four or five years later gets called merit, and people literally get hired or not hired on it.

### Thread 2: the AI literacy tour and the signals from the field (~02:26–02:33)

Replit runs what he calls an **AI literacy tour**, which has been through **Chicago, New York, Los Angeles, Atlanta, and the Bay Area**, asking from the ground up: what does it feel like to be a student right now, and what does it feel like to be a teacher receiving AI mandates from above and trying to translate AI literacy into something meaningful for yourself and your community? The people he talks to range from preschool teachers to R1 researchers and professors.

One slide shows a community session in East Palo Alto with participants **from age 7 to 77** discussing resource allocation issues in the city. He captured what the seven- and eight-year-olds said alongside what the 75- and 76-year-olds said, on sticky notes and his phone, then uploaded it into a Replit app and **thought with AI as a partner** — the point being to show a community that doesn't identify as computer scientists or engineers how easy it is.

The signals from the work world are stark:

- At the beginning of 2026, unemployment among **young recent college graduates was about 5.7%**.
- More strikingly, **about 41.5% were underemployed** — "I might have graduated from a really fancy school, but I might be working in something underneath my intellectual capability or even my interest."
- The World Economic Forum reports **nearly 40% of workers' current skills are expected to change between 2026 and 2030**. He translates it: if 100 people represented all eight billion, **59 of them would have to shift, reskill, and repivot within four years.**

None of that means the institution has no value, he says — it means **the connection between education, student capability, and opportunity is currently under strain** and needs solving.

His own path is the argument: EE at UIUC → networking software engineer at Cisco in the Bay Area → Haas MBA in 2015 → putting down a lot of the programming and product management skills → and, after leaving AWS for Replit, picking those design/engineering/product skills back up to build for technical and non-technical people alike. Hence: **learning, unlearning, and relearning is the core skill.**

### Thread 3: AI is not the next edtech gadget (~02:33–02:40)

He deliberately distinguishes AI from the calculator and from Google circa 2003. Yes, it automates grading, paper summarization, and lesson planning — but he sees **a once-in-a-century opportunity to rebuild education around human potential.** He believes everyone has an innate passion and skill to deliver something to the other eight billion of us, and that vibe coding and agentic AI can help people reach peak performance. **"For the first time in history, imagining agentic assistants and personal tutors is a real thing that can be achieved within the next couple of years."**

He is pointed about the distributional angle. In Palo Alto, neighbors send kids to Saturday school and to tutors that keep them out until 6pm — "students whose parents know how to navigate the system, that's pretty soft." What he cares about is the other side: students **not confident enough to raise a hand in a crowded lecture hall.** A 24/7 personal tutor means the student too shy to ask at 2 a.m. gets an answer; students who need an explanation **a different way** get one (visual versus auditory learners, students who do well in orals but not timed written exams); students who need accommodations get them **without embarrassment, exhaustion, or judgment** from a teacher who is often in a one-to-many setting. And multilingual support: living in the Bay Area for 21 years as a monolingual English speaker, he asked how many in the room speak more than one language — "so I am underachieving all of you" — but notes you can speak to Replit in French, Spanish, or any native tongue and have the apps you build translate for whoever is on the other side of the interaction.

He explicitly rejects the replacement framing. This is about **expanding the reach of one person** for a class of 15, 50, or 100. When the teacher becomes less a broadcaster and more a designer, coach, mentor, critic, and community builder, students get more room to grow into leadership and ownership. **"AI can definitely deliver the information, but what the teacher needs to do — and why that matters — is that very personal care and concern, that intangible thing, that belief the teacher has in the student"** that gets a student to stay up two extra hours or take pride in the work they turn in.

He stretches the boundary of "education" with an atypical case: a Grammy-winning musician, signed to a label for ten years and three albums, released from that deal five years ago, who came to the Replit office. His question wasn't technical — he wants to run his own record label and fix what plagued him inside the larger music industry, starting with **revenue recognition for streaming royalties** (fractions of pennies per stream across Spotify, YouTube Music, and the rest) and the runaround he got when he tried to audit what he was owed. No computer science background; he's using vibe coding to reimagine that part of the industry. "Even though he's not part of an actual university, that still falls under education in my scope — music education, business education, technology education."

### Thread 4: so how does assessment change? (~02:48–02:52)

His position is blunt: **"I think testing is pretty dead at this point."**

In Redesigning Finance he asks students to **record five- to seven-minute YouTube explanations** of themselves grappling with a topic. One theme from last year's class: if you're redesigning reinsurance and the insurance industry to improve the **claimant's** experience for the next LA wildfire or the next Florida flood, how do you design at the claimant level, the insurer level, and the reinsurer level? Students **build something and then defend it synchronously** — "so unless they've learned how to master deep faking, they're putting the work into actually thinking through it and putting a prototype and their video next to it as a submission."

His grading is redesigned too: all group work, but **adaptive** — weighted by the student's year in school (freshman through master's) and by background (engineering versus brand-new to technology), and scored on the **fidelity of the design** plus **collaboration as measured by how their teammates vote**, not by how the instructors and TAs read the group.

He replaces the assessment question entirely. Not "**did the student use AI?**" but:

- Did the student actually **think**?
- Did the student **verify** the work?
- Did they **cite sources** and say where it came from?
- Did the student **improve** the work?
- Did the student **explain the decisions and choices** that led to the output?
- Can the student **defend the conclusion**?
- **Can the student tell us where the machine got it wrong?** — using their own judgment and expertise to evaluate what the machine said.

In practice: **an oral defense after every major individual or group project**, and students submitting not just a final answer but **a tracked record of their reasoning.** He built a system inside Replit for students to reflect on lectures, submit assignments, and track that arc — "**the space between two lectures, you might have learned a lot. The space between one exam and the next, you might have learned a lot. And the traditional system doesn't capture those moments.**"

Two cases where process beat domain expertise:

- A San Francisco life-sciences hackathon where students used Replit for **biomarker discovery** and drug-discovery work. He admits he didn't do particularly well in molecular and cellular biology or chemistry, but as a judge his feedback focused on **how deeply they thought about the solution and how many people they surveyed** — their process — rather than his domain expertise. Even without going deep in a domain, lived experience and perspective can make what students build better.
- **Jack, 15, at Holy Trinity High School in Chicago**, who commutes 25–30 miles to school. The principal gave students Replit access last spring, and Jack took the school's own disciplines and principles and built a system teachers use **from their phones** to reward behavior aligned with those values. Students accumulate **XP**, shown on a leaderboard on the **digital signage in the lobby as students walk in from the buses**, redeemable for special things at the school. A vibe-coding platform being used to **change the culture and environment of a school.**
  Asked how he thought about learning AI, Jack broke it into three: **learning with AI** (tutor, collaborator, critic, translator); **learning about AI** (security, governance, how models and algorithms work — from the school's one teacher who did a deep professional-development dive and brought it back to the sophomores, juniors, and seniors); and **learning beyond AI** (Bluetooth streaming his app to the signage system, plus the community impact and issues around the school). Brandon sees those three as a good starting frame, extending well beyond the classroom into medicine, justice, and resourcing.

He's also candid that this becomes a philosophical and ideological conversation quickly: there are things technology cannot cure — economic inequality, poverty, war — where money is sometimes a factor but never the whole solution. He wants to talk to communities and students about those principles alongside the AI literacy.

### Thread 5: the Replit platform tour (~02:42–02:48, 03:04–03:12)

He asked an audience member to define Replit for someone who's never used it, and got: **"from idea to built AI application without the requirement of knowing much about the technology underneath."** He took that.

What he actually clicked through:

- The **prompt box**, familiar from ChatGPT or Claude, next to an **import** button for work started elsewhere.
- **511 integrations and connectors**, personal and enterprise — Dropbox, Discord, Slack, Google Drive, Databricks, Google Sheets. "It's a lot more fun to connect into all of these applications before you build the thing you want to build": *go grab my Google Drive, my Dropbox, my Databricks and my Google Sheets, and make an application that does XYZ.*
- **Output types** — website, mobile app, design, games, slide deck — which steer the model. **The slide deck for this talk was built in Replit.**
- **Learn and documentation** in the bottom left, with video content taking people from zero to 100 and a bit beyond.
- **Modes**: **Lite** for basic asks ("change my slide background from black to orange," "change the text of this slide"), **Economy** as the default middle-of-the-road reasoning, and **Power** for genuinely ambitious work — with the ability to click into each and **select closed or open models**. "Choosing the right model for the right thing you're asking Replit to do is part of the experience."

The last stretch is a **vibe coding 101** walkthrough of building end to end:

1. **Multiplayer.** An invite button at the top of the workspace lets other developers **prompt the same body of code** — "in the same way you can build out a Google Doc with five or six people, you can build software."
2. **Your first prompt.** He starts newcomers on a **personal portfolio page**: "make me something that'll help me express what I've accomplished in my career," throw in a picture of yourself, go.
3. **Publish**, which abstracts hosting, database provisioning, security scanning — everything needed to go from localhost on your laptop to a URL that works for everyone.
4. **Add a database.** "When you uploaded your pictures — if it was just a front-end page I couldn't have done that." He opens **Tools → Database** live, showing Replit's **development** database (for pre-publish testing) alongside the **production** database: 22 rows in dev versus 32–33 in production. "That's the difference between doing something locally before you publish, and publishing it live to the world."
5. **Add APIs** — weather, stock time series, Shopify, or any service — so the app pulls fresh data into the interface on load.
6. **Add auth.** "**The shortest line in this whole presentation that will allow you to do something cool is: add Replit Auth to my app.**" Five or six words produces a login portal with Google, Apple, and the usual providers, so users can log their sessions, pictures, and text.

He closes on **the limitations of vibe coding**, and is honest about them:

- **You do need to know a little about how product building works** to figure this stuff out.
- **You'll hit unfamiliar errors.** Screenshot them and drag them into the interface: "I don't know what this is and how to fix it." **The same Replit Agent building your application is the one you ask to get unblocked** — you don't have to wait until a human can help you.
- **Complexity and technical debt.** He thinks **debugging is the most useful skill on the list**, and learning it as a non-technical person is a lot of trial and error — time spent with the agent picking up what traditional engineers learn in class.
- **Guardrails.** Security scans before publish, plus interface-level validations and judgment about what's appropriate. "We do as much as we can on the platform side to protect users and builders, **but there's some common sense and responsibility on your side too.**"

### Thread 6: five commitments and proof of work (~03:00–03:04, 03:09–03:10)

Five commitments for teachers, researchers, and students:

1. **Guarantee AI access for every student** — from well-resourced universities down to what he thinks is an appropriate floor at middle and high school.
2. **Redesign assessment around critical thinking** rather than right-answer/wrong-answer. "There's a lot of gray area in the life we live today" — a spectrum is worth considering.
3. **Reward teaching innovation as seriously as research.** He sees a stark contrast in academia between rewarding good teaching and rewarding research, and wants higher ed shining a light on people who can coach 25, 50, or 100 at a time into AI literacy. "That's a big opportunity for us."
4. **Replace the one-time degree with lifelong learning.** He references an **on-ramp/off-ramp** idea discussed among Stanford adjuncts a few years back: once you start at an institution you're **there for life** — leave at 25 and come back at 30, or leave at 45 and come back at 47. He concedes **the economics and the exact implementation are still open questions**, but the human need for community is already understood.
5. **Measure capability and mobility, not rankings.** Giving students a **proof of work** system as they graduate and look for jobs is a big opportunity. "I thought in jest it'd be fun to have a funeral service for the resume, for the transcript, maybe for the GPA" — because where he thinks this lands is that **you point me to your portfolio of built work** and the evidence of everything you've done solo and collaboratively; and sitting across the interview table, **your ability to tell the story, to show the forks you faced and the ones you chose and why**, is what decides whether he's excited to bring you onto the team.

The Penn State story anchors that fifth point. Four recently graduated students came to the Replit offices, still building the businesses they started in college. He asked whether each of them ran businesses *and* attended classes. "Kind of" — for every class, **one of them was the leader**, went to that class, learned everything, and came back and taught the other three. Four classes a semester, each of them leading one. What did they do with the freed-up time from the other three? Built businesses — four of them over four years. Did they make money? "Five figures? A couple grand?" — "No, **each of us made like a million dollars each over four years in ARR**."

Which made him wonder whether, instead of GPA, transcript, and resume, the goal should be **learning information, monetizing it, participating in the economy across four years, and walking across the stage with zero debt.** He polled the room on whether that's reasonable, and added: "I think I would hire those people."

He also showed a photo of **his three kids — 14, 10, and 7 — whom he calls his three startups**, emptying his wallet at the end of every pay cycle to make them happy. His motivation is that in four years the oldest startup goes to college, and nobody knows what learning, education, credentialing, college, or work will look like in 2030. "If you have ideas about this and you feel like you know what's going to happen in 2030, **please see me immediately after this presentation.**" He puts the **experimentation window at about a year to eighteen months, maybe two years**, to try everything and see what sticks.

Replit's **Faculty Fellows** program is the mechanism: a cohort now about **75 teachers** large, with a monthly webinar, where people who said yes to experimentation build experiences on Replit, put them in front of students or use them in research, and report back on **what worked and what didn't** — so the next person who hasn't dipped a toe in feels more confident on the back of that shared experience.

### An atypical teaching case: teaching Shaquille O'Neal to vibe code (~02:56–03:00)

In December, Brandon and Replit founder Amjad were on set in Atlanta teaching **Shaquille O'Neal** to vibe code. The first obstacle was physical: **his hands are too big to type.** The workaround was to open multiple browser tabs, hit F5, and **just start talking.**

In **90 minutes** they built three things:

- **Shaq GPT**, to answer every sports question, with **"Charles Barkley sucks" hardcoded into any question about Charles Barkley**, his TNT broadcast partner.
- **Shaq Daddy**: "Brandon, I want to solve the loneliness epidemic in America. There's a lot of single men that need to know how to talk to women, and we need to get these men married" — a pickup line generator.
- An **advertisement and investment tracker**, since Shaq's brand is everywhere (he and Snoop Dogg are "neck and neck"), to see year-to-date 2026 or all-time returns on his time and his brand.

The apps aren't really the point. What he wanted from it was **seeing someone like that be vulnerable and okay with not knowing things, and try anyway.** That's the vision for Replit's education team: find people with the willingness and humility to try, and once they've done it, have them take it back to their audiences and their alma maters (Shaq went to LSU). "If you have ideas about how to scale this on a platform or a person that other people look up to, or that kids see as cool, that's actually part of my strategy on the education team." Expect more of it with Shaq and others as back-to-school season arrives.

### Quotes

> "We've confused time served in college institutions with learning. We've confused the credentials with a student's capability to actually perform. And sometimes we've confused sorting students throughout four or five years with actually educating them." (~02:29)

The whole indictment of higher education in three sentences.

> "College has become this extraordinarily expensive sorting system." (~02:29)

The conclusion that follows from it.

> "The question should no longer be, did the student use AI? … Did the student actually think? Did the student verify the work? … Can the student tell us where the machine got it wrong?" (~02:51)

The assessment question replaced wholesale — the last item being the real test of judgment.

> "The same tool that you're using to build out your application is the same Replit agent that you can ask questions to in order to get unblocked." (~03:12)

For a non-technical builder, this is the most practically useful line in the platform tour.

> "Each of us made like a million dollars each over four years in ARR for the businesses that we started." (~03:10)

The Penn State students' own words, and the strongest support for replacing transcripts with portfolios.

## 提到的專案與資源 / Projects & Resources

| 名稱 Name | 說明 | Description | 備註 Notes |
|-----------|------|-------------|------------|
| Replit Agent | 平台核心的 agentic coding 介面,從 prompt 到部署 | The platform's agentic coding interface, from prompt to deployment | 現場示範用它當天早上做出 scroll wall app / used live to build the morning's scroll-wall app |
| Replit Agent modes | Lite / Economy / Power 三種模式,每種可再選封閉或開源模型 | Lite / Economy / Power modes, each with closed- or open-model selection | 講者口述作 "light mode",官方名稱為 **Lite** / he said "light mode"; the official name is **Lite** |
| Replit Auth | 一句 prompt 即可加入的登入機制(Google、Apple 等) | Authentication added with a single prompt (Google, Apple, and the usual providers) | 「整場最短、卻最有用的一行」/ "the shortest line in this whole presentation" |
| Replit Integrations | 511 個個人與企業連接器(Dropbox、Slack、Google Drive、Databricks 等) | 511 personal and enterprise connectors (Dropbox, Slack, Google Drive, Databricks, …) | 數字為講者口述 / figure as spoken |
| Faculty Fellows | Replit 的教師實驗 cohort,約 75 人,每月 webinar 分享成敗 | Replit's cohort of experimenting faculty, ~75 members, monthly webinar on what worked and didn't | |
| AI Literacy Tour | Replit 走訪芝加哥、紐約、洛杉磯、亞特蘭大與灣區的訪談計畫 | Replit's listening tour across Chicago, New York, Los Angeles, Atlanta, and the Bay Area | |
| Redesigning Finance | 講者在 Stanford d.school 每年春季開的課,以錄影解說與同步辯護取代考試 | His spring-quarter course at the Stanford d.school, replacing exams with recorded explanations and synchronous defense | |
| 2084-edu.replit.app | 現場 scroll wall app 與簡報的網址 | The live scroll-wall app and the deck | 網址依逐字稿聽寫,拼法待確認 / URL transcribed by ear, spelling unverified |

## 逐字稿勘誤 / Transcript Corrections

| 字幕原文 Heard as | 應為 Should be |
|-------------------|----------------|
| Replet / Rep | Replit |
| Mckll / Michelle / Michael | Michele Catasta(Replit 早上場講者 / the morning's Replit speaker) |
| Amja | Amjad Masad(Replit 創辦人 / founder) |
| light mode | Lite mode(Replit 官方模式名稱 / official mode name) |
| hos business school | Haas School of Business |
| UIU | UIUC(University of Illinois Urbana-Champaign) |
| Vive coding | vibe coding |
| in justest | in jest |
| grock | grok(理解 / to grasp) |
| Dr. Chin / Dr. Chen | 同一位觀眾,姓氏拼法待確認 / same audience member, surname spelling unverified |

## 待確認 / To Verify

- **Replit 成立年份**:trivia 環節台下答「10 年」被判定為正確答案,但講者未複述確切年份。/ In the trivia the answer "10 years" was accepted, but he never restated the founding year.
- **早上場的 Replit 講者**:逐字稿為 "Mckll"(他說「看起來像 Michelle、像 Michael,但他叫 Mckll」),幾乎確定是 **Michele Catasta**(President & Head of AI, Replit),但議程頁未在本次查證中直接確認。/ Almost certainly **Michele Catasta**, President & Head of AI at Replit, but not confirmed against the agenda page here.
- **葛萊美得主音樂人的姓名**:台上刻意未點名。/ The Grammy-winning musician was deliberately not named.
- **示範 app 網址**:逐字稿聽寫為 `2084-edu.replit.app`,數字與連字號拼法未確認。/ The demo app URL, transcribed as `2084-edu.replit.app`, is unverified.
- **就業數據出處**:5.7% 失業率與 41.5% 低度就業為講者口述,未點名資料來源;WEF「近 40% 技能改變」與他換算的「59/100 人需再訓練」之間的推導未在台上說明。/ The 5.7% and 41.5% figures were given without a cited source, and the step from WEF's "nearly 40% of skills change" to "59 of 100 people must reskill" was not explained on stage.
- **Faculty Fellows 的公開申請管道**未在台上給出。/ No public application channel for Faculty Fellows was given.
- **Holy Trinity High School 的 Jack**:僅有名字,學生全名與專案是否公開未知。/ Only a first name was given for the Holy Trinity student; full name and whether the project is public are unknown.
