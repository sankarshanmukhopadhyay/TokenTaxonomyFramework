# MRV Extension Sets

Version 3.0 introduces MRV Extension Sets: grouped templates for entities, messages, formulas, and variables that are specific to the quality standard, methodology, registry process, or Activity Impact Module being used in a dMRV workflow.

Extension sets are reusable governance artifacts. They translate methodology-specific evidence requirements into a package that can be deployed, instantiated, reviewed, and validated by ecosystem participants.

## Why extension sets matter

Issuing registries govern methodologies that describe how projects produce evidence and how claims become creditable outcomes. Those methodologies often contain variables, formulas, parameters, message exchanges, and validation conditions that are not part of the base dMRV schema.

An extension set provides a machine-readable way to register those methodology-specific requirements while preserving a common dMRV process model.

## Package structure

Each extension set should use this structure:

```text
ExtensionName/
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
  GettingStarted.md or README.md
```

### Deployment package

The deployment package registers reusable templates:

- **Entity Extension Templates** describe additional data required for entities such as Activity Impact Modules.
- **Formula Templates** capture methodology formulas, documentation, and expected syntax.
- **Variable Templates** define parameters used by formulas and monitoring workflows.
- **Message Pairs** describe request/response patterns for custom workflows.
- **Extension Set metadata** groups templates into deployable modules.

### Instance package

The instance package shows how deployed templates are used in a concrete process:

- **Claim Sources** identify evidence inputs.
- **AIM Fixed Variables** bind fixed values for a specific Activity Impact Module or deployment scenario.

## Contribution expectations

An extension-set pull request should include:

- deployment and instance packages;
- sample data or validation notes;
- known limitations;
- methodology or registry assumptions;
- validation evidence from the repository scripts.

The repository checks parseability and package completeness. It does not certify the legal, scientific, economic, or registry correctness of the submitted methodology content.

## Current extension sets

- [`sample/`](sample/GettingStarted.md): sample Verra VM0049 CCS+ extension-set material.
- [`VRE-PARFE-HydroRE/`](VRE-PARFE-HydroRE/GettingStarted.md): VRE-PARFE HydroRE extension-set material.

The generated [dMRV extension catalog](../../docs/dmrv-extension-catalog.md) indexes deployment and instance package contents.

## Validation

Run the validation suite before contributing:

```bash
python scripts/validate_json.py
python scripts/check_internal_links.py
python scripts/check_artifact_structure.py
python scripts/build_artifact_index.py --check
```

See [`../../CONTRIBUTING.md`](../../CONTRIBUTING.md) for repository-level contribution requirements.
