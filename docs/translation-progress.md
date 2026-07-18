# 中文翻译进度

更新时间：2026-07-18

## 当前基线

- 上游仓库：`RefoundAI/lenny-skills`
- 上游分支：`main`
- 上游版本：`v2.0.0`
- 上游提交：`13598cc`
- 中文 fork：`oldwinter/lenny-skills`

## 已完成范围

- `README.md`：1 / 1
- 面向 agent 执行的 `skills/*/SKILL.md`：76 / 76
- `skills/*/references/guest-insights.md`：76 / 76 已添加中文阅读说明，英文核验引文保持原文
- `skills/*/references/artifacts.md`：76 / 76 已添加中文使用说明，英文框架、模板和 prompt 保持原文
- 翻译规范：
  - `docs/translation-glossary.md`
  - `docs/translation-profile.zh-CN.md`

## 翻译策略

- 翻译标题、说明、步骤、问题、常见错误、安装和贡献说明。
- 保留直接引述的英文原文，在相邻中文段落中说明原则和行动方式。
- 保留 skill slug、路径、命令、URL、frontmatter key、package 名、API 名和配置键。
- 保留人物、公司、产品、组织、Podcast 和 repository 等专有名词。
- v2 references 是经过来源核验的引文、框架和模板语料；为避免改写出处或破坏模板，将其作为英文规范资料保留，并在每个文件顶部提供中文使用边界。

## 未完成范围

- 面向用户和 agent 的运行时翻译：0 个文件。
- `LICENSE` 保持原文，避免改变法律文本含义。

## 验证

本次同步检查：

```bash
git diff --check
```

另外对 76 个 skill 的 frontmatter、Markdown 链接、代码围栏和 reference 路径进行逐文件结构对照。
