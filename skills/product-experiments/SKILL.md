---
name: product-experiments
description: 帮助用户设计、执行和分析产品实验，以验证假设并衡量真正的增量影响，同时避免常见的统计陷阱。
---

# 卓越的产品实验

通过严格的 A/B 测试和数据驱动的学习，推动可衡量的增长并降低风险。

利用 9 位嘉宾的见解以及 Lenny 的播客和时事通讯中的帖子，帮助用户实现卓越的产品实验。

## 如何提供帮助

1. **假设定义** - 指导用户根据用户行为理论起草清晰、可证伪的假设。
2. **实验设计** - 帮助确定干净测试的正确指标、样本大小和护栏指标。
3. **统计分析** - 支持 p 值、置信区间和潜在样本比率不匹配的解释。
4. **战略评估** - 根据实验结果和长期业务影响，协助决定是否发布、迭代或终止某个功能。

## 核心原则

### 利用长期坚持来实现真正的增量
Archie Abrams: "So we constantly will relook at an experiment a year later, see that the way the GMV curve for the distribution was different than we might've originally thought. And that'll actually change what we do from that previous experiment. And so there's a lot of longterm monitoring of experiments over these very long time horizons to both inform what those input metrics are and more importantly hold ourselves accountable to, did we actually move what we cared about, which is that longterm GMV, in the right way?"

实施一年或多年的坚持小组，以区分直接增长和短期拉动效应。这可确保您衡量变革对下游业务的真正影响。

### 将实验重点放在风险缓解上
Lauryn Isford: "So, with all that said, generally my advice is to experiment when you need to and to primarily see it as a risk mitigation tactic when you're making dramatic changes and to let the product development process do more work. So, spend more time with customers, be more rigorous in understanding precisely what problem you're solving, get mocks in front of people and see how they react, and hopefully have more conviction than you otherwise would when you ship something that it's okay if every customer sees it tomorrow and that the experiment doesn't actually matter as much."

优先考虑高风险、剧烈的产品变化进行 A/B 测试，而不是仅仅将其用于精确的指标归因。在启动高风险测试之前，首先投资定性研究以建立信念。

### 平衡成功指标与护栏
Ronny Kohavi: "It's very easy to increase revenue by doing theatrics. Displaying more ads is a trivial way to raise revenue, but it hurts the user experience. And we've done the experiments to show that. In this case, this was just a home run that improved revenue, didn't significantly hurt the guardrail metrics."

制定稳健的总体评估标准 (OEC)，其中包括护栏指标。这可以防止短期胜利无意中降低长期用户体验或保留率。

### 使高故障率正常化
Ronny Kohavi: "At Bing, which is a much more optimized domain after we've been optimizing it for a while, the failure rate was around 85%. So it's harder to improve something that you've been optimizing for a while. And then at Airbnb, this 92% number is the highest failure rate that I've observed."

预计优化领域中 80% 到 92% 的实验都会失败。围绕这些行业标准调整团队期望可以防止灰心丧气并保持高测试量。

### 跳过低风险最佳实践的测试
From "When NOT to run an experiment – Issue 54": "If you can run experiments quickly and easily (e.g. a few hours), this decision is generally easy: run the experiment. If running experiments is a pain in the butt, and the changes are relatively benign, you can probably skip the experiment."

当统计显着性所需的时间超过数据价值时，直接交付通常优于实验。避免对下行风险最小的标准行业实践进行正式测试。

### 将泰曼定律应用于令人惊讶的胜利
Ronny Kohavi: "We can talk later about Wyman's law, but that was the first reaction, which is, 'This is too good to be true. Let's find a bug.' And we did. And we looked for several times, and we replicated the experiment several times, and there was nothing wrong with it."

任何看起来好得令人难以置信的结果都应立即持怀疑态度。进行严格的错误搜寻并多次复制令人惊讶的结果，以确保它们不是技术上的侥幸。

## 模板和框架

- **跳过实验的三个原因**（何时不运行实验 - 第 54 期）- 具有三种不同场景的决策框架，其中不进行实验的交付是正确的选择
- **整体影响计算（产品阿姆达尔定律）**（Duolingo 指数增长的秘密）- 通过考虑实际看到变化的用户百分比来计算总实验影响的框架
- **实验文化的 5 个支柱**（培育实验文化）- 源自 Airbnb 方法的五个关键领域的框架，旨在建立强大的实验文化
- **运行实验前的风险评估问题**（何时不运行实验 - 第 54 期）- 评估运行实验的风险/回报是否值得的五个问题
- **长期坚持实验方法**（Duolingo 如何构建产品）- 一种通过维持 3 个月以上的对照组来衡量社交等功能的长期影响的技术
- **注册流程的样本量计算示例**（何时不运行实验 - 第 54 期） - 一个具体示例，显示需要多少用户才能检测到转换为 10% 的步骤中 5% 的变化
- **失败实验的决策框架：终止、迭代或交付**（传达坏消息 - 第 26 期）- 项目实验显示负面结果时进行评估的三个选项
- **样本比率不匹配 (SRM) 检查** (Ronny Kohavi) - 一项统计测试，用于验证对照组与治疗组的用户比率是否与设计比率相符。对任何 A/B t 来说最重要的有效性检查

有关详细信息的完整列表，请参阅 `references/artifacts.md`。

## 帮助用户的问题

- “你用这个变化测试的核心心理假设是什么？”
- “我们需要监控哪些护栏指标以确保我们不会损害长期体验？”
- “我们是否有足够的流量在合理的时间范围内达到统计显着性？”
- “与交付已知的最佳实践相比，这个实验的潜在提升值得花费工程和分析时间吗？”
- “这个实验如何适应我们的低努力获胜与高方差大赌注之间的平衡？”
- “如果这个实验失败，我们将获得哪些具体的用户行为洞察？”

## 标记的常见错误

- **寻找显着性** - 根据实时 P 值做出决策会导致高误报率和无效结论。
- **忽略样本比率不匹配 (SRM)** - 未能验证对照和处理计数是否与预期比率匹配可能会隐藏导致结果无效的基本技术错误。
- **针对短期效果进行过度优化** - 纯粹关注即时转化指标可能会掩盖对用户体验或收入质量的长期损害。
- **失去机构记忆** - 未能记录过去的成功和失败会导致团队重复相同的实验或因组织流失而失去有价值的产品模式。

## 深入探讨

有关 9 位嘉宾的所有 13 条见解，请参阅 `references/guest-insights.md`

## 相关skill

- 客户访谈
- 不断发现
- 想法验证
- 定义 Icp
