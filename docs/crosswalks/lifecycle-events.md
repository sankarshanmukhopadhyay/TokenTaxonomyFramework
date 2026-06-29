# Lifecycle and CDM-Inspired Events

Financial and institutional token systems need auditable lifecycle events. The ISDA Common Domain Model demonstrates the value of standardized lifecycle data and process representation. TTF can adopt that discipline without becoming a trade-processing model.

| Lifecycle event | Evidence to retain |
|---|---|
| Define template | Artifact identifier, authority, version, formula, and validation result. |
| Issue or mint | Issuer authority, quantity, holder or account, timestamp, and policy context. |
| Transfer | Sender, recipient, eligibility result, policy decision, quantity, finality point. |
| Encumber | Secured party, obligation reference, collateral state, release conditions. |
| Redeem | Holder, redemption right, asset or cash settlement reference, finality evidence. |
| Burn or retire | Actor, reason, quantity, registry or claim linkage, irreversibility evidence. |
| Pause or suspend | Authorized actor, policy basis, affected scope, reinstatement condition. |
| Revoke or withdraw | Authority, reason, affected artifact or token class, migration or dispute route. |
| Supersede | Prior artifact, successor artifact, compatibility statement, migration notes. |

## Review Rule

If a lifecycle event changes ownership, rights, eligibility, claim status, or supply, it should produce evidence that can be validated independently of the prose description.
