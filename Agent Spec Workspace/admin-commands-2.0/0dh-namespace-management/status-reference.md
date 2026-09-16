# Namespace Management Status Reference

## Command-Specific Status Values

| SCT | SC | Status | Typical condition |
|---:|---:|---|---|
| `1h` | `0Ah` | Invalid Format | Invalid user data format, unsupported PI/metadata resources, unavailable format, or invalid security state. |
| `1h` | `15h` | Namespace Insufficient Capacity | Create requires more unallocated capacity than available. |
| `1h` | `16h` | Namespace Identifier Unavailable | Namespace count or identifier availability limit exceeded. |
| `1h` | `1Bh` | Thin Provisioning Not Supported | Requested thin provisioning is unsupported. |
| `1h` | `24h` | ANA Group Identifier Invalid | `ANAGRPID` is invalid or unsupported. |
| `1h` | `29h` | I/O Command Set Not Supported | Requested `CSI` is not supported by the controller. |
| `1h` | `2Ch` | Invalid I/O Command Set | Requested I/O command-set association is invalid for the create operation. |

## Other Relevant Status

| Status | Typical condition |
|---|---|
| Namespace is Write Protected | Operation prohibited by namespace write protection. |
| Invalid Field in Command | Reserved `SEL`, reserved fields, malformed command field usage. |

## Testing Note

Namespace Management failures often depend on Identify Controller capacity/capability fields and command-set support. A test should read the capability source before expecting a specific create failure.
