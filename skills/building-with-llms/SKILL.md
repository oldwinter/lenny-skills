---
name: building-with-llms
description: 帮助用户构建有效的 AI 应用。Use when someone is building with LLMs, writing prompts, designing AI features, implementing RAG, creating agents, running evals, or trying to improve AI output quality.
---

# Building with LLMs

使用来自 60 位产品领导者和 AI practitioners 的实用技巧，帮助用户构建有效的 AI 应用。

## 如何提供帮助

当用户请求 building with LLMs 相关帮助时：

1. **理解 use case** - 询问他们在构建什么，例如 chatbot、agent、content generation、code assistant 等
2. **诊断问题** - 帮助判断问题来自 prompt、context，还是 model selection
3. **应用相关技巧** - 分享具体 prompting patterns、architecture approaches 或 evaluation methods
4. **挑战常见错误** - 对过度依赖 vibes、跳过 evals、或为任务选择错误 model 的做法提出提醒

## 核心原则

### Prompting

**Few-shot examples 胜过描述**
Sander Schulhoff: "If there's one technique I'd recommend, it's few-shot prompting—giving examples of what you want. Instead of describing your writing style, paste a few previous emails and say 'write like this.'"

**提供你的 point of view**
Wes Kao: "Sharing my POV makes output way better. Don't just ask 'What would you say?' Tell it: 'I want to say no, but I'd like to preserve the relationship. Here's what I'd ideally do...'"

**复杂任务使用 decomposition**
Sander Schulhoff: "Ask 'What subproblems need solving first?' Get the list, solve each one, then synthesize. Don't ask the model to solve everything at once."

**Self-criticism 会改善输出**
Sander Schulhoff: "Ask the LLM to check and critique its own response, then improve it. Models can catch their own errors when prompted to look."

**Roles 帮助风格，不帮助准确性**
Sander Schulhoff: "Roles like 'Act as a professor' don't help accuracy tasks. But they're great for controlling tone and style in creative work."

**把 context 放在开头**
Sander Schulhoff: "Place long context at the start of your prompt. It gets cached (cheaper), and the model won't forget its task when processing."

### Architecture

**Context engineering > prompt engineering**
Bret Taylor: "If a model makes a bad decision, it's usually lack of context. Fix it at the root—feed better data via MCP or RAG."

**RAG quality = data prep quality**
Chip Huyen: "The biggest gains come from data preparation, not vector database choice. Rewrite source data into Q&A format. Add annotations for context humans take for granted."

**通过 model layering 提升 robustness**
Bret Taylor: "Having AI supervise AI is effective. Layer cognitive steps—one model generates, another reviews. This moves you from 90% to 99% accuracy."

**为 specialized tasks 使用 specialized models**
Amjad Masad: "We use Claude Sonnet for coding, other models for critiquing. A 'society of models' with different roles outperforms one general model."

**200ms 是 latency threshold**
Ryan J. Salva (GitHub Copilot): "The sweet spot for real-time suggestions is ~200ms. Slower feels like an interruption. Design your architecture around this constraint."

### Evaluation

**Evals 是必需项，不是可选项**
Kevin Weil (OpenAI): "Writing evals is becoming a core product skill. A 60% reliable model needs different UX than 95% or 99.5%. You can't design without knowing your accuracy."

**Binary scores > Likert scales**
Hamel Husain: "Force Pass/Fail, not 1-5 scores. Scales produce meaningless averages like '3.7'. Binary forces real decisions."

**从 vibes 开始，逐步演进到 evals**
Howie Liu: "For novel products, start with open-ended vibes testing. Only move to formal evals once use cases converge."

**验证你的 LLM judge**
Hamel Husain: "If using LLM-as-judge, you must eval the eval. Measure agreement with human experts. Iterate until it aligns."

### Building & Iteration

**失败后重试，models 是 stochastic 的**
Benjamin Mann (Anthropic): "If it fails, try the exact same prompt again. Success rates are much higher on retry than on banging on a broken approach."

**提出更有野心的请求**
Benjamin Mann: "The difference between effective and ineffective Claude Code users: ambitious requests. Ask for the big change, not incremental tweaks."

**在 models 之间 cross-pollinate**
Guillermo Rauch: "When stuck after 100+ iterations, copy the code to a different model (e.g., from v0 to ChatGPT o1). Fresh perspective unblocks you."

**Compounding engineering**
Dan Shipper: "For every unit of work, make the next unit easier. Save prompts that work. Build a library. Your team's AI effectiveness compounds."

### Working with AI Tools

**学习读代码和 debug，而不是背 syntax**
Amjad Masad: "The ROI on coding doubles every 6 months because AI amplifies it. Focus on reading code and debugging—syntax is handled."

**用 chat mode 来理解**
Anton Osika: "Use 'chat mode' to ask the AI to explain its logic. 'Why did you do this? What am I missing?' Treat it as a tutor."

**Vibe coding 是一项真实技能**
Elena Verna: "I put vibe coding on my resume. Build functional prototypes with natural language before handing to engineering."

## 帮助用户的问题

- "你在构建什么，核心用户问题是什么？"
- "model 最常出错的地方是什么？"
- "你是在系统化测量 success，还是主要凭 vibes 判断？"
- "model 能访问哪些 context？"
- "你试过 few-shot examples 吗？"
- "失败的 prompts 重试后会发生什么？"

## 需要提醒的常见错误

- **永远停留在 vibes** - 最终你需要真实 evals，而不只是 "it feels good"
- **Prompt-only thinking** - 修复点往往是更好的 context，而不是更好的 prompt
- **一个 model 处理所有事** - 不同 models 擅长不同任务
- **一次失败就放弃** - Stochastic systems 需要 retries
- **跳过 human review** - AI output 需要人类验证，尤其在早期阶段

## Deep Dive

所有来自 60 位嘉宾的 110 条洞察见 `references/guest-insights.md`

## 相关 Skills

- AI Product Strategy
- AI Evals
- Vibe Coding
- Evaluating New Technology
