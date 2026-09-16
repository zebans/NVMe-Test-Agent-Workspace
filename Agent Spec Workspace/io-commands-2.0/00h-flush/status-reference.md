# Flush Status Reference

| Status | When it applies | Test/FW interpretation |
|---|---|---|
| `Invalid Namespace or Format` | `VWC[2:1]=10b` and `NSID=FFFFFFFFh`. | Controller does not support all-namespace Flush with that `VWC` setting. |
| Common I/O command status | Other failures. | Section 7.1 does not define another Flush-specific status. |

