# Lockdown Restrictions

| Restriction | Meaning | Violation / outcome |
|---|---|---|
| Target must be prohibitable | Not all commands/features support Lockdown prohibition. | `Prohibition of Command Execution Not Supported`. |
| Management Endpoint must exist for OOB interface choices | `IFC=01b` or `10b` requires Management Endpoint presence. | `Invalid Field in Command`. |
| PCIe Command Set scope cannot apply to Admin SQ interfaces | `SCP=4h` is invalid with `IFC=00b` or `01b`. | `Invalid Field in Command`. |
| UUID Index only applies in a narrow feature case | Requires Lockdown UUID support, Set Features UUID support, `SCP=2h`, and vendor specific Feature Identifier support. | Otherwise ignored / not specified by `CDW14`. |

