# dMRV Extension Set Example

A dMRV extension set should be contributed as a directory under `dmrv/extensions/` with two package areas:

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
GettingStarted.md
```

The deployment package registers reusable methodology-specific templates. The instance package shows how those templates are bound for a concrete use case. The getting-started document explains assumptions, limitations, and validation steps.
