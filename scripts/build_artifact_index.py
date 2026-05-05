#!/usr/bin/env python3
"""Build deterministic Markdown catalogs for taxonomy artifacts and dMRV extensions."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

CATALOG_PATH = Path("docs/artifact-catalog.md")
TEMPLATE_CATALOG_PATH = Path("docs/token-template-catalog.md")
DMRV_CATALOG_PATH = Path("docs/dmrv-extension-catalog.md")


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def list_files(root: Path, suffixes: tuple[str, ...]) -> list[Path]:
    if not root.exists():
        return []
    return sorted(path for path in root.rglob("*") if path.is_file() and path.suffix.lower() in suffixes)


def markdown_table(rows: list[tuple[str, str, str]]) -> str:
    if not rows:
        return "| Item | Type | Path |\n|---|---|---|\n| _None found_ |  |  |\n"
    lines = ["| Item | Type | Path |", "|---|---|---|"]
    for item, kind, path in rows:
        safe_item = item.replace("|", "\\|")
        lines.append(f"| {safe_item} | {kind} | `{path}` |")
    return "\n".join(lines) + "\n"


def artifact_name(path: Path) -> str:
    try:
        data = load_json(path)
    except Exception:
        return path.stem
    if isinstance(data, dict):
        for key in ("name", "symbol", "id", "type"):
            value = data.get(key)
            if isinstance(value, str) and value.strip():
                return value.strip()
    return path.stem


def build_artifact_catalog(root: Path) -> str:
    rows = []
    for path in list_files(root / "artifacts", (".json", ".proto")):
        if path.name in {"Taxonomy.json", "FormulaGrammar.json"}:
            kind = "taxonomy-root"
        elif path.suffix == ".proto":
            kind = "proto"
        else:
            kind = path.parent.name
        rows.append((artifact_name(path) if path.suffix == ".json" else path.stem, kind, path.relative_to(root).as_posix()))
    return f"""# Artifact Catalog

This catalog is generated from repository contents by `scripts/build_artifact_index.py`. It gives maintainers and adopters a deterministic view of the machine-readable taxonomy publication surface.

{markdown_table(rows)}"""


def build_template_catalog(root: Path) -> str:
    rows = []
    for path in list_files(root / "artifacts", (".json",)):
        if any(part.lower() in {"template", "templates", "token-templates"} for part in path.parts):
            rows.append((artifact_name(path), "token-template", path.relative_to(root).as_posix()))
    if not rows:
        for path in list_files(root / "artifacts", (".json",)):
            rows.append((artifact_name(path), "artifact-json", path.relative_to(root).as_posix()))
    return f"""# Token Template Catalog

This catalog provides a developer-facing index of JSON artifacts that can be used while composing token templates, formulas, definitions, and specifications.

{markdown_table(rows)}"""


def build_dmrv_catalog(root: Path) -> str:
    rows = []
    ext_root = root / "dmrv" / "extensions"
    if ext_root.exists():
        for extension in sorted(path for path in ext_root.iterdir() if path.is_dir()):
            for package in ["DeploymentPackage", "InstancePackage"]:
                package_path = extension / package
                for path in list_files(package_path, (".json", ".proto")):
                    rows.append((extension.name, package, path.relative_to(root).as_posix()))
    return f"""# dMRV Extension Catalog

This catalog indexes dMRV extension-set packages. Extension sets are treated as reusable governance artifacts: they register methodology-specific entity extensions, formulas, variables, messages, and instance bindings.

{markdown_table(rows)}"""


def write_or_check(path: Path, content: str, check: bool) -> bool:
    if check:
        return path.exists() and path.read_text(encoding="utf-8") == content
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Build artifact catalog docs")
    parser.add_argument("--root", default=".")
    parser.add_argument("--check", action="store_true", help="Fail if generated catalogs are stale")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    outputs = {
        CATALOG_PATH: build_artifact_catalog(root),
        TEMPLATE_CATALOG_PATH: build_template_catalog(root),
        DMRV_CATALOG_PATH: build_dmrv_catalog(root),
    }
    stale = []
    for rel, content in outputs.items():
        if not write_or_check(root / rel, content, args.check):
            stale.append(rel.as_posix())
    if stale:
        print("Generated catalog files are stale:")
        for path in stale:
            print(f"- {path}")
        print("Run: python scripts/build_artifact_index.py")
        return 1
    if args.check:
        print("Generated catalogs are current")
    else:
        print("Generated catalogs updated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
