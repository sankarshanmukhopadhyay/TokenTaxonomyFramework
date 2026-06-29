# BIS Tokenized Money and Unified-Ledger Crosswalk

BIS work on tokenized money and unified ledgers highlights the importance of settlement assets, central bank money, tokenized deposits, tokenized assets, and programmable platforms. TTF can describe these instruments without assuming a specific ledger design.

| BIS design concern | TTF mapping |
|---|---|
| Settlement asset quality | Record issuer type, liability model, backing asset, and settlement finality. |
| Tokenized deposits | Distinguish bank liability tokens from non-bank stable-value tokens. |
| Programmability | Model controls as behaviors and control messages rather than informal feature claims. |
| Atomic settlement | Describe lifecycle event pairs and evidence receipts for delivery-versus-payment or payment-versus-payment flows. |
| Interoperability across ledgers | Record identifier scheme, network or platform, bridge assumptions, and operational limits. |

## Recommended Metadata

Stable-value, tokenized-deposit, and settlement-asset artifacts should include `rightsModel.redemptionRights`, `settlement.finalityPoint`, `evidence.requiredEvidence`, and `transferControls.policyReference` where applicable.
