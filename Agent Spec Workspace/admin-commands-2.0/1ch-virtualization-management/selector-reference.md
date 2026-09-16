# Virtualization Management Selector Reference

| Selector | Location | Meaning |
|---|---|---|
| Controller Identifier | `CDW10.CNTLID` bits 31:16 | Controller whose resources are modified. |
| Resource Type | `CDW10.RT` bits 10:08 | Type of controller resource. |
| Action | `CDW10.ACT` bits 03:00 | Operation to perform. |
| Number of Controller Resources | `CDW11.NR` bits 15:00 | Number of resources to allocate or assign. |

## Resource Type Values

| `RT` | Meaning |
|---|---|
| `000b` | VQ Resources. |
| `001b` | VI Resources. |
| `010b`-`111b` | Reserved. |

## Action Values

| `ACT` | Meaning |
|---|---|
| `0h` | Reserved. |
| `1h` | Primary Controller Flexible Allocation. |
| `2h`-`6h` | Reserved. |
| `7h` | Secondary Controller Offline. |
| `8h` | Secondary Controller Assign. |
| `9h` | Secondary Controller Online. |
| `Ah`-`Fh` | Reserved. |

