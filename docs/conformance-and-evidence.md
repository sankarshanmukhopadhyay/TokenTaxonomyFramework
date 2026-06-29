# Conformance and Evidence Guide

This repository is a publication surface for taxonomy artifacts. A conformant contribution should be understandable to reviewers, reusable by implementers, and checkable by machines.

## Conformance expectations

| Artifact class | Minimum expectation |
|---|---|
| JSON artifact | Parses as valid JSON and follows the relevant TTF or dMRV structure. |
| Schema-described artifact | Passes dependency-free schema-policy checks when `--schema-policy` is enabled. |
| Proto artifact | Is documented by the surrounding artifact or specification text. |
| Markdown documentation | Uses valid internal links and aligns with the current repository structure. |
| dMRV extension set | Includes deployment package, instance package, sample data or validation notes, and known limitations. |
| Generated catalog | Is regenerated whenever artifact inventory changes. |

## Evidence model

| Evidence | Producer | Purpose |
|---|---|---|
| JSON validation output | `scripts/validate_json.py` | Demonstrates machine-readable artifacts are parseable. |
| Schema-policy output | `scripts/validate_json.py --schema-policy` | Demonstrates schema files, artifact roots, optional governance metadata, and dMRV package shapes are checkable. |
| Link-check output | `scripts/check_internal_links.py` | Demonstrates GitHub Pages and repository navigation integrity. |
| Artifact-structure output | `scripts/check_artifact_structure.py` | Demonstrates required package files are present. |
| Catalog check output | `scripts/build_artifact_index.py --check` | Demonstrates human-facing indexes match repository contents. |
| Pull request checklist | Contributor | Captures scope, authority, review, and documentation assertions. |

## Authority, delegation, and scope

Artifact changes should make their authority chain explicit. A pull request should identify whether the change is:

- a framework-level taxonomy change;
- a workgroup-maintained artifact update;
- a dMRV extension-set contribution;
- a documentation-only clarification; or
- a generated catalog refresh.

A contribution should not imply endorsement by an issuing registry, verifier, supplier, methodology owner, or standards body unless that authority is documented in the artifact or accompanying documentation.

## Enforcement and revocation

Machine-verifiable checks enforce baseline repository integrity. They do not verify the economic, legal, scientific, or registry correctness of a methodology. Where an artifact is replaced, deprecated, or withdrawn, the change should be documented in `CHANGELOG.md` and the relevant artifact documentation. Deprecated artifacts should remain discoverable unless there is a legal or security reason to remove them.

Enforcement should be explicit about what is machine-checked and what remains a human or institutional review. For example, schema-policy checks can verify that an artifact declares a lifecycle state, but they cannot prove that an issuer has regulatory authorization. A dMRV package can be structurally complete while still requiring external scientific, registry, or verifier review.

## Assurance profiles

| Profile | Required evidence | Suitable use |
|---|---|---|
| Bronze | JSON parseability, valid internal links, artifact package structure, and current catalogs. | Drafts, examples, learning artifacts, and early-stage taxonomy contributions. |
| Silver | Bronze plus schema-policy checks, governance metadata, lifecycle state, authority statement, and documented evidence expectations. | Regulated-token designs, dMRV extension sets, tokenized-asset templates, and implementation-facing examples. |
| Gold | Silver plus external identifier references where applicable, independent review evidence, control-message or lifecycle-event test evidence, and migration/revocation notes. | Production-facing specifications, financial-asset tokenization, collateral workflows, registry-linked dMRV claims, and institutional integrations. |

## Authority, delegation, and scope checklist

| Question | Evidence location |
|---|---|
| Who controls the artifact definition? | `governanceMetadata.authority` or contribution rationale. |
| What authority is delegated to issuers, custodians, verifiers, registries, or operators? | `delegationScope`, extension-set documentation, or token template notes. |
| What is outside the artifact scope? | README, known limitations, or evidence notes. |
| Who can pause, revoke, supersede, or withdraw? | `lifecycle`, control-message documentation, and revocation notes. |
| What survives as an audit record? | `evidence.requiredEvidence`, validation report, or lifecycle event receipt. |

## Breaking changes

A change should be treated as breaking when it alters an artifact identifier, removes an expected field, changes semantics of an existing field, removes a proto message used by implementations, or changes extension-set package structure. Breaking changes should include migration notes and, where practical, compatibility examples.
