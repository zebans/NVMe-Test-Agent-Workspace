# Get LBA Status Command Facts

| Item | Value |
|---|---|
| Command | Get LBA Status |
| Opcode | `86h` |
| Source | NVMe Base Spec 2.0 Figure 138 / Identify Controller capability notes |
| Command set | Admin opcode; NVM/ZNS command-set-specific semantics |
| Data transfer | `10b`, controller to host |
| NSID usage | Used; `FFFFFFFFh` not supported by Figure 138 note 4 |
| Detailed definition | Applicable NVM or ZNS Command Set specification |

## Core Behavior

Base Spec 2.0 identifies Get LBA Status as an Admin opcode and command-set-specific command. It does not expand the command fields in the Base Admin command sections.

Use the applicable NVM or ZNS Command Set specification for command-specific fields, payload, and status behavior.
