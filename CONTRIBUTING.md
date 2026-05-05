# Contributing to the Token Taxonomy Framework

Thank you for contributing. This repository publishes taxonomy documentation, machine-readable artifacts, proto definitions, dMRV samples, and extension-set packages. Contributions should be clear to human reviewers and safe for automated consumers.

## Contribution types

| Type | Examples | Required evidence |
|---|---|---|
| Documentation | README, specification text, guides, examples | Link check and reviewer rationale. |
| Taxonomy artifact | JSON artifact, token template, behavior, property set | JSON validation, catalog regeneration, documentation update. |
| Proto/control message | `.proto` file or control-message documentation | Documentation update and compatibility note. |
| dMRV extension set | Deployment package, instance package, samples | Package-structure check, JSON validation, known limitations. |
| Governance/maintenance | CI, scripts, contribution docs | Validation output and maintenance rationale. |

## Required local checks

Run these commands before opening a pull request:

```bash
python scripts/validate_json.py
python scripts/check_internal_links.py
python scripts/check_artifact_structure.py
python scripts/build_artifact_index.py --check
```

If artifact inventory changed, regenerate catalogs first:

```bash
python scripts/build_artifact_index.py
```

## Artifact governance

Artifact changes should clearly state:

- the scope of the change;
- the authority or workgroup responsible for the artifact;
- whether the change is additive, corrective, deprecated, or breaking;
- whether downstream implementers need migration guidance;
- what validation evidence was produced.

## dMRV extension-set submissions

A dMRV extension-set contribution should include:

```text
DeploymentPackage/
  ExtensionSet.json
  EntityExtensionTemplates.json
  FormulaTemplates.json
  MessagePairs.json
  VariableTemplates.json
  protos/
InstancePackage/
  AimFixedVariables.json
  ClaimSources.json
GettingStarted.md or README.md
```

The repository validation scripts check for the minimum package shape. They do not verify the scientific, registry, economic, or legal correctness of methodology content. Contributors remain responsible for documenting methodology assumptions, registry dependencies, and review limitations.

## Documentation expectations

- Use repository-relative links for local files.
- Keep GitHub Pages compatibility intact.
- Update README or docs when changing user-facing structure.
- Avoid stale language such as temporary “new” markers unless tied to a release note.

## Pull request review

A pull request should be reviewable as an executable governance change: reviewers should be able to determine what authority is being exercised, what artifact scope is affected, what checks enforce the change, and what evidence remains after merge.
