# Flush Restrictions

| Restriction | Meaning | Violation / outcome |
|---|---|---|
| Command-specific fields are reserved | Flush uses `NSID` and common command fields only. | Reserved-field validation applies. |
| `NSID=FFFFFFFFh` depends on `VWC[2:1]` | All-namespace Flush is not always supported. | `Invalid Namespace or Format` for `VWC[2:1]=10b`. |
| Flush only orders prior completed commands for selected namespace(s) | Applies to commands completed before Flush submission. | Do not infer later command ordering. |

