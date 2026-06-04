---
name: managing-tech-debt
description: 帮助用户战略性管理 technical debt。Use when someone is dealing with legacy code, planning refactoring work, deciding between rewrites vs. incremental fixes, trying to get buy-in for tech debt reduction, or balancing new features with maintenance.
---

# Managing Tech Debt

使用来自 18 位产品领导者的洞察，帮助用户战略性管理 technical debt。

## 如何提供帮助

当用户请求 tech debt 相关帮助时：

1. **理解 situation** - 询问 debt 的性质（legacy systems、code quality、architectural limitations）、表现方式（slow velocity、incidents、inability to ship），以及 business context
2. **诊断 urgency** - 判断它是在阻塞 critical business needs，还是 slower-burning issue
3. **选择合适 approach** - 帮助他们在 incremental improvement、targeted refactoring 或极少数情况下 full rewrite 之间选择
4. **构建 business case** - 帮助量化 debt 成本，并向 stakeholders 传达 value

## 核心原则

### Rewrites 几乎永远不会按预期工作
Camille Fournier: "Engineers notoriously, notoriously, notoriously, massively underestimate the migration time for old system to new system. By the way, you still have to support the old system while you're working on the new system." Full rewrites 是陷阱。优先 incremental evolution：提升具体 components，而不是从零开始。

### Tech debt 是 product debt
Ebi Atawodi: "Infrastructure is the product. Period. I cannot build a skyscraper on a shaky foundation. So it is your problem too - it's not for the engineer to be barging on the door." Technical debt 应由 PMs 作为 "product debt" 共同 owning，而不是当成 engineering-only concern。把它纳入 Top 10 Problems list。

### Startups 应该战略性承担 debt
Gaurav Misra: "As a startup your job is to take on technical debt because that is how you operate faster than a bigger company." Debt 是 leverage；评估某个问题是否可以由未来招聘来解决，而不是今天解决。但要监控 "interest"：如果 maintenance 占用 80-90% 时间，你已经耗尽 runway。

### 删除代码要多于写代码
Farhan Thawar: "We have a Delete Code Club. We can almost always find a million-plus lines of code to delete. Everything gets easier - the codebase loads faster, it's easier to understand." 创建专门时间或团队只负责移除 unused code。Deletion 会提升 velocity 和 clarity。

### Tech debt 对用户可见
Matt Mullenweg: "You can see [tech debt] in the interface or how their products integrate with themselves." Fragmented UIs 和 features 之间糟糕 integration 是 accumulated debt 的 user-facing symptoms。寻找 inconsistencies 来识别 debt 积累处。

### 量化 pay down debt 的价值
Casey Winters: "The most impactful projects are the hardest to measure, so they get chronically underfunded. Build custom metrics to show the value, run small tests that prove the worthwhile-ness of the investment." 创建 custom metrics 并运行 experiments 来证明 business value。与 engineering 和 design 对齐，形成统一立场。

### 立即修 bugs，不要 backlog
Geoff Charles: "We don't have a bug backlog. We fix every bug once they're surfaced almost." 把 bugs 直接分配给 on-call engineer，确保即时 pain awareness。Bug backlogs 会变成 graveyards。

### Debt 会给 innovation 加天花板
Eeke de Milliano: "Sometimes teams are just getting bogged down by urgent work - too much tech debt, bugs, instability. There's no way they can focus on bigger, creative stuff if they're heads-down dealing with incidents all day." 诊断团队是否陷入 "hierarchy of needs" trap。优先 debt reduction，释放 headspace 做 creative work。

### Tech debt 是 champagne problem
Julia Schottenstein: "We would be so lucky to have tech debt because that means people are using the product. What we didn't need at launch was a distributed scheduler - we had no users." 先构建最简单、最 naive version。接受 debt 作为把 product 交到 users 手里的 trade-off。

### 为 dark tunnels 做计划
Melanie Perkins: "We thought it would take six months... it took two years of not shipping any product." Major rewrites 是会让 shipping 停滞的 "dark tunnels"。如果必须做，用 gamify 维持团队 momentum。

### 为 1-2 年后设计
Austin Hay: "Think one to two years down the road about what we're going to need. When setting up tools, ask: 'What happens a year from now if I don't change anything?'" 提前实施 SSO 或 proper data schemas 等 foundational elements，避免以后灾难性 migration。

## 帮助用户的问题

- "这项 debt 是否阻塞 critical business needs，还是一个 slower-burning issue？"
- "Engineering time 中有多少比例花在 maintenance vs. new features？"
- "你们是否估算过 rewrite 实际需要多久？是谁做的估算？"
- "如果再 6 个月什么都不做，会发生什么？"
- "有没有 incremental improvement 的方式，而不是 rewrite？"
- "你会如何向 stakeholders 量化这项 debt 的成本？"

## 需要提醒的常见错误

- **规划 full rewrite** - Rewrites 几乎不会按计划进行。通常比估算多 2-3 倍时间，而且必须同时支持两个 systems
- **把 tech debt 当成 engineering 的问题** - 这是 product debt。PMs 应与 engineers 一起 owning
- **让 bug backlogs 堆积** - Bug backlogs 会变成 graveyards。要么立即修，要么决定不修
- **在 product-market fit 前 over-engineering** - Debt 是 champagne problem。先构建 naive solutions，并接受 debt 作为学习成本
- **没有量化成本** - Tech debt 投资常因价值无法衡量而 underfunded。建立 metrics 并运行 experiments 证明 ROI

## Deep Dive

所有来自 18 位嘉宾的 20 条洞察见 `references/guest-insights.md`

## 相关 Skills

- Technical Roadmaps
- Platform & Infrastructure
- Engineering Culture
- Evaluating Trade-offs
