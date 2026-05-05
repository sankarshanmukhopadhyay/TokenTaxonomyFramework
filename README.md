# Token Taxonomy Framework

©2026 InterWork Alliance Inc. ("IWA"). All Rights Reserved. This GitHub repository has been set up to provide information to the public. Use of the information in this repository is subject to the terms of the agreement in the [LICENSE](LICENSE) file.

[View this site as a web page.](https://interwork-alliance.github.io/TokenTaxonomyFramework/)

## What this repository provides

The Token Taxonomy Framework (TTF) repository is a standards and artifact publication surface for designing, composing, documenting, and validating token specifications. It combines explanatory documentation with machine-readable artifacts so token designers, standards authors, implementers, and assurance teams can work from the same vocabulary and reusable artifact library.

The repository provides:

- A conceptual taxonomy for token construction and classification.
- A taxonomy object model for tool builders and implementers.
- A machine-readable artifact format for base token types, behaviors, behavior groups, property sets, formulas, definitions, and specifications.
- Protocol buffer models and control-message documentation for implementation-facing workflows.
- A Digital Measurement, Reporting and Verification (dMRV) workspace for business-process and ecological-market use cases.
- Validation scripts and generated catalogs that make the artifact library easier to inspect, test, and publish.

## Who should use this repository

| Audience | Primary use |
|---|---|
| Standards authors | Define reusable token concepts, artifact structures, and extension patterns. |
| Developers | Consume JSON and proto artifacts in tools, services, or token design workflows. |
| Business architects | Understand how token definitions become implementation-ready specifications. |
| Assurance and conformance teams | Validate artifact integrity, trace documentation coverage, and review dMRV extension packages. |
| dMRV participants | Model methodology-specific variables, formulas, messages, and claim evidence. |

## Repository map

| Area | Purpose |
|---|---|
| [`token-taxonomy.md`](token-taxonomy.md) | Taxonomy overview, syntax, and token classification concepts. |
| [`taxonomy-model.md`](taxonomy-model.md) | Technical overview of the taxonomy object model. |
| [`logicalIM.md`](logicalIM.md) | Logical information model reference. |
| [`taxonomy-artifact-format.md`](taxonomy-artifact-format.md) | Artifact representation and authoring rules. |
| [`token-control-messages.md`](token-control-messages.md) | Control-message model for implementation and certification workflows. |
| [`artifacts/`](artifacts/) | Machine-readable taxonomy artifacts and proto definitions. |
| [`dmrv/`](dmrv/readme.md) | Digital MRV standards workspace, samples, protos, and extension sets. |
| [`docs/`](docs/index.md) | Generated catalogs, validation guidance, and conformance/evidence notes. |
| [`scripts/`](scripts/) | Local and CI validation utilities. |
| [`examples/`](examples/README.md) | Minimal adoption examples and validation-report patterns. |

## Core concepts

TTF treats a token specification as a composition of reusable artifacts. A token is not only named in prose; it is described through a structured artifact set that can be reviewed, reused, rendered, and validated. This allows implementers to move from policy and business-language definitions toward concrete machine-readable specifications.

The key design principle is that taxonomy artifacts should be understandable by humans and checkable by machines. Documentation explains intent and context. JSON and proto files provide implementation-grade structure. Validation scripts create evidence that the repository remains parseable and internally navigable.

## dMRV workspace

The [Digital Measurement, Reporting and Verification workspace](dmrv/readme.md) applies the TTF publication pattern to ecological-market and sustainability workflows. It contains token schemas, sample data, protocol buffer definitions, OpenAPI material, and extension-set examples.

dMRV extension sets allow methodology-specific variables, formulas, entity extensions, and message pairs to be packaged as reusable artifacts. This is especially useful when a quality standard, registry, verifier, or supplier needs to express the evidence requirements behind a claim or crediting process.

## Validation and quality checks

Run the validation suite locally before opening a pull request:

```bash
python scripts/validate_json.py
python scripts/check_internal_links.py
python scripts/check_artifact_structure.py
python scripts/build_artifact_index.py --check
```

To regenerate catalogs after artifact inventory changes:

```bash
python scripts/build_artifact_index.py
```

The GitHub Actions workflow in [`.github/workflows/validate.yml`](.github/workflows/validate.yml) runs the same checks on pushes and pull requests.

## Catalogs and assurance documentation

- [Documentation index](docs/index.md)
- [Artifact catalog](docs/artifact-catalog.md)
- [Token template catalog](docs/token-template-catalog.md)
- [dMRV extension catalog](docs/dmrv-extension-catalog.md)
- [Validation guide](docs/validation.md)
- [Conformance and evidence guide](docs/conformance-and-evidence.md)

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes. Artifact changes should include validation evidence and documentation updates. dMRV extension submissions should include a deployment package, an instance package, sample data or validation notes, and known limitations.

## Legal notices

Welcome to the InterWork Alliance (“IWA”). By accessing or using this GitHub repository, you agree to abide by the terms of the agreement in the [LICENSE](LICENSE) file.
