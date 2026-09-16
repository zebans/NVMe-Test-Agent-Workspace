# Device Self-test Status Reference

| Status | When it applies | Test/FW interpretation |
|---|---|---|
| `Device Self-test in Progress` | A short or extended self-test is requested while a self-test is already in progress. | New self-test command is rejected because operation already exists. |
| `Invalid Namespace or Format` | `NSID` specifies an invalid namespace ID. | Namespace selector is not valid. |
| `Invalid Field in Command` | `NSID` specifies an inactive namespace ID. | Namespace exists as a value but is inactive for this command. |

## Scope Note

Whether "self-test in progress" is evaluated per-controller or per-NVM-subsystem depends on Identify Controller `DSTO` bit 0.

