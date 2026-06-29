# Token Taxonomy Framework Documentation

This documentation layer makes the repository easier to adopt, validate, and publish through GitHub Pages. It does not replace the framework specifications; it provides navigation, evidence expectations, and machine-verifiable maintenance guidance.

## Start here

| Document | Purpose |
|---|---|
| [Artifact catalog](artifact-catalog.md) | Generated index of taxonomy JSON and proto artifacts. |
| [Token template catalog](token-template-catalog.md) | Generated index of token-template-oriented artifacts. |
| [dMRV extension catalog](dmrv-extension-catalog.md) | Generated index of dMRV deployment and instance packages. |
| [Validation guide](validation.md) | How to run local and CI checks. |
| [Conformance and evidence guide](conformance-and-evidence.md) | What evidence should exist for valid artifacts and extension sets. |
| [Tokenization landscape](tokenization-landscape.md) | Current tokenization classes, design pressure, and v1.3.0 metadata expectations. |
| [Crosswalks](crosswalks/README.md) | Mapping guides for identifiers, regulatory categories, permissioned controls, lifecycle events, and organizational identity. |

## Adoption path

1. Read the [taxonomy overview](../token-taxonomy.md) to understand the framework vocabulary.
2. Review the [taxonomy artifact format](../taxonomy-artifact-format.md) to understand repository artifact conventions.
3. Inspect the [artifact catalog](artifact-catalog.md) and select reusable components.
4. Run the validation scripts before modifying JSON, proto, or Markdown files.
5. For dMRV work, use the [dMRV workspace](../dmrv/readme.md) and [dMRV extension catalog](dmrv-extension-catalog.md).
6. For regulated, financial, identity-bound, or evidence-heavy token designs, review the [tokenization landscape](tokenization-landscape.md) and relevant [crosswalks](crosswalks/README.md).
