# Lockdown Command Facts

| Item | Value |
|---|---|
| Command | Lockdown |
| Opcode | `24h` |
| Source | NVMe Base Spec 2.0 section 5.19, Figures 291-293 |
| Command set | Admin |
| Data transfer | No data transfer |
| NSID usage | No |
| Completion queue | Admin Completion Queue |

## Core Behavior

Lockdown prohibits or allows execution of a command opcode or Set Features Feature Identifier based on command fields.

The command uses `CDW10` and `CDW14`. All other command-specific fields are reserved.
