# Fabrics Commands Admin Opcode Facts

| Item | Value |
|---|---|
| Admin opcode | `7Fh` |
| Meaning | Fabrics Commands |
| Source | NVMe Base Spec 2.0 Figure 138 and section 6 |
| Data transfer | Fabrics command-specific |
| NSID usage | Fabrics command-specific |
| Detailed folder | `fabrics-base-2.0/commands` |

## Core Behavior

All Fabrics commands use Admin opcode `7Fh`. The individual Fabrics command is selected by Fabrics command capsule fields, not by this Admin opcode folder alone.
