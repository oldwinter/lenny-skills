---
name: writing-specs-designs
description: 帮助用户写出有效 specs 和 design documents。Use when someone is creating technical specs, feature specs, design docs, or trying to communicate product requirements to engineering and design teams.
---

# Writing Specs & Designs

使用来自 7 位产品领导者的框架和洞察，帮助用户写出有效 specs 和 design documents。

## 如何提供帮助

当用户请求 specs 和 design docs 相关帮助时：

1. **确定 fidelity level** - 询问他们需要 conceptual alignment（low-fi），还是 detailed implementation guidance（high-fi）
2. **鼓励 prototyping over polish** - 尽可能推动 functional prototypes，而不是 static documentation
3. **关注 moving pieces** - 帮助他们识别 key affordances、connections 和 system behaviors
4. **考虑 long-term implications** - 提醒他们 temporary shortcuts 往往会变成 permanent design decisions

## 核心原则

### Low-fidelity sketches drive collaboration
Christina Wodtke: "If I got on the whiteboard and drew really badly, somebody else will go, 'No, no, no, it doesn't work that way. Give me this pen.' It gets you so fast to a shared vision." '画得不好' 会邀请 participation 和 corrections，从而加速 alignment。

### Well-shaped specs 既 clarifies 又不过度 specifying
Ryan Singer: "The output of the shaping session is some kind of drawing or diagram where engineers, product, and design are all saying, 'I know exactly what to go build.'" 目标是达到一种 detail level：team 能看到 'electricity in the walls'，但不会规定 UI details。

### Prototype to feel the product
Tamar Yehoshua: "I can't tell you if this is going to work. I have to feel it. I have to try it. A mock-up doesn't tell you what it's going to feel like." 推动使用带 real data 的 prototypes 来 test experience，而不只是 static screenshots。

### Code prototypes over static mocks
Noah Weiss: "We stopped spending cycles on design explorations of static mocks and said, 'How quickly can we get into prototyping the path in real software, even if it's messy and throwaway?'" 尽快转向 real software prototypes。

### Products live in the pixels
Nikita Bier: "You should be designing the hierarchy, the pixels, the flows, everything. Products live and die in the pixels." 对 zero-to-one products，要 own granular design details；每次 tap 都很珍贵。

### Optimize every tap
Nikita Bier: "Every tap on a mobile app is a miracle. Users will turn and bounce to their next app very quickly." 用 extreme efficiency 设计；每次 interaction 都必须提供 immediate value。

### 使用 fat marker sketches
Ryan Singer: "Use breadboarding and fat marker sketching. We're going to hit this button, go to here, this calculation runs, then we get this answer." Fat markers 能避免陷入 colors 或 spacing 这类 UI details。

### Shortcuts become permanent
Tom Conrad: "Temporary design shortcuts often become permanent product legacies that persist through multiple technical rewrites." 注意 early implementation details 可能会定义 long-term user expectations。

### PMs 应该学会 sketch
Ravi Mehta: "Learn how to sketch, learn Balsamiq. Having that ability to think at a conceptual level about how UI and UX works is a critical part of being a PM." 培养创建 conceptual wireframes 的 self-sufficiency。

## 帮助用户的问题

- "你需要 team alignment（low-fi sketch），还是 implementation guidance（high-fi spec）？"
- "你能否 prototype this，而不是 document it？"
- "这个 solution 中 10 个以内的 moving pieces 是什么？"
- "你是否用 real users test 过这个 design，而不只是 stakeholders？"
- "哪些 temporary shortcuts 可能变成 permanent decisions？"
- "这个 flow 中每次 tap 是否都给 user 提供清晰 value？"

## 需要提醒的常见错误

- **Over-specified wireframes** - High-fidelity mockups 会拖慢 collaboration；从 fat marker sketches 开始
- **Static mocks for complex interactions** - 用 real prototypes test feel，而不是 screenshots
- **Ignoring pixel-level details** - 对 consumer products 来说，每次 tap 和 transition 都重要
- **Specs that no one reads** - 如果 engineers 不使用 document，说明 format 或 fidelity 错了
- **Temporary decisions that persist** - 认识到 early shortcuts 可能持续几十年

## Deep Dive

所有来自 7 位嘉宾的 10 条洞察见 `references/guest-insights.md`

## 相关 Skills

- Writing PRDs
- Usability Testing
- Stakeholder Alignment
- Shipping Products
