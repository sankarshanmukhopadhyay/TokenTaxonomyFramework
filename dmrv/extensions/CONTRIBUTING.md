# Contributing dMRV Extension Sets

This guide supplements the repository-level [contribution guide](../../CONTRIBUTING.md).

## Minimum package checklist

- [ ] `DeploymentPackage/ExtensionSet.json`
- [ ] `DeploymentPackage/EntityExtensionTemplates.json`
- [ ] `DeploymentPackage/FormulaTemplates.json`
- [ ] `DeploymentPackage/MessagePairs.json`
- [ ] `DeploymentPackage/VariableTemplates.json`
- [ ] `DeploymentPackage/protos/`, if custom proto messages are required
- [ ] `InstancePackage/AimFixedVariables.json`
- [ ] `InstancePackage/ClaimSources.json`
- [ ] `GettingStarted.md` or `README.md`
- [ ] Known limitations and review assumptions documented
- [ ] Validation scripts pass

## Review boundary

Maintainers can review repository structure, JSON parseability, documentation, and package completeness. Contributors are responsible for the correctness of methodology interpretation, registry alignment, scientific assumptions, and participant-specific governance decisions.
