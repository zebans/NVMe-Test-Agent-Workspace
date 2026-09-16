# Security Receive Command Facts

| Item | Value |
|---|---|
| Command | Security Receive |
| Opcode | `82h` |
| Source | NVMe Base Spec 2.0 section 5.25, Figures 306-309 |
| Command set | Admin |
| Data transfer | `10b`, controller to host |
| Completion queue | Admin Completion Queue |
| NSID usage | Security Protocol specific |

## Core Behavior

Security Receive transfers status and data results of one or more previously submitted Security Send commands from controller to host. The association with previous Security Send commands and the returned data format are Security Protocol dependent and defined in SPC-5.

Security Receive data may not be retained if communication is lost between controller and host, or if a Controller Level Reset occurs.
