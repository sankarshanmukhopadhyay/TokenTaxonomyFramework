# Schema Policy

The schemas in this directory document the v1.3.0 validation posture for Token Taxonomy Framework publication artifacts. They are intentionally incremental: existing legacy artifacts remain valid when they preserve the established TTF shape, while new and updated artifacts can adopt stronger governance metadata without breaking existing consumers.

## Schema Classes

| Schema | Scope |
|---|---|
| [`taxonomy-artifact.schema.json`](taxonomy-artifact.schema.json) | Base shape for TTF taxonomy artifacts that use an `artifact` object. |
| [`governance-metadata.schema.json`](governance-metadata.schema.json) | Optional v1.3.0 metadata for authority, lifecycle, enforcement, evidence, jurisdiction, custody, and rights. |
| [`dmrv-extension-package.schema.json`](dmrv-extension-package.schema.json) | Baseline shape for dMRV extension package JSON files. |

## Validation Approach

`scripts/validate_json.py --schema-policy` performs dependency-free schema-policy checks suitable for local shells and GitHub Actions. It verifies that:

- schema files are valid JSON Schema documents;
- taxonomy artifact JSON files expose either the legacy TTF artifact shape or a root taxonomy version object;
- v1.3.0 governance metadata, when present, uses recognized lifecycle and conformance values;
- dMRV extension package files are JSON objects or arrays and remain parseable publication artifacts.

The policy is designed to produce review evidence without converting this repository into an implementation-specific product registry.
