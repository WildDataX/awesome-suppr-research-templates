# 结构式摘要模板

## Background

- 研究背景：
- 现有证据缺口：
- 本研究目的：

## Methods

- 研究设计：
- 数据来源/研究对象：
- 暴露、干预或核心变量：
- 主要结局：
- 统计方法：

## Results

- 样本量：
- 主要发现：
- 效应量与置信区间：
- 敏感性分析或亚组结果：

## Conclusions

- 结论只写本研究数据能够支持的内容。
- 避免把相关性写成因果性。
- 避免使用 "prove", "definitively", "revolutionary" 等过度确定词。

## Suppr Prompt

```text
请根据下面的研究材料，生成一版结构式英文摘要草稿。

要求：
1. 分为 Background, Methods, Results, Conclusions。
2. 只使用我提供的信息，不补造样本量、P 值、置信区间或结论。
3. Results 中优先呈现定量结果。
4. Conclusions 保持克制，说明适用边界。
5. 输出后列出“需要作者补充核对的信息”。

研究材料：
{粘贴研究设计、样本、主要结果和结论}
```

