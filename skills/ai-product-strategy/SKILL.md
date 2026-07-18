---
name: ai-product-strategy
description: 帮助用户决定在何处有效应用AI，管理从确定性软件到概率性软件的过渡，并通过垂直化和专有数据建立长期防御能力。
---

# AI产品策略

优先考虑高影响力的工作流程并引导非确定性开发，以构建防御性的 AI 产品。

利用 26 位嘉宾的见解以及 Lenny 的播客和时事通讯中的帖子，帮助用户制定AI产品策略。

## 如何提供帮助

1. **定义楔子** - 识别AI可以为用户提供不成比例回报的高摩擦杂务。
2. **选择架构** - 根据实时数据与特定行为的需求，在检索增强生成 (RAG) 和微调之间进行选择。
3. **安全地扩展自主权** - 设计一种分级的自主方法，让人类在转向完全自动化之前保持在循环中。
4. **针对曲线构建** - 将产品路线图与未来模型功能相结合，而不是针对当今的限制构建复杂的脚手架。

## 核心原则

### 考虑到不完美输出
Alex Komoroske: "LLMs allow writing shitty software to be significantly cheaper, not necessarily good software, but good enough in certain contexts. And also it means that there's certain software now that isn't plain old computing that can be run cheaply. It's relatively expensive marginal cost."

设计产品体验时假设 AI 是不确定且不完美的，而不是试图强制 UI 具有 100% 的准确性。

### 将产品视为生命体
Asha Sharma: "Because these models are so effective at this point, you want to start to tune them to certain types of outcomes. All of a sudden, these are these living organisms that just get better with the more interactions that happen. I think this is the new IP of every single company products that think and live and learn."

通过团队在获取数据和改进学习循环方面的新陈代谢而不是静态功能发布来衡量成功。

### 寻找垂直化的防御力
Logan Kilpatrick: "We're not going to launch some of these varied verticalized products. We're not going to launch an AI sales agent. That's just not what we're building towards. And companies who are and have some domain specific knowledge and they're really excited about that problem space, they can go into that and leverage our models and end up continuing to be on the cutting edge without having to do all that R&D effort themselves."

通过针对领域专业知识提供结构性优势的特定行业利基，避免与基础模型竞争。

### 孵化特定超能力
Noah Weiss: "I think in the AI space, we're trying to hear from customers, what do you wish Slack could do if it had these new superpowers? Let's incubate a couple teams or prototype, give them space to run and pilot and then get something to launch that's amazing. Blows people away. That's the formula that we've seen."

通过识别特定的客户需求并为专门的团队提供独立的原型设计空间，避免通用AI功能。

### 为模型的未来而打造
Sherwin Wu V2: "The field and the models themselves are just changing so, so quickly. They tend to disrupt themselves. The models will eat your scaffolding for breakfast."

针对 12 到 18 个月内预期的功能进行设计，以避免构建最终被模型本机吸收的自定义脚手架。

### 采用渐进式自治方法
Aishwarya Naresh Reganti + Kiriti Badam: "You need to be deliberately starting in places where there is minimal impact and more human control so that you have a good grip of what are the current capabilities and what can I do with them and then slowly lean into the more agency and lesser control."

从人机交互建议开始，然后扩展到完全自主交互，从而安全地部署代理系统。

## 模板和框架

- **AI 术语表 - 20 多个关键术语**（AI 术语表）- AI 术语的综合参考列表，其中包含“像我 5 岁一样解释”定义，旨在方便会议时使用
- **AI产品构建者的 12 条原则**（构建AI产品的反直觉建议）- 一套构建AI产品的 12 条反直觉原则，由 GitHub、Canva、Superhuman、Perplexi 等公司的 20 多个AI产品领导者汇编而成
- **CC/CD（持续校准/持续开发）框架**（为什么您的 AI 产品需要不同的开发生命周期）- AI 产品的六步开发生命周期框架，考虑了非确定性和机构控制权衡。取代传统的 CI/CD 思维
- **AI集成决策框架**（摘要：AI和产品管理 | Marily Nika（Meta，Google）） - 何时以及如何将AI添加到产品中的决策方法
- **应用于AI产品构建的痛苦教训** (Sherwin Wu V2) - 将 Rich Sutton 的痛苦教训扩展到使用AI构建产品 — 脚手架和解决方法被模型改进所吞噬
- **AI初创企业防御性框架** (Peter Deng) - 构建防御性AI初创企业的三大支柱：专有数据飞轮、精心设计的工作流程以及克服现有分销的产品工艺。
- **AI产品思维方式转变：原型优先与设计优先**（构建AI产品的反直觉建议）- 将传统软件开发方法与可行性不确定的AI原生方法进行对比的框架
- **AI产品差异化堆栈：数据>接口>模型**（构建AI产品的反直觉建议）-AI产品持久竞争优势所在的层次结构
- **AI中的粘性护城河** (Scott Wu) - 在AI产品中，防御性来自于复合粘性（积累的知识、团队工作流程、学习），而不是硬性的进入壁垒

有关详细信息的完整列表，请参阅 `references/artifacts.md`。

## 帮助用户的问题

- “在您的产品中，自动化带来最大回报的高摩擦琐事是什么？”
- “您的用例是否需要访问实时的内部数据或特定的、一致的行为风格？”
- “你如何设计接口来处理不确定或不正确的AI输出？”
- “您是否正在构建一个基础模型更新可能会在一年内过时的功能？”
- “您拥有哪些竞争对手无法轻易访问或复制的专有数据？”
- “随着时间的推移，你将如何衡量产品学习循环的新陈代谢？”

## 标记的常见错误

- **针对当前模型的限制进行构建** - 创建复杂的脚手架来解决当今模型的弱点是一种失败的策略，因为基础模型很快就会吸收该功能。
- **为了AI本身而添加AI** - 没有经过验证、数据支持的用户问题的通用AI功能无法提供有意义的价值或防御性。
- **假设 100% 准确度** - 当模型不可避免地产生幻觉时，未能考虑AI的概率性质会导致用户体验破裂。
- **将提示工程优先于数据** - AI功能的有效性通常更多地受到基础数据的质量和及时性的限制，而不是提示本身。

## 深入探讨

有关 26 位来宾的全部 45 条见解，请参阅 `references/guest-insights.md`

## 相关skill

- AI 评估
- AI 原生用户体验
