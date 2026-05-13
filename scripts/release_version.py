from __future__ import annotations

import argparse
import json
import re
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPO = "WildDataX/awesome-suppr-research-templates"


def load_token() -> str:
    env_path = next((p / ".env.local" for p in [ROOT, *ROOT.parents] if (p / ".env.local").exists()), None)
    if not env_path:
        raise RuntimeError(".env.local not found")
    text = env_path.read_text(encoding="utf-8-sig")
    match = re.search(r"^\s*SUPPR_TEMPLATE_REPO_TOKEN\s*=\s*(.+?)\s*$", text, re.M)
    if not match:
        raise RuntimeError("SUPPR_TEMPLATE_REPO_TOKEN not found")
    return match.group(1).strip().strip('"').strip("'")


def request(method: str, url: str, token: str, payload=None, content_type="application/json; charset=utf-8"):
    data = None
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "suppr-template-release",
    }
    if payload is not None:
        data = payload if isinstance(payload, (bytes, bytearray)) else json.dumps(payload, ensure_ascii=False).encode("utf-8")
        headers["Content-Type"] = content_type
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        with opener.open(req, timeout=60) as response:
            text = response.read().decode("utf-8")
            return json.loads(text) if text else None
    except urllib.error.HTTPError as exc:
        text = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"{method} {url} failed {exc.code}: {text}") from exc


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a GitHub release and upload ZIP assets.")
    parser.add_argument("--version", required=True)
    parser.add_argument("--notes", default="")
    args = parser.parse_args()

    token = load_token()
    notes_path = ROOT / (args.notes or f"RELEASE_NOTES_{args.version}.md")
    body = notes_path.read_text(encoding="utf-8") if notes_path.exists() else f"Release {args.version}"
    tag = args.version if args.version.startswith("v") else f"v{args.version}"

    try:
        release = request("GET", f"https://api.github.com/repos/{REPO}/releases/tags/{tag}", token)
    except RuntimeError as exc:
        if "failed 404" not in str(exc):
            raise
        release = request("POST", f"https://api.github.com/repos/{REPO}/releases", token, {
            "tag_name": tag,
            "target_commitish": "main",
            "name": f"{tag} - Suppr Research Templates",
            "body": body,
            "draft": False,
            "prerelease": False,
        })

    existing = {asset["name"]: asset for asset in release.get("assets", [])}
    upload_base = release["upload_url"].split("{", 1)[0]
    uploaded = []
    for asset in sorted((ROOT / "downloads").glob("*.zip")):
        if asset.name in existing:
            uploaded.append({"name": asset.name, "status": "exists", "url": existing[asset.name]["browser_download_url"]})
            continue
        url = upload_base + "?name=" + urllib.parse.quote(asset.name)
        result = request("POST", url, token, asset.read_bytes(), "application/zip")
        uploaded.append({"name": result["name"], "status": "uploaded", "url": result["browser_download_url"]})

    print(json.dumps({"release": release["html_url"], "assets": uploaded}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
