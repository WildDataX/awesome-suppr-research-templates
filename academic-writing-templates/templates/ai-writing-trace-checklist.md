# AI 写作痕迹自查表

这个清单用于检查论文草稿是否出现“空泛、过度平滑、证据不足”的 AI 写作痕迹。目标不是伪装，而是让稿件更真实、更可核查、更符合学术写作要求。

## High-Risk Patterns

| 风险 | 例子 | 修改方式 |
| --- | --- | --- |
| 空泛评价 | plays a crucial role, significant impact | 换成具体机制、指标或研究场景 |
| 过度承诺 | prove, undoubtedly, revolutionary | 改成 may, suggest, was associated with |
| 无来源判断 | widely recognized, many studies show | 补具体引用或删除 |
| 逻辑跳跃 | 从相关性直接写临床建议 | 加研究设计边界 |
| 重复句式 | 每段都用 However/Moreover 开头 | 按论证关系重写 |
| 术语不一致 | 同一变量多种译法 | 用术语表统一 |

## Sentence-Level Review

- 每段第一句是否有明确功能？
- 每个结论是否能回到表、图或引用？
- 是否存在没有主语的抽象判断？
- 是否把研究背景写得过于宏大？
- 是否把局限性写成模板化免责声明？

## Evidence Check

| Claim | Evidence source | Needs citation? | Revision |
| --- | --- | --- | --- |
|  |  |  |  |

## Suppr Prompt

```text
请检查下面这段学术写作是否存在空泛、过度承诺、证据不足或 AI 腔问题。

要求：
1. 不要只给泛泛建议，要逐句指出问题。
2. 对每个问题给出修改版本。
3. 标注哪些句子需要补引用。
4. 保留作者原意，不要扩写成新的结论。

文本：
{粘贴段落}
```

