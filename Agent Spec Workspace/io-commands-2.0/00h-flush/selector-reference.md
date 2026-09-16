# Flush Selector Reference

| Selector | Location | Meaning |
|---|---|---|
| Namespace Identifier | `NSID` | Selects namespace scope for Flush. |
| Volatile Write Cache all-namespace support | Identify Controller `VWC` bits 2:1 | Defines Flush behavior for `NSID=FFFFFFFFh`. |

## `NSID=FFFFFFFFh` Behavior

| `VWC[2:1]` | Behavior |
|---|---|
| `11b` | Flush applies to all namespaces attached to the controller processing the command. |
| `10b` | Controller aborts with `Invalid Namespace or Format`. |
| `00b` | Behavior is not indicated; Base 1.4+ compliant controllers shall not set this value. |

