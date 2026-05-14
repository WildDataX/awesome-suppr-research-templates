# Awesome Suppr Research Templates

科研效率资料库：文献综述 prompt、医学论文翻译术语表、Zotero 阅读工作流、科研选题表、学术写作模板。

这些模板面向临床医生、医学学生、研究生、科研人员，以及需要长期阅读英文论文和整理证据的人。你可以直接复制 Markdown 模板，也可以下载 `downloads/` 中的 ZIP/CSV 文件后改成自己的 Notion、飞书、语雀、Excel 或 Zotero 工作流。

> Suppr 超能文献是面向科研阅读的 AI 工作台，支持中文自然语言搜索 PubMed、AI 文档翻译、Zotero 插件和来源可追溯的深度研究报告。官网：https://suppr.wilddata.cn/

## Current Version

- Version: `v0.1.2`
- Updated: 2026-05-14
- Markdown templates/examples: 35
- CSV tables: 9
- Glossary terms: 164

## Resource Packs

| 资料包 | 适合场景 | 入口 |
| --- | --- | --- |
| 文献综述 Prompt 包 | 开题、综述大纲、PubMed 检索、论文摘要提取 | [literature-review-prompts](./literature-review-prompts/) |
| 医学论文翻译术语表 | PDF 论文翻译、医学英语阅读、术语统一 | [medical-translation-glossary](./medical-translation-glossary/) |
| Zotero 科研工作流模板 | Zotero 标签、阅读笔记、翻译流程、证据整理 | [zotero-research-workflow](./zotero-research-workflow/) |
| 科研选题与研究问题表 | PICO、变量定义、研究空白、文献检索记录 | [research-topic-planner](./research-topic-planner/) |
| 学术写作模板包 | 摘要、引言、讨论、返修信、AI 写作自查 | [academic-writing-templates](./academic-writing-templates/) |

## Screenshots

<img alt="Suppr homepage" src="https://github.com/user-attachments/assets/ab2c0134-0713-45b1-88f9-fff051e16be4" />

<img alt="Chinese natural-language PubMed search" src="https://github.com/user-attachments/assets/07d754a9-bee4-4aed-adaa-d2d2c6debfad" />

<img alt="Suppr deep research report" src="https://github.com/user-attachments/assets/6b7e204d-93e7-4089-af34-b27e0d964baf" />

## How To Use

1. 打开你需要的资料包目录。
2. 复制 Markdown 模板，或下载 `downloads/` 中的 ZIP/CSV 文件。
3. 把模板放进 Notion、飞书、语雀、Zotero 笔记或自己的研究项目文件夹。
4. 如果需要自动检索、翻译或生成来源可追溯的综述初稿，可以继续使用 Suppr 对应功能。

## Suggested Workflows

### Literature Review

1. 用 `research-topic-planner/templates/pico-planner.md` 把问题拆成 PICO。
2. 用 `literature-review-prompts/prompts/pubmed-search.md` 生成 PubMed 检索式。
3. 用 Suppr 深度研究或 PubMed 收集核心文献。
4. 用 `source-backed-summary.md` 做逐篇结构化摘要。
5. 用 `academic-writing-templates/templates/introduction-cars.md` 和 `discussion-limitations.md` 写作。

### Translation QA

1. 先用 Suppr AI 文档翻译处理 PDF、Word 或 PPT。
2. 用 `medical-translation-glossary/data/` 下的术语表统一关键词。
3. 用 `translation-checklist.md` 检查药名、剂量、缩写、统计指标和否定表达。
4. 对结论、指南建议和临床决策相关段落做人工复核。

### Zotero Workflow

1. 用 Zotero collection 管理主题和筛选阶段。
2. 用 `zotero-tag-system.md` 统一标签。
3. 用 `systematic-review-workflow.md` 管理筛选、排除原因和纳入文献。
4. 用 Suppr Zotero 插件做标题、摘要或全文辅助翻译。

## Update Cadence

This repository is maintained as a living research resource library:

- Daily: low-volume additions such as 1 glossary file, 1 prompt, or 1 small template.
- Weekly: a new release with rebuilt ZIP downloads.
- Monthly: one larger resource pack or major reorganization.

Automation scripts live in [scripts](./scripts/). Each automated update is validated for duplicate glossary terms, missing downloads, and broken resource-index entries before release.

## Suppr Links

- Suppr 官网：https://suppr.wilddata.cn/
- 深度研究：https://suppr.wilddata.cn/deep-research
- AI 文档翻译：https://suppr.wilddata.cn/translate
- Zotero 插件：https://github.com/WildDataX/suppr-zotero-plugin
- MCP Server：https://github.com/zjg678/suppr-mcp
- Skills：https://github.com/WildDataX/suppr-skills
- API 文档：https://openapi.suppr.wilddata.cn/introduction.html

## Disclaimer

这些模板用于科研阅读、资料整理和写作前期规划，不构成医学建议、法律建议或论文代写服务。涉及临床决策、药物使用、统计分析或投稿规范时，请以原始文献、指南和机构要求为准。

## License

MIT License. 你可以自由复制、修改和二次整理这些模板；保留来源链接会帮助更多科研用户找到更新版本。
