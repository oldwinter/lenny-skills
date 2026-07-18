---
name: ai-native-ux
description: 通过设计管理流动性、意图和代理的界面，同时保持信任和控制，帮助用户与概率模型交互。
---

# 设计AI原生用户体验

从静态界面过渡到利用模型智能的流畅、意图驱动的交互。

利用 14 位嘉宾的见解以及 Lenny 的播客和时事通讯中的帖子，帮助用户设计AI原生用户体验。

## 如何提供帮助

1. **映射机构控制平衡** - 帮助用户决定哪些任务应该由AI自动化，哪些任务需要人工监督。
2. **非确定性设计** - 帮助创建 UI 模式，以适应不同的模型输出并提供简单的纠正机制。
3. **结构会话语法** - 指导用户定义隐形规则和结构化元素，使自然语言界面可预测。
4. **迭代反馈循环** - 帮助实现简单、高频的反馈机制，以根据用户交互优化模型性能。

## 核心原则

### 流畅设计
Aishwarya Naresh Reganti + Kiriti Badam: "Most people tend to ignore the non-determinism. You don't know how the user might behave with your product, and you also don't know how the LLM might respond to that. The second difference is the agency control trade-off."

从固定按钮和表单转向通过自然语言表达用户意图的界面。这需要在语言的灵活性和传统 UI 的精确度之间进行权衡。

### 定义清晰的决策边界
Adriel Frederick: "And I was like yeah, the reason that falls down is the algorithms don't understand long term effects often, nor do they understand how people might respond to it, nor do they understand your intent for the product, and I think it's really important for product managers to play that role. That is our job. When you are working on algorithmic heavy products, your job is figuring out what the algorithm should be responsible for, what people are responsible for, and the framework for making decisions."

明确确定哪些决策属于算法以及哪些决策需要人工干预。该框架弥合了机器优化和人类意图之间的差距。

### 构建语言的结构化语法
Aparna Chennapragada: "Natural language interface. NLX is the new UX. Often I hear a product builders say, 'Oh, yeah. With AI, the model eats the products.' That doesn't mean it's not designed."

自然语言体验不应完全留给模型。设计人员必须定义会议或播客等特定环境中固有的不可见 UI 结构和语法。

### 轻松实施纠正
Gustav Söderström: "And the AI DJ is you press a button, a digitized person, there's a real person named X, digitized X. So he's now an AI, comes on and talks to you about music that you like and suggests music, and you can listen to it. And if you don't like it, you can just call him back and he says, 'Okay, now, let's listen to something maybe from a few summers ago,' or 'Here's some new stuff that were trending yesterday in The Last of Us episode or something like that.'"

由于AI输出本质上是可变的，因此优先考虑简单的反馈循环。使用数字化角色或“寻求帮助”按钮，让用户感觉更自然地纠正AI错误。

### 优化指令遵循
Kevin Weil: "It's very good at instruction following. That's actually something that I think people... I'm starting to see people discover with it, but you can do very complex things. You can give it two images, one is your living room and the other is a whole bunch of photos or memorabilia or things you want and you say, 'Tell me how you would arrange these things.'"

将交互模式从简单命令转变为复杂的多步骤指令。设计用户体验以利用模型跨多模式输入的推理能力。

### 通过机构控制阶梯进行扩展
From "Why your AI product needs a different development lifecycle": "Start by identifying a set of features that are high control and low agency (version 1 in the image above). These should be small, testable, and easy to observe. From there, think about how those capabilities can evolve over time by gradually increasing agency, one version at a time."

仅在低风险环境中验证性能后才增加AI自主权。从高控制功能开始，将崇高的代理目标分解为小的、可测试的行为。

### 保留用户流程状态
Ryan J. Salva: "When you are in the editor, it could be VS Code, it could be IntelliJ, it could be them, essentially, as you are typing, Copilot will provide suggestions usually in kind of this italicized gray text that is really, to your point, kind of magical what it's able to infer."

使用斜体灰色文本等非破坏性提示将AI建议直接集成到现有工具中。这确保AI在不破坏用户创作动力的情况下为用户提供帮助。

## 模板和框架

- **NLX（自然语言体验）设计元素** (Aparna Chennapragada) - 一组必须在对话式 AI 界面中显式设计的隐形 UI 构造。
- **AI使像素自由** (Sam Schillace) - 正如互联网使信息分发自由一样，AI将使像素生产自由 - 将整个软件行业从静态应用程序转变为动态应用程序
- **容错用户界面** (Gustav Söderström) - AI 产品的设计原则，其中 UI 的构建是为了适应底层机器学习模型的错误率。
- **Canva Magic Media UX Evolution**（构建 AI 产品的反直觉建议）- Canva 如何迭代其文本到图像的 AI 功能，以减少空提示框的恐吓并引导用户获得更好的结果
- **AI 代理的低负面设计模式**（通过 AI 代理让产品管理再次变得有趣）- 四种模式可限制 AI 代理错误的风险，同时保留优势，适用于任何代理设计。
- **AI 建议的 200 毫秒延迟最佳点** (Ryan J. Salva) - 内联 AI 代码建议的最佳响应时间，以维持开发人员流程状态
- **AI Pair Programmer Framing** (Ryan J. Salva) - 用于指导 AI 编码工具的道德和用户体验决策的产品角色/隐喻

有关详细信息的完整列表，请参阅 `references/artifacts.md`。

## 帮助用户的问题

- “在此工作流程中，人类控制和AI机构之间的当前细分是什么？”
- “界面如何处理模型提供不正确或低置信度响应的情况？”
- “我们是否提供了足够的视觉提示来帮助用户跳过空白提示框？”
- “要使这次对话感觉结构化且有用，需要哪些隐形 UI 语法？”
- “AI响应的延迟是否足够快以维持用户的心流状态？”
- “我们如何区分用户创作的内容和AI生成的建议？”

## 标记的常见错误

- **空提示陷阱** - 期望用户准确地知道要输入什么而不提供视觉起点或引导选项会导致用户瘫痪。
- **过度构建刚性 UI** - 对模型功能的特定 UI 元素进行硬编码会使产品脆弱且无法跟上 AI 快速改进的步伐。
- **黑匣子自治** - 在没有早期人机交互控制的情况下增加AI机构，使得调试变得不可能，并且在发生错误时会破坏用户的信任。
- **忽略非确定性** - 当模型不可避免地产生不同的结果时，将AI视为固定决策引擎会导致用户体验破裂。

## 深入探讨

有关 14 位来宾的全部 14 条见解，请参阅 `references/guest-insights.md`

## 相关skill

- AI产品策略
- AI 评估
