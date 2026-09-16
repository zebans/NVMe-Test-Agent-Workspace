# Vendor Specific Admin Commands Facts

| Item | Value |
|---|---|
| Opcode range | `C0h`-`FFh` |
| Command type | Vendor-specific Admin commands |
| Source | NVMe Base Spec 2.0 Figure 138 |
| Command set | Admin |
| Data transfer | Vendor-specific / encoded by opcode bits and vendor definition |
| Detailed definition | Vendor-specific documentation |

## Core Behavior

Base Spec 2.0 identifies `C0h`-`FFh` as the vendor-specific Admin command range. It does not define command semantics for this range.
