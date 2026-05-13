# 文献综述 Prompt 包

这个资料包用于文献综述前期：选题拆解、PubMed 检索式生成、论文摘要提取、研究空白分析、综述大纲生成和引用核查。

适合：

- 写开题报告、综述、课题背景的人
- 需要快速进入一个陌生研究方向的人
- 医学、生命科学、药学、公共卫生、护理等方向的研究者

## Files

| 文件 | 用途 |
| --- | --- |
| [prompts/literature-review.md](./prompts/literature-review.md) | 从研究主题到综述大纲 |
| [prompts/pubmed-search.md](./prompts/pubmed-search.md) | 中文问题转 PubMed 检索策略 |
| [prompts/source-backed-summary.md](./prompts/source-backed-summary.md) | 单篇/多篇论文结构化摘要 |
| [prompts/systematic-review.md](./prompts/systematic-review.md) | 系统综述方案设计 |
| [prompts/meta-analysis-extraction.md](./prompts/meta-analysis-extraction.md) | Meta 分析数据提取 |
| [prompts/risk-of-bias-rct.md](./prompts/risk-of-bias-rct.md) | RCT 偏倚风险评估 |
| [prompts/peer-review-response.md](./prompts/peer-review-response.md) | 审稿意见回复草稿 |
| [prompts/research-gap-analysis.md](./prompts/research-gap-analysis.md) | 研究空白分析 |
| [examples/medical-literature-review-example.md](./examples/medical-literature-review-example.md) | 示例工作流 |
| [examples/diabetes-cardiovascular-review.md](./examples/diabetes-cardiovascular-review.md) | 糖尿病心血管结局综述示例 |
| [examples/oncology-immunotherapy-review.md](./examples/oncology-immunotherapy-review.md) | 肿瘤免疫治疗综述示例 |

## Recommended Workflow

1. 用 `pubmed-search.md` 把中文研究问题转换为检索词和 PubMed 检索式。
2. 在 PubMed、Suppr 或其他数据库中检索文献。
3. 用 `source-backed-summary.md` 提取每篇论文的研究对象、方法、结果和局限。
4. 用 `literature-review.md` 生成综述大纲和研究空白。
5. 人工核对引用、结论和证据等级。

Suppr 深度研究入口：https://suppr.wilddata.cn/deep-research

## Safety Notes

- 不要让 AI 编造引用。
- 每个关键观点都要回到 DOI、PMID、原文表格或指南原文核查。
- 综述初稿只能作为结构化阅读辅助，不应直接作为最终论文提交。
