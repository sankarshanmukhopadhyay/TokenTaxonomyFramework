# Changelog

## Unreleased

## v1.3.0 - Tokenization Governance, Crosswalks, and Schema Policy

### Added

- Added GitHub Actions validation workflow for JSON, schema-policy, internal-link, artifact-structure, and generated-catalog checks.
- Added v1.3.0 tokenization landscape guide covering regulated RWAs, tokenized money, tokenized securities, collateral tokens, dMRV claims, stable-value tokens, and verifiable document/title tokens.
- Added crosswalks for ISO Digital Token Identifier, MiCA categories, IOSCO financial asset tokenization concerns, BIS tokenized money and unified-ledger concepts, ERC-3643 permissioned tokens, LEI/vLEI organizational identity, and lifecycle events.
- Added schema policy documentation and JSON Schema files for taxonomy artifacts, governance metadata, and dMRV extension package JSON.
- Added dependency-free `--schema-policy` validation mode to `scripts/validate_json.py`.
- Added v1.3.0 governance metadata guidance for authority, delegation, lifecycle, rights model, transfer controls, revocation, and evidence.
- Added Bronze, Silver, and Gold assurance profiles for artifact and extension-set review.
- Added regulated tokenization examples for permissioned RWA, tokenized bond, stable-value, dMRV claim, and verifiable document/title patterns.

### Changed

- Updated README navigation to include tokenization landscape, crosswalks, schema policy, and schema-policy validation.
- Updated contribution guidance to require stronger authority, lifecycle, revocation, and evidence documentation for regulated or evidence-sensitive artifacts.
- Updated dMRV documentation and extension-set checklist with methodology authority, verifier role, measurement boundary, double-counting, registry dependency, revocation, and auditability expectations.
- Updated validation documentation and validation report format to include schema-policy evidence and assurance interpretation.

### Fixed

- Added the missing `.github/workflows/validate.yml` file referenced by existing validation documentation.
- Restored internal-link validation to a clean state with no broken local Markdown links.

### Validation

- `python scripts/validate_json.py`
- `python scripts/validate_json.py --schema-policy`
- `python scripts/check_internal_links.py`
- `python scripts/check_artifact_structure.py`
- `python scripts/build_artifact_index.py --check`

### Added

- Added repository validation scripts for JSON parsing, internal Markdown links, artifact package structure, and generated catalog freshness.
- Added GitHub Actions validation workflow for pushes and pull requests.
- Added documentation index, artifact catalog, token template catalog, dMRV extension catalog, validation guide, and conformance/evidence guide.
- Added contributor governance files, support guidance, security guidance, and pull request checklist.
- Added example documentation for minimal token artifacts, dMRV extension sets, and validation evidence reports.

### Changed

- Refreshed the root README to provide durable navigation, adoption guidance, validation commands, and dMRV positioning.
- Refreshed dMRV documentation to align links with the current repository layout.
- Improved dMRV extension documentation with explicit package requirements and validation expectations.

### Fixed

- Fixed invalid JSON in dMRV sample files and the VRE-PARFE-HydroRE variable template package.
- Replaced stale or broken documentation references with current repository paths.
