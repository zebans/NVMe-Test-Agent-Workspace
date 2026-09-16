# Security Send Command Facts

| Item | Value |
|---|---|
| Command | Security Send |
| Opcode | `81h` |
| Source | NVMe Base Spec 2.0 section 5.26, Figures 310-312 |
| Command set | Admin |
| Data transfer | `01b`, host to controller |
| Completion queue | Admin Completion Queue |
| NSID usage | Security Protocol specific |

## Core Behavior

Security Send transfers security protocol data to the controller. The transferred data contains security protocol specific commands and may contain data or parameters associated with those commands.

Status and data to be returned for security protocol commands submitted by Security Send are retrieved with Security Receive. The association between Send and Receive is Security Protocol dependent as defined in SPC-5.
