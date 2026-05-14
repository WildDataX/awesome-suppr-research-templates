from __future__ import annotations

import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOWNLOADS = ROOT / "downloads"
PACKS = {
    "literature-review-prompts": "suppr-literature-review-prompts.zip",
    "medical-translation-glossary": "suppr-medical-translation-glossary.zip",
    "research-topic-planner": "suppr-research-topic-planner.zip",
    "zotero-research-workflow": "suppr-zotero-research-workflow.zip",
    "academic-writing-templates": "suppr-academic-writing-templates.zip",
}


def build_zip(source_dir: Path, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(source_dir.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(source_dir))


def main() -> None:
    for pack, zip_name in PACKS.items():
        build_zip(ROOT / pack, DOWNLOADS / zip_name)
        print(f"built {DOWNLOADS / zip_name}")


if __name__ == "__main__":
    main()
