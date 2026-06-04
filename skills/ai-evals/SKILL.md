---
name: ai-evals
description: 帮助用户创建并运行 AI evals。Use when someone is building evals for LLM products, measuring model quality, creating test cases, designing rubrics, or trying to systematically measure AI output quality.
---

# AI Evals

使用 AI practitioners 的洞察，帮助用户为 AI 产品创建系统化评估。

## 如何提供帮助

当用户请求 AI evals 相关帮助时：

1. **理解他们要评估什么** - 询问他们正在测试哪个 AI feature 或 model，以及什么样的输出算 "good"
2. **帮助设计 eval 方法** - 建议 rubrics、test cases 和 measurement methods
3. **指导 implementation** - 帮助他们思考 edge cases、scoring criteria 和 iteration cycles
4. **连接到产品需求** - 确保 evals 对齐真实用户需求，而不只是技术指标

## 核心原则

### Evals 是新的 PRD
Brendan Foody: "If the model is the product, then the eval is the product requirement document." Evals 定义了 AI 产品里的成功标准；它们不是可选的质量检查，而是核心 specification。

### Evals 是核心产品能力
Hamel Husain & Shreya Shankar: "Both the chief product officers of Anthropic and OpenAI shared that evals are becoming the most important new skill for product builders." 这不只是 ML engineers 的工作，产品人员也需要掌握。

### 工作流很重要
构建好的 evals 需要 error analysis、open coding（写下哪里出了问题）、聚类失败模式，并创建 rubrics。这是一个系统化流程，而不是一次性测试。

## 帮助用户的问题

- "对这个 AI output 来说，'good' 具体是什么样？"
- "你见过最常见的 failure modes 是什么？"
- "你如何判断 model 变好了还是变差了？"
- "你测量的是用户真正关心的东西吗？"
- "你是否已经手动 review 足够多的 outputs，以理解 failure patterns？"

## 需要提醒的常见错误

- **跳过人工 review** - 如果没有先通过 manual trace analysis 理解 failure patterns，就写不出好的 evals
- **使用模糊标准** - "The output should be good" 不是 eval；你需要具体、可测量的标准
- **LLM-as-judge 但不验证** - 如果用 LLM 做 judge，必须用人类专家结果验证这个 judge
- **用 Likert scales 代替 binary** - 尽量强制 Pass/Fail 决策；1-5 分量表容易产生无意义的平均值

## Deep Dive

所有来自 2 位嘉宾的 2 条洞察见 `references/guest-insights.md`

## 相关 Skills

- Building with LLMs
- AI Product Strategy
- Evaluating New Technology
