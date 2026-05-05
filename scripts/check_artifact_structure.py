#!/usr/bin/env python3
"""Validate minimum structure for taxonomy and dMRV artifact packages."""
from __future__ import annotations

import argparse
from pathlib import Path

REQUIRED_EXTENSION_DEPLOYMENT_FILES = {
    "ExtensionSet.json",
    "EntityExtensionTemplates.json",
    "FormulaTemplates.json",
    "MessagePairs.json",
    "VariableTemplates.json",
}
REQUIRED_EXTENSION_INSTANCE_FILES = {"AimFixedVariables.json", "ClaimSources.json"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Check repository artifact package structure")
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    failures: list[str] = []

    artifacts = root / "artifacts"
    if not artifacts.exists():
        failures.append("Missing artifacts/ directory")
    else:
        for required in ["Taxonomy.json", "FormulaGrammar.json", "Readme.md", "base/base.json", "base/tokens.proto"]:
            if not (artifacts / required).exists():
                failures.append(f"Missing artifacts/{required}")

    ext_root = root / "dmrv" / "extensions"
    if ext_root.exists():
        for extension in sorted(path for path in ext_root.iterdir() if path.is_dir()):
            deployment = extension / "DeploymentPackage"
            instance = extension / "InstancePackage"
            for filename in REQUIRED_EXTENSION_DEPLOYMENT_FILES:
                if not (deployment / filename).exists():
                    failures.append(f"{extension.relative_to(root)} missing DeploymentPackage/{filename}")
            for filename in REQUIRED_EXTENSION_INSTANCE_FILES:
                if not (instance / filename).exists():
                    failures.append(f"{extension.relative_to(root)} missing InstancePackage/{filename}")
            if not (extension / "GettingStarted.md").exists() and not (extension / "README.md").exists():
                failures.append(f"{extension.relative_to(root)} missing GettingStarted.md or README.md")
    else:
        failures.append("Missing dmrv/extensions/ directory")

    if failures:
        print("Artifact structure check failed")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("Artifact structure check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
