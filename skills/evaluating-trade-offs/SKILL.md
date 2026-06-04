---
name: evaluating-trade-offs
description: 帮助用户在相互竞争的选项之间做出更好的决策。Use when someone is weighing pros and cons, comparing alternatives, struggling with a difficult choice, deciding between speed and quality, or asking "should we do X or Y?"
---

# Evaluating Trade-offs

使用来自 40 位产品领导者的框架和 mental models，帮助用户在相互竞争的选项之间做出更清晰决策。

## 如何提供帮助

当用户请求 evaluating trade-offs 相关帮助时：

1. **理解 decision context** - 询问他们在优化什么（short-term vs. long-term、growth vs. quality、speed vs. thoroughness），以及这个 decision 为什么困难
2. **识别真实 constraints** - 帮助区分 actual constraints 和 assumed constraints。问："如果 [constraint] 不是问题，你会怎么做？"
3. **揭示 hidden costs** - 帮助量化每个选项的完整成本，包括 maintenance burden、opportunity cost 和 second-order effects
4. **应用合适 framework** - 对复杂 multi-factor decisions 使用 weighted criteria matrices；对 continuation decisions 使用简单的 "would I start this today?" test

## 核心原则

### 优化 order-of-magnitude，而不是 precision
Alex Komoroske: "It doesn't really matter if it's 1,000 or 1,001, who cares? It's orders of magnitude larger than the alternative, and so it is better." 在不确定环境中不要浪费精力追求 false precision，重点判断某个选项是否明显更好，而不是边际更好。

### 应用 "would I start this today?" test
Annie Duke: "If you wouldn't start this today, then that means that everything that you're putting into this going forward is the actual waste." 评估是否继续项目时，完全忽略 sunk costs。唯一相关问题是：以今天的认知，你还会开始这件事吗？

### Think more, ship better
Anuj Rathi: "Most experiments should be thought experiments. They should not even be tried out because they're obviously going to fail." 不要默认 "let's just try it"；严谨的前置思考能在消耗 engineering resources 前淘汰弱想法。

### 为长期收益接受 "worse first"
Graham Weaver: "Everything you want is on the other side of worse first." 有意义的改变需要接受短期下降。问 5 年后的自己希望你做什么，而不是明天怎么更轻松。

### 创建 decision tenets，消除重复争论
Bob Baxley: "Tenets are really decision-making tools... you sort of make a rule for yourself." 找出团队反复争论的问题，并创建 tenet 一次性决定方向。好的 tenets 足够具体，以至于有人能合理主张相反观点。

### 量化 countervailing metrics
Ronny Kohavi: "Here's the money that we generate from the emails. Here's the money that we're losing on long-term value. What's the trade-off?" 给负面用户行为（unsubscribes、churn）赋予 dollar values，以便客观权衡短期收益。

### 使用 weighted criteria matrix
Nicole Forsgren: "Identify the criteria that are most important to you... give everything a score, and just multiply it out." 创建 decision-making spreadsheet：options 做 rows，weighted criteria 做 columns。这个过程常常在计算完成前就揭示答案。

### 向 leadership 呈现清晰 "either/or" choices
Geoff Charles: "Be very clear with the tradeoffs... present those tradeoffs back to your leadership team. Here's what we're doing and here's what we're not doing." 像说明正在做什么一样清楚地说明不做什么。用 options "menu" 强制做决策。

### 分离 "can" 和 "should"
John Cutler: "Some people are just locked into the can. They're uber pragmatic... others ask 'What should we do here?'" 不要让 feasibility constraints 主导 strategic thinking。显式问：如果 technical debt 不是问题，我们应该做什么？

### 用 data 诊断，用 design 治疗
Julie Zhuo: "Data is not a tool that's going to tell you what you should build... but it can tell you if you have a problem." 用 data 识别问题和 gaps，但依靠 design 和 intuition 发明 solutions。

### 警惕 analysis 自身的成本
Stewart Butterfield: "The cost of doing the analysis was this much. So it's guaranteed to be a loser." 评估用于分析 decision 的 person-hours 是否已经超过潜在改进的最大 upside。

### 识别谁会 lose
Ramesh Johari: "Many of the changes that are most consequential create winners and losers." 发布 feature 时，显式识别谁会损失，并判断 winners 是否为 ecosystem 提供更高 net value。

## 帮助用户的问题

- "你在优化什么：今天、这个季度，还是今年？"
- "如果你还没有投入其中，你今天会开始做这件事吗？"
- "每个选项的完整 'all-in' cost 是什么，包括 maintenance 和 opportunity cost？"
- "这个 decision 是 reversible，还是 one-way door？"
- "如果选择 option A，谁会 lose？这个 trade-off 可以接受吗？"
- "5 年后的你会希望今天做了什么？"

## 需要提醒的常见错误

- **False precision** - 花太多时间区分边际差异，而真实问题是 order-of-magnitude
- **Sunk cost fallacy** - 因为已经投入而继续失败路径，而不是评估未来价值
- **Analysis paralysis** - 决策成本超过选项之间价值差异
- **忽视 second-order effects** - 没考虑 launch 后的 maintenance burden、feature creep 或 organizational complexity
- **默认使用自己的 skillset** - 正如 Bret Taylor 所说："If you're a great engineer, the answer to almost every problem is engineering... you probably should question it"

## Deep Dive

所有来自 40 位嘉宾的 42 条洞察见 `references/guest-insights.md`

## 相关 Skills

- Prioritizing Roadmap
- Running Decision Processes
- Scoping and Cutting
- Managing Tech Debt
