# Digital Measurement, Reporting and Verification Workspace

The Digital Measurement, Reporting and Verification (dMRV) workspace applies the Token Taxonomy Framework publication model to ecological-market and sustainability workflows. It documents process-level token schemas, sample data, protocol buffers, OpenAPI material, and methodology-specific extension sets.

The core purpose of this workspace is to move beyond a single token definition and describe how multiple parties, claims, measurements, validations, and verification artifacts relate to one another within a business process.

## Publication pattern

The workspace follows the same general pattern used by standards-oriented publication repositories:

- an overview and documentation layer for business and technical readers;
- protocol buffer definitions for implementation-facing models;
- JSON sample data for testability and illustration;
- OpenAPI material for API-oriented consumption;
- extension-set packages for methodology-specific variables, formulas, entity extensions, and message pairs.

## dMRV technical specification

- [Current v3.0 specification](https://interworkalliance.github.io/TokenTaxonomyFramework/dmrv/spec/index.html)
- [Previous v2 specification](https://interworkalliance.github.io/TokenTaxonomyFramework/dmrv/spec/v2/index.html)

## Token schemas and protocol buffers

The dMRV token and contract schemas are initially defined with Protocol Buffers and then represented through JSON samples and generated documentation.

| File | Purpose |
|---|---|
| [`protos/sustainability.proto`](protos/sustainability.proto) | Sustainability and dMRV domain messages. |
| [`protos/common.proto`](protos/common.proto) | Common data structures. |
| [`protos/dmrv.proto`](protos/dmrv.proto) | dMRV process messages. |
| [`protos/buildMrvModel.sh`](protos/buildMrvModel.sh) | Helper script for rebuilding model outputs where the required toolchain is available. |

## Token instance data samples

The [`spec/samples/`](spec/samples/) directory contains JSON sample data for dMRV token schemas. These samples are used as implementation examples and as repository validation inputs.

The [`spec/v2/samples/`](spec/v2/samples/) directory contains samples aligned with the previous v2 publication.

## OpenAPI material

The current OpenAPI artifact is available at [`spec/dmrv-openapi.json`](spec/dmrv-openapi.json). The previous v2 OpenAPI schema is available at [`spec/v2/openapi-schema.json`](spec/v2/openapi-schema.json).

Historical tooling may have generated these outputs from service implementations outside this repository. The repository now treats the committed OpenAPI and sample JSON files as publication artifacts that must remain parseable and linkable.

## MRV extensions

The dMRV framework includes contextual extension sets for quality standards, methodologies, registry processes, and participant-specific evidence workflows. Extension sets are documented in [`extensions/readme.md`](extensions/readme.md) and indexed in the [dMRV extension catalog](../docs/dmrv-extension-catalog.md).

## dMRV governance and assurance

dMRV artifacts should be reviewed as claim-governance infrastructure. A valid package structure only proves that the repository can parse and publish the extension set. It does not prove that the methodology is scientifically correct, accepted by a registry, or sufficient for credit issuance.

For v1.3.0, dMRV contributors should document:

| Governance area | Required documentation |
|---|---|
| Methodology authority | Methodology, quality standard, registry, or governing process that authorizes the variables and formulas. |
| Measurement boundary | Project, geography, date range, activity boundary, leakage boundary, and applicable baseline assumptions. |
| Verifier role | Verifier identity, authorization or accreditation basis, review scope, and evidence retained. |
| Claim source | Sensor, document, registry, attestation, model output, or manual source used to support the claim. |
| Double-counting control | Registry dependency, unique claim identifier, retirement or cancellation mechanism, and conflict check. |
| Revocation or correction | Conditions under which a claim, credit, variable, or extension set can be corrected, suspended, revoked, or superseded. |
| Audit trail | Validation output, source evidence references, methodology version, verifier decision, and lifecycle event receipts. |

Extension sets intended for production or registry-linked workflows should target the Silver or Gold assurance profile in [the conformance and evidence guide](../docs/conformance-and-evidence.md).

## Validation

Run repository validation from the repository root:

```bash
python scripts/validate_json.py
python scripts/validate_json.py --schema-policy
python scripts/check_internal_links.py
python scripts/check_artifact_structure.py
python scripts/build_artifact_index.py --check
```

See the [validation guide](../docs/validation.md) and [conformance/evidence guide](../docs/conformance-and-evidence.md) for the governance model behind these checks.
