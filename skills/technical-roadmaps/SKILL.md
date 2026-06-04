---
name: technical-roadmaps
description: 帮助用户创建 technical roadmaps。Use when someone is planning engineering work, prioritizing tech debt, building architecture roadmaps, or aligning technical and product strategy.
---

# Technical Roadmaps

使用来自 1 位产品领导者的框架和洞察，帮助用户创建有效 technical roadmaps。

## 如何提供帮助

当用户请求 technical roadmaps 相关帮助时：

1. **理解 context** - 询问当前 technical state、team size 和 business constraints
2. **确保写下来** - 没有 documented 的 strategy 无法 debug，也无法围绕它 align
3. **应用 Rumelt framework** - 结构化为 Diagnosis（问题是什么）、Guiding Policies（决策原则）和 Actions（要做什么）
4. **Favor boring strategies** - 帮助他们抵抗引入 new tools 的冲动，尤其当 existing tools 已经足够时

## 核心原则

### Write it down
Will Larson: "The first rule of strategy is that if you write it down, then you can improve it. If it's not written down, it's hard to say if this PM is just not a good PM or if they're trying to apply a strategy they've misunderstood." Written strategy 提供一个可以 critique 和 improve 的 baseline。

### Boring strategies often win
Will Larson: "A common strategy that's really good but very boring is we only use the tools we have today. Engineers want to introduce new programming languages, new databases, new cloud providers. A really good strategy for almost all companies is we just use the standard kit we already have." 把 engineering energy 聚焦到 business-valued problems，而不是 technical novelty。

### 使用 Rumelt framework
使用 Richard Rumelt 的 framework 结构化 technical strategy：Diagnosis（core challenge 是什么？）、Guiding Policies（哪些 principles 指导 decisions？）和 Actions（你会做哪些 specific things？）。

### 创建 standard kit
定义 approved tools、languages 和 platforms 的 list。这能限制 technical sprawl，让 teams 专注于解决 core product problems，而不是 reinventing infrastructure。

## 帮助用户的问题

- "这份 technical strategy 是否写在任何人都能 reference 的地方？"
- "你要解决的 core technical challenge 是什么（diagnosis）？"
- "哪些 principles 会指导你的 technical decisions（guiding policies）？"
- "你引入 new tools 是因为需要，还是因为它们有趣？"
- "你的 approved technologies 'standard kit' 是什么样？"
- "这份 technical roadmap 如何连接到 business outcomes？"

## 需要提醒的常见错误

- **Unwritten strategy** - 只存在某个人脑子里的 strategy 无法 debug，也无法围绕它 align
- **Tool proliferation** - 在 existing technologies 已经可用时引入 new technologies，会制造 maintenance burden
- **No connection to business value** - 没有绑定 product 或 business outcomes 的 technical roadmaps 缺少 justification
- **All diagnosis, no action** - Good strategy 需要 specific actions，而不只是 problem analysis
- **Missing guiding policies** - 没有 principles，每个 technical decision 都会变成从零开始的 debate

## Deep Dive

所有来自 1 位嘉宾的 2 条洞察见 `references/guest-insights.md`

## 相关 Skills

- Managing Tech Debt
- Platform Strategy
- Engineering Culture
- Prioritizing Roadmap
