---
name: building-with-ai-agents
description: 通过关注高层指导、并行任务分配和严格的自动化审查，帮助用户掌握从手动编码到管理AI驱动的开发工作流程的过渡。
---

# 使用 AI 代理进行构建

从编写代码行过渡到指导并行的自主代理团队。

利用 15 位嘉宾的见解以及 Lenny 的播客和时事通讯中的帖子，帮助用户使用AI代理进行构建。

## 如何提供帮助

1. **识别任务** - 使用初级实习生框架来查找适合委派的重复性或明确定义的工程任务。
2. **定义说明** - 起草精确、精细的提示，并通过 Markdown 文件和过去的示例提供上下文。
3. **管理并行线程** - 跨不同的拉取请求或功能同时指导多个代理以扩展输出。
4. **审查和迭代** - 通过审查代码逻辑并使用AI主导的同行审查来维持监督，以确保部署前的质量。

## 核心原则

### 方向的转变
Boris Cherny: "100% of my code is written by Claude Code. I have not edited a single line by hand since November. Every day, I ship 10, 20, 30 pull requests. So, at the moment I have, like, five agents running."

停止手动代码编辑，转而指导多个 AI 代理同时处理不同的拉取请求，以最大限度地提高生产力。

### 绝对特异性
Lazar Jovanovic: "AI just don't understand what do you mean when you say, 'You know what I mean?' So you need to be specific. I'm optimizing 100% of my time today on good judgment, clarity, quality, taste."

放弃该工具理解您的隐含意图并提供精细说明的假设，就像您正在与技术联合创始人交谈一样。

### 高级推理和编排
Marc Andreessen: "Over the holiday break, it feels like the AI coding thing really hit critical mass and the world's best programmers, including Linus Torvalds, for the first time over the holiday break basically said, 'Yeah, AI is now coding better than we can.'"

将您的角色从手动执行转变为推理和编排，使用 AI 实现标准程序员 10 倍的输出。

### 异步协调
Scott Wu: "Our whole team is only like 15 engineers a year. We use a ton of Devin when we're building Devin. Most folks on the team are definitely working with up to five Devins at once, and so Devin merges like several hundred pull requests into production in the Devin code bases every month."

通过一次将不同的任务分配给多个代理实例，从同步单任务转移到协调并行团队。

### 消除手动逃生舱口
Sherwin Wu V2: "There's a team that's actually doing an experiment right now within OpenAI where they are maintaining a 100% Codex-written code base. They run into the exact problems that you're describing. And so usually you're like, 'All right, I'll roll up my sleeves and figure it out.' This team doesn't have that escape hatch."

当代理陷入困境时，抵制手动修复代码的冲动；相反，致力于掌握仅通过AI解决问题所需的模型控制。

### 多模型同行评审
Zevi Arnovitz: "It's very difficult for me to catch mistakes. What I'll do is basically /review. This tells Claude to start reviewing its own code, but what's even cooler is I have Codex as well as Cursor open. I will have each of them review the code."

通过强制不同的AI模型在部署前相互交叉检查逻辑错误来弥补技术知识差距。

## 模板和框架

- **AI Agent Builder 元提示**（通过 AI 代理让产品管理再次变得有趣）- 粘贴到具有深度研究功能（o3 Deep Research 或 Perplexity Deep Research）的 LLM 中的综合提示，可生成特定于平台的 ste
- **Devin（自主 AI 工程师）的 10 个用例**（Devin 免费一年：世界上最先进的自主 AI 软件工程师）- 团队使用 Devin 的 10 种具体方式的列表，从简单的工程任务进展到更广泛的产品和分析工作。
- **任务委派初级实习生测试**（通过 AI 代理让产品管理再次变得有趣） - 用于确定将哪些任务委派给 AI 代理的心理模型：问问自己，您会分配给一个聪明、积极、零经验的初级实习生。
- **/同行评审命令** (Zevi Arnovitz) - 将 Claude 框定为开发负责人的提示，接收来自其他团队负责人（其他 AI 模型）的代码评审反馈，指示其捍卫其决定
- **AI 项目规划 PRD（Markdown 文件）** (Lazar Jovanovic) - 一套 Markdown 文档，用于为 AI 编码代理提供持久的动态上下文，以便他们不会丢失项目范围。
- **4x4 调试框架** (Lazar Jovanovic) - 一个四步顺序过程，用于在不知道如何编码的情况下修复损坏的 AI 生成的代码。
- **/探索阶段命令** (Zevi Arnovitz) - 告诉 Claude 在编写任何代码之前深入探索问题的提示 - 从 Linear 获取上下文，分析代码库，并询问澄清问题
- **/create plan command** (Zevi Arnovitz) - 从探索交换中生成结构化 Markdown 计划文件的提示，其中包含每个任务的状态跟踪器、TLDR、关键决策和任务布雷

有关详细信息的完整列表，请参阅 `references/artifacts.md`。

## 帮助用户的问题

- “目前哪些重复性工程任务最拖慢您团队的速度？”
- “您是否有现有文档或Markdown 文件可以向新加入者解释您的代码库结构？”
- “您是否能够忍住手动修复错误而不是重新提示代理的冲动？”
- “您希望这些代理与 Slack 或 Linear 等哪些通信工具集成？”
- “您是否对成功有明确的定义，或者有一个完美的拉取请求模板供代理遵循？”

## 标记的常见错误

- **Vibe Coding** - 在不彻底了解实现细节的情况下生成代码会导致系统无法维护。
- **含糊提示** - 假设AI知道你的意思而不提供细粒度的、具体的技术限制会导致输出不一致。
- **手动干预** - 当AI脱轨时恢复到手动编码会阻止您学习如何有效地引导模型以实现长期规模。
- **同步管理** - 将代理视为聊天工具而不是异步团队成员会阻止您实现并行开发的收益。

## 深入探讨

有关 15 位嘉宾的所有 31 条见解，请参阅 `references/guest-insights.md`

## 相关skill

- 写产品
- 交付速度
- AI辅助原型设计
- 产品工具栈
