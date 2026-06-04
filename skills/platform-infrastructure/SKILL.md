---
name: platform-infrastructure
description: 帮助用户构建并扩展内部平台和 technical infrastructure。Use when someone is deciding whether to build vs buy tooling, designing developer platforms, creating shared services, or managing technical debt at scale.
---

# Platform Infrastructure

使用来自 5 位 product 和 engineering leaders 的洞察，帮助用户设计并扩展 internal platforms 和 shared technical infrastructure。

## 如何提供帮助

当用户请求 platform infrastructure 相关帮助时：

1. **理解 platform purpose** - 询问他们是为 internal developers、external partners，还是两者构建
2. **评估 organizational readiness** - 判断他们是否具备支持 platform 的 adoption 和 governance structures
3. **识别 leverage points** - 帮助他们找到 platform investment 能创造最大 value multiplication 的地方
4. **为 adoption 设计** - 确保 platform 解决真实 developer problems，而不是理论问题

## 核心原则

### 将 common capabilities 抽象成 shared infrastructure
Daniel Lereya: "We actually stopped for the first time and say, 'What is the column like?' And we also organized all the product architecture around it... making the work of adding a new column just thinking about the specific." 扩展 feature velocity 需要把重复 components 抽象成 shared infrastructure，让 developers 只聚焦 unique logic。

### Invisible infrastructure 往往最重要
Asha Sharma: "It wasn't the hundreds of features, it was all in the infrastructure and the platform... performance, reliability, privacy, safety, all of those things." Major platforms 的成功常取决于 reliability、speed 等 "invisible" qualities，而不是 visible features。

### 在需要前规划 scale
Ivan Zhao: "During COVID, we just couldn't scale up our infrastructure. For the longest time, Simon's really good at don't do premature optimization... we're running off even the largest instance there is for Postgres." 避免 premature optimization 是好事，但 infrastructure 必须提前规划，避免 usage spikes 时出现 "doomsday" scenarios。

### 把 discoverability 构建进 architecture
Eli Schwartz: "If you create a categorized sitemap where you can say, 'These are all the questions on health and from the sitemap... then a search engine can navigate through the entire site, and all of the questions and answers are discoverable.'" 对 large-scale platforms，HTML sitemaps 和 internal linking 等结构性决策对 search engine discoverability 至关重要。

### 默认使用 server-side tracking
Vijay: "The biggest mistake is setting up analytics using client side SDKs... start tracking events from your servers instead of from your clients." Server-side tracking 在 data reliability、cross-platform consistency 和 developer maintenance 上优于 client-side SDKs。

## 帮助用户的问题

- "这个 platform 的 'users' 是谁？他们今天在解决什么 problems？"
- "当前 developer experience pain point 中，哪个最消耗 productivity？"
- "你如何衡量这个 platform 是否真的被 adopted？"
- "这是 build vs buy decision，还是现在应该继续 manual process？"
- "你的 'doomsday clock' 是什么：当前 infrastructure 什么时候会到极限？"

## 需要提醒的常见错误

- **为抽象未来构建** - 基于预期 needs 创建 capabilities，而不是基于当前 developer pain
- **Platform without product ownership** - 把 infrastructure 当 technical project，而没有 dedicated product management
- **避免 premature optimization 直到太晚** - 不监控 infrastructure limits，没能在 failure 前触发 scaling projects
- **默认 client-side tracking** - 使用 browser SDKs，而不是 server-side event tracking
- **忽视 migration cost** - 构建新 platforms，却没考虑把 teams 从 existing solutions 迁移出来的成本

## Deep Dive

所有来自 5 位嘉宾的 6 条洞察见 `references/guest-insights.md`

## 相关 Skills

- platform-strategy
- product-operations
- scoping-cutting
