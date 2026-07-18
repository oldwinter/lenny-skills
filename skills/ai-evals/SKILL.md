---
name: ai-evals
description: 帮助用户构建强大的基础设施，使用人工、基于代码和法学硕士作为法官的方法来测量、监控和迭代AI产品性能。
---

# AI评估策略

超越氛围检查，转向对 AI 产品质量和可靠性进行系统、实证的测量。

利用 11 位嘉宾的见解以及 Lenny 的播客和时事通讯中的帖子，帮助用户制定AI评估策略。

## 如何提供帮助

1. **识别故障模式** - 帮助用户对真实痕迹进行错误分析，找出系统具体故障的位置。
2. **选择评估方法** - 根据具体的技术用例推荐人员、代码和 LLM 法官的正确组合。
3. **构建黄金集** - 协助整理高质量示例的参考数据集，作为您的应用程序的基本事实。
4. **可操作性** - 指导用户将这些评估集成到 CI/CD 管道中，以实现持续的质量改进。

## 核心原则

### 价值链自动化
Brendan Foody: "I think that for enterprises especially, the core way to think about it is how can they build a test or systematic way to measure how well AI automates their core value chain? So if it's an architecture firm that's producing these architecture diagrams of what they provide to their end customer, how can they effectively measure that? And each company has its own value chain or maybe a handful of them if it's a multi-product company."

确定您的业务独有的核心可交付成果，并开发系统测试来衡量AI复制这些特定任务的准确程度。

### 优先考虑主观卓越
Edwin Chen: "We are looking for a Nobel Prize-winning poetry. Is this poetry unique? Is it full of subtle imagery? Does it surprise you and target your heart? Does it teach you something about the nature of moonlight?"

真正的数据质量是由深刻的、主观的人类卓越性定义的，例如情感共鸣和独特性，而不是肤浅的二进制检查。

### 消除振动检查
Hamel Husain & Shreya Shankar: "Evals help you create metrics that you can use to measure how your application is doing and kind of give you a way to improve your application with confidence. That you have a feedback signal in which to iterate against."

创建系统指标来跟踪应用程序质量随时间的变化，使团队能够像传统软件一样自信地迭代提示或模型。

### 结构化判断逻辑
From "Beyond vibe checks: A PM’s complete guide to evals": "Clearly articulating what you want your judge-LLM to measure isn’t just a step in the process; it’s the difference between a mediocre AI and one that consistently delights users. Building these writing skills requires practice and attention."

使用结构化提示编写有效的自动评估，该提示定义了法官的角色、数据、成功标准和特定标签。

## 模板和框架

- **LLM-as-a-Judge Playbook**（构建可改进 AI 产品的评估系统）- 用于构建、验证和衡量 LLM 法官的系统性三步流程，为主观 AI 质量提供可信的二进制通过/失败指标：
- **三种评估方法（人工、基于代码、基于法学硕士）**（超越氛围检查：PM 的完整评估指南）- 一个决策框架，用于根据您的用例选择正确的评估方法，每种方法都有优缺点。
- **评估公式（四部分结构）**（超越氛围检查：PM 的完整评估指南）- 一个由四部分组成的公式，用于编写有效的基于 LLM 的评估提示，任何 PM 都可以使用它来构建判断 LLM 提示。
- **用于AI错误分析的开放编码和轴向编码**（构建改进AI产品的评估系统） - 一种适用于AI产品评估的定性研究方法，用于从用户交互数据中发现故障模式并对其进行分类。
- **RAG 评估框架（检索器 + 生成器）**（构建改进 AI 产品的评估系统）- RAG 系统的两部分评估方法，分别评估检索器和生成器组件，并为每个组件提供特定指标。
- **AI Eval Improvement Flywheel**（构建可改进 AI 产品的评估系统）- 闭环流程，同时使用 CI 安全网和生产发现引擎来创建持续的 AI 产品改进。
- **参考数据集结构**（为什么您的AI产品需要不同的开发生命周期） - 用于构建初始参考数据集（20-100个示例）的模板，以打破冷启动并为AI系统评估提供基线。
- **代理工作流程的转换失败矩阵**（构建改进 AI 产品的评估系统）- 一种诊断工具，用于准确定位代理的多步骤工作流程中的哪一步发生故障，从而实现数据驱动的调试。

有关详细信息的完整列表，请参阅 `references/artifacts.md`。

## 帮助用户的问题

- “您的用户目前在生产中遇到的前 3 到 5 种故障模式是什么？”
- “您是否有一个领域专家或仁慈的独裁者来定义此功能的质量？”
- “您当前的评估过程中手动与自动的比例是多少？”
- “您的系统非确定性主要发生在检索阶段还是生成阶段？”
- “您是否已经建立了至少包含 20 到 50 个人类标记示例的黄金数据集？”
- “目前，当您切换模型或更改系统提示时，您如何衡量性能增量？”

## 标记的常见错误

- **依靠氛围检查** - 手动和轶事测试会导致质量不一致和隐藏的回归，随着时间的推移会损害用户的信任。
- **痴迷于即时工程** - 仅关注提示而忽略底层评估系统会阻止团队系统地扩展或爬山。
- **使用通用指标进行产品报告** - 现成的分数对于过滤很有用，但通常无法捕获业务逻辑特有的特定值或故障。
- **忽略组件隔离** - 在 RAG 系统中，无法将检索器与生成器分开进行评估，因此无法知道堆栈的哪一部分发生了故障。
- **忽视非确定性** - 未能考虑法学硕士的随机性会导致对结果的错误信心，而这些结果可能不会在生产中重复。

## 深入探讨

有关 11 位嘉宾的全部 33 条见解，请参阅 `references/guest-insights.md`

## 相关skill

- AI产品策略
- AI 原生用户体验
