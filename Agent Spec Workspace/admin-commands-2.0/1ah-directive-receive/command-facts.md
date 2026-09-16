# Directive Receive Command Facts

| Item | Value |
|---|---|
| Command | Directive Receive |
| Opcode | `1Ah` |
| Source | NVMe Base Spec 2.0 section 5.10, Figures 174-177 |
| Command set | Admin |
| Data transfer | `10b`, controller to host |
| Completion queue | Admin Completion Queue |
| NSID usage | Conditional; `FFFFFFFFh` support depends on Directive Operation |

## Core Behavior

Directive Receive returns a data buffer whose content depends on Directive Type and Directive Operation.

The command uses `DPTR`, `CDW10`, and `CDW11`. `CDW12` and `CDW13` may be used depending on Directive Type and Directive Operation. Other command-specific fields are reserved.
