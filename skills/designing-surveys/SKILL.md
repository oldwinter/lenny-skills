---
name: designing-surveys
description: 帮助用户设计有效问卷。Use when someone is creating customer surveys, NPS measurements, product-market fit surveys, or feedback collection mechanisms.
---

# Designing Surveys

使用来自 9 位产品领导者的框架，帮助用户设计有效 surveys；这些领导者曾构建严谨的 research 和 feedback systems。

## 如何提供帮助

当用户请求 surveys 相关帮助时：

1. **澄清目标** - 判断他们是在衡量 satisfaction、识别 problems，还是 prioritizing features
2. **选择合适 metric** - 帮助他们在 NPS、CSAT、PMF survey 或 custom approaches 之间选择
3. **设计干净问题** - 确保每个问题只精确测量一件事
4. **触达正确 respondents** - 帮助他们找到具有新鲜、相关体验的用户

## 核心原则

### NPS 在科学上有缺陷
Judd Antin: "NPS is the best example of the marketing industry marketing itself. The consensus in the survey science community is that NPS makes all the mistakes. Customer satisfaction, a simple CSAT metric, is better. It has better data properties, it is more precise, it is more correlated to business outcomes." 优先使用带 5-7 项量表的 CSAT。

### 用 constraints 强制 prioritization
Nicole Forsgren: "Let them pick three, just three. Of those three, how often does this affect you? Is this hourly? Is this daily? Is this weekly?" 限制 respondents 只选 top barriers，保持数据干净，再测量 frequency 来加权 impact。

### 在正确时间调查你的最佳客户
Gia Laudi: "Very importantly, they signed up for your product recently enough that they remember what life was like before. Generally, we say that's in the three to six-month range." 面向使用产品 3-6 个月的 customers，这时他们对 'before' state 的记忆仍然新鲜。

### Onboarding surveys 可以提升 conversion
Laura Schaffer: "We just asked for forgiveness and put these questions into the signup flow. An improved conversion by like 5%, just improved signups." 以 targeted questions 形式添加 'good friction'，能让用户确认自己来对地方，从而提高 conversion。

### 避免 double-barreled questions
Nicole Forsgren: "You're asking four different questions there. If someone answers yes, was it the build? Was it the test? Was it slow or was it flaky?" 确保每个 survey question 只问一个具体变量。

### 用 MaxDiff 做 feature prioritization
Madhavan Ramanujam: "Identify the most important for you, and the least important. If you do this a few times, you will be able to prioritize the entire feature set in a relative fashion." MaxDiff（Most/Least）surveys 比简单排序更适合识别 value drivers。

## 帮助用户的问题

- "这个 survey 会支持哪个具体决策？"
- "你每个问题只问一件事，还是把多件事混在一起？"
- "你的 'best' customers 是谁？他们什么时候注册的？"
- "所有 scale options 在 mobile 上不用滚动就能看到吗？"
- "你如何强制 respondents 做 prioritization，而不是把所有东西都打高分？"

## 需要提醒的常见错误

- **Double-barreled questions** - 在一个问题里同时问 speed 和 complexity
- **选项太多** - 允许 respondents 无限选择，而不是强制 prioritization
- **时机错误** - 调查太新的 customers（没经验）或太老的 customers（忘了 'before'）
- **NPS worship** - 依赖已知有科学缺陷的 metric，而不是更简单、更好的替代项
- **隐藏 scale options** - Mobile surveys 如果看不到所有选项，会制造 response bias

## Deep Dive

所有来自 9 位嘉宾的 10 条洞察见 `references/guest-insights.md`

## 相关 Skills

- Writing North Star Metrics
- Defining Product Vision
- Prioritizing Roadmap
- Setting OKRs & Goals
