# Vendor Specific I/O Commands Facts

| Item | Value |
|---|---|
| Opcode range | `80h`-`FFh` |
| Command type | Vendor-specific I/O commands |
| Source | NVMe Base Spec 2.0 Figure 390 |
| Submission queue | I/O Submission Queue |
| NSID usage | Used |
| Data transfer | Vendor-specific / encoded by opcode bits and vendor definition |
| Detailed definition | Vendor-specific documentation |

## Core Behavior

Base Spec 2.0 identifies `80h`-`FFh` as the vendor-specific I/O command range. It does not define command semantics for this range.
