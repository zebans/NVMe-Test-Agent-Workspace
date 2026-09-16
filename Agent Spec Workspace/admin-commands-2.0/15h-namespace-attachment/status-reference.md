# Namespace Attachment Status Reference

## Command-Specific Status Values

| SCT | SC | Status | Typical condition |
|---:|---:|---|---|
| `1h` | `18h` | Namespace Already Attached | Attach requested for a controller already attached. |
| `1h` | `19h` | Namespace Is Private | Private namespace is already attached to one controller. |
| `1h` | `1Ah` | Namespace Not Attached | Detach requested for a controller not attached. |
| `1h` | `1Ch` | Controller List Invalid | Controller List is invalid or includes an Admin controller. |
| `1h` | `25h` | ANA Attach Failed | ANA condition prevented attach. |
| `1h` | `27h` | Namespace Attachment Limit Exceeded | `MAXDNA` or `MAXCNA` limit exceeded. |
| `1h` | `29h` | I/O Command Set Not Supported | Target controller does not support the namespace command set. |
| `1h` | `2Ah` | I/O Command Set Not Enabled | Command set is restricted by the I/O Command Set Profile feature. |

## Other Relevant Status

| Status | Typical condition |
|---|---|
| Invalid Field in Command | Reserved `SEL`, reserved command field usage, malformed command. |
| Invalid Namespace or Format | Namespace identifier does not identify a usable namespace for the operation. |

## First-Failure Rule

If a Controller List entry fails, the command reports the byte offset of that first failing entry in the Error Information Log Entry and does not process later entries.
