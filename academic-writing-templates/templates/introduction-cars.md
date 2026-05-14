# 引言 CARS 结构模板

CARS = Create A Research Space，适合把引言写成“领域重要性 -> 现有不足 -> 本研究贡献”的结构。

## Move 1: Establish A Territory

- 研究领域为什么重要？
- 临床、公共卫生、基础研究或方法学意义是什么？
- 有哪些高质量指南、综述或代表性研究可以引用？

示例句：

```text
{Topic} remains a major challenge in {field}, particularly among {population}.
Prior studies have shown that {known finding}, suggesting that {mechanism or implication}.
```

## Move 2: Establish A Niche

- 现有研究缺什么？
- 是人群不足、随访不足、结局不足、方法不足，还是真实世界证据不足？
- 注意不要夸大“完全没人做过”。

示例句：

```text
However, evidence remains limited regarding {specific gap}.
Most existing studies have focused on {known area}, while {understudied area} has received less attention.
```

## Move 3: Occupy The Niche

- 本研究要回答什么问题？
- 使用什么数据或方法？
- 预期贡献是什么？

示例句：

```text
Therefore, we aimed to evaluate {research question} using {data/source/design}.
This study may help clarify {specific contribution} and inform {practice or future research}.
```

## Suppr Prompt

```text
请基于下面的研究问题和证据，按 CARS 结构生成引言大纲。

要求：
1. 分成领域重要性、现有不足、本研究目的三部分。
2. 每个关键判断后标注需要引用的文献类型。
3. 不要编造 DOI、PMID 或作者名。
4. 输出 3 个不同写作角度，供作者选择。

研究问题：
{粘贴研究问题}

已知证据：
{粘贴文献摘要或 Suppr 深度研究结果}
```

