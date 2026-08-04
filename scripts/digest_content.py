# Daily digest content for the site — hand-authored synthesis, bilingual.
# Each theme's refs are (page_slug, talk_slug) pairs, validated at build time
# against the parsed notes; a typo here fails the build instead of shipping a
# dead link. Talk titles/speakers are NOT duplicated here — the renderer looks
# them up from SITE_PAGES so labels stay in sync with the notes.

DIGEST = {
    "slug": "digest",
    "layout": "digest",
    "icon": "summarize",
    "title": {"en": "Digest", "zh": "統整重點"},
    "hero": {
        "kicker": {"en": "The two days, distilled", "zh": "兩天議程,一次讀完"},
        "heading": {"en": "Daily digest", "zh": "每日統整重點"},
        "lede": {
            "en": "What actually happened across the four stages, day by day: the themes that kept resurfacing, and the talks behind each of them. Every reference links to the full note.",
            "zh": "把四個舞台、兩天的內容收斂成幾條反覆出現的主軸,每條主軸都列出背後的相關演講——點任何一個引用都會進到該場的完整筆記。",
        },
    },
    "days": [
        {
            "key": "2026-08-01",
            "label": {"en": "Saturday · August 1", "zh": "8 月 1 日(六)"},
            "intro": {
                "en": "Day one walked the stack from the compute floor to the research frontier. The through-line: raw capability is no longer the bottleneck — the design of environments, verification and control is.",
                "zh": "第一天把技術棧從算力底層一路走到研究前沿,貫穿全場的主旋律是:模型能力本身已不是瓶頸,瓶頸移到了環境、驗證與控制權的設計。",
            },
            "themes": [
                {
                    "title": {"en": "Building under the compute ceiling", "zh": "算力天花板下的基礎設施"},
                    "body": {
                        "en": "DeSantis set the tone with constraint-driven innovation: power, silicon and supply chains shape the AI systems problem. From there the infrastructure track ran through accelerated computing and lab notebooks for agents, to Stoica's two fundamental gaps in agentic software engineering, photonic computing, and whether Kubernetes is the right substrate for agent-shaped workloads.",
                        "zh": "DeSantis 開場定調「約束驅動創新」:電力、晶片與供應鏈的限制形塑了 AI 系統問題的樣貌。基礎設施這條線從加速運算、給 agent 的實驗記錄本,一路到 Stoica 指出 coding agent 的兩個根本缺口、光子運算,以及「Kubernetes 到底適不適合 agent 形狀的工作負載」。",
                    },
                    "refs": [
                        ("sat-plenary", "peter-desantis--constraint-driven-innovation-a-look-at-the-ai-systems-problem"),
                        ("sat-plenary", "jonathan-cohen--accelerated-computing-for-agentic-ai"),
                        ("sat-plenary", "chuan-li--a-lab-notebook-for-agents"),
                        ("sat-plenary", "panel--agentic-ai-infrastructure-platform"),
                        ("sat-compass", "ion-stoica--the-limits-of-ai-coding-agents"),
                        ("sat-compass", "nick-harris--photonics-is-the-future-of-computing"),
                        ("sat-compass", "tim-hockin--is-kubernetes-good-for-agents"),
                    ],
                },
                {
                    "title": {"en": "Software engineering, rewritten", "zh": "軟體工程被重寫:從寫程式到設計環境"},
                    "body": {
                        "en": "The clearest consensus of the day: the human job has moved from writing code to designing the environment the agent works in. Steinberger runs 20-hour loops and 64 sub-agents; Lopopolo prompts agents as lazily as he'd prompt a principal engineer; Catasta wants to deprecate prompting entirely; on Nexus, Cognition shared RL lessons from training coding agents and Yutori argued computer-use models will agentify the web, not APIs.",
                        "zh": "全天最明確的共識:人的工作已經從「寫程式」變成「設計 agent 所處的環境」。Steinberger 跑 20 小時的 loop、同時開 64 個 sub-agent;Lopopolo 主張要能像 prompt 資深工程師一樣懶散地 prompt agent;Catasta 的北極星是把 prompting 整個廢掉;Nexus 舞台上 Cognition 分享訓練 coding agent 的 RL 教訓,Yutori 則主張 computer-use 模型會 agent 化整個 web 而非 API。",
                    },
                    "refs": [
                        ("sat-plenary", "peter-steinberger--no-doors-for-agents"),
                        ("sat-plenary", "ryan-lopopolo--harness-engineering"),
                        ("sat-plenary", "michele-catasta--continual-learning-for-agents"),
                        ("sat-plenary", "alex-graveley--omniscient-agents"),
                        ("sat-plenary", "panel--future-of-software-engineering"),
                        ("sat-nexus", "silas-alberti--scaling-rl-for-coding-agents"),
                        ("sat-nexus", "dhruv-batra--computer-use-models-will-agentify-the-web-not-apis"),
                    ],
                },
                {
                    "title": {"en": "Security: even the exam hall is attack surface", "zh": "安全:連考場都成了攻擊面"},
                    "body": {
                        "en": "Dawn Song's keynote anchored the day's security thread: agent flexibility is attack surface, the OpenAI–Hugging Face sandbox escape showed evaluation infrastructure itself can be breached, and the way out is automated red-teaming plus provably-secure code. Zaremba reframed safety as fire-style resilience — an ecosystem, not a silver bullet — while the Nexus security session ran from runtime guardrails to supply-chain attacks and agents going rogue.",
                        "zh": "Dawn Song 的 keynote 是全天資安線的錨點:agent 的彈性就是攻擊面,OpenAI–Hugging Face 沙盒逃逸事件證明連評估基礎設施本身都會被打穿,出路是自動化 red teaming 加上可證明安全的程式碼。Zaremba 把安全重新框成「火」式的 resilience——是生態系而非銀彈;Nexus 資安場次則從 runtime guardrails、供應鏈攻擊一路談到 agent 叛變。",
                    },
                    "refs": [
                        ("sat-plenary", "dawn-song--towards-building-safe-and-secure-agentic-ai"),
                        ("sat-plenary", "wojciech-zaremba--building-resilience-for-the-intelligence-age"),
                        ("sat-nexus", "bo-li--securing-ai-agents"),
                        ("sat-nexus", "milad-nasr--end-to-end-security-research-with-a-language-model"),
                        ("sat-nexus", "mohamed-nabeel--ghost-in-the-web-store"),
                        ("sat-nexus", "itsik-mantin--when-good-agents-go-rogue"),
                        ("sat-nexus", "jon-rav-shende--observability-is-not-governance"),
                        ("sat-nexus", "workshop--future-of-agent-evaluation"),
                    ],
                },
                {
                    "title": {"en": "Robots & world models: simulation is the new infrastructure", "zh": "機器人與世界模型:模擬是新的基礎建設"},
                    "body": {
                        "en": "Levine made the case for robot foundation models and Jim Fan sketched the endgame; Fidler traced simulation's three generations — hand-built art, NeRF reconstruction, and generative world models that went from five minutes per five-second clip to real-time on a consumer GPU in a single year. Sony AI's table-tennis robot and Waymo's physical-autonomy lessons pulled trustworthiness back into the physical world.",
                        "zh": "Levine 論證 robot foundation models,Jim Fan 描繪機器人的終局;Fidler 把模擬分成三個世代——美術手刻、NeRF 重建、生成式世界模型,而生成式這代在一年內從「5 秒影片跑 5 分鐘」進化到消費級顯卡即時。Sony AI 的桌球機器人與 Waymo 的實體自主性教訓,把「可信任」拉回物理世界。",
                    },
                    "refs": [
                        ("sat-plenary", "sergey-levine--robot-foundation-models"),
                        ("sat-plenary", "jim-fan--robotics-endgame"),
                        ("sat-plenary", "panel--robotics-and-world-models"),
                        ("sat-atlas", "sanja-fidler--world-models-for-physical-ai-simulation"),
                        ("sat-atlas", "peter-stone--outplaying-elite-table-tennis-players-with-an-autonomous-robot"),
                        ("sat-atlas", "vincent-vanhoucke--trustworthy-agents-in-the-real-world"),
                        ("sat-atlas", "bolei-zhou--scaling-sidewalk-autonomy-with-world-models"),
                    ],
                },
                {
                    "title": {"en": "AI for science, many-pronged", "zh": "AI for Science 的分進合擊"},
                    "body": {
                        "en": "The Nexus morning was a full session on scientific discovery: Buehler's multi-agent swarms and large reasoning models, Zou on the collective intelligence of agents, Princeton's LabOS AI-XR co-scientist that sees and works alongside humans, Rose Yu's agentic co-scientists, and Goodfire on learning science back out of superhuman AI.",
                        "zh": "Nexus 整個上午都在談科學發現:Buehler 的 multi-agent swarms 與大型推理模型、Zou 談 agent 的集體智慧、Princeton 的 LabOS AI-XR co-scientist(看得見、能與人並肩工作)、Rose Yu 的 agentic co-scientists,以及 Goodfire 主張從超人 AI 身上把科學「學回來」。",
                    },
                    "refs": [
                        ("sat-nexus", "markus-buehler--superintelligence-for-scientific-discovery"),
                        ("sat-nexus", "james-zou--harnessing-the-collective-intelligence-of-agents-for-science"),
                        ("sat-nexus", "mengdi-wang--labos-the-ai-xr-co-scientist"),
                        ("sat-nexus", "rose-yu--towards-ai-co-scientists"),
                        ("sat-nexus", "eric-ho--unlocking-scientific-abundance-by-learning-from-superhuman-ai"),
                    ],
                },
                {
                    "title": {"en": "Recursive self-improvement: excitement with brakes on", "zh": "RSI 與長視野:興奮與剎車並存"},
                    "body": {
                        "en": "Day one treated recursive self-improvement with equal parts excitement and caution: the Song–Sekhon fireside demystified the \"foom\", Vinyals argued RSI is throttled by how hard evaluation and ideation really are, Tworek mapped the opportunities and failure modes of long-horizon agents, and Ng closed the day defending decades-away AGI definitions and open models.",
                        "zh": "第一天對「遞迴自我改進」的態度是興奮與剎車並存:Song×Sekhon 的對談為「Foom」除魅,Vinyals 指出 RSI 會被「評估與 ideation 其實很難」卡住,Tworek 盤點長視野 agent 的機會與失敗模式,Ng 則在壓軸對談裡捍衛「AGI 還要數十年」的定義與 open models。",
                    },
                    "refs": [
                        ("sat-plenary", "fireside--demystifying-the-foom"),
                        ("sat-plenary", "oriol-vinyals--a-practical-perspective-on-recursive-self-improvement"),
                        ("sat-plenary", "jerry-tworek--opportunities-and-challenges-for-long-horizon-agents"),
                        ("sat-plenary", "panel--agentic-ai-foundational-capabilities"),
                        ("sat-plenary", "fireside--andrew-ng-alfred-lin"),
                    ],
                },
            ],
        },
        {
            "key": "2026-08-02",
            "label": {"en": "Sunday · August 2", "zh": "8 月 2 日(日)"},
            "intro": {
                "en": "Day two turned to deployment: enterprise governance, evaluation methodology, and putting agents into finance, science and production systems. \"Measure first, then grant autonomy\" was the refrain.",
                "zh": "第二天轉向落地:企業治理、評估方法學,以及把 agent 放進金融、科學與生產系統的實務。全天的主旋律是「先量測、再放權」。",
            },
            "themes": [
                {
                    "title": {"en": "Governance is the adoption bottleneck", "zh": "治理是企業採用的瓶頸"},
                    "body": {
                        "en": "Ironclad's CTO set the frame — the rate limiter on AI adoption is organizational, not technical. Google Cloud talked agent governance, HubSpot explained why off-the-shelf AI hit a wall, Credo AI proposed \"earned autonomy\" with the can/may/act ladder compiled into the harness, Dan Klein contrasted superintelligence with super-reliability, and Salesforce kept the human in the loop.",
                        "zh": "Ironclad CTO 開場定框:AI 採用的限速器是組織,不是技術。Google Cloud 談 agent governance、HubSpot 解釋現成 AI 為何撞牆、Credo AI 提出「掙來的自主權」——把 can/may/act 的授權階梯直接編譯進 harness、Dan Klein 對比超智慧與超可靠,Salesforce 則把人留在迴圈裡。",
                    },
                    "refs": [
                        ("sun-atlas", "sunita-verma--rate-limiter-on-ai-adoption-is-organizational"),
                        ("sun-plenary", "rao-surapaneni--enterprise-ai-agent-governance"),
                        ("sun-plenary", "duncan-lennox--off-the-shelf-ai-hit-a-wall"),
                        ("sun-plenary", "panel--enterprise-ai"),
                        ("sun-compass", "eric-aldana--earning-autonomy-governance-as-code"),
                        ("sun-atlas", "dan-klein--superintelligence-vs-super-reliability"),
                        ("sun-compass", "kathy-baxter--the-human-in-the-loop"),
                        ("sun-plenary", "fireside--ali-ghodsi-andy-konwinski"),
                    ],
                },
                {
                    "title": {"en": "Evaluation becomes the battleground", "zh": "評估成為主戰場"},
                    "body": {
                        "en": "Two stages each dedicated a full session to evals: Agent Arena's causal evaluations in the real world, benchmarking as an art and science, evals-first reliability and spec-driven agents on Atlas; then DigitalOcean's \"preferences > benchmarks\", the exam before enterprise deployment, ScarfBench's enterprise-Java migrations and Hex's \"the points don't matter\" on Compass. The shared verdict: benchmark scores are not production reliability.",
                        "zh": "兩個舞台各排了一整個場次談評估:Atlas 上有 Agent Arena 的真實世界因果評估、benchmark 的藝術與科學、evals-first 與 spec-driven agents;Compass 則有 DigitalOcean 的「偏好 > benchmark」、企業部署前的入職考、ScarfBench 的企業 Java 遷移與 Hex 的「分數根本不重要」。共同判詞:benchmark 分數不等於生產環境的可靠度。",
                    },
                    "refs": [
                        ("sun-atlas", "anastasios-angelopoulos--agent-arena-causal-evaluations-of-agents-in-the-real-world"),
                        ("sun-atlas", "vincent-sunn-chen--the-art-and-science-of-benchmarking-agents"),
                        ("sun-atlas", "priya-ponnapalli--building-reliable-agents-an-evals-first-approach"),
                        ("sun-atlas", "srijith-rajamohan--spec-driven-agents-hierarchical-specs-tooling-and-trajectory-based-evaluation"),
                        ("sun-compass", "debarshi-raha--preferences-over-benchmarks-model-routing"),
                        ("sun-compass", "yuan-emily-xue--the-exam-before-enterprise-deployment"),
                        ("sun-compass", "rahul-krishna--scarfbench-can-agents-migrate-enterprise-java"),
                        ("sun-compass", "grace-tang--data-benchmarks-everythings-made-up"),
                        ("sun-compass", "aayush-agrawal--evals-the-engine-for-agent-improvement"),
                    ],
                },
                {
                    "title": {"en": "Frontier research: personal agents and scientific discovery", "zh": "前沿研究:個人化 agent 與科學發現"},
                    "body": {
                        "en": "Socher pitched the Eureka Machine — recursive superintelligence for science; Ed Chi laid out the future of personalized universal agents; Periodic Labs combined experiments, LLMs and theory to hunt quantum materials; Babuschkin argued personal AI needs continual learning. The math session stretched the horizon further, from sparse-reward long-horizon tasks to the unit distance conjecture.",
                        "zh": "Socher 提出 Eureka Machine——用於科學的遞迴超智慧;Ed Chi 描繪個人化通用 agent 的未來;Periodic Labs 用「實驗 × LLM × 理論」找量子材料;Babuschkin 主張個人 AI 需要持續學習。數學場次把視野拉得更遠:從稀疏獎勵的長視野任務到 unit distance conjecture。",
                    },
                    "refs": [
                        ("sun-plenary", "richard-socher--the-eureka-machine-recursive-superintelligence-for-science"),
                        ("sun-plenary", "ed-chi--the-future-of-personalized-universal-agents"),
                        ("sun-plenary", "ekin-dogus-cubuk--combining-experiments-large-language-models-and-theory-to-discover-quantum-materials"),
                        ("sun-plenary", "igor-babuschkin--personal-ai-and-continual-learning-new-frontiers-in-agentic-ai"),
                        ("sun-plenary", "panel--frontier-research"),
                        ("sun-atlas", "sergei-gukov--the-future-of-ai-for-long-horizon-and-sparse-reward-tasks"),
                        ("sun-atlas", "lijie-chen--the-unit-distance-conjecture-and-ai-for-math"),
                    ],
                },
                {
                    "title": {"en": "Trust, deepfakes and the human", "zh": "信任、深偽與人"},
                    "body": {
                        "en": "The Compass safety morning ran the trust gamut: Bregler on how agents with new tools can counter deepfakes and add context, trustworthy agents in regulated domains, ARIA's society of agents trusting at machine speed, Lawrence on viable systems and judgment, and continual learning versus safety in computer-use agents.",
                        "zh": "Compass 的安全場把「信任」談了一輪:Bregler 講配上新工具的 agent 如何反制深偽並補上脈絡、受監管領域的可信 agent、ARIA 的「機器速度下的 agent 社會」、Lawrence 的 viable systems 與判斷力,以及 computer-use agent 的持續學習與安全拉鋸。",
                    },
                    "refs": [
                        ("sun-compass", "chris-bregler--deepfakes-and-more"),
                        ("sun-compass", "lovedeep-gondara--trustworthy-agentic-ai-in-regulated-domains"),
                        ("sun-compass", "alex-obadia--a-society-of-agents"),
                        ("sun-compass", "neil-lawrence--viable-systems-judgment-and-ai-safety"),
                        ("sun-compass", "huan-sun--smarter-and-safer-everyday"),
                    ],
                },
                {
                    "title": {"en": "The agentic economy", "zh": "Agentic 經濟:錢包、銀行與新創"},
                    "body": {
                        "en": "Circle sketched payment rails for an economy where agents transact, Wells Fargo reimagined banking, Capital One shared the enterprise frontier, and the finance panel weighed what changes when money moves at agent speed — before twelve startups closed the summit in the spotlight.",
                        "zh": "Circle 描繪 agent 直接交易的經濟需要什麼支付軌道、Wells Fargo 重新想像銀行、Capital One 分享企業前沿,金融座談則衡量「錢以 agent 速度移動」時規則怎麼變——最後由 12 家新創的 spotlight 為峰會收尾。",
                    },
                    "refs": [
                        ("sun-plenary", "nikhil-chandhok--building-infrastructure-for-the-agentic-economy"),
                        ("sun-plenary", "faraz-shafiq--reimagining-banking-in-the-ai-era"),
                        ("sun-plenary", "milind-naphade--advancing-the-state-of-the-art-the-frontier-of-enterprise-agentic-ai"),
                        ("sun-plenary", "panel--agentic-ai-in-finance-and-legal"),
                        ("sun-plenary", "startup-spotlight"),
                    ],
                },
                {
                    "title": {"en": "Production-grade agent systems", "zh": "把 agent 開進生產環境"},
                    "body": {
                        "en": "The systems track got concrete: Nvidia's lessons from using agents to build production AI systems, Postman's road from demos to reliable infrastructure, Factory's software factory, SK hynix's rack-scale disaggregated serving with shared-memory KV cache — and Invoca's reminder that agentic AI is a UX problem disguised as a technology breakthrough.",
                        "zh": "系統這條線非常具體:Nvidia 用 agent 蓋生產 AI 系統的教訓、Postman 從 demo 走到可靠基礎設施、Factory 的軟體工廠、SK hynix 的 rack 級共享記憶體 KV cache 分離式 serving——還有 Invoca 的提醒:「agentic AI 是一個偽裝成技術突破的 UX 問題」。",
                    },
                    "refs": [
                        ("sun-compass", "jun-yang--using-agents-to-build-production-ai-systems"),
                        ("sun-compass", "rick-crawford--from-agent-demos-to-production"),
                        ("sun-compass", "eno-reyes--building-the-software-factory"),
                        ("sun-compass", "jongryool-kim--disaggregated-llm-serving-with-shared-memory-kv-cache"),
                        ("sun-compass", "surbhi-rathore--agentic-ai-is-a-ux-problem"),
                        ("sun-plenary", "panel--agentic-ai-developer-platforms"),
                    ],
                },
            ],
        },
    ],
}
