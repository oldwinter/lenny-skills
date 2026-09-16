# Lenny's Product Management Skills for Claude Code 中文版 2.0

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/skills-76-blue)](https://github.com/oldwinter/lenny-skills/tree/main/skills)

**76 个产品管理和工程 skill**，从 [Lenny's Podcast](https://www.lennyspodcast.com/) 和 [Lenny's Newsletter](https://www.lennysnewsletter.com/) 的完整档案中提取：597 集播客与文章、4,019 条来源见解；每一条引文均已对照来源逐字核验。

由 [Refound AI](https://refoundai.com) 策划。请访问 [refoundai.com/lenny-skills](https://refoundai.com/lenny-skills/) 浏览包含指南、引文和模板的完整数据库。

## 2.0 新增内容

- **以产品运营模型的形式组织**——skill被分组到产品组织实际运行的流程领域：战略、规划、发现、构建、发布、增长、团队和运营节奏，以及垂直剧本和职业轨迹。
- **包括时事通讯内容** — 1.0 仅限播客； 2.0 添加了来自 349 个时事通讯帖子的框架和模板，包括“X 如何构建产品”系列。
- **每项skill的模板和框架** — 每项skill均附带宾客实际使用的命名框架、清单和模板，位于 `references/artifacts.md` 中。
- **经过验证的引用** — 每个引用都会根据源记录或帖子进行逐字检查。没有释义漂移。

## 什么是 Skills？

Skills 是为 AI 代理提供专业知识和工作流程的 Markdown 文件。将它们添加到项目后，当你处理匹配的任务时，Claude Code（或任何读取 `SKILL.md` 的代理）会应用相应框架。

## 安装

复制用表格链接里的英文目录名，不要用中文标题。`编写PRD` 对应 `writing-prds`，`路线图优先级` 对应 `roadmap-prioritization`。按中文去 `.claude/skills/编写PRD` 会找不到。

先 clone 这个 fork：

```bash
git clone https://github.com/oldwinter/lenny-skills.git
```

复制一个：

```bash
mkdir -p .claude/skills
cp -R lenny-skills/skills/writing-prds .claude/skills/
```

复制全部：

```bash
mkdir -p .claude/skills
cp -R lenny-skills/skills/. .claude/skills/
```

或者通过 [refoundai.com/lenny-skills](https://refoundai.com/lenny-skills/) 上的下载链接获取个人skill。

## 使用

装好后直接用中文描述任务，例如「帮我写一份 PRD」或「帮我排一下路线图优先级」。Skill 靠 `SKILL.md` 的 `description` 匹配任务，不是靠中文标题当斜杠命令。

`writing-prds` 和 `roadmap-prioritization` 只出现在复制路径和 frontmatter `name` 里。不要输入 `/编写PRD`。

## Skills

### 战略与定位

| skill | 它可以帮助你做什么 | 来源 |
|---|---|---|
| [定义产品策略](skills/defining-product-strategy/) | 通过做出推动客户行为的艰难选择，将愿景转化为具体的行动计划。 | 47 |
| [创建产品愿景](skills/product-vision/) | 设计一个理想的未来状态，激励团队并指导战略决策。 | 22 |
| [战略产品定位](skills/positioning/) | 定义使您的产品的独特价值显而易见且不可否认的背景 | 28 |
| [定价策略与优化](skills/pricing-strategy/) | 设计并迭代能够体现产品真正价值的定价模型。 | 21 |
| [北极星指标](skills/north-star-metrics/) | 围绕单一、可量化的客户价值和业务成功衡量标准调整您的团队和战略。 | 15 |
| [衡量产品市场契合度](skills/measuring-pmf/) | 从推销你的产品转变为感受市场把它从你身上拉出来。 | 21 |
| [竞争策略](skills/competitive-strategy/) | 通过确定结构性力量和以客户为中心的差异化，建立持久的护城河并智胜竞争对手。 | 24 |
| [从失败中恢复](skills/recovering-from-failure/) | 将产品挫折和停滞的增长转化为战略突破和转型机会。 | 20 |

### 规划和优先顺序

| skill | 它可以帮助你做什么 | 来源 |
|---|---|---|
| [路线图优先级](skills/roadmap-prioritization/) | 根据证据和需求，将混乱的积压工作转变为高投资回报率的战略计划。 | 43 |
| [目标设定和 OKR](skills/goal-setting-okrs/) | 通过将长期战略转化为雄心勃勃的可衡量成果来推动组织重点。 | 19 |
| [规划节奏优化](skills/planning-cadence/) | 通过结构化、分层的规划程序，使长期战略与短期执行保持一致。 | 13 |
| [高风险决策](skills/high-stakes-decisions/) | 以速度和结构清晰的方式应对不可逆转的选择和极端的不确定性。 | 30 |
| [评估权衡](skills/evaluating-trade-offs/) | 掌握权衡竞争选项的艺术，以最大限度地提高长期影响和团队速度。 | 14 |

### 发现与研究

| skill | 它可以帮助你做什么 | 来源 |
|---|---|---|
| [掌握客户访谈](skills/customer-interviews/) | 揭示深层用户痛点和行为触发因素，以构建人们真正需要的产品。 | 11 |
| [持续产品发现](skills/continuous-discovery/) | 将客户反馈从定期琐事转变为产品决策的高频引擎。 | 23 |
| [想法验证](skills/idea-validation/) | 从意见转向基于证据的开发，停止构建人们不想要的东西。 | 34 |
| [卓越的产品实验](skills/product-experiments/) | 通过严格的 A/B 测试和数据驱动的学习，推动可衡量的增长并降低风险。 | 9 |
| [定义您的ICP](skills/defining-icp/) | 缩小您的关注范围，赢得市场滩头阵地并建立不可否认的势头。 | 15 |
| [分析用户反馈](skills/analyzing-user-feedback/) | 通过扩展同理心和综合，将原始信号转化为可行的见解。 | 19 |
| [产品品味和直觉](skills/product-taste/) | 开发可靠的内部指南针来识别和打造世界一流的产品。 | 36 |

### 构建与交付

| skill | 它可以帮助你做什么 | 来源 |
|---|---|---|
| [编写PRD](skills/writing-prds/) | 定义明确的问题和有限的解决方案，以最大限度地提高团队速度和创造性产出。 | 14 |
| [交付速度](skills/shipping-velocity/) | 通过消除组织摩擦和建立高强度的交付文化来加速执行。 | 19 |
| [AI 辅助原型设计](skills/ai-assisted-prototyping/) | 使用自然语言和 AI 工具将抽象的产品概念转化为可运行的交互式软件。 | 15 |
| [使用 AI 代理进行构建](skills/building-with-ai-agents/) | 从编写代码行过渡到指导并行的自主代理团队。 | 15 |
| [产品堆栈策略](skills/product-tool-stack/) | 通过平衡既定标准与 AI 原生速度来构建高性能产品工具包。 | 6 |
| [工程健康和生产力](skills/engineering-health/) | 通过平衡技术卓越与战略开发人员投资来保持高交付速度。 | 18 |

### 发布和上市

| skill | 它可以帮助你做什么 | 来源 |
|---|---|---|
| [产品发布计划](skills/launch-planning/) | 通过将产品更新转化为引人注目的市场活动来建立动力并推动采用。 | 18 |
| [PLG 销售集成](skills/plg-sales-integration/) | 弥合自助服务采用和企业交易之间的差距，以最大限度地提高收入。 | 13 |
| [掌握企业销售动作](skills/enterprise-sales-motion/) | 从创始人主导的销售转变为可重复、可扩展的企业引擎。 | 16 |
| [获取第一批B2B客户](skills/first-b2b-customers/) | 通过手动操作和高度信任的关系，从零过渡到前十名付费客户。 | 7 |
| [营销组织和堆栈](skills/marketing-org-and-stack/) | 通过将专业人才与可扩展的数据基础设施结合起来，构建高性能的营销组织。 | 11 |
| [掌握公关和媒体](skills/pr-and-press/) | 将媒体报道变成可信度、增长和品牌权威的战略引擎。 | 9 |
| [命名和品牌](skills/naming-and-branding/) | 建立独特的身份，作为永久的竞争武器和情感锚。 | 11 |

### 增长和保留

| skill | 它可以帮助你做什么 | 来源 |
|---|---|---|
| [构建可持续增长模型](skills/growth-model/) | 超越线性漏斗，构建复合循环，推动可扩展的长期产品增长。 | 30 |
| [获取渠道策略](skills/acquisition-channels/) | 识别、测试和扩展推动可持续增长的分销引擎。 | 25 |
| [用户入门和激活](skills/user-onboarding-activation/) | 弥合初始注册和实现价值之间的差距，以最大限度地提高长期保留率。 | 25 |
| [掌握留存率和参与度](skills/retention-engagement/) | 通过将产品嵌入工作流程并创造复合用户价值来实现可持续增长。 | 17 |
| [推荐和口碑](skills/referrals-word-of-mouth/) | 通过有机宣传和结构化推荐循环，将用户满意度转变为高杠杆增长引擎。 | 13 |
| [SEO增长策略](skills/seo-strategy/) | 使用编程数据和系统实验将有机搜索转变为可扩展的获取引擎。 | 9 |
| [增长实验速度](skills/growth-experimentation/) | 打造高产出引擎，将小额胜利转化为大规模增长。 | 10 |
| [国际市场拓展](skills/international-expansion/) | 通过平衡本地同理心与运营手册，在全球范围内扩展您的产品。 | 8 |

### 团队与组织

| skill | 它可以帮助你做什么 | 来源 |
|---|---|---|
| [聘请世界一流的产品人才](skills/hiring-product-talent/) | 通过寻找、评估和关闭最优秀的 1% 人才，建立一个高杠杆率的产品组织。 | 30 |
| [面试和评估候选人](skills/interviewing-evaluating-candidates/) | 超越简历来评估高保真信号，如代理、第一性原理思维和实际工艺。 | 48 |
| [产品和工程的组织设计](skills/org-design/) | 构建您的团队，以最大限度地提高自主性、速度和战略一致性。 | 60 |
| [建立增长团队](skills/building-growth-team/) | 组建和组建一支高影响力的团队，以扩大分销规模并优化用户旅程。 | 14 |
| [创始人高管团队建设](skills/founding-exec-team/) | 设计和扩展核心领导层，推动公司从零增长到一。 | 15 |
| [辅导和人才发展](skills/coaching-development/) | 从问题解决者转变为成长加速器，打造一支高绩效团队。 | 34 |
| [建立高绩效团队文化](skills/team-culture/) | 建立一种主人翁精神、透明度和强度的文化，以推动产品的长期成功。 | 53 |
| [提供有效反馈](skills/giving-feedback/) | 将困难的对话转化为增长和高绩效的催化剂。 | 30 |
| [修复表现不佳的团队](skills/fixing-underperforming-teams/) | 诊断功能障碍的根本原因，并采取果断行动以恢复高性能。 | 12 |
| [领导组织变革](skills/leading-org-change/) | 在不中断业务的情况下改变文化、结构和运营。 | 58 |

### 运营节奏与沟通

| skill | 它可以帮助你做什么 | 来源 |
|---|---|---|
| [有效的产品评论](skills/product-reviews/) | 举办严格的协调会议，提高质量标准并加快决策制定。 | 12 |
| [高管沟通](skills/executive-communication/) | 掌握框架、透明度和决策沟通的艺术，以建立与领导层的信任。 | 9 |
| [为领导者进行向上管理](skills/managing-up/) | 将您与领导层的关系从汇报关系转变为高度信任的战略伙伴关系。 | 21 |
| [召开有效的会议](skills/running-meetings/) | 将日历从令人心碎的时间沉没变成高速对准机器。 | 12 |
| [领导者书面沟通](skills/written-communication/) | 通过结构化、清晰且有说服力的写作来扩大您的影响力并推动一致。 | 12 |
| [干系人对齐](skills/stakeholder-alignment/) | 通过梳理激励机制并共同设计方案，推动跨职能协作。 | 57 |

### 剧本：市场

| skill | 它可以帮助你做什么 | 来源 |
|---|---|---|
| [市场基础知识](skills/marketplace-fundamentals/) | 建立、引导和扩展买家和卖家的自我维持生态系统。 | 7 |
| [供需平衡](skills/supply-demand-balance/) | 通过识别瓶颈并战略性地扩展市场的困难部分来掌握市场流动性。 | 6 |
| [市场流动性与抽成率](skills/marketplace-liquidity-take-rates/) | 优化交易可靠性和商业化之间的平衡，构建有竞争壁垒的生态系统。 | 6 |

### 手册：构建 AI 产品

| skill | 它可以帮助你做什么 | 来源 |
|---|---|---|
| [AI产品策略](skills/ai-product-strategy/) | 优先考虑高影响力的工作流程并引导非确定性开发，以构建防御性的 AI 产品。 | 34 |
| [AI评估策略](skills/ai-evals/) | 超越氛围检查，转向对 AI 产品质量和可靠性进行系统、实证的测量。 | 11 |
| [设计AI-原生用户体验](skills/ai-native-ux/) | 从静态界面过渡到利用模型智能的流畅、意图驱动的交互。 | 14 |

### 剧本：从零到一

| skill | 它可以帮助你做什么 | 来源 |
|---|---|---|
| [评估创业想法](skills/evaluating-startup-ideas/) | 在构建之前系统地验证问题解决方案的适合性、市场时机和业务可行性。 | 28 |
| [初创公司筹款和退出](skills/fundraising/) | 掌握筹集资金、管理投资者关系和战略收购的艺术。 | 16 |
| [创始人主导的销售](skills/founder-sales/) | 掌握亲自销售产品的艺术，以建立信任并找到产品与市场的契合点。 | 6 |

### 操作手册：企业与 PLG

| skill | 它可以帮助你做什么 | 来源 |
|---|---|---|
| [PLG 基础知识](skills/plg-fundamentals/) | 将您的产品转变为分发、激活和扩展的主要引擎。 | 9 |

### 职业生涯

| skill | 它可以帮助你做什么 | 来源 |
|---|---|---|
| [闯入产品管理](skills/breaking-into-product/) | 战略性地引导您进入第一个产品管理职位的竞争道路。 | 11 |
| [PM 职业发展](skills/pm-career-growth/) | 通过掌握影响力、所有权和战略远见，从任务执行者转变为高影响力的产品领导者。 | 99 |
| [职业转型](skills/career-transitions/) | 通过优化高增长环境和内部能量来超越默认路径。 | 56 |
| [准备晋升案例](skills/building-a-promotion-case/) | 将职业影响力转化为有说服力、有数据支撑的论据，为下一步职业发展提供依据。 | 6 |
| [科技行业薪酬谈判](skills/negotiating-compensation/) | 掌握市场基准、信息收集和协作谈判方法，争取更合理的整体回报。 | 1 |
| [个人品牌网络](skills/personal-brand-network/) | 将您的专业知识转化为磁性网络和高亲和力的受众。 | 21 |
| [掌握公开演讲](skills/public-speaking/) | 将您的技术专业知识转化为令人信服的叙述，以掌握权威并推动行动。 | 12 |
| [时间和精力管理](skills/time-energy-management/) | 将时间和精力视为战略资产，保护您的注意力并提高绩效。 | 46 |
| [创始人心理学和复原力](skills/founder-psychology/) | 掌握内部环境以维持高绩效并驾驭领导力的情绪过山车。 | 38 |

## 归因

所有见解、引用、框架和模板均源自 Lenny Rachitsky 的播客和时事通讯，并且仍然是他和他的客人的知识产权。每个skill都链接回源剧集和帖子。如果您发现这些有用，请[订阅Lenny's Newsletter](https://www.lennysnewsletter.com/subscribe)。

## 贡献

找到提高skill的方法了吗？打开 PR。请保留报价的逐字内容和来源。

## 许可证

MIT 用于skill文件的结构和组织。底层内容属于 Lenny Rachitsky 和播客嘉宾；与归因一起使用，免费且不受限制。
