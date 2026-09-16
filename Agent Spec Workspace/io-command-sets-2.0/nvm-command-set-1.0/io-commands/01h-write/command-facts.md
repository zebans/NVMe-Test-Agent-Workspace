# NVM Write Command Facts

| Item | Value |
|---|---|
| Command | Write |
| Opcode | `01h` |
| Source | NVM Command Set 1.0 section 3.2.6, Figures 59-67 |
| Data direction | Host to controller |
| Queue | I/O Submission Queue / I/O Completion Queue |
| NSID | Uses Namespace Identifier |
| Payload | User data buffer and optional metadata / protection information |

Write writes data and metadata, if applicable, to the I/O controller for the logical blocks indicated by `SLBA` and `NLB`.
