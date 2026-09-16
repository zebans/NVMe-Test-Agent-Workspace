# Capacity Management Command Facts

| Item | Value |
|---|---|
| Command | Capacity Management |
| Opcode | `20h` |
| Source | NVMe Base Spec 2.0 section 5.3, Figures 149-151 |
| Command set | Admin |
| Data transfer | No data transfer |
| NSID usage | No |
| Completion queue | Admin Completion Queue |

## Core Behavior

Capacity Management configures Endurance Groups and NVM Sets by selecting a supported capacity configuration, creating/deleting an Endurance Group, or creating/deleting an NVM Set.

The command uses `CDW10`, `CDW11`, and `CDW12`. All other command-specific fields are reserved.
