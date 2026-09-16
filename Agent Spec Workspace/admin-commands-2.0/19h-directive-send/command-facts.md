# Directive Send Command Facts

| Item | Value |
|---|---|
| Command | Directive Send |
| Opcode | `19h` |
| Source | NVMe Base Spec 2.0 section 5.11, Figures 178-180 |
| Command set | Admin |
| Data transfer | `01b`, host to controller |
| Completion queue | Admin Completion Queue |
| NSID usage | Conditional; `FFFFFFFFh` support depends on Directive Operation |

## Core Behavior

Directive Send transfers a data buffer to the controller. The buffer content and behavior depend on Directive Type and Directive Operation.

The command uses `DPTR`, `CDW10`, and `CDW11`. `CDW12` and `CDW13` may be used depending on Directive Type and Directive Operation. Other command-specific fields are reserved.
