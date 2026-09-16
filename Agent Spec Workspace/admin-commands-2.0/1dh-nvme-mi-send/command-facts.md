# NVMe-MI Send Command Facts

| Item | Value |
|---|---|
| Command | NVMe-MI Send |
| Opcode | `1Dh` |
| Source | NVMe Base Spec 2.0 section 5.21 |
| Command set | Admin |
| Data transfer | `01b`, host to controller |
| NSID usage | No |
| Detailed definition | NVM Express Management Interface Specification |

## Core Behavior

Base Spec 2.0 refers NVMe-MI Send details to the NVM Express Management Interface Specification. The Base layer identifies the opcode and data direction; it does not define the NVMe-MI payload here.
