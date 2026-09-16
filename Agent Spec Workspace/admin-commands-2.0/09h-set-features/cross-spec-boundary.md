# Set Features Cross-Spec Boundary

Source: NVMe Base Specification 2.0, section 5.27.

## Base-Owned

| Area | Base ownership |
|---|---|
| Command opcode and dwords | `09h`, DPTR, CDW10, CDW14, feature-specific CDW11/CDW12/CDW13/CDW15. |
| Base feature selector table | Figure 316. |
| Base feature fields | Section 5.27.1 Base-defined Feature Identifiers. |
| Set Features command-specific status values | Figure 370 and global command-specific status table. |

## External Or Shared Ownership

| Area | Boundary |
|---|---|
| I/O Command Set specific feature (`20h`) | Payload and semantics belong to the applicable I/O Command Set spec. |
| I/O Command Set specific fields | Examples include LBA Format Extension Enable and command-set range overlap behavior. |
| Vendor specific features (`C0h`-`FFh`) | Vendor-owned payload and UUID selection behavior. |
| Security / TCG / MI interactions | Only referenced when a feature explicitly points to another spec. |
| API usage | PyNVMe call syntax belongs to API layer documentation, not this spec folder. |
