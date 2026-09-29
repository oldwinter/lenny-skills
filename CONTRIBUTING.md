# 为 Lenny's Product Skills 做贡献

感谢你有兴趣改进这些 skills！这份指南会帮助你更有效地贡献。

## 贡献方式

### 1. 修复错误或过时信息
- 不准确的出处归因
- 过时的框架
- 拼写错误或格式问题

### 2. 改进已有 Skills
- 补充 podcast 节目中的缺失框架
- 让建议更可执行、更具体
- 增加更好的诊断问题
- 改进 "Common Mistakes to Flag" 部分

### 3. 新增 Skills
- Skills 应基于 Lenny's Podcast 嘉宾的洞察
- 至少包含 3-5 条有实质内容且带归因的原则
- 应该可执行，而不只是提供信息

## Skill 文件格式

每个 skill 位于 `skills/{skill-name}/SKILL.md`：

```markdown
---
name: skill-name
description: 当用户需要[任务或决策]时使用；帮助用户[可执行结果]。
---

# Skill 中文标题

利用 [N] 位产品领导者的框架和见解，帮助用户[目标]。

## 如何提供帮助

当用户需要[主题]方面的帮助时：

1. **First step** - [What to do]
2. **Second step** - [What to do]
3. **Third step** - [What to do]
4. **Fourth step** - [What to do]

## 核心原则

### Principle title
[Guest Name]: "[Direct quote or close paraphrase]" [Actionable guidance explaining how to apply this.]

### Another principle
[Guest Name]: "[Quote]" [Guidance]

## 帮助用户的问题

- "[Diagnostic question]"
- "[Another question]"

## 标记的常见错误

- **[Mistake pattern]** - [Why it's wrong and what to do instead]
- **[Another mistake]** - [Explanation]

## 深入探讨

有关 [M] 个来源的全部 [N] 条见解，请参阅 `references/guest-insights.md`

## 相关skill

- [Related skill 1]
- [Related skill 2]
```

## 质量标准

### Descriptions
- 使用自然、可执行的中文描述
- 明确说明任务触发条件，例如“当用户需要……时使用”
- 保留会影响检索的行业缩写和英文术语（如 PM、PRD、OKR、ICP、LLM）
- 控制在 200 个字符以内

### Principles
- 始终归因到具体嘉宾
- 尽可能包含直接引用
- 在 quote 后添加可执行指导
- 每个 skill 目标为 5-15 条原则

### Questions
- 应该是诊断型问题，而不是诱导型问题
- 帮助 Claude 理解用户的具体处境
- 应该是 Claude 实际会问的问题

### Common Mistakes
- 应该是具体、可观察的模式
- 说明为什么有问题
- 建议替代做法

## Pull Request 流程

1. Fork 本仓库
2. 创建分支：`git checkout -b improve-skill-name`
3. 完成修改
4. 复制到 `.claude/skills/` 并实际试用
5. 提交 PR，并说明：
   - 你改了什么
   - 为什么改（如果新增内容，请引用 podcast episode）
   - 你如何测试

## Code of Conduct

- 保持尊重和建设性
- 准确标注来源
- 聚焦可执行、实用的建议
- 把用户成功作为优先级

## 有问题？

如果有不确定的地方，请打开 issue！
