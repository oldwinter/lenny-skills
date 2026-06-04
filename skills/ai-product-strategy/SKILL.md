---
name: ai-product-strategy
description: 帮助用户定义 AI 产品策略。Use when someone is building an AI product, deciding where to apply AI in their product, planning an AI roadmap, evaluating build vs buy for AI capabilities, or figuring out how to integrate AI into existing products.
---

# AI Product Strategy

使用来自 94 位产品领导者和 AI practitioners 的框架，帮助用户围绕 AI 产品做出战略决策。

## 如何提供帮助

当用户请求 AI product strategy 相关帮助时：

1. **理解上下文** - 询问他们在构建什么、解决什么问题，以及当前处在 AI journey 的哪个阶段
2. **澄清问题** - 帮助区分 "AI for AI's sake" 和 AI 确实能解决的真实用户问题
3. **指导架构决策** - 帮助他们思考 build vs buy、model selection 和 human-AI boundaries
4. **为迭代做规划** - 强调 feedback loops、evals，以及为 model 快速进步而构建

## 核心原则

### 从问题开始，而不是从 AI 开始
Aishwarya Naresh Reganti: "In all the advancements of AI, one slippery slope is to keep thinking about solution complexity and forget the problem you're trying to solve. Start with minimal impact use cases to gain a grip on current capabilities." 不要被方案复杂度牵着走，先确认你到底在解决哪个用户问题。

### 定义 human-AI boundary
Adriel Frederick: "When working on algorithmic products, your job is figuring out what the algorithm should be responsible for, what people are responsible for, and the framework for making decisions." 这条边界是核心 PM 决策。

### AI 是 magical duct tape
Alex Komoroske: "LLMs are magical duct tape—distilled intuition of society. They make writing 'good enough' software significantly cheaper but increase marginal inference costs." 理解新的成本结构：AI 降低了构建 "good enough" software 的成本，但提高了边际 inference cost。

### 为 slope 构建，而不是为 snapshot 构建
Asha Sharma: "You have to build for the slope instead of the snapshot of where you are." AI capabilities 变化很快；构建灵活架构，让 model 进步时可以替换。

### 为 squishiness 设计
Alex Komoroske: "Even at 99% accuracy, if it punches the user in the face 1% of the time, that's not a viable product. Design assuming the AI will be squishy and not fully accurate." 默认 AI 会有不稳定和不完全准确的时候，并据此设计体验。

### Flywheels 胜过 first-mover advantage
Aishwarya Naresh Reganti: "It's not about being first to have an agent. It's about building the right flywheels to improve over time." 记录人类动作，创造能让系统持续改进的数据循环。

### 未来是 model society，而不是 single model
Amjad Masad: "Future products will be made of many different models—it's quite a heavy engineering project." 为不同任务使用专门 models，例如 reasoning、speed、coding 等。

### 为每个任务使用合适工具
Albert Cheng: "We run chess engines for evaluations. LLMs translate that into natural language. Use the right technology for the right task." 在 deterministic algorithms 表现更好的地方，不要强行使用 LLMs。

### 人类是瓶颈
Alexander Embiricos: "The current limiting factor is human typing speed and multitasking on prompts. Build systems that are 'default useful' without constant prompting." 构建无需持续 prompt 也能默认有用的系统。

### 考虑 non-determinism
Aishwarya Naresh Reganti: "Most people ignore the non-determinism. You don't know how users will behave with natural language, and you don't know how the LLM will respond." 要为用户自然语言行为和 LLM response 的变化性做设计。

### Agents 需要 autonomy + complexity + natural interaction
Aparna Chennapragada: "Effective agents have (1) increasing autonomy to handle higher-order tasks, (2) ability to handle complex multi-step workflows, and (3) natural, often asynchronous interaction." 判断 agent 机会时，同时看自主性、复杂多步工作流和自然交互。

### 重建你的直觉
Aishwarya Naresh Reganti: "Leaders have to get hands-on—not implementing, but rebuilding intuitions. Be comfortable that your intuitions might not be right." 领导者需要亲自上手，不一定写实现，但要重建判断力；每天留时间保持更新。

## 帮助用户的问题

- "你想用 AI 解决哪个具体用户问题？"
- "哪些事情应该由 AI 决定，哪些应该由人决定？"
- "当 AI 在 5% 的场景里失败时，你会怎么处理？"
- "什么 feedback loops 会让系统随时间改进？"
- "你是在为今天的 model capabilities 构建，还是也预期了后续改进？"
- "你是否已经设置 evals 和 observability？"

## 需要提醒的常见错误

- **为了 AI 而 AI** - 在没有清晰用户问题的情况下添加 AI features
- **Single-model thinking** - 没有考虑为不同任务使用 specialized models
- **忽视失败场景** - 没有为 AI 出错时的 UX 做设计
- **静态架构** - 构建无法随着 model improvements 演进的系统
- **跳过 evals** - 没有从第一天建立 measurement 和 observability
- **过度自动化** - 在人类仍能创造价值的 loop 里移除人

## Deep Dive

所有来自 94 位嘉宾的 179 条洞察见 `references/guest-insights.md`

## 相关 Skills

- Building with LLMs
- AI Evals
- Evaluating New Technology
- Platform Strategy
