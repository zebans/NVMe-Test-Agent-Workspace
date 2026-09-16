# Virtualization Management Command Facts

| Item | Value |
|---|---|
| Command | Virtualization Management |
| Opcode | `1Ch` |
| Source | NVMe Base Spec 2.0 section 5.28, Figures 371-374 |
| Command set | Admin |
| Data transfer | No data transfer |
| NSID usage | No |
| Completion queue | Admin Completion Queue |

## Core Behavior

Virtualization Management modifies controller resources for primary and secondary controllers. It uses `CDW10` and `CDW11`; all other command-specific fields are reserved.

The resource type selects VQ or VI resources. The action selects primary flexible allocation or secondary controller offline/assign/online behavior.
