# MiCA Crosswalk

The EU Markets in Crypto-Assets Regulation distinguishes asset-referenced tokens, e-money tokens, and other crypto-assets. TTF is not a MiCA compliance framework, but its artifacts can capture the design evidence needed by projects that must classify or explain a token.

| MiCA-oriented question | TTF artifact evidence |
|---|---|
| Is the token asset-referenced, e-money-like, or another crypto-asset? | Record a non-binding classification note under `governanceMetadata.regulatoryMappings`. |
| Who is the issuer or offeror? | Record issuer authority and organizational identifier under `governanceMetadata.authority`. |
| What rights does the holder receive? | Record legal claim, economic rights, redemption rights, and dispute forum under `rightsModel`. |
| What disclosures and risk factors exist? | Link disclosure or white-paper references under `evidence.requiredEvidence`. |
| What reserve, liquidity, or redemption model applies? | Record reserve model and redemption rights where applicable. |
| What happens if the token is suspended or withdrawn? | Use lifecycle state, revocation reference, migration notes, and affected controls. |

## Boundary

This crosswalk supports design traceability. It does not determine legal classification, authorization status, or regulatory approval.
