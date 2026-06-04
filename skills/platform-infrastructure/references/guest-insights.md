# Platform & Infrastructure - 所有嘉宾洞察

*5 位嘉宾，6 次提及*

---

## Asha Sharma
*Asha Sharma*

> "it wasn't the hundreds of features, it was all in the infrastructure and the platform... performance, reliability, privacy, safety, all of those things."

**洞察：** 重大 platforms（如 WhatsApp 或 Instacart）的成功往往取决于 'invisible' infrastructure qualities，而不是 visible features。

**战术建议：**
- 在 communication platforms 中优先考虑 reliability、speed 和 end-to-end encryption
- 关注 data residency 和 availability，建立 enterprise customers 的 trust

*时间戳：38:21*


## Daniel Lereya
*Daniel Lereya*

> "We actually stopped for the first time and say, 'What is the column like?' And we also organized all the product architecture around it... we defined what is it, and then create an infrastructure for all these shared things, making the work of adding a new column just thinking about the specific product that you want to provide."

**洞察：** Scaling feature velocity 需要把 common capabilities 抽象进 shared infrastructure，让 developers 只关注 unique logic。

**战术建议：**
- 识别 repetitive feature components，并把它们构建进 core platform architecture
- 在 infrastructure level 标准化 'export to Excel' 或 'filtering' 等 capabilities

*时间戳：00:13:30*

---

> "We need few of our most talented people that are now not going to contribute features anymore. We are putting them on a separate place, and let's think and solve this problem while thinking about 100X."

**洞察：** Critical infrastructure projects（如 MondayDB）需要 dedicated teams 专注于 100X scale，而不是 incremental feature work。

**战术建议：**
- 隔离 top talent，让他们投入能提供 competitive edge 的 long-term architectural shifts
- 按 current capacity 的 100X 做 planning，提前预判 infrastructure breaking points

*时间戳：01:13:19*


## Eli Schwartz
*Eli Schwartz*

> "If you create a categorized sitemap where you can say, 'These are all the questions on health and from the sitemap... then a search engine can navigate through the entire site, and all of the questions and answers are discoverable.'"

**洞察：** 对 large-scale platforms 来说，HTML sitemap 和清晰 internal linking 对 search engine discoverability 至关重要。

**战术建议：**
- 构建 categorized HTML sitemap，让 bots 能 navigate 整个 site depth
- 在每个 page 实现 'related content' links，为 search engines 创建 crawlable web

*时间戳：00:54:48*


## Ivan Zhao
*Ivan Zhao*

> "During COVID, we just couldn't scale up our infrastructure. For the longest time, Simon's really good at don't do premature optimization, so for the longest time, we Notion runs on one instance of Postgres database... we're running off even the largest instance there is for Postgres. So there's a doomsday clock... we just need to go as fast as you can to become sharding problem."

**洞察：** 避免 premature optimization 是好事，但 infrastructure 必须提前足够 planning，避免 usage spikes 时出现 'doomsday' scenarios。

**战术建议：**
- Monitor database limits，并设置 'doomsday clock'，在 failure 前触发 sharding 等 scaling projects。
- 准备好暂停 feature development，完全聚焦 critical infrastructure scaling。

*时间戳：00:49:31*


## Vijay
*Vijay*

> "The biggest mistake is setting up analytics using client side SDKs... start tracking events from your servers instead of from your clients."

**洞察：** 在 data reliability、cross-platform consistency 和 developer maintenance 方面，server-side tracking 优于 client-side SDKs。

**战术建议：**
- 默认使用 server-side event tracking，避免 ad-blockers 导致 data loss
- 使用带 user IDs 的 server-side logs 作为 behavioral events 的 primary source

*时间戳：35:12*

