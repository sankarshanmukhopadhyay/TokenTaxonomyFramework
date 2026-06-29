# Validation Report

This report records the local validation evidence for the `v1.3.0 - Tokenization Governance, Crosswalks, and Schema Policy` release.

## Commands executed

```bash
python scripts/validate_json.py
python scripts/validate_json.py --schema-policy
python scripts/check_internal_links.py
python scripts/check_artifact_structure.py
python scripts/build_artifact_index.py --check
```

## Result

```text
Validated 153 JSON files
Invalid JSON files: 0
Schema policy failures: 0
Checked 101 local Markdown links
Broken local links: 0
Artifact structure check passed
Generated catalogs are current
```

## Interpretation

The repository has a machine-verifiable evidence set for artifact integrity, schema-policy conformance, documentation navigation, dMRV extension package completeness, and generated catalog freshness.

This evidence does not certify legal, regulatory, economic, scientific, registry, reserve, or issuer-authority correctness. Those claims require the authority and evidence review described in [`conformance-and-evidence.md`](conformance-and-evidence.md).
