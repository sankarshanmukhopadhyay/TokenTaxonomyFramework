# ISO Digital Token Identifier Crosswalk

ISO 24165 defines the Digital Token Identifier registration and data-element model. TTF should not duplicate the ISO registry. Instead, artifacts should be able to reference a DTI or another identifier scheme when an external identifier exists.

| ISO DTI concern | TTF v1.3.0 mapping |
|---|---|
| Identifier assignment | `governanceMetadata.identifiers[]` should record scheme, value, assigning authority, and registry URL where available. |
| Token-to-identifier relationship | The artifact should state whether the identifier refers to the token class, token template, deployed implementation, or issuer-specific instrument. |
| Registry data elements | The artifact should avoid inventing conflicting semantics and should link to the registry record when public. |
| Version and lifecycle | Identifier changes, deprecations, and supersessions should be reflected in `governanceMetadata.lifecycle`. |

## Implementation Guidance

Use ISO DTI metadata only when the token or instrument has an assigned identifier. For draft templates, examples, and pre-registration designs, record `identifierScheme` as `none` or leave the identifier unset. Do not imply DTI registration through naming alone.
