from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BACKLOG_FILE = ROOT / "data" / "update_backlog.json"


GENERATORS = {
    "daily-glossary-imaging-terms": lambda: (
        "medical-translation-glossary/data/imaging-terms.csv",
        "English,Chinese,Notes\n"
        "computed tomography,计算机断层扫描,缩写 CT\n"
        "magnetic resonance imaging,磁共振成像,缩写 MRI\n"
        "ultrasound,超声,\n"
        "contrast-enhanced imaging,增强成像,\n"
        "radiomics,影像组学,\n"
        "lesion segmentation,病灶分割,\n"
        "sensitivity,敏感度,影像诊断中也常用\n"
        "specificity,特异度,影像诊断中也常用\n",
    ),
    "daily-prompt-guideline-summary": lambda: (
        "literature-review-prompts/prompts/guideline-summary.md",
        "# 临床指南摘要 Prompt\n\n"
        "```text\n"
        "你是一名临床指南阅读助手。请基于我提供的指南原文片段，提取推荐意见、证据等级和适用人群。\n\n"
        "指南内容：\n{粘贴指南片段}\n\n"
        "请输出：\n"
        "1. 推荐意见原文摘要。\n"
        "2. 推荐强度和证据等级。\n"
        "3. 适用人群。\n"
        "4. 不适用或需谨慎的人群。\n"
        "5. 与既往指南相比的变化。\n"
        "6. 需要回原文核查的表格或脚注。\n\n"
        "要求：不要把指南建议扩展到未覆盖人群；不要生成指南中不存在的推荐等级。\n"
        "```\n",
    ),
    "daily-template-manuscript-outline": lambda: (
        "research-topic-planner/templates/manuscript-outline.md",
        "# 医学论文大纲模板\n\n"
        "## Title\n\n-\n\n"
        "## Abstract\n\n- Background:\n- Methods:\n- Results:\n- Conclusions:\n\n"
        "## Introduction\n\n1. 研究背景\n2. 未解决问题\n3. 本研究目的\n\n"
        "## Methods\n\n1. Study design\n2. Participants\n3. Exposure/intervention\n4. Outcomes\n5. Statistical analysis\n\n"
        "## Results\n\n1. Baseline characteristics\n2. Primary outcome\n3. Secondary outcomes\n4. Sensitivity/subgroup analyses\n\n"
        "## Discussion\n\n1. Principal findings\n2. Comparison with prior studies\n3. Strengths and limitations\n4. Implications\n\n",
    ),
    "weekly-example-public-health": lambda: (
        "literature-review-prompts/examples/public-health-screening-review.md",
        "# 示例：公共卫生筛查综述\n\n"
        "## 研究问题\n\n社区筛查项目能否提高慢性病早期发现率并改善长期结局？\n\n"
        "## PICO\n\n| 元素 | 内容 |\n| --- | --- |\n| P | 社区成年人群 |\n| I | 慢性病筛查项目 |\n| C | 常规照护或无筛查 |\n| O | 早期发现率、治疗启动率、长期并发症、成本效果 |\n\n"
        "## 写作提醒\n\n- 区分筛查准确性、筛查覆盖率和长期健康结局。\n"
        "- 注意 lead-time bias 和 overdiagnosis。\n"
        "- 成本效果和资源可及性应单独讨论。\n",
    ),
    "weekly-zotero-systematic-review-workflow": lambda: (
        "zotero-research-workflow/templates/systematic-review-workflow.md",
        "# Zotero 系统综述工作流\n\n"
        "1. 建立 collection：`01-imported`, `02-screen-title-abstract`, `03-full-text`, `04-included`, `05-excluded`。\n"
        "2. 用 tags 标记排除原因：`exclude/population`, `exclude/intervention`, `exclude/outcome`, `exclude/design`。\n"
        "3. 对纳入文献添加研究设计和证据等级标签。\n"
        "4. 用 notes 保存数据提取表和偏倚风险判断。\n"
        "5. 导出 included collection 用于参考文献管理。\n",
    ),
}


def read_backlog() -> dict:
    return json.loads(BACKLOG_FILE.read_text(encoding="utf-8-sig"))


def write_backlog(data: dict) -> None:
    BACKLOG_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def apply_task(task: dict) -> dict:
    generator = GENERATORS.get(task["id"])
    if not generator:
        return {**task, "result": "no_generator"}
    rel_path, content = generator()
    path = ROOT / rel_path
    if path.exists():
        return {**task, "result": "exists"}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    task["status"] = "done"
    task["completed_at"] = dt.date.today().isoformat()
    return {**task, "result": "created", "path": rel_path}


def main() -> None:
    parser = argparse.ArgumentParser(description="Apply small reviewed resource updates from backlog.")
    parser.add_argument("--mode", choices=["daily", "weekly", "monthly"], default="daily")
    parser.add_argument("--limit", type=int, default=3)
    args = parser.parse_args()

    backlog = read_backlog()
    results = []
    changed = False
    for task in backlog.get(args.mode, []):
        if task.get("status") != "pending":
            continue
        result = apply_task(task)
        results.append(result)
        if result.get("result") == "created":
            task.update({"status": "done", "completed_at": result["completed_at"]})
            changed = True
        if len(results) >= args.limit:
            break
    if changed:
        write_backlog(backlog)

    run_dir = ROOT / "runs" / dt.date.today().isoformat()
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / f"{args.mode}_update_report.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"mode": args.mode, "selected": len(results), "results": results}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
