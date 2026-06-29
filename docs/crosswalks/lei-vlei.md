# LEI and vLEI Organizational Identity Crosswalk

Legal Entity Identifiers and verifiable LEIs provide organizational identity anchors for issuers, custodians, verifiers, registries, and authorized representatives. TTF artifacts should be able to record these anchors where available.

| Actor | Recommended artifact metadata |
|---|---|
| Issuer | `authority.identifierScheme`, `authority.identifier`, and issuance scope. |
| Custodian | Custody model, custodian identifier, asset safeguarding evidence. |
| Verifier | Verifier identifier, accreditation or authorization scope, verification evidence. |
| Registry | Registry identifier, registry record URL, revocation or status endpoint. |
| Smart-contract operator | Operator identity, authority to upgrade, pause, revoke, or recover. |
| Authorized representative | Role credential or delegation reference where the acting person signs for an organization. |

## Boundary

LEI and vLEI references improve verifiability of organizational roles. They do not by themselves prove that a token is legally valid, properly backed, or regulator-approved.
