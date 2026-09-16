# Lockdown Status Reference

| Status | When it applies | Test/FW interpretation |
|---|---|---|
| `Prohibition of Command Execution Not Supported` | Specified opcode or Feature Identifier does not support being prohibited by Lockdown. | Target is not prohibitable. |
| `Invalid Field in Command` | `IFC=01b` or `10b` but subsystem has no Management Endpoint; or `IFC=00b/01b` with `SCP=4h`. | Field combination is illegal. |

