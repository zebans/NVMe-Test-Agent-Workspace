# Flush Command Facts

| Item | Value |
|---|---|
| Command | Flush |
| Opcode | `00h` |
| Source | NVMe Base Spec 2.0 section 7.1 |
| Command set | I/O |
| Data transfer | No data transfer |
| NSID usage | Yes |
| Completion queue | Associated I/O Completion Queue |

## Core Behavior

Flush requests that volatile write cache contents be made non-volatile.

If volatile write cache is enabled, Flush shall commit data and metadata associated with the specified namespace(s) to non-volatile media. It applies to commands for the specified namespace(s) completed by the controller before Flush submission.

The controller may also flush additional data and/or metadata from any namespace.
