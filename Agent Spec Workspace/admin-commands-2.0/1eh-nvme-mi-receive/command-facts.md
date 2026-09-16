# NVMe-MI Receive Command Facts

| Item | Value |
|---|---|
| Command | NVMe-MI Receive |
| Opcode | `1Eh` |
| Source | NVMe Base Spec 2.0 section 5.20 |
| Command set | Admin |
| Data transfer | `10b`, controller to host |
| NSID usage | No |
| Detailed definition | NVM Express Management Interface Specification |

## Core Behavior

Base Spec 2.0 refers NVMe-MI Receive details to the NVM Express Management Interface Specification. The Base layer identifies the opcode and data direction; it does not define the NVMe-MI payload here.
