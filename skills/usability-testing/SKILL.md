---
name: usability-testing
description: 帮助用户开展有效 usability testing。Use when someone is planning user tests, designing prototype validation, preparing usability studies, or trying to understand why users struggle with their product.
---

# Usability Testing

使用来自 11 位产品领导者的框架和洞察，帮助用户开展有效 usability testing。

## 如何提供帮助

当用户请求 usability testing 相关帮助时：

1. **澄清 goal** - 判断他们是在 validating concept、finding friction points，还是 optimizing conversion
2. **选择正确 fidelity** - 帮助他们在 Wizard of Oz tests、fake doors、prototypes 或 production testing 之间选择
3. **设计 test** - 指导 recruiting users、创建 scenarios，以及观察什么
4. **规划 iteration** - 讨论 findings 如何流回 product development process

## 核心原则

### Fake it before you build it
Itamar Gilad: "Initially you fake it - fake door test, smoke test, Wizard of Oz tests. We showed the tabbed inbox working to people, but it wasn't really Gmail, it was just a facade." 在写 production code 前，用 faked versions 验证 core value propositions，让 humans 在幕后执行 automated task。

### Small samples reveal big friction
Melanie Perkins: "It's amazing how you can find 10 random people on the internet and they can give such astute feedback that's so representative for such a large number of people." 只用 10 个 random people 做 tests，也能识别 core product issues。

### Watch users, don't just ask them
Uri Levine: "Simply watch users and see what they're doing. If they're not doing what you expect, then ask them why." Direct observation 能揭示 surveys 会错过的 behaviors 和 needs。当 users 偏离 expected path 时，问 'why'。

### Test multiple options, not one
Kristen Berman: "We never do a UX study where we're just showing people one thing. We always present multiple options and relatively look for which one drives the intended behavior." Single-design testing 无法有效预测 behavior。

### 克服 creator bias
Guillermo Rauch: "You tend to overrate how well your products work. It's very important to give your product to another person and watch them interact with it." 直接观察 users，有助于克服高估 product intuitiveness 的倾向。

### Micro-level testing drives millions
Judd Antin: "We changed seven characters and made Airbnb millions of dollars because we found out the button felt scary." 不要把 usability testing 当成 junior work；发现 scary 或 confusing CTAs 会巨大影响 conversion。

### 逐步推进 testing stages
Itamar Gilad: "Mid-level tests are about building a rough version - early adopter programs, alphas, longitudinal user studies, and fish food (testing on your own team)." 从 fish fooding 到 dogfooding 再到 alphas 逐步推进，iteratively 增加 confidence。

### Make testing a team sport
Noah Weiss: "We had PMs, engineers, designers, and the user researcher all in one Slack thread live, responding and reacting to the usability session." 让 cross-functional teams 在 shared chat threads 中 live-react sessions，以提升 engagement。

## 帮助用户的问题

- "你想 observe 或 validate 的 specific behavior 是什么？"
- "你需要 validate concept（使用 fake doors），还是 optimize execution（使用 real product）？"
- "你会如何 recruit 那些有 'zero skin in the game'、能给 honest feedback 的 users？"
- "你是在 test 一个 option，还是多个 options 做 compare？"
- "你会如何处理 findings？它们如何流回 development？"
- "team 中还有谁应该 observe 这些 sessions？"

## 需要提醒的常见错误

- **Testing only one design** - Present multiple options 来衡量 relative performance
- **Building before validating** - 写 production code 前先用 Wizard of Oz 或 fake door tests
- **Relying on internal intuition** - Employees 太熟悉 product，难以发现 real user friction
- **Ignoring micro-level issues** - Small copy changes 和 button labels 可能有巨大 business impact
- **Testing in isolation** - 把 engineers 和 designers 带入 sessions，建立 shared understanding

## Deep Dive

所有来自 11 位嘉宾的 14 条洞察见 `references/guest-insights.md`

## 相关 Skills

- Customer Research
- Writing PRDs
- Shipping Products
- Designing Growth Loops
