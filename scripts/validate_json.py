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


def is_artifact_json(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    return rel.parts[:1] == ("artifacts",)


def is_dmrv_extension_json(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    return len(rel.parts) >= 4 and rel.parts[:2] == ("dmrv", "extensions") and rel.parts[-2] in {
        "DeploymentPackage",
        "InstancePackage",
    }


def validate_governance_metadata(path: Path, data: object) -> list[str]:
    if not isinstance(data, dict) or "governanceMetadata" not in data:
        return []
    metadata = data.get("governanceMetadata")
    if not isinstance(metadata, dict):
        return ["governanceMetadata must be an object when present"]
    failures: list[str] = []
    lifecycle = metadata.get("lifecycle")
    if lifecycle is not None:
        if not isinstance(lifecycle, dict):
            failures.append("governanceMetadata.lifecycle must be an object")
        else:
            state = lifecycle.get("state")
            if state not in {None, "draft", "active", "deprecated", "superseded", "withdrawn"}:
                failures.append("governanceMetadata.lifecycle.state must be draft, active, deprecated, superseded, or withdrawn")
    evidence = metadata.get("evidence")
    if evidence is not None:
        if not isinstance(evidence, dict):
            failures.append("governanceMetadata.evidence must be an object")
        else:
            level = evidence.get("conformanceLevel")
            if level not in {None, "bronze", "silver", "gold"}:
                failures.append("governanceMetadata.evidence.conformanceLevel must be bronze, silver, or gold")
    return failures


def validate_schema_policy(root: Path, path: Path, data: object) -> list[str]:
    rel = path.relative_to(root)
    failures: list[str] = []
    if rel.parts[:1] == ("schemas",):
        if not isinstance(data, dict):
            failures.append("schema file must be a JSON object")
        elif "$schema" not in data or "title" not in data:
            failures.append("schema file must include $schema and title")
        return failures
    if is_artifact_json(path, root):
        if not isinstance(data, dict):
            failures.append("artifact JSON must be an object")
        elif "artifact" not in data and "version" not in data and "singleTokenGrammar" not in data:
            failures.append("artifact JSON must include artifact, version, or singleTokenGrammar root object")
        failures.extend(validate_governance_metadata(path, data))
    if is_dmrv_extension_json(path, root) and not isinstance(data, (dict, list)):
        failures.append("dMRV extension package JSON must be an object or array")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate repository JSON files")
    parser.add_argument("--root", default=".", help="Repository root. Defaults to current directory.")
    parser.add_argument(
        "--schema-policy",
        action="store_true",
        help="Run dependency-free schema-policy checks in addition to JSON parsing.",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    failures: list[tuple[Path, str]] = []
    policy_failures: list[tuple[Path, str]] = []
    count = 0

    for path in iter_json_files(root):
        count += 1
        try:
            with path.open("r", encoding="utf-8") as handle:
                data = json.load(handle)
        except Exception as exc:  # noqa: BLE001 - produce deterministic CLI report
            failures.append((path.relative_to(root), str(exc)))
            continue
        if args.schema_policy:
            for error in validate_schema_policy(root, path, data):
                policy_failures.append((path.relative_to(root), error))

    if failures or policy_failures:
        print(f"Validated {count} JSON files")
        print(f"Invalid JSON files: {len(failures)}")
        for path, error in failures:
            print(f"- {path}: {error}")
        if args.schema_policy:
            print(f"Schema policy failures: {len(policy_failures)}")
            for path, error in policy_failures:
                print(f"- {path}: {error}")
        return 1

    print(f"Validated {count} JSON files")
    print("Invalid JSON files: 0")
    if args.schema_policy:
        print("Schema policy failures: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
