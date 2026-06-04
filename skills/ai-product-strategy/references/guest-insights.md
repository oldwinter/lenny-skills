# AI Product Strategy - 全部嘉宾洞察

*94 位嘉宾，179 次提及*

---

## Alex Hardimen
*Alex Hardimen*

> "We're training algorithms on specific data sets, like editorial important scores that actually come from our journalists. What that allows us to do is actually scale editorial judgment to a large group of readers. Those algorithms... they're trained on editorial signal and then they can still work towards driving towards outcomes like reach, engagement, conversion, et cetera."

**洞察：** AI 策略应侧重于使用算法来扩展人类的专业知识和判断力，而不仅仅是优化参与度。

**战术建议：**
- 在proprietary 'expert' 数据集（例如编辑分数）上训练算法
- 使用 AI 将人类判断扩展到更多受众
- 平衡专家信号与传统参与结果

*时间戳：01:04:25*


## Adriel Frederick
*Adriel Frederick*

> "When you are working on algorithmic heavy products, your job is figuring out what the algorithm should be responsible for, what people are responsible for, and the framework for making decisions."

**洞察：** PM 在 AI 产品中的核心作用是定义自动算法决策和人类判断之间的边界。

**战术建议：**
- 确定哪些决策需要算法尚无法掌握的长期战略意图。
- 创建一个框架，指定机器与人类操作员的职责。

*时间戳：00:00:00*

---

> "It's more about giving people the information that they can use for decisions that they alone are good at and giving machines the power to amplify a person's intent... I think about it as designing an interface and make it an extension of yourself rather than a black box."

**洞察：** AI 应该被设计为一个放大人类意图的工具，而不是一个autonomous black box的独立black box。

**战术建议：**
- 设计界面，为人们提供做出战略选择所需的背景。
- 使用 ML 针对特定目标进行优化，同时允许人类设置战略约束。

*时间戳：00:38:15*


## Albert Cheng
*Albert Cheng*

> "Behind the scenes, we're running chess engines to basically spit out evaluations for every move that you make. And then we translate that and make that approachable to the user using their native language and plain approachable style... that part is LLMs."

**洞察：** 最好的 AI 产品使用正确的技术来完成正确的任务：用于逻辑/ 计算的专用引擎和用于人性化通信的 LLMs。

**战术建议：**
- 使用 LLMs 将复杂的技术数据（例如引擎 evaluations）翻译成自然的、鼓励用户的语言。

*时间戳：00:49:07*


## Alexander Embiricos
*Alexander Embiricos*

> "One of our major goals with Codex is to get to proactivity. If we're going to build a super system, has to be able to do things. One of the learnings over the past year is that for models to do stuff, they're much more effective when they can use a computer. It turns out the best way for models to use computers is simply to write code. And so we're kind of getting to this idea where if you want to build any agent, maybe you should be building a coding agent."

**洞察：** AI agents 与计算机交互和控制计算机的最有效方法是编写和执行代码，而不是使用可访问性 APIs 或视觉点击。

**战术建议：**
- 将编码能力优先作为任何功能 AI agent 的核心能力
- 关注 'proactivity'，其中 agent 在没有直接 prompt 的情况下介入或采取行动

*时间戳：00:00:47*

---

> "I actually think Chat is a very good interface when you don't know what you're supposed to use it for... you start using it even outside of work to just help you. You become very comfortable with the idea of being accelerated with AI. So then you get to work and you just can naturally just, 'Yeah, I'm just going to ask it for this and I don't need to know about all the connectors or all the different features.'"

**洞察：** Chat 作为通用的 'common denominator' 界面，允许用户访问复杂的 AI 功能，而无需学习特定的工具配置。

**战术建议：**
- 使用 Chat 作为发现和一般帮助的入口点
- 仅当users 需要深入到诸如编码之类的功能域时才显示specialized GUI

*时间戳：00:26:10*

---

> "I think that the current limiting factor, I mean, there's many, but I think a current underappreciated limiting factor is literally human typing speed or human multitasking speed on writing prompts... we need to unblock those productivity loops from humans having to prompt and humans having to manually validate all the work."

**洞察：** AI 生产力的主要瓶颈是 'human-in-the-loop' 对 prompting 的要求以及手动验证输出。

**战术建议：**
- 构建允许 agents 成为 'default useful' 且无需恒定 prompting 的系统
- 开发automated validation loops，这样人们就不必手动审查每个 AI 操作

*时间戳：01:11:29*


## Aishwarya Naresh Reganti + Kiriti Badam
*Aishwarya Naresh Reganti + Kiriti Badam*

> "Most people tend to ignore the non-determinism. You don't know how the user might behave with your product, and you also don't know how the LLM might respond to that. The second difference is the agency control trade-off. Every time you hand over decision-making capabilities to agentic systems, you're kind of relinquishing some amount of control on your end."

**洞察：** 由于不确定的输入/ 输出以及系统自主性和人类控制之间的必要权衡，AI 产品与传统软件不同。

**战术建议：**
- 考虑natural language界面中的non-deterministicuser behavior。
- 平衡授予 agent 的代理级别与用户保留的控制量。

*时间戳：00:08:01*

---

> "So we recommend building step-by-step. When you start small, it forces you to think about what is the problem that I'm going to solve. In all this advancements of the AI, one easy, slippery slope is to keep thinking about complexities of the solution and forget the problem that you're trying to solve."

**洞察：** 成功的 AI 部署需要 'problem-first' 方法，从低影响、high-control version开始，在扩展复杂性之前进行学习。

**战术建议：**
- 从影响最小的用例开始，以掌握当前的功能。
- 随着对系统可靠性信心的增强，逐渐增加agency。

*时间戳：00:11:39*

---

> "It's not about being the first company to have an agent among your competitors. It's about have you built the right flywheels in place so that you can improve over time."

**洞察：** AI 的竞争优势来自于构建迭代反馈循环（flywheel），而不仅仅是率先将静态 agent 推向市场。

**战术建议：**
- 专注于构建一个随着时间的推移学习和改进的管道，而不是 'one-click' 解决方案。
- 在早期版本中记录人类行为，以创建数据flywheel以改进系统。

*时间戳：00:30:31*

---

> "I used to work with the CEO of now Rackspace, Gagan. So he would have this block every day in the morning, which would say catching up with AI 4:00 to 6:00 AM... I think leaders have to get back to being hands-on. And that's not because they have to be implementing these things, but more of rebuilding their intuitions because you must be comfortable with the fact that your intuitions might not be right."

**洞察：** AI 的领导力需要通过实践学习重建专业直觉并跟上快速的技术变革。

**战术建议：**
- 每天留出专门的时间来了解 AI 开发的最新动态。
- 愿意在 AI 的背景下挑战和重新学习长期持有的产品直觉。

*时间戳：00:25:43*


## Alex Komoroske
*Alex Komoroske*

> "I think LLMs are truly a disruptive technology. In fact, I would argue that what we're seeing in the industry is us trying to use mature playbooks from the end stage of the last tech era in one that doesn't really fit yet. To me, LLMs are magical duct tape. They're formed principally by the distilled intuition of all of society into a thing that operates between, a cost structure between human and plain old computing."

**洞察：** AI 改变了软件的基本成本结构，需要脱离传统的剧本，在传统剧本中，软件编写成本昂贵，但运行成本低廉。

**战术建议：**
- 认识到 LLMs 使编写 'good enough' 软件的成本显著降低，但增加了边际inference cost。
- 避免消费者启动 models 仅基于广告，因为广告收入可能无法清除inference cost。

*时间戳：00:10:56*

---

> "I see all these places where people will build products and they'll say 80% of the time, 90% percent of the time, it's great. 5% of the time it punches the user in the face... even if you get it down to 99% of the time, it's fine. If it punches in the face, that's not a viable product. And so how do you design your products assuming that this thing will be squishy and not fully accurate and fully work?"

**洞察：** AI 时代的产品设计必须考虑'squishy'和 LLMs 的non-deterministic，而不是将它们视为完美的预言机。

**战术建议：**
- 设计产品用户体验以处理 AI 可能不准确或失败的情况。
- 既然 'magical duct tape' (LLMs) 存在，就专注于构建可能的事物，而不是仅仅尝试使 AI 100% 自主。

*时间戳：00:13:24*


## Amjad Masad
*Amjad Masad*

> "I actually wrote about it back in '22. I said it's going to be society of models, like products will be made of a lot of different models, and it's quite a heavy engineering project."

**洞察：** 未来的 AI 产品将不会构建在单个 model 上，而是构建在专门的 models 的精心策划的生态系统上。

**战术建议：**
- 架构系统根据多个基础 models 的特定优势（例如推理与速度）来利用它们。

*时间戳：00:33:47*

---

> "I could imagine whatever, five years from now, someone running a billion dollar company with zero employees where it's like the support is handled by AI, the development is handled by AI, and you're just building and creating this thing that people are finding valuable."

**洞察：** AI 使 'hyper-efficient' 公司的未来成为可能，其中支持和开发等核心功能完全自动化，使创始人能够完全专注于价值创造。

**战术建议：**
- 评估业务 models，该业务 models 可以利用自主 agents 以最少的人员规模扩展至高收入。

*时间戳：00:53:08*


## Anton Osika
*Anton Osika*

> "The reason why we're doing Lovable is that I don't know about your mom, but my mom doesn't write code... we are building for this 99% of the population who don't write code."

**洞察：** AI product strategy 应侧重于为非技术大多数人实现复杂技能的民主化。

**战术建议：**
- 针对缺乏专业技术技能的'99%'
- 专注natural language界面，降低进入门槛

*时间戳：00:06:52*

---

> "The frontier of where this is a problem is very rapidly receding back. So what we did was we identified the most important areas, so specifically adding login, creating data persistence, adding payment with Stripe. Those are the things that we made sure it doesn't get stuck on."

**洞察：** 识别并系统地解决 'stuck points' 中 AI agents 通常无法确保可靠的用户体验的问题。

**战术建议：**
- 识别 AI 生成中的常见故障点（例如身份验证、支付）
- 定量调整系统以解决这些特定瓶颈

*时间戳：00:29:04*


## Aparna Chennapragada
*Aparna Chennapragada*

> "When I think about agents, I think about these three things. One is an increasing level of autonomy and kind of independence that you can delegate higher and higher order tasks. Second, I think of as complexity. It's not a one-shot, 'Hey, create this image or do this thing or summarize the document,' it's build me this prototype that expresses my idea of, say, an augmented reality app. And then the third one I think of is it's a much more natural interaction."

**洞察：** 有效的 AI agents 的定义是其自主性、处理复杂多步骤任务的能力以及自然且通常异步的交互 models。

**战术建议：**
- 为高层目标的委托而设计，而不仅仅是精细运动辅助
- 专注于复杂的多步骤工作流程，而不是简单的一次性 prompts
- 合并异步功能，以便 agent 在用户离开时工作

*时间戳：00:17:10*


## Asha Sharma
*Asha Sharma*

> "all of a sudden these are these living organisms that just get better with the more interactions that happen. I think this is the new IP of every single company products that think and live and learn."

**洞察：** AI 产品正在从静态工件转变为通过连续数据循环和交互而进化的活体有机体。

**战术建议：**
- 关注产品团队的'metabolism'摄取数据、消化奖励 models
- 根据价格、性能或质量等特定结果调整 models

*时间戳：05:26*

---

> "I think that where companies fail is that they're doing AI for AI's sake. They have a ton of projects that they're kicking off at the same time without a blueprint to understand how it actually worked and what their Stack looks like and they aren't treating it like a real investment, and so they don't have the measurement and the observability and the evals all set up."

**洞察：** AI 的成功实施需要战略蓝图、严格的衡量，并将 AI 视为核心投资而不是一系列实验。

**战术建议：**
- 在扩展之前建立清晰的测量、可观察性和 evaluation 框架 (evals)
- 规划现有流程并将 AI 应用于特定痛点，例如客户支持或减少欺诈

*时间戳：10:56*

---

> "I feel like you have to actually build for the slope instead of the snapshot of where you are."

**洞察：** AI 的product strategy必须考虑技术变革的快速速度，而不仅仅是当前的技术水平。

**战术建议：**
- 构建灵活的架构，允许在改进时更换 models 或工具
- 随着产出的边际成本接近于零，预计对生产力的指数需求

*时间戳：11:54*


## Benjamin Mann
*Benjamin Mann*

> "I think progress has actually been accelerating where if you look at the cadence of model releases, it used to be once a year and now with the improvements in our post-training techniques, we're seeing releases every month or three months, and so I would say progress is actually accelerating in many ways, but there's this weird time compression effect."

**洞察：** AI 的进度通过更快的发布节奏而加速，这可能会由于 'time compression.' 而造成平台期的错误认知

**战术建议：**
- 监控 model 发布的节奏，而不仅仅是单次跳跃的幅度来衡量行业进展
- 在 AI 开发中考虑 'time dilation'，其中快速迭代可以掩盖潜在的指数增长

*时间戳：00:08:06*

---

> "I think my favorite role in that time has been when I started the labs team about a year ago, whose fundamental goal was to do transfer from research to end user products and experiences. Because fundamentally I think the way that Anthropic can differentiate itself and really win is to be on the cutting edge."

**洞察：** 专用的 'Labs' 功能对于弥合前沿研究和可行的最终用户产品体验之间的差距是必要的。

**战术建议：**
- 组建专业团队，负责'transfer'从研究突破到产品功能的打造
- 专注于'computer use'和凭证管理作为高信任、高差异化的产品领域

*时间戳：01:03:07*

---

> "I guess concretely we think about skating to where the puck is going and what that looks like is really understand the exponential... don't build for today, build for six months from now, build for a year from now. And the things that aren't quite working that are working 20% of the time, will start working 100% of the time."

**洞察：** AI 产品规划必须基于未来 models 的预期功能，而不是基于当前 models 的局限性。

**战术建议：**
- 预计在 6-12 个月内构建 model 功能，以避免交付过时的产品
- 如果目前可靠性较低（例如，20% 的成功率）的功能处于指数改进曲线上，请对其进行投资

*时间戳：01:06:21*


## Ben Horowitz
*Ben Horowitz*

> "I think the application layer is going to be very, very interesting... Chat GPT, like it or not, it's got a real moat... the applications are both more complex and kind of stickier than people thought they were originally. The thing that people got very wrong is this whole thin wrapper around GPT, that's really wrong."

**洞察：** AI 的护城河是通过复杂的应用逻辑和用户粘性构建的，而不仅仅是访问基础 model。

**战术建议：**
- 避免构建'thin wrappers'；专注领域深度融合
- 寻找软件以前无法解决问题的机会

*时间戳：01:04:08*

---

> "Everything that we couldn't solve with software we can solve now, almost. So it's a really big world."

**洞察：** AI 最大的机会在于解决以前传统确定性软件无法解决的问题。

**战术建议：**
- 识别 'fat-tail' 人类行为或传统代码无法处理的罕见边缘情况

*时间戳：01:11:48*


## Brian Balfour
*Brian Balfour*

> "My prediction, the new distribution platform will be ChatGPT... I think the bigger thing will be whatever they do with launching a third-party platform on top of ChatGPT, there's a bunch of signals that they're about to launch that."

**洞察：** 像 ChatGPT 这样的 AI 平台正在从技术转变转向分销转变，为初创公司创造了新的 'escape velocity' 机会。

**战术建议：**
- 监控第三方 agent 平台作为新分销渠道的出现。
- 根据留存率和参与深度评估 AI 平台，而不仅仅是每月活跃用户 (MAU)。

*时间戳：00:12:02*

---

> "My hypothesis... is that the moat is about context and memory. These models by themselves, if you compare them side by side, they generate the same result, and so the actual difference-maker is which one has more of your context, because it's the context plus the model that produces the best output."

**洞察：** 在 AI 时代，产品防御力从 model 本身转向用户上下文和记忆的积累。

**战术建议：**
- 投资 'context connectors'，让你的产品能够存储和调用用户特定数据。
- 专注于创建一个flywheel，更多的使用可以带来更好的个性化环境和卓越的输出。

*时间戳：00:30:25*


## Cam Adams
*Cam Adams*

> "We approach AI inside the product through three pillars. First of these is that we need to build some of our own AI tech... Second pillar is just finding the world's best AI people to partner with... And for us, the third pillar is our app ecosystem."

**洞察：** 强大的 AI strategy平衡了proprietary model 建设、战略合作伙伴关系和开放的开发者生态系统。

**战术建议：**
- 仅在你拥有数据优势或对核心业务至关重要的情况下构建proprietary AI
- 与一流的供应商合作，满足 LLMs 等商品 AI 需求
- 创建应用生态系统，让第三方 AI 开发者接触你的用户群

*时间戳：00:56:53*


## Bret Taylor
*Bret Taylor*

> "I think there's three segments of the AI market... frontier model market... tooling... applied AI market. I think this will play out for companies who build agents. I think agent is the new app."

**洞察：** AI 市场分为资本支出重的前沿 models、有风险的工具和解决特定业务问题的高价值应用 agents。

**战术建议：**
- 重点关注 'Applied AI'，其中 agent 是主要产品外形规格
- 构建 agents，使其能够自主完成工作，而不仅仅是提高个人生产力

*时间戳：00:52:36*

---

> "The whole market is going to go towards agents. I think the whole market is going to go towards outcomes-based pricing. It's just so obviously the correct way to build and sell software."

**洞察：** 软件的未来是自主的 agents，其定价基于其提供的价值，而不是其占用的席位。

**战术建议：**
- 将product strategy定位于自主任务完成，而不仅仅是人机交互工具

*时间戳：00:59:31*


## Chip Huyen
*Chip Huyen*

> "What actually improves AI apps, talking to users, building more reliable platforms, preparing better data, optimizing end-to-end workflows, writing better prompts."

**洞察：** 成功的 AI 产品建立在基本的产品工作和数据质量之上，而不是追逐最新的技术框架。

**战术建议：**
- 优先考虑与用户交谈，而不是及时了解每个 AI 新闻周期
- 专注于编写更好的 prompts 并优化端到端工作流程
- 避免过度使用未经测试的新技术，这些技术以后很难切换

*时间戳：00:05:30*

---

> "I do ask people to ask their managers, 'Would you rather give everyone on the team very expensive coding agent subscriptions or you get an extra head count?' Almost every one, the managers will say head count."

**洞察：** 高管 AI 目标与经理级生产力需求之间存在脱节，因为 AI 生产力提升难以衡量。

**战术建议：**
- 使用 'headcount vs. AI subscription' 问题来衡量 AI 工具在团队中的感知价值
- 专注于识别具有清晰、可衡量结果的用例（例如销售机器人的转化率），以推动采用

*时间戳：00:44:28*

---

> "When it comes to, think about voice, it's an entirely different beast... we need to think about latency because I think multiple steps... And there's a question, what does it make you sound natural?"

**洞察：** 多模态 AI，特别是语音，将挑战从 model 功能转移到延迟和中断检测等传统工程问题。

**战术建议：**
- 解决 'forced interruption' 问题，让语音机器人感觉自然
- 优化多跳延迟（STT 到 LLM 到 TTS）以实现实时交互

*时间戳：01:01:45*


## Chandra Janakiraman
*Chandra Janakiraman*

> "There are two ways to get AI to assist you in the strategy formulation process. The first is to support the preparation phase in terms of research... The second one is in this idea called generating mock strategies."

**洞察：** AI 可以通过进行大量竞争性研究并提供全面的 'mock' 起点来加速战略工作。

**战术建议：**
- 使用 AI 分析大量竞争对手发行说明库中的主题
- 与 LLMs 生成'mock strategies'，在人工向下选择之前确定综合投资领域

*时间戳：01:27:52*


## Christopher Miller
*Christopher Miller*

> "I get to help lead HubSpot in terms of how we should be thinking about building the foundational technology to create AI-powered experiences and then also lead the strategy of how we leverage those experiences to help that B2B business builder be way more successful using our platform than they might've been in years past."

**洞察：** AI product strategy涉及平衡基础设施的开发与推动客户成功的特定用户体验的创建。

**战术建议：**
- 专注于构建可为多种 AI 体验提供支持的基础技术
- 利用 AI 帮助用户比传统软件方法更成功地取得成果

*时间戳：00:04:54*


## Claire Vo
*Claire Vo*

> "I hold myself to the bar as a technology leader, I need to be leading the league on understanding what this can disrupt, using these tools to make a better team, and actually shifting the size and shape of my organization in response to the technology around us."

**洞察：** 领导者必须主动重组其组织和人才比例，以响应 AI 驱动的效率提升。

**战术建议：**
- 在开始新的职位描述之前，将某个角色自动化一周
- 将焦点从 'communication'（交易信息）转移到 'influence'（买入）
- 研究non-deterministic产品以了解它们与传统软件的区别

*时间戳：01:03:30*


## David Placek
*David Placek*

> "Engineers come to us wanting more sophisticated names where they are likely to end up with another Codium or an Anduril or an Anthropic... we think what you're doing needs to be much more tangible, and something that people can grab onto, and much more natural as opposed to a Codium."

**洞察：** AI 产品受益于有形、自然的名称，可以消除消费者的怀疑和技术抽象。

**战术建议：**
- 在 AI 中摆脱抽象、听起来技术性的名称
- 使用隐喻和自然概念（例如风帆冲浪）让 AI 感觉更容易理解

*时间戳：00:37:42*


## Dan Shipper
*Dan Shipper*

> "There are these things that were historically really expensive that only rich people or big companies could buy... what AI does is it allows you to be like, oh, I could just use cloud for that... And then if it does, we will unbundle it into its own separate thing that becomes an app."

**洞察：** 可行的 AI product strategy是识别昂贵、高需求的人工服务，并将其分解为经济实惠、专业的 AI 应用程序。

**战术建议：**
- 首先使用通用聊天机器人 (ChatGPT/Claude) 测试产品创意，看看工作流程是否有价值
- 在公开发布之前，通过自己团队的内部采用来衡量产品的成功

*时间戳：00:57:38*

---

> "I think the number one predictor is, 'Does the CEO use ChatGPT?'... If the CEO is in it all the time, being like, 'This is the coolest thing,' everybody else is going to start doing it. If the CEO is like, 'I don't know, this is for someone else,' no one else is going to be able to lead that charge."

**洞察：** AI 在组织内的成功采用主要取决于首席执行官的个人参与度和对工具的直觉。

**战术建议：**
- CEO 在使用 AI 起草内容时应在备忘录中明确提及
- 率先垂范，根据个人使用体验设定合理预期

*时间戳：01:12:00*


## Dalton Caldwell
*Dalton Caldwell*

> "Small fine tune models as an alternative to gigantic generic ones... we'll probably be able to create better and better glue so all sorts of software systems can talk to each other. And so again, very broad idea. But yeah, I think we'll see a lot of very successful companies where that's the kernel of the idea they start with."

**洞察：** 可行的 AI 策略包括从通用 models 转向专门的、微调的 models，并将 LLMs 用作企业系统的 'glue'。

**战术建议：**
- 探索针对特定垂直用例的小型、微调 models
- 识别可以用 LLMs 替换或改进的脆弱企业 'glue'

*时间戳：00:55:37*


## Dr. Fei Fei Li
*Dr. Fei Fei Li*

> "That combination of the trio technology, big data, neural network, and GPU was kind of the golden recipe for modern AI. And then fast-forward, the public moment of AI, which is the ChatGPT moment, if you look at the ingredients of what brought ChatGPT to the world technically still use these three ingredients."

**洞察：** 现代 AI 的突破建立在三个核心支柱的融合之上：海量数据集、神经网络架构和高性能 GPU。

**战术建议：**
- 专注于 'trio' 技术：大数据、神经网络和计算 (GPU)。
- 认识到扩展现有架构是必要的，但不足以实现未来的突破。

*时间戳：00:19:12*

---

> "I think scaling loss of more data, more GPUs, and bigger current model architecture is there's still a lot to be done there, but I absolutely think we need to innovate more. There's not a single deeply scientific discipline in human history that has arrived at a place that says we're done, we're done innovating and AI is one of the, if not the youngest discipline in human civilization."

**洞察：** 虽然扩展计算和数据是有效的，但高级 AI 的真正进步需要在抽象、情商和科学推理等领域进行根本性创新。

**战术建议：**
- 超越电流互感器架构，寻找抽象和创造力方面的创新。
- 识别对象识别或空间智能等 'North Star' 问题，以推动 model 开发。

*时间戳：00:26:44*

---

> "A simple way to understand a world model is that this model can allow anyone to create any worlds in their mind's eye by prompting whether it's an image or a sentence. And also be able to interact in this world whether you are browsing and walking or picking objects up or changing things as well as to reason within this world."

**洞察：** World models 代表了从被动内容生成到创建交互式、可导航和基于理性的 3D 环境的转变。

**战术建议：**
- 开发 models，允许在 3D 空间内进行交互和推理，而不仅仅是 2D 输出。
- 使用世界 models 作为体现 AI（机器人）和空间智能的基础。

*时间戳：00:34:56*

---

> "It turns out simpler model with a ton of data always win at the end of the day instead of the more complex model with less data... why can't bitter lesson work in robotics alone? ...you hope to get actions out of robots, but your training data lacks actions in 3D worlds... we have to find different ways to fit a, what do they call, a square in a round hole, that what we have is tons of web videos."

**洞察：** 'Bitter Lesson'（扩展数据/ 计算）更难应用于机器人技术，因为与 LLMs 的大量文本相比，缺乏高质量的 3D 动作数据。

**战术建议：**
- 使用远程操作或合成数据补充网络视频数据来训练机器人 models。
- 认识到机器人技术需要实体和供应链，使得产品化历程比纯软件 AI 更长。

*时间戳：00:41:17*


## Dhanji R. Prasanna
*Dhanji R. Prasanna*

> "Our number one priority is through automate Block, which means getting AI and getting AI forms of automation through our entire company. ... we find engineering teams that are very, very AI forward that are using Goose every day are reporting about eight to 10 hours saved per week, and this is self-reported."

**洞察：** 通过 AI 将内部自动化视为公司的首要任务，以推动生产力的大幅提高。

**战术建议：**
- 通过 'manual hours saved' 衡量 AI 对所有部门（而不仅仅是工程部门）的影响
- 利用数据科学家通过 PR 量等吞吐量指标来验证自我报告的生产力提升

*时间戳：00:15:46*

---

> "The truth is the value is changing every day. And so you need to be adaptable and look at what the value is today and plan for what the value will be tomorrow and then slowly expand to the areas where it's most efficacious."

**洞察：** AI 策略必须灵活，因为底层 models 的功能正在快速发展。

**战术建议：**
- 确定 AI 目前优于人类的领域（例如，简单的工具构建）与表现不佳的领域（例如，复杂的架构）
- 顺应 model 改进的浪潮，而不是等待该技术的 'final' 版本

*时间戳：00:17:17*


## Drew Houston
*Drew Houston*

> "Dash connects to all your different apps. It gives you universal search. Then obviously after ChatGPT, not only can you do conventional search, but you can ask questions in natural language, and answer a lot of the questions that ChatGPT can't because it's not connected to your stuff."

**洞察：** AI product strategy 应侧重于通过将 LLMs 连接到碎片化的proprietary user data来解决 'context' 问题。

**战术建议：**
- 构建连接器平台来索引 SaaS 应用程序的 'known universe'，以提供个性化的 AI 答案。
- 专注于通用搜索和natural language查询作为组织用户工作生活的方式。

*时间戳：01:11:08*


## Dharmesh Shah
*Dharmesh Shah*

> "we're going from what was an imperative model... to what engineers would call a declarative model. A declarative model is you describe the outcome you want, not the steps to get there"

**洞察：** AI product strategy的核心转变是从分步用户指令（点击/ 滑动）转向基于结果的描述（natural language）。

**战术建议：**
- 确定可以消除 user's thought and the software' 接口之间的 'translation layer' 的用例。
- 构建允许用户表达意图而不是执行步骤的产品。

*时间戳：01:34:31*


## Dylan Field
*Dylan Field*

> "I was looking online on social media and I think people are already zeroing in the right conversation, which is, okay, in a world of more software being created by AI, what does that mean and the impact on craft and the impact on quality and the need to have more unique design and how design is a differentiator."

**洞察：** 在 AI 驱动的软件环境中，product strategy必须注重craft和独特设计作为主要竞争优势。

**战术建议：**
- 评估 AI 生成的特征如何影响产品的整体质量和 'soul'
- 确定 AI 可以处理 'obvious' 任务的领域，以便人们能够专注于独特的差异化

*时间戳：03:37*

---

> "PMs are no longer saying to the designer, 'Hey, can you draw this thing out for me?' That frees up designer time to go explore more deeply the stuff they need to go into and it allows anyone to add to that first conversation of, where should we go?"

**洞察：** AI 将产品开发流程从执行重（绘制模型）转变为探索重（战略方向）。

**战术建议：**
- 使用 AI 使非设计功能的原型制作过程民主化
- AI 策略的重点是缩短从想法到工作原型的路径

*时间戳：00:45:24*


## Edwin Chen
*Edwin Chen*

> "I'm worried that instead of building AI that will actually advance us as a species, curing cancer, solving poverty, understand the universe, we are optimizing for AI slop instead. But we're optimizing your models for the types of people who buy tabloids at a grocery store. We're basically teaching our models to chase dopamine instead of truth."

**洞察：** 当前的 AI 开发存在优先考虑参与和 'flashy' 响应而不是准确性和有意义的人类进步的风险。

**战术建议：**
- 避免仅仅为了用户参与或 'dopamine' 点击而优化 models
- 专注于 'truth' 和高实用性结果，而不是表面性能

*时间戳：00:01:18*

---

> "I don't trust the benchmarks at all... the benchmarks themselves are often honestly just wrong. They have wrong answers... these benchmarks at the end of the day, they often have well-defined objective answers that make them very easy for models to hill-climb on in a way that's very different from the messiness and ambiguity of the real world."

**洞察：** 标准 AI 基准测试通常存在缺陷且容易被欺骗，无法代表真实世界的性能和模糊性。

**战术建议：**
- 对 model 在学术基准上的表现持怀疑态度
- 优先针对混乱、模糊的现实世界任务而不是客观答案基准测试 models

*时间戳：00:18:00*

---

> "The way we really care about measuring model progress is by running all these human evaluations... because or searchers or annotators, they are experts at the top of their fields, and they are not just giving your responses, they're actually working through the responses deeply themselves... they're going to evaluate the models in a very deep way, so they're going to pay attention to accuracy and instruction following, all these things that casual users don't"

**洞察：** 领域专家进行的深度人工 evaluation 优于随意的user feedback或衡量真实 model 进度的自动基准。

**战术建议：**
- 使用专家人工注释者进行事实检查并深入 evaluate model 输出
- 超越 'vibes' 和华丽的响应来测量准确性和指令遵循

*时间戳：00:20:15*

---

> "I've realized that the values that the companies have will shape the model... Do you want a model that says, 'You're absolutely right. There are definitely 20 more ways to improve this email,' and it continues for 50 more iterations or do you want a model that's optimizing for your time and productivity and just says, 'No. You need to stop. Your email's great. Just send it and move on'?"

**洞察：** AI models 将根据其创建者选择的特定值和目标函数变得越来越差异化。

**战术建议：**
- 定义你希望 AI 产品体现的特定 'personality' 和价值体系
- 决定是否针对用户参与度（花费的时间）或用户生产力（节省的时间）进行优化

*时间戳：00:48:20*


## Eoghan McCabe
*Eoghan McCabe*

> "You don't have a choice. AI is going to disrupt in the most aggressive violent ways. If you're not in it, you're about to get kicked out of all of it."

**洞察：** AI 颠覆是一种生存威胁，需要积极、全面的承诺，而不是增量采用。

**战术建议：**
- 承认 AI 将颠覆几乎所有软件类别。
- 积极行动，成为颠覆的一部分，而不是与之对抗。

*时间戳：00:00:00*

---

> "We were only six weeks into the launch of GPT 3.5 when we actually had a beta version of Fin. I got a text from Des, my co-founder, a week or so after the launch of GPT 3.5 and he said, 'The AI team have something interesting and they actually think we could make a product out of this.'"

**洞察：** 当发生基础技术转变时，原型设计的速度至关重要。

**战术建议：**
- 使现有 AI/ML 团队能够立即尝试新的 models。
- 目标是在 model 主要版本发布后的几周内获得工作原型。

*时间戳：00:11:10*

---

> "I jumped hard on AI and announced that we were going to spend nearly $100 million of our own cash on that. We allocated a lot of capital, but I also restarted the culture."

**洞察：** 成功的 AI 转型需要大量的资本配置和文化重置，以支持高速创新。

**战术建议：**
- 专门为 AI 开发分配大量预算。
- 使公司文化与 AI 时代的需求（速度、弹性）保持一致。

*时间戳：00:28:40*


## Eric Ries
*Eric Ries*

> "AI is a management technology. The thing it does is manage intelligence and other intelligences... It will really change management a lot because it changes the individual span of control quite a lot."

**洞察：** AI's primary impact on organizations is its ability to summarize information and expand an individual' 的控制范围。

**战术建议：**
- 使用 AI 总结组织活动
- 设计 agents 时具有明确的采购政策
- 选择在各种未来场景中具有道德意义的行动

*时间戳：01:20:35*


## Ethan Smith
*Ethan Smith*

> "Answer Engine Optimization is how do I show up in LLMs as an answer?"

**洞察：** AEO 是确保产品或品牌被引用为大语言模型响应中的主要答案的战略过程。

**战术建议：**
- 专注于在各种引用中尽可能多地被提及，而不是仅仅对单个链接进行排名。
- 针对对话问题的 'long tail' 进行优化，这些问题在聊天中比传统搜索更重要。

*时间戳：00:00:02*

---

> "The LLM is summarizing many citations and so you need to get mentioned as many times as possible. Usually when you ask something like, 'What's the best tool for X?' The first answer will be mentioned the most in the citations."

**洞察：** LLMs 根据通过 RAG 检索的来源中提及的频率和权威性来确定 'best' 答案。

**战术建议：**
- 识别 LLM 所引用的具体引用（网站、视频、线程）。
- 在这些特定的高权威引用中增加品牌提及率，以提升 LLM 的内部排名。

*时间戳：00:11:18*


## Eric Simons
*Eric Simons*

> "Software is deterministic. When you write code and you hit run, it either runs or it doesn't... It makes technical sense why, of anything, LLMs are going to get insanely better at writing code than probably most other types of applications for LLMs."

**洞察：** AI 策略应侧重于确定性垂直领域，其中可以通过自动化测试和排列应用强化学习。

**战术建议：**
- 将 AI 的工作重点放在具有确定性结果的任务上（例如代码执行）
- 使用自动化环境通过强化学习生成高质量的训练数据

*时间戳：01:09:13*

---

> "PMs, they're going to be 'writing code', quote, unquote, instead of just writing a JIRA ticket and waiting for a developer to do it... The winners, at least, their org charts are going to completely change, and how they approach building products and shipping products."

**洞察：** AI 将转变组织结构，使 PMs 和设计师直接驱动 UI 的'coding'，而工程师则专注于复杂的非商品逻辑。

**战术建议：**
- 准备一个组织结构图，其中 PMs 和设计人员可以通过 AI 直接 'fingertip' 访问代码库
- 将工程资源从 'cookie-cutter' UI 工作转向智力挑战任务

*时间戳：00:55:30*


## Geoffrey Moore
*Geoffrey Moore*

> "From a customer's point of view, there's AI in the early market, there's AI in the bowling alley, there's AI in the chasm, there's AI in the tornado, and there's AI on Main Street."

**洞察：** AI 产品同时存在于采用生命周期的所有阶段，每个阶段都需要不同的策略。

**战术建议：**
- 确定你的 AI 功能是 'Main Street' 生产力插件（如 Copilot）还是 'Bowling Alley' 专用解决方案（如 AI 辅导）。
- 对于专业的 AI，专注于高生产率回报和适度风险。

*时间戳：00:59:50*


## Gaurav Misra
*Gaurav Misra*

> "Our goal specifically for video is not to build professional tools... We're building for the person who could not have created video before."

**洞察：** AI strategy的重点是通过弥合技能和时间差距来降低非专业人士的进入门槛。

**战术建议：**
- 确定 AI 可以为缺乏专业工具的用户桥接的 'skill gaps' 或 'time gaps'。
- 专注于特定的 AI 利基（如谈话视频），而不是解决实际问题的通用生成。
- 区分 'documentation' 视频（真实）和 'storytelling' 视频（AI 增强），以指导安全和产品重点。

*时间戳：00:10:55*


## Hamel Husain & Shreya Shankar
*Hamel Husain & Shreya Shankar*

> "To build great AI products, you need to be really good at building evals. It's the highest ROI activity you can engage in."

**洞察：** 开发 evaluation 系统是 AI 产品开发中最关键和高回报的活动。

**战术建议：**
- 专注打造 evals 核心能力
- 优先考虑系统测量而不是氛围检查

*时间戳：00:00:00*

---

> "Evals is a way to systematically measure and improve an AI application, and it really doesn't have to be scary or unapproachable at all. It really is, at its core, data analytics on your LLM application"

**洞察：** AI evaluation 本质上是一种应用于大语言 model 输出的数据分析的特殊形式。

**战术建议：**
- 将 evals 视为系统测量框架
- 使用数据分析原理迭代 LLM 应用程序

*时间戳：00:05:49*

---

> "You can appoint one person whose taste that you trust. It should be the person with domain expertise. Oftentimes, it is the product manager."

**洞察：** 具有领域专业知识的 'benevolent dictator' 应领导 evaluation 流程，以避免委员会驱动的停滞。

**战术建议：**
- 任命一名单一领域专家来领导开放编码
- 确保拥有最适合产品的 'taste' 的人员定义质量标准

*时间戳：00:01:09*


## Grant Lee
*Grant Lee*

> "It's not just one model. It's maybe 20 plus models powering all different parts of the product, and then you're thinking about the orchestration that's required and you're thinking about, obviously if you're experimenting constantly being able to test across the newest models versus models that have been around that are cheaper, you're doing a lot to really... Your job is to, again, align value, maximize the value you're delivering to the end user in a way that's sustainable for you as a business."

**洞察：** 耐用的 AI 产品超越了简单的 'wrappers'，通过编排多个 models 来解决深层的端到端用户工作流程。

**战术建议：**
- 拥有端到端工作流程，而不仅仅是提供单个 AI 功能。
- 使用不同的 models 来完成不同的任务（例如，一种用于轮廓，一种用于视觉布局，一种用于图像生成）。
- 不断尝试新的 models，以平衡性能与inference cost。

*时间戳：01:20:15*


## Hamilton Helmer
*Hamilton Helmer*

> "Will AI models develop so that they learn in a way that for one user's interaction helps another user's interaction? That would be a powerful network economy. Or if it learns, if you think of if it learns about you and becomes a better psychiatrist or something, then that's a switching cost."

**洞察：** AI 可以通过数据驱动的网络经济或深度个性化带来的高转换成本来创造战略力量。

**战术建议：**
- 探索 AI 学习如何创建网络经济，其中一个用户的数据可以改善所有其他用户的体验。

*时间戳：00:39:44*


## Guillermo Rauch
*Guillermo Rauch*

> "When you're building AI products, it's a constant stream of user feedback. So for people that are thinking about not building AI products, it's going to be hard to compete with something that has such a tight feedback loop with users. The whole idea is to capture users' feedback so the next iteration of the model, the prompt, the fine-tuning, the examples, the rag is better."

**洞察：** AI 产品的竞争优势是能够利用源源不断的user feedback来立即改进底层 model、RAG 或 prompts。

**战术建议：**
- 构建基础设施来捕获用户 'thumbs up/down'，以通知下一次迭代的微调。
- 将user feedback视为 RAG（Retrieval- 增强一代）改进的直接输入。

*时间戳：01:02:40*


## Gustav Söderström
*Gustav Söderström*

> "The internet started with curation... then the world switched from curation to recommendation... And I think what we're entering now is we're going from your curation to recommendation to generation. And I suspect it will be as big of a shift that you will eventually have to rethink your products."

**洞察：** 从基于推荐的产品到基于生成的产品的转变需要对用户界面和业务 models 进行根本性的重新思考。

**战术建议：**
- 识别用户不知道自己想要什么的 'zero intent' 用例，并使用生成式 AI 来填补空白
- 区分使用 AI 进行迭代改进（安全、分类）与核心生成功能

*时间戳：00:13:30*

---

> "The way to think about these diffusion models if and when they get good enough at generating music is probably the same like an instrument. It's just a much more powerful instrument and we'll probably see a new type of creator that wasn't proficient at any instrument."

**洞察：** Generative AI 应被视为一种高杠杆工具，它可以实现新的流派和类型的创作者，而不仅仅是现有艺术的替代品。

**战术建议：**
- 重点关注 AI 如何帮助创作者成为 'truly unique'，而不仅仅是生成通用内容
- 寻找新业务 models，让权利持有者从生成技术中受益

*时间戳：00:22:51*


## Hilary Gridley
*Hilary Gridley*

> "Designing reward loops... The reward loop needs to be powerful, it needs to be immediate, and it needs to be emotional, so that when this person does the thing that you want them to do, they feel like a million bucks. ... I like Custom GPTs as a tool for helping people learn to use LLMs... because they get the joy of like, 'Oh, this helps me. This was cool,' without any of the despair of, 'Oh, I'm not very good at prompting.'"

**洞察：** 推动 AI 的采用需要设计即时的情感奖励循环，以最大限度地减少学习新工具的摩擦。

**战术建议：**
- 从有趣、低风险的 AI 用例（例如假期计划）开始养成习惯。
- 提供预构建的定制 GPT，以便用户无需先掌握 prompting 即可立即获得价值。
- 确保 AI 输出提供 'million bucks' 的成就感或节省时间。

*时间戳：01:05:48*


## Inbal S
*Inbal S*

> "The user of the AI tools to develop software needs to form a different thinking. You need to start figuring out how are you using these AI tools to help you be successful. And it's no longer just the actual code writing, it's really evolving your thinking to the big picture, to the connected experience, to connected systems"

**洞察：** AI 将开发人员的角色从战术代码编写转变为高级系统架构和全局思维。

**战术建议：**
- 专注于理解系统和环境而不仅仅是语法
- 利用 AI 处理简单代码，以便初级开发人员可以更早地学习架构

*时间戳：00:00:00*

---

> "Generative AI will replace humans. I don't see that happening in the near future. The way I think about it, you always need that human in the loop because AI cannot replace innovation. That creative spark, that creative thinking that is the center of humanity, this will not be replaced by AI"

**洞察：** AI 是一个提高效率的工具，但人类的创新和'creative spark'仍然是无法自动化的核心。

**战术建议：**
- 为所有 AI 生成的输出保留 'human in the loop'
- 将人力集中在创新和创造性问题解决上，而不是重复性任务上

*时间戳：00:05:11*

---

> "What is that problem that we're trying to solve and how can we leverage AI better to help solve the problem versus what do we do with AI? So it's really working backwards from the customer problem from what we're trying to solve, and then realize what are the best tools that we have in order to do that work better"

**洞察：** 从客户问题入手，确定 AI 是否是解决问题的正确工具，以避免 'AI for AI' 的缘故。

**战术建议：**
- 在选择 AI 作为解决方案之前，从客户问题出发进行逆向分析
- 确定手动或高摩擦工作流程作为 AI 集成的主要候选者

*时间戳：14:38*

---

> "The design philosophy for Copilot is very much aligned with the working backwards concept... It's really putting yourself in the shoes of your customers and figuring out what is it that they need, how is that experience going to work for them? If it's an extra tool and if you need to ask for it and if you need to ask for it or if you need to wait for it, then developers will not adopt it."

**洞察：** AI 工具必须无缝集成到现有工作流程中，以避免阻碍采用的摩擦。

**战术建议：**
- 将 AI 功能设计得直观、顺畅
- 确保 AI 助手不会“'t require the user to '等待”或执行额外步骤来获取价值

*时间戳：19:05*

---

> "There is no one metric to rule them all. It's a combination of the things that you're looking to measure out of adopting AI... productivity is not the right metrics against each one of these components. When we're implementing AI to GitHub Advanced Security, writing more secure code is the right element. It's like how many secrets were we able to prevent from leaking?"

**洞察：** AI 的成功应该通过特定的结果（如安全性或质量）来衡量，而不是通过单一的通用生产力指标来衡量。

**战术建议：**
- 测量 'time to value' 而不仅仅是 'time saved'
- 使用特定的质量指标，例如阻止的秘密或检测到的错误以确保安全 AI

*时间戳：20:35*


## Howie Liu
*Howie Liu*

> "How would you execute on that mission using a fully AI native approach? If you can't, then you should find a buyer and then if you really care about this mission, go and start the next carnation of it."

**洞察：** 通过全新的 AI 原生镜头评估你的产品使命，以确定现有资产是优势还是劣势。

**战术建议：**
- 问：'How would an AI-native company execute on our mission?'
- 使用 AI 作为 'DSL'（领域特定语言）来操作现有产品原语，而不是从头开始生成所有内容
- 优先考虑 'vibe coding' 和 agentic 应用程序构建，而不是传统的纯 GUI 界面

*时间戳：00:35:08*

---

> "I think to really understand the solution space of what's possible, you have to be in the details. I mean, literally, you can't just look at screenshots or a pre-recorded video of a new product feature. AI is something you have to play with"

**洞察：** 要了解 AI 解决方案空间，领导者必须亲自尝试底层原语和 models，而不仅仅是审查最终产品。

**战术建议：**
- 通过 API 或聊天界面直接使用底层原语，以了解 model 边界
- 专注于创建视觉隐喻和可供性，帮助用户理解底层 AI 功能

*时间戳：00:12:46*


## Ivan Zhao
*Ivan Zhao*

> "I always feels like AI language model feels like a new type of wood. It feels like aluminum. It's a new type of material... Mass air travel wasn't available until aluminum become cheap enough that people can make airplanes that support this at cost... AI is really good with bundled offerings. AI is really good with horizontal tools."

**洞察：** AI 应被视为一种新的原材料，可以实现以前不可能的架构权衡，特别是有利于水平、捆绑平台。

**战术建议：**
- 利用 AI's ability to reason across disparate data sets to strengthen a horizontal product' 的价值主张。
- 构建 AI 'connectors' 将外部数据拉入你的核心生态系统，以增强 AI 的推理能力。

*时间戳：00:39:13*

---

> "The first product was our AI writer product. Second product is AI Q&A or connectors. Please look at all the information in Notion and give your answer... the third one, which is even more fascinating... if we're just putting AI coding agent on top of it, you can create any kind of knowledge, customer software, customer agent for whatever your vertical use cases you need."

**洞察：** AI 产品演变从简单的生成（编写）到 retrieval（问答）再到自主组装（agents 构建定制软件）。

**战术建议：**
- 序列 AI 的特点是从低复杂度（写入）到高复杂度（自主 agents）。
- 使用 AI 通过让'blank slate'为用户组装组件来解决模块化工具的'blank slate'问题。

*时间戳：00:58:17*


## Jake Knapp + John Zeratsky
*Jake Knapp + John Zeratsky*

> "We found that it's especially valuable for AI startups. So it just turns out that a lot of the complex issues you have to figure out with turning something that may not initially be trustworthy may require a big behavior shift to customers who aren't used to working in this way and sometimes artificial intelligence can produce things that feel kind of alien to people. And so making this stuff actually useful, more than just a chatbot with little stars that's in the corner... but something that's really meaningful."

**洞察：** AI product strategy需要解决用户的信任和重大行为转变问题。

**战术建议：**
- 专注于使 AI 具有 'meaningful' 功能，而不仅仅是添加通用聊天机器人。
- 将 AI 引入传统工作流程时解决 'trust hurdle' 问题。

*时间戳：01:31:20*


## Jason Droege
*Jason Droege*

> "The general trend right now is going from models knowing things to models doing things. The next question becomes, what can it do for me? How does the agent make decisions for you?"

**洞察：** AI 的战略前沿正在从知识 retrieval 转向 agentic 行动和决策。

**战术建议：**
- 将产品开发重点放在 agentic 工作流程上，其中 models 在软件环境中导航
- 设计允许 agents 在准确性较低时向人类弹出反馈的系统

*时间戳：00:35:47*

---

> "These things take 6 to 12 months to get them truly robust enough where an important process can be automated. Like with any of these major tech revolutions, headlines tell one story and then on the ground, laying broadband means you need to dig up every single road in America to lay it."

**洞察：** 企业 AI 自动化需要大量 'operational chiseling' 和时间（6-12 个月）才能达到production-grade reliability。

**战术建议：**
- 规划超出initial POC (POC) 的长实施周期
- 专注于mission-critical processes的可靠性和 'five nines' 准确性

*时间戳：00:39:00*


## Jonathan Becker
*Jonathan Becker*

> "The effect ultimately that we've seen from a human capital point of view is displacement. We have more people now than we've ever had, but the nature of the work that they do is more strategic. It's more about modeling, validation, asking the right questions, being focused around creative levers. And less so the like trench work of implementation and bid modifiers at the keyword level on Google search, and some of the really hardcore manual analysis we had to do."

**洞察：** AI 将人类角色从手动执行转变为高级strategic modeling 和creative direction。

**战术建议：**
- 将human capital重点放在strategic modeling 和验证上
- 自动执行手动任务，例如bid modifiers和keyword-level analysis

*时间戳：00:00:00*


## Karina Nguyen
*Karina Nguyen*

> "Creative thinking and you kind of want to generate a bunch of ideas and filter through them and not just build the best product experience. I think it's actually really, really hard to teach the model how to be aesthetic or really good visual design or how to be extremely creative in the way they write."

**洞察：** creative reasoning、美学和high-level idea filtering仍然难以自动化，但对于 AI 产品团队来说却是高价值技能。

**战术建议：**
- 重点培养 'aesthetic' 和 'creative' judgment，而 models 目前缺乏。

*时间戳：00:00:26*

---

> "Because file uploads... It's like form follows function. It's like the form factor, the file uploads can enable people to just literally upload anything, the books, any reports, financial and ask any task to the model."

**洞察：** AI 中的产品价值通常来自form factor（如文件上传），而不仅仅是underlying model capability。

**战术建议：**
- 设计符合熟悉的用户任务（例如上传文档）的form factor以解锁 model utility。

*时间戳：00:37:04*

---

> "You want to build for the future. So it's like it doesn't necessarily matter whether the model is good or not, good right now, but you can build product ideas such that by the time the models will be really good, it'll work really well."

**洞察：** 有效的 AI 策略涉及设计能够预见未来 model 改进而不仅仅是当前限制的产品体验。

**战术建议：**
- 原型产品创意在今天可能会失败，但随着inference cost的下降和intelligence increases，将会成功。

*时间戳：00:43:53*

---

> "I think what models are really good at is connecting the dots, I think. It's like if you have user feedback from this source, but you also have an internal dashboard with metrics and then you have other feedback or input and then it can create a plan for you, recommendations even."

**洞察：** AI 非常擅长将不同的数据源（反馈、指标、日志）合成为一个cohesive strategy 或 plan。

**战术建议：**
- 使用 LLMs 聚合和总结user feedback和内部指标，以识别最痛苦的user flows。

*时间戳：00:50:10*


## Keith Coleman & Jay Baxter
*Keith Coleman & Jay Baxter*

> "take existing notes as input... have an LLM generate a ton of different variants, and then basically make the simulated jury to basically get a representative group of contributors for community notes who would be rating the note and try to predict based on their past ratings how they would rate these LLM generated notes."

**洞察：** LLMs 可用于模拟user feedback并生成可能达成共识的高质量content variants。

**战术建议：**
- 使用 LLMs 根据现有用户输入生成一段内容的多个变体
- 使用历史数据模拟user rating process，以预测哪些 AI-generated content最有帮助

*时间戳：01:39:13*


## Kevin Weil
*Kevin Weil*

> "Everywhere I've ever worked before this, you kind of know what technology you're building on... but that's not true at all with AI. Every two months, computers can do something they've never been able to do before and you need to completely think differently about what you're doing."

**洞察：** AI product strategy需要思维方式转变，因为底层技术是一个移动的目标而不是固定的基础。

**战术建议：**
- 预计技术每两个月就会改变一次
- 基于新的 model 功能频繁重新调整 evaluate 产品方向

*时间戳：00:16:19*

---

> "Our general mindset is in two months, there's going to be a better model and it's going to blow away whatever the current set of limitations are... If you're building and the product that you're building is kind of right on the edge of the capabilities of the models, keep going because you're doing something right."

**洞察：** 通过构建几乎可能的功能来采用 'model maximalism'，因为 model 可能会在发布时赶上。

**战术建议：**
- 不要针对当前 model 的限制过度设计脚手架
- 构建可推动 model 功能当前优势的产品

*时间戳：00:31:12*

---

> "I think the future is really going to be incredibly smart, broad-based models that are fine-tuned and tailored with company-specific or use case-specific data so that they perform really well on company-specific, or use case-specific things."

**洞察：** AI strategy的下一阶段涉及通过微调将强大的通用 models 与proprietary行业特定数据相结合。

**战术建议：**
- 识别可用于微调的非公开数据
- 开发自定义基准来衡量特定用例的性能

*时间戳：00:23:58*

---

> "We use ensembles of models much more internally than people might think... If we have 10 different problems, we might solve them using 20 different model calls, some of which are using specialized fine-tuned models... You want to break the problem down into more specific tasks versus some broader set of high level tasks."

**洞察：** 复杂的 AI 产品应构建为专门的、经过微调的 models 的整体，而不是单个通用的 model 调用。

**战术建议：**
- 将广泛的问题分解为具体的子任务
- 根据每个子任务的延迟和成本需求，使用不同的 model 大小（例如 4o 与 4o mini）

*时间戳：01:00:32*


## Luc Levesque
*Luc Levesque*

> "What we're about to see is basically Google... showed a big box on top of the search results that answers the query directly... how do you optimize in a world where it's not so much about optimizing for the platform, but teaching the AI what you do and why you're the best in the world at it."

**洞察：** 搜索引擎中的生成式 AI 将策略从关键字优化转移到 'teaching' 和 AI 来推荐你的品牌。

**战术建议：**
- 识别有被 AI 搜索摘要蚕食风险的 'informational' 关键字
- 将焦点转向 'transactional' 意图，用户仍然需要单击才能完成操作

*时间戳：00:52:42*


## Madhavan Ramanujam
*Madhavan Ramanujam 2.0*

> "AI pricing is very different from the previous vintage of companies... we have moved from software being a pay for access to now you're paying for work delivered. So the monetization model's become key."

**洞察：** AI 将价值主张从提供工具（访问）转变为提供结果（工作），从而需要对 models 的定价进行根本性改变。

**战术建议：**
- 关注 'pay for work delivered' 而不是 'pay for access'
- 通过准确展示 AI 如何影响客户 KPI 来解决 'attribution problem'

*时间戳：00:27:51*

---

> "What that would mean is, how do I build functionality in the products to actually show attribution, how do I build more agentic workforces to take the human out of the loop and be more autonomous, and being thoughtful about your vision and strategy so that you will orient yourself towards more outcome-based pricing models."

**洞察：** AI 策略应侧重于提高产品自主性和构建明确跟踪和显示价值归因的功能。

**战术建议：**
- 构建展示客户 KPI 价值归属的仪表板
- 开发 agentic 功能以从 'copilot' 迁移到 'autonomous' 模式

*时间戳：00:46:05*


## Logan Kilpatrick
*Logan Kilpatrick*

> "I'm really, really excited to see more people. I think 2024 is the year of multimodal AI, but it's also the year that people really push the boundaries of some of these new UX paradigms around AI."

**洞察：** AI 产品开发的下一阶段将超越聊天界面，进入多模式和新的 UX 范例，例如无限画布。

**战术建议：**
- 探索 'infinite canvases' 等接口，其中 AI 可以以非线性格式填充详细信息、文件和视频。
- 超越主流的聊天界面，寻找更多以人为本的数据交互方式。

*时间戳：00:09:30*

---

> "I think GPTs is our first step towards the agent future. Again, today when you use A GPT, it's really you send a message, you get an answer back almost right away... I think as GPTs continue to get more robust, you'll actually be able to say, 'Hey, go and do this thing and just let me know when you're done.'"

**洞察：** AI 策略正在从即时聊天响应转向可以执行异步复杂任务的 'agents'。

**战术建议：**
- 设计允许用户将任务委派给 AI 并在完成后收到通知而不需要主动等待的产品。
- 为 AI 在有意义的请求上花费更多 'thought time' 的未来而构建。

*时间戳：00:45:48*

---

> "I heard from a friend that there's kind of this tip that when you're building products today, you should build towards a GPT-5 future, not based on limitations of GPT-4 today."

**洞察：** 产品路线图应针对未来 models 的预测功能进行设计，而不是受当前 model 限制的约束。

**战术建议：**
- 假设未来的 models 将更快、更智能，并解决更高层次的问题。
- 规划一个 AI 工具变成 'normal' 并快速集成的世界，而不是假设它们仍然是新鲜事物。

*时间戳：00:48:22*

---

> "I think products that move beyond this chat interface really are going to have such an advantage. And also, thinking about how to take your use case to the next level... What I really want is just ask my question... Get an answer to that question in a very data grounded way."

**洞察：** AI 产品的最大机会是用直接的、基于数据的natural language答案取代复杂的仪表板和过滤器。

**战术建议：**
- 确定用户当前导航复杂 UI 过滤器的区域，并将其替换为单个natural language查询。
- 重点提供数据中 'what is happening' 的摘要，而不仅仅是显示原始示例。

*时间戳：00:55:34*


## Marc Benioff
*Marc Benioff*

> "AI is the defining technology of our lifetime and probably any lifetime."

**洞察：** AI 不仅仅是一项功能，而且是一项根本性转变，需要对产品方向进行彻底的重新 eval 调整。

**战术建议：**
- 将 AI 作为未来所有产品开发的主要镜头

*时间戳：36:33*

---

> "Step one was we had to automate all these customer touch points... step three is the agentic platform on top of that. Then, the fourth layer that will come will be the robotic drone layer where those robots and drones will then feed off of the platform and all of these capabilities."

**洞察：** AI 产品的演变遵循特定的顺序：接触点自动化、数据聚合、agentic 层，最后是物理机器人。

**战术建议：**
- 首先自动化客户接触点以创建交互基线
- 将所有交互数据聚合到统一的'Data Cloud'中
- 在数据之上构建 'agentic' 层来处理自主任务

*时间戳：37:18*


## Marily Nika
*Marily Nika*

> "I believe that ballpark managers will be AI product managers in the future. And this is because we see all products needing to have a personalized experience, a recommender system that is actually good."

**洞察：** 随着个性化和自动化成为标准要求，AI 将成为产品管理的默认选择。

**战术建议：**
- 预计每个产品最终都需要个性化的体验或推荐系统。
- 为 'AI PM' 和 'Generalist PM' 角色合并的未来做好准备。

*时间戳：00:08:39*

---

> "Don't do it for your MVP. It makes zero sense. Do not waste time of data scientists that can train models with using powerful machines that are going take weeks to train. This is because if you have an MVP and you just want to get buy-in for an idea or feature that may use AI in the future, take it, create a little figma prototype and just show it some users, just fake what the AI is going to be doing."

**洞察：** 避免将实际的 AI 用于 MVP；相反，使用低保真原型来实现 'fake' AI 功能并首先验证市场。

**战术建议：**
- 使用 Figma 原型模拟 AI 功能以进行初始用户测试。
- 只有在验证了问题并拥有足够的数据后，才投资培训 models。

*时间戳：00:14:42*

---

> "AI product development is different. As I mentioned before, sometimes you're actually managing the problem and not the product and you're trying to secure out if there is a problem that makes sense to be answered by a smart solution."

**洞察：** AI PMing 涉及管理高度的不确定性并关注问题解决方案的契合度而不仅仅是功能交付。

**战术建议：**
- 向领导层澄清，AI/ 研究的进展可能并不总是导致发布。
- 如果 model 结果不符合假设，请准备好调整或关闭项目。

*时间戳：00:28:02*


## Marty Cagan
*Marty Cagan 2.0*

> "I've been on so many of these calls where we've been talking about the implications of probabilistic software versus deterministic software and what is okay? The lawyers are weighing in already with the legal perspective, but also ethical perspective and just if this is mission critical, is this something that we could be okay with having a probabilistic answer?"

**洞察：** AI 将 PM 的重点转向概率软件结果的可行性和道德影响。

**战术建议：**
- 评估在关键任务功能中使用概率性 AI 答案的风险。
- 在定义 AI product strategy时尽早考虑法律和道德观点。

*时间戳：00:53:45*


## Matt MacInnis
*Matt MacInnis*

> "Point solutions don't have enough data in the age of AI to be useful. You got to be able to provide the AI with a lot of context about a lot of data so it can do things. It can do joins. It can do correlations."

**洞察：** AI 的价值正在转向具有广泛的第一方数据集的平台，而不是孤立的点解决方案。

**战术建议：**
- 专注于构建 'common business data graph'，为 AI 提供有用的上下文。
- 避免通过有限的集成构建依赖于 'drinking data through a straw' 的 AI 点解决方案。

*时间戳：01:18:49*


## Matt Mullenweg
*Matt Mullenweg*

> "Llama, you can obviously download and run locally and all these sorts of things, right? You don't have to use their SaaS service. However, there's a clause in it that says if you're above a certain threshold of monthly active users... You need a license from them. And so that does not give you the freedom to use the software for any purpose."

**洞察：** 真正的开源 AI 策略要求可以自由地将 models 用于任何目的，而不会造成供应商锁定的任意用户数量限制。

**战术建议：**
- 审核 AI model 许可证中可能限制未来增长的 'user threshold' 条款
- 选择基础型 models 时区分 'open weights' 和真正的 'open source'

*时间戳：00:23:52*

---

> "But I can't wait for more automated scanning there, and I think that could vastly upgrade the security of open source. The other thing that's really exciting is right now you see people building apps and stuff and it's just sort of custom generated code, but I think the next generation of these models... is when the open source models you say like, 'Hey, build me a website.' It actually installs WordPress, and then builds on top of that."

**洞察：** AI 辅助开发的未来在于 agents，它构建在已建立的开源引擎之上，而不是生成完全自定义的、未维护的代码库。

**战术建议：**
- 使用 AI 自动对第三方插件和扩展进行安全扫描
- 直接 AI agents 构建在经过审核的开源平台之上，以确保长期可维护性

*时间戳：00:32:03*


## Mayur Kamat
*Mayur Kamat*

> "At a company level, there is an incredible set of advancements across these three areas: developer productivity, customer support, and fraud."

**洞察：** ROI 对于 AI 在企业中最直接、最大规模的是编码效率、支持自动化和基于模式的欺诈检测。

**战术建议：**
- 部署 AI co-pilot 可将开发人员的工作效率提高 20-25%。
- 使用 LLMs 自动执行 'bottom 70%' 客户支持查询。
- 应用 AI 检测欺诈者的语言和交易模式。

*时间戳：01:16:58*


## Melanie Perkins
*Melanie Perkins*

> "I think being able to integrate it into the product where it actually helps people to get their work done where it genuinely helps them to achieve their goals... AI is just kind of naturally a very critical part of that equation for us."

**洞察：** AI 应直接嵌入到现有的用户工作流程中，以减少想法与其执行之间的摩擦。

**战术建议：**
- 将 AI 工具直接嵌入到用户已经工作的核心编辑器或 'elements' 选项卡中
- 优先考虑解决特定用户请求的 AI 功能（例如教师的安全控制）

*时间戳：00:52:56*


## Michael Truell
*Michael Truell*

> "At this point, every magic moment in Cursor involves a custom model in some way... picking your spots carefully, not trying to reinvent the wheel, not trying to focus on places, and maybe where the best foundation models are excellent, but instead kind of focusing on their weaknesses, and how you can complement them."

**洞察：** 要在 AI 产品中创建 'magic moments'，开发人员应使用 models 的集合，将大型基础 models 与用于特定任务的小型专用定制 models 相结合。

**战术建议：**
- 使用定制 models 来执行需要高速（例如 <300ms）或低成本的任务。
- 将定制 model 开发的重点放在基础 models 的弱点上，而不是试图复制其一般智能。

*时间戳：00:33:18*

---

> "We take the sketches of the changes that these models are suggesting, you make with that code base. And then we have models that then fill in the details of, the high level thinking is done by the smartest models, they spend a few tokens on doing that, and then these smaller specialty incredibly fast models, coupled with some inference tricks, then take those high level changes and turn them actually into full code diffs."

**洞察：** 'ensemble' 方法（使用智能 models 进行推理并使用快速 models 进行执行）优化了质量和性能。

**战术建议：**
- 使用高推理 models（如 Sonnet 或 GPT-4）进行高级 'sketches' 工作。
- 使用更小、更快的 models 填写技术细节并生成最终输出。

*时间戳：00:37:02*


## Mihika Kapoor
*Mihika Kapoor*

> "I think that the key to being successful at zero-to-one is to honestly have optimism that borders on delusion. You need to be insane, almost like reality distortion field where you don't hear the word no, or at the very least, you translate it into a not yet."

**洞察：** 领导从零到一的 AI 计划需要 'keeper of the flame' 心态，以在早期开发的模糊性中保持势头。

**战术建议：**
- 专注于'black-boxification'——使 AI 输出具有交互性和可操作性，而不是静态的
- 在决定是否在现有公司内部建立时寻找分销或平台优势
- 利用黑客马拉松快速制作原型并确保雄心勃勃的新产品方向获得初步支持

*时间戳：01:23:12*


## Mike Krieger
*Mike Krieger*

> "The functional unit of work at Anthropic is no longer take the model and then go work with design and product to go ship a product. It's more like we are in the post-training conversations around how these things should work and then we are in the building process and we're feeding those things back and looping them back."

**洞察：** 当产品团队融入后期培训和研究流程而不是仅仅在成品 models 之上构建 UX 时，最有效的 AI 产品开发就会发生。

**战术建议：**
- 在微调和培训后阶段，让产品经理直接与研究人员一起工作。
- 重点关注 model 功能和产品体验的交集，而不仅仅是 prompting 现成的 models。

*时间戳：00:23:07*

---

> "I think there's still a lot of value in two things. One is making this all comprehensible... Two is... strategy, how we win, where we'll play... And then the third one is opening people's eyes to what's possible, which is a continuation of making it understandable."

**洞察：** 产品团队通过策略为 AI 提供独特的价值，使复杂的功能变得易于理解，并向用户展示'art of the possible'。

**战术建议：**
- 专注于缩小 'overhang'——models 的功能与用户实际使用方式之间的差距。
- 优先考虑同理心和人类心理学，使非技术用户能够理解 AI 的功能。

*时间戳：00:24:42*

---

> "I think things that are going to, I can't promise this as a five to 10 year thing, but at least one to three years, things that feel defensible or durable. One is understanding of a particular market... Two was paired with that is differentiated go to market... Then the last one is... a completely different take on what the form factor is by which we interface with AI."

**洞察：** AI 初创公司的防御力来自于深厚的垂直市场知识、专门的市场关系或全新的界面形式因素。

**战术建议：**
- 为具有复杂合规性或工作流程需求的特定行业（例如法律、生物技术）构建产品。
- 尝试 'weird' 或高级用户外形规格，现有企业采用这些外形规格的速度太慢。

*时间戳：00:47:51*


## Naomi Ionita
*Naomi Ionita*

> "I think what I described around marketing and sales, just because they really touch the dollars. It can be this ROI story around saving time, but also driving revenue. There'll be plenty of really effective examples within things like customer support. I mean the cost savings potential. There's going to be massive."

**洞察：** AI 策略应重点关注高 ROI 领域，例如销售、营销和支持，自动化直接影响利润。

**战术建议：**
- 将 AI 实施重点放在创收或高成本节约功能上，例如 SDR 出站或客户支持

*时间戳：48:48*


## Nick Turley
*Nick Turley*

> "I've never ever worked on a product that is so empirical in its nature where, if you don't stop, and watch, and listen to what people are doing, you're going to miss so much, both on the utility and on the risks, actually. Because normally, by the time you ship a product, you know what it's going to do... And with AI, because I think so much of it is emergent, you actually really need to stop and listen after you launch something."

**洞察：** AI 产品开发需要采用实证方法，因为功能和风险是自然出现的而不是预先定义的。

**战术建议：**
- 观察发布后的user behavior，以识别紧急效用和风险
- 根据现实用例而不是先验推理迭代 model

*时间戳：00:19:14*

---

> "One thing we've learned with ChatGPT is that there really is no distinction between the model and the product. The model is the product and therefore you need to iterate on it like a product."

**洞察：** 在 AI 应用中，model 和接口密不可分，需要 model 本身以产品思维进行管理。

**战术建议：**
- 针对特定的高价值用例（例如编码或写作）系统地改进 model
- 把'vibes'和个性当作产品特性来调教

*时间戳：00:29:18*

---

> "I think that in the original release, making it free was a big deal... making it free and putting a nice UI on it, very consequential in the way that you take for granted now. And this is why I think that A, distribution and the interface are continuously important even in 2025."

**洞察：** 通过免费访问和简洁的 UI 来降低摩擦对于复杂 AI 技术的大规模采用至关重要。

**战术建议：**
- 优先考虑消除摩擦（例如登录要求）以推动增长
- 使用免费套餐收集 model 迭代所需的海量数据

*时间戳：00:37:34*

---

> "If we're shipping a feature and it doesn't get 2X better as the model gets 2X smarter, it's probably not a feature we should be shipping."

**洞察：** AI 功能的一个关键试金石是它们是否与底层 model 的智能成比例地扩展。

**战术建议：**
- 根据功能从未来 model 智能增益中受益的能力来评估功能
- 专注于 'interdisciplinary' 开发，使研究和产品目标保持一致

*时间戳：01:04:23*

---

> "I started writing evals before I knew what an eval was because I was just outlining very clearly specified ideal behavior for various use cases... it might be the lingua franca of how to communicate what the product should be doing to people who do AI research."

**洞察：** 编写 evaluations (evals) 是产品经理向 AI 研究人员传达所需行为的主要方式。

**战术建议：**
- 通过概述特定用例的理想 model 行为来阐明成功
- 使用 evals 作为产品需求和技术研究之间的桥梁

*时间戳：01:14:41*


## Nicole Forsgren
*Nicole Forsgren*

> "People really fundamentally shift the way they work when they work with an AI-enabled tool... you spend more time reviewing code than writing code... we've changed what your mental model is. So we've changed the friction model that you expect. We've changed the cognitive load of what you expect."

**洞察：** AI 工具将主要的开发人员活动从创建转变为审查，从根本上改变了工作所需的认知负荷和心理 models。

**战术建议：**
- 根据 AI 工具如何为更困难的任务释放认知空间，而不仅仅是在简单任务上节省时间来评估 AI 工具。
- 将 AI 集成到工作流程时，请考虑 'trust' 和 'reliability' 等新的生产力维度。

*时间戳：00:51:04*

---

> "I think there are a lot of ways that we can pull in AI tools to help us refine our strategy, refine our message, think about the experimentation methods or targets of experimentation... because now, the engineering can go, or at least the prototyping especially, much, much faster. We can throw out prototypes. We can run any tests and experiments that are customer facing"

**洞察：** AI 通过实现快速原型设计和更快的客户实验来加速策略到执行的循环。

**战术建议：**
- 使用 AI 快速生成和测试多个战略替代方案或原型。
- 使用 AI 加速，将从创意到生产实验的反馈周期缩短至不到一周。

*时间戳：00:30:26*


## Noah Weiss
*Noah Weiss*

> "One of the big ones, was that the promise of the UI has to match the quality of the underlying data, which is to say... I think this is actually one of the failings of the various LMs right now is they all appear supremely confident even when they're completely hallucinating. I think that's going to be something that people are going to have to work on a lot, which is to figure out how to be not so faultless, to acknowledge when you're not sure."

**洞察：** 确保用户界面的置信度与底层 AI 数据的实际准确性相匹配，以维护用户的信任。

**战术建议：**
- 承认 AI 响应的不确定性，而不是在出现幻觉时出现 'supremely confident'。
- 提供数据来源的透明度以建立可信度。

*时间戳：00:21:42*

---

> "What we want to do is actually spin up a couple different teams that are focused on prototyping, using that common infrastructure but in specific directions that are all a little bit different. We've got a common ML, let's say in search team and now we have a bunch of teams that are working in parallel and different customer problems that we're trying to solve using that shared infrastructure."

**洞察：** 通过拥有一个中央基础设施/ML 团队来支持多个专注于特定客户问题的临时原型团队来组织 AI 开发。

**战术建议：**
- 使用混合 model：中央 ML 基础设施 + 分散式原型设计团队。
- 从正常的季度计划中为 AI 原型设计团队提供 'get out of jail free card'，以提高学习速度。

*时间戳：00:25:42*


## Noam Lovinsky
*Noam Lovinsky*

> "Grammarly is one of the few products where you just install it and it makes you better. You don't have to configure it, you don't have to manipulate it, you don't have to change anything about what you're doing. ... essentially it's like a huge AI achievement masquerading as a little UX innovation."

**洞察：** 成功的 AI 产品应重点关注具有零配置价值、可集成到现有工作流程中的 'meeting the user where they are'。

**战术建议：**
- 设计可集成到现有工作流程而不是需要新工作流程的 AI 功能
- 专注于 'invisible' AI，无需复杂的 prompting 或设置即可提供价值

*时间戳：00:52:14*


## Paul Adams
*Paul Adams*

> "I'd start with the thing your product does. "What's the core premise behind it? Why do people use it? What problem does it solve for them?" That kind of thing. So, go back to basics. And then ask, "Can AI do that?" And for a lot, the answer is going to be, "Yes, it can.""

**洞察：** 通过根据当前 AI 功能映射核心产品前提和客户问题来评估 AI 集成。

**战术建议：**
- 确定你的产品解决的核心问题。
- 确定 AI 是否可以取代当前解决方案或仅对其进行增强。

*时间戳：00:00:14*

---

> "You're going to need to map what your product does against what AI can do... for some of it'll be replacement. AI would replace, it'll just do it. And, in other places, it'll be augmentation. It'll augment. It'll help people."

**洞察：** AI 策略涉及决定该技术是从根本上取代工作流程还是充当 'copilot' 来帮助用户。

**战术建议：**
- 根据 AI 的编写、总结、推理和采取行动的能力映射产品功能。

*时间戳：00:22:07*

---

> "Don't bolt it on. I think some people are still in that camp... Don't be like, "Oh, we'll have a bunch of AI people..." And we do have some specialists. But generally speaking, we're trying to have everyone learn about it."

**洞察：** 避免将 AI 孤立到一个单独的团队中；相反，将 AI 知识集成到整个产品组织中。

**战术建议：**
- 鼓励通才 PMs 和工程师学习 AI 接口和框架。
- 避免创建仅向现有产品添加 AI 功能的 'side team'。

*时间戳：00:37:08*


## Ramesh Johari
*Ramesh Johari*

> "Predicting is about picking up patterns, but making decisions, it's about thinking about these differences... the first and most important thing that I feel very strongly about in what would I get a data scientist to do is... get them to be thinking in the back of their mind always that their goal is to help the business make decisions. And that the distinction between causation and correlation matters a lot."

**洞察：** 数据科学在产品中的最高杠杆作用是从简单的预测（相关性）转向为业务决策提供信息的因果推理。

**战术建议：**
- 将数据团队的重点从构建预测性 models 转移到识别特定产品变更的因果影响。

*时间戳：00:33:21*

---

> "What AI has done for us is it's massively expanded the frontier of things we could think about our problem, hypotheses we could have, maybe things we could test... I really think actually what that does is puts more pressure on the human, not less. I think it becomes more important for humans to be in the loop in interacting with these tools to drive the funneling down process of identifying what matters."

**洞察：** AI 扩大了可能的假设和创意的数量，使 'funneling' 的人类角色和优先级比以往任何时候都更加重要。

**战术建议：**
- 使用 AI 生成大量可测试的假设或创意，但保持人工监督以选择与战略目标一致的假设或创意。

*时间戳：01:09:35*


## Ravi Mehta
*Ravi Mehta*

> "I think one of the most interesting things about it is not AI as a replacement for people, but AI as a way to amplify people and make them more effective. And I think we'll see a lot of that in terms of both image generation and text generation where it's less about AI doing all the work and more about AI providing a really good starting point."

**洞察：** AI's current primary value is as an 'amplifier”为人类专家的完善提供了高质量的起点。

**战术建议：**
- 使用 AI 生成初始草稿或建议（例如指导反馈），然后由专家进行定制。
- 尝试不同的 prompting 风格（例如，行动导向与同情）来模拟不同的角色或领导风格。

*时间戳：01:14:32*


## Rahul Vohra
*Rahul Vohra*

> "I think for me the biggest surprise has been how unpredictable the user love has been in terms of what they love and what they don't love... everything I thought would work out well, people use it less than they thought they did. And everything where I was like, 'I don't know, but let's build the thing,' people love that."

**洞察：** AI 产品的成功往往是违反直觉的；简单的功能可以推动大规模的参与，而复杂的功能可能会滞后。

**战术建议：**
- 尝试使用 'commodity' AI 功能（例如书写辅助），因为它们通常具有最高的实用性。
- 准备好根据实际使用数据而不是创始人的直觉来调整 AI 路线图。

*时间戳：01:14:25*


## Roger Martin
*Roger Martin*

> "It is super hard when the guts of how you make money is under threat, and you just don't want that thing to go away... But my general advice is always the same, which is, it can take a while, but in the end the customers will triumph."

**洞察：** AI 策略通常会迫使你在保护传统收入和遵循客户偏好的 'tide' 之间做出选择。

**战术建议：**
- 确定 'customer tide' 正在移动的位置，即使它威胁到你当前的业务 model。
- 避免尝试'hold back the tide'新技术；相反，我们应该努力寻找如何在新的现实中为客户提供服务。

*时间戳：01:06:14*


## Robby Stein
*Robby Stein*

> "AI is expansionary. There's actually just more and more questions being asked and curiosity that can be fulfilled now with AI."

**洞察：** AI 不仅仅取代现有的搜索行为；它使用户能够满足更深层次的好奇心，从而扩大了查询总量。

**战术建议：**
- 确定用户当前 'hacking' 你的产品的用例（例如，将 'AI' 添加到搜索查询），以查找 AI 可以在哪些方面增加价值。
- 将 AI 功能重点放在扩展时刻，而不仅仅是取代核心基础需求。

*时间戳：00:08:54*

---

> "We wanted to be the best at informational needs, that's what's Google's all about, and so how does it find information? How does it know if information is right? How does it check its work? These are all things that we built into the model."

**洞察：** 有效的 AI 策略涉及将 models 专门用于特定领域（例如信息 retrieval），而不仅仅是通用聊天。

**战术建议：**
- 将 'check your work' 机制构建到 models 中，以确保信息任务的准确性。
- 使用查询扇出允许 models 使用搜索作为实时数据 retrieval 的工具。

*时间戳：00:18:15*


## Ryan J. Salva
*Ryan J. Salva*

> "We see it range anywhere from the upper twenties to the forties across all the different languages. ... AI is going to infuse pretty much our entire development stack in the not so distant future. Copilot is really just the very tip of the sphere for a lot of innovations and better managing maybe our build queues or helping to... Here's a great one. I don't know about you, but often the comments that I get with commit messages and PRs aren't super great. It puts a lot of effort onto the code reviewer to go figure out what the developer was actually trying to do. What if AI could summarize all of your changes with your full request and you just have to, as the contributing developer, just review it to make sure it's accurate, send it on its way, and you don't have to put in extra effort for that."

**洞察：** AI 应被视为一种增强工具，可以消除死记硬背的苦差事（例如总结 PR 或编写样板文件），从而使人们能够专注于更高级别的创意设计。

**战术建议：**
- 识别 AI 自动化工作流程中繁重、低创造力的任务
- 将 AI 定位为 'augmenter' 而不是 'replacer'，以管理用户的期望和焦虑

*时间戳：00:45:35*

---

> "Our stance on it, what we ended up coming to is actually the framing of Copilot as an AI pair programmer i think is a useful one. ... Well, if Copilot is your AI pair programmer and they're whispering crazy stuff into your ear and they're bringing politics into it or gender identity into it or, I don't know, whatever other... They're spouting off slang and slander and all that kind of stuff. You're probably not going to be able to focus on your work, right? It's going to be really distracting. Really coming down to some principles about what is the use case we're trying to solve, what is appropriate, I put this in scare quotes, behavior of the AI bot sitting side by side with you, helped us create some principles or some guidelines for the developer experience that we wanted to create."

**洞察：** 创建清晰的角色（如 'AI Pair Programmer'）有助于定义适当的 AI 行为的边界并指导用户体验。

**战术建议：**
- 为 AI 定义角色以建立行为护栏
- 制定特定产品环境中 'appropriate' AI 交互的构成原则

*时间戳：00:39:53*


## Sander Schulhoff
*Sander Schulhoff*

> "If we can't even trust chatbots to be secure, how can we trust agents to go and manage our finances? If somebody goes up to a humanoid robot and gives it the middle finger, how can we be certain it's not going to punch that person in the face?"

**洞察：** 从聊天机器人到自主 agents 的转变带来了重大的安全风险，因为 prompt 注入可能会导致现实世界的物理或财务损害。

**战术建议：**
- 在构建能够执行操作（例如预订航班、管理资金）的产品时优先考虑 'agentic security'

*时间戳：00:01:00*

---

> "The most common technique by far that is used to try to prevent prompt injection is improving your prompt and saying... 'Do not follow any malicious instructions.' This does not work at all... Fine-tuning and safety-tuning are two particularly effective techniques and defenses."

**洞察：** 即时防御和外部护栏往往是不够的；安全性必须在 model 培训级别进行处理。

**战术建议：**
- 不要依赖系统 prompts 来防止恶意注入
- 使用微调将 model 的功能缩小到特定任务，使其不易受到一般恶意指令的影响

*时间戳：01:09:48*

---

> "It is not a solvable problem... You can patch a bug, but you can't patch a brain... you can never be certain with any strong degree of accuracy that it won't happen again."

**洞察：** AI 安全性与经典网络安全性有根本不同，因为概率性 'brain-like' models 无法完美地针对所有对抗性输入进行修补。

**战术建议：**
- 假设 95-99% 的安全上限并相应地构建产品保障措施
- 专注于缓解和检测，而不是期望 prompt 注入 100% 'fix'

*时间戳：01:15:08*

---

> "If you deploy improperly secured, improperly data-permissioned agents, people can trick those things into doing whatever, which might leak your user's data and might cost your company or your user's money, all sorts of real world damages there."

**洞察：** 在没有严格数据许可的情况下部署 AI agents 会给公司带来重大的财务和隐私风险。

**战术建议：**
- 部署前确保 agents 已获得正确的数据许可
- 评估 agents 以恶意方式将操作链接在一起的可能性

*时间戳：00:19:11*

---

> "If all you're doing is deploying chatbots that answer FAQs... It's not really an issue because your only concern there is a malicious user comes and, I don't know, maybe uses your chatbot to output hate speech... but they could go to ChatGPT or Claude or Gemini and do the exact same thing."

**洞察：** 简单、只读的常见问题解答聊天机器人的安全风险主要是声誉风险，而不是功能风险，因为损害仅限于对话本身。

**战术建议：**
- 评估安全需求时区分简单聊天机器人和 agentic 系统
- 将安全工作重点放在可以采取行动或访问敏感用户数据的系统上

*时间戳：00:46:24*


## Sarah Tavel
*Sarah Tavel*

> "LLMs may make it possible to bring on a supply type that maybe the long tail, that was just, it was too much effort to reach out to them, onboard them, but maybe if you automate that work, you actually create an opportunity to expand the supply in a way that none of us can anticipate right now."

**洞察：** AI 可以通过自动化长尾供应商的高摩擦入职和管理来解锁新的市场供应。

**战术建议：**
- 寻找以前过于昂贵而无法手动获取的供应部分，并使用 LLMs 来自动化其集成

*时间戳：01:44:15*


## Shaun Clowes
*Shaun Clowes*

> "LLMs can only be as good as the data they are given and how recent that data is. They're ultimately like information shredders. They are limitless information eaters. You can never have enough information to give to an LLM to truly gain its value."

**洞察：** AI 产品的有效性与提供给 model 的数据上下文的数量、质量和新近度直接相关。

**战术建议：**
- 优先构建为 LLMs 提供高质量实时上下文的数据管道，而不是简单地选择 'best' model。

*时间戳：00:21:11*

---

> "It's a data management problem. It's getting access to good data, getting access to high quality data, getting access to timely data and getting it to the LLM to get the LLM to make a smart decision. That's where 90% of the calories go."

**洞察：** AI 产品开发主要是数据管理挑战，而不是 modeling 或 prompting 挑战。

**战术建议：**
- 将 90% 的精力投入到 AI 的数据质量和可访问性上，而不仅仅是 UI 或 prompt 工程。

*时间戳：00:23:21*


## Shweta Shriva
*Shweta Shriva*

> "We're using a lot of human driving data to train our deep models. So it's important to make sure that the behavior of the car doesn't seem robotic... we have deep learned models that can understand what the other road users' intent is. So, stuff like which way the pedestrian is looking or what is their body orientation because that could tell you which way they're headed."

**洞察：** AI 产品应该利用人类行为数据来模仿自然交互和社会规范，而不是显得机器人。

**战术建议：**
- 使用人类行为数据来训练 models，以避免不自然或 'robotic' 产品交互。
- 将意图识别（例如身体方向、凝视）融入 AI models 中，以处理复杂的人类环境。

*时间戳：06:07*


## Tomer Cohen
*Tomer Cohen*

> "What is the objective of the algorithm? I would challenge you to ask folks... what is the objective of the algorithm and can you write it down for me on a board? They should be able to do so, ultimately it's a mathematical formula and then it's like what features have you added to the algorithm? ...what investment do you have in data collections and fine-tuning?"

**洞察：** AI 优先的产品领导者必须超越将 AI 视为black box的做法，并掌握 model 的目标、功能和数据策略。

**战术建议：**
- 将算法的数学目标定义为核心产品要求。
- 投资基础设施和数据收集作为主要产品杠杆，而不仅仅是 UI 功能。
- 从控制确切的用户体验转向控制 AI 使用的 'ingredients'（数据和指南）。

*时间戳：00:40:13*

---

> "AI is the ultimate matchmaker. It's underutilized, it's misunderstood... in a marketplace it's all about value exchange. And if I'm able to do value exchange really well, then people will come back and they do and they engage."

**洞察：** AI 在市场中的核心战略价值在于其促进高质量撮合和价值交换的能力。

**战术建议：**
- 将 AI 目标重点放在下游价值（例如有意义的对话）上，而不仅仅是顶级点击。

*时间戳：00:31:21*

---

> "We call it the full stack builder model. The goal itself is to empower great builders to take their idea and to take it to market, regardless of their role and the stack and which team they're on. It's really fluid interaction between human and machine."

**洞察：** 全栈构建器 model 旨在通过使用 AI 使个人拥有从创意到发布的整个产品生命周期，从而降低组织复杂性。

**战术建议：**
- 使构建者能够跨越传统的功能边界进行工作
- 将人类的努力集中在愿景、同理心、沟通、创造力和判断力上
- 自动执行重复的流程步骤以提高迭代速度

*时间戳：00:12:03*

---

> "The platform for us as an example is rearchitecting all of our core platforms so AI can reason over it. So we're building kind of this composable UI components with server side that we actually build. We're basically building for AI to be ready to bring it in."

**洞察：** 成功的 AI 集成需要重新架构技术平台和设计系统，以便 AI agents 能够有效地推理和操作代码库。

**战术建议：**
- 重新架构核心平台以提高 AI 的可读性
- 构建 AI 可以组装的可组合 UI 组件
- 自定义第三方 AI 工具以与internal proprietary stack配合使用

*时间戳：00:17:17*


## Varun Mohan
*Varun Mohan*

> "We should be cannibalizing the existing state of our product every six to 12 months. Every six to 12 months, it should make our existing product look silly. It should almost make the form factor of existing product look dumb."

**洞察：** 在快速发展的 AI 市场中，公司必须愿意颠覆自己的成功产品才能保持领先地位。

**战术建议：**
- 每 6-12 个月计划一次主要产品范式转变
- 投资长期研发可能会使当前功能过时

*时间戳：00:00:00*

---

> "Where is the layer that you can actually differentiate on? And we believe the application layer is a very, very deep layer to go out and differentiate on. What are the number of ways we can build better user experiences and better workflows for developers? We think there's effectively no ceiling on that."

**洞察：** AI 的价值正在从基础设施转移到构建独特的用户体验和工作流程的应用程序层。

**战术建议：**
- 专注于垂直集成和自定义 UI/UX 而不仅仅是 model 包装器
- 确定可以使用 AI 从根本上重新构想的特定用户工作流程

*时间戳：00:10:00*

---

> "If AI is writing over 90% of the code... the ROI of building technology has actually gone up. This actually means you hire more. The best thing to do is just get your hands dirty with all of these products. You could be a force multiplier to your organization in ways in which they never even anticipated."

**洞察：** AI 增加了工程的 ROI，鼓励'technology ceilings'高的公司在人才方面进行更多投资。

**战术建议：**
- 使用 AI 增加组织可生产的技术的数量和复杂性
- 鼓励非技术角色使用 AI 工具构建自定义内部解决方案

*时间戳：00:00:29*


## Brendan Foody
*Brendan Foody*

> "If the model is the product, then the eval is the product requirement document. And the way that researchers' day-to-day looks is that they'll run dozens of experiments where they'll make small improvements on an eval set."

**洞察：** 评估是 AI models 的基本产品要求，也是衡量进展和成功的主要基准。

**战术建议：**
- 对于 AI 产品，将 evals 视为 PRD
- 运行迭代实验，对 eval 集进行小的、可测量的改进

*时间戳：00:06:39*

---

> "I think that for enterprises especially, the core way to think about it is how can they build a test or systematic way to measure how well AI automates their core value chain?"

**洞察：** 有效应用 AI 的先决条件是定义一种系统方法来衡量其对公司特定价值链的自动化程度。

**战术建议：**
- 确定企业的核心价值链
- 构建系统测试来衡量 AI 在自动化特定链方面的性能

*时间戳：00:07:39*


## Andrew Wilkinson
*Andrew Wilkinson*

> "I think the fundamental question is, do all jobs just become a single prompt? For example, does a CEO just grow the business while making the customers happy and turning a profit... and it is able to actually be an omniscient presence that can run a whole company."

**洞察：** AI 的长期发展轨迹表明，将转向 'omniscient' agents，后者可以管理整个业务功能，有可能取代传统的知识工作。

**战术建议：**
- 为未来做好准备，到 2027 年 AI models 可能会变成 'smarter than all PhDs'。
- 随着 AI 降低劳动力成本，专注于积累财富并实现计算和能源多元化。
- 在 AI 丰富的世界中识别 'human-only' 的附加价值，例如幽默、地位和身体联系。

*时间戳：00:58:43*


## Garrett Lord
*Garrett Lord*

> "The models have gotten so good that the generalists are no longer needed. What they really need is experts, experts across every area that the models are focused on."

**洞察：** AI 策略正在从通才数据标记转向专家主导的后训练，以改进 model 在专业领域的推理。

**战术建议：**
- 专注于先进的 STEM 领域和法律、医学等衍生专业功能，以实现 model 的改进
- 目标专家（博士、硕士）可以识别 models 在推理或基本事实中的缺陷

*时间戳：00:10:52*

---

> "We like to say the only moat in human data is access to an audience. Basically, there are many, many small players in this space... they're basically running TikTok ads... The huge advantage that we've had... is we built a decade of trust with 18 million people."

**洞察：** AI 数据产品的可持续护城河是对值得信赖的、高意向受众的proprietary access，而不是依赖绩效营销。

**战术建议：**
- 利用现有的品牌亲和力来降低数据贡献者的客户获取成本
- 使用用户表现的历史数据为特定的标签任务找到合适的专家

*时间戳：00:30:50*


## Paige Costello
*Paige Costello*

> "When it came to the massive leap forward in LLMs recently, we staffed a team to really prototype quickly, and discover what was possible, and just apply hypotheses outside of the typical norms of how we work. So they went straight to prototyping instead of going through that Double Diamond I was explaining earlier."

**洞察：** 对于像 LLMs 这样快速发展的技术，可以绕过标准的繁重流程，转而采用快速原型设计，以快速发现技术可能性。

**战术建议：**
- 组建专门的团队，在正常产品周期之外对 AI 假设进行原型设计。
- 在处理高不确定性技术时，跳过正式的发现阶段，有利于立即进行原型设计。

*时间戳：00:40:08*


## Peter Deng
*Peter Deng*

> "A lot of the value is still going to require a bunch of hustle from a lot of builders to really turn that new source of energy and channel it into something that we humans want to use that solves some of our problems."

**洞察：** 仅有 AGI 是不够的；产品制造商必须将 'harness' 和 AI 的能量引导到特定的以人为本的解决方案中。

**战术建议：**
- 专注于将原始 AI 智能转化为有用产品所需的 'elbow grease'
- 识别 AI 比现有工具更符合人体工程学的特定人类问题

*时间戳：00:08:15*

---

> "The data flywheel thing is really interesting because the models will get really good at whatever data you show it... being very mindful of the data that you have access to to start your flywheel going and what you can do to keep on going with that flywheel is going to be a critical thing."

**洞察：** AI 的防御能力来自proprietary数据flywheel和深度集成的工作流程。

**战术建议：**
- 确定proprietary data sources以启动初始 model 训练 flywheel
- 构建通过用户交互自然生成更多高质量数据的工作流程

*时间戳：00:29:36*

---

> "I think that close, tight-knit relationship at any of these large model companies between post training and product is going to produce some really incredible stuff."

**洞察：** AI PMs 的最大优势是直接与研究和培训后团队合作来微调 model 行为。

**战术建议：**
- 将 PMs 嵌入研究团队以影响 model 'vibe' 和功能
- 专注于微调和后期训练，而不仅仅是 UI 层

*时间戳：00:35:15*


## Scott Belsky
*Scott Belsky*

> "I think that the greatest performers I've ever worked with... preserve the time to explore lots of possibilities... generative AI and AI for all, when it talks to me about just product leaders exploring possibilities, this should expand the surface area."

**洞察：** Generative AI 为产品领导者提供了超能力，使他们能够在更短的时间内探索更大的可能性和场景。

**战术建议：**
- 使用 AI 生成多个 'what if' 场景，以扩展你的思维，超越最初的解决方案
- 将 AI 视为 'intern' 以创建初始草稿或缩略图，然后进行优化
- 定期使用新兴的 AI 工具，了解它们如何增强你的特定创意流程

*时间戳：00:33:05*


## Scott Wu
*Scott Wu*

> "I think the big shift that we really felt we would see is moving from kind of this text to text model to an actual autonomous system that can make decisions, that can interact with the real world, that can take in feedback, that can iterate and take multiple steps to solve problems. And now we call that agents, but that was what we were really excited about at the time."

**洞察：** AI product strategy的核心转变是从简单的文本完成转向能够进行多步推理和现实世界交互的自主 agents。

**战术建议：**
- 专注于构建自主系统而不仅仅是文本到文本完成工具
- 设计可以接受反馈并迭代自己工作的系统

*时间戳：00:13:34*

---

> "I think the product experience itself is going to change every single time. And then obviously there, there's all of the practicality of just getting it out there in the world. And so folks obviously need to learn how to use the new technology. There's a lot to do to deploy into all of the messiness of real world software."

**洞察：** AI product strategy必须考虑到随着 model 功能的改进而不断变化的用户体验以及处理混乱的现实世界边缘情况的需要。

**战术建议：**
- 预计产品界面将需要随着每一代新一代 model 功能的变化而改变
- 优先考虑处理现实世界的复杂性和 'messiness' 而非理论性能

*时间戳：00:56:04*


## Timothy Davis
*Timothy Davis*

> "You guys have been using AI for years now. Smart Bidding is AI. All of the recommendations within Google Ads is AI. Ad copy recommendations is AI, and that's always been in the platform."

**洞察：** 认识到效果营销中的 AI 通常已经嵌入到平台原生自动化中，例如智能出价和算法推荐。

**战术建议：**
- 利用平台原生的 AI 进行竞价和广告文案迭代，而不是寻找外部工具来完成基本任务

*时间戳：01:30:59*


## Tamar Yehoshua
*Tamar Yehoshua*

> "In five to 10 years, I think the lines between product managers and engineers and designers are going to blur because AI will enable product managers to build prototypes, to build designs... I'm of the believer that we're just going to have a lot more software."

**洞察：** AI 将使执行和grunt work商品化，从而导致功能角色的模糊和软件输出的大幅增加。

*时间戳：00:50:21*

---

> "The industry is transforming so rapidly that you need to make sure that your product gets better as the LLMs get better. And that too many people are building things to make up and compensate for the LLMs that all that work is going to go away. So it's okay to do it to understand that it's going to go away, but that can't be your differentiator."

**洞察：** 避免围绕解决当前 LLM 限制构建核心价值主张，因为这些差距可能会由 model 提供商弥补。

**战术建议：**
- 确保你的产品的独特价值在于 base LLM capability 之外的能力（例如proprietary data access 或 specific workflows）。

*时间戳：01:03:45*


## Casey Winters
*Casey Winters_*

> "If you thought the PM job was just filling in frameworks, you're going to get replaced by AI."

**洞察：** 机械地遵循框架的 PMs 将被替换；那些拥有专业知识的人将会蓬勃发展。

**战术建议：**
- 建立subject-matter expertise
- 使用 AI 进行grunt work

*时间戳：00:24:41*


## David Singleton
*David Singleton*

> "We can have GPT-4 read all our docs and answer questions for developers."

**洞察：** 应用 LLMs 使复杂的产品可以通过natural language访问。

**战术建议：**
- 使用documentation embeddings
- 将natural language翻译为technical queries

*时间戳：01:03:44*


## Jag Duggal
*Jag Duggal*

> "Companies need to figure out what AI native means, not how to append AI at the corners."

**洞察：** AI-native 需要以 AI 为核心，from first principles重新构想产品。

**战术建议：**
- 询问：如果 AI 从一开始就存在，你会如何设计？
- 以 AI 为核心

*时间戳：01:11:12*


## Krithika Shankarraman
*Krithika Shankarraman*

> "Taste is going to become a distinguishing factor in the age of AI."

**洞察：** 在 AI 时代，品味和craft成为关键的差异化因素。

**战术建议：**
- 投资培养 taste
- 使用 AI 增强而不是取代判断

*时间戳：00:55:31*


## Sam Schillace
*Sam Schillace*

> "AI isn't a feature of your product. Your product is a feature of AI."

**洞察：** 变革性的 AI 产品将 AI 视为platform foundation，而不是bolt-on feature。

**战术建议：**
- 构建需要 AI 的产品
- 将 AI 视为enabler of new categories

*时间戳：01:03:01*


