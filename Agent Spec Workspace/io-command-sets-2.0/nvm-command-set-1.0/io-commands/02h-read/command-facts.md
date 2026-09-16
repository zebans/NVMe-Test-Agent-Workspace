# NVM Read Command Facts

| Item | Value |
|---|---|
| Command | Read |
| Opcode | `02h` |
| Source | NVM Command Set 1.0 section 3.2.4, Figures 44-52 |
| Data direction | Controller to host |
| Queue | I/O Submission Queue / I/O Completion Queue |
| NSID | Uses Namespace Identifier |
| Payload | User data buffer and optional metadata / protection information |

Read transfers data and metadata, if applicable, from the controller to the host for the LBA range selected by `SLBA` and `NLB`.
