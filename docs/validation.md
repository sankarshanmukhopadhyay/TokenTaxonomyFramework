# Validation Guide

The repository contains machine-readable standards artifacts. Validation is therefore part of the governance model: it produces evidence that published artifacts are parseable, navigable, and structurally complete.

## Local validation

Run all checks from the repository root:

```bash
python scripts/validate_json.py
python scripts/check_internal_links.py
python scripts/check_artifact_structure.py
python scripts/build_artifact_index.py --check
```

## Checks

| Script | Evidence produced | Failure condition |
|---|---|---|
| `scripts/validate_json.py` | Count of valid and invalid JSON files. | Any `.json` file cannot be parsed. |
| `scripts/check_internal_links.py` | Count of local Markdown links checked. | Any local Markdown link points to a missing file or leaves the repository. |
| `scripts/check_artifact_structure.py` | Pass/fail report for required artifact package files. | Required root artifacts or dMRV package files are missing. |
| `scripts/build_artifact_index.py --check` | Confirmation that generated catalogs are current. | Catalog content differs from repository inventory. |

## Regenerating catalogs

After adding, removing, or moving artifacts, regenerate the catalogs:

```bash
python scripts/build_artifact_index.py
```

Commit the updated files under `docs/` with the artifact change.

## CI enforcement

The workflow in [`../.github/workflows/validate.yml`](../.github/workflows/validate.yml) runs the same checks on pushes and pull requests. Maintainers should treat a green validation run as the minimum evidence required before merging artifact or documentation changes.
