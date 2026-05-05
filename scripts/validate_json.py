#!/usr/bin/env python3
"""Validate every JSON artifact in the repository.

The Token Taxonomy Framework is consumed as a standards and artifact
repository. Invalid JSON is therefore not a formatting problem; it breaks the
machine-verifiable publication surface. This script intentionally has no third
party dependencies so it can run in GitHub Actions and local developer shells.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

DEFAULT_EXCLUDES = {".git", "node_modules", "vendor", "_site"}


def iter_json_files(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*.json")):
        if any(part in DEFAULT_EXCLUDES for part in path.parts):
            continue
        yield path


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate repository JSON files")
    parser.add_argument("--root", default=".", help="Repository root. Defaults to current directory.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    failures: list[tuple[Path, str]] = []
    count = 0

    for path in iter_json_files(root):
        count += 1
        try:
            with path.open("r", encoding="utf-8") as handle:
                json.load(handle)
        except Exception as exc:  # noqa: BLE001 - produce deterministic CLI report
            failures.append((path.relative_to(root), str(exc)))

    if failures:
        print(f"Validated {count} JSON files")
        print(f"Invalid JSON files: {len(failures)}")
        for path, error in failures:
            print(f"- {path}: {error}")
        return 1

    print(f"Validated {count} JSON files")
    print("Invalid JSON files: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
