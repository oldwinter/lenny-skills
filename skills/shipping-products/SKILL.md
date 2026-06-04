---
name: shipping-products
description: 帮助用户更快、更高质量地 ship products。Use when someone is planning a launch, struggling to release features, dealing with shipping velocity issues, or trying to establish better release practices.
---

# Shipping Products

使用来自 47 位产品领导者的框架和洞察，帮助用户有效 ship products。

## 如何提供帮助

当用户请求 shipping 相关帮助时：

1. **理解 blocker** - 询问是什么阻碍 ship：scope、quality concerns、dependencies，还是 organizational friction
2. **评估 context** - 判断这是 new product、feature iteration，还是 infrastructure change
3. **挑战 timelines** - 应用 'maximally accelerated' 原则识别 critical path
4. **指导 quality tradeoffs** - 帮助在 speed 和适合该 product type 的 quality standards 之间取得平衡

## 核心原则

### Speed 是 competence 的信号
Nan Yu: "If you look at people at the pinnacle of their craft, you can tell how good the output is going to be by how fast they're going." 高 speed 加上 quality 说明的是 mastery，而不是 sloppy。用 speed 增加 iterations 和 tested variations。

### Ship 是为了获得 feedback
Dylan Field: "Get it out as fast as you possibly can. The faster you get it out, the more feedback you get." 优先 shipping speed 来加速 feedback loop，这是 early product development 中最有价值的资产。

### Speed 和 stability 一起提升
Nicole Forsgren: "When you move faster, you are more stable. You're pushing smaller changes more often with a smaller blast radius." 更频繁地 push smaller changes，以降低 complexity，并让 failures 更容易 debug。

### 99% done 就是 0% done
Dmitry Zlokazov: "If something is 99% done, it's closer to 0% rather than 100%." Product 在 fully finished and launched 前，对 customer value 是零。保持 relentless focus，直到 shipping complete。

### 问为什么不能明天 ship
Nick Turley: "Why can't we do this now? If this was the most important thing and you wanted to truly maximally accelerate it, what would you do?" 用这个问题剥离 non-essential blockers，识别 critical path。

### 使用 quality checklists
Matt MacInnis: "We have a Product Quality List that articulates the standards we want you to meet when you ship." 创建 release 前必须满足的 PQL checklist，并在 bugs slip through 后持续迭代。

### 先 ship 学习，再 polish
Nick Turley: "You won't know what to polish until after you ship." 在 AI 这类 emergent products 中，尽早 ship，根据 real-world usage 发现哪些 areas 真正需要 polish。

### Tempo 比 org design 更重要
Patrick Campbell: "Your tempo framework is more important than your org design. If a team is always planning but doesn't ship, you don't have alignment on what good tempo looks like." 为每个 department 定义 shipping frequency expectations。

### Perfect execution 才能验证 strategy
Naomi Gleit: "Only with perfect execution can we reevaluate whether the strategy is right or wrong." Poor execution 会让 failure 的原因变得 ambiguous。properly ship，才能学习 strategy 是否正确。

### 小而持续的 gains 会 compound
Keith Yandell: "If you continuously push up what you ship by a week, you'll end up lapping competitors because you start the next thing a week sooner." Small velocity improvements 会通过 compound interest 创造巨大的 competitive advantages。

## 帮助用户的问题

- "要明天 ship 需要什么？真正 block 你的是什么？"
- "这是 reliability 很重要的 mission-critical product，还是可以 raw ship and iterate？"
- "能让你从 real users 学到东西的 smallest version 是什么？"
- "谁是有 authority 做最终 trade-off decisions 的 single person？"
- "必须满足的 quality bar 是什么？哪些可以 launch 后 polish？"
- "你上一次拥有 working、testable version 是什么时候？"

## 需要提醒的常见错误

- **Over-polishing before launch** - 在看到 real usage patterns 前，你不知道什么需要 polish
- **Waiting for pixel-perfect designs** - Early versions 不需要 pixel perfection；它们需要的是可交互的 working software
- **Feature flag sprawl** - 过量 feature flags 会制造 technical debt 和 launch 时的 hidden failure points
- **No single decision maker** - Coherent product design 需要一个有 moral authority 做 trade-off decisions 的人
- **Confusing activity with shipping** - 如果没有实际 release 的 velocity，高质量 ideation 和 documentation 都没有用

## Deep Dive

所有来自 47 位嘉宾的 55 条洞察见 `references/guest-insights.md`

## 相关 Skills

- Writing PRDs
- Stakeholder Alignment
- Setting OKRs & Goals
- Usability Testing
