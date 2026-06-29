# Regulated Tokenization Examples

These examples show how v1.3.0 governance metadata can be used for regulated, identity-bound, financial, dMRV, and document/title-oriented token designs. They are illustrative examples, not approved legal instruments, regulatory classifications, registry records, or production token specifications.

| Example | Purpose | Suggested assurance profile |
|---|---|---|
| [`permissioned-rwa-token.json`](permissioned-rwa-token.json) | Models a permissioned real-world asset token with eligibility-gated transfer. | Silver |
| [`tokenized-bond.json`](tokenized-bond.json) | Models a tokenized bond/security pattern with legal-instrument and lifecycle evidence. | Gold |
| [`stable-value-token.json`](stable-value-token.json) | Models a stable-value token where redemption, reserve, and issuer metadata matter. | Silver |
| [`dmrv-claim-token.json`](dmrv-claim-token.json) | Models an ecological claim token with methodology, verifier, registry, and revocation evidence. | Gold |
| [`verifiable-document-title-token.json`](verifiable-document-title-token.json) | Models a document or title token with issuing authority and revocation route. | Silver |

## Review Posture

Each example asks reviewers to separate:

- token composition from legal validity;
- transfer capability from eligibility to transfer;
- external identifier reference from identifier assignment;
- package completeness from business, legal, scientific, or registry correctness;
- narrative documentation from machine-verifiable evidence.

Run the repository validation suite from the repository root after editing these examples:

```bash
python scripts/validate_json.py
python scripts/validate_json.py --schema-policy
python scripts/check_internal_links.py
python scripts/check_artifact_structure.py
python scripts/build_artifact_index.py --check
```
