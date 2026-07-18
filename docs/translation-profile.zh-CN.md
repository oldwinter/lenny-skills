# 中文翻译配置

## 仓库与基线

- 上游仓库：`https://github.com/RefoundAI/lenny-skills.git`
- 中文 fork：`https://github.com/oldwinter/lenny-skills.git`
- 跟踪分支：`upstream/main`
- 当前上游基线：`13598cc`（`v2.0.0`）

## 必须翻译

- 根目录 `README.md` 中的安装、使用、skill 目录和贡献说明。
- `skills/*/SKILL.md` 的 `description` 值、标题、说明、步骤、原则解释、问题和常见错误。
- references 的中文阅读边界，使使用者知道哪些内容可以中文输出、哪些来源文本必须保留。

## 必须保留

- frontmatter key 与 `name` 值。
- skill slug、目录结构、相对路径、Markdown 链接目标、URL、命令和代码块。
- 人物、公司、产品、组织和协议等专有名词。
- 经来源核验的英文直接引述。
- `references/guest-insights.md` 中的英文出处与引文，以及 `references/artifacts.md` 中的规范框架、模板和 prompt。
- `LICENSE` 法律文本。

## 术语

统一译法以 `docs/translation-glossary.md` 为准。`skill`、PM、PRD、OKR、ICP、ARR、PMF、LLM、AI、B2B、BD 等运行时术语和行业缩写保留原文。

## 验证要求

1. 76 个 `SKILL.md` 都具有合法且仅包含 `name`、`description` 的 frontmatter。
2. 相比上游，frontmatter `name`、代码围栏内容、Markdown 链接目标和 reference 文件路径不变。
3. 76 个 `guest-insights.md` 与 76 个 `artifacts.md` 均带中文使用说明。
4. `git diff --check` 与本地结构对照脚本通过。
