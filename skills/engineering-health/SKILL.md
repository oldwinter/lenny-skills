---
name: engineering-health
description: 通过 Core 4 等框架衡量健康状况、将技术债务作为杠杆进行管理以及使用 AI 工具优化工作流程，帮助用户建立可持续的工程文化。
---

# 工程健康和生产力

通过平衡技术卓越与战略开发人员投资来保持高交付速度。

利用 18 位嘉宾的见解以及 Lenny 的播客和时事通讯中的帖子，帮助用户改善工程健康并提高工作效率。

## 如何提供帮助

1. **基线健康状况** - 使用 Core 4 或 DORA 框架为团队绩效建立定量和定性起点。
2. **优化工作流程** - 识别从代码完成到生产部署的路径中的瓶颈，以释放隐藏的速度。
3. **管理技术债务** - 将技术投资视为业务投资回报率，以确保非功能工作的支持。
4. **利用AI工具** - 将AI集成到开发生命周期中，将工程师的注意力从语法转移到架构。

## 核心原则

### 通过价值与数量来评估AI
Chip Huyen: "It's really hard to measure productivity. So, I do ask people to ask their managers, "Would you rather give everyone on the team very expensive coding agent subscriptions or you get an extra head count?" Almost every one, the managers will say head count."

将AI工具的成本和产出与额外员工的价值进行比较，而不是仅仅关注原始生产力的提高。

### 将焦点转向建筑
Inbal S: "The user of the AI tools to develop software needs to form a different thinking. You need to start figuring out how are you using these AI tools to help you be successful. And it's no longer just the actual code writing, it's really evolving your thinking to the big picture, to the connected experience, to connected systems."

使用AI处理手动语法，以便工程师可以将更多时间花在高级系统设计和产品理解上。

### 实现AI内部工具的现代化
Mike Krieger: "We really rapidly became bottlenecked on other things like our merge queue. We had to completely re-architect it because so much more code was being written and so many more pull requests were being submitted. Over half of our pull requests are Claude Code generated."

必须重新架构合并队列等内部工具，以处理AI编码生成的拉取请求量的大幅增加。

### 衡量多维生产力
Nicole Forsgren: "So productivity, I think, is basically how much we can get done and how much we can do over time. And I think that's why it's so important to have this holistic measure because we can't just brute force it, right. And so that's why when my team and a bunch of my peers study productivity, we include this community effect because software is a team sport."

避免原始输出指标：相反，使用平衡的视图，包括团队动态、可持续性和工作流程摩擦。

### 自动化质量门
Sherwin Wu V2: "100% of our PRs are reviewed by Codex daily as well. So basically any code that goes into production that's merged in, Codex kind of has its eyes on and suggests improvements, suggests changes in the PRs."

随着代码量的增加，实施AI驱动的自动审查以保持质量，而不会造成手动瓶颈。

### 基准AI进展
Dhanji R. Prasanna: "We find engineering teams that are very, very AI forward are reporting about eight to 10 hours save per week. Whenever I hear a stat like this, I think an important element is this is the worst it will ever be. This is now the baseline."

跟踪AI前沿团队每周节省的时间，以建立一个性能基准，该基准将随着技术的成熟而发展。

### 激励代码删除
Farhan Thawar: "We have a Delete Code Club. We can always almost find a million-plus lines of code to delete, which is insane."

积极删除过时的代码，以防止系统复杂性减慢开发速度。

### 将技术债务视为杠杆
Gaurav Misra: "I actually think as a startup your job is to take on technical debt because that is how you operate faster than a bigger company. Bigger companies don't take contact technical debt, they pay it usually right away, or they're paying back technical debt from the days when they were a startup."

当技术债务为新的市场价值的交付速度提供显着优势时，故意选择承担技术债务。

### 优化最后一英里
From "Increasing team velocity": "Talk to your engineers about opportunities to speed up their review, approval, and deployment process."

专注于代码完成和部署之间的技术工作流程，以实现交付速度的最显着提升。

## 模板和框架

- **Core 4 框架**（Core 4 简介：衡量和提高产品速度的最佳方式）- 一个统一的开发人员生产力框架，具有四个维度，旨在相互保持紧张关系，提供团队绩效的平衡视图。共同作者
- **DORA 指标（四个关键）** (Nicole Forsgren) - 衡量软件交付性能的四个指标，分为速度和稳定性。
- **工程效率投资的 ROI 框架**（引入核心 4：衡量和提高产品速度的最佳方法）- 两个互补的框架，用于向领导层展示开发人员体验改进的业务案例。
- **Core 4 基线调查模板**（Core 4 简介：测量和提高产品速度的最佳方式）- 即插即用的调查模板，可发送给工程团队以收集所有四个 Core 4 维度的基线测量结果。回复必须是匿名的。
- **Unsexy Investment Justification Playbook** (Casey Winters) - 获得技术债务、性能和用户体验改进支持的策略。
- **抛光季节（年度质量仪式）**（Linear 如何构建产品）- 一年一度的年终仪式，Linear 会集中时间修复用户提交的错误、剪纸和质量问题。
- **SPACE Framework** (Nicole Forsgren) - 一个用于跨五个维度衡量复杂创意工作的框架，以确保指标的平衡。
- **哭泣的章鱼按钮（剪纸）** (David Singleton) - 嵌入开发人员环境中的内部工具，用于立即报告摩擦。
- **季度油脂周**（Duolingo 如何构建产品）- 专门的季度周，产品团队专门致力于清除错误和技术债务
- **技术债务跑道** (Gaurav Misra) - 一种将技术债务视为财务杠杆的心理模型，使用“利率”来确定债务何时对初创公司造成致命影响。

有关详细信息的完整列表，请参阅 `references/artifacts.md`。

## 帮助用户的问题

- “目前您的工程能力中有多少百分比用于维护与新功能？”
- “一段代码从完成到部署到生产中通常需要多长时间？”
- “您是否对开发人员进行了调查，以确定他们日常工作流程中最大的摩擦点？”
- “对于如何决定偿还技术债务与构建新功能，您是否有一个明确的框架？”
- “您目前如何衡量AI工具在您的工程组织中的影响和采用情况？”
- “目前影响您产品质量的三个最大的剪纸或用户体验烦恼是什么？”

## 标记的常见错误

- **衡量原始输出与影响** - 关注代码行数或 PR 数量会忽略代码质量，并可能导致倦怠和系统脆弱性。
- **将所有债务视为负面因素** - 避免所有技术债务可能会阻止初创公司快速发展以找到适合市场的产品。
- **仅依靠自动化指标** - 定量数据可以识别问题的存在，但需要定性开发人员反馈来诊断特定的摩擦点。
- **将测试作为安全网进行投资** - 如果没有强大的单元测试，工程师就会失去重构代码或快速行动而不破坏事物的信心。

## 深入探讨

有关 18 位嘉宾的全部 21 条见解，请参阅 `references/guest-insights.md`

## 相关skill

- 写产品
- 交付速度
- AI辅助原型设计
- 与AI代理一起构建
